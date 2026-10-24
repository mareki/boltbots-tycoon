# Product Repository

> Artifact class: Navigation
> Linked owners: root `AGENTS.md`, `AH-SPEC-DISTRIBUTION-001`, and product artifacts named below

This repository uses a versioned Agentic Harness to plan, design, implement, verify, and evolve the product with coordinated AI Agents and explicit Human Authority.

## Start Here

Every Agent reads `AGENTS.md`, this README, `docs/handover.md`, `.agentic-harness/manifest.md`, and the task route before reading code or broader documentation.

For Harness `1.3.0+`, an ordinary Run starts from one compact Run Contract. `--check-run` reads only
that Contract and its exact named sources; it creates no report, event, activation file or document
hash. D1-D3 Spawn-review clearance is recorded in the same Contract. Full repository validation is
separate CI/release/audit work.

Harness installation ends with lifecycle `installed_uninitialized`; it does not begin discovery or planning. Commit and push that self-contained baseline first. Then open a separate new Codex task in this Product repository. Codex reads the installed startup chain and requests these inputs:

```text
product-input/prd.md                         required
product-input/technical-requirements.md      optional
product-input/mockups/                       optional PNG/JPG/SVG or HTML/CSS/JS
product-input/research/                      optional
product-input/brand/                         optional
```

After supplying them, explicitly ask: “Initialize this product from the provided PRD and optional
inputs.” Only this separate instruction starts initialization. The first `domain_foundation` Run
proposes the MVP/six-week Bounded Contexts, Context Map,
First-Class Product Objects, structural/behavior model, and module boundaries, then stops for the
Human Domain Decision. Only after approval does a separate `bootstrap_initialization` Run create
the Product Vision, detailed requirements/use cases, contracts, technical/design foundation,
rolling plan, and Human Initialization Review Pack. Both gates stop before functional Product work.

## Operating Boundary

- `.agentic-harness/` is the integrity-pinned, read-only Harness core.
- `product-input/` is human-owned, Agent-read-only intake; Agent drafts and snapshots go under `docs/product/`.
- `docs/` owns product truth, design, plans, work, review, and evidence manifests.
- Material Product code/infrastructure requires approved initialization and an authorized Run.
  D0 routine uses its existing authorized task, diff and focused result evidence without Run/WP/Slice;
  authorized delivery uses Delivery §2.2 routine RC. This does not waive Product initialization.
- `staging` is the integration/deployment branch; Delivery Slices use `slice/<slice-id>` and normally batch modular Work Packages into one final CDK-backed Staging release candidate; `main` tracks the last successfully promoted release lineage.
- The Product Release Policy owns the application version scheme independently from the installed Harness version; final RCs reserve a version, while only successful Production promotion publishes it.

## Product Orientation

Initialization replaces this generic section with the product name, why it exists, target user/outcome, exact Product Vision link, local start/test commands, deployed environment route, Module Entry Maps, and operator/recovery route. It MUST keep the protected startup links above and MUST NOT duplicate canonical product rules.

Current product status and the next safe action live only in `docs/handover.md`.

For material multi-step work, that handover points to the existing plan/worklist with original
requirements, current evidence, open steps and next action. Resume reads it before selecting work.
Optional Harness logging is off unless enabled for the named task; use
`.agentic-harness/workflows/harness-logging.md`. Its concise reports in `docs/harness-logs/**`
are diagnostic references, not another HIP intake, Work hierarchy or completion approval.

Harness learning is proposal-only from Product work: use `.agentic-harness/workflows/propose-harness-improvement.md` and one thorough narrative `docs/harness-proposals/YYYY-MM-DD-<stable-logical-slug>.md`. Do not invent another intake directory. Products never follow `latest`; compatible upgrades replace only `.agentic-harness/**` and then perform a Product-owned impact recalibration.

For an existing Product without the Harness, use `adopt-existing-product.md` / `.sh`. Adoption
first stages `.agentic-harness/**` without overwriting Product-owned root files. Human-owned
root/routing integration and explicit Context coverage activate the Harness later; untouched
legacy Contexts remain non-blocking until work changes them.

The Human-facing upgrade entry is the exact target release's root `upgrade-product.md` / `upgrade-product.sh`. The parameterless script authenticates and swaps one immutable Core, validates it, reports the relevant history, and never mutates Product-owned files or Git state.

An upgrade request binds its target and disclosed changes under Evolution §8; Core replacement preserves Product-owned roots,
CI and notifiers. Recalibration identifies only the consumer changes needed for actual next work.
