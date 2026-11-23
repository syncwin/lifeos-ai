# Log check before stopping (recipe)

Applies once per session, in a LifeOS session only (a LifeOS skill or a LifeOS entity tool was used), just before your final answer. No hook runs it; you check it yourself.

1. Find the last call that wrote a log row: a tool whose name matches `log_entry` or `lifeos` plus `log`, or `mcp__memory__save_progress`. Find the last file change: Write, Edit, MultiEdit or NotebookEdit.
2. If no file changed, or the last log call is after the last file change: nothing to do.
3. Otherwise log the work once (what, evidence, status) with the log tool or `mcp__memory__save_progress`, then end with the request ledger (`scratchpad.md`).
4. If no log tool is connected, say so in one line and note the work in the end-of-day report. Do not loop: do this at most once per session.
