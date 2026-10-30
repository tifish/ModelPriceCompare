"""Fetch fresh official source text, including Markdown and embedded HTML data.

Usage: python -X utf8 scripts/fetch_official.py URL --output PATH
Only read-only GET requests are retried. A failed fetch never overwrites output.
"""

import argparse
import json
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def fetch(url, attempts=3, opener=urlopen, sleep=time.sleep):
    errors = []
    for attempt in range(attempts):
        try:
            request = Request(url, headers={"User-Agent": "ModelPriceCompare/1.0"})
            with opener(request, timeout=30) as response:
                text = response.read().decode(response.headers.get_content_charset() or "utf-8")
                if not text.strip():
                    raise ValueError("Empty response; source is not verified")
                return text, {"url": response.url, "attempts": attempt + 1, "errors": errors}
        except (HTTPError, URLError, TimeoutError) as error:
            errors.append(str(error))
            retryable = not isinstance(error, HTTPError) or error.code in (408, 429, 500, 502, 503, 504)
            if not retryable or attempt + 1 == attempts:
                raise RuntimeError(f"Source fetch failed: {url}; {errors}") from error
            sleep(2 ** attempt)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not args.url.startswith("https://"):
        parser.error("Use an official HTTPS source URL")
    try:
        text, meta = fetch(args.url)
        args.output.write_text(text, encoding="utf-8", newline="\n")
        print(json.dumps({**meta, "output": str(args.output), "characters": len(text)}, ensure_ascii=False))
    except (RuntimeError, ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
