# Module Entry Map — {{BOUNDED_CONTEXT}}

> Artifact ID: `{{PRODUCT}}-MODULE-{{CONTEXT}}`  
> Instantiated artifact class: Navigation  
> Semantic owner: {{OWNER}}

## Purpose And Language

{{ONE_PARAGRAPH_PURPOSE_AND_KEY_TERMS}}

## Read In This Order

1. Effective Domain Foundation/context: `{{PATHS}}`
2. Domain Spec: `{{PATH}}`
3. Public Contracts: `{{PATHS}}`
4. Core Flows: `{{PATHS}}`
5. Code entry: `{{PATH}}`
6. Tests/evidence route: `{{PATHS}}`

## Module And Hexagonal Boundary

- One logical module for this Bounded Context: `{{MODULE_ENTRY_PATH}}`
- Domain/application core: {{DOMAIN_APPLICATION_ENTRY_OR_COMBINED_SMALL_MODULE}}
- Inbound ports and real adapters: {{ACTUAL_ENTRY_CONTRACTS_AND_ADAPTERS_OR_NONE}}
- Outbound ports and real adapters: {{ACTUAL_DEPENDENCY_CONTRACTS_AND_ADAPTERS_OR_NONE}}
- Persistence/framework/UI dependencies remain outside the domain core: {{ENFORCEMENT_OR_NOT_APPLICABLE}}

Create a port, adapter, service, or layer directory only for a real boundary. A small context may
combine files or directories while preserving dependency direction and the public module boundary.

## Context Map

| Direction | Context | Relationship | Contract | Owner |
|---|---|---|---|---|
| {{IN_OUT}} | {{CONTEXT}} | {{TYPE}} | {{ID_PATH}} | {{OWNER}} |

## Avoid Mixing

- {{RESPONSIBILITY_OWNED_ELSEWHERE}}
- No private imports or direct persistence access across contexts.
- {{ADDITIONAL_NEGATIVE_BOUNDARIES}}
