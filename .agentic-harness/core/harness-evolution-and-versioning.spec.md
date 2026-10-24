# Harness Evolution And Versioning

> Artifact ID: `AH-SPEC-EVOLUTION-001`
> Artifact class: Harness specification
> Authority: Canonical
> Status: Active
> Semantic owner: Master Harness Governance
> Version: 1.0.2
> Governing artifacts: `AH-CONSTITUTION-001`, `AH-SPEC-ARTIFACTS-001`, `AH-SPEC-COLLABORATION-001`, `AH-SPEC-WORK-001`, `AH-SPEC-DISTRIBUTION-001`
> Review: `AH-REV-1-5-1-COMPLETION-DIAGNOSTICS-001` (acceptance and evidence limits in the referenced Review; prior historical reviews retained)
> Owns: product-originated learning, Harness Improvement Proposals, upstream authority, master pull requests, versioning, releases, migrations, product adoption, and rejection history

## 1. Purpose And Non-Authority

Optional task reports under Work §9.1 at `docs/harness-logs/**` are local diagnostic observations,
not a second HIP intake or improvement approval. A requested cross-report analysis may cite them
and distinguish recurring observations from hypotheses; proposals still follow §3 and upstream
data minimization under §4. Recording alone never authorizes uploads or silent rule changes.

Product experience SHOULD improve the Harness, but an observation in one Product is not automatically a reusable rule. A Product Agent may analyze evidence and create a Harness Improvement Proposal (`HIP`) only under `docs/harness-proposals/**`. The HIP is a thorough narrative Markdown record named `YYYY-MM-DD-<stable-logical-slug>.md`; its stable Artifact ID survives revisions and an approved file move. Product Agents MUST NOT invent another Harness-learning intake, edit installed Core, mutate a Master checkout, open/push/merge upstream work, publish a release, or upgrade the Product unless the exact later authority exists.

The canonical upstream is `https://github.com/langvis/agentic_harness.git`, GitHub repository ID `1328705370` (`R_kgDOTzJvWg`) under owner ID `288767329` (`O_kgDOETY9YQ`). These repository-owned values are descriptive, not a self-authenticating trust anchor. Before remote or release action, the execution environment supplies independently protected expected numeric repository/owner IDs; authenticated provider metadata MUST match them and this specification. Preflight also binds remote URL, default/target branch, base commit, authenticated principal, permissions, and immutable provider IDs. A matching repository name, fork, URL string, branch, local remote, or repository-edited configuration is not proof of identity.

## 2. Evolution Lifecycle And Three Human Gates

```text
product observation
  -> local narrative HIP draft/review
  -> Human Proposal Approval
  -> authorized proposal-only upstream PR and archival record
  -> separate authorized Master Run on work/<hip-id>
  -> separate generalized implementation PR + independent reviews/evals
  -> Human Merge Approval for exact PR/commit
  -> immutable Harness release
  -> authenticated Product Core replacement
  -> Product-owned recalibration
```

The three approvals are independent and non-transferable:

1. **Proposal Approval** accepts the exact HIP for upstream elaboration and permits its authorized proposal-only PR plus preparation of a bounded Master Run/implementation-PR path. It never authorizes a merge. Merging even the archival proposal PR requires a separately named Human Merge Approval bound to its exact head and proposed merge result; the two decisions MAY share one Human interaction but remain distinct authority records. Proposal Approval does not approve the Master Run Contract, either merge, release, or adoption.
2. **Master Merge Approval** applies only to the exact reviewed PR head and resulting merge candidate. Material change invalidates it. It does not approve any product upgrade.
3. **Product Migration Approval** applies whenever adoption requires changing Product-owned files, independently of the Harness version class. Compatible `.agentic-harness/**` replacement and read-only recalibration do not invent a routine Product PR or Human Gate.

Reversible analysis, branch work, PR creation, reviews, CI, and release assembly need no additional Human Gate when explicitly covered by the relevant approved Run. Agents MUST NOT collapse the three gates or invent more routine gates.

## 3. Harness Improvement Proposal Contract

A HIP is a versioned Decision proposal. Its Markdown schema is narrative rather than a checklist substitute and includes:

- HIP ID/status/owner, source Product ID, installed Harness version/manifest digest, and exact observation/evidence references;
- an executive incident narrative and the original Human assignment/problem statement;
- relevant chronology: how Codex/Agents worked, what they produced, how Agents coordinated/reviewed, and which observed decisions or omissions led to the result;
- Product/user/process outcome, Human evaluation, cost/rework/trust impact, frequency, severity, affected roles/workflows/specs, and why the Harness—not only the Product—owns the gap;
- visibly separate confirmed observations, Human-reported observations, causal hypotheses, confidence/evidence gaps, and open decisions; raw private reasoning is not fabricated or required upstream;
- generalized rule hypothesis, applicability boundary, counterexamples, and Products for which it should not apply;
- alternatives including product-local handling and no change, rejected options, non-goals, simplicity/cost impact, and expected benefit;
- expected Harness version class, separate compatibility/migration/rollback implications, validators/evals to add, and success/anti-criteria;
- provenance, confidentiality, privacy, secret, license, and upstream-data review;
- independent Product/Process, Architecture/Delivery, and Devil/Simplicity findings, dispositions, and remaining dissent;
- exact Human Proposal decision.

Narrative quality is judged from causal usefulness, evidence boundaries, and decision value. Word count, heading count, or rhetorical detail alone cannot pass semantic review. The Master ships one template that preserves these headings without forcing raw Product identifiers, screenshots, source, logs, or private Agent transcripts upstream.

Lifecycle: `draft -> local_review -> awaiting_human_proposal_decision -> approved_for_upstream | rejected | deferred | duplicate -> upstream_in_progress -> upstream_pr_open -> released | closed`. Rejection/defer/duplicate remains traceable; resubmission requires new evidence or changed applicability.

Proposal Approval MAY authorize a local Product workaround only when normal Product authority allows it. A workaround remains Product-owned; it MUST NOT impersonate Core or silently weaken it.

### 3.1 Proposal-Only Upstream Pull Request

After exact Human Proposal Approval and explicit upstream authority, the Product may push one clean proposal branch and open one proposal-only PR. Its final base-to-head diff and every intervening commit contain exactly one dated HIP Markdown file under `docs/harness-proposals/**`; no transient or final Core, workflow, validator, test, release, Product-code, or competing Harness-learning-intake mutation is permitted. Rename/delete sequences do not erase prohibited commit history. Ordinary Product documents outside a Harness-learning submission are not reserved by generic words such as “change request.”

The proposal PR records learning and its reviews; it does not implement the requested outcomes. If accepted, the Master creates a separate Work Contract, `work/<hip-id>` branch, and implementation PR. Rejected/deferred/duplicate proposals remain traceable without becoming policy.

## 4. Data Minimization And Provenance

Upstream material is deny-by-default. The Master payload MUST NOT contain raw PRD text, product code, internal names/IDs, credentials, secrets, personal/customer data, production logs, screenshots, proprietary business rules, or license-restricted third-party material unless the human and applicable legal/data authority explicitly approve the exact content.

The upstream package uses the minimum generalized, redacted, aggregated, or synthetic reproduction. Before Master mutation it records source provenance, usage rights, redaction, secret/PII scan, residual re-identification risk, and why each retained datum is necessary. A detected secret/private key, unresolved rights, or unnecessary personal/customer datum blocks upstream work.

## 5. Master Run And Pull Request

After Proposal Approval, the team creates a separate Master Execution Run with:

- exact HIP revision/digest and approval;
- canonical upstream identity, verified base commit, `work/<hip-id>` branch, allowed files/actions, author, independent reviewers, budgets, and stop boundary;
- prohibited product repository/Core mutation and prohibited direct writes to protected default/release branches;
- affected specs, migrations, compatibility range, release notes, validator/eval plan, and rollback;
- remote credential capability by reference and no secrets in Agent context/evidence.

The Agent may create and push the work branch and open the implementation PR only when the Run explicitly authorizes those external actions. That PR is separate from the proposal-only PR and binds HIP, Run Contract ID/revision, source/base/head commits, findings/dispositions, compatibility/migration, deterministic checks, agentic eval evidence, and Dissent.

Product/Process, Architecture/Delivery, and Devil/Simplicity independently review the exact candidate. The author cannot approve. A one-product preference becomes Core only when the applicability boundary and general value are evidenced; otherwise reject, defer, create an optional profile, or keep it product-local.

## 6. Merge, CI, And Release Integrity

Human Merge Approval is bound to the exact PR head and proposed merge result. Protected merge/queue CI reruns required validators and evals on the exact resulting commit. Drift, force-push, changed dependency/fixture/eval, failed check, or different merge commit invalidates approval and returns to review.

A release is assembled only from the verified merged commit on the authenticated canonical default branch using the source lock and distribution rules. The assembler derives the source commit and origin from Git; caller-provided labels cannot replace observed provenance. The commit MUST descend from the exact Human-approved base/merge candidate, and product repository history is forbidden as a Master branch ancestor. Two assemblies from identical inputs MUST produce the same protected-payload digest. The Release Record binds:

- SemVer, immutable source commit/tag/provider IDs, manifest and tree digests, profile/core inventory, schema and compatibility range;
- deterministic build/tool inputs, provenance/attestation or externally trusted expected manifest digest;
- migration chain, release notes, known limitations, validation/eval evidence, and rollback/forward-fix path.

The repository contains only the reviewed Release Evidence Policy and Eval definitions; it never self-attests the hash of its own future commit. Formal asset publication is fail-closed unless an immutable Release Attestation supplied and digest-pinned outside the repository binds the exact source commit, Source/Eval/Policy digests, passed deterministic CI, every required agentic Eval trial and its digest-verified raw artifact, a separate non-trial review artifact for each case, independent council Review, and provider-observed Human Merge Approval. The assembler independently re-observes repository/owner identity, same-repository `work/<hip-id>` PR, exact base/head/merge commit, a linear PR commit chain without foreign/merge history, and an externally expected non-author human approver on the exact head. It paginates all provider review/commit events and derives the latest review per stable provider user by submitted time plus immutable event ID; an older approval cannot hide a later dismissal or changes request. Every completed release is installable from its immutable tag; there is no release-candidate or non-installable release state. Published tags/assets are immutable. A defect produces an advisory and new version; it never replaces an existing release or moves a `latest` dependency. Release automation uses least-privilege short-lived identity and cannot approve its own merge.

For new1.4.0+ ordinary tagged-source publication, Evaluation§5.1 owns the bounded work-sample
default. Required scoped deterministic checks, independent review, immutable source authentication
and Human publication authority remain binding. The formal asset-attestation requirements above
apply only to that explicitly selected distribution/assurance profile; missing formal evidence
must remain visible but is not automatically required by the ordinary tagged-source path.

## 7. Harness Version Classification And Compatibility

A completed cohesive change batch is released once as an immutable tag named `YYYYMMDD-<exact-semver>-<stable-logical-name>` after its scoped verification, independent review, commit, and push. The eight-digit date and SemVer MUST equal the release date and Release Plan; for example `20260811-1.0.6-idempotent-core-upgrades`. Trivial intermediate edits do not receive their own tags. The default release increment changes only the final numeric version component. A Major-version change requires explicit prior Human authorization; an Agent MAY recommend it with compatibility evidence but MUST NOT select it autonomously. Released versions are installable; the repository does not model a separate candidate/installability switch.

Harness versions use `MAJOR.MINOR.PATCH` syntax with this project-specific scope classification.
They do not promise strict SemVer backward compatibility: compatibility is disclosed separately.

- **Major:** a new Harness generation or fundamental redesign of its architecture/execution model;
  explicit prior Human authorization is mandatory.
- **Minor:** substantial capabilities or optimizations within the existing Harness architecture.
- **Patch:** bounded fixes/refinements without a substantial capability or architecture change.

Workflow, authority, schema and consumer changes MUST be described in the impact history with their
actual compatibility, migration and recovery implications. A Minor label does not imply semantic
compatibility or authorize Product changes. Supported starting version/schema pairs prove only the
technical Core replacement path. The Product's own release policy and SemVer meaning are unchanged.

The Human classifies the proportionate-execution improvements as `1.5.0`: an optimization of the
existing Harness, with the disclosed workflow/consumer changes retained. Artifact-internal spec
versions are independent of the Harness release number and are not renumbered retroactively.

Each compatible release declares exact supported starting Harness-version/overlay-schema pairs and carries an immutable, contiguous impact-history entry for every adjacent release edge. The upgrader replaces `.agentic-harness/**` once, even across several versions, then routes all intervening history entries to Product recalibration. Downgrade is unsupported unless separately designed and authorized. A missing, ambiguous, or non-contiguous history edge stops before replacement.

The final numeric version component is the normal compatible-release increment. Any required change outside `.agentic-harness/**` is outside the Core replacement boundary and requires a separately authorized Product migration. No version class authorizes overwriting Product-owned files.

A patch may correct an internally contradictory control sequence when it adds no Product-owned
migration and preserves the intended authority/safety boundary. Restoring Human-authorized
pre-Run analysis/preparation while retaining fail-closed mutation admission is such a semantic
correction; it MUST include the adjacent impact-history and regression evidence that demonstrate
both the removed false block and preserved negative controls.

Likewise, `1.3.1` corrects already-binding task-wide duties and their protected entry routing. Its
compact current-Run evidence makes existing checks inspectable; it introduces no Product behavior,
new approval, or automatic Product-file migration. Historical Runs remain pinned, while new tasks
use the installed correction and current template. Regression evidence must cover actual old Root
entry chains, D0 proportionality, truthful recovery, and the Core-only replacement boundary.

Changing required evals or thresholds is a separate reviewed change. Evaluation§5.1's Human-approved
prospective bounded profile is such a change, not evidence that old Cases passed. Preserve locked
old Cases/failures and contracts; do not remove an observed defect or weaken its oracle to pass a
sample. Any further profile/threshold change needs its own explicit authority and independent review.

## 8. Product Core Replacement And Recalibration

Products never auto-follow a branch, mutable tag, or `latest`. The release-specific parameterless entrypoint fixes and authenticates one immutable target tag, verifies the installed protected identity and complete history chain, replaces only `.agentic-harness/**`, validates the target, and reports the relevant history entries. It does not require or create a Git branch, clean Product worktree, Run disposition, plan digest,
Product PR, commit or push. Core replacement under an authorized upgrade request adds no duplicate Human Gate. The request
binds the fixed target and its disclosed changes under Distribution §8; a supported technical
version/schema pair is not Product migration authority. Replacement still swaps Core only.

The Product team then performs one read-only semantic comparison between the intervening history and current Product Vision, plans, Slices, Work Packages, Runs, design, and evidence. It records one Product-owned recalibration result without rewriting those artifacts automatically. `required_before_continue` blocks affected future work until handled; `deferred` names a trigger; `human_decision` identifies the exact decision. Product-owned migration remains separate and explicit.

## 9. Security Urgency And Stop Rules

A security issue may use private reporting, restricted evidence, shortened review time, and an expedited Run. It never permits self-merge, mutable release replacement, silent product rollout, fabricated evidence, or bypass of the applicable human decisions.

Stop for upstream identity mismatch, unavailable release authority, product-data leakage, unclear licensing, failing required check, non-reproducible assembly, missing history edge, unsupported product version, invalid protected target, or unrecoverable replacement state.

## 10. Acceptance And Anti-Criteria

Accept only when every lifecycle step has one authority, exact immutable targets, bounded actions, Evidence, and a stop boundary; rejected learning remains traceable; generalization is justified; and adoption is reversible or has an explicit forward-fix path.

Reject direct product-to-master mutation, Proposal Approval reused for merge/adoption, self-review, product-specific leakage, release from dirty/mutable input, overwritten release assets, automatic Product-file mutation, heuristic ownership, or redundant Human Gates for already-authorized compatible Core replacement.
