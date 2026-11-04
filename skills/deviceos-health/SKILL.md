---
name: deviceos-health
description: "Reads PC and phone health for LifeOS DeviceOS. Use for \"is my PC healthy\", \"disk space\", \"what needs updating\", \"why is it slow\". Starter skill; read-only."
license: MIT
metadata:
  displayName: "DeviceOS Health"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# DeviceOS Health
Needs: EntityOS MCP for the device list; a device reader (shell or MCP) for readings.

1. Devices and thresholds: `search_context("devices and policies")`.
2. Read only: disk, memory, pending updates, battery, uptime. Quote each reading with the command or tool that produced it; no reading means [UNKNOWN].
3. Report what is above or below threshold; propose fixes as tasks, do not apply them.

Next: `deviceos-backup` if backups look stale.

Scratchpad: end per `lifeos/references/scratchpad.md`.
