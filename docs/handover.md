# Product Handover

> Artifact class: Navigation  
> Linked owners: `docs/harness-state/bootstrap-and-installation.md` and future active Work/Run/checkpoint artifacts

## Current State

- Product lifecycle: `installed_uninitialized`
- Product/Vision Brief: `not_available` — initialization has not run.
- Domain Foundation: `not_available` — domain modeling has not run.
- Milestone / Delivery Slice / Work Package / Execution Run: `not_available` — no product work is authorized.
- Canonical Bootstrap State: `docs/harness-state/bootstrap-and-installation.md`.
- Last verified state: installed Harness integrity must be checked against `.agentic-harness/manifest.md` and the external trust anchor recorded in Bootstrap State.
- Checkpoint: `non_transferable` until repository and Harness release have an immutable pushed baseline.
- External side effects: none known.

## Human Gate Or Blocker

- Required PRD may not yet exist at `product-input/prd.md`.
- No detailed Product conception or delivery-intended implementation is authorized before the
  Human Domain Decision and Human Initialization Gate.

## Next Safe Action

Verify the installed manifest. Then report that Harness installation is complete, request the
required PRD and optional inputs, provide the command “Initialize this product from the provided
PRD and optional inputs,” and stop. Product initialization begins
only after that separate explicit human instruction. It starts the Domain Foundation Run; stop at its Human Domain Decision before
the separate Bootstrap Initialization Run.

This file is an operational index. It MUST link future canonical product specs, plans, reviews, and checkpoints rather than duplicate them.
