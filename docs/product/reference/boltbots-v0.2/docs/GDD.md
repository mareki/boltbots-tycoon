# GAME DESIGN DOCUMENT — BoltBots Tycoon

**GDD v0.1 | Owner approval: PENDING | Updated: 2026-10-24**

## 1. High concept

**One-line pitch:** Build an adorable robotics factory, automate production, unlock distinctive robot blueprints and show off a personal robot empire with friends.

**Player fantasy:** "I started with a tiny workbench. Now my own clever factory builds a glowing fleet of customized robots." The player sees their creation evolve rather than watching an opaque number increase.

**Genre:** Casual factory Tycoon + light collection/incremental simulator.

**Platform and constraints:** Roblox; touch-first with mouse/keyboard and controller considered. Primary audience players interested in cheerful building and collecting; design suitable for Roblox's young and mixed-age audience. Target 1–4 players per server session initially (plot allocation to be confirmed through performance testing). Free-to-play; no paid randomized rewards in MVP.

**Unique selling proposition:** Satisfying visible production + compact modular manufacturing + robot customization in a friendly futuristic world, with onboarding dramatically simpler than simulation-heavy industrial games.

## 2. Player experience pillars

1. **Immediate delight:** First robot visibly assembled in the opening 60 seconds; receive clear feedback and a meaningful upgrade within two minutes.
2. **Visible automation:** Machines, conveyors, effects and displayed robots reflect actual progress, not meaningless decoration.
3. **Collect and express:** New robot blueprints and visual variants create long-term goals; factory exhibits encourage sharing.
4. **Depth without chores:** The player can optimize layouts in later updates, but v1 is understandable without a wiki.
5. **Trustworthy economy:** Fair earn rates, no predatory paid blockers, real price labels and clean undo/confirmation interactions.

## 3. First-time-user journey

| Time | Expected experience | Success evidence |
|---|---|---|
| 0–15 seconds | Spawn at a colorful personal plot; single focus cue | Player can identify first interaction |
| 15–60 seconds | Place or activate basic assembler and produce first starter robot | `tutorial_step=first_robot` completion |
| 1–2 minutes | Collect starter cash; buy first speed upgrade | First upgrade; clear before/after feedback |
| 2–5 minutes | Add second conveyor or machine; choose a robot color | Meaningful build choice and cosmetic expression |
| 5–10 minutes | Unlock second blueprint; see next machine/goal and friend's showcase | Return-intent prompt without pressure |
| 10–20 minutes | Unlock next production stage, optional optimization | Measured retention and engagement |

These are **design targets**, not verified outcomes. Require playtesting with novices, on phone and desktop.

## 4. Core gameplay loop

```text
Choose machine / position -> produce robot units -> collect cash and blueprint XP
             |                                            |
             v                                            v
       See animated line                          Buy upgrades / blueprints
             |                                            |
             +----------------- repeat -------------------+
                                  |
                                  v
                     Customize + exhibit + share
```

**Moment-to-moment controls:** walk/rotate camera, interact with highlighted machine using ProximityPrompt or a contextual touchscreen control, preview placement ghost, confirm/cancel, open upgrade/shop/collection tabs.

**Loss/failure:** None in MVP. Players cannot permanently lose a purchased machine through misclick or visitor griefing. Optional challenge objectives are positive rewards, not punishments.

## 5. Systems: MVP (approved scope proposal)

### 5.1 Plot ownership

- Each player is assigned exactly one isolated starter plot for the session. Visitors can look but not modify or claim ownership of other plots.
- Plot layout is grid-snapped, with predefined allowed sockets during MVP to reduce complexity. Freeform conveyor routing is **post-MVP**.
- Placements persist by stable IDs and are reconstructed server-side on join. Saving must be resilient to transient DataStore failures.

### 5.2 Manufacturing

- One core production chain: **parts bin -> assembler -> packaging line -> cash pickup**.
- Machine runs on a server-authoritative tick; effects are client-side and may be pooled for performance.
- Track `machineId`, level, rate, source/target mapping and upgrade cost in shared tables read by the server; client sees replicated configuration, not writes balances.
- Production never requires buying Robux or watching an ad to continue.
- No real-world energy/water pollution mechanics in MVP. Advanced factory strategy is future scope.

### 5.3 Progression and starter economy

| Unlock | Soft currency (provisional) | Role |
|---|---:|---|
| First assembler | Free | Opening tutorial |
| Assembly speed L2 | 50 Factory Cash | First upgrade |
| Conveyor visual improvement | 120 Factory Cash | Visible production boost |
| Second station | 350 Factory Cash | New mechanical goal |
| Blueprint #2 | 600 Factory Cash + tutorial completed | New robot silhouette |
| Quality module | 1,000 Factory Cash | Production multiplier |
| Blueprint #3 | 2,000 Factory Cash | Longer-term collectible |

**Balancing targets, not promises:** initial cash production 1 unit/second; first upgrade reached by ~2 minutes allowing for tutorial learning; first visible new robot within 1 minute. Agent must simulate economy across 30-minute new-user paths and validate time-to-upgrade using playtests.

- Only one earnable currency in MVP: **Factory Cash** (not purchasable with Robux in initial launch).
- Blueprint XP is a progression value, not a second paid currency.
- Offline earnings: **P1 experiment**, cap to avoid compulsion and prevent unbounded economy inflation; excluded from first playable slice.
- No prestige reset, loot boxes, paid random eggs, gacha, trading or limited-time FOMO offers in MVP.

### 5.4 Robot collection

Five robot families for MVP (design placeholder names): **Scout, Bolt, Orbit, Luma, Atlas**. Each has distinct shape language, animation and manufacturing requirement. Rarity is based on known unlock progression, not paid randomness. Player may select color trim and choose one display pedestal robot.

| Family | Identity | Unlock mechanism |
|---|---|---|
| Scout | Tiny rounded explorer | Tutorial |
| Bolt | Fast cube-legged helper | Early blueprint purchase |
| Orbit | Floating ring assistant | Factory level 2 |
| Luma | Light-emitting service bot | Mid-progression |
| Atlas | Large construction companion | Late-MVP objective |

Robots are currently collectibles/decorative in v1, not autonomous companions with AI pathfinding. The latter is a higher-cost future feature requiring separate scope approval.

### 5.5 Social / viral affordances

- Visitors can inspect a factory; cannot steal robots or interfere with output.
- Visible friendly "factory showcase" pedestals create screenshot moments.
- Optional "visit a friend" entry point only if it can be implemented safely and is approved in scope; no general chat feature is built by us.
- Future exploration: co-op assembly missions, shared weekly community build theme, user-made factory tours. Each requires safety/privacy review.

## 6. World and art

One cheerful, low-to-mid-poly robotic industrial district: floating signage, big friendly machine shapes, clear machine silhouette outlines, blue/cyan energy lines and warm yellow highlights. No smoky grimdark realism. Views from third-person Roblox camera; players navigate the scene physically. See `VISUAL_DESIGN_BIBLE.md` for canonical requirements.

## 7. Monetization fit

MVP monetization is **cosmetic-first** and should not ship until UX and retention tests pass. Candidates are a lifetime VIP visual theme pass, a blueprint skin pack and optional factory decoration themes. Repeated functional speed boosters should be deferred for the first release until meaningful fairness tests exist. See `MONETIZATION_LIVEOPS.md`.

## 8. Content roadmap beyond MVP (not committed)

- V1.1: photo mode, factory showcase templates, save slot previews, improved mobile camera.
- V1.2: seasonal **non-exclusive** cosmetics and an optional collaborative robot-delivery challenge.
- V2: grid-based optimization, multiple production chains, robot helpers, cooperative factories.

No implementation of this post-MVP list without an explicitly accepted milestone and budget.

## 9. Key risks and mitigations

| Risk | Mitigation |
|---|---|
| Generic tycoon with weak differentiation | Unique robot assembly visual identity; first-minute usability tests |
| Endless "click to earn" becomes boring | Automation unlocking, exhibition, aesthetic customization and clearer progression choices |
| Too much scope for solo-agent production | One world, one chain, five blueprints; strict P0 gate |
| Child-audience monetization pressure | Cosmetic-first, transparent prices, no random paid loot, no fake countdowns |
| Exploits inflate economy | Server authority, validation, rate limiting, receipt idempotency |
| Mobile frame drops | Simulate conveyors instead of physics-heavy active item parts |
| Asset/IP conflict | Source provenance ledger, original naming and visual differentiation |

## 10. Approval questions requiring owner decision

- Is the cheerful/tactile, slightly stylized 3D direction accepted?
- Is single-plot casual automation preferable to deep Factorio-like routing for MVP?
- Should initial UI be English-only with German localization infrastructure?
- Is a cosmetic-only monetization launch acceptable, with functional boosts deferred pending retention data?

Until accepted, these are tracked assumptions, not authorization to spend money or release publicly.
