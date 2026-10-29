"""r63 F0b: 1h klines and funding of the r63 universe from data.binance.vision (PROTOCOL_R63 §2).

    python -P r63_data.py download [--workers 16]   # data/r63/bars/<SYM>_1h.npy, _funding.npy + download.json
    python -P r63_data.py manifest                  # data/r63/manifest.json: sha256 + coverage per symbol

Months 2020-01..2024-12 only (2025 sealed, 2026 reserved). Every ZIP is checked against its .CHECKSUM
(r52_download.zip_frame) and parsed in memory; only the arrays are kept. `load(sym)` returns the
cleaned tramos (segments) the engine trades, with causal eligibility and slippage tiers.
"""
import argparse
import hashlib
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor

import numpy as np

import r52_download as dl
import r63

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r63')
BARS = os.path.join(OUT, 'bars')
BASE = 'https://data.binance.vision/data/futures/um/monthly'
FIRST_MONTH = '2020-01'
CUT_MS = 1_735_689_600_000            # 2025-01-01 00:00 UTC, exclusive
HOUR, DAY = 3_600_000, 86_400_000
MAX_FILL_H = 24                        # §2: gaps up to 24h become flat bars; longer gaps split the symbol
DELIST_BEFORE_MS = 1_734_998_400_000   # 2024-12-24: a tramo ending earlier closes with the delisting cost
DELIST_SLIP = 0.01                     # §2: taker fee + 100 bp at the last close, no advance notice
MIN_AGE_D, VOL_WIN_D, MIN_QVOL = 90, 30, 2e6
SLIP_TIERS = ((50e6, 5e-4), (10e6, 10e-4), (0.0, 20e-4))   # 30-day median USDT volume -> taker slippage
MIN_TRAMO_H = 24 * 35                  # shorter tramos cannot hold the 30-day sigma warm-up plus a trade


def months_for(span):
    a, b = max(span[0], FIRST_MONTH), min(span[1], r63.CUT_MONTH)
    out, (y, m) = [], map(int, a.split('-'))
    while f'{y}-{m:02d}' <= b:
        out.append(f'{y}-{m:02d}')
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return out


def one(item):
    sym, span = item
    p1h, pf = os.path.join(BARS, f'{sym}_1h.npy'), os.path.join(BARS, f'{sym}_funding.npy')
    ms = months_for(span)
    if not os.path.exists(p1h):
        parts = []
        for m in ms:
            df = dl.zip_frame(f'{BASE}/klines/{sym}/1h/{sym}-1h-{m}.zip')
            if df is not None and len(df):
                parts.append(df.iloc[:, [0, 1, 2, 3, 4, 5, 7, 9]].to_numpy(dtype=float))
        a = np.vstack(parts) if parts else np.zeros((0, 8))
        if len(a):
            a = a[np.argsort(a[:, 0], kind='stable')]
            a = a[np.r_[True, np.diff(a[:, 0]) > 0]]
            a = a[a[:, 0] < CUT_MS]
        np.save(p1h, a)
    if not os.path.exists(pf):
        rows = []
        for m in ms:
            df = dl.zip_frame(f'{BASE}/fundingRate/{sym}/{sym}-fundingRate-{m}.zip')
            if df is not None and len(df):
                rows.extend(df.iloc[:, [0, 2]].to_numpy(dtype=float).tolist())
        f = np.array(rows) if rows else np.zeros((0, 2))
        if len(f):
            f = f[np.argsort(f[:, 0])]
            f = f[f[:, 0] < CUT_MS]
        np.save(pf, f)
    return {'symbol': sym, 'months': len(ms), 'h1_rows': int(len(np.load(p1h))),
            'funding_rows': int(len(np.load(pf)))}


def download(workers):
    os.makedirs(BARS, exist_ok=True)
    p = r63.load_partition()
    items = [(s, p['months'][s]) for s in sorted(p['D63'] + p['L63'])]

    def safe(it):
        try:
            r = one(it)
        except Exception as e:                     # one symbol failing must not stop the rest; a re-run resumes
            r = {'symbol': it[0], 'error': str(e)}
        print(json.dumps(r), flush=True)
        return r
    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(safe, items))
    with open(os.path.join(OUT, 'download.json'), 'w') as f:
        json.dump({'n': len(res), 'errors': [r for r in res if 'error' in r], 'symbols': res}, f, indent=1)
    print(f"done: {len(res)} symbols, {sum('error' in r for r in res)} errors", flush=True)


# ----------------------------------------------------------------------------------------------
# Cleaning (§2)
# ----------------------------------------------------------------------------------------------
def raw(sym):
    return np.load(os.path.join(BARS, f'{sym}_1h.npy')), np.load(os.path.join(BARS, f'{sym}_funding.npy'))


def clean(a):
    """List of tramos, each [t, o, h, l, c, vol, qvol, taker_buy] on a full hourly grid."""
    if not len(a):
        return []
    a = a[np.isfinite(a[:, 1:5]).all(1) & (a[:, 1:5] > 0).all(1) & (a[:, 0] < CUT_MS)]
    live = np.flatnonzero(a[:, 5] > 0)
    if not len(live):
        return []
    a = a[:live[-1] + 1]                           # the life ends at the last bar that traded
    t = a[:, 0].astype(np.int64)
    cuts = np.flatnonzero(np.diff(t) // HOUR > MAX_FILL_H) + 1
    out = []
    for seg in np.split(np.arange(len(a)), cuts):
        s = a[seg]
        ts = s[:, 0].astype(np.int64)
        grid = np.arange(ts[0], ts[-1] + HOUR, HOUR)
        g = np.zeros((len(grid), 8))
        idx = (ts - ts[0]) // HOUR
        have = np.zeros(len(grid), bool)
        have[idx] = True
        g[:, 0] = grid
        g[idx, 1:] = s[:, 1:]
        # flat fill: O = H = L = C = previous close, no volume
        last = np.maximum.accumulate(np.where(have, np.arange(len(grid)), 0))
        miss = ~have
        g[miss, 1:5] = g[last[miss], 4][:, None]
        if len(g) > MIN_TRAMO_H:
            out.append(g)
    return out


def daily_qvol(tramos):
    """(days, quote volume) over the symbol's whole life; hours between tramos count as 0 volume."""
    t = np.concatenate([g[:, 0] for g in tramos]).astype(np.int64)
    q = np.concatenate([g[:, 6] for g in tramos])
    d0, d1 = t[0] // DAY * DAY, t[-1] // DAY * DAY
    days = np.arange(d0, d1 + DAY, DAY)
    v = np.zeros(len(days))
    np.add.at(v, (t // DAY * DAY - d0) // DAY, q)
    return days, v


def eligibility(tramos, first_ms):
    """Per day: (days, eligible, 30-day median quote volume), each from days strictly before."""
    days, v = daily_qvol(tramos)
    med = np.full(len(days), np.nan)
    if len(days) > VOL_WIN_D:
        w = np.lib.stride_tricks.sliding_window_view(v, VOL_WIN_D)[:-1]     # rows end at day i-1
        med[VOL_WIN_D:] = np.median(w, axis=1)
    age = (days - first_ms) / DAY
    return days, (age >= MIN_AGE_D) & (med >= MIN_QVOL), med


def slip_of(med):
    out = np.full(len(med), SLIP_TIERS[-1][1])
    m = np.nan_to_num(med, nan=-1.0)
    for lo, s in reversed(SLIP_TIERS):
        out[m >= lo] = s
    return out


def first_bar(a):
    ok = np.isfinite(a[:, 1:5]).all(1) & (a[:, 1:5] > 0).all(1)
    return int(a[ok][0, 0])


def load(sym):
    """{'tramos': [bars...], 'funding', 'days', 'elig', 'med', 'first'} for one symbol, or None."""
    a, f = raw(sym)
    tr = clean(a)
    if not tr:
        return None
    first = first_bar(a)                          # age counts from the symbol's first bar (§2)
    days, elig, med = eligibility(tr, first)
    return {'tramos': tr, 'funding': f, 'days': days, 'elig': elig, 'med': med, 'first': first}


def _year(ms):
    return np.asarray(ms, np.int64).astype('datetime64[ms]').astype('datetime64[Y]').astype(int) + 1970


def manifest():
    p = r63.load_partition()
    dev = set(p['D63'])
    out = {}
    for s in sorted(p['D63'] + p['L63']):
        a, f = raw(s)
        x = load(s)
        rec = {'set': 'D63' if s in dev else 'L63', 'rows': int(len(a)),
               'sha256': hashlib.sha256(a.tobytes() + f.tobytes()).hexdigest()}
        if x is None:
            rec['usable'] = False
        else:
            ends = [int(g[-1, 0]) for g in x['tramos']]
            yr = _year(x['days'])
            rec.update(usable=True, first=x['first'], last=ends[-1], n_tramos=len(x['tramos']),
                       delisted=bool(ends[-1] < DELIST_BEFORE_MS),
                       filled_h=int(sum(((g[:, 5] == 0) & (g[:, 1] == g[:, 4])).sum() for g in x['tramos'])),
                       elig_days=int(x['elig'].sum()),
                       elig_by_year={str(y): int(x['elig'][yr == y].sum()) for y in range(2020, 2025)})
        out[s] = rec
    with open(os.path.join(OUT, 'manifest.json'), 'w') as fh:
        json.dump(out, fh, indent=1)
    print(f'{len(out)} symbols, usable {sum(r.get("usable", False) for r in out.values())}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd')
    ap.add_argument('--workers', type=int, default=16)
    args = ap.parse_args()
    if args.cmd == 'download':
        download(args.workers)
    elif args.cmd == 'manifest':
        manifest()
    else:
        print(__doc__)
        sys.exit(1)
