---
name: lifeos-work
description: "Starter and router for the work module, work, clients, projects, content and follow-ups. Use for \"plan my week\", \"log my work\", \"start my day\", \"end of day report\", \"did that work pay off\", \"a manager sent me a request\", \"check this draft\". Routes to the work stages."
license: MIT
---

# LifeOS Work
Needs: LifeOS MCP; module `work` enabled; task store (`${CLAUDE_PLUGIN_ROOT}/references/tracker.md`).
Needs the core `lifeos` plugin for the MCP connection and shared rules; if its tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

## Routing table

Read top to bottom; first matching row wins (phrases match as whole words, case-insensitive). Checked against `evals/router/cases.json`.

| Order | Trigger phrases | Skill | Then |
|---|---|---|---|
| 0 | sprint plan; plan my week; plan this week; deliver by friday; re-plan | `lifeos-work-sprint` | (none) |
| 1 | log my work; log this work; log what i did; record what i did; note the decision; question queue | `lifeos-work-log` | (none) |
| 2 | start my day; morning plan; end of day report; plan tomorrow; weekly wrap | `lifeos-work-report` | (none) |
| 3 | did that change work; check results; 28 day; baseline; did it pay off; how did that page perform | `lifeos-work-results` | (none) |
| 4 | manager sent; new request; add this to my plan; is this a duplicate | `lifeos-work-intake` | (none) |
| 5 | should this be a page; cluster these keywords; plan content for these queries; multi-constraint | `lifeos-work-demand` | (none) |
| 6 | check this draft; too promotional; edit for voice; review my copy; proof this text | `lifeos-work-writing` | (none) |
| 20 | research this topic; research this brief; fact table; sourced research; no brief yet, research first | `lifeos-work-research` | (none) |
| 21 | on-page seo; aeo; answer engine; schema markup; seo audit of this page | `lifeos-work` | hand off to plugin content-seo-strategy; pass brand context from LifeOS entity data |
| 22 | humanize; sounds like ai; make this sound human; ai-written | `lifeos-work` | hand off to plugin humanizeai; pass voice from LifeOS entity data |
| 23 | audit my site; whole-site content audit; prune merge; what should i delete; search console export | `lifeos-work` | hand off to plugin content-audit-strategy; pass brand context from LifeOS entity data |
| 24 | 30 60 90; how is this piece performing; why isn't this ranking; check-in on published | `lifeos-work` | hand off to plugin content-performance-tracker; pass the baseline and expected outcome |
| 25 | audit entity; nap consistency; conversion path; is my site converting; consistency sweep; cited but never named; tracking diagnosis; consent audit | `lifeos-work` | run the audit with the audit methods reference in lifeos-work and LifeOS entity facts |
| 26 | find me a niche; niche ideas; what should i write about | `lifeos-work` | hand off to plugin content-niche-discovery; pass brand context from LifeOS entity data |
| 27 | content brief; build a brief; content outline; outline this article; structure this page | `lifeos-work-brief` | (none) |
| 28 | draft this article; draft this page; write the draft; draft from this brief; write the body | `lifeos-work-draft` | (none) |
| 29 | final review; ready to publish; fact-lock; qa gate; compliance check | `lifeos-work-review` | (none) |
| 30 | work module; clients; projects; follow-ups | `lifeos-work` | (none) |

Default when no row matches: ask one closed question, "Is this (a) planning or logging work, (b) a report or results check, (c) a request to triage, (d) writing or content, or (e) none of these?", and stop. Never answer the stage work yourself: load the stage with the Skill tool using the full slug `<plugin>:<skill>` (for example `lifeos-work:lifeos-work-sprint`); without the Skill tool, read its `SKILL.md` by relative path from the plugin root.

Stage order when several apply: intake, sprint, log, report, results. Content chain: research, brief, draft, review. Stages inherit the shared rules; a stage with a stale upstream input lists it as a task and does not run it.

## Stage gate, business and inputs
- **Stage gate:** route to the chosen stage only and load only the references that stage needs. This gate overrides any skill's own "usually followed by" chaining; the one chain that runs on is research, brief, draft, review (`lifeos-work-research`, `lifeos-work-brief`, `lifeos-work-draft`, `lifeos-work-review`). A missing required input: name it and stop.
- **Business:** work about a brand picks the entity from LifeOS entity data `list_entities` (relation owned or client); detect it from a domain or hostname with `search_context` and ask once, with the list, only if several fit. "New business" forces the add-client recipe of the `lifeos-entity` skill before any stage; "all business units" is for sprint stages only.
- **Task store first:** sprint and planning stages load the current LifeOS task store (`${CLAUDE_PLUGIN_ROOT}/references/tracker.md`) before planning. Without it, tasks are silently dropped from the plan: stop and say so instead of planning from memory.
- **Details to collect per stage:** Plan Week: confirmed working days and wanted tasks. Execute: the task id. Close Day or Week: what finished, what started and did not finish, what was discovered, decisions taken. Any stage: a client task list, a freeze, an approval, a holiday or a contradiction.

## Plugin handoffs
Not part of LifeOS (research, brief, draft and review are built in); installed plugins do this work. Pass brand context from LifeOS entity data (`get_context`, `search_context`); if the plugin is not installed, say so and name it. Rules that travel: `${CLAUDE_PLUGIN_ROOT}/references/core-rules.md`, Handoffs to installed plugins.

| Request | Plugin |
|---|---|
| On-page SEO and AEO mechanics beyond the brief | `content-seo-strategy` |
| Drafting voice, humanizing | `humanizeai` |
| Whole-site content audit (exports, prune, merge, update, keep) | `content-audit-strategy` |
| Site, entity and conversion audit | LifeOS runs it with `references/audit-methods.md` (AEO, cited-but-never-named, consistency sweep, local listing, tracking, consent, conversion path) and LifeOS entity facts; `content-audit-strategy` only for a whole-site content inventory |
| Finding a monetizable content niche or angle | `content-niche-discovery` |
| Per-piece performance check-ins (30, 60, 90 days) | `content-performance-tracker` |
| Project file organizing | `lifeos-device-files` |

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- The request went to the stage in the table; stale upstream stages are listed as proposed tasks, not run.
- Stage order followed: intake, sprint, log, report, results.

## Handoff
Delivered: The chosen stage's result, then a verifier pass.
Next: check a finished deliverable -> `lifeos-verify`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
