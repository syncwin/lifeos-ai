---
name: selfos-routines
description: "Defines and runs personal routines for LifeOS. Use for \"my morning routine\", \"weekly review checklist\", \"start my evening wind-down\", \"add a step to my routine\". Starter skill."
license: MIT
metadata:
  displayName: "SelfOS Routines"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# SelfOS Routines
Needs: EntityOS MCP; task store.

1. Read the routine from `search_context("routines")`; if none, draft one with the user: name, trigger time, ordered steps, 10 steps maximum.
2. Run: walk the steps one at a time, record done or skipped per step in the task log.
3. Edit: show the diff of steps, wait for a yes, then save.
4. Weekly: summarise completion rate per routine; no judgement words.

Next: `lifeos-selfos`.

Scratchpad: end per `lifeos/references/scratchpad.md`.
