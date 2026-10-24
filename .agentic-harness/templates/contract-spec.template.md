# Contract Spec — {{CONTRACT_NAME}}

> Artifact ID: `{{PRODUCT}}-CONTRACT-{{NNN}}`  
> Instantiated artifact class: Product specification  
> Authority: Cross-context public contract  
> Revision status: `draft`  
> Provider/semantic owner: {{OWNER}}  
> Consumers: {{CONSUMERS}}  
> Revision/version/compatibility: {{REVISION_VERSION_POLICY}}  
> Governing artifacts: {{IDS}}  
> Review: {{REVIEW_ID_OR_PENDING}}

## Purpose And Boundary

{{USER_DOMAIN_PURPOSE_AND_WHAT_THIS_CONTRACT_DOES_NOT_OWN}}

## Operation / Event

- Kind: `command | query | event | protocol`
- Input/schema: {{REFERENCE_OR_DEFINITION}}
- Output/schema: {{REFERENCE_OR_DEFINITION}}
- Semantic units/meaning: {{SEMANTICS}}

## Behavior

| Case | Preconditions/auth | Result/state/event | Error/denial semantics | Idempotency/retry |
|---|---|---|---|---|
| success | {{RULE}} | {{RESULT}} | n/a | {{RULE}} |
| {{FAILURE}} | {{RULE}} | {{RESULT}} | {{STABLE_ERROR}} | {{RULE}} |

## Guarantees And Limits

{{ORDERING_CONSISTENCY_CONCURRENCY_TIMEOUT_RATE_LIMIT_SIZE}}

## Data And Logging

{{CLASSIFICATION_REDACTION_RETENTION}}

## Conformance And Evidence

| Adapter/consumer | Required shared core | Mode-specific cases | Real staging evidence/not-observed |
|---|---|---|---|
| {{PARTY}} | {{TEST_IDS}} | {{TEST_IDS}} | {{EVIDENCE_PLAN}} |

## Migration And Deprecation

{{EXPAND_BACKFILL_VALIDATE_SWITCH_CONTRACT_REMOVAL}}
