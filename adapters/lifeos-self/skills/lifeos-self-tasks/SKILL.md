---
name: lifeos-self-tasks
description: "Personal task capture and review for LifeOS. Use when the user says \"add a task\", \"what is on my plate\", \"what is due this week\", \"mark X done\", \"what is overdue\", or \"add this to my to-do list\". One task list, no side lists."
license: MIT
---

# Self Tasks
Needs: LifeOS MCP; task store (`${CLAUDE_PLUGIN_ROOT}/references/tracker.md`).
For self tasks, the core `lifeos` plugin is required: if its MCP tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

1. Capture: save the user's words verbatim as the title, then due date, priority, owner. Ask only for what is missing.
2. Review: list open tasks by due date, overdue first, at most two in progress.
3. Change or close: update the row; no deletes (`${CLAUDE_PLUGIN_ROOT}/references/rules.md`, Task store).
4. Priority rules and categories: `search_context("priorities")`.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- Each task has the user's words as title plus due date, priority and owner (asked only when missing).
- At most two tasks are in progress; nothing was deleted.

## Handoff
Delivered: The task list or the saved change.
Next: needs a nudge -> `lifeos-self-reminders`; record -> `lifeos-work-log`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
