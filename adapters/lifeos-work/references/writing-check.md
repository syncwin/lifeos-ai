# Writing check (recipe)

The deterministic draft check, done by reading. No script runs; the earlier Python checker is maintainer tooling in `dev/`. Limits and phrase lists come from the "Checker data" section of `patterns.md` (lines `limit <name>: <n>` and `phrases <N>: a | b | c`). Defaults when a limit line is missing: max_words 1200, max_sentence_words 35, max_paragraph_lines 8.

Work through the draft line by line, number the lines, and report one line per check as PASS, WARN, FAIL or SKIP.

| Check | How | Result |
|---|---|---|
| Length | Count words (letters, digits, apostrophes and hyphens make a word). | FAIL when over max_words, else PASS |
| Sentence length | Skip lines starting `#`, `|` or a code fence. Split other lines at `.`, `!` or `?` followed by a space. | WARN listing lines with a sentence over max_sentence_words, else PASS |
| Paragraph length (pattern 9) | A paragraph is consecutive non-empty lines that do not start `#`, `|`, `-` or `*`. | WARN listing the start line of each over max_paragraph_lines, else PASS |
| Headings (pattern 9) | None: SKIP. Otherwise more than one H1, a jump of more than one level (H2 to H4), or a repeated heading text (case-insensitive) each make a problem. | FAIL listing the problems, else PASS |
| FAQ block | Heading containing "faq" or "frequently asked": count later lines ending in `?` (ignoring a trailing `*`). No such heading: SKIP. | WARN under 2 questions, else PASS |
| Banned phrases | For each `phrases <N>` line, search each phrase case-insensitively as whole words. | WARN `pattern N: "phrase" line 3, 9` per hit; PASS `pattern N: no banned phrases` |
| Owner banned terms (pattern 10) | Terms from `search_context("voice")`, same whole-word match. None given: SKIP with the note to read them from LifeOS entity data. | FAIL on any hit, else PASS |

End with `RESULT: FAIL` (any FAIL), `RESULT: WARN` (any WARN) or `RESULT: PASS`.
