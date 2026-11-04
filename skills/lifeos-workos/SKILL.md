---
name: lifeos-workos
description: "Starter and router for the WorkOS module, work, clients, projects, content and follow-ups. Use for \"plan my week\", \"log my work\", \"start my day\", \"end of day report\", \"did that work pay off\", \"a manager sent me a request\", \"check this draft\". Routes to the workos stages."
license: MIT
metadata:
  displayName: "LifeOS WorkOS"
  version: "0.1.0"
  author: "@wasimness"
  company: "SyncWin"
---

# LifeOS WorkOS
Needs: EntityOS MCP; module `workos` enabled; task store (`lifeos/references/tracker.md`).

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

Next: the chosen stage, then `lifeos-verifier`.

Scratchpad: end per `lifeos/references/scratchpad.md`.
