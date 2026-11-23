---
name: lifeos-workos-intake
description: "Absorbs outside requests for LifeOS WorkOS from managers, colleagues, clients or the owner's own ideas. Use when the user says \"my manager sent this\", \"a manager sent me a new request\", \"new request\", \"add this to my plan\", \"is this a duplicate\", or pastes a request to triage."
license: MIT
---

# WorkOS Intake
Needs: task store; EntityOS MCP for ownership rules.
For workos intake, the core `lifeos` plugin is required: if its MCP tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

1. Save the requester's text verbatim first. No paraphrase.
2. Read it back; flag truncated text and missing attachments.
3. Map each item to existing tasks: duplicate, frozen, or new. Ownership and frozen rules: `search_context("entity ownership rules")`.
4. Register new items; log one row. A new item that is a code or build change for an agent gets a problem and acceptance criteria before it is planned: `${CLAUDE_PLUGIN_ROOT}/references/factory-workflow.md`.
5. Output the mapped list with the decisions the owner must make. A reply or status sent back to the requester is outbound: `${CLAUDE_PLUGIN_ROOT}/references/risk-check.md`.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- The requester's text is saved verbatim; truncation and missing attachments are flagged.
- Each item is mapped (duplicate, frozen or new) and the owner's decisions are listed; any reply to the requester went through a filled risk-check block.

## Handoff
Delivered: A mapped list of requests with the decisions the owner must make.
Next: plan it -> `lifeos-workos-sprint`; record it -> `lifeos-workos-log`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
