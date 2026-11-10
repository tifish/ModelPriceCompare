import unittest
from sync_report_tables import sync


class SyncTests(unittest.TestCase):
    def test_csv_order_overrides_inserted_same_price_row(self):
        text = 'intro\r\n| Provider | Model | Hit x | Hit | Miss x | Miss | Out x | Out | Basis |\n|---|---|---|---|---|---|---|---|---|\n| P | New | 1x | $1 | 1x | $1 | 1x | $1 | B |\n| P | Old | 1x | $1 | 1x | $1 | 1x | $1 | B |\nend\r\n'
        rows = []
        for model in ('Old', 'New'):
            r = dict(provider='P', model=model, price_basis='B')
            for prefix in ('input_cache_hit', 'input_cache_miss', 'output'):
                r[prefix+'_multiplier']='1.00'
                r[prefix+'_usd_per_1m']='1'
            rows.append(r)
        result=sync(text, rows, None)
        self.assertLess(result.index('| Old |'), result.index('| New |'))
        self.assertTrue(result.startswith('intro\r\n'))
        self.assertTrue(result.endswith('end\r\n'))
        self.assertEqual(sync(result, rows, None), result)
        crlf = text.replace('\r\n', '\n').replace('\n', '\r\n')
        self.assertEqual(sync(crlf, rows, None), result.replace('\r\n', '\n').replace('\n', '\r\n'))
