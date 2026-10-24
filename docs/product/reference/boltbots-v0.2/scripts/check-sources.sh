#!/usr/bin/env bash
# Static configuration sanity checks; does not run Luau or Roblox Studio.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
for script in scripts/*.sh; do
  bash -n "$script"
done
python3 - <<'PY'
import json
import sys
from pathlib import Path
root = Path.cwd()
for path in sorted(root.rglob('*.json')):
    if 'build' in path.parts:
        continue
    json.loads(path.read_text(encoding='utf-8'))
try:
    import tomllib
except ImportError:
    raise SystemExit('Python 3.11+ is required for the rokit.toml check')
with (root/'rokit.toml').open('rb') as f:
    manifest = tomllib.load(f)
assert manifest['tools']['rojo'] == 'rojo-rbx/rojo@7.7.1'
project = json.loads((root/'default.project.json').read_text(encoding='utf-8'))
assert project['name'] == 'BoltBotsTycoon'
assert (root/'src/ServerScriptService/Services/WorldBuilder.luau').exists()
assert (root/'src/ReplicatedStorage/Shared/EconomyRules.luau').exists()
assert (root/'src/StarterPlayer/StarterPlayerScripts/Client.client.luau').exists()
assert (root/'docs/SPRINT_01.md').exists()
for reference in ('01_factory_world_concept.png','02_hud_concept.png','03_robot_shop_concept.png'):
    assert (root/'assets/mockups'/reference).is_file(), reference
print('PASS: Shell syntax, JSON, TOML, source tree and reference assets')
print('NOT CHECKED: Luau compilation, Rojo build, Studio runtime, multiplayer or mobile UI')
PY
