# Artifact And Source-Of-Truth Model

> Artifact ID: `AH-SPEC-ARTIFACTS-001`
> Artifact class: Harness specification
> Authority: Canonical
> Status: Active
> Semantic owner: Master Harness Architecture
> Version: 1.0.2
> Governing artifact: `AH-CONSTITUTION-001`
> Review: `AH-REV-1-5-1-COMPLETION-DIAGNOSTICS-001` (acceptance and evidence limits in the referenced Review; prior historical reviews retained)
> Owns: artifact classes, canonical ownership, identity, lifecycle, traceability, invalidation, and handover boundaries

## 1. Artifact Classes

Every durable file belongs to exactly one primary class:

| Class | Purpose | May authorize behavior? |
|---|---|---|
| Constitutional | non-negotiable authority and invariants | yes, at the highest harness level |
| Harness specification | reusable governance, workflow, engineering, distribution, or evaluation rule | yes, within Constitution |
| Profile | selectable organization or technology policy | yes, within Constitution |
| Product specification | product-wide, bounded-context, contract, cross-domain, UX, quality, or operational truth | yes, within higher rules |
| Decision record | resolves an explicit choice, exception, or human override and preserves rationale | only for its declared decision scope |
| Work contract | Milestone, Delivery Slice, Work Package, Technical Risk Experiment, Execution Run, acceptance, and stop boundary | authorizes only declared scope, actions, and target state |
| Editable source | mockup source, diagram source, schema source, or other maintained input | no unless referenced by a canonical specification |
| Generated view | rendered image, index, report, or packaged derivative | no; source and generator own meaning |
| Evidence | immutable observation from review, test, pipeline, deployment, screenshot, log, or cost check | proves only what it directly observed |
| Navigation | README, routing map, handover, or index | no; it links and summarizes |
| Reference | historical, external or optional diagnostic learning material | no, unless deliberately adopted by a canonical source |

Templates define required shape but do not become product truth until instantiated, identified, reviewed, and approved where required.

A Feature/Capability definition is Product specification scope, not a Work Contract. Material change becomes executable through an approved Delivery Slice, its Work Packages and
authorized Run. Collaboration §4 D0 routine instead binds the existing task, diff and evidence.

## 2. Canonical Ownership

Every durable rule, decision, work scope, and acceptance claim MUST have one canonical owner. Other artifacts link to it by stable ID and path. They MAY summarize for navigation but MUST NOT restate it as an independent rule.

When a rule applies globally, it belongs in a global product specification. When it belongs to one bounded context, that context owns it. Inter-context behavior belongs to an explicit public contract or cross-domain orchestration specification—not to a random consumer module.

Implementation, tests, comments, screenshots, handovers, and generated reports MUST NOT silently become the canonical source for behavior.

A Work Contract—including a Delivery Slice Contract—cannot introduce durable product behavior. Any new or changed rule MUST become active in the owning global, bounded-context, contract, or cross-domain specification through the final acceptance evidence below. After completion, Work Contracts remain historical scope, integration, and completion records.

## 3. Identity And Version

Metadata is class-specific:

| Artifact class | Required metadata |
|---|---|
| Constitutional / Harness specification / Profile / Product specification | stable ID, class, authority, lifecycle status, semantic owner, version or revision, governing artifacts, review reference |
| Decision / Review record | stable ID, class, target revision or digest, author/reviewers, status or outcome, date, authority, evidence references |
| Work contract | stable ID, class, current object-specific status, semantic owner, revision, governing specs, Decision Authority, reviewers, target completion level |
| Editable source / Generated view | stable ID or deterministic path, source owner, source revision, generator and source reference where generated |
| Evidence | stable ID, observation state, timestamp, environment, immutable subject and raw-evidence reference |
| Navigation / Reference | title, class or explicit reference label, and linked owners; no approval lifecycle is required |

Dependencies, consumers, expiry, and supersession links are additionally required whenever they exist or affect invalidation.

Stable IDs and paths are retained; no pending→completed move is required for delivery.
Review metadata lives outside its reviewed payload and does not invalidate itself.
Stable IDs survive necessary file moves. Links use repository-relative paths. An evidence reference additionally binds to an immutable commit, build, deployment, or content digest so a later edit cannot change what was approved.

## 4. Lifecycle

Normative document revisions use:

```text
draft -> in_review -> approved -> active -> superseded
                    \-> rejected
```

- `draft`: may be incomplete; cannot authorize implementation.
- `in_review`: frozen at a declared revision or digest.
- `approved`: content passed required governance but is not necessarily activated.
- `active`: current source of truth.
- `rejected`: must not be implemented; rationale remains traceable.
- `superseded`: retained for traceability and points to its replacement.

Material correction during review creates a new revision or digest, invalidates affected review decisions, and requires re-review. A purely mechanical change may preserve review only with deterministic proof that meaning did not change.

Raw evidence is immutable and remains `observed`. A separate evidence registry revision may mark that observation `invalidated` or `expired`, with reason and replacement reference; the raw artifact itself is never rewritten. Navigation and reference files have no approval state.

For1.5 material delivery, the existing **final immutable Review Record** is the authoritative
acceptance/verified-spec-activation source. The existing non-author Final Approver finalizes it
only after actual evidence and finding closure, binding exact candidate, verified spec revisions,
superseded predecessors, authority, result and retrievable evidence. Preserve required Human Gates.
Store it in the existing durable artifact store; the RC fixes its planned evidence destination
before execution. A planned reference is not an observation. A fresh context resolves Deployment
history → RC → final Review. Missing, inaccessible or contradictory evidence cannot prove new
activation. The Deployment history separately owns actual serving state; the Product Release
Record retains its Production purpose. No second completion registry is created.

Specifications can remain at stable paths as intent/implementation while the Review establishes
accepted behavior. Work/navigation status fields are derived; no required post-delivery metadata
commit, spec move or second deployment. Runtime/build Markdown remains an actual build input.
D0 uses candidate-bound outcome/delivery evidence without inventing material Review or spec
activation. Actor, time, predecessor and authority remain in the governing evidence; a status
label alone has no effect.

For an ordinary Harness `1.2.7+` Execution Run, current `run_status` is recorded directly in its
versioned Run Contract. Updating status does not create a second artifact. Git records who changed
it and when. Missions and externally irreversible actions may retain their separately owned event
or evidence models; they do not impose those models on ordinary Runs.

No Contract is immutable. An expressly authorized correction, extension, or schema migration:

1. increments the Contract revision by exactly one;
2. records the concrete reason and Decision/Human Authority;
3. leaves the previous revision in Git; and
4. makes the new revision current only after its applicable check and authorization.

Ordinary Run revision evidence stays in that Contract and Git. It requires no content hash, Run
Contract Revision Event or migration of terminal historical Runs. Non-Run Contract classes keep
their owner-specific revision and review process.

## 5. Traceability Graph

The minimum product chain is:

```text
PRD requirement
  -> actor / provisional use case / outcome
  -> approved Domain Foundation / Context Map
  -> domain specification / public context contract
  -> detailed use case / journey or flow
  -> public contract or architecture decision
  -> milestone -> feature / capability <-> Delivery Slice -> Work Package
  -> acceptance criterion and anti-criterion
  -> implementation and test
  -> Product Delivery Release Candidate and evidence bundle
  -> technical and human acceptance
```

Not every node needs a separate file. Every material link needs a stable identifier and must be discoverable without scanning the whole repository.

For each PRD requirement, traceability MUST reveal whether it is accepted into MVP, deferred with rationale, rejected, or unresolved. For every Feature/Capability it reveals which Slices advance which partial outcomes. For each Work Package, it reveals its parent Slice and which approved requirement or necessary enabler authorizes it. D0 traces task → diff/source → focused result and, when authorized, RC/delivery evidence instead
of this material hierarchy. Missing actual task or delivery authority remains impermissible.

## 6. Change And Invalidation

A material change identifies affected downstream artifacts before approval. The owner classifies each dependent as:

- `unchanged` with rationale;
- `update_required`;
- `re_review_required`;
- `invalidated`;
- `superseded`.

Changed PRD meaning, Bounded Contexts, aggregate/ownership/tenant/cardinality/invariant/role/lifecycle/First-Class decisions, public contracts, core flows, lifecycle state, architecture profiles, or acceptance criteria MUST trigger an impact review under `AH-SPEC-DOMAIN-001` where applicable. Previously green tests or screenshots do not remain valid when their relevant inputs changed.

No artifact is silently rewritten to conceal a decision change. Material changes use a new version
or revision and retain the decision trail. Contracts follow the explicit in-place revision mechanism
in Section 4; raw Evidence remains immutable.

## 7. Handover Boundary

The handover is a curated operational index, not a backlog, journal, specification, or evidence store. It contains only:

- current authorized objective and mode;
- current product, Milestone, Delivery Slice, Work Package, and Execution Run IDs;
- last verified state and immutable checkpoint reference;
- blockers or gates needing attention;
- exact next safe action;
- links to canonical plans, decisions, specs, and evidence.

Detailed history belongs in decisions, review records, checkpoints, and evidence. Completed material moves out of active routing without deleting traceability.

## 8. Truthfulness Rules

- A plan is not implementation.
- Implementation is not verification.
- A mock is not a provider observation.
- A local pass is not a CI or staging pass.
- A deployment event is not proof of user behavior.
- Reviewer agreement is not human acceptance.
- A generated image is not its editable design source.
- An Interactive HTML Mockup/design reference is not Product implementation or a functional prototype.
- A functional prototype contains real Product behavior and requires a post-Initialization Delivery Slice or Technical Risk Experiment lifecycle.
- A Technical Risk Experiment or early verification deployment is not a promotable release candidate.
- A `slice_ready` package is not a technically accepted Delivery Slice.
- Missing access produces `blocked` or `not_observed`, never assumed success.
