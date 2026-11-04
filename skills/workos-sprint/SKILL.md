---
name: workos-sprint
description: "Weekly delivery plan for LifeOS WorkOS. Use when the user says \"plan my week\", \"plan this week\", \"sprint plan\", \"what can I deliver by Friday\", \"what should I work on this week\", or \"re-plan after the new request\". One plan per week; a second plan is a defect."
license: MIT
metadata:
  displayName: "WorkOS Sprint"
  version: "0.2.0"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Sprint
Needs: EntityOS MCP; task store.
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Ask priorities first. Read `search_context("priorities")`, `search_context("working hours, capacity, owners per task type")`.
2. Gather open tasks from every list, blocked items, the question queue.
3. Write one sprint row and plan items sized by outcome, not hours. Two tasks in progress at most. Estimates that carry over stay visibly marked.
4. Stale upstream stages (intake, results) appear as proposed tasks, not as run work.
5. List exclusions with the reason.
6. Show the plan; save after a yes.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- One sprint row with plan items sized by outcome; at most two in progress; exclusions listed with reasons.
- The plan was shown and saved only after a yes; stale upstream stages appear as proposed tasks.

## Handoff
Delivered: The weekly plan.
Next: log work as it happens -> `workos-log`; new requests first -> `workos-intake`.

Scratchpad: end per `references/scratchpad.md`.
