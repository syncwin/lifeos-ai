---
name: workos-report
description: "Day start and day end reports for LifeOS WorkOS. Use for \"start my day\", \"morning plan\", \"end of day report\", \"what did I finish today\", \"weekly wrap\". Plain language, fixed template per audience."
license: MIT
metadata:
  displayName: "WorkOS Reports"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Reports
Needs: EntityOS MCP; task store; `workos-log` rows for the day.

1. Audience and headings: `search_context("audiences, report headings, tone")`. Missing: ask once.
2. Start: priorities, objectives in triage order, blockers, open manager questions, task plan with estimates.
3. End: finished, produced, carried; evidence per item; one tracker write for the whole day. Last working day of the week folds in the week end.
4. Plain words, no jargon. Verify against the log before saving.

Next: `lifeos-verifier`, then save.

Scratchpad: end per `lifeos/references/scratchpad.md`.
