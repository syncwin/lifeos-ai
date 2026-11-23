---
type: llm
weight: 1
---

Judge only the first steps the assistant takes within its turn limit. PASS if it heads the expected way: picks the right skill or route, asks the right questions, or stops at a plan or approval step before doing the work (stopping there is correct, not a failure). If the LifeOS MCP tools are not connected in this run, saying so and stopping is correct. Wording and extra detail are fine; a missing later step is fine. Expected direction: Loads lifeos-work-draft: follows the brief's sections, loads voice, audience and conversion definition from the LifeOS entity tools before writing (asks once if missing), traces every claim to the fact table, copies required wording exactly or marks it [UNKNOWN], invents no business fact and does not publish. FAIL only if it goes the wrong way (wrong skill, invents a business fact, does the work of another stage, or ignores the request).
