---
name: selfos-reminders
description: "Creates and reviews personal reminders for LifeOS. Use for \"remind me to...\", \"nudge me on Friday\", \"what reminders do I have\", \"snooze that\". Starter skill."
license: MIT
metadata:
  displayName: "SelfOS Reminders"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# SelfOS Reminders
Needs: EntityOS MCP; a reminder channel (calendar or messaging connector) if one is connected.

1. Parse what, when, repeat. Resolve relative dates with `search_context("personal schedule preferences")` (timezone, quiet hours). Ambiguous time: ask once.
2. Creating a reminder is an outbound write: show what, when, where, wait for a yes (`lifeos/references/rules.md`, approvals).
3. No channel connected: store it as a dated task and say no alert will fire.
4. Snooze or cancel updates the row; never deletes it.

Next: `lifeos-selfos`.

Scratchpad: end per `lifeos/references/scratchpad.md`.
