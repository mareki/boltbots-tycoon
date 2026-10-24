# Technical Architecture v0.2 — BoltBots Tycoon

## Principles

1. **Server authoritative:** all currencies, purchases, unlocks, production state, rewards and inventory are verified by server logic.
2. **Data-oriented, testable:** domain logic should be independent of Roblox APIs when feasible; state transitions accept explicit inputs and return outputs for unit testing.
3. **One writer for economy:** transactions mutate balances only through a central EconomyService with consistent validation and observability.
4. **Incremental MVP:** every milestone creates a usable vertical slice, not a half-implemented feature forest.
5. **File-first:** `src/` and `default.project.json` are git-versioned; Rojo builds a place and syncs scripts when suitable.

## Proposed folders (to be built by Codex)

```text
src/
  ReplicatedStorage/
    Shared/
      GameConfig.luau
      Types.luau
      EconomyRules.luau
      MachineCatalog.luau
      RobotCatalog.luau
      Remotes/ (definitions / contracts only)
  ServerScriptService/
    Main.server.luau
    Services/
      PlayerDataService.luau
      PlotService.luau
      ProductionService.luau
      EconomyService.luau
      UpgradeService.luau
      RobotCollectionService.luau
      PurchaseService.luau
      AnalyticsService.luau
  StarterPlayer/
    StarterPlayerScripts/
      Client.client.luau
      Controllers/
        HUDController.luau
        ShopController.luau
        BuildController.luau
        TutorialController.luau
```

Current starter has only stubs; this directory tree is a design target.

## Trust boundaries and state flow

```text
Touch / Mouse / Gamepad
    -> Client UX (request, no authority)
    -> Versioned RemoteEvent / RemoteFunction contract
    -> Server validation (identity, plot ownership, cooldown, price, allowed action)
    -> Economy/Production/Inventory domain update
    -> Persist with retries / write throttling / session-safety strategy
    -> Replicated state delta (server -> clients)
    -> UI feedback and analytics
```

Server must calculate prices and output rates. Never accept `coins`, `productionAmount`, `ownedGamePass`, `rarity` or `purchasePrice` as a client-trusted value. Use separate server-side grant paths for sandbox tests.

## Data schema proposal (versioned)

```lua
PlayerProfile = {
  schemaVersion = 1,
  cash = 0,
  lifetimeEarned = 0,
  tutorialStep = 0,
  ownedBlueprints = {"starter-bot"},
  equippedRobot = "starter-bot",
  factory = { layoutVersion = 1, machines = {}, upgrades = {} },
  cosmetics = {},
  lastSeenAt = 0,
  receipts = {}
}
```

- Use Roblox DataStoreService with explicit data versioning, concurrency protection, write coalescing, exit-save strategy and robust handling of failure modes.
- Avoid unbounded receipts in profile; choose bounded/idempotent receipt mechanisms per Roblox `ProcessReceipt` guidelines.
- Cap offline progress calculations on elapsed real time; never use client-provided timestamps.
- Create migration tests for each schema version. No profile wipes during updates without owner approval.

## Roblox engine performance targets (initial design goals)

- Mobile-first HUD; explicit small-screen checks at 16:9, 19.5:9 and tablet aspect ratios.
- Few active physical conveyor parts at a time; use batched, pooled or simulated visuals where needed.
- No per-part infinite loops for dozens of machines; central tick scheduler (e.g. 1Hz authoritative production accounting) with client animations independent of rewards.
- Object streaming compatible where supported; request limits and device testing gate later.
- Startup usable within a reasonable target (initial goal ~10s on test devices), instrument p50/p95 rather than claim benchmarks.

## Telemetry event taxonomy

| Event | Properties (no direct personal data) |
|---|---|
| `session_start` | session_id, version, device_class |
| `tutorial_step` | step_id, duration_s, result |
| `machine_purchase` | sku, soft_cost, player_level |
| `robot_unlocked` | robot_id, source |
| `shop_view` | surface, shop_version |
| `purchase_started` | product_key, type |
| `purchase_confirmed` | product_key, receipt_reference_hash, source |
| `session_end` | duration_s, progression_stage |

Roblox developer analytics and platform policies determine which events can/should be submitted and stored. Never log raw payment credentials, chat messages or personal identifiers into external tracking systems.

## Test pyramid

1. **Pure unit tests** for economy rules, machine rates, unlock prerequisites, profiles and offline progress calculations.
2. **Rojo build + static validation** for file/project structure, code analysis and reproducibility.
3. **Studio CLI smoke tests** for runtime module resolution and basic service wiring.
4. **Studio manual/agent assisted end-to-end** on Mac with mobile emulation and at least two test players for server/client correctness.
5. **Private Roblox test experience** for persistence and monetization behavior before any public release; owner approval required.

## Known technical unknowns

- Stable real end-to-end purchase test flow depends on sandbox/Studio behavior and published private place.
- Rojo plugin and Studio version may change; verify actual commands on owner Mac.
- Native Studio CLI `RunScript` coverage does not prove render fidelity, controls or networking under real client conditions.
- Automated UI clicking needs accessible computer-control tooling and permissions; implement cautiously, with capture-based evidence and fallback manual approval.

## Current M1 implementation boundary

The `EconomyRules` module owns pure deterministic pricing and production rules. `Main.server.luau` owns in-memory profiles and plot allocation; `WorldBuilder` creates anchored factory geometry on server boot. The LocalScript renders only; its `RequestUpgrade` sends no client-side price or plot ID. All profiles currently reset after leaving; `DataStoreService` is intentionally deferred until M2. `GetSnapshot` answers only for the invoking player. Do not change this trust boundary while adding saving or robots.
