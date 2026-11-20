# Improvements

Log feedback and ideas here; move to Accepted when approved.

## Inbox
Format: date · idea · source

- 2026-11-04 · Budget guard for scrapers (balance, estimate, stop floor) · plan Block 1
- 2026-11-15 · pending: EntityOS records (see retention plan, G4): compliance-and-sourcing rules, dates-in-content decision, AI-usage and editorial-disclosure rule, credential and ranking claim rule, voice bans, pre-publish self-check SOP, and the brand-voice, persona, authoritative-sources, writing-patterns and business-unit example templates -> EntityOS policy, SOP and context records · strategist port

## Accepted

## Done
- 2026-11-15 | Strategist port gaps closed in 0.4.0: G1 audit-methods (S100 to S110) -> `lifeos-workos/references/audit-methods.md`; G2 patterns intake protocol and seed patterns (S136, S137) -> `lifeos-workos-writing/references/patterns.md`; G3 onboarding steps and sources research method (S140, S146, S147, S149) -> `lifeos-entityos/references/add-client.md`; G5 prompt guidance (S016, S018, S020, S021) -> `prompts/lifeos.json`, router and `lifeos-workos`; G7 evals (S169); S138 patterns start empty; tracker spec rewritten for the one LifeOS task store | strategist port | Done in 0.4.0
- 2026-11-05 | Security first (enterprise level): never break existing behaviour (tests + review before merge); secure-by-default foundation for every project: secret scanning, least-privilege tokens, dependency pinning/audit (supply chain), input validation, signed releases, threat model in each brief, Critical/Important security findings block release. | User | Done in 0.2.1
- 2026-11-15 | Store guard hook (block destructive SQL, wildcard selects) | plan Block 1 | not needed: the Worker runs only fixed parameterized SQL and has no raw-SQL tool (worker src/db.ts); revisit if one is added
- 2026-11-15 | Draft, link, contrast and image check scripts for `workos-writing` | plan Block 1 | covered by the lifeos-workos-writing references/writing-check.md recipe; the Python checker stays in dev/
- 2026-11-15 | Wire module switches to the LifeOS MCP `list_modules` tool | plan Block 1 | done in 0.3.1

## Follow-up: multi-platform converter (decided 2026-11-20)
LifeOS should work from Claude, Codex, Grok, Hermes Agent and other platforms through one remote MCP server. Workflows are written once in plain Markdown. A build step converts them into each platform's format. As of 0.5.0, skill bodies avoid Claude-only wording. Three Claude-specific items are left for the converter to rewrite, because the Claude directory validator requires them: the `${CLAUDE_PLUGIN_ROOT}` reference paths, the "Skill tool" loader line in the 4 routers (rule P026), and the frontmatter/plugin.json packaging.
