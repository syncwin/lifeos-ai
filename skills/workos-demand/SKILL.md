---
name: workos-demand
description: "Conversational-demand test for LifeOS WorkOS content planning. Use for \"should this be a page\", \"plan content for these queries\", \"cluster these keywords\", \"multi-constraint searches\"."
license: MIT
metadata:
  displayName: "WorkOS Demand Test"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Demand Test
Needs: EntityOS MCP.

1. Markets and audiences: `search_context("markets, audiences")`.
2. Rule: a query cluster becomes a page only if one asset can answer several of its queries together. Otherwise it stays a keyword list.
3. Per cluster output: queries, the single asset that would answer them, PASS or FAIL, one line why.
4. Passing clusters get a brief: intent, entities, sources, questions to answer. Review it against the checklist before any drafting.

Next: `workos-sprint` to schedule briefs.

Scratchpad: end per `lifeos/references/scratchpad.md`.
