import unittest
import subprocess
import sys
import tempfile
from pathlib import Path

from inspect_sources import readable


class SourceInspectionTests(unittest.TestCase):
    def test_renamed_and_missing_snapshots_are_explicit(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            current, old = root / 'current', root / 'old'
            current.mkdir()
            old.mkdir()
            (current / 'claude.txt').write_text('模型 $8', encoding='utf-8')
            (old / 'anthropic.txt').write_text('模型 $8', encoding='utf-8')
            command = [sys.executable, '-X', 'utf8', str(Path(__file__).with_name('inspect_sources.py')),
                       str(current), '--previous', str(old)]
            missing = subprocess.run(command, capture_output=True, encoding='utf-8', check=True)
            self.assertIn('NO PREVIOUS SNAPSHOT:', missing.stdout)
            mapped = subprocess.run(command + ['--previous-name', 'claude=anthropic'],
                                    capture_output=True, encoding='utf-8', check=True)
            self.assertIn('Full source unchanged: True', mapped.stdout)
            self.assertNotIn('NO PREVIOUS SNAPSHOT:', mapped.stdout)

    def test_unicode_prices_links_and_script_exclusion(self):
        text, links = readable('''<!doctype html><html><style>hidden</style>
<a href="/models/fable-5-2/overview">模型 “Fable”</a>
<table><tr><td>$0.20</td><td>$8</td><td>$40</td></tr></table>
<script>throw new Error("must not run");</script></html>''')
        self.assertIn('模型 “Fable”', text)
        self.assertIn('$0.20\n$8\n$40', text)
        self.assertNotIn('hidden', text)
        self.assertNotIn('must not run', text)
        self.assertEqual(links, {'/models/fable-5-2/overview'})

    def test_markdown_is_preserved(self):
        source = '| 模型 | 价格 |\r\n| Fable | $8 |\n'
        self.assertEqual(readable(source), (source, set()))


if __name__ == '__main__':
    unittest.main()
