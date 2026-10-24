# Product Initialization And Rolling Planning

> Artifact ID: `AH-SPEC-INITIALIZATION-001`
> Artifact class: Harness specification
> Authority: Canonical
> Status: Active
> Semantic owner: Master Harness Product System
> Version: 0.6.2
> Governing artifacts: `AH-CONSTITUTION-001`, `AH-SPEC-ARTIFACTS-001`, `AH-SPEC-COLLABORATION-001`, `AH-SPEC-DOMAIN-001`, `AH-SPEC-WORK-001`, `AH-SPEC-PRODUCT-RELEASE-001`
> Review: `AH-REV-1-5-3-REMOVE-ADDED-RULES-001` (acceptance and limits in the referenced Review; prior historical reviews retained)
> Owns: product intake, post-Domain-Gate discovery, MVP, strategic horizons, Delivery-Slice planning, Walking Skeleton, Technical Risk Experiments, rolling planning, initialization outputs, Product Release Policy creation, and Human Initialization Gate

## 1. Entry Contract

Greenfield Product creation has two bounded phases. Safe intake and the `domain_foundation` Run
first produce the exact Human decision required by `AH-SPEC-DOMAIN-001`. Only an effective Domain
Foundation admits the separate `bootstrap_initialization` Run governed here. The two phases may
occur in one Human conversation when evidence is ready, but they retain separate artifacts,
decisions, and authority.

A request only to read, assess or explain the procedure authorizes that answer and minimal source
inspection, not initialization, Foundation/Run creation or modeling. A separately authorized
Domain-only assignment stops at its named Human Gate. Input availability or maturity does not
grant permission for another phase.

Initialization begins in a new product repository with:

- **required:** a Product Requirements Document (PRD);
- **optional:** product-specific Technical Requirements or Architecture Document;
- **optional:** mockups as PNG/JPG/SVG files or an HTML/CSS/JavaScript mockup directory;
- **optional:** brand material, research, data samples, domain references, and explicit human constraints.

A product idea without a PRD starts a discovery pre-step that creates a draft PRD. The Human Product Authority must approve that PRD revision before formal initialization continues.

Optional technical input may repeat, strengthen, contradict, or extend the product-agnostic engineering baseline. Intake preserves it faithfully and classifies every applicable statement. Only the canonical Product Technical Delta avoids duplication by linking confirmations and retaining product-specific strengthening, conflicts, or exceptions. Missing optional technical input means “derive a proposed product delta”, not “ignore non-functional requirements”.

User-provided mockups, HTML, and assets are authorized as Product-work inputs by default, subject to confidentiality, rights, safety, and executable-input inspection. After classification they are provisionally binding for their covered surfaces unless the Human Product Authority explicitly marks a named aspect illustrative; they are not yet approved Product truth. A new Product adopts the covered mockup contract. An existing Product additionally preserves its established shared shell, Design System, global tokens, shared components and cross-page behavior unless an exact global-change outcome authorizes their revision. The team preserves source bytes, records coverage and design anchors, safely renders where permitted, and creates a candidate by adopting the source, consistently filling gaps, or proposing evidenced corrections. General improvement authority and silence never authorize redesign, substitution, omission or semantic reinterpretation. Illegal, unusable, unsafe, license-restricted, materially contradictory, or technically infeasible input may be limited or rejected only with exact evidence, scope, and authority.

## 2. Input Inventory And Classification

Before persistence or agent distribution, Intake classifies confidentiality, personal data, secrets, and usage rights. Repository-safe inputs are preserved as repository-owned immutable snapshots. Secrets MUST NOT enter Git, specifications, prompts, logs, renders, or evidence. Confidential, personal, or license-restricted source remains in an authorized protected store; the repository holds a redacted or synthetic working snapshot plus immutable digest, access-class reference, owner, and retention rule. Data minimization prevents unnecessary replication into agent contexts or evidence.

Every used input must therefore be reproducible as a safe repository snapshot or as another immutable, authorized, durably retrievable content artifact. A digest alone is sufficient only when its exact content remains durably retrievable to authorized reviewers. Directory inputs require a deterministic manifest of relative file paths and per-file digests. Intake records source, date, owner, format, classification, rights, retention, and parsing/render status, then maps each meaningful statement to a requirement ID and classifies uncertainty as:

| Class | Meaning | Required response |
|---|---|---|
| `blocking_missing` | no coherent product can be planned or a dangerous ambiguity exists | stop and ask the human with a recommendation |
| `direction_setting` | alternatives materially change user value, business scope, data, architecture, cost, or irreversibility | present options and obtain a human decision |
| `reversible_assumption` | a safe default can be changed cheaply inside the rolling horizon | proceed with explicit assumption, owner, validation trigger, and fallback |
| `deferred` | not needed for MVP or the current six-week horizon | preserve with rationale and revisit trigger |
| `resolved` | evidence or authority is sufficient | link the owning artifact or decision |

Agents ask the fewest questions needed to prevent material divergence. Questions MUST state why the answer matters and recommend a default. Safe direction-setting questions SHOULD be bundled into one Decision Brief; stop immediately only when continued work is likely to be discarded, unsafe, or materially costly. Silence never resolves `blocking_missing` or `direction_setting` uncertainty.

Reuse named safe inputs and record meaningful gaps/conflicts using Domain §3, without a second
intake report. Existing resolved meaning is referenced, not restated for volume. Immutable
retrieval duties remain intact; ask only real blocking or direction-setting questions.

Absent optional visual input is neither `blocking_missing` nor `direction_setting` by itself. The authorized Initializer creates the bounded Mockup Contract and design-reference candidate from Product evidence and presents them at the existing Human Initialization Gate; an earlier pause requires a concrete conflict, material deviation, likely waste, danger, or material cost.

Contradictory inputs are not silently merged. The team identifies the conflict, applicable authority, user impact, alternatives, and recommended disposition.

## 3. Independent Product Understanding

The pre-Gate Domain review follows `AH-SPEC-DOMAIN-001` and limits UX input to actors, jobs,
outcomes, gross use cases, and material accessibility/experience constraints. It does not finalize
journeys, information architecture, navigation, screens, or flows.

After an effective Foundation exists, the initialization team produces bounded assessments:

- **Product/Analysis:** target users, problem, outcomes, business assumptions, MVP, success signals, and missing decisions;
- **UX/Design:** journeys, information architecture, core flows, states, accessibility, content, and design implications derived from the effective Foundation and use cases;
- **Architecture/Engineering:** public contracts, data, integration, security/privacy, operational feasibility, delivery, and cost within the approved context boundaries.

Each assessment cites input requirement IDs and records counterevidence. The Lead then creates a synthesis, conflict list, and proposed decisions. The Devil's-Advocate/Simplicity perspective tests whether the proposal solves the stated problem with the smallest coherent scope.

Initialization uses Collaboration §§1.1,4–5's version-appropriate team and separate start control.
The exact brief binds Human instruction, Bootstrap State, safe inputs, phase-appropriate effective
Foundation or pre-Gate scope, role-specific questions, evidence and stop conditions. The Spawn
Reviewer does not create or approve Product truth. Compatible Product, UX and Engineering
functions may share one assigned Agent; independent review remains separate from creation.
Do not generate an assessment document or Agent for every function.

Agreement is not presumed from shared context. Material conflicts remain visible through the review and dissent process.

## 4. Required Initialization Outputs

The effective Domain Foundation and Human Domain Decision are prerequisites, not outputs recreated
by this phase. The Initializer produces reviewable, linked revisions of:

1. **Product Brief And Vision Brief:** problem, audience, jobs/outcomes, value proposition, 12–18 month direction, quality principles, non-goals, business assumptions, success measures, risks, and open decisions. Before it exists, the bounded `bootstrap_initialization` team works from the exact Human instruction, effective Foundation decision, and safe PRD/input snapshot digests. Once synthesized, the exact candidate Vision revision becomes mandatory initialization context; after Human Approval, the active Vision is mandatory for every later Agent and Run.
2. **Requirement Register:** every PRD requirement with disposition `mvp`, `later`, `rejected`, or `unresolved`, plus source and rationale.
3. **Actors, Segments, And Use Cases:** actor/role and relevant user-segment descriptions are required; personas are created only when evidence supports differentiating goals or behavior. No invented names, biographies, demographics, or motivations. Otherwise record `personas: not_created` with rationale. Use cases include permissions, preconditions, success, failure, and denial outcomes.
4. **Journeys And Core Flows:** ordered user/system interactions and state transitions linked to requirements and the effective Foundation, including Design §7's proportionate interaction meaning.
5. **Product Technical Delta:** installed Harness ID/version/digest; selected organization and technical profile IDs/versions/digests; each applicable rule classified `conforms`, `strengthens`, or `exception`; product-specific NFRs, data classification, integrations, and compliance/domain needs. Every `exception` links the required ADR and Human Authority.
6. **Product Release Policy:** Product release unit, selected version scheme and grammar, compatibility audience, initial/increment rules, version source of truth, immutable Product tag grammar, candidate/publication semantics, component mapping, migrations, rollback, and release-record evidence as defined by `AH-SPEC-PRODUCT-RELEASE-001`. SemVer is the default; another deterministic scheme requires Product rationale, not a Harness exception.
7. **Foundation Binding And Target Spec Set:** exact effective Foundation/decision, approved context/module routes, global Product Target Specs, public Contract Target Specs, and required Cross-Domain/Orchestration Target Specs. Domain Target Specs are linked from the Foundation rather than recreated.
8. **Architecture Proposal:** simplest deployable topology, key decisions/ADRs, risks, security/privacy posture, delivery path, and idle/usage cost hypothesis.
9. **Design System v0, Mockup Contract, And Interactive HTML Mockup:** as defined by `AH-SPEC-DESIGN-001`. For a customer-facing UI product this records the classified baseline, coverage, design anchors, permitted deltas, bounded creation scope/budget, maintained Product-owned source, and exact rendered PNG evidence. Work is adaptive: create the smallest coherent high-quality design reference when visual input is absent; preserve and consistently extend static input; safely adopt adequate executable input rather than redundantly rebuilding it.
10. **MVP Contract:** target users, core outcome, included/excluded capabilities, measurable success, release constraints, and kill conditions.
11. **Planning Set:** Vision, strategic outcomes, candidate Milestones, detailed six-week plan, two-week checkpoints, Features/Capabilities, Delivery Slices, approved Work Packages, deployment policy, and proposed first Execution Runs. The first implementation Slice is the Walking Skeleton defined below.
12. **Traceability View:** PRD → actor/provisional use case → effective Domain Foundation/context → detailed use case/flow → public contract → MVP/Milestone → Feature/Capability ↔ Delivery Slice → Work Package → acceptance/evidence plan.
13. **Initialization Review Pack:** the exact revisions, independent reviews, findings, dissent, risks, requested human decisions, and approval checklist.

Every Initialization explicitly records `privileged_product_access: applicable | not_applicable | unresolved`, even when the PRD is silent. `not_applicable` names the product reason; `unresolved` becomes `direction_setting` only when it materially changes the MVP, first operable deployment, security, or six-week plan. When applicable, semantic ownership remains separated:

- the Requirement/Product specification owns Product Admin/Backoffice actors, use cases, roles, outcome policy, prohibited Product actions, and their evidence;
- Domain and public Contract specifications own enforceable server-side permission/denial, tenant/data-scope, self-elevation prevention, and audit-event semantics;
- the Design specification owns navigation, screens, first-access/denial/recovery flows, and representative Backoffice outcomes;
- the Product Technical Delta owns only technical identity-provider/environment selection, first personal Admin protected reference, enrollment/expiry, MFA/step-up, identity separation, idempotency/reconciliation, lifecycle/offboarding/recovery/break-glass, and Delivery/Promotion decisions, while linking the semantic owners above.

The planning set maps the existing Delivery Slice/Work Package and Production Promotion dependency that makes access operational, without inventing a dedicated Admin milestone or authorizing a real invitation.

Outputs MAY share a file where ownership remains unambiguous and size stays navigable. The system MUST NOT create one file per list item merely to look complete.

## 5. Foundation-Bound Architecture And Contracts

Domain discovery, Context Coverage, semantic completeness, and Context-to-module rules are owned by
`AH-SPEC-DOMAIN-001`. Initialization verifies that the effective Foundation covers the proposed MVP
and first six-week horizon. Expanding that horizon to an uncovered/new context returns only the
affected scope to the Domain process.

After the Domain Gate, public Contract and Cross-Domain Target Specs define commands, queries,
events, errors, compatibility, authorization, and orchestration at the already approved boundaries.
They MUST NOT silently move an invariant, ownership rule, or aggregate boundary. A discovered
boundary conflict creates a Domain impact proposal before dependent planning continues.

The Architecture Proposal maps each context to one logical module and the pragmatic hexagonal rules
in `AH-SPEC-DOMAIN-001`/`AH-SPEC-ENGINEERING-001`. It is reproducibly bound to the installed Harness
and selected profile IDs, versions, and digests. Deviations require an ADR with alternatives,
Product reason, cost, migration, and the authority required by the profile.

## 6. MVP Selection

The MVP is the smallest coherent end-to-end product that tests the central value proposition safely. It MUST include a complete primary outcome, not only technical foundations or disconnected screens.

Selection considers:

- user value and frequency;
- evidence uncertainty and learning value;
- dependency and integration risk;
- security, privacy, data, and operational obligations;
- design coherence and accessibility;
- implementation and idle/usage cost;
- ability to verify on real staging.

Every excluded capability has a rationale and revisit trigger. “Later” is not approval to prebuild abstractions for hypothetical scope.

## 7. Planning Horizons

Planning fidelity decreases with distance:

| Horizon | Required fidelity |
|---|---|
| 12–18 months | product vision and directional outcomes |
| 12 / 6 / 3 months | strategic outcome hypotheses, dependencies, and decision triggers |
| next 6 weeks | ordered Milestones, Features/Capabilities, Delivery Slices, Work Packages, acceptance, deployment policy, risks, dependencies, and capacity assumptions |
| next 2 weeks | implementation-ready Delivery Slices, executable Work Packages, and proposed Execution Runs |

The initial six-week plan normally contains three two-week checkpoints. A 4–6 week Milestone may span two or three checkpoints. One to two technically acceptable Slices per checkpoint is a planning orientation, not a quota. The plan reserves room for validation and correction rather than assuming perfect first-pass delivery.

The first implementation Delivery Slice is a **Walking Skeleton**: the smallest real end-to-end path that produces observable core user or operator value and proves the necessary delivery route. For a typical web product it includes only the required UI, application/API, Domain behavior, adapter/persistence, tests, CI/CD, CDK, real Staging deployment, and minimum observability. A layer is omitted when genuinely irrelevant and the Slice records why. Infrastructure, login, design tokens, a component library, or a health check alone is not a Walking Skeleton.

The Walking Skeleton is deliberately thin: it proves one central outcome rather than building the full platform, all future abstractions, or a speculative component library. Its Slice Contract and Product Delivery Release Candidate follow `AH-SPEC-WORK-001` and `AH-SPEC-DELIVERY-001`.

A **functional prototype** contains real Product behavior and is never an Initialization artifact. After Human Initialization Approval it is either delivery-intended work inside the first Walking-Skeleton Delivery Slice or a hypothesis-bound, non-promotable Technical Risk Experiment under the lifecycle below. No third prototype lifecycle exists.

### Technical Risk Experiments

A **Technical Risk Experiment** is a time-boxed, non-delivery investigation used only when a material architecture, provider, IAM, migration, performance, or integration uncertainty cannot be resolved safely from existing evidence. Initialization proposes rather than executes it. The separate Experiment Work Contract and Execution Run required by `AH-SPEC-WORK-001` MUST declare:

- one falsifiable hypothesis and the decision it informs;
- strict scope, duration, agent/cost budget, environment, credentials, data class, and permitted side effects;
- isolation, cleanup/TTL, rollback, and stop conditions;
- required observation and how the result changes the Slice/architecture plan;
- `experiment_only` and `non_promotable` status.

An experiment is not routine repository setup, CDK scaffolding, or initial architecture design. It creates evidence, not Product completion. Its source path and resources remain permanently non-promotable and non-importable by Product runtime code. Adoption means digest-identifying selected learning, then copying or reimplementing it in Product-owned source through a later authorized Work Package as new implementation with full ownership, architecture, security, accessibility where applicable, tests, cost, maintainability, and Slice evidence. Experiment reviews or completion evidence do not transfer.

## 8. Rolling Replanning

After every technically accepted Delivery Slice, every material Technical Risk Experiment, each two-week checkpoint, and each Milestone decision, Product/Analysis reviews user/product evidence, UX reviews flow evidence, Architecture/Engineering reviews boundary and operational evidence, and Quality reviews completion truth.

The review decides for each future item: retain, refine, reorder, split, merge, defer, replace, or invalidate. It updates only the detail justified by the current horizon and preserves traceability to the prior plan.

The next two weeks remain implementation-ready and the rolling six-week window is replenished continuously. The team revalidates the next intended Slice before its Run begins and keeps later Slices structured but revisable. Distant Milestones are not decomposed into fixed tasks. A material MVP or Milestone outcome change is Human-gated; a Slice/package reslice that preserves accepted outcomes is a `D2` decision and creates no routine Human Gate.

## 9. Initialization Review Pack

The pack presented to the human MUST be inspectable without reading the whole repository and contains:

- one-page product synthesis and explicit “what we believe” statement;
- requirement disposition and unresolved questions;
- MVP scope, non-goals, success measures, and kill conditions;
- actors/segments, evidence-supported personas if any, use cases, journeys, and screen/flow traceability;
- public contracts, architecture, data/security posture, cost hypothesis, and exact Product Release Policy revision;
- exact effective Domain Foundation revision, Domain Review, Human Domain Decision, covered horizon,
  remaining hypotheses, and any scoped override;
- privileged Product access applicability and, where applicable, exact role/flow/bootstrap/lifecycle plan with protected principal references only;
- Design System v0, Mockup Contract, locally runnable Interactive HTML Mockup/design reference, and rendered multi-screen storyboards where a customer-facing UI applies;
- Vision, 3/6/12-month strategic view, first Milestone, six-week Delivery-Slice plan, Walking Skeleton, deployment policy, and first proposed Runs;
- council findings, dispositions, remaining dissent, assumptions, risks, and overrides;
- exact revisions/digests and the decisions requested from the human.

The pack distinguishes product approval, Product Release Policy approval, design approval, plan approval, profile/exception approval, and permission to begin implementation. The human can approve them together only by explicitly naming each decision.

Every council reviewer begins by restating the target user, central value, primary MVP outcome, and why the proposed plan/design should realize it. A mismatch is a blocking context finding; wording differences without outcome impact are not.

Use Domain §9's decision-oriented explanation for actual Initialization decisions. Distinguish
adopted evidence, new conclusions, open choices and Product consequences from technical appendices.
State the decisions/phase boundaries being approved; Domain completion is not whole Initialization.
Compatible decisions may share a readable brief without merging authority. Reviewer functions
follow Collaboration, not a separate document/Agent allocation per council label.

## 10. Human Initialization Gate

Initialization is `D3 human-gated`. The exact pack revision receives one outcome:

- `approved`: named decisions and first implementation Run may be authorized;
- `approved_with_overrides`: overrides and accepted risks are recorded before activation;
- `changes_requested`: affected artifacts return to revision and independent re-review;
- `rejected`: initialization stops with rationale;
- `paused`: missing external decision or input is named without implying rejection.

No Product implementation or functional prototype may begin before approval. The Interactive HTML Mockup is Initialization design evidence only under `AH-SPEC-DESIGN-001`: it is `design_reference_only`, uses synthetic data, calls no Product backend or cloud resource, stays isolated from Product runtime source, and cannot prove delivery. Initialization may propose a separately `experiment_only` Technical Risk Experiment; it cannot execute one under bootstrap authority. Design-reference and experiment paths remain permanently non-importable and non-promotable. A later authorized Walking-Skeleton Work Package may technically reimplement the digest-bound design reference in Product-owned runtime source under the complete normal review and Slice evidence path, but may not reinterpret its binding observable contract or silently override established Product-wide UI owners. Neither design evidence nor experiment evidence may be presented as implemented, deployed, staging-verified, or delivered functionality.

Initialization approval is invalid when its exact effective Foundation binding is missing, stale,
or does not cover the accepted MVP/first six-week horizon.

The gate decision matrix is explicit:

- the Product Brief, requirement dispositions, MVP, Architecture Proposal, Design System/Interactive HTML Mockup revision, Delivery-Slice plan, and rolling plan MAY become `active`; the already effective Domain Foundation remains bound to its earlier Human decision;
- unimplemented behavior, Domain, Contract, and Cross-Domain revisions remain `approved target` until verified implementation activates them under `AH-SPEC-WORK-001`;
- named first Execution Runs remain `proposed` and may enter Capability Preflight;
- human approval of an exact Run Contract is an authorization prerequisite, not the `authorized` state itself;
- after documented successful Preflight, the Decision Authority may transition the Run to `authorized`; the Run becomes `active` after the applicable direct Contract check;
- the Gate meeting may perform the `authorized` transition only when that exact Run already completed Preflight successfully.

Initialization approval does not freeze the entire roadmap or authorize later Runs, production promotion, live customer data, or Harness mutation.

It also does not authorize a real Production Admin invitation, credential delivery, or privilege assignment. That external action remains bound to the exact Production authority in `AH-SPEC-DELIVERY-001` and may be bundled into the existing Production Promotion decision rather than creating another meeting.
