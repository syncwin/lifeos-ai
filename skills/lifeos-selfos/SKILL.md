---
name: lifeos-selfos
description: "Starter skill for the SelfOS module, personal life. Use for \"add a task\", \"what is on my plate\", \"remind me to...\", \"my morning routine\", \"find my insurance document\". Routes to the selfos stages."
license: MIT
metadata:
  displayName: "LifeOS SelfOS"
  version: "0.2.4"
  author: "@wasimness"
  company: "SyncWin"
---

# LifeOS SelfOS
Needs: EntityOS MCP; module `selfos` enabled.
Start: run the `lifeos` router first if it hasn't run in this chat.

| Request | Stage |
|---|---|
| Add, list, change, close a personal task | `selfos-tasks` |
| Time- or event-based reminder | `selfos-reminders` |
| Recurring routine, habit, checklist | `selfos-routines` |
| Find a personal document | search the task store, then `list_entities`; report the path, do not open or move it |

Personal preferences (timezone, quiet hours, routine times): `search_context("personal schedule preferences")`.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- The request went to exactly one stage (tasks, reminders or routines) or a document path was reported.
- No document was opened or moved.

## Handoff
Delivered: The chosen stage's result.
Next: tasks -> `selfos-tasks`; reminders -> `selfos-reminders`; routines -> `selfos-routines`.

Scratchpad: end per `references/scratchpad.md`.
