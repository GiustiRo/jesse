"""r52 F0: download the U50 universe from data.binance.vision (USDT-M perpetuals only).

PROTOCOL_R52.md section 0. For every symbol in data/r52/universe50.json and every month
2020-01..2025-12 (2026 is reserved):
* 1h klines (with taker buy volume) and funding rates, kept whole;
* for BTC, ETH and the 20 largest alts (line 2), 1m klines reduced to quarter-hour rows:
  bucket open time, opening-minute volume and taker-buy volume, bucket volume and close. The
  raw minutes are not kept (volume), only what the QOI signal needs.
Each ZIP is checked against its published SHA-256 before use. Months before a listing answer 404
and are skipped. Output: data/r52/<SYMBOL>_1h.npy, _funding.npy, _q15.npy plus manifest.json.

    python research_scripts/r52_download.py [--workers 8]
"""
import argparse
import hashlib
import io
import json
import os
import sys
import time
import urllib.error
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r52')
BASE = 'https://data.binance.vision/data/futures/um/monthly'
MONTHS = [f'{y}-{m:02d}' for y in range(2020, 2026) for m in range(1, 13)]
RETRIES = 10


def log(msg):
    print(msg, flush=True)


def fetch(url):
    """Bytes of a URL, None on 404; retries transient errors with backoff."""
    for k in range(RETRIES):
        try:
            with urllib.request.urlopen(url, timeout=300) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(min(2 ** k, 120))
        except Exception:
            time.sleep(min(2 ** k, 120))
    raise RuntimeError(f'failed after {RETRIES} tries: {url}')


def zip_frame(url):
    """DataFrame of a checksum-verified monthly ZIP (no header; header row dropped if present)."""
    import pandas as pd
    raw = fetch(url)
    if raw is None:
        return None
    chk = fetch(url + '.CHECKSUM')
    if chk is not None:
        want = chk.decode().split()[0]
        if hashlib.sha256(raw).hexdigest() != want:
            raise RuntimeError(f'checksum mismatch: {url}')
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        df = pd.read_csv(z.open(z.namelist()[0]), header=None, low_memory=False)
    if not str(df.iat[0, 0]).lstrip('-').isdigit():
        df = df.iloc[1:]
    return df.apply(pd.to_numeric, errors='coerce')


def klines(sym, interval, reduce=None):
    """Monthly klines as [open_time, open, high, low, close, volume, quote_volume, taker_buy
    volume]; `reduce` maps each month's array to a smaller one (1m -> quarter hours) so the
    raw minutes never sit in memory all at once."""
    parts = []
    for m in MONTHS:
        df = zip_frame(f'{BASE}/klines/{sym}/{interval}/{sym}-{interval}-{m}.zip')
        if df is None or not len(df):
            continue
        a = df.iloc[:, [0, 1, 2, 3, 4, 5, 7, 9]].to_numpy(dtype=float)
        a = a[np.argsort(a[:, 0])]
        parts.append(reduce(a) if reduce else a)
    if not parts:
        return np.zeros((0, 5 if reduce else 8))
    a = np.vstack(parts)
    a = a[np.argsort(a[:, 0])]
    return a[np.r_[True, np.diff(a[:, 0]) > 0]]


def funding(sym):
    out = []
    for m in MONTHS:
        df = zip_frame(f'{BASE}/fundingRate/{sym}/{sym}-fundingRate-{m}.zip')
        if df is not None and len(df):
            out.extend(df.iloc[:, [0, 2]].to_numpy(dtype=float).tolist())
    a = np.array(out) if out else np.zeros((0, 2))
    return a[np.argsort(a[:, 0])] if len(a) else a


def quarter_hours(m1):
    """Quarter-hour rows from 1m klines: [bucket_ms, open-minute volume, open-minute taker buy,
    bucket volume, bucket close]."""
    t = m1[:, 0].astype(np.int64)
    bucket = t // 900_000 * 900_000
    first = t == bucket
    cut = np.flatnonzero(np.diff(bucket)) + 1
    starts, stops = np.r_[0, cut], np.r_[cut, len(t)]
    rows = []
    for a, b in zip(starts, stops):
        f = a if first[a] else None
        rows.append([bucket[a], m1[f, 5] if f is not None else np.nan, m1[f, 7] if f is not None else np.nan,
                     m1[a:b, 5].sum(), m1[b - 1, 4]])
    return np.array(rows)


def one(item):
    sym, need_q = item
    res = {'symbol': sym}
    p1h = os.path.join(OUT, f'{sym}_1h.npy')
    if not os.path.exists(p1h):
        np.save(p1h, klines(sym, '1h'))
    a = np.load(p1h)
    res['h1_rows'] = int(len(a))
    res['h1_first'] = int(a[0, 0]) if len(a) else None
    gaps = np.diff(a[:, 0]) / 3_600_000 if len(a) > 1 else np.array([])
    res['h1_gaps_gt_1h'] = int((gaps > 1).sum())
    res['h1_max_gap_h'] = float(gaps.max()) if len(gaps) else 0.0
    pf = os.path.join(OUT, f'{sym}_funding.npy')
    if not os.path.exists(pf):
        np.save(pf, funding(sym))
    res['funding_rows'] = int(len(np.load(pf)))
    if need_q:
        pq = os.path.join(OUT, f'{sym}_q15.npy')
        if not os.path.exists(pq):
            np.save(pq, klines(sym, '1m', reduce=quarter_hours))
        res['q15_rows'] = int(len(np.load(pq)))
    log(json.dumps(res))
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--workers', type=int, default=8)
    # r53: the QOI feature needs quarter-hour rows for all 50 symbols, not only line 2's 22.
    ap.add_argument('--q-all', action='store_true')
    args = ap.parse_args()
    uni = json.load(open(os.path.join(OUT, 'universe50.json')))
    syms = [u['symbol'] for u in uni]
    alts = [s for s in syms if s not in ('BTCUSDT', 'ETHUSDT')][:20]
    q = set(syms) if args.q_all else {'BTCUSDT', 'ETHUSDT', *alts}
    # 1m-heavy symbols first so the long downloads start early.
    items = sorted(((s, s in q) for s in syms), key=lambda x: not x[1])
    def safe(item):
        # One symbol failing (network) must not abort the others; a re-run resumes from the
        # saved files.
        try:
            return one(item)
        except Exception as e:
            log(json.dumps({'symbol': item[0], 'error': str(e)}))
            return {'symbol': item[0], 'error': str(e)}
    with ThreadPoolExecutor(args.workers) as ex:
        res = list(ex.map(safe, items))
    json.dump({'symbols': res, 'q_basket_alts': alts, 'months': [MONTHS[0], MONTHS[-1]]},
              open(os.path.join(OUT, 'manifest.json'), 'w'), indent=1)
    log('done')


if __name__ == '__main__':
    sys.exit(main())
