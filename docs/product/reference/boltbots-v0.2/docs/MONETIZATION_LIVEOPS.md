# Monetization, Economy Integrity & LiveOps Specification

**Version:** v0.1 | **State:** PRE-LAUNCH CONCEPT — commerce implementation requires owner approval.

## 1. Philosophy

Fun and fairness come first. The game remains complete and enjoyable without purchase. Monetization is aimed at identity and convenience, not by making base gameplay intentionally unpleasant. Pricing is presented clearly; buying is never the only route to rewarding progress.

Roblox's monetization guidelines prohibit misleading or pressure-based purchase prompts. Avoid fake time limits, 'always on sale' labels, dark patterns and paid randomization in v1. Read current policies again at release.

## 2. Draft SKU catalog (price hypotheses, NOT approved)

| SKU | Type | Proposed price | Entitlement and disclosure | Status |
|---|---|---:|---|---|
| `PASS_NEON_VIP` | Pass, one time | 399 Robux | Neon-themed cosmetic machine skin + chat-free VIP badge | P1 / needs approval |
| `PASS_BOT_STYLE` | Pass, one time | 149 Robux | Alternate robot paint pack, no rate advantage | P1 / needs approval |
| `PROD_FACTORY_DECOR` | Developer Product, repeatable only if justified | 99 Robux | One selected décor bundle, with duplicate purchase handled clearly | P2 / design review |
| `PROD_TEMP_BOOST` | Developer Product, repeatable | 79 Robux | Temporary production buff with explicit expiry, can disadvantage free players | DEFER by default |

Do not create or sell any SKU before human approval of product name, price, artwork, rights, policy fit and implementation tests.

## 3. Purchase architecture

1. UI reads an approved product catalog and prompts Roblox's native confirmation flow.
2. Server never trusts the client to declare ownership or transaction success.
3. Permanent pass entitlements checked against platform ownership; handle errors and cache invalidation safely.
4. Developer product rewards use a single, durable `MarketplaceService.ProcessReceipt` grant path. Fulfillment must be **idempotent** on `PurchaseId`; retries, disconnects and duplicate delivery cannot mint multiple rewards.
5. No 'success' analytics until server delivery is verified; record failed and deferred receipts for recovery.
6. Explicit test modes must never accidentally grant permanent production entitlements.
7. Paid items and pass permissions stored minimally; avoid embedding credentials in client or logs.

## 4. Financial model (sanity example only)

For an experience-owned pass/developer product with a representative 70% developer allocation and a standard DevEx conversion of $0.0038 per eligible earned Robux (verify on actual release date):

`Eligible dollar-equivalent ~= monthly active users * payer rate * avg Robux spent/payer * 0.70 * 0.0038`

Hypothetical: 40,000 MAU x 3% payers x 300 Robux = 360,000 gross Robux -> 252,000 potentially earned Robux -> **$957.60 equivalent** before fees, operating costs and taxes. Not guaranteed and not a liquidity promise. DevEx minimums and conditions apply. Other revenue types have other allocations. Roblox also currently advertises a higher DevEx rate for certain eligible transactions with age-verified U.S. adults; it is excluded from the conservative example. The exact earning eligibility is determined by Roblox (see official DevEx docs).

Never forecast profitability by comparing only acquisition clicks to first-session spend. Use payer lifetime value vs cost to acquire active paying cohorts; cohort retention matters more than raw visit spikes.

## 5. Key metrics and event definitions

| Metric | Definition | Owner review cadence |
|---|---|---|
| D1/D7 retention | Roblox returning cohort users | Weekly |
| Session duration | Measured actual play session, distribution not only mean | Weekly |
| FTUE completion | Completed tutorial / new sessions | After every tutorial iteration |
| Shop exposure | Unique players who saw offer without forced popups | Weekly after commerce release |
| Conversion | Eligible unique purchasers / eligible active exposed users | Weekly |
| Earned Robux | Eligible earned Robux after applicable platform rules | Monthly |
| Developer payout | Actual DevEx cash received | Accounting, not estimated |
| UA ROAS | Cohort earned value vs verified campaign spend | On sufficient sample only |

## 6. LiveOps plan after beta

- Weekly low-risk balance fix and usability optimization; new assets require provenance.
- Monthly (if metrics justify) new robot blueprint or decor; no artificial scarcity deadlines.
- Feature flag/catalog changes require staging checks and rollback plan.
- Incident response: disable affected purchase SKU, preserve receipt logs, ensure affected players are compensated without duplicate grants.
- Maintenance: backup source and release manifests; keep on-call owner contact and changelog.

## 7. Release blockers for commerce

- [ ] Owner approved price and product matrix.
- [ ] Paid purchase flow live/sandbox tested on approved private experience.
- [ ] Receipt idempotency verified, refund/restoration behavior reviewed.
- [ ] UI visibly displays exact prices and benefits; platform policies and content rating checked.
- [ ] Analytics can distinguish exposures and purchases from Studio tests.
- [ ] Access permissions for Roblox Open Cloud, if used, are least privilege and secrets stored outside Git.
