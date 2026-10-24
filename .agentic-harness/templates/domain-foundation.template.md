# Domain Foundation — {{PRODUCT}}

> Artifact ID: `{{PRODUCT}}-DOMAIN-FOUNDATION-001`
> Instantiated artifact class: Product specification
> Authority: Product-wide domain horizon and context boundaries
> Revision status: `draft`
> Semantic owner: {{OWNER}}
> Revision: {{REVISION}}
> Governing artifacts: `AH-SPEC-DOMAIN-001`, {{REQUIREMENT_INPUT_IDS}}
> Review/Human decision: {{REVIEW_AND_DECISION_OR_PENDING}}

## Scope And Evidence Classes

- Provisional Product scope/domain horizon: {{MVP_AND_SIX_WEEK_HORIZON}}
- Confirmed requirements: {{IDS}}
- Derived hypotheses: {{IDS}}
- Blocking/direction decisions: {{IDS_OR_NONE}}

Before adding content, use these existing sections to reference sufficiently evidenced C1–C3
meaning and identify actual missing/conflicting meaning with brief reasons. This is no new matrix
or coverage lifecycle. Adopt exact retrievable sources with explicit ownership; elaborate only
gaps or necessary consolidation. A manifest is not a semantic approval. Thin/conflicting inputs
still need the relevant decisions; rich input does not require rewriting or one file per heading.

## C1 — Domain Framing

### Ubiquitous Language

| Term ID | Context | Exact meaning | Rejected synonym/confusion | Evidence |
|---|---|---|---|---|
| {{TERM_ID}} | {{CONTEXT_OR_GLOBAL}} | {{MEANING}} | {{BOUNDARY}} | {{REQ_USE_CASE_OR_HYPOTHESIS}} |

### Actors, Roles, Processes, Context Candidates

{{ACTORS_ACCOUNTS_MEMBERSHIPS_TENANTS_CORE_PROCESSES_CONTEXT_CANDIDATES_AND_ALTERNATIVES}}

## C2 — Structural Model

The referenced Domain Specs own Aggregate/Entity/Value-Object details, relationships,
cardinalities, ownership/tenancy, invariants, and negative boundaries. This Foundation owns their
Product-wide index and Context Map.

| Context ID | Responsibility / not-owned | Coverage | Domain Spec | Logical module boundary |
|---|---|---|---|---|
| {{CONTEXT_ID}} | {{BOUNDARY}} | {{COVERAGE}} | {{PATH}} | {{MODULE_ID_AND_RESPONSIBILITY}} |

## C3 — Behavior And Impact

{{LIFECYCLE_PERMISSION_USE_CASE_CROSS_CONTEXT_FIRST_CLASS_AND_DOWNSTREAM_IMPACT_SUMMARY}}

## Context Map And Bound Diagram

{{CONTEXT_MAP_WITH_RELATIONSHIP_DIRECTION_TRANSLATION_CONSISTENCY_AND_FAILURE_OWNERSHIP}}

<!-- domain-foundation:start -->
```json
{
  "schema_version": "1",
  "foundation_id": "{{PRODUCT}}-DOMAIN-FOUNDATION-001",
  "revision": 1,
  "revision_status": "draft",
  "effectiveness": "pending_human_decision",
  "horizon": {
    "mvp": "{{MVP_HORIZON}}",
    "six_week": "{{SIX_WEEK_HORIZON}}"
  },
  "contexts": [
    {
      "id": "{{CONTEXT_ID}}",
      "name": "{{CONTEXT_NAME}}",
      "coverage": "legacy_unmodeled | partially_modeled | domain_model_effective",
      "domain_spec": "{{REPOSITORY_RELATIVE_PATH}}",
      "logical_module": "{{LOGICAL_MODULE_ID}}"
    }
  ],
  "diagram": {
    "source": "{{REPOSITORY_RELATIVE_SOURCE_PATH}}",
    "render": "{{REPOSITORY_RELATIVE_RENDER_PATH}}",
    "generator": "{{GENERATOR_AND_VERSION}}",
    "source_sha256": "{{SHA256}}",
    "render_sha256": "{{SHA256}}"
  },
  "open_decisions": [],
  "review_ref": "pending",
  "human_decision_ref": "pending"
}
```
<!-- domain-foundation:end -->

## Traceability, Scenarios, And Decisions

{{ELEMENT_RELATION_INVARIANT_FIRST_CLASS_TO_REQUIREMENT_USE_CASE_OR_HYPOTHESIS_LINKS}}

{{POSITIVE_NEGATIVE_BOUNDARY_SCENARIOS}}

Only an exact Human outcome `approved | approved_with_overrides` for this revision may advance the
artifact through the normative revision lifecycle and set `effectiveness` to
`domain_model_effective`. A Module Entry Map becomes mandatory only when a Context is
implementation-ready. Detailed MVP, contracts, architecture, IA/navigation/routing, mockup,
Slice/Package/Run planning, and Product implementation remain blocked before effectiveness.
