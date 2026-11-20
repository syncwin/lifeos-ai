---
name: lifeos-workos-review
description: "Final review gate for a finished draft, for LifeOS WorkOS: QA, compliance and a fact-lock check. Use when the user says \"final review\", \"is this ready to publish\", \"fact-lock\", \"QA gate\", or \"compliance check\". Fixes only what fails; never rewrites from scratch."
license: MIT
---

# WorkOS Review
Needs: EntityOS MCP; the draft, its brief and its fact table.
For workos review, the core `lifeos` plugin is required: if its MCP tools are missing, say so and stop.
Start: run the `lifeos` router first if it has not run.

1. Pass 0: confirm the humanize pass ran on the whole draft. Cold draft: run it now. Tool missing: say so, apply the fallback, record the substitution; never mark it passed.
2. Pass A, compliance loop, one category at a time until all are clean: brief and structure, voice and point of view (`search_context("voice")`), plain language, accuracy, required wording, links and closing action, grammar, entity facts, then the pattern check (`lifeos-workos-writing`).
3. Fact-lock gate: every number, name, date, quote and claim in the draft is compared with the fact table and with EntityOS. A mismatch or a claim with no source is a FAIL, listed with its line. A claim backed by stored facts cites the claim ID; no claim, answer [UNKNOWN].
4. Compliance gate: regulator-required clauses, disclaimers and jurisdiction scope match the stored claims word for word (`search_context("regulator, required clauses, exclusions")`). Excluded topics must not appear.
5. Pass B, a separate reader pass: could someone with no background explain every part and the next step? Also check repeats, links and meta. Only then is the draft clean.
6. Fix only what failed, as targeted edits. Editing the draft file needs a filled `${CLAUDE_PLUGIN_ROOT}/references/risk-check.md` block; keep a copy of the pre-edit text.
7. A decision only the owner can make is surfaced as one flagged item, not buried. Detector or plagiarism reports are flagged for the owner, never self-passed.
8. Deliver exactly the two review files from `${CLAUDE_PLUGIN_ROOT}/references/writing-standards.md`; no third file.

## Done check
Graded by the `lifeos-verify` agent plus the common Done check lines.
- Pass 0, Pass A, the fact-lock and compliance gates and Pass B each have a result; any FAIL names its line.
- Every fact check cites a fact-table row or claim ID, or says [UNKNOWN]; exactly two review files were delivered.

## Handoff
Delivered: A pass or fail verdict per gate, targeted fixes, and the two review files.
Next: independent check -> `lifeos-verify`; published later -> `lifeos-workos-results`.

Scratchpad: end per `${CLAUDE_PLUGIN_ROOT}/references/scratchpad.md`.
