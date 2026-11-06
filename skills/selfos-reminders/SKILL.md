---
name: selfos-reminders
description: "Time- and event-based reminders for LifeOS SelfOS. Use when the user says \"remind me to...\", \"remind me about\", \"set a reminder\", \"ping me when\", \"snooze that\", or \"cancel the reminder\". Resolves dates from the owner's schedule preferences; creating one needs a risk check."
license: MIT
metadata:
  displayName: "SelfOS Reminders"
  version: "0.2.4"
  author: "@wasimness"
  company: "SyncWin"
---

# SelfOS Reminders
Needs: EntityOS MCP; a reminder channel (calendar or messaging connector) if one is connected.
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Parse what, when, repeat. Resolve relative dates with `search_context("personal schedule preferences")` (timezone, quiet hours). Ambiguous time: ask once.
2. Creating a reminder is an outbound write: fill in `references/risk-check.md` (what, when, where) and wait for its exact reply.
3. No channel connected: store it as a dated task and say no alert will fire.
4. Snooze or cancel updates the row; never deletes it.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- What, when and repeat are stated with the resolved timezone; ambiguous times were asked once.
- A reminder was created only after a filled risk-check block and its exact reply; with no channel it is a dated task and the answer says no alert will fire.

## Handoff
Delivered: A created reminder, or a dated task with the no-alert note.
Next: the task behind it -> `selfos-tasks`; module menu -> `lifeos-selfos`.

Scratchpad: end per `references/scratchpad.md`.
