---
name: lifeos-self-routines
description: "Defines and runs personal routines for LifeOS. Use for \"my morning routine\", \"weekly review checklist\", \"start my evening wind-down\", \"add a step to my routine\". Starter skill."
license: MIT
---

# Self Routines
Needs: LifeOS MCP; task store.
For self routines, the core `lifeos` plugin is required: if its MCP tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

1. Read the routine from `search_context("routines")`; if none, draft one with the user: name, trigger time, ordered steps, 10 steps maximum.
2. Run: walk the steps one at a time, record done or skipped per step in the task log.
3. Edit: show the diff of steps, wait for a yes, then save.
4. Weekly: summarise completion rate per routine; no judgement words.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- Each routine step is listed in order with its time or trigger.
- Changes update the routine row; nothing was deleted.

## Handoff
Delivered: The routine or checklist, or the updated version.
Next: a step needs a reminder -> `lifeos-self-reminders`; a step is a task -> `lifeos-self-tasks`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
