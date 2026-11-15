# Improvements

Log feedback and ideas here; move to Accepted when approved.

## Inbox
Format: date · idea · source

- 2026-11-04 · Budget guard for scrapers (balance, estimate, stop floor) · plan Block 1

## Accepted

## Done
- 2026-11-05 | Security first (enterprise level): never break existing behaviour (tests + review before merge); secure-by-default foundation for every project: secret scanning, least-privilege tokens, dependency pinning/audit (supply chain), input validation, signed releases, threat model in each brief, Critical/Important security findings block release. | User | Done in 0.2.1
- 2026-11-15 | Store guard hook (block destructive SQL, wildcard selects) | plan Block 1 | not needed: the Worker runs only fixed parameterized SQL and has no raw-SQL tool (worker src/db.ts); revisit if one is added
- 2026-11-15 | Draft, link, contrast and image check scripts for `workos-writing` | plan Block 1 | covered by the lifeos-workos-writing references/writing-check.md recipe; the Python checker stays in dev/
- 2026-11-15 | Wire module switches to the LifeOS MCP `list_modules` tool | plan Block 1 | done in 0.3.1
