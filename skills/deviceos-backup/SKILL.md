---
name: deviceos-backup
description: "Checks backups for LifeOS DeviceOS. Use for \"did the backup run\", \"is my data safe\", \"when was the last backup\", \"test a restore\". Starter skill; read-only."
license: MIT
metadata:
  displayName: "DeviceOS Backup"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# DeviceOS Backup
Needs: EntityOS MCP; access to backup logs or status.

1. Backup policy (what, where, how often): `search_context("devices and policies")`.
2. Compare the last successful run time and size with the policy. Stale or missing is a flag, with the evidence.
3. Restore tests are proposed, never run without a yes; never delete or overwrite backups.

Next: `workos-log` to record the check.

Scratchpad: end per `lifeos/references/scratchpad.md`.
