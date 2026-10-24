# Sprint 01 - Playable Robot Factory Vertical Slice

**Status:** PROTOTYPE IMPLEMENTED IN SOURCE; local Roblox Studio execution NOT YET VERIFIED.

## Delivered in v0.2 source

- Four distinct world-space factory plots, generated from original native parts on server boot.
- Unique per-player plot assignment and server-side validated upgrade requests.
- Automatic factory cycle with a visible animated Scout robot at each production completion.
- Earn 25 Factory Cash per completed robot; first assembler upgrade costs 50 cash.
- Accessible starter HUD, progress, cycle timer and upgrade button (requires phone/desktop visual inspection).
- Pure economy rules module with repeatable Studio CLI rule-smoke assertions.
- No monetization, external models, private Roblox uploads, persistence or paid actions.

## Acceptance and evidence checklist

| ID | Case | Evidence needed | Status |
|---|---|---|---|
| B0.1 | Mac environment doctor | `scripts/doctor-macos.sh` output | NOT RUN - owner Mac required |
| B0.2 | Rojo project build | Exit 0 and nonempty `.rbxlx` | NOT RUN - Rojo unavailable in authoring environment |
| B0.3 | Studio rules smoke | CLI `BOLTBOTS_SMOKE_OK` output | NOT RUN - owner Mac required |
| M1.1 | Spawn and world | Studio Play screenshot of own factory | NOT RUN - owner Mac required |
| M1.2 | First robot in under 60s | Timer + robot production video | NOT RUN - owner Mac required |
| M1.3 | Upgrade | Two robots => 50 Cash => Level 2; cash becomes 0 | NOT RUN - owner Mac required |
| M1.4 | Isolation | Studio 2-player test: second user cannot mutate plot 1 | NOT RUN - owner Mac required |
| M1.5 | Mobile HUD | 16:9 desktop and phone emulator screenshots | NOT RUN - owner Mac required |
| M1.6 | Server exploit guard | Spurious remote args rejected; forged position no console purchase | NOT RUN - owner Mac required |

## Accepted limitations for this engineering slice

- Progress resets on rejoin. Persistence/data migrations are separate P0 requirements for the next slice and are **not implemented**.
- Prototype robots do not have inventory/rarities; more robot blueprints remain later-sprint work.
- The gameplay environment may reveal layout, collision, text scaling or Luau type issues when tested in actual Studio. Codex must fix and provide proof; the above checklist is not an assertion of a play-tested game.
- Builds generated via Rojo are local only, not a published Roblox experience.

## Codex next action

Read `docs/FIRST_CODEX_TASK.md`. Run macOS diagnostics and install the official toolchain with owner approval; then build and execute the test matrix above, fix failures, attach proof to `docs/IMPLEMENTATION_LOG.md` and only then plan M2 persistence.
