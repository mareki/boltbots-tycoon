# CODEX AGENT PLAYBOOK — Autonomous-but-accountable Development

**Core idea:** Codex is project engineering lead in the owner's local workspace. Product specifications determine what to build; tests and evidence determine whether it is done. Agent count is a tool, not a goal.

## 1. Agent roster (logical roles; may run sequentially)

| Agent | Responsibility | Typical outputs | Cross-role conflicts |
|---|---|---|---|
| `lead-integrator` | Architecture, plan, merges, task acceptance, logs | Git changes, milestone report | Sole writer on central project config |
| `gameplay-engineer` | Server logic, economy, machines, progression | Pure Luau modules, server tests | Coordinates with economy schema owner |
| `ux-ui-engineer` | HUD, FTUE, shop presentation, touch handling | Client controllers, Studio screenshots | Must not independently alter currency rules |
| `environment-artist` | Original assets, lighting, assembly animations | Models, rights ledger, screenshots | Must avoid foreign toolbox scripts |
| `qa-security` | Exploits, saving, performance, E2E | Test scripts, review report | Independent reviewer (prefer read-only) |
| `market-analyst` | Competitor observation, attribution, KPI plan | Evidence-graded analysis | No copying competitor assets |
| `release-operator` | Private staging, release checklists, rollback | Build manifests, deployment proposal | Owner must approve publishing |

Agent framework isn't guaranteed to manifest exactly as seven independently running processes. Use built-in subagents when available; otherwise simulate roles with sequential focused tasks. Do not let multiple agents race to edit Rojo mapping, data schema or main economy config.

## 2. Standard task card

```text
Task ID: LOOP-01
Objective: Complete server-authoritative 3-stage assembly line.
Read: docs/GDD.md sections 3-5; docs/PRD.md LOOP-01, ECO-01; docs/ARCHITECTURE.md
File ownership: src/ServerScriptService/Services/ProductionService.luau; tests/... only
Dependencies: SYS-01 plot ownership, base build
Expected implementation: event/data contract, production tick, upgrade-independent reward
Acceptance: no client-authoritative rewards; invalid requests rejected;
            deterministic unit tests; in-Studio smoke evidence
Required proof: command logs, test results, screenshot from actual Studio
Approval needed: none for repo files, yes for new external executable
```

Tasks should be vertical slices with exact PRD IDs, file ownership, and verifiable evidence.

## 3. Execution routine

**Plan -> Build -> Verify -> Review -> Commit -> Report**

- First collect environment facts and repo status; do not assume installed dependencies.
- Issue small, scoped tasks. Parallelize read-only research and independent tests; avoid parallel editing of shared core systems.
- Document versions and dependency licenses. Use vetted artifacts; prefer pinned releases.
- Run checks after each meaningful change. If Studio is inaccessible, explicitly mark visual/runtime tests NOT RUN.
- Keep a record of failures and iterations. A red test is not a successful milestone.
- Make atomic commits with PRD IDs in commit messages.
- Update `docs/IMPLEMENTATION_LOG.md` after each finished task.

## 4. Evidence / implementation log format

```markdown
### 2026-10-24 — BOOT-01 [PASS|FAIL|NOT RUN]
**Environment:** macOS version, CPU, Roblox Studio version, Codex version.
**Files changed:** scripts/...  docs/...
**Actions:** exact commands with sanitized stdout/stderr (link to log)
**Tests:** doctor: PASS; rojo build: PASS; Studio CLI: NOT RUN (not installed)
**Screenshots:** assets/evidence/... (actual Studio, not AI concept)
**Risks/approvals:** no payments; login needed
**Next:** BOOT-02
```

## 5. Definition of Done vs. evidence

- Code works in the real target runtime, not merely parses in an IDE.
- Engine or Studio visual work has actual in-engine screenshots/video; synthesized concept images are **not test evidence**.
- Financial and profile mutations have negative tests (invalid client input, duplicate processing, simultaneous requests, abrupt disconnect).
- Accessibility and touch controls validated.
- Any license, source, price or functionality uncertainty recorded clearly.

## 6. Approval escalation triggers

Agent must stop and ask for precise consent before:

1. Installing OS-wide executables, enabling accessibility/automation permissions or calling `sudo`.
2. Creating GitHub repositories, Roblox experiences/groups/keys or public cloud resources in an owner's account.
3. Spending fiat or Robux; starting advertisements or creator deals.
4. Publishing outside private staging or enabling in-game monetization.
5. Removing local files beyond project build/cache directories, changing macOS security settings or uploading private content.
6. Adding features contrary to the approved no-gacha/no-pressure default.

The agent should propose a safe command/action and describe scope, effects and rollback; never request owner passwords in chat.

## 7. First release sprint ownership

- `lead-integrator`: BOOT-01..04, SYS-01 skeleton and architecture control.
- `qa-security`: spec test harness, invalid remote requests, saving failure tests.
- `gameplay-engineer`: LOOP-01, ECO-01, FTUE-03 integration.
- `ux-ui-engineer`: FTUE-01/02, UI-01/02 and phone layouts.
- `environment-artist`: factory plot + five robot silhouettes + asset provenance.
- `market-analyst`: competitor observation log after owner account approval; no unsourced metrics.

## 8. Handoff contract to product owner

Every milestone message must include: `Implemented`, `Verified`, `Known gaps`, `Approvals needed`, `Next scope`. Maximum 1–2 human actions, only those that require the owner's identity, payment authority, app-level consent or creative approval. No generic "please code/test this" requests.

## 9. Codex configurations

`AGENTS.md` in the repo root is intentionally sufficient to bootstrap. Optional subagent configuration belongs to a separate reviewed step once the installed Codex client capabilities and supported syntax are verified. Do **not** blindly install unverified MCP servers or commit OAuth tokens to speed up onboarding.
