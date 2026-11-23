---
name: lifeos-work-writing
description: "Checks drafts against a numbered writing-patterns glossary for LifeOS Work. Use when the user says \"check this draft\", \"is this too promotional\", \"edit for voice\", \"review my copy\", or \"proof this text\". Runs a deterministic checker first. Writers and reviewers cite patterns by number."
license: MIT
---

# Work Writing Check
Needs: LifeOS MCP.
For work writing, the core `lifeos` plugin is required: if its MCP tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

1. Voice, language variant, banned terms: `search_context("voice")`. Missing: ask once.
2. Check against `${CLAUDE_PLUGIN_ROOT}/references/patterns.md`; cite findings by pattern number with line.
3. Run the checks in `${CLAUDE_PLUGIN_ROOT}/references/writing-check.md` on the draft (banned terms from step 1). They give PASS, WARN, FAIL or SKIP with line numbers for length, headings and banned phrases; include that output.
4. Do not rewrite unless asked; report first.
5. Per-business patterns live in LifeOS entity brand context, start empty and grow from reviewer pattern frequency; never pre-populate guessed patterns (`${CLAUDE_PLUGIN_ROOT}/references/patterns.md`, Maintaining the glossary).
6. Drafting and review rules (humanize checkpoints, three review passes, preservation contract, the two review files): `${CLAUDE_PLUGIN_ROOT}/references/writing-standards.md`.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- Findings cite pattern numbers with line numbers, and the checker output (PASS, WARN, FAIL, SKIP) is included.
- The draft was not rewritten unless asked.

## Handoff
Delivered: A findings list by pattern number and the checker output.
Next: final gate -> `lifeos-verify`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
