# Workflow: Promote To Production

> Artifact ID: `AH-VIEW-WORKFLOW-PROMOTE-001`  
> Artifact class: Generated view  
> Source owner/revision: `AH-SPEC-DELIVERY-001`, exact release manifest  
> Generator/source: Master Harness release assembler / canonical workflow projection

## Default Human Gate

Production Promotion is not implied by Milestone, Slice technical acceptance, Staging, or PR approval. The human approves the exact final Product Delivery Release Candidate Manifest, its `reserved_unpublished` intended Product version and proposed immutable Product release tag, Product Release Policy revision, Production target, Run, migrations, action, and accepted risk.

Human Approval is an authorization prerequisite, not a Run-state transition and not a deployment action.

## Pre-Promotion

- verify the current lifecycle state. A first Production launch may remain `pre_customer` under its rules. A transition to `live_customer_data` is a separate Human Gate requiring the declared data, migration, restore, recovery, and ownership evidence;
- verify byte-identical application/migration artifacts already exercised on staging;
- verify the final candidate owns its exact reservation and fail closed on any conflicting active reservation, consumed/partial/skipped/published state, Product Release Record, or local/remote Product tag;
- verify exact immutable Production CDK assembly/diff from the same trusted Product Delivery Release Candidate provenance;
- compare permitted staging/production differences; run policy/security/drift/unmanaged-resource checks;
- confirm staging evidence freshness, WAF rollout, test/monitoring, cost impact, rollback/roll-forward, Recovery Owner, and external side effects;
- when privileged Product access applies, verify exact Human Approval binds protected personal principal reference, provider tenant/environment, Product role/tenant scope, single-use method/expiry, MFA/step-up, idempotency/reconciliation, Activation/Recovery Owners, and bootstrap disablement; Initialization approval alone is insufficient;
- confirm Production role is assumable only by this protected human-gated job.

Any rebuild, resynthesis, context change, source/spec drift, or changed artifact creates a new final Product Delivery Release Candidate and returns to Staging verification. A `verification_candidate` is never promotable.

## Run Activation

1. Complete Capability Preflight for the exact Production Run, role, account/region, artifacts/diff, migration, smoke, evidence capture, side effects, cost, and recovery.
2. After verifying the exact Human Approval reference, the predeclared Decision Authority records `preflight -> authorized`.
3. Record `authorized -> active` under Work §5.
4. State drift, changed preflight evidence, or approval mismatch causes immediate safe stop before further mutation.

## Promotion

1. Record Human Approval for the exact candidate, intended Product version/tag, Policy revision, and Production action.
2. Immediately before the first Production mutation, append Product version state `consumed_for_promotion`, then deploy the exact manifest to Production.
3. Run safe, non-destructive smoke without creating customer data.
4. If exactly approved, reconcile the managed identity-provider state and perform the single authorized personal Product Admin enrollment/invitation. Never receive, print, store, or evidence its value. Identical completed state is a no-op; expired/partial/duplicate/wrong-tenant/wrong-role/conflicting state stops without automatic re-invite.
5. Remain in `verification` until required protected Human activation/reset/MFA and redacted role/tenant/denial evidence exist, or pause honestly for that Human action. Consume/disable temporary bootstrap capability after success.
6. Immediately append actual deployment/current-serving and privileged-access state—without credentials—to the governed Ledgers.
7. On success, create/push the exact Product tag on the candidate commit and re-observe provider resolution; only then finalize the immutable Product Release Record, append release state `published`, update current-serving Product-version evidence, advance `main` to the exact lineage, preserve evidence, transition the Run `active -> verification -> completed` and perform authorized notifications.
8. On crash/failure after `consumed_for_promotion`, reconcile provider/deployment evidence. Restore `reserved_unpublished` only when no Production mutation is proven; otherwise append `consumed_partial` plus actual serving/recovery state. Retry tag/record/branch reconciliation idempotently without repeating deployment. Only the same exact candidate may complete; otherwise append `skipped` and roll/forward with a new version. Keep `main` at prior success until complete, transition to `blocked` or `paused`.

Material final acceptance is resolved through Deployment history → RC → final immutable Review.
A1.5 routine RC uses exact task/outcome evidence instead of synthetic Slice acceptance; this
Production operation still has its own D3 Human authority and applicable reviewed Run. Candidate A
approval never carries to changed B. Atomic version/tag uniqueness remains protected.
