# Product Release Policy — {{PRODUCT}}

> Artifact ID: `{{PRODUCT}}-RELEASE-POLICY-{{NNN}}`
> Instantiated artifact class: Product specification
> Authority: Product-wide application-release identity
> Revision status: `draft`
> Semantic owner: Product / Architecture / Delivery
> Revision/version: {{REVISION}}
> Governing artifacts: `AH-SPEC-PRODUCT-RELEASE-001`, `AH-SPEC-DELIVERY-001`
> Review: `{{REVIEW_ID_OR_PENDING}}`

## Release Unit And Version Source

- Product release unit: {{WHOLE_PRODUCT_OR_DEFINED_RELEASE_SET}}
- Primary version scheme: `semver | calver | other_deterministic_monotonic`
- Exact grammar and ordering: {{GRAMMAR_ORDER}}
- Initial-version rule: {{RULE}}
- Single version source of truth/path: {{OWNING_ARTIFACT_OR_GENERATED_SOURCE}}
- Version decision owner and evidence: {{OWNER_METHOD}}
- Alternative-to-SemVer rationale or `not_applicable`: {{PRODUCT_REASON_OR_NA}}

## Compatibility And Increment Policy

- Compatibility audience: {{USERS_OPERATORS_API_SDK_EVENT_FILE_AUTOMATION_CONSUMERS}}
- Compatibility surfaces and promises: {{CONTRACTS_AND_SUPPORT_WINDOWS}}
- Major/breaking or equivalent rule: {{RULE_EXAMPLE}}
- Minor/capability or equivalent rule: {{RULE_EXAMPLE}}
- Patch/correction or equivalent rule: {{RULE_EXAMPLE}}
- Prerelease/build metadata treatment: {{RULE}}

## Product Tags, Candidates, And Publication

- Immutable Product Git-tag grammar: {{DEFAULT_PRODUCT_V_EXACT_VERSION_OR_OTHER}}
- Final RC version state before Production: `reserved_unpublished`
- Verification Candidate Product version/tag: `not_applicable`
- Collision and uniqueness check: {{METHOD}}
- Product Release Identity Ledger location and event ID grammar: {{RULE}}
- Collision domain: active reservations, consumed/partial/skipped/published states, Release Records, and local/remote Product tags
- Reservation-transfer and crash-reconciliation rules: {{RULES}}
- Successful publication evidence: {{PRODUCT_RELEASE_RECORD_AND_DEPLOYMENT_LEDGER_PATHS}}
- Failed/corrected unpublished candidate treatment: {{RULE}}
- Published version/tag immutability rule: {{RULE}}

## Components, Migrations, And Recovery

- Component-version policy: {{ONE_PRODUCT_VERSION_MAP_OR_JUSTIFIED_INDEPENDENT_COMPONENTS}}
- Release-set mapping to deployable artifact digests: {{METHOD}}
- Database/API/event/file schema version relationship: {{SEPARATE_IDENTITIES_AND_MAPPING}}
- Migration/upgrade compatibility: {{RULE}}
- Rollback/hotfix/forward-fix version treatment: {{RULE}}
- Discontinued versions/support communication: {{RULE}}

## Operational Discovery And Evidence

- Safe operator-visible current-version diagnostic: {{ROUTE_OR_COMMAND}}
- User-visible support version, when useful: {{SURFACE_OR_NOT_APPLICABLE}}
- Product Release Record location/ID grammar: {{RULE}}
- Deployment Ledger location and current-serving projection: {{RULE}}
- Release-note location/ID grammar: {{RULE}}

## Examples And Anti-Criteria

{{AT_LEAST_ONE_VALID_MAJOR_MINOR_PATCH_OR_EQUIVALENT_EXAMPLE}}

- Harness versions, Delivery Slice IDs, RC IDs, deployment IDs, and schema versions never substitute for the Product version.
- Staging or a `verification_candidate` never publishes or consumes a Product version.
- Published versions/tags are never moved, reused, or assigned different bytes or meaning.
