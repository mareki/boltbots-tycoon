# Execution Run — {{TITLE}}

> Artifact ID: `{{PRODUCT}}-RUN-{{NNN}}`
> Artifact class: Work contract
> Semantic owner: {{OWNER}}

D0 routine uses the existing task, diff and focused evidence: do not instantiate this template.
No WP/Slice/Domain Binding, Spawn or task-controls form is required for that path.

This block is the complete ordinary material-Run start contract. Do not create a projection, report, event
or activation record. Update `status` in place; Git keeps history.

<!-- run-contract:start -->
```json
{
  "schema_version": "1",
  "revision": 1,
  "status": "approved",
  "harness_version": "{{SEMVER}}",
  "run_kind": "product_delivery | technical_risk_experiment | domain_foundation | bootstrap_initialization | governance",
  "decision_class": "{{D1_D2_D3}}",
  "targets": [
    {"id": "{{SLICE_WORK_EXPERIMENT_OR_GOVERNANCE_ID}}", "path": "{{EXACT_SOURCE_PATH}}"}
  ],
  "outcome": "{{OBSERVABLE_PRODUCT_OR_USER_OUTCOME}}",
  "allowed_paths": ["{{REPOSITORY_RELATIVE_PATH}}"],
  "non_goals": ["{{EXPLICIT_NON_GOAL}}"],
  "decision": {
    "authority": "{{DECISION_AUTHORITY}}",
    "approval_ref": "{{EXACT_APPROVAL_REFERENCE}}",
    "lead": "{{LEAD_AGENT_ID}}",
    "reasoning": "high | xhigh | max | ultra",
    "agents": ["{{LEAD_AGENT_ID}}"],
    "reviewers": [],
    "max_corrections": 3,
    "effort_override": "none"
  },
  "external_actions": {
    "allowed": [],
    "prohibited": ["{{EXPLICITLY_PROHIBITED_ACTION}}"]
  },
  "completion_evidence": ["{{TEST_REVIEW_OR_OBSERVATION}}"],
  "agent_start": {
    "applicability": "required | not_applicable_d0",
    "spawn_reviewer": "{{AGENT_ID_OR_NOT_APPLICABLE}}",
    "clearance": "pass | not_applicable",
    "cleared_agents": ["{{LEAD_AGENT_ID_OR_EMPTY_FOR_D0}}"]
  }
}
```
<!-- run-contract:end -->

Use Lead, one independent working reviewer and separate Spawn in `agents`; only the working
reviewer appears in `reviewers`. Ordinary1.5 corrections≤3 by default; a tighter existing limit
remains binding. At most two workers/three total identities concurrently. Historical pre1.5 retains
its pinned rules. Work §10 owns one reserve and one affected closure per material correction; the
last cycle may finish tests/closure. A Mission references its approved total, never a local reset.
Before work, record below a concrete finite working bound including preparation/initial work.
Agent-start clearance survives in-scope candidate corrections; content approval does not.

Only when Collaboration's bounded third-working-reviewer condition has prior Human authority, add
`decision.review_escalation` with exactly `trigger` (`critical_competence_gap` or
`unresolved_material_dissent`), the exact `question`, additional `reviewer` ID and `max_reviews: 1`.
Name the exact conditional Human allocation/amendment in `effort_override` and the actual trigger,
evidence and scope in this Run. Then list both working reviewers plus Lead and Spawn: four allocated
identities, never four working Agents. This adds one focused assessment, no automatic correction.
Keep Spawn outside content quorum and do not overrule blockers by vote. Then run:

```bash
python3 .agentic-harness/validators/validate_harness.py --root . --check-run {{RUN_CONTRACT_PATH}}
```

## Progress And Evidence

For material multi-step work, keep the existing plan/worklist here or link the already maintained
Work/ Human plan: original requirement/source → required result → open/verified state/evidence →
remaining action/dependency. Start from the next open item; update at coherent boundaries and
before pause, with a pointer in the existing handover. Do not copy an existing authoritative list.
At closure, the independent reviewer works from original sources to actual evidence for every
criterion. A wording change, unrelated green suite or aggregate PASS does not fill missing work.

For new ordinary `1.3.1+` Runs, populate this single evidence block from actual task-entry progress,
including preparation. `0` and empty lists below are template seeds, never a reset instruction.
Work §5.1 owns the duty groups/triggers; Ordinary Admission §4.1 owns this structure. Every group
describes the next action and later trigger, with evidence or a justified conditional non-applicability.

<!-- task-controls:start -->
```json
{
  "checked_revision": 1,
  "progress": 0,
  "updates": [],
  "drift_checks": [],
  "obligations": {
    "entry_integrity": {"state": "blocked", "evidence": "{{ENTRY_INTEGRITY_OBSERVATION}}"},
    "scope_authority": {"state": "blocked", "evidence": "{{SCOPE_AUTHORITY_OBSERVATION}}"},
    "agent_start_review": {"state": "blocked", "evidence": "{{START_CURRENT_REVIEW_AND_NEXT_TRIGGER}}"},
    "human_gates": {"state": "blocked", "evidence": "{{CURRENT_GATE_DECISION_OR_NA_AND_NEXT_TRIGGER}}"},
    "capability": {"state": "blocked", "evidence": "{{CAPABILITY_OBSERVATION_OR_NA}}"},
    "mutation_boundary": {"state": "blocked", "evidence": "{{NEXT_ACTION_AND_BOUNDARY_OBSERVATION}}"},
    "budget_stop": {"state": "blocked", "evidence": "{{CONSUMED_REMAINING_BUDGET_AND_STOP}}"},
    "routed_requirements": {"state": "blocked", "evidence": "{{ROUTED_DUE_REQUIREMENTS_AND_EVIDENCE}}"}
  }
}
```
<!-- task-controls:end -->

Each update is an object with `percent` and `evidence` (achieved outcome, next action, blocker).
Each scheduled drift adds `reviewer` and `decision`. Retain every 10/20-percent prefix through
current progress. At 40/80 use a cleared assigned non-author reviewer; D0 alone uses
`not_applicable_d0` while retaining Lead drift. Other checks name the Lead. A missed threshold's
same evidence field states the omission, actual later observation, impact and owning authority's
resolution; never fabricate timely delivery. Refresh checks at each due boundary before rechecking.
This block is evidence, not a second authorization or proof of actual timing/semantic compliance.

An honestly completed partial Run may end below100% of the overall Human task. Carry the actual
percentage into its successor. For a carried drift observation, optionally add `origin_run` with
the original Run's `id` and `revision`, and name that Run in `targets`. Preserve the observation's
four original fields; reference its true origin directly. Its original valid assignment governs
the old check; current assignment governs new checks. Never rewrite historical files or add a
second progress counter to accommodate a reviewer change.

- Finite working bound including preparation and initial implementation: {{BOUND}}
- Authoritative correction owner / total / consumed / remaining: {{THIS_TASK_OR_MISSION_REF_AND_COUNTS}}
- Original outcome / observed sources / assumptions / permitted actions: {{DISTINCT_REFS}}
- Current outcome/progress: {{OUTCOME_PROGRESS}}
- Verification evidence: {{EVIDENCE_OR_PENDING}}
- Findings / residual risk: {{FINDINGS_OR_NONE}}

Missions retain their separately owned Mission envelope and checkpoint controls.

For `domain_foundation`, `targets` name only pre-existing Human, Bootstrap, or input authority; the
Foundation, review pack, and Human Domain Decision are outputs. Downstream Runs target the exact
effective Foundation or the Work Package plus its applicable sources under Domain §12. For affected
Contexts include every exact Foundation/Review or legacy-exception source; for a wholly domain-free
1.4.1+ Package include the existing scope/context sources supporting its `not_applicable_reason`.
