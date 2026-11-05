"""Stop log guard: if files or records changed after the last log row, ask once to log.

Log tool name pattern: first argument (regex; default matches tool names with log_entry or lifeos..log).
Only fires in sessions that used LifeOS (a lifeos/entityos tool or skill), at most once per
session (state file in the first non-flag argument's folder or CLAUDE_PLUGIN_DATA).
Never blocks twice in a row (stop_hook_active) and never blocks on bad input.
"""
import json
import os
import re
import sys

CHANGE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}


def tool_uses(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            try:
                msg = json.loads(line).get("message") or {}
            except ValueError:
                continue
            content = msg.get("content")
            if msg.get("role") != "assistant" or not isinstance(content, list):
                continue
            for block in content:
                if isinstance(block, dict) and block.get("type") == "tool_use":
                    yield str(block.get("name", "")), json.dumps(block.get("input") or {})


def main():
    try:
        event = json.load(sys.stdin)
        if event.get("stop_hook_active"):
            return 0
        path = event.get("transcript_path")
        if not path or not os.path.isfile(path):
            return 0
        pattern = re.compile((sys.argv[1] if len(sys.argv) > 1 else r"log_?entr|lifeos.*log"), re.I)
        lifeos = re.compile(r"lifeos|entityos", re.I)
        used = False
        last_change = last_log = -1
        for i, (name, args) in enumerate(tool_uses(path)):
            if lifeos.search(name) or (name == "Skill" and lifeos.search(args)):
                used = True
            if pattern.search(name):
                last_log = i
            elif name in CHANGE_TOOLS:
                last_change = i
        if not used or last_change <= last_log:
            return 0
        data = os.environ.get("CLAUDE_PLUGIN_DATA") or os.path.dirname(path)
        state = os.path.join(data, "log_guard_seen.txt")
        sid = str(event.get("session_id") or path)
        seen = open(state, encoding="utf-8").read().split() if os.path.isfile(state) else []
        if sid in seen:
            return 0
        os.makedirs(data, exist_ok=True)
        with open(state, "a", encoding="utf-8") as f:
            f.write(sid + "\n")
        print(json.dumps({
                "decision": "block",
                "reason": "Files changed after the last log row. LifeOS: log the work once (what, evidence, status) with the log tool if connected, else in the end-of-day report; then end with the request ledger.",
            }))
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
