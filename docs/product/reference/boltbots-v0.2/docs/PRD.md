# PRODUCT REQUIREMENTS DOCUMENT — BoltBots Tycoon

**PRD v0.1 | Intended audience:** Product owner, lead Codex agent, implementation subagents, QA.  
**Statuses:** PROPOSED until approved; READY after dependency resolution; DONE only with evidence.  
**Scope:** P0 = critical for first MVP; P1 = after MVP; P2 = exploration.

## 1. Product objectives and non-goals

**Objective O1:** First-time players can assemble their first visible robot in under 60 seconds without instructions outside the game.  
**O2:** Players can meaningfully automate, upgrade and decorate one factory with saved progress.  
**O3:** Server-side authoritative state protects cash, inventory, and paid entitlements.  
**O4:** Gameplay is comprehensible on desktop and mobile.  
**O5:** Release only with trustworthy QA, telemetry, age-appropriate commerce, and human publishing approval.

**Non-goals:** exact simulation of industrial logistics, PvP theft, complex physics, paid randomized loot, player trading, multi-world storyline, uncontrolled user-generated content, full automation of accounts/payments/public release.

## 2. Functional requirements

### Platform / account / initial project

| ID | Pri | Requirement | Acceptance criteria |
|---|---|---|---|
| BOOT-01 | P0 | Local macOS toolchain | Doctor report documents macOS, Git, Codex, Rokit/Rojo, Roblox Studio; missing steps explicit |
| BOOT-02 | P0 | Reproducible source build | `bash scripts/build.sh` creates `.rbxlx` with exit 0 from clean checkout |
| BOOT-03 | P0 | Runtime smoke | Studio CLI or documented manual equivalent verifies correct boot and module wiring |
| BOOT-04 | P0 | Agent logging and approval gate | Each implemented requirement points to evidence and high-risk actions require human approval |
| SYS-01 | P0 | Player plot ownership | 2 clients never edit each other's plots; server rejects forged plot IDs |
| SYS-02 | P0 | Persisted player profile | Save/rejoin restores cash, blueprints and machines; failure behavior tested |
| SYS-03 | P0 | Safe migrations | `schemaVersion` included and at least one migration fixture/test passes |
| SYS-04 | P0 | Server-side economy | All production, unlock and spend calculations validated server side |

### First-time UX and game loop

| ID | Pri | Requirement | Acceptance criteria |
|---|---|---|---|
| FTUE-01 | P0 | Immediate orientation | First interactive objective obvious on mobile and desktop without outside explanation |
| FTUE-02 | P0 | First visible robot | Novice test cohort median time-to-first-robot target <=60s; instrument and report actual |
| FTUE-03 | P0 | First upgrade | Player can buy speed L2, see feedback and compare output before/after; no negative balance |
| LOOP-01 | P0 | Basic manufacturing chain | Parts -> assembler -> packaging reward; output deterministic server-side |
| LOOP-02 | P0 | Machine upgrade catalog | Versioned machine configs; increasing costs; server computes price/rate |
| LOOP-03 | P0 | Collect 5 robot designs | 5 unique unlockable robot families, persistent ownership and visual distinction |
| LOOP-04 | P0 | Factory cosmetics | At least 3 free color/detail choices and one saveable display placement |
| LOOP-05 | P0 | Progression goals | Clear next unlock at all stages; end-of-MVP milestone shown, no dead-end UI |
| LOOP-06 | P1 | Bounded offline progress | Documented cap, server clock, cannot mint money via client clock/time spoofing |
| SOC-01 | P1 | Friendly visit showcase | Visitor can view but cannot mutate plot; privacy/access considerations documented |

### UI, accessibility, performance

| ID | Pri | Requirement | Acceptance criteria |
|---|---|---|---|
| UI-01 | P0 | Responsive core HUD | Cash, production rate, goal and menu controls readable and usable on phone + desktop |
| UI-02 | P0 | Accessible interaction feedback | Visible/textual feedback accompanies color or effect; no color-only state |
| UI-03 | P0 | Shop-independent progression | Complete MVP without spending Robux; no artificially paid progression gates |
| UI-04 | P0 | Explicit buy and cancel states | Upgrade requires valid current server price and user intent; failed buys don't spend |
| UI-05 | P1 | Settings | Sound toggle, reduced-motion setting and basic UI scale test |
| PERF-01 | P0 | Mobile playability | Measured smooth play on at least one lower-end target phone; report frame-time and memory, avoid invented pass thresholds |
| PERF-02 | P0 | Stable server cost | No runaway production loops; profiling evidence for 2-4 players and multiple factories |

### Economy, commerce, analytics

| ID | Pri | Requirement | Acceptance criteria |
|---|---|---|---|
| ECO-01 | P0 | Deterministic upgrade pricing | Invalid purchases, double buys and simultaneous requests cannot duplicate rewards |
| ECO-02 | P0 | Balance sanity suite | Unit tests cover zero balance, cost boundary, overflow, duplicates and invalid rate |
| MON-01 | P1 | Cosmetic Game Pass entitlement | Server verifies ownership; UI reflects it; no false grant in Studio |
| MON-02 | P1 | Repeatable products if approved | `ProcessReceipt` with idempotent durable fulfillment, retries and logging; do not implement until approved |
| MON-03 | P1 | Compliance review | Paid item labels, prompts, age policy and required disclosures checked before launch |
| ANL-01 | P0 | Event taxonomy | `session_start`, `tutorial_step`, `machine_purchase`, `robot_unlocked`, `session_end` measurable in dev |
| ANL-02 | P1 | Commerce instrumentation | Shop view, attempt, successful receipt, failures; distinguish studio test from production |
| LIVE-01 | P1 | Versioned balancing | Config-driven prices/output, rollback possible and performance smoke passed |

### Quality and release

| ID | Pri | Requirement | Acceptance criteria |
|---|---|---|---|
| QA-01 | P0 | Automated build and validation | All required checks pass on clean workspace or have tracked blockers |
| QA-02 | P0 | Exploit tests | Crafted remote requests cannot modify other plots or award unearned cash/items |
| QA-03 | P0 | End-to-end checks | New session, upgrade, save/rejoin and 2-player isolation recorded with screenshots/logs |
| QA-04 | P0 | Asset rights ledger | Every imported model/sound/texture has author, origin, license, use approval |
| REL-01 | P0 | Private beta checklist | Owner-approved private place is playable; analytics and support path configured |
| REL-02 | P0 | Public launch gate | Human explicitly approves publish, policy compliance, budget, store and rollback plan |

## 3. Quality attributes

**Security:** all external client requests rejected by default until schema and gameplay condition validated. Rate-limit sensitive actions; guard duplicates, race conditions, overlapping sessions and unauthorized plot operations.

**Reliability:** never lose progression silently; clearly surface save errors in dev builds and log bounded retry behavior; release requires data migration/rollback plan.

**Usability:** UI on multiple screen sizes, robust touch target sizing, no critical instructions only as tiny text, scalable instructional cues; avatar camera interactions testable.

**Performance:** measure with Roblox profiling on real Mac/phone and fixed test scenarios. Frame-rate targets are budget-dependent; establish baseline before setting hard release bar.

**Compliance:** observe Roblox community standards, commerce and randomized item policy. Specifically avoid paid random rewards/false discounts/pressure tactics in MVP.

## 4. Analytics and success metrics

| Metric | Instrumentation | Initial hypothesis |
|---|---|---|
| Time to first robot | First `robot_unlocked` minus `session_start` | Median <=60s |
| Tutorial completion | Unique completed / starters | >75% after usability iteration (target only) |
| D1 retention | Roblox dashboard cohort metric | Track and compare to genre benchmarks, not assume |
| D7 retention | Roblox dashboard cohort metric | Track and compare to genre benchmarks |
| First paid conversion | Purchasers / relevant eligible active users | Do not set target until baseline established |
| Crash/error rate | Logs and synthetic smoke | No unresolved P0 defects at private beta |

Retention and revenue thresholds must be selected **after** credible benchmarks and initial tests; hardcoding arbitrary benchmarks as pass/fail would be misleading.

## 5. MVP definition of done

All P0 requirements demonstrably implemented, tested and logged; owner reviews video/screenshot evidence, plays a real Studio build, approves branding and monetization status; no unreviewed external dependency, secret or third-party license issues.

## 6. Delivery sequencing

`BOOT-*` -> `SYS-01, SYS-04, LOOP-01` -> `FTUE-* + UI-*` -> `SYS-02/03` -> `LOOP-02/03/04/05 + ECO-*` -> `ANL-01` -> `QA-*/PERF-*` -> `REL-01` -> later `MON-* + REL-02`.

See `ROADMAP.md` for candidate task slicing and `AGENT_PLAYBOOK.md` for evidence format.

## Implementation note v0.2

M1 partial source satisfies *parts* of SYS-01/SYS-04, FTUE-01/02/03, LOOP-01/02, ECO-01 and UI-01 in design, but no acceptance criterion is marked DONE until actual Roblox Studio Play tests, exploit tests and device screenshots are recorded. SYS-02/03 persistence and LOOP-03 5 blueprints are not yet implemented. See `docs/SPRINT_01.md`.
