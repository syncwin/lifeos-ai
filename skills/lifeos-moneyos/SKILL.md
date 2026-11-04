---
name: lifeos-moneyos
description: "Starter skill for the MoneyOS module, money records. Use for \"log this expense\", \"scan this receipt\", \"what bills are due\", \"my subscriptions\", \"am I on budget\". Records and reports only; it never moves money."
license: MIT
metadata:
  displayName: "LifeOS MoneyOS"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# LifeOS MoneyOS
Needs: EntityOS MCP; module `moneyos` enabled (off by default).

1. Categories, currency, budgets: `search_context("money categories, currency, budgets")`.
2. Receipt to expense: extract date, merchant, amount, category; show it and wait for a yes before saving. Unreadable fields are [UNKNOWN], not guessed.
3. Reports: totals by category and period, bills due soon, subscriptions with renewal dates. Label numbers [DATA].
4. Never pay, transfer, trade or give financial advice; hand the action to the user.

Next: `lifeos-knowledgeos` to file the receipt image.

Scratchpad: end per `lifeos/references/scratchpad.md`.
