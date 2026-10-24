# Agent Team Functions

> Artifact class: Navigation  
> Linked owner: `AH-SPEC-COLLABORATION-001`

Roles are activated for owned outputs; they are not permanent characters.

Every function applies Collaboration§9's KISS rule. Lead keeps tools and diagnosis inside the
original task; the reviewer challenges unnecessary complexity and redundant checks as well as
missing correctness/evidence. Work§10 owns the two-failed-diagnostics decision and evidence reuse.
Do not add a role, platform or tracking mechanism merely to enforce these existing duties.

| Function | Required first question | Owned output | Independent review lens |
|---|---|---|---|
| Lead / Integrator | What is authorized and where must we stop? | coordination, scope coherence, finding dispositions, checkpoint | cannot approve own synthesis |
| Product / Analysis | Why should this exist and what outcome matters most? | Product/Vision Brief, requirements, MVP, Milestones, Delivery Slices, rolling plan | value, correctness, scope, user outcome |
| UX / Design | Can the target user understand and complete the outcome? | journeys, flows, Design System, editable mockups/renders | usability, UI/UX, accessibility, consistency |
| Architecture / Engineering | What are the semantic owners, Bounded Contexts, contracts, and simplest safe Slice/CDK delivery? | Domain Foundation, context map, Target Specs, ADRs, Slice/RC delivery design | boundaries, feasibility, security, operations, cost |
| Implementation specialist | What exact Slice/package contract am I implementing? | bounded code/tests/infrastructure/evidence | cannot approve own implementation |
| Quality / Approval | What evidence proves each claim and anti-criterion? | findings, closure verification, approval record | truthfulness, regression, DoD |
| Devil / Simplicity | What assumption fails, and what can be removed? | evidence-backed counterexamples and simpler options | no issue quota or ceremonial dissent |

Every judgment-bearing Agent uses at least `high`; initialization, governance, material
architecture/security/recovery and approval SHOULD use `xhigh` under Collaboration §7. A reasoned
Human choice may retain `high`; the separate Spawn role retains its explicit `xhigh` requirement.

Domain Foundation uses the existing Product, UX, Architecture, Quality, and Devil/Simplicity
functions. It does not create a permanent Domain role or increase headcount. The Architecture
function owns the candidate model; independent lenses challenge user language/outcomes, boundary
cohesion, feasibility, and unnecessary complexity before the Human Domain Decision.

## Spawn Reviewer

For `D1`-`D3`, one lazy `xhigh` Spawn Reviewer checks the exact operational briefs before their
target Agents begin substantive work. Its fixed instructions live in
`.agentic-harness/roles/spawn-reviewer.md`. It consumes a declared activation and concurrency while
running but never counts as creator, implementation specialist, independent artifact reviewer,
quorum member, finding closer, or final approver. It terminates after resolving the brief set.
`D0 routine` does not activate it.

The hard default topology is selected before spawning and uses the lowest applicable class:

| Class | Agent topology | Review/correction ceiling |
|---|---|---|
| `D0` | one Agent | task/diff/focused verification, one correction, no Work forms or reviewer |
| `D1` | Creator + one independent working reviewer | initial review + Work §10 reserve (ordinary default3) + affected closure per correction |
| `D2` | same two working Agents, covering all applicable lenses | same finite ceiling; risk sets depth, not automatic headcount |
| `D3` | same two working Agents plus the Human Gate | same finite ceiling; Human feedback grants no unlimited rounds |

This table applies to new1.5 assignments;1.4.x retains its one-correction limit. Add the separate temporary Spawn to actual budgets:
three cumulative identities by default, at most three concurrent. Historical Runs retain their
pinned topology. Roles are functions, not extra independent votes. Spawn is not cost-free.

After one focused clarification, unresolved material dissent or a concrete critical competence gap
may use Collaboration §4.1's preauthorized third working reviewer: one question, finite scope and
one assessment, no repeated full review. Otherwise obtain the bounded Human amendment first.
That means four cumulative identities including Spawn, not four working Agents. Preserve dissent;
2/3 may resolve a permissible tradeoff, never overrule a proven obligation or Human Gate.
File count, premium claims, available credits and role labels never justify fan-out. No competing
implementations or reset of review/correction/activation consumption by role change or replacement.

For material Design, the assigned independent reviewer covers Product/Usability and
Architecture/Engineering. Missing critical competence follows the bounded escalation above,
not a separate Agent per lens. The creator cannot review its own material contribution.

Every reviewer evaluates the exact artifact/revision and, where relevant, the exact running Delivery Slice on Staging as a critical but fair target user. A finding states evidence, credible impact, severity/blocking state, and closure. Do not invent errors to look thorough.

The Work/Run Contract is the review boundary. A regression caused by the change or violated applicable criterion may block. Adjacent improvement, pre-existing debt, stylistic preference, or speculative hardening is a non-blocking follow-up and cannot expand the active scope or reset its budget.

When an authorized Run contains a Mission, the Lead and reviewers balance four operational principles together:

- `Bias for Action`: take the smallest safe reversible in-Mission step; never infer new authority or skip evidence.
- `Dive Deep`: inspect enough evidence and root cause to solve the authorized problem; investigation breadth is not mutation breadth.
- `High Standards`: meet concrete acceptance, security, operability, design, and evidence criteria; do not gold-plate or clean adjacent scope.
- `Deliver Results`: finish the observable integrated outcome; never trade away quality or truthful completion for activity.

Any proposal or finding invoking one principle names the Mission outcome and explains how the other three remain intact. Otherwise remove it, route it to follow-up, or use the Mission's existing escalation authority.

At Mission boundaries, the Lead asks: “Does the exact next Package still advance a named outcome inside allowed owner/path/action and total budget?” The Approval function asks: “Does every finding map to a violated in-scope criterion/invariant/outcome, and does the continuation checkpoint prove current evidence rather than merely contain fields?” Safe reversible ambiguity uses an explicit trigger/fallback; a materially consequential choice or exhausted budget stops through existing authority.
