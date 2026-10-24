# QA, Compliance, Privacy & Release Gates

## 1. Test matrix

| Layer | Scenario | Evidence / blocking rule |
|---|---|---|
| Schema/build | Valid `default.project.json`; Rojo resolves files | Build log; blocks even private beta if broken |
| Economy | zero balance, boundary, multiple rapid purchase requests | deterministic unit test, no negative cash |
| Authority | forged playerId/plotId/price/output | server rejects, no asset/currency mutation |
| Save/load | rejoin, API transient errors, schema upgrade, quit during save | actual Studio/private test and logs |
| Production | automated 3-stage chain yields deterministic cash | Studio runtime + output test |
| UX | touch first interaction, shop exit, upgrades | mobile emulator + real phone observation |
| Multiplayer | 2 clients, unauthorized attempts to modify visitor plot | Studio 2-player session |
| Performance | 4 player plots and active assembly effects | profile output on representative devices |
| Accessibility | no color-only warnings; UI scale and mute | checklist + annotated screenshots |
| Commerce | pass ownership, receipt duplicate/retry, cancel purchase | private approved test, no accidental real charges |
| Recovery | rollback build, data migration and error alert | written reproducible recovery exercise |

## 2. Beta release gates

- B0 completed and `rojo build` repeatable.
- P0 gameplay specs complete, no known exploitable currency/entitlement path.
- Tested first session with at least five novice participants where feasible; record actual time to first robot and observed blockers.
- Cross-device playtest done; no showstopper crashes or unusable touch targets.
- Assets rights ledger complete, product name checked for conflicts, Roblox content and age policies reviewed.
- DataStore use and save migration evidence captured; no silent data loss.
- If telemetry includes third-party tools, privacy and data processing reviewed.
- Private experience ID created only with owner's account approval; owner runs a real session.

## 3. Public release gates

- Approved release candidate with version + source commit and archived build artifact.
- Publishing eligibility, platform declarations, content maturity, metadata and appropriate privacy settings confirmed in current Creator Dashboard.
- Monetization disabled by default unless separately approved and purchase systems fully tested.
- Rollback guide ready; channel for player reports identified; account access not shared with agents beyond approved least-privilege mechanisms.
- Owner explicitly authorizes public visibility and any financial spend.

## 4. Roblox 2026 distribution eligibility — important operational dependency

According to Roblox's current Creator Hub publishing guide, release eligibility is **audience-dependent**. Do not assume a new developer account can immediately make a game available to young users.

- **Initial age-checked 16+ audience:** a creator account in good standing and at least two days old, an age check, and the required maturity/content declaration. Launch audience is restricted according to the content rating/answers.
- **Audience including Roblox Kids / Select (under 16):** in addition, identity/age verification appropriate to the creator's age, 2FA, a qualifying two-month Roblox Plus/Premium subscription **or** a one-time refundable fee as applicable, full maturity questionnaire, relevant rating and game evaluation. Roblox's Kids/Select guide currently describes an evaluation condition of 250 unique plays by highly engaged users over the preceding 60 days; eligibility and fees may change.
- **Action:** At B0, the owner and agent choose intended launch audience. At REL-01, the release agent collects a fresh screenshot of live Creator Dashboard eligibility **before** budgeting age-targeted creator campaigns. Do not infer prices/eligibility from old docs.

Official guides: https://create.roblox.com/docs/production/publishing/publish-games-and-places and https://create.roblox.com/docs/production/publishing/kids-and-select

## 5. Risk register

| Risk | Severity | Mitigation / owner action |
|---|---|---|
| User account compromise | Critical | login only via official flows, no cookies, 2FA, least privilege |
| Duplicate developer product grants | Critical | server-only idempotent ProcessReceipt path, receipt tests |
| Persistent profile corruption | High | versioned schema, migration fixtures, backup plan |
| IP infringement | High | origin record for each asset; original AI concepts not traced clones |
| Harmful purchase pressure | High | cosmetic-first, clear native confirmation, policy review |
| Mac automation overreach | High | permission approvals per action, no unsafe shell tricks |
| Sudden Roblox API/policy change | Medium | official source recheck before launch, staging tests |
| Low player retention | Business | instrument FTUE, test before ad scale |

## 6. Rollback playbook (draft)

- Tag/identify last known good build and source revision.
- Disable affected paid product surfaces if fulfillment is broken; avoid abandoning receipts.
- Pause update and investigate server logs and schema migration effects.
- Restore functionality via approved Studio/Open Cloud deployment, preserving saved data; verify affected user cohorts.
- Log incident, mitigation and root cause in release history.

## 7. Publication ownership

Codex may create a **proposal** for publication and automate eligible staging steps when permissions allow. Final toggles, payments, account verification and public publishing are owner-authorized actions. This package is not a promise of "one-click guaranteed money".
