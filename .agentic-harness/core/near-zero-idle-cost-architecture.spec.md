# Near-Zero Idle Cost Architecture

> Artifact ID: `AH-SPEC-COST-001`  
> Artifact class: Harness specification  
> Authority: Canonical  
> Status: Active  
> Semantic owner: Master Harness Architecture And FinOps  
> Version: 0.1.0  
> Governing artifacts: `AH-CONSTITUTION-001`, `AH-SPEC-ENGINEERING-001`, `AH-SPEC-INITIALIZATION-001`  
> Review: `AH-REV-MASTER-001 / section-05`  
> Owns: Near-Zero Idle Cost definition, measurement, defaults, exception path, evidence, and scaling reevaluation

## 1. Objective

Near-Zero Idle Cost Architecture means a product creates little variable cloud cost when no user invokes it and keeps its unavoidable operational floor explicit, measured, and small. It is an architecture objective, not a promise of literal zero cost.

The default ceiling is a conservative estimated monthly operational floor of **EUR 25 per product**, across the required persistent staging and production footprint combined, unless the Human Product Authority approves a product-specific exception.

The target is evaluated without promotional credits or temporary free-tier assumptions. Taxes, currency conversion date, region, and amortized annual charges such as domain registration are stated rather than hidden.

## 2. Cost Model

Every product maintains a versioned cost model with:

- pricing date, currency conversion date, provider, account, and region;
- resource/service, environment, semantic owner, and allocation tags;
- `fixed_idle`: charged merely because the resource exists;
- `storage_idle`: retained bytes, backups, artifacts, logs, and snapshots;
- `scheduled_floor`: mandatory regression, backup, monitoring, certificate, or maintenance activity that runs without users;
- `usage_variable`: requests, compute time, transfer, messages, reads/writes, and third-party calls;
- `step_cost`: thresholds that add capacity or fixed resources;
- expected MVP usage scenarios and uncertainty range;
- observed post-deploy cost and variance from estimate.

The **operational floor** is `fixed_idle + storage_idle + scheduled_floor`. It includes every provider required to operate staging and production: cloud, CI/CD, DNS/domain, e-mail, authentication, monitoring, security, storage, and other mandatory SaaS. “No traffic” MUST NOT omit scheduled jobs, backups, observability, WAF/security controls, retained data, unavoidable health checks, bots/baseline scans, or required non-production environments.

Shared or organization-level services use a documented, consistent allocation driver. The model records the shared service's total cost, allocation rule, participating products, and this product's amount. Shared labeling cannot reduce a benefiting product's allocation to zero.

The planning estimate uses a pinned pricing snapshot, 730 hours per normalized month for hourly resources, zero human-user traffic, all mandatory scheduled/background activity, all persistent environments, allocated shared/third-party cost, and an explicit uncertainty range. The conservative supported upper estimate must be at or below EUR 25. If a credible range materially crosses the ceiling, the product needs correction or an Exception ADR; averages, favorable FX, tax treatment, credits, or rounding cannot manufacture compliance.

## 3. Architectural Defaults

Prefer capabilities that scale to zero or charge per use:

- event/request-driven compute;
- on-demand/key-value or object storage where access patterns fit;
- managed queues/events with no reserved capacity;
- static delivery and edge caching;
- ephemeral build/test resources and automatic environment cleanup;
- storage lifecycle, retention, TTL, compression, and cardinality control;
- shared fixed-cost controls only where isolation and risk permit.

These are preferences, not permission to force a poor data or domain model. The chosen service must satisfy contracts, access patterns, consistency, recovery, security, latency, and operability.

## 4. Fixed-Cost Pressure

The default architecture MUST NOT introduce the following without an ADR, quantified alternatives, and explicit Human Approval:

- always-on virtual machines or containers;
- always-on relational database capacity;
- NAT gateways or equivalent hourly network appliances;
- provisioned search, streaming, cache, or analytics clusters;
- private connectivity endpoints with material hourly charges;
- provisioned concurrency or reserved minimum compute;
- per-environment duplication of a material fixed-cost control when safe sharing or an on-demand design exists;
- any managed service whose minimum capacity alone threatens the operational-floor target.

Security, legal, recovery, or product correctness may justify an exception. Cost pressure MUST NOT remove a required control or force an unsuitable persistence model; it triggers an explicit trade-off decision.

## 5. Exception ADR

An exception records:

- requirement that the default cannot satisfy;
- all credible lower-idle alternatives, normally at least two, and why they fail; if fewer exist, the searched solution space and market/technical constraint rather than invented options;
- exact service/configuration and environments;
- monthly idle, scheduled, and usage cost estimates with pricing references;
- expected traffic/load point where the option becomes preferable;
- security, reliability, data, latency, migration, and vendor-lock implications;
- budget owner, expiry/review trigger, downscale/cleanup, and exit path;
- Human Approval reference.

An exception is scoped; it does not waive cost review for adjacent resources.

## 6. Cost In Architecture And Delivery

Every material architecture decision and infrastructure Work Package states:

- change to operational floor;
- variable cost drivers and expected use;
- tags/allocation owner;
- cost test or inspection method;
- cleanup and rollback behavior;
- whether it remains under the current ceiling.

Initialization provides an estimated baseline. Staging deployment verifies the actual resource inventory, idle-bearing configurations, tags, and updated forecast. At deployment, a named Cost Owner creates a reconciliation Work Package with provider-specific billing-lag assumption and due dates: by default after 14 full observed days and again after the first complete billing month. Observations are monthly-normalized with the same allocation and activity assumptions and retain an uncertainty band.

Unless a profile is stricter, variance is material when it crosses the EUR 25 ceiling or exceeds the greater of EUR 5/month and 20 percent of the estimate. An unexplained material variance invalidates cost acceptance and creates a correction or Exception-ADR decision; merely updating the model is insufficient. A package cannot be technically accepted while an unexplained material fixed-cost resource exists.

## 7. Growth And Re-Architecture

Pay-per-use services may become more expensive than provisioned capacity under sustained traffic. The team monitors measured request volume, duration, data access, transfer, concurrency, latency, and cost per user/outcome.

Re-architecture is proposed when observed data crosses a predeclared review threshold—not because of hypothetical future scale. The decision compares total cost, engineering effort, operational burden, reliability, migration risk, and reversibility. High traffic may justify provisioned compute or relational capacity through the normal ADR and Human Approval path.

## 8. Cost Controls Without Dashboard Sprawl

Cost governance uses allocation tags, budget/anomaly signals, resource inventory, and a small number of actionable views. Creating many dashboards, custom high-cardinality metrics, alarms, or scheduled tests can violate the objective even when application compute scales to zero.

Each control needs an owner, decision it enables, monthly cost estimate, alert destination, and deletion/review trigger. Duplicate or unactionable controls are removed.

## 9. Acceptance And Anti-Criteria

Acceptance requires:

- a complete operational-floor inventory across persistent environments;
- conservative supported upper total at or below EUR 25/month or an approved exception;
- no reliance on expiring credits;
- cost-bearing resources and scheduled activity mapped to owner and purpose;
- post-deploy inventory/forecast evidence and later billing reconciliation;
- cleanup and scale-review triggers.

Anti-criteria include:

- claiming “zero cost” while fixed or scheduled costs exist;
- choosing a service only because it is serverless despite incompatible access patterns;
- hiding staging, security, monitoring, backup, storage, or data-transfer cost;
- optimizing hypothetical scale with an always-on service before measured need;
- reducing essential security, data integrity, accessibility, or recovery merely to meet the ceiling.
