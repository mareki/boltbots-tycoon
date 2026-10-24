# Governed Artifact Templates

> Artifact class: Navigation  
> Linked owners: `AH-SPEC-ARTIFACTS-001`, `AH-SPEC-DISTRIBUTION-001`, and the owning workflow/specification named by each template

Every `.template.md` file in this directory has primary payload class `Reference`. Its `Instantiated artifact class` line defines the single primary class of a product artifact created from it; instantiation rewrites that label to `Artifact class`, resolves all required fields, assigns a stable ID/revision, and applies the owning lifecycle. The template itself never authorizes product behavior.

| Template | Instantiated class | Owning contract |
|---|---|---|
| `architecture-proposal.template.md` | Product specification | `AH-SPEC-ENGINEERING-001` |
| `bootstrap-and-installation-state.template.md` | Work contract | `AH-SPEC-DISTRIBUTION-001` |
| `brownfield-adoption-state.template.md` | Work contract | `AH-SPEC-DISTRIBUTION-001` |
| `checkpoint-and-evidence.template.md` | Evidence | `AH-SPEC-WORK-001` |
| `contract-spec.template.md` | Product specification | `AH-SPEC-ENGINEERING-001` |
| `decision-record.template.md` | Decision record | `AH-SPEC-ARTIFACTS-001` |
| `delivery-slice.template.md` | Work contract | `AH-SPEC-WORK-001` |
| `design-system-and-flow.template.md` | Product specification | `AH-SPEC-DESIGN-001` |
| `domain-foundation-review-pack.template.md` | Review record | `AH-SPEC-DOMAIN-001` |
| `domain-foundation.template.md` | Product specification | `AH-SPEC-DOMAIN-001` |
| `domain-spec.template.md` | Product specification | `AH-SPEC-DOMAIN-001` |
| `execution-run.template.md` | Work contract | `AH-SPEC-WORK-001` |
| `eval-case.template.md` | Work contract | `AH-SPEC-EVALUATION-001` |
| `harness-improvement-proposal.template.md` | Decision record | `AH-SPEC-EVOLUTION-001` |
| `harness-log.template.md` | Reference | `AH-SPEC-WORK-001` §9.1 |
| `initialization-review-pack.template.md` | Review record | `AH-SPEC-INITIALIZATION-001` |
| `milestone-and-six-week-plan.template.md` | Work contract | `AH-SPEC-WORK-001` |
| `module-entry-map.template.md` | Navigation | `AH-SPEC-ENGINEERING-001` |
| `orchestration-spec.template.md` | Product specification | `AH-SPEC-ENGINEERING-001` |
| `product-technical-delta.template.md` | Product specification | `AH-SPEC-INITIALIZATION-001` |
| `product-release-policy.template.md` | Product specification | `AH-SPEC-PRODUCT-RELEASE-001` |
| `product-release-identity-event.template.md` | Evidence | `AH-SPEC-PRODUCT-RELEASE-001` |
| `product-release-record.template.md` | Evidence | `AH-SPEC-PRODUCT-RELEASE-001` / `AH-SPEC-DELIVERY-001` |
| `product-delivery-rc-manifest.template.md` | Evidence | `AH-SPEC-DELIVERY-001` |
| `product-harness-upgrade.template.md` | Work contract | `AH-SPEC-EVOLUTION-001` |
| `product-vision-brief.template.md` | Product specification | `AH-SPEC-INITIALIZATION-001` |
| `requirement-and-use-case-register.template.md` | Product specification | `AH-SPEC-INITIALIZATION-001` |
| `review-record.template.md` | Review record | `AH-SPEC-COLLABORATION-001` |
| `technical-risk-experiment.template.md` | Work contract | `AH-SPEC-WORK-001` |
| `work-package.template.md` | Work contract | `AH-SPEC-WORK-001` |

For a new Product, instantiate the Domain Foundation and its review pack before detailed Product,
UX, technical, or delivery artifacts. For Brownfield adoption, stage Core first; instantiate the
adoption state only after a Human-owned root/routing integration decision. Templates do not make
staged Core active and never authorize overwriting Product-owned files.

The opt-in diagnostic log remains a Reference under Work §9.1, identified by its existing task
and report path; it needs no separate artifact ID, revision lifecycle or D0 Run. Instantiate it
only for explicit task logging, not during installation or every routine task.
