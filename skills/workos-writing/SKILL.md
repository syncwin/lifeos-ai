---
name: workos-writing
description: "Checks drafts against a numbered writing-patterns glossary for LifeOS WorkOS. Use when the user says \"check this draft\", \"is this too promotional\", \"edit for voice\", \"review my copy\", or \"proof this text\". Runs a deterministic checker first. Writers and reviewers cite patterns by number."
license: MIT
metadata:
  displayName: "WorkOS Writing Check"
  version: "0.2.0"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Writing Check
Needs: EntityOS MCP.
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Voice, language variant, banned terms: `search_context("voice")`. Missing: ask once.
2. Check against `references/patterns.md`; cite findings by pattern number with line.
3. Run the checker on the draft file: `python -I -X utf8 ${CLAUDE_SKILL_DIR}/scripts/check_draft.py <draft> [--ban "term,term"]` (banned terms from step 1). It prints PASS, WARN, FAIL or SKIP with line numbers for length, headings and banned phrases; include its output.
4. Do not rewrite unless asked; report first.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- Findings cite pattern numbers with line numbers, and the checker output (PASS, WARN, FAIL, SKIP) is included.
- The draft was not rewritten unless asked.

## Handoff
Delivered: A findings list by pattern number and the checker output.
Next: final gate -> `lifeos-verifier`.

Scratchpad: end per `references/scratchpad.md`.
