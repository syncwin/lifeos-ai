# EntityOS offline
Use when the EntityOS connector is missing, or its cheapest call (`search_context("priorities")`) fails twice in a row.

1. Stop calling EntityOS. Do not retry a third time.
2. Ask once: "EntityOS is not reachable. Do you want a manual step-by-step pack instead? It lists what to do by hand, without your stored facts." Wait for the answer.
3. Yes: give the manual pack for the request (numbered steps the owner can do alone, each needing no owner fact from EntityOS). No: say how to fix it (set the EntityOS URL and token under plugin options) and offer to continue without owner facts.
4. Continue the work without owner facts. Never invent one: priorities, brands, people, paths, policies, voice and limits are [UNKNOWN] until the owner types them in this chat. Typed answers are used for this run only and flagged as unverified.
5. Do not run steps that need an owner fact to be safe (for example moves, restores, money). List them as proposed tasks.
6. The scratchpad flags: "EntityOS offline; owner facts unverified".
