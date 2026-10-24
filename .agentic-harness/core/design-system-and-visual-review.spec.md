# Design System And Visual Review

> Artifact ID: `AH-SPEC-DESIGN-001`
> Artifact class: Harness specification
> Authority: Canonical
> Status: Active
> Semantic owner: Master Harness Product Design
> Version: 0.6.0
> Governing artifacts: `AH-CONSTITUTION-001`, `AH-SPEC-COLLABORATION-001`, `AH-SPEC-ARTIFACTS-001`, `AH-SPEC-DOMAIN-001`, `AH-SPEC-INITIALIZATION-001`
> Review: baseline `AH-REV-DOMAIN-FOUNDATION-ADOPTION-001`; integration candidate `AH-RUN-CONSOLIDATED-CORRECTIONS-S3-S4-001`
> Owns: Design System v0, Mockup Contracts, Interactive HTML Mockups/design references, supplied visual baselines, source/renders, flow coverage, UI traceability, visual review, and implementation comparison

## 1. Design-First Boundary And Artifact Names

A new customer-facing UI Product establishes Design System v0 and an approved design reference before delivery-intended UI implementation. During Initialization the executable visual artifact is an **Interactive HTML Mockup**: locally runnable HTML/CSS with bounded interaction, deterministic synthetic data, and no real Product behavior. It is `design_reference_only`, permanently non-promotable, and must not be called or represented as a functional prototype.

Intake may classify and safely inspect supplied visual evidence before the Human Domain Decision.
Detailed information architecture, navigation, routing, flows, screens, Mockup Contract, Design
System v0, and design-reference creation begin only after an effective Foundation exists. They bind
its exact revision and derive structure from user tasks/use cases rather than mirroring contexts,
Aggregates, or First-Class Product Objects one-to-one.

The only prospective exception is the `1.0.13+` `owner_approved_standalone` path in section 13:
when no approved mockup/design reference exists, the Run's already predeclared Decision Authority
may authorize standalone critical-user screenshot review before mutation. It does not permit
ignoring or replacing an existing approved reference, skipping candidate images, or downgrading
`significant_ui`.

A **functional prototype** contains real Product behavior. It begins only after Human Initialization Approval under either the first Walking-Skeleton Delivery Slice when delivery-intended, or a Technical Risk Experiment when hypothesis-bound and non-promotable. No third prototype lifecycle exists.

The goal of the Initialization design reference is to validate understanding, flow, usability, visual direction, and reusable primitives early while avoiding duplicate visual work, expensive redesign, and a speculative full component library. A Product without a human-facing UI records `not_applicable` with Product rationale in the Initialization Review Pack.

New screens, material flow changes, navigation changes, and new interaction patterns require a reviewed mockup before implementation. Minor changes that reuse an approved component and do not alter flow MAY use direct implementation plus visual review; the Work Contract records why no mockup was needed.

## 2. Design System v0 Contract

Design System v0 defines only what the approved MVP flows and first six-week horizon need. Its required core is:

- experience principles and intended emotional character;
- color roles and contrast-safe tokens;
- typography roles and scale;
- spacing, sizing, grid, and layout tokens;
- responsive breakpoints and layout behavior;
- content voice, terminology, labels, validation, and error language;
- initial reusable components derived exclusively from approved flows, with variants, states, composition, and accessibility behavior;
- explicit non-goals and extension rules.

Brand assets, radii, elevation, layering, motion, iconography, imagery, and extended patterns are included only when required by approved flows. An unused category may be recorded `not_applicable` without a separate artifact.

Tokens and component names are semantic rather than screen-specific. A new component is justified only when composition of existing primitives would harm usability, accessibility, consistency, or maintainability.

## 3. Mockup Contract Before Material Creation

After the Human Domain Decision and Product/flow synthesis, and before costly visual creation, the Design owner prepares one compact Mockup Contract. It binds:

- exact supplied-source digests, rights/safety classification, covered surfaces, and durable evidence owner;
- primary user outcome, flow steps, representative screens/states/viewports, and explicit coverage gaps;
- identity anchors plus color/type roles, shell/layout/composition, component/icon language, information density, and imagery role;
- allowed minor corrections, proposed material deviations, new-surface extension rules, and explicit non-goals;
- maintained Product-owned source path, render procedure, source-versus-candidate comparison set, and review owner;
- creator/reviewer topology, bounded screen/state scope, Agent/cost budget, stop condition, and expected decision value.

The primary flow reference binds §7's interaction meaning, including existing reviewed evidence
or its bounded delta. Before costly visual creation, the assigned independent reviewer walks the
material flow from entry to outcome against the named Product sources. Missing or contradictory
work-object, state, action or decision meaning blocks affected design, not unrelated work.
Resolve it with the semantic owner; a screen or reviewer may not invent Product authority. This
is an early lens of the budgeted review, not another full review, Human Gate or separate artifact.
Cheap bounded exploratory sketches may expose uncertainty, but not make invented meaning final.

When no adequate baseline exists, the authorized Initialization Run records the Mockup Contract, creates the bounded candidate autonomously from Product evidence, and presents both at the existing Human Initialization Gate. Absence alone creates no additional Human interruption. An earlier bounded Design Direction Checkpoint is used only when a concrete unresolved `direction_setting` conflict or proposed material deviation makes continued creation likely to be discarded or materially costly. This uses the existing Decision-Brief/pause path rather than creating another constitutional gate. When supplied sources establish the direction and the Contract proposes only consistent gap filling, the explicit Human instruction to use those sources satisfies the direction decision.

## 4. Adaptive Initial Design Coverage

The Initializer chooses the smallest coherent evidence set needed for the Product and supplied inputs; page count is not a quality proxy.

- **No adequate visual input:** create a high-quality Interactive HTML Mockup for the primary outcome, normally two or three representative screens plus the necessary annotated or simulated states. Include landing, authentication, navigation, or mobile views only when the Product/flow actually requires them.
- **Static PNG/JPG/SVG input:** retain it unchanged as the provisional baseline, derive Design System v0 and the flow/coverage map from it, and create only missing reference screens, responsive variants, or states needed to make the implementation contract coherent.
- **Adequate HTML/CSS/JavaScript input:** inspect and safely render it, then copy the exact adopted digest-bound source into the maintained Product-owned design path when rights and ownership permit. Do not rebuild it solely to satisfy a Harness-generated artifact requirement.
- **Incomplete or conflicting input:** preserve valid covered surfaces, identify exact gaps/conflicts, and propose the minimum correction or extension through the Mockup Contract.

The evidence must tell a coherent story from entry to primary outcome. Alternate, loading, empty, validation, error, permission/denial, destructive-confirmation, recovery, responsive, and accessibility behavior may be represented through interactive states, separate reference screens, or precise annotations according to decision value. Additional Admin/Backoffice, collaboration, onboarding, payment, export, or recovery coverage is required only when it is relevant to the MVP, first six-week horizon, or first operable deployment. The Harness MUST NOT invent a generic dashboard or irrelevant flow.

## 5. Binding Baseline, Permitted Deltas, And Source Safety

The baseline lifecycle is:

```text
immutable supplied evidence
  -> rights/safety-classified provisional baseline for covered surfaces
  -> Mockup Contract + candidate design reference
  -> Human Initialization Gate
  -> active Product design reference
```

After classification, supplied visual input is binding for every covered surface unless the Human
Product Authority explicitly classifies a named aspect as illustrative. For a new Product, the
mockup governs its covered UI. For an existing Product, it governs the changed surface while the
Product's established shared shell, Design System, global tokens, shared components and cross-page
behavior remain binding. A page-local mockup never implicitly authorizes a fork or global change to
those Product-wide owners; that requires an explicitly scoped global Design-System or shell change.

General authority to improve the Product, UI or code does not authorize reinterpretation of a
binding mockup. Covered structure, content, ordering, CTA intent, assets, states and interactions
MUST be preserved. Free redesign or usability/process improvement is permitted only when the exact
Work Package names that change as an outcome. Agents MAY still fix broken links, impossible
behavior, approved Product contradictions, responsive reflow, accessibility or security defects,
and missing states, and MAY extend uncovered flows consistently. Each such delta remains explicit
and evidenced; silence never authorizes substitution, omission or semantic reinterpretation.

Replacing a named identity anchor is material. Coordinated change across at least two of these axes is presumptively material: color/type roles; shell/layout/composition; component/icon language; information density/imagery role. A material deviation requires exact Human approval of the reason, affected surfaces, and matched source/candidate renders before the divergent candidate can become authoritative.

Supplied executable mockups are untrusted. Before HTML/JavaScript execution, the team performs static inspection of source, dependencies, package/lifecycle scripts, external requests, sensitive-data access, and applicable rights. Rendering runs in isolation with no secrets/cloud credentials, read-only input, temporary output, no host write access, and no network by default. An allowlisted dependency, script, or endpoint needs a recorded reason. `product-input/**` remains Human-owned/read-only; adoption copies selected source into a maintained Product-owned design path instead of mutating the input.

An Agent-introduced premise inside visual intake, creation, review, or HIP routing that causes omission, substitution, refusal, stop, exception, or a new Human decision MUST cite exact Human input, Harness authority, or observed evidence. Unsupported uncertainty remains an uncertainty; it does not become policy. Verified legal, license, privacy, security, accessibility, feasibility, and correctness restrictions remain enforceable.

## 6. Interactive HTML Mockup Source And Render Contract

The maintained design reference has:

- editable HTML/CSS and only the bounded JavaScript needed for local design interaction;
- a direct local render procedure requiring no cloud account, Product backend, secret, or external provider;
- deterministic synthetic fixtures and required simulated states;
- named viewport, route/state, fixture, source revision, and PNG render evidence;
- traceability to journey, flow step, requirement, component inventory, and baseline coverage.

Every such source is marked `design_reference_only`. It MUST NOT call Product APIs, cloud services, analytics, identity providers, payment providers, or Production data. Its path remains permanently non-importable and non-promotable. A later authorized Walking-Skeleton Work Package MAY technically reimplement the digest-identified design reference in Product runtime source with normal ownership, architecture, security, accessibility, testing, cost, maintainability, staging, and Slice evidence. Technical reimplementation changes code ownership and composition, not the binding observable mockup contract or established Product-wide UI owners. Design approval or render evidence does not transfer as implementation evidence.

Later low-risk design changes MAY use another editable reviewable source when interactive HTML adds no decision value. The Work Contract records the rationale. Generated renders never replace their source; review and approval bind both exact source and exact renders.

## 7. Screen And Flow Inventory

Every flow inventory states:

- actor, trigger, preconditions, permissions, and intended outcome;
- ordered step and screen IDs;
- user action, system response, data/contract interaction, and next state per step;
- alternate, failure, denial, cancellation, retry, and recovery routes;
- desktop/mobile behavior and accessibility considerations;
- components reused, introduced, or deliberately deferred.

For new or materially changed workflow UI, the existing inventory MUST coherently explain:

- user goal, entry and observable end; what overview rows/cards and details represent, and why
  meaningful grouping serves the user instead of mechanically mirroring backend jobs;
- object lifecycle, revision, component progress and final decision where they differ; an
  aggregate status is valid only if its meaning is unambiguous;
- each meaningful step's screen/control, action, role/guard, affected object, state effect and
  next step, including relevant failure, denial and recovery;
- each decision's object, revision/version and target where applicable, and the source rule
  governing preservation or invalidation after a change; and
- relevant partial-progress, revision, recheck and final-completion scenarios through the
  authorized downstream boundary, without presenting later planning/execution as done.

These are semantic duties, not mandatory new columns or files. Use the smallest sufficient
narrative, table or annotated source reference. Existing reviewed flows plus a justified delta
suffice; static/copy-only UI with unchanged meaning needs no invented lifecycle or re-modeling.
No universal parent-row layout or automatic preservation/invalidation rule is prescribed.
Product contracts decide. Existing conforming evidence remains usable without a new heading.

Every data-reading or state-changing step names the semantic Domain Owner and relevant Command, Query, Event, success/error/auth Contract IDs, or explicitly records `contract: none` with rationale. Traceability is:

```text
PRD requirement -> effective Domain Foundation -> use case -> journey -> flow -> step -> screen/state
  -> Domain Owner -> Command/Query/Event Contract and semantics
  -> design-reference source/render -> component -> Feature/Capability
  -> Delivery Slice -> Work Package -> visual evidence
```

An attractive screen that does not complete the required user outcome fails review.

## 8. Accessibility And Responsive Baseline

The initial design MUST specify semantic structure, keyboard path, visible focus, labels/instructions, error association, contrast, non-color cues, target size, zoom/reflow, and reduced-motion behavior. The applicable product profile later names the technical standard and test tooling.

Mockups include annotations where a static image cannot prove behavior. Mobile is not a scaled desktop screenshot; content priority, navigation, controls, overflow, and interruption/recovery are reviewed explicitly.

## 9. Cross-Functional Mockup Review

Interactive HTML Mockups, mockup sets and material revisions are `D2`. Version-appropriate team
size, separate start review, critical quorum and bounded escalation follow Collaboration §§1.1,4–5.
The creator differs from every independent reviewer. The assigned reviewer covers both
Product/Usability (requirements, value, terminology, interaction meaning, hierarchy, states,
accessibility intent, responsive behavior and MVP coherence) and Architecture/Engineering
(Domain/contracts, feasibility, data, performance, integration and reuse). Several functions
remain one independent voice. A concrete critical UX competence gap or unresolved material
dissent follows the bounded third-working-Agent path, not automatic fan-out from a D2 label or
generic usability concern. Creator self-check is not independent approval or final acceptance.

Devil's-Advocate/Simplicity review is required when flow size, novelty, cost, or complexity is material. It asks what can be removed or simplified without breaking the outcome.

Reviewers inspect the actual rendered PNGs, editable candidate source, and coverage-matched supplied baseline renders; a textual description alone cannot approve visual design. Findings map to exact screen/state IDs and named baseline axes. Review records list every actual deviation with classification, reason, authority, and disposition. Any material source change invalidates affected render approval.

## 10. Scope Reslicing From Design

If design-reference work reveals that a Feature, Delivery Slice, or Work Package is too large or too small, Product/Analysis proposes a split or merge. UX verifies that every resulting Slice retains a coherent user path and observable outcome; Architecture/Engineering verifies dependencies, domain boundaries, contracts, data transitions, deployment boundary, rollback, and delivery order.

If the proposed reslice changes a context, ownership, invariant, lifecycle, role, or First-Class
decision, the affected scope first follows `AH-SPEC-DOMAIN-001` impact/reapproval. Design work does
not silently redefine the domain.

The reviewed decision updates Milestone, Feature/Capability mapping, Delivery Slices, Work Packages, traceability, design-reference ownership, and acceptance criteria together. No role may change material MVP scope unilaterally, and no Slice may leave an unreachable or misleading UI state.

## 11. Implementation Comparison

UI completion evidence compares the exact running Delivery Slice with the approved design-reference revision on named viewports and states. The comparison includes:

- flow and content correctness;
- layout, hierarchy, typography, color, spacing, and component variants;
- keyboard/focus and relevant accessibility behavior;
- loading, empty, error, permission, and responsive states;
- intentional deviations and their approved rationale.

Pixel equality is not the objective because runtime composition, responsive behavior and established
Product-wide styles may require technical transformation. This creates no design freedom: every
covered observable difference must map to an established Product-wide owner, a required technical
or accessibility correction, or an exact authorized deviation. Unexplained content, structure,
order, asset, state, interaction, behavioral, token or usability divergence is a finding. Local
screenshots prove only local behavior; deploy-relevant acceptance also requires screenshots and
interaction evidence from real staging.

## 12. Design Evolution

Design System v0 evolves through actual product needs. A material token, primitive, pattern, or interaction change identifies affected screens/components, migration scope, visual regression evidence, and deprecation path.

Product-specific visual learning remains in the product. A reusable Harness process improvement follows the Harness Improvement Proposal path and MUST NOT copy product branding or assumptions into the master.

## 13. Prospective Material-UI Assurance

For Run revisions pinned to Harness `1.0.13+`, the current Run Contract selects exactly one
`material_ui | minor_ui | non_visual` applicability in the compact `visual-assurance` projection.
This is one applicability decision, not a new lifecycle or visual-only admission system.

- `material_ui` covers a new or materially changed customer-facing screen, navigation, layout,
  hierarchy, composition, density, component language or interaction pattern. Before first UI
  mutation it binds either the approved design-reference Artifact ID/exact current file digest or the exact predeclared
  Decision Authority's standalone-review decision when no mockup exists, plus the few
  representative critical surfaces/states that must later be rendered.
- `minor_ui` binds an owner-approved direct rationale for a mechanical, copy-only or established-
  pattern change without material flow/navigation/composition change; its authority is the Run's
  predeclared Decision Authority.
- `non_visual` records a concrete non-visual rationale. It has no structured screenshot burden.

Before a material Run may enter or remain in visual verification, one existing Review record binds
the exact candidate/source commit, design-reference revision, representative coverage and
digest-identified candidate/baseline images. Every image records its surface, state and viewport.
The Product/UX reviewer names the exact image IDs actually inspected and the available
`browser | image_tool` capability. Missing images, stale candidate binding, missing inspection
capability or an uninspected required image is `not_observed` and blocks completion.
Image references resolve under the existing Run evidence directory at validation time; their
actual raster bytes must exist, be non-symlink files and match the declared SHA-256.

When a design reference exists, comparison covers hierarchy, proportions, composition, density,
whitespace, clipping, consistency and usability without requiring pixel equality. Without a
comparison render, the approved design-creation/deviation decision and an independent critical-
user assessment must be explicit. Document width, geometry, Lighthouse, accessibility or other
proxies retain their narrow claims and cannot substitute for image inspection.

`significant_ui` cannot be downgraded to `minor_ui` or `non_visual`. A `material_user_flow` may be
`non_visual` when its concrete rationale shows that it has no rendered surface; otherwise it may
select material assurance. Material UI uses the corresponding D2 classification, while
`minor_ui` remains a D1 bounded change. The admitted Lead is included among material contributors. The creator/material
contributors cannot be the Product/UX reviewer or the predeclared Decision Authority/Final
Approver. A
non-author signature without the required image basis remains insufficient. A material correction
invalidates only affected candidate images and their review; the next pass uses the existing Run
and Package-2 correction/closure budget. Representative coverage is required, never a universal
page, device, viewport or screenshot quota. Deterministic validation proves structure, identity,
digests and bindings only; visual quality remains agentic judgment.
