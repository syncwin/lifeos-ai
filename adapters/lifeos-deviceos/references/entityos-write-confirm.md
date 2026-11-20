# EntityOS write confirmation (recipe)

Applies before every call to an EntityOS tool whose action part (the text after the second `__` in the tool name) starts with write, update, create, delete, put, remove, insert, upsert, patch or merge, in any letter case. Read tools such as `get_input_schema`, `list_output` or `compute_stats` do not match and need no confirmation.

1. Before the call, show what will be stored or changed: the entity, the fields, the old and new values (`risk-check.md` block).
2. Wait for an explicit yes from the user in chat. Do not make the call without it. No hook asks for you; you ask.
3. After a yes, make the call once; report what was stored.
