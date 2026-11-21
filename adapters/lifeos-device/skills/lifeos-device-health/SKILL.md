---
name: lifeos-device-health
description: "Reads PC and phone health for LifeOS Device. Use when the user asks \"is my PC healthy\", \"why is my PC slow\", \"how much disk space is left\", \"what needs updating\", \"check my phone battery\", or \"what is eating memory\". Read-only."
license: MIT
---

# Device Health
Needs: LifeOS MCP for the device list; a device reader (shell or MCP) for readings.
For device health, the core `lifeos` plugin is required: if its MCP tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

1. Devices and thresholds: `search_context("devices and policies")`.
2. Read only: disk, memory, pending updates, battery, uptime. Quote each reading with the command or tool that produced it; no reading means [UNKNOWN].
3. Report what is above or below threshold; propose fixes as tasks, do not apply them.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- Each reading (disk, memory, updates, battery, startup) is [DATA] with its source, or [UNKNOWN] with the reason.
- Nothing was changed; fixes are proposed tasks.

## Handoff
Delivered: A health summary with flagged items and proposed fixes.
Next: record the check -> `lifeos-work-log`; backup concern -> `lifeos-device-backup`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
