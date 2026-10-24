# FIRST CODEX TASK - BOLTBOTS MAC BOOTSTRAP AND FIRST PLAYABLE TEST

You are the local lead engineering agent for **BoltBots Tycoon** on the owner's Mac.
Read `AGENTS.md`, `README.md`, `docs/BOOTSTRAP_MACOS.md`, `docs/SPRINT_01.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, and `docs/VISUAL_DESIGN_BIBLE.md` before touching code.

Take initiative. Diagnose, install with narrow approval, build, run, debug, and document. Do not ask the owner to write code or edit configurations.

## Phase B0: Verify and prepare the Mac

1. Verify the shell is macOS. Run `bash scripts/doctor-macos.sh` and `bash scripts/check-sources.sh`. Record exact versions and command outputs in `docs/IMPLEMENTATION_LOG.md`.
2. If prerequisites are missing, propose each OS-level installation from verified official sources and get owner approval for the specific command. `scripts/bootstrap-macos.sh` shows the approved project flow. Do not pipe unreviewed remote scripts to shell, disable macOS security, or request passwords/MFA.
3. Install or verify Git, Rokit and pinned Rojo 7.7.1. Install/configure Roblox Studio using the official source; guide owner through the sign-in/MFA dialog one step at a time if necessary. Install compatible Rojo Studio plugin.
4. Run `bash scripts/build.sh`; investigate and fix Rojo mapping, Luau syntax and source errors. Run `bash scripts/studio-smoke.sh` for the static engine-side smoke as available. Never treat a static RunScript smoke as a Play-mode proof.
5. Initialize a local Git repository and commit baseline changes. Do not create an external GitHub remote without separate authorization.

## Phase M1: Verify actual gameplay already included in source

6. The repository includes **prototype source, not a verified game**: `src/ServerScriptService/Main.server.luau`, `Services/WorldBuilder.luau`, `ReplicatedStorage/Shared/EconomyRules.luau`, `Client.client.luau`.
7. Open the built `.rbxlx` in Roblox Studio and run in Play mode. Ensure the factory floor, four separated plots, first Scout robot (under 60s), coin award and assembler upgrade work. Fix any Luau runtime issues, collisions, UI readability or camera/spawn problems you observe. Record an actual video or screenshot; never fabricate one.
8. Validate the server-authoritative upgrade protocol: disallow arbitrary client amounts, other-player plots and repeated requests; test at least 2 Studio clients. Roblox ProximityPrompt triggers require additional server ownership/distance checks.
9. Validate mobile emulator HUD and desktop. Measure real time-to-first-robot, first-upgrade flow and any crashes, rather than asserting targets automatically passed.
10. Run `scripts/check-sources.sh`, `scripts/build.sh` and Studio smoke again after fixes. Create a succinct status matrix for `docs/SPRINT_01.md` and update `docs/IMPLEMENTATION_LOG.md`.

## Next safe step after M1

Once M1 checks pass, propose M2 (DataStore persistence, migration tests and safe reconnect behavior) with changed files and security/rollback design. Implement routine code automatically when safe; defer account, cloud, public release, purchases, DevEx and paid advertisements for explicit approval.

## Completion format

DONE / VERIFIED WITH EVIDENCE / FAILED OR NOT RUN / OWNER ACTION NEEDED / NEXT SAFE STEP.
No public publishing, no paid spend, no broad API credentials, no production keys, no claim that a game is complete after a static build.
