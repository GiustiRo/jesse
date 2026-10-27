"""r58: what separates a good C6 breakout from a bad one (PROTOCOL_R58.md).

Host Python (network; the container's DNS failed in r52):
    python research_scripts/r58.py oi_probe      # F0: OI history coverage on data.binance.vision
    python research_scripts/r58.py n3_select     # F0: the N3 universe, committed before any download
    python research_scripts/r58.py n3_download   # F0: 1h klines + funding of N3, 2020-01..2024-12
Research container:
    python research_scripts/r58.py n3_panel      # F0: panel U50 + N3, H20/H40 labels, P5 on N3
    python research_scripts/r58.py states        # F0: per-bar and per-day partitions, before any join
    python research_scripts/r58.py selftest      # F0: cuts, reconciliation and reproduction checks
    python research_scripts/r58.py diag          # F1: sweep on the U50-alt C6 trades (N + 0)

No C6 trade is read before `states` has written data/r58/f0_cuts.json and f0_bars_*.npz. Every
array stops at 2024-12-31; 2025 is sealed (the r54 event file holds 544 trades of 2025, dropped at
load). A trade's variables come from its signal bar: the 4h bar whose close places the order (R2
fills at that close; R3 places a limit there that fills on the next bar), so every value is known
when the order is sent. Daily states use the last fully closed day before the signal close.
"""
import bisect
import hashlib
import json
import math
import os
import sys
import urllib.error
import urllib.request

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
OUT = os.path.join(DATA, 'r58')
N3_DIR = os.path.join(OUT, 'n3')
U50_DIR = os.path.join(DATA, 'r52')
N2_DIR = os.path.join(DATA, 'r56', 'n2')
DAY = 86_400_000
H4 = 4 * 3_600_000
CUT_MS = 1735689600000                    # 2025-01-01 00:00 UTC, exclusive
SIM_FROM = 1602720000000                  # 2020-10-15, r54 V1 start
N3_PICK = 30
VISION = 'https://data.binance.vision/data/futures/um/daily/metrics'

# Bar-feature windows, fixed in PROTOCOL_R58.md §0 before any trade is read.
RELVOL_BARS = 180                         # 30 days of 4h bars, the median volume reference
RELVOL_MIN = 90
SIG_BARS = 180                            # sigma30: R1's 30-day std of 4h log returns
FUND_WIN = 7 * DAY
FUND_MIN_EVENTS = 90                      # ~30 days of 8h settlements before a percentile exists
FUND_SAT = 0.90
ROUND_ATR = 1.0
ROUND_STEPS = (1.0, 2.0, 5.0, 10.0)       # round levels {1, 2, 5} x 10^k


def log(x):
    print(x, flush=True)


def ms(day):
    import pandas as pd
    return int(pd.Timestamp(day, tz='UTC').value // 10**6)


# ----------------------------------------------------------------------------------------------
# Host: OI probe, N3 selection and download
# ----------------------------------------------------------------------------------------------
def _status(url):
    req = urllib.request.Request(url, method='HEAD')
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


def oi_probe():
    """First day with a daily `metrics` file (5-minute OI) for BTC and three U50 alts. The rule
    (PROTOCOL_R58.md §0, V5b) needs OI from <= 2021-07-01 on every bank; monthly files do not exist."""
    import pandas as pd
    days = [d.strftime('%Y-%m-%d') for d in pd.date_range('2021-06-01', '2022-01-15', freq='D')]
    out = {'source': VISION, 'monthly_files': _status(VISION.replace('daily', 'monthly') + '/BTCUSDT/BTCUSDT-metrics-2022-01.zip'),
           'first_day': {}}
    for sym in ('BTCUSDT', 'SOLUSDT', 'AAVEUSDT', 'CHZUSDT'):
        lo, hi = 0, len(days) - 1          # binary search: files are contiguous once they start
        if _status(f'{VISION}/{sym}/{sym}-metrics-{days[0]}.zip') == 200:
            out['first_day'][sym] = f'<= {days[0]}'
            continue
        while lo < hi:
            mid = (lo + hi) // 2
            if _status(f'{VISION}/{sym}/{sym}-metrics-{days[mid]}.zip') == 200:
                hi = mid
            else:
                lo = mid + 1
        out['first_day'][sym] = days[lo]
    alts = [v for k, v in out['first_day'].items() if k != 'BTCUSDT']
    out['rule_cover_2021_07'] = all(v.startswith('<=') for v in alts)
    out['decision'] = 'V5b runs' if out['rule_cover_2021_07'] else 'V5b dropped (no OI before the alts first day); no N_tematica'
    json.dump(out, open(os.path.join(OUT, 'oi_probe.json'), 'w'), indent=1)
    log(json.dumps(out))


def n3_select():
    """r56_fresh's N2 rule on today's exchange data, excluding U50 and N2: up to 30 symbols."""
    import r56_fresh as fr
    os.makedirs(N3_DIR, exist_ok=True)
    u50 = {u['symbol'] for u in json.load(open(os.path.join(U50_DIR, 'universe50.json')))}
    n2 = {u['symbol'] for u in json.load(open(os.path.join(N2_DIR, 'universe_n2.json')))['selected']}
    info = fr._get(f'{fr.FAPI}/exchangeInfo')
    vol = {t['symbol']: float(t['quoteVolume']) for t in fr._get(f'{fr.FAPI}/ticker/24hr')}
    cands = []
    for s in info['symbols']:
        if (s.get('contractType') == 'PERPETUAL' and s.get('quoteAsset') == 'USDT' and s.get('status') == 'TRADING'
                and int(s.get('onboardDate', 1 << 62)) < fr.ONBOARD_BEFORE_MS and s['symbol'] not in u50
                and s['symbol'] not in n2 and s.get('baseAsset') not in fr.STABLES
                # r58 amendment before any download: index contracts (BTCDOM) are not coins.
                and s.get('underlyingType', 'COIN') != 'INDEX'):
            cands.append({'symbol': s['symbol'], 'onboard': int(s['onboardDate']), 'vol24h': vol.get(s['symbol'], 0.0)})
    cands.sort(key=lambda x: -x['vol24h'])
    out = {'rule': ('r56_fresh N2 rule (USDT-M PERPETUAL, TRADING, onboarded before 2022-07-01, base not a '
                    'stablecoin), excluding U50, N2 and index contracts (underlyingType INDEX); the 30 with the '
                    'largest 24h quote volume. Committed '
                    'before any download.'),
           'n_candidates': len(cands), 'selected': cands[:N3_PICK]}
    json.dump(out, open(os.path.join(OUT, 'universe_n3.json'), 'w'), indent=2)
    log(json.dumps([c['symbol'] for c in out['selected']]) + f' {len(cands)} candidates')


def n3_download(workers=6):
    import r52_download as dl
    import r56_fresh as fr
    from concurrent.futures import ThreadPoolExecutor
    dl.MONTHS = fr.MONTHS              # 2020-01..2024-12: 2025 is not even fetched
    fr.OUT = N3_DIR
    sel = [c['symbol'] for c in json.load(open(os.path.join(OUT, 'universe_n3.json')))['selected']]
    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(fr._one, sel))
    for r in res:
        assert 'error' in r or r['h1_last'] is None or r['h1_last'] < CUT_MS, 'data past 2024'
    json.dump({'symbols': res, 'months': [fr.MONTHS[0], fr.MONTHS[-1]]}, open(os.path.join(OUT, 'manifest_n3.json'), 'w'), indent=1)
    log('done')


# ----------------------------------------------------------------------------------------------
# Container: N3 panel and P5 forecasts
# ----------------------------------------------------------------------------------------------
def _p5_preds(panel, labels, sfx):
    import r56_eval as ev
    ev.MODE70, ev.CACHE_SFX, ev.PANEL70, ev.LABELS70 = True, sfx, panel, labels
    ev._CTX.clear()
    try:
        return ev.fit_predict(ev.SPECS['P5']['feats'](), 'range40', coins='n2', kind='logit')
    finally:
        ev.MODE70, ev.CACHE_SFX, ev.PANEL70, ev.LABELS70 = False, '', 'panel70', 'labels70'
        ev._CTX.clear()


def n3_panel():
    """panel_n3.npz / labels_n3.npz (U50 + N3, as r56_panel.run_panel70) and P5 on N3. The model is
    refitted per quarter on the same U50 development coins as for N2, so the N2 run is first
    reproduced bit for bit from panel70 to prove the path."""
    import r56_eval as ev
    import r56_panel as pn
    rep = _p5_preds('panel70', 'labels70', '_70')
    ref = np.load(os.path.join(ev.OUT, 'pred_n2_P5_range40.npy')).astype(float)
    ok = np.allclose(np.nan_to_num(rep, nan=-9), np.nan_to_num(ref, nan=-9), atol=1e-6)
    log(f'N2 P5 reproduction: {ok}')
    assert ok, 'the r56 P5 path does not reproduce pred_n2_P5_range40'
    n3 = [u['symbol'] for u in json.load(open(os.path.join(OUT, 'universe_n3.json')))['selected']
          if os.path.exists(os.path.join(N3_DIR, f"{u['symbol']}_1h.npy"))]
    syms = [u['symbol'] for u in pn.universe()] + n3
    day_ms, syms, P = pn.load_panel(syms, {x: N3_DIR for x in n3})
    t20 = json.load(open(os.path.join(pn.OUT, 'f0_labels.json')))['thresholds']
    t40 = json.load(open(os.path.join(pn.OUT, 'f6_labels_h40.json')))['thresholds']
    L20, _ = pn.label_set(P, day_ms, 20, t20['a'], t20['e'], t20['k'])
    L40, _ = pn.label_set(P, day_ms, 40, t20['a'], t40['e'], t40['k'], suffix='40')
    np.savez_compressed(os.path.join(pn.OUT, 'panel_n3.npz'), day_ms=day_ms, syms=np.array(syms),
                        is_n2=np.array([x in n3 for x in syms]),
                        **{f: P[f] for f in ('o', 'h', 'l', 'c', 'rv', 'qv', 'atr', 'elig')})
    np.savez_compressed(os.path.join(pn.OUT, 'labels_n3.npz'), **L20, **L40)
    preds = _p5_preds('panel_n3', 'labels_n3', '_n3')
    k = np.array([x in n3 for x in syms])
    np.save(os.path.join(OUT, 'pred_n3_P5_range40.npy'), preds[:, k].astype(np.float32))
    json.dump({'n3_syms': n3, 'n2_p5_reproduced': bool(ok),
               'n3_p5_rows': int(np.isfinite(preds[:, k, 1]).sum())},
              open(os.path.join(OUT, 'n3_panel.json'), 'w'), indent=1)
    log(f'panel_n3: {len(syms)} coins, {len(n3)} N3')


# ----------------------------------------------------------------------------------------------
# Container: partitions (bars and days), written before any trade is read
# ----------------------------------------------------------------------------------------------
def banks():
    u50 = [u['symbol'] for u in json.load(open(os.path.join(U50_DIR, 'universe50.json')))]
    n2 = [u['symbol'] for u in json.load(open(os.path.join(N2_DIR, 'universe_n2.json')))['selected']]
    n3 = json.load(open(os.path.join(OUT, 'n3_panel.json')))['n3_syms']
    return {'u50': ([s for s in u50 if s not in ('BTCUSDT', 'ETHUSDT')], U50_DIR), 'n2': (n2, N2_DIR),
            'n3': (n3, N3_DIR)}


def h4_bars(src, sym):
    """r54_v1.h4_bars (Jesse layout T, O, C, H, L, V) from `src`, cut at 2024-12-31, plus the 4h
    taker-buy volume (column 7 of the r52 1h rows)."""
    from r50_harness import T, O, C, H, L, V
    a = np.load(os.path.join(src, f'{sym}_1h.npy'))
    a = a[a[:, 0] + 3_600_000 <= CUT_MS]
    b = (a[:, 0] // H4 * H4).astype(np.int64)
    cut = np.flatnonzero(np.diff(b)) + 1
    s, e = np.r_[0, cut], np.r_[cut, len(a)]
    out = np.empty((len(s), 6))
    out[:, T] = b[s]
    out[:, O] = a[s, 1]
    out[:, C] = a[e - 1, 4]
    out[:, H] = np.maximum.reduceat(a[:, 2], s)
    out[:, L] = np.minimum.reduceat(a[:, 3], s)
    out[:, V] = np.add.reduceat(a[:, 5], s)
    return out, np.add.reduceat(a[:, 7], s), a


def next_round(p):
    """Smallest level in {1, 2, 5} x 10^k strictly above p."""
    k = math.floor(math.log10(p))
    for m in ROUND_STEPS:
        lv = m * 10.0 ** k
        if lv > p * (1 + 1e-12):
            return lv
    return 10.0 ** (k + 1) * 2


def funding_pct(src, sym, close_ts):
    """Per bar close: the trailing 7-day funding sum and its percentile in the coin's own history
    of 7-day sums at settlements up to then (expanding; NaN before 90 settlements)."""
    f = np.load(os.path.join(src, f'{sym}_funding.npy'))
    f = f[f[:, 0] < CUT_MS]
    if not len(f):
        n = len(close_ts)
        return np.full(n, np.nan), np.full(n, np.nan)
    t, r = f[:, 0].astype(np.int64), f[:, 1]
    cs = np.r_[0.0, np.cumsum(r)]
    lo = np.searchsorted(t, t - FUND_WIN, side='right')
    s7 = cs[np.arange(1, len(t) + 1)] - cs[lo]            # sum over (t - 7d, t]
    pct = np.full(len(t), np.nan)
    seen = []
    for i, x in enumerate(s7):
        bisect.insort(seen, x)
        if i + 1 >= FUND_MIN_EVENTS:
            pct[i] = bisect.bisect_right(seen, x) / len(seen)
    k = np.searchsorted(t, close_ts, side='right') - 1     # last settlement at or before the close
    ok = k >= 0
    out_s, out_p = np.full(len(close_ts), np.nan), np.full(len(close_ts), np.nan)
    out_s[ok], out_p[ok] = s7[k[ok]], pct[k[ok]]
    return out_s, out_p


def bar_features(src, sym):
    """(close_ts, columns) per 4h bar: relvol, taker, sigma30, atr14, close, round_atr, fund7, fund_pct."""
    import jesse.indicators as ta
    from r50_harness import T, C, V
    bars, tbv, _ = h4_bars(src, sym)
    close_ts = (bars[:, T] + H4).astype(np.int64)
    v, c = bars[:, V], bars[:, C]
    n = len(bars)
    relvol = np.full(n, np.nan)
    for i in range(RELVOL_MIN, n):
        ref = np.median(v[max(0, i - RELVOL_BARS):i])
        relvol[i] = v[i] / ref if ref > 0 else np.nan
    taker = np.where(v > 0, 2 * tbv / np.where(v > 0, v, 1) - 1, np.nan)
    lr = np.r_[np.nan, np.diff(np.log(c))]
    sig = np.full(n, np.nan)
    for i in range(SIG_BARS, n):
        sig[i] = np.std(lr[i - SIG_BARS + 1:i + 1])
    atr = ta.atr(bars, period=14, sequential=True)
    rnd = np.array([(next_round(c[i]) - c[i]) / atr[i] if np.isfinite(atr[i]) and atr[i] > 0 else np.nan
                    for i in range(n)])
    f7, fp = funding_pct(src, sym, close_ts)
    cols = np.column_stack([relvol, taker, sig, atr, c, rnd, f7, fp])
    return close_ts, cols


BAR_COLS = ('relvol', 'taker', 'sigma30', 'atr14', 'close', 'round_atr', 'fund7', 'fund_pct')


def day_states():
    """Per bank: days, persist_vol (r56 vara) and p(range 40d) of P5, columns in bank order."""
    import r56_eval as ev
    import r57
    L = np.load(os.path.join(ev.OUT, 'labels.npz'))
    z = np.load(os.path.join(ev.OUT, 'panel.npz'))
    days, syms = z['day_ms'], [str(s) for s in z['syms']]
    hold = json.load(open(os.path.join(ev.OUT, 'holdout.json')))['holdout']
    is_hold = np.array([s in hold for s in syms])
    R = r57._merge(r57._load('pred_P5_range40'), r57._load('pred_hold_P5_range40'), is_hold)[..., 1]
    out = {}
    b = banks()
    j = [syms.index(s) for s in b['u50'][0]]
    out['u50'] = {'days': days, 'persist': L['persist_vol'][:, j], 'p_rng': R[:, j]}
    z7, L7 = np.load(os.path.join(ev.OUT, 'panel70.npz')), np.load(os.path.join(ev.OUT, 'labels70.npz'))
    s7 = [str(s) for s in z7['syms']]
    n2c = np.flatnonzero(z7['is_n2'])
    p7 = r57._load('pred_n2_P5_range40')[..., 1]
    j = [s7.index(s) for s in b['n2'][0]]
    assert set(j) <= set(n2c.tolist()) and (z7['day_ms'] == days).all()
    out['n2'] = {'days': days, 'persist': L7['persist_vol'][:, j], 'p_rng': p7[:, j]}
    z3, L3 = np.load(os.path.join(ev.OUT, 'panel_n3.npz')), np.load(os.path.join(ev.OUT, 'labels_n3.npz'))
    s3 = [str(s) for s in z3['syms']]
    n3c = [s3[k] for k in np.flatnonzero(z3['is_n2'])]
    p3 = np.load(os.path.join(OUT, 'pred_n3_P5_range40.npy')).astype(float)[..., 1]
    assert n3c == b['n3'][0] and (z3['day_ms'] == days).all()
    j = [s3.index(s) for s in b['n3'][0]]
    out['n3'] = {'days': days, 'persist': L3['persist_vol'][:, j], 'p_rng': p3}
    return out


def dvol_states():
    """BTC/ETH per day: DVOL close (annualised, /100) minus the 20-day realised vol from 1h returns
    (sqrt(365/20 * sum of daily RV)), and the median cut over 2021-03-24..2024-12-31 days."""
    import pandas as pd
    import r56_eval as ev
    z = np.load(os.path.join(ev.OUT, 'panel.npz'))
    days, syms = z['day_ms'], [str(s) for s in z['syms']]
    out = {}
    for coin in ('BTC', 'ETH'):
        d = pd.read_csv(os.path.join(OUT, f'dvol_{coin}_1d.csv'))
        d = d[d['ts_ms'] < CUT_MS]
        dv = pd.Series(d['close'].values / 100, index=d['ts_ms'].values).reindex(days).values
        rv = z['rv'][:, syms.index(f'{coin}USDT')]
        rv20 = np.sqrt(365 / 20 * pd.Series(rv).rolling(20).sum().values)
        out[coin] = dv - rv20
    m = np.concatenate([out[k][(days >= ms('2021-03-24')) & np.isfinite(out[k])] for k in out])
    return days, out, float(np.median(m))


def states():
    os.makedirs(OUT, exist_ok=True)
    b = banks()
    feats = {}
    for bank, (syms, src) in b.items():
        arr = {}
        for s in syms:
            ts, cols = bar_features(src, s)
            assert ts[-1] <= CUT_MS
            arr[f'{s}__ts'], arr[f'{s}__x'] = ts, cols
        np.savez_compressed(os.path.join(OUT, f'f0_bars_{bank}.npz'), **arr)
        feats[bank] = arr
        log(f'{bank}: {len(syms)} coins')
    # Cuts on every U50-alt bar from the r54 start to 2024-12-31 (no trade involved).
    pool = {k: [] for k in ('relvol', 'taker', 'sigma30')}
    for s in b['u50'][0]:
        ts, x = feats['u50'][f'{s}__ts'], feats['u50'][f'{s}__x']
        m = ts >= SIM_FROM
        for k in pool:
            v = x[m, BAR_COLS.index(k)]
            pool[k].append(v[np.isfinite(v)])
    cuts = {k: [float(q) for q in np.quantile(np.concatenate(v), [1 / 3, 2 / 3])] for k, v in pool.items()}
    ds = day_states()
    np.savez_compressed(os.path.join(OUT, 'f0_days.npz'), **{f'{bk}__{k}': v for bk, d in ds.items() for k, v in d.items()})
    ddays, dv, dcut = dvol_states()
    np.savez_compressed(os.path.join(OUT, 'f0_dvol.npz'), days=ddays, BTC=dv['BTC'], ETH=dv['ETH'])
    p_cut = json.load(open(os.path.join(DATA, 'r57', 'f0_cuts.json')))['p_range_cut_q2_3_dev']
    shares = {}
    for bank, (syms, _) in b.items():
        x = np.concatenate([feats[bank][f'{s}__x'][feats[bank][f'{s}__ts'] >= SIM_FROM] for s in syms])
        pe, pr = ds[bank]['persist'], ds[bank]['p_rng']
        shares[bank] = {
            'bars': int(len(x)),
            'relvol_top': float(np.nanmean(x[:, 0] >= cuts['relvol'][1])),
            'taker_top': float(np.nanmean(x[:, 1] >= cuts['taker'][1])),
            'round_near': float(np.nanmean(x[:, 5] < ROUND_ATR)),
            'fund_sat': float(np.nanmean(x[np.isfinite(x[:, 7]), 7] >= FUND_SAT)),
            'persist_compression_coin_days': float(np.mean(pe[np.isfinite(pe)] == 0)),
            'p_range_high_coin_days': float(np.mean(pr[np.isfinite(pr)] >= p_cut))}
    info = {'protocol': 'PROTOCOL_R58.md §0', 'bar_columns': BAR_COLS, 'tercile_cuts_u50_alt_bars': cuts,
            'p_range_cut': p_cut, 'fund_sat_pct': FUND_SAT, 'round_atr': ROUND_ATR, 'dvol_minus_rv_median': dcut,
            'banks': {k: v[0] for k, v in b.items()}, 'class_shares_on_bars_and_days': shares}
    json.dump(info, open(os.path.join(OUT, 'f0_cuts.json'), 'w'), indent=1)
    log(json.dumps(info)[:3000])


# ----------------------------------------------------------------------------------------------
# Container: selftest (reads C6 events only to count and reproduce, never joined with states)
# ----------------------------------------------------------------------------------------------
def load_events(path=os.path.join(U50_DIR, 'v1_events.json')):
    ev_ = json.load(open(path))
    kept = [e for e in ev_ if e['opened'] < CUT_MS]
    return kept, len(ev_) - len(kept)


def selftest():
    import r54_v1 as v1
    import r57
    import r50_f1b as fb
    from r50_harness import T
    res = {}
    kept, dropped = load_events()
    res['events'] = {'kept_le_2024': len(kept), 'dropped_2025': dropped,
                     'closed_after_cut_among_kept': sum(e['closed'] >= CUT_MS for e in kept)}
    assert all(e['opened'] < CUT_MS for e in kept)
    # r57 F1 sample: 2021-07-02+ with a T3 state and a persistence state (r57.diag_trades filter).
    s = r57.load_states()
    col = {x: j for j, x in enumerate(s['syms'])}
    w = [e for e in kept if e['opened'] >= r57.DIAG_FROM]
    no_t3 = no_pe = 0
    for e in w:
        r = r57.row_for(s['days'], e['opened'])
        j = col[e['sym']]
        if int(s['s_t3'][r, j]) < 0:
            no_t3 += 1
        elif not np.isfinite(s['persist'][r, j]):
            no_pe += 1
    res['r57_reconciliation'] = {'window_2021_07_02_2024': len(w), 'no_t3_state': no_t3, 'no_persist': no_pe,
                                 'r57_sample': len(w) - no_t3 - no_pe}
    assert len(w) - no_t3 - no_pe == 1408, res['r57_reconciliation']
    # Signal bar: every R2 opens at a 4h close; every R3 at the close after its signal bar.
    res['opened_on_4h_close'] = bool(all(e['opened'] % H4 == 0 for e in kept))
    # 4h aggregation equals r54_v1.h4_bars on the same rows.
    a, _, _ = h4_bars(U50_DIR, 'SOLUSDT')
    v1.DATA = U50_DIR
    ref, _ = v1.h4_bars('SOLUSDT')
    res['h4_equal_r54'] = bool(np.array_equal(a, ref[:len(a)]))
    # Frozen C6 on three alts, data cut at 2024-12-31, reproduces the stored trades that close before.
    rep = {}
    for sym in ('SOLUSDT', 'AVAXUSDT', 'DOGEUSDT'):
        bars, _, h1 = h4_bars(U50_DIR, sym)
        start = max(SIM_FROM, int(bars[min(v1.WARM_BARS, len(bars) - 1), T]))
        got = []
        for retest in (False, True):
            ts, eq, acct = v1.simulate(bars, start, fb.r2_r3_decider(bars, retest), v1.funding_cursor(sym, h1, int(bars[0, T])))
            got += [(int(t['opened']), round(float(t['pnl']), 6)) for t in acct.trades if t['closed'] is not None and t['closed'] < CUT_MS]
        want = [(e['opened'], round(e['pnl'], 6)) for e in kept if e['sym'] == sym and e['closed'] < CUT_MS]
        rep[sym] = {'n': len(want), 'equal': sorted(got) == sorted(want)}
    res['c6_reproduction'] = rep
    # labels70's first 50 columns are labels.npz (persistence on N2 comes from the same classifier).
    import r56_eval as ev
    L, L7 = np.load(os.path.join(ev.OUT, 'labels.npz')), np.load(os.path.join(ev.OUT, 'labels70.npz'))
    res['labels70_u50_equal'] = bool(np.array_equal(L['persist_vol'], L7['persist_vol'][:, :50], equal_nan=True))
    L3 = np.load(os.path.join(ev.OUT, 'labels_n3.npz'))
    res['labels_n3_u50_equal'] = bool(np.array_equal(L['persist_vol'], L3['persist_vol'][:, :50], equal_nan=True))
    res['n3_panel'] = json.load(open(os.path.join(OUT, 'n3_panel.json')))
    ok = (res['opened_on_4h_close'] and res['h4_equal_r54'] and all(v['equal'] for v in rep.values())
          and res['labels70_u50_equal'] and res['labels_n3_u50_equal'] and res['n3_panel']['n2_p5_reproduced'])
    res['pass'] = bool(ok)
    json.dump(res, open(os.path.join(OUT, 'f0_selftest.json'), 'w'), indent=1)
    log(json.dumps(res))
    assert ok


# ----------------------------------------------------------------------------------------------
# F1: diagnostic sweep on the U50-alt C6 trades (PROTOCOL_R58.md §2), N + 0
# ----------------------------------------------------------------------------------------------
SEED, N_BOOT = 58, 5000
YEARS = ('2021', '2022', '2023', '2024')
CANDIDATES = ('V1', 'V2', 'V3', 'V4', 'V5a', 'V6')
RETAIN_MIN, TOP_LOSS_X, COND_SHARE = 0.40, 1.5, 0.50      # eligibility rules 4, 5 and 3


def load_bank(bank):
    z = np.load(os.path.join(OUT, f'f0_bars_{bank}.npz'))
    d = np.load(os.path.join(OUT, 'f0_days.npz'))
    syms = banks()[bank][0]
    bars = {s: (z[f'{s}__ts'], z[f'{s}__x']) for s in syms}
    days = {k.split('__')[1]: d[k] for k in d.files if k.startswith(bank + '__')}
    return syms, bars, days


def trade_table(events, bank, cuts):
    """One row per trade: R, dates and the variables of its signal bar / previous closed day.
    V* is 1 favourable, 0 rest, NaN while the variable does not exist yet."""
    import pandas as pd
    import r57
    syms, bars, days = load_bank(bank)
    col = {s: j for j, s in enumerate(syms)}
    c = cuts['tercile_cuts_u50_alt_bars']
    rows = []
    for e in events:
        sig = e['opened'] - (H4 if e['sleeve'] == 'R3' else 0)
        ts, x = bars[e['sym']]
        k = int(np.searchsorted(ts, sig))
        assert k < len(ts) and ts[k] == sig, (e, sig)
        relvol, taker, sig30, _, _, rnd, _, fpct = x[k]
        r = r57.row_for(days['days'], sig)
        j = col[e['sym']]
        pe, pr = days['persist'][r, j], days['p_rng'][r, j]
        f = lambda ok, v: float(ok) if np.isfinite(v) else np.nan
        rows.append({'sym': e['sym'], 'sleeve': e['sleeve'], 'opened': e['opened'], 'closed': e['closed'], 'R': e['R'],
                     'year': pd.Timestamp(e['opened'], unit='ms').strftime('%Y'),
                     'week': r57._week(e['opened']), 'cweek': r57._week(e['closed']), 'persist': pe,
                     'sig30_t': float(np.searchsorted(c['sigma30'], sig30)) if np.isfinite(sig30) else np.nan,
                     'V1': f(pe == 0, pe), 'V2': f(pr < cuts['p_range_cut'], pr),
                     'V3': f(relvol >= c['relvol'][1], relvol), 'V4': f(taker >= c['taker'][1], taker),
                     'V5a': f(fpct < FUND_SAT, fpct), 'V6': f(rnd >= ROUND_ATR, rnd)})
    return pd.DataFrame(rows)


def _d(R, g):
    return float(R[g].mean() - R[~g].mean()) if g.any() and (~g).any() else np.nan


def _cond(R, g, strata):
    """n-weighted mean of the within-stratum differences (strata holding both classes only)."""
    num = den = 0.0
    for s in np.unique(strata[np.isfinite(strata)]):
        m = strata == s
        if g[m].any() and (~g[m]).any():
            num += m.sum() * _d(R[m], g[m])
            den += m.sum()
    return num / den if den else np.nan


def _weekly_sharpe(df, keep):
    """Approximate basket Sharpe (declared in §2): weekly sum of R by closing week, annualised."""
    import pandas as pd
    wk = df['cweek'].values
    s = pd.Series(np.where(keep, df['R'].values, 0.0)).groupby(wk).sum().values
    return float(s.mean() / s.std() * math.sqrt(52)) if s.std() > 0 else np.nan


def sweep(df, names):
    """Per variable: D, D by year, D conditional on V1 and on sigma30 (weekly-block bootstrap CIs),
    retention, top-decile loss, the approximate weekly-R Sharpe and the §2 eligibility rule."""
    import r57
    R = df['R'].values
    vals = {v: (np.isfinite(df[v].values), df[v].values == 1) for v in names}
    pe, st = df['persist'].values, df['sig30_t'].values.astype(float)

    def stat(ix):
        out = []
        for v in names:
            ok, g = vals[v]
            m = ix[ok[ix]]
            out += [_d(R[m], g[m]), _cond(R[m], g[m], pe[m]) if v != 'V1' else np.nan, _cond(R[m], g[m], st[m])]
        return tuple(out)
    old = r57.N_BOOT
    r57.N_BOOT = N_BOOT
    try:
        bs = r57.block_boot(df['week'].values, stat, np.random.default_rng(SEED))
    finally:
        r57.N_BOOT = old
    yrs = df['year'].values
    res = {}
    for i, v in enumerate(names):
        ok, g = vals[v]
        Rm, gm, ym = R[ok], g[ok], yrs[ok]
        b = bs[:, 3 * i:3 * i + 3]
        top = Rm >= np.quantile(Rm, 0.9)
        retain = float(gm.mean())
        e = {'n': int(ok.sum()), 'n_fav': int(gm.sum()), 'mean_R_fav': float(Rm[gm].mean()), 'mean_R_rest': float(Rm[~gm].mean()),
             'win_fav': float((Rm[gm] > 0).mean()), 'win_rest': float((Rm[~gm] > 0).mean()),
             'D': _d(Rm, gm), 'D_ci90': np.nanpercentile(b[:, 0], [5, 95]).tolist(), 'D_se': float(np.nanstd(b[:, 0])),
             'D_by_year': {y: _d(Rm[ym == y], gm[ym == y]) for y in YEARS},
             'D_cond_V1': None if v == 'V1' else _cond(Rm, gm, pe[ok]),
             'D_cond_V1_ci90': None if v == 'V1' else np.nanpercentile(b[:, 1], [5, 95]).tolist(),
             'D_cond_V1_se': None if v == 'V1' else float(np.nanstd(b[:, 1])),
             'D_cond_sigma30': _cond(Rm, gm, st[ok]), 'D_cond_sigma30_ci90': np.nanpercentile(b[:, 2], [5, 95]).tolist(),
             'retained': retain, 'top_decile_lost': float((top & ~gm).sum() / top.sum()),
             'weekly_sharpe_fav': _weekly_sharpe(df[ok], gm),
             'weekly_sharpe_all_valid': _weekly_sharpe(df[ok], np.ones(len(gm), bool))}
        rule = {'1_D_pos_ci90': bool(e['D'] > 0 and e['D_ci90'][0] > 0),
                '2_years_pos_ge_3': sum(1 for x in e['D_by_year'].values() if x == x and x > 0) >= 3,
                '3_cond_V1': True if v == 'V1' else bool(e['D_cond_V1'] > 0 and e['D_cond_V1'] >= COND_SHARE * e['D']),
                '4_retained_ge_40': retain >= RETAIN_MIN,
                '5_top_decile': e['top_decile_lost'] <= TOP_LOSS_X * (1 - retain)}
        e['rule'], e['eligible'] = rule, bool(all(rule.values()))
        e['score'] = e['D'] / e['D_se'] if v == 'V1' else e['D_cond_V1'] / e['D_cond_V1_se']
        res[v] = e
    return res


def c6_btc_eth_v7():
    """Descriptive (b): frozen C6 on P-r55's BTC/ETH (common window, bars cut at 2024-12-31), R per
    trade by V1, V3 and V7 (DVOL - RV below the median), trades opened 2021-03-25..2024."""
    import r50_engines as en
    import r50_f1b as fb
    import r57
    import r56_eval as ev
    from r50_harness import T, V
    cuts = json.load(open(os.path.join(OUT, 'f0_cuts.json')))
    syms = [str(s) for s in np.load(os.path.join(ev.OUT, 'panel.npz'))['syms']]
    L = np.load(os.path.join(ev.OUT, 'labels.npz'))
    dv = np.load(os.path.join(OUT, 'f0_dvol.npz'))
    out = {}
    for name in ('BTC', 'ETH'):
        d = fb.load_both(name, 'common')
        h4 = d['h4'][d['h4'][:, T] + H4 <= CUT_MS]
        close = h4[:, T] + H4
        rows = []
        for retest in (False, True):
            ts, eq, acct = en.simulate(h4, d['start_ms'], fb.r2_r3_decider(h4, retest), name, d['funding'], fb.H4_MS)
            for t in acct.trades:
                if t['opened'] < ms('2021-03-25') or t['opened'] >= CUT_MS:
                    continue
                k = int(np.searchsorted(ts, t['opened'], side='left'))
                Rt = t['pnl'] / (0.01 * (eq[k - 1] if k > 0 else en.BALANCE))
                i = int(np.searchsorted(close, t['opened'] - (H4 if retest else 0)))
                ref = np.median(h4[max(0, i - RELVOL_BARS):i, V]) if i >= RELVOL_MIN else np.nan
                r = r57.row_for(dv['days'], int(close[i]))
                rows.append((Rt, L['persist_vol'][r, syms.index(f'{name}USDT')], h4[i, V] / ref, dv[name][r]))
        A = np.array(rows, dtype=float)
        part = {'V1_compression': (A[:, 1] == 0, np.isfinite(A[:, 1])),
                'V3_relvol_top': (A[:, 2] >= cuts['tercile_cuts_u50_alt_bars']['relvol'][1], np.isfinite(A[:, 2])),
                'V7_dvol_minus_rv_low': (A[:, 3] < cuts['dvol_minus_rv_median'], np.isfinite(A[:, 3]))}
        out[name] = {'n': int(len(A)), 'mean_R': float(A[:, 0].mean())}
        for k, (g, ok) in part.items():
            out[name][k] = {'n_valid': int(ok.sum()), 'n_fav': int((g & ok).sum()),
                            'mean_R_fav': float(A[g & ok, 0].mean()) if (g & ok).any() else None,
                            'mean_R_rest': float(A[~g & ok, 0].mean()) if (~g & ok).any() else None}
    return out


def diag():
    import warnings
    warnings.simplefilter('ignore')
    cuts = json.load(open(os.path.join(OUT, 'f0_cuts.json')))
    events, dropped = load_events()
    events = [e for e in events if e['opened'] >= SIM_FROM]
    df = trade_table(events, 'u50', cuts)
    res = {'protocol': 'PROTOCOL_R58.md §2', 'n_added': 0, 'n_tematica': {'before': 12, 'added': 7, 'after': 19},
           'n_trades': int(len(df)), 'dropped_2025': dropped, 'mean_R_all': float(df['R'].mean()),
           'variables': sweep(df, CANDIDATES)}
    el = sorted((v for v in CANDIDATES if res['variables'][v]['eligible']), key=lambda v: -res['variables'][v]['score'])
    res['eligible'], res['selected'] = el, el[:3]
    res['b_btc_eth'] = c6_btc_eth_v7()
    df.to_csv(os.path.join(OUT, 'f1_trades_u50.csv'), index=False)
    json.dump(res, open(os.path.join(OUT, 'f1_diag.json'), 'w'), indent=1, default=float)
    for v in CANDIDATES:
        e = res['variables'][v]
        log(f"{v} n={e['n']} fav={e['n_fav']} D={e['D']:+.3f} ci={np.round(e['D_ci90'], 3)} condV1={e['D_cond_V1']} "
            f"condS={e['D_cond_sigma30']:+.3f} ret={e['retained']:.2f} top={e['top_decile_lost']:.2f} rule={e['rule']}")
    log(f"eligible {el} selected {res['selected']}")
    log(json.dumps(res['b_btc_eth'], default=float))


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = {'oi_probe': oi_probe, 'n3_select': n3_select, 'n3_download': n3_download, 'n3_panel': n3_panel,
          'states': states, 'selftest': selftest, 'diag': diag}.get(cmd)
    if fn is None:
        print(__doc__)
        return 1
    os.makedirs(OUT, exist_ok=True)
    fn()
    return 0


if __name__ == '__main__':
    sys.exit(main())
