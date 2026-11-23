---
name: lifeos-work-sprint
description: "Weekly delivery plan for LifeOS Work. Use when the user says \"plan my week\", \"plan this week\", \"sprint plan\", \"what can I deliver by Friday\", \"what should I work on this week\", or \"re-plan after the new request\". One plan per week; a second plan is a defect."
license: MIT
---

# Work Sprint
Needs: LifeOS MCP; task store.
For work sprint, the core `lifeos` plugin is required: if its MCP tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

1. Ask priorities first. Read `search_context("priorities")`, `search_context("working hours, capacity, owners per task type")`.
2. Gather open tasks from every list, blocked items, the question queue. Method for sizing, sequencing, executing a task, the content boundary and day reports: `${CLAUDE_PLUGIN_ROOT}/references/execution-and-reporting.md`; tracker structure: `${CLAUDE_PLUGIN_ROOT}/references/workbook-and-tracker-spec.md`. Shared rules: `${CLAUDE_PLUGIN_ROOT}/references/core-rules.md`.
3. Write one sprint row and plan items sized by outcome, not hours. Two tasks in progress at most. Estimates that carry over stay visibly marked.
4. A task that is a code or build change done by an agent is sized and run as a written task with named checks, a pull request and a person's review: `${CLAUDE_PLUGIN_ROOT}/references/factory-workflow.md`.
5. Stale upstream stages (intake, results) appear as proposed tasks, not as run work.
6. List exclusions with the reason.
7. Show the plan; save after a yes.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- One sprint row with plan items sized by outcome; at most two in progress; exclusions listed with reasons.
- The plan was shown and saved only after a yes; stale upstream stages appear as proposed tasks.

## Handoff
Delivered: The weekly plan.
Next: log work as it happens -> `lifeos-work-log`; new requests first -> `lifeos-work-intake`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
