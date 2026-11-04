---
name: workos-log
description: "Audit trail of work for LifeOS WorkOS. Use when the user says \"log this\", \"log what I did today\", \"record what I did\", \"note the decision\", \"add to the question queue\", or after any chat that changed files or records."
license: MIT
metadata:
  displayName: "WorkOS Log"
  version: "0.2.0"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Log
Needs: task store (`references/tracker.md`); EntityOS MCP for tag vocabulary.
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Log as you go: one row per unit of work with what, evidence (path, link, command output), tag, status.
2. Decisions, questions and flags go to their own tables, not into free text.
3. Writes follow `references/rules.md` (Task store).
4. Tags and statuses: `search_context("log tags and statuses")`.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- Each row has what, evidence (path, link or command output), tag and status.
- Decisions, questions and flags are in their own tables.

## Handoff
Delivered: Logged rows with evidence; open questions queued.
Next: end of day -> `workos-report`.

Scratchpad: end per `references/scratchpad.md`.
