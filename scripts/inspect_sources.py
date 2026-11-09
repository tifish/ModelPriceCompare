"""Inspect fetched HTML without shell-embedded parsing or executing page scripts.

Usage: python -X utf8 scripts/inspect_sources.py SOURCE_DIR [--previous DIR]
Writes readable .clean files and prints bounded text diffs and model links.
Embedded pricing data still needs separate inspection in the original source.
"""

import argparse
import difflib
from html.parser import HTMLParser
from pathlib import Path


class SourceText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.links = set()
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        if tag == 'a':
            self.links.update(value for key, value in attrs if key == 'href' and value)

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = max(0, self.skip - 1)

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data.strip())


def readable(text):
    if '<html' not in text.lower() and '<!doctype' not in text.lower():
        return text, set()
    parser = SourceText()
    parser.feed(text)
    # Hydration payloads can appear outside script tags; retain them in the raw file.
    return '\n'.join(part for part in parser.parts if len(part) < 1500), parser.links


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source_dir', type=Path)
    parser.add_argument('--previous', type=Path)
    args = parser.parse_args()
    for path in sorted(args.source_dir.glob('*.txt')):
        text, links = readable(path.read_text(encoding='utf-8'))
        path.with_suffix('.clean').write_text(text, encoding='utf-8')
        print('\nSOURCE', path.stem)
        if args.previous and (args.previous / path.name).exists():
            old, _ = readable((args.previous / path.name).read_text(encoding='utf-8'))
            print(''.join(difflib.unified_diff(old.splitlines(True), text.splitlines(True), n=2)))
        for link in sorted(links):
            if any(term in link for term in ('5-2', '5.2', 'models/overview')):
                print('MODEL LINK', link)


if __name__ == '__main__':
    main()
