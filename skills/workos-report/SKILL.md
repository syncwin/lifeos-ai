---
name: workos-report
description: "Day start and day end reports for LifeOS WorkOS. Use when the user says \"start my day\", \"morning plan\", \"end of day report\", \"plan tomorrow\", \"what did I finish today\", or \"weekly wrap\". Plain language, fixed template per audience."
license: MIT
metadata:
  displayName: "WorkOS Reports"
  version: "0.2.4"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Reports
Needs: EntityOS MCP; task store; `workos-log` rows for the day.
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Audience and headings: `search_context("audiences, report headings, tone")`. Missing: ask once.
2. Start: priorities, objectives in triage order, blockers, open manager questions, task plan with estimates.
3. End: finished, produced, carried; evidence per item; one tracker write for the whole day. Last working day of the week folds in the week end.
4. Plain words, no jargon. Verify against the log before saving.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- The report uses the audience's headings and plain words, and every item has evidence from the log.
- One tracker write for the whole day; the report was checked against the log before saving.

## Handoff
Delivered: A day-start or day-end report, saved after the verifier pass.
Next: verify, then save -> `lifeos-verifier`; returned tasks -> `workos-sprint`.

Scratchpad: end per `references/scratchpad.md`.
