---
name: lifeos-deviceos-files
description: "Finds and organises files for LifeOS DeviceOS. Use when the user says \"find my file\", \"where is that file\", \"clean up this folder\", \"organise my downloads\", \"where do outputs go\", or \"move these files\". Searches first; moves need a risk check."
license: MIT
---

# DeviceOS Files
Needs: EntityOS MCP for folder rules.
Start: run the `lifeos` router first if it has not run.

1. Where things belong: `search_context("file locations and rules")`.
2. Search first and report paths. Moves go to a holding folder from those rules, never straight to deletion.
3. Project file organizing (quick check versus full audit, one decision per file, never rename a tracker, file registry): `lifeos/references/core-rules.md`, File organizing.
4. Show the proposed move list inside a `lifeos/references/risk-check.md` block; apply only on its exact reply, one batch per approval.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- Search results list real paths; nothing moved or deleted without a filled risk-check block and its exact reply.
- Every move went to the holding folder from the file rules, in one approved batch.

## Handoff
Delivered: Paths found, or an approved and applied move list with the holding-folder location.
Next: record the change -> `lifeos-workos-log`.

Scratchpad: end per `lifeos/references/scratchpad.md`.
