#!/usr/bin/env python3
"""Deterministic draft checker for workos-writing, built from references/patterns.md.

Usage: python -I -X utf8 check_draft.py <draft.md|txt> [--ban "term,term"] [--patterns <patterns.md>]
Prints one line per check: PASS, WARN, FAIL or SKIP, with line numbers. Exit 1 if any FAIL.
Checks: length, sentence length, paragraph length, heading structure, FAQ block (SKIP when the
draft has none), banned phrases by pattern number, extra banned terms (pattern 10).
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_rules(path):
    phrases, limits = {}, {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"phrases (\d+):\s*(.+)$", line)
        if m:
            phrases[int(m.group(1))] = [p.strip() for p in m.group(2).split("|") if p.strip()]
        m = re.match(r"limit (\w+):\s*(\d+)\s*$", line)
        if m:
            limits[m.group(1)] = int(m.group(2))
    return phrases, limits


def find_phrase(lines, phrase):
    pat = re.compile(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", re.I)
    return [i + 1 for i, l in enumerate(lines) if pat.search(l)]


def fmt_hits(hits):
    return "; ".join('"%s" line %s' % (p, ", ".join(map(str, ls))) for p, ls in hits)


def main(argv):
    if not argv or argv[0].startswith("--"):
        print('usage: check_draft.py <draft> [--ban "a,b"] [--patterns file]')
        return 2
    draft = Path(argv[0])
    ban, patterns = [], HERE.parent / "references" / "patterns.md"
    rest = argv[1:]
    while rest:
        k = rest.pop(0)
        if k == "--ban" and rest:
            ban = [b.strip() for b in rest.pop(0).split(",") if b.strip()]
        elif k == "--patterns" and rest:
            patterns = Path(rest.pop(0))
    if not draft.is_file():
        print("FAIL file: %s not found" % draft)
        return 2
    phrases, limits = load_rules(patterns)
    text = draft.read_text(encoding="utf-8")
    lines = text.splitlines()
    out = []

    words = len(re.findall(r"\b[\w'-]+\b", text))
    mw = limits.get("max_words", 1200)
    out.append(("PASS" if words <= mw else "FAIL", "length: %d words (max %d)" % (words, mw)))

    msw = limits.get("max_sentence_words", 35)
    long_s = []
    for i, l in enumerate(lines):
        if l.lstrip().startswith(("#", "|", "```")):
            continue
        for s in re.split(r"(?<=[.!?])\s+", l):
            if len(s.split()) > msw:
                long_s.append(i + 1)
    out.append(("PASS" if not long_s else "WARN", "sentence length (max %d words): %s" % (msw, ", ".join("line %d" % n for n in sorted(set(long_s))) or "none over")))

    mpl = limits.get("max_paragraph_lines", 8)
    runs, cur, start = [], 0, 0
    for i, l in enumerate(lines + [""]):
        if l.strip() and not l.lstrip().startswith(("#", "|", "-", "*")):
            if cur == 0:
                start = i + 1
            cur += 1
        else:
            if cur > mpl:
                runs.append(start)
            cur = 0
    out.append(("PASS" if not runs else "WARN", "paragraph length (pattern 9, max %d lines): %s" % (mpl, ", ".join("line %d" % n for n in runs) or "none over")))

    heads = []
    for i, l in enumerate(lines):
        m = re.match(r"(#{1,6})\s+(.*\S)", l)
        if m:
            heads.append((i + 1, len(m.group(1)), m.group(2)))
    if not heads:
        out.append(("SKIP", "headings: draft has none"))
    else:
        bad = []
        h1 = [n for n, lv, _ in heads if lv == 1]
        if len(h1) > 1:
            bad.append("more than one H1 at " + ", ".join("line %d" % n for n in h1))
        prev = 0
        for n, lv, _ in heads:
            if prev and lv > prev + 1:
                bad.append("line %d skips from H%d to H%d" % (n, prev, lv))
            prev = lv
        seen = {}
        for n, _, tx in heads:
            if tx.lower() in seen:
                bad.append("line %d repeats heading from line %d" % (n, seen[tx.lower()]))
            seen.setdefault(tx.lower(), n)
        out.append(("PASS" if not bad else "FAIL", "headings (pattern 9): " + ("; ".join(bad) or "consistent")))

    faq = [n for n, _, tx in heads if "faq" in tx.lower() or "frequently asked" in tx.lower()]
    if not faq:
        out.append(("SKIP", "FAQ block: none in draft"))
    else:
        qs = [l for l in lines[faq[0]:] if l.strip().rstrip("*").endswith("?")]
        out.append(("PASS" if len(qs) >= 2 else "WARN", "FAQ block at line %d: %d question(s)" % (faq[0], len(qs))))

    for num in sorted(phrases):
        hits = [(p, find_phrase(lines, p)) for p in phrases[num]]
        hits = [(p, ls) for p, ls in hits if ls]
        if hits:
            out.append(("WARN", "pattern %d: %s" % (num, fmt_hits(hits))))
        else:
            out.append(("PASS", "pattern %d: no banned phrases" % num))

    if ban:
        hits = [(p, find_phrase(lines, p)) for p in ban]
        hits = [(p, ls) for p, ls in hits if ls]
        if hits:
            out.append(("FAIL", "pattern 10 (owner banned terms): " + fmt_hits(hits)))
        else:
            out.append(("PASS", "pattern 10 (owner banned terms): none found"))
    else:
        out.append(("SKIP", 'pattern 10: no --ban terms given (read them from search_context("voice"))'))

    for status, msg in out:
        print("%s %s" % (status, msg))
    failed = any(s == "FAIL" for s, _ in out)
    warned = any(s == "WARN" for s, _ in out)
    print("RESULT: " + ("FAIL" if failed else "WARN" if warned else "PASS"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
