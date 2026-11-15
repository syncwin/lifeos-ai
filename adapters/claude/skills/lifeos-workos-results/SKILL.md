---
name: lifeos-workos-results
description: "Results loop for LifeOS WorkOS, learning which work paid. Use when the user says \"did that change work\", \"check results\", \"28 day reading\", \"baseline before go-live\", \"did it pay off\", or \"how did that page perform\". Verdicts follow fixed time gates."
license: MIT
---

# WorkOS Results
Needs: EntityOS MCP; task store; a metric source.
Start: run the `lifeos` router first if it has not run.

1. Metric source, region filter, KPI definitions: `search_context("metric source, region filter, KPI definitions")`.
2. Baseline is captured before the change goes live. No baseline: the verdict is [UNKNOWN] and a task is added.
3. Gates: first reading at 28 days (verdict no better than "too early"), verdict allowed at 8 weeks, final at 12. Flat means failed and returns as a task.
4. Readings are taken only in this stage; every other stage reads stored verdicts.
5. Label each number [DATA]; unmeasurable items say why.
6. A number moved or fell: diagnose it with `references/decline-diagnosis-method.md` (segment first, separate events); verdict table and AI-visibility panel: `lifeos-workos-demand/references/scoring-and-verdict-framework.md`.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- A baseline exists for each change, or the verdict is [UNKNOWN] and a task was added.
- Verdicts respect the time gates (28 days too early at best, 8 weeks verdict, 12 weeks final); numbers are [DATA].

## Handoff
Delivered: Readings and verdicts per change; failed items returned as tasks.
Next: returned tasks -> `lifeos-workos-sprint`.

Scratchpad: end per `lifeos/references/scratchpad.md`.
