"""Free 1-minute SPY proxy from the Dukascopy historical feed (Fase 2, Pilar 2).

Downloads Dukascopy daily `BID_candles_min_1.bi5` files for `USA500.IDX/USD` (S&P 500 CFD,
quoted ~23h/5d like ES futures), divides OHLC by 10 to match the SPY / Binance `SPYUSDT` price
scale, drops closed-market minutes, and writes a CSV ready for the MCP tool
`clean_and_import_custom_candle_csv` (symbol `SPY-USDT`).

Why this source: Binance `SPYUSDT` only lists from 2026-04-06 and the Massive free tier only
covers a rolling two years, while Dukascopy's feed is free, keyless and goes back to 2010.

Run locally (stdlib + numpy only, no installs)::

    python bot/research_scripts/dukascopy_download.py --start 2019-10-01 --end 2025-12-31

Raw daily files are cached under `research_scripts/data/dukascopy_cache/<instrument>/` so an
interrupted or rate-limited run resumes without re-downloading. The CSV lands in
`research_scripts/data/`, i.e. project path `research_scripts/data/<file>.csv` for the MCP.

Format notes (Dukascopy convention, verified by --probe against the known index level):
* URL month is zero-based (`/2020/00/02/` is 2 Jan 2020); timestamps are UTC.
* Each record is 24 bytes big-endian: uint32 seconds-from-midnight, uint32 open, close, low,
  high (in price points), float32 volume. Indices use 1/1000 price points.
* Days without trading come back empty or as flat zero-volume minutes; zero-volume minutes are
  dropped so market closures stay real gaps (Jesse's timestamp simulator supports gaps, while
  forward-filled flat candles would fake low-volatility "compression" in ATR-based logic).
"""
import argparse
import csv
import lzma
import os
import struct
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone

import numpy as np

BASE_URL = 'https://datafeed.dukascopy.com/datafeed'
HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, 'data')
POINT_DIVISOR = {'USA500IDXUSD': 1000.0, 'XAUUSD': 1000.0}
# Dukascopy throttles bursts with 503/429. A fixed polite delay plus exponential backoff keeps
# a ~1,600-file run reliable without hammering the free service.
REQUEST_DELAY_S = 0.35
MAX_RETRIES = 8


def _url(inst: str, d: date) -> str:
    return f'{BASE_URL}/{inst}/{d.year}/{d.month - 1:02d}/{d.day:02d}/BID_candles_min_1.bi5'


def _fetch(inst: str, d: date, cache_dir: str) -> bytes:
    path = os.path.join(cache_dir, f'{d.isoformat()}.bi5')
    if os.path.exists(path):
        with open(path, 'rb') as fh:
            return fh.read()
    delay = 2.0
    for attempt in range(MAX_RETRIES):
        try:
            req = urllib.request.Request(_url(inst, d), headers={'User-Agent': 'Mozilla/5.0'})
            raw = urllib.request.urlopen(req, timeout=40).read()
            with open(path, 'wb') as fh:
                fh.write(raw)
            time.sleep(REQUEST_DELAY_S)
            return raw
        except urllib.error.HTTPError as e:
            if e.code == 404:
                # No file for that day (holiday / weekend): cache as empty so it is not retried.
                open(path, 'wb').close()
                return b''
            print(f'  {d} HTTP {e.code}, retry {attempt + 1}/{MAX_RETRIES} in {delay:.0f}s', flush=True)
        except Exception as e:  # network hiccup
            print(f'  {d} {type(e).__name__}: {e}, retry {attempt + 1}/{MAX_RETRIES} in {delay:.0f}s', flush=True)
        time.sleep(delay)
        delay = min(delay * 2, 120)
    raise RuntimeError(f'giving up on {d} after {MAX_RETRIES} retries')


def _decode(raw: bytes, d: date, divisor: float) -> np.ndarray:
    if not raw:
        return np.empty((0, 6))
    data = lzma.decompress(raw)
    n = len(data) // 24
    rec = np.frombuffer(data[: n * 24], dtype=np.dtype([('t', '>u4'), ('o', '>u4'), ('c', '>u4'),
                                                         ('l', '>u4'), ('h', '>u4'), ('v', '>f4')]))
    day_ms = int(datetime(d.year, d.month, d.day, tzinfo=timezone.utc).timestamp() * 1000)
    out = np.column_stack([
        day_ms + rec['t'].astype(np.int64) * 1000,
        rec['o'] / divisor, rec['h'] / divisor, rec['l'] / divisor, rec['c'] / divisor,
        rec['v'].astype(np.float64),
    ])
    return out[out[:, 5] > 0]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--instrument', default='USA500IDXUSD')
    ap.add_argument('--start', default='2019-10-01')
    ap.add_argument('--end', default='2025-12-31')
    ap.add_argument('--scale', type=float, default=10.0, help='divide prices by this (10 maps SPX to SPY scale)')
    ap.add_argument('--out', default=None)
    ap.add_argument('--probe', action='store_true', help='decode one day and print, no CSV')
    args = ap.parse_args()

    inst = args.instrument
    divisor = POINT_DIVISOR.get(inst, 1000.0)
    cache_dir = os.path.join(DATA_DIR, 'dukascopy_cache', inst)
    os.makedirs(cache_dir, exist_ok=True)
    start, end = date.fromisoformat(args.start), date.fromisoformat(args.end)

    if args.probe:
        rows = _decode(_fetch(inst, start, cache_dir), start, divisor)
        print(len(rows), 'rows'); print(rows[:3]); print(rows[-3:])
        return

    out = args.out or os.path.join(DATA_DIR, f'{inst}_div{args.scale:g}_1m_{args.start}_{args.end}.csv')
    days = [start + timedelta(days=i) for i in range((end - start).days + 1)]
    # Saturday is fully closed for US index CFDs; Sunday carries the evening reopen.
    days = [d for d in days if d.weekday() != 5]
    total_rows, last_ts = 0, -1
    with open(out, 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        for i, d in enumerate(days):
            rows = _decode(_fetch(inst, d, cache_dir), d, divisor)
            if len(rows):
                rows[:, 1:5] /= args.scale
                if rows[0, 0] <= last_ts:
                    raise RuntimeError(f'non-increasing timestamps at {d}')
                last_ts = rows[-1, 0]
                for r in rows:
                    w.writerow([int(r[0]), f'{r[1]:.4f}', f'{r[2]:.4f}', f'{r[3]:.4f}', f'{r[4]:.4f}', f'{r[5]:.4f}'])
                total_rows += len(rows)
            if i % 50 == 0:
                print(f'{d} ({i + 1}/{len(days)}) rows so far {total_rows}', flush=True)
    print(f'wrote {total_rows} rows to {out}')


if __name__ == '__main__':
    sys.exit(main())
