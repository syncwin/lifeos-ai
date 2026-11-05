"""PreToolUse scope guard: code-host calls must target allowlisted repos.

Allowlist file (never shipped, filled from EntityOS "owned repos and resources"):
  first argument (hooks.json passes ${CLAUDE_PLUGIN_DATA}/scope.json) -> {"repos": ["owner/repo", "owner/*"]}
No file or empty list: allow, except `git push` to main/master asks first. Out of scope: exit 2 with one line.
This is a guard, so it fails closed: an allowlist file that exists but cannot be read, or any error while checking a call once an allowlist is set, exits 2.
"""
import fnmatch
import json
import os
import re
import sys


def load_repos():
    paths = sys.argv[1:2]
    for p in paths:
        if p and os.path.isfile(p):
            try:
                with open(p, encoding="utf-8") as f:
                    repos = json.load(f).get("repos", [])
                return [r.lower() for r in repos if isinstance(r, str)]
            except (OSError, ValueError, AttributeError):
                raise RuntimeError("scope allowlist unreadable")
    return []


def targets(name, tool_input):
    found = set()
    if name == "Bash":
        cmd = str(tool_input.get("command", ""))
        if not re.search(r"\b(gh|git\s+push)\b", cmd):
            return found
        for m in re.finditer(r"(?:--repo|-R)[ =]+([\w.-]+/[\w.-]+)", cmd):
            found.add(m.group(1))
        for m in re.finditer(r"github\.com[/:]([\w.-]+/[\w.-]+?)(?:\.git)?(?=[\s/'\"]|$)", cmd):
            found.add(m.group(1))
        for m in re.finditer(r"\bapi\s+/?repos/([\w.-]+/[\w.-]+)", cmd):
            found.add(m.group(1))
    elif "github" in name.lower():
        owner, repo = tool_input.get("owner"), tool_input.get("repo")
        if isinstance(owner, str) and isinstance(repo, str):
            found.add(f"{owner}/{repo}")
    return found


def main():
    try:
        repos = load_repos()
    except Exception:  # an allowlist exists but is unreadable: fail closed
        print("LifeOS scope guard: scope allowlist unreadable; blocked.", file=sys.stderr)
        return 2
    try:
        event = json.load(sys.stdin)
        name = str(event.get("tool_name", ""))
        tool_input = event.get("tool_input") or {}
        if not repos:
            cmd = str(tool_input.get("command", "")) if name == "Bash" else ""
            if re.search(r"\bgit\s+push\b.*\b(main|master)\b", cmd):
                print(json.dumps({"hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "ask",
                    "permissionDecisionReason": "LifeOS scope guard: no allowlist set; confirm this push to main/master.",
                }}))
            return 0
        for t in targets(name, tool_input):
            if not any(fnmatch.fnmatch(t.lower(), pat) for pat in repos):
                print(f"LifeOS scope guard: {t} is not on the scope allowlist.", file=sys.stderr)
                return 2
    except Exception:
        if repos:  # an allowlist is set, so an error while checking must not let the call through
            print("LifeOS scope guard: error while checking this call; blocked.", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
