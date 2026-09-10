#!/usr/bin/env python3
"""Convert grandMA3 release-notes PDF to searchable Markdown.

Requires: pypdf (pip install pypdf)
Uses layout extraction mode for better word spacing than default extract_text().
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    print(
        "Missing dependency: pypdf\n"
        "Install in a venv, e.g.:\n"
        "  python3 -m venv .venv-pdf && .venv-pdf/bin/pip install pypdf\n"
        "  .venv-pdf/bin/python pdf-to-md.py --input Release_Notes_v2.4.pdf",
        file=sys.stderr,
    )
    sys.exit(1)

MAIN_SECTIONS = {
    "1": "Features",
    "2": "Other Enhancements",
    "3": "Changes",
    "4": "Bug Fixes",
    "5": "Deprecated",
    "6": "Appendix",
    "7": "Known Limitations",
}

FEATURE_H3 = {
    "Phaser Recipes and Shapes",
    "Presets",
    "MIDI Show Control (MSC)",
    "Preview",
    "Improved MVR and Partial Show Read",
    "Phone Tethering via USB",
}

BUG_CATEGORIES = {
    "3D",
    "Command Line and Macro",
    "Connections",
    "Patch",
    "Phaser",
    "Playback",
    "Windows, Views, and Menus",
}

CALLOUTS = {"Hint:", "Important:", "Known Limitation:", "Restriction:", "Requirement:"}
SKIP_LINES = {"Table of Contents", "Let's Get Started", "Release Notes 2.4"}


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def is_noise_line(s: str) -> bool:
    if not s.strip():
        return False
    if re.search(r"malighting\.com|Waldbüttelbrunn|Dachdeckerstr", s, re.I):
        return True
    if norm(s) in SKIP_LINES:
        return True
    if re.match(r"^(2026-05-18|English)$", norm(s)):
        return True
    if re.match(r"^Version 2\.4 \| 2026-05-18", norm(s)):
        return True
    if re.match(r"^Page\s*\d+\s*of\s*\d+", norm(s), re.I):
        return True
    if re.search(r"\.{8,}\s*\d+\s*$", s):
        return True
    return False


def light_cleanup(s: str) -> str:
    s = norm(s.replace("\t", " "))
    for pat, repl in [
        (r"\binthe\b", "in the"),
        (r"\binfront\b", "in front"),
        (r"\btitlebar\b", "title bar"),
        (r"\ballattributes\b", "all attributes"),
        (r"\ballfixtures\b", "all fixtures"),
        (r"\bifyou\b", "if you"),
        (r"\bIfthe\b", "If the"),
        (r"\bIfa\b", "If a"),
        (r"\bIfall\b", "If all"),
        (r"\bifthere\b", "if there"),
        (r"\bifthe\b", "if the"),
        (r"\ballthe\b", "all the"),
        (r"\ballstations\b", "all stations"),
        (r"\bforexample\b", "for example"),
        (r"\bisdeprecated\b", "is deprecated"),
        (r"\binstallprocess\b", "install process"),
        (r"\bshowfiles\b", "show files"),
        (r"\bleftside\b", "left side"),
        (r"\bpriorityover\b", "priority over"),
        (r",which\b", ", which"),
    ]:
        s = re.sub(pat, repl, s, flags=re.I)
    return s


def heading_level(s: str):
    s = norm(s)
    m = re.match(r"^(\d+)\.\s+(.+)$", s)
    if m:
        num, title = m.group(1), norm(m.group(2))
        if num in MAIN_SECTIONS and title == MAIN_SECTIONS[num]:
            return 2
        return None
    if s in FEATURE_H3:
        return 3
    if s in BUG_CATEGORIES:
        return 3
    if s == "Description":
        return 4
    if re.match(r"^(Added|Improved|New)\b", s) and len(s) < 100 and not s.endswith("."):
        return 4
    if s == "Updated predefined content:":
        return 4
    return None


def format_callout(label: str, body: list[str]) -> list[str]:
    return [f"> **{label.rstrip(':')}:** {light_cleanup(' '.join(body))}", ""]


def convert_bullet(s: str) -> str:
    s = s.strip()
    if s.startswith("·") or s.startswith("•"):
        return "- " + light_cleanup(s[1:].strip())
    if re.match(r"^o\s+", s):
        return "  - " + light_cleanup(s[2:].strip())
    if s.startswith("§ "):
        return "    - " + light_cleanup(s[2:].strip())
    return light_cleanup(s)


def extract_pdf_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    return "\n\n".join(
        (p.extract_text(extraction_mode="layout") or "") for p in reader.pages
    )


def to_markdown(raw: str, source_name: str) -> str:
    lines = [ln.rstrip() for ln in raw.splitlines()]
    md = [
        "# grandMA3 Release Notes",
        "",
        "> Text extracted from the official MA Lighting PDF "
        f"(`{source_name}`). Layout is approximate; optimized for search and diff.",
        "",
        "## Table of Contents",
        "",
    ]
    for num, title in MAIN_SECTIONS.items():
        anchor = f"{num}-{title.lower().replace(' ', '-')}"
        md.append(f"- [{num}. {title}](#{anchor})")
    md.extend(["", "## Let's Get Started", ""])

    i = 0
    pending_callout: str | None = None
    callout_body: list[str] = []
    seen_h2: set[str] = set()

    def flush_callout() -> None:
        nonlocal pending_callout, callout_body
        if pending_callout and callout_body:
            md.extend(format_callout(pending_callout, callout_body))
        pending_callout = None
        callout_body = []

    while i < len(lines):
        stripped = lines[i].strip()
        if is_noise_line(stripped):
            i += 1
            continue
        if not stripped:
            flush_callout()
            if md and md[-1] != "":
                md.append("")
            i += 1
            continue

        if stripped in CALLOUTS:
            flush_callout()
            pending_callout = stripped
            i += 1
            continue
        if stripped in {"Known Limitation", "Restriction", "Important", "Hint", "Requirement"}:
            flush_callout()
            pending_callout = stripped + ":"
            i += 1
            continue

        if pending_callout:
            if (
                stripped.startswith(("·", "•", "o ", "§ "))
                or re.match(r"^\d+\.\s+", stripped)
                or heading_level(stripped)
            ):
                flush_callout()
            else:
                callout_body.append(stripped)
                i += 1
                continue

        lvl = heading_level(stripped)
        if lvl:
            flush_callout()
            title = light_cleanup(re.sub(r"\.{3,}.*$", "", stripped))
            if lvl == 2:
                if title in seen_h2:
                    i += 1
                    continue
                seen_h2.add(title)
            md.append(f"{'#' * lvl} {title}")
            md.append("")
            i += 1
            continue

        if stripped.startswith("User name[") or (">" in stripped and "Please" in stripped):
            md.extend(["```", stripped, "```", ""])
            i += 1
            continue
        if stripped.startswith(("·", "•", "o ", "§ ")):
            md.append(convert_bullet(stripped))
            i += 1
            continue
        if re.match(r"^\d+\.\s+", stripped):
            md.append(light_cleanup(stripped))
            i += 1
            continue

        para = stripped
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or is_noise_line(nxt):
                break
            if nxt in CALLOUTS or nxt in {
                "Known Limitation",
                "Restriction",
                "Important",
                "Hint",
                "Requirement",
            }:
                break
            if heading_level(nxt) or nxt == "Description":
                break
            if nxt.startswith(("·", "•", "o ", "§ ")) or re.match(r"^\d+\.\s+", nxt):
                break
            if nxt.startswith("User name["):
                break
            if para.endswith(("-", "—")) or (nxt and nxt[0].islower()):
                para = para.rstrip("-— ") + " " + nxt
            elif not re.search(r"[.!?:]$", para):
                para += " " + nxt
            else:
                break
            i += 1
        md.append(light_cleanup(para))
        md.append("")

    flush_callout()
    return re.sub(r"\n{3,}", "\n\n", "\n".join(md)).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert grandMA3 release-notes PDF to searchable Markdown."
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        type=Path,
        help="Path to Release_Notes_*.pdf",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        help="Output .md path (default: same basename as input)",
    )
    args = parser.parse_args()

    pdf_path = args.input.resolve()
    if not pdf_path.is_file():
        print(f"Input not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        out_path = args.output.resolve()
    elif pdf_path.parent.name == "release-notes-pdf":
        out_path = (pdf_path.parent.parent / "release-notes" / (pdf_path.stem + ".md")).resolve()
    else:
        out_path = pdf_path.with_suffix(".md").resolve()
    raw = extract_pdf_text(pdf_path)
    markdown = to_markdown(raw, pdf_path.name)
    out_path.write_text(markdown, encoding="utf-8")
    print(f"Wrote {out_path} ({len(markdown)} chars, {markdown.count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()
