# Agent Collaboration And Approval

> Artifact ID: `AH-SPEC-COLLABORATION-001`  
> Artifact class: Harness specification  
> Authority: Canonical  
> Status: Active  
> Semantic owner: Master Harness Governance  
> Version: 2.0.2
> Governing artifact: `AH-CONSTITUTION-001`  
> Review: `AH-REV-1-5-1-COMPLETION-DIAGNOSTICS-001` (acceptance and evidence limits in the referenced Review; prior historical reviews retained)
> Owns: role functions, independent review, decision classes, quorum, dissent, reasoning floor, fan-out, and review records

## 1. Principle

The harness coordinates multiple independent perspectives around owned outputs. It MUST NOT simulate teamwork by assigning many role names to one unreviewed line of reasoning.

Roles are functions invoked for a decision or artifact, not permanent personas that must remain active. Each active agent receives a bounded responsibility, required context, expected output, review questions, and stop condition.

The current rules below apply to new assignments under Harness `1.5.0+`. The two-working-Agent topology began in `1.4.0`.
Historical executed Runs retain their pinned topology, quorum and correction limits: before1.4.0,
D2/D3 used Creator plus two independent reviewers and at most two corrections;1.4.x ordinary D1–D3 allowed one correction and D0 was mechanical with no correction. Core replacement
does not rewrite those contracts or weaken their evidence. New activation uses the installed
rules; an old pin is not a way to start current work under obsolete rules.

### 1.1 Agent Start Control

Agent Start Control applies when a `D1`-`D3` Agent actually begins its bounded responsibility. It
MUST NOT require a Run Contract or second Human approval before an Agent performs directly
Human-authorized read-only analysis or prepares that single Contract.

The Lead prepares each Agent's exact operational brief. The brief contains only:

- the bounded objective and authority boundary;
- exact routed artifact/specification/Contract/evidence references;
- expected output and evidence;
- perspective-specific review questions; and
- stop conditions for missing context, evidence, capability, or authority.

The brief distinguishes the requested outcome, observed current state (with sources), assumptions,
and permitted actions. Resolve a consequential contradiction before planning affected work.
Permission to execute only on Staging does not change required cross-environment behavior.
Reviewers begin with the original task and relevant sources, then inspect plan and diff.

The brief references canonical criteria; it MUST NOT copy them into a second checklist or create a
parallel acceptance model. Supplying the whole Harness without routing is not a valid brief.

A lazy, non-author **Spawn Reviewer** MUST inspect the exact brief and routed sources before the
target begins substantive responsibility. The outcome is `pass | changes_required`. Before a Run
exists, that pass permits only read-only analysis and preparation of the single Run Contract. For
implementation or review, the pass and cleared Agent IDs are recorded directly in the current Run
Contract. No separate activation artifact or document digest is created.

A direct Human Task Mandate is sufficient assignment authority when it clearly authorizes the
requested analysis or execution outcome and repository/action boundary. The Lead MAY operationalize
it with canonical defaults and create the required control-plane artifacts without asking for the
same Human approval again. A missing material choice, scope expansion, new external action or
constitutional Human Gate still stops for the owning authority.

An unchanged preparation clearance MAY be reused when authority, target Agent, brief, routed sources,
objective and scope did not materially change. Any material difference requires a fresh Spawn-
Reviewer pass.

The Run declares every planned Agent identity/function and the finite cumulative allocation, but
clearance is checked when that Agent starts. A later reviewer is not cleared before its exact
candidate and evidence exist. Completion requires Contract clearance for every Agent whose
participation is claimed. Exactly one brief carries `Creator /
Implementer`; that Agent MAY also be Lead but MUST differ from every independent reviewer.

The Spawn Reviewer:

- checks whether the target can perform its actual responsibility from the brief, rather than
  accepting the target's self-description or the creator's completion summary;
- may block only missing or contradictory context, boundary, evidence, review lens, capability,
  authority, or stop behavior that can affect the authorized outcome;
- MUST NOT add Product scope, acceptance criteria, finding quotas, style preferences, speculative
  hardening, or generic Harness prose;
- performs no Product/domain work, implementation, artifact acceptance, quorum, finding closure,
  or final approval; and
- terminates after the reviewed brief set is resolved.

The Spawn Reviewer is bootstrapped only from the integrity-verified protected role projection and
mandatory entry chain. It is the sole recursion exception: requiring another Spawn Reviewer for it
would create an infinite regress. It remains a judgment-bearing `xhigh` Agent, consumes one finite
Agent activation, and counts toward concurrent/cumulative Run budgets even though it never counts
toward the creator/reviewer quorum. Its temporary participation fits the declared concurrency
ceiling and ends when the brief check finishes. Its additional activation
must be declared in the derived Run budget before implementation mutation; a pre-`1.2.0` Run needs
an exact Human-approved effort-profile exception.

The cumulative Run allocation counts every planned target Agent plus the lazy Spawn Reviewer.
For1.4.0+ D1–D3 this means three allocated identities by default: Creator, one independent
artifact reviewer, and one separate Spawn Reviewer. At most two working Agents act concurrently;
the temporarily active Spawn Reviewer may bring concurrent identities to three. Reuse the same
Spawn identity for later exact brief checks where available; a replacement still consumes the
cumulative allocation. Its activations and observable cost are reported, never treated as free.
An authorized third working reviewer means four cumulative identities including Spawn, not four
working Agents. Its lazy start check must fit the declared concurrency/activation budget.

`D0 routine` work, deterministic tools, and non-judgment-bearing commands do not activate a Spawn
Reviewer. Routine work needs no Run or N/A start form. The Lead/main Agent is not exempt: its
brief is reviewed before it begins applicable substantive work. A later or replacement Agent
requires a fresh pass. Assignment clearance binds the Agent, responsibility, authority, routed
source responsibilities and stop boundary. In-scope code corrections, updated evidence or clearance
metadata alone do not invalidate it, including on resume. A changed responsibility or authority
does. Artifact approval separately binds the exact relevant candidate revision under §6. Keep
clearance/approval metadata outside the payload it approves; use retrievable source references,
not a second manually maintained brief/role/tree digest list. Core authentication remains intact.

Repository instructions cannot prevent an out-of-band provider invocation. The Harness therefore
claims only that missing or stale Agent-start evidence withholds Harness-valid activation,
continuation, review, acceptance, and completion at the control surfaces it owns.

### 1.2 Retrospective Start-Omission Recovery

A missed start check is a process incident, not proof that every resulting artifact is defective.
For an already completed ordinary Run, the Human MAY authorize a bounded retrospective assessment
under Ordinary Admission §6.1. An assigned non-author reviewer actually examines the original
assignment, routed sources, resulting evidence and consequences of the omission. The reviewer
may reuse unchanged prior artifact-review evidence; only real gaps require correction. The
reviewer records the actual later date, findings/dispositions, residual risk and exact evidence.
This is not a Spawn pass and MUST NOT be backdated or rewrite the original start fields.

The Human accepts the specific residual risk after that assessment. An explicit prior conditional
decision may cover only the already named omission if the assessment finds no additional material
risk; otherwise a new Human decision is required. Missing authority, unperformed checks, unresolved
findings and other Human Gates cannot be healed by the start-omission mechanism. An independent
reviewer may not be the creator, a material contributor, or the original start-only Spawn Reviewer.
The current repair work itself requires normal prospective start clearance and finite authority.

A valid recovery disposes the historical omission without requiring repeat implementation or
invalidating still-current independent evidence. It never authorizes new work. Future Runs and
reactivation require the normal timely Spawn Review; routine use of recovery as a substitute is
forbidden. No new mandatory document, review cycle or hash chain applies to conforming Runs.

## 2. Role Functions

The minimum team capabilities are:

| Function | Primary responsibility | Cannot solely approve |
|---|---|---|
| Lead / Integrator | classifies and coordinates work within an already authorized workflow or Execution Run, maintains coherence, dispositions findings, and assembles the final result | its own material synthesis or implementation; any external, destructive, cost, or production authority |
| Product / Analysis | user problem, value, scope, use cases, MVP, acceptance outcomes, and rolling plan | product artifacts it authored |
| UX / Design | journeys, information architecture, design system, flows, states, accessibility, and mockups | designs it authored |
| Architecture / Engineering | domains, contracts, technical feasibility, simplicity, security, delivery, and integration | architecture or code it authored |
| Implementation specialist | bounded frontend, backend, infrastructure, data, or test implementation | its own implementation completion |
| Quality / Approval | criteria quality, test and evidence sufficiency, regression and completion decision | an artifact it materially co-authored |
| Devil's advocate / Economy | hidden assumptions, excessive complexity, failure modes, cost, and rejected alternatives | final disposition of its own objections |

Product risk MAY activate domain, security, privacy, legal, accessibility, operations, or other specialists. One agent MAY fulfill multiple compatible functions, but it counts as only one independent perspective. The creator and every required independent reviewer MUST be different agents.

## 3. Independent Work Protocol

For every material artifact or decision:

1. Every `D1`–`D3` authorized work contract declares owner, Decision Authority/final approver, decision class, required perspectives, acceptance and anti-criteria, and evidence expected before creation begins. The Lead may operationalize but not invent that authority.
2. The creator produces a traceable proposal without presuming approval.
3. Reviewers first assess independently using perspective-specific questions.
4. Each reviewer records concrete findings with severity, blocking state, affected criteria or evidence, closure condition, and requested disposition. A bare `approved` is insufficient when review scope contains material risk.
5. The creator or Lead resolves each finding as `accepted`, `mitigated`, `rejected-with-rationale`, or `deferred-with-owner-and-trigger`.
6. Reviewers verify the dispositions that affect their finding.
7. The predeclared final approver records the decision, remaining dissent, conditions, and evidence references. The final approver MUST NOT be the creator or a material contributor. For `D3`, the named human gate owner is the final approver.

Shared model lineage or shared context MUST NOT be treated as proof of independence. Independence is strengthened through distinct review questions, separate initial assessments, evidence citations, explicit counterexamples, and visible dissent.

## 4. Decision Classes And Required Review

| Class | Typical examples | Minimum governance |
|---|---|---|
| `D0 routine` | mechanical fixes; explicitly prescribed low-risk reversible copy or appearance changes | task, diff and focused result check; no Run/WP/Slice, Spawn or independent review |
| `D1 bounded` | reversible implementation inside an approved contract | creator plus one independent engineering/quality review; approved Execution Run |
| `D2 material` | Delivery Slice, work package, user flow, module contract, architecture choice, Slice/package split, significant UI | creator plus one independent reviewer covering required Product/UX/Engineering and quality/simplicity lenses; all blocking findings closed; bounded third working Agent only under §4.1 |
| `D3 human-gated` | Domain Foundation or initialization approval, MVP/milestone acceptance, production, customer-data transition, destructive/irreversible/material-cost action, harness evolution | `D2` review plus explicit human approval |

A product profile MAY strengthen review depth and required evidence. For1.4.0+ assignments,
it is not an independent staffing exception: an additional working reviewer still requires §4.1's
concrete trigger, prior authority and finite allocation. Historical pre1.4.0 profile minima retain
their pinned meaning. Profiles MUST NOT weaken constitutional human gates. Review depth is selected
by impact, reversibility, uncertainty, security/privacy exposure, architectural reach and cost—not
by document length.

The three-council unanimous review used to create the master harness is a build-time control for this foundational work. It is not a requirement that every future `D1` change consume three agents.

### 4.1 Mandatory Effort Profiles

Work MUST use the lowest class whose concrete trigger applies. File count, document length, a desire for “premium” quality, available credits, role names, or a reviewer's preference are not escalation triggers.

| Class | Default Agent topology | Review/correction ceiling |
|---|---|---|
| `D0` | one executing Agent; no sub-Agent or independent reviewer | initial implementation plus at most one coherent correction and relevant verification; unknown impact reclassifies |
| `D1` | one Creator plus one independent reviewer; two working Agents, separate temporary Spawn per §1.1 | one initial review; default three technical correction cycles, at most one targeted closure per material correction; Work §10 owns counting |
| `D2` | same two-working-Agent default; required lenses covered by the assigned reviewer | same finite review/correction ceiling as D1; risk changes depth, not automatic headcount |
| `D3` | same two working Agents plus the existing Human Gate and separate Spawn | same finite ceiling; Human feedback does not create unlimited rounds |

Reviewers inspect and challenge; they MUST NOT implement competing solutions for consolidation.
One Agent may cover several compatible functions, but remains one independent voice. A specialist
may cover an existing function without increasing headcount; a new identity consumes allocation.
The task has one authoritative finite technical correction reserve under Work §10. A Mission uses
its approved total, never a fresh default for each Package/Run. Material plan/design/result reviews
remain independent decisions; closure is attached to the actual correction, not another exhaustible
review counter. A tighter existing authorization remains binding.

A third working Agent is exceptional: a critical-risk competence gap the assigned team cannot
cover, or unresolved material evidence-backed dissent after one focused clarification attempt.
Before activation, name the exact question, missing perspective, independent reviewer, scope,
evidence and finite additional review budget in the existing Run. Use an exact preapproved
conditional Human allocation when its trigger holds; otherwise obtain a bounded Human amendment.
A critical label, another role, available credits or a finding alone grants no extra allocation.
This path adds at most one independent working reviewer and one focused assessment; it does not
restart the full review or grant another correction. A fourth working Agent is not part of this
path. If it cannot resolve the issue within authority/budget, checkpoint and escalate to Human.
The separate Spawn Reviewer remains start-only and never substitutes for that specialist.

Replacement, restart, role relabeling and successor Runs do not reset cumulative Agent, review or
correction consumption. Early flow review is a lens within the already budgeted review, not an
extra full review, and unchanged valid findings/evidence are reused. The start control is a
separate bounded brief check, not artifact acceptance or another content-review round.

A unanimous actionable `in_scope_blocking` finding is a correction trigger, not a Human escalation trigger. This remains true when an earlier correction introduced the new in-scope defect. When the finding has a concrete closure condition, the approved user outcome and Mission scope are unchanged, a distinct evidence-backed hypothesis exists, and correction reserve remains, the Lead MUST choose the smallest evidenced `correct | simplify | rollback | reimplement` response, use the next cycle from the single task/Mission reserve and continue without Human interruption. Administrative object changes create neither new authority nor extra reserve. Attempts and failure signatures remain cumulative.

Classification triggers are narrow:

- `D0`: mechanical work or explicitly prescribed reversible low-risk copy/appearance with understood impact. Exclude prices/payments, legal/contract promises, authorization, data/state transitions, public contracts, architecture, interactions, material UI and unknown impact. A one-line business rule is not routine.
- `D1`: reversible work inside one approved package, bounded module/contract, and existing architecture with no material user-flow, security/privacy, data, deployment-authority, or cross-domain decision.
- `D2`: a Delivery Slice; material user flow or significant UI direction; public contract or multi-domain interaction; architecture boundary; security/privacy design; material reslice; or another decision whose independent Product/UX/Engineering perspectives materially change the outcome.
- `D3`: only an existing constitutional Human Gate: Domain Foundation or initialization approval, MVP/milestone acceptance, Production, live-customer-data transition, destructive/irreversible/material-cost action, or Harness evolution.

When no `D2`/`D3` trigger can be named with affected outcome/evidence, the work remains `D1`. Discovery of a real higher trigger pauses affected mutation and proposes a Run amendment. Increasing Agent count is never an autonomous consequence of a reviewer finding; allocating an already authorized correction cycle is permitted only under the preceding reserve rule.

### 4.2 Scope And Review Economy

The active Work/Run Contract is the review boundary. A reviewer may block only a regression caused by the change, a violated applicable rule/criterion, missing evidence for the claimed state, or a credible safety/product failure inside that boundary. Adjacent improvement, pre-existing debt, stylistic preference, speculative hardening, and unrelated cleanup become non-blocking follow-up proposals with an owner/trigger; they MUST NOT expand the current implementation or restart a full review.

Review breadth is not implementation authority. Reviewers label each finding `in_scope_blocking | in_scope_non_blocking | adjacent_follow_up`; only the first two may change the active candidate, and only a violated criterion or credible in-scope failure may block. The Lead rejects a requested change that cannot map to the Scope Lock, even when the change is beneficial in isolation. Expanding the Scope Lock requires its named Decision Authority before another Agent, path family, semantic owner, outcome, or external action is added.

All findings from one review revision are consolidated before correction. The creator performs one coherent correction pass rather than responding serially to reviewers. Closure review is restricted to the changed finding scope unless the correction creates a concrete new regression. Agents MUST NOT reset consumed correction authority by renaming the review, switching role labels, spawning a replacement reviewer, or fragmenting one correction into several messages.

## 5. Approval, Quorum, And Dissent

Quorum means all required perspectives participated, all blocking findings have an explicit disposition, evidence is sufficient for the claimed state, and the authorized approver accepted the result. Counting votes alone is not quorum.

Review outcomes are:

- `approved`;
- `approved_with_conditions`;
- `changes_requested`;
- `rejected`;
- `escalated_to_human`.

Any unresolved blocking finding prevents approval. A non-blocking dissent MAY remain, but MUST be preserved with rationale, risk owner, review trigger, and affected scope. Agents MUST NOT erase dissent to manufacture consensus.

A finding uses `severity: critical | major | minor | observation` and a separate `blocking: true | false`. A finding is blocking when approval would otherwise violate a higher rule, an acceptance or anti-criterion, safety/security/privacy, data integrity, required evidence, or the artifact's declared purpose. The originating reviewer sets the blocking state. The Lead MUST NOT downgrade it unilaterally; disagreement follows the dissent and deadlock path. A human may accept a block only through a valid constitutional override, which becomes the finding's recorded disposition.

`critical` is reserved for a reproducible, evidence-backed violation of an applicable `MUST`,
invariant, acceptance/anti-criterion, safety/security/privacy boundary or data-integrity obligation
that makes the outcome invalid or unsafe. Urgency, preference, adjacent debt or hypothetical risk
alone is not critical. Both working Agents must agree in the default D1–D3 team; with an authorized
third working Agent, at least two must agree, including an independent reviewer. Spawn never votes.
A suspected D0 critical finding forces reclassification and independent review. Without the
applicable agreement, retain the supported lower severity; an independently blocking finding
remains blocking and the Lead cannot downgrade it unilaterally.

Keep related critical findings and hypotheses together in the existing finding record. Critical
recurrence triggers an immediate evidence-led drift/convergence decision: recheck outcome, scope,
benefit, complexity, evidence and remaining authority; choose continue with a new bounded
hypothesis, simplify, roll back, reimplement or checkpoint/escalate. There is no separate numeric
causal-chain correction ceiling. Work §10's single reserve and two-failed-diagnostics decision
apply; an actual unsafe action or missing authority/capability stops immediately.

For a permissible in-scope tradeoff, the two working Agents seek agreement. After one focused
clarification, unresolved material dissent follows §4.1's bounded independent third-reviewer path.
That path may decide a permissible tradeoff by2/3 including an independent reviewer; preserve the
minority rationale, risk owner and review trigger. Votes do not close an evidenced rule violation,
replace the originating reviewer's evidence-based disposition, change the non-author final
approver, or waive a Human Gate. A necessary risk override, unavailable allocation or remaining
deadlock goes to Human with options, evidence, costs and recommendation. Affected/dependent work
stops at the narrowest boundary; unrelated work gains no scope. No forced consensus or endless loop.

## 6. Review Record Contract

Every newly created durable top-level Review record MUST use
`docs/reviews/YYYYMMDD-<harness-semver>-<stable-logical-name>-review.md`. The date is the
record's canonical review date, the SemVer is the exact Harness version being reviewed or,
for a non-release-scoped review, the active Harness version, and the logical name uses
lowercase ASCII words separated by single hyphens. Stable Artifact IDs remain unchanged
when a file moves. Raw artifacts below `docs/reviews/evidence/**` are excluded because their
immutable Run/evidence identities own their paths. Compatible Product Core replacement does
not rename Product-owned historical records; the Master validator enforces the convention on
the migrated Master tree, while the released template governs new Product records.

Every `D2` or `D3` review record MUST include:

- record ID, exact target artifact revision or digest, decision class, date, and status;
- predeclared Decision Authority and final approver;
- creator and material contributors;
- required reviewer functions and actual reviewers;
- acceptance criteria, anti-criteria, and evidence references;
- independent findings with severity, blocking state, affected criterion or evidence, closure condition, and requested change;
- disposition and verification for every finding;
- remaining dissent, conditions, risk owner, and expiry or review trigger;
- final approver and, where required, human approval reference.

`D1` reviews MAY use a compact record but still identify creator, reviewer, evidence, findings, dispositions, and outcome.

Approval is valid only for the exact target revision or digest recorded. Any material correction creates a new revision or digest, invalidates approval for the affected scope, and requires the affected reviewers to review again. A deterministic mechanical change MAY retain approval only when its unchanged meaning and transformation are machine-verifiable and recorded.

## 7. Reasoning And Agent Budget

`high` is the harness minimum reasoning level for every judgment-bearing agent. Constitution, governance, product initialization, material architecture, security/privacy, recovery, and approval SHOULD use `xhigh`. A profile or human MAY raise but MUST NOT lower this minimum.

Deterministic linters, renderers, validators, test runners, and formatters are tools, not lower-reasoning substitute agents.

Concurrency and cumulative identity allocation follow §§1.1/4.1: D0 has one Agent; D1–D3 default
to two working Agents plus the separate temporary Spawn. Track working-role count, actual
concurrency and all allocated identities distinctly in the existing Run, never count role labels
as extra voices. The bounded third-working-Agent path needs prior authority and finite cost.
Multiple Agents MUST NOT duplicate implementation unless deliberate independent evaluation is
the explicitly authorized purpose.

The foundational construction of this master harness has an explicit human-authorized exception: one Lead plus three independent council agents. This exception does not propagate to product execution defaults.

The harness does not claim to meter provider credits precisely. Every Execution Run instead bounds cost through:

- a narrow authorized scope and context route;
- named artifacts and stop boundary;
- maximum active agents and retry policy;
- reasoning floor and any required `xhigh` tasks;
- checkpoints at work-package boundaries;
- a stop when another attempt lacks a new hypothesis or evidence.

Every material Run declares creator/reviewer allocation, maximum concurrency, required initial
reviews, the Work §10 authoritative correction reserve (or its Mission-owner reference), targeted
closure and escalation authority. The concrete finite working bound includes preparation and
initial implementation. Check remaining authority before another Agent or correction. Exhaustion
forbids the next mutation, not verification/closure of the final allowed cycle. No new Run resets
consumption or grants scope. Routine uses its task context and no budget document.

## 8. Collaboration Handoffs

A handoff MUST transfer artifact identifiers and versions, resolved and unresolved findings, relevant decisions, current evidence, exact next action, and stop conditions. Narrative summaries without durable references are insufficient.

For material multi-step work, transfer the existing plan/worklist reference under Work §5.1,
including open original requirements and their evidence gaps. A summary of only the latest
subtask does not replace the full authorized outcome. Reviewers begin closure from those original
requirements and source changes, then seek implementation/evidence, not only the creator's diff.

The receiving agent verifies that referenced artifacts still match the repository state before continuing. If they do not, it records drift and returns to the owning decision rather than silently merging incompatible assumptions.

## 9. Simplicity Guard

KISS applies to every task and phase, including preparation, diagnosis, tooling and review—not
only Product architecture. Choose the smallest sufficient approach that preserves required
correctness, safety and evidence. Activity or tooling volume is not progress; progress closes
the original acceptance criteria. A technical obstacle does not authorize a new infrastructure
project. Broad permission to correct or finish work does not expand its outcome/path/action scope.

Before introducing a container, service, custom runner, framework or replacement execution path,
name the exact unmet criterion, why an existing supported path cannot satisfy it, and the smallest
necessary change. Reuse existing infrastructure when sufficient. New infrastructure outside the
current Scope Lock requires its owning authority before implementation, even if technically
useful. Record that decision briefly in the existing Run/checkpoint; create no extra gate, report
or tracking mechanism. Containers are neither a default nor categorically forbidden.

Reviewer findings apply the same proportionality rule. Reject unnecessary work, not evidence
obligations; a difficult mandatory check remains missing until genuinely observed or changed by
its owning authority. Work§10 governs bounded diagnosis and reuse of still-valid evidence.

Every material plan and architecture review includes both:

- a standards perspective asking whether product, contract, security, quality, and operational obligations are satisfied; and
- a simplicity perspective asking what can be removed, deferred, combined, or implemented more directly without violating those obligations.

Premium quality means the smallest coherent system supported by evidence. It does not mean maximum abstraction, role count, document count, or infrastructure.

Prefer exact Git revisions and retrievable source references when they supply the required identity.
Do not add parallel digest lists, reports, gates or tracking files without a concrete integrity or
authority need. Existing Core/release authentication, external evidence and source/render bindings
remain intact; simplicity does not remove their separately owned controls.

Every non-obvious complexity in a material proposal or finding MUST cite one confirmed requirement, observed failure, or concretely applicable higher obligation, plus its affected user/Product outcome. If two approaches satisfy the same obligations, reviewers prefer the one with fewer concepts, states, dependencies, gates, and user steps. Generic future-proofing, remote hypotheticals, and extreme edge cases without current evidence are omitted or recorded only as non-blocking observations with a concrete activation trigger. They cannot expand scope, block approval, or justify another Agent or review cycle.

## 10. Vision And Critical-User Lens

Every judgment-bearing agent receives and confirms the exact active Product Vision Brief before work. The brief states why the product should exist, target users, primary outcome, value promise, quality principles, current MVP/milestone, non-goals, and success evidence. An agent that cannot explain its artifact's contribution to that outcome stops and repairs context rather than optimizing an isolated task.

The only pre-Vision exception is the bounded Greenfield Domain/Initialization bootstrap in which no
approved Vision or Domain Foundation can yet exist. The first `domain_foundation` Run binds the
exact Human instruction, active Bootstrap State, explicitly named inputs, and safe input digests;
the Foundation, review, and Human Domain Decision are outputs. After that Gate, the separate
`bootstrap_initialization` Run additionally binds the exact effective Foundation and later the
candidate Vision revision. Contract preparation/activation follows `AH-SPEC-WORK-001` and
`AH-SPEC-ORDINARY-ADMISSION-001`; neither Run may require a future output as its own start target.
Only Human Initialization Approval activates the Vision and detailed initialization decisions. No
later work may use this exception.

Every material review evaluates the artifact and, when deploy-relevant, the exact running Delivery Slice on Staging from the perspective of a critical but fair target user. It considers Product Vision contribution, product correctness, end-to-end outcome, usability, flow, information hierarchy, UI/UX consistency, accessibility, trust, perceived quality, latency where relevant, failure/recovery, and unnecessary effort.

A finding MUST name an observable gap or credible scenario, evidence, affected user/product outcome, severity/blocking state, and closure condition. Reviewers do not have a finding quota and MUST NOT invent hypothetical defects to appear critical. Speculation without plausible likelihood or impact is labeled a non-blocking observation or omitted. Devil's advocacy searches for disconfirming evidence, not ceremonial disagreement.

Reviewers also reject unnecessary solution complexity: every added mechanism must pass the evidence-led simplicity invariant, while usability and avoidable user/operator effort are evaluated as product-quality outcomes rather than secondary preferences.

Premium output and efficient output are aligned: use capable agents and strong first-pass specifications to reduce rework. Credit control comes from narrow context, distinct ownership, bounded fan-out, batched reviews, and finite correction cycles—not from lowering the reasoning floor or accepting weak evidence.

After each technically accepted Delivery Slice, Product/Analysis, UX, Architecture/Engineering, and Quality independently revalidate the evidence relevant to their lens and jointly disposition the rolling-plan impact. This is a `D2` agent decision when the accepted MVP and Milestone outcome remain unchanged; it is not a routine Human Gate. A changed accepted outcome, new constitutional risk acceptance, or another existing `D3` trigger is escalated to the Human Product Authority.
