# Module list
Use at the module switch (router Gate step 1) to learn which modules are enabled.

1. If the LifeOS MCP tool `lifeos_list_modules` is available, call it once per session (read-only, no arguments) and reuse the result for every later module check in that session. It returns `owner` and `modules` (id, name, description) for enabled modules only.
2. A module missing from the result is disabled: decline it and name it, never delete it.
3. If the tool is not available or the call fails, fall back to the current method: ask once which modules are on.
