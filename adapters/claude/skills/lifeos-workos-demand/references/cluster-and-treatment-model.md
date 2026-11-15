# Cluster Model, Treatment Decisions, and Handoff

Planning method for `lifeos-workos-demand`. Business inputs (capacity, exclusion list, conversion definition, whether properties may cross-link, authors) come from EntityOS (`get_context`, `get_policy`, `search_context`). Scoring and verdicts: `scoring-and-verdict-framework.md`. Shared rules: `lifeos/references/core-rules.md`.

## Planning workflow (one queue, not two lists)
Decides. Upstream stages produce findings and scores; planning turns them into one queue covering existing pages and new pages, because they compete for the same publishing hours. **Why one queue:** a page at position eight with real impressions and no answer block usually returns more, faster, than a new page starting from nothing, but only if both are ranked on the same list. Split them and refresh work quietly stops, because new content feels more like progress.

**Inputs:** scored opportunities and results verdicts (required); the competitor gap table (required before a first plan; without it the plan assumes everything scored is winnable, and a cluster held entirely by unbeatable incumbents needs re-aiming, not queuing); page-level findings forwarded from `content-audit-strategy` (strongly preferred); the business record and the content tracker.

**Mode A: topic and cluster planning.**
1. Treat every existing page with one of the five treatments below, with a stated reason.
2. Build the clusters (below). Every planned item states which conversational queries it answers; an item answering only one is justified in one line or merged into a neighbor.
3. **One queue, ranked by:** (1) expected conversion impact (conversion-potential rating for new work; impressions, position and intent for existing pages; measured conversion data outranks both when it exists); (2) speed to result (an existing page with impressions moves in weeks, a new page in months); (3) effort (cheap and high-impact first); (4) dependency (fill `Gated On`: a spoke before its pillar loses most of the benefit; a page rewritten before its cannibalization conflict is resolved may be the wrong page; a page rewritten during an unrecovered decline cannot be fairly read); (5) winnability from the competitor analysis (a high-scoring unwinnable cluster ranks below a lower-scoring open one); (6) fit with the ideal customer, as the tiebreaker. Every item is actionable: names the page or URL, what is created or changed, and the condition that makes it done. "Write about X" is not a plan item.
4. **Size to capacity.** Plan to the stated capacity, not to how many opportunities exist. Where capacity is unstated, derive it from hours and throughput (`search_context("working hours, capacity, owners per task type")`), recommend a figure with the reasoning, and record it as a Decision so later runs do not re-derive it.
5. Hand off (below).

**Mode B: whole-catalog audit (50+ pages, real data).** Tier every page by real performance data, never a category-level guess. Recommend prune, merge, update or keep per page, each citing the specific data point that justifies it (zero clicks in 12 months, cannibalizing a stronger page). Run a content-gap analysis against audience and pillar coverage. Feed the action list into Mode A's sequencing. For a whole-site audit from exports use `content-audit-strategy`.

**The six content rules** every planned item inherits, stated once at handoff instead of repeated per item:
1. The answer opens the piece: a complete, quotable sentence in the first hundred words, true out of context, resolving the reader's core question.
2. Every question is a real heading, not bold paragraph text pretending to be one.
3. Every figure is dated and sourced by name, never "recent data shows".
4. The business's own name appears in the body, not only the footer (the on-page half of fixing a cited-but-unnamed gap).
5. A real author or team identity and a genuine date; never bulk-refresh dates on content that was not revised.
6. One page per intent: a duplicate splits the retrieval signal exactly as it splits the ranking signal.

**Output:** writes the Content Tracker tab, sets `Status` and `Promoted To` on consumed Opportunities rows, and writes Findings rows. Every row carries `Dependency`, `Gated On` and `Conversational Queries`. Rows enter the one sprint through `lifeos-workos-sprint`, tagged `Owner Skill: Content`; **planning never plans a sprint itself.** The report holds the reasoning (shape of the plan, what was rejected and why, what ran on modelled versus measured data); the tracker holds the work; nothing appears in both.

**Non-negotiables:** never plan beyond stated capacity; never recommend something already queued, briefed, drafting or published; never write briefs, outlines or copy (handoff is a hard boundary); never recommend anything on the exclusion list; every leave-alone is stated (an absent page reads as an oversight); every impact figure is labelled modelled or measured; evergreen candidates stay low confidence until validated; every item carries an answer-target sentence with a figure and its date.

## The cluster model
A topic cluster is a **link structure**, not a list of related titles: if internal linking is not specified, what exists is a content calendar with a better name and none of the benefit.

**Structure:** a **pillar** (one page covering the whole topic at breadth, targets the head term, links to every spoke, receives a link back from each) and **spokes** (each covering one sub-question in depth, linking up to the pillar and sideways to two or three genuinely related siblings). **Depth: two levels**; a third level almost always means the second was drawn too narrowly and produces pages nobody links to. **Size: three to about eight spokes**: fewer is a page, not a cluster; past eight the pillar cannot cover them, which is the point to split into two clusters.

**Build order:** (0) validate against real results before committing: queries that look related can be answered by entirely different pages; check the top current results overlap (roughly three or four shared results in the top ten). (1) Name the head query the pillar targets; no head query, no pillar. (2) Place every existing page first: clusters are usually assembled from what is live plus a few gaps, not built from nothing. (3) Assign gaps from scored opportunities, in score order, after the exclusion gate. (4) Specify every link: for each page, what links in, what it links out to, the anchor-text intent; this is the part that gets skipped and the part that does the work. (5) Check the pillar can carry it: a pillar that is a thin index of links ranks for nothing. (6) Check linked pages are safe to link to: do not point a pillar at a page that may be removed or merged; resolve that first.

**Every page is marked live, queued or gap.** An orphaned page that belongs to a cluster but has no internal links pointing to it is the cheapest cluster fix available: no new content, one or two links, and a page that was already ranking starts contributing.

**Cluster health checklist:** pillar exists, is live, and answers the head query instead of indexing links · every spoke links up to the pillar · the pillar links down to every spoke · every spoke links sideways to at least two siblings · no two spokes target the same query · anchor text varies and describes the destination · no orphans inside the cluster · every page carries an answer target and (where the business uses one) a named author · the cluster maps to a real audience need, not just a keyword group.

**Sub-topics that are not pages:** a question at the same intent as the pillar becomes a dated section on the pillar, not its own page: a separate page would cannibalize the pillar the day it published. Say this explicitly in the plan; "we should cover X separately" recurs, and the answer needs to be on record.

**Cross-unit clusters** (multi-property businesses): a cluster can span properties only if the business record permits cross-linking between them (`search_context("cross-linking between properties")`). The rule that holds regardless: **a link is placed because it serves the reader**; links inserted only to move authority between owned properties, with no reason a reader would follow them, are visible as exactly that. Where the record says its own properties may compete for the same query, do not build the plan around preventing it: note the overlap and move on.

**Common failures:** pillar written last (spokes link nowhere until it exists) · spokes too narrow (should have been one page) · built from keywords instead of real reader questions · linking left unspecified ("link where relevant" produces no links: name the pages) · everything defaulted to one content type (some spokes are service pages, comparison pages, location pages or tools) · length used as the strategy (comprehensive is not cited more often than short and focused: write the length the question needs).

## Existing-page treatment: five options, choose the first that fits
Work down the list and stop at the first match. Every candidate page gets exactly one treatment with a stated reason; the reason is what stops the page being reconsidered from scratch next quarter.

1. **Is anything on it factually wrong or outdated on a regulated, financial or legal topic?** Refresh. Outranks everything: a stale figure stated confidently is an accuracy failure however the page otherwise performs.
2. **Does another page on the same site compete for the same query?** Consolidate: one absorbs the others, the rest redirect to it. Resolve before investing in either page. Specify which URL survives and why, what redirects, what content moves; removing content in a merge is normal, losing it silently is not. **Expect a dip before recovery** and say so when recommending it, or an unexplained post-merge drop reads as a mistake and gets reversed.
3. **Does it rank well with click-through well below the expected rate for its position, and lack the structural signals of an easily extracted page?** Restructure: the ranking works, the page does not. Usually the cheapest meaningful win on an established site: an hour or two against months for a new page to mature.
4. **Does it rank and plateau, with adjacent unanswered sub-questions at the same intent?** Expand: beats creating a new page when the queries share one intent, loses to creating when they do not.
5. **Everything else:** Leave alone, used often and stated explicitly. A page performing adequately with no accuracy problem and no structural defect is not improved by being rewritten, and the hours come from the same budget as everything else. Every leave-alone still appears in the tracker so the judgment is visible, not the page overlooked.

**Estimating** (planning defaults, not measurements; replace with this business's own tracker history once enough completed items exist, and say which is used):

| Treatment | Typical effort | Typical time to result |
|---|---|---|
| Refresh | 1 to 2 hours | Weeks |
| Restructure | 1 to 3 hours | Weeks |
| Consolidate | 2 to 4 hours plus redirects | Weeks, then a dip before recovery |
| Expand | 3 to 6 hours | 1 to 3 months |
| New page | 4 to 10 hours | 3 to 6 months |

Movement is commonly visible at 4 to 6 weeks; a verdict is not reliable before 8 and is final at 12 (a practitioner convention, not a documented rule: state it as such).

**Never recommend:** deleting a page with impressions or traffic, unless it is being consolidated and redirected (deletion without redirection throws away accumulated signal for nothing) · rewriting a page that is performing, on general principle or because it is old (age is not a defect) · treating an automated or feed-generated page the business cannot edit as a content-treatment candidate (that finding goes to the audit backlog as a template or indexation issue) · a refresh with no specific thing named to change ("update and improve" is not a treatment) · a rewrite during an unrecovered site migration, where the result cannot be fairly read.

## Handoff to the content pipeline
**Hand over what is specific to this piece. Hand over nothing the pipeline already holds.** The pipeline (research, structure, drafter, reviewer: `content-structure-strategy`, `content-seo-strategy`, `lifeos-workos-writing`, `humanizeai`) carries voice, entity facts, compliance rules, link inventories and writing patterns already, from EntityOS; restating any of it here creates a second copy that will drift. Where a handoff needs to reference something the pipeline holds, name it and point; never reproduce it.

**What travels, per item:** Type (new, refresh, restructure, consolidate, expand) · working title · target URL (existing pages only) · primary query and cluster members · search intent · **answer target** (the one question the opening passage must answer, written as a quotable sentence carrying a figure and its date) · audience segment · cluster and internal links, named · word-count range (set from intent and what is already performing, not a house default) · point of view · for existing pages, the specific change (never "update and improve") · source constraints (what must be verified before publication) · dependency tier and whether a second sign-off is needed · **baseline recorded: yes or no, with date. An existing page must not be changed until its baseline is in the tracker.**

**What never travels:** voice notes, tone guidance, style rules · entity facts, addresses, contact details, legal or regulatory positions · compliance requirements and disclaimers · internal-link inventories the pipeline already fetches · CTA phrasing · author bio and credential content · anything already in the pipeline's reference files. If the pipeline lacks one of these, that is a gap in the pipeline: note it as a suggestion for whoever owns it (core change control), never patch around it here.

**Completeness check before sending** (the brief completeness gate in `core-rules.md`, scoped to planning): POV stated or inferable · keyword block present · internal link targets named or the pipeline's own inventory confirmed sufficient · word-count range stated · for existing pages, the specific change named and the page accessible · answer target written as a sentence, not a topic · baseline recorded for anything touching a live page · approval tier flagged where required. Missing one or two: ask in one batched question. Missing more: not ready; say so.

**After handoff:** set the item's status to Briefed in the tracker. It leaves planning's scope until it returns as published, at which point it enters the results loop for its scheduled readings. **Do not follow it into production**: reviewing a draft or adjusting copy is the pipeline's work; doing it here creates two owners for one piece and conflicting instructions to whoever is writing.
