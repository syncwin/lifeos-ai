---
name: lifeos-selfos
description: "Starter skill for the SelfOS module, personal life. Use for \"add a task\", \"what is on my plate\", \"remind me to...\", \"my morning routine\", \"find my insurance document\". Routes to the selfos stages."
license: MIT
---

# LifeOS SelfOS
Needs: EntityOS MCP; module `selfos` enabled.
Start: run the `lifeos` router first if it has not run.

| Request | Stage |
|---|---|
| Add, list, change, close a personal task | `lifeos-selfos-tasks` |
| Time- or event-based reminder | `lifeos-selfos-reminders` |
| Recurring routine, habit, checklist | `lifeos-selfos-routines` |
| Find a personal document | search the task store, then `list_entities`; report the path, do not open or move it |

Personal preferences (timezone, quiet hours, routine times): `search_context("personal schedule preferences")`.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- The request went to exactly one stage (tasks, reminders or routines) or a document path was reported.
- No document was opened or moved.

## Handoff
Delivered: The chosen stage's result.
Next: tasks -> `lifeos-selfos-tasks`; reminders -> `lifeos-selfos-reminders`; routines -> `lifeos-selfos-routines`.

Scratchpad: end per `lifeos/references/scratchpad.md`.
