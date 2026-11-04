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

## Checker data (read by scripts/check_draft.py)
Lines starting `phrases N:` list banned phrases for pattern N, separated by `|`, matched case-insensitively as whole words. `limit` lines set numeric limits.
phrases 2: game-changer | cutting-edge | revolutionary | world-class | unlock the power | take it to the next level | seamless | robust solution
phrases 4: it is important to note | it should be noted | needless to say | in today's world | in today's fast-paced | at the end of the day | when it comes to
phrases 6: the best | always | never | guaranteed | 100%
phrases 7: in conclusion | to sum up | in summary | let me know | hope this helps | feel free to reach out | don't hesitate to
limit max_words: 1200
limit max_sentence_words: 35
limit max_paragraph_lines: 8
