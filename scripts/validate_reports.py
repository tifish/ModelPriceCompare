"""Validate CSV, model list, bilingual table values and generated HTML locally.

Run after build_html.py. This checks artifact consistency, not live source accuracy.
"""

import csv
import json
import re
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRICES = ["input_cache_hit_usd_per_1m", "input_cache_miss_usd_per_1m", "output_usd_per_1m"]
MULTIPLIERS = ["input_cache_hit_multiplier", "input_cache_miss_multiplier", "output_multiplier"]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def table_rows(text):
    # Select the first Markdown table, remove header and alignment row structurally.
    table = re.search(r"(?m)^\|[^\n]*\n\|[-:| ]+\n((?:\|[^\n]*\n)+)", text)
    require(table is not None, "Missing report table")
    return [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in table[1].splitlines()]


def normalize_model(model):
    return model.replace("（短上下文）", " (short context)").replace("（长上下文）", " (long context)")


def validate(root=ROOT):
    with (root / "model_price_comparison.csv").open(encoding="utf-8-sig", newline="") as source:
        rows = list(csv.DictReader(source))
    require(bool(rows), "Empty CSV")
    models = (root / "models.txt").read_text(encoding="utf-8-sig").splitlines()
    bases = {re.sub(r" \((?:short context|long context|peak|off-peak)\)$", "", r["model"]) for r in rows}
    require(len(models) == len(set(models)) and set(models) == bases, "Model list differs from CSV")
    require(len({r['model'] for r in rows}) == len(rows), "Duplicate price row")
    for price, mult in zip(PRICES, MULTIPLIERS):
        values = [Decimal(r[price]) for r in rows]
        require(all(v.is_finite() and v >= 0 for v in values), f"Invalid prices: {price}")
        base = min(v for v in values if v > 0)
        for row, value in zip(rows, values):
            require(abs(value / base - Decimal(row[mult])) <= Decimal('.005'), f"Wrong multiplier: {row['model']} {mult}")
    hits = [Decimal(r[PRICES[0]]) for r in rows]
    require(hits == sorted(hits, reverse=True), "Cache-hit sort order is wrong")
    en = (root / 'README.md').read_text(encoding='utf-8')
    zh = (root / 'README.zh-CN.md').read_text(encoding='utf-8')
    date = re.search(r"Generated: (\d{4}-\d{2}-\d{2})", en)[1]
    require(re.search(r"生成日期：(\d{4}-\d{2}-\d{2})", zh)[1] == date, "Report dates differ")
    rate = Decimal(re.search(r"1 USD = ([\d.]+) CNY", zh)[1])
    for report, currency_rate in [(en, Decimal(1)), (zh, rate)]:
        table = table_rows(report)
        require(len(table) == len(rows), "Report/CSV row counts differ")
        for cells, row in zip(table, rows):
            require(len(cells) == 9, "Invalid table columns")
            require(cells[0] == row['provider'] and normalize_model(cells[1]) == row['model'] and cells[8] == row['price_basis'], f"Report identity mismatch: {row['model']}")
            for i, (price, mult) in enumerate(zip(PRICES, MULTIPLIERS)):
                require(Decimal(cells[2 + 2*i].removesuffix('x')) == Decimal(row[mult]), f"Report multiplier mismatch: {row['model']}")
                value = Decimal(cells[3 + 2*i].lstrip('$¥'))
                tolerance = Decimal(0) if currency_rate == 1 else Decimal('.005')
                require(abs(value - Decimal(row[price]) * currency_rate) <= tolerance, f"Report price mismatch: {row['model']}")
    html = (root / 'index.html').read_text(encoding='utf-8')
    data = json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>', html, re.S)[1])
    require(data['generated'] == date and Decimal(str(data['cnyRate'])) == rate, "HTML metadata is stale")
    expected = []
    for r in rows:
        item = dict(provider=r['provider'], model=r['model'], basis=r['price_basis'], url=r['source_url'], notes=r['notes'])
        item.update({k: float(r[col]) for k, col in zip(['hit', 'miss', 'out', 'hitX', 'missX', 'outX'], PRICES + MULTIPLIERS)})
        expected.append(item)
    require(data['rows'] == expected, "HTML rows differ from CSV; rebuild index.html")
    return len(models), len(rows)


if __name__ == '__main__':
    models, rows = validate()
    print(f'Validated {models} models and {rows} price rows across CSV, bilingual reports and HTML.')
