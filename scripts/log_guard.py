"""Stop log guard: if files or records changed after the last log row, ask once to log.

Log tool name pattern: first argument (regex; default matches tool names with log_entry or lifeos..log).
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
                    yield str(block.get("name", ""))


def main():
    try:
        event = json.load(sys.stdin)
        if event.get("stop_hook_active"):
            return 0
        path = event.get("transcript_path")
        if not path or not os.path.isfile(path):
            return 0
        pattern = re.compile((sys.argv[1] if len(sys.argv) > 1 else r"log_?entr|lifeos.*log"), re.I)
        last_change = last_log = -1
        for i, name in enumerate(tool_uses(path)):
            if pattern.search(name):
                last_log = i
            elif name in CHANGE_TOOLS:
                last_change = i
        if last_change > last_log:
            print(json.dumps({
                "decision": "block",
                "reason": "Files changed after the last log row. Log the work once (what, evidence, status), then end with the request ledger.",
            }))
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
