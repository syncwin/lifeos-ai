# lifeos-ai agent guide

LifeOS Claude plugin (`lifeos`, command `/lifeos`): router, feed, module skills, verifier agent, guard hooks. No owner fact is hardcoded; all come from EntityOS MCP.

**Structure:** `skills/` (router `lifeos`, `lifeos-feed`, `lifeos-<module>`, `workos-*`, `deviceos-*`, `selfos-*`), `agents/lifeos-verifier.md`, `hooks/hooks.json`, `scripts/*_guard.py`, `evals/`, `prompts/`, `skills/lifeos/references/` (shared rules).

## Commands
- Validate: `python -I -X utf8 A:\Dev\projects\aiaddon\skills\aiaddon-review\scripts\validate_extension.py . --target directory --strict` (expect 0 errors, 0 warnings)
- Evals (real model calls): `claude plugin eval . --trust-plugin --ablation none --allow-tools Read Glob Grep Skill -j 4 --no-publish`. Write results outside the repo (`D:\SyncWin\AI Outputs\lifeos\eval-results`).
- Rebuild eval cases: `python -I A:\Automation\plugin-evals\regen_evals.py . lifeos ""`

## Rules
- Never hardcode an owner fact, name, path, brand or URL. Add a new `search_context` query to `skills/lifeos/references/rules.md` instead.
- Skill names not confirmed by the plan are placeholders; do not rename without the user.
- Keep each `SKILL.md` short; shared rules live once in `skills/lifeos/references/`.
- On release bump `version` in `plugin.json` and every skill and agent `metadata.version` together; add a `CHANGELOG.md` entry.
- Hooks take settings as arguments (no environment reads) and use the Python standard library only; bad input never blocks.
- No commits, pushes or PRs unless asked. Branch and PR; never push to main. Never commit secrets.

## Docs
README.md, CHANGELOG.md; ideas in `IMPROVEMENTS.md`.
