---
name: lifeos-device
description: "Starter and router for the device module, PC and phone health, backups, files and automation. Use for \"is my PC healthy\", \"did the backup run\", \"where is that file\", \"what is eating disk space\", \"set up an automation\". Routes to the device stages."
license: MIT
---

# LifeOS Device
Needs: LifeOS MCP; module `device` enabled.
Needs the core `lifeos` plugin for the MCP connection and shared rules; if its tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

## Routing table

Read top to bottom; first matching row wins (phrases match as whole words, case-insensitive). Checked against `evals/router/cases.json`.

| Order | Trigger phrases | Skill | Then |
|---|---|---|---|
| 10 | backup; backups; test a restore | `lifeos-device-backup` | (none) |
| 11 | find my file; where is that file; clean up this folder; organise my downloads; move these files; where do outputs go; organize the project files; organise the project files; project files are outdated | `lifeos-device-files` | (none) |
| 12 | pc healthy; why is my pc slow; disk space; phone battery; eating memory; needs updating | `lifeos-device-health` | (none) |
| 13 | set up an automation; automation; device module | `lifeos-device` | (none) |

Default when no row matches: ask one closed question, "Is this (a) device health, (b) backups, (c) files, or (d) none of these?", and stop. Never answer the stage work yourself: load the stage with the Skill tool using the full slug `<plugin>:<skill>` (for example `lifeos-device:lifeos-device-backup`); without the Skill tool, read its `SKILL.md` by relative path from the plugin root.

A new scheduled task or automation: show the plan in a `${CLAUDE_PLUGIN_ROOT}/references/risk-check.md` block and run nothing hidden.

Device inventory and policies: `search_context("devices and policies")`. Read-only first; any change goes through `${CLAUDE_PLUGIN_ROOT}/references/risk-check.md`.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- The request went to exactly one stage (health, backup or files), or a plan was shown through a risk-check block.
- No automation was created or run without the exact reply.

## Handoff
Delivered: The chosen stage's result.
Next: health -> `lifeos-device-health`; backups -> `lifeos-device-backup`; files -> `lifeos-device-files`; record -> `lifeos-work-log`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
