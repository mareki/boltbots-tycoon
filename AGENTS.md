# Product Agent Entry Point

Every new Agent context MUST begin by reading, in order:

1. `README.md`
2. `docs/handover.md`
3. `.agentic-harness/manifest.md`
4. `.agentic-harness/policies/operating-policy.md`
5. `docs/specs/spec-routing.md`
6. the effective Domain Foundation and Product Vision when they exist
7. only the specifications, contracts, work, and evidence routed for the task

Root `AGENTS.md` is seeded once and then Product-owned. Release-specific Harness rules and workflows live only inside `.agentic-harness/**`, so compatible upgrades never need to rewrite this file. Product-specific guidance belongs in `docs/agent-extensions.md` and cannot weaken Human instructions or the installed Core.

Harness installation is a completed, separate phase and never authorizes Product initialization or implementation.

Applicable installed duties begin with the Human task, including entry and preparation. The protected
Manifest/Operating Policy route supplies them; no repeated rules or special Human prompt is needed.

Before any `D1`-`D3` Agent performs judgment-bearing work, follow the Agent-start control loaded
through `.agentic-harness/policies/operating-policy.md`. A dedicated Spawn Reviewer must clear the
exact routed assignment before substantive work; it cannot implement or approve that work.
