# Cross-Domain Orchestration Spec — {{FLOW}}

> Artifact ID: `{{PRODUCT}}-ORCHESTRATION-{{NNN}}`  
> Instantiated artifact class: Product specification  
> Authority: Named cross-domain flow  
> Revision status: `draft`  
> Semantic owner: {{OWNER}}  
> Revision/version: {{REVISION}}  
> Governing artifacts: {{VISION_REQUIREMENT_DOMAIN_CONTRACT_IDS}}  
> Review: {{REVIEW_ID_OR_PENDING}}

## Outcome And Boundary

- Vision/user/use-case contribution: {{REFS_AND_OUTCOME}}
- Starts/ends when: {{BOUNDARIES}}
- Coordinates: {{CONTEXT_IDS}}
- Explicitly does not own: {{DOMAIN_RULES_AND_DATA_NOT_OWNED}}

## Flow

| Step | Actor/context | Command/query/event contract | Preconditions/idempotency | Success state | Denial/failure/timeout/compensation |
|---|---|---|---|---|---|
| {{STEP}} | {{OWNER}} | {{CONTRACT_ID}} | {{GUARDS}} | {{OUTCOME}} | {{FAILURE_RECOVERY}} |

## Consistency And Recovery

{{TRANSACTION_BOUNDARIES_ORDERING_RETRY_DUPLICATION_COMPENSATION_OBSERVABILITY}}

## Acceptance, Anti-Criteria, And Evidence

| ID | Observable outcome or prohibited outcome | Required contract/component/real-staging evidence |
|---|---|---|
| {{ID}} | {{CRITERION}} | {{EVIDENCE}} |
