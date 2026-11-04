---
name: deviceos-files
description: "Finds and organises files for LifeOS DeviceOS. Use when the user says \"find my file\", \"where is that file\", \"clean up this folder\", \"organise my downloads\", \"where do outputs go\", or \"move these files\". Searches first; moves need a risk check."
license: MIT
metadata:
  displayName: "DeviceOS Files"
  version: "0.2.0"
  author: "@wasimness"
  company: "SyncWin"
---

# DeviceOS Files
Needs: EntityOS MCP for folder rules.
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Where things belong: `search_context("file locations and rules")`.
2. Search first and report paths. Moves go to a holding folder from those rules, never straight to deletion.
3. Show the proposed move list inside a `references/risk-check.md` block; apply only on its exact reply, one batch per approval.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- Search results list real paths; nothing moved or deleted without a filled risk-check block and its exact reply.
- Every move went to the holding folder from the file rules, in one approved batch.

## Handoff
Delivered: Paths found, or an approved and applied move list with the holding-folder location.
Next: record the change -> `workos-log`.

Scratchpad: end per `references/scratchpad.md`.
