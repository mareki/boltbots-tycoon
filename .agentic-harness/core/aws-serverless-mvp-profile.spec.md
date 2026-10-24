# AWS Serverless MVP Profile

> Artifact ID: `AH-PROFILE-AWS-SERVERLESS-MVP-001`  
> Artifact class: Profile  
> Authority: Canonical; default technical profile  
> Status: Active  
> Semantic owner: Master Harness AWS Architecture  
> Version: 0.2.1  
> Governing artifacts: `AH-CONSTITUTION-001`, `AH-SPEC-ENGINEERING-001`, `AH-SPEC-COST-001`, `AH-SPEC-WORK-001`  
> Review: `AH-REV-ADMIN-BOOTSTRAP-001`  
> Owns: AWS/CDK/serverless and TypeScript greenfield defaults, environments, Delivery-Slice infrastructure, tags, security, secrets, identity, observability, data, backup, and cost controls

## 1. Selection And Scope

This is the default technical profile for generated products. Initialization records its ID, version, and integrity digest. A different cloud/profile or any weakening exception requires product rationale, impact comparison, and Human Approval.

AWS is an implementation preference, not a domain dependency. Domain and application code remain behind ports; AWS SDKs and event/storage shapes stay in adapters.

## 2. Environment Model

Every product defines:

- `local`: developer/agent runtime with controlled fakes, local services, or sandboxes;
- `staging`: persistent integration and technical acceptance environment using synthetic data;
- `production`: customer environment reached only through promotion.

Staging and production have separate stacks, configuration, identities, secrets, data, deployment roles, and evidence. Separate AWS accounts are preferred when the organization can operate them safely; otherwise the product documents stack/role boundaries and blast-radius controls in one account. A single primary region is the MVP default unless data residency, latency, or recovery evidence requires more.

Temporary preview, verification, experiment, or test resources have owner, Run plus Delivery-Slice/Work-Package/Experiment ID as applicable, expiry, cost tags, and automated cleanup. They are not part of the persistent footprint unless explicitly adopted through normal Product implementation governance.

## 3. Infrastructure As Code

- AWS CDK v2 defines every persistent AWS resource, policy, alarm, log group, backup rule, dashboard, WAF association, and deployment parameter.
- CDK/runtime/compiler/package-manager dependencies, context, Synth command, and bootstrap assumptions are exactly pinned and recorded.
- CI runs format/lint/type checks, unit tests for constructs, `cdk synth`, policy/security analysis, and a reviewed diff before deployment.
- Manual console mutation is prohibited except an authorized incident containment action; any emergency change is recorded and reconciled into CDK or reverted immediately afterward.
- CloudFormation/resource drift and unmanaged-resource inventory are checked before Production Promotion and after incident console changes. Managed drift, unsupported drift checks, and unmanaged resources are classified; unexplained drift stops promotion until reconciled or explicitly accepted.
- Destructive replacement, removal policies, data retention, and cross-stack dependencies are explicit. Production data resources default to retain/protect; disposable staging data follows lifecycle rules.
- Deployment outputs expose only non-secret references needed by tests and evidence.

CDK constructs are organized by product/domain ownership and platform capability. A giant shared stack or universal construct library is not a goal.

### Greenfield TypeScript Default

For a new AWS-serverless web product, the preferred starting stack is:

- TypeScript for CDK;
- Node.js plus TypeScript for Lambda/application adapters and use cases when product/domain evidence does not favor another runtime;
- TypeScript for the web frontend when a web UI applies;
- one explicitly selected package manager with one committed lockfile strategy.

The Product Technical Delta pins exact Node.js runtime, TypeScript, package manager, package-manager runtime, CDK CLI, `aws-cdk-lib`, Constructs, plugins, format/lint/type/test tools, Synth commands, context files, and bootstrap assumptions. Floating tags and unbounded dependency ranges are prohibited for release-candidate identity; CI verifies lockfile-consistent installs and records the exact toolchain in the Product Delivery Release Candidate Manifest.

TypeScript is a productivity, ecosystem, cross-layer consistency, and Lambda cold-start/deployment-size preference—not a Near-Zero Idle Cost invariant. A different language/runtime is valid when the Product Technical Delta compares domain ecosystem, team/agent maintainability, library maturity, security, deployment artifact, cold/warm performance, observability, operating cost, and migration impact. Selection is reviewed in the existing Human Initialization Gate; it creates no separate Human ceremony unless the alternative also triggers an existing profile/cost/security exception.

## 4. Near-Zero Serverless Defaults

Preferred services, only when their semantics fit, are:

- Lambda for request/event/background compute;
- DynamoDB on-demand for access patterns that fit key-value/document modeling;
- S3 for objects/static assets and lifecycle-managed artifacts;
- API Gateway, Lambda Function URLs, CloudFront, EventBridge, SQS, SNS, or Step Functions when the required contract justifies them;
- managed identity such as Cognito when it satisfies product UX, security, tenancy, and recovery requirements.

DynamoDB access patterns, keys, indexes, consistency, hot-key risk, item size, conditional writes, TTL, backup, and ownership are designed before tables. On-demand is the MVP default. Single-table design is optional, never dogma; physical co-location preserves semantic ownership and contract-only interaction.

Lambda functions have explicit memory/timeout, bounded concurrency where needed, idempotency, structured logging, and least-privilege roles. Asynchronous/queued semantics define retry plus DLQ or failure destination when loss/replay risk requires it; synchronous functions instead define timeout, error mapping, idempotency, and upstream retry contract. Functions are not placed in a VPC by default. A VPC, NAT Gateway, interface endpoint/PrivateLink, provisioned concurrency, RDS/Aurora, always-on Fargate, OpenSearch, or other material idle resource follows `AH-SPEC-COST-001` Exception ADR and Human Approval.

## 5. Tagging And Resource Inventory

Every taggable resource receives at least:

- `product`;
- `environment`;
- `owner`;
- `domain` or `platform-capability`;
- `cost-center`;
- `managed-by=cdk`;
- `delivery-slice` for Slice-owned or temporary resources;
- `work-package` for temporary resources;
- `experiment` for Technical Risk Experiment resources;
- `data-classification` where supported and appropriate.

The organization activates the chosen user-defined cost-allocation tags in AWS Billing; resource tags alone are not treated as cost-report evidence. Untaggable or shared charges use the allocation rule from `AH-SPEC-COST-001`.

Post-deploy validation inventories actual resources, required tags, public exposure, deletion protection, retention, backup, and idle-bearing configuration. Unexplained or unmanaged resources block technical acceptance.

## 6. IAM, Secrets, And Configuration

- Humans and workloads receive least-privilege roles; wildcard permissions require scope/rationale and security review.
- Human AWS control-plane access uses individual federated/Identity Center or equivalent identities, MFA, separate least-privilege roles, and audit-recorded sessions. Shared IAM users and long-lived human access keys are prohibited. A time-bounded break-glass path has individual attribution, strong authentication, alerting, reason, post-use revocation, and review.
- CI/CD uses OIDC federation and short-lived AWS credentials. Trust policies bind repository, protected ref/environment, approved workflow, audience, and other available claims. The Staging role cannot mutate Production; the Production role is assumable only by the human-gated Promotion job. Long-lived AWS access keys in CI, local files, or secrets stores are prohibited.
- Untrusted pull-request code receives no cloud credential, secret, Production artifact/cache write, or privileged runner access.
- Runtime credentials, API keys, and sensitive configuration live in AWS Secrets Manager. Non-secret configuration may use typed deployment config or Systems Manager Parameter Store.
- Non-AWS secrets used only by pipeline jobs MAY live in the protected CI environment secret store with narrow job/environment scope, masking, rotation/expiry, owner, and gate; they MUST NOT be copied into runtime configuration.
- Applications retrieve secrets at runtime through narrow roles and cache responsibly; values never appear in CDK outputs, Git, specs, pipeline arguments, logs, screenshots, or evidence.
- Secret creation, access, rotation, expiry, recovery, and deletion have an owner. Rotation automation is risk- and cost-based; material secret lifecycle changes remain human-gated.
- Customer-managed KMS keys are introduced only when policy, cross-account access, or risk requires them; their fixed cost enters the cost model.

## 7. Public Surface And WAF

Public production web applications and APIs use AWS WAFv2 on the applicable CloudFront/API surface by default. The rule set begins small: managed/common protections, rate or abuse control justified by the threat model, redacted sampling/logging, owner, test, and cost. WAF is defense-in-depth; it does not replace authentication, authorization, validation, least privilege, business limits, resilience, or DDoS/cost analysis. Association alone is not security-acceptance evidence.

A WAF exception requires a Security ADR and Human Approval showing exposure, compensating controls, risk, and cost. Staging WAF is risk-based; restricted access may be preferable when it produces the same relevant behavior at lower fixed cost. WAF rules MUST be tested for allowed critical flows as well as intended blocks to prevent self-inflicted outages. When the Production rules are absent from persistent staging, the exact rule revision is tested through an isolated temporary association or equivalent safe harness; unobserved Production behavior remains labeled, and rollout uses count/canary mode where supported plus a tested rollback plan.

No public AWS resource, bucket, function, or API exists merely for convenience. Public access is explicit in CDK and included in the threat model.

## 8. Observability

The MVP observability baseline is lean and actionable:

- structured JSON application logs with timestamp, level, service/context, environment, correlation/trace ID, outcome, and safe error code;
- no secrets or personal data by default; field allowlists/redaction at source;
- CloudWatch log retention of **7 days** by default; longer retention requires product/security/legal reason and cost entry;
- native service metrics before custom metrics;
- low-cardinality custom metrics only when they drive a named decision or alert;
- one operational dashboard, at most two initially without an ADR, covering critical health, errors, latency, throttles/backlog, and user-outcome signal;
- few actionable alarms with severity, owner, runbook, destination, and recovery expectation;
- budget/anomaly signal and tagged cost view sized to the product.

Tracing and verbose/debug logs are sampled or time-bounded. Dashboard, alarm, log ingestion, query, metric, and trace costs belong to the operational-floor model.

## 9. Data, Backup, And Lifecycle

The Product Technical Delta classifies each dataset, owner, retention, deletion, RPO/RTO, backup, restore, and migration need.

- `pre_customer`: staging/production data may be disposable when fixtures and required evidence are reproducible; backups are risk-based.
- `live_customer_data`: critical durable data has enabled and costed point-in-time/versioned/backup protection appropriate to RPO/RTO before the lifecycle gate.
- DynamoDB TTL, S3 lifecycle/versioning, log retention, artifact expiry, and backup retention prevent unbounded accumulation.
- Restore verification occurs before `live_customer_data`, after material backup/restore configuration changes, and thereafter at product-risk cadence—not automatically every night.

Backup existence is not recovery evidence. A restore probe verifies access, integrity, reconstruction steps, isolation, timing, cleanup, and whether the result meets declared RPO/RTO.

## 10. Product Identity Environments And Privileged Bootstrap

When privileged Product access is applicable, CDK provisions only the managed identity infrastructure, Product roles/groups/claims, server-side authorization boundaries, audit path, and a narrowly assumable short-lived provisioning role. CDK and deployment configuration MUST NOT create a Human Product Admin, password, temporary credential, or invitation token and MUST NOT expose one through CloudFormation outputs. Product Admin identities remain separate from AWS Identity Center/IAM operators even when the same person owns both roles.

An exact Human-approved post-deploy action uses the managed identity provider to enroll the protected personal principal reference bound by the Production Run. The action is idempotent and reconciles provider state before mutation: an identical active binding is a no-op; expired, partial, duplicate, wrong-tenant, wrong-role, or conflicting state stops; a new invitation after failure/expiry requires the authority named by the Run. Provider-generated invitation or temporary-secret delivery bypasses Agents, repositories, pipelines, and evidence and forces activation/reset before normal use.

Production privileged identities use MFA by default, record activation, role/tenant scope, MFA status, role changes, last use where available, disable/revoke, recovery, and break-glass events without credential values, and implement the exception path in `AH-SPEC-ENGINEERING-001` where necessary. A public bootstrap endpoint, continuously enabled bootstrap Lambda, permanent shared emergency Admin, or deployment-time re-invite is prohibited. Any temporary provisioning resource/permission is disabled or removed after successful reconciliation.

### Staging Identities And Test Data

Staging maintains stable **product test personas** separately from AWS/operator identities:

- normal-user and admin product roles when those roles exist;
- separate automation normal-user/admin identities;
- individual Human QA accounts for each authorized person when auditability matters.

A shared human test persona is permitted only by explicit approval and can never carry AWS/control-plane, production, or audit-significant authority. An account registry records persona/owner, purpose, role, secret reference, creation, rotation/reset, last use, disable/delete trigger, and an environment-specific account cap.

Credentials remain in authorized secret stores. Tests reuse approved personas rather than continually create accounts, use unique Run-scoped entities beneath them, and clean or deterministically reset state. All data is synthetic. Production identities/data MUST NOT be reused.

Authorization tests cover user/admin denial boundaries; automation accounts receive no broader privileges than their scenario needs.

Staging proves role/tenant denial, activation/reset, expiry/revocation, MFA/step-up where safely testable, and Admin/normal/automation separation using synthetic identities. It never reuses a Production principal, invitation, credential, provider tenant, or customer data. Staging evidence validates contracts and provider integration but does not authorize or prove a real Production Admin.

## 11. Profile Exceptions And Evidence

Every deviation is classified `strengthens` or `exception` in the Product Technical Delta. Exceptions link an ADR, cost/security/operations impact, owner, review trigger, exit/migration path, and Human Approval.

Profile conformance evidence includes CDK source/synth/diff, security and boundary checks, deployed resource inventory, tags, log retention, WAF/public-surface state, secret/IAM configuration without values, backup posture, stable test identities, staging behavior, and operational-floor forecast.

## 12. Official AWS References

- [AWS CDK v2 development guide](https://docs.aws.amazon.com/cdk/v2/guide/develop.html)
- [DynamoDB on-demand capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html)
- [AWS cost-allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html)
- [IAM OIDC federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html)
- [AWS Secrets Manager best practices](https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html)
- [CloudWatch Logs retention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)
- [AWS WAF for API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html)
