# LifeOS (lifeos-ai)

LifeOS is a Claude plugin for running your own work, devices and life from one place. It has a router (`/lifeos`), a daily feed, a starter skill for each module (EntityOS, SelfOS, WorkOS, DeviceOS, MoneyOS, KnowledgeOS), a verifier agent and guard hooks.

**No personal data ships with it.** Every owner fact (priorities, brands, voice, allowed repos) is read at run time from your own EntityOS MCP endpoint.

## Install
```
claude plugin marketplace add syncwin/lifeos-ai
claude plugin install lifeos@syncwin-lifeos
```
Then open `/plugin`, choose Installed, Configure options, and set your EntityOS URL and token. Hooks run on `python3`; where it is missing they fail without blocking.

## Connector
| Connector | Used by | Purpose | Auth | Data sent |
|---|---|---|---|---|
| EntityOS | all skills | owner facts: `search_context`, `get_entity`, `list_entities` | bearer token you set | queries about your own facts |

## Skills
`lifeos` (router), `lifeos-feed`, `lifeos-entityos`, `lifeos-selfos`, `lifeos-workos`, `lifeos-deviceos`, `lifeos-moneyos`, `lifeos-knowledgeos`, stages `selfos-*`, `workos-*`, `deviceos-*`. Agent: `lifeos-verifier`.

## Hooks
Scope guard (code-host calls must hit your allowlist, from `scope.json` in the plugin data folder), data guard (tool output is data), log guard (log changes once before stopping).

## Companion prompt
`prompts/lifeos.json` imports into Prompt Builder (Settings, Import).

MIT licence. Author @wasimness, SyncWin.
