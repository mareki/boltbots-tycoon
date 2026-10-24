# Harness Validators

> Artifact class: Navigation
> Linked owner: `AH-SPEC-EVALUATION-001`

## Ordinary Run Start

For a Harness `1.2.7+` ordinary Run, check only its Contract and exact named targets:

```bash
python3 .agentic-harness/validators/validate_harness.py --root . \
  --check-run docs/work/<run>.md
```

This command does not run repository-wide validation and emits no report or digest. Exit `0` means
the named Contract passed; exit `1` means it did not. The check proves structural scope and authority
only, never semantic correctness or Product quality.

For `1.3.0+`, this direct check also enforces the narrow Domain sequence: Domain creation targets
pre-existing inputs rather than future outputs; Bootstrap Initialization targets the exact
effective Foundation and Human Domain Review; Product Delivery targets its Work Package plus every
Foundation or context-specific Legacy Exception named by the Package. It still performs no broad
repository discovery.

## Repository Validation

Use the separate full validation for CI, upgrades, releases or an expressly requested audit:

```bash
python3 .agentic-harness/validators/validate_harness.py --root . --mode product \
  --expected-manifest-sha256 <trusted-release-manifest-digest>
```

Use `--mode master` in the Master Harness repository and `--format json` for CI. Full validation
checks all owned repository artifacts and installed-Core integrity. Its unrelated findings do not
change a `--check-run` result. Exit `2` means the validator itself could not execute.

Full Product validation additionally checks the structural Domain Foundation, review, Context,
Brownfield adoption, downstream binding, and Legacy Exception blocks. These checks prove schema,
identity, exact references, lifecycle coherence, and file/digest bindings—not domain quality.

Pre-`1.2.7` Admission Reports, Run State Events and Agent Activation Records are read only for
historical compatibility. New ordinary Runs do not create or update them.

Harness1.5 D0 routine needs no Run, WP/Slice, Domain Binding or task-controls form. Do not call
`--check-run` on an invented routine Contract. Delivery RC validation accepts the explicit1.5
routine task identity while retaining actual release/build integrity. Deterministic checks cannot
prove semantic D0 eligibility, real authority, actual CI/provider operation termination or truthful acceptance.
