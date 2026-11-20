---
name: lifeos-deviceos-backup
description: "Checks whether backups ran and are healthy, for LifeOS DeviceOS. Use when the user asks \"is my PC backup healthy\", \"did the backup run\", \"is my data safe\", \"when was the last backup\", \"check my backups\", or \"test a restore\". Read-only; restores need a risk check."
license: MIT
---

# DeviceOS Backup
Needs: EntityOS MCP; access to backup logs or status.
For deviceos backup, the core `lifeos` plugin is required: if its MCP tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

1. Backup policy (what, where, how often): `search_context("devices and policies")`.
2. Compare the last successful run time and size with the policy. Stale or missing is a flag, with the evidence.
3. A restore test is a risky action: fill in `${CLAUDE_PLUGIN_ROOT}/references/risk-check.md`, restore to a new folder, never over live data or backups.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- Each backup is compared with the policy: last good run, size, and the evidence line [DATA], or [UNKNOWN] with the reason.
- No restore, delete or overwrite happened without a filled risk-check block and its exact reply.

## Handoff
Delivered: A per-backup status (ok, stale, missing) with evidence, plus any proposed restore test.
Next: record the check -> `lifeos-workos-log`; fix files or paths -> `lifeos-deviceos-files`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
