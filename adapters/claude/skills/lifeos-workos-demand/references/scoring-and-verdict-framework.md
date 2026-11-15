# Scoring, Clustering, and Verdict Framework

Method for `lifeos-workos-demand` (scoring, clustering, mapping) and `lifeos-workos-results` (verdicts, AI-visibility panel). The numbers below are starting defaults, not universal constants: recalibrate per business once real tracker history exists, and say in the report which figures are defaults and which are calibrated. Business inputs (market, ideal customer, existing pillars, constraints and no-gos, conversion definition, approved sources) come from EntityOS (`get_context`, `get_policy`, `search_context("markets, audiences")`, `search_context("approved sources")`).

## Scope and run opening
- No plans, sequencing, briefs, outlines or copy in a scoring run: that is the planning half of `lifeos-workos-demand` (`cluster-and-treatment-model.md`).
- **New-content and rewrite candidates stay separated**: an existing page is never presented as a new-content recommendation.
- Site health and decline diagnosis are not assessed here: forward one line to `content-audit-strategy` (site) or `lifeos-workos-results` (decline). Competitor work stops at public search presence (pages, structure, entity signals, citation footprint), not business model or pricing.
- Ask for the date range explicitly; a 28-day default is too short for this read. Open the run by stating what was inferred in three or four lines: domain, market, date range, filters, sitemap contents, anything missing.
- Modes: scoring always runs; competitor analysis runs before any first content plan and is not optional then; evergreen discovery runs on the schedule the business record sets; results mode runs at the top of every session, before scoring, because a verdict on a treatment type changes what is recommended next.

## Workflow (ten steps)
1. **Exclusion gate first** (below).
2. **Inventory and normalize.** List what is supplied and what is missing, and what the gap costs. If a normalization script is warranted for this business's export columns, build it once real exports are in hand and flag it as a next step.
3. **Cluster** semantically, then by situation. **Audience decides which unit or property a query routes to**, not surface topic similarity. Where clustering carries a URL decision, validate against real results (screenshots or a live check), not wording similarity alone.
4. **Coverage check**: covered, partial or gap.
5. **Score** on the four axes plus intent value.
6. **Enrich** each cluster: intent, conversational form, asset type (page, comparison, tool), the answer-target sentence, effort, confidence, target period.
7. **Dimension check**: confirm queries, pages, clicks, impressions, position, trends, gaps, clustering and coverage were all examined; name anything the data cannot support instead of skipping it silently.
8. **Evergreen discovery**, low confidence by default.
9. **Competitor analysis**: say which scores moved and why; an unexplained adjustment cannot be checked.
10. **Keyword and content mapping**: every relevant query to exactly one existing or planned item, so downstream stages read one map instead of re-deriving coverage.

## The exclusion gate: runs before scoring, not after
Build the exclusion list from the business record's constraints and no-gos first. A forbidden query is never scored: flag it in "Do Not Create" with a reason. Scoring a forbidden query and rejecting it afterward invites relitigating it. A high-scoring forbidden query goes in "Do Not Create", never presented as a missed opportunity.

## Opportunity score, 0 to 100 (default weights)
| Component | Default weight | Input | Rule |
|---|---|---|---|
| Demand | 25 | Cluster impressions (or an equivalent volume signal) | `log10(volume)` normalized against the highest-volume cluster in the run, so one head term does not flatten the rest |
| Winnability | 25 | Best current position in cluster | Band table below |
| Click upside | 20 | Projected clicks at target position minus current | This business's own CTR curve (below), target position 4 by default |
| Intent value | 20 | Query intent tier | Tier table below |
| Coverage gap | 10 | Coverage verdict | Gap 10, Partial 4, Covered excluded entirely |

**Winnability bands:** position 5 to 20 scores 25 (already relevant, nothing targets it properly); 21 to 50 scores 16; 3 to 4 scores 12 (near the ceiling, less headroom); 51+ scores 8 (leans on demand); unranked scores 6, flagged low confidence.

**Intent tiers:** transactional (names a purchase, booking, quote or price) 20; commercial investigation (compares or evaluates before deciding) 16; local or specific informational 10; general informational 5. The business's conversion goal decides which tier counts as transactional: a lead-gen business and an e-commerce business draw this line differently. Read it from EntityOS (conversion definition); do not assume.

**Modifiers, applied after scoring, never inside it:** a trend multiplier (0.85 to 1.15) from an equal-length period-over-period comparison, fixed at 1.0 and stated as "not measured" without one; an effort divisor (Low 1.0, Medium 1.3, High 1.8). Priority rank is score divided by the divisor, but the raw score stays visible.

**Lead and conversion potential is a separate scale (High, Medium, Low)**, never blended into the opportunity score or any traffic score: rated from measured conversion behavior of comparable pages where available, falling back to intent tier, then to buying-journey stage. State plainly when it ran on the intent proxy instead of measured data.

**Confidence:** High (volume at or above a business-calibrated floor and the site already ranks somewhere for it); Medium (real but thin); Low (under the floor, unranked, or unverified coverage). Low-confidence rows appear in the report and never enter the top action bucket.

**Action-plan thresholds (defaults):** 70+ with Low or Medium effort and non-Low confidence: create immediately; 55 to 69, or 70+ at High effort: within 30 days; 40 to 54: within 90 days; under 40, or unverified coverage: monitor.

## Calibration check, every run
Demand is normalized against the run's own distribution, so scores are relative to this dataset, not absolute. On a small export (roughly under 50 clusters) scores compress upward and most rows land in "create immediately", which is meaningless as a priority signal. **If more than about a third of scored rows sit above 70, say so** and rank by relative position within the run instead of treating the thresholds as gospel; a bigger export (a full year beats a quarter) fixes it properly.

## Noise controls
Drop items under a low-volume floor before clustering; exclude brand-name queries from scoring entirely; establish the market from the site index and top queries, then filter to it; route excluded items to "Do not create" with a reason instead of dropping them silently (out of market, already covered, already served by two competing items, a transaction type the business does not serve, anything on the exclusion list).

## Seasonality
Read the seasonal shape from the data where available, from the queries where not. Every recommendation carries a suggested publish date roughly six to eight weeks ahead of its demand peak, so it has time to index and settle. Where the data shows no seasonality, say so and leave timing open.

## What scoring cannot see: say this every run
Search and demand data understates real demand (it covers only what the business already surfaces on; evergreen discovery covers the blind spot); impressions are position-dependent (a page-two result accrues impressions with no clicks: reach, not demand); an averaged position blends segments and can hide a head-term collapse; a keyword-difficulty tool measures the authority of current top pages, not whether this business can win (winnability comes from competitor work). **A score is a starting position, not a verdict.**

## Small datasets
Weight by volume, never average raw CTR or raw position. Apply the noise floor before scoring, not after. Prefer coarse bands to fine scores on thin data: a score to one decimal place on forty clusters implies precision that is not there.

## Conversational clustering and the one-asset test
Cluster semantic-first, then validate against real results: token or embedding similarity is intent-blind. Before consolidating or committing to a cluster, check that the top current results overlap (roughly three or four shared results in the top ten is the working threshold). **Coverage matched on a slug or title alone is unverified** and cannot enter the top action bucket.

Write every cluster in **conversational form**, the way a real person would ask, before scoring; a cluster whose conversational form cannot be written drops to low confidence. Never invent one to fit a keyword; label an invented one a hypothesis.

**The one-asset test:** can one strong page, comparison table or tool answer several of these queries together? If yes, that is one real cluster. If no, it was a list of keywords wearing a cluster's name: send it back.

**Striking distance is a working range, not a hard boundary** (roughly positions 4 to 15 for search-ranked content): rank inside it by volume and intent, not by position alone; an item at position 12 with high volume beats one at position 8 with negligible volume.

## Coverage check
**Covered**: drop, count it. **Partial** (ranking or existing but wrong intent): rewrite candidate, forwarded to the planning half (`cluster-and-treatment-model.md`), excluded from the new-content action plan. **Gap**: eligible for scoring.

## Keyword and content mapping
Attach every relevant query to exactly one existing or planned content item, never two. Tag every term with one action:

| Tag | Rule | Drafting use |
|---|---|---|
| Protect | Already earns clicks at a strong position | Keep in title, H1, opening |
| Striking distance | In the working range, real volume | Exact phrase in an H2 and the answer capsule |
| Coverage gap | Real volume, weak position | Add a section or FAQ |
| Gap | No page ranks for it at all | Assign to the planned page that should own it, or open a new row |
| Monitor | Below the noise floor | Cover only where it fits naturally |
| Route to other unit | Off scope for this property (multi-unit business) | Belongs to that unit's site |
| Exclude | Off-intent or off-topic entirely | Never targeted |

Append an AEO-question flag to any question-form query: it becomes an H3 or FAQ with a short direct answer. A page's summary row states its Primary Keyword, its full Conversational Queries breakdown by tag, and its Must-Answer Questions.

**Checks before delivery:** every relevant query is mapped once; no term is the target of two items; every gap has an owner; every figure carries its window, filter and source.

## Evergreen discovery
Runs on its own schedule. Draws from the approved sources in EntityOS (`search_context("approved sources")`). **Never scored on the four axes, always marked low confidence** until validated by actual results.

## Competitor and winnability analysis
Required before a first content plan. For each contested cluster: who currently wins, what their page has that this business's does not, whether the target is genuinely winnable. **State when a target is not winnable and what to aim at instead.** Never build a competitor set from reputation alone.

## Report format
**Ceiling: 40 lines per section.** If it does not change a decision, it does not go in; detail belongs in the underlying data. Sections, each stating "none" in one line if empty: (1) run summary (business, date range, filter, files used, what was missing); (2) what the demand says, 3 to 4 lines; (3) content-type taxonomy considered (not just one default type); (4) scored opportunity table, one row per recommendation, sorted by priority rank; (5) opportunity detail for the top two buckets only: suggested title, target queries, intent, why it exists, evidence, content type, an answer-target sentence with a figure and its date, estimated impact (labelled an estimate), lead potential (labelled modelled or measured), links and cluster, effort, confidence, publish-by; (6) fix-before-creating (CTR anomalies and cannibalization, cheaper to fix than to write something new); (7) rewrite candidates (partial coverage, excluded from the new-content plan, forwarded to planning); (8) evergreen candidates, always low confidence; (9) do-not-create, every exclusion with a reason; (10) coverage audit summary, including how many verdicts were verified versus matched superficially; (11) method and limits (what ran on real data versus proxies, whether calibration fired, whether an AI surface makes projections optimistic).

**Quality gate:** every number traces to a supplied file or a stated assumption; every projection is labelled an estimate with its assumption; recommendations span more than one content type unless the business record narrows it; the do-not-create list has a reason on every line; nothing on the exclusion list appears as an opportunity; evergreen is unscored and low confidence; unverified coverage is stated as such; no briefs, outlines, draft copy or sprint plans anywhere in this report.

**Non-negotiables:** no metric the data does not contain; every third-party estimate labelled an estimate; no comparison period means the trend multiplier is 1.0, stated plainly; brand and entity terms excluded from scoring; the do-not-create list is mandatory; never invent a conversational query (label it a hypothesis); a verdict without a baseline is Unmeasurable, never inferred; never attribute a page's movement to a change without a stated mechanism.

**Output location:** scoring writes the Opportunities tab (every Do Not Create row with its reason), competitor mode writes Winnability on scored rows, evergreen writes Opportunities at low confidence, results mode writes Latest and Verdict on tracked rows (`lifeos-workos-sprint/references/workbook-and-tracker-spec.md`). Every Findings row carries Figure, Window, Filter, Source and Date in their own columns; no separate durable file.

## Building this business's own CTR curve
**A single universal curve is not defensible**: CTR varies by intent, brand versus non-brand, device, market, and what else is on the results page; a benchmark curve built before AI answer surfaces became common describes a layout that may no longer exist. Build the site's own curve from three to six months of the business's own market-filtered data, brand queries excluded; round position to whole numbers and band it (1, 2, 3, 4, 5, 6 to 10, 11 to 20, 21 to 50, 51+); **weight by volume, never average raw CTR**; require a minimum volume per band before trusting it, falling back to a benchmark shape only for thin bands; record the curve's date and window as a Decision and rebuild it periodically. State every run how many bands came from the business's own data versus a benchmark.

**Benchmark reference points** (verify current before quoting; this space moves fast and these figures date quickly): pre-AI-era baselines put position 1 around the high-20s percent CTR, falling steeply by position 10; several 2025-era studies found position-1 CTR falling year over year as AI-generated answers appear above organic results, with lower positions gaining relative share as users scroll past; independent analyses found large organic CTR reductions on queries where an AI answer appears, with a substantial CTR premium for being cited within that answer versus not appearing in it. **Never present a single AI-related CTR-decline figure as the number**: published ranges vary widely by sample and method; give the range and name the source. **Being cited is the response, not withdrawal**: cited items earn more clicks than uncited ones on the same AI-answer results, which is why the answer-target sentence matters more, not less, on exactly these queries. Never apply one flat CTR threshold across positions; compare every figure to the benchmark for its own band.

## Results verdicts
Results mode, at the top of every session, for every tracked item with a verdict due: read the latest figures against the baseline (same shape, same filters, window normalized to a per-day rate if unequal), set the verdict from the table, check for a competing event in the same window, and reclassify similar queued items up or down based on what the verdict says about the treatment type.

| Verdict | When |
|---|---|
| **Unmeasurable** | No baseline exists. Never converted into a real verdict by reasoning around the gap. |
| **Too Early** | Inside the first-read window (commonly about 28 days); never called success or failure yet. |
| **Working** | Clear positive movement at the final read window (commonly 8 to 12 weeks), attributable with a stated mechanism. |
| **Failed** | Clear negative or flat movement at the final read window, no positive mechanism found. |
| **Confounded** | A competing event landed in the same window: not attributable either way, and the verdict says which event. |

**A `Working` verdict on a treatment type raises the score of similar queued items; a `Failed` one lowers them.** Never attribute movement to a change without a stated mechanism: correlation across one period is not causation.

## AI-visibility panel
A fixed prompt set, in conversational form, run on a consistent schedule across the AI assistants the business cares about, logged out, with a consistent market and language filter and the same order across every assistant. The set changes only through a logged Decision saying what changed and why. Track **Cited** and **Named** as separate, never-combined metrics: the gap between them is the finding. A business named often but rarely cited usually has a structure or schema problem (route to `content-audit-strategy` and `content-seo-strategy` with EntityOS facts), not a content-quality problem; a prompt flipping to absent across every surface at once is an entity problem, not a content problem. A single-cycle move of one or two points is noise; direction across three consecutive captures is the shortest span worth calling a trend.
