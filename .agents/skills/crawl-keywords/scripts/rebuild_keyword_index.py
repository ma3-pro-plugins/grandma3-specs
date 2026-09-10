#!/usr/bin/env python3
"""Rebuild specs/keywords/_index.md and options/_index.md.

Columns: Keyword (linked) + short Official description. No shortcuts column.
Run from repo root after a keyword crawl.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path("specs/keywords")
MAX_DESC = 160


def frontmatter_keyword(text: str) -> str | None:
    m = re.search(r'(?m)^keyword:\s*"([^"]+)"\s*$', text)
    return m.group(1) if m else None


def clean_prose(body: str) -> str:
    body = re.split(r"(?m)^\s*\|", body, maxsplit=1)[0]
    body = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", body)
    body = re.sub(r"\[\]\([^)]*\)", "", body)
    body = re.sub(r"[*_`]+", "", body)
    body = re.sub(r"(?m)^\s*[-*]\s+.*$", " ", body)
    body = re.sub(r"-{3,}|={3,}", " ", body)
    body = re.sub(r"\s+", " ", body).strip()
    return body


def extract_description(text: str) -> str:
    # ### Description (optional leading spaces / odd heading)
    m = re.search(
        r"(?ims)^###\s*Description\s*\n+(.*?)(?=^###\s|\n##\s|\Z)",
        text,
    )
    if m:
        body = clean_prose(m.group(1))
        if body:
            return body

    # Bare "Description" line (some symbol pages)
    m = re.search(
        r"(?ims)^Description\s*\n+(.*?)(?=^###\s|^##\s|^\|\s|\Z)",
        text,
    )
    if m:
        body = clean_prose(m.group(1))
        if body:
            return body

    # ## … Keyword section
    m = re.search(r"(?ims)^##\s+[^\n]*Keyword\s*\n+(.*?)(?=^##\s|\Z)", text)
    if m:
        for p in re.split(r"\n\s*\n", m.group(1)):
            c = clean_prose(p)
            if len(c) < 25:
                continue
            low = c.lower()
            if low.startswith("to enter") or "malighting.com" in low:
                continue
            return c

    om = re.search(r"(?ms)^## Official\s*\n(.*?)(?=^## |\Z)", text)
    if om:
        for p in re.split(r"\n\s*\n", om.group(1)):
            c = clean_prose(p)
            if len(c) < 25:
                continue
            low = c.lower()
            if low.startswith("to enter") or "type the shortcut" in low:
                continue
            if "malighting.com" in low or low.startswith("grandma3 user manual"):
                continue
            return c
    return ""


def summarize(desc: str, keyword: str) -> str:
    if not desc:
        return "No Official description in the Target manual page."
    # Prefer first sentence; if it ends with ':' (lead-in to a table), keep that clause
    m = re.match(r"^(.+?[.!?])(\s|$)", desc)
    if m:
        first = m.group(1).strip()
    else:
        # lead-in ending with colon before a list/table
        m2 = re.match(r"^(.+?:)\s*", desc)
        first = m2.group(1).strip() if m2 else desc.strip()
        if first.endswith(":"):
            first = first[:-1].rstrip() + "."
    if len(first) < 25 and "." in desc[len(first) :]:
        m3 = re.match(r"^(.+?[.!?])\s+(.+?[.!?])", desc)
        if m3:
            first = (m3.group(1) + " " + m3.group(2)).strip()
    if len(first) <= MAX_DESC:
        out = first
    else:
        cut = first[: MAX_DESC - 1]
        if " " in cut:
            cut = cut.rsplit(" ", 1)[0]
        out = cut.rstrip(".,;:") + "…"
    return out.replace("|", "\\|")


def rows_for(dirpath: Path) -> list[tuple[str, str, str]]:
    rows = []
    for p in sorted(dirpath.glob("*.md")):
        if p.name.startswith("_"):
            continue
        text = p.read_text(errors="replace")
        kw = frontmatter_keyword(text) or p.stem
        desc = summarize(extract_description(text), kw)
        rows.append((kw, p.name, desc))
    rows.sort(key=lambda r: (r[0].lstrip("/").lower(), r[0]))
    return rows


def write_general(rows_g: list, rows_o: list) -> None:
    lines = [
        "# Keyword Specs",
        "",
        f"Live dictionary for **Target** ([`../versions.md`](../versions.md)): "
        f"**{len(rows_g)} general** + **{len(rows_o)} option** Specs from the grandMA3 **2.5** HTML manual.",
        "Layout: [`CONTEXT.md`](../../CONTEXT.md). Shortcuts live in each Spec’s frontmatter — not listed here.",
        "",
        "Descriptions are short Official blurbs so agents can pick the right keyword.",
        "",
        "## General",
        "",
        "| Keyword | Description |",
        "| --- | --- |",
    ]
    for kw, fname, desc in rows_g:
        lines.append(f"| [`{kw}`]({fname}) | {desc} |")
    lines += [
        "",
        "## Option keywords",
        "",
        "Full list with descriptions: [`options/_index.md`](options/_index.md).",
        "",
        "| Keyword | Description |",
        "| --- | --- |",
    ]
    for kw, fname, desc in rows_o:
        lines.append(f"| [`{kw}`](options/{fname}) | {desc} |")
    lines.append("")
    (ROOT / "_index.md").write_text("\n".join(lines) + "\n")


def write_options(rows_o: list) -> None:
    lines = [
        "# Option Keyword Specs",
        "",
        f"**{len(rows_o)} option** keywords for Target ([`../../versions.md`](../../versions.md)). "
        "See also [`../_index.md`](../_index.md).",
        "Shortcuts live in each Spec’s frontmatter — not listed here.",
        "",
        "| Keyword | Description |",
        "| --- | --- |",
    ]
    for kw, fname, desc in rows_o:
        lines.append(f"| [`{kw}`]({fname}) | {desc} |")
    lines.append("")
    (ROOT / "options" / "_index.md").write_text("\n".join(lines) + "\n")


def main() -> int:
    if not ROOT.is_dir():
        sys.stderr.write("Run from repo root (missing specs/keywords/)\n")
        return 2
    rows_g = rows_for(ROOT)
    rows_o = rows_for(ROOT / "options")
    write_general(rows_g, rows_o)
    write_options(rows_o)
    empty = sum(1 for *_, d in rows_g + rows_o if d.startswith("No Official"))
    print(f"Wrote indexes: {len(rows_g)} general + {len(rows_o)} option ({empty} empty Official)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
