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

## Plugin handoffs
Not ported into LifeOS; installed plugins do this work. Pass brand context from EntityOS (`get_context`, `search_context`); if the plugin is not installed, say so and name it. Rules that travel: `lifeos/references/core-rules.md`, Handoffs to installed plugins.

| Request | Plugin |
|---|---|
| Content research, content briefs and outlines | `content-structure-strategy` |
| On-page SEO and AEO | `content-seo-strategy` |
| Drafting voice, humanizing | `humanizeai` |
| Whole-site content audit (exports, prune, merge) | `content-audit-strategy` |
| Site, entity and conversion audit | `content-audit-strategy` plus EntityOS facts |
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
