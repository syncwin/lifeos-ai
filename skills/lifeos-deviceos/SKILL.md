---
name: lifeos-deviceos
description: "Starter and router for the DeviceOS module, PC and phone health, backups, files and automation. Use for \"is my PC healthy\", \"did the backup run\", \"where is that file\", \"what is eating disk space\", \"set up an automation\". Routes to the deviceos stages."
license: MIT
metadata:
  displayName: "LifeOS DeviceOS"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# LifeOS DeviceOS
Needs: EntityOS MCP; module `deviceos` enabled.

| Request | Stage |
|---|---|
| Disk, memory, updates, battery, startup | `deviceos-health` |
| Backup status, schedule, restore check | `deviceos-backup` |
| Find, organise, move files | `deviceos-files` |
| New scheduled task or automation | write the plan, show it, wait for a yes; run nothing hidden |

Device inventory and policies: `search_context("devices and policies")`. Read-only first; any change is shown and approved per action.

Next: the chosen stage.

Scratchpad: end per `lifeos/references/scratchpad.md`.
