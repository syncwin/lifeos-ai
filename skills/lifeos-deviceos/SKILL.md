---
name: lifeos-deviceos
description: "Starter and router for the DeviceOS module, PC and phone health, backups, files and automation. Use for \"is my PC healthy\", \"did the backup run\", \"where is that file\", \"what is eating disk space\", \"set up an automation\". Routes to the deviceos stages."
license: MIT
metadata:
  displayName: "LifeOS DeviceOS"
  version: "0.2.1"
  author: "@wasimness"
  company: "SyncWin"
---

# LifeOS DeviceOS
Needs: EntityOS MCP; module `deviceos` enabled.
Start: run the `lifeos` router first if it hasn't run in this chat.

| Request | Stage |
|---|---|
| Disk, memory, updates, battery, startup | `deviceos-health` |
| Backup status, schedule, restore check | `deviceos-backup` |
| Find, organise, move files | `deviceos-files` |
| New scheduled task or automation | show the plan in a `references/risk-check.md` block; run nothing hidden |

Device inventory and policies: `search_context("devices and policies")`. Read-only first; any change goes through `references/risk-check.md`.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- The request went to exactly one stage (health, backup or files), or a plan was shown through a risk-check block.
- No automation was created or run without the exact reply.

## Handoff
Delivered: The chosen stage's result.
Next: health -> `deviceos-health`; backups -> `deviceos-backup`; files -> `deviceos-files`; record -> `workos-log`.

Scratchpad: end per `references/scratchpad.md`.
