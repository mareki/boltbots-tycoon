# VISUAL DESIGN BIBLE v0.1 — BoltBots Tycoon

**Visual vision:** Premium-friendly retro-futurist toy factory: bright, approachable, legible at a glance on small phones; mechanical satisfaction without realistic pollution, aggression or visual clutter.

The included `assets/mockups/*.png` are **original AI-assisted CONCEPT REFERENCES**, not in-engine screenshots or pixel-perfect game UI. Text, fictional values, individual robot forms and button positions require human design review and source implementation. They are not cleared final game assets merely because they are included here.

## 1. Creative pillars

- **Toy precision:** robust machine shapes, subtle bevels, oversized recognizable control surfaces.
- **Cheerful technology:** cyan power, amber highlights, indigo structure, rounded friendly robots.
- **Action readability:** one major objective on-screen at once, obvious interactable surfaces and progression feedback.
- **Mobile-first:** avoid tiny text, narrow margins, floating UI across thumb controls.
- **Designed, not copied:** no recognizable competitors' mascots, layouts, type treatments, environment compositions or sound motifs.

## 2. Canonical color design tokens

| Token | Hex | Use |
|---|---|---|
| `ink.deep` | `#101B35` | Main high-contrast HUD panel background |
| `ink.panel` | `#172B4D` | Card/background elevation |
| `brand.cyan` | `#48D8F4` | Energy, select, active production line |
| `brand.amber` | `#FFCE53` | Factory Cash, main progress highlight |
| `brand.coral` | `#FF956B` | Warm accessory accents |
| `brand.violet` | `#A784F7` | High-end robot identity, never solely as rarity cue |
| `positive` | `#5AD9A6` | Successful actions / confirmed upgrades |
| `danger` | `#F4747B` | Error states with icon and text |
| `text.main` | `#F4F8FF` | HUD text on dark |
| `text.muted` | `#B9C8DB` | Secondary labels |
| `surface.light` | `#E7F3FF` | Bright world background surfaces |

Use `assets/design-tokens.json` for export to Luau/Studio. Text contrast must be inspected on actual game surfaces; palette alone doesn't guarantee accessibility.

## 3. Robot art direction

- Proportions: toy silhouettes, head-to-body emphasis, big legible eyes/sensors and unique posture.
- Sculptural vocabulary: broad chamfers, soft cuboids, round shoulder guards, no sharp weapons or scary grins.
- Primary material: painted polymer with controlled gloss; limited brushed metal and emissive visor accents.
- Animation: 0.4–0.8s assembly burst, satisfying but restrained idle motion; low-motion alternative to reduce sensory overload.
- Identity: five robot families named Scout/Bolt/Orbit/Luma/Atlas; do not mimic exact faces or shapes in competitor images.
- Rarity signaling: descriptive label + clear distinct silhouette; never color-only.

### Starter robot reference

`assets/mockups/03_robot_shop_concept.png` displays one **rough composition** with variants and a proposed shop. The actual shipped robot collection must be newly modeled and rights-cleared, with distinct color/shape for each family.

## 4. Environment concept

`assets/mockups/01_factory_world_concept.png`: birds-eye/three-quarter view of a wide, playful robot assembly hall. Keep sightlines clear, use modular building blocks and frequent moving visual cues. The map should remain navigable with default Roblox character scale and camera mechanics. Prefer bespoke in-engine geometry and verified licensed meshes over marketplace model packs containing untrusted scripts.

**Starter plot plan:** 1 arrival zone (left), 1 main interactive assembler, 1 cash pickup/display zone, 2 locked expansion sockets, 1 robot showcase pedestal, 1 exit/return area. Use color-coded floor lanes to direct first-time players.

**Materials:** matte painted metal, warm polymer casing, a few glossy emissive strips, no high-noise photorealistic textures.

**Lighting:** soft daytime with clean shadows; gameplay objects must remain readable at low graphics settings. Neon effects should support cues, not carry vital information.

## 5. HUD and shop

`assets/mockups/02_hud_concept.png` is a visual mood board only. The intended production HUD should **not** copy its exact layout blindly; implement following constraints instead.

**HUD hierarchy:**
1. Top: Factory Cash total + unobtrusive production rate (human-readable abbreviated numbers).
2. Left or top-left: current task, one clear next unlock.
3. Bottom: build / collection / upgrades / shop controls, with 44+ logical px touch-target guideline (adapt to Roblox scaling and testing).
4. World-space marker: only current required object highlights for FTUE.
5. Toast: one success/error message at a time with text + icon, dismissable.

**Shop design:** separate Cosmetics and Upgrades tabs; each offer has image, precise Robux price, explicit reward and a *single* confirm interaction. Never fake limited stock, unreadable fine print, auto-open at critical gameplay frustration moments, obscure close buttons or imitated system UI.

**Responsive presets:** phone portrait-ish 19.5:9, phone landscape 16:9, desktop 16:9, tablet 4:3; inspect with Studio emulator and at least one real phone. Keep safe margin for notch/camera and Roblox core GUI. Use `GuiService:GetGuiInset()` or appropriate current APIs where justified; avoid hardcoded pixel offsets.

## 6. Typography and iconography

- Player-facing UI: simple rounded sans-serif available/approved in Roblox Studio; do not require distributing third-party font files.
- Heads: bold, short, sentence case. Body: normal weight and concise instructions. Prices: tabular digits if possible.
- Use high-contrast pictograms with text labels; 3D affordances pair with a textual interaction prompt.
- Localized string keys from first implementation; no visual baked-in text on shop item art.

## 7. Animation/feedback spec

| Interaction | Feedback | Limit |
|---|---|---|
| Robot completed | Arm assembles, robot lights up, small reward pulse | <1.2s and skippable/reduced motion |
| Upgrade purchased | Machine visibly changes, rate value animates once | Do not obscure control or gameplay |
| Invalid purchase | Contextual message explaining why | No negative balance |
| Blueprint unlocked | Dedicated card + model rotation | No gambling-style reveal or fake chance |
| Save restored | Short unobtrusive success indicator | Do not misrepresent actual failed save |

## 8. Required visual asset deliverables (owned by Codex/art process)

- [ ] Consistent graybox screenshot on 16:9 and 19.5:9, with focus path drawn.
- [ ] 5 unique robot silhouettes, model provenance and style checks.
- [ ] Production line modules: input bin, assembler, packager, speed upgrade, display pedestal.
- [ ] HUD design pass at 3 breakpoints plus no color-only states.
- [ ] Commerce screens with real price variables, verified Roblox purchase behavior.
- [ ] Screenshot/video evidence from **actual** Roblox Studio runtime.
- [ ] No copyrighted game imitation, untrusted toolbox models or AI-generated text blindly imported.

## 9. Review rubric

Score 1–5: silhouette uniqueness, tiny-screen readability, immediate focus, visual reward, UI consistency, performance, originality, consent-friendly shop. Any score under 3 blocks aesthetic approval; final asset licensing and Studio performance checks are separate hard gates.
