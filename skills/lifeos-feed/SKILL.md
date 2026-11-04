---
name: lifeos-feed
description: "Builds the LifeOS daily feed or an on-demand feed. Use for \"show my feed\", \"what should I look at today\", \"daily drop\", \"/feed\", or thumbs up, tune and \"not for me\" feedback on a card. Pulls sources the owner approved, ranks by stated priorities, returns a short list of actionable cards."
license: MIT
metadata:
  displayName: "LifeOS Feed"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# LifeOS Feed
Needs: EntityOS MCP. Source connectors are optional; list which were unavailable.

1. Read `search_context("priorities")`, `search_context("approved sources")`, `search_context("feed preferences and card limit")`. Missing: ask once.
2. Collect items only from approved sources. Dedupe against cards already shown (task store).
3. Rank by priority match, freshness, actionability. Keep at or under the card limit (default 10).
4. Each card: title, one-line why, source, label [DATA] or [OPINION], one action (open, save, do, snooze).
5. Feedback (thumbs, tune, "not for me") is stored through the task store and applied next run; never argue with it.

Next: `lifeos-knowledgeos` for a save, `lifeos-selfos` or `lifeos-workos` for a task.

Scratchpad: end per `lifeos/references/scratchpad.md`.
