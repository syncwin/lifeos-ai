---
name: workos-demand
description: "Conversational-demand test for LifeOS WorkOS content planning. Use for \"should this be a page\", \"plan content for these queries\", \"cluster these keywords\", \"multi-constraint searches\"."
license: MIT
metadata:
  displayName: "WorkOS Demand Test"
  version: "0.2.1"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Demand Test
Needs: EntityOS MCP.
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Markets and audiences: `search_context("markets, audiences")`.
2. Rule: a query cluster becomes a page only if one asset can answer several of its queries together. Otherwise it stays a keyword list.
3. Per cluster output: queries, the single asset that would answer them, PASS or FAIL, one line why.
4. Passing clusters get a brief: intent, entities, sources, questions to answer. Review it against the checklist before any drafting.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- Each cluster lists its queries, the single asset that answers them, PASS or FAIL and one line why.
- Passing clusters have a brief reviewed against the checklist before any drafting.

## Handoff
Delivered: Cluster verdicts and briefs for passing clusters.
Next: schedule briefs -> `workos-sprint`; check the draft later -> `workos-writing`.

Scratchpad: end per `references/scratchpad.md`.
