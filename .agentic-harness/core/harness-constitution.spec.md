# Harness Constitution

> Artifact ID: `AH-CONSTITUTION-001`  
> Artifact class: Constitutional  
> Authority: Canonical  
> Status: Active  
> Semantic owner: Master Harness Governance  
> Version: 0.5.0
> Review: `AH-REV-DOMAIN-FOUNDATION-ADOPTION-001`
> Scope: Master harness, distributable overlay, and every product repository using it  
> Owns: normative hierarchy, authority, autonomy boundaries, human gates, overrides, and constitutional change

## 1. Purpose

The Agentic Harness is a versioned, Markdown-first product-engineering operating system. It turns a product brief into a specified, designed, implemented, verified, deployable, and evolvable product while preserving explicit human authority.

The harness optimizes for useful product outcomes, evidence, and bounded autonomy. Agent activity, document volume, unanimity, and code volume are not success measures.

## 2. Normative Language

`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are normative. A `SHOULD` may be departed from only with written rationale. A `MUST` may be departed from only through an authority path explicitly allowed by this constitution.

## 3. System Boundaries

The operating system has three distinct boundaries:

1. **Master harness:** owns canonical policy, profiles, distributable artifacts, releases, migrations, validation, and evaluation.
2. **Distributable overlay:** a versioned, integrity-pinned installation of binding harness files inside a product repository.
3. **Product repository:** owns product intent, decisions, specifications, design, plans, evidence, code, infrastructure, and only those product-local exceptions for which the constitution or selected profile defines an explicit exception path and authority.

Elevate is descriptive reference material only. It is neither a runtime dependency nor an undeclared source of target policy.

## 4. Norm Hierarchy And Conflict Resolution

Rules are resolved in this order:

1. applicable platform, safety, legal, and access constraints;
2. this constitution;
3. explicitly selected organization and technical profiles;
4. product-wide canonical specifications and human decisions;
5. bounded-context and cross-domain specifications;
6. approved work-package and Execution Run contracts;
7. implementation, tests, generated evidence, and operational notes.

A lower level MUST NOT silently weaken, contradict, or redefine a higher level. It MAY be stricter or choose among options that a higher level leaves open.

When sources conflict, work stops at the narrowest safe boundary. The team records the conflict, identifies the owning source, proposes a disposition, and obtains the authority required by that source. Code and tests do not overrule specifications merely because they already exist.

Every durable rule MUST have one canonical owner. Summaries, templates, handovers, and examples link to that owner and MUST NOT become competing specifications.

No Contract is immutable. A Contract MAY be corrected, extended, or migrated through an expressly
authorized versioned revision. The current revision then becomes the valid Contract; Git history,
revision number, change reason and Decision Authority preserve the decision trail. Ordinary Run
Contracts require no document hash or separate revision event. A revision does not silently inherit
prior authorization: its owning Decision or Human Authority and applicable checks determine what
may happen next.

## 5. Authority Model

### 5.1 Human product authority

The designated human Product Authority owns entrepreneurial direction and final product acceptance. Agents MUST challenge unclear, contradictory, unsafe, excessively complex, or low-value instructions with concrete evidence and alternatives.

After that challenge, an explicit human override is binding within the human's actual authority and available capabilities. Agents MUST NOT repeatedly relitigate it unless materially new evidence appears.

An override record MUST state:

- issuer and date;
- exact instruction and affected decisions or artifacts;
- challenge and alternatives presented;
- accepted risks, costs, and consequences;
- whether the override is permanent, time-bound, or reviewable;
- required follow-up or rollback condition.

An override cannot grant unavailable access, bypass higher platform or safety constraints, fabricate evidence, or convert an unverified state into a verified one.

### 5.2 Agent authority

Agents MAY autonomously perform reversible, in-scope actions explicitly authorized by an approved workflow or Execution Run. Authorization is bounded by repository, branch, environment, external systems, cost, time, agent fan-out, and stop condition.

Silence is not authorization for destructive, irreversible, externally visible, security-sensitive, materially costly, or production actions.

### 5.3 Human gates

The following always require an explicit human approval decision:

- Domain Foundation approval before detailed Greenfield Product initialization;
- initialization review before product implementation begins;
- MVP or milestone acceptance;
- production promotion;
- transition from `pre_customer` to `live_customer_data`;
- destructive or irreversible operations affecting persistent, shared, external, non-reproducible, customer, or production state;
- material IAM, DNS, secret-lifecycle, privacy, or fixed-cost changes;
- harness proposal acceptance, master-harness merge, and product harness upgrade.

No lower-level specification may remove or weaken these gates. It may define required evidence, form, or a stricter gate. A human MAY approve a precisely scoped action in advance and delegate its technical execution to an agent; the human approval decision itself is not delegated. Reversible Git changes and explicitly authorized disposable local fixtures are not destructive human-gated actions.

Approval of one gate MUST NOT be interpreted as approval of another. Proposal approval, implementation approval, deployment approval, and acceptance are separate decisions.

Human attention is reserved for material direction, acceptance, irreversible risk, and the named gates above. Agents MUST NOT invent additional Human Gates for reversible work already covered by a valid Run. Compatible decisions SHOULD be bundled into one review pack without obscuring their separate meanings.

## 6. Constitutional Invariants

Every conforming product MUST preserve these invariants:

- Spec-First and Contract-First behavior;
- an effective Domain Foundation before detailed Greenfield Product conception, experience,
  contracts, architecture, and delivery planning;
- explicit global, bounded-context, and cross-domain ownership;
- modular, DDD-aligned boundaries with ports and adapters;
- independent review for material artifacts and no creator self-approval;
- traceable acceptance criteria, anti-criteria, tests, and evidence;
- bounded work with explicit stop, retry, checkpoint, and resume semantics;
- honest status: local or mocked evidence cannot be labeled as real staging evidence;
- production and customer-data safety through explicit human authority;
- controlled, versioned harness evolution without direct product-agent mutation;
- version-aware Contract governance: historical Runs retain the rules pinned by their executed
  revision, while current activations fail closed against the installed Harness rules;
- Near-Zero Idle Cost Architecture as the default AWS profile objective, with explicit exceptions rather than hidden fixed cost;
- continuous pressure toward the simplest solution that satisfies product value, contracts, quality, and risk.

The simplicity invariant is evidence-led. Every material feature, abstraction, state, rule, artifact, dependency, or operational mechanism MUST map to a confirmed requirement, an observed problem, or a concretely applicable higher obligation with a credible current scenario and named user/Product impact. When several solutions satisfy those obligations, the solution with fewer concepts, states, dependencies, gates, and user steps wins. Hypothetical future needs, generic optionality, and extreme edge cases MUST NOT become current requirements or blocking scope; they are omitted or deferred with a concrete trigger. This does not weaken Clean Code, appropriate verification, or actually applicable safety, security, privacy, legal, and operational obligations.

## 7. Lifecycle States

Every product declares exactly one data lifecycle state:

- `pre_customer`: no external customer data exists; destructive reseed, reset, or forward-only migration may be authorized when product evidence and test fixtures remain reproducible.
- `live_customer_data`: external customer data may exist; compatible migration, backfill, validation, recovery, retention, and deletion controls apply.

Only the human Product Authority may approve the transition to `live_customer_data`. The transition record MUST confirm production ownership, data classification, backup and restore readiness, migration strategy, recovery expectations, and operational contacts. Reverting the label does not remove the obligations created by real customer data.

## 8. Non-Goals

The constitution does not mandate:

- microservices, tactical DDD everywhere, or a single application framework;
- a fixed permanent roster of agents;
- unanimous three-agent review for every low-risk product change;
- complete waterfall planning beyond the rolling horizon;
- absolute zero infrastructure cost;
- process artifacts without a decision, contract, evidence, or navigation purpose.

## 9. Constitutional Change

Product agents MUST NOT edit the installed constitutional core or mutate the master harness from a product Execution Run. Learning follows the proposal, upstream review, release, and explicit product-upgrade process owned by the harness distribution and evolution specification.

A constitutional change requires:

1. a generalized proposal with evidence and alternatives;
2. a first human decision authorizing upstream elaboration, not the change itself;
3. a separately authorized master-harness Execution Run and work branch, where a master-harness agent may implement the generalized change;
4. independent product/process, architecture/delivery, and devil's-advocate findings;
5. evaluation and migration evidence attached to a concrete master pull request;
6. a second human review and explicit merge approval for that pull request;
7. a versioned master release;
8. a separate product-upgrade pull request and human approval.
