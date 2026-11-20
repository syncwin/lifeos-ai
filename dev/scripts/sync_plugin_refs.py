#!/usr/bin/env python3
"""Copy the core's shared references into each module plugin's own references/ folder.

Usage: python -I -X utf8 dev/scripts/sync_plugin_refs.py [--check]
Reads dev/plugin-refs.json: {"core": <core references folder>, "plugins": {<folder under adapters/>: [<file>, ...]}}.
Without --check it copies. With --check it copies nothing and exits 1 when a copy is missing or differs, when a
plugin holds a core-named file its manifest entry does not list, when the manifest names an unknown plugin or
file, or when a `${CLAUDE_PLUGIN_ROOT}/references/<file>` pointer in a plugin does not resolve inside that plugin.
Maintainer tooling: never shipped.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ADAPTERS = ROOT / "adapters"
POINTER = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/references/([\w.\-]+)")


def rows(path):
    return [l.strip() for l in path.read_text(encoding="utf-8").splitlines() if re.match(r"\| \d+ \|", l)]


def router_rows(cfg):
    """A module router's routing rows must equal the core table rows whose skill lives in that module."""
    out = []
    core_rows = rows(ADAPTERS / "claude/skills/lifeos/SKILL.md")
    for plugin in sorted(cfg["plugins"]):
        router = ADAPTERS / plugin / "skills" / plugin / "SKILL.md"
        mine = rows(router) if router.is_file() else []
        if not mine:
            continue
        skills = {d.name for d in (ADAPTERS / plugin / "skills").iterdir() if d.is_dir()}
        want = [r for r in core_rows if re.findall(r"`([^`]+)`", r.strip("|").split("|")[2])[0] in skills]
        if want != mine:
            out.append(f"router rows differ: {plugin} routing table does not match the core table")
    return out


def main():
    check = "--check" in sys.argv[1:]
    cfg = json.loads((ROOT / "dev" / "plugin-refs.json").read_text(encoding="utf-8"))
    core = ROOT / cfg["core"]
    core_files = {p.name for p in core.glob("*.md")}
    problems, copied = [], 0
    for plugin, names in sorted(cfg["plugins"].items()):
        pdir = ADAPTERS / plugin
        if not pdir.is_dir():
            problems.append(f"manifest names unknown plugin {plugin}")
            continue
        refs = pdir / "references"
        for name in names:
            if name not in core_files:
                problems.append(f"manifest names {name} for {plugin}, which is not in the core")
                continue
            src, dst = core / name, refs / name
            data = src.read_bytes()
            if dst.is_file() and dst.read_bytes() == data:
                continue
            if check:
                problems.append(("drift: " if dst.exists() else "missing: ") + f"{plugin}/references/{name}")
            else:
                refs.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(data)
                copied += 1
        if refs.is_dir():
            for f in sorted(refs.glob("*.md")):
                if f.name in core_files and f.name not in names:
                    problems.append(f"stale: {plugin}/references/{f.name} is a core file the manifest does not list")
        for f in sorted(pdir.rglob("*.md")):
            for m in POINTER.finditer(f.read_text(encoding="utf-8")):
                if not (refs / m.group(1)).is_file():
                    problems.append(f"broken pointer: {f.relative_to(ROOT).as_posix()} -> references/{m.group(1)}")
    problems += router_rows(cfg)
    for p in sorted(set(problems)):
        print(p)
    if check:
        print("plugin references in sync" if not problems else f"{len(set(problems))} problem(s)")
        return 1 if problems else 0
    print(f"copied {copied} file(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
