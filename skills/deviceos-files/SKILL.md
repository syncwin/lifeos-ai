---
name: deviceos-files
description: "File search and organisation for LifeOS DeviceOS. Use for \"find my file\", \"clean up this folder\", \"where do outputs go\", \"organise downloads\". Starter skill."
license: MIT
metadata:
  displayName: "DeviceOS Files"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# DeviceOS Files
Needs: EntityOS MCP for folder rules.

1. Where things belong: `search_context("file locations and rules")`.
2. Search first and report paths. Moves go to a holding folder from those rules, never straight to deletion.
3. Show the proposed move list; apply only after a yes, one batch per approval.

Next: `workos-log` to record the change.

Scratchpad: end per `lifeos/references/scratchpad.md`.
