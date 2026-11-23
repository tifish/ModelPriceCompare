"""Fetch fresh official source text, including Markdown and embedded HTML data.

Usage: python -X utf8 scripts/fetch_official.py URL --output PATH
Only read-only GET requests are retried. A failed fetch never overwrites output.
"""

import argparse
import http.client
import json
import socket
import ssl
import sys
import time
from http.client import HTTPException
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import HTTPSHandler, Request, build_opener


class FailoverHTTPSConnection(http.client.HTTPSConnection):
    """Fail over across resolved DNS addresses on TCP connect or TLS handshake errors."""

    def connect(self):
        if self._tunnel_host:
            return super().connect()
        infos = socket.getaddrinfo(self.host, self.port, 0, socket.SOCK_STREAM)
        if not infos:
            raise OSError(f"getaddrinfo returned no addresses for {self.host}")
        seen = set()
        last_error = None
        for af, socktype, proto, _, sa in infos:
            key = (af, socktype, proto, sa)
            if key in seen:
                continue
            seen.add(key)
            sock = None
            try:
                sock = socket.socket(af, socktype, proto)
                if self.timeout is not socket._GLOBAL_DEFAULT_TIMEOUT:
                    sock.settimeout(self.timeout)
                if self.source_address:
                    sock.bind(self.source_address)
                sock.connect(sa)
                self.sock = self._context.wrap_socket(sock, server_hostname=self.host)
                return
            except ssl.SSLCertVerificationError:
                if sock is not None:
                    sock.close()
                raise
            except OSError as error:
                last_error = error
                if sock is not None:
                    sock.close()
        raise last_error


class FailoverHTTPSHandler(HTTPSHandler):
    def https_open(self, req):
        return self.do_open(FailoverHTTPSConnection, req, context=self._context)


_DEFAULT_OPENER = build_opener(FailoverHTTPSHandler())


def fetch(url, attempts=3, opener=None, sleep=time.sleep):
    open_url = _DEFAULT_OPENER.open if opener is None else opener
    errors = []
    for attempt in range(attempts):
        try:
            request = Request(url, headers={"User-Agent": "ModelPriceCompare/1.0", "Connection": "close"})
            with open_url(request, timeout=30) as response:
                text = response.read().decode(response.headers.get_content_charset() or "utf-8")
                if not text.strip():
                    raise ValueError("Empty response; source is not verified")
                return text, {"url": response.url, "attempts": attempt + 1, "errors": errors}
        except (HTTPError, URLError, TimeoutError, ConnectionError, HTTPException) as error:
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
