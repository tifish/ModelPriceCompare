"""Synchronize bilingual table order and prices from CSV, preserving other text."""
import csv
import re
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sync(text, rows, rate):
    pattern = r'(?m)^(\|[^\n]*\n\|[-:| ]+\r?\n)((?:\|[^\n]*\n)+)'
    def replace(match):
        existing = {}
        endings = {}
        for line in match[2].splitlines(keepends=True):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            model = cells[1].replace('（短上下文）', ' (short context)').replace('（长上下文）', ' (long context)')
            existing[model] = cells
            endings[model] = '\r\n' if line.endswith('\r\n') else '\n'
        lines = []
        newline = '\r\n' if match[2].splitlines(keepends=True)[0].endswith('\r\n') else '\n'
        for row in rows:
            cells = existing[row['model']]
            cells[0], cells[8] = row['provider'], row['price_basis']
            for i, prefix in enumerate(('input_cache_hit', 'input_cache_miss', 'output')):
                cells[2+i*2] = row[prefix+'_multiplier']+'x'
                value = Decimal(row[prefix+'_usd_per_1m'])
                cells[3+i*2] = ('$'+format(value.normalize(), 'f') if rate is None else
                    '¥'+str((value*rate).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
            lines.append('| '+' | '.join(cells)+' |'+endings.get(row['model'], newline))
        return match[1]+''.join(lines)
    result, count = re.subn(pattern, replace, text, count=1)
    if count != 1:
        raise ValueError('Missing report table')
    return result


def main():
    with (ROOT/'model_price_comparison.csv').open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    edits = []
    for name in ('README.md', 'README.zh-CN.md'):
        path = ROOT/name
        text = path.read_bytes().decode('utf-8')
        rate = None if name == 'README.md' else Decimal(re.search(r'1 USD = ([\d.]+) CNY', text)[1])
        edits.append((path, sync(text, rows, rate)))
    for path, text in edits:
        path.write_bytes(text.encode('utf-8'))


if __name__ == '__main__':
    main()
