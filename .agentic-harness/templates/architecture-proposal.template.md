# Architecture Proposal — {{PRODUCT}}

> Artifact ID: `{{PRODUCT}}-ARCHITECTURE-001`
> Instantiated artifact class: Product specification
> Authority: Product-wide technical topology and delivery shape
> Revision status: `draft`
> Semantic owner: Architecture / Engineering
> Revision/version: {{REVISION}}
> Governing artifacts: `AH-SPEC-DOMAIN-001`, exact effective Foundation {{FOUNDATION_REF}}, {{PROFILE_DECISION_IDS}}
> Review: {{REVIEW_ID_OR_PENDING}}

## Simplest Deployable Shape

- MVP/first-six-week boundary: {{SCOPE}}
- Architecture style and why: {{STYLE}}
- Deployment/runtime topology: {{TOPOLOGY}}
- Security/data/quality/design/delivery/cost owners: {{GLOBAL_SPEC_REFS}}
- Rejected more-complex and less-sufficient alternatives: {{ALTERNATIVES}}

## Context-To-Module Map

| Context ID | Logical module/code root | Public contract | Domain/Application/real ports/adapters | Deployment disposition |
|---|---|---|---|---|
| {{ID}} | {{PATH}} | {{CONTRACT_IDS}} | {{STRUCTURE_OR_COMBINED_RATIONALE}} | {{SHARED_OR_SPLIT_WITH_EVIDENCE}} |

## Cross-Context And External Boundaries

| Owner | Boundary/purpose | Contract/port | Adapter/mode | Consistency/failure owner | Evidence |
|---|---|---|---|---|---|
| {{OWNER}} | {{PURPOSE}} | {{CONTRACT}} | {{ADAPTER}} | {{RULE}} | {{REF}} |

## Decisions, Risks, Migration, And Recovery

{{ADRS_EXCEPTIONS_SECURITY_COST_MIGRATION_RECOVERY}}

Do not add an interface, adapter, layer directory, service, database split, or shared abstraction
without a current boundary/requirement and observable benefit.
