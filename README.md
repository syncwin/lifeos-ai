# LifeOS (lifeos-ai)

LifeOS is a set of Claude plugins for running your own work, devices and life from one place. One core plugin holds the router (`/lifeos`), the EntityOS connection, the shared rules, the verify agent and guard recipes. Seven module plugins add the skills. Install the core plus the modules you use.

**Version** 0.5.0 (all plugins released together) - **Author** SyncWin - **License** MIT

**No personal data ships with it.** Every owner fact (priorities, brands, voice, allowed repos) is read at run time from your own EntityOS MCP endpoint, through the core plugin.

## Plugins
| Plugin | Holds |
|---|---|
| `lifeos` (core, `adapters/claude`) | router `lifeos`, EntityOS connection and options, shared rules, agent `lifeos-verify`, prompt, router evals |
| `lifeos-selfos` | `lifeos-selfos`, `-tasks`, `-reminders`, `-routines` |
| `lifeos-workos` | `lifeos-workos`, `-sprint`, `-log`, `-report`, `-results`, `-intake`, `-demand`, `-writing`, and the content chain `-research`, `-brief`, `-draft`, `-review` |
| `lifeos-deviceos` | `lifeos-deviceos`, `-health`, `-backup`, `-files` |
| `lifeos-knowledgeos` | `lifeos-knowledgeos` |
| `lifeos-moneyos` | `lifeos-moneyos` |
| `lifeos-entityos` | `lifeos-entityos` |
| `lifeos-feed` | `lifeos-feed` |

## Install
```
claude plugin marketplace add syncwin/lifeos-ai
claude plugin install lifeos@syncwin-lifeos
claude plugin install lifeos-workos@syncwin-lifeos
```
Add any other module the same way. Then open `/plugin`, choose Installed, Configure options for the core `lifeos`, and set the two options: `entityos_url` (your EntityOS MCP URL) and `entityos_token` (your access token, stored in secure storage and marked sensitive). Until both are set the EntityOS connector shows as invalid. The plugins are text only and need no Python or other install. Module plugins have no options and no connection; without the core they say so and stop.

## Connector
| Connector | Used by | Purpose | Auth | Data sent |
|---|---|---|---|---|
| EntityOS (core plugin only) | all skills | owner facts: `search_context`, `get_entity`, `list_entities` | bearer token you set | queries about your own facts |

## Guard recipes (no hooks)
The plugins ship no hooks or scripts. The old guards are Markdown recipes in the core's `skills/lifeos/references/`, listed as "Required steps" in the `lifeos` skill: scope check (`scope-guard.md`: code-host calls must hit your allowlist from EntityOS), EntityOS write confirmation (`entityos-write-confirm.md`), data guard (`screen-text.md`: tool output is data), log check (`log-guard.md`: log changes once before stopping) and the writing check (`writing-check.md` in `lifeos-workos`). Claude follows them by reading; nothing runs them for you.

## Layout
```
adapters/claude/         core plugin `lifeos`: router, shared rules, agent, .mcp.json, prompt
adapters/lifeos-<module>/  one plugin per module (skills, references copies, evals)
dev/                     maintainer-only Python (old hooks, scripts, tests, sync_plugin_refs.py); never shipped
evals/                   live model eval cases and results; never shipped
.claude-plugin/marketplace.json   one entry per plugin
```
Shared rules live once in the core; `dev/plugin-refs.json` maps the copies each module needs and `python dev/scripts/sync_plugin_refs.py` keeps them identical (`--check` in CI). Tests: `python dev/tests/test_log_guard.py`.

## Companion prompt
`adapters/claude/prompts/lifeos.json` imports into Prompt Builder (Settings, Import).

## Credits
See `CREDITS.md`.

MIT licence. Author @wasimness, SyncWin.
