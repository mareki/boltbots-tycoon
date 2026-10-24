# Product Release Identity Event — {{PRODUCT_VERSION}} / {{SEQUENCE}}

> Artifact ID: `{{PRODUCT}}-RELEASE-IDENTITY-EVENT-{{NNN}}`
> Instantiated artifact class: Evidence
> Observation state: `observed`
> Timestamp/environment: {{TIME_PRODUCT_REPOSITORY_OR_PRODUCTION}}
> Immutable subject: Product version `{{PRODUCT_VERSION}}` / tag `{{PRODUCT_RELEASE_TAG}}`
> Raw evidence references: {{RC_LEDGER_PROVIDER_DEPLOYMENT_TAG_REFS}}
> Product Release Policy ID / revision SHA-256: `{{POLICY_ID}}` / `{{SHA256}}`
> Owning final RC ID / SHA-256: `{{RC_ID}}` / `{{SHA256}}`

## Transition

- Sequence: `{{SEQUENCE}}`
- Previous-event SHA-256: `{{GENESIS_OR_SHA256}}`
- From / to: `{{FROM_STATE}}` / `{{TO_STATE}}`
- Event kind: `reserve | reservation_transfer | consume | reconcile_no_mutation | partial | publish | skip`
- Actor / Decision Authority: {{ACTOR_AUTHORITY}}
- Guard evidence: {{COLLISION_SCOPE_AND_STATE_EVIDENCE}}
- Production mutation observation: `none_proven | occurred | may_have_occurred | not_applicable`
- Recovery Owner / next action: {{OWNER_ACTION}}

State is derived from the append-only digest chain. A transfer retains the same version/tag and changes ownership only to the exact replacement RC atomically. `published` and `skipped` are terminal.
