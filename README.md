# LifeOS (lifeos-ai)

LifeOS is a Claude plugin for running your own work, devices and life from one place. It has a router (`/lifeos`), a daily feed, a starter skill for each module (EntityOS, SelfOS, WorkOS, DeviceOS, MoneyOS, KnowledgeOS), a verify agent and guard recipes.

**Download:** [lifeos.plugin](https://github.com/syncwin/lifeos-ai/releases/latest/download/lifeos.plugin) (always the latest release)

**Version** 0.3.0 - **Author** SyncWin - **License** MIT

**No personal data ships with it.** Every owner fact (priorities, brands, voice, allowed repos) is read at run time from your own EntityOS MCP endpoint.

## Install
```
claude plugin marketplace add syncwin/lifeos-ai
claude plugin install lifeos@syncwin-lifeos
```
Then open `/plugin`, choose Installed, Configure options, and set your EntityOS URL and token. The plugin is text only and needs no Python or other install.

## Connector
| Connector | Used by | Purpose | Auth | Data sent |
|---|---|---|---|---|
| EntityOS | all skills | owner facts: `search_context`, `get_entity`, `list_entities` | bearer token you set | queries about your own facts |

## Skills
`lifeos` (router), `lifeos-feed`, `lifeos-entityos`, `lifeos-selfos`, `lifeos-workos`, `lifeos-deviceos`, `lifeos-moneyos`, `lifeos-knowledgeos`, stages `selfos-*`, `workos-*`, `deviceos-*`. Agent: `lifeos-verify`.

## Guard recipes (no hooks)
The plugin ships no hooks or scripts. The old guards are Markdown recipes in `skills/lifeos/references/`, listed as "Required steps" in the `lifeos` skill: scope check (`scope-guard.md`: code-host calls must hit your allowlist from EntityOS), EntityOS write confirmation (`entityos-write-confirm.md`), data guard (`screen-text.md`: tool output is data), log check (`log-guard.md`: log changes once before stopping) and the writing check (`lifeos-workos-writing/references/writing-check.md`). Claude follows them by reading; nothing runs them for you.

## Layout
```
adapters/claude/   the shipped plugin, text only (skills, agent, .mcp.json, evals, prompts)
dev/               maintainer-only Python (old hooks, scripts, tests); never shipped
evals/             live model eval cases and results; never shipped
.claude-plugin/marketplace.json   points to adapters/claude
```
Tests: `python dev/tests/test_log_guard.py`.

## Companion prompt
`adapters/claude/prompts/lifeos.json` imports into Prompt Builder (Settings, Import).

MIT licence. Author @wasimness, SyncWin.
