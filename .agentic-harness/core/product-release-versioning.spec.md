# Product Release Versioning

> Artifact ID: `AH-SPEC-PRODUCT-RELEASE-001`
> Artifact class: Harness specification
> Authority: Canonical
> Status: Active
> Semantic owner: Master Harness Product Delivery
> Version: 0.2.2
> Governing artifacts: `AH-CONSTITUTION-001`, `AH-SPEC-ARTIFACTS-001`, `AH-SPEC-INITIALIZATION-001`, `AH-SPEC-DELIVERY-001`
> Review: `AH-REV-1-5-3-REMOVE-ADDED-RULES-001` (acceptance and limits in the referenced Review; prior historical reviews retained)
> Owns: Product application-release policy, version scheme, release-unit identity, version reservation/publication, Product release tags, component-version mapping, and version-history invariants

## 1. Purpose And Boundaries

Every Product needs a durable answer to “which application release is this?” The Harness version, Product application version, Product Delivery Release Candidate ID, source commit, deployment ID, database schema version, API contract version, and component/package versions are distinct identities. None may silently stand in for another.

The Harness requires a Product-owned **Product Release Policy** and immutable release evidence. The Product chooses the version scheme within this contract. Semantic Versioning is the default, not a universal fiction imposed on every delivery model.

This specification does not version the Harness itself; `AH-SPEC-EVOLUTION-001` owns that lifecycle.

## 2. Product Release Policy

Initialization creates one Product-wide Product Release Policy as a canonical Product specification. Its exact revision is approved at the existing Human Initialization Gate and owns:

- the Product release unit: normally the complete externally operated Product;
- version scheme and exact grammar, initial-version rule, ordering, increment/classification rules, and examples;
- compatibility audience and surfaces, including public API/SDK/file/event contracts, operator obligations, user-visible behavior, and supported upgrade paths where applicable;
- default immutable Product Git-tag grammar and the single source of version truth used by build/release tooling;
- treatment of prerelease/build metadata, multiple deployables/components, migrations, rollbacks, hotfixes, and discontinued versions;
- authority for choosing the next intended version and evidence required to publish it.

The policy MUST select exactly one primary Product version scheme. Allowed choices include `semver`, `calver`, or another deterministic monotonic scheme defined completely by the Product. `semver` is selected when no evidenced Product constraint makes another scheme more truthful. A non-SemVer choice records the Product reason and concrete benefit; it is not a Harness exception and creates no additional Human Gate.

Continuously delivered Products are not exempt. They still expose an immutable Product release identity for support, incident response, rollback, evidence, and current-serving-state inspection.

## 3. Semantic Versioning Default

When `semver` is selected, the Product uses `MAJOR.MINOR.PATCH` and defines its compatibility audience rather than classifying mechanically from file count or deployment size:

- **Major:** an intentionally incompatible change to a supported external Product contract or upgrade promise that requires coordinated consumer/operator action or ends a declared compatibility line;
- **Minor:** backward-compatible Product capability or externally meaningful behavior added within the current compatibility line;
- **Patch:** backward-compatible defect, security, operational, performance, content, or internal change that adds no externally promised capability requiring Minor classification.

A normal SaaS UI evolution is not automatically Major merely because users cannot select an older UI. The Product Policy states which user/operator promises constitute compatibility. Public API, SDK, event, import/export, automation, or stored-data obligations remain explicit even when the Product is SaaS.

Unless Product evidence selects another start, pre-stable Product development begins at `0.1.0`; `1.0.0` marks the first compatibility line the Product is prepared to support. Prerelease identifiers MAY label distributable non-Production artifacts only when the Policy defines them. Build metadata MUST NOT create two meanings for one published version.

The default SemVer Product tag is `product-v<exact-version>`, for example `product-v1.4.2`. A Product may define another unambiguous namespace in its Policy.

## 4. Release Unit And Components

The default release unit is one Product, even when several application, frontend, function, worker, migration, or infrastructure artifacts are deployed together. One Product version maps to their exact immutable digest set in the final Product Delivery Release Candidate and Product Release Record.

Independent component versions are permitted only when components have genuinely independent consumers, compatibility policies, or release lifecycles. The Product Policy then defines each component namespace and preserves one top-level Product release version or release-set identity that maps all deployed component versions and digests. Internal package versions do not become Product releases by default.

## 5. Candidate, Publication, And Consumption

A final Product Delivery Release Candidate, including the Delivery §2.2 routine variant, binds:

- one **intended Product version** that is valid under the exact approved Product Release Policy revision;
- state `reserved_unpublished`;
- the proposed immutable Product release tag;
- exact source, specification, migration, application, component, toolchain, infrastructure, provenance, and Staging evidence already required by `AH-SPEC-DELIVERY-001`.

Reservation is an append-only **Product Release Identity Ledger** event owned by Product Delivery. Before reservation, the final RC Manifest bytes are completely rendered in transaction staging with state `reserved_unpublished`, frozen, and hashed; they are not yet authoritative. One recovery-safe atomic transaction persists both those exact RC bytes and the genesis reservation that binds their ID/digest, version/tag, and exact Policy revision. Recovery accepts both matching artifacts or neither and never exposes an unreserved final RC. The authoritative collision check fails closed when either the version or tag appears in any active reservation owned by another RC, `consumed_for_promotion`, `consumed_partial`, `skipped`, `published`, Product Release Record, or local/remote Product tag. Missing/unavailable Ledger or provider-tag evidence blocks reservation and Promotion; checking only published versions is insufficient.

A corrected unpublished final candidate MAY retain the same intended version only through one explicit `reservation_transfer` event that invalidates the prior RC ownership and atomically persists/binds the frozen replacement RC bytes and ID/digest. Transfer requires unchanged release scope/classification, no Production mutation, repeated candidate evidence, and recovery that exposes either the old ownership or the complete new binding. Otherwise the corrected candidate selects another valid version. A scope or compatibility change always re-runs the Policy's version decision.

An early `verification_candidate` is `non_promotable`, binds no intended Product version or Product release tag, and cannot consume, publish, or imply one. Its RC identity is sufficient.

The Product Release Identity Ledger uses this state machine; the immutable RC Manifest itself remains `reserved_unpublished` evidence and is never edited:

```text
none -> reserved_unpublished
reserved_unpublished -> reserved_unpublished   (reservation_transfer only)
reserved_unpublished -> consumed_for_promotion
consumed_for_promotion -> reserved_unpublished (reconciliation proves no Production mutation)
consumed_for_promotion -> consumed_partial
consumed_for_promotion -> published
consumed_partial -> published                   (same exact RC recovery only)
consumed_partial -> skipped
```

`published` and `skipped` are terminal. Every event binds its immediate predecessor digest, exact version/tag/Policy/RC, actor, timestamp, authority, guard, observed deployment/provider/tag state, and recovery owner. State is derived from the last valid event; labels in an RC, plan, tag, or mutable summary do not advance it.

Production publication follows this idempotently reconcilable order:

1. recheck the entire collision domain and exact reservation owner;
2. append `consumed_for_promotion` immediately before the first authorized Production mutation;
3. deploy the exact approved final candidate without rebuild/resynthesis and immediately append actual deployment/current-serving state to the Deployment Ledger;
4. complete smoke, activation, and any approved privileged bootstrap;
5. create/push the exact Product tag on the candidate source commit and re-observe provider resolution to that commit;
6. only after tag and deployment observations exist, finalize the immutable Product Release Record;
7. append `published`, then advance `main` to the exact lineage and re-observe all projections.

Each step re-reads Ledger/provider/deployment state and treats already-exact state as a no-op. A crash after `consumed_for_promotion` first proves from provider/deployment evidence whether Production mutation occurred: if definitely none, append the allowed restoration to `reserved_unpublished`; otherwise append `consumed_partial`. Any failure after Production mutation records actual serving state and `consumed_partial`; recovery may finish only the same exact RC/version/tag or append `skipped` and roll/forward according to actual state. A tag/record/`main` failure never repeats deployment. A published or consumed Product version/tag is never reused, moved, deleted to conceal history, or assigned different bytes/meaning. Product release publication does not alter the installed Harness version.

## 6. Product Release Record And Operational Truth

Routine work does not waive version uniqueness, reservation or exact Human Production approval.
Its task/candidate result evidence replaces artificial Slice acceptance; material work retains the
final Review Record under Artifact §4. The short identity lock is separate from development lifetime.

Every successful Production promotion creates one immutable Product Release Record binding:

- Product ID, published Product version, scheme, Product Release Policy ID/revision/digest, and Product release tag;
- exact final Product Delivery Release Candidate ID/digest, source commit/tree, application/component/migration/artifact and Production-assembly digests;
- Human Production Approval, pipeline/build/deployment identities, timestamps, environment, smoke/activation result, and Deployment Ledger event;
- prior and new current-serving Product versions, rollback/forward-fix target, known limitations, and release-note reference.

The Product Release Identity Ledger is truth for version ownership/publication state; the Deployment Ledger remains truth for actual deployments and current serving state. Git tags and release notes are discoverability/identity evidence, not proof that Production succeeded. A rollback appends actual state and may restore a previously published version; it never republishes, renumbers, or rewrites that earlier release.

The running Product SHOULD expose the current Product version through a safe operator-visible diagnostic and, when useful, a user-visible support surface. It MUST NOT expose secrets, private infrastructure identity, or sensitive provenance.

## 7. Initialization, Change, And Existing Products

The Human Initialization Review Pack presents the exact Product Release Policy revision alongside Product, design, plan, profile, and implementation decisions. The Policy choice is part of those existing Initialization decisions; it does not create a separate constitutional Gate.

A later Policy change is a Product-wide material specification change. It requires independent `D2` review and the Product Authority already governing the affected Product/compatibility promise. It MUST define treatment of existing published versions and tags without rewriting them.

Harness upgrade never creates or edits the Product-owned Policy. A Product upgrading from a Harness version without this requirement performs Product-owned recalibration:

- `required_before_continue` when a future final RC or Production promotion lacks an approved Product Release Policy;
- `no_change` only when an existing Product-owned policy already satisfies this contract and is linked by exact revision;
- `deferred` only when no release-capable work can proceed before the named trigger;
- `human_decision` when the scheme or compatibility audience materially affects Product promises.

## 8. Acceptance And Anti-Criteria

Accept only when every release-capable Product has one explicit Policy, every final candidate reserves one valid intended version/tag, every successful promotion publishes one immutable version-to-bytes identity, actual serving state remains inspectable, and alternative schemes are deterministic and justified.

Reject Product/Harness version coupling, mutable `latest` identity, version publication from Staging or verification candidates, automatic Product-file mutation during Harness upgrade, tag movement/reuse, version inference from commit count/date without Policy, mandatory independent component versions, or a SemVer label whose Product compatibility meaning is undefined.
