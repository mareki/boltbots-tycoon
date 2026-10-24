# Human Domain Foundation Review Pack — {{PRODUCT}}

> Artifact ID: `{{PRODUCT}}-DOMAIN-REVIEW-{{NNN}}`
> Instantiated artifact class: Review record
> Status/outcome: `open`
> Decision class: `D3 human-gated`
> Exact Foundation revision/SHA-256: {{TARGET_AND_SHA256}}
> Creator/material contributors: {{AGENTS}}
> Independent reviewers: {{AGENTS}}
> Decision Authority/final Human Approver: {{AUTHORITY}}
> Opened/closed dates: {{DATES}}

## Decision Summary

- Adopted knowledge versus genuinely new learning: {{ADOPTED_AND_NEW}}
- Exact Human decision / real alternatives and Product consequences: {{DECISION_OR_NO_OPEN_MODELING_CHOICE}}
- Recommendation and uncertainty in plain Product language: {{RECOMMENDATION}}
- Domain horizon and proposed Foundation: {{REF}}
- Why these Bounded Contexts: {{EVIDENCE_AND_REJECTED_ALTERNATIVES}}
- Core semantic risks/open decisions: {{RISKS_OR_NONE}}
- Simplest sufficient model and omitted/deferred scope: {{RATIONALE}}

Lead with understandable decisions, not internal IDs/digests; technical bindings follow below.
Do not invent questions when exact Foundation approval is the only remaining decision. Clarify a
Human-reported incomprehensible brief before relying on the response; no comprehension quiz.
At the Gate state the Domain phase and stop before Bootstrap/Product code. A verification Run
with pending Human decision and ineffective Foundation is valid; recheck its revision on resume.

## Review Evidence

- C1 framing and evidence classes: {{REFS}}
- C2 structure, Context Map, source/render: {{REFS}}
- C3 behavior/permissions/use cases/First-Class decisions: {{REFS}}
- Positive, negative, and boundary scenarios: {{REFS}}
- Product/Domain, Architecture/Delivery, and Devil/Simplicity findings: {{REFS}}

## Findings And Dispositions

{{FINDINGS_WITH_SEVERITY_BLOCKING_EVIDENCE_CLOSURE_DISPOSITION_DISSENT}}

## Human Domain Decision

| Exact decision | Allowed value |
|---|---|
| Outcome | `approved | approved_with_overrides | changes_requested | paused | rejected` |
| Foundation revision | {{REVISION}} |
| Covered contexts/horizon | {{SCOPE}} |
| Overrides/accepted risk/owner/trigger | {{DETAIL_OR_NONE}} |
| Human authority/date | {{AUTHORITY_DATE}} |

<!-- domain-review:start -->
```json
{
  "schema_version": "1",
  "harness_version": "{{SEMVER}}",
  "review_id": "{{PRODUCT}}-DOMAIN-REVIEW-{{NNN}}",
  "foundation_id": "{{PRODUCT}}-DOMAIN-FOUNDATION-001",
  "foundation_revision": 1,
  "candidate_sha256": "{{SHA256}}",
  "creator": "{{CREATOR_ID}}",
  "reviewers": ["{{REVIEWER_1_ID}}"],
  "blocking_findings_closed": false,
  "review_outcome": "open",
  "human_decision": {
    "outcome": "pending",
    "authority": "pending",
    "decided_at": "pending",
    "overrides": []
  }
}
```
<!-- domain-review:end -->

This pack indexes the exact model and decision. It is not a second source of Domain meaning and
does not authorize detailed initialization unless the exact Human outcome makes the Foundation
effective.

New1.4.0+ reviews bind their creating Harness version above and use Collaboration's independent
review count; any additional reviewer needs the owning Run's actual allocation/start authority.
Spawn is never a Domain reviewer. Historical blocks without a version retain two reviewers and
are not rewritten by upgrade; explicit pre1.4.0 versions likewise keep their old count.
