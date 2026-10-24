# Harness Improvement Proposal — {{TITLE}}

> Artifact ID: `{{PRODUCT}}-HIP-{{NNN}}`
> Instantiated artifact class: Decision record
> Version: `{{VERSION}}`
> Status: `draft`
> Decision class: `D3 human-gated`
> Submitted at: `{{YYYY-MM-DD}}`
> Source Product ID: {{SOURCE_PRODUCT_ID_OR_PROTECTED_REFERENCE}}
> Installed Harness version: {{HARNESS_VERSION}}
> Installed Harness manifest SHA-256: {{MANIFEST_SHA256}}
> Evidence custodian/access/retention: {{EVIDENCE_BOUNDARY}}
> Author/material contributors: {{AUTHORS}}
> Independent reviewers: {{REVIEWERS}}
> Semantic owner: {{OWNER}}
> Human Proposal Authority: {{AUTHORITY_OR_PENDING}}
> Confidentiality: {{CLASSIFICATION}}

File this artifact only as `docs/harness-proposals/YYYY-MM-DD-<stable-logical-slug>.md`. Keep the narrative causally useful and concrete. Do not replace evidence with verbosity, fabricate private Agent reasoning, or copy raw Product identity, screenshots, code, logs, PRD text, customer/personal data, credentials, or restricted material upstream.

## Executive Narrative

{{CONCISE_COMPLETE_INCIDENT_STORY}}

## Original Human Assignment And Reasonable Expectation

Describe what the Human asked for, supplied inputs and constraints, the expected Harness behavior, and the authority boundary.

{{ASSIGNMENT_AND_EXPECTATION}}

## Observed Product And Agent Chronology

Describe what Codex and the Agents actually did in relevant sequence: created artifacts/actions, handoffs, discussions, reviews, stops or failures. Distinguish directly inspectable evidence, Human-reported observations, and unavailable private execution detail.

{{CHRONOLOGY}}

## Agent Collaboration And Review Behavior

Explain how Agents divided work, what they agreed or challenged, which premises propagated, how reviewers evaluated the candidate, and why the collaboration did or did not catch the failure. Do not claim hidden chain-of-thought; report observable messages, artifacts, actions, and outcomes only.

{{COLLABORATION_REVIEW}}

## Evaluation Of The Result

Explain why the result succeeded or failed against the assignment, user outcome, applicable Harness rules, evidence, and quality expectations.

{{EVALUATION}}

## Product, User, Cost, Rework, And Trust Impact

State frequency/severity, affected roles/workflows/specs, user/Product impact, effort or cost where observable, rework, risk, and why the Harness—not only this Product—owns the learning.

{{IMPACT}}

## Confirmed Observations, Human Reports, Hypotheses, And Open Decisions

### Confirmed observations

{{DIRECT_EVIDENCE}}

### Human-reported observations

{{HUMAN_REPORTS}}

### Derived causal hypotheses and confidence

{{HYPOTHESES_CONFIDENCE}}

### Evidence gaps and open decisions

{{GAPS_DECISIONS}}

## Generalization, Applicability, And Counterexamples

State the reusable rule hypothesis, applicable Product/context classes, counterexamples, Products for which it must not apply, and risks of overgeneralization.

{{GENERALIZATION_BOUNDARY}}

## Requested Reusable Outcomes

Describe outcomes and invariants. Keep solution direction non-binding until the separate Master Run owns final design.

{{OUTCOMES}}

## Alternatives, Simplicity, And Cost

Compare at least no change, Product-local handling, and a Harness change. Include complexity, ceremony, compatibility/migration, expected benefit, and rejected options.

{{ALTERNATIVES}}

## Expected Compatibility, Migration, Validation, And Evaluation

State expected Harness version class, separate compatibility and supported versions/schema impact, migration/rollback/forward-fix implications, deterministic validators, synthetic evals, false-positive controls, and known blind spots.

{{COMPATIBILITY_EVIDENCE_PLAN}}

## Acceptance Criteria

{{ACCEPTANCE}}

## Anti-Criteria And Non-Goals

{{ANTI_CRITERIA}}

## Evidence, Provenance, Rights, And Data Minimization

State immutable generalized/redacted/synthetic evidence references, custodian/access/retention, rights classification, removed sensitive material, secret/PII/license scans, residual re-identification risk, and which facts cannot be independently verified upstream.

{{UPSTREAM_DATA_REVIEW}}

## Independent Findings, Dispositions, Dissent, And Human Decision

{{PRODUCT_PROCESS_ARCHITECTURE_DELIVERY_DEVIL_FINDINGS_AND_DISPOSITIONS}}

Human outcome: `pending | approved_for_upstream | rejected | deferred | duplicate`. Proposal Approval permits only the exact proposal-only PR and preparation of a separate Master Run/implementation PR path. It does not approve that Run, implementation merge, release, Product adoption, or Product Upgrade.
