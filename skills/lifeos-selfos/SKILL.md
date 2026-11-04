---
name: lifeos-selfos
description: "Starter skill for the SelfOS module, personal life. Use for \"add a task\", \"what is on my plate\", \"remind me to...\", \"my morning routine\", \"find my insurance document\". Routes to the selfos stages."
license: MIT
metadata:
  displayName: "LifeOS SelfOS"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# LifeOS SelfOS
Needs: EntityOS MCP; module `selfos` enabled.

| Request | Stage |
|---|---|
| Add, list, change, close a personal task | `selfos-tasks` |
| Time- or event-based reminder | `selfos-reminders` |
| Recurring routine, habit, checklist | `selfos-routines` |
| Find a personal document | search the task store, then `list_entities`; report the path, do not open or move it |

Personal preferences (timezone, quiet hours, routine times): `search_context("personal schedule preferences")`.

Next: the chosen stage.

Scratchpad: end per `lifeos/references/scratchpad.md`.
