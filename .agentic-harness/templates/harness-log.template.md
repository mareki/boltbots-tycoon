# Harness Log — {{TASK}}

> Artifact class: Reference
> Task / original request reference: {{TASK_REF}}
> Harness version / source reference: {{VERSION_AND_SOURCE}}
> Logging: {{enabled_disabled_finished}}
> Activation / current-state observation: {{HUMAN_INSTRUCTION_AND_OBSERVED_TIME}}

Create only after explicit activation for this task. Work §9.1 owns the behavior.
Use one report in docs/harness-logs/YYYY-MM-DD-<task>.md. Keep it concise; no new Run for D0.
State changes and this path belong in the existing task/Run/handover context for fresh resume.

## Requested Result And Starting Facts

{{ORIGINAL_OUTCOME_RELEVANT_FACTS_AND_REFERENCES}}

## Observed Course

| Observed time or unknown | Agent role / phase | Action and short factual reason | Result / existing evidence |
|---|---|---|---|
| {{TIME}} | {{ROLE_PHASE}} | {{ACTION_REASON}} | {{RESULT_REF}} |

Record significant boundaries, failures, retries, waits and Human interventions, not every tool call.
Summarize only relevant sanitized input/output. Separate observed facts, Human reports and causal
hypotheses; missing time, usage or evidence stays unknown. Do not store private model reasoning,
full prompt/tool dumps, credentials or unnecessary personal/customer data.

## Outcome Or Resume

Keep these current fields up to date in place; earlier events stay in the course history.

- Actual result / unresolved original requirements: {{RESULT_OPEN}}
- Existing plan, evidence and next safe action: {{REFERENCES_NEXT}}
- Observed corrections, Human interventions and elapsed/wait time, or unknown: {{OBSERVATIONS}}
- Logging state and reason: {{ENABLED_DISABLED_FINISHED_REASON}}

Keep earlier failures visible. This report is diagnostic, not acceptance or execution authority.
No mandatory extra commit, deployment or Agent work is created by this report.
