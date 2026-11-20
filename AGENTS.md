# lifeos-ai agent guide

LifeOS Claude plugin (`lifeos`, command `/lifeos`): router, feed, module skills, verify agent, guard recipes. No owner fact is hardcoded; all come from EntityOS MCP.

**Structure:** eight plugins in one marketplace, all released together. The core `lifeos` stays at `adapters/claude/` (the plugin directory tracks that path): `.claude-plugin/plugin.json` with the `userConfig`, `.mcp.json`, `skills/lifeos/` (router and `references/`, the shared rules and guard recipes), `agents/lifeos-verify.md`, `prompts/`, `evals/router/cases.json` and `evals/evals.json`, plus copies of README, CHANGELOG, LICENSE, PUBLIC-SAFETY and `.gitignore`. Each module is its own plugin folder `adapters/<plugin>/` with `.claude-plugin/plugin.json` (no `userConfig`, no `.mcp.json`; only the core holds the MCP connection), `skills/`, `references/`, README, CHANGELOG, LICENSE, PUBLIC-SAFETY and `.gitignore`:
- `lifeos-selfos`: `lifeos-selfos`, `-tasks`, `-reminders`, `-routines`
- `lifeos-workos`: `lifeos-workos`, `-sprint`, `-log`, `-report`, `-results`, `-intake`, `-demand`, `-writing`, `-research`, `-brief`, `-draft`, `-review`; its `references/` also holds the method files several stages share
- `lifeos-deviceos`: `lifeos-deviceos`, `-health`, `-backup`, `-files`
- `lifeos-knowledgeos`, `lifeos-moneyos`, `lifeos-entityos`, `lifeos-feed`: one skill each

Shared rules live once in `adapters/claude/skills/lifeos/references/`. `dev/plugin-refs.json` maps each module to the core files it needs; `python -I -X utf8 dev/scripts/sync_plugin_refs.py` copies them into the module's `references/` and `--check` (CI) exits 1 on drift. Edit a shared rule in the core only, then run the sync. The root keeps `.claude-plugin/marketplace.json` (one entry per plugin, `source ./adapters/<folder>`), `CREDITS.md`, the same docs, `dev/` (Python tools, old hooks and tests, not shipped), `evals/` (live model cases, not shipped) and `.github/`. Edit README and CHANGELOG at the root and in `adapters/claude/` and keep those copies identical.

## Commands
- Directory gate (must pass, 0 errors and 0 warnings), once per plugin folder under `adapters/`: `python -I -X utf8 <aiaddon>/dev/aiaddon-review/scripts/validate_extension.py adapters/<plugin> --strict --target directory --require-meta author,company`
- Router: `route_check.py adapters/claude` (the core, selfos, workos and deviceos have router evals; the others have one skill); refs: `python -I -X utf8 dev/scripts/sync_plugin_refs.py --check`; secrets: `scan_secrets.py . --history` (false positives only in `.public-safety-allow`)
- Validate: `claude plugin validate adapters/<plugin> --strict` for each plugin and `claude plugin validate . --strict`
- Tests: `python dev/tests/test_log_guard.py`. Old draft checker: `python -I dev/scripts/check_draft.py <draft> --patterns adapters/lifeos-workos/references/patterns.md`
- Evals (real model calls), per plugin: `claude plugin eval adapters/claude --trust-plugin --ablation none --allow-tools Read Glob Grep Skill -j 4 --no-publish`. Write results outside the repo (`<owner-outputs>/lifeos/eval-results`).

## Rules
- **Directory compliance:** the shipped plugin is Markdown, JSON and YAML only (plus LICENSE and `.gitignore`): no hooks, no scripts, text-only skill frontmatter (no `metadata` block in SKILL.md files). `plugin.json` keeps its top-level `metadata` object: the Claude Code manifest docs list it as a valid free-form field that Claude Code ignores. Hook and script behaviour lives as recipes in `adapters/claude/skills/lifeos/references/` and `adapters/lifeos-workos/references/`; the Python in `dev/` is maintainer tooling.
- Never hardcode an owner fact, name, path, brand or URL. Add a new `search_context` query to `adapters/claude/skills/lifeos/references/rules.md` instead. The content-chain skills read every business fact (voice, audience, regulator, sources, exclusions) from EntityOS claims and cite claim IDs or answer UNKNOWN; credit adapted methods in `CREDITS.md`.
- Never pick skill or other permanent names without the user's confirmation. Every non-router skill and agent is prefixed `lifeos-`.
- Keep each `SKILL.md` short; shared rules live once in the core and are copied per module. Skills point to `${CLAUDE_PLUGIN_ROOT}/references/<file>` (a `../` path leaves the skill folder and fails the validator). Every module skill, starter and stage alike, carries a line (stages word it per stage, since the validator flags verbatim repeats) that it needs the core `lifeos` plugin and stops when its tools are missing. Module router tables (selfos, workos, deviceos) are the core rows whose skill lives in that module; `sync_plugin_refs.py --check` fails when they differ. Specific stage rows come before module starter rows.
- On release bump `version` (and `metadata.version`) in every plugin's `plugin.json` and the marketplace entries together; add a `CHANGELOG.md` entry (root and `adapters/claude/` copies identical; each module plugin keeps its own short changelog).
- Never publish secrets or private data (keys, tokens, personal contact data, client names, internal URLs, local paths).
- No commits, pushes or PRs unless asked. Branch and PR; never push to main. Never commit secrets.

## Docs
README.md, CHANGELOG.md; ideas in `IMPROVEMENTS.md`.
