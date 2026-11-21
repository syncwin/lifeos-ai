# Task Store Field and Column Guide

Field guide for the one LifeOS task store (`${CLAUDE_PLUGIN_ROOT}/references/tracker.md`), read by `lifeos-work-sprint`, `lifeos-work-report`, `lifeos-work-log`, `lifeos-work-results` and `lifeos-work-demand`. There is **one store**: no second workbook, no parallel spreadsheet, no side list. Business facts (conversion definition, reader, naming) come from LifeOS entity data (`search_context`). Where the owner already keeps a spreadsheet, it is an import or export of this store, mapped once, with the mapping kept in LifeOS entity data (`search_context("task store column mapping")`); it never becomes a second source of truth. The file name of any export is never renamed once created.

Contents: where each kind of record lives; plan item columns; findings fields; readings and snapshots; row caps; write discipline; durable record.

## One store, one sprint
All work (content and web or ops, every business unit) is rows in the same store, and there is **one sprint**: a sprint row plus plan items. A row for content work carries `owner_skill = content` and is executed by handing the work to the content pipeline, which reports back; the day close fills only its production and result columns on rows completed that day. A second sprint, or a second plan, anywhere is a defect: the operator has one working day. A business with only content work, or only web work, in scope uses the same store; the kind column keeps the boundary visible.

## Where each kind of record lives
| Record | Store table | Notes |
|---|---|---|
| Scored candidates (one per cluster, including every `Do Not Create` row with its reason) | `plan_items`, `kind = opportunity` | Promoted to content items by setting `kind` and `status`; never copied |
| The one content queue: existing-page treatments and new content | `plan_items`, `kind = content` | Carries `dependency_tier`, `gated_on`, `conversational_queries` (or an equivalent search-intent field) |
| Site, entity and conversion-path fixes | `plan_items`, `kind = web` | Findings converted into tasks |
| Keyword and query map | `plan_items` rows linked by `item_id` | Every keyword or query maps to exactly one item id |
| The sprint | `sprints` plus its `plan_items` | One per week |
| Work done, evidence | `log_entries` | Sprint log: what happened, status, actual time, discoveries |
| Settled calls | `decisions` | So later runs stop re-deriving them |
| Open-questions queue | `questions` | `${CLAUDE_PLUGIN_ROOT}/references/core-rules.md` |
| Evidence rows | `findings` (append-only history) | Field list below |
| Per-page performance readings, baselines, AI-visibility readings | `readings` (append-only history) | `metric` distinguishes page metrics from Cited and Named counts |
| Dated rollup numbers | `snapshots` (append-only history) | Never overwritten |
| Day reports | `day_reports` | One start and one end per working day |

## Plan item columns (beyond the key columns in `tracker.md`)
| Column | Standard |
|---|---|
| kind | `opportunity`, `content` or `web` |
| owner_skill | `content` when handed to the content pipeline, else blank |
| dependency_tier | CORE, OPT-APPROVAL or OPT-DEV (`${CLAUDE_PLUGIN_ROOT}/references/core-rules.md`) |
| gated_on | Task ids, or blank; blank means Tier 0, eligible for the next sprint |
| expected_outcome | Written before the work starts |
| outcome / verdict | Filled at the reading date; a complete row past its reading date with no outcome is flagged |
| actual | Hours, used only for calibrating estimates, never reported as the achievement |
| baseline_recorded | Date, or blank; an existing page must not be changed until it is set |
| reading_due | The date the first reading is owed |

A user-owned store may name these differently; map once in LifeOS entity data. Columns beyond `tracker.md`'s key columns are added once by the store owner; until then the value goes in the row's text.

## Findings fields
Every `findings` row carries all of these, or it is an observation, not a finding:

| Field | Standard |
|---|---|
| Finding | One sentence, specific: "H1 missing" qualifies, "on-page issues" does not |
| URL / Location | The specific page, or `site-wide` |
| Band and severity | Priority band and severity, kept as separate axes (core rules, rule 6) |
| Figure, Window, Source, Date | Evidence provenance; a row that cannot fill these is an observation |
| Lead/conversion link | How this reaches the business's conversion definition (LifeOS entity data). Cannot fill it: **Low by definition**, not a judgment call |
| Effort | Hours or minutes |
| Fix | Location, instruction, done-test, named for the actual tool or CMS in use |
| Dependency tier | CORE / OPT-APPROVAL / OPT-DEV |
| Gated On | Task ids, or blank |

Sort findings by band, then dependency tier, then severity, then effort ascending. **Every OPT-APPROVAL finding opens a `questions` row** naming the decision owed and what changes with each answer: a finding that needs a decision with no question row will sit untouched. Nothing appears in both a finding and its task row: the task holds the work, the finding holds the reasoning.

## Readings and snapshots
`readings`, `snapshots` and `findings` are **append-only**: a row that overwrites the previous one destroys the only trend line the system has. Every capture is a new dated row, never an edit to an old one. Baselines are readings flagged as baseline, captured before a live change.

## Row caps and actionability
Keep each view to what is actionable this cycle: a store with 300 "someday" rows stops being read. A row is actionable when it names the specific page or item, what is created or changed, and the condition that makes it done. "Write about X" and "Improve the homepage" are not actionable rows.

## Write discipline
- The store is written **once a day, at the day close** (Close Week folds into the last Close Day), never mid-day and never per task. Mid-day work goes to `log_entries` and the sprint log; plan item status changes at close.
- Write order and parameterised writes follow `${CLAUDE_PLUGIN_ROOT}/references/rules.md` (Task store) and `tracker.md`; rows are edited in place, never rebuilt from a fresh export.
- A store, view or export is never renamed once created.
- Headings in any export stay Title Case.
- Read the store first: sprint and planning stages load the current store data before planning, and a stage that cannot load it stops and says so instead of planning from memory, because tasks missing from the plan are silently dropped.

## Durable record
There is no prose strategy document: what would sit in one is a finding with its evidence in its own columns. Reports, briefs, research and drafts are Markdown working deliverables and are not the durable record; the durable record is the store.
