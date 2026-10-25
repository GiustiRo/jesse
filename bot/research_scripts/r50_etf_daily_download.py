"""r50 F3 validation data: daily ETF bars (EWJ, EWY) from Yahoo Finance's public chart API.

The Binance perpetuals EWJUSDT/EWYUSDT only exist since 2026-03, so validation uses the ETF's
own daily history. OHLC are Yahoo's split-adjusted prices; `adjclose` (dividends included) is
kept as an extra column. Sleeves trade the price series, so dividends are not earned: a
declared bias against long sleeves.

Source note (2026-10-25): Stooq now answers scripted requests with a JavaScript proof-of-work
bot check, which r50 does not bypass. Platinum, approved only from Stooq daily, was therefore
excluded from validation for data.

The request ends at 2026-01-01 00:00 UTC (exclusive) and later bars are dropped again before
writing: 2026 is reserved in r50. Standard library only, so it can run outside the Jesse host.

    python research_scripts/r50_etf_daily_download.py EWJ EWY

Writes research_scripts/data/r50/etf/<TICKER>_daily_2000-01-01_2025-12-31.csv plus a manifest
with the data checks (continuity, OHLC validity, gaps).
"""
import csv
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r50', 'etf')
URL = ('https://query1.finance.yahoo.com/v8/finance/chart/{sym}'
       '?period1=946684800&period2=1767225600&interval=1d&events=split')
LAST_DAY = '2025-12-31'
# A gap longer than this many calendar days between bars is not a weekend or a holiday run.
MAX_GAP_DAYS = 5
# Real exchange closures longer than that (NYSE shut 2001-09-11..14 after the attacks).
KNOWN_CLOSURES = {('2001-09-10', '2001-09-17')}


def log(msg) -> None:
    print(msg, flush=True)


def fetch(ticker: str) -> dict:
    req = urllib.request.Request(URL.format(sym=ticker), headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=60) as r:
        res = json.loads(r.read())['chart']['result'][0]
    q, adj = res['indicators']['quote'][0], res['indicators']['adjclose'][0]['adjclose']
    rows, invalid = [], []
    for k, t in enumerate(res['timestamp']):
        # US ETF bars are stamped at the 09:30 New York open; the UTC date is the session date.
        d = datetime.fromtimestamp(t, tz=timezone.utc).date().isoformat()
        if d > LAST_DAY:
            continue
        o, h, l, c, v = (q[x][k] for x in ('open', 'high', 'low', 'close', 'volume'))
        if None in (o, h, l, c) or min(o, h, l, c) <= 0 or h < max(o, c, l) or l > min(o, c, h):
            invalid.append(d)
            continue
        rows.append([d, o, h, l, c, v or 0, adj[k]])
    dates = [r[0] for r in rows]
    days = [datetime.fromisoformat(d) for d in dates]
    gaps = [(a.date().isoformat(), b.date().isoformat(), (b - a).days) for a, b in zip(days, days[1:])
            if (b - a).days > MAX_GAP_DAYS
            and (a.date().isoformat(), b.date().isoformat()) not in KNOWN_CLOSURES]
    checks = {'starts_by_2012': bool(dates) and dates[0] <= '2012-01-31',
              'ordered_unique_dates': dates == sorted(set(dates)),
              'all_ohlc_valid': not invalid, 'no_long_gaps': not gaps}
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f'{ticker}_daily_2000-01-01_{LAST_DAY}.csv')
    with open(path, 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['date', 'open', 'high', 'low', 'close', 'volume', 'adjclose'])
        w.writerows(rows)
    info = {'ticker': ticker, 'source': 'Yahoo Finance chart API v8 (split-adjusted OHLC; adjclose with dividends)',
            'rows': len(rows), 'first': dates[0] if dates else None, 'last': dates[-1] if dates else None,
            'checks': checks, 'passed': all(checks.values()), 'invalid_rows': invalid[:50],
            'long_gaps': gaps[:50], 'path': os.path.relpath(path, HERE)}
    with open(path + '.manifest.json', 'w') as fh:
        json.dump(info, fh, indent=2)
    return info


def main() -> None:
    for t in sys.argv[1:] or ['EWJ', 'EWY']:
        info = fetch(t.upper())
        log(json.dumps({k: info[k] for k in ('ticker', 'rows', 'first', 'last', 'checks', 'passed', 'invalid_rows', 'long_gaps')}))


if __name__ == '__main__':
    sys.exit(main())
