# B0 — macOS Bootstrap and local agent architecture

**Goal:** Codex works against a local Git/Rojo repository and performs implementation plus repeatable build/test tasks; Roblox Studio supplies the actual engine and visual editor. Safe account and publication gates remain human-controlled.

## 1. Execution architecture

```text
Mac owner
  ├─ ChatGPT / Codex UI (product brief, approvals, PRs, evidence)
  └─ Local Codex CLI in project directory (tools + shell in approved sandbox)
        ├─ AGENTS.md + docs/ (instructions and constraints)
        ├─ Git repo (source of truth, optional GitHub private remote)
        ├─ Rokit -> pinned Rojo (toolchain)
        ├─ src/*.luau + default.project.json
        │     └─ rojo build -> build/BoltBotsTycoon.rbxlx
        ├─ Roblox Studio macOS (/Applications/RobloxStudio.app)
        │     ├─ opens generated place and runs sessions
        │     ├─ CLI RunScript smoke checks where supported
        │     └─ Studio GUI for visual/mobile/multiplayer checks
        └─ Later: Roblox Open Cloud with least-privilege credentials
              └─ private test uploads / release only with explicit approval
```

**No cloud dependencies for the first playable prototype.** Never pretend local Codex can log in to Roblox, bypass 2FA, or operate dialogs if the installed client has no computer-control permission.

## 2. Mac requirements

- Confirm macOS version and architecture (`sw_vers`, `uname -m`) before doing anything. Roblox recommends macOS 14+ and 8 GB RAM; actual project ambitions benefit from additional RAM.
- Work in a non-synced local directory initially (avoid Dropbox/iCloud merge collisions).
- Internet connectivity and a personal Roblox account are required for Studio authentication. A GitHub account is optional until remote backup/CI is approved.
- The Mac owner must approve prompts for installing unsigned/untrusted-looking tools, macOS privacy/accessibility permissions, Apple developer tools and sign-ins.

## 3. First-run sequence (agent-led)

**Step B0.1 — Preflight, non-destructive**

```bash
bash scripts/doctor-macos.sh
```

Report platform, Git, xcode-select, Codex, Roblox Studio, Rokit/Rojo. If not macOS, STOP and request an environment switch rather than assuming this machine is the user's Mac.

**Step B0.2 — Start Codex**

- Preferred UI: current ChatGPT desktop app (Codex integrated) at https://chatgpt.com/download/.
- CLI: use official install guidance at https://learn.chatgpt.com/docs/codex/cli. It currently offers a macOS installer script (`https://chatgpt.com/codex/install.sh`); an npm alternative may also be available. Download-and-review before running, rather than piping uninspected scripts into shell.
- Owner authenticates interactively; agents must not ask for passwords or MFA codes.

**Step B0.3 — Install local prerequisites**

- Xcode Command Line Tools: `xcode-select --install` if `xcode-select -p` fails; a macOS dialog can need owner confirmation.
- Git: normally provided via Command Line Tools; confirm `git --version`.
- Rokit: official repository https://github.com/rojo-rbx/rokit. Agent downloads installation script, inspects it, requests permission, then runs it.
- Project version pin: `rokit.toml` declares `rojo-rbx/rojo@7.7.1`. Run `rokit install`. Confirm `rojo --version`.
- Optional GitHub CLI is not required for B0; if remote repo needed, install and authorize `gh` with owner's agreement.

**Step B0.4 — Roblox Studio**

- Official macOS Studio download: https://create.roblox.com/docs/studio/setup.
- Install `RobloxStudio.dmg` and launch Roblox Studio. Agent can assist with opening pages and local file operations; browser sign-in, MFA and system privacy permissions remain owner-controlled.
- Confirm executable exists at `/Applications/RobloxStudio.app/Contents/MacOS/RobloxStudio` (actual path may vary by user installation).
- Install the Rojo Studio plugin with `rojo plugin install` (when supported); verify plugin activation inside Roblox Studio and connect it to `rojo serve` if sync is needed.
- Git repository -> Rojo build remains fallback even if live sync cannot be established.

**Step B0.5 — Build and smoke-check**

```bash
bash scripts/build.sh
bash scripts/studio-smoke.sh
```

The generated `.rbxlx` is a **stub place** to validate integration, not the game. The Studio CLI supports `--task RunScript`, `--localPlaceFile`, `--runScriptFile`, `--outputFile`, `--quitAfterExecution`. It may start a GUI window and require a logged-in, permitted Studio instance. Record failures instead of forcing unsafe workarounds.

**Step B0.6 — Git and evidence**

Initialize a local Git repository if needed; make a baseline commit after inspection. A private GitHub remote is optional and requires owner approval. Record environment versions, build outputs and smoke results in the implementation log.

## 4. Interactive bootstrap helper

Run `bash scripts/bootstrap-macos.sh` to view pending work without making changes. Run `bash scripts/bootstrap-macos.sh --apply` only after reviewing actions; it asks separately before official installer execution. The helper cannot silently handle Roblox login, 2FA or App permissions.

## 5. Publisher-account readiness review (read-only initially)

The owner should choose whether the first public launch is to eligible 16+ audiences or aims to include Roblox Kids / Select. Current Roblox requirements differ materially (age checks, two-factor authentication, potential refundable fee or qualifying subscription, evaluation, content rating). See `QA_RELEASE.md` and official publishing docs. This review **does not authorize** account verification or payment without the owner.

## 6. Non-goals for B0

No automated public upload; no creation of permanent broad-scope Roblox API keys; no payment provider; no profile scraping or scraping competitor code; no bypasses for App permissions; no asset purchases.

## 7. Completion evidence and gate

- [ ] Valid macOS machine and documented version/architecture.
- [ ] `codex` starts in project directory and reads `AGENTS.md`.
- [ ] Git works; Roblox Studio opens and owner signs in.
- [ ] `rokit install` and `rojo --version` succeed.
- [ ] `bash scripts/build.sh` exits 0 and produces `.rbxlx`.
- [ ] Studio CLI smoke returns verifiable `BOLTBOTS_SMOKE_OK` or a documented B0 blocker.
- [ ] Private commit created; no credentials in repository or logs.

## 8. Official references

- Roblox Studio: https://create.roblox.com/docs/studio/setup
- Roblox Studio CLI: https://create.roblox.com/docs/studio/command-line-interface
- Filesystem synchronization: https://create.roblox.com/docs/scripting/sync
- Rokit: https://github.com/rojo-rbx/rokit
- Rojo releases: https://github.com/rojo-rbx/rojo/releases
- Codex CLI: https://learn.chatgpt.com/docs/codex/cli
- AGENTS.md: https://learn.chatgpt.com/docs/agent-configuration/agents-md
