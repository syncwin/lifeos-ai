#!/usr/bin/env python3
"""Check the core router across all plugins: the Module routes table, then the Routing table, against dev/router-cases.json.

Usage: python -I -X utf8 dev/scripts/check_module_routes.py
The validator only lets the core's `Routing table` name skills that live in the core, so the rows for skills in the module
plugins sit in the `Module routes` section of adapters/claude/skills/lifeos/SKILL.md. Read together (module routes first, then
the Routing table; phrases match as whole words, first matching row wins, `!` excludes), they must send every case prompt in
dev/router-cases.json to its expected skill, or to `ask` when no row matches. Maintainer tooling: never shipped.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def section(text, title):
    m = re.search(r"^#{2,4}[^\n]*" + title + r"[^\n]*\n(.*?)(?=^#{1,4} |\Z)", text, re.M | re.S | re.I)
    return m.group(1) if m else ""


def parse(body):
    rows = []
    for line in body.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or not line.lstrip().startswith("|") or re.fullmatch(r"[-: ]+", cells[0]) or cells[0].lower() == "order":
            continue
        slugs = re.findall(r"`([^`]+)`", cells[2])
        if slugs:
            rows.append(([p.strip().lower() for p in cells[1].split(";") if p.strip()], slugs[0].split(":")[-1]))
    return rows


def route(rows, prompt):
    q = prompt.lower()
    has = lambda ph: re.search(r"(?<![\w])" + re.escape(ph) + r"(?![\w])", q)
    for phrases, slug in rows:
        if any(has(ph[1:]) for ph in phrases if ph.startswith("!")):
            continue
        if any(has(ph) for ph in phrases if not ph.startswith("!")):
            return slug
    return "ask"


def main():
    text = (ROOT / "adapters/claude/skills/lifeos/SKILL.md").read_text(encoding="utf-8")
    rows = parse(section(text, "Module routes")) + parse(section(text, "Routing table"))
    cases = json.loads((ROOT / "dev/router-cases.json").read_text(encoding="utf-8"))["cases"]
    bad = [f"'{c['prompt']}' routed to {route(rows, c['prompt'])}, expected {c['expected']}" for c in cases if route(rows, c["prompt"]) != c["expected"]]
    skills = {d.name for p in (ROOT / "adapters").iterdir() for d in (p / "skills").iterdir() if d.is_dir()} - {"lifeos"}
    for s in sorted(skills):
        if sum(1 for c in cases if c["expected"] == s) < 2:
            bad.append(f"skill {s} has fewer than 2 router cases")
    for s in sorted({slug for _, slug in rows} - skills):
        bad.append(f"routed slug {s} is not a skill folder in any plugin")
    for b in bad:
        print("FAIL", b)
    print(f"all {len(cases)} cases route as expected" if not bad else f"{len(bad)} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
