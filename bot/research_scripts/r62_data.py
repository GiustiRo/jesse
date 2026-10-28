"""r62 F0: 1h and daily bars for the factory (PROTOCOL_R62 §1), native, no Jesse DB.

CFDs come from the Dukascopy 1-minute CSVs in data/ (BID, CFD proxy); BTC/ETH from the r52 perpetual
1h arrays with their funding. Everything is cut at r58.CUT_MS (2025-01-01, exclusive).

    python -P r62_data.py build
"""
import hashlib
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
OUT = os.path.join(DATA, 'r62', 'bars')
MANIFEST = os.path.join(DATA, 'r62', 'bars_manifest.json')
CUT_MS = 1_735_689_600_000          # r58.CUT_MS
FROM_MS = 1_506_816_000_000         # 2017-10-01: a year of warmup before the 2018-10-01 window
HOUR, DAY = 3_600_000, 86_400_000
T, O, H, L, C, V = range(6)

CSV = {
    'XAU': ['XAUUSD_div1_1m_2010-01-01_2025-12-31.csv'],
    'SPX': ['USA500IDXUSD_div10_1m_2010-01-01_2025-12-31.csv'],
    # LIGHTCMD has no rows 2020-04..07 (the negative-price period); the gap is left open.
    'WTI': ['LIGHTCMDUSD_div1_1m_2010-01-01_2020-03-31.csv', 'LIGHTCMDUSD_div1_1m_2020-08-01_2025-12-31.csv'],
    'GAS': ['GASCMDUSD_div1_1m_2010-01-01_2025-12-31.csv'],
    'BOND': ['USTBONDTRUSD_div1_1m_2018-03-01_2025-12-31.csv'],
    'XAG': ['XAGUSD_div1_1m_2010-01-01_2025-12-31.csv'],
    'NDX': ['USATECHIDXUSD_div1_1m_2010-01-01_2025-12-31.csv'],
    'COPPER': ['COPPERCMDUSD_div1_1m_2010-01-01_2025-12-31.csv'],
    'DEU': ['DEUIDXEUR_div1_1m_2010-01-01_2025-12-31.csv'],
}
CRYPTO = {'BTC': 'BTCUSDT', 'ETH': 'ETHUSDT'}
ETF = {'EWJ': 'EWJ_daily_2000-01-01_2025-12-31.csv', 'EWY': 'EWY_daily_2000-01-01_2025-12-31.csv'}
CORE = ['BTC', 'ETH', 'XAU', 'SPX', 'WTI', 'GAS', 'BOND']
VALID = ['XAG', 'NDX', 'COPPER', 'DEU']


def minutes_to_hours(m):
    """Aggregate 1m rows [t,o,h,l,c,v] into UTC hourly bars (only hours with minutes)."""
    hr = (m[:, T].astype(np.int64) // HOUR) * HOUR
    cut = np.flatnonzero(np.diff(hr)) + 1
    s, e = np.r_[0, cut], np.r_[cut, len(m)]
    out = np.empty((len(s), 6))
    out[:, T] = hr[s]
    out[:, O] = m[s, O]
    out[:, C] = m[e - 1, C]
    out[:, H] = np.maximum.reduceat(m[:, H], s)
    out[:, L] = np.minimum.reduceat(m[:, L], s)
    out[:, V] = np.add.reduceat(m[:, V], s)
    return out


def hours_to_days(h, cfd):
    """UTC daily bars from hourly ones; CFD Saturday/Sunday hours join Monday (r50 convention)."""
    day = (h[:, T].astype(np.int64) // DAY) * DAY
    if cfd:
        wd = ((day // DAY) + 3) % 7          # 0 = Monday
        day = np.where(wd == 5, day + 2 * DAY, np.where(wd == 6, day + DAY, day))
        keep = day < CUT_MS
        h, day = h[keep], day[keep]
    cut = np.flatnonzero(np.diff(day)) + 1
    s, e = np.r_[0, cut], np.r_[cut, len(h)]
    out = np.empty((len(s), 6))
    out[:, T] = day[s]
    out[:, O] = h[s, O]
    out[:, C] = h[e - 1, C]
    out[:, H] = np.maximum.reduceat(h[:, H], s)
    out[:, L] = np.minimum.reduceat(h[:, L], s)
    out[:, V] = np.add.reduceat(h[:, V], s)
    return out


def load_csv(name):
    import pandas as pd
    parts = []
    for fn in CSV[name]:
        df = pd.read_csv(os.path.join(DATA, fn), dtype=float)
        a = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']].to_numpy()
        parts.append(a[(a[:, 0] >= FROM_MS) & (a[:, 0] < CUT_MS)])
    m = np.concatenate(parts)
    m = m[np.argsort(m[:, 0], kind='stable')]
    _, keep = np.unique(m[:, 0], return_index=True)
    return m[keep]


def load_etf(name):
    import pandas as pd
    df = pd.read_csv(os.path.join(DATA, 'r50', 'etf', ETF[name]))
    cols = {c.lower(): c for c in df.columns}
    t = pd.to_datetime(df[cols.get('date', df.columns[0])], utc=True).astype('int64') // 10 ** 6
    a = np.c_[t, df[cols['open']], df[cols['high']], df[cols['low']], df[cols['close']],
              df[cols.get('volume', cols['close'])]].astype(float)
    # Dividend-adjust OHLC with Yahoo's adjclose so the transfer test sees total returns.
    if 'adjclose' in cols:
        a[:, 1:5] *= (df[cols['adjclose']].to_numpy(float) / df[cols['close']].to_numpy(float))[:, None]
    a = a[(a[:, 0] >= FROM_MS) & (a[:, 0] < CUT_MS)]
    return a


def _save(name, **arrays):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f'{name}.npz')
    np.savez(path, **arrays)
    return path


def build():
    man = {}
    for name in CSV:
        h = minutes_to_hours(load_csv(name))
        d = hours_to_days(h, cfd=True)
        man[name] = _save(name, h1=h, d1=d)
        print(name, len(h), len(d))
    for name, sym in CRYPTO.items():
        a = np.load(os.path.join(DATA, 'r52', f'{sym}_1h.npy'))
        a = a[a[:, 0] < CUT_MS]
        h = a[:, [0, 1, 2, 3, 4, 5]].copy()       # r52 layout: t, o, h, l, c, v, quote_vol, trades
        f = np.load(os.path.join(DATA, 'r52', f'{sym}_funding.npy'))
        f = f[f[:, 0] < CUT_MS]
        man[name] = _save(name, h1=h, d1=hours_to_days(h, cfd=False), funding=f)
        print(name, len(h))
    for name in ETF:
        man[name] = _save(name, d1=load_etf(name))
    out = {}
    for name, p in man.items():
        with open(p, 'rb') as fh:
            out[name] = {'file': os.path.relpath(p, HERE).replace('\\', '/'),
                         'sha256': hashlib.sha256(fh.read()).hexdigest()}
    with open(MANIFEST, 'w') as f:
        json.dump(out, f, indent=1)


def load(name):
    """{'h1','d1'[,'funding']} for one asset, sha-checked against the manifest."""
    with open(MANIFEST) as f:
        ent = json.load(f)[name]
    p = os.path.join(HERE, ent['file'])
    with open(p, 'rb') as fh:
        assert hashlib.sha256(fh.read()).hexdigest() == ent['sha256'], f'{name}: bars sha mismatch'
    z = np.load(p)
    out = {k: z[k] for k in z.files}
    for k, v in out.items():
        assert (v[:, 0] < CUT_MS).all(), f'{name}/{k}: data after the cut'
    return out


if __name__ == '__main__':
    {'build': build}[sys.argv[1]]()
