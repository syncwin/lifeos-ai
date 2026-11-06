---
name: deviceos-health
description: "Reads PC and phone health for LifeOS DeviceOS. Use when the user asks \"is my PC healthy\", \"why is my PC slow\", \"how much disk space is left\", \"what needs updating\", \"check my phone battery\", or \"what is eating memory\". Read-only."
license: MIT
metadata:
  displayName: "DeviceOS Health"
  version: "0.2.4"
  author: "@wasimness"
  company: "SyncWin"
---

# DeviceOS Health
Needs: EntityOS MCP for the device list; a device reader (shell or MCP) for readings.
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Devices and thresholds: `search_context("devices and policies")`.
2. Read only: disk, memory, pending updates, battery, uptime. Quote each reading with the command or tool that produced it; no reading means [UNKNOWN].
3. Report what is above or below threshold; propose fixes as tasks, do not apply them.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- Each reading (disk, memory, updates, battery, startup) is [DATA] with its source, or [UNKNOWN] with the reason.
- Nothing was changed; fixes are proposed tasks.

## Handoff
Delivered: A health summary with flagged items and proposed fixes.
Next: record the check -> `workos-log`; backup concern -> `deviceos-backup`.

Scratchpad: end per `references/scratchpad.md`.
