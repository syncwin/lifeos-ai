#!/usr/bin/env python3
"""Fail when the plugins in this repo differ from the app's module registry (dev/module-registry.json).

Usage: python -I -X utf8 dev/scripts/check_module_registry.py
Checks: adapters/ holds the core folder plus one adapters/lifeos-<id> per plugin module and nothing else; the
marketplace lists exactly the core plugin and lifeos-<id> per plugin module, each source pointing at its folder; every
plugin.json name matches its marketplace entry; the core has one skill lifeos-<id> per core module; every module
plugin has the starter skill lifeos-<id>. Maintainer tooling: never shipped.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ADAPTERS = ROOT / "adapters"


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def main():
    reg = load(ROOT / "dev" / "module-registry.json")
    core, core_dir = reg["core_plugin"], reg["core_folder"]
    want_dirs = {core_dir} | {f"lifeos-{m}" for m in reg["plugin_modules"]}
    have_dirs = {d.name for d in ADAPTERS.iterdir() if d.is_dir()}
    problems = []
    for d in sorted(want_dirs - have_dirs):
        problems.append(f"registry module has no plugin folder: adapters/{d}")
    for d in sorted(have_dirs - want_dirs):
        problems.append(f"plugin folder not in the module registry: adapters/{d}")
    market = {p["name"]: p for p in load(ROOT / ".claude-plugin" / "marketplace.json")["plugins"]}
    want_names = {core} | {f"lifeos-{m}" for m in reg["plugin_modules"]}
    for n in sorted(want_names - set(market)):
        problems.append(f"marketplace is missing plugin {n}")
    for n in sorted(set(market) - want_names):
        problems.append(f"marketplace lists plugin {n}, which is not in the module registry")
    for n, p in sorted(market.items()):
        folder = core_dir if n == core else n
        if p.get("source") != f"./adapters/{folder}":
            problems.append(f"marketplace source of {n} is {p.get('source')}, want ./adapters/{folder}")
        mf = ADAPTERS / folder / ".claude-plugin" / "plugin.json"
        if mf.is_file():
            if load(mf).get("name") != n:
                problems.append(f"{mf.relative_to(ROOT).as_posix()} name differs from marketplace entry {n}")
            if load(mf).get("version") != p.get("version"):
                problems.append(f"{n}: plugin.json version differs from the marketplace version")
    for m in reg["core_modules"]:
        if not (ADAPTERS / core_dir / "skills" / f"lifeos-{m}" / "SKILL.md").is_file():
            problems.append(f"core module {m} has no skill adapters/{core_dir}/skills/lifeos-{m}")
    for m in reg["plugin_modules"]:
        if not (ADAPTERS / f"lifeos-{m}" / "skills" / f"lifeos-{m}" / "SKILL.md").is_file():
            problems.append(f"module {m} has no starter skill lifeos-{m}")
    for p in problems:
        print(p)
    print("plugin list matches the module registry" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
