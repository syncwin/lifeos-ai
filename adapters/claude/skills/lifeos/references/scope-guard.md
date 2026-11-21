# Scope check (recipe)

Applies before every Bash command that runs `gh` or `git push`, and every GitHub connector tool call (tool name contains "github"). No hook runs it; you perform it by reading the call before you make it.

## 1. Get the allowlist

Run `search_context("owned repos and resources")` in LifeOS entity data. The answer is a list of `owner/repo` patterns, where `*` matches any characters (for example `owner/*`). Compare case-insensitively. If the user keeps a `scope.json` (`{"repos": ["owner/repo"]}`) in a folder they name, read that too. A list you cannot read or understand counts as set but unusable: see section 4.

## 2. Work out the targets of the call

- Bash: repo after `--repo` or `-R`; `github.com/<owner>/<repo>` or `github.com:<owner>/<repo>` in a URL or remote (without `.git`); `api repos/<owner>/<repo>` (or `api /repos/...`).
- GitHub connector: the `owner` and `repo` arguments.
- A command with no `gh` and no `git push`, or a call with no target, has nothing to check.

## 3. Decide

- Allowlist empty or none stored: allow, except `git push` toward `main` or `master`: stop and ask the user to confirm that push first ("no allowlist set; confirm this push to main/master").
- Allowlist set: every target must match a pattern. If one does not, do not make the call; tell the user in one line: "<owner/repo> is not on the scope allowlist."

## 4. Fail closed

With an allowlist set, an unreadable list, or any doubt about what the call targets, do not make the call. Say so in one line and ask.
