# Delivery, Staging, And Recovery

> Artifact ID: `AH-SPEC-DELIVERY-001`  
> Artifact class: Harness specification  
> Authority: Canonical  
> Status: Active  
> Semantic owner: Master Harness Delivery  
> Version: 1.0.4
> Governing artifacts: `AH-CONSTITUTION-001`, `AH-SPEC-WORK-001`, `AH-SPEC-ENGINEERING-001`, `AH-SPEC-PRODUCT-RELEASE-001`, `AH-PROFILE-AWS-SERVERLESS-MVP-001`
> Review: `AH-REV-1-5-3-REMOVE-ADDED-RULES-001` (acceptance and limits in the referenced Review; prior historical reviews retained)
> Owns: Delivery-Slice Git flow, Product Delivery Release Candidates, adaptive deployment cadence, CI/CD, local/mock/real verification, staging, regression, production promotion, Product release publication evidence, action authority, pipeline correction, rollback, and recovery

## 1. Branch And Environment Flow

The default flow is:

```text
slice/<slice-id> -> staging -> main
                         |         |
                         v         v
                    staging env  production env
```

- A short-lived Slice Branch starts from the latest verified `staging` commit.
- Agents may commit and push that branch when the Execution Run authorizes it. Work Packages normally become coherent commits and checkpoints on the Slice Branch; their CI/review does not trigger a Staging deployment by default.
- Every included Package reaches `slice_ready` before the final Slice candidate is integrated against current `staging`. Required CI runs on the resulting integration commit. Drift from reviewed specs/contracts triggers affected re-review. Only that exact integration commit may become the final Slice release candidate and deploy Staging.
- `staging` is the integration branch and deploy target, not the default shared WIP branch.
- `main` represents the source lineage of the last successfully promoted release and is protected. It is not evidence of the currently running cloud state; the immutable Deployment Ledger is operational truth.
- Direct mutation on `staging` requires explicit Human Exception and is never the default.

Material-work commits identify Delivery Slice and Work Package IDs; routine commits reference their task and contain coherent, reviewable state. Safe checkpoints are pushed at package and Slice boundaries and before authorized interruption when possible. Generated evidence and large binaries use the configured artifact store rather than bloating Git, while manifests remain versioned.

## 2. Pipeline Architecture

### 2.1 Fast Validation

Runs on Slice Branch pushes and pull requests, with affected-scope selection at Work-Package commits:

- Markdown/spec metadata, route, link, contract, traceability, and boundary validation;
- format, lint, types/static analysis, dead/unused dependency checks appropriate to the stack;
- unit, UI component, application, and contract tests selected by affected scope;
- secret, dependency, license, SAST, and IaC security checks;
- CDK format/test/synth and reviewed infrastructure diff;
- build/package reproducibility and artifact manifest.

Repository-local or open-source CLI analysis is preferred initially; a permanent paid analysis server is not required. Reports are retained as CI artifacts with stable finding IDs and dispositions.

### 2.2 Slice Release Candidate, Staging Build, And Deploy

The default clean path creates one final Staging deployment per coherent change. Concurrent
observations bind the exact target; a later mutation invalidates only observations that require
unchanged state. No separate coordination or lease form is required for1.5.2+ RCs.
Merge of the final Slice candidate into `staging`:

1. verifies the exact Slice/Package revisions, source commit, active specs, approved Target Specs, closed package findings, and `slice_ready` states;
2. builds the deployable application and migration artifacts exactly once;
3. in the same trusted build provenance, pins source/spec digests, runtime/compiler/package-manager/CDK/construct versions, lockfiles, context and bootstrap assumptions, and produces immutable environment-specific Staging and Production CDK assemblies/diffs;
4. creates an immutable **Product Delivery Release Candidate Manifest** binding all identities and artifacts below, including the exact Product release identity required by `AH-SPEC-PRODUCT-RELEASE-001`;
5. deploys the Staging assembly through CDK with the staging role;
6. runs health/smoke, selected real integration and complete critical Slice E2E flows;
7. captures relevant screenshots, logs, metrics, deployment state, public exposure, resource/tag inventory, and cost forecast;
8. maps evidence to Slice and included-package acceptance/anti-criteria, closes critical-user and technical findings, and submits the exact candidate for Slice technical acceptance.

A successful deployment event alone is not `staging_verified`; the required product behavior must be observed.

The Product Delivery Release Candidate Manifest is distinct from the Harness Release Manifest. It binds:

- Product and work identity: material Slice/Milestone/Package bindings below, or the1.5 routine variant defined below;
- for a `final` candidate, intended Product version and proposed immutable Product release tag in `reserved_unpublished` state plus exact approved Product Release Policy ID/revision/digest; for a `verification_candidate`, explicit `not_applicable` Product version, tag, and Policy binding;
- final `staging` merge commit, source tree, active and approved-target specification digests, migrations, generated API/schema assets, and product-data lifecycle state;
- application, frontend/static, Lambda/function, migration, and other deployable artifact digests;
- exact lockfiles, dependency inventory/SBOM, Node/runtime, TypeScript/compiler, package-manager, CDK CLI, `aws-cdk-lib`, Constructs/plugin versions, Synth command, CDK context, and bootstrap assumptions;
- immutable Staging and Production cloud-assembly tree digests, templates/assets, environment parameters, reviewed diffs, and permitted environment differences;
- trusted build/pipeline/provenance identity, creation time, expiry/retention, prior green recovery candidate, and `final | verification_candidate` classification.

Any relevant source, spec, package, migration, dependency, toolchain, context, assembly, diff, or artifact change invalidates the candidate. A new candidate repeats affected CI and candidate-specific Staging evidence, reusing unaffected
checks/build artifacts only when their relevant inputs remain unchanged; IDs or manifests MUST NOT be edited to hide drift.

### Routine Work Identity

A1.5 D0 task may use this existing RC/delivery path without creating Milestone, Slice, Package,
Domain Binding or independent material Review. The RC states `Harness version: 1.5.0` (or later),
`Work identity: routine`, `Task reference`, `D0 rationale`, `Delivery authority`, and source commit.
Omit Slice/Milestone/Package/Feature digest fields and package rows. Material RCs retain their
complete bindings. Classification remains `final | verification_candidate`, not a third type.
Final version reservation, Production Gate and relevant source/spec/build/toolchain/provenance/
assembly/recovery identity remain; existing build data generates digests rather than manual lists.
The responsible Agent checks the exact requested result and actual deployment evidence: a green
pipeline alone does not prove the right title. A routine final candidate's outcome evidence replaces
material Slice acceptance only for this explicitly bounded variant. No material spec activates.

The Human task or approved Product delivery policy must actually authorize target/action. Local
edit permission alone does not authorize Staging. Existing pipeline security checks and Production
approval remain. If Product tooling requires the old hierarchy, disclose the narrow unsupported
path and propose its separately authorized adaptation; do not forge missing Work objects.

### 2.3 Adaptive Verification Deployments

An internal Work Package does not deploy merely because it completed local review. The Slice Contract evaluates early real-environment evidence when a concrete IAM/CDK diff, migration, authentication, external provider, central public contract, high uncertainty, or high blast-radius risk would make waiting for the final Slice candidate materially less safe.

An early candidate:

- is preauthorized by the Slice Contract and active Run with hypothesis, target, side effects, cost, data, max count, cleanup/restore, and evidence goal;
- receives its own immutable Product Delivery Release Candidate Manifest classified `verification_candidate` and `non_promotable`;
- binds no intended Product version or Product release tag and cannot reserve, publish, consume, or imply one;
- runs preferably in an isolated preview/verification environment with owner, Slice/Run ID, TTL, cost tags, and automated cleanup;
- may use shared Staging only with explicit `unverified` status, stable test-target isolation, and restoration of the last green final candidate afterward;
- cannot activate Target Specs, move a Package/Slice to technical completion, satisfy final Staging acceptance, or enter Production promotion.

A correction deployment after a failed final-candidate review is allowed only inside the Slice correction budget and creates a new final candidate identity. Thus “one final deploy” is the default clean path, not an unsafe one-attempt dogma.

### 2.4 Scheduled Regression

A separate scheduled workflow runs a focused regression suite nightly when a persistent staging environment exists. It includes critical user outcomes, auth/denial, contract/provider health, and selected visual/accessibility checks at a scope whose cost fits the operational floor. A broader suite MAY run less frequently according to risk and cost.

Failure sends an actionable e-mail or approved team notification with product/environment, source/artifact/deployment IDs, failed flow/test, first failure evidence, logs, owner, and triage link. A stable incident/finding key deduplicates an acknowledged open failure and escalates by policy instead of sending an endless identical-message storm. Scheduled retries are bounded and never hide the original failure.

### 2.5 Production Promotion

Production promotion deploys the byte-identical application and migration artifacts exercised on Staging. Infrastructure is environment-specific: the Promotion job uses the exact Production CDK assembly/diff already bound into the final Product Delivery Release Candidate Manifest, verifies parity and permitted environment differences against the Staging assembly, and performs policy, security, drift, and concrete Production-diff review. After the Human Gate it MUST NOT rebuild, resynthesize, or change context; any change creates a new final candidate and repeats Staging verification.

The sequence is:

1. freeze the exact Staging source commit and final Product Delivery Release Candidate Manifest, including its `reserved_unpublished` intended Product version, proposed immutable Product release tag, and Product Release Policy revision;
2. verify the final RC owns its exact reservation and fail closed on any conflicting active reservation, consumed/partial/skipped/published state, Product Release Record, or local/remote Product tag; then verify staging evidence, Production assembly/diff, migration/rollback, lifecycle, and drift; when privileged Product access applies, also verify the protected personal principal reference, provider tenant/environment, Product role and tenant/data scope, enrollment mode/expiry, MFA/step-up rule, idempotency/reconciliation behavior, Activation and Recovery Owners, redacted evidence, and bootstrap-disablement plan;
3. obtain Human Approval naming manifest, intended Product version/tag, target, Run, action, and any real privileged-access enrollment/invitation;
4. immediately before the first Production mutation, append version state `consumed_for_promotion`, then deploy Production and run safe post-deploy smoke;
5. when the exact approval includes privileged Product bootstrap, reconcile provider state, perform the one authorized enrollment/invitation without exposing its value, and remain in `verification` until required protected Human activation/MFA plus redacted role/tenant/denial evidence exists; pause honestly while Human activation is pending;
6. on successful deployment, immediately append actual deployment/current-serving state; after smoke/activation/bootstrap success, create and push the exact Product tag, re-observe its provider resolution, finalize the immutable Product Release Record from those observations, append Product release state `published`, and only then advance `main` to that exact lineage;
7. on crash/failure after `consumed_for_promotion`, reconcile actual provider/deployment evidence: append restoration to `reserved_unpublished` only when no Production mutation is proven; otherwise append `consumed_partial`, actual current-serving state, and recovery evidence, keep `main` at the prior successful release, and never repeat deployment merely to repair tag/record/branch state. Only the same exact candidate may complete publication; otherwise append terminal `skipped` and roll/forward with a new version.

The Product Release Identity Ledger records version ownership and publication state. The Deployment Ledger records Product version/tag/Policy revision, final candidate and source commit, application/migration/Production-assembly digests, approved Production diff, human decision, pipeline, actual deployment IDs/state, timestamps, smoke/activation result, rollback/forward action, prior/current serving Product versions, and current serving artifact. The immutable Product Release Record specified by `AH-SPEC-PRODUCT-RELEASE-001` is finalized only after successful deployment and exact Product-tag observation. Partial promotion from a different or newer staging head is prohibited.

## 3. Local, Mock, Sandbox, And Real Modes

Local development can start the product through documented deterministic commands. Required dependencies declare one or more risk-appropriate modes:

- controlled fake/mock behind the real port;
- provider sandbox/emulator when it adds distinct value;
- real staging adapter.

Shared contract-core tests run against every implemented mode. Controlled modes cover difficult failure, denial, timeout, rate-limit, and retry cases. Critical provider semantics receive safely triggerable real staging evidence; untriggerable states remain `not_observed`, never invented.

Mocks prove domain/application behavior against a port. They do not prove IAM, network, deployment, provider limits, serialization, or real credentials.

For every external provider used by staging/E2E, the Run declares mode/tenant, exact recipient or target class, data classification, permitted side effects, cost limit, idempotency, cleanup/reconciliation, and authority. Sandbox/sink calls to isolated test tenants may be autonomous inside the Run. Real communication to third parties, value transfer, mutation of non-test data, or material spend requires exact Human Approval. Test e-mail addresses, phone numbers, payment instruments, webhook targets, AI/API tenants, and provider records are isolated from customers.

## 4. Staging Verification

For material deploy-relevant Delivery Slices, the agent team:

- confirms the active Product Vision Brief and reviews as a critical but fair target user, not only as a test operator;
- confirms the final Product Delivery Release Candidate, deployment, and target artifact IDs;
- uses stable secret-managed automation identities and Run-scoped synthetic fixtures;
- exercises acceptance, failure, denial, permissions, and recovery paths required by risk;
- reviews browser/UI behavior at approved viewports and states;
- captures staging screenshots and compares them with approved mockup source/renders;
- inspects relevant redacted logs, metrics, queues/backlogs, and provider state;
- verifies no unexplained resources, public exposure, tag gaps, retention drift, or fixed cost;
- cleans Run-scoped data without destroying shared test identities.

The user-perspective review explicitly evaluates whether the promised outcome is understandable and achievable; flow continuity; usability; information hierarchy; UI/UX and Design-System consistency; accessibility; trust; relevant latency; errors/denials/recovery; and avoidable user effort. Findings require observable staging evidence and concrete user/product impact. Reviewers do not manufacture defects or block on taste presented as fact.

Visual approval records intentional differences; pixel equality is not required. A flow must remain usable, accessible, contract-correct, consistent with the Design System, and aligned with the product vision.

For a `material_ui` Run on Harness `1.0.13+`, the exact candidate images and actual Product/UX
inspection required by `AH-SPEC-DESIGN-001` are part of this existing Staging/technical-acceptance
evidence. Technical metrics, prose or signatures cannot replace them. `minor_ui` and `non_visual`
follow their proportionate declared path without inheriting material-UI evidence volume.

## 5. External Action Authority

| Action | Default authority |
|---|---|
| local code/spec/test/mockup changes inside Run | autonomous |
| commit/push authorized Slice Branch or subordinate Package Branch | autonomous |
| create/update Slice-Branch PR | autonomous when Run permits |
| merge final Slice candidate to `staging` and deploy Staging | autonomous when Slice Contract, Run, Preflight and action authority permit |
| bounded early Verification Candidate deployment | autonomous only when exact trigger, target, count, side effects, cost, cleanup and restore authority are preauthorized |
| inspect CI, staging, AWS logs/metrics/resources, screenshots, and cost evidence | autonomous read-only |
| rollback staging to last green artifact | autonomous only when named in Run recovery authority |
| production promotion or rollback | explicit Human Approval, unless exact action was preapproved |
| production/customer data deletion or destructive migration | explicit Human Approval |
| material IAM, DNS, secret lifecycle, public exposure, fixed cost, or account change | explicit Human Approval |
| create/re-invite a real Production Product Admin or assign/change Production Product privileges | explicit Human Approval binding environment/provider tenant, protected personal principal reference, Product role/scope, method/expiry, idempotency, and recovery; normally bundled into Production Promotion |
| real third-party communication, value transfer, non-test data mutation, or material provider spend | explicit Human Approval |

Read-only inspection never authorizes mutation. Approval of an architecture or package does not implicitly approve its external action.

Normal later invitations or role changes performed interactively by an already authorized Human Product Admin under active Product policy are Product operations, not a new Harness Gate. An Agent or automation performing the same real action still requires the exact authority above. Staging synthetic Admin provisioning may be autonomous only inside an authorized Run with isolated provider tenant, recipient class, role cap, idempotency, cleanup, and zero Production reuse.

## 6. Pipeline Monitoring And Correction

After an authorized push/deploy, the responsible agent monitors the pipeline to terminal state and records the workflow/run URL or ID, source/artifact, environment, stages, result, and first failing evidence.

On failure it classifies code, test, infrastructure, permission, environment, provider, data, or flaky/transient cause. Technical corrections draw from Work §10's single task/Mission reserve and require new evidence/hypothesis. Missing permission, secret, Human Decision, unsafe migration, or uncertain external side effect stops immediately.

Choose continuation by actual failure: code/configuration/IAM/artifact fixes need affected local
checks and a new candidate; known safe transient test/cleanup failures may use their prebounded
retry; archive/notifier failures resume only the missing safe step without rebuilding/redeploying.
Archive continuation uses the existing CI run/attempt identity for distinct observations, or
verifies an already stored identical artifact before treating that step as complete. Do not
overwrite immutable evidence or mistake an archive-key collision for a new application defect.
Unknown partial cloud/provider state is reconciled before any retry. Preserve original failures.
Relevant deploy/migration scripts include their actual helper/configuration/permission dependencies;
mocks never prove effective IAM. Use the same authoritative focused commands locally and in CI,
not a duplicate full pipeline. Aim for short feedback (often1–2min for small local checks), never
truncate a necessary integration/cloud observation to an arbitrary time target. Exhaustion checkpoints the last safe state and escalates with attempted hypotheses, logs, blast radius, rollback recommendation, and exact missing decision/capability.

When pipeline feedback itself is the observed problem, inspect existing step timings once to
separate queue/build/provision/deploy/verification from retries. Place applicable inexpensive
compile/type/configuration/contract failures before expensive provisioning/deployment and use
the existing job/artifact reuse mechanisms. Do not introduce a second local pipeline, generic
cache service or timing quota. A successful normal run still has a cost; fewer failed reruns do
not prove its duration improved. Retain measured limits and unresolved environment-bound checks.

Expected provider visibility delay remains in the existing verification/pause/recheck path when the expected observation, bounded window, authorized read-only action, unchanged provider/candidate/configuration state and next trigger are recorded. That recheck does not consume technical correction authority. Any configuration, identity, candidate, deployment or provider-state mutation is a correction and uses the existing applicable budget and action authority.

## 7. Definition Of Done

The completion ladder and state truth are owned by Work. Artifact §4 owns the final immutable
material Review Record and its discoverability through Deployment history → RC → Review. Finalize
only after actual evidence/closure, with the existing non-author approver. The RC predeclares the
durable evidence destination, which is not itself proof. No mandatory spec move or post-release
metadata commit triggers another deployment. Runtime/build Markdown remains a real input.
Notify only the actual required accepted outcome/revision; routine and repair completion need no
spec-move detector. A failed archive/notification does not undo observed deployment, nor justify
redeploying it. An explicitly commissioned notification remains unresolved task work until fixed.
Product-owned workflow filters/notifiers must be adapted separately; Core replacement cannot do it.
For that adaptation, classify actual build/runtime inputs separately from plan/review/log-only
files rather than excluding every Markdown file. Completion consumers resolve the accepted
candidate/result from the existing evidence; they do not require a moved Spec or a particular
repair-Package label. Reconcile a queued/running delivery before an overall-success notification.
Prefer the existing machine-readable completion contract. Where a consumer parses Markdown,
keep its producer/template and parser on one explicit field contract and test the affected
normal/repair cases together; a renamed human-readable label must not silently change completion.
Do not add a parallel status schema when the existing accepted-result contract suffices.
Delivery evidence adds these guards:

- `slice_ready`: Package-local evidence is green and its exact commit is integrated into the frozen Slice candidate without claiming Staging truth;
- `integrated`: exact final Slice `staging` commit and fast/integration CI are green;
- `staging_deployed`: final Product Delivery Release Candidate and successful CDK deployment IDs exist;
- `staging_verified`: required real flows, provider behavior, screenshots, logs/metrics, and cleanup are evidenced;
- `technically_accepted`: independent reviewers closed all blocks and the predeclared Final Approver accepted evidence and residual risk.

For `material_ui`, `staging_verified`/`technically_accepted` additionally require the exact
candidate-bound visual Review projection and locally resolvable digest-matching raster evidence.
Where no mockup exists, the exact Decision Authority may preselect standalone critical-user image
review instead of a baseline comparison; candidate images remain mandatory. A material correction makes affected renders and their
approval stale; it does not create a new correction counter, reviewer round or lifecycle state.

If Staging access, users, provider, browser, logs, or deployment permission is absent, the Slice is not staging-verified and cannot be technically accepted when deployment is relevant. An early Verification Candidate never changes this rule.

## 8. Data Migration

In `pre_customer`, an authorized Delivery Slice/Work Package may reset/reseed disposable data and use forward-only migrations when fixtures and evidence are reproducible.

In `live_customer_data`, migration uses expand → backfill → validate → switch → contract. The package defines compatibility window, read/write behavior during transition, idempotent backfill, integrity totals, failure restart, rollback/forward recovery, retention, and cleanup. Destructive contraction occurs only after validation and Human Approval.

Feature flags remain exceptional under `AH-SPEC-ENGINEERING-001`; migration flags have owner, environment defaults, telemetry, expiry, and removal package.

## 9. Backup And Restore Verification

Before `live_customer_data`, every critical durable dataset demonstrates a restore probe in isolation:

- restore source and timestamp are identified;
- restored integrity and key invariants are verified;
- application/read path or recovery tooling can use the restored data;
- elapsed time is measured against RTO and data point against RPO;
- access is restricted and temporary restore resources are cleaned;
- failure and remediation are recorded.

Repeat after material backup/restore configuration change and at the Product Technical Delta's risk cadence. Nightly restore tests are not a generic requirement. Backup status without successful restore evidence is insufficient.

## 10. Rollback And Incident Recovery

Every deployment, through its Run or routine task/RC, names:

- Recovery Owner;
- last green application/infrastructure artifact;
- data migration state and reversible boundary;
- containment, rollback, roll-forward, and external-side-effect reconciliation steps;
- evidence and communication destination;
- actions that require Human Approval.

Staging may automatically return to the last green artifact only under predeclared recovery authority. Production containment and rollback remain human-approved by default. Rollback never rewinds customer data blindly; after irreversible/partially external effects, the team contains, reconciles, and uses the approved forward/compensation plan.

Critical dependencies have explicit timeout, rate-limit/429, 5xx/unavailable, retry/idempotency, degraded outcome, and user-message tests where relevant. The harness does not require broad chaos engineering without a demonstrated resilience risk.

An incident closes only after service/data state is known, evidence is preserved, temporary access/configuration is removed, cost and security impact are assessed, and follow-up Work Packages have owners.

## 11. Notifications And Ownership

Pipeline, regression, deployment, cost, security, and backup alerts route to a real owner and human-visible destination. E-mail is the default minimum for unattended nightly regression failure. Alerts without an actionable owner/runbook are removed rather than accumulated.

No agent creates external notification channels, users, DNS, IAM principals, secrets, or paid tooling without the authority matrix and applicable Human Gate.
