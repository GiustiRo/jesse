"""r50 F3 validation data: daily ETF bars (EWJ, EWY) from Stooq's free CSV endpoint.

The Binance perpetuals EWJUSDT/EWYUSDT only exist since 2026-03, so validation uses the ETF's
own daily history (price, split-adjusted as Stooq serves it; dividends not added, a declared
bias against long sleeves). The request itself is bounded to 2025-12-31 and rows after that
date are dropped again before writing: 2026 is reserved in r50.

    python research_scripts/r50_etf_daily_download.py EWJ EWY

Writes research_scripts/data/r50/etf/<TICKER>_daily_2000-01-01_2025-12-31.csv plus a manifest.
"""
import csv
import io
import json
import os
import sys

import requests
import jesse.models  # noqa: F401 - initialize models before the logger import in standalone jobs
from jesse import helpers as jh

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r50', 'etf')
URL = 'https://stooq.com/q/d/l/?s={sym}.us&i=d&d1=20000101&d2=20251231'
LAST_DAY = '2025-12-31'


def fetch(ticker: str) -> dict:
    r = requests.get(URL.format(sym=ticker.lower()), timeout=60, headers={'User-Agent': 'Mozilla/5.0'})
    r.raise_for_status()
    text = r.text
    if not text.startswith('Date,'):
        # Stooq answers errors and rate limits with a short non-CSV body.
        raise RuntimeError(f'{ticker}: unexpected response {text[:120]!r}')
    rows = [row for row in csv.DictReader(io.StringIO(text)) if row['Date'] <= LAST_DAY]
    for row in rows:
        o, h, l, c = (float(row[k]) for k in ('Open', 'High', 'Low', 'Close'))
        if min(o, h, l, c) <= 0 or h < max(o, c, l) or l > min(o, c, h):
            raise ValueError(f'{ticker}: invalid OHLC on {row["Date"]}')
    dates = [row['Date'] for row in rows]
    if dates != sorted(set(dates)):
        raise ValueError(f'{ticker}: duplicate or unordered dates')
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f'{ticker}_daily_2000-01-01_{LAST_DAY}.csv')
    with open(path, 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['date', 'open', 'high', 'low', 'close', 'volume'])
        for row in rows:
            w.writerow([row['Date'], row['Open'], row['High'], row['Low'], row['Close'], row.get('Volume', '')])
    info = {'ticker': ticker, 'source': 'stooq.com daily CSV (ETF, split-adjusted, no dividends)',
            'rows': len(rows), 'first': dates[0] if dates else None, 'last': dates[-1] if dates else None,
            'path': os.path.relpath(path, HERE)}
    with open(path + '.manifest.json', 'w') as fh:
        json.dump(info, fh, indent=2)
    return info


def main() -> None:
    for t in sys.argv[1:] or ['EWJ', 'EWY']:
        jh.debug(fetch(t.upper()))


if __name__ == '__main__':
    sys.exit(main())
