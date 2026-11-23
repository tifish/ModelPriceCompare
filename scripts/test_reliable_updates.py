"""Regression checks for recovered source and artifact failures (no live network)."""

import shutil
import socket
import ssl
import subprocess
import tempfile
import unittest
from email.message import Message
from pathlib import Path
from unittest.mock import Mock
from unittest.mock import patch
import fetch_sources
from urllib.error import HTTPError, URLError

from fetch_official import FailoverHTTPSConnection, fetch
from update_verification import update_report
from validate_reports import ROOT, table_rows, validate


class ReliableUpdatesTests(unittest.TestCase):
    def test_batch_fetch_preserves_unicode_and_reports_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            arguments = ['fetch_sources.py', directory, 'good=https://example.org/good', 'bad=https://example.org/bad']
            def retrieve(url):
                if url.endswith('/bad'):
                    raise RuntimeError('source unavailable')
                return '价格 🎉', dict(url=url, attempts=1, errors=[])
            with patch('sys.argv', arguments), patch('fetch_sources.fetch', side_effect=retrieve), patch('builtins.print'):
                self.assertEqual(fetch_sources.main(), 1)
            self.assertEqual((Path(directory) / 'good.txt').read_text(encoding='utf-8'), '价格 🎉')
            self.assertFalse((Path(directory) / 'bad.txt').exists())

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

    def test_connection_reset_during_read_retries_and_recovers(self):
        broken = Mock()
        broken.read.side_effect = ConnectionResetError(10054, 'Connection reset by peer')
        broken.__enter__ = Mock(return_value=broken)
        broken.__exit__ = Mock(return_value=False)
        opener = Mock(side_effect=[broken, self.response('GLM-5.3 $1.4')])
        sleep = Mock()
        text, meta = fetch('https://example.org/pricing', opener=opener, sleep=sleep)
        self.assertEqual(text, 'GLM-5.3 $1.4')
        self.assertEqual(meta['attempts'], 2)
        self.assertEqual(len(meta['errors']), 1)
        self.assertIn('10054', meta['errors'][0])
        self.assertEqual(opener.call_args_list[0][0][0].get_header('Connection'), 'close')
        sleep.assert_called_once_with(1)

    def test_https_connection_fails_over_after_tls_handshake_reset(self):
        infos = [
            (socket.AF_INET, socket.SOCK_STREAM, 6, '', ('76.76.21.93', 443)),
            (socket.AF_INET, socket.SOCK_STREAM, 6, '', ('76.76.21.241', 443)),
        ]
        first_sock, second_sock, wrapped_sock = Mock(), Mock(), Mock()
        context = Mock()
        context.wrap_socket.side_effect = [
            ConnectionResetError(10054, 'Connection reset by peer'),
            wrapped_sock,
        ]
        conn = FailoverHTTPSConnection('docs.z.ai', 443, timeout=15, context=context)
        with patch('fetch_official.socket.getaddrinfo', return_value=infos), \
             patch('fetch_official.socket.socket', side_effect=[first_sock, second_sock]):
            conn.connect()
        first_sock.connect.assert_called_once_with(('76.76.21.93', 443))
        first_sock.close.assert_called_once()
        second_sock.connect.assert_called_once_with(('76.76.21.241', 443))
        self.assertEqual(context.wrap_socket.call_count, 2)
        self.assertEqual(context.wrap_socket.call_args_list[1].kwargs['server_hostname'], 'docs.z.ai')
        self.assertIs(conn.sock, wrapped_sock)

    def test_https_connection_does_not_bypass_cert_verification_error(self):
        infos = [
            (socket.AF_INET, socket.SOCK_STREAM, 6, '', ('76.76.21.93', 443)),
            (socket.AF_INET, socket.SOCK_STREAM, 6, '', ('76.76.21.241', 443)),
        ]
        first_sock = Mock()
        context = Mock()
        context.wrap_socket.side_effect = ssl.SSLCertVerificationError(1, 'certificate verify failed')
        conn = FailoverHTTPSConnection('docs.z.ai', 443, timeout=15, context=context)
        with patch('fetch_official.socket.getaddrinfo', return_value=infos), \
             patch('fetch_official.socket.socket', return_value=first_sock) as sock_ctor:
            with self.assertRaises(ssl.SSLCertVerificationError):
                conn.connect()
        self.assertEqual(sock_ctor.call_count, 1)
        first_sock.close.assert_called_once()

    def test_mixed_line_endings_and_idempotence(self):
        raw = b'Title\r\nGenerated: 2026-10-29\n\r\n## Important Notes\r\n\n- old\n'
        updated = update_report(raw, '2026-10-30', 'Checked')
        self.assertEqual(updated, raw.replace(b'2026-10-29', b'2026-10-30').replace(b'## Important Notes\r\n', b'## Important Notes\r\n\n- Checked\n'))
        self.assertEqual(update_report(updated, '2026-10-30', 'Checked'), updated)

    def test_git_crlf_and_real_trailing_spaces(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args):
                return subprocess.run(['git', '-C', str(root), *args], capture_output=True)
            self.assertEqual(git('init').returncode, 0)
            shutil.copyfile(ROOT / '.gitattributes', root / '.gitattributes')
            for name in ['README.md', 'model_price_comparison.csv']:
                p = root / name
                p.write_bytes(b'old\r\n')
                self.assertEqual(git('-c', 'core.autocrlf=false', 'add', name).returncode, 0)
                p.write_bytes(b'updated\r\n')
                self.assertEqual(git('diff', '--check', '--', name).returncode, 0)
                p.write_bytes(b'updated \r\n')
                self.assertNotEqual(git('diff', '--check', '--', name).returncode, 0)
                p.write_bytes(b'old\r\n')

    def test_verification_note_encoding_damage(self):
        raw = '生成日期：2026-11-05\r\n## 重要说明\r\n'.encode('utf-8')
        for note in ['2026-11-07 ????? token ???', '核验\ufffd失败', 'Checked prices']:
            with self.assertRaises(ValueError):
                update_report(raw, '2026-11-07', note, chinese=True)
        updated = update_report(raw, '2026-11-07', '已核验价格，无变化。', chinese=True)
        self.assertIn('已核验价格，无变化。'.encode('utf-8'), updated)

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
