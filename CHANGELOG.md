# Changelog

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
