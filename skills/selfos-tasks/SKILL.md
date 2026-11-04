---
name: selfos-tasks
description: "Personal task capture and review for LifeOS. Use for \"add a task\", \"what is due this week\", \"mark X done\", \"what is overdue\". Starter skill; one task list, no side lists."
license: MIT
metadata:
  displayName: "SelfOS Tasks"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# SelfOS Tasks
Needs: EntityOS MCP; task store (`lifeos/references/tracker.md`).

1. Capture: save the user's words verbatim as the title, then due date, priority, owner. Ask only for what is missing.
2. Review: list open tasks by due date, overdue first, at most two in progress.
3. Change or close: update the row; never delete (`lifeos/references/rules.md`, task store).
4. Priority rules and categories: `search_context("priorities")`.

Next: `selfos-reminders` if the task needs a nudge.

Scratchpad: end per `lifeos/references/scratchpad.md`.
