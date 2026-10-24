# Install Agentic Harness In A New Product Repository

Copy the prompt below into a new Codex task whose workspace is the Product Git repository. Replace `PRODUCT_ID` with the stable uppercase Product ID, for example `AMPLIFIC`. This task installs only the Harness. Existing non-conflicting Product files are preserved; Product inputs and product initialization belong to a later, separate task.

This is an installation convenience, not an activation template for later work. Once installed,
Manifest → Operating Policy supplies task-wide duties from ordinary Human instructions, including
preparation progress and due drift checks. Installation still grants no Product implementation authority.

```text
Install Agentic Harness 1.5.3 in this repository for PRODUCT_ID.

This instruction authorizes Harness installation only. It does not authorize reading or interpreting a PRD or mockups, product discovery, product initialization, planning, implementation, deployment, credentials, invitations, or any other Product action.

1. Confirm that this workspace is the root of an existing Product Git repository. Existing files such as `.gitignore`, `.DS_Store`, and non-conflicting `docs/**` are allowed and must remain byte-identical; stop only for an exact Harness destination collision or unsafe path type.
2. Confirm Git, Python 3.10+, and authenticated read access to `https://github.com/langvis/agentic_harness.git`.
3. Clone exactly tag `20260930-1.5.3-remove-added-rules` into a safe temporary directory. Never use `main`, another branch, or `latest`.
4. Run that checkout's `bootstrap.sh` with the exact checkout as `--source`, this repository root as `--target`, `PRODUCT_ID` as `--product`, and `--yes`. Do not reproduce its copy or validation logic manually.
5. Remove the temporary checkout after successful installation.
6. Verify that `AGENTS.md`, `README.md`, `docs/handover.md`, and `.agentic-harness/manifest.md` exist and that the lifecycle in `docs/handover.md` is `installed_uninitialized`.
7. Report that Harness installation is complete, recommend committing and pushing this self-contained baseline, explain that a later separately authorized initialization first establishes the Domain Foundation and Human Domain Gate before the remaining Product initialization, and stop.

Do not follow `.agentic-harness/workflows/initialize-product.md` in this task, even when Product inputs already exist. If bootstrap or integrity verification fails, stop with the concrete blocker. Do not claim installation success and do not improvise around the Harness.
```
