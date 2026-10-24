# Harness Distribution And Product Bootstrap

> Artifact ID: `AH-SPEC-DISTRIBUTION-001`
> Artifact class: Harness specification
> Authority: Canonical
> Status: Active
> Semantic owner: Master Harness Distribution
> Version: 1.0.3
> Governing artifacts: `AH-CONSTITUTION-001`, `AH-SPEC-ARTIFACTS-001`, `AH-SPEC-DOMAIN-001`, `AH-SPEC-INITIALIZATION-001`, `AH-SPEC-WORK-001`
> Review: `AH-REV-1-5-2-REMOVE-LEASES-001` (acceptance and limits in the referenced Review; prior historical reviews retained)
> Owns: release bundle, product overlay, startup anchors, manifest/integrity, protected/writable boundaries, bootstrap lifecycle, Brownfield adoption, and repository layout

## 1. Distribution Unit

A Harness release produces one immutable Product Repository Overlay. The release assembler copies approved canonical specs/profiles verbatim into the overlay core and adds root anchors, operational policy, role and workflow guides, templates, validator metadata, release notes, and adjacent-version impact history.

The master source remains canonical for authoring. The installed, integrity-pinned core is binding inside a product at its pinned release. Generated copies are never hand-edited; their manifest links master source path, release commit, and SHA-256.

The source overlay lives at `harness/product-repo-overlay/`. For a release, the assembler replaces its core source map with actual immutable copies. An overlay containing unresolved release/install tokens, non-active core specs, missing files, or mismatched digests is invalid.

The human-facing installation entry point is the root `bootstrap.sh`; a Product creator MUST NOT need to understand, locate, or manually handle an overlay bundle or the lower-level installer. Bootstrap accepts an explicit Product repository root and Product ID, obtains exactly one immutable Harness version, performs all trust and target preflight before mutation, assembles only in a temporary directory, delegates the actual mutation to `install_or_upgrade.py`, runs the installed validator, and removes temporary source/release data. Fresh-install eligibility is collision-based, not emptiness-based: existing Product-owned paths such as `.gitignore`, `.DS_Store`, or non-conflicting files below `docs/**` remain byte-identical and do not by themselves force Brownfield adoption. Preflight rejects only an exact non-identical release destination, an unsafe destination or parent type, a symlink/path escape, or another declared safety conflict; it never overwrites an existing byte. It never follows `main`, another branch, or `latest`, never commits or pushes the Product repository, and never authorizes Product implementation.

Version `1.0.0` and later releases support an authenticated tagged-source distribution from the canonical private Git repository. Bootstrap clones its exact declared `YYYYMMDD-<exact-semver>-<stable-logical-name>` tag; the assembler requires the tag's SemVer to equal the Release Plan and a clean checkout whose HEAD carries only that release tag, whose configured origin matches the explicitly trusted repository, and whose remote tag resolves to the same source commit. The Source Lock MUST bind only active, digest-exact Core/Profile sources, and the resulting Manifest binds the observed tag and commit. The intermediate assembled overlay remains an internal temporary implementation detail. An explicitly supplied local source is allowed for offline use or testing only when the caller intentionally trusts that checkout; it must satisfy the same exact-tag, clean-source, origin, Source-Lock, and remote-resolution checks.

Every overlay payload has exactly one class from `AH-SPEC-ARTIFACTS-001`, recorded in the protected inventory or directly in navigation/generated metadata. Protected template files are `Reference` payloads; their separately labeled `Instantiated artifact class` becomes the product artifact's class only after instantiation.

## 2. Installed Boundary

```text
AGENTS.md             protected root boot anchor
README.md             product-owned orientation with validated startup invariants
.agentic-harness/
  manifest.md           immutable release manifest
  core/                 immutable released Constitution/specs/profiles
  policies/             portable operating entry
  roles/                role-function activation and review questions
  workflows/            initialization, execution, resume, promotion
  templates/            governed Markdown artifact templates
  validators/           release-provided checks and configuration
product-input/          human-owned, Agent-read-only PRD and optional inputs
docs/harness-state/     product-owned install/bootstrap/verification state
docs/                   product-owned truth, work, review, and evidence indexes
applications/ domains/ orchestration/ platform/ packages/ tests/
```

Only directories needed by actual artifacts are created during bootstrap. Code directories appear when the approved architecture and first Work Package need them.

Bootstrap seeds root `AGENTS.md`, `README.md`, `docs/handover.md`, `docs/specs/spec-routing.md`, `docs/harness-state/**`, and `product-input/**` once. After installation every path outside `.agentic-harness/**` is Product- or Human-owned and a compatible Harness upgrade MUST NOT replace, delete, normalize, or append to it. Root `AGENTS.md` remains the repository's only special-semantics Agent-instruction file; additional or nested `AGENTS.md` files are forbidden. Product-specific Agent guidance lives only in `docs/agent-extensions.md` and MUST NOT weaken higher rules. Compatible releases keep the seeded root entry chain usable and place evolving rules inside `.agentic-harness/**`. A required external-file change is a separately authorized Product migration, never an implicit upgrade side effect.

The protected payload contains the released Spawn-Reviewer role projection. New installations may
make the existing root entry router explicitly point to Agent-start control, but compatible
upgrades MUST NOT rewrite a Product-owned root `AGENTS.md`. Supported old roots load the protected
Manifest but may not directly load the Operating Policy. The protected Manifest MUST explicitly
route to `.agentic-harness/policies/operating-policy.md` before task work; that policy routes to
Work §5.1 before preparation. This bridge carries current duties after Core replacement without
requiring a Product-root edit or special Human prompt. The role projection is operational guidance owned by
`AH-SPEC-COLLABORATION-001`, not a second normative rule source.

Harness `1.2.1` upgrades replace that protected policy, role, workflow, template and validator
behavior inside `.agentic-harness/**` only. They do not rewrite Product-owned root instructions or
Contracts. Product recalibration records `required_before_continue` only for an Agent that is about
to start without an applicable current clearance; it does not migrate historical Agent activity or
force later reviewer clearance before a candidate exists.

`product-input/**` is human-owned and Agent-read-only. Agents may inventory and safely snapshot it, but MUST NOT overwrite, normalize, or improve it in place. Agent-generated draft intent, redacted working copies, and change proposals live under `docs/product/` until the human supplies or approves them as new input.

## 3. Mandatory Entry Chain

Every fresh Agent context reads, in order:

1. root `README.md`;
2. `docs/handover.md`;
3. `.agentic-harness/manifest.md`, verifies no unresolved integrity warning, and follows its
   protected Operating Policy route, including task-wide Work §5.1;
4. the task route in `docs/specs/spec-routing.md`;
5. the exact effective Domain Foundation and Product Vision revisions named by the active Run,
   omitting only those not yet possible for the current bootstrap phase;
6. only the routed product/module specs, contracts, Work Contract, and evidence needed for the task.

Root `AGENTS.md` makes this chain binding and blocks repository-wide scanning by default. Before the
first `domain_foundation` Run exists, read-only admission uses the exact Human instruction, active
Bootstrap State, and explicitly named inputs. Agents hash without copying and prepare/preflight the
provisional Contract ephemerally; the non-creator Decision Authority authorizes it. Persist the one
Contract, run the direct check, coordinate actual conflicting resource access, and set it active before safe snapshots or Domain
artifacts are written. After the Human Domain Decision, `bootstrap_initialization` additionally
binds the effective Foundation and later its candidate Vision. No later work uses either pre-Vision
exception. Missing required entry, routing, context, manifest, or integrity evidence fails
Preflight rather than triggering improvisation.

## 4. Version And Integrity Manifest

The immutable release manifest and protected machine-readable Release Metadata contain:

- Harness release version and channel;
- master repository URL, release tag, and source commit;
- protected-payload tree digest;
- every protected file path below `.agentic-harness/**`, source artifact ID/version, and SHA-256;
- every bundled available organization/technical profile ID, version, and digest;
- supported product overlay schema version;
- supported starting releases and the complete adjacent-version impact-history chain;
- protected and product-writable path rules;
- verification command and external trust-anchor method.

Release Metadata binds the exact SemVer, overlay schema, supported starting version/schema pairs, ordered history entries and their digests, source commit, tag, immutable provider repository/owner IDs, in-repository Evidence Policy digest, and externally anchored Release Attestation digest. Human-readable Manifest fields are a projection of the same Release Plan. Every duplicated scalar, compatibility list, ordered history-ID list, Evidence Policy digest, and Attestation digest is compared canonically; any disagreement blocks assembly or installation.

The manifest never hashes itself and contains no mutable installation or verification fields. Its own SHA-256 MUST be pinned outside the installed protected boundary by a signed release attestation or an installer-/human-supplied expected digest verified against an immutable master release/commit. Installation identity, expected manifest digest, last verification, and Bootstrap state live in product-owned append-only state/evidence, never in the release manifest.

The protected-payload digest algorithm is reproducible: reject paths containing tab, newline, NUL, `..`, or non-POSIX separators; calculate lowercase SHA-256 over each file's raw bytes; sort repository-relative paths by unsigned UTF-8 byte order; concatenate `path`, one tab, the 64-character digest, and one LF per entry; calculate SHA-256 over those UTF-8 bytes. Inventory includes every regular file under `.agentic-harness/**` except `.agentic-harness/manifest.md`; symlinks are forbidden. Root and Product files are deliberately outside the upgrade inventory. The external anchor authenticates the manifest itself.

Product validation has two explicit file universes. Installed `.agentic-harness/**` integrity is
always evaluated from the raw filesystem against the authenticated Manifest. Product-owned content
checks use Git's exact cached-plus-untracked-nonignored inventory (`git ls-files --cached --others
--exclude-standard`). Thus tracked files remain responsible even if an ignore rule later matches
them, while ignored third-party, generated, cache and build artifacts are not Product truth and are
not scanned for Product links, nested Agent instructions, release tokens or secrets. The validator
MUST fail closed when that Git inventory is unavailable; it MUST NOT replace ownership with a
directory-name allow/deny list or a blind filesystem walk.

An unresolved packaging token is exactly: two less-than characters; prefix `AH_`; kind `RELEASE` or `INSTALL`; a colon; an identifier matching uppercase letter followed by uppercase letters, digits, or underscore; and two greater-than characters. Release-stage tokens are permitted only in the master source overlay's generated Release Manifest and protected Release Metadata; install-stage tokens are permitted only in the initial Bootstrap State. Every token MUST be fully resolved during its named release/install stage. The installed-product verifier scans every regular file in the responsible Git inventory except protected template sources for that grammar.

A template-instantiation marker is exactly two left braces, an uppercase-underscore identifier, and two right braces. It is intentionally permitted in released files under `.agentic-harness/templates/**`. Outside that protected directory, any matching marker in a non-draft artifact is unresolved and blocking; explanatory documents spell the grammar textually instead of embedding a literal marker. This fail-closed location/lifecycle rule avoids guesswork about whether a marker is data or prose.

Any trust-anchor mismatch, protected-file mismatch, missing file, unresolved release/install token, unrecognized protected file, unauthorized nested/additional `AGENTS.md`, or unsupported schema sets verification to failed in product-owned evidence. Product mutation stops. The Agent may diagnose and propose reinstall/upgrade but MUST NOT repair protected files or rewrite the trust anchor ad hoc.

## 5. Product-Owned Layout

Bootstrap creates or routes actual product artifacts to:

```text
docs/handover.md
docs/harness-state/bootstrap-and-installation.md
docs/product/                 inputs, Product/Vision Brief, requirements, use cases
docs/strategy/                MVP, vision, outcomes, milestones, six-week plan
docs/specs/global/            cross-product architecture/quality/security/design/delivery truth
docs/specs/spec-routing.md
docs/domains/                 Product-wide Domain Foundation and Context Map
docs/domains/<context>/       Module Entry Map, Domain Specs, public contracts
docs/orchestration/           cross-domain flow specs
docs/architecture/decisions/  ADRs and exceptions
docs/design/                  Design System, flows, editable sources, render manifests
docs/work/                    packages, Execution Runs, checkpoints
docs/reviews/                 review records and evidence manifests
docs/harness-proposals/       dated narrative Product-originated Harness Improvement Proposals
```

Heavy/raw CI artifacts, screenshots, logs, SBOMs, and deployment outputs may live in a configured immutable artifact store. Their repository manifests preserve IDs, digests, environment, retention, and access.

## 6. Bootstrap Lifecycle

```text
uninstalled -> installed_uninitialized -> intake_ready -> modeling_domain
  -> awaiting_human_domain_gate -> domain_foundation_effective
  -> initializing -> awaiting_human_initialization_gate -> initialized
```

1. **Install:** verify destination, authenticate the released manifest against its external trust anchor, copy the exact released overlay, verify protected inventory/tree digest, instantiate product-owned install state, and refuse to overwrite unknown files.
2. **Read-only admission:** verify Git/remote/branch, Harness integrity, required tools, High/xhigh Agent availability, exact human instruction, and named inputs. Classify inputs and hash safe bytes in place without copying, executing, or modifying them.
3. **Domain Run preparation:** the Bootstrap Work Contract supplies scope. Without mutation,
   calculate safe input digests and prepare the exact provisional `domain_foundation` Contract.
4. **Domain Run activation:** the non-creator Decision Authority authorizes the Contract after
   Preflight. Persist it, run `--check-run`, coordinate actual conflicting resource access, and set it active before snapshots or
   Foundation artifacts are written.
5. **Domain Foundation:** create C1-C3, bound diagrams, Context Coverage, and the exact Domain Review
   Pack; stop at the Human Domain Decision.
6. **Initialization Run:** after an effective Foundation, authorize/activate the separate
   `bootstrap_initialization` Contract targeting that exact revision.
7. **Initialize and review:** create Product/Vision, detailed use cases/flows, contracts,
   architecture, design reference, MVP, and rolling plan; assemble the Initialization Review Pack.
8. **Initialization Gate:** stop at the Human Initialization Gate. No delivery-intended Product
   implementation begins before approval.
9. **Activate:** activate approved decision artifacts/plan/design, leave unimplemented Target Specs
   approved until implementation, and admit explicitly named Runs to Preflight.

The canonical product-owned Bootstrap State is a Work Contract, not the handover. Every transition records prior/current state, actor, timestamp, input/manifest digest, Domain and Initialization Run/Review/Decision IDs where applicable, and transition evidence. The handover only links it. The workflow is idempotent by artifact ID and revision. Restart continues from the last valid state; it never generates duplicate artifacts or silently overwrites human input.

For a fresh Product repository, bootstrap permits only `.git/**` and optional `product-input/**` before installation. It rejects root/home targets, non-repository targets, source/target overlap, symlink components, special files, unknown root entries, and non-identical collisions before mutation. Human-owned inputs are byte-digested before and after installation and MUST remain unchanged. A second invocation against the exact valid declared-version Manifest is a verified no-op; a different same-version Manifest, damaged Core, partial transaction, or another version stops for recovery or the explicit upgrade workflow.

The companion `start-new-product.md` is an installation-only convenience prompt, not an authority source. It pins the exact released tag, delegates installation to `bootstrap.sh`, verifies lifecycle `installed_uninitialized`, reports the later separate intake/initialization command, and MUST stop. It MUST NOT read Product inputs, follow the initialization workflow, or authorize discovery, planning, prototyping, or Review-Pack assembly. A new Codex context reads the installed root `AGENTS.md`, Product README, and handover; without a separate explicit initialization instruction it requests the required PRD and optional inputs, provides the exact initialization command, and stops.

## 7. Input Convention

Default human input paths are:

```text
product-input/prd.md                         required
product-input/technical-requirements.md      optional
product-input/mockups/                       optional image or HTML source
product-input/research/                      optional
product-input/brand/                         optional
```

Alternative paths are allowed when the human names them. The safe intake and untrusted-executable rules of `AH-SPEC-INITIALIZATION-001` remain mandatory.

The natural-language command “Initialize this product from the provided PRD and optional inputs” is sufficient authorization to perform safe intake, Domain Foundation preparation, and—after the Human Domain Decision—initialization through assembly of the Human Initialization Review Pack. It is not authorization to approve either Gate or implement the Product.

The Product Technical Delta becomes the product-owned, human-approved profile-selection lock. It binds selected profile IDs, versions, digests, exceptions, and review decision. Profile selection never mutates the immutable release manifest, which inventories all profiles available in that release.

## 8. Install And Upgrade Safety

### Brownfield adoption

Brownfield adoption is a separate `adopt` operation; fresh `bootstrap.sh` remains strict. Adoption:

1. inventories the existing Git repository read-only and produces an exact collision/integration
   plan before mutation;
2. authenticates and stages one fixed immutable Harness Core;
3. refuses symlink/path escape, source/target overlap, special files, protected collision, and any
   overwrite of an existing Product-owned byte;
4. installs or rolls back the protected Core transactionally under one lock;
5. treats root instruction/routing integration as a separate exact Human-authorized Product change;
6. records Context Coverage under `AH-SPEC-DOMAIN-001`; and
7. reports staged Core as inactive/incomplete until entry routing and Coverage are verified.

The adoption entrypoint may create a missing non-colliding Product-owned seed only when its exact
path/content was in the preflight plan and the Human explicitly selected integration. It never
edits an existing root `AGENTS.md`, README, Handover, route, Product spec, code, or input. Repeated
execution against the identical valid staged/active state is a verified no-op. Failure restores the
prior Core and any newly created seeds or stops with a recovery record; it does not leave an active
claim.

Brownfield remodeling is optional context by context. New contexts are strict; changes in uncovered
legacy scope require the exact model or Human Legacy Exception. Core installation alone does not
perform Product semantic migration.

### Core Replacement And Intentional Product Adoption

Fresh installation, compatible Core upgrade, and Brownfield adoption are separate operations. Install may seed the complete Product repository overlay only under explicit fresh-install authority and an exact collision-free plan; that boundary does not require an otherwise empty repository. Brownfield adoption remains the deliberate choice when an existing Product must receive only inactive Core staging without root integration. A compatible upgrade authenticates one fixed immutable target release and replaces exactly `.agentic-harness/**`; it never interprets Product lifecycle, Runs, branches, plans, handover, README, Product input, Product code, or other Product-owned state. Brownfield adoption may create only an absent `.agentic-harness/**` tree as `inactive_staged` and cannot activate Product integration.

For1.5.2+, install/adopt require authority and transaction identity, never `--lease-evidence`.
Existing short filesystem transactions protect only the actual installation/Core replacement,
not ongoing development. Core upgrade does not remove Product-owned legacy scripts automatically;
remove their old lease gates under Product authority when adapting affected consumers. New Harness
work never creates lease state, renewals, cleanup/handoff duties or substitute lock forms.

The parameterless upgrade entrypoint reads the actual installed version AND overlay schema from protected Release Metadata, requires that exact supported pair, verifies a complete adjacent-history chain to the fixed target, stages the complete target Core on the same filesystem, and performs a directory replacement under one exclusive filesystem lock. A small sibling recovery record binds target path, old/new versions, phase, old/new Manifest digests, and backup/staged paths. Validation success removes backup and recovery state; handled failure restores the prior Core exactly. Repeated execution against the exact valid target is a validated no-op. Unsupported downgrade, missing history edge, source/target overlap, path escape, symlink, invalid target inventory, or incomplete recoverable replacement stops without touching Product-owned bytes.

An authorized1.5 upgrade request binds that target and its disclosed workflow/authority changes;
do not ask again when the request already grants this authority. The supported version/schema list proves a technical replacement path, not
semantic consent. The parameterless fixed-target entrypoint is invoked only under that authority;
it performs the same Core-only transaction, never automated Product-owned migration. Retain pre1.5
historical interpretation, but re-admit live work at a safe boundary under current rules, carrying
actual prior authority, consumed budgets and tighter limits. An increase requires its own decision.

Recalibration targets old root Run/Slice instructions, RC consumers, obsolete Product-owned lease gates, spec-move/status
consumers, durable Review access and CI/notifier triggers for the work actually next. Separately
authorize needed Product edits. Missing adaptation blocks only the affected delivery/acceptance
claim, never unrelated Product work. Validate fresh and each supported actual starting pair,
including refusal before swap for unsupported installed schema; no invented intermediate upgrade.

History describes possible semantic impact; it does not mutate Product truth. After replacement, a
separate Product-owned recalibration evaluates the relevant history entries and records
`no_change`, `required_before_continue`, `deferred`, or `human_decision`, with evidence and trigger.
For an affected consumer, name its actual file/job or state owner, observed old assumption,
minimum adaptation, existing focused check and authorized next action in that same record.
Do not create a second adoption audit or claim Product readiness from Core replacement alone.
Product plans are never rewritten automatically. Product-owned Contracts likewise remain untouched
by Core replacement: historical revisions keep their pinned rules. A new `1.3.0+` ordinary Run
uses the current single-Contract format. A rare automatic change to other
Product-owned files is an explicit Product migration with separate Human authorization, not part of
normal upgrade.

Post-upgrade Product validation does not project the current Run schema onto an older Contract.
Historical files remain in the Product-owned Git inventory for generic link, secret and token
controls; they require no migration merely to satisfy the new ordinary-Run format.

No product Agent may edit master source through normal product work. Harness learning follows the evolution specification and an independently authorized Master Run.

The distributed proposal workflow and template use only `docs/harness-proposals/YYYY-MM-DD-<stable-logical-slug>.md`. Proposal-only upstream validation is an explicit Git/PR check: it observes the exact base/head and all intervening commits, rejects mixed or transient non-HIP paths, and does not infer success when provider/Git evidence is unavailable. Ordinary Product validation does not reserve generic document names outside a declared Harness-learning submission.

## 9. Release Acceptance

An overlay release is acceptable only when:

- root anchors route correctly in a fresh context;
- every protected file digest matches the manifest;
- all referenced canonical core sources are active and approved;
- no release/install token remains in an installed tracked file; declared instantiation markers remain valid inside protected template sources;
- workflows and templates implement, but do not contradict, their canonical contracts;
- the selected evaluation profile's required work samples or Evals pass under Evaluation§5.1/9;
  ordinary tagged-source releases use bounded samples, while explicitly selected formal assets
  retain extended assurance; deterministic install/integrity/negative controls remain required;
- adjacent-version impact history, replacement compatibility, and rollback are documented;
- generated product files remain clearly separate from protected Harness core.

Instantiated product artifacts MAY retain unresolved instantiation markers only while `draft`. Any transition to `in_review`, `approved`, `active`, `authorized`, or any claimed Evidence state fails when required fields, example rows, or markers remain. `not_applicable` is a resolved value only with the rationale and authority required by the owning contract.
