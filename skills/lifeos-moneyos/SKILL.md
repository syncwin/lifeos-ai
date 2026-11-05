---
name: lifeos-moneyos
description: "Starter skill for the MoneyOS module, money records. Use when the user says \"log this expense\", \"log this receipt\", \"scan this receipt\", \"what bills are due\", \"my subscriptions\", or \"am I on budget\". Records and reports only; it never moves money."
license: MIT
metadata:
  displayName: "LifeOS MoneyOS"
  version: "0.2.1"
  author: "@wasimness"
  company: "SyncWin"
---

# LifeOS MoneyOS
Needs: EntityOS MCP; module `moneyos` enabled (off by default).
Start: run the `lifeos` router first if it hasn't run in this chat.

1. Categories, currency, budgets: `search_context("money categories, currency, budgets")`.
2. Receipt to expense: extract date, merchant, amount, category; fill in `references/risk-check.md` and save only on its exact reply. Unreadable fields are [UNKNOWN], not guessed.
3. Reports: totals by category and period, bills due soon, subscriptions with renewal dates. Label numbers [DATA].
4. Records and reports only; money rules in `references/rules.md` (Approvals).

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- Each expense shows date, merchant, amount, category; unreadable fields are [UNKNOWN] and nothing was saved without a filled risk-check block and its exact reply.
- Report numbers are [DATA]; no payment, transfer, trade or financial advice was given.

## Handoff
Delivered: Saved expense records or a spending, bills and subscriptions report.
Next: file the receipt image -> `lifeos-knowledgeos`; record -> `workos-log`.

Scratchpad: end per `references/scratchpad.md`.
