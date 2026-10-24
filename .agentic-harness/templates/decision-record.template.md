# Decision Record — {{TITLE}}

> Artifact ID: `{{PRODUCT}}-ADR-{{NNN}}`  
> Instantiated artifact class: Decision record  
> Status: `proposed`  
> Decision class / classification trigger ID: {{D0_D1_D2_D3}} / {{TRIGGER_ID}}
> Classification evidence: {{CONCRETE_AFFECTED_OUTCOME_AND_EVIDENCE}}
> Author / reviewers: {{AUTHOR_AND_REVIEWERS}}  
> Owner / Decision Authority / Human Gate: {{AUTHORITIES}}  
> Target revisions: {{TARGETS}}  
> Date: {{DATE}}  
> Evidence references: {{REFS}}

## Context And Decision Needed

{{PROBLEM_REQUIREMENT_CONSTRAINT_EVIDENCE}}

Explain what is already established, what is newly learned, and the exact real choice in ordinary
Product language. State consequences and recommendation/uncertainty before technical IDs or
appendices. If no choice remains, say so; do not invent questions or a new Gate to fill this form.

## Product Vision And User Impact

{{WHY_USER_OUTCOME_QUALITY_IMPACT}}

## Options

| Option | Product/UX | Architecture/security/operations | Idle/usage cost | Reversibility/migration | Evidence/uncertainty |
|---|---|---|---|---|---|
| {{OPTION}} | {{IMPACT}} | {{IMPACT}} | {{COST}} | {{REVERSIBILITY}} | {{EVIDENCE}} |

List all credible options. If the search finds fewer than expected, document the search boundary instead of inventing alternatives.

## Decision And Rationale

{{CHOICE_WHY_SIMPLEST_COHERENT}}

## Consequences, Risks, And Follow-Up

{{POSITIVE_NEGATIVE_OWNER_TRIGGER_EXIT_PATH}}

## Override / Exception

If applicable: human instruction, prior challenge, accepted risks/cost, scope, expiry/review trigger, and rollback/exit.

For an approved Brownfield Legacy Exception, retain and resolve this block; otherwise remove it:

<!-- legacy-domain-exception:start -->
```json
{
  "schema_version": "1",
  "context_id": "{{CONTEXT_ID}}",
  "change_scope": ["{{REPOSITORY_RELATIVE_PATH}}"],
  "exact_change": "{{EXACT_MATERIAL_CHANGE}}",
  "reason": "{{WHY_EXCEPTION_IS_NEEDED}}",
  "alternatives": ["{{MODELING_OR_SMALLER_SCOPE_ALTERNATIVE}}"],
  "decision": "approved",
  "human_authority": "{{EXACT_HUMAN_AUTHORITY_REF}}",
  "owner": "{{RISK_AND_CLOSURE_OWNER}}",
  "expiry_or_review_trigger": "{{TRIGGER}}",
  "accepted_risk": "{{SEMANTIC_RISK}}",
  "affected_runs": ["{{EXACT_RUN_ID}}"],
  "modeling_disproportionate_because": "{{CONCRETE_COST_OR_DELAY_RELATIVE_TO_CHANGE}}"
}
```
<!-- legacy-domain-exception:end -->

## Review And Approval

{{REVIEW_ID_FINDINGS_DISPOSITIONS_FINAL_AUTHORITY}}
