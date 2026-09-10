#!/usr/bin/env python3
"""Parse MA Lighting grandMA3 downloads page for the newest software build.

Only counts versions in grandMA3 package filenames (grandMA3_vX.Y.Z.W, …).

Usage:
  latest_from_downloads.py           # fetch live page
  latest_from_downloads.py --html F  # parse local HTML

Prints: VERSION<TAB>RELEASE_NOTES_BASENAME<TAB>FORCE_DOWNLOAD_QUERY
Exit 2 if no version found.
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path

URL = "https://www.malighting.com/downloads/products/grandma3/"
PKG_VER = re.compile(r"grandMA3(?:_[A-Za-z0-9]+)*_v(\d+\.\d+\.\d+\.\d+)", re.I)
RN_BASENAME = re.compile(
    r"((?:\d{4}-\d{2}-\d{2}_)?(?:grandMA3_)?Release_Notes_v\d+\.\d+(?:\.\d+\.\d+)?\.pdf)",
    re.I,
)
FORCE_RE = re.compile(r'eID=csForceDownload&(?:amp;)?download=([^"\'&\s]+)', re.I)


def ver_tuple(v: str) -> tuple[int, ...]:
    return tuple(int(p) for p in v.split("."))


def pad4(v: str) -> tuple[int, ...]:
    parts = [int(p) for p in v.split(".")]
    while len(parts) < 4:
        parts.append(0)
    return tuple(parts[:4])


def pick_release_notes(html: str, latest: str) -> str:
    mm = ".".join(latest.split(".")[:2])
    exact = None
    best_mm = None
    best_mm_vt = (-1,)
    for m in RN_BASENAME.finditer(html):
        name = m.group(1)
        vm = re.search(r"v(\d+\.\d+(?:\.\d+\.\d+)?)", name, re.I)
        if not vm:
            continue
        ver = vm.group(1)
        if ver == latest:
            exact = name
            break
        if ver.startswith(mm) or ver == mm:
            vt = pad4(ver)
            if vt <= ver_tuple(latest) and vt >= best_mm_vt:
                best_mm_vt = vt
                best_mm = name
    return exact or best_mm or ""


def pick_force(html: str, rn_name: str) -> str:
    if not rn_name:
        return ""
    idx = html.find(rn_name)
    if idx < 0:
        return ""
    window = html[max(0, idx - 1500) : idx + 100]
    fm = FORCE_RE.search(window)
    if not fm:
        return ""
    return f"eID=csForceDownload&download={fm.group(1)}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", type=Path, help="Local HTML file instead of fetching")
    args = ap.parse_args()
    if args.html:
        html = args.html.read_text(errors="replace")
    else:
        req = urllib.request.Request(URL, headers={"User-Agent": "grandma3-specs-adopt/1.0"})
        html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")

    cands = set(PKG_VER.findall(html))
    if not cands:
        sys.stderr.write("No grandMA3_vX.Y.Z.W package versions found\n")
        return 2
    latest = max(cands, key=ver_tuple)
    rn = pick_release_notes(html, latest)
    force = pick_force(html, rn)
    print(f"{latest}\t{rn}\t{force}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
