# Workflow: Resume Or Transfer Work

> Artifact ID: `AH-VIEW-WORKFLOW-RESUME-001`  
> Artifact class: Generated view  
> Source owner/revision: `AH-SPEC-WORK-001`, exact release manifest  
> Generator/source: Master Harness release assembler / canonical workflow projection

## Cross-Person Or Cross-Machine Transfer Preconditions

- checkpoint is marked `transferable`;
- all resume-relevant in-scope work is committed and pushed;
- Harness version/digest, artifact/deployment IDs, external state, and last green rollback are referenced.

If any condition fails, do not claim safe transfer. Ask the prior owner/human to create a safe checkpoint or explicitly authorize bounded salvage/recovery from `non_transferable` state.

## Same-Owner Local Resume

A `non_transferable` checkpoint may be resumed only by the same owner in the same verified workspace after exact dirty-state, Harness integrity, repository, environment, side-effect, remaining authority/budget verification. The owner records why transferability is unnecessary. Another person or machine requires explicit salvage authority, preservation of the original state, a new clean checkpoint, and MUST NOT claim the old state was safely transferred.

## Resume

If this task has an explicit Harness-logging state, recover that state and its report path from
the existing task/Run/handover context. Follow [the logging workflow](harness-logging.md): continue
the same enabled report, respect a later disable, and do not activate logging for a new task.

Resume is part of the same task: carry earlier progress, reports, drift checks, findings and consumed
budgets without reset or a second delegated percentage sequence. Read the owner’s current
status/next action; earlier observations remain labeled history. Refresh Work §5.1 coverage for the exact next action. Existing checkpoints
reference the ordinary Run's one `task-controls` block; historical Runs are not silently migrated.
Missing or previously skipped checks require explicit truthful resolution before affected work.

1. Read mandatory entry chain and the linked existing material-work plan before selecting work.
   Recover all original requirements, actual evidence, open steps and decisions, not only the last
   subtask. Then read exact Vision, Run, Slice, Package or Experiment revisions;
   read the applicable Foundation/coverage or existing sources supporting explicit domain-free
   applicability under Domain §12. Recheck that justification against the current scope on resume.
2. Verify manifest integrity and, for transfer, fetch the named remote commit without overwriting unrelated local work; for same-owner local resume, match the recorded clean/dirty state exactly.
3. Compare remote/branch/dirty state, Product Delivery Release Candidate classification/digest, CI, artifact/deployment, Staging/provider side effects, attempts, findings, and Human Decisions with checkpoint.
4. For a Mission, compare its exact Run/Package revisions, readable pre-mutation intent reference (pre1.5.1: digest), actual path mapping, assumptions/triggers, invariant/evidence state, remaining total budget, dependency baseline, next eligible item, and continuation decision. Any mismatch is drift and forbids silent continuation.
5. Reuse valid evidence; rerun only checks invalidated by observed state changes. Resolve material
   acceptance through Deployment history → RC → final immutable Review, not local status labels.
   Missing/contradictory evidence cannot prove activation. Classify pipeline failure before retry: a
   changed candidate needs affected checks; archive/notifier repair never requires redeployment.
6. Revalidate the exact Foundation revision or Brownfield legacy exception for every changed
   Context. A stale/withdrawn Foundation or newly uncovered Context stops only affected work.
7. Revalidate the assignment clearance. Changed responsibility/authority requires a new Spawn
   pass. An in-scope candidate correction or review metadata alone does not; changed content still
   needs affected review. D0 resumes from task/diff/evidence without new Work objects or controls.
8. For an ordinary non-Mission Run, invoke
   `--check-run` against the exact current Contract and its named targets, then set its status back
   to `active`. Work §10 counts the next coherent correction once against the existing task/Mission
   reserve; the last cycle may finish tests/closure. Administrative completed work reenters only
   under Work §7 with valid original mandate/work bound/reserve and non-author reviewed revision.
9. Perform the checkpoint's single next safe action within remaining Run scope/budget. A changed
   scope, authority, target, allowed action or budget requires an authorized Contract revision and
   another direct check rather than silent continuation.

Drift creates a new checkpoint, correction authorization, or replanning decision. Never silently continue from a different commit, environment, Harness release, spec, or provider state.

If a material Contract field changes, reach a safe state, obtain the declared Decision/Human
Authority, increment the revision, record the reason there and run the direct check again. Git
preserves the earlier revision.
