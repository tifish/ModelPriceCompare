"""Inspect fetched HTML without shell-embedded parsing or executing page scripts.

Usage: python -X utf8 scripts/inspect_sources.py SOURCE_DIR [--previous DIR]
Writes readable .clean files and prints bounded text diffs and model links.
Embedded pricing data still needs separate inspection in the original source.
"""

import argparse
import difflib
import re
from html.parser import HTMLParser
from pathlib import Path


class SourceText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.links = set()
        self.skip = 0
        self.in_pre = False

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        if tag == 'pre':
            self.in_pre = True
        if tag == 'a':
            self.links.update(value for key, value in attrs if key == 'href' and value)

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = max(0, self.skip - 1)
        if tag == 'pre':
            self.in_pre = False

    def handle_data(self, data):
        # Google AI Studio serves complete Markdown documents in a single <pre>.
        # Other oversized text nodes may be hydration data, kept in the raw file.
        if self.skip:
            return
        data = data.strip()
        if data and (self.in_pre or len(data) < 1500):
            self.parts.append(data)


def readable(text):
    if '<html' not in text.lower() and '<!doctype' not in text.lower():
        return text, set()
    parser = SourceText()
    parser.feed(text)
    return '\n'.join(parser.parts), parser.links


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source_dir', type=Path)
    parser.add_argument('--previous', type=Path)
    parser.add_argument('--previous-name', action='append', default=[], metavar='CURRENT=OLD',
                        help='Map renamed source snapshots explicitly')
    args = parser.parse_args()
    names = dict(item.split('=', 1) for item in args.previous_name)
    for path in sorted(args.source_dir.glob('*.txt')):
        text, links = readable(path.read_text(encoding='utf-8'))
        path.with_suffix('.clean').write_text(text, encoding='utf-8')
        print('\nSOURCE', path.stem)
        previous = args.previous / (names.get(path.stem, path.stem) + '.txt') if args.previous else None
        if previous and previous.exists():
            raw = path.read_text(encoding='utf-8')
            old_raw = previous.read_text(encoding='utf-8')
            print('Full source unchanged:', old_raw == raw)
            old_tables = re.findall(r'<table\b.*?</table>', old_raw, re.S)
            tables = re.findall(r'<table\b.*?</table>', raw, re.S)
            if old_tables or tables:
                print('HTML tables unchanged:', old_tables == tables)
            if 'DocTable' in raw:
                chunks = lambda s: [s[max(0, m.start()-50):m.start()+6500] for m in re.finditer('DocTable', s)]
                print('Embedded DocTable sections unchanged:', chunks(old_raw) == chunks(raw))
            old, _ = readable(old_raw)
            print(''.join(difflib.unified_diff(old.splitlines(True), text.splitlines(True), n=2)))
        elif previous:
            print('NO PREVIOUS SNAPSHOT:', previous, '(not verified unchanged)')
        for link in sorted(links):
            if any(term in link for term in ('5-2', '5.2', 'models/overview')):
                print('MODEL LINK', link)


if __name__ == '__main__':
    main()
