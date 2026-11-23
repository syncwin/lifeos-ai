---
name: lifeos-work-brief
description: "Builds the content brief or outline for one piece, for LifeOS Work. Use when the user says \"content brief\", \"build a brief\", \"content outline\", \"outline this article\", or \"structure this page\". Needs research first; hands a checked brief to drafting."
license: MIT
---

# Work Brief
Needs: LifeOS MCP; a fact table from `lifeos-work-research`.
For work brief, the core `lifeos` plugin is required: if its MCP tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

1. Source. A research file exists: build from it. Only a topic or notes: do not outline, go to `lifeos-work-research` first. An approved brief needs changes: edit it in place and state the change in one line on top.
2. Business inputs from LifeOS entity data, citing claim IDs: `search_context("voice")`, `search_context("conversion definition")`, `search_context("keyword map")`. A missing input is [UNKNOWN]; ask once.
3. Pick the page type (article, comparison, service page, legal page, FAQ, landing page). It sets the shape: a legal page follows the required clauses as stored, a service page leads with the conversion action, an article leads with the reader's question, a comparison leads with the options table.
4. Outline with a label on every heading (`H1:` to `H4:`, levels in order) and one line of purpose per section. FAQ only where real, distinct questions exist.
5. Tier the keywords: protect terms in title and opening, near-ranking terms in a heading and the answer block, gaps get their own section, question terms become a short direct answer. Never target a term mapped to another item or excluded.
6. Add: an answer block draft, a named schema type, two to four internal-link anchors drawn from target topics, a meta title and description within the stored limits. Method detail: `${CLAUDE_PLUGIN_ROOT}/references/core-rules.md`, Briefs and on-page SEO.
7. Run the brief completeness gate (point of view, keyword block, link targets, word-count range) before handing over.
8. Saving over an existing brief file needs a filled `${CLAUDE_PLUGIN_ROOT}/references/risk-check.md` block.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- Page type, reader, answer block, labelled outline, keyword tiers, schema type, link targets and meta are present.
- The completeness gate passed; business inputs cite claim IDs or say [UNKNOWN]; no outline was built without research.

## Handoff
Delivered: A labelled brief that now outranks drafting defaults for this piece.
Next: write it -> `lifeos-work-draft`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
