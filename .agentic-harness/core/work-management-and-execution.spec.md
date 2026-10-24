# Work Management And Execution

> Artifact ID: `AH-SPEC-WORK-001`
> Artifact class: Harness specification
> Authority: Canonical
> Status: Active
> Semantic owner: Master Harness Delivery
> Version: 2.0.4
> Governing artifacts: `AH-CONSTITUTION-001`, `AH-SPEC-ARTIFACTS-001`, `AH-SPEC-COLLABORATION-001`, `AH-SPEC-DOMAIN-001`
> Review: `AH-REV-1-5-3-REMOVE-ADDED-RULES-001` (acceptance and limits in the referenced Review; prior historical reviews retained)
> Owns: work hierarchy, Mission envelopes, Delivery Slices, package contracts, Execution Runs, capability preflight, status, retry, stop, checkpoint, resume, replanning, and completion claims

## 1. Work Hierarchy

For new Harness1.5 work, D0 routine under Collaboration §4 needs only the existing task, diff and
focused result evidence. It creates no Run, Package, Slice, Domain Binding, Spawn, review or
percentage/task-controls form. It can use authorized Delivery §2.2 without synthetic hierarchy.
No new test is mandatory when existing static/manual/visual/automated evidence suffices. A task
reference, finite working bound, at most one correction and actual external-action authority remain.
Unknown impact is resolved narrowly or reclassified; it is not an exemption.

Material Product work is organized as:

```text
Effective Domain Foundation (current horizon)
  -> Vision (12–18 months)
    -> Strategic outcomes (approximately 3 / 6 / 12 months)
      -> Milestone (normally 4–6 weeks or 2–3 sprints)
        -> Delivery Slice
          -> Work Package
            -> Task

Feature / Capability <-> one or more Delivery Slices
```

- The **Domain Foundation** is the semantic prerequisite and coverage boundary for detailed Product
  work; it is not another backlog level or a decomposition into pages/services.
- The **Vision** is directional and outcome-oriented, not a promised backlog.
- **Strategic outcomes** express measurable product or business movement and may change with evidence.
- A **Milestone** is a coherent, human-reviewable product increment composed of mutually compatible Delivery Slices.
- A **Feature / Capability** describes product scope and a recognizable user or operational ability. It is not execution authority and may be delivered across multiple Slices; one Slice may advance compatible parts of several Features when its outcome remains coherent.
- A **Delivery Slice** is the smallest coherent vertical unit that normally becomes one immutable release candidate, one CDK-backed Staging deployment, and one technical-acceptance decision. It produces an observable user or operator outcome through every actually affected layer.
- A **Work Package** is the smallest independently specifiable, implementable, reviewable, and checkpointable change. It may be technical or layer-specific when its parent Slice remains vertical. One Work Package MAY constitute the entire Slice.
- A **Task** is an execution detail and MUST NOT carry product scope that is absent from its parent package.

“Functional prototype” is not a separate work type. Real Product behavior intended for delivery belongs to a Delivery Slice and normally begins with the Walking Skeleton. Throwaway behavior created only to answer one material uncertainty belongs to a Technical Risk Experiment with `experiment_only`/`non_promotable` source, evidence, cleanup, and stop semantics. An Initialization Interactive HTML Mockup is design evidence and belongs to neither lifecycle.

Detailed planning covers the next six weeks, with two-week checkpoints. More distant items remain hypotheses at lower fidelity. Completion or invalidation of a checkpoint triggers refinement of the next horizon; it does not trigger blind continuation of an obsolete plan.

### 1.1 Mission Envelope

A **Mission** is an optional authorization envelope embedded in one existing Execution Run Contract. It is not a new artifact class, hierarchy level, backlog, or substitute for a Milestone, Delivery Slice, Work Package, Technical Risk Experiment, Run, or Human Gate. It exists only when one Human decision intentionally authorizes a coherent ordered multi-package outcome.

The Execution Run Contract is the canonical Mission owner and MUST bind:

- stable `mission_id`, exact Human request/decision reference, active Vision revision where applicable, and Mission Decision Authority;
- required outcomes with observable completion evidence, invariants that remain true, explicit non-goals, prohibited outcomes, integration boundary, and final stop;
- either an exact ordered Package/Slice/Experiment sequence or bounded package-instantiation rules naming allowed outcome IDs, semantic owners, path families, environments, external actions, dependencies, decision class ceiling, and maximum item count;
- decisions delegated to the Lead, the non-Human authority allowed to approve an in-Mission Package Contract, and decisions reserved for an existing Decision or Human Authority;
- finite Mission-total technical correction reserve, working window covering preparation/first implementation, Agent allocation, external-action and observable cost bounds; sub-Run/Package correction fields reference the same remaining reserve, not independent limits;
- package-boundary checkpoints, continuation evidence, next-item selection rule, and stop/escalation conditions.

An existing Delivery Slice, Work Package, or Experiment Contract references `mission_id` and maps its outcome, dependency/order, evidence, budget allocation, and stop boundary to that canonical Run section. Later items are durable instances of the existing Work Contract class: the Lead may create a bounded candidate under the Mission rules, but its predeclared non-Human Package Decision Authority must approve the exact contract before mutation. Generated narrative or an agent's plan is not authority.

The machine-readable Mission projection selects exactly one mode: `exact_ordered_items` binds every Package ID and Contract digest in advance; `bounded_instantiation` binds allowed Package-ID prefix, outcomes, semantic owners, path prefixes, environments/actions, `sequential` dependency rule, exact non-Human Package Decision Authority, decision-class ceiling, maximum item count, per-item Agent ceilings and total Mission budgets; in1.5 the existing per-item correction value references the Mission total rather than a separate reserve. A later bounded Package retains a machine-readable projection inside its existing Work Contract with exact Mission/Run, unique contiguous instantiation index, exact predecessor dependency, allowed sets, class/budgets, and matching Package Decision Authority; the checkpoint then binds that exact Package file digest and, for `continue`, the already-existing next Package ID/digest. Both or neither mode, skipped/duplicate indices, an unknown next Package, or foreign authority is invalid.

Human approval of the exact Mission authorizes only its named sequence or bounded instantiation space. The Lead may choose safe reversible implementation details, select the next eligible item, create an allowed candidate contract, disposition in-scope findings, and continue after a passing guard. The Lead may not add or change a required outcome, invariant, accepted Product/design/architecture direction, semantic owner, path family, environment, external action, constitutional risk, Human Gate, or total budget. Such a change stops at the narrowest boundary for the existing authority.

A Mission MAY span several Delivery Slices only when each Slice is named or deterministically bounded and retains its own integration boundary, immutable final release candidate, Staging evidence, technical acceptance, rolling revalidation, rollback, and any Milestone/Production Human Gate. Mission continuation never fuses those boundaries.

For a non-deployable internal Package, minimum continuation evidence is the exact reviewed Package revision, passing package-local criteria/regressions, integration or real-consumer evidence named by its parent Slice, closed blocking findings, a transferable checkpoint, remaining Mission budget, and a still-valid next dependency. It may become `slice_ready`; it cannot claim Staging or Slice acceptance.

Legacy Work/Run Contracts without a Mission remain valid under their pinned Harness release and
MUST NOT inherit Mission authority. Adding a Mission is an expressly authorized material Contract
revision under Section 5.2 and requires the applicable review, Preflight, and admission. A historical completed Run gains no Mission authority. New1.5 administrative reentry follows §7
and cannot create a Mission or enlarge prior authority.

### 1.2 Mission Runtime And Continuation Guard

The Lead evaluates one compact intent before selecting a Package and again before its first mutation: named Mission outcome, exact Package Contract, required behavior, allowed semantic owners/paths/environments/external actions, invariants, non-goals, acceptance/anti-criteria, remaining budgets, and any safe reversible assumption. For new1.5.1+ Missions, retain this readable intent in the existing Work/Run plan before mutation; checkpoints reference its exact revision/section and observed result, not a parallel manually calculated intent or path-mapping hash. Historical pre1.5.1 Missions retain their pinned digest fields. Actual Run/Package/RC artifact authentication remains unchanged. A new document per file edit is prohibited ceremony.

Before expanding an intended path/owner/action, the Lead repeats the check. Investigation outside the allowed mutation paths is permitted when read-only and necessary; discovered debt or opportunity is recorded only as a non-blocking adjacent follow-up with owner/trigger and is not implemented.

Before Package continuation, a Mission checkpoint MUST bind the Mission/Run/Package revisions, readable pre-mutation intent reference (historical pre1.5.1: digest), actual changed-path-to-Package-and-Mission mapping, current acceptance/regression/integration evidence, invariants, assumptions and validation triggers, findings/dispositions/follow-ups, attempts and remaining per-Package/total budgets, dependency/baseline drift, next eligible item, and one decision: `continue | stop | escalate | complete`. `continue` is valid only when every current change maps, blocking findings are closed, evidence and assumptions remain current, budget remains, the next item is authorized, and the transferable checkpoint is pushed where the Mission requires transfer.

A missing detail becomes a **reversible assumption** only when one safe bounded choice preserves the Mission and can be tested before irreversible or externally material impact. The record states the assumption, evidence, validation trigger, fallback, and authority boundary. Competing choices with materially different Product/business/security/cost consequences are not assumptions and use the existing escalation authority.

Ordinary in-scope implementation, test, integration, specification-coherence, visual/accessibility, and evidence defects enter the declared correction loop without a Human interruption. This includes an in-scope defect introduced by an earlier correction. From current evidence the Lead may `correct`, `simplify`, `rollback`, or `reimplement` while the approved user outcome, invariants, Scope Lock, environment/action/risk boundaries and finite authority remain unchanged; the existing checkpoint records expected user benefit plus validation/rollback trigger. Each attempt records a distinct evidence-backed hypothesis. All1.5 technical correction draws once from the existing Mission owner; no extra continuation Run or local ceiling is required. Preserve cumulative attempts/failure signatures and return only affected scope to correction. Same-signature exhaustion without new evidence or total Mission-budget exhaustion produces `stop`/`escalate`, never renamed attempts. A unanimous actionable review finding with a concrete closure condition is a correction trigger, not a Human gate. A reviewer finding must be classified `in_scope_blocking | in_scope_non_blocking | adjacent_follow_up` and map to a violated criterion, invariant, credible in-scope failure, or Mission outcome. It cannot add an outcome, owner, path, Agent, external action, or budget without prior expansion authority.

## 2. Work Package Contract

Before implementation, every Work Package MUST declare:

- stable ID, owning Milestone, Delivery Slice, mapped Feature/Capability outcome, document `revision_status`, package `work_status`, and semantic owner;
- user or operational outcome and traceable requirement IDs;
- in-scope behavior, explicit non-goals, and do-not-touch boundaries;
- affected domains, public contracts, UI flows, data, infrastructure, dependencies, active current specs, and approved target spec revisions;
- exact effective Domain Foundation revision for affected contexts, or for Brownfield change the
  exact covering model/Legacy Exception permitted by `AH-SPEC-DOMAIN-001`; a wholly domain-free
  Package uses the explicit justified Binding variant owned by Domain §12;
- specific acceptance criteria and anti-criteria;
- known problem and current evidence, proposed implementation approach, the simplest sufficient alternative, evidence for every non-obvious complexity, and hypothetical/generalized cases deferred with concrete activation triggers;
- test and evidence plan, including the exact criteria proved at package level and those deferred to the parent Slice's integration, Staging, visual, security, or cost evidence;
- migration, rollback, cleanup, and feature-flag implications;
- lowest applicable decision class, its concrete classification trigger/evidence, creator, reviewers, Decision Authority/final approver, and human gate if any;
- class-bound coordination budget: creator/implementer count, independent reviewer count, maximum active Agents, initial review count, consolidated correction-pass ceiling, closure-review ceiling, and escalation authority;
- deployment impact `none | application | infrastructure | migration | mixed`, any early-verification trigger, size, uncertainty, known risks, and package stop boundary.

A material workflow-UI Package references existing Design §7 interaction meaning and its relevant
revision/delta before costly creation; it does not duplicate the model. Read/explain-only requests
remain within Initialization §1's authority boundary and require no implementation Run.

An **acceptance criterion** states an observable condition required for success. An **anti-criterion** states an observable outcome that MUST NOT occur, including regressions, prohibited scope, unsafe fallback, or architectural boundary violation. “Clean”, “works”, “good UX”, or “fully tested” are invalid without a concrete observation.

Every material solution element MUST map to a confirmed requirement, observed problem, or concretely applicable higher obligation and its named outcome. If a simpler approach satisfies the same obligations, it is selected. Generic platforms, speculative abstractions, additional lifecycle states, and extreme-edge handling remain out of scope until their concrete trigger occurs. Verification removes unmapped complexity; it does not preserve it as harmless optionality.

## 3. Package Sizing, Delivery Slices, And Grouping

A package is too large when it cannot be understood within one bounded context set, implemented and reviewed as a coherent change, verified with bounded evidence, safely rolled back, or resumed from a clear checkpoint. A package is too small when its independent contract, review, and checkpoint cost exceeds the learning or risk reduction it creates; adjacent changes SHOULD then be combined without erasing criteria.

Material split or merge proposals are `D2` decisions. Product/Analysis proposes outcome boundaries; UX verifies flow coherence; Architecture/Engineering verifies domain, dependency, sequencing, and integration effects. The decision records preserved behavior, dependencies, migration order, and what changed in the milestone.

Every Delivery Slice is a `D2` Work Contract and MUST declare:

- stable Slice ID, owning Milestone, mapped Features/Capabilities and the exact partial outcomes it advances;
- target user or operator, observable outcome, start/end state, connected flow, and explicit non-goals;
- ordered Work Packages and their dependency, integration, checkpoint, and rollback boundaries;
- affected UI, application, domain, contract, data, infrastructure, security, observability, and cost layers, with explicit `not_applicable` rationale instead of artificial layers;
- integration branch/baseline, target environment, deployment policy;
- acceptance and anti-criteria mapped to package evidence and final Slice evidence;
- normal final-deployment budget plus any pre-authorized risk/correction candidate budget;
- Product Delivery Release Candidate identity, recovery point, Decision Authority, independent reviewers, and stop boundary;
- post-Slice Vision/MVP/flow/contract/architecture/cost/risk and rolling-plan revalidation owner.

A Slice is too large when it contains independently valuable outcomes, spans more than one Milestone, cannot be integrated and critically reviewed as one story, exceeds a bounded rollback/recovery scope, or is unlikely to reach technical acceptance within one two-week checkpoint. It is too small when it exposes no observable outcome, exists only as a horizontal UI/API/database layer, or would create deployment/review ceremony without material integration evidence. One to two Slices per two-week checkpoint is an orientation, never a quota.

Several approved Work Packages MAY form an ordered sequence inside one Slice. Grouping prevents unnecessary Human stops and repeated Staging deployments between small compatible packages. It MUST NOT erase per-package criteria, evidence, ownership, rollback, or checkpoint boundaries. Several approved Slices MAY form a named Run sequence only when each retains its own release candidate, Staging evidence, acceptance boundary, and stop/checkpoint.

## 4. Work And Milestone States

Document revision, work activity, and evidence maturity are orthogonal. Changing one MUST NOT silently change another.

A Work Package uses:

```text
proposed -> approved -> active -> verification -> slice_ready -> technically_completed
    |          |          |            |              |
    v          v          v            v              v
invalidated  blocked   changes_requested <----------+
    \-----------\-------------------------------> superseded
```

| From | To | Authority and guard |
|---|---|---|
| `proposed` | `approved` | Decision Authority; approved contract, active unchanged specs plus approved target spec revisions, required `D2` review |
| `approved` | `active` | Lead; an authorized active Run names the package |
| `active` | `verification` | Lead; authorized mutation complete and scope frozen |
| `verification` | `changes_requested` | Final Approver; blocking findings or missing evidence recorded and correction budget remains |
| `verification` | `slice_ready` | package Final Approver; package criteria and independent review pass, exact source commit is integrated into the parent Slice candidate, and all deferred Slice-level evidence is named |
| `slice_ready` | `changes_requested` | package or Slice Final Approver; integration, Staging, or Slice review exposes a package defect; old source/review/evidence binding is invalidated within the remaining authorized correction reserve |
| `slice_ready` | `technically_completed` | Slice Final Approver; the exact parent Slice is `technically_completed` and its accepted evidence is mapped to this package's remaining criteria |
| `active` or `verification` | `blocked` | Lead; blocker and safe checkpoint recorded |
| `blocked` or `changes_requested` | `active` | Decision Authority; blocker resolved or correction cycle authorized in a valid Run |
| `proposed` or `approved` | `invalidated` | semantic owner and Decision Authority; changed evidence removed scope authority |
| any non-terminal state | `superseded` | Decision Authority, after cancelling any active Run; replacement or cancellation decision linked |

`superseded` is terminal. A1.5 administrative `technically_completed` state may reenter only under §7. `slice_ready` is not Done and MUST NOT be presented as staging-verified or technically accepted. A `slice_ready -> changes_requested -> active` correction creates a new implementation/evidence revision, invalidates affected package and Slice candidate evidence, serializes only the actual conflicting resource, reruns local review and integration, and returns through `verification`; a material Contract change additionally needs a reviewed Contract revision. A blocked package remains active in routing and handover; an invalidated or superseded package leaves active routing but remains traceable. Canonical product specs are never altered merely by a package-state transition.

Specifications retain stable paths. An approved target describes intent; implemented and accepted/
delivered states are distinct. Artifact §4 makes the final immutable Review Record the authority
for material acceptance and verified spec activation, binding candidate, spec revisions and their
predecessors. Work statuses/navigation are derived views, not a second truth or mandatory
post-delivery commit. A package cannot activate a deploy-relevant target early.

A Delivery Slice uses:

```text
proposed -> approved -> active -> verification -> technically_completed
    |          |          |            |
    v          v          v            v
invalidated  blocked   changes_requested
    \-----------\-----------> superseded
```

| From | To | Authority and guard |
|---|---|---|
| `proposed` | `approved` | Decision Authority; complete `D2` Slice Contract and reviews |
| `approved` | `active` | Lead; authorized Run exists |
| `active` | `verification` | Lead; all included Packages are `slice_ready`, scope is frozen, and the exact final Product Delivery Release Candidate is identified |
| `verification` | `changes_requested` | Slice Final Approver; blocking integration, Staging, critical-user, architecture, security, cost, or evidence finding remains within correction budget |
| `verification` | `technically_completed` | Slice Final Approver; exact Product Delivery Release Candidate passed integration CI, CDK-backed Staging deployment, required real-environment checks, critical-user and independent technical review, finding closure, and final technical acceptance; final immutable Review Record binds verified target activation and package completion |
| `active` or `verification` | `blocked` | Lead; blocker, environment truth, rollback point, and checkpoint are recorded |
| `blocked` or `changes_requested` | `active` | Decision Authority; blocker resolved or bounded Correction Run authorized, affected evidence invalidated, and actual conflicting access is serialized |
| `proposed` or `approved` | `invalidated` | semantic owner and Decision Authority; changed product evidence removes scope authority |
| any non-terminal state | `superseded` | Decision Authority, after cancelling active Runs and linking replacement/cancellation |

`superseded` is terminal;1.5 administrative completion reentry follows §7. A predeclared deployment `not_applicable` is valid only for a genuinely non-runnable deliverable whose observable outcome is proven by exact real consumer/integration evidence. An internal library, infrastructure, API, or other horizontal enabler of a deployable Product remains a Work Package inside a vertical deployable Slice and cannot bypass Staging by declaring itself a non-deployable Slice.

A Milestone uses:

```text
planned -> active -> ready_for_human_review -> accepted
   |         |                 |                 |
   \---------\-----------------+-> rejected -----+-> superseded
```

`ready_for_human_review` requires all included Delivery Slices to be technically completed or explicitly removed through approved replanning. `accepted` requires the Milestone's Human Gate. `rejected` records requested changes and returns only through a revised, approved Milestone plan; `superseded` is terminal.

The Product/Analysis owner may propose a milestone transition. The Decision Authority activates or submits it for review; only the human Product Authority may accept, reject, or approve a material replacement. A rejected milestone has no active delivery authority until its revised plan is approved.

## 5. Execution Run

An Execution Run is an authorization envelope orthogonal to the work hierarchy. It authorizes a named Work-Package subset inside one Slice, one complete Slice, an explicitly ordered Slice sequence, or one non-delivery Technical Risk Experiment. A Feature or Milestone alone is not execution authority.

Before that envelope exists, a direct Human Task Mandate or already valid Work authority MAY start
bounded `assignment_preparation`: read-only analysis plus the minimum Work/Run Contract, Agent
brief, Projection and Preflight preparation needed to present an admissible Run. This is not an
Execution Run, lifecycle state or implementation authority. It MUST NOT mutate Product/work
behavior, perform external actions, review/accept a candidate, claim completion or bypass a Human
Gate. The prepared Run traces every material field either to the mandate, an owning canonical rule
or an explicitly identified unresolved decision.

When a Human explicitly authorizes execution and delegates operationalization within a stated
boundary, canonical defaults and the narrowest sufficient Run MAY be derived without requesting a
duplicate Human approval. A material choice or expansion not settled by that mandate still returns
to its Decision/Human Authority. The exact Run must pass normal Preflight, authorization, Agent
activation and admission before implementation mutation begins.

Before activation, every run MUST declare:

- Run ID, Run kind `product_delivery | technical_risk_experiment | domain_foundation | bootstrap_initialization | governance`, Harness version, repository, and remote; every Git-mutating Run binds exact starting commit, current branch, and target branch, and every authorized Slice or Experiment additionally binds its environment; only a demonstrably non-Git-mutating Run may record those Git fields `not_applicable` with rationale;
- purpose context by `run_kind`: Product Delivery binds the exact active Product Vision Brief, applicable Domain sources or explicit domain-free justification under Domain §12, target user/outcome, and Slice/package contribution to the current MVP/Milestone; a Technical Risk Experiment binds the relevant active Vision where one exists or the named pre-Vision Product/architecture decision, hypothesis, and decision contribution without requiring a package; `domain_foundation` begins with exact Human instruction, active Bootstrap State, owning Work Contract, and safe named input identities/digests, then creates Foundation/review/decision as outputs; `bootstrap_initialization` begins with the exact effective Foundation decision and Human instruction, then binds its candidate Vision revision as soon as durably created; Governance binds the exact Master/governance objective, HIP or owning Work Contract, constitutional and Human authority evidence, and protected invariants without inventing a Product Vision;
- authorized target set by `run_kind`: Product Delivery names Slice and Work-Package IDs/order plus any permitted boundary continuation; a Technical Risk Experiment names its Experiment ID, exact approved Experiment Contract, hypothesis/decision target, required observation, cleanup target, and conclusion evidence; Bootstrap or Governance names the exact owning Work IDs, artifacts/sections, and ordered boundaries;
- allowed modules, paths or globs and permitted accompanying spec, test, and evidence classes; prohibited infrastructure, environment, and external-action scope;
- one compact **Scope Lock**: the Human/requested outcomes, minimum sufficient change, allowed path families, explicit non-goals/prohibited outcomes, change-to-outcome evidence required at verification, adjacent-findings disposition, and exact expansion authority;
- Lead, active agents, role functions, reasoning level, Decision Authority, reviewers, and human gate owner;
- for Harness `1.2.7+`, the planned Agent IDs, reviewers, finite correction ceiling and Agent-start
  clearance recorded directly in the Run Contract; older projections remain historical only;
- decision class plus concrete classification trigger/evidence; creator/implementer and reviewer counts; maximum concurrency; initial-review, consolidated-correction, and closure-review ceilings; escalation authority; one authoritative task/Mission technical-correction reserve under §10; operational budget/working-window trigger; and checkpoint cadence;
- required capabilities, credentials by reference, test accounts, tools, and environment access;
- completion evidence and target level for every applicable target: package/Slice completion for Product Delivery, `concluded` plus verified cleanup for an Experiment, or the exact declared Bootstrap/Governance work outcome;
- stop boundary, pause triggers, escalation route, and rollback point.

### 5.1 Task-Wide Duties, Progress, Drift, And Cumulative Credit Protection

D0 routine is exempt from the percentage and task-controls machinery below; retain task authority
and relevant checks without manufacturing records. D1–D3 retain the existing20% drift cadence,
including a proportionate impact/risk/uncertainty and effort assessment in that same check.

Apply Collaboration§9's KISS rule from the first task action. Each work stretch must advance an
original authorized outcome or a necessary named evidence obligation. Preparation, diagnostics,
tool development and review are not independent outcomes unless explicitly commissioned. Choose
the smallest existing supported path; a capability failure does not silently expand the Scope
Lock. Keep scope/approach decisions in the current Run or checkpoint, not additional control files.

Applicable Harness duties begin with the Human task, including entry reading, routing, analysis,
`assignment_preparation`, admission and Preflight. An ordinary Human instruction suffices; neither
repeating rules nor a special prompt activates them. Calling a phase “outside the Run” does not
exempt it. Preparation remains non-execution and grants no Product mutation, acceptance or external
action authority. Duties apply at their owning specification's trigger, not all indiscriminately
at entry. Installation-only and inactive Brownfield staging retain their existing authority boundaries.

The Lead checks coverage of the following existing duty families against the current next action.
These groups are an index, not new policy owners or a substitute for routed requirements:

| Coverage key | Owning rule and due trigger |
|---|---|
| `entry_integrity` | Distribution §3–4: mandatory entry/integrity before task work, and recheck on resume or integrity change |
| `scope_authority` | Constitution and Work §5: Human mandate and exact Scope Lock before judgment/mutation; amendment before expansion |
| `agent_start_review` | Collaboration §1.1, §3–4: exact Agent-start clearance before responsibility; independent review/quorum before the respective approval |
| `human_gates` | Constitution and routed Gate owner: exact Human decision before the gated action, never inferred from general task authority |
| `capability` | Work §5–6: applicable tools, access and capability before use; Delivery owns deployment execution |
| `mutation_boundary` | Work §5 and Distribution: allowed paths/actions and protected/Product boundary before writes/external actions; stop on loss of authority |
| `budget_stop` | Collaboration §4 and Work §5.1, §11: finite cumulative budget, findings, stop boundary and safe checkpoint before continuation |
| `routed_requirements` | All task-routed owners: applicable Spec-First, Domain, design, security, evidence, delivery and other obligations at their own triggers |

For1.5.2+ the coverage key is `capability`; historical pre1.5.2 task-controls retain their
released `capability_lease` key without creating a duty for new work. The withdrawn2.0.0
release was the original1.5.0 contract and retains that historical interpretation.

Before every mutation stretch, review/acceptance, external action, completion and resume, refresh
this coverage and perform each due check. A previous successful check is not a perpetual clearance.
Refreshing coverage is a brief assessment of changed facts, not an instruction to rerun tools or
rewrite all eight entries when their evidence and next-action applicability remain unchanged.
Reuse a passing ordinary Contract check under Ordinary Admission §4; rerun at start/resume or
when the Contract, its named sources, authority or other checked inputs change. Progress prose
alone does not invalidate unchanged admission. Actual capability, shared writers and external
authority are still checked at their own action boundary; valid syntax never proves those facts.
`satisfied` means all currently due checks in that group have supporting observations; future
triggers are named, not prematurely marked performed. `not_applicable` requires a concrete reason
for the current action and the next applicability trigger, never a blanket phase exemption.
Missing evidence, a missed duty, or unresolved applicability sets the affected group `blocked` and
stops affected continuation. Resolve under the original authority, not an invented extra Human Gate.

Before a Run exists, keep this compact status and due progress/drift evidence in active communication;
no Run or extra file is required for read-only work. New ordinary Runs pinned to `1.3.1+` carry it in
one `task-controls` evidence block in their existing progress section (schema owned by Ordinary
Admission §4.1). Transfer actual preparation progress/checks into it. Existing checkpoints reference
that Run status rather than duplicate it. The Lead owns one progress/drift sequence for the
Human-authorized aggregate. Delegated work, sample subjects and resumed substeps report their
results/open work to that owner; they do not start their own percentage ladder or wait for a
second40/80% approval. Independently authorized Human tasks retain their own applicable controls.
Missions retain their existing checkpoint mechanism.
Historical Runs keep their pinned format; a new task uses the installed rules and carries prior
consumption when continuing the same authorized outcome. Activation, correction, rename, successor
Run or resume cannot reset progress, findings or budgets.

For material multi-step work, use the existing Work/Run plan and progress section as one durable
worklist: original requirement/source, required result, current open/verified state and evidence,
remaining step/dependency and next action. Reuse an existing Human-supplied plan; do not add a
parallel acceptance list or tracking file. Preserve the complete authorized outcome, not only
the current substep. At work boundaries and before pause/context handoff, update the changed
items and point the existing handover to this owner. Replace current status and next-action
fields in place; retain earlier observations as clearly labeled history, not conflicting current
instructions. Resume reads that plan before selecting
the next open step. D0 retains its task/diff/evidence without this material-work form.
Before completion, independently trace every original requirement and subsequent Human change
to its actual evidence. Existing fulfillment may be reused; a changed rule, green unrelated suite
or aggregate PASS is not evidence of an unobserved required behavior. An unresolved required item
remains open unless its owning Human authority explicitly changes the promised scope; preserve
that decision and its evidence limits instead of silently deferring or narrowing the outcome.

Historical pre1.5 Mission convergence blocks retain their format. For1.4.x their `critical_quorum` uses
`D0: reclassify` and `D1`, `D2`, `D3: 2_of_2_or_authorized_2_of_3`, applying Collaboration's
working-Agent distinction; Spawn never votes. Pre1.4.0 blocks retain their original constants.
New1.5 uses the existing Mission total/checkpoint instead of a parallel convergence budget block.
Existing item correction fields reference that total; checkpoint `corrections_used` is cumulative
Mission consumption and plus `mission_corrections_remaining` equals the total. A later item cannot
reset it. Necessary closures are attached to corrections, not an independent review reserve.
Agent allocation/concurrency and progress/drift duties remain in the existing Mission record.

Task progress and bounded Run status are distinct. A completed partial Run retains the actual
percentage of the Human task, even below100; its successor carries that percentage and evidence.
Only completion of the full Human-authorized task warrants100%. A Run's `completed` status alone
does not prove that the whole task ended. Carried drift observations retain their original valid
Lead/reviewer assignment, even when the successor has a different authorized team; new observations
use the new Run's assignment. Bind original evidence through exact named Run sources under Ordinary
Admission §4.1, not a second counter, lifecycle or re-review of already valid observations.

Progress names the Human-authorized aggregate and current phase. In an explicitly Domain-only
task,100% means the promised Domain output and Gate handoff, not an effective Foundation or
completed overall Initialization. Whole-Initialization work retains aggregate progress and
cumulative consumption at the Domain boundary; no extra machine-readable counter is created.

If a percentage report/check was missed, its existing evidence field explicitly records the missed
threshold, actual later observation, consequences and resolution by the original responsible
authority. A complete numeric prefix means documented coverage/resolution, not proof of timely
communication. Never fabricate earlier delivery, approve a missed Gate retrospectively, or erase
the incident. Unresolved consequences keep the affected action blocked.

Every D1–D3 Human task reports outcome-based progress at `10, 20, ..., 100` percent, including completed
preparation toward its authorized outcome. Progress is monotonic and measures completed outcomes
and evidence, not time, messages, token use or activity volume. Estimate from the actual remaining
work; entry/preflight are neither excluded nor assigned automatic equal phase weights. Do not
manufacture 20% merely because entry reading ended. Each update states achieved outcome/evidence,
next bounded action and any blocker; it creates no scope or completion authority. An uninterrupted
or asynchronous task MAY retain the next update until a communication boundary, but MUST NOT skip
or combine checkpoint values. Use communication or the existing Run progress section, never a new
durable file per percentage.

The Lead performs a scheduled drift check at `20, 40, 60, 80, 100` percent and an event-triggered check on critical recurrence or material new evidence. The `40` and `80` percent checks require independent validation by one assigned non-author reviewer; the event-triggered check uses the applicable critical quorum from `AH-SPEC-COLLABORATION-001`. Reviewers need not remain active between these checkpoints. Each check records:

Historical pre1.5 D0 keeps its original recorded controls. New1.5 D0 creates none. Material checks record:

- original purpose, required outcome, Scope Lock, and actual changed paths/mechanisms;
- whether every active finding and mechanism maps to a current obligation or observable benefit;
- breadth, unnecessary complexity, and what can be removed, deferred, simplified, rolled back, or reimplemented;
- cumulative Agent/review/remediation consumption, remaining authorized total, and finish forecast;
- one decision: `continue | simplify | rollback | reimplement | checkpoint_and_escalate`.

Every Run directly names its finite Agent team and correction ceiling. Replacing or renaming a Run
for the same authorized outcome does not reset consumed corrections; only an explicit Human-approved
Contract revision may raise the limit. No separate budget-lineage artifact or projection is required.

Work §10 owns the single1.5 technical correction reserve; there is no separate causal-chain or
Package ceiling. Old consumed limits remain binding across upgrade unless expressly increased.

When the Run carries a Mission, it additionally declares every field in Section 1.1 and the
versioned continuation guard used at each package boundary. A `mission_id` reference without the
complete canonical Mission block is invalid.

For an ordinary Harness `1.2.7+` Run, current status and evidence are updated directly in the
versioned Run Contract. Git preserves history. Authorization applies to the stated revision and is
not reusable after a material scope, authority, target, action or budget change.

### 5.2 Execution Run Contract Revision

A material ordinary-Run change first reaches a safe non-mutating state, increments the visible
revision by one, records the reason and Decision/Human Authority in the same Contract, and reruns
the direct Contract check. Git preserves the prior revision. No document hash, revision event,
Admission Report or schema-only migration is required. Historical Runs keep their pinned rules and
are not rewritten by a Harness upgrade.

For Harness1.5.2+, there is no Harness lease mechanism: no agent claims, renewals, expiry,
takeover, handoff or lease evidence. Repository and Product rules govern their own Git and
deployment procedures.

For an ordered Slice sequence retain its candidate/evidence/acceptance checkpoints and rolling
revalidation, then verify the next baseline and authority. No new Run or ownership-transfer
record is needed solely for that boundary.

A Technical Risk Experiment uses its own `D1` or `D2` non-delivery Work Contract with stable Experiment ID, `experiment_status`, hypothesis, decision owner, exact Run, Capability Preflight, external-action authority, data/cost/side-effect limits, TTL/cleanup, evidence, and stop condition. Initialization may propose this Contract; execution begins only after its own Decision Authority approves and its Run becomes `active`. Existing `D3` Human Gates still apply to destructive, irreversible, material IAM/security/privacy/DNS/secret/fixed-cost or real-provider effects. Experiment state is `proposed -> approved -> active -> verification -> concluded`, with `blocked`, `changes_requested`, `cancelled`, and `superseded`; `concluded` means evidence captured and cleanup verified, never Product delivery.

An **Early Verification Candidate** is different: it is immutable Product code from an active Slice, deployed only when a declared IAM/CDK, migration, auth, provider, central-contract, uncertainty, or blast-radius trigger makes earlier real evidence materially safer than waiting. Its Slice Contract and Run preauthorize hypothesis, target, cost, side effects, cleanup/restore, evidence, and bounded count. It is marked `verification_candidate` and `non_promotable`, cannot activate target specs or advance Slice/package completion, and never replaces the final Product Delivery Release Candidate.

For the first `domain_foundation`, the installed active Bootstrap Work Contract supplies package
scope. Raw-input inspection, provisional Contract construction, and Preflight remain read-only and
ephemeral. The non-creator Decision Authority authorizes the Contract; after the direct check it may create safe snapshots, Foundation, review, and decision outputs. The later
`bootstrap_initialization` targets the effective Foundation and creates post-Gate Product/design/
planning artifacts. Neither Run names its future outputs as start targets. This is not a general
pre-Run mutation exception.

The Lead MAY coordinate only inside this envelope. Discovering adjacent useful work creates a proposed package or follow-up run; it does not expand the active run.

For a Mission, the Lead additionally executes the Section 1.2 guard before selection, before first mutation, before path/owner/action expansion, after implementation, and before continuation. A stale Mission/Package digest, unmapped change, failed invariant, unresolved block, exhausted budget, unauthorized next item, or materially divergent assumption stops at the narrowest safe boundary.

The Scope Lock is interpreted narrowly. Discovery is evidence, not authorization. A change is allowed only when it is necessary for a named required outcome, required by an applicable higher rule for that outcome, or needed to keep the changed path coherent and verifiable. A new outcome, semantic owner, path family, Agent, external action, or materially higher budget stops affected mutation and requires a separately authorized Run amendment before work continues. At verification, every changed path and every non-obvious mechanism maps to one required outcome and current evidence; unrelated cleanup, speculative abstraction, generic future-proofing, opportunistic refactoring, extreme-edge handling, and “while here” improvements are removed or recorded as non-blocking follow-up with a concrete trigger. File count alone is neither permission nor a scope-quality metric.

Before Agent activation, Preflight applies Collaboration §§1.1,4–5 to the actual assignment and
pinned rules. New1.4.0+ D1–D3 work defaults to Creator plus one independent working reviewer and
the separate temporary Spawn Reviewer; D0 needs no reviewer. Bind the concrete class trigger,
finite cumulative/concurrent allocations and any exact conditional third-working-Agent authority.
Missing classification evidence does not justify a larger team. Spawn checks do not count toward
artifact quorum or silently grant extra working capacity. Higher topology or extra rounds require
their exact prior authority; historical Runs retain their released limits.

Review findings remain inside the Work/Run boundary. Adjacent improvement and pre-existing debt are routed to follow-up; they cannot silently enlarge the package, add reviewers, or reset budgets. Findings are consolidated per target revision, corrected in one coherent pass, and re-reviewed only for their closure scope. Budget exhaustion stops the Run even when more credits or Agents happen to be available.

## 6. Capability Preflight

Before mutating work begins, the Lead verifies and records:

- installed harness version and integrity;
- repository, current branch, remote, clean/dirty state, and collaborator changes;
- required runtimes, dependency access, tests, renderers, browser, and local start capability;
- CI/CD visibility and permission to inspect or trigger it;
- target AWS account/profile/region, deployment role, and CDK capability when applicable;
- secret references without exposing values;
- stable staging user/admin and automation identities when applicable;
- ability to capture required logs, screenshots, artifact IDs, and cost evidence;
- human approvals already required for the authorized actions;
- rollback or safe-stop capability.

A missing capability is classified as:

- `required_blocker`: run remains `preflight_blocked`;
- `degradable`: an alternative scope or lower target completion level is proposed;
- `not_applicable`: recorded with rationale.

Any proposed reduction of authorized scope or target completion level is a Run Contract amendment requiring the predeclared Decision Authority; for `D3`, it requires the human gate owner. Without re-authorization, the run is `preflight_blocked`.

Agents MUST NOT promise staging verification, deployment, external-provider behavior, or production readiness when the corresponding capability is unavailable.

## 7. Run State Machine

Allowed transitions are:

| From | To | Actor | Guard and required evidence |
|---|---|---|---|
| `proposed` | `preflight` | Lead | complete draft Run Contract plus the exact approved target Contract set for its `run_kind`: Slice/package, Technical Risk Experiment, Domain Foundation, Bootstrap, or Governance |
| `preflight` | `preflight_blocked` | Lead | at least one required capability or authority is missing |
| `preflight_blocked` | `preflight` | Lead | evidence that the named blocker may now be rechecked |
| `preflight` | `authorized` | Decision Authority | preflight passed, reviewers and target levels fixed, required gates referenced |
| `authorized` | `active` | Lead | starting branch/commit and external state match |
| `active` | `verification` | Lead | authorized mutation complete; no unreviewed scope expansion |
| `active` or `verification` | `paused` | Lead, Decision Authority, or human | checkpoint written; authority temporarily inactive |
| `active` or `verification` | `blocked` | Lead | blocker record and safe-state evidence written |
| `paused` | `active` | Lead | resume validation passed, authority remains valid, necessary resource access acquired or transferred |
| `blocked` | `preflight` | Lead | blocker resolution changes capability, scope, environment, or authority |
| `blocked` | `active` | Lead | blocker resolved with evidence; contract and preflight remain valid; necessary resource access coordinated |
| `verification` | `changes_requested` | final approver | blocking findings or missing evidence recorded within correction budget |
| `changes_requested` | `active` | Decision Authority | a bounded correction cycle is explicitly authorized and necessary resource access is valid |
| `verification` | `completed` | Decision Authority | declared run scope reached every target level with required evidence |
| any non-terminal state | `cancelled` | Decision Authority or human Product Authority | reason, revoked authority, last checkpoint, cleanup/rollback, and successor if any recorded |

`cancelled` is terminal. In1.5 an administrative `completed`/`technically_completed` object may
return through reviewed `changes_requested`/`active` revision only when the original outcome is
proven unfulfilled and original mandate, working bound and remaining reserve still apply. The
non-author approver confirms the material revision; current admission precedes mutation. Retain
old observed results. A genuinely fulfilled/ended mandate and unused budget grant no later repair
authority. New outcomes or expired authority need the owning decision. Published candidates/tags
remain immutable; a changed candidate has a new identity and candidate A's Production approval
does not approve B. Historical completed contracts retain their original meaning.

`completed` `completed` means only that the authorization envelope ended at its recorded `achieved_level`; it does not by itself mark a Delivery Slice, Work Package, Feature/Capability, or Milestone complete. A delivery Run whose target is `technically_accepted` cannot complete at a lower level without an approved Run Contract amendment. Budget exhaustion normally produces `paused` or `blocked`, not `completed`.

The human Product Authority may pause or cancel a run at any time. A run MUST also stop when its scope completes, its stop boundary is reached, authority is exhausted, a required human gate is reached, a blocker prevents honest progress, a dangerous side effect is possible, or retry policy is exhausted. It MUST NOT start the next proposed run without authorization.

## 8. Completion Ladder

Work Packages and Delivery Slices report only the highest level actually evidenced. D0 reports
implemented, locally verified or actually delivered from its task/candidate evidence without
artificial intermediate Work objects or independent material acceptance:

| Level | Applies to | Entry criterion |
|---|---|---|
| `specified` | Package | approved Work Contract, parent Slice, active current specs, and approved target revisions for changed behavior |
| `implemented` | Package | implementation is bound to an identified source commit |
| `locally_verified` | Package | every required package-local check and local-start observation is green or explicitly not applicable |
| `independently_reviewed` | Package | required package quorum is met with no open blocking package finding for the target revision |
| `slice_ready` | Package | exact commit is integrated into the Slice candidate and all remaining criteria are explicitly mapped to Slice-level evidence |
| `integrated` | Slice | identified Slice commit passed required integration CI and every included package is `slice_ready` |
| `staging_deployed` | Slice | exact immutable Product Delivery Release Candidate and Staging deployment IDs are recorded |
| `staging_verified` | Slice | the connected Slice outcome and mapped package criteria were exercised on real Staging through required smoke, E2E, visual, log, provider, security, infrastructure, and cost evidence |
| `technically_accepted` | Slice and included Packages | critical-user findings are closed; the predeclared non-author Slice Final Approver accepts the exact evidence and residual risks; the final immutable Review Record binds verified target activation and included package completion |

Levels are cumulative inside the applicable entity. Slice evidence applies only to exact included package revisions and their mapped criteria. A step may be `not_applicable` only when the Slice Contract predeclares the reason and Decision Authority; it MUST NOT skip an observation required to prove a later claim. A deploy-relevant Slice cannot be `technically_accepted` without real Staging evidence. Only a genuinely standalone non-runnable deliverable may mark deployment levels not applicable when exact real consumer/integration evidence proves its observable outcome. An internal library or horizontal enabler of a deployable Product stays inside a vertical deployable Slice.

Human milestone acceptance is exclusively a Milestone state and cannot be inferred from technical approval. New evidence or upstream changes MAY invalidate a prior completion level.

## 9. Evidence Bundle

The run's evidence bundle MUST include, as applicable:

- Slice/package revisions, Product Delivery Release Candidate identity, source commit, immutable build, pipeline run, deployment, and environment IDs;
- acceptance and anti-criteria mapped to observations;
- local, unit, component, contract, integration, security, IaC, and regression results;
- local start and real staging smoke/E2E results;
- mockup-to-implementation comparison, viewport/state screenshots, and visual findings;
- relevant logs and metrics with secrets and personal data removed;
- cost and architecture checks;
- review records, finding dispositions, remaining dissent, and human decisions;
- known limitations, not-observed claims, cleanup, and rollback reference.

Evidence records command or workflow, timestamp, result, environment, and immutable reference. Summaries link to raw artifacts where available. Failed evidence remains visible after correction.

### 9.1 Optional Harness Logging

Harness logging is disabled by default and requires explicit activation for the named task.
It adds one diagnostic Markdown report at `docs/harness-logs/YYYY-MM-DD-<task>.md`, using the
existing task identity and the shipped template; never overwrite another task's report. It is
a mutable Reference summary, not approval, execution authority or replacement raw Evidence.
Record activation and report path in the existing task/Run/handover context. D0 needs no Run
or additional Work hierarchy. Explicit deactivation and task end stop recording; preserve the
disabled state for fresh resume and keep old reports. Another task does not inherit activation.
Late activation starts from observed current state, with earlier gaps stated rather than invented.

At existing work boundaries and meaningful failures/interventions, briefly retain original
outcome, Harness/source references, actual Agent roles, relevant sanitized input/output summaries,
short factual decision reasons, actions/checks/results and existing evidence links, retries,
Human interventions, observed timing, remaining work and next step. Distinguish observation,
Human report and hypothesis; unavailable timing/usage remains unknown. Do not capture private
model reasoning, full prompts/tool dumps, credentials or unnecessary personal/customer data.
Reuse existing observations; logging alone creates no Agent, check, gate or background process.
Update the report’s current outcome/resume fields in place while preserving historical events.

Resume reads the current activation state and continues the same task report when enabled.
Recording failure is disclosed without turning logging into an automatic task/release blocker.
Sanitized reports may accompany authorized normal commits; no mandatory logging-only closure
commit or deployment. Product CI treats this diagnostic directory as non-runtime documentation
unless it is genuinely consumed by a build. Later analysis is separately requested, cites report
observations and gaps, and makes no automatic uploads or rule changes. Evolution's existing HIP
route remains the sole route for an actual upstream improvement proposal.

## 10. Retry And Failure Control

For an ancillary technical obstacle, two unsuccessful targeted diagnostic attempts trigger an
approach/proportionality decision BEFORE another variant or mechanism. Count attempts across
renaming, tools and resumed contexts. State the original criterion, what was learned, the simplest
supported alternative and the remaining time/attempt boundary in the existing checkpoint. Continue
only with new evidence and authority covering that bounded path; otherwise stop the affected work
and identify the exact missing capability/decision. This earlier decision point neither grants
additional correction cycles nor replaces the finite Run/Package limits below.

Reuse successful checks and evidence while their relevant inputs, environment and obligations
remain unchanged. Repeat only the checks invalidated by a concrete change; identify that change.
A new thread, role, checkpoint or desire for reassurance is not invalidation. Run a broad suite
only when a concrete cross-cutting change or an applicable release contract requires it. Do not
claim reused evidence covers new behavior or omit a genuinely required current-candidate check.

An attempt record contains failure signature, environment, observation, hypothesis, change, result, and new evidence.

For Harness1.5, keep **one authoritative finite technical correction reserve** in the existing
task/Run or Mission owner. D0 allows one cycle after initial implementation, ordinary D1–D3 default
to three, and a larger Mission explicitly proposes a finite total justified by its scope and work
window for Human authorization. A tighter existing limit wins. Mission subitems reference that
same total and consumption; never multiply defaults or exhaust a separate local counter. The
concrete finite working bound starts with preparation and initial implementation, not first review.
Time/cost/external-action limits bound different risks and remain in force. No new budget ledger.

A cycle begins when the Lead starts one coherent cause correction of observed gaps in a candidate
first presented as reviewable, and includes its relevant verification. Consolidated findings,
individual edits, normal first-pass TDD red/green steps and test commands are not separate cycles.
After completed verification, a remaining or newly introduced defect needs the next cycle. Do not
relabel an already failed candidate as initial implementation. The last allowed cycle may finish
its tests and targeted independent closure; exhaustion stops only a further required mutation.
Material corrections receive at most one affected closure each, with no separate exhausted review
counter. Distinct necessary material plan/design/result decisions still require independent review.

Retain the first failure and a new evidence-backed hypothesis. Safe transient test/cleanup retries
are not technical cycles only when bounded in advance, unchanged in candidate/configuration and
safe to repeat. Expected read-only provider visibility uses the same rule. Code/configuration/IAM/
artifact changes consume a cycle; rest budget is never action authority. Two failed targeted
diagnostics still require the approach decision above; no separate same-signature/causal-chain or
Package correction ceiling. Renaming, restarting or upgrading cannot reset consumed authority.
Ordinary work cannot draw a Mission reserve it does not belong to. Increasing a limit requires an
exact prior Human-approved Contract revision with the new finite value and reason.

Stop earlier when access, secrets, a product decision, a required provider, data safety, authorization, or rollback confidence is missing. After repeated staging failures, return to package or architecture planning rather than indefinitely patching symptoms.

Exhaustion produces `blocked` with:

- concise failure signature and impact;
- attempts and falsified hypotheses;
- evidence and current environment state;
- safest rollback or containment option;
- exact human decision or capability needed;
- recommended next experiment, if one exists.

## 11. Checkpoint, Pause, And Resume

Checkpoints SHOULD occur at Work-Package and Delivery-Slice boundaries. A mid-package pause is permitted when resource limits, human interruption, external outage, or safety require it.

A resumable checkpoint MUST record:

- Run, Milestone, Slice, Feature/Capability, and Work-Package IDs;
- pinned harness version and integrity;
- repository, branch, pushed commit, target environment, and immutable artifact/deployment ID;
- clean or dirty state, including exact uncommitted files and ownership;
- collaborators and external side effects;
- criteria completed, evidence gathered, reviews pending, and known regressions;
- failure signatures, attempt count, hypotheses, and unresolved findings;
- next single safe action, stop condition, and last green rollback point.

Checkpoint transferability is binary. A checkpoint is `transferable` only when all resume-relevant in-scope work is committed and pushed, harness version and integrity are pinned, required artifacts are immutable, and external state is verifiably referenced. Remaining dirty files must be proven unrelated and excluded from the Run; otherwise the checkpoint is `non_transferable`. Every non-transferable checkpoint MUST preserve exact dirty-state recovery instructions without claiming that another person can safely resume.

Cross-person or cross-machine transfer requires `transferable`. The same owner MAY resume a `non_transferable` checkpoint only in the same verified workspace after exact dirty-state, integrity, repository, environment, external-side-effect, remaining-authority/budget verification. Another owner or machine requires explicit Decision Authority for bounded salvage: preserve the original state, reconstruct a clean checkpoint, and never claim the prior state was safely transferred.

The receiving or resuming agent reads mandatory entry documents, verifies harness integrity, fetches the referenced commit when transfer applies, compares remote, branch, repository, dirty state and external state to the checkpoint, and re-runs the narrowest relevant verification. It resolves accepted
state through Deployment history → RC → final Review under Artifact §4, not navigation alone. Drift causes a new checkpoint or replanning decision, not silent continuation.

## 12. Replanning

After every technically accepted Delivery Slice, and additionally at every two-week checkpoint or material Risk Experiment, Product/Analysis, UX, Architecture/Engineering, and Quality revalidate the active Vision, MVP outcome, flows, Capability coverage, contracts, architecture assumptions, cost, risks, and current evidence. They retain, refine, reorder, split, merge, defer, replace, or invalidate future Slices and packages, then make the next two weeks implementation-ready and keep the following six weeks structured.

Replanning MUST preserve the original decision trail, update affected traceability, and keep only the rolling six-week horizon detailed. A reslice that preserves the accepted MVP and Milestone outcome is `D2` and does not create a routine Human Gate. Changing an accepted MVP or Milestone outcome, a previously Human-gated risk acceptance, or another constitutional Human decision returns to the applicable Human Authority.

Agents MUST NOT preserve obsolete planned work merely because it already has a document. They also MUST NOT discard accepted product outcomes while reslicing delivery mechanics. Material scope change follows `D2` review; milestone or MVP change follows the applicable human gate.
