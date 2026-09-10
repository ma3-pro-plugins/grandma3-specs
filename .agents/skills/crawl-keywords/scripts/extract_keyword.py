#!/usr/bin/env python3
"""Extract one grandMA3 manual keyword HTML page into a Keyword Spec Markdown body.

Used by the crawl-keywords skill. Replaces ## Official only when the caller merges
into an existing file; this script prints/writes a full Spec or Official section.

AI-friendly example rule (locked in CONTEXT.md):
  Manual tables show:  User name[Fixture]>Store Cue 1
  We store only:       Store Cue 1
  Strip the CLI prompt (anything matching User name[...]>) including the '>'.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.stderr.write("Need beautifulsoup4 (+ lxml). pip install beautifulsoup4 lxml html2text\n")
    sys.exit(1)

try:
    import html2text
except ImportError:
    html2text = None

CLI_PROMPT = re.compile(r"User name\[[^\]]+\]\s*>\s*", re.I)
# Also catch odd variants without brackets content quirks
CLI_PROMPT_LOOSE = re.compile(r"^\s*User name\[[^\]]*\]\s*>\s*", re.M)


def clean(s: str) -> str:
    return re.sub(r"[ \t]+", " ", s.replace("\xa0", " ").replace("\u200b", "")).strip()


def strip_cli_prompt(text: str) -> str:
    """Remove command-line chrome; keep only the command after '>'."""
    lines = []
    for line in text.splitlines():
        if "User name[" in line and ">" in line:
            m = re.search(r"User name\[[^\]]+\]\s*>\s*(.+?)(?:\s*\|+\s*)?$", line)
            if m:
                cmd = m.group(1).strip().rstrip("|").strip()
                cmd = re.sub(r"\s*\|+\s*$", "", cmd).strip()
                # Prefer a single table cell with the bare command in backticks
                # Fenced command — no CLI chrome, easy for agents to copy
                lines.append("```")
                lines.append(cmd)
                lines.append("```")
                continue
        if line.strip() == "Paste to Command Line":
            continue
        lines.append(line)
    out = "\n".join(lines)
    out = CLI_PROMPT.sub("", out)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out


def keyword_from_html(html: str, kind: str, src_name: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    title = clean(soup.title.get_text() if soup.title else "")
    title = re.sub(r"\s+Option Keywords?$", "", title, flags=re.I)
    title = re.sub(r"\s+Keyword$", "", title, flags=re.I)
    if kind == "option":
        if not title.startswith("/"):
            stem = Path(src_name).stem
            if stem.startswith("ok_"):
                stem = stem[3:]
            title = "/" + "".join(p[:1].upper() + p[1:] for p in stem.split("_"))
        title = title.split()[0]
    return title


def shortcuts_from_html(html: str, kind: str) -> list[str]:
    soup = BeautifulSoup(html, "lxml")
    sc: list[str] = []
    for ul in soup.find_all("ul"):
        if "shortcut" not in ul.get_text(" ", strip=True).lower():
            continue
        for li in ul.find_all("li"):
            lit = li.get_text(" ", strip=True)
            if "shortcut" not in lit.lower():
                continue
            # <strong> and <b>
            parts = []
            for tag in li.find_all(["strong", "b"]):
                parts.append(clean(tag.get_text()))
            if not parts:
                # plain text: "Type the shortcut F or Fi"
                m = re.search(r"shortcut[s]?\s+(.+)$", lit, re.I)
                if m:
                    parts = [clean(p) for p in re.split(r"\s+or\s+", m.group(1), flags=re.I)]
            for raw in parts:
                for p in re.split(r"\s+or\s+", raw, flags=re.I):
                    s = clean(p).strip("*").strip()
                    if not s or s in ("/", "&"):
                        continue
                    if kind == "option" and not s.startswith("/"):
                        s = "/" + s.lstrip()
                    if s.startswith("/") and len(s) < 2:
                        continue
                    if s not in sc:
                        sc.append(s)
    return sc


def official_md(html: str, base_url: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    topic = soup.select_one("div.topic-content") or soup.body
    for sel in [".CHHeadingLink", "script", "style"]:
        for el in topic.select(sel):
            el.decompose()
    for hk in topic.select("span.hardkey"):
        code = soup.new_tag("code")
        code.string = hk.get_text()
        hk.replace_with(code)

    if html2text is None:
        text = topic.get_text("\n", strip=True)
    else:
        h2t = html2text.HTML2Text()
        h2t.ignore_links = False
        h2t.body_width = 0
        h2t.protect_links = True
        h2t.unicode_snob = True
        h2t.ignore_images = True
        text = h2t.handle(str(topic))

    # Start at "To enter"
    lines = text.splitlines()
    start = 0
    for i, line in enumerate(lines):
        if re.match(r"^To enter\b", line.strip(), re.I):
            start = i
            break
    md = "\n".join(lines[start:]).strip()

    # Demote headings one level under ## Official
    md = "\n".join("#" + line if line.startswith("#") else line for line in md.splitlines())

    # Absolute links; unwrap html2text <file.html>
    md = re.sub(
        r"\]\(\<([^)#>]+\.html)(#[^>]*)?\>\)",
        lambda m: f"]({base_url}/{m.group(1)}{m.group(2) or ''})",
        md,
    )
    md = re.sub(
        r"\]\((?!https?://|mailto:)([^)#]+\.html)(#[^)]*)?\)",
        lambda m: f"]({base_url}/{m.group(1)}{m.group(2) or ''})",
        md,
    )
    md = re.sub(r"(?m)^Paste to Command Line\s*$", "", md)
    md = strip_cli_prompt(md)
    md = re.sub(r"(?m)^\*{2,}\s*$", "", md)
    md = re.sub(r"(?m)^#{3,}\s*$", "", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def build_spec(html: str, kind: str, src_name: str, manual_url: str, base_url: str) -> str:
    keyword = keyword_from_html(html, kind, src_name)
    shortcuts = shortcuts_from_html(html, kind)
    body = official_md(html, base_url.rstrip("/"))
    sc = ", ".join(f'"{s}"' for s in shortcuts)
    return (
        f"---\n"
        f'keyword: "{keyword}"\n'
        f"kind: {kind}\n"
        f"shortcuts: [{sc}]\n"
        f'manual_url: "{manual_url}"\n'
        f"---\n\n"
        f"## Official\n\n"
        f"{body}\n\n"
        f"## Extra\n\n"
        f"<!-- Contributor notes. Crawler must not overwrite this section. -->\n"
    )


def merge_preserve_extra(existing: str, new_spec: str) -> str:
    """Replace Official + frontmatter fields except introduced; keep Extra and introduced."""
    intro = None
    m = re.search(r"(?m)^introduced:\s*(.+)$", existing)
    if m:
        intro = m.group(1).strip()

    extra = ""
    em = re.search(r"(?ms)^## Extra\s*\n(.*)\Z", existing)
    if em:
        extra = em.group(0).rstrip() + "\n"
    else:
        extra = "## Extra\n\n<!-- Contributor notes. Crawler must not overwrite this section. -->\n"
    # Take new file through end of Official
    om = re.search(r"(?ms)^(---\n.*?---\n\n## Official\n.*?)(?=^## Extra|\Z)", new_spec)
    head = om.group(1).rstrip() + "\n\n" if om else new_spec
    if intro is not None and "introduced:" not in head:
        head = re.sub(r"(?m)^(manual_url:.*)$", rf"\1\nintroduced: {intro}", head, count=1)
    elif intro is not None:
        head = re.sub(r"(?m)^introduced:\s*.*$", f"introduced: {intro}", head)

    return head + extra


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", "-i", required=True, help="Keyword HTML file")
    ap.add_argument("--kind", choices=["general", "option"], required=True)
    ap.add_argument("--manual-url", required=True)
    ap.add_argument(
        "--base-url",
        default="https://help.malighting.com/grandMA3/2.5/HTML",
        help="Base URL for resolving relative manual links",
    )
    ap.add_argument("--output", "-o", help="Write Spec Markdown here")
    ap.add_argument(
        "--merge-into",
        help="Existing Spec path: replace Official, keep Extra and introduced",
    )
    ap.add_argument("--stdout-official-only", action="store_true")
    args = ap.parse_args()

    html = Path(args.input).read_text(errors="replace")
    spec = build_spec(html, args.kind, Path(args.input).name, args.manual_url, args.base_url)

    if args.merge_into:
        existing = Path(args.merge_into).read_text()
        spec = merge_preserve_extra(existing, spec)

    if args.stdout_official_only:
        m = re.search(r"(?ms)^## Official\n(.*?)(?=^## Extra|\Z)", spec)
        sys.stdout.write((m.group(1).strip() + "\n") if m else spec)
        return

    if args.output:
        Path(args.output).write_text(spec)
    else:
        sys.stdout.write(spec)


if __name__ == "__main__":
    main()
