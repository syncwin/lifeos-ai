#!/usr/bin/env python3
"""Copy shared/ references into each skill's own references/ folder.

Usage: python -I -X utf8 scripts/sync_shared.py [--check]
Reads shared/manifest.json. Without --check, copies. With --check, copies nothing and
exits 1 when a copy is missing or differs, or a skill holds a shared file the manifest
does not list for it.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"
SKILLS = ROOT / "skills"


def plan():
    cfg = json.loads((SHARED / "manifest.json").read_text(encoding="utf-8"))
    all_skills = sorted(p.name for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())
    files = cfg["files"]
    want = {}
    problems = []
    for name, skills in files.items():
        if not (SHARED / name).is_file():
            problems.append(f"missing source shared/{name}")
            continue
        targets = all_skills if skills == ["*"] else skills
        for s in targets:
            if s not in all_skills:
                problems.append(f"manifest names unknown skill {s} for {name}")
                continue
            want[(s, name)] = SHARED / name
    for s in all_skills:
        ref = SKILLS / s / "references"
        for name in files:
            if (ref / name).exists() and (s, name) not in want:
                problems.append(f"stale: skills/{s}/references/{name} is not listed in the manifest")
    return want, problems


def main():
    check = "--check" in sys.argv[1:]
    want, problems = plan()
    copied = 0
    for (skill, name), src in sorted(want.items()):
        dst = SKILLS / skill / "references" / name
        data = src.read_bytes()
        if dst.is_file() and dst.read_bytes() == data:
            continue
        if check:
            problems.append(("drift: " if dst.exists() else "missing: ") + f"skills/{skill}/references/{name}")
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(data)
            copied += 1
    for p in problems:
        print(p)
    if check:
        print("shared copies in sync" if not problems else f"{len(problems)} problem(s)")
    else:
        print(f"copied {copied} file(s); {len(want)} targets")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
