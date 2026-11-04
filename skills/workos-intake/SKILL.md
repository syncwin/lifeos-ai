---
name: workos-intake
description: "Absorbs outside requests for LifeOS WorkOS from managers, colleagues, clients or the owner's own ideas. Use for \"my manager sent this\", \"new request\", \"add this to the plan\", \"is this a duplicate\"."
license: MIT
metadata:
  displayName: "WorkOS Intake"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Intake
Needs: task store; EntityOS MCP for ownership rules.

1. Save the requester's text verbatim first. No paraphrase.
2. Read it back; flag truncated text and missing attachments.
3. Map each item to existing tasks: duplicate, frozen, or new. Ownership and frozen rules: `search_context("entity ownership rules")`.
4. Register new items; log one row.
5. Output the mapped list with the decisions the owner must make.

Next: `workos-sprint`.

Scratchpad: end per `lifeos/references/scratchpad.md`.
