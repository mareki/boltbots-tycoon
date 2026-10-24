# Roadmap and Backlog — 90-day planning horizon

Dates are **estimated work ranges**, not automatic future task execution or delivery promises. This is a sequencing aid for a locally-run agent team, subject to hardware/setup, testing and approvals.

## Milestone B0: Environment / integration — Week 1

- BOOT-01: Mac doctor; record machine version, security restrictions.
- BOOT-02: Codex Git/Rokit/Rojo and reproducible Rojo place build.
- BOOT-03: Roblox Studio install and CLI/GUI smoke evidence.
- BOOT-04: repo baseline, no secrets, owner gate and log format.
- Output: verified local "hello Roblox" boot, not a full game.

## Milestone M1: First fun — Weeks 2–3

- SYS-01 plot isolation; SYS-04 server authority (initial).
- LOOP-01 deterministic parts->assembler->packager chain.
- FTUE-01/02 first-robot guided path; touch CTA.
- Output: novice gets first robot, game doesn't depend on Robux.

## Milestone M2: Retain progress — Weeks 4–5

- SYS-02 DataStore save/rejoin; SYS-03 schema migrations.
- LOOP-02 machine upgrades; ECO-01/02 validations.
- UI-01/02 responsive HUD and non-color-only feedback.
- Output: 15-minute playtest loop with persisted upgrades.

## Milestone M3: Identity and polish — Weeks 6–7

- LOOP-03 five original robot models/blueprints.
- LOOP-04/05 customization and clear long-term goal.
- Perf stability, improved sound/animation and 16:9/19.5:9 layouts.
- Output: visually coherent first-world private alpha.

## Milestone M4: Private beta and observation — Weeks 8–9

- ANL-01 measurement of session, FTUE and unlock funnels.
- QA-01..04, PERF-01/02.
- Run actual player tests, log completion and pain points.
- Output: factual evidence for improve/pivot/scale decision.

## Milestone M5: Revenue readiness + release — Weeks 10–12

- Optional owner-approved MON-01 cosmetic pass and commerce testing.
- REL-01 private staging; REL-02 public launch only after owner gate.
- Observed organic content tests; limited advertising only on explicit budget approval.
- Output: public-ready candidate, not guaranteed user acquisition.

## Backlog prioritization

For each feature estimate: player value 1–5, development effort 1–5, verification effort 1–5, exploit risk 1–5. Select first tasks with high player value and low integration risk. Split features > one sprint into smaller verifiable vertical slices.

## Stop / rethink triggers

- After the first novice tests the first-minute goal is repeatedly missed: prioritize FTUE revision.
- Save errors/duplication/exploits: block beta/commerce immediately.
- Poor retention after a meaningful sample: do not increase ads; improve core loop and onboarding.
- Originality/rights doubts: replace asset before public release.
