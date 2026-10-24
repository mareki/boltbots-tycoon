# Ordinary Run Contract Check

> Artifact ID: `AH-SPEC-ORDINARY-ADMISSION-001`
> Artifact class: Harness specification
> Authority: Canonical Harness specification
> Status: Active
> Semantic owner: Master Harness Governance
> Version: 3.0.4
> Governing artifacts: `AH-CONSTITUTION-001`, `AH-SPEC-ARTIFACTS-001`, `AH-SPEC-COLLABORATION-001`, `AH-SPEC-DOMAIN-001`, `AH-SPEC-WORK-001`, `AH-SPEC-EVALUATION-001`
> Review: `AH-REV-1-5-3-REMOVE-ADDED-RULES-001` (acceptance and limits in the referenced Review; prior historical reviews retained)
> Owns: the direct start check for ordinary non-Mission Execution Runs

## 1. Purpose

An ordinary Run needs one authoritative Run Contract. Before implementation starts, the Harness
checks that Contract and the exact Slice, Work Package, Experiment or Governance targets named in
it. A passing check means only that the documented scope and authority are structurally complete
and non-contradictory. It does not prove that the work is useful, correct or safe in every respect.

The check is deliberately not a repository-health audit. Unrelated repository findings cannot
block the Run and cannot consume the Run's correction or review budget.

## 2. Applicability And Compatibility

This contract applies prospectively to ordinary non-Mission Runs created for Harness `1.2.7` or
newer. Missions keep their separately specified package/checkpoint controls. Read-only analysis
and bounded assignment preparation are not Execution Runs.

New1.5 D0 routine has no Run or task-controls block and never needs a synthetic `--check-run`
pass. Collaboration §4/Work §1 own its task/diff/evidence and Delivery authority.

Read-only preparation and material tasks are nevertheless part of the Human task and subject to Work §5.1 from task entry. The absence
of a Run is not an exemption and does not authorize implementation.

Runs pinned to an older Harness keep their released historical meaning. They do not need migration,
new reports or rewritten evidence merely because the installed Harness was upgraded.

For new1.4.0+ Runs, Collaboration's default is two working Agents plus one separate Spawn Reviewer.
The existing `agent_start` shape stays exactly `applicability, spawn_reviewer, clearance,
cleared_agents`; no renamed `reviewer` key, mixed keys or new activation artifact is introduced.
Historical pre1.5 D0 is exactly one Lead, no reviewer, zero corrections and explicit N/A start values.
A1.5 routine task needs none; an unnecessarily supplied1.5 D0 Run is rejected with that guidance.
D1–D3 name exactly Lead, one independent working reviewer and a different Spawn in `decision.agents`;
`decision.reviewers` excludes Lead and Spawn. Spawn participates only in starts. Cleared IDs must
belong to that allocation; starting requires the Lead pass, completion requires all claimed
participants. The ordinary correction ceiling is three for1.5, one for1.4.x; a deliberately lower nonnegative
limit is valid. Work §10 owns consumption, finite working bound and closure after the final cycle.

Only a bounded exceptional third working reviewer adds `decision.review_escalation`, with exactly
`trigger` (`critical_competence_gap | unresolved_material_dissent`), nonempty `question`, `reviewer`
(the additional independent reviewer ID), and integer `max_reviews: 1`. Existing `effort_override`
names its exact `human-approved:` conditional allocation/amendment; the Run's decision text binds
evidence, scope and the condition actually met before activation. This optional object adds one
focused assessment, not a routine report or additional correction. The allocated identities are
then exactly Lead, two independent working reviewers and separate Spawn. No other Agent is part of
this path. Any correction ceiling above its version default still requires the exact Human effort override and finite
declared value; an override does not suppress identity, start or escalation-shape checks.

Pre1.4.0 Runs retain their historical count/schema checks, including their authorized exceptions.
Current Run start/resume still requires the installed version. Domain Review's own local version
binding selects its count under Domain §8, never the downstream Run or current installation alone;
this preserves previously approved Foundation evidence across upgrades.

## 3. The Single Start Document

The Run Contract is the only ordinary-Run start document. It directly contains:

- Run ID, revision, kind, installed Harness version, status and decision class;
- exact named target IDs and paths;
- observable Product/user outcome, allowed paths and explicit non-goals;
- Decision Authority, Lead, planned Agents, reviewers, reasoning floor and correction ceiling;
- allowed and prohibited external actions;
- required completion evidence; and
- Agent-start applicability and, where required, the Spawn Reviewer's clearance.

These fields may be concise. A field may be `not_applicable` only when the owning specification
permits it and the reason is stated. The Contract must not reproduce the full contents of its named
targets.

The ordinary path creates no Admission Projection, Admission Report, Run State Event, document
hash, digest chain or separate Agent Activation Record. Git supplies change history. Release/Core,
package, build and externally exchanged artifact digests remain governed by their own specifications.

For `domain_foundation`, exact targets are only pre-existing Human authority, Bootstrap/Work
Contract, and named safe inputs. Foundation, review, and Human Domain Decision are outputs. A later
`bootstrap_initialization` Run targets the exact effective Foundation/decision. Product-delivery
Runs target their Work Package and its applicable sources under Domain §12: exact Foundation/decision
or covering model/Legacy Exception for affected Contexts; for a wholly domain-free1.4.1+ Package,
the existing sources supporting its explicit `not_applicable_reason`. No Foundation/exception is
required for that variant. This does not waive bootstrap sequencing or other start prerequisites.

## 4. Direct Check

Reuse a passing check while its Contract, named sources, authority and other checked inputs are
unchanged. Run it at start/resume and after a relevant input change, including status or claimed
Agent-clearance changes before completion. A prose progress update or another file edit inside
unchanged scope does not alone demand another invocation. Work §5.1 still checks actual capability,
resource state and external authority at their action boundary; this structural check proves none
of those live facts. No additional cache, digest list or check-result artifact is required.

The supported entry point is:

```bash
python3 .agentic-harness/validators/validate_harness.py --root . --check-run <run-contract-path>
```

The check reads only:

1. the named Run Contract;
2. the exact source artifacts explicitly named as its targets; and
3. installed release metadata needed to select the applicable contract version.

It applies the run-kind-specific target rule above without discovering unnamed Domain artifacts.

Repository enumeration is permitted only to resolve an exact named Artifact ID when the Contract
does not provide its path. Findings in any other file are outside the result. The command must not
call, depend on or silently turn into full repository validation.

The check fails when the Contract is missing, malformed, not approved, internally contradictory,
below its reasoning floor, beyond its declared team/correction limit, outside its path/action
authority, missing an applicable Agent-start clearance, or names a missing target. Diagnostics identify the
exact field and minimum remediation. It does not auto-fill authority or normalize a failure into a
pass.

### 4.1 Task-Control Evidence For New 1.3.1+ Runs

One `task-controls` JSON block stays in the existing Run progress section, separate from the
unchanged authority block. Its exact fields are `checked_revision`, `progress`, `updates`,
`drift_checks`, and `obligations`. It creates no additional authority or lifecycle state.

- `checked_revision`: positive integer equal to this Run's revision, rebound after a real recheck.
- `progress`: integer 0–100 of the Human task; booleans are not integers. A completed partial Run
  may retain a lower percentage. Only full task completion warrants100%; Run status cannot prove it.
- `updates`: ordered objects with exactly `percent` and nonempty `evidence`. Percentages form the
  complete 10, 20, … prefix through progress. Evidence includes outcome, next action and blocker.
- `drift_checks`: ordered objects with exactly `percent`, `reviewer`, `decision`, `evidence`, forming
  the complete 20, 40, … prefix. Evidence covers Work §5.1's scope, complexity, budgets and forecast.
  Decisions are `continue | simplify | rollback | reimplement | checkpoint_and_escalate`.
  The 40/80 reviewer is a cleared assigned non-author Agent, not the Spawn Reviewer; only D0 uses
  `not_applicable_d0`. Other scheduled checks name the Lead. Event-triggered checks remain in the
  existing findings/evidence section, not fabricated scheduled entries.
  A carried observation may additionally contain `origin_run` with exactly `id` and positive integer
  `revision`. That original Run must already be an exact named `targets` source, not the current Run.
  Its exact revision and original Lead/reviewer/class/clearance assignment govern that observation;
  current assignment still governs every new check. When the original has `1.3.1+` task-controls,
  the original non-carried observation must match the four core fields exactly. Reference the true
  origin directly, never a recursive predecessor chain. For older pinned direct Runs, source-bound
  assignment is checked structurally while the original observation remains semantic evidence; no
  new block is demanded in historical files. Missing, stale or invalid original sources fail closed.
- `obligations`: exactly the eight version-appropriate coverage keys in Work §5.1 (`capability` for1.5.2+; historical `capability_lease` before1.5.2), each with `state` and nonempty
  `evidence`. State is `satisfied | not_applicable | blocked`; evidence binds the current next action,
  owning trigger and observation or non-applicability reason. Non-applicability cannot exempt the
  always-due entry, scope, mutation-boundary, budget or routed-requirement coverage groups.

The checker rejects malformed/duplicate blocks or JSON keys, invalid types, gaps/duplicates,
revision mismatch, missing duty groups, false structural independence, and a `blocked` duty in an
approved/active/verification/completed Run. A blocked/cancelled Run may retain blocked-duty evidence
for diagnosis, but the direct start/continuation command must reject its blocked/cancelled status.
Completed Runs require every claimed participating Agent to have recorded clearance. Recheck this
same Contract when due under §4 at Work §5.1 boundaries; missing or stale observations forbid affected continuation.

Recovery uses Work §5.1's honest missed-duty evidence within the same block. The checker proves
documented structure and consistency only: it cannot verify real-time delivery, prior-progress
monotonicity across unseen snapshots, semantic applicability, evidence truth, actual external state
or out-of-band tool actions. A passing check never substitutes for those owning controls or Human
approval. Existing historical Runs are not rewritten or forced to acquire this block by upgrade.
The original-source check reads only an already named target and does not recursively admit that
historical Run or enumerate its dependencies. It verifies recorded assignment/available observation
binding, not historical timing, authority authenticity or the truth of older free-text evidence.

## 5. Status And Revision

The current ordinary-Run status is written directly in the Contract and is one of `approved`,
`active`, `verification`, `blocked`, `completed` or `cancelled`.

- `approved` means the Decision Authority approved the stated revision and the direct check passed.
- `active` means implementation started under that approved revision.
- `verification` means implementation stopped and the declared evidence is being checked.
- completed/cancelled status records the result and residual risk;1.5 administrative reentry
  follows Work §7, retaining valid mandate, original consumption and non-author reviewed revision.

A material change to scope, authority, allowed action, target identity or budget increments the
Contract revision and requires the Decision Authority again. It does not require a second document
or content hash. The previous version remains available in Git. Routine progress and evidence links
may be updated without manufacturing a revision event or Spawn pass. Assignment clearance is
independent of an in-scope candidate correction; affected content approval remains revision-bound.

## 6. Separate Repository Validation

Full Harness validation remains useful for CI, upgrades, release assembly and explicitly requested
repository-wide audits. It is not an ordinary-Run admission prerequisite. Its findings are reported
separately and do not change the result of `--check-run`.

### 6.1 Completed-Run Start-Omission Disposition

The current validator MAY recognize one optional `agent-start-recovery` JSON block in the existing
completed ordinary Run. This is an additive incident disposition, including for historical
1.2.7+ direct contracts: the original contract/schema/version/start fields are not migrated.
It does not admit active, approved, blocked, cancelled or verification work, nor waive any other
contract, evidence, Domain, integrity or Human-Gate finding. No CI switch or Run-ID allowlist exists.

The block has exactly: `schema_version` (`1`), `run_id`, positive `run_revision`,
`contract_sha256`, `reviewer`, `reviewed_at` (UTC ISO8601), `assessment`, `evidence`,
`unresolved_findings` (empty), and `human_decision`.
The contract binding is SHA256 of the unchanged parsed `run-contract` serialized as sorted-key
compact JSON (`sort_keys=True, separators=(",", ":")`, ASCII escaping). This single incident binding
prevents stale use after any contract edit; it creates no general ordinary-Run digest chain.
`evidence` is a nonempty list of unique exact safe relative regular-file paths and their SHA256s,
each object exactly `path, sha256`; it names the reviewed outputs/evidence, never this same Run.
Content changes invalidate the disposition, rather than silently inheriting approval. Only those
explicit evidence paths are read; no repository enumeration or recursive Run admission is added.

`reviewer` is an actually participating independent reviewer listed in the original contract, not
its Lead, creator/material contributor or Spawn Reviewer. `assessment` records the original
assignment/source assessment, omission consequences, preserved prior reviews, corrected gaps and
residual limits. Semantic truth and real authority remain independently reviewed evidence, not
facts a JSON parser can prove. `human_decision` has exactly `authority` (the original Decision
Authority), `approval_ref` (an exact `human-approved:` reference), and `accepted_risk` (nonempty
specific risk/disposition). Collaboration §1.2 governs actual and conditional Human decisions.

Recovery requires `agent_start.applicability: required`, `clearance: not_applicable`, and the
original well-formed start fields, never a manufactured `pass`. All recorded original participants
are covered by the actual retrospective assessment, not retrospectively cleared. The absence of
timely clearance alone no longer blocks the completed Run or its genuine independent40/80
observations; reviewer identity/independence, complete progress/duty evidence and all other checks
remain enforced. Original missed-duty evidence is preserved and its consequences explicitly
resolved; no fabricated timely observations or hidden findings are permitted.

Absent recovery retains existing behavior. Duplicate/malformed/stale recovery blocks, wrong
subject/revision, missing/changed/unsafe evidence, self-review, absent Human disposition, unresolved
findings or use outside completed status fail closed. Direct and full validation share this rule.
A direct success for a recovered completed Run MUST identify it as historical recovery, not start
authorization. A new/active Run still needs its normal Spawn pass; recovery cannot be carried over.

## 7. Verification

Deterministic tests must prove:

- a minimal valid D0/D1 Contract passes without reports, events, hashes or extra roles;
- each missing or contradictory authority-critical field fails precisely;
- an exact missing or duplicate target fails;
- an unrelated invalid historical or current file does not affect `--check-run`;
- `--check-run` does not invoke full repository validation;
- older historical Runs remain readable without migration;
- full repository validation remains independently callable; and
- a first `domain_foundation` Contract passes without naming future outputs, while a downstream Run
  fails on a missing/stale effective Foundation or required Legacy Exception.

Current regression controls include two working Agents plus distinct Spawn, missing/foreign/self
reviewer, false D0, uncleared/foreign participants, mixed start keys, unauthorized or malformed
third-reviewer allocation, correction limits, and supported historical controls. A valid Domain
Run in verification awaiting Human decision remains admissible without making its Foundation
effective. Bootstrap still rejects missing Human approval or stale candidates. Full Domain and
direct admission use the same version-appropriate independent-review and Human/candidate checks.

## 8. Acceptance And Non-Goals

Accepted only when an ordinary Run can start from one approved, directly checked Contract and no
supported ordinary workflow asks for a projection, report, event chain, document digest or separate
activation artifact.

The direct check adds no role, lifecycle state, service, repository audit, or Human Gate of its own.
It enforces only the exact Domain decision required by `AH-SPEC-DOMAIN-001` and does not claim
semantic correctness, Product value, rendered quality, security approval, or operating-system
containment.
