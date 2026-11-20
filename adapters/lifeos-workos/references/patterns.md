# Writing patterns (cite by number)

1. Jargon or unexplained acronyms.
2. Promotional tone (hype, adjectives that sell).
3. Unhedged claims with no source.
4. Filler (throat-clearing, restating the question).
5. Vague referents ("this", "it", "they" with no anchor).
6. Superlatives and absolutes ("best", "always", "never").
7. Closers that summarise or invite ("In conclusion", "Let me know").
8. Dates and numbers without a unit, source or timeframe.
9. Formatting that hides meaning (walls of text, decorative bold, inconsistent headings).
10. Language variant mismatch or banned terms from `search_context("voice")`.

11. Table data restated in the surrounding prose (introduce a table in a full sentence, add context, do not repeat its numbers: duplication reads as padding and gives a figure two places to go stale).
12. Heading level labels (`H2:` and similar) printed as visible text instead of rendered as real headings (labels are structure markers for the drafter, not content).
13. Dates in the article body (a "last updated" line, "as of [month and year]", a bare year hung on a statistic) unless the owner's policy in EntityOS allows them (fix: state the fact plainly, and where a figure needs its period, fold the period into the fact itself instead of presenting it as a freshness marker; why: a dated page reads stale a quarter later even when every figure is still correct); a source citation's own publication date is the exception, because it belongs to the source.
14. An audience or customer segment list that omits the real majority segment named in the audience record (give the majority segment its own explicit mention).

Notes: pattern 1 also holds this business's own industry swap list (a jargon term is replaced by what it means, not by a synonym that still needs specialist knowledge); pattern 10 covers one language variant per document, with quoted source material keeping its original spelling.

## Maintaining the glossary (pattern intake protocol)
The glossary holds rules, not an archive of every sentence an editor corrected. Per-business patterns are stored in EntityOS as part of the entity's brand context (`search_context("writing patterns")`), not in this file. They **start empty and grow from reviewer pattern frequency** (the Pattern Frequency section of each review scratchpad); never pre-populate guessed patterns, and an empty list is correct for a business with no review history. Generic AI-writing tells belong to `humanizeai`, not here.

Every entry has four parts: **Pattern** (one sentence, the abstract flaw, generalized beyond the wording that revealed it); **Fix** (one sentence, the general correction); **Why** (one sentence, the underlying reason: accuracy, specificity, hedging, evergreen-ness, jurisdiction; this lets the rule generalize); **One example** (two only for two distinct sub-cases of one mechanism).

For each editor-flagged pair, ask "what is this an instance of" before touching the glossary, with three outcomes: (1) already covered and the existing example makes the rule clear: add nothing; (2) already covered but this instance shows a nuance the prose does not state: fold the nuance into the Pattern, Fix and Why sentences without a second example; (3) a genuinely new mechanism: add a new entry, one example. This ties the glossary's size to the number of distinct mechanisms, not the number of sentences flagged.

Trimming: from the recorded pattern frequencies, a category that has not triggered across many recent drafts drops back to its Pattern, Fix and Why sentences with the example removed; a rule the drafting stage has clearly internalized does not keep its training wheels. Writes to EntityOS follow `${CLAUDE_PLUGIN_ROOT}/references/entityos-write-confirm.md`; patterns are proposed as `unverified` until the owner confirms.

## Checker data (read by the writing-check recipe)
Lines starting `phrases N:` list banned phrases for pattern N, separated by `|`, matched case-insensitively as whole words. `limit` lines set numeric limits.
phrases 2: game-changer | cutting-edge | revolutionary | world-class | unlock the power | take it to the next level | seamless | robust solution
phrases 4: it is important to note | it should be noted | needless to say | in today's world | in today's fast-paced | at the end of the day | when it comes to
phrases 6: the best | always | never | guaranteed | 100%
phrases 7: in conclusion | to sum up | in summary | let me know | hope this helps | feel free to reach out | don't hesitate to
limit max_words: 1200
limit max_sentence_words: 35
limit max_paragraph_lines: 8
