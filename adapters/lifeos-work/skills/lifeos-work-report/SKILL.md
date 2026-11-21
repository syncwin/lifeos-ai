---
name: lifeos-work-report
description: "Day start and day end reports for LifeOS Work. Use when the user says \"start my day\", \"morning plan\", \"end of day report\", \"plan tomorrow\", \"what did I finish today\", or \"weekly wrap\". Plain language, fixed template per audience."
license: MIT
---

# Work Reports
Needs: LifeOS MCP; task store; `lifeos-work-log` rows for the day.
For work report, the core `lifeos` plugin is required: if its MCP tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

1. Audience and headings: `search_context("audiences, report headings, tone")`. Missing: ask once.
2. Open and Close templates and their rules (no hours as achievement, failed attempts count, `None` for empty sections): `${CLAUDE_PLUGIN_ROOT}/references/execution-and-reporting.md`; tracker write rules: `${CLAUDE_PLUGIN_ROOT}/references/workbook-and-tracker-spec.md`.
3. Start: priorities, objectives in triage order, blockers, open manager questions, task plan with estimates.
4. End: finished, produced, carried; evidence per item; one tracker write for the whole day. Last working day of the week folds in the week end.
5. Plain words, no jargon. Verify against the log before saving.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- The report uses the audience's headings and plain words, and every item has evidence from the log.
- One tracker write for the whole day; the report was checked against the log before saving.

## Handoff
Delivered: A day-start or day-end report, saved after the verifier pass.
Next: verify, then save -> `lifeos-verify`; returned tasks -> `lifeos-work-sprint`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
