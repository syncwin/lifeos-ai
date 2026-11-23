# Writing and Structure Standards

Industry-agnostic drafting and review mechanics for `lifeos-work-writing`. Voice specifics (language variant, point of view, banned phrases, heading case, required clauses, disclaimers, CTA convention, site index) come from LifeOS entity data (`search_context("voice")`, `get_policy`, `get_context`), never from this file. The numbered glossary is `patterns.md`; the deterministic checks are `writing-check.md`. Shared rules: `${CLAUDE_PLUGIN_ROOT}/references/core-rules.md`.

Contents: priority order; voice; drafting rules; humanize checkpoints; standalone humanization; four-exception rule; paragraph rules; meta block; headings; page-type defaults; acronyms; linking; CTA; word count; self-check; review gate; the two review files.

## Priority order and working from an existing draft
Priority is absolute: the brief or outline, then this file, then everything else. Follow the brief's structure exactly: no added, removed or reordered sections even where this file would suggest it. Where they conflict, the brief wins and the conflicting rule is set aside for that piece only.

With an existing draft and no brief, the draft's own headings inherit brief-level protection: required, wording and order kept. Preserve every piece of substantive information (figures, sources, examples, caveats). Cut genuine redundancy (a figure restated across sections, two paragraphs making one point). A structural change that looks necessary is raised, not made silently. Missing non-negotiable elements (an answer capsule, an FAQ, a conclusion) are proposed, not inserted, except the disclaimer and meta block, which are mandatory regardless.

## Step 0: load the business's voice, not a generic one
Read voice and reader from LifeOS entity data and any business-unit voice override. **Never default to a generic "professional and friendly" voice.** If LifeOS entity data states too little to draft from, ask within budget instead of guessing a tone. Determine POV from the brief and hold it start to finish: switching POV mid-piece is the most common failure. Anonymous-team or named-author POV, whichever LifeOS entity data specifies.

## Drafting rules
1. Structure comes from the brief, not habit: section order and answer-capsule placement exactly.
2. **Every factual claim traces to the research fact table.** No entry means flag it as unverified; do not publish silently. Before writing, apply the fabricated-source test (owner policy from LifeOS entity data) to anything attributed to a named source.
3. Regulated-industry language stays verbatim where LifeOS entity data names a regulator or required clauses; brand voice never applies to those clauses.
4. The four-exception rule (below).
5. Plain-English default and strict paragraph rules, enforced per section (see checkpoints).
6. No entity fact gets invented: addresses, names, phone numbers and claims about what the business offers come from LifeOS entity data.
7. Disclaimer, jurisdiction scoping and dates policy per the owner's compliance policy in LifeOS entity data.
8. Acronyms, meta block, headings, linking, CTA and citation mechanics per the sections below.
Output: a full draft matching the brief's structure, plus a short note listing any claim it could not source, any brief section it deviated from and why, and confirmation that the CTA matches the business's conversion definition. The draft is not delivery-ready until the review gate clears.

## The humanize checkpoints (three, always `humanizeai`)
1. **Per section:** draft one section, check paragraph length and plain-language compliance, run `humanizeai` against that section in full, fix everything found, then proceed. Never carry a violation forward to "fix later".
2. **Full document before handoff:** once the whole draft is assembled, run a second complete `humanizeai` pass over it as one piece. This catches document-wide patterns (a repeating paragraph opener, section-to-section rhythm uniformity) the per-section passes cannot see. Fix everything flagged before handoff.
3. **Verified before compliance review** (review Pass 0 below).
If `humanizeai` is not installed, say so once, name it, apply the enforceable subset (the paragraph, plain-language and pattern rules here and in `patterns.md`), and record the substitution; never mark it passed.

## Standalone humanization pass (on an already-reviewed piece)
When `humanizeai` runs alone against a piece that already cleared review, it rewrites how the piece reads and changes nothing else.
- **Must survive byte for byte:** the meta block (all five fields); every heading (wording, level, case, as real heading elements); any disclaimer block (verbatim, with its bold label); every figure, statistic and citation and its hedge; every link and its anchor placement; entity names, addresses and contact routes; quoted source material; table data; FAQ questions; list structure.
- **Must not appear as a result:** new facts, claims or numbers of any kind; personal anecdotes or first-person singular where LifeOS entity data specifies team voice; urgency or scarcity phrasing; a new date beyond a source's own citation date.
- **Free to change:** sentence rhythm, transitions, paragraph flow, word choice where meaning is untouched.
Load the voice, these standards and the brief before running it. Afterward do not re-run all review passes: verify the preservation contract held, then re-check only what a rewrite can disturb (meta block, headings and heading case, disclaimer, figures and citations, link placement and spacing, language-variant consistency, voice bans, dates). Anything changed beyond rhythm, transitions, flow or neutral word choice is a regression: restore it from the pre-pass version.

## The four-exception rule against filler statements
Avoid four kinds of statement in published content, **except where an exception genuinely applies** (four real outs, not one):
- **Generalized statements:** broad claims with no specific evidence. Replace with a concrete, balanced description of what is actually there.
- **Subjective statements:** opinions or value judgments stated as fact ("upscale", "top choice", "truly wonderful"). State the observable fact; let the reader form the opinion.
- **Promotional statements:** marketing language or exaggerated sales-style wording that oversells instead of informing.
- **Non-evergreen statements:** time-sensitive detail (a stat, a ranking, a price, a count) that goes stale quickly. Use durable phrasing wherever the content does not specifically need the snapshot.

**The exception clause:** a statement in one of these categories can stand if it is (1) essential to what the piece is trying to say, (2) contextually relevant to this content type, (3) backed by a verifiable source (not just softened wording), or (4) explicitly required by the brief. The rule targets unnecessary instances, not all specificity or every well-evidenced claim.

## Paragraph and plain-language rules
- Every paragraph stays short and scannable: a workable default is 50 words or fewer, mixing one-, two- and three-sentence paragraphs instead of a uniform length.
- **Island test:** each paragraph is understandable alone, without depending on the one before or after.
- Plain language for the stated audience: no jargon the target reader would not use, unless the audience is technical. Define any unavoidable technical term on first use.
- **Enforcement is per section, not end of draft**, then a full-document pass once assembled (checkpoints above).

## Required meta block
Ships with every published piece, above the H1, as a bold-labelled list (never a table): **Meta Title** (under about 60 characters, primary keyword near the front); **Meta Description** (about 140 to 160 characters, states what the reader gets, no urgency or sales phrasing); **Meta Tags** (comma-separated, from the brief's keyword block); **Page Slug** (lowercase, hyphenated, no dates or filler words); **Target destination** (the specific site or property this publishes to). These sit outside the word count.

## Heading mechanics
- A brief marks each heading's level (`H1:`, `H2:`, `H3:`). The draft renders that level as a **real heading element**, never printing the literal label as visible text.
- Heading levels stay sequential: no H2 followed directly by an H4.
- **Heading case follows LifeOS entity data** (Title Case is the common default), applied consistently across every heading regardless of how the brief typed it, unless the brief gives an explicit case instruction.
- List content (bullets, table cells, checklist items) is sentence case, so a list item does not masquerade as a heading.

## Structural defaults by page type
- **Answer capsule** near the top for pages competing for a direct-answer or AI-answer placement: a complete, quotable sentence resolving the core question, true out of context, before supporting detail.
- **Master or comparison tables** wherever the content is inherently comparative (pricing tiers, plans, specs, neighborhoods, product lines); once a fact is in the table, do not restate the figure in the prose. The table is the source of record; the prose adds context.
- **FAQ block** only where real, distinct questions exist, aligned to search and reader intent, never padded to hit a count. Lead each answer with the direct answer.
- **A closing section** (commonly "Conclusion") that is forward-looking, not a restatement, with the CTA inside it.
- **Formatting restraint:** tables, lists and quotes sit alongside prose and do not replace it. A section built only from formatted blocks reads as fragmented notes. Each element earns its place by making something clearer than a sentence would.

## Acronym and abbreviation handling
Only official, recognized terms get abbreviated, never an invented shorthand. Spell out the full name with the acronym in parentheses on first use, everywhere in the piece (not just the first section). If a term appears once, plain language beats introducing an acronym that is never reused.

## Linking mechanics
- **Internal links first from the brief's own list**, then filled from the business's actual site index in LifeOS entity data; never a constructed or guessed URL.
- **Anchor text attributes the source, not the raw figure:** state a figure in plain prose, then attribute it in a separate clause with the source name as the hyperlink, not a link wrapped around the number. Reserve this for genuinely key figures.
- **Link spacing:** one link per sentence at most, placed where it is contextually relevant as the content is written; never batched at the end of a paragraph or section.
- **Citation format** for a sourced figure: publication name, the specific page or report it came from, and its publication date, for example "According to **[publication]** in [report name], published [date], ...", with the anchor on the bolded publication name.
- **Source lines under any table of statistics**, linking each figure's source with descriptive anchor text.
- **External links** only where the brief requires one or a claim needs authoritative backing; no fixed minimum, no unnecessary count.
- **Never link:** a competitor's site (inspiration only), a low-authority or unverified site, a generic homepage as a promotional anchor.

## CTA rules
Natural placement, declarative sentences, never rhetorical questions. The closing CTA is action-only: no internal or external links inside it, so it drives exactly one action. Additional contextual CTAs after major sections are fine only where the brief calls for a lead-generation structure; default to a single closing CTA.

## Word count
Count everything from the opening heading through the final paragraph inclusive: body prose, headings, FAQ, table content, CTA, disclaimer. Exclude the meta block and other non-body metadata.

## Pre-handoff self-check
Before treating a draft as complete, self-check it against the categories that have caused real revision rounds most often for this business, tracked in a short, business-specific "known issues" note that grows over time (LifeOS entity data writing patterns; parallel to the pattern-frequency tally in the review scratchpad). Catching them first means the review finds less to send back.

## The review gate: three passes, never collapsed
- **Pass 0, humanization verification.** Confirm the full-document `humanizeai` pass actually ran and worked, before any compliance checking. If the draft arrives cold (no visibility into how it was produced), run a full pass now; never assume it was done. If `humanizeai` is missing, apply the fallback and record the substitution; never mark it passed.
- **Pass A, iterative compliance loop.** A step-by-step self-audit against the writing and compliance standards and the brief, one category at a time, repeated until every category is clean (normally several rounds before the person sees the draft). Categories, cross-referenced against the brief and known-issues notes: brief and structure compliance, voice/POV/tone, paragraph and plain language, accuracy and compliance and legal, linking/CTAs/FAQs, grammar and quality, entity-fact accuracy, business-specific conventions.
- **Pass B, final editorial review**, a separate, later pass run as a distinct reviewer would read it, not the writer re-checking its own work; name it as such. **Reader-comprehension test:** every piece must be understandable by a reader with zero specialist knowledge of the business's industry: plain English, no unexplained jargon, professional (not casual) tone, every acronym spelled out on first use and only if it is a real recognized term; where a concept is genuinely complex, explain the mechanism instead of relabeling it with simpler words. Could someone with no industry background read it once and explain back what every part means and what happens next? If not, it fails the gate. Pass B also confirms: an explicit redundancy check (restated facts, duplicate ideas, a fact in both prose and a table: cut it), full compliance with the approved brief, every link working with no unnecessary external link and source lines under statistics tables, keyword-tier coverage as mapped, every factual claim cited per the owner's sourcing policy, the meta block present and complete, heading mechanics correct, no unauthorized dates.

**No partial pass, ever.** A draft leaves review only once every category is clean, Pass 0 is confirmed and Pass B is complete. If a category cannot be resolved without a decision only the person can make, surface that specific item clearly: the one legitimate reason a draft goes out with an open item, and it is flagged, never buried.

**AI detection and remediation:** if the workflow includes AI-detection, plagiarism or grammar reports, check them here, flagged for the author and never self-marked as passed (they are not agent-verifiable). Where a detector flags specific paragraphs: rewrite only those, run `humanizeai` on them to diagnose the underlying pattern, and if the same pattern recurs across pieces, note it as a suggestion for the package owner (core change control) instead of patching the taxonomy here.

## Review deliverables: exactly two files, every time
| File | Contents |
|---|---|
| `scratchpad.md` | Compliance checklist results, fixes applied, flagged-for-author items, sources verified, pattern-frequency tally |
| `session-lessons.md` | What this session produced, what got missed on the first pass, decisions made and why, what to watch for next time, open questions |

**Never create a third report file**; a pattern-frequency log is a section inside the scratchpad. (This is the review's own pair; the stage's closing ledger still ends per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.)

`scratchpad.md` skeleton:
```
# Scratchpad: [piece title]

## 1. Compliance Checklist Results
[per category: pass count, full detail on any failure]

## 2. Humanization Notes
[condensed from humanizeai: what changed, what was deliberately left, anything flagged but not changed]

## 3. Flagged for the Author
[AI-detection, plagiarism, grammar reports, anything needing a human decision]

## 4. Sources Verified
[claim -> source; anything that could not be verified]

## 5. Pattern Frequency
[known-issue category tags that triggered a fix this draft, comma-separated]
```

`session-lessons.md` skeleton:
```
# Session Lessons: [piece title]

## 1. What This Session Produced
## 2. What Got Missed on the First Pass
## 3. Decisions Made and Why
## 4. What to Watch For Next Time
## 5. Open Questions for the Editor
```

**Every lesson must be traceable to something that happened in this session**: a lesson that would read identically on any other piece is filler; cut it. Recurring mistakes are the highest-value entries: where something also appeared in earlier work for this business, say so and name the pattern. **Before ending the turn, confirm:** both files written in full, no third report file, both presented alongside the piece.
