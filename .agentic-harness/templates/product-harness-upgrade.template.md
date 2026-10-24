# Product Harness Upgrade — {{OLD_VERSION}} To {{NEW_VERSION}}

> Artifact ID: `{{PRODUCT}}-HARNESS-UPGRADE-{{NNN}}`  
> Instantiated artifact class: Work contract  
> Revision status: `draft`  
> Work status: `proposed`  
> Semantic owner / revision: Product Harness Integration / {{REVISION}}  
> Governing specifications: `AH-SPEC-PRODUCT-UPGRADE-001`, `AH-SPEC-EVOLUTION-001`, `AH-SPEC-DISTRIBUTION-001`, Product Technical Delta
> Decision Authority / independent reviewer / Human Upgrade Approver: {{AUTHORITIES}}
> Target completion level: exact Human-approved Product Upgrade merge

## Repository, Versions, And Trust

- Product ID / repository / authenticated remote / branch / head: {{PRODUCT_REPOSITORY}}
- Current release/version/schema/manifest/tree/trust: {{CURRENT}}
- Target release/tag/version/schema/source commit/manifest/tree/provider trust: {{TARGET}}
- Exact compatibility edge / descriptor ID/path/SHA-256: {{COMPATIBILITY}}
- Canonical plan artifact / SHA-256 / observed-at: {{PLAN}}

## Lifecycle And Existing Work

- Current Product lifecycle and preserved post-upgrade value: {{LIFECYCLE}}
- Completed/cancelled historical Runs and evidence preservation snapshot: {{HISTORY}}
- Proposed/authorized Runs to cancel, supersede, regenerate, or review: {{PROPOSED_WORK}}
- Active/verification/changes-requested/paused/blocked Runs, checkpoints, side effects, and disposition: {{ACTIVE_WORK}}
- Explicit old-pin finish or checkpoint-to-new-Run supersession evidence: {{RUN_BOUNDARY}}

## Impact, Paths, And Decisions

- Protected create/replace/remove diff and changed rule/profile/template/validator IDs: {{PROTECTED_DIFF}}
- `preserve_byte_exact` inventory and digest: {{PRESERVED_PATHS}}
- Declared Product migration operations or exact `none`: {{MIGRATIONS}}
- Transaction-owned state/evidence outputs: {{TRANSACTION_OUTPUTS}}
- Product Technical Delta, regressions, security/privacy/cost impact: {{PRODUCT_IMPACT}}
- Conflicts, Product-semantic choices, non-goals, and exact authority needed: {{DECISIONS}}

## Transaction, Validation, And Recovery

- Upgrade Run/digest, actor, allowed actions/environments: {{RUN_AUTHORITY}}
- Transaction ID, external recovery boundary, journal and before-snapshot digests: {{TRANSACTION}}
- Dry-run/result, idempotent repeat, interruption/recovery evidence: {{TRANSACTION_EVIDENCE}}
- Protected integrity, startup/routing, lifecycle/active-work, migration, preservation, and Product regression evidence: {{VALIDATION}}
- Rollback-before-completion / forward-fix-after-acceptance boundary: {{RECOVERY}}
- Residual risks and exact invalidators: {{RISKS_INVALIDATORS}}

## Machine-Readable Upgrade Binding

```json
{
  "schema_version": "1",
  "operation": "product_harness_upgrade",
  "product_id": "{{PRODUCT_ID}}",
  "current_version": "{{OLD_VERSION}}",
  "current_schema": "{{OLD_SCHEMA}}",
  "current_manifest_sha256": "{{OLD_MANIFEST_SHA256}}",
  "target_version": "{{NEW_VERSION}}",
  "target_schema": "{{NEW_SCHEMA}}",
  "target_manifest_sha256": "{{NEW_MANIFEST_SHA256}}",
  "migration_id": "{{MIGRATION_ID}}",
  "migration_sha256": "{{MIGRATION_SHA256}}",
  "plan_sha256": "{{PLAN_SHA256}}",
  "plan_decision": "{{READY_FOR_AUTHORIZED_APPLY_OR_STOP}}",
  "before_snapshot_sha256": "{{BEFORE_SNAPSHOT_SHA256}}",
  "transaction_evidence_sha256": "{{TRANSACTION_EVIDENCE_SHA256}}",
  "apply_evidence_sha256": "{{APPLY_EVIDENCE_SHA256}}",
  "result_evidence_sha256": "{{RESULT_EVIDENCE_SHA256}}",
  "result_commit": "{{RESULT_COMMIT}}",
  "result_manifest_sha256": "{{RESULT_MANIFEST_SHA256}}",
  "pull_request_head": "{{PR_HEAD_COMMIT}}",
  "proposed_merge_result": "{{PROPOSED_MERGE_RESULT_COMMIT}}",
  "human_decision": "{{PENDING_APPROVED_OR_REJECTED}}",
  "human_decision_evidence_sha256": "{{HUMAN_DECISION_EVIDENCE_SHA256}}",
  "accepted_risks_sha256": "{{ACCEPTED_RISKS_SHA256}}",
  "human_decision_timestamp": "{{HUMAN_DECISION_TIMESTAMP_OR_PENDING}}"
}
```

## Independent Review And Human Gate

{{FINDINGS_DISPOSITIONS_DISSENT}}

- Exact PR/head/proposed merge result and binding digest: {{PR_TARGET}}
- Human Product Upgrade decision (`pending | approved | rejected`) / evidence digest / accepted-risks digest / timestamp: {{HUMAN_DECISION}}
- Invalidators: any plan, apply, result, transaction evidence, PR head, proposed merge result, risk, or Human-decision drift

Opening the PR is not approval. Master Proposal/Merge Approval, credentials, a green dry-run, or an older Product approval does not approve this exact upgrade.
