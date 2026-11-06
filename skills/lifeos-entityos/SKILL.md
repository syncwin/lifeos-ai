---
name: lifeos-entityos
description: "Answers and maintains facts about the owner, brands, people and sources through EntityOS. Use when the user asks \"what do I know about X\", \"who is X\", \"which brands do I run\", \"remember that...\", \"is this fact still true\", \"where does this value belong\", or when another LifeOS skill finds an owner fact missing."
license: MIT
metadata:
  displayName: "LifeOS EntityOS"
  version: "0.2.4"
  author: "@wasimness"
  company: "SyncWin"
---

# LifeOS EntityOS
Needs: EntityOS MCP.
Start: run the `lifeos` router first if it hasn't run in this chat.

0. EntityOS missing or its cheapest call fails twice: `references/entityos-offline.md`.
1. Look up: `search_context(query)` first, then `get_entity(id)` or `list_entities(type)` for detail. Quote the source of each claim.
2. Not found: say so, ask once, and offer to store the answer through EntityOS if a write tool is connected (`references/risk-check.md`; the write hook also asks); otherwise note it in the task log as an open question.
3. Conflicting claims: show both with sources and dates; the owner decides. Never merge silently.
4. Facts come only from what EntityOS returned this run (`references/rules.md`, Owner facts).

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- Every claim quotes its EntityOS source from this run; not-found items are asked once and marked [UNKNOWN].
- Conflicting claims were shown side by side with sources and dates, never merged.

## Handoff
Delivered: The answer with sources, or the stored fact the owner confirmed.
Next: the skill that needed the fact -> the calling skill.

Scratchpad: end per `references/scratchpad.md`.
