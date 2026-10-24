# Workflow: Upgrade Product Harness

> Artifact ID: `AH-VIEW-WORKFLOW-UPGRADE-001`
> Artifact class: Generated view
> Source owner/revision: `AH-SPEC-EVOLUTION-001`, `AH-SPEC-DISTRIBUTION-001`, exact release manifest
> Generator/source: Master Harness release assembler / canonical workflow projection

## Replace The Core

1. Use the authorized upgrade request for the exact target and its disclosed changes. No duplicate
   confirmation when the request already grants this authority. Obtain the target release's parameterless `upgrade-product.sh` from its exact authenticated immutable tag.
2. Run it from the Product repository root. It verifies actual installed version/schema, supported pair, Core, target Manifest and complete
   adjacent-history chain before swap.
3. Replace exactly `.agentic-harness/**` under one filesystem lock and recoverable directory swap. The swap does not rewrite or require a particular Product lifecycle, Run status, branch or clean worktree.
4. Validate the exact target. A repeated invocation is a validated no-op. Failure restores the prior Core.
5. Do not change any path outside `.agentic-harness/**`.

Core replacement never validates historical Product Runs against newly introduced fields and never
rewrites Product-owned Contracts. A completed Contract remains governed by its pinned revision.

For `1.3.1+`, the replaced protected Manifest routes old root entry chains to current Operating
Policy and Work §5.1. Verify that route during installation validation; do not edit a Product root
to add it. New tasks include preparation in duty/progress accounting and new ordinary Runs use the
compact task-control evidence. This does not retroactively rewrite past observations or require a
Run merely to perform the separately authorized Core replacement.

For a Product installed before `1.0.6`, a retained root Upgrade-PR/Human-Gate instruction remains binding unless the Human's exact upgrade request explicitly overrides it for the compatible Core-only replacement. Do not modify the Product-owned root file.

## Recalibrate The Product

1. Read only the intervening `.agentic-harness/history/**` entries reported by the script.
2. Compare their concrete impact with the minimum relevant current Product Vision, plan, Slices, Work Packages, Runs, design, and evidence.
3. Create or resume one Product-owned `docs/harness-state/recalibration-<from>-to-<to>.md`.
4. Use only `no_change`, `required_before_continue`, `deferred` with trigger, or `human_decision` with an exact question.
5. Never rewrite Product plans automatically. Route any required change through normal Product authority.

An old Contract keeps its pinned historical meaning. Do not migrate or rewrite it merely because
the Harness changed. A newly authorized `1.2.7+` ordinary Run uses the single current Run Contract
and `--check-run`; it creates no Admission Report, Run State Event, document hash or Agent Activation
Record.

A change outside `.agentic-harness/**` is not a compatible upgrade. It requires an explicitly authorized Product migration and still may not overwrite Product files silently.

Upgrade does not retroactively activate Domain Foundation governance in an existing Product. Keep
historical Contracts pinned. Use the separate Brownfield adoption workflow to record root/routing
integration and Context coverage; apply the ratchet only when later work changes a named Context.

For1.5 recalibrate only affected old root Run/Slice requirements, RC consumers, obsolete Product-owned lease gates,
spec-move/status consumers, durable final Review access and CI/notifier triggers. Separately
authorize required Product edits; an unavailable path blocks its own delivery/acceptance claim.
Re-admit live work at a safe boundary under current rules, carrying consumed budgets and actual
old authority. Historical evidence is unchanged; defaults never retroactively increase authority.

For1.5.1 make the same existing recalibration record actionable for each affected consumer:
name its actual file/job or state owner, observed old assumption, minimum necessary adaptation,
existing verification command/example, readiness impact and authorized next action. Use only
applicable rows; this is not an extra audit or document:

| Consumer | Concrete adaptation to inspect |
|---|---|
| Root instructions / work plans | Remove unconditional Work hierarchy for D0 through normal Product authority; material multi-step work links one persistent original-requirement plan. |
| Fast checks / deploy helpers | Exercise changed helpers and actual configuration/permission contracts before the slow deploy step; local mocks do not establish cloud permissions. |
| CI path filters | Distinguish runtime/build inputs from plan/review/harness-log-only changes; preserve real Markdown build inputs, avoid metadata-only redeploys. |
| Completion / notifier | Read accepted candidate/result and required task outcomes; cover routine and repair completion without Spec moves or fragile Work-field spelling. Wait for relevant delivery result; retry only the missing notification step when safe. |
| Removed lease mechanism | Remove obsolete Product-owned lease commands/gates under Product authority. The1.5.2 additions prescribing checkout isolation, CI serialization and Git publication are withdrawn in1.5.3. No replacement mechanism; Core replacement does not edit Product consumers. |
| New Mission checkpoints / logging | Use readable intent/path references under1.5.1 without rewriting old pins; logging stays off until requested and stores reports in Product-owned docs/harness-logs. |

Derive this from the few affected files/history entries. If no change is needed, cite the observed
match. The Core-only step never applies these Product edits, runs their pipeline or declares them
verified. Report the smallest concrete follow-up and let independent work continue.

For archive/notification consumers found in that affected scope, check existing CI run/attempt
identity (or byte-identical stored-result reuse) so reruns do not overwrite or collide with prior
evidence. Prefer the existing completion data contract; a Markdown parser must match its actual
producer/template and include the relevant repair case in its focused contract test. No new
status schema or external Product change is authorized by Core replacement.
