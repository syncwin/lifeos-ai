---
name: lifeos-deviceos
description: "Starter and router for the DeviceOS module, PC and phone health, backups, files and automation. Use for \"is my PC healthy\", \"did the backup run\", \"where is that file\", \"what is eating disk space\", \"set up an automation\". Routes to the deviceos stages."
license: MIT
---

# LifeOS DeviceOS
Needs: EntityOS MCP; module `deviceos` enabled.
Start: run the `lifeos` router first if it has not run.

| Request | Stage |
|---|---|
| Disk, memory, updates, battery, startup | `lifeos-deviceos-health` |
| Backup status, schedule, restore check | `lifeos-deviceos-backup` |
| Find, organise, move files | `lifeos-deviceos-files` |
| New scheduled task or automation | show the plan in a `lifeos/references/risk-check.md` block; run nothing hidden |

Device inventory and policies: `search_context("devices and policies")`. Read-only first; any change goes through `lifeos/references/risk-check.md`.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- The request went to exactly one stage (health, backup or files), or a plan was shown through a risk-check block.
- No automation was created or run without the exact reply.

## Handoff
Delivered: The chosen stage's result.
Next: health -> `lifeos-deviceos-health`; backups -> `lifeos-deviceos-backup`; files -> `lifeos-deviceos-files`; record -> `lifeos-workos-log`.

Scratchpad: end per `lifeos/references/scratchpad.md`.
