---
name: lifeos-workos-draft
description: "Drafts the body of an article or page from an approved brief, for LifeOS WorkOS. Use when the user says \"draft this article\", \"draft this page\", \"write the draft\", \"draft from this brief\", or \"write the body\". Voice and facts come from EntityOS and the fact table."
license: MIT
---

# WorkOS Draft
Needs: EntityOS MCP; a brief and its fact table.
For workos draft, the core `lifeos` plugin is required: if its MCP tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

1. Priority: brief, then this skill, then defaults. Follow the brief's sections and order; a conflict is raised, not settled silently. A draft with no brief: its own headings count as the brief, keep substance, cut only true repetition, and propose (never insert) missing parts.
2. Load the voice first, never a generic one: `search_context("voice")`, `search_context("audience")`, `search_context("conversion definition")`. Hold one point of view from start to finish. Missing voice: ask once.
3. Every factual claim traces to a fact-table row. No row: mark it unverified in the hand-off note, do not state it as fact. A claim attributed to a named source must exist in that source.
4. Required legal or regulatory wording is copied exactly from the stored claim (`search_context("required clauses, disclaimers")`) and cited by claim ID. Missing: [UNKNOWN], ask.
5. Never invent an owner or business fact (names, addresses, offers, contact routes); read it from EntityOS or leave it [UNKNOWN].
6. Plain language, short paragraphs, terms spelled out on first use, labelled headings written as real headings, closing action matching the stored conversion definition. Mechanics: `${CLAUDE_PLUGIN_ROOT}/references/writing-standards.md`.
7. Per section: draft, check it, run the humanize pass (`humanizeai`, or the fallback in the standards), fix, move on. Then one full-document pass.
8. Saving the draft over an existing file needs a filled `${CLAUDE_PLUGIN_ROOT}/references/risk-check.md` block. Never publish.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- The draft matches the brief's structure; the note lists unsourced claims and any deviation with its reason.
- Voice, required wording and entity facts cite EntityOS claim IDs or say [UNKNOWN]; nothing was invented or published.

## Handoff
Delivered: A full draft plus a short note of unverified claims and deviations.
Next: gate it -> `lifeos-workos-review`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
