---
name: lifeos
description: "Entry point and router for LifeOS, the personal operating system. Use for /lifeos and for any request about the user's own work, tasks, reminders, routines, devices, backups, money, saves, daily feed or facts about themselves, such as \"plan my week\", \"log what I did today\", \"remind me to renew my passport\", \"is my PC backup healthy\", \"what did I save about X\", \"show my feed\". Detects the module, checks it is enabled, then sends the work to the right skill. Not for generic coding, WordPress or questions that need no personal data."
license: MIT
metadata:
  displayName: "LifeOS"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# LifeOS (router)
Needs: EntityOS MCP connected (`search_context`, `get_entity`, `list_entities`). If it is not, stop and tell the user to set the EntityOS URL and token under plugin options.

## 1. Route
Classify the request, then load exactly one skill. Several modules means run them in the order listed, one at a time.

| Request is about | Skill |
|---|---|
| Daily or on-demand feed, cards, tune "not for me" | `lifeos-feed` |
| Facts about the owner, brands, people, sources | `lifeos-entityos` |
| Personal tasks, reminders, routines, documents | `lifeos-selfos` (stages: `selfos-tasks`, `selfos-reminders`, `selfos-routines`) |
| Work, clients, projects, content, follow-ups | `lifeos-workos` (stages: `workos-sprint`, `workos-log`, `workos-report`, `workos-results`, `workos-intake`, `workos-demand`, `workos-writing`) |
| PC and phone health, backups, files, automation | `lifeos-deviceos` (stages: `deviceos-health`, `deviceos-backup`, `deviceos-files`) |
| Expenses, receipts, bills, subscriptions, budgets | `lifeos-moneyos` |
| Saves, links, notes, search, learning | `lifeos-knowledgeos` |
| "Is this done / check this" on any deliverable | agent `lifeos-verifier` |

## 2. Gate
1. Module switch: ask the LifeOS module list when connected (a disabled module is declined and named, never deleted); otherwise ask once.
2. Stage prerequisites: `search_context("stage prerequisites, freshness limits")`. A stale upstream stage is listed as a proposed task, not run.
3. Diagnose the cause before auditing or fixing.
4. Never answer stage work yourself; load the stage skill.

Shared rules (owner facts, approvals, evidence labels, change control): `references/rules.md`. Task store spec: `references/tracker.md`.

Scratchpad: end per `references/scratchpad.md`. Next: the chosen skill, then `lifeos-verifier` before calling a deliverable done.
