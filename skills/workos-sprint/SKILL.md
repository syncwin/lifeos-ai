---
name: workos-sprint
description: "Weekly delivery plan for LifeOS WorkOS. Use for \"plan this week\", \"sprint plan\", \"what can I deliver by Friday\", \"re-plan after the new request\". One plan per week; a second plan is a defect."
license: MIT
metadata:
  displayName: "WorkOS Sprint"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Sprint
Needs: EntityOS MCP; task store.

1. Ask priorities first. Read `search_context("priorities")`, `search_context("working hours, capacity, owners per task type")`.
2. Gather open tasks from every list, blocked items, the question queue.
3. Write one sprint row and plan items sized by outcome, not hours. Two tasks in progress at most. Estimates that carry over stay visibly marked.
4. Stale upstream stages (intake, results) appear as proposed tasks, not as run work.
5. List exclusions with the reason.
6. Show the plan; save after a yes.

Next: `workos-log` as work happens.

Scratchpad: end per `lifeos/references/scratchpad.md`.
