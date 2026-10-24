# Workflow: Optional Harness Logging

> Artifact ID: `AH-VIEW-WORKFLOW-HARNESS-LOGGING-001`
> Artifact class: Generated view
> Source owner/revision: `AH-SPEC-WORK-001` §9.1, `AH-SPEC-EVOLUTION-001`, exact release manifest
> Generator/source: Master Harness release assembler / canonical workflow projection

## Activation And Recording

Logging is off by default. An explicit instruction such as “enable Harness logging for this task”
activates only that task. Record the instruction, current state and report path in the existing
task/Run/handover context. D0 remains task/diff/evidence; create no Run merely for logging.

1. Use the existing task identity to create one report from the shipped
   [template](../templates/harness-log.template.md) at `docs/harness-logs/YYYY-MM-DD-<task>.md`.
   Do not overwrite an unrelated report. Late activation records earlier gaps honestly.
2. At existing work boundaries and significant failures/interventions, append short observed
   actions, relevant sanitized input/output summaries, factual reasons, results and evidence links.
   Capture known roles, repeats, waits and times; leave unknown data unknown. No full transcripts,
   private model reasoning, secrets or unnecessary personal/customer data.
3. On pause, retain current logging state, report path, actual open work and next step in the
   existing handover. Replace current outcome/resume fields in place, retaining earlier events
   as history. A fresh context reads them and continues the same task's enabled report.
4. On explicit disable, persist `disabled` in that same context and stop recording. On task end,
   mark `finished` with the observed outcome. Preserve the report; never inherit activation into
   another task or reactivate after resume from an obsolete enable instruction.

Use existing observations and references. No extra Agent, validation, permission round, service,
automatic export or mandatory logging-only commit/deployment. Report a failed write honestly;
repair it proportionately within the task, without declaring the whole task failed solely for
diagnostic logging. Sanitized reports may accompany normal authorized commits. The report does
not alter original evidence, budgets, scope or completion authority.

## Later Analysis On Request

Read only the requested reports. Compare requirement completion, corrections, Human interventions,
waits, repeated checks and observed outcomes. Cite source reports/entries and distinguish a
recurring observation from a causal hypothesis. Report missing data and unlike task/risk classes;
do not infer universal reliability or savings from the sample. Twenty or thirty reports are a
possible useful collection, never a required quota or reason to manufacture additional runs.
Any actual upstream improvement proposal uses the existing HIP workflow and authority. Analysis
does not change rules, upload reports or schedule background work automatically.
