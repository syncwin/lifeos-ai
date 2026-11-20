---
name: lifeos-selfos
description: "Starter skill for the SelfOS module, personal life. Use for \"add a task\", \"what is on my plate\", \"remind me to...\", \"my morning routine\", \"find my insurance document\". Routes to the selfos stages."
license: MIT
---

# LifeOS SelfOS
Needs: EntityOS MCP; module `selfos` enabled.
Needs the core `lifeos` plugin for the MCP connection and shared rules; if its tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

## Routing table

Read top to bottom; first matching row wins (phrases match as whole words, case-insensitive). Checked against `evals/router/cases.json`.

| Order | Trigger phrases | Skill | Then |
|---|---|---|---|
| 7 | remind me; set a reminder; snooze; cancel the reminder | `lifeos-selfos-reminders` | (none) |
| 8 | routine; wind-down; wind down | `lifeos-selfos-routines` | (none) |
| 9 | add a task; on my plate; to-do list; mark done; overdue | `lifeos-selfos-tasks` | (none) |
| 18 | selfos; insurance document; personal life | `lifeos-selfos` | (none) |

Default when no row matches: ask one closed question, "Is this (a) a personal task, (b) a reminder, (c) a routine, or (d) none of these?", and stop. Never answer the stage work yourself: load the stage with the Skill tool using the full slug `<plugin>:<skill>` (for example `lifeos-selfos:lifeos-selfos-tasks`); without the Skill tool, read its `SKILL.md` by relative path from the plugin root.

Finding a personal document: search the task store, then `list_entities`; report the path, never open or move it.

Personal preferences (timezone, quiet hours, routine times): `search_context("personal schedule preferences")`.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- The request went to exactly one stage (tasks, reminders or routines) or a document path was reported.
- No document was opened or moved.

## Handoff
Delivered: The chosen stage's result.
Next: tasks -> `lifeos-selfos-tasks`; reminders -> `lifeos-selfos-reminders`; routines -> `lifeos-selfos-routines`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
