# Eval results (2026-11-04)

Command: `claude plugin eval . --trust-plugin --ablation none --allow-tools Read Glob Grep Skill -j 4 --no-publish` (1 run per case, 13 cases, $1.06). Raw output is kept outside the repo.

| Case | Score | Pass |
|---|---|---|
| 01 focus today | 1.00 | pass |
| 02 plan week (workos-sprint) | 0.67 | trigger-sub fail |
| 03 passport reminder (selfos-reminders) | 0.67 | trigger-sub fail |
| 04 backup health (deviceos-backup) | 0.67 | trigger-sub fail |
| 05 daily feed (lifeos-feed) | 0.67 | trigger-sub fail |
| 06 log and plan (workos-log) | 0.67 | trigger-sub fail |
| 07 receipt (lifeos-moneyos) | 1.00 | pass |
| 08 save link (lifeos-knowledgeos) | 0.67 | trigger-sub fail |
| 09 manager request (workos-intake) | 1.00 | pass |
| 10 edit lifeos skill | 1.00 | pass |
| 11 python function (negative) | 1.00 | pass |
| 12 WordPress CPT (negative) | 1.00 | pass |
| 13 Nowa deploy (negative) | 1.00 | pass |

Totals: 7 of 13 cases fully pass; the router trigger and result judge pass in all 13. The new `trigger-sub` grader (expected sub-skill loads) passes for 07 and 09 and fails for 02-06 and 08.

Cause (not a description defect): the sandbox has no EntityOS mock (`plugin:lifeos:entityos` is not started), and the router says to stop and tell the user to connect EntityOS, so the run ends before the sub-skill loads. Next step: add `evals/mocks/entityos/` so the router can proceed, then rerun.
