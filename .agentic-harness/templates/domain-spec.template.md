# Domain Spec — {{BOUNDED_CONTEXT}}

> Artifact ID: `{{PRODUCT}}-DOMAIN-{{CONTEXT}}-{{NNN}}`  
> Instantiated artifact class: Product specification  
> Authority: Bounded context  
> Revision status: `draft`  
> Semantic owner: {{OWNER}}  
> Version: {{VERSION}}  
> Governing globals: {{IDS}}  
> Domain Foundation/context revision: {{FOUNDATION_AND_CONTEXT_REF}}
> Review: {{REVIEW_ID_OR_PENDING}}

## Purpose And User Contribution

- Vision/outcome link: {{VISION_AND_OUTCOME}}
- Owned responsibility: {{RESPONSIBILITY}}
- Explicitly not owned: {{NEGATIVE_BOUNDARIES}}

## Ubiquitous Language

| Term | Exact meaning | Not to be confused with |
|---|---|---|
| {{TERM}} | {{MEANING}} | {{BOUNDARY}} |

## Invariants And Policies

| Rule ID | Invariant/policy | Success | Failure/denial | Requirement/use-case/hypothesis refs | Test IDs |
|---|---|---|---|---|---|
| {{RULE_ID}} | {{RULE}} | {{OUTCOME}} | {{OUTCOME}} | {{TRACEABILITY}} | {{TESTS}} |

## State Model

{{STATES_TRANSITIONS_GUARDS_AUTHORITY}}

## Structural Model

| Element ID/name | Kind | Responsibility and identity semantics | Aggregate/root | Ownership/tenancy | Lifecycle authority | Requirement/use-case/hypothesis refs |
|---|---|---|---|---|---|---|
| {{ELEMENT}} | {{ENTITY_VALUE_OBJECT_AGGREGATE_POLICY}} | {{RESPONSIBILITY_IDENTITY}} | {{AGGREGATE_REF_OR_NONE}} | {{OWNERSHIP}} | {{AUTHORITY}} | {{TRACEABILITY}} |

### Relationships

| Relation ID | From element + cardinality | Relationship semantics | To element + cardinality | Aggregate/boundary constraint | Invariant/source refs |
|---|---|---|---|---|---|
| {{RELATION_ID}} | {{FROM_CARDINALITY}} | {{SEMANTICS}} | {{TO_CARDINALITY}} | {{CONSTRAINT}} | {{TRACEABILITY}} |

## Actors, Permissions, Use Cases, And Product Objects

| Actor/role | Permission boundary | Use case/trigger | Preconditions | Success outcome | Failure/denial/recovery | First-Class Product Object | Requirement/contract refs |
|---|---|---|---|---|---|---|---|
| {{ACTOR}} | {{BOUNDARY}} | {{USE_CASE}} | {{PRECONDITIONS}} | {{SUCCESS}} | {{FAILURE_DENIAL_RECOVERY}} | {{OBJECT}} | {{REFS}} |

## Commands, Queries, Events

| ID | Kind | Semantics | Contract reference |
|---|---|---|---|
| {{ID}} | {{TYPE}} | {{MEANING}} | {{CONTRACT_ID}} |

## Data Ownership And Privacy

{{OWNED_DATA_ACCESS_RETENTION_LOG_RULES}}

## Context Relationships And Orchestration

{{CONTEXT_MAP_LINKS}}

## Acceptance And Anti-Criteria

{{OBSERVABLE_REQUIREMENTS_AND_PROHIBITED_OUTCOMES}}

<!-- domain-context:start -->
```json
{
  "schema_version": "1",
  "context_id": "{{CONTEXT_ID}}",
  "foundation_id": "{{FOUNDATION_ID}}",
  "foundation_revision": 1,
  "status": "draft | approved",
  "implementation_readiness": "modeled | implementation_ready",
  "module_entry": "not_required | {{REPOSITORY_RELATIVE_PATH}}",
  "review_ref": "{{REVIEW_REF_OR_PENDING}}",
  "elements": [
    {
      "id": "{{ELEMENT_ID}}",
      "kind": "aggregate_root | entity | value_object | domain_service | external_concept",
      "responsibility": "{{RESPONSIBILITY_AND_IDENTITY}}",
      "aggregate": "{{AGGREGATE_ID_OR_SELF_OR_NOT_APPLICABLE}}",
      "ownership": "{{OWNERSHIP_RULE}}",
      "tenancy": "{{TENANCY_OR_NOT_APPLICABLE_WITH_REASON}}",
      "lifecycle_authority": "{{AUTHORITY_OR_NOT_APPLICABLE_WITH_REASON}}",
      "trace_refs": ["{{REQUIREMENT_USE_CASE_OR_HYPOTHESIS_ID}}"]
    }
  ],
  "relationship_disposition": "modeled | none_with_reason: {{DOMAIN_REASON}}",
  "relationships": [
    {
      "id": "{{RELATION_ID}}",
      "from": "{{ELEMENT_ID}}",
      "from_cardinality": "one | zero_or_one | one_or_more | zero_or_more | many",
      "semantics": "{{RELATIONSHIP_SEMANTICS}}",
      "to": "{{ELEMENT_ID}}",
      "to_cardinality": "one | zero_or_one | one_or_more | zero_or_more | many",
      "boundary": "{{AGGREGATE_OR_CONTEXT_CONSTRAINT}}",
      "trace_refs": ["{{REQUIREMENT_USE_CASE_OR_HYPOTHESIS_ID}}"]
    }
  ],
  "invariants": [
    {
      "id": "{{RULE_ID}}",
      "rule": "{{INVARIANT}}",
      "failure_or_denial": "{{PROHIBITED_STATE_OR_DENIAL}}",
      "trace_refs": ["{{REQUIREMENT_USE_CASE_OR_HYPOTHESIS_ID}}"]
    }
  ],
  "use_cases": [
    {
      "id": "{{USE_CASE_ID}}",
      "actor_or_role": "{{ACTOR_OR_ROLE}}",
      "permission_boundary": "{{ALLOWED_AND_DENIED_SCOPE}}",
      "preconditions": "{{PRECONDITIONS}}",
      "success": "{{SUCCESS_OUTCOME}}",
      "failure_or_denial": "{{FAILURE_DENIAL_OR_RECOVERY}}",
      "first_class_disposition": "{{FIRST_CLASS_OBJECT_OR_REJECTED_WITH_REASON}}",
      "trace_refs": ["{{REQUIREMENT_OR_HYPOTHESIS_ID}}"]
    }
  ]
}
```
<!-- domain-context:end -->
