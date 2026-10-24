# Domain Modeling And Bounded-Context Architecture

> Artifact ID: `AH-SPEC-DOMAIN-001`  
> Artifact class: Harness specification  
> Authority: Canonical  
> Status: Active  
> Semantic owner: Master Harness Domain Architecture  
> Version: 1.1.1
> Governing artifacts: `AH-CONSTITUTION-001`, `AH-SPEC-ARTIFACTS-001`, `AH-SPEC-COLLABORATION-001`, `AH-SPEC-WORK-001`  
> Review: baseline `AH-REV-DOMAIN-FOUNDATION-ADOPTION-001`; integration candidate `AH-RUN-CONSOLIDATED-CORRECTIONS-S3-S4-001`
> Owns: Domain Foundation phases, semantic completeness, First-Class Product Objects, Context Coverage, Human Domain Decision, domain invalidation, and Bounded-Context-to-module architecture

## 1. Purpose And Applicability

The Domain Foundation establishes the smallest coherent semantic model needed before a team fixes
detailed Product scope, experience, contracts, architecture, data shape, or delivery work. Its
purpose is better decisions and fewer contradictions, not maximum modeling volume.

Every newly initialized Product MUST complete this specification for the contexts required by its
MVP and first six-week horizon. A Product MAY model farther contexts directionally, but MUST label
them as hypotheses rather than implementation-ready truth.

An existing Product adopts this model incrementally under Section 11. Installing or upgrading the
Harness MUST NOT by itself make existing Product-owned artifacts invalid, rewrite them, or block
unrelated legacy work.

This specification owns Domain semantics and applicability. Initialization owns the enclosing
Product process, Engineering owns implementation quality, Design owns experience artifacts, Work
owns execution, Collaboration owns Agent topology/quorum, and Distribution owns installation and
upgrade mechanics. Those specifications link here and MUST NOT restate a competing Domain model.

## 2. Definitions

- **Domain Foundation:** the Product-wide index, Context Map, in-scope Domain Target Specs, bound
  diagrams, traceability, findings, and exact Human Domain Decision for one revision and horizon.
- **Bounded Context:** a semantic boundary with its own language, invariants, ownership, model, and
  explicit public interaction surface.
- **Context Coverage:** the recorded modeling state of one discovered context under Section 11.
- **Domain Target Spec:** the candidate Product specification for one context. It becomes active
  only under the applicable acceptance lifecycle.
- **First-Class Product Object:** a deliberately selected domain object with stable identity,
  user/operator-relevant lifecycle, independently addressable tasks, and independent permission or
  management decisions.
- **Domain horizon:** the named MVP and rolling-plan scope whose contexts require sufficient detail.
- **Effective Foundation:** the exact Foundation revision approved by the Human Domain Decision for
  its named horizon, with no fundamental unresolved decision inside that coverage.

First-Class status does not imply Aggregate Root, database table, API resource, route, navigation
item, page, service, deployment unit, or team ownership. Each of those remains a separate decision.

## 3. Sequence And Pre-Gate Boundary

The required Greenfield order is:

```text
safe intake
  -> provisional Product scope
  -> C1 Domain Framing
  -> C2 Structural Model
  -> C3 Behavioral And Impact Model
  -> independent Domain review
  -> Human Domain Decision
  -> detailed MVP, contracts, architecture, data, IA/navigation/routing,
     design/mockup, six-week Slice/Package/Run planning
  -> Human Initialization Gate
  -> Product implementation
```

Before the Human Domain Decision, authorized Agents MAY:

- classify requirements, uncertainty, actors, and gross use cases;
- establish a provisional Product scope and domain horizon;
- perform C1-C3 discovery;
- inspect existing technology and inputs read-only for concrete feasibility or risk; and
- prepare the Domain Foundation, its review, and the Human decision request.

They MUST NOT finalize or begin:

- the MVP Contract or detailed delivery plan;
- Delivery Slices, implementation Work Packages, or Product-delivery Runs;
- information architecture, navigation, routing, screens, detailed flows, or mockups;
- database schemas, public API/event contracts, or irreversible architecture commitments; or
- Product implementation or a prototype intended to become deliverable code.

A provisional use case describes actor, desired outcome, and gross success/failure boundary only.
Detailed interaction, contract, and delivery decisions wait for the effective Foundation.

An earlier Human question is permitted only when a concrete direction-setting uncertainty makes
continued modeling likely to be discarded, unsafe, or materially costly. It is not a second
mandatory Domain Gate.

Within an authorized Domain assignment, compare named safe inputs to C1–C3 before producing
more model content. In the existing Foundation/index identify sufficiently evidenced, conflicting
and missing meanings; retrievable references and brief reasons suffice. This is not a new coverage
lifecycle, mandatory matrix, intake gate or document. A manifest proves retrieval/integrity, not
semantic completeness or approval.

Adopt sufficient meaning by exact source reference with clear ownership. Reconciliation or new
modeling MUST name the concrete gap, contradiction or necessary consolidation it resolves. Do not
rewrite rich PRDs or generate files/diagrams to fill templates. Thin/conflicting input still needs
all relevant C1–C3 decisions; cost cannot justify silently choosing a direction-setting Domain rule.
Reuse never makes a Foundation effective without its exact Human Domain Decision.

## 4. C1 — Domain Framing

C1 records:

- Ubiquitous Language terms, definitions, synonyms to reject, and context-specific meanings;
- actors, accounts, memberships, roles, and external systems;
- ownership and tenant candidates;
- core jobs, outcomes, business processes, and gross use cases;
- candidate Bounded Contexts with evidence and rejected alternatives;
- candidate First-Class Product Objects; and
- confirmed requirements, derived hypotheses, blocking uncertainties, and direction decisions as
  visibly different classes.

Context candidates follow language, invariants, ownership, lifecycle, permissions, change reasons,
and integration needs. A screen, route, table, framework package, organizational chart, or desired
microservice split is not sufficient evidence for a context.

## 5. C2 — Structural Model

For every in-horizon context, C2 records:

- stable IDs and names for Aggregate Roots, Entities, Value Objects, Domain Services where
  justified, and relevant external concepts;
- responsibility and semantic owner for every element;
- relationships with direction and explicit cardinality;
- aggregate and transaction consistency boundaries;
- ownership, tenant, visibility, and data-scope rules;
- invariants and prohibited states;
- negative boundaries stating what the context and each public contract do not own; and
- Context Map relationships, translation/anti-corruption needs, and public interaction direction.

A list of nouns or entity/table diagram is insufficient. Every material element and relationship
MUST trace to a requirement, use case, or explicit hypothesis.

## 6. C3 — Behavioral And Impact Model

For every in-horizon context, C3 records:

- lifecycle states, valid transitions, initiators, guards, effects, and prohibited transitions;
- role/permission decisions including denial behavior and tenant/data scope;
- core commands, queries, decisions, and use cases per relevant object/context;
- positive, negative, and boundary scenarios;
- cross-context orchestration without leaking internal models;
- final First-Class Product Object decisions and rejected candidates;
- consequences for later MVP, contracts, architecture, persistence, security/privacy, UX, planning,
  migration, and evidence; and
- remaining non-fundamental hypotheses with owner and resolution trigger.

One object need not have a lifecycle when the domain evidence does not support one. Recording
`not_applicable` with a domain reason is preferable to inventing states.

## 7. Artifact, Identity, Diagram, And Trace Contract

The Foundation contains:

1. one Product-wide Foundation/index with horizon, contexts, Context Coverage, revision, and links;
2. one Domain Target Spec per in-horizon context;
3. one Context Map;
4. maintained local diagram source using Mermaid by default or another deterministic format;
5. deterministic rendered views with generator identity and source/revision binding; and
6. one Domain Foundation Review Pack binding exact candidate revision, findings, dispositions,
   dissent, decision request, and Human decision.

Small Products MAY combine these concerns in fewer files or views when semantic ownership remains
clear. They MUST NOT create one file per checklist item or omit a duty to reduce document count.

Sufficient source material may fulfill these concerns by reference within existing owners;
duplication is not required. Preserve provenance, confidentiality and authority classification.
Adoption into Product truth remains an explicit reviewed decision, not a presumption that supplied
statements are authoritative. Existing exact candidate/review and source/render bindings apply;
no parallel digest inventory is added.

Textual definitions and diagrams use the same stable IDs. Product specifications own semantics;
diagrams are generated/bound structural views. A changed diagram source invalidates its prior
render. A render without its source/generator identity cannot support approval.

Every context, model element, relationship, cardinality, invariant, lifecycle, permission, use case,
and First-Class decision traces to at least one confirmed requirement/use case or explicitly owned
hypothesis. Traceability is navigable without a repository-wide scan.

## 8. Semantic Completeness And Review

Deterministic tools MAY prove required fields, stable identity, reference integrity, coverage,
traceability, revision matching, source/render binding, decision presence, and absence of forbidden
downstream artifacts before the Gate. They MUST NOT claim semantic correctness from field presence,
word counts, diagram size, or keyword matching.

Independent review evaluates the exact candidate for:

- fidelity to Product evidence and Ubiquitous Language;
- missing or falsely split/combined contexts;
- aggregate, ownership, tenant, cardinality, invariant, permission, and lifecycle consistency;
- usefulness of First-Class decisions for real user/operator work;
- cross-context leakage and contract direction;
- under-modeling that leaves downstream decisions arbitrary;
- over-modeling, speculative abstraction, and ceremonial architecture; and
- the smallest model sufficient for the named horizon.

There is no finding quota. A clean `approved` recommendation is valid when evidence is strong.
Review functions and quorum follow `AH-SPEC-COLLABORATION-001`; this specification does not set an
Agent count.

Review tests faithful reuse, whether every new element resolves an actual gap, and §9's readable
decision brief. Reject both under-modeling and needless re-authoring. Document count and agreement
alone prove neither quality nor usability.

New1.4.0+ Domain Review blocks retain schema1 and add `harness_version`, the exact creating
Harness version, to select Collaboration's review count. One independent reviewer is the default;
two may participate only under its bounded escalation; a stricter profile alone grants no additional
working-Agent allocation. The owning Run
records exact allocation/start authority; this Review field creates none. Existing blocks without
that field retain their historical two-reviewer minimum; an explicit pre1.4.0 pin also retains it.
Core upgrade never inserts a new pin into old evidence. Direct and full checks apply the same
version-selected count and exact Human/candidate guards. Review identity/revision and authority
must genuinely change before its quorum changes; a new label does not reapprove an old candidate.

## 9. Human Domain Decision, Effectiveness, And Invalidation

The Human-facing summary MUST explain in ordinary Product language what was adopted, what was
newly learned, the exact decision needed, real alternatives and their Product consequences, and
the recommendation with its uncertainty. Put technical IDs, digests and exhaustive evidence in
linked detail, not the main explanation. If no modeling choice remains, say so and request approval
of the exact Foundation; invent no options or questions to make the Gate look substantive.
A Human report that the brief is incomprehensible requires clarifying it before treating the
response as informed. No quiz, extra gate or Agent assertion proves Human understanding.

At the waiting point identify the Domain phase, candidate revision, remaining Human decision and
stop before Bootstrap Initialization/Product implementation. The Run may be `verification` while
the Human decision is `pending` and the Foundation ineffective: different objects' states, not
another shared status. Resume rechecks candidate and authority; stale approval grants no new work.

The Human Domain Decision is a `D3` gate with outcomes:

```text
approved
approved_with_overrides
changes_requested
paused
rejected
```

`approved` and `approved_with_overrides` name the exact Foundation revision, horizon, covered
contexts, review record, remaining hypotheses, and decision owner. An override additionally names
the exact affected decision, challenge/alternatives, accepted risk, owner, expiry/review trigger,
and affected downstream scope.

Only those two outcomes make the named revision `domain_model_effective`. Other outcomes block only
the affected Domain and dependent downstream work. They do not authorize detailed initialization.

The following changes require a Domain impact proposal before dependent work continues:

- adding/removing a Bounded Context or core Entity;
- changing an aggregate boundary, ownership/tenant rule, relationship cardinality, invariant,
  role/permission, lifecycle, or First-Class decision; or
- changing a cross-context responsibility or public interaction direction.

The impact classifies each dependent as `unchanged`, `update_required`, `re_review_required`,
`invalidated`, or `superseded`. Only affected and dependent work stops. Reapproval binds the new
exact revision; unrelated effective contexts remain usable.

## 10. Bounded Context To Module Architecture

Every implementation-ready Bounded Context maps to one logical module and one Module Entry Map. A
logical module is a semantic/code dependency boundary, not automatically a repository, workspace,
process, service, deployment unit, database, or team.

The default deployable is the simplest coherent shape, normally a modular monolith. Splitting a
service/deployment requires concrete independent scaling, isolation, ownership, regulatory,
availability, or release evidence that outweighs operational cost.

Within a context module:

- Domain code is independent of framework and infrastructure concerns;
- Application code orchestrates use cases and domain transactions;
- inbound/outbound ports exist only at real replaceable or cross-boundary seams;
- adapters implement those real seams;
- the context exposes only an explicit public contract; and
- other contexts use that contract or explicit cross-domain orchestration, never internal domain or
  persistence types.

Empty layer directories, one-interface-per-class patterns, generic repositories, or adapters around
non-boundaries are prohibited ceremony. A small context MAY combine files/layers while preserving
dependency direction and testability. Shared primitives remain minimal, stable, and semantically
neutral; shared domain behavior belongs to an explicit owner instead.

Persistence models do not define the domain. Later IA/navigation/routing follows user tasks, use
cases, and the effective Foundation; it does not mirror Aggregates mechanically.

## 11. Existing Products And Context Coverage

Brownfield adoption records every discovered in-scope context as exactly one of:

- `legacy_unmodeled`: known context without an effective Foundation;
- `partially_modeled`: a bounded model exists but one or more required C1-C3/review/decision duties
  remain incomplete; or
- `domain_model_effective`: an exact Human-approved Foundation revision covers the context.

Adoption is incomplete until discovered in-scope contexts are classified. It does not need extra
`unassessed` or `candidate` states: incomplete adoption already represents that condition.

Rules are a progressive ratchet:

- a new context MUST complete the strict Domain Foundation path;
- unrelated unchanged legacy work is not globally blocked;
- a material change inside `legacy_unmodeled` or uncovered `partially_modeled` scope first models
  the exact affected scope or obtains an exact Human Legacy Exception; and
- effective contexts follow normal impact/reapproval.

A Legacy Exception names context/scope, exact change, reason, alternatives, accepted semantic risk,
owner, expiry/review trigger, affected Runs, and why modeling first is disproportionate. It cannot
cover the whole repository, future unknown work, a new context, or silent bypass.

Installing/upgrading protected Core is not adoption. Brownfield adoption becomes active only after
the separately authorized root/routing integration and Context Coverage are present and verified.
Staged Core alone MUST be reported as incomplete/inactive and may be rolled back without Product
file loss.

## 12. Run Binding And Enforcement

The first `domain_foundation` Run is a controlled pre-Vision Run. Its initial Contract targets only
pre-existing authority and inputs: exact Human mandate, active Bootstrap State, safe input
identities/digests, and the owning bootstrap/domain Work Contract. The Foundation, review, and Human
decision are outputs and cannot be required as start inputs.

After the Gate, detailed initialization targets the exact effective Foundation and Human decision.
Product-delivery Runs bind each affected Context to its exact effective Foundation and Human
decision, or the exact covering model/Legacy Exception for changed legacy scope.

For new Harness `1.4.1+` Product-delivery Runs, a wholly domain-free Work Package MAY instead use
one schema1 Domain Binding with exactly `schema_version`, `contexts: []`, and a nonempty string
`not_applicable_reason`. The reason explains why the entire authorized Package affects no Bounded
Context and cites its effective scope/context decision through existing Package sources and exact
Run targets. A shared design-system component library can qualify when its approved scope excludes
domain behavior; its name or directory alone does not establish that fact.

Without `not_applicable_reason`, the existing nonempty Context Binding remains unchanged. Combining
the field with nonempty contexts, omitting the Binding, or providing an empty/non-string reason is
invalid. Unknown or unassessed impact is not non-applicability. Mixed scope binds every affected
Context and cannot use the domain-free variant. No dummy Context, Foundation, Legacy Exception,
Brownfield adoption, extra applicability document or new Human Gate is required for domain-free
work. Existing initialization, authority, design, review and Slice evidence duties still apply.

The assigned independent reviewer verifies the reason against the named sources, scope and actual
change. Structural validation checks the declared variant, not the semantic truth of prose. If
domain impact emerges, revise the Package/Run and satisfy the affected Context bindings before that
mutation. Historical Runs retain their pinned rules; Core replacement does not rewrite their
Bindings. Current start/resume uses the installed version and an authorized current revision.

Direct Run checking reads only the Contract, exact named targets, and installed release metadata.
It does not enumerate repository health or validate unrelated Domain artifacts. Full structural
Domain validation remains a separate repository validation/release/adoption operation.

## 13. Acceptance And Anti-Criteria

Accept this model only when Greenfield sequencing is fail-closed, Brownfield adoption is safe and
incremental, semantic review remains human/Agent judgment, exact-source admission remains narrow,
and module rules are useful without architecture ceremony.

Reject noun-only models, implicit cardinality/ownership/tenancy, missing denial/lifecycle behavior
where applicable, self-approval, stale decision/render binding, global legacy exceptions, automatic
Product-file mutation, Aggregate-to-page/service mapping, duplicated semantic ownership, and any
claim that deterministic structure proves Domain quality.
