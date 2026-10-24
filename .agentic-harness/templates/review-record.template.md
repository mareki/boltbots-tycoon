# Review Record — {{TARGET}}

<!-- Final path: docs/reviews/YYYYMMDD-<harness-semver>-<stable-logical-name>-review.md -->

> Artifact ID: `{{PRODUCT}}-REVIEW-{{NNN}}`  
> Instantiated artifact class: Review record  
> Review date: `{{YYYY-MM-DD}}`
> Harness version: `{{SEMVER}}`
> Status/outcome: `open`  
> Target artifact/revision/SHA-256: {{EXACT_TARGET}}  
> Decision class: {{D1_D2_D3}}  
> Initial review or affected correction closure: {{REVIEW_SCOPE_AND_AUTHORITATIVE_RESERVE_REF}}
> Creator/material contributors: {{AGENTS}}  
> Required functions and actual reviewer Agent IDs: {{AGENTS}}  
> Decision Authority / Final Approver / Human Gate Owner: {{AUTHORITIES}}  
> Opened/closed timestamps: {{TIMESTAMPS}}
> Evidence references: {{REFS}}

## Vision And Review Contract

- Product Vision revision: {{VISION}}
- Effective Domain Foundation/context coverage or approved Brownfield legacy exceptions: {{DOMAIN_BINDINGS}}
- Target user/why/outcome: {{RESTATEMENT}}
- Original Human task/requirements and authorized changes: {{ORIGINAL_SOURCE_REFS}}
- Acceptance criteria and existing plan/worklist: {{IDS_AND_PLAN_REF}}
- Anti-criteria: {{IDS}}
- Evidence references: {{REFS}}
- Perspective-specific questions: {{QUESTIONS}}
- In-scope review boundary / follow-up routing: {{BOUNDARY_AND_FOLLOW_UP_INDEX}}

Before reviewing the diff, trace each original requirement through the existing plan to actual
implementation and evidence. Reference that criterion map rather than creating another tracker.
Record missing required results as open findings; do not silently move them to follow-up. Reuse
valid existing evidence and keep local/model/simulated observations distinct from real deployment.

## Independent Findings

| ID | Reviewer | Class `in_scope_blocking/in_scope_non_blocking/adjacent_follow_up` | Severity `critical/major/minor/observation` | Blocking | Violated criterion/invariant/Mission outcome or follow-up owner-trigger | Observable evidence/impact | Requested closure |
|---|---|---|---|---|---|---|---|
| {{FINDING}} | {{AGENT}} | {{CLASS}} | {{SEVERITY}} | {{BOOL}} | {{MAPPING}} | {{EVIDENCE_IMPACT}} | {{CONDITION}} |

No finding quota applies. Do not convert taste, remote hypotheticals, or wording preferences without outcome impact into blocks.

Apply the evidence-led simplicity invariant: every non-obvious mechanism must map to a confirmed requirement, observed problem, or concretely applicable higher obligation and named outcome. Prefer the simpler sufficient approach; omit or defer generic future-proofing and extreme edge cases with a concrete trigger. Unjustified complexity is an in-scope quality defect, while hypothetical hardening cannot expand the active scope.

Reviewers do not create competing implementations. Findings for this target revision are consolidated before correction. Adjacent improvements and pre-existing debt are routed as non-blocking follow-ups; they do not expand scope or reset the cycle ceiling.

For Agent-behavior changes, apply Evaluation§5.1 in this record: predeclare one/two work samples,
candidate/inputs, outcomes/valid controls, fresh subjects, assessor and the five-minute-per-call
plus five-minute-shared-assessment limit. Preserve actual outputs, tool/usage limitations and
pass/fail/incomplete reasons here or linked existing evidence. No automatic repeats or mandatory
extra artifact; larger trials/formal assurance need explicit bounded Human selection.

Under1.4.0+ the assigned independent reviewer covers all required compatible lenses; multiple role
labels remain one voice. The separate Spawn Reviewer checks starts only, never content quorum.
For1.5 Work §10 owns one technical reserve and one affected closure per material correction.
No independent exhausted review counter; the last permitted cycle may finish closure.
After one clarification, unresolved material dissent or a critical competence gap may use an
authorized third working reviewer for one exact question. Preserve its independent evidence and
remaining dissent;2/3 resolves only permissible tradeoffs, never an evidenced obligation or Gate.

## Dispositions And Verification

| Finding | `accepted/mitigated/rejected-with-rationale/deferred-with-owner-trigger/override` | Change/evidence | Originating reviewer closure |
|---|---|---|---|
| {{ID}} | {{DISPOSITION}} | {{REF}} | {{STATUS}} |

## Critical-User Review

For a running product record correctness, outcome completion, usability/flow, UI/UX consistency, accessibility, trust, relevant latency, errors/denial/recovery, avoidable effort, mockup differences, and staging evidence.

For a `material_ui` Run instantiate this projection in the existing Review record. Every listed
image is a real raster file under `docs/reviews/evidence/{{RUN_ID}}/**`, matches its SHA-256, and
must be actually available to and inspected by the named reviewer. Omit it for `minor_ui`
and `non_visual` unless proportionate visual evidence adds decision value.

<!-- visual-review-evidence:start -->
```json
{
  "schema_version": "1",
  "run_id": "{{RUN_ID}}",
  "candidate": {"id": "{{CANDIDATE_ID}}", "source_commit": "{{COMMIT}}"},
  "design_reference": {"id": "{{REFERENCE_ID}}", "sha256": "{{SHA256}}"},
  "representative_coverage": "{{COVERAGE_RULE}}",
  "images": [
    {
      "id": "{{IMAGE_ID}}",
      "role": "candidate | baseline",
      "artifact_ref": "docs/reviews/evidence/{{RUN_ID}}/{{IMAGE_FILE}}",
      "sha256": "{{SHA256}}",
      "surface": "{{SURFACE_ID}}",
      "state": "{{STATE_ID}}",
      "viewport": "{{WIDTH}}x{{HEIGHT}}"
    }
  ],
  "comparisons": [
    {"candidate_image_id": "{{CANDIDATE_IMAGE_ID}}", "baseline_image_id": "{{BASELINE_IMAGE_ID}}"}
  ],
  "review": {
    "reviewer_id": "{{PRODUCT_UX_REVIEWER_ID}}",
    "capability": "browser | image_tool",
    "inspected_image_ids": ["{{IMAGE_ID}}"],
    "axes": ["composition", "hierarchy", "proportions", "density_whitespace", "clipping", "consistency", "usability"],
    "outcome": "approved | changes_requested"
  },
  "creator_material_contributor_ids": ["{{CREATOR_ID}}"],
  "final_approver_id": "{{PREDECLARED_DECISION_AUTHORITY_REF}}"
}
```
<!-- visual-review-evidence:end -->

## Final Material Acceptance

Finalize this existing record immutably only after actual evidence and closure; draft/planned
location is not acceptance. D0 routine does not instantiate it. Artifact §4 is the owner.

- Exact final candidate / deployment evidence: {{IMMUTABLE_REFS}}
- Verified specification revisions / superseded predecessor revisions: {{EXACT_REFS}}
- Non-author Final Approver / authority / actual result / timestamp: {{ACCEPTANCE}}
- Durable destination fixed by RC / discoverability from deployment history: {{REFS}}

Missing/inaccessible/contradictory final evidence does not prove activation. Work/navigation labels
are derived. No spec move or post-delivery metadata commit is required; runtime Markdown still
counts as Product/build input. Production Release Record retains its separate purpose.

## Dissent, Conditions, And Decision

- Remaining dissent/risk owner/review trigger: {{DISSENT}}
- Conditions/expiry: {{CONDITIONS}}
- Final outcome and approver: {{OUTCOME_AUTHORITY}}
- Human decision reference where required: {{REF}}
