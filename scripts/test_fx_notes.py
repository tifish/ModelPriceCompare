import unittest
from decimal import Decimal
from validate_reports import validate_fx_notes


class FxNotesTests(unittest.TestCase):
    en = '- USD/CNY reference rate for the Chinese README is `1 USD = 6.6710 CNY`, observation `2026-11-13`, published `2026-11-16`.'
    zh = '- 汇率采用近似值 `1 USD = 6.6710 CNY`。观测 `2026-11-13`，发布 `2026-11-16`。'

    def test_current_notes(self):
        validate_fx_notes(self.en, self.zh, Decimal('6.6710'))

    def test_stale_english_rate(self):
        with self.assertRaisesRegex(ValueError, 'rate is stale'):
            validate_fx_notes(self.en.replace('6.6710', '6.6538'), self.zh, Decimal('6.6710'))

    def test_stale_source_date(self):
        with self.assertRaisesRegex(ValueError, 'dates differ'):
            validate_fx_notes(self.en.replace('2026-11-13', '2026-10-30'), self.zh, Decimal('6.6710'))
