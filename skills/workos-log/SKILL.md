---
name: workos-log
description: "Audit trail of work for LifeOS WorkOS. Use for \"log this\", \"record what I did\", \"note the decision\", \"add to the question queue\", after any chat that changed files or records."
license: MIT
metadata:
  displayName: "WorkOS Log"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Log
Needs: task store (`lifeos/references/tracker.md`); EntityOS MCP for tag vocabulary.

1. Log as you go: one row per unit of work with what, evidence (path, link, command output), tag, status.
2. Decisions, questions and flags go to their own tables, not into free text.
3. Writes follow the task store rules in `lifeos/references/rules.md`. Store down: write an export file in the project folder and say so.
4. Tags and statuses: `search_context("log tags and statuses")`.

Next: `workos-report` at day end.

Scratchpad: end per `lifeos/references/scratchpad.md`.
