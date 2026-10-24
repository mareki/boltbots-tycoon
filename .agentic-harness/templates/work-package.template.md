# Work Package — {{TITLE}}

> Artifact ID: `{{PRODUCT}}-WP-{{NNN}}`  
> Instantiated artifact class: Work contract  
> Revision status: `draft`  
> Work status: `proposed`  
> Semantic owner / revision: {{OWNER_REVISION}}  
> Governing specifications: {{SPEC_IDS_VERSIONS}}  
> Milestone / Delivery Slice / Feature-Capability outcome: {{IDS_AND_OUTCOME}}  
> Decision class / classification trigger ID: `{{D1_D2_D3}}` / `{{TRIGGER_ID}}`
> Classification evidence: {{CONCRETE_AFFECTED_OUTCOME_AND_EVIDENCE}}
> Creator: {{AGENT}}  
> Reviewers / Final Approver: {{AGENTS_AND_AUTHORITY}}  
> Review record: {{REVIEW_ID_OR_PENDING}}  
> Target completion level: {{LEVEL}}
> Mission ID / outcome / order / budget allocation or `none`: {{MISSION_MAPPING_OR_NONE}}

## Vision And Outcome

- Product Vision revision: {{VISION}}
- Target user/outcome: {{OUTCOME}}
- Requirement/use case/flow IDs: {{IDS}}
- Material workflow UI: exact existing interaction-meaning revision/delta, or reasoned reuse/N/A: {{FLOW_REFERENCE_OR_RATIONALE}}
- Package contribution: {{WHY_THIS_PACKAGE}}
- Deployment impact `none/application/infrastructure/migration/mixed`: {{IMPACT}}
- Early-verification trigger or `none`: {{TRIGGER_RATIONALE}}

## Scope

- In scope: {{BEHAVIOR}}
- Non-goals: {{NON_GOALS}}
- Do not touch: {{PATHS_BEHAVIOR_ENV}}
- Domains/contracts/UI/data/infrastructure affected: {{IDS}}
- Effective Foundation/context revisions or approved Brownfield legacy-exception references, or justified domain-free applicability under Domain §12: {{DOMAIN_BINDINGS}}
- Active current specs and approved Target revisions: {{IDS_VERSIONS}}
- Dependencies/order: {{DEPENDENCIES}}
- Mission continuation evidence and next guard or `not_applicable`: {{MISSION_CONTINUATION_OR_NA}}
- Pre-mutation intent: named Mission outcome, exact Package revision, behavior, permitted owners/paths/environments/actions, invariants/non-goals, criteria, remaining budget, and reversible-assumption reference or `not_applicable`: {{INTENT_BINDING_OR_NA}}

## Acceptance Criteria

Use this existing section as the criterion owner; reference the original requirement and Human
changes, current open/verified state, evidence and remaining step here or in the existing Run plan.
Do not duplicate the same status in another checklist. A criterion with no observed required
evidence stays open; scope reduction requires its owning Human authority.

| ID | Observable condition | Evidence level/method |
|---|---|---|
| {{AC_ID}} | {{CONDITION}} | {{EVIDENCE}} |

## Anti-Criteria

| ID | Prohibited observable outcome | Detection/evidence |
|---|---|---|
| {{ANTI_ID}} | {{OUTCOME}} | {{METHOD}} |

## Approach And Simplicity

- Known problem, current evidence, and affected user/Product outcome: {{PROBLEM_EVIDENCE_OUTCOME}}
- Proposed approach: {{APPROACH}}
- Simplest sufficient alternative and why it does or does not satisfy the same obligations: {{OPTION_AND_DECISION}}
- Evidence mapping for every non-obvious complexity: {{REQUIREMENT_PROBLEM_OR_APPLICABLE_OBLIGATION}}
- Hypothetical, generic, or extreme-edge cases deferred with concrete activation triggers: {{DEFERRED_CASES_AND_TRIGGERS_OR_NONE}}

## Verification And Recovery

- Risk tier/test layers: {{PLAN}}
- Package-local evidence / deferred parent-Slice Staging-provider-visual-security-cost evidence: {{PLAN_AND_EXACT_CRITERIA_MAP}}
- Migration/flags/cleanup: {{PLAN}}
- Rollback/last safe boundary: {{PLAN}}
- Stop boundary and known risks: {{BOUNDARY}}
- Coordination budget: {{CREATOR_REVIEWERS_MAX_ACTIVE_INITIAL_REVIEW_CORRECTION_CLOSURE_LIMITS}}

Use Collaboration's version-appropriate topology. Under1.4.0+ default to two working Agents plus
separate temporary Spawn; count actual identities, not role names. Early flow review consumes the
existing review budget. A conditional third working reviewer needs one exact question, evidence,
authority and finite additional allocation, not another implementation or full-review loop.
- Escalation authority/reference or `none`: {{AUTHORITY_OR_NONE}}

<!-- domain-binding:start -->
```json
{
  "schema_version": "1",
  "contexts": [
    {
      "id": "{{CONTEXT_ID}}",
      "foundation_ref": "{{EXACT_PATH_AND_REVISION_OR_NONE}}",
      "legacy_exception_ref": "{{EXACT_PATH_OR_NONE}}"
    }
  ]
}
```
<!-- domain-binding:end -->

For a wholly domain-free Package under Harness1.4.1+, replace the object above with
`{"schema_version":"1","contexts":[],"not_applicable_reason":"concrete reason and effective scope/context decision reference"}`.
Retain exactly one Binding block. Cite the actual supporting decision in existing Package sources
and exact Run targets. The independent reviewer verifies the entire scope; unknown impact is not
domain freedom. With affected Contexts use the original variant without `not_applicable_reason`.
Domain §12 owns this rule; do not invent a Context, Foundation, Legacy Exception or extra document.

For a Package created by bounded Mission instantiation, retain this projection inside the existing Work Contract; omit it for `none` or an exact predeclared sequence:

<!-- mission-package:start -->
```json
{
  "schema_version": "1",
  "mission_id": "{{MISSION_ID}}",
  "run_id": "{{RUN_ID}}",
  "instantiation_index": 0,
  "depends_on": "none",
  "outcomes": ["{{OUTCOME_ID}}"],
  "semantic_owners": ["{{OWNER_ID}}"],
  "path_prefixes": ["{{SAFE_RELATIVE_PREFIX}}"],
  "environments": ["{{ENVIRONMENT_OR_NONE}}"],
  "external_actions": ["{{ACTION_OR_NONE}}"],
  "decision_class": "D1",
  "decision_authority": "{{NON_HUMAN_PACKAGE_AUTHORITY}}",
  "max_agents": 3,
  "max_corrections": 1
}
```
<!-- mission-package:end -->

`slice_ready` means the exact Package revision passed its own evidence/review and is integrated into its parent Slice candidate. It is not staging-verified, technically accepted, or independently deployable by default.

D0 routine does not instantiate this Package or Domain Binding. For1.5 Mission projection,
`max_corrections` references the exact Mission total, not a local allowance; checkpoint consumption
is cumulative for that Mission. Work §10 owns counting. Final material Review under Artifact §4
establishes acceptance; Work labels are derived and require no post-delivery spec move/commit.
