---
name: lifeos-workos
description: "Starter and router for the WorkOS module, work, clients, projects, content and follow-ups. Use for \"plan my week\", \"log my work\", \"start my day\", \"end of day report\", \"did that work pay off\", \"a manager sent me a request\", \"check this draft\". Routes to the workos stages."
license: MIT
metadata:
  displayName: "LifeOS WorkOS"
  version: "0.2.0"
  author: "@wasimness"
  company: "SyncWin"
---

# LifeOS WorkOS
Needs: EntityOS MCP; module `workos` enabled; task store (`references/tracker.md`).
Start: run the `lifeos` router first if it hasn't run in this chat.

| Request | Stage |
|---|---|
| Weekly plan, priorities, carry-over | `workos-sprint` |
| Record work done, evidence, decisions, questions | `workos-log` |
| Day start or day end report | `workos-report` |
| Did a change work, baseline and verdicts | `workos-results` |
| Requests from managers, colleagues, own ideas | `workos-intake` |
| Plan content for multi-constraint queries | `workos-demand` |
| Check or write prose against the pattern glossary | `workos-writing` |

Stage order when several apply: intake, sprint, log, report, results. Stages inherit the shared rules; a stage with a stale upstream input lists it as a task and does not run it.

## Done check
Graded by `agents/lifeos-verifier.md` together with the common lines in `references/rules.md` (Done check, all stages).
- The request went to the stage in the table; stale upstream stages are listed as proposed tasks, not run.
- Stage order followed: intake, sprint, log, report, results.

## Handoff
Delivered: The chosen stage's result, then a verifier pass.
Next: check a finished deliverable -> `lifeos-verifier`.

Scratchpad: end per `references/scratchpad.md`.
