# BoltBots Tycoon - implementation evidence log

## 2026-10-24 - Authoring environment (not owner Mac)

- Migrated prior Robot Factory Tycoon concept to provisional brand **BoltBots Tycoon**, pending trademark/name clearance.
- Added first vertical-slice source: generated factory world, four plot positions, automatically produced Scout robots, server-only cash and upgrade cost calculation, player-facing HUD.
- Added `scripts/start-codex-macos.sh`, `scripts/check-sources.sh`, Studio CLI rule assertions, and sprint-01 verification plan.
- No software installed on the owner's Mac. No sign-in or account action. No public publishing or spending.
- The source is a prototype and has not been exercised in Roblox Studio Play mode.

## Local execution to fill in by Codex

| Check | Expected evidence | State |
|---|---|---|
| Mac doctor | macOS version, CPU, installed tool versions | NOT RUN |
| Static configuration | Output of `bash scripts/check-sources.sh` | NOT RUN |
| Rojo 7.7.1 build | Exit code, place file location/size | NOT RUN |
| Studio CLI smoke | `BOLTBOTS_SMOKE_OK` and CLI logs | NOT RUN |
| Play mode | Screenshot/video of real running factory | NOT RUN |
| 2-player isolation | Server test and negative cases | NOT RUN |
| Mobile HUD | Emulated phone screenshot + noted issues | NOT RUN |
| Git baseline | Commit identifier without secrets | NOT RUN |

Record *actual* commands and results; if a test cannot run, preserve NOT RUN and explain why.
