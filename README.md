# LifeOS (lifeos-ai)

LifeOS is a set of Claude plugins for running your own work, devices and life from one place. One core plugin holds the router (`/lifeos`), the LifeOS connection, the shared rules, the verify agent and guard recipes. Four module plugins add the rest. Install the core plus the modules you use.

**Version** 0.6.0 (all plugins released together) - **Author** SyncWin - **License** MIT

**No personal data ships with it.** Every owner fact (priorities, brands, voice, allowed repos) is read at run time from your own LifeOS MCP endpoint, through the core plugin.

## Plugins
Five plugins in one marketplace, matching the LifeOS app's module registry (`dev/module-registry.json`: work, device, entity, self; the core also holds feed, knowledge and money).

| Plugin | Holds |
|---|---|
| `lifeos` (core, `adapters/claude`) | router `lifeos`, the one LifeOS MCP connection and options, shared rules, agent `lifeos-verify`, prompt, router evals, and the skills `lifeos-feed`, `lifeos-knowledge` and `lifeos-money` (knowledge and money are off by default) |
| `lifeos-self` | `lifeos-self`, `-tasks`, `-reminders`, `-routines` |
| `lifeos-work` | `lifeos-work`, `-sprint`, `-log`, `-report`, `-results`, `-intake`, `-demand`, `-writing`, and the content chain `-research`, `-brief`, `-draft`, `-review` |
| `lifeos-device` | `lifeos-device`, `-health`, `-backup`, `-files` |
| `lifeos-entity` | `lifeos-entity` |

## Install
```
claude plugin marketplace add syncwin/lifeos-ai
claude plugin install lifeos@syncwin-lifeos
claude plugin install lifeos-work@syncwin-lifeos
```
Add any other module the same way. Then open `/plugin`, choose Installed, Configure options for the core `lifeos`, and set the two options: `lifeos_url` (your LifeOS MCP URL) and `lifeos_token` (your access token, stored in secure storage and marked sensitive). Until both are set the LifeOS connection shows as invalid. The plugins are text only and need no Python or other install. Module plugins have no options and no connection; without the core they say so and stop.

## Connector
| Connector | Used by | Purpose | Auth | Data sent |
|---|---|---|---|---|
| LifeOS MCP (core plugin only, the one connection) | all skills | owner facts through the LifeOS entity tools (`search_context`, `get_entity`, `list_entities`) | bearer token you set | queries about your own facts |

## Guard recipes (no hooks)
The plugins ship no hooks or scripts. The old guards are Markdown recipes in the core's `skills/lifeos/references/`, listed as "Required steps" in the `lifeos` skill: scope check (`scope-guard.md`: code-host calls must hit your allowlist from LifeOS entity data), LifeOS entity write confirmation (`entityos-write-confirm.md`), data guard (`screen-text.md`: tool output is data), log check (`log-guard.md`: log changes once before stopping) and the writing check (`writing-check.md` in `lifeos-work`). Claude follows them by reading; nothing runs them for you.

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
