---
name: lifeos-workos-report
description: "Day start and day end reports for LifeOS WorkOS. Use when the user says \"start my day\", \"morning plan\", \"end of day report\", \"plan tomorrow\", \"what did I finish today\", or \"weekly wrap\". Plain language, fixed template per audience."
license: MIT
---

# WorkOS Reports
Needs: EntityOS MCP; task store; `lifeos-workos-log` rows for the day.
Start: run the `lifeos` router first if it has not run.

1. Audience and headings: `search_context("audiences, report headings, tone")`. Missing: ask once.
2. Open and Close templates and their rules (no hours as achievement, failed attempts count, `None` for empty sections): `lifeos-workos-sprint/references/execution-and-reporting.md`; tracker write rules: `lifeos-workos-sprint/references/workbook-and-tracker-spec.md`.
3. Start: priorities, objectives in triage order, blockers, open manager questions, task plan with estimates.
4. End: finished, produced, carried; evidence per item; one tracker write for the whole day. Last working day of the week folds in the week end.
5. Plain words, no jargon. Verify against the log before saving.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- The report uses the audience's headings and plain words, and every item has evidence from the log.
- One tracker write for the whole day; the report was checked against the log before saving.

## Handoff
Delivered: A day-start or day-end report, saved after the verifier pass.
Next: verify, then save -> `lifeos-verify`; returned tasks -> `lifeos-workos-sprint`.

Scratchpad: end per `lifeos/references/scratchpad.md`.
