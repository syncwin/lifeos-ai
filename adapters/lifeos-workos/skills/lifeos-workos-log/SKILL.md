---
name: lifeos-workos-log
description: "Audit trail of work for LifeOS WorkOS. Use when the user says \"log this\", \"log what I did today\", \"record what I did\", \"note the decision\", \"add to the question queue\", or after any chat that changed files or records."
license: MIT
---

# WorkOS Log
Needs: task store (`${CLAUDE_PLUGIN_ROOT}/references/tracker.md`); EntityOS MCP for tag vocabulary.
For workos log, the core `lifeos` plugin is required: if its MCP tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.
Method (log line format, sprint log versus tracker, baselines, question queue): `${CLAUDE_PLUGIN_ROOT}/references/execution-and-reporting.md`, `${CLAUDE_PLUGIN_ROOT}/references/core-rules.md`.

1. Log as you go: one row per unit of work with what, evidence (path, link, command output), tag, status.
2. Decisions, questions and flags go to their own tables, not into free text.
3. Writes follow `${CLAUDE_PLUGIN_ROOT}/references/rules.md` (Task store).
4. Tags and statuses: `search_context("log tags and statuses")`.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- Each row has what, evidence (path, link or command output), tag and status.
- Decisions, questions and flags are in their own tables.

## Handoff
Delivered: Logged rows with evidence; open questions queued.
Next: end of day -> `lifeos-workos-report`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
