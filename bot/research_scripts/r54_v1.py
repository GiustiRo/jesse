"""r54 V1: frozen C6 (r50 R2 + R3, 5caf4a53) on the 48 U50 alts (PROTOCOL_R54.md V1).

No rule changes: `r50_f1b.r2_r3_decider` runs on 4h bars aggregated from data.binance.vision 1h
klines, with r50 costs and each symbol's real funding (mark approximated by the 1h close of the
settlement hour, declared). Metrics 2021-01-01..2024-12-31; 2025 is sealed. It also writes every
R2/R3 trade as an event for M1 (meta-labeling).

    python research_scripts/r54_v1.py run

writes data/r52/v1.json and data/r52/v1_events.json.
"""
import json
import math
import os
import sys
from datetime import datetime, timezone

import numpy as np

import r50_engines as en
import r50_f1b as fb
import r50_f1c as fc
from r50_harness import T, O, C, H, L, V, DAY_MS

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'r52')
H4 = 4 * 3_600_000
SIM_FROM = 1602720000000          # 2020-10-15, P1's common-window start
MEASURE = ('2021-01-01', '2025-01-01')
WARM_BARS = 100                   # r2_r3_decider needs 100 bars before its first setup


def h4_bars(sym):
    a = np.load(os.path.join(DATA, f'{sym}_1h.npy'))
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
    return out, a


def funding_cursor(sym, h1, bars0):
    f = np.load(os.path.join(DATA, f'{sym}_funding.npy'))
    if not len(f):
        return None
    eff = (f[:, 0].astype(np.int64) // 60_000) * 60_000
    hour = eff // 3_600_000 * 3_600_000
    idx = np.searchsorted(h1[:, 0], hour, side='right') - 1
    mark = np.where(idx >= 0, h1[np.clip(idx, 0, None), 4], np.nan)
    ok = np.isfinite(mark)
    eff, mark, rate = eff[ok], mark[ok], f[ok, 1]
    return [eff, mark, rate, int(np.searchsorted(eff, bars0, side='left'))]


def simulate(bars, start_ms, decide, fcur):
    """r50_engines.simulate with an explicit funding cursor (vision funding)."""
    acct = en.Account(en.BALANCE, en.TAKER, en.LEVERAGE)
    k0 = int(np.searchsorted(bars[:, T], start_ms, side='left'))
    ts_out, eq_out = [], []
    for i in range(k0, len(bars)):
        close_ts = int(bars[i, T]) + H4
        en._pay(acct, fcur, close_ts)
        decide(i, acct, close_ts)
        ts_out.append(close_ts)
        eq_out.append(acct.equity(bars[i, C]))
    return np.array(ts_out, dtype=np.int64), np.array(eq_out), acct


def trim(cv, end):
    d, v = cv
    k = int(np.searchsorted(d, en.hz._ms(end)))
    return d[:k], v[:k]


def run():
    uni = [u['symbol'] for u in json.load(open(os.path.join(DATA, 'universe50.json')))]
    alts = [s for s in uni if s not in ('BTCUSDT', 'ETHUSDT')]
    res, curves, events = {'alts': {}}, {}, []
    for sym in alts:
        bars, h1 = h4_bars(sym)
        start = max(SIM_FROM, int(bars[min(WARM_BARS, len(bars) - 1), T]))
        if start >= en.hz._ms(MEASURE[1]):
            continue
        frm = datetime.fromtimestamp(start / 1000, tz=timezone.utc).date().isoformat()
        sleeves = []
        for retest in (False, True):
            dec = fb.r2_r3_decider(bars, retest)
            fcur = funding_cursor(sym, h1, int(bars[0, T]))
            ts, eq, acct = simulate(bars, start, dec, fcur)
            cv = en.calendar(ts, eq, frm, '2026-01-01')
            sleeves.append(cv)
            # Events for M1: R = trade PnL over the 1% risk budget at entry.
            for t in acct.trades:
                k = int(np.searchsorted(ts, t['opened'], side='left'))
                eq0 = eq[k - 1] if k > 0 else en.BALANCE
                events.append({'sym': sym, 'sleeve': 'R3' if retest else 'R2', 'opened': int(t['opened']),
                               'closed': int(t['closed']), 'pnl': float(t['pnl']), 'R': float(t['pnl'] / (0.01 * eq0))})
        c6 = fc.mean_curve(sleeves)
        curves[sym] = c6
        d, v = trim(c6, MEASURE[1])
        m = en.metrics(d, v, [], max(MEASURE[0], frm))
        if m:
            m['collapse'] = m['sharpe'] < -0.5 or m['max_dd'] < -0.30
            res['alts'][sym] = m
    meas = {s: trim(cv, MEASURE[1]) for s, cv in curves.items()}
    b = fb.basket(meas, list(meas))
    bm = en.metrics(b[0], b[1], [], MEASURE[0])
    years = (len(b[1]) - int(np.searchsorted(b[0], en.hz._ms(MEASURE[0])))) / 365
    t_stat = bm['sharpe'] * math.sqrt(years)
    n = len(res['alts'])
    pos = sum(1 for m in res['alts'].values() if m['sharpe'] > 0)
    col = sum(1 for m in res['alts'].values() if m['collapse'])
    res['basket'] = dict(bm, t_stat=t_stat)
    res['summary'] = {'alts': n, 'positive': pos, 'collapses': col,
                      'gates': {'majority_pos': pos > n / 2, 'collapses_le_10pct': col <= 0.10 * n,
                                'basket_sharpe_pos': bm['sharpe'] > 0, 'basket_t_ge_1_28': t_stat >= 1.28}}
    res['summary']['pass'] = all(res['summary']['gates'].values())
    res['sol_xrp_bnb'] = {s: res['alts'].get(s) for s in ('SOLUSDT', 'XRPUSDT', 'BNBUSDT')}
    json.dump(res, open(os.path.join(DATA, 'v1.json'), 'w'), indent=1, default=float)
    json.dump(events, open(os.path.join(DATA, 'v1_events.json'), 'w'))
    np.save(os.path.join(DATA, 'v1_curves.npy'), curves, allow_pickle=True)
    print(json.dumps(res['summary'], default=float))
    print('basket', json.dumps({k: res['basket'][k] for k in ('from', 'to', 'sharpe', 'cagr', 'max_dd', 'quarters_pos', 't_stat')}, default=float))
    for s in ('SOLUSDT', 'XRPUSDT', 'BNBUSDT'):
        m = res['alts'].get(s)
        print(s, m and {k: round(m[k], 3) for k in ('sharpe', 'cagr', 'max_dd')})
    srt = sorted(res['alts'].items(), key=lambda x: x[1]['sharpe'])
    print('worst', [(s, round(m['sharpe'], 2), round(m['max_dd'], 2)) for s, m in srt[:5]])
    print('best', [(s, round(m['sharpe'], 2)) for s, m in srt[-5:]])
    print('events', len(events))


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
