---
name: selfos-tasks
description: "Personal task capture and review for LifeOS. Use when the user says \"add a task\", \"what is on my plate\", \"what is due this week\", \"mark X done\", \"what is overdue\", or \"add this to my to-do list\". One task list, no side lists."
license: MIT
metadata:
  displayName: "SelfOS Tasks"
  version: "0.2.0"
  author: "@wasimness"
  company: "SyncWin"
---

# SelfOS Tasks
Needs: EntityOS MCP; task store (`references/tracker.md`).
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Capture: save the user's words verbatim as the title, then due date, priority, owner. Ask only for what is missing.
2. Review: list open tasks by due date, overdue first, at most two in progress.
3. Change or close: update the row; no deletes (`references/rules.md`, Task store).
4. Priority rules and categories: `search_context("priorities")`.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- Each task has the user's words as title plus due date, priority and owner (asked only when missing).
- At most two tasks are in progress; nothing was deleted.

## Handoff
Delivered: The task list or the saved change.
Next: needs a nudge -> `selfos-reminders`; record -> `workos-log`.

Scratchpad: end per `references/scratchpad.md`.
