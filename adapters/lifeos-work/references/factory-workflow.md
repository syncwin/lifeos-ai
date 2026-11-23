# Agent Factory Workflow

Method for a work task that is a code or build change done by an agent. Read by `lifeos-work-sprint` (when sizing such a task) and `lifeos-work-intake` (when a request is one). Shared rules: `${CLAUDE_PLUGIN_ROOT}/references/core-rules.md`. Anything that touches the outside world (merge, push, a message to the requester) follows `${CLAUDE_PLUGIN_ROOT}/references/risk-check.md`.

Contents: the loop; written task; checks first; isolated work; failing checks; merge gate; human review; holdout checks; start small.

## The loop
Task written, checks named, agent works in isolation, pull request opened, checks run, a person reviews, merge gate passes, merge. No step is skipped for a small change.

## 1. Every change starts as a written task
One issue or task per change, saved before any work starts, with two parts: the problem (what is wrong or missing, for whom, how it shows) and acceptance criteria (a short list of statements that are plainly true or false when the work is done). A request without both goes back to the requester, or to the owner, as a question. The agent never starts from a chat remark.

## 2. Checks first
Before the agent builds, name the checks that prove each criterion: an automated test, a command with an expected result, or a manual step with a stated outcome. Write them into the task beside the criteria. A criterion with no check is rewritten until it has one. Checks are written or approved by someone other than the building agent where practical, so the agent cannot grade its own work.

## 3. Own worktree, own branch, then a pull request
The agent works in its own worktree on its own branch, never in the main checkout and never on the main branch. When the checks pass locally it opens a pull request that links the task, lists the criteria with the check that covers each, and states what was not done. It does not merge.

## 4. Failing checks go back to the agent
When the automated checks fail on the pull request, hand the failure output back to the agent for a fix. Cap the tries at three (a different number only if the owner set one in the task). After the last try, stop, leave the branch as it is, and report: which check fails, what was tried, and a guess at the cause. Never loosen a check or delete a test to get green.

## 5. Merge gate
Merge only when every line is true; otherwise report which one is not.
- All required checks passed on the latest commit.
- Review is approved by a person.
- The change matches the task: every criterion is met and nothing outside the task was changed.
- No secrets, private data or unrelated files in the diff.

## 6. Human review on every pull request
A person reads every pull request. The one who requested the change is not the one who approves it. If only one person exists, a second reviewer is found before merge, and the gap is listed in the report. An agent review may add comments; it never replaces the person.

## 7. Holdout checks (larger work, optional)
For larger or riskier work, keep some checks hidden from the building agent: a person or separate agent writes them from the task alone and runs them against the finished branch. A failure goes back as a plain description of the behavior that broke, never the hidden check itself. Use this when visible checks could be satisfied by a shortcut.

## 8. Start small
Begin with one agent and small, well-described tasks: one outcome, a few criteria, a short diff. Widen the size or add agents only after several tasks passed the gate without rework. A setup with no review step is not offered, whatever the task size.
