# Product Delivery Release Candidate Manifest — {{SLICE_ID}}

> Artifact ID: `{{PRODUCT}}-DELIVERY-RC-{{NNN}}`  
> Instantiated artifact class: Evidence  
> Observation state: `observed`  
> Harness version: `{{SEMVER}}`
> Work identity: `slice | routine`
> Candidate classification: `final | verification_candidate`  
> Promotion state: `eligible_after_technical_and_human_gates | non_promotable`  
> Product release version state: `reserved_unpublished | not_applicable`
> Intended Product version: `{{VERSION_OR_NOT_APPLICABLE}}`
> Proposed Product release tag: `{{TAG_OR_NOT_APPLICABLE}}`
> Product Release Policy ID / revision SHA-256: `{{POLICY_ID_OR_NOT_APPLICABLE}}` / `{{SHA256_OR_NOT_APPLICABLE}}`
> Timestamp/environment: {{TIME_BUILD_ENVIRONMENT}}  
> Immutable subject: {{SLICE_REVISION_AND_STAGING_MERGE_COMMIT}}  
> Raw evidence references: {{PIPELINE_PROVENANCE_AND_ARTIFACT_REFS}}  
> Slice ID / Contract SHA-256: `{{SLICE_ID}}` / `{{SHA256}}`  
> Milestone ID / revision SHA-256: `{{MILESTONE_ID}}` / `{{SHA256}}`  
> Included Package Set SHA-256: `{{SHA256}}`  
> Feature-Capability Mapping SHA-256: `{{SHA256}}`  
> Source commit: `{{GIT_COMMIT_40_TO_64_HEX}}`  
> Source tree SHA-256: `{{SHA256}}`  
> Specification Set SHA-256: `{{SHA256}}`  
> Application Artifact Set SHA-256: `{{SHA256}}`  
> Migration Set SHA-256: `{{SHA256}}`  
> Lockfile Set SHA-256: `{{SHA256}}`  
> SBOM SHA-256: `{{SHA256}}`  
> Toolchain Identity SHA-256: `{{SHA256}}`  
> Staging Assembly Tree SHA-256: `{{SHA256}}`  
> Staging Diff SHA-256: `{{SHA256}}`  
> Production Assembly Tree SHA-256: `{{SHA256}}`  
> Production Diff SHA-256: `{{SHA256}}`  
> Build Provenance SHA-256: `{{SHA256}}`  

For `routine` under1.5, omit Slice/Milestone/Included Package Set/Feature-Capability digest headers
and the package table. Replace them with nonempty `Task reference`, `D0 rationale` and `Delivery
authority` headers. Retain exact source/build/spec/toolchain/environment/provenance/recovery inputs
from existing build data, final version reservation and Production Gate. No Run/WP/Slice/independent
material Review is invented. `final | verification_candidate` stays a separate classification.
For `slice`, retain all original work bindings. Never mix both variants.

## Product And Work Identity

- Product / lifecycle state: {{PRODUCT}} / `pre_customer | live_customer_data`
- Intended Product version/tag and Policy revision, or explicit verification-candidate `not_applicable`: {{PRODUCT_RELEASE_IDENTITY}}
- Product Vision / MVP / Milestone / Delivery Slice revisions: {{REFS}}
- Feature/Capability partial outcomes: {{IDS_OUTCOMES}}
- Approved Slice Contract and Review digests: {{REFS}}

The Included Package Set digest is SHA-256 over byte-sorted UTF-8 rows `package-id TAB contract-sha256 TAB source-commit LF` from this exact table:

| Package ID | Contract SHA-256 | Source commit |
|---|---|---|
| `{{PACKAGE_ID}}` | `{{SHA256}}` | `{{GIT_COMMIT_40_TO_64_HEX}}` |

## Source And Specification Identity

- Repository / source tree / final `staging` merge commit: {{REFS_DIGESTS}}
- Active and approved Target Spec digests: {{REFS_DIGESTS}}
- Migrations / generated API-schema assets / data-lifecycle state: {{REFS_DIGESTS}}

## Application And Toolchain Artifacts

| Artifact or pin | Version/digest/immutable reference |
|---|---|
| Application/frontend/functions/migrations | {{REFS}} |
| Lockfiles and dependency inventory/SBOM | {{REFS}} |
| Node/runtime, TypeScript/compiler, package manager | {{PINS}} |
| CDK CLI, `aws-cdk-lib`, Constructs/plugins | {{PINS}} |
| Synth command, context, bootstrap assumptions | {{REFS}} |

## Environment-Specific IaC

| Environment | Cloud-assembly tree/templates/assets digest | Reviewed diff/parameters | Permitted difference rationale |
|---|---|---|---|
| Staging | {{DIGESTS}} | {{REFS}} | {{RATIONALE}} |
| Production | {{DIGESTS}} | {{REFS}} | {{RATIONALE}} |

## Provenance, Validity, And Recovery

- Trusted pipeline/build identity: {{REF}}
- Prior green recovery candidate / Deployment Ledger: {{REFS}}
- Retention/expiry: {{RULE}}
- Planned durable final Review destination (material) or task/outcome evidence (routine): {{REF}}
- Staging deployment and evidence refs, when observed: {{REFS_OR_PENDING}}
- Planned evidence addresses are not observed acceptance. Deployment history points here, then to
  the final immutable material Review or routine result. No post-delivery spec move is required.
- Invalidators: any relevant source, spec, package, migration, dependency, toolchain, context, assembly, diff, or artifact change

A `final` candidate uses `reserved_unpublished` and exact version/tag/Policy bindings. A `verification_candidate` uses `not_applicable` for Product version, tag, and Policy binding; it is always `non_promotable`, cannot consume or imply a Product version, cannot activate Target Specs, and cannot satisfy final Slice completion. Production promotion of a final candidate rebuilds or resynthesizes nothing.
