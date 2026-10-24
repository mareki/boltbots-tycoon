# Eval Case — {{TITLE}}

> Artifact ID: `{{PRODUCT_OR_HARNESS}}-EVAL-{{NNN}}`  
> Instantiated artifact class: Work contract  
> Revision status: `draft`  
> Work status: `proposed`  
> Semantic owner / revision: Quality / {{REVISION}}  
> Governing specifications/invariants: {{IDS}}  
> Decision Authority / evaluator / reviewer: {{AUTHORITIES}}  
> Target completion level: observed eval result with independent review

## Fixture And Configuration

- Purpose/risk: {{PURPOSE}}
- Fixture/source/version/digest and initial state: {{FIXTURE}}
- Vision/Harness/model/reasoning/prompt/tool versions: {{CONFIG}}
- Data class/isolation/no-side-effect boundary: {{SAFETY}}

## Run Contract

- Allowed/prohibited actions and Human Gates: {{AUTHORITY}}
- Capabilities/budget/trials/stop: {{LIMITS}}
- Expected artifacts/evidence: {{OUTPUTS}}

## Oracle And Rubric

| Observable | Deterministic requirement / score | Threshold | Evidence |
|---|---|---|---|
| {{OUTCOME}} | {{RULE}} | {{THRESHOLD}} | {{REF}} |

## Results

| Trial/config | Outcome | Failures/unauthorized actions | Score/variance | Raw evidence |
|---|---|---|---|---|
| {{TRIAL}} | {{RESULT}} | {{FINDINGS}} | {{SCORE}} | {{REF}} |

Retain every trial. Record blind spots, N/A rationale/authority, baseline comparison, false-positive review, evaluator independence, usage/cost when observable, and final disposition.
