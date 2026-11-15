# Workbook and Tracker Specification

Business-agnostic spec for the durable work record. Read by `lifeos-workos-sprint`, `lifeos-workos-report`, `lifeos-workos-log`, `lifeos-workos-results` and `lifeos-workos-demand`. Where the owner keeps the record in the LifeOS task store (`lifeos/references/tracker.md`), the tabs below map to its tables and views once, and the mapping is kept in EntityOS (`search_context("task store column mapping")`). Where the owner keeps spreadsheets, the file names come from EntityOS (`search_context("file naming rules")`); this spec fixes the structure, not the names.

## Two workbooks, one business
| Workbook | Owns |
|---|---|
| Content workbook | Opportunities, Content Tracker, Content Findings, Content Snapshot, Keyword Map, its own Decisions and Questions tabs |
| Web workbook | Web Tracker, **the one Sprint tab**, Web Findings, Web Snapshot, Page Readings, AI Visibility, its own Decisions and Questions tabs |

**There is one sprint, and it lives in the web workbook**, even though it carries tasks from both. A row tagged `Owner Skill: Content` in the Sprint tab is executed by handing the work to the content pipeline, which reports back; the web workbook's day close fills only the production and result columns on rows completed that day. A Sprint tab in the content workbook is a defect: it means a second sprint exists, and the operator has only one working day.

A business with only content work, or only web work, in scope still gets both workbooks created empty instead of skipped: the boundary stays visible even if one side is idle.

## Standard tabs
| Tab | Lives in | Purpose |
|---|---|---|
| Opportunities | Content | Scored candidates, one row per cluster, including every `Do Not Create` row with its reason |
| Content Tracker | Content | The one queue: existing-page treatments and new-content items, `Status`, `Dependency`, `Gated On`, `Conversational Queries` (or an equivalent search-intent field) |
| Keyword Map | Content | Every keyword or query mapped to exactly one tracker row's ID |
| Web Tracker | Web | Findings converted into tasks: site, entity and conversion-path fixes |
| Sprint | Web | The one weekly and daily operating cadence, across both workbooks |
| Page Readings | Web | Dated performance snapshots per page, append-only |
| AI Visibility | Web | Dated AI-assistant citation readings, append-only |
| Findings (one per workbook) | Both | Evidence rows; field spec below |
| Snapshot (one per workbook) | Both | Dated rollup numbers, append-only, never overwritten |
| Decisions (one per workbook) | Both | Settled calls, so later runs stop re-deriving them |
| Open Questions (one per workbook) | Both | The open-questions queue (`lifeos/references/core-rules.md`) |

## Findings row: required fields
Every Findings row carries all of these, or it is an observation, not a finding:

| Field | Standard |
|---|---|
| Finding | One sentence, specific: "H1 missing" qualifies, "on-page issues" does not |
| URL / Location | The specific page, or `site-wide` |
| Band and severity | Priority band and severity, kept as separate axes (core rules, rule 6) |
| Figure, Window, Source, Date | Evidence provenance; a row that cannot fill these is an observation |
| Lead/conversion link | How this reaches the business's conversion definition (from EntityOS). Cannot fill it: **Low by definition**, not a judgment call |
| Effort | Hours or minutes |
| Fix | Location, instruction, done-test, named for the actual tool or CMS in use |
| Dependency tier | CORE / OPT-APPROVAL / OPT-DEV |
| Gated On | Task IDs, or blank; blank means Tier 0, eligible for the next sprint |

Sort findings by band, then dependency tier, then severity, then effort ascending. **Every OPT-APPROVAL finding opens an Open Questions row** naming the decision owed and what changes with each answer: a finding that needs a decision with no question row logged will sit untouched.

## Row caps and actionability
Keep each tab to what is actionable this cycle: a tracker with 300 "someday" rows stops being read. A row is actionable when it names the specific page or item, what is being created or changed, and the condition that makes it done. "Write about X" and "Improve the homepage" are not actionable rows.

## Snapshot discipline
**Snapshot tabs are append-only.** A row that overwrites the previous one destroys the only trend line the system has. Every capture is a new dated row, never an edit to an old one.

## Write discipline
- Edit trackers in place (for example with a spreadsheet library), never rebuilt from a fresh export.
- Trackers are never renamed: an existing tracker keeps its exact original file name through every update.
- Trackers are written **once a day, at the day close**, never mid-day and never per task.
- Every heading inside a tracker stays Title Case.
- Nothing appears in both a Findings row and its corresponding tracker row: the tracker holds the work, Findings holds the reasoning.

## Durable record
There is no prose strategy document: what would sit in one is a Findings row with its evidence in its own columns. Reports, briefs, research and drafts are Markdown working deliverables and are not the durable record, which is the two workbooks (or the task store tables they map to).
