# Brownfield Harness Adoption State — {{PRODUCT}}

> Artifact ID: `{{PRODUCT}}-HARNESS-ADOPTION-001`
> Instantiated artifact class: Work contract
> Revision status: `active`
> Work status: `active`
> Semantic owner / revision: Harness Adoption / {{REVISION}}
> Governing specifications: `AH-SPEC-DISTRIBUTION-001`, `AH-SPEC-DOMAIN-001`
> Decision Authority: {{HUMAN_AUTHORITY}}

## Inventory, Collision, And Core Identity

- Repository/Git identity and inventory evidence: {{REF}}
- Exact Harness release/tag/source/manifest digest: {{IDENTITY}}
- Collision/symlink/path-escape/no-overwrite result: {{REF}}
- Transaction/recovery record: {{REF_OR_NONE}}

## Integration And Activation

- Root/routing integration plan: {{PATHS_AND_CONTENT_DECISION}}
- Exact Human integration authority: {{REF_OR_PENDING}}
- Verified mandatory entry chain: {{EVIDENCE_OR_PENDING}}
- Activation: `inactive_staged | active`

## Context Coverage

| Context ID | Evidence/path | Coverage `legacy_unmodeled/partially_modeled/domain_model_effective` | Foundation/exception ref | Next trigger |
|---|---|---|---|---|
| {{CONTEXT_ID}} | {{REF}} | {{COVERAGE}} | {{REF_OR_NONE}} | {{TRIGGER}} |

<!-- brownfield-adoption:start -->
```json
{
  "schema_version": "1",
  "adoption_id": "{{PRODUCT}}-HARNESS-ADOPTION-001",
  "harness_version": "{{SEMVER}}",
  "activation": "inactive_staged",
  "root_routing_authority": "pending",
  "entry_chain_evidence": "pending",
  "contexts": [
    {
      "id": "{{CONTEXT_ID}}",
      "coverage": "legacy_unmodeled | partially_modeled | domain_model_effective",
      "foundation_or_exception": "none"
    }
  ],
  "no_overwrite_evidence": "{{EVIDENCE_REF}}",
  "rollback_evidence": "{{EVIDENCE_REF_OR_NOT_APPLICABLE}}"
}
```
<!-- brownfield-adoption:end -->

Staged Core is not an active Harness. Do not add `unassessed` or `candidate` context states; keep
adoption incomplete until discovered in-scope contexts are classified.
