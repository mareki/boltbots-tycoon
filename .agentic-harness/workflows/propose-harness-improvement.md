# Workflow: Propose A Harness Improvement

> Artifact ID: `AH-VIEW-WORKFLOW-HIP-001`
> Artifact class: Generated view
> Source owner/revision: `AH-SPEC-EVOLUTION-001`, exact release manifest
> Generator/source: Master Harness release assembler / canonical workflow projection

## Product-Local Proposal

1. Verify Product Vision, installed Harness version/manifest digest, active Run authority, and exact product observation/evidence.
2. Create or revise only one `docs/harness-proposals/YYYY-MM-DD-<stable-logical-slug>.md` from the governed HIP template; retain a stable HIP Artifact ID. Never create `docs/change-requests/**` or another Harness-learning intake, and never edit root `AGENTS.md`, `.agentic-harness/**`, a Master checkout, release, Product code, or Product pin.
3. Write a thorough causal narrative: original Human assignment/problem statement; relevant Product and Agent chronology; observed inter-Agent coordination/review behavior; resulting Product/user outcome; cost/rework/trust impact; and why the Harness—not only the Product—owns the gap.
4. Keep confirmed/direct evidence, Human-reported observations, causal hypotheses/confidence, evidence gaps, and open decisions visibly separate. Do not fabricate hidden Agent reasoning or use verbosity/word count as a substitute for evidence.
5. Generalize the requested outcomes; state applicability/counterexamples, Product-local/no-change alternatives, simplicity/cost, Harness version class, separate compatibility/migration/eval implications, success/anti-criteria, and non-goals.
6. Remove raw PRD/code/log/screenshot content, Product/customer names and IDs, secrets, PII, proprietary rules, and restricted material. Record provenance, rights, redaction, retention/access, scan evidence, and residual limits.
7. Obtain independent Product/Process, Architecture/Delivery, and Devil/Simplicity review. Preserve findings, dispositions, dissent, and rejected/deferred/duplicate outcomes.
8. Stop at exact Human Proposal Approval. This gate may authorize one clean proposal-only upstream PR and preparation of a separate Master Run path; it does not authorize implementation.

## Proposal-Only Upstream Pull Request

Only when exact Human authority includes upstream submission:

1. Verify the authenticated canonical upstream and immutable base/head.
2. Use a clean branch whose base-to-head diff and every commit touch exactly the one approved dated HIP Markdown file—no transient Core, workflow, validator, test, release, Product-code, or competing-intake path.
3. Run proposal validation with the exact Git base and head. Rename/delete history does not erase a prohibited touch.
4. Push and open the proposal-only PR only when those external actions are authorized. Bind the final HIP digest and independent findings.
5. Stop. The proposal PR records learning; it does not implement it.

## Authorized Upstream Elaboration

Only after Proposal Approval and independently authorized Master execution:

1. Create a separate Master Execution Run bound to the exact HIP digest, verified canonical upstream `https://github.com/langvis/agentic_harness.git`, immutable base commit, `work/<hip-id>` branch, external-action authority, reviewers, budgets, and stop.
2. Re-run privacy/license/provenance/secret checks on the exact upstream payload.
3. Implement generalized Core/spec/template/migration/eval changes in the separate Master work branch; do not edit installed Product Core and do not reuse the proposal-only PR.
4. Run validators/evals and independent reviews; open the PR only if the Run authorizes push/PR actions.
5. Bind PR/provider IDs, base/head/merge candidate, HIP, Run digest, findings, compatibility, migrations, release notes, and Evidence.
6. Stop at Human Merge Approval for the exact PR/commit. Any material drift invalidates it.
7. After merge, release automation may create the immutable version authorized by the Master Run. It does not upgrade the originating product.

Rejected or deferred HIPs remain product-local records. Resubmission needs new evidence.
