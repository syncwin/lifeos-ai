# Execution Playbook and Day Reports

Method for `lifeos-workos-sprint`, also read by `lifeos-workos-report` and `lifeos-workos-log`. Business facts (working days, capacity, reader, conversion definition, platform) come from EntityOS (`get_context`, `search_context("working hours, capacity, owners per task type")`, `search_context("audiences, report headings, tone")`). Shared rules: `lifeos/references/core-rules.md`.

Contents: one sprint; cadence versus measurement; outcome not hours; before starting and sizing; commitment; shape; Plan Week; sequencing; dependencies; sprint record; exclusions; estimating; content boundary; execute a task; update; deliverables by stage; non-negotiables; day reports (Open, Close).

## One sprint across every business unit
There is one sprint, across all units and both kinds of work (content and web/ops). A second sprint anywhere is a defect: the operator has one working day and cannot run two. Upstream stages decide what to do; this one does it and records it.

## A sprint is a delivery cadence, not a measurement window
A sprint (commonly one week) is how work gets committed and shipped. Results run on a slower loop (commonly 8 to 12 weeks), so a sprint reports what was finished and can never report whether it worked. The sprint reports output; the results reading reports outcome, on its own schedule. A sprint that ships good work into a market that has not responded yet is still a successful sprint; say so plainly.

## Outcome, not hours
Hours are an input, never the report. The measures, in order: (1) what shipped, named, with its done-when condition met and verified; (2) what it should move, written before the work starts as an Expected Outcome; (3) what actually moved, filled in at the reading date as the Outcome or Verdict; (4) whether it reaches the business's conversion definition. A shipped item with no stated reason it matters was low severity and should not have outranked one that had one. **A close report that leads with hours has failed the standard.** Hours belong in an `Actual` field for calibrating future estimates, and nowhere else.

## Before starting
Load the business record, the task store, the sprint log. Read Decisions in the store and merge the open-questions queues: a task whose approach is already settled is not re-derived at execution time. Live fetches often fail, so every validation step that needs live state asks for a specific check (URL inspection, screenshot, view-source) instead of inferring.

## Before sizing
Ask two things every cycle, batched: which days this cycle are confirmed working days, and which tasks the operator wants included (never assume last week's schedule repeats). The operator chooses; this stage proposes in priority order and never assigns. **A day off announced ahead of time never becomes a workday in the file, even if work happened that day**: the record reflects what was asked, not what happened to occur. Content throughput is commonly one piece a day start to finish, so a week of six confirmed days is six pieces at the absolute ceiling, which is why the commitment rule matters more than raw hours arithmetic.

## Commitment
Commit roughly 65% of nominal hours as a starting convention, not a measured constant and adjustable. The remainder absorbs what always happens: an undocumented platform quirk, something that breaks mid-fix, a request arriving mid-week. **After three or four cycles, replace it with this business's observed throughput** (from the `Actual` field) and say in the report which figure is used. A sprint that is always fully committed always fails, and a plan that always fails stops being read as evidence of work.

**Work in progress is capped at two items**, not two per day: two at a time; lead time grows with the number in flight. **At least one committed objective must start and finish inside the cycle and produce something visible** (a live page with a corrected passage, a corrected listing, an event firing, a piece published). If everything committed is long-horizon, split something: a multi-cycle item almost always has a first slice that stands alone. **Both kinds of work (content and web/ops) are represented every cycle**: one kind alone stalls the other, and the deferred kind (entity and tracking fixes especially) compounds silently under everything else. Where a cycle must be one-sided, say so and why.

## Shape
One objective is one clear objective and it finishes something: never two folded into one, never a minor action dressed up as an objective. Each objective is self-contained and carries every subtask needed start to end. Two main objectives per working period is a reasonable default. Subtasks are numbered under their parent (3.1, 3.2) so they paste into a planner. Objective names are unique and **objective numbers stay stable across the cycle**, even out of day order. An alternative to a gated objective is a regular numbered objective with "(alternative)" after its name, never a separate alternatives section.

## Plan Week
Re-runs strategy against current data instead of re-planning leftovers. Pull open items from the planning stage (`lifeos-workos-demand`) and from audit and results findings; size them against the confirmed working days and hours of this cycle.

## Sequencing
Ordering is not just priority: some work makes other work pointless if done out of order.

**First, dependency tier** (core rules): everything with an empty `Gated On` is Tier 0 and fills the cycle first because it cannot stall; Tier 1 is whatever Tier 0 unblocks, sequenced right behind the task that clears it; Tier 2 follows; anything waiting on a person sits Blocked with its question row and enters the next cycle once answered.

**Then, within a tier:** measurement before optimization (with no verified conversion tracking nothing downstream can be proven to have worked); blockers before improvements (an unindexable page does not benefit from better copy); existing items before new ones where the existing item already has real reach; entity and consistency fixes early and once (cheap, one-time, they compound, and they are the work most likely to be deferred forever because nothing visibly breaks); content growth never omitted, prioritized by importance, not treated as a lower category; fit with the ideal customer as the tiebreaker.

## Dependencies and the question queue
Every subtask carries CORE, OPT-APPROVAL or OPT-DEV. **No CORE subtask depends on an OPT one**: where one does, split until the CORE half stands alone. Every OPT subtask names an alternative of similar value that runs if the dependency does not clear in time, and opens a question row one working period before it becomes active: flag approval-tier items at planning time, not when execution reaches them, because a fix reversed after publication costs more than the question would have. **Batch developer requests into one handover per working period**, as its own block. Group related small fixes into one scoped request: twenty tickets for twenty instances of one template fault get triaged as twenty low-priority tickets; one scoped request for the template gets done.

## What the sprint record holds
Objectives, subtasks, task numbers, dependency tags and tiers, estimates, expected outcomes and done-when conditions. Nothing else: evidence, diagnosis and why-it-matters live on the task-store row and the source document; a second copy drifts.

## Exclusions
What was excluded from a cycle, and why, goes into the chat reply at planning time, including anything displaced by lost time. Anything material becomes a Decision. Without this, no one can tell what was rejected from what was simply missed.

## Estimating and carry-over
Estimate from the store's own effort history; where none exists, estimate conservatively and mark it unvalidated (a confident unvalidated estimate is how a plan loses credibility). Unfinished work carries forward with its original task number and a revised estimate, never reset to zero. **An item carried two consecutive cycles is flagged for an explicit decision: commit it or kill it.** Silent carry-over fills a backlog with things nobody intends to do; killing it is a legitimate answer and goes to Decisions with its reason.

## The content boundary
A row tagged as a content task is handed to the content pipeline (`content-structure-strategy`, `lifeos-workos-writing`, `humanizeai`), not executed in the sprint:

| Belongs in the sprint | Goes to the content pipeline |
|---|---|
| An answer block replacing an opening paragraph | A full page or post, new or rewritten |
| A title or meta rewrite | A brief, outline or research report |
| A heading restructure on an existing page | Anything needing brand voice or compliance review |
| An internal-link pass | Anything that changes what a page argues |
| A corrected figure in existing copy | A cluster, calendar or treatment decision |

Handing off is not leaving the sprint: the row stays in the sprint, its status is tracked here, and the day close records its outcome like any other.

## Execute a task
1. Read the task in full: what to do, done-when, dependency tier, gated-on, question reference, evidence needed. Where `Gated On` names an unresolved task, say so and run the named alternative.
2. **Check the dependency tier before producing anything:** CORE executes directly; OPT-APPROVAL produces the deliverable plus the exact question for the decision owner, filed to the queue, and does not go live; OPT-DEV produces a developer handover instead of a direct edit.
3. Verify current state before changing it: a fix applied to something already correct destroys confidence in every other row.
4. **Produce the deliverable itself**, not a description: the literal corrected text, the literal structured-data block, the literal redirect table.
5. Verify every figure against its primary source before it enters published copy.
6. Validate against "done when" literally, name what the operator has to check and what a pass looks like.
7. **Record a baseline before any change to a live page** and set the reading date. Without one, the results loop can only return Unmeasurable.
8. Append to the sprint log: what happened, status, actual time, anything discovered. Not to the task store.

## Update
Records a mid-sprint change (a new task, a changed priority, a resolved blocker) without waiting for the day close. It still does not write the task store.

## Deliverable by workflow stage: produce the thing, not a description of it
"Add the structured-data block" is a task; the deliverable is the actual markup, ready to paste.

- **Technical fixes:** the exact setting, its exact location, current value and new value, named for the actual platform or CMS in use. Template-level changes are fixed once at the template, not per page. **Where it touches theme or platform code, the database or hardcoded output, it is OPT-DEV**: produce the developer handover, not the edit. State the validation step (a live inspection tool, a re-crawl, a response-header check).
- **On-site content fixes:** the literal corrected copy: an answer block written to the writing rules (`lifeos-workos-demand/references/cluster-and-treatment-model.md`, six content rules), every figure verified against its primary source before it goes in, questions as real headings, the business's own name in body text, internal links named both directions. **Record the baseline before it ships.** Scope boundary: an answer block, a title or meta fix, a heading restructure, a link pass or a corrected figure belongs here; a full page or post goes to the content pipeline.
- **Entity fixes and listings:** corrected field text, ready to paste, grouped by property (a consistency sweep). Where no login exists, this is a copy-supply task, complete when the text is delivered, not when the profile changes. Verify the live value first; ask for a screenshot where it cannot be checked directly.
- **Analytics and tracking fixes:** the configuration spelled out (variables, triggers, tags named consistently, each event carrying the page path as a parameter, no personal data in parameters). **Check the consent position before any tag goes live.** Validation is always a real trigger test, never configuration alone.
- **Off-site and social fixes:** the bio, about or profile copy as text, written per platform, not pasted identically everywhere.

**Developer handover format**, one scoped request written for someone who has never seen the audit: Objective (the outcome) · Technical requirement (what changes, precisely) · Affected URLs or templates (scope, with counts) · Acceptance (the condition that makes it done, and how to check it) · Not in scope. Group related fixes into one request.

**Approval items:** an OPT-APPROVAL task produces two things: the deliverable, ready to go, and the exact question the decision owner has to answer, phrased so it can be answered in one line. Nothing goes live first. Where the item has a running alternative, say which one is active meanwhile.

**Validation, every task:** read the done-when condition literally and check the deliverable against those exact words, not the spirit of the task; name the verification artifact the operator has to produce where live state cannot be checked directly; state what a pass and a fail look like; where a task cannot be validated, record it as unverified, not complete.

**When to stop and ask** (inside the question budget: one batched message, three questions at most, each naming what it unblocks): a gated task is still unresolved; a figure cannot be verified against a primary source; live state cannot be established and the fix depends on it; the task contradicts a logged Decision, a stated freeze or another instruction. **Escalate; do not silently choose.**

## Non-negotiables
- Recommend and produce, never publish.
- The task store is written once per working day, at the day close, never during the day, never twice.
- Never rename a tracker or task-store export.
- Never write a page in the sprint: content rows are handed over, not absorbed.
- Never mark a task complete without its verification artifact.
- Never skip the baseline on a live-page change.
- Never invent a figure to fill a gap: an unverifiable number blocks the deliverable and is named as the blocker.
- Never re-litigate a settled decision at execution time.
- Never let a sprint stall on one unanswered question: the named alternative runs, the question stays open.
- Never turn a stated day off into a workday, even if work happened that day.
- Every file written follows the naming rules from EntityOS (`lifeos/references/core-rules.md`, File naming); the brand's full real name appears in anything an end reader sees.

## Day reports: two files, one at each end of a working period
Markdown, presented in the reply. **Neither carries hours as an achievement.** The Open report goes to whoever runs the day; the Close report goes to the reader the business record names. Close Week folds into the last working day's Close: the week's outcomes against the plan, and what carries forward.

### Open (start of period)
Built from the sprint record and the open-questions queue, merged across both kinds of work. Its job: make the period startable with no decision needed and workable without returning to the store; every task carries its own context, steps and checks.

```markdown
# Open: [date]

## Doing today
1. [Obj no] [Objective] · [Unit/property] · [Content or Web]. Done when [condition].
   Should move [expected outcome]. [Est]
2. [...]

## Questions
1. [Question]. Unblocks [task no]. Needed by [date]. [What changes with each answer, one line]
2. [...]

## Blocked, not touching today
| Task | Waiting on | Since | Alternative running instead |

## Carried in
[One line per item carried from last period, with its revised estimate.]

## Task plan
### [n]. [Task no]: [Task name] ([Est])
**Context.** [What is wrong, the evidence with date and source, why it matters for the goal.]
**Steps**
- [ ] [Exact action: setting, URL, ID, value, or wording to use]
- [ ] [...]
**Done when:** [the check that proves it, and the artifact to keep]
**Watch out:** [the one trap that would break it; omit if none]
**Log line:** `[date] | [task no] | [what was done] | [status] | <actual> | [evidence]`
```

Two or three questions at most, drawn from the queues of both kinds of work together, going out one working period ahead of the task they unblock. **Every one names a task number**: a question with no task number is not asked. Everything under "Doing today" is Tier 0 or already unblocked; an item still waiting on an open question appears under Blocked with its alternative named. Where nothing is blocked and no question is due, write `None` in one word instead of dropping the section: its absence should read as a state, not an omission.

### Close (end of period)
Carries finished work and nothing else: tight and scannable. Base it on the operator's own final work report where supplied; otherwise on tasks actually marked complete, using their names from the working log. **Never invent an item, never promote an in-progress item to done, never restate an objective name as though it were an outcome.**

```markdown
# Close: [date]

[Workstream]

1. [What was done, and what it produced or proved]
2. [Next item]

[Next workstream]

1. [...]

## Now measurable
[Task no, what shipped, and the date its reading is due. Only items that changed
a live page or a live setting. Omit the heading entirely if there are none.]
```

Workstreams are named for the thing being worked on, not for a tracker category ("Post-Migration Redirects", not "Technical Fixes"). One sentence per item: what was done, then the figure or outcome that proves it.

| Weak | Strong |
|---|---|
| Fixed the redirects | Rebuilt and imported the corrected table at 189 rules, every target mapped to a current URL, nothing deleted |
| Worked on internal links | Applied 70 link pairs across every relevant page, with the remaining 117 carried forward |
| Tried the suggested fix | Attempted the suggested platform change, which returned errors on unrelated pages across several variations and was rolled back |

**A failed attempt counts as completed work when it closed off an approach**: it cost time and changes what happens next; say what was tried, what it did, and that it was rolled back. Partial work is reported with its remainder on the same line.

**Rules:** report only work actually completed (no carried items as their own entries, no planned work, no displaced work) · use objective and subtask names exactly as logged, no added interpretation · never turn a stated day off into a workday · never report hours as the achievement (they belong in `Actual`) · no preamble, no wrap-up, no unrequested explanation.
