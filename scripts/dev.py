#!/usr/bin/env python3
"""Small macOS tool setup, doctor and build entry point (Python standard library)."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / ".tools"
BIN = TOOLS / "bin"
PINS = json.loads((ROOT / "toolchain.json").read_text())
RECEIPT = TOOLS / "installed.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args, **kwargs):
    return subprocess.run([str(a) for a in args], check=True, **kwargs)


def download(spec):
    cache = TOOLS / "downloads" / spec["sha256"]
    cache.parent.mkdir(parents=True, exist_ok=True)
    if not cache.exists() or sha(cache) != spec["sha256"]:
        request = urllib.request.Request(spec["url"], headers={"User-Agent": "BoltBots-setup"})
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = response.read()
        if hashlib.sha256(payload).hexdigest() != spec["sha256"]:
            raise RuntimeError("Download checksum mismatch: " + spec["url"])
        cache.write_bytes(payload)
    return cache


def setup():
    if platform.system() != "Darwin":
        raise RuntimeError("This setup is verified for macOS only; see docs/setup.md.")
    arch = platform.machine()
    if arch not in ("arm64", "x86_64"):
        raise RuntimeError("Unsupported Python process architecture: " + arch)
    BIN.mkdir(parents=True, exist_ok=True)
    binaries = {}
    for tool, names in (("rojo", ["rojo"]), ("luau", ["luau", "luau-compile", "luau-analyze"])):
        spec = PINS[tool]["macos"]
        if tool == "rojo":
            spec = spec[arch]
        archive = download(spec)
        with zipfile.ZipFile(archive) as bundle:
            for name in names:
                matches = [n for n in bundle.namelist() if Path(n).name == name]
                if len(matches) != 1:
                    raise RuntimeError("Missing/ambiguous official binary: " + name)
                target = BIN / name
                target.write_bytes(bundle.read(matches[0]))
                target.chmod(0o755)
                binaries[name] = sha(target)
    # A tiny script verifies the installed interpreter rather than relying on --version support.
    probe = TOOLS / "probe.luau"
    probe.write_text('assert(1 + 1 == 2)\nprint("Luau executable OK")\n')
    run([BIN / "rojo", "--version"])
    run([BIN / "luau", probe])
    RECEIPT.write_text(json.dumps({"toolchain_sha256": sha(ROOT / "toolchain.json"),
                                  "python_process_arch": arch, "binaries": binaries}, indent=2) + "\n")
    print("Installed pinned tools in", BIN)


def require_tools():
    if not RECEIPT.is_file():
        raise RuntimeError("Tools missing. Run: python3 scripts/dev.py setup")
    receipt = json.loads(RECEIPT.read_text())
    if receipt["toolchain_sha256"] != sha(ROOT / "toolchain.json"):
        raise RuntimeError("Tool pins changed. Run setup again.")
    for name in ("rojo", "luau", "luau-compile", "luau-analyze"):
        path = BIN / name
        if not path.is_file() or sha(path) != receipt["binaries"].get(name):
            raise RuntimeError("Installed tool changed/missing: " + name + "; run setup again.")


def doctor():
    print("OS:", platform.platform(), "| Python process architecture:", platform.machine())
    print("Python:", sys.version.split()[0], sys.executable)
    missing = []
    git = shutil.which("git")
    print("Git:", git or "MISSING")
    if git:
        run([git, "--version"])
    else:
        missing.append("Git")
    studio = next((p for p in (Path("/Applications/RobloxStudio.app"),
                               Path.home() / "Applications/RobloxStudio.app") if p.exists()), None)
    print("Studio app found:", studio or "MISSING", "(launch/login is a separate UI check)")
    if studio is None:
        missing.append("Roblox Studio")
    try:
        require_tools()
        run([BIN / "rojo", "--version"])
        run([BIN / "luau", TOOLS / "probe.luau"])
        run([BIN / "luau-compile", "--help"], stdout=subprocess.DEVNULL)
        run([BIN / "luau-analyze", "--help"], stdout=subprocess.DEVNULL)
        print("Luau release pin:", PINS["luau"]["version"], "| all binary checksums OK")
    except (RuntimeError, OSError, subprocess.CalledProcessError) as error:
        print("Tool execution: MISSING/FAILED:", error)
        missing.append("project tools")
    plugin = Path.home() / "Documents/Roblox/Plugins/RojoManagedPlugin.rbxm"
    print("Rojo plugin file:", plugin if plugin.is_file() else "NOT CONFIRMED",
          "(Studio visibility/connection checked separately)")
    if not plugin.is_file() or sha(plugin) != PINS["rojo"]["plugin"]["cli_embedded_sha256"]:
        missing.append("matching Rojo plugin")
    print("Missing/failed requirements:", ", ".join(missing) if missing else "none")
    return 1 if missing else 0


def plugin_install():
    require_tools()
    # Rojo manages this one file. Refuse to overwrite another plugin/version silently.
    plugin = Path.home() / "Documents/Roblox/Plugins/RojoManagedPlugin.rbxm"
    if plugin.exists() and sha(plugin) != PINS["rojo"]["plugin"]["cli_embedded_sha256"]:
        raise RuntimeError("A different managed Rojo plugin exists; inspect before replacing: " + str(plugin))
    run([BIN / "rojo", "plugin", "install"])
    if not plugin.is_file() or sha(plugin) != PINS["rojo"]["plugin"]["cli_embedded_sha256"]:
        raise RuntimeError("Plugin location/hash not confirmed; inspect CLI output before proceeding.")
    print("Plugin verified:", plugin, sha(plugin))


def build():
    require_tools()
    output = ROOT / "build/BoltBots.rbxlx"
    output.parent.mkdir(exist_ok=True)
    run([BIN / "rojo", "build", ROOT / "default.project.json", "--output", output], cwd=ROOT)
    print("Build SHA256:", sha(output))


def check():
    require_tools()
    files = sorted((ROOT / "src").rglob("*.luau"))
    if not files:
        raise RuntimeError("No runtime source files found")
    for path in files:
        run([BIN / "luau-compile", "--null", path], stdout=subprocess.DEVNULL)
    print("Syntax OK:", len(files), "runtime files")
    # Standalone Luau has no Roblox `script` Instance. Adapt ONLY the module import in a
    # temporary copy; all rule logic under test is the exact active source.
    shared = ROOT / "src/ReplicatedStorage/Shared"
    with tempfile.TemporaryDirectory(prefix="boltbots-rules-") as tmp:
        temp = Path(tmp)
        shutil.copy2(shared / "GameConfig.luau", temp / "GameConfig.luau")
        source = (shared / "EconomyRules.luau").read_text()
        dependency = "local Config = require(script.Parent.GameConfig)"
        if source.count(dependency) != 1:
            raise RuntimeError("Rule import changed; update the explicit CLI test adapter.")
        (temp / "EconomyRules.luau").write_text(source.replace(dependency, 'local Config = require("./GameConfig")'))
        shutil.copy2(ROOT / "tests/economy-rules.luau", temp / "economy-rules.luau")
        run([BIN / "luau-analyze", temp / "GameConfig.luau", temp / "EconomyRules.luau",
             temp / "economy-rules.luau"])
        run([BIN / "luau", temp / "economy-rules.luau"])
    print("Rule tests/type checks OK. Roblox API typing, Play and multiplayer are not covered.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["setup", "doctor", "plugin-install", "build", "check", "serve"])
    args = parser.parse_args()
    if args.command == "serve":
        require_tools()
        run([BIN / "rojo", "serve", ROOT / "default.project.json", "--address", "127.0.0.1"], cwd=ROOT)
    else:
        result = {"setup": setup, "doctor": doctor, "plugin-install": plugin_install,
                  "build": build, "check": check}[args.command]()
        return result or 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RuntimeError, OSError, ValueError, subprocess.CalledProcessError) as error:
        print("ERROR:", error, file=sys.stderr)
        sys.exit(1)
