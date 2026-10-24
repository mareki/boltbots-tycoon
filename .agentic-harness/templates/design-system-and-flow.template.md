# Design System And Flow — {{PRODUCT_OR_FLOW}}

> Artifact ID: `{{PRODUCT}}-DESIGN-{{NNN}}`
> Instantiated artifact class: Product specification
> Authority: Product-wide design and named flows
> Revision status: `draft`
> Semantic owner / creator: {{OWNER}}
> Revision/version: {{REVISION}}
> Governing artifacts: {{VISION_REQUIREMENTS_DOMAIN_CONTRACT_IDS}}
> Effective Domain Foundation/context revisions: {{FOUNDATION_CONTEXT_REFS}}
> Creator is excluded from approval quorum
> Review: {{REVIEW_ID_OR_PENDING}}

## Design System v0

- Experience principles: {{PRINCIPLES}}
- Semantic color/contrast tokens: {{TOKENS}}
- Typography: {{TOKENS}}
- Spacing/layout/responsive: {{TOKENS}}
- Content/error language: {{RULES}}
- Accessibility behavior: {{RULES}}
- Components derived from approved flows: {{COMPONENTS_AND_STATES}}
- Applicable optional categories / N/A: {{BRAND_MOTION_IMAGERY_ELEVATION}}
- Non-goals and extension rule: {{NON_GOALS}}

## Mockup Contract

- Supplied source digests / rights-safety classification / evidence owner: {{BASELINE_PROVENANCE}}
- Input mode: `absent | static | executable | mixed`; covered surfaces and gaps: {{COVERAGE}}
- Identity anchors and baseline axes: {{IDENTITY_COLOR_TYPE_LAYOUT_COMPONENT_DENSITY_IMAGERY}}
- Primary outcome / representative screens, states, viewports: {{BOUNDED_SCOPE}}
- Permitted minor corrections / proposed material deviations / extension rule: {{DELTA_CONTRACT}}
- Maintained Product-owned source path / render and matched-comparison procedure: {{SOURCE_RENDER_PLAN}}
- Creator/reviewers / Agent-cost budget / stop condition / decision value: {{EFFORT_AND_STOP}}
- Design Direction Checkpoint: `not_required_authorized_no_input | not_required_existing_direction | pending_direction_setting | approved_direction_setting`; authority/evidence: {{DIRECTION_DECISION}}

## Flow Inventory

Information architecture, navigation, routes, and screens express user tasks across Contexts; they
must not mirror Bounded Contexts, aggregates, or First-Class Product Objects one-to-one without
observable user evidence.

Privileged Product access applicability: `applicable | not_applicable | unresolved`. UI horizon: `MVP | first_six_weeks | first_operable_deployment | deferred | not_applicable`. `unresolved` follows the Initialization decision rule and cannot be disguised as design deferral. When applicable in the named horizon, include first-access/enrollment, permission denial, recovery, and one representative Product-specific Backoffice outcome—never a generic Admin dashboard invented by the Harness.

| Flow/step/screen ID | Actor/trigger | User action and system outcome | Domain owner + Contract IDs/semantics | Alt/failure/denial/recovery | Desktop/mobile/a11y |
|---|---|---|---|---|---|
| {{ID}} | {{ACTOR}} | {{ACTION_OUTCOME}} | {{OWNER_CONTRACT}} | {{STATES}} | {{NOTES}} |

For material workflow UI, explain here or by an exact reviewed source reference: user goal/entry/end;
what rows/cards/details represent and why they are grouped; distinct lifecycle, revision, component
progress and final-decision meanings; each screen/control's action, role/guard and state effect;
decision scope (object/version/target) and source-owned invalidation/preservation after change.
Walk relevant partial progress → revision → recheck → final outcome → downstream stop. Do not infer
universal grouping or validity rules from backend structure. Use the smallest sufficient account;
unchanged/static/copy-only work references the checked flow and justified delta, not a new model.

The assigned independent reviewer checks that meaning before costly visual creation, within the
existing review budget. Resolve concrete source conflicts with the semantic owner. Early semantic
review does not replace later actual image inspection or holistic visual acceptance.

## Source And Render Manifest

This section is a non-authoritative index. For the initial customer-facing UI, the maintained editable source is a locally runnable `design_reference_only` Interactive HTML Mockup using deterministic synthetic fixtures and no Product backend/cloud/provider/secret. `product-input/**` remains immutable; adopted source is copied into Product-owned `docs/design/**`. Each source and render retains its own class, revision/digest, owner, and provenance.

| Screen/state | Baseline source/render digest | `design_reference_only` candidate revision/path | Local start/viewport/fixture/route | Candidate PNG digest/path | Requirement/flow/component/Slice IDs |
|---|---|---|---|---|---|
| {{SCREEN}} | {{BASELINE}} | {{SOURCE}} | {{RENDER_INPUT}} | {{PNG}} | {{TRACEABILITY}} |

## Material Deviation Register

| Screen/state | Changed identity/system axes | Minor/material | Exact reason/evidence | Authority/disposition |
|---|---|---|---|---|
| {{SCREEN}} | {{AXES}} | {{CLASS}} | {{EVIDENCE}} | {{AUTHORITY}} |

## Critical-User Review

Assess against Product Vision: correctness, outcome completion, usability, hierarchy, UI/UX consistency, accessibility, trust, relevant latency, failure/recovery, avoidable effort, and technical feasibility. Findings require render/source evidence and user impact; taste alone is not a block.

## Scope Reslice / Implementation Comparison

Design-reference paths remain permanently non-importable/non-promotable. An authorized Walking-
Skeleton Work Package technically reimplements the binding design reference as new Product runtime
source without reinterpreting its covered observable contract. For an existing Product, established
shared shell, Design System, global tokens, shared components and cross-page behavior remain
binding unless the Work Package explicitly authorizes their global revision. A functional
prototype is either that Delivery Slice or a separately approved Technical Risk Experiment; no
third lifecycle exists.

{{SLICE_SPLIT_DECISIONS_OR_LATER_STAGING_COMPARISON}}
