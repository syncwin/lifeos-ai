---
name: lifeos-feed
description: "Builds the LifeOS daily feed or an on-demand feed. Use when the user says \"show my feed\", \"show me my daily feed\", \"what should I look at today\", \"daily drop\", \"what is new for me\", \"/feed\", or gives thumbs up, tune or \"not for me\" feedback on a card. Ranks approved sources by stated priorities into a short list of actionable cards."
license: MIT
metadata:
  displayName: "LifeOS Feed"
  version: "0.2.4"
  author: "@wasimness"
  company: "SyncWin"
---

# LifeOS Feed
Needs: EntityOS MCP. Source connectors are optional; list which were unavailable.
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Read `search_context("priorities")`, `search_context("approved sources")`, `search_context("feed preferences and card limit")`. Missing: ask once.
2. Collect items only from approved sources. Get today's cards with `lifeos_get_feed`; it already skips dismissed and snoozed cards, so do not show those again.
3. Rank each card by score = urgency × importance × freshness. Urgency: overdue highest, then due today, then later; no due date is low but still ranked. Importance: from the stated priorities (tags, type, module). Freshness: newer beats older, never below a floor. Then lower cards similar (same module, tags or source) to ones the user gave a thumbs down or "not for me". Keep at or under the card limit (default 10) and mark the top 3 as the daily picks.
4. Each card: title, one-line why, source, label [DATA] or [OPINION], and its actions: done, snooze, open, dismiss (plus reply or file where they apply).
5. Actions and feedback are written with `lifeos_feed_act` (done, snooze, dismiss) and `lifeos_feed_feedback` (thumbs, tune, "not for me"); they apply on the next run. Never argue with feedback.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- At most the card limit (default 10) of cards, ranked by urgency × importance × freshness with the top 3 marked, each with title, why, source, [DATA] or [OPINION] label and its actions.
- Only approved sources were used; unavailable source connectors are listed.

## Handoff
Delivered: A ranked list of actionable cards; feedback stored for the next run.
Next: save a card -> `lifeos-knowledgeos`; personal task -> `lifeos-selfos`; work task -> `lifeos-workos`.

Scratchpad: end per `references/scratchpad.md`.
