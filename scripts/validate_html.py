#!/usr/bin/env python3
"""Lightweight static validation for HTML Content Board output."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path


class Inspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.images: list[dict[str, str]] = []
        self.html_lang = ""
        self.has_title = False
        self.has_viewport = False
        self._in_title = False
        self.title_text = ""

    def handle_starttag(self, tag: str, attrs):
        data = dict(attrs)
        if tag == "html":
            self.html_lang = data.get("lang", "").strip()
        elif tag == "title":
            self.has_title = True
            self._in_title = True
        elif tag == "meta" and data.get("name", "").lower() == "viewport":
            self.has_viewport = True
        elif tag == "a":
            self.hrefs.append(data.get("href", ""))
        elif tag == "img":
            self.images.append({"src": data.get("src", ""), "alt": data.get("alt", "")})

        if "id" in data:
            self.ids.append(data["id"])

    def handle_endtag(self, tag: str):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str):
        if self._in_title:
            self.title_text += data


def is_external(value: str) -> bool:
    return bool(re.match(r"^(?:https?:|mailto:|tel:|data:|blob:|javascript:)", value, re.I))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("html", type=Path)
    args = parser.parse_args()

    path: Path = args.html
    if not path.exists():
        print(f"FAIL: file not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8")
    inspector = Inspector()
    inspector.feed(text)

    failures: list[str] = []
    warnings: list[str] = []

    if not inspector.has_title or not inspector.title_text.strip():
        failures.append("Missing or empty <title>.")
    if not inspector.has_viewport:
        failures.append("Missing viewport meta tag.")
    if not inspector.html_lang:
        warnings.append("Missing <html lang=...>.")

    duplicates = sorted({x for x in inspector.ids if inspector.ids.count(x) > 1})
    if duplicates:
        failures.append("Duplicate IDs: " + ", ".join(duplicates))

    id_set = set(inspector.ids)
    for href in inspector.hrefs:
        if not href:
            warnings.append("Empty href found.")
        elif href.startswith("#") and href != "#" and href[1:] not in id_set:
            failures.append(f"Anchor target missing: {href}")
        elif href == "#":
            warnings.append("Placeholder href='#' found.")

    base = path.parent
    for img in inspector.images:
        src = img["src"].strip()
        alt = img["alt"].strip()
        if not alt:
            warnings.append(f"Image missing useful alt text: {src or '[empty src]'}")
        if not src:
            failures.append("Image with empty src found.")
        elif not is_external(src) and not src.startswith("/"):
            clean = src.split("?", 1)[0].split("#", 1)[0]
            if clean and not (base / clean).exists():
                failures.append(f"Local image not found: {src}")

    machine_path_patterns = [r"[A-Za-z]:\\Users\\", r"/Users/", r"/home/[^/]+/", r"/mnt/data/"]
    for pattern in machine_path_patterns:
        if re.search(pattern, text):
            warnings.append(f"Possible absolute machine path found: pattern {pattern}")

    print(f"Validated: {path}")
    if failures:
        print("\nFAILURES")
        for item in failures:
            print(f"- {item}")
    if warnings:
        print("\nWARNINGS")
        for item in warnings:
            print(f"- {item}")
    if not failures and not warnings:
        print("PASS: no issues found by lightweight static checks.")
    elif not failures:
        print("\nPASS WITH WARNINGS")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
