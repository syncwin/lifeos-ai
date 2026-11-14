"""Stop log guard: if files changed after the last log row, ask once to log.

Runs only in LifeOS sessions (a lifeos/entityos tool or a LifeOS skill was used in the transcript).
Blocks at most once per session (marker file keyed by session_id in the temp dir).
Log tools: first argument (regex; default log_entry / lifeos..log) plus mcp__memory__save_progress.
If no log tool is visible in the transcript, warns once and does not block.
Fails open on every error.
"""
import hashlib
import json
import os
import re
import sys
import tempfile

CHANGE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
DEFAULT_LOG = r"log_?entr|lifeos.*log"
MEMORY_LOG = r"^mcp__memory__save_progress$"
LIFEOS_TOOL = re.compile(r"lifeos|entityos", re.I)
LIFEOS_SKILL = re.compile(r"^(lifeos[:\-]|lifeos$|(workos|selfos|deviceos|moneyos)-)", re.I)


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
                    yield str(block.get("name", "")), block.get("input") or {}


def is_lifeos(name, args):
    if name == "Skill":
        skill = args.get("skill") if isinstance(args, dict) else ""
        return bool(LIFEOS_SKILL.search(str(skill or "")))
    return name.startswith("mcp__") and bool(LIFEOS_TOOL.search(name))


def first_time(session_id):
    """True the first time this session is seen (atomic marker file); fail open elsewhere."""
    d = os.path.join(tempfile.gettempdir(), "lifeos-log-guard")
    os.makedirs(d, exist_ok=True)
    marker = os.path.join(d, hashlib.sha256(session_id.encode("utf-8", "replace")).hexdigest()[:32])
    try:
        os.close(os.open(marker, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
        return True
    except FileExistsError:
        return False


def main():
    try:
        event = json.load(sys.stdin)
        if event.get("stop_hook_active"):
            return 0
        path = event.get("transcript_path")
        if not path or not os.path.isfile(path):
            return 0
        pattern = re.compile((sys.argv[1] if len(sys.argv) > 1 else DEFAULT_LOG) + "|" + MEMORY_LOG, re.I)
        used = False
        last_change = last_log = -1
        for i, (name, args) in enumerate(tool_uses(path)):
            if is_lifeos(name, args):
                used = True
            if pattern.search(name):
                last_log = i
            elif name in CHANGE_TOOLS:
                last_change = i
        if not used or last_change <= last_log:
            return 0
        sid = str(event.get("session_id") or path)
        if not first_time(sid):
            return 0
        with open(path, encoding="utf-8", errors="replace") as f:
            raw = f.read()
        # A log tool is "available" if its name appears anywhere in the transcript (tool list or earlier call).
        available = re.search(r"mcp__[A-Za-z0-9_\-]*(" + pattern.pattern + ")", raw, re.I) or "mcp__memory__save_progress" in raw
        if not available:
            print(json.dumps({"systemMessage": "LifeOS: files changed but no log tool is connected; note the work in the end-of-day report."}))
            return 0
        print(json.dumps({
            "decision": "block",
            "reason": "Files changed after the last log row. LifeOS: log the work once (what, evidence, status) with the log tool (or mcp__memory__save_progress), then end with the request ledger.",
        }))
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
