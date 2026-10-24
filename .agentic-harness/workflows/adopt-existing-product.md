# Workflow: Adopt Harness In An Existing Product

> Artifact ID: `AH-VIEW-WORKFLOW-ADOPT-001`
> Artifact class: Generated view
> Source owner/revision: `AH-SPEC-DISTRIBUTION-001`, `AH-SPEC-DOMAIN-001`, exact release manifest
> Generator/source: Master Harness release assembler / canonical workflow projection

## Stage Core Safely

1. Authenticate the exact immutable Harness release and run its `adopt-existing-product.sh` from
   the existing Git repository root.
2. The installer may create only `.agentic-harness/**`. It rejects symlinks, path escapes,
   collisions, an already installed different Core, and any operation that would overwrite a
   Product-owned path. A failed swap restores the prior state.
3. Keep staged Core `inactive_staged`. Installation alone does not change root instructions,
   routing, Product lifecycle, architecture, plans, or historical Contracts.

## Integrate And Cover Incrementally

1. Under explicit Human authority, compare existing root instructions and routing with the staged
   entry chain. Resolve collisions deliberately; never replace Product-owned files automatically.
2. Instantiate one Brownfield Adoption State. Record root/routing authority and classify each
   identified Context only as `legacy_unmodeled`, `partially_modeled`, or
   `domain_model_effective`.
3. Activate the Harness only when the entry chain is reachable and coverage evidence is explicit.
   The protected Manifest then routes to Operating Policy and Work §5.1 task-wide duties, including
   preparation. Staged inactive Core is not an instruction to rewrite Product roots or activate itself.
4. Later work may change a Context only when it binds an effective Domain Foundation revision or a
   context-specific approved legacy exception. This ratchet does not block untouched legacy areas.
5. Model and modularize additional Contexts through ordinary approved work. Prefer one logical
   module per Bounded Context and pragmatic hexagonal boundaries; do not require a big-bang rewrite.

Upgrade remains a separate Core-only operation and never performs these Product-owned decisions.
