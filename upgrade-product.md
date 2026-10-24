# Upgrade An Existing Product To Agentic Harness 1.5.3

This patch withdraws the1.5.2 additions mandating checkout isolation, serialized CI deployment
and a specific Git publication procedure. No replacement mechanism is added. The Harness lease
removal remains. Core replacement preserves Product-owned files; any adaptation remains separately
authorized. The prompt supplies exact target authorization.

```text
I authorize this Product's upgrade to Agentic Harness `1.5.3` from immutable tag `20260930-1.5.3-remove-added-rules` in `https://github.com/langvis/agentic_harness.git`, with withdrawal of the added checkout, CI and Git publication prescriptions while preserving lease removal. The expected source is `1.5.2`; if another supported version is installed, use its actual value as FROM_VERSION and read every intervening impact-history entry.

For this Core-only replacement I override legacy root instructions requiring an upgrade branch, PR or duplicate Human Gate. Do not edit those roots or any Product-owned file except the one recalibration below.

1. Verify the installed Core and actual version/overlay-schema from authenticated Release Metadata. The target must support that exact pair and its complete history; unsupported pairs stop before replacement.
2. Obtain the exact tag's upgrade-product.sh and run it without arguments from Product root. It replaces only .agentic-harness/** and validates or restores the prior Core.
3. Read only printed intervening history and the minimum Product sources needed for impact. Create/resume only docs/harness-state/recalibration-<FROM_VERSION>-to-1.5.3.md; for1.5.2 use docs/harness-state/recalibration-1.5.2-to-1.5.3.md. Do not commit or push.
4. Preserve historical Runs/evidence. Before later live continuation, re-admit at a safe boundary under current rules with actual old mandate, consumed budgets and tighter limits. Defaults do not expand authority.
5. Compare only consumers affected by the actual intervening history. For1.5.2 to1.5.3, identify any Product-owned copies of the withdrawn checkout-isolation, CI-serialization or Git-publication prescriptions. Do not introduce a substitute mechanism. Earlier upgrades also retain the1.5.2 lease removal: new Runs use `capability`, and install/adopt no longer accept `--lease-evidence`. Product-owned lease gates are not removed automatically. Name any actual affected file/job, minimum adaptation, existing check and next authorized action in the same record; record no_change, required_before_continue, trigger-bound deferred or human_decision. Unrelated work is not globally blocked. Logging stays off unless explicitly enabled.
6. Do not automatically rewrite Product plans/specs/Runs/CI/notifiers/code, activate Brownfield adoption or create Domain models/bindings. Routine is allowed only within its actual low-risk/task/delivery authority; material domain work retains Foundation/Exception duties. Product implementation and deployments remain separate.
7. Report observed Core version, history and concrete recalibration/remaining work, then stop. A successful technical swap is not complete Product migration or proven autonomous delivery.
```
