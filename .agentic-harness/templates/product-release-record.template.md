# Product Release Record — {{PRODUCT_VERSION}}

> Artifact ID: `{{PRODUCT}}-RELEASE-{{VERSION_SLUG}}`
> Instantiated artifact class: Evidence
> Observation state: `observed`
> Timestamp/environment: {{PRODUCTION_COMPLETION_TIME_ENVIRONMENT}}
> Immutable subject: Product version `{{PRODUCT_VERSION}}` / tag `{{PRODUCT_RELEASE_TAG}}`
> Raw evidence references: {{PIPELINE_DEPLOYMENT_LEDGER_TAG_AND_SMOKE_REFS}}
> Version scheme: {{SCHEME}}
> Product Release Policy ID / revision SHA-256: `{{POLICY_ID}}` / `{{SHA256}}`
> Final Product Delivery RC ID / SHA-256: `{{RC_ID}}` / `{{SHA256}}`
> Source commit / tree SHA-256: `{{GIT_COMMIT_40_TO_64_HEX}}` / `{{SHA256}}`
> Application Artifact Set SHA-256: `{{SHA256}}`
> Migration Set SHA-256: `{{SHA256}}`
> Production Assembly Tree SHA-256: `{{SHA256}}`
> Deployment Ledger event SHA-256: `{{SHA256}}`

## Publication Result

- Product / published version / immutable tag: {{PRODUCT}} / `{{PRODUCT_VERSION}}` / `{{PRODUCT_RELEASE_TAG}}`
- Human Production Approval: {{REF}}
- Trusted pipeline/build and actual deployment IDs: {{REFS}}
- Production smoke/activation result: {{RESULT_REFS}}
- Publication/tag observation: {{REF}}

## Serving State And Recovery

- Prior current-serving Product version/artifacts: {{VERSION_REFS_OR_NONE}}
- New current-serving Product version/artifacts: {{VERSION_REFS}}
- Rollback/forward-fix target and owner: {{REF_OWNER}}
- Known limitations and release notes: {{REFS}}

This record exists only after successful Production promotion. The Deployment Ledger remains operational truth; this record and its Git tag do not independently prove current serving state.
