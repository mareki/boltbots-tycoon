# Bootstrap And Installation State — {{PRODUCT}}

> Artifact ID: `{{PRODUCT}}-BOOTSTRAP-001`  
> Instantiated artifact class: Work contract  
> Revision status: `active`  
> Work status: `active`  
> Bootstrap lifecycle state: `installed_uninitialized | intake_ready | modeling_domain | awaiting_human_domain_gate | domain_foundation_effective | initializing | awaiting_human_initialization_gate | initialized`
> Semantic owner / revision: Harness Bootstrap / {{REVISION}}  
> Governing specifications: `AH-SPEC-DISTRIBUTION-001`, `AH-SPEC-INITIALIZATION-001`  
> Decision Authority / reviewers: {{AUTHORITY_REVIEWERS}}  
> Target completion level: `initialized` after Human Initialization Approval

## Installation Identity And Verification

- Harness release/tag/source commit: {{IDENTITY}}
- Expected external manifest SHA-256 and trust source: {{DIGEST_TRUST_SOURCE}}
- Actual manifest/protected-payload tree SHA-256: {{DIGESTS}}
- Installation actor/time/tool: {{ACTOR_TIME_TOOL}}
- Last verification evidence: {{IMMUTABLE_REF}}
- Selected Product Technical Delta/profile lock: {{REF_OR_PENDING}}

## Current Transition

| Prior state | Current state | Actor/time | Input/Run/Review IDs | Guard and transition evidence |
|---|---|---|---|---|
| {{PRIOR}} | {{CURRENT}} | {{ACTOR_TIME}} | {{IDS}} | {{EVIDENCE}} |

## Input Snapshot

- Human initialization instruction: {{EXACT_REF}}
- PRD and optional-input safe snapshot/digests: {{REFS}}
- Sensitive/restricted protected-store references: {{REDACTED_REFS_OR_NOT_APPLICABLE}}
- Candidate/active Product Vision revision: {{REF_OR_NOT_AVAILABLE_WITH_REASON}}
- Candidate/effective Domain Foundation revision: {{REF_OR_NOT_AVAILABLE_WITH_REASON}}
- Human Domain Decision reference: {{REF_OR_PENDING}}

## Next Allowed Transition

- Guard: {{GUARD}}
- Exact next safe action: {{ACTION}}
- Required decision/capability: {{NEED}}
- Stop condition: {{STOP}}

This state does not authorize delivery implementation. The handover links this exact revision and never owns Bootstrap truth.
