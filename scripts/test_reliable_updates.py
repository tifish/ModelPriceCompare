"""Regression checks for recovered source and artifact failures (no live network)."""

import shutil
import tempfile
import unittest
from email.message import Message
from pathlib import Path
from unittest.mock import Mock
from urllib.error import HTTPError, URLError

from fetch_official import fetch
from update_verification import update_report
from validate_reports import ROOT, table_rows, validate


class ReliableUpdatesTests(unittest.TestCase):
    def response(self, text):
        response = Mock()
        response.headers = Message()
        response.headers['Content-Type'] = 'text/markdown; charset=utf-8'
        response.read.return_value = text.encode('utf-8')
        response.url = 'https://example.org/pricing.md'
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        return response

    def test_markdown_unicode_and_recovery_audit(self):
        opener = Mock(side_effect=[URLError('temporary'), self.response('# 价格 🎉')])
        sleep = Mock()
        text, meta = fetch('https://example.org/pricing.md', opener=opener, sleep=sleep)
        self.assertEqual(text, '# 价格 🎉')
        self.assertEqual(meta['attempts'], 2)
        self.assertEqual(len(meta['errors']), 1)
        sleep.assert_called_once_with(1)

    def test_permanent_failure_does_not_retry(self):
        opener = Mock(side_effect=HTTPError('https://example.org', 404, 'missing', {}, None))
        with self.assertRaises(RuntimeError):
            fetch('https://example.org', opener=opener, sleep=Mock())
        self.assertEqual(opener.call_count, 1)

    def test_transient_failure_is_bounded(self):
        opener = Mock(side_effect=URLError('offline'))
        sleep = Mock()
        with self.assertRaises(RuntimeError):
            fetch('https://example.org', opener=opener, sleep=sleep)
        self.assertEqual(opener.call_count, 3)
        self.assertEqual(sleep.call_count, 2)

    def test_mixed_line_endings_and_idempotence(self):
        raw = b'Title\r\nGenerated: 2026-10-29\n\r\n## Important Notes\r\n\n- old\n'
        updated = update_report(raw, '2026-10-30', 'Checked')
        self.assertEqual(updated, raw.replace(b'2026-10-29', b'2026-10-30').replace(b'## Important Notes\r\n', b'## Important Notes\r\n\n- Checked\n'))
        self.assertEqual(update_report(updated, '2026-10-30', 'Checked'), updated)

    def test_separator_is_not_a_price_row(self):
        self.assertEqual(table_rows('| A | B |\n|---|---:|\n| one | two |\n'), [['one', 'two']])

    def test_current_artifacts_and_corrupted_price(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ['models.txt', 'model_price_comparison.csv', 'README.md', 'README.zh-CN.md', 'index.html']:
                shutil.copyfile(ROOT / name, root / name)
            validate(root)
            p = root / 'README.md'
            text = p.read_text(encoding='utf-8')
            import re
            text, count = re.subn(r'\$[\d.]+', '$999999', text, count=1)
            self.assertEqual(count, 1)
            p.write_text(text, encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Report price mismatch'):
                validate(root)


if __name__ == '__main__':
    unittest.main()
