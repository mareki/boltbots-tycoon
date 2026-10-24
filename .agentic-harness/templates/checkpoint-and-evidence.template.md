# Checkpoint And Evidence Index — {{RUN}}

> Artifact ID: `{{PRODUCT}}-CHECKPOINT-{{NNN}}`  
> Instantiated artifact class: Evidence  
> Observation state: `observed`  
> Timestamp/environment: {{TIME_ENVIRONMENT}}  
> Immutable subject: {{RUN_REVISION_SOURCE_COMMIT_AND_EXTERNAL_STATE}}  
> Raw evidence references: {{IMMUTABLE_REFS_AND_DIGESTS}}  
> Transferability: `transferable | non_transferable`  
> Run/Milestone/Delivery-Slice/Feature-Capability/Package or Experiment IDs: {{IDS}}  
> Harness/profile pins: {{IDS_VERSIONS_DIGESTS}}  
> Evidence owner: {{OWNER}}

## Repository And Shared Resources

- Repository/remote/branch/pushed commit: {{REFS}}
- Dirty files and proof unrelated, or non-transferable recovery: {{STATE}}
- Active collaborators: {{AGENTS}}

## Artifact, Pipeline, And Environment State

- Source/spec/mockup revisions: {{REFS}}
- Product Delivery Release Candidate classification/digest, application/migration/CDK assembly IDs: {{REFS_OR_NA}}
- CI/staging Deployment IDs and target environment: {{REFS}}
- External/provider side effects and cleanup: {{STATE}}
- Last green rollback: {{REF}}

## Criteria And Evidence Map

| Acceptance/anti-criterion | Highest completion level | Raw immutable evidence | Result / not-observed |
|---|---|---|---|
| {{ID}} | {{LEVEL}} | {{REF_DIGEST}} | {{RESULT}} |

Include required local/tests, pipeline, real staging flows, critical-user review, screenshots/mockup comparison, redacted logs/metrics, resources/tags/security/cost, reviews, and Human Decisions.

For a Package boundary, distinguish `slice_ready` from parent-Slice Staging evidence. For a Slice boundary, bind the exact final candidate; for an early candidate, preserve `verification_candidate/non_promotable` and cleanup/restore evidence.

## Mission Continuation Guard Or Explicit Absence

- Mission ID or `none`: {{MISSION_ID_OR_NONE}}
- Mission / Run / current Package revisions and digests: {{EXACT_BINDINGS_OR_NA}}
- Pre-mutation intent reference and permitted outcome/owner/path/environment/action set: {{INTENT_OR_NA}}
- Actual changed-path to Package-and-Mission outcome mapping reference: {{PATH_MAP_OR_NA}}
- Current acceptance/regression/integration evidence and invariant result: {{EVIDENCE_OR_NA}}
- Reversible assumptions, evidence, validation triggers, fallbacks, and authority boundaries or `none`: {{ASSUMPTIONS_OR_NA}}
- Findings/dispositions and adjacent follow-ups with owner/trigger or `none`: {{FINDINGS_OR_NA}}
- Attempts and remaining Package/Mission Agent/review/correction/time/external-action/cost budgets: {{BUDGET_OR_NA}}
- Dependency/baseline drift and next eligible item: {{DEPENDENCY_NEXT_OR_NA}}
- Continuation decision `continue | stop | escalate | complete`: {{DECISION_OR_NA}}
- Decision guard evidence / exact escalation need: {{GUARD_OR_NA}}

`continue` requires mapped changes, current evidence/assumptions, passing invariants, closed blocking findings, remaining budget, an authorized next item, and the required pushed transferable checkpoint. Field presence proves structure only, not semantic correctness.

For an active Mission instantiate the corresponding deterministic binding:

<!-- mission-checkpoint:start -->
```json
{
  "schema_version": "1",
  "mission_id": "{{MISSION_ID}}",
  "run_id": "{{RUN_ID}}",
  "run_sha256": "{{RUN_SHA256}}",
  "package_id": "{{PACKAGE_ID}}",
  "package_sha256": "{{PACKAGE_SHA256}}",
  "instantiation_index": 0,
  "decision_class": "D1",
  "outcomes": ["{{OUTCOME_ID}}"],
  "semantic_owners": ["{{OWNER_ID}}"],
  "changed_paths": ["{{SAFE_RELATIVE_CHANGED_PATH}}"],
  "environments": ["{{ENVIRONMENT_OR_NONE}}"],
  "external_actions": ["{{ACTION_OR_NONE}}"],
  "agent_activations_used": 1,
  "corrections_used": 0,
  "mission_agent_activations_remaining": 1,
  "mission_corrections_remaining": 1,
  "next_item": "{{NEXT_PACKAGE_ID_OR_NONE}}",
  "next_item_sha256": "{{NEXT_PACKAGE_SHA256_OR_NONE}}",
  "decision": "continue"
}
```
<!-- mission-checkpoint:end -->

## Failures And Findings

| Signature/finding | Attempt/hypothesis/change | Evidence/result | Remaining budget/closure |
|---|---|---|---|
| {{ID}} | {{DETAIL}} | {{REF}} | {{STATUS}} |

## Progress And Drift

Carry task-entry/preparation progress, findings and consumption; never reset on activation/resume.
For an ordinary `1.3.1+` Run, reference its current `task-controls` block and checked revision here,
including any explicitly missed-duty resolution. Do not copy it into a second status authority.
Missions retain their existing checkpoint control below; all tasks follow Work §5.1 triggers.

- Outcome-based progress checkpoint: `{{10_20_30_40_50_60_70_80_90_100}}`
- Achieved outcome/evidence and next bounded action: {{RESULT_NEXT}}
- Scheduled or event trigger: `progress | drift_20 | drift_40 | drift_60 | drift_80 | drift_100 | critical_recurrence`
- Original purpose/Scope Lock to actual path/mechanism mapping: {{MAP}}
- Unmapped breadth or complexity and remove/defer/simplify/rollback/reimplement result: {{DISPOSITION}}
- Budget lineage / prior + current consumption / remaining total / finish forecast: {{BUDGET_STATE}}
- Independent validator or applicable quorum and decision: {{ACTORS_DECISION}}

Progress updates remain in active communication or this existing checkpoint/event family; do not create a durable file per percentage.

## Resume Index

- Existing plan/worklist reference, open original requirements and pending evidence: {{PLAN_OPEN_REFS}}

For1.5.1+ Mission checkpoints the intent/path fields above reference readable sections at exact
revisions; do not calculate two manual hashes. Historical checkpoints keep their pinned fields.
The existing Run/Package/RC artifact digests remain intact.

- Exact next single safe action: {{ACTION}}
- Governing Run revision and authority remaining / gates: {{AUTHORITY}}
- Stop condition: {{STOP}}
- Capability or decision needed: {{NEED}}

This index does not create or expand authority; the exact active Run remains the Work Contract. `transferable` is valid only if all resume-relevant in-scope work is committed/pushed, pins and immutable artifacts exist, external state is verifiable.

D0 routine resumes from its task/diff/result evidence and does not instantiate this template.
For1.5 Missions, `corrections_used` is cumulative across the whole Mission; it plus remaining
must equal the authoritative total. Item fields only reference that total. No separate convergence
remediation/review ledger or new IDs to reset consumption. The last allowed cycle may complete
its tests/closure with zero remaining; another mutation requires new authority. Administrative
reentry follows Work §7 with non-author reviewed revision and still-valid original mandate.
Resolve material acceptance through Deployment history → RC → final Review; preserve failed or
unavailable evidence rather than deriving acceptance from Work/navigation labels.
