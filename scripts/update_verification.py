"""Update report date and prepend supplied verification notes without changing old line endings.

Usage: python -X utf8 scripts/update_verification.py --date YYYY-MM-DD --en-note PATH --zh-note PATH
Notes must describe completed verification; this script does not verify online prices.
"""

import argparse
import datetime
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def update_report(raw, date, note, chinese=False):
    text = raw.decode("utf-8")
    prefix = "生成日期：" if chinese else "Generated: "
    heading = "## 重要说明" if chinese else "## Important Notes"
    pattern = re.escape(prefix) + r"\d{4}-\d{2}-\d{2}"
    if len(re.findall(pattern, text)) != 1 or text.count(heading) != 1:
        raise ValueError("Report date or notes heading is missing/ambiguous")
    note = note.strip()
    if not note or "\n" in note or "\r" in note:
        raise ValueError("Supply one nonempty paragraph per note")
    if not note.startswith("- "):
        note = "- " + note
    text = re.sub(pattern, prefix + date, text, count=1)
    if note not in text.splitlines():
        text = re.sub(re.escape(heading) + r"(\r?\n)", lambda m: m[0] + "\n" + note + "\n", text, count=1)
    return text.encode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, type=datetime.date.fromisoformat)
    parser.add_argument("--en-note", required=True, type=Path)
    parser.add_argument("--zh-note", required=True, type=Path)
    args = parser.parse_args()
    edits = []
    for name, note, chinese in [("README.md", args.en_note, False), ("README.zh-CN.md", args.zh_note, True)]:
        path = ROOT / name
        edits.append((path, update_report(path.read_bytes(), args.date.isoformat(), note.read_text(encoding="utf-8-sig"), chinese)))
    for path, data in edits:
        path.write_bytes(data)


if __name__ == "__main__":
    main()
