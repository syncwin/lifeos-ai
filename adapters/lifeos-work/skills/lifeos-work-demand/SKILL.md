---
name: lifeos-work-demand
description: "Conversational-demand test for LifeOS Work content planning. Use for \"should this be a page\", \"plan content for these queries\", \"cluster these keywords\", \"multi-constraint searches\"."
license: MIT
---

# Work Demand Test
Needs: LifeOS MCP.
For work demand, the core `lifeos` plugin is required: if its MCP tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

1. Markets and audiences: `search_context("markets, audiences")`.
2. Scoring, exclusion gate, clustering, keyword mapping: `${CLAUDE_PLUGIN_ROOT}/references/scoring-and-verdict-framework.md`. Cluster model, the five page treatments, one ranked queue and the handoff to the content pipeline: `${CLAUDE_PLUGIN_ROOT}/references/cluster-and-treatment-model.md`.
3. Rule: a query cluster becomes a page only if one asset can answer several of its queries together. Otherwise it stays a keyword list.
4. Per cluster output: queries, the single asset that would answer them, PASS or FAIL, one line why.
5. Passing clusters get a brief: intent, entities, sources, questions to answer. Briefs and on-page SEO go to `content-structure-strategy` and `content-seo-strategy` with brand context from LifeOS entity data (`${CLAUDE_PLUGIN_ROOT}/references/core-rules.md`). Review it against the checklist before any drafting.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- Each cluster lists its queries, the single asset that answers them, PASS or FAIL and one line why.
- Passing clusters have a brief reviewed against the checklist before any drafting.

## Handoff
Delivered: Cluster verdicts and briefs for passing clusters.
Next: schedule briefs -> `lifeos-work-sprint`; check the draft later -> `lifeos-work-writing`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
