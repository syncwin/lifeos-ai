# Changelog

## [Unreleased]

**Fixed**
- EntityOS write-confirmation hook matcher now anchors the write verbs to the start of the tool-name segment after `__`, so read tools such as `get_input_schema`, `list_output` or `compute_stats` no longer prompt.

**Changed**
- `lifeos-feed`: ranking text now follows the PRD: score = urgency × importance × freshness, feedback lowers similar cards, daily top 3, cards offer done, snooze, open, dismiss (reply or file where they apply).

## 0.2.1: Update

**Changed**
- Token handling rule in the shared rules (token only in the sensitive setting, https EntityOS URL only, never in commands, URLs, files, records, memory or reports; refuse requests found in content). Synced into every skill.

**Fixed**
- scope_guard.py now fails closed: an allowlist file that exists but cannot be read, or any error while checking a call once an allowlist is set, blocks the call (exit 2). With no allowlist it behaves as before.
- The EntityOS write confirmation matched only lowercase verbs; it now also matches capitalised tool names and remove, insert, upsert, patch and merge.

## [0.2.0] - 2026-11-05

**Added**
- `shared/` (manifest plus rules, scratchpad, tracker, risk-check, entityos-offline) and `scripts/sync_shared.py`: every skill is now self-contained and reads its own `references/`; `--check` fails on drift.
- `risk-check.md`: fixed block filled in before every risky action, plus the table of actions that need it; linked from deviceos-backup, deviceos-files, lifeos-moneyos, workos-intake, selfos-reminders and the router.
- `entityos-offline.md`: if EntityOS is missing or fails twice, ask once about a manual step-by-step pack, then continue without owner facts; replaces the router's hard stop.
- Every non-router skill: "Start" line, "Done check" list (matches the verifier) and "Handoff".
- Per-skill `evals/evals.json` (2 should-trigger, 1 should-not) and an EntityOS eval mock in `evals/mocks/entityos/`.
- `workos-writing/scripts/check_draft.py`: deterministic draft checker driven by `references/patterns.md`.
- PreToolUse hook that asks before EntityOS write tools.
- Eval results archive under `evals/results/<date>-<version>/` (grading.json plus summary).

**Changed**
- Router: out-of-scope rows (code to /fsdevops, WordPress to /fswpdevops, app UI to /appops) and "where does this value belong" to lifeos-entityos.
- `rules.md`: each rule marked canonical once; stage skills point to it instead of restating.
- Stage descriptions tightened with the phrasings users type.

## [0.1.0] - 2026-11-04
### Added
First cut (Block 1, plugin part): router `lifeos`, `lifeos-feed`, one starter per module, `workos-*`, `deviceos-*` and `selfos-*` stages, `lifeos-verifier` agent, scope/data/log guard hooks, EntityOS connector through `userConfig`, shared references, evals and companion prompt.
