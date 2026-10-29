"""r62 F0: free Binance data for the liquidation-cascade proxy (PROTOCOL_R62 §6).

USDT-M `liquidationSnapshot` was removed from data.binance.vision (empty prefix; Binance issue 337,
2026-10-06). What is left and free:
  - futures/um/daily/metrics: 5-minute open interest and taker ratios (proxy input);
  - futures/cm/daily/liquidationSnapshot: COIN-M forced orders, 2023-06-25 -> 2024-10-14 (only to
    validate the proxy; it is another market and too short to trade on).

Usage (run from research_scripts/, with `python -P` so neither cwd nor data/ can shadow a module (-I would also drop the user site-packages that hold numpy here)):
    python -P r62_liq.py download
    python -P r62_liq.py build        # parse, coverage report, proxy and AUC -> data/r62/liq_f0.json
"""
import csv
import hashlib
import io
import json
import os
import sys
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r62')
RAW = os.path.join(OUT, 'raw')
BASE = 'https://data.binance.vision/data/futures'
UM = ('BTCUSDT', 'ETHUSDT')
CM = {'BTCUSDT': 'BTCUSD_PERP', 'ETHUSDT': 'ETHUSD_PERP'}
# COIN-M contract face value in USD (Binance contract specs): quantities are in contracts.
CM_FACE = {'BTCUSD_PERP': 100.0, 'ETHUSD_PERP': 10.0}
UM_RANGE = (date(2020, 9, 1), date(2024, 12, 31))
CM_RANGE = (date(2023, 6, 25), date(2024, 10, 14))
DAY = 86_400_000
HOUR = 3_600_000
# §6.5 gates, fixed in the protocol before any data was read.
MIN_COVER, MIN_AUC, MIN_TOP_DAYS = 0.90, 0.70, 30


def _days(a, b):
    d = a
    while d <= b:
        yield d
        d += timedelta(days=1)


def _get(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read()


def _fetch(kind, sym, d):
    """Download one daily zip and check it against Binance's .CHECKSUM; returns a status string."""
    name = f'{sym}-{kind}-{d.isoformat()}.zip'
    seg = 'um' if kind == 'metrics' else 'cm'
    dst = os.path.join(RAW, kind, sym, name)
    if os.path.exists(dst):
        return 'cached'
    url = f'{BASE}/{seg}/daily/{kind}/{sym}/{name}'
    try:
        blob = _get(url)
    except Exception as e:  # missing days are a coverage fact, not an error
        return f'missing:{getattr(e, "code", type(e).__name__)}'
    try:
        want = _get(url + '.CHECKSUM').decode().split()[0]
    except Exception:
        want = None
    if want and hashlib.sha256(blob).hexdigest() != want:
        return 'bad_checksum'
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'wb') as f:
        f.write(blob)
    return 'ok' if want else 'ok_nochecksum'


def download():
    jobs = [('metrics', s, d) for s in UM for d in _days(*UM_RANGE)]
    jobs += [('liquidationSnapshot', CM[s], d) for s in UM for d in _days(*CM_RANGE)]
    with ThreadPoolExecutor(16) as ex:
        res = list(ex.map(lambda j: (j, _fetch(*j)), jobs))
    tally = {}
    for (kind, sym, _), st in res:
        k = f'{kind}/{sym}/{st.split(":")[0]}'
        tally[k] = tally.get(k, 0) + 1
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, 'liq_download.json'), 'w') as f:
        json.dump({'tally': tally, 'missing': sorted(f'{k}/{s}/{d}' for (k, s, d), st in res
                                                       if st.startswith('missing'))}, f, indent=1)
    print(json.dumps(tally, indent=1))


def _rows(path):
    with zipfile.ZipFile(path) as z:
        with z.open(z.namelist()[0]) as fh:
            rd = list(csv.reader(io.TextIOWrapper(fh)))
    if rd and not rd[0][0].replace('.', '').isdigit() and not rd[0][0][:4].isdigit():
        hdr, rd = rd[0], rd[1:]
    else:
        hdr = None
    return hdr, rd


def _ms(s):
    """metrics create_time is 'YYYY-MM-DD HH:MM:SS' UTC; snapshots use epoch ms."""
    if s.isdigit():
        return int(s)
    from datetime import datetime, timezone
    return int(datetime.strptime(s, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc).timestamp() * 1000)


def load_metrics(sym):
    """5-minute rows (t, oi_coins, oi_value, taker_ls_ratio), sorted and de-duplicated."""
    folder = os.path.join(RAW, 'metrics', sym)
    out = []
    for fn in sorted(os.listdir(folder)):
        hdr, rows = _rows(os.path.join(folder, fn))
        ix = {h: i for i, h in enumerate(hdr)} if hdr else None
        for r in rows:
            try:
                t = _ms(r[ix['create_time']] if ix else r[0])
                oi = float(r[ix['sum_open_interest']] if ix else r[2])
                oiv = float(r[ix['sum_open_interest_value']] if ix else r[3])
                tk = r[ix['sum_taker_long_short_vol_ratio']] if ix else r[7]
                out.append((t, oi, oiv, float(tk) if tk not in ('', None) else np.nan))
            except (ValueError, IndexError, KeyError):
                continue
    a = np.array(sorted(set(out)), dtype=float)
    a = a[a[:, 0] < 1_735_689_600_000]          # r58.CUT_MS: nothing from 2025
    _, keep = np.unique(a[:, 0], return_index=True)
    return a[keep]


def load_liqs(cm_sym):
    """Daily USD notional of COIN-M forced orders (filled quantity x face value)."""
    folder = os.path.join(RAW, 'liquidationSnapshot', cm_sym)
    by_day = {}
    for fn in sorted(os.listdir(folder)):
        hdr, rows = _rows(os.path.join(folder, fn))
        ix = {h: i for i, h in enumerate(hdr)} if hdr else None
        seen = set()  # issue 337 reports every row twice in these files
        for r in rows:
            key = tuple(r)
            if key in seen:
                continue
            seen.add(key)
            try:
                t = int(r[ix['time']] if ix else r[0])
                q = float(r[ix['accumulated_fill_quantity']] if ix else r[9])
            except (ValueError, IndexError, KeyError):
                continue
            d = t // DAY * DAY
            by_day[d] = by_day.get(d, 0.0) + q * CM_FACE[cm_sym]
    return by_day


def coverage(m):
    """Share of the expected 288 five-minute rows present per year, first non-null OI, gaps > 1 day."""
    t = m[:, 0]
    first = int(t[np.isfinite(m[:, 1]) & (m[:, 1] > 0)][0])
    years = {}
    for y in range(2020, 2025):
        # Calendar-year share: a feed that starts mid-year counts as missing before it starts.
        a = _ms(f'{y}-01-01 00:00:00')
        b = _ms(f'{y + 1}-01-01 00:00:00')
        n = int(((t >= a) & (t < b)).sum())
        years[str(y)] = round(n / max((b - a) / 300_000, 1), 4)
    gaps = np.diff(t)
    big = [(int(t[i]), round(float(gaps[i]) / DAY, 2)) for i in np.flatnonzero(gaps > DAY)]
    return {'first_ms': first, 'years': years, 'gaps_gt_1d': big}


def proxy_hourly(m):
    """Hourly cascade inputs: dOI z-score (negative = deleveraging) on hourly OI, causal 30-day sigma.

    Returns (hour_ts, z_doi) with sigma from the previous 720 hours only."""
    t = m[:, 0]
    h = (t // HOUR) * HOUR
    last = np.r_[np.flatnonzero(np.diff(h)), len(h) - 1]     # last 5-min row in each hour
    ht, oi = h[last], m[last, 1]
    d = np.r_[np.nan, np.diff(np.log(oi))]
    # Hours missing in the feed make the next diff span more than one hour: drop those diffs.
    d[1:][np.diff(ht) != HOUR] = np.nan
    z = np.full_like(d, np.nan)
    for i in range(720, len(d)):
        w = d[i - 720:i]
        w = w[np.isfinite(w)]
        if len(w) > 360 and w.std() > 0:
            z[i] = (d[i] - w.mean()) / w.std()
    return ht.astype(np.int64), z


def daily_intensity(ht, z, close_t, close):
    """§6.3: sum over the day's hours of max(0, -z_dOI) * |z_ret| (causal sigmas)."""
    r = np.r_[np.nan, np.diff(np.log(close))]
    zr = np.full_like(r, np.nan)
    for i in range(720, len(r)):
        w = r[i - 720:i]
        w = w[np.isfinite(w)]
        if len(w) > 360 and w.std() > 0:
            zr[i] = r[i] / w.std()
    zr_at = dict(zip(close_t.astype(np.int64).tolist(), zr))
    out = {}
    for t, zz in zip(ht.tolist(), z):
        # dOI over hour [t-1h, t] meets the return of the bar that opened at t-1h.
        rr = zr_at.get(t - HOUR)
        if rr is None or not np.isfinite(zz) or not np.isfinite(rr):
            continue
        out[t // DAY * DAY] = out.get(t // DAY * DAY, 0.0) + max(0.0, -zz) * abs(rr)
    return out


def auc(score, label):
    s, y = np.asarray(score, float), np.asarray(label, bool)
    pos, neg = s[y], s[~y]
    if not len(pos) or not len(neg):
        return None
    ranks = np.argsort(np.argsort(np.r_[pos, neg])) + 1.0
    # average ranks for ties
    allv = np.r_[pos, neg]
    for v in np.unique(allv):
        k = allv == v
        if k.sum() > 1:
            ranks[k] = ranks[k].mean()
    return float((ranks[:len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))


def build():
    rep = {'gates': {'min_cover': MIN_COVER, 'min_auc': MIN_AUC, 'min_top_days': MIN_TOP_DAYS}}
    ok = True
    for sym in UM:
        m = load_metrics(sym)
        cov = coverage(m)
        bars = np.load(os.path.join(HERE, 'data', 'r52', f'{sym}_1h.npy'))
        bars = bars[bars[:, 0] < 1_735_689_600_000]
        ht, z = proxy_hourly(m)
        inten = daily_intensity(ht, z, bars[:, 0], bars[:, 4])
        liq = load_liqs(CM[sym])
        days = sorted(set(liq) & set(inten))
        lv = np.array([liq[d] for d in days])
        top = lv >= np.quantile(lv, 0.9)
        a = auc([inten[d] for d in days], top)
        cover_ok = all(cov['years'][y] >= MIN_COVER for y in ('2021', '2022', '2023', '2024'))
        sym_ok = cover_ok and a is not None and a >= MIN_AUC and int(top.sum()) >= MIN_TOP_DAYS
        ok &= sym_ok
        rep[sym] = {'coverage': cov, 'cm_symbol': CM[sym], 'cm_days': len(liq), 'joint_days': len(days),
                    'top_decile_days': int(top.sum()), 'auc': None if a is None else round(a, 4),
                    'cover_ok': cover_ok, 'pass': sym_ok,
                    'rho_spearman': round(float(np.corrcoef(np.argsort(np.argsort(lv)),
                                                            np.argsort(np.argsort([inten[d] for d in days])))[0, 1]), 4)}
        np.savez(os.path.join(OUT, f'oi_{sym}.npz'), ht=ht, z_doi=z)
    rep['cascade_enabled'] = bool(ok)
    with open(os.path.join(OUT, 'liq_f0.json'), 'w') as f:
        json.dump(rep, f, indent=1)
    print(json.dumps(rep, indent=1))


if __name__ == '__main__':
    {'download': download, 'build': build}[sys.argv[1]]()
