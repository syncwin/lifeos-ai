---
name: lifeos-entityos
description: "Answers and maintains facts about the owner, brands, people and sources through EntityOS. Use for \"what do I know about X\", \"who is X\", \"which brands do I run\", \"remember that...\", \"is this fact still true\", or when another LifeOS skill finds an owner fact missing."
license: MIT
metadata:
  displayName: "LifeOS EntityOS"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# LifeOS EntityOS
Needs: EntityOS MCP.

1. Look up: `search_context(query)` first, then `get_entity(id)` or `list_entities(type)` for detail. Quote the source of each claim.
2. Not found: say so, ask once, and offer to store the answer through EntityOS if a write tool is connected; otherwise note it in the task log as an open question.
3. Conflicting claims: show both with sources and dates; the owner decides. Never merge silently.
4. Never output facts from memory of earlier chats; only what EntityOS returned this run.

Next: the skill that needed the fact.

Scratchpad: end per `lifeos/references/scratchpad.md`.
