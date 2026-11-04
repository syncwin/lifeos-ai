---
name: workos-writing
description: "Checks drafts against a numbered writing-patterns glossary for LifeOS WorkOS. Use for \"check this draft\", \"is this too promotional\", \"edit for voice\", \"review my copy\". Writers and reviewers cite patterns by number."
license: MIT
metadata:
  displayName: "WorkOS Writing Check"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# WorkOS Writing Check
Needs: EntityOS MCP.

1. Voice, language variant, banned terms: `search_context("voice")`. Missing: ask once.
2. Check against `references/patterns.md`; cite findings by pattern number with line.
3. Mechanical rules (structure, headings, FAQ block) print PASS, WARN, FAIL or SKIP with line numbers.
4. Do not rewrite unless asked; report first.

Next: `lifeos-verifier` for the final gate.

Scratchpad: end per `lifeos/references/scratchpad.md`.
