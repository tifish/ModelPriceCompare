"""Fetch named official sources concurrently without shell-embedded Python.

Usage: python -X utf8 scripts/fetch_sources.py OUTPUT_DIR name=HTTPS_URL ...
Any failed source makes the command fail; inspect retry errors in the metadata.
"""

import argparse
import concurrent.futures
import json
from pathlib import Path

from fetch_official import fetch


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output_dir', type=Path)
    parser.add_argument('sources', nargs='+')
    args = parser.parse_args()
    sources = []
    for source in args.sources:
        name, separator, url = source.partition('=')
        if not separator or not name.replace('-', '').isalnum() or not url.startswith('https://'):
            parser.error('Sources must be safe-name=https://official-source')
        sources.append((name, url))
    args.output_dir.mkdir(parents=True, exist_ok=True)

    def retrieve(source):
        name, url = source
        content, metadata = fetch(url)
        (args.output_dir / (name + '.txt')).write_text(content, encoding='utf-8')
        return dict(name=name, characters=len(content), **metadata)

    failed = False
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(retrieve, source): source[0] for source in sources}
        for future in concurrent.futures.as_completed(futures):
            try:
                print(json.dumps(future.result(), ensure_ascii=False))
            except Exception as error:
                failed = True
                print(json.dumps(dict(name=futures[future], error=str(error)), ensure_ascii=False))
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
