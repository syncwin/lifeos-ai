# Changelog

## [0.6.0] - 2026-11-21

Breaking: five plugins instead of eight, and every module slug is renamed to the pattern `lifeos-<module>`. All plugins are released together at 0.6.0.

### Changed
- Plugins: the core `lifeos` (now also holds the `lifeos-feed`, `lifeos-knowledge` and `lifeos-money` skills; knowledge and money are parked, off by default per the module switch) plus `lifeos-work`, `lifeos-device`, `lifeos-entity` and `lifeos-self`. The plugins `lifeos-feed`, `lifeos-knowledgeos` and `lifeos-moneyos` are gone.
- One LifeOS MCP connection only. The separate `entityos` MCP server and its options `entityos_url` and `entityos_token` are removed; the core now has the server `lifeos` with the options `lifeos_url` and `lifeos_token`. Entity data is part of LifeOS (the LifeOS entity tools, `lifeos_entity_*`); the shared rules and skills say "LifeOS entity data" instead of EntityOS. The shared-reference file names `entityos-offline.md` and `entityos-write-confirm.md` are unchanged.
- Router tables (core and module copies), router and skill evals, prompt, README, CREDITS, PUBLIC-SAFETY and `dev/plugin-refs.json` use the new slugs. Routing triggers `workos`, `selfos`, `deviceos` and `moneyos` became `work module`, `self module`, `device module` and `money module`.

### Added
- `dev/module-registry.json` (the app's module list) and `dev/scripts/check_module_registry.py`, run in CI: the plugin folders and marketplace entries must match the registry.

### Migration (old to new)
| Old | New |
|---|---|
| plugin `lifeos-workos` and skills `lifeos-workos`, `lifeos-workos-<stage>` | plugin `lifeos-work`, skills `lifeos-work`, `lifeos-work-<stage>` |
| plugin `lifeos-deviceos` and skills `lifeos-deviceos`, `lifeos-deviceos-<stage>` | plugin `lifeos-device`, skills `lifeos-device`, `lifeos-device-<stage>` |
| plugin `lifeos-selfos` and skills `lifeos-selfos`, `lifeos-selfos-<stage>` | plugin `lifeos-self`, skills `lifeos-self`, `lifeos-self-<stage>` |
| plugin and skill `lifeos-entityos` | plugin and skill `lifeos-entity` |
| plugin `lifeos-feed`, skill `lifeos-feed` | skill `lifeos-feed` in the core `lifeos` |
| plugin and skill `lifeos-knowledgeos` | skill `lifeos-knowledge` in the core `lifeos` |
| plugin and skill `lifeos-moneyos` | skill `lifeos-money` in the core `lifeos` |
| MCP server `entityos`, options `entityos_url`, `entityos_token` | MCP server `lifeos`, options `lifeos_url`, `lifeos_token` |

To migrate: uninstall the old module plugins, install the new ones, and set `lifeos_url` and `lifeos_token` in the core plugin options.

## [0.5.0] - 2026-11-20

Split into eight plugins in one marketplace, all released together at 0.5.0. Behaviour of the existing skills is unchanged.

### Added
- Seven module plugins, each its own folder under `adapters/`: `lifeos-selfos`, `lifeos-workos`, `lifeos-deviceos`, `lifeos-knowledgeos`, `lifeos-moneyos`, `lifeos-entityos`, `lifeos-feed`. Each has a manifest without options or connection, README, CHANGELOG, LICENSE, `.gitignore` and `references/` copies of the core rules its skills read. The starter skill of each module says it needs the core `lifeos` plugin and stops when its tools are missing.
- Four WorkOS content-chain skills: `lifeos-workos-research` (sourced fact table and gap list), `lifeos-workos-brief` (labelled outline with keyword tiers and a completeness gate), `lifeos-workos-draft` (draft from the brief with voice and required wording read from EntityOS) and `lifeos-workos-review` (humanize check, compliance loop, fact-lock and compliance gates, reader pass). Business facts are read at run time as EntityOS claims; skills cite claim IDs or answer `[UNKNOWN]`. Router rows 20, 27, 28 and 29 and seven router cases.
- `dev/scripts/sync_plugin_refs.py` and `dev/plugin-refs.json`: copy the core's shared references into each module plugin; `--check` exits 1 on drift and runs in CI. CI now validates every `adapters/*` plugin and runs the router check where router evals exist.
- `CREDITS.md`.

### Changed
- The core `lifeos` plugin keeps the router, `skills/lifeos/references/`, `agents/lifeos-verify.md`, `.mcp.json`, the options, the prompt and the router evals; the router loads skills as `<plugin>:<skill>` and names a module plugin that is not installed.
- Skills moved with `git mv` and kept their evals. Pointers to shared rules are `${CLAUDE_PLUGIN_ROOT}/references/<file>` and resolve inside the plugin. The WorkOS method files shared by several stages (sprint, demand and writing references) moved to the plugin's `references/`, which fixes the cross-skill pointers in the log, report and results stages.
- Router out-of-scope and routing evals: owner-specific stacks in eval prompts replaced by neutral wording.

## [0.4.0] - 2026-11-15

Strategist port: the brand-agnostic methods of the retired strategist plugin move into LifeOS. Every brand fact is read from EntityOS at run time (`get_context`, `get_policy`, `search_context`); no skill carries brand, owner, client, regulator or example data.

### Added
- `skills/lifeos/references/core-rules.md` (shared): the seven rules, token discipline, clarification gate, brief completeness gate, companion plugins, dependency tiers, open-questions queue, absorbing outside items, file naming and publishing identity, file precedence, never-invent list, stage boundaries, plugin handoff rules (research, briefs, site and entity audit, performance check-ins) and file-organizing rules.
- `lifeos-workos-sprint/references/execution-and-reporting.md` and `workbook-and-tracker-spec.md` (also used by `lifeos-workos-report` and `lifeos-workos-log`): sprint cadence, commitment and WIP rules, sequencing, the content boundary, execute-a-task steps, deliverables by stage, Open and Close day reports, tracker tabs, Findings fields, append-only snapshots and write discipline (tracker written once a day at close).
- `lifeos-workos-demand/references/scoring-and-verdict-framework.md` and `cluster-and-treatment-model.md`: exclusion gate, opportunity score, calibration, one-asset test, keyword mapping, CTR curve, verdicts, AI-visibility panel; cluster model, five page treatments, one ranked queue, six content rules, handoff to the content pipeline.
- `lifeos-workos-results/references/decline-diagnosis-method.md`: decision tree, segmenting, dilution, concurrent events, migration signatures, AI answer surfaces.
- `lifeos-workos-writing/references/writing-standards.md`: four-exception rule, paragraph and heading mechanics, meta block, linking and CTA rules, the three humanize checkpoints, the standalone-humanization preservation contract, the three review passes and the two review files.
- Router routes 20 to 25 load `lifeos-workos`, whose Plugin handoffs table names the installed plugin (`content-structure-strategy`, `content-seo-strategy`, `humanizeai`, `content-audit-strategy`, `content-performance-tracker`); brand context is passed from EntityOS and a missing plugin is named. Project file organizing routes to `lifeos-deviceos-files`. 14 new router eval cases.
- `lifeos-entityos/references/add-client.md`: "add a new client" / "onboard a client" recipe. Asks the basics, drafts the entity (relation client, engagement block), profile and voice sources and `unverified` draft contexts, asks before writing, never imports access or credential sections. Two router cases and two skill evals.
- `lifeos-workos/references/audit-methods.md`: site (AEO extractability), entity (cited-but-never-named, consistency sweep, local listing, author identity, reviews, social) and conversion-path (capture inventory, tracking diagnosis, consent) methods, so LifeOS runs the audit itself; `content-audit-strategy` stays for whole-site content inventories. `content-niche-discovery` added to the plugin handoffs.
- `lifeos-workos-writing/references/patterns.md`: patterns 11 to 14 and the pattern intake protocol. Per-business patterns live in EntityOS brand context, start empty and grow from reviewer pattern frequency; never pre-populated.
- `lifeos-entityos/references/add-client.md`: update check, batched intake, multi-brand check, persona and voice records with the authorship convention, the approved-sources research method (method only), global versus local facts, closing confirmation.
- Stage gate, business selector (entity from `list_entities`, relation owned or client) and per-stage details in `lifeos-workos` and the router; the router and prompt warn that sprint and planning stages without the current task store drop tasks, and load the store first (`prompts/lifeos.json`).
- Skill evals for the ported stages and 3 more router cases.

### Changed
- `workbook-and-tracker-spec.md` rewritten as the field and column guide for the one LifeOS task store (the two-workbook model is dropped; write once at the day close, never rename kept).
- Each affected SKILL.md points to its new references at the step where they apply.

## [0.3.1] - 2026-11-15

### Changed
- Module switch: the router now calls the LifeOS MCP tool `lifeos_list_modules` once per session when it is available and uses its result (new `skills/lifeos/references/module-list.md`); without the tool it asks once, as before.

## [0.3.0] - 2026-11-14

Directory-compliant single-branch layout. `main` is both the public repo and the Anthropic plugin directory source; the shipped plugin is `adapters/claude/` and is text only.

### Renamed (old name -> new name)
- Skills: `deviceos-backup` -> `lifeos-deviceos-backup`, `deviceos-files` -> `lifeos-deviceos-files`, `deviceos-health` -> `lifeos-deviceos-health`, `selfos-reminders` -> `lifeos-selfos-reminders`, `selfos-routines` -> `lifeos-selfos-routines`, `selfos-tasks` -> `lifeos-selfos-tasks`, `workos-demand`, `workos-intake`, `workos-log`, `workos-report`, `workos-results`, `workos-sprint`, `workos-writing` -> the same name with the `lifeos-` prefix.
- Agent: `lifeos-verifier` -> `lifeos-verify`.

### Removed from the plugin
- `hooks/hooks.json`, `scripts/*.py` (`data_guard`, `log_guard`, `scope_guard`, `screen_text`, `sync_shared`, `injection_model.json`) and `skills/workos-writing/scripts/check_draft.py`. They moved unchanged to `dev/` (`dev/hooks`, `dev/scripts`), with the test in `dev/tests`.
- The `metadata` block in every skill and agent frontmatter (directory policy wants text-only frontmatter). The version lives in `plugin.json` and the marketplace entry.
- The `shared/` folder and its sync: the five shared references (`rules`, `scratchpad`, `risk-check`, `tracker`, `entityos-offline`) were identical copies in every skill. They now live once in `skills/lifeos/references/` and every other skill points to `../lifeos/references/`. Nothing in them changed.

### Added (hook and script behaviour as recipes, no feature lost)
- Router "Required steps" table and a "Routing table" with tie-breaks and a default question (`evals/router/cases.json`).
- `skills/lifeos/references/scope-guard.md` (scope_guard: code-host calls against the EntityOS allowlist, ask before a push to main), `entityos-write-confirm.md` (the EntityOS write-confirmation hook), `screen-text.md` (data_guard and screen_text: judged injection screen), `log-guard.md` (log_guard: log once before stopping).
- `skills/lifeos-workos-writing/references/writing-check.md` (check_draft: the deterministic draft check by reading).
- `.public-safety-allow`, `PUBLIC-SAFETY.md`, public-safety `.gitignore` preset, CI (`ci.yml`).

### Changed
- Release workflow builds `lifeos.plugin` from `adapters/claude` and asserts no code ships; `.mcp.json` (the EntityOS remote connector and its `userConfig`) is unchanged.
- Local paths removed from `AGENTS.md` and `evals/RESULTS.md`; docs describe the new layout. Old history hits (local paths, the public support address) are allowlisted, not rewritten.
- The judged injection screen has no numeric score (the old script's classifier cannot be reproduced by reading).

## [0.2.4] - 2026-11-06

### Changed
- Standing rule: research before building. Check current official docs and widely recommended, secure practice before choosing an approach, file, tool, config or dependency; cite the source; mark anything unverified; never guess; keep research scoped to the task.

## [0.2.3] - 2026-11-06
### Fixed
- Stop log guard: LifeOS-session detection now checks the Skill name (not any text in its arguments), so other sessions that merely mention lifeos are never blocked. Blocks at most once per session (marker keyed by session_id in the temp dir). `mcp__memory__save_progress` counts as a log. If no log tool is visible, it warns once and does not block. Fails open on every error. Added tests/test_log_guard.py.

## [0.2.2] - 2026-11-05
### Fixed
- Stop log guard only fires in sessions that used LifeOS, at most once per session.

## [Unreleased]

**Added**
- GitHub Actions workflow `release-plugin.yml` builds `lifeos.plugin` and attaches it to each release for a one-click download link (README).

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
