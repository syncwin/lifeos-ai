---
name: selfos-routines
description: "Defines and runs personal routines for LifeOS. Use for \"my morning routine\", \"weekly review checklist\", \"start my evening wind-down\", \"add a step to my routine\". Starter skill."
license: MIT
metadata:
  displayName: "SelfOS Routines"
  version: "0.2.1"
  author: "@wasimness"
  company: "SyncWin"
---

# SelfOS Routines
Needs: EntityOS MCP; task store.
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Read the routine from `search_context("routines")`; if none, draft one with the user: name, trigger time, ordered steps, 10 steps maximum.
2. Run: walk the steps one at a time, record done or skipped per step in the task log.
3. Edit: show the diff of steps, wait for a yes, then save.
4. Weekly: summarise completion rate per routine; no judgement words.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- Each routine step is listed in order with its time or trigger.
- Changes update the routine row; nothing was deleted.

## Handoff
Delivered: The routine or checklist, or the updated version.
Next: a step needs a reminder -> `selfos-reminders`; a step is a task -> `selfos-tasks`.

Scratchpad: end per `references/scratchpad.md`.
