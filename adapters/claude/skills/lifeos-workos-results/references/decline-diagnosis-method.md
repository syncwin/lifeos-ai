# Decline Diagnosis: Decision Tree and Method

Method for `lifeos-workos-results`. The question is never "did the number drop". It is "which of several things moved, when, by how much, and which of them is ours to fix." Business inputs (market and region filter, metric source, KPI definitions, documented past decisions) come from EntityOS (`search_context("metric source, region filter, KPI definitions")`). Verdict table, CTR curve and AI-visibility panel: `lifeos-workos-demand/references/scoring-and-verdict-framework.md`. Shared rules: `lifeos/references/core-rules.md`.

Contents: two directions; export check; decision tree; segmenting; CTR versus ranking; cannibalization; dilution; concurrent events; snippet rewriting; migration signatures; AI answer surfaces; output shape.

## Two directions of one discipline
Diagnosing a drop, and checking whether a fix worked, plus the AI-era measurement (the visibility panel). This stage explains movements; it does not run checklists, score demand or decide what to build. A finding that a page's opening passage is unquotable is an audit finding; that its clicks fell 77% in a week, and why, is this stage's.

**Before starting:** load the business record and read Decisions: half of what looks like a new decline is often a documented one with a settled cause.

**Direction 1, diagnose a movement.** Three failure modes this stage exists to prevent: (1) merging separate events into one cause (a site can lose ground to several unrelated things in one quarter; merging them yields a fix for one and a mystery for the other two); (2) reading a page-level average as the truth (where most impressions sit in a long tail, page-level position can look flat while the head term falls sharply: always drill to query level); (3) blaming what changed most recently (the obvious suspect is often the smaller share: attribute by segment, with numbers, before naming a cause). Establish the exact window and magnitude from the data. List every candidate event in the same window (algorithm or platform update, a site change, seasonality, a competitor's move, a tracking break) and rule them in or out against the most specific evidence, not the vaguest plausible story. State the cause with a confidence level; where evidence does not decide it, say so and name what evidence would.

**Direction 2, verdict on a shipped fix.** Standard windows: an initial read at about 28 days and a fuller read at 8 to 12 weeks (adjust to the business's cadence). The verdict is one of the five in the framework table (Unmeasurable, Too Early, Working, Failed, Confounded). **A complete row past its reading date with no outcome filled in is work nobody can prove did anything**: say so instead of quietly listing it as done. Log the verdict against the tracker. **When a new pull overturns a documented finding:** correct the earlier claim, retire the old series outright instead of reconciling the two, and record the supersede as a Decision.

**Output location:** writes the web tracker, never a separate durable file, never the content tracker: a diagnosis writes new tracker rows with `Gated On` filled and Findings rows, one per event, each carrying its share of the loss; a results verdict writes `Outcome` on completed rows, appends Page Readings and adds Findings rows; the AI panel appends AI Visibility and writes Cited and Named counts on the Snapshot row with movement since last capture. Snapshot is append-only (`lifeos-workos-sprint/references/workbook-and-tracker-spec.md`). Every claim carries figure, window, filter, source and date, or it does not go in.

**Standards:** separate events stay separate (where two causes overlap in time, each is dated and given its share); a change is attributed to an action only with a stated mechanism (correlation across one period is not causation); a cause outside the business's control is named as such and the recovery target set accordingly; a change is called a success or failure only after its window closes; a single-cycle AI-visibility move of one or two points is noise, and direction across three consecutive captures is the shortest span worth calling a trend. The AI panel uses the same fixed prompt set every time, in conversational form, logged out, with a consistent market and language filter and the same order across assistants; Cited and Named stay separate and are never combined; a prompt flipping to absent across every surface at once is an entity problem (route to `content-audit-strategy` entity mode with EntityOS facts), not a content problem.

## Before anything: check the export
Date range, market or country filter, equal window lengths (normalize unequal windows to a per-day rate). Segment to this business's actual market; a blended figure carries drag from irrelevant geographies and is a different number from the one that matters. Set the date range wide enough for seasonal context (a year or more) before concluding anything: a drop that recurs every year is seasonality, not a defect. State the range, filter and window equality in the first line of the diagnosis.

## The decision tree
Read impressions or reach, clicks or engagement, and position or ranking together; the combination names the cause class:

| Impressions | Clicks | Position | Cause class |
|---|---|---|---|
| Down | Down | Down | Ranking loss: an algorithm or platform update, competitor displacement, or a technical or indexing fault |
| Flat | Down | Flat | Presentation problem: title, snippet, or a results-page feature taking the click before it happens |
| Flat or up | Down | Flat | Dilution or a results-page feature: the query is shown to more people, or an AI-generated answer satisfies it first |
| Down | Down | Flat | Demand or upstream absorption: fewer searches reaching the result at all |
| Flat | Flat | Down | Early displacement: clicks usually follow within weeks |

Where impressions hold and clicks fall, the title or snippet is the likely problem, not the ranking: check that before touching anything downstream.

## Segment before naming a cause
A site-wide percentage is not a diagnosis; attribute it: **by page** (per-day figures before and after, per URL, each page's share of the total loss; usually one or two pages carry most of it); **by query**, for every page carrying a material share (this is where position dilution shows up); **by branded versus non-branded** (a branded decline is a business problem, not a search one); **by market or geography** (confirm the loss is where it matters); **cross-check against a second, independent data source** (two sources moving in opposite directions signals a tracking fault, not a ranking one). Report the shares: "page X carries 77% of the loss, a recent migration carries 20%, everything else carries 3%" is a diagnosis; "traffic is down 41%" is a number.

## CTR problem or ranking problem
Where clicks are the complaint, the position band names which it is: positions 1 to 3 with weak CTR is a results-page problem, not a weak title (check what else is on the page before touching the snippet); positions 4 to 10 with weak CTR is a snippet or intent-match problem, usually the highest return per hour in the whole diagnosis; positions 6 to 10 with normal CTR for that band is a ranking problem, and no snippet work overcomes a weak position. **Never apply one flat CTR threshold across positions**: a floor that flags a normal position-10 result as broken can hide a genuinely broken position-2 one; compare every figure to this business's own curve for its band.

## Cannibalization, and its false positives
Detected from one query returning two or more of the business's own items across a period. Three traps to clear before calling it: **averaged position hides geography and variants** (segment before concluding); **distance matters** (two items at positions three and eleven split almost nothing, two at three and four split real traffic); **an archive, tag or paginated URL ranking is usually an indexation problem**, not cannibalization, and needs a different fix.

## Position dilution
A page-level average can hide a head-term decline whenever a large share of a page's reach sits in a long tail at weak positions: the page-level figure stays flat while the term that produces clicks falls sharply. Whenever a page loses clicks at a "stable" average position, drill to the head term and build a time series on that query alone. **If the query-level series contradicts the page-level series, the query-level series is the truth**: retire the page-level one outright instead of reconciling the two.

## Separating concurrent events
Sites lose ground to several unrelated things at once; merging them produces one fix and two mysteries. For each candidate event establish: the period it starts (weekly resolution, not monthly, since a monthly view hides a step change); its signature (a constant-position CTR fall is dilution; a position stepping down over two or three weeks is displacement; a single-week position step at a known change date is that change); its share of the loss; and whether it is within this business's control at all (dilution inside a query, or a competitor's own move, is not fixable by editing the page: say so and set the recovery target accordingly). Write each event as its own dated paragraph with its own numbers, never one merged narrative.

## Snippet and presentation rewriting
Where impressions and position hold but clicks fall, check what is actually displayed: a search or AI platform frequently ignores a clean meta description and builds its own snippet from on-page text, which is how an unrelated string can end up as the pitch shown in results. Where on-page text is the source, the fix is the on-page text, not the meta description alone.

## Migration signatures
Redirects done correctly do not cause lasting ranking-signal loss, and platforms recrawl and reprocess over time: stabilization after a well-executed move typically takes 4 to 12 weeks, longer on larger sites. The signature of a migration still in progress: old items still holding clicks, new items drawing impressions at worse positions than their old counterparts, overall reach roughly flat. That is reprocessing, not a penalty. **At weeks 5 to 6, check before escalating:** every old URL redirects directly to its final destination with no chains; internal links point at final destinations, not through redirects; old URLs are still being recrawled; new URLs are indexed. **Escalate only past roughly 12 weeks**: long recovery tails are common, and most failures trace to incomplete redirects, chains or misconfigured redirect types, not to the act of moving.

## AI-generated answer surfaces
Where impressions rise and clicks fall on informational queries, an AI-generated answer may be satisfying the query before the click. Do not quote a single CTR-decline percentage without naming its source: published figures vary widely by sample and method, and at least one major analysis reframes much of the apparent decline as a denominator effect (impressions rising while clicks stayed flat). Give the range and the sources. **Cited items earn materially more clicks than uncited ones on the same AI-answer results**: the response is to become the cited source, not to withdraw from the query. Where a platform's own AI-visibility report exists, use it for direction only: it typically reports reach or impressions without click or query-level detail, and blends related surface types; never infer a CTR from it.

## Output shape
Four paragraphs at most in the diagnosis: what moved (window, filter, per-day figures); where the loss sits, by segment, with shares; each event, dated, with its signature and whether it is within the business's control; what is now withdrawn from a previous diagnosis, in one sentence. Then the tasks it produces, into the tracker.
