---
name: workos-intake
description: "Absorbs outside requests for LifeOS WorkOS from managers, colleagues, clients or the owner's own ideas. Use when the user says \"my manager sent this\", \"a manager sent me a new request\", \"new request\", \"add this to my plan\", \"is this a duplicate\", or pastes a request to triage."
license: MIT
metadata:
  displayName: "WorkOS Intake"
  version: "0.2.0"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Intake
Needs: task store; EntityOS MCP for ownership rules.
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Save the requester's text verbatim first. No paraphrase.
2. Read it back; flag truncated text and missing attachments.
3. Map each item to existing tasks: duplicate, frozen, or new. Ownership and frozen rules: `search_context("entity ownership rules")`.
4. Register new items; log one row.
5. Output the mapped list with the decisions the owner must make. A reply or status sent back to the requester is outbound: `references/risk-check.md`.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- The requester's text is saved verbatim; truncation and missing attachments are flagged.
- Each item is mapped (duplicate, frozen or new) and the owner's decisions are listed; any reply to the requester went through a filled risk-check block.

## Handoff
Delivered: A mapped list of requests with the decisions the owner must make.
Next: plan it -> `workos-sprint`; record it -> `workos-log`.

Scratchpad: end per `references/scratchpad.md`.
