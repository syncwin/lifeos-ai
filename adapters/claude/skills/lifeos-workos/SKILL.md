---
name: lifeos-workos
description: "Starter and router for the WorkOS module, work, clients, projects, content and follow-ups. Use for \"plan my week\", \"log my work\", \"start my day\", \"end of day report\", \"did that work pay off\", \"a manager sent me a request\", \"check this draft\". Routes to the workos stages."
license: MIT
---

# LifeOS WorkOS
Needs: EntityOS MCP; module `workos` enabled; task store (`lifeos/references/tracker.md`).
Start: run the `lifeos` router first if it has not run.

| Request | Stage |
|---|---|
| Weekly plan, priorities, carry-over | `lifeos-workos-sprint` |
| Record work done, evidence, decisions, questions | `lifeos-workos-log` |
| Day start or day end report | `lifeos-workos-report` |
| Did a change work, baseline and verdicts | `lifeos-workos-results` |
| Requests from managers, colleagues, own ideas | `lifeos-workos-intake` |
| Plan content for multi-constraint queries | `lifeos-workos-demand` |
| Check or write prose against the pattern glossary | `lifeos-workos-writing` |

Stage order when several apply: intake, sprint, log, report, results. Stages inherit the shared rules; a stage with a stale upstream input lists it as a task and does not run it.

## Stage gate, business and inputs
- **Stage gate:** route to the chosen stage only and load only the references that stage needs. This gate overrides any skill's own "usually followed by" chaining; the one chain that runs on is research, brief, draft, review. A missing required input: name it and stop.
- **Business:** work about a brand picks the entity from EntityOS `list_entities` (relation owned or client); detect it from a domain or hostname with `search_context` and ask once, with the list, only if several fit. "New business" forces `lifeos-entityos/references/add-client.md` before any stage; "all business units" is for sprint stages only.
- **Task store first:** sprint and planning stages load the current LifeOS task store (`lifeos/references/tracker.md`) before planning. Without it, tasks are silently dropped from the plan: stop and say so instead of planning from memory.
- **Details to collect per stage:** Plan Week: confirmed working days and wanted tasks. Execute: the task id. Close Day or Week: what finished, what started and did not finish, what was discovered, decisions taken. Any stage: a client task list, a freeze, an approval, a holiday or a contradiction.

## Plugin handoffs
Not ported into LifeOS; installed plugins do this work. Pass brand context from EntityOS (`get_context`, `search_context`); if the plugin is not installed, say so and name it. Rules that travel: `lifeos/references/core-rules.md`, Handoffs to installed plugins.

| Request | Plugin |
|---|---|
| Content research, content briefs and outlines | `content-structure-strategy` |
| On-page SEO and AEO | `content-seo-strategy` |
| Drafting voice, humanizing | `humanizeai` |
| Whole-site content audit (exports, prune, merge, update, keep) | `content-audit-strategy` |
| Site, entity and conversion audit | LifeOS runs it with `references/audit-methods.md` (AEO, cited-but-never-named, consistency sweep, local listing, tracking, consent, conversion path) and EntityOS facts; `content-audit-strategy` only for a whole-site content inventory |
| Finding a monetizable content niche or angle | `content-niche-discovery` |
| Per-piece performance check-ins (30, 60, 90 days) | `content-performance-tracker` |
| Project file organizing | `lifeos-deviceos-files` |

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- The request went to the stage in the table; stale upstream stages are listed as proposed tasks, not run.
- Stage order followed: intake, sprint, log, report, results.

## Handoff
Delivered: The chosen stage's result, then a verifier pass.
Next: check a finished deliverable -> `lifeos-verify`.

Scratchpad: end per `lifeos/references/scratchpad.md`.
