---
name: workos-results
description: "Results loop for LifeOS WorkOS, learning which work paid. Use for \"did that change work\", \"check results\", \"28 day reading\", \"baseline before go-live\". Verdicts follow fixed time gates."
license: MIT
metadata:
  displayName: "WorkOS Results"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Results
Needs: EntityOS MCP; task store; a metric source.

1. Metric source, region filter, KPI definitions: `search_context("metric source, region filter, KPI definitions")`.
2. Baseline is captured before the change goes live. No baseline: the verdict is [UNKNOWN] and a task is added.
3. Gates: first reading at 28 days (verdict no better than "too early"), verdict allowed at 8 weeks, final at 12. Flat means failed and returns as a task.
4. Readings are taken only in this stage; every other stage reads stored verdicts.
5. Label each number [DATA]; unmeasurable items say why.

Next: `workos-sprint` for returned tasks.

Scratchpad: end per `lifeos/references/scratchpad.md`.
