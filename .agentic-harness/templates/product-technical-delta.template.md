# Product Technical Delta — {{PRODUCT}}

> Artifact ID: `{{PRODUCT}}-TECH-DELTA-{{NNN}}`  
> Instantiated artifact class: Product specification  
> Authority: Product-wide technical profile selection and delta  
> Revision status: `draft`  
> Semantic owner: Architecture / Engineering  
> Revision/version: {{REVISION}}  
> Governing artifacts: {{CONSTITUTION_PROFILE_REQUIREMENT_IDS}}  
> Harness: `{{ID_VERSION_DIGEST}}`  
> Selected profiles: `{{ID_VERSION_DIGEST_LIST}}`  
> Review: `{{REVIEW_ID_OR_PENDING}}`

This exact human-approved revision is the product's profile-selection lock; the release manifest only inventories profiles available for selection.

## Applicability Matrix

| Baseline/profile rule | Classification `conforms/strengthens/exception/not_applicable` | Product rule or linked source | ADR/Human Authority |
|---|---|---|---|
| {{RULE_ID}} | {{CLASS}} | {{RULE_OR_LINK}} | {{REF}} |

## Product-Specific NFRs

| ID | User/operational outcome | Metric and conditions | Target | Evidence method |
|---|---|---|---|---|
| {{NFR_ID}} | {{OUTCOME}} | {{PERCENTILE_DATASET_DEVICE_NETWORK}} | {{TARGET}} | {{METHOD}} |

## Data And Privacy

| Field/dataset | Owner | Classification/purpose | Retention/deletion | Logs/analytics/screenshots/LLM | RPO/RTO/backup |
|---|---|---|---|---|---|
| {{DATA}} | {{OWNER}} | {{CLASS_PURPOSE}} | {{RULE}} | {{RULE}} | {{RULE}} |

## Integrations, Compliance, And Domain Constraints

{{TRACEABLE_REQUIREMENTS}}

## Privileged Product Access Bootstrap

- Applicability and Product rationale: `applicable | not_applicable | unresolved` / {{RATIONALE}}
- Product Admin/Backoffice role, use-case, outcome-policy, and prohibited-action references owned by Requirement/Product specs: {{PRODUCT_SPEC_REFS_OR_NOT_APPLICABLE}}
- Server-side authorization/denial, tenant/data-scope, self-elevation-prevention, and audit-event references owned by Domain/Contract specs: {{DOMAIN_CONTRACT_REFS_OR_NOT_APPLICABLE}}
- Navigation, first-access/denial/recovery, and representative Backoffice-flow references owned by Design specs: {{DESIGN_REFS_OR_NOT_APPLICABLE}}
- Staging human test personas and separate automation identities: {{STAGING_IDENTITY_REGISTRY_REFS_OR_NOT_APPLICABLE}}
- First Production Admin protected principal reference, provider tenant/environment, role/scope, and Human Action Owner: {{PROTECTED_REFS_OR_NOT_APPLICABLE}}
- Single-use enrollment method, TTL, forced activation/reset, MFA/step-up, and bootstrap disablement: {{METHOD_RULES_OR_NOT_APPLICABLE}}
- Idempotency/reconciliation for existing, expired, partial, duplicate, wrong-tenant, and conflicting state: {{RULES_OR_NOT_APPLICABLE}}
- Audit fields without credential values; lifecycle, offboarding, recovery, and break-glass Owner: {{RULES_OR_NOT_APPLICABLE}}
- Delivery Slice/Work Package and Production Promotion dependency: {{TRACEABILITY_OR_NOT_APPLICABLE}}
- Explicit exceptions/ADRs/Human risk acceptance: {{REFS_OR_NOT_APPLICABLE}}

No password, temporary credential, invitation value, personal address, or other secret/PII is recorded here. Production privilege creation or invitation remains a separate exact external action, normally bundled into the Production Promotion decision.

This Technical Delta owns technical identity/bootstrap/profile decisions and references the Product, Domain/Contract, and Design owners above; it MUST NOT redefine their role, authorization, tenant, or flow semantics.

## Language, Runtime, And Delivery Toolchain

- Selected stack and rationale: {{TYPESCRIPT_NODE_CDK_DEFAULT_OR_COMPARATIVE_DELTA}}
- Exact Node/runtime, TypeScript/compiler, package manager and lockfile strategy: {{PINS}}
- Exact CDK CLI, `aws-cdk-lib`, Constructs/plugins, Synth command, context and bootstrap assumptions: {{PINS_AND_REFS}}
- Formatter/linter/type/test/build tools: {{PINS}}
- Alternative stack comparison across domain ecosystem, maintainability, library maturity, security, artifact/cold-warm performance, observability, cost, and migration: {{COMPARISON_OR_NOT_APPLICABLE}}

## Cost Model And Exceptions

{{OPERATIONAL_FLOOR_USAGE_SCENARIOS_ADRS}}
