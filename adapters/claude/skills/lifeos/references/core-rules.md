# Work core rules (shared)

Shared once for every WorkOS stage and for the plugin handoffs in the router. Brand-agnostic: every business fact (names, addresses, contact routes, voice, constraints, regulators, who reads the output, conversion definition, tools, capacity) is read at run time from EntityOS with `get_context`, `get_policy` or `search_context`, never from a skill. Where this file says "business record", it means those EntityOS reads for the active brand. Approvals, evidence labels and the task store stay canonical in `rules.md` and `tracker.md`.

Contents: the seven rules; token and effort discipline; clarification gate; brief completeness gate; companion plugins; dependency tiers; open-questions queue; absorbing outside items; file naming; change control; file precedence; what is never invented; compliance and sourcing; stage boundaries; handoffs to installed plugins; file organizing.

## The seven rules
1. **Recommend and produce, never publish.** No writes to a website, listing, directory, social profile or CRM, even where credentials exist. Every fix ships as location, instruction and done-test, named for the tool in use. Where no login exists, the deliverable is corrected text to paste, logged as a copy-supply task.
2. **Ask before spending paid credits.** Name the report, why free data cannot answer it, and the cost. Wait for approval (`risk-check.md`). Never bundle several paid pulls behind one approval.
3. **Ask inside the budget.** One batched message per stage, three questions at most, each naming what it unblocks and what changes with the answer. A question that cannot state both is not asked: assume instead and write the assumption into the output.
4. **Evidence standards apply everywhere.** Segment by the business's actual market, use equal comparison windows (normalize unequal windows to a per-day rate; a 76-day window against a 42-day window understates the second by about 45% on raw figures), label estimates as estimates, never invent a statistic, correct a superseded finding instead of annotating around it.
5. **Read the tracker first, update it at close.** One task store per active engagement; the store plus the sprint log are the whole durable record. Write it once a day, at close, never mid-day: a mid-day write describes intentions, and readers take it as fact.
6. **Priority, severity and dependency are three separate axes.** Never collapse them into one score: a low-severity item can be top priority if it blocks everything else. A tool's own severity rating is input, never the answer: a hundred low-value warnings do not outrank one broken contact form.
7. **Leave every file tighter than it was found.** Fix a stale reference, dead link or contradiction you notice, even if it is not the stage's main job.

## Token and effort discipline
- Load only the reference the current stage needs; the SKILL.md says which covers which situation.
- Sample, do not crawl: homepage, top five by impressions, top five by clicks, one per page template, plus anything flagged. A pattern across a template is one template finding, not twenty page findings.
- Read tabular exports (CSV, TSV, XLSX) directly; never route them through a markdown-conversion tool, which is for PDF, DOCX and HTML.
- Stop when the answer is decided. More evidence for a settled conclusion is spend without output.
- Cap the output, not just the input. A length ceiling in a skill is a limit, not a target.

## The clarification gate (before every stage)
Clarify first, execute second; never proceed with unresolved requirements. Run it again at each stage, not once per session: clearing it for drafting does not clear it for review.
1. Check that everything the stage needs is present and understood.
2. Identify what is missing, unclear, contradictory, or a decision that is not yours.
3. Ask only those questions, batched in one message, and wait.
4. Confirm the stage now has what it needs, then start.

Never: guess a missing input; start on incomplete requirements; write the content and park unresolved issues as open questions at the end; finish a stage and redo it after clarification.

**Do not ask** what the business record already settles (entity names, addresses, the CTA convention, voice). Looking it up is the answer. **Do ask** about: an absent required input; two instructions that contradict each other (including a self-contradicting brief); a fact with no authoritative source; a scope or angle decision nothing else settles; anything where guessing would put an unverifiable claim into published content. Contradictions are raised, never silently resolved: picking the more sensible of two conflicting instructions hides the conflict from the person who could fix it at the source.

## Brief completeness gate (before a brief goes to drafting)
Check mechanically, in one pass, before handing a brief to the drafter:
- [ ] POV is stated or inferable (second person, third person or team voice).
- [ ] A keyword and topic block exists (primary and secondary terms).
- [ ] Internal-link opportunities are listed, even loosely.
- [ ] A word-count target or range is stated.

Missing one or two: ask in one batched question. Missing more: the brief needs building properly first; say so instead of proceeding thin.

## Companion plugins and what to do if missing
| Plugin | Role | If it is not installed |
|---|---|---|
| `humanizeai` (router of the humanize plugin) | Runs at three checkpoints: per section while drafting, over the full document before handoff, and verified before compliance review | Say once that it is required and name it, then apply the enforceable subset in `lifeos-workos-writing/references/writing-standards.md` and record the substitution in the review scratchpad. Never fake a pass that did not run. |
| `markdown-converter` | Converts a non-Markdown upload (PDF, DOCX and similar) before anything else touches it | Say the same, read the file with whatever document tooling exists, carry on. |

Say it once, at the start of a run. Never fabricate the output of a plugin that is not there. Always run `humanizeai` in full; never restate or summarize its internal categories in LifeOS files; point to it by name and invoke it, so this plugin does not drift from it.

## Dependency tiers (for any task or fix)
| Tier | Meaning | What happens |
|---|---|---|
| CORE | No approval or developer needed | Executed directly |
| OPT-APPROVAL | Needs a business decision first | Deliverable produced plus the exact question for the decision owner, filed to the open-questions queue; does not go live until answered |
| OPT-DEV | Needs a developer or platform change this system cannot make | A developer handover is produced instead of a direct edit |

A task with `Gated On` blank is Tier 0 and can start today, which makes it eligible for the next sprint. A task gated on another task or an open question says so plainly instead of being worked around.

## The open-questions queue
Separate from the per-stage question budget, on its own cadence, for anything that blocks a task without blocking the current stage.
- Two or three questions per cycle, raised one working period ahead of the task they unblock.
- Each logs the question, the task it unblocks, what changes with each plausible answer, when the answer is needed, and the answer once given. A question with no task attached is not logged.
- An answer becomes a decision entry the same day and the task moves from Blocked to Not Started.
- If the answer misses its needed-by date, the task's named fallback runs and the question stays open. A sprint never stalls on one unanswered question.
- **Who reads this:** the business record names who reads the output (operator, internal manager or external contact) and their reading style (outcomes or activity, technical or plain). Every report, approval request and question queue is written for that named reader.

## Absorbing outside items
A task list, a colleague's idea or the operator's own note does not become a task by being written down. When one arrives outside a stage run (also `lifeos-workos-intake`):
1. Map it onto existing task-store items first.
2. Count what is already tasked, what is new, and what conflicts with something planned.
3. Escalate contradictions; never silently choose.
4. Never run a second, parallel task list next to the store.
5. Anything that is another stage's job is forwarded there in one line (a content idea during a site audit goes to the opportunities list, not the audit's findings).

## File naming and publishing identity
File prefixes, document-name patterns and any approved short form of the brand come from `search_context("file naming rules")`; never invent a per-brand abbreviation. A document-type vocabulary (SOP, DOC, PLAN, REF, RECORD) and no dates in file names (dates go in the file header) are the defaults when EntityOS names none. A business-unit file carries that unit's short code from EntityOS in its title; a whole-business file carries none. **Published content always uses the brand's real name; an internal short form never appears on a live page, in a meta title, or in anything an end reader sees.** A leaked abbreviation is an entity-consistency defect, not a style choice: flag it like any compliance issue. Keep one file registry listing every active file (see File organizing below).

## Change control
These skills do not update, version-bump or repackage themselves in use. A real gap is a one or two sentence suggestion for the package owner (`rules.md`, Core change control), never a direct edit, and approval from whoever runs the session is not authorization to change the installed package.

## File precedence when two sources disagree
1. The content brief for the piece (always wins, including structure and sections).
2. Verified entity facts from the business record (`get_context`, `get_policy`); they override everything else on any point they cover.
3. The stage skill running now: its mechanics complement the brief and entity facts, never override them.
4. A business-unit record: authoritative for that unit's market, tools and site specifics.
5. Brand voice from EntityOS: governs tone, never structure.
6. Persona or audience records: authoritative for audience, credentials and shared resources.

The higher source wins; the lower one is wrong and gets fixed, not worked around. Raise a contradiction instead of resolving it silently.

## What never gets invented
Anything about how the business operates comes from the business record or it stays out of the output: entity names, addresses, contact routes, which tracking tools are live, who receives customer data, how a reader opts out or requests deletion, whether calls are recorded, what a lead form transmits, where reviews come from, what the product or listing feed is. Negative facts matter as much as positive ones: a cookie banner, a chatbot or an automated unsubscribe the business does not have is exactly what gets invented when a field is left blank instead of marked "none". Reading an entity fact off a URL, a directory or an old page instead of EntityOS is the same error as inventing one: a different address found in the wild is a defect to report, not a source to trust.

## Compliance and sourcing
Rules about regulators, required clauses, disclaimers, jurisdiction scope, the closed list of allowed sources and the fabricated-source test are owner policy. Read them with `get_policy` / `search_context("compliance and sourcing rules")`; if EntityOS holds none, ask once and offer to store the answer. Regulated-industry language stays verbatim where EntityOS names required clauses, and brand voice never applies to those clauses. Competitor pages are never a factual source.

## Stage boundaries
- **Goal:** leads or conversions from the business's actual ideal customer. A page that ranks and reaches nobody in the target audience is not a win. Conversion potential travels on its own scale at every stage and is never blended into a traffic or visibility score.
- Opportunity scoring (`lifeos-workos-demand`) never assesses site health, diagnoses a decline, sequences or plans, or writes copy. Planning never scores keywords, audits, or writes briefs or copy. Results (`lifeos-workos-results`) never runs a checklist audit, scores keywords or plans content. The sprint (`lifeos-workos-sprint`) never re-audits, re-diagnoses, writes a page or publishes. The writing check never drafts from scratch; it verifies and drives targeted fixes.
- A finding that fits two stages belongs to the one whose question it answers: a missing H1 is an audit finding; why clicks fell is a results question; the literal replacement heading is a sprint deliverable; whether a page is worth writing is the demand and planning call.
- Where a request spans several stages, sequence the handoffs explicitly and say so; never silently collapse two stages into one output. One stage runs at a time unless the user asks for chaining. The exception: a research, brief, draft, review chain runs on without prompting, stopping only at an essential-questions gate that needs the person's own answer.
- After any stage that creates, renames or rewrites a file, and always after a day close, do a quick file-organizing check (below).
- Unknown business: if no business record exists yet in EntityOS for the brand implied, offer to create one with `lifeos-entityos` (identity, voice, audience, sources, constraints, conversion definition, writing patterns) before any content or web stage. Never infer one brand's answers from another's. Detect the active brand from a domain, sitemap URL or hostname via `search_context`; never ask which brand if it is derivable.
- Non-Markdown upload: run `markdown-converter` first, before any other step.

## Handoffs to installed plugins (what to pass and rules that travel)
Pass brand context from EntityOS (`get_context`, `search_context`) to the plugin; if the plugin is not installed, say so and name it. The routes are in the router's routing table. Rules carried over from the retired strategist that apply to those handoffs:

**Research before a brief (`content-structure-strategy`).** Two modes. Brief-scoped (a brief exists): research stays strictly inside the brief's headings and keywords, in order. Research-first (no brief): an essential-questions gate runs first and nothing is searched before every answer is in: target property or unit, page type, topic and optional primary keyword ("you choose" is recorded as an assumption), geographic or jurisdictional scope, primary audience, must-include and must-avoid plus competitor URLs and pages not to cannibalize. Do not ask what research itself answers (subtopics, FAQs, gaps) or what the business record holds. The output is research only; writing, tone, SEO or publishing directions found in a supplied brief fall outside it. Claims need support: each is verified every statistic, date, regulation, ranking or distance against an allowed source, cross-checked with a second source, conflicts are reported instead of picking a number, and an unverifiable item is marked a Research Gap instead of being filled. Capture full citation metadata (publisher, exact page or report title, publication date). Fact table columns: Section, Claim Needed, Sourced Fact, Publication, Page Title, Published Date, URL, Confidence, Notes. Competitive gap analysis (supplied competitor URLs first, else the current top 3 to 5 results) covers structure, coverage, intent, credibility, localization and recency, never as a factual source; output a SERP synthesis, a gap matrix and 3 to 5 priority gaps. Stop when every section has enough verified evidence. A research-first run stops at the Research Report; the brief is the next step.

**Briefs and on-page SEO/AEO (`content-structure-strategy`, `content-seo-strategy`).** Build a brief from a Research Report (proposed sections become body, the question space becomes FAQ, assumptions stay visible); notes with no research go to research first; an approved brief is revised in place with the delta stated on top; a legal or compliance page reads entity facts first and nothing may read as pending. Page type sets the structural default (legal follows required clauses verbatim, commercial leads with the conversion action, a blog post leads with the reader's question, a comparison leads with the options table). Heading labels (`H1:` to `H4:`, or an explicit block label) are mandatory in a brief and render as real headings, never as visible text. Tier keywords from the keyword map: protect terms in title, H1 and opening; striking-distance terms in an H2 and the answer capsule; coverage gaps get their own section or FAQ; question-form terms become an H3 or FAQ with a short direct answer; never target a term mapped to another item or excluded. Mechanics: entity-attribute-value phrasing in the capsule, a named schema type per page type, 2 to 4 internal-link anchors drawn from the target page's topic, meta title and description to the business's limits. The brief outranks the drafting defaults for that piece.

**Site, entity and conversion audit (run by LifeOS: full method in `lifeos-workos/references/audit-methods.md`; `content-audit-strategy` only for a whole-site content inventory from exports).** Three independent modes, run whichever applies: site (index status, architecture, internal links, on-page structure, structured data, experience, duplicate risk, AEO extractability as its own check), entity (consistency sweep, local-listing completeness, author identity, reviews, social profiles, the cited-but-never-named diagnosis, benchmark two or three peers briefly), conversion path (every form, every CTA against the conversion definition, phone/chat/booking routes, analytics events firing, consent posture; measurement outranks nearly everything else in sequencing). Read constraints before any recommendation; with several brands run one mode across all first. Live fetches often fail: ask for a live-URL check, screenshot or view-source and record unverified items as unverified. Check every entity claim against EntityOS, never against what looks right. Automated or feed-generated pages nobody can edit only get an indexation, cannibalization and template-schema question. Every OPT-APPROVAL finding opens a question row; state what was not checked. Never invent speed scores or traffic figures, never let a tool's severity set the band, never recommend a duplicate listing (confirm what exists), markup the business forbids, or a rich-result type that no longer exists.

**Performance check-ins (`content-performance-tracker`).** Pass the baseline and verdict gates from `lifeos-workos-results`, and the expected outcome written at planning time.

**Drafting voice and humanizing (`humanizeai`).** See `lifeos-workos-writing/references/writing-standards.md` (checkpoints and preservation contract).

## File organizing
For project file clean-ups use `lifeos-deviceos-files` with these rules. Two depths: a quick check (default, after any file-producing stage: is the touched file referenced correctly everywhere, did a rename break a pointer) and a full audit on request (registry reconciliation, stale-reference sweep across every Markdown file and tracker cell, per-file decisions, and where the folder is not writable a ready-to-upload set).

One decision per file: Keep, Update, Merge (consolidate, keep the more complete content, confirm nothing unique to the losing file is dropped before deleting a side), Replace, Rename (update every reference before renaming, never after), Archive (to the holding folder from the file rules), Delete (only with explicit confirmation, and per `rules.md` never straight to deletion), Create.

Hard rules: never rename a tracker or task-store export (it is referenced by exact name); check every reference before renaming anything else; keep a file registry (file, purpose, owning stage, last touched); never change task data inside a tracker. State which mode ran: a report that reads like a completed action when nothing was written is the failure to prevent. A quick check is a one or two line confirmation or the specific issue found; do not expand it into a full audit uninvited.
