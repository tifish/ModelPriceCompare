import unittest

from inspect_sources import readable


class SourceInspectionTests(unittest.TestCase):
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
