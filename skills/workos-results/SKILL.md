---
name: workos-results
description: "Results loop for LifeOS WorkOS, learning which work paid. Use when the user says \"did that change work\", \"check results\", \"28 day reading\", \"baseline before go-live\", \"did it pay off\", or \"how did that page perform\". Verdicts follow fixed time gates."
license: MIT
metadata:
  displayName: "WorkOS Results"
  version: "0.2.1"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Results
Needs: EntityOS MCP; task store; a metric source.
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Metric source, region filter, KPI definitions: `search_context("metric source, region filter, KPI definitions")`.
2. Baseline is captured before the change goes live. No baseline: the verdict is [UNKNOWN] and a task is added.
3. Gates: first reading at 28 days (verdict no better than "too early"), verdict allowed at 8 weeks, final at 12. Flat means failed and returns as a task.
4. Readings are taken only in this stage; every other stage reads stored verdicts.
5. Label each number [DATA]; unmeasurable items say why.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- A baseline exists for each change, or the verdict is [UNKNOWN] and a task was added.
- Verdicts respect the time gates (28 days too early at best, 8 weeks verdict, 12 weeks final); numbers are [DATA].

## Handoff
Delivered: Readings and verdicts per change; failed items returned as tasks.
Next: returned tasks -> `workos-sprint`.

Scratchpad: end per `references/scratchpad.md`.
