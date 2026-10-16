"""Build index.html (interactive price table for GitHub Pages) from model_price_comparison.csv.

Usage: python scripts/build_html.py
"""

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "model_price_comparison.csv"
README_EN = ROOT / "README.md"
README_ZH = ROOT / "README.zh-CN.md"
OUT_PATH = ROOT / "index.html"

def read_rows():
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    data = []
    for row in rows:
        item = {
            "provider": row["provider"],
            "model": row["model"],
            "basis": row["price_basis"],
            "hitX": float(row["input_cache_hit_multiplier"]),
            "hit": float(row["input_cache_hit_usd_per_1m"]),
            "missX": float(row["input_cache_miss_multiplier"]),
            "miss": float(row["input_cache_miss_usd_per_1m"]),
            "outX": float(row["output_multiplier"]),
            "out": float(row["output_usd_per_1m"]),
            "url": row["source_url"],
            "notes": row["notes"],
        }
        data.append(item)
    return data


def read_meta():
    en = README_EN.read_text(encoding="utf-8")
    zh = README_ZH.read_text(encoding="utf-8")
    generated = re.search(r"Generated:\s*(\d{4}-\d{2}-\d{2})", en)
    rate = re.search(r"1 USD = ([\d.]+) CNY", zh)
    if not generated or not rate:
        raise SystemExit("Could not find generated date or USD/CNY rate in READMEs")
    return {"generated": generated.group(1), "cnyRate": float(rate.group(1))}


def main():
    payload = {"rows": read_rows(), **read_meta()}
    data_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = TEMPLATE.replace("__DATA__", data_json).replace("__GENERATED__", payload["generated"])
    OUT_PATH.write_text(html, encoding="utf-8", newline="\n")
    print(f"Wrote {OUT_PATH.name}: {len(payload['rows'])} rows, generated {payload['generated']}")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Model Token Price Comparison</title>
<meta name="description" content="LLM API token prices normalized to USD per 1M tokens, verified against official provider pricing pages. Generated __GENERATED__.">
<style>
:root {
  --bg: #ffffff; --fg: #1f2328; --muted: #656d76; --border: #d0d7de; --panel: #f6f8fa;
  --accent: #0969da; --chip-on: #ddf4ff; --chip-on-border: #54aeff; --row-hover: #f3f8ff;
  --heat: 9, 105, 218;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0d1117; --fg: #e6edf3; --muted: #8d96a0; --border: #30363d; --panel: #161b22;
    --accent: #4493f8; --chip-on: #12304f; --chip-on-border: #1f6feb; --row-hover: #1b2330;
    --heat: 68, 147, 248;
  }
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--fg);
  font: 14px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", "PingFang SC", "Microsoft YaHei", Helvetica, Arial, sans-serif; }
main { max-width: 1400px; margin: 0 auto; padding: 24px 16px 48px; }
h1 { font-size: 24px; margin: 0 0 4px; }
.sub { color: var(--muted); margin: 0 0 16px; }
.sub a, .links a { color: var(--accent); text-decoration: none; }
.sub a:hover, .links a:hover { text-decoration: underline; }
.toolbar { display: flex; flex-wrap: wrap; gap: 12px 24px; align-items: center; padding: 12px;
  background: var(--panel); border: 1px solid var(--border); border-radius: 8px; margin-bottom: 12px; }
.group { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
.group-label { color: var(--muted); font-size: 12px; margin-right: 4px; }
button { font: inherit; cursor: pointer; }
.chip { border: 1px solid var(--border); background: var(--bg); color: var(--muted);
  border-radius: 999px; padding: 3px 12px; font-size: 13px; }
.chip[aria-pressed="true"] { background: var(--chip-on); border-color: var(--chip-on-border); color: var(--fg); }
.chip .count { opacity: .65; margin-left: 4px; font-size: 12px; }
.link-btn { border: 0; background: none; color: var(--accent); padding: 3px 4px; font-size: 13px; }
.seg { display: inline-flex; border: 1px solid var(--border); border-radius: 6px; overflow: hidden; }
.seg button { border: 0; background: var(--bg); color: var(--muted); padding: 3px 10px; font-size: 13px; }
.seg button[aria-pressed="true"] { background: var(--chip-on); color: var(--fg); }
.status { color: var(--muted); font-size: 12px; margin: 0 0 8px; }
.table-wrap { overflow-x: auto; border: 1px solid var(--border); border-radius: 8px; }
table { border-collapse: collapse; width: 100%; font-variant-numeric: tabular-nums; }
th, td { padding: 6px 10px; border-bottom: 1px solid var(--border); white-space: nowrap; text-align: left; }
th { position: sticky; top: 0; background: var(--panel); font-weight: 600; font-size: 13px; z-index: 1; }
th.sortable { cursor: pointer; user-select: none; }
th.sortable:hover { color: var(--accent); }
th .arrow { display: inline-block; width: 1em; color: var(--accent); }
th.num, td.num { text-align: right; }
td.mult { color: var(--muted); font-size: 12px; }
tbody tr.data:hover { background: var(--row-hover); }
tbody tr.data { cursor: pointer; }
td.basis { color: var(--muted); font-size: 12px; white-space: normal; min-width: 180px; }
td.model { font-weight: 500; }
.tag { display: inline-block; font-size: 11px; padding: 0 6px; border-radius: 4px; margin-left: 6px;
  border: 1px solid #d4a72c; color: #9a6700; font-weight: 400; }
tr.notes td { white-space: normal; color: var(--muted); font-size: 12px; background: var(--panel); padding: 8px 12px 10px 24px; }
tr.notes a { color: var(--accent); word-break: break-all; }
.empty { padding: 24px; text-align: center; color: var(--muted); }
footer { color: var(--muted); font-size: 12px; margin-top: 16px; }
</style>
</head>
<body>
<main>
  <h1 data-i18n="title"></h1>
  <p class="sub">
    <span data-i18n="generated"></span> <strong id="generated"></strong> ·
    <a href="README.html" data-i18n="reportEn"></a> ·
    <a href="README.zh-CN.html" data-i18n="reportZh"></a> ·
    <a href="model_price_comparison.csv" data-i18n="csv"></a> ·
    <a href="https://github.com/tifish/ModelPriceCompare">GitHub</a>
  </p>

  <div class="toolbar">
    <div class="group" id="providers">
      <span class="group-label" data-i18n="providers"></span>
    </div>
    <div class="group">
      <button class="link-btn" id="all" data-i18n="all"></button>
      <button class="link-btn" id="none" data-i18n="none"></button>
    </div>
    <div class="group">
      <span class="group-label" data-i18n="currency"></span>
      <span class="seg" id="currency">
        <button data-v="USD">USD $</button><button data-v="CNY">CNY ¥</button>
      </span>
    </div>
    <div class="group">
      <span class="group-label" data-i18n="language"></span>
      <span class="seg" id="lang">
        <button data-v="en">English</button><button data-v="zh">中文</button>
      </span>
    </div>
  </div>

  <p class="status" id="status"></p>
  <div class="table-wrap">
    <table>
      <thead><tr id="head"></tr></thead>
      <tbody id="body"></tbody>
    </table>
  </div>
  <footer id="footer"></footer>
</main>

<script id="data" type="application/json">__DATA__</script>
<script>
(() => {
  const DATA = JSON.parse(document.getElementById("data").textContent);
  const ROWS = DATA.rows.map((r, i) => ({ ...r, idx: i }));
  const PROVIDERS = [...new Set(ROWS.map(r => r.provider))];

  const I18N = {
    en: {
      title: "Model Token Price Comparison", generated: "Generated:", reportEn: "English report",
      reportZh: "中文报告", csv: "CSV", providers: "Providers", all: "All", none: "None",
      currency: "Currency", language: "Language",
      cols: { provider: "Provider", model: "Model", hitX: "Hit x", hit: "Input cache hit", missX: "Miss x",
              miss: "Input cache miss", outX: "Output x", out: "Output", basis: "Basis" },
      status: (n, t) => `Showing ${n} of ${t} price rows. Prices per 1M tokens. Click a column header to sort; click a row for notes and source.`,
      footer: r => `Multipliers use the cheapest model in each price category across all providers as 1.00x. CNY amounts are approximate at 1 USD = ${r} CNY. Batch, Flex, Fast mode, data residency, cache writes/storage, tools, promotions, and enterprise discounts are excluded unless noted. Verify against the official pricing pages before relying on these numbers.`,
      empty: "No providers selected.", source: "Source:", unverified: "unverified",
    },
    zh: {
      title: "模型 Token 价格比较", generated: "生成日期：", reportEn: "English report",
      reportZh: "中文报告", csv: "CSV", providers: "提供方", all: "全选", none: "全不选",
      currency: "币种", language: "语言",
      cols: { provider: "提供方", model: "模型", hitX: "命中倍率", hit: "输入缓存命中", missX: "未命中倍率",
              miss: "输入缓存未命中", outX: "输出倍率", out: "输出", basis: "价格口径" },
      status: (n, t) => `显示 ${n} / ${t} 条价格记录。价格单位为每 1M tokens。点击表头排序；点击行查看备注与来源。`,
      footer: r => `倍率以全部提供方中每个价格类别最便宜的模型为 1.00x。人民币按 1 USD = ${r} CNY 近似换算。除非注明，Batch、Flex、Fast 模式、数据驻留、缓存写入/存储、工具、促销及企业折扣均不计入。使用前请以官方价格页为准。`,
      empty: "未选择任何提供方。", source: "来源：", unverified: "未核实",
    },
  };
  const ZH_MODEL = [
    [/ \(long context\)$/, "（长上下文）"], [/ \(short context\)$/, "（短上下文）"],
    [/ \(off-peak\)$/, "（低峰）"], [/ \(peak\)$/, "（高峰）"],
    [/ \(>200K prompts\)$/, "（>200K 提示）"], [/ \(<=200K prompts\)$/, "（<=200K 提示）"],
  ];

  const COLS = [
    { key: "provider", type: "text" }, { key: "model", type: "text" },
    { key: "hitX", type: "mult" }, { key: "hit", type: "price" },
    { key: "missX", type: "mult" }, { key: "miss", type: "price" },
    { key: "outX", type: "mult" }, { key: "out", type: "price" },
    { key: "basis", type: "text" },
  ];
  const MAX_LOG = Object.fromEntries(["hitX", "missX", "outX"].map(k => [k, Math.log(Math.max(...ROWS.map(r => r[k])))]));

  const load = (k, d) => { try { const v = JSON.parse(localStorage.getItem("mpc." + k)); return v ?? d; } catch { return d; } };
  const save = (k, v) => { try { localStorage.setItem("mpc." + k, JSON.stringify(v)); } catch {} };

  const navZh = (navigator.language || "").toLowerCase().startsWith("zh");
  const state = {
    lang: load("lang", navZh ? "zh" : "en"),
    currency: load("currency", navZh ? "CNY" : "USD"),
    hidden: new Set(load("hidden", [])),
    sortKey: null, sortDir: 1,   // null => original order (cache-hit price desc)
    open: new Set(),
  };

  const esc = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const fmtPrice = usd => {
    if (state.currency === "USD") return "$" + String(+usd.toPrecision(6));
    const v = usd * DATA.cnyRate;
    if (v >= 0.1) return "¥" + v.toFixed(2);
    return "¥" + String(+v.toFixed(Math.max(2, 1 - Math.floor(Math.log10(v)) + 2)));
  };
  const modelName = m => state.lang === "zh" ? ZH_MODEL.reduce((s, [re, rep]) => s.replace(re, rep), m) : m;

  function renderProviders() {
    const box = document.getElementById("providers");
    box.querySelectorAll(".chip").forEach(b => b.remove());
    for (const p of PROVIDERS) {
      const b = document.createElement("button");
      b.className = "chip";
      b.setAttribute("aria-pressed", String(!state.hidden.has(p)));
      b.innerHTML = `${esc(p)}<span class="count">${ROWS.filter(r => r.provider === p).length}</span>`;
      b.onclick = () => { state.hidden.has(p) ? state.hidden.delete(p) : state.hidden.add(p); save("hidden", [...state.hidden]); render(); };
      box.appendChild(b);
    }
  }

  function renderHead() {
    const t = I18N[state.lang];
    document.getElementById("head").innerHTML = COLS.map(c => {
      const arrow = state.sortKey === c.key ? (state.sortDir > 0 ? "▲" : "▼") : "";
      const num = c.type !== "text" ? " num" : "";
      return `<th class="sortable${num}" data-key="${c.key}" aria-sort="${state.sortKey === c.key ? (state.sortDir > 0 ? "ascending" : "descending") : "none"}">${num ? `<span class="arrow">${arrow}</span>` : ""}${esc(t.cols[c.key])}${num ? "" : `<span class="arrow">${arrow}</span>`}</th>`;
    }).join("");
    document.querySelectorAll("#head th").forEach(th => th.onclick = () => {
      const k = th.dataset.key, type = COLS.find(c => c.key === k).type;
      if (state.sortKey === k) {
        // numeric: desc -> asc -> original; text: asc -> desc -> original
        const first = type === "text" ? 1 : -1;
        if (state.sortDir === first) state.sortDir = -first; else state.sortKey = null;
      } else { state.sortKey = k; state.sortDir = type === "text" ? 1 : -1; }
      render();
    });
  }

  function sorted(rows) {
    if (!state.sortKey) return rows;
    const k = state.sortKey, d = state.sortDir;
    const isText = COLS.find(c => c.key === k).type === "text";
    return [...rows].sort((a, b) => {
      const c = isText ? String(a[k]).localeCompare(String(b[k]), undefined, { numeric: true }) : a[k] - b[k];
      return c * d || a.idx - b.idx;
    });
  }

  function heat(row, key) {
    const a = MAX_LOG[key] > 0 ? Math.log(Math.max(row[key], 1)) / MAX_LOG[key] : 0;
    return `background: rgba(var(--heat), ${(a * 0.22).toFixed(3)})`;
  }

  function renderBody() {
    const t = I18N[state.lang];
    const rows = sorted(ROWS.filter(r => !state.hidden.has(r.provider)));
    const body = document.getElementById("body");
    if (!rows.length) { body.innerHTML = `<tr><td class="empty" colspan="${COLS.length}">${esc(t.empty)}</td></tr>`; }
    else body.innerHTML = rows.map(r => {
      const unverified = /unverified/i.test(r.basis);
      const tag = unverified ? `<span class="tag">${esc(t.unverified)}</span>` : "";
      const main = `<tr class="data" data-idx="${r.idx}" title="${esc(r.notes)}">
        <td>${esc(r.provider)}</td>
        <td class="model">${esc(modelName(r.model))}${tag}</td>
        <td class="num mult">${r.hitX.toFixed(2)}x</td><td class="num" style="${heat(r, "hitX")}">${fmtPrice(r.hit)}</td>
        <td class="num mult">${r.missX.toFixed(2)}x</td><td class="num" style="${heat(r, "missX")}">${fmtPrice(r.miss)}</td>
        <td class="num mult">${r.outX.toFixed(2)}x</td><td class="num" style="${heat(r, "outX")}">${fmtPrice(r.out)}</td>
        <td class="basis">${esc(r.basis)}</td></tr>`;
      const notes = state.open.has(r.idx)
        ? `<tr class="notes"><td colspan="${COLS.length}">${esc(r.notes)}<br>${esc(t.source)} <a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(r.url)}</a></td></tr>` : "";
      return main + notes;
    }).join("");
    body.querySelectorAll("tr.data").forEach(tr => tr.onclick = () => {
      const i = +tr.dataset.idx; state.open.has(i) ? state.open.delete(i) : state.open.add(i); renderBody();
    });
    document.getElementById("status").textContent = t.status(rows.length, ROWS.length);
  }

  function renderStatic() {
    const t = I18N[state.lang];
    document.documentElement.lang = state.lang === "zh" ? "zh-CN" : "en";
    document.title = t.title;
    document.querySelectorAll("[data-i18n]").forEach(el => el.textContent = t[el.dataset.i18n]);
    document.getElementById("generated").textContent = DATA.generated;
    document.getElementById("footer").textContent = t.footer(DATA.cnyRate);
    for (const [id, val] of [["lang", state.lang], ["currency", state.currency]])
      document.querySelectorAll(`#${id} button`).forEach(b => b.setAttribute("aria-pressed", String(b.dataset.v === val)));
  }

  function render() { renderStatic(); renderProviders(); renderHead(); renderBody(); }

  document.getElementById("all").onclick = () => { state.hidden.clear(); save("hidden", []); render(); };
  document.getElementById("none").onclick = () => { PROVIDERS.forEach(p => state.hidden.add(p)); save("hidden", [...state.hidden]); render(); };
  for (const id of ["lang", "currency"])
    document.querySelectorAll(`#${id} button`).forEach(b => b.onclick = () => { state[id] = b.dataset.v; save(id, b.dataset.v); render(); });

  render();
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
