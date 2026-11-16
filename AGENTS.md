# lifeos-ai agent guide

LifeOS Claude plugin (`lifeos`, command `/lifeos`): router, feed, module skills, verify agent, guard recipes. No owner fact is hardcoded; all come from EntityOS MCP.

**Structure:** the shipped plugin is `adapters/claude/` (`.claude-plugin/plugin.json`, `.mcp.json`, `skills/` with router `lifeos`, `lifeos-feed`, `lifeos-<module>`, `lifeos-workos-*`, `lifeos-deviceos-*`, `lifeos-selfos-*`; `agents/lifeos-verify.md`; `evals/router/cases.json` and `evals/evals.json`; `prompts/`; copies of README, CHANGELOG, LICENSE, PUBLIC-SAFETY, `.gitignore`). Shared rules live once in `skills/lifeos/references/` together with the guard recipes. The root keeps `.claude-plugin/marketplace.json` (source `./adapters/claude`), the same docs, `dev/` (Python tools, old hooks and tests, not shipped), `evals/` (live model cases, not shipped) and `.github/`. Edit the docs in both places and keep the copies identical.

## Commands
- Directory gate (must pass, 0 errors and 0 warnings): `python -I -X utf8 <aiaddon>/dev/aiaddon-review/scripts/validate_extension.py adapters/claude --strict --target directory --require-meta author,company`
- Router: `route_check.py adapters/claude`; secrets: `scan_secrets.py . --history` (false positives only in `.public-safety-allow`)
- Validate: `claude plugin validate adapters/claude --strict` and `claude plugin validate . --strict`
- Tests: `python dev/tests/test_log_guard.py`. Old draft checker: `python -I dev/scripts/check_draft.py <draft> --patterns adapters/claude/skills/lifeos-workos-writing/references/patterns.md`
- Evals (real model calls): `claude plugin eval adapters/claude --trust-plugin --ablation none --allow-tools Read Glob Grep Skill -j 4 --no-publish`. Write results outside the repo (`<owner-outputs>/lifeos/eval-results`).

## Rules
- **Directory compliance:** the shipped plugin is Markdown, JSON and YAML only (plus LICENSE and `.gitignore`): no hooks, no scripts, text-only skill frontmatter (no `metadata` block in SKILL.md files). `plugin.json` keeps its top-level `metadata` object: the Claude Code manifest docs list it as a valid free-form field that Claude Code ignores. Hook and script behaviour lives as recipes in `skills/lifeos/references/` and `skills/lifeos-workos-writing/references/`; the Python in `dev/` is maintainer tooling.
- Never hardcode an owner fact, name, path, brand or URL. Add a new `search_context` query to `skills/lifeos/references/rules.md` instead.
- Never pick skill or other permanent names without the user's confirmation. Every non-router skill and agent is prefixed `lifeos-`.
- Keep each `SKILL.md` short; shared rules live once in `skills/lifeos/references/` (other skills point to `../lifeos/references/`).
- On release bump `version` in `adapters/claude/.claude-plugin/plugin.json` and the marketplace entry together; add a `CHANGELOG.md` entry (root and `adapters/claude/` copies).
- Never publish secrets or private data (keys, tokens, personal contact data, client names, internal URLs, local paths).
- No commits, pushes or PRs unless asked. Branch and PR; never push to main. Never commit secrets.

## Docs
README.md, CHANGELOG.md; ideas in `IMPROVEMENTS.md`.
