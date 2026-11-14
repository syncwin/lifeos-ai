---
name: lifeos-moneyos
description: "Starter skill for the MoneyOS module, money records. Use when the user says \"log this expense\", \"log this receipt\", \"scan this receipt\", \"what bills are due\", \"my subscriptions\", or \"am I on budget\". Records and reports only; it never moves money."
license: MIT
---

# LifeOS MoneyOS
Needs: EntityOS MCP; module `moneyos` enabled (off by default).
Start: run the `lifeos` router first if it has not run.

1. Categories, currency, budgets: `search_context("money categories, currency, budgets")`.
2. Receipt to expense: extract date, merchant, amount, category; fill in `lifeos/references/risk-check.md` and save only on its exact reply. Unreadable fields are [UNKNOWN], not guessed.
3. Reports: totals by category and period, bills due soon, subscriptions with renewal dates. Label numbers [DATA].
4. Records and reports only; money rules in `lifeos/references/rules.md` (Approvals).

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- Each expense shows date, merchant, amount, category; unreadable fields are [UNKNOWN] and nothing was saved without a filled risk-check block and its exact reply.
- Report numbers are [DATA]; no payment, transfer, trade or financial advice was given.

## Handoff
Delivered: Saved expense records or a spending, bills and subscriptions report.
Next: file the receipt image -> `lifeos-knowledgeos`; record -> `lifeos-workos-log`.

Scratchpad: end per `lifeos/references/scratchpad.md`.
