# Product-Agnostic Engineering Baseline

> Artifact ID: `AH-SPEC-ENGINEERING-001`
> Artifact class: Harness specification
> Authority: Canonical
> Status: Active
> Semantic owner: Master Harness Engineering
> Version: 0.4.1
> Governing artifacts: `AH-CONSTITUTION-001`, `AH-SPEC-ARTIFACTS-001`, `AH-SPEC-DOMAIN-001`, `AH-SPEC-WORK-001`, `AH-SPEC-INITIALIZATION-001`
> Review: `AH-REV-PROPORTIONATE-EXECUTION-001` (current candidate; disposition in record)
> Owns: Spec-/Contract-First engineering, modular DDD/hexagonal boundaries, Clean Code, coding conventions, Delivery-Slice quality, testing, security, accessibility, migrations, flags, and technical quality

## 1. Baseline And Product Delta

This specification is the reusable engineering floor for every generated product. A selected technology profile makes it concrete for languages, frameworks, cloud, CI, deployment, tools, and numerical thresholds. A Product Technical Delta may confirm or strengthen it; an exception requires the declared authority and MUST NOT silently weaken the Constitution.

Product architecture is driven by user outcomes and domain semantics. Tools and cloud services serve those boundaries; they do not define them.

## 2. Spec-First Structure

Every product maintains distinct canonical layers:

- **Domain Foundation:** Product-wide horizon, Context Map, Context Coverage, stable domain
  identities, review, and exact Human Domain Decision owned by `AH-SPEC-DOMAIN-001`;
- **global product specs:** architecture, quality, testing, security/privacy, data lifecycle, design, delivery, observability, and cost rules that cross domains;
- **bounded-context specs:** language, invariants, commands/queries/events, state transitions, data ownership, failure/denial behavior, and negative boundaries owned by one context;
- **public contract specs:** explicit consumer/provider semantics between contexts or external systems;
- **cross-domain orchestration specs:** multi-context flows whose orchestration has an explicit owner;
- **Work Contracts:** temporary authorized Milestone, Delivery-Slice, Work-Package, Experiment, and Run scope that links but never replaces the owning specs.

Each context has one compact Module Entry Map that leads to its active specs, public contracts, core flows, code, tests, owners, and avoid-mixing boundaries. It MAY combine README and agent-routing responsibilities in one file; larger modules MAY separate them without duplicating meaning. A new agent MUST be able to understand a module and its interactions without scanning the repository.

Unimplemented target behavior remains an approved Target Spec. It becomes active only with the verified implementation transition defined by `AH-SPEC-WORK-001`.

## 3. Modular DDD And Hexagonal Architecture

Every implementation-ready Bounded Context maps to one logical module. The default application
shape is a modular monolith with:

- a thin framework/application shell;
- domain modules aligned to bounded contexts;
- explicit cross-domain orchestration;
- platform adapters for runtime, persistence, identity, messaging, providers, and observability;
- a deliberately small shared-primitives area.

Inside a context, dependencies point inward:

```text
adapters -> application/use cases -> domain
                 ^                    |
                 |------ ports <------|
```

- Domain rules MUST NOT depend on UI frameworks, cloud SDKs, databases, transport types, or concrete providers.
- Ports are defined by the consuming inner layer; adapters implement them.
- Contexts interact only through published contracts, never persistence reach-through or private imports. Several contexts MAY share one physical database or table for cost/operations only when each record/key/schema has one semantic owner, no context reads or writes another owner's data directly, and all interaction crosses a port/contract. Shared storage is never an integration contract.
- Cross-domain orchestration may coordinate but MUST NOT steal the domains' invariants.
- A concept has one semantic owner and one obvious implementation home.
- Shared code is limited to stable, genuinely cross-domain primitives. Similar-looking domain concepts remain separate when their meanings differ.

Tactical DDD patterns are used when they clarify invariants and lifecycle. Entities, aggregates,
repositories, events, value objects, ports, adapters, or empty layer directories MUST NOT be
created ceremonially. Small modules MAY combine files/layers while preserving dependency direction,
public boundary, and testability.

## 4. Contract-First Boundaries

Public Product contracts are finalized only after the Human-approved Domain Foundation establishes
their semantic owners and boundaries. A contract change that moves ownership, an invariant, or a
context relationship returns the affected scope to Domain impact review.

Every public contract defines:

- owner, consumers, version, lifecycle, and compatibility policy;
- command/query/event or protocol schema and semantic meaning;
- authorization, validation, success, denial, error, timeout, and retry behavior;
- idempotency, ordering, concurrency, and consistency guarantees where relevant;
- personal-data classification and logging constraints;
- conformance examples and consumer/provider tests;
- migration, deprecation, and removal conditions.

The port and risk profile select necessary adapter modes; the harness does not require mock, sandbox, and real implementations for every port. Every adapter that exists passes the relevant shared contract-core suite. Critical external integrations require at least a controlled fake and real staging evidence. Sandbox/emulator mode is added only when available and it provides distinct learning or safety value.

Fakes and sandboxes exercise deterministic success, failure, denial, retry, and timeout semantics where supported. Real staging proves only safely triggerable critical provider behavior; provider states that cannot be induced safely or deterministically are recorded `not_observed` and remain covered by the closest controlled mode. A mock cannot prove provider integration.

Breaking public changes require an explicit migration decision. After `live_customer_data`, data/contract evolution follows expand → backfill → validate → switch → contract, with rollback and compatibility evidence.

## 5. Code Quality And Conventions

Code MUST favor clarity at the owning abstraction level:

- names express domain intent and units;
- functions and modules have one coherent responsibility and narrow public surfaces;
- control flow is explicit; errors are typed/classified and never silently swallowed;
- validation occurs at trust boundaries while domain invariants remain enforced inside;
- dependencies are injected through ports; global mutable state is prohibited;
- configuration is typed, validated early, environment-aware, and secret-free in source;
- generated code, migrations, fixtures, and product code are visibly separated;
- Interactive HTML Mockup/design-reference and Technical Risk Experiment paths are permanently separated from Product runtime/import graphs; selected learning enters Product-owned source only as new implementation under an authorized Work Package;
- comments explain non-obvious rationale, not restate syntax;
- duplication is removed only after shared meaning and ownership are proven;
- generic `utils`, catch-all services, god objects, circular dependencies, and speculative abstractions are prohibited.

Reuse existing components, contracts, and primitives before creating alternatives. Reuse MUST NOT cross semantic ownership merely to reduce line count.

Confirmed dead code, unused exports/dependencies, obsolete feature paths, commented-out implementations, expired flags, and superseded adapters inside removed/replaced paths or the affected Work-Package scope are removed in that package. Confirmed unrelated dead code becomes a bounded follow-up rather than hidden scope expansion. Suspected dead code is traced through runtime, reflection, configuration, deployment, and consumers only as far as needed for the concrete deletion decision. “Keep it just in case” is not a retention reason; evidence precedes deletion.

Each technology profile pins formatter, linter, type/static analysis, dependency policy, naming, file/module boundaries, and generated-code treatment. Deterministic conventions are CI-enforced rather than repeatedly debated by agents.

## 6. Risk-Ranked Testing Strategy

Testing proves product rules and integration behavior, not a percentage alone. Choose depth by
impact, blast radius, reversibility and concrete uncertainty, in the existing task understanding;
no scorecard or new document. Investigate uncertainty narrowly before deciding. Stop validation
when required claims are supported; file count and transitive reach alone justify no broad suite.
Use existing focused tests first. T4/D0 need no new test merely to mirror a text edit; the correct
visible result can be enough. Reuse valid evidence and unchanged build artifacts under Work §10.
Risk tiers and decision classes are different views of the same understood impact, not duplicate
assessments. Deep checks belong at actually changed high-risk boundaries.

| Risk tier | Examples | Minimum evidence |
|---|---|---|
| `T1 critical` | authorization; sensitive personal data; data access/export/deletion/disclosure/integrity risk; payments/value; irreversible transitions; destructive action; cross-domain invariant | rule-level unit tests; denial/failure/state tests; contract/integration evidence; critical real-staging flow; security review |
| `T2 high` | primary user outcome, durable data transition, external provider, recovery-sensitive behavior | unit/component behavior; contract or technical integration; relevant staging smoke/E2E |
| `T3 standard` | bounded feature behavior and common UI states | focused unit/component tests plus integration at changed boundary |
| `T4 low` | copy, deterministic mapping, non-behavioral styling | static checks and targeted visual/manual evidence; broader tests only if regression risk warrants |

Required test layers, when applicable:

- **domain unit tests:** every business rule and state transition, including success, failure, denial, and boundary cases;
- **application/use-case tests:** orchestration through ports without concrete infrastructure;
- **UI component behavior:** interaction, state, validation, keyboard/focus, and accessibility semantics;
- **module integration:** real collaboration inside one semantic owner;
- **contract conformance:** producer, consumer, fake, sandbox, and real adapter against shared semantics;
- **technical integration:** persistence, identity, queue, external API, configuration, and IaC boundaries;
- **critical E2E and smoke:** few complete user outcomes on a real deployed environment;
- **visual/accessibility evidence:** approved viewports/states plus automated and human checks;
- **migration/recovery tests:** where lifecycle and data risk require them.

Unit, component, and controlled fake/contract tests MUST be deterministic, isolated, parallel-safe, and use synthetic/minimal data. Real integration and E2E tests instead use controlled fixtures, unique Run data, bounded waits/retries, and classified external transients. A retry never erases the first failure. Flakiness remains visible evidence with owner and correction budget; it is never permanently ignored.

A technology profile MAY define numerical coverage thresholds, but coverage cannot substitute for rule and outcome coverage. Critical invariants are explicitly mapped to test IDs. `T1`–`T3` changes and deterministically automatable behavior require relevant automated evidence. A `T4` change may be technically accepted with its predeclared static, visual, or manual evidence when automation would add no meaningful regression protection.

Work Packages own focused rule, component, contract, and changed-boundary evidence and must be independently reviewable before `slice_ready`. Their parent Delivery Slice owns the exact integrated source, release candidate, complete connected outcome, CDK/IaC behavior, real Staging checks, critical-user review, and cross-package regression evidence. Shared Slice evidence is mapped only to the exact included Package revisions; it never erases a Package failure or makes an untested revision green.

## 7. Security And Privacy Engineering

Security is risk-based and begins in specification:

- identify assets, trust boundaries, actors, abuse cases, data flows, and likely threats;
- apply least privilege and explicit authorization at every protected operation;
- validate and encode at boundaries; parameterize interpreter/database operations;
- encrypt sensitive data in transit and at rest using managed capabilities;
- keep secrets out of source, prompts, logs, screenshots, tests, and evidence;
- pin/lock dependencies, review provenance, scan vulnerabilities and licenses, and produce a dependency inventory/SBOM where supported;
- run static, dependency, secret, and IaC analysis in CI and address findings by risk;
- use synthetic test data; do not copy production personal data into development or agent context;
- inventory personal-data fields with owner, purpose, lawful/product need, retention, deletion, log, analytics, screenshot, and LLM-processing rules;
- ensure logs and evidence are personal-data-free by default and redact unavoidable sensitive context.

Web products map applicable controls to pinned OWASP ASVS 5.0.0 requirement IDs; the risk profile selects depth rather than claiming blanket certification. Security review is mandatory for `T1` behavior and material auth, IAM, data, public-surface, dependency, or trust-boundary change.

### Privileged Product Access Bootstrap

Privileged Product identities are separate from cloud/control-plane operators. When a Product needs Admin or Backoffice access, its Product Technical Delta defines individual roles, server-side allow/deny and tenant/data scope, first-access enrollment, MFA/step-up posture, audit events, offboarding, recovery, and time-bounded break-glass behavior. Hiding navigation or controls is never authorization.

Production MUST NOT contain a default, demo, static, shared, or deployment-generated privileged credential. The first privileged Product user is an individually attributable identity enrolled through a single-use, short-lived provider invitation, a temporary credential with forced replacement, or a security-equivalent passwordless flow. Credential or invitation values MUST NOT enter source, Git, IaC/stack outputs, prompts, Agent context, CI output/configuration, logs, screenshots, tests, or evidence. If a temporary secret is unavoidable, the provider delivers it directly through an approved protected channel; neither an Agent nor the Product repository receives it.

Bootstrap is one-time, idempotent, and auditable: the request binds environment, protected principal reference, role, tenant/scope, expiry, issuer/approver, and recovery owner; identical completed state is a no-op; conflicting or partial state stops for reconciliation; successful enrollment consumes or disables the bootstrap path. Production admins are personal and audit-significant. MFA is required for Production privileged access by default and step-up is required for impersonation, personal-data, money, security, or destructive actions; an exception needs compensating controls, an ADR, explicit Human risk acceptance, and a review/exit trigger.

Staging human personas, Staging automation, Production Product identities, and cloud/control-plane identities remain separate trust boundaries. Recovery and break glass remain individually attributable, strongly authenticated, time-bounded, alerted, reviewed, and revoked after use. These rules do not require a generic Admin UI, identity platform, role taxonomy, or separate milestone where the Product has no corresponding need.

## 8. Accessibility And Performance

Customer-facing web products target WCAG 2.2 Level AA. Automated checks are necessary but insufficient; keyboard, focus order, semantics, zoom/reflow, contrast, announcements, errors, and primary flows receive human or agent-assisted inspection.

Performance requirements are product-specific and expressed as measured user outcomes for named flows, datasets, devices, network conditions, and percentiles. The harness does not invent generic “performance budgets” with no product basis. It requires a reproducible baseline and explicit targets only where performance affects product value, cost, safety, or capacity.

Load and stress tests are activated by expected traffic, concurrency, provider limits, or scaling risk. They are not mandatory ceremony for an unvalidated MVP with no stated load risk.

## 9. Feature Flags And Compatibility

Feature flags are off by default. They are permitted only for:

- a critical kill switch;
- a compatible migration transition;
- an unavoidable, controlled activation of a materially risky capability.

Every allowed flag declares owner, purpose, default per environment, authorization, telemetry, expiry, and a removal Work Package. Flags MUST NOT hide unfinished work, create permanent dual behavior, or replace branch, deployment, or product decisions.

Before external customers, authorized reset, reseed, or forward migration may discard disposable product data. After `live_customer_data`, compatible schema/contract change, backfill, validation, rollback, retention, and deletion evidence are mandatory.

## 10. Quality Review And Simplicity

Every material engineering plan receives two distinct questions:

1. Does it satisfy product rules, contracts, architecture, security, testing, operability, and evidence obligations?
2. What can be removed, deferred, combined, or made more direct without weakening those obligations?

The review rejects both under-engineered shortcuts and abstractions, services, tests, flags, dashboards, or documents that solve no current requirement or demonstrated risk.

## 11. Pinned External Baselines

- [W3C Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/) — target Level AA for customer-facing web products.
- [OWASP Application Security Verification Standard 5.0.0](https://github.com/OWASP/ASVS/tree/v5.0.0_release) — versioned security requirement vocabulary used selectively by risk.
