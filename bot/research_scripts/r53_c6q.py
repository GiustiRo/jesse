"""r53 F2: QOI as an entry filter on C6 (C6q).

PROTOCOL_R53.md section "Ensayo F2: QOI como filtro de C6"
(strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261026-r53/), fixed before this
file was written:

* C6q = C6 (R2 + R3 on BTC/ETH 4h, r50 code frozen) that only opens when z(QOI) > 0 on the 4h
  signal bar, with the same z as r52 F2 (r52_q.bars_4h, stamped at bar close).
* It replaces C6 inside P1 under the r51 inclusion rule, on P1's windows cut at 2024-12-31:
  pass if (d_sharpe_long >= 0.05 or (d_q_pos_long >= 1 and d_sharpe_long >= 0)) and
  d_sharpe_common >= -0.05.
* QOI exists only on perpetual data (2020+), so the 2018-09+ lens uses unfiltered C6 before
  2020-10-15, as declared in the protocol.

2025 is sealed and 2026 reserved: every metric below stops at 2024-12-31. The full P1q
component curves (through 2025) are saved unmeasured for a later sealed check.

    python research_scripts/r53_c6q.py run

writes research_scripts/data/r52/c6q.json and data/r52/c6q_components.npy.
"""
import json
import os
import sys

import numpy as np
import jesse.models  # noqa: F401 - must load before candle_service (circular import otherwise)
import jesse.indicators as ta

import r50_harness as hz
import r50_engines as en
import r50_f1b as fb
import r50_f1c as fc
import r50_f2 as f2
import r51_lib as lib
import r52_q as q
from r50_harness import T, O, C, H, L, DAY_MS
from r50_engines import COMMON, MEASURE_FROM, simulate, calendar, daily_returns

OUT = os.path.join(lib.HERE, 'data', 'r52')
N_DECLARED = 124
SEAL = '2024-12-31'                      # last measured day (2025 sealed, 2026 reserved)
SEAL_MS = hz._ms(SEAL)
SEAL_END_MS = SEAL_MS + DAY_MS
SPLICE = '2020-10-15'                    # perpetual C6q starts here (r50 common-window start)
SPLICE_MS = hz._ms(SPLICE)
QSYM = {'BTC': 'BTCUSDT', 'ETH': 'ETHUSDT'}
DS_MIN, DS_COMMON_MAX_DROP = 0.05, 0.05  # r51 inclusion rule
KEYS = ('from', 'to', 'cagr', 'max_dd', 'sharpe', 'vol_realized', 'pf_trades', 'months_pos', 'quarters_pos',
        'q_pos_count', 'n_quarters', 'median_month', 'without_best2_months', 'dsr', 'by_year')


# ----------------------------------------------------------------------------------------------
# Filter and decider
# ----------------------------------------------------------------------------------------------
def qoi_allow(h4, name):
    """Boolean per h4 bar (stamped at OPEN): z(QOI) of that bar, read at its close, is > 0.

    r52_q.bars_4h stamps each bar at its close, so the bar opening at t matches index t + 4h.
    A missing or NaN z (no QOI data, z warmup) blocks the entry."""
    df, _ = q.bars_4h(QSYM[name])
    zmap = dict(zip((df.index.asi8 // 10**6 - q.H4_MS).tolist(), df['z'].values.tolist()))
    z = np.array([zmap.get(int(t), np.nan) for t in h4[:, T]])
    return np.isfinite(z) & (z > 0), z


def r2_r3_decider_q(bars, retest, allow, max_stop=0.055, log=None):
    """fb.r2_r3_decider copied verbatim, with one extra gate: a new entry signal (R2 market entry,
    R3 limit placement) needs allow[i]. Exits and the fill of an already placed R3 limit are
    untouched. `log` (optional list) collects the signal-bar index of every filled entry; it does
    not affect the logic. The reproduction test checks this copy against the frozen original."""
    c, h, l, o = bars[:, C], bars[:, H], bars[:, L], bars[:, O]
    e20 = ta.ema(bars, period=20, sequential=True)
    e80 = ta.ema(bars, period=80, sequential=True)
    atr = ta.atr(bars, period=14, sequential=True)
    adx = ta.adx(bars, period=14, sequential=True)
    rsi = ta.rsi(bars, period=14, sequential=True)
    hh26 = en.prior_max(h, 26)
    st = {'limit': None}

    def setup(i):
        return (i >= 100 and np.isfinite([e20[i], e80[i], e80[i - 4], atr[i], adx[i], rsi[i], hh26[i]]).all()
                and atr[i] > 0 and c[i] > e80[i] and e20[i] > e80[i] > e80[i - 4] and adx[i] >= 26
                and 52 <= rsi[i] <= 76 and h[i] - l[i] <= 3 * atr[i])

    def open_pos(acct, i, price, dist, ts, fee, sig):
        q_ = fb.risk_qty(acct, price, dist)
        if q_ > 0:
            fb._trade(acct, q_, price, ts, fee)
            st.update(entry=price, r=dist, stop=price - dist, best_close=price, extreme=h[i], hi=h[i],
                      be_on_extreme=not retest)
            if log is not None:
                log.append(sig)

    def decide(i, acct, ts):
        if acct.is_open:
            if fb.stop_exit(acct, st, o, l, i, ts):
                return
            st['hi'] = h[i]
            fb.chandelier(st, c[i], atr[i], 4.2, 2.25 if retest else 1.75, fb.TAKER, True)
            return
        if retest and st['limit'] is not None:
            px, dist = st['limit']
            st['limit'] = None
            if l[i] < px:
                open_pos(acct, i, px, dist, ts, fb.MAKER, i - 1)   # limit was placed on bar i - 1
                if acct.is_open and l[i] <= st['stop']:  # same-bar stop after the fill
                    fb._trade(acct, -acct.qty, st['stop'] * (1 - fb.STOP_SLIP), ts, fb.TAKER)
                return
        if not (setup(i) and allow[i]):   # r53 F2: the only change
            return
        if retest:
            entry = hh26[i]
            if entry < c[i] <= entry + atr[i] and 0 < 2 * atr[i] < entry:
                st['limit'] = (entry, 2 * atr[i])
        elif c[i] > hh26[i]:
            frac = max(2 * atr[i] / c[i], 0.008)
            if max_stop is None or frac <= max_stop:
                open_pos(acct, i, c[i], frac * c[i], ts, fb.TAKER, i)
    return decide


def run_c6(name, d, allow, frm):
    """Both sleeves on one coin: C6 curve (mean of R2/R3 calendar curves), trades, entry logs."""
    curves, trades, logs = [], [], {}
    for retest in (False, True):
        log = []
        ts, eq, acct = simulate(d['h4'], d['start_ms'], r2_r3_decider_q(d['h4'], retest, allow, log=log), name,
                                d['funding'], fb.H4_MS)
        curves.append(calendar(ts, eq, frm, COMMON[1]))
        trades += acct.trades
        logs['R3' if retest else 'R2'] = log
    return fc.mean_curve(curves), trades, logs


# ----------------------------------------------------------------------------------------------
# Helpers (every measurement goes through cut())
# ----------------------------------------------------------------------------------------------
def cut(cv, from_ms=None):
    days, vals = cv
    keep = days <= SEAL_MS
    if from_ms is not None:
        keep &= days >= from_ms - DAY_MS
    return days[keep], vals[keep]


def sealed_trades(trades, from_ms=0):
    return [t for t in trades if from_ms <= t['closed'] < SEAL_END_MS]


def splice(spot, perp):
    """Spot C6 daily returns through day SPLICE, perpetual C6q returns afterwards.

    The perpetual curve's first day (SPLICE) is its 10k baseline, so its first return is the
    next day; the spot return of day SPLICE is kept. The spot position open at the splice (if
    any) is not carried over: the perpetual run starts flat, as in the r50 common window."""
    rs, rp = daily_returns(*spot), daily_returns(*perp)
    days = sorted([d for d in rs if d <= SPLICE_MS] + [d for d in rp if d > SPLICE_MS])
    r = np.array([rs[d] if d <= SPLICE_MS else rp[d] for d in days])
    return np.r_[days[0] - DAY_MS, days], en.BALANCE * np.r_[1.0, np.cumprod(1 + r)]


def evaluate(comps, trades, start):
    cutc = {k: cut(v, start) for k, v in comps.items()}
    days, vals, contrib, _ = lib.portfolio_attr(cutc, list(cutc))
    m = f2.r9(days, vals, [t['pnl'] for t in sealed_trades(trades, start)])
    m['q_pos_count'] = int(round(m['quarters_pos'] * m['n_quarters']))
    out = {k: m[k] for k in KEYS}
    out['contrib_sum'] = {k: float(v.sum()) for k, v in contrib.items()}
    return out


def compare(p1, p1q, tr_p1, tr_p1q):
    """P1 vs P1q in both windows on the same days (later component start + 1 day -> SEAL)."""
    out = {}
    for w in ('long', 'common'):
        start = max(int(cv[0][0]) for cv in list(p1[w].values()) + list(p1q[w].values())) + DAY_MS
        out[w] = {'from': lib._date(start), 'P1': evaluate(p1[w], tr_p1[w], start),
                  'P1q': evaluate(p1q[w], tr_p1q[w], start)}
    dl = out['long']['P1q']['sharpe'] - out['long']['P1']['sharpe']
    dq = out['long']['P1q']['q_pos_count'] - out['long']['P1']['q_pos_count']
    dc = out['common']['P1q']['sharpe'] - out['common']['P1']['sharpe']
    ok = (dl >= DS_MIN or (dq >= 1 and dl >= 0)) and dc >= -DS_COMMON_MAX_DROP
    return {'pass': bool(ok), 'd_sharpe_long': dl, 'd_q_pos_long': dq, 'd_sharpe_common': dc, 'detail': out}


def standalone(cv, trades):
    """Metrics from 2021-01-01 to SEAL on the perpetual curve."""
    m = en.metrics(*cut(cv), sealed_trades(trades), MEASURE_FROM)
    return {k: m[k] for k in ('from', 'to', 'sharpe', 'cagr', 'max_dd', 'quarters_pos', 'trades', 'trades_per_year')}


def entries_in_window(h4, sigs):
    close = h4[np.array(sigs, dtype=int), T] + fb.H4_MS if sigs else np.array([])
    m0 = hz._ms(MEASURE_FROM)
    return [s for s, t in zip(sigs, close) if m0 <= t <= SEAL_END_MS]


# ----------------------------------------------------------------------------------------------
# Reproduction test
# ----------------------------------------------------------------------------------------------
def reproduction_test(d):
    """With an always-true filter the copy must reproduce fb.r2_r3_decider exactly on BTC perp,
    2021-01-01 to 2024-12-31 (bars after the seal are dropped before simulating)."""
    h4 = d['h4'][d['h4'][:, T] + fb.H4_MS <= SEAL_END_MS]
    start = hz._ms(MEASURE_FROM)
    res = {}
    for retest in (False, True):
        a = simulate(h4, start, fb.r2_r3_decider(h4, retest), 'BTC', d['funding'], fb.H4_MS)
        b = simulate(h4, start, r2_r3_decider_q(h4, retest, np.ones(len(h4), bool)), 'BTC', d['funding'], fb.H4_MS)
        same = (np.array_equal(a[0], b[0]) and np.array_equal(a[1], b[1]) and a[2].trades == b[2].trades
                and a[2].order_log == b[2].order_log)
        res['R3' if retest else 'R2'] = {'identical': bool(same), 'trades': len(a[2].trades), 'orders': len(a[2].order_log)}
    assert all(v['identical'] for v in res.values()), res
    return res


# ----------------------------------------------------------------------------------------------
def run():
    f2.N_DECLARED = N_DECLARED
    res = {'protocol': 'RESEARCH_HUB/revisions/20261026-r53/PROTOCOL_R53.md#ensayo-f2', 'n_declared': N_DECLARED,
           'measured_through': SEAL,
           'long_window_choice': (f'2018-09+ lens: C6q per coin = unfiltered spot C6 daily returns through {SPLICE} '
                                  f'spliced with perpetual C6q returns from the next day; the perpetual run starts '
                                  f'flat on {SPLICE} (no position carried); basket over coins as fb.basket. '
                                  f'Common window: perpetual C6q directly.')}
    sl = {w: lib.p1_sleeves(w) for w in ('common', 'long')}   # r1, r1_tr, c6, c6_tr, data
    perp = sl['common'][4]
    res['reproduction_test'] = reproduction_test(perp['BTC'])

    # Perpetual C6 (unfiltered, check vs r51) and C6q per coin.
    c6p, c6p_tr, c6q, c6q_tr, removed, cover = {}, {}, {}, {}, {}, {}
    for name in fc.CRYPTO:
        d = perp[name]
        frm = lib._date(d['start_ms'])
        allow, z = qoi_allow(d['h4'], name)
        c6p[name], c6p_tr[name], logs0 = run_c6(name, d, np.ones(len(d['h4']), bool), frm)
        c6q[name], c6q_tr[name], logsq = run_c6(name, d, allow, frm)
        ref = sl['common'][2][name]
        assert np.array_equal(ref[0], c6p[name][0]) and np.allclose(ref[1], c6p[name][1], rtol=0, atol=1e-9), name
        mw = (d['h4'][:, T] + fb.H4_MS >= hz._ms(MEASURE_FROM)) & (d['h4'][:, T] + fb.H4_MS <= SEAL_END_MS)
        cover[name] = {'bars': int(mw.sum()), 'z_finite': float(np.isfinite(z[mw]).mean()), 'z_pos': float(allow[mw].mean())}
        removed[name] = {}
        for s in ('R2', 'R3'):
            e0 = entries_in_window(d['h4'], logs0[s])
            eq_ = entries_in_window(d['h4'], logsq[s])
            blocked = sum(1 for i in e0 if not allow[i])
            removed[name][s] = {'c6_entries': len(e0), 'c6q_entries': len(eq_), 'c6_entries_blocked': blocked,
                                'share_blocked': blocked / len(e0) if e0 else None}
    tot0 = sum(v[s]['c6_entries'] for v in removed.values() for s in v)
    totb = sum(v[s]['c6_entries_blocked'] for v in removed.values() for s in v)
    totq = sum(v[s]['c6q_entries'] for v in removed.values() for s in v)
    removed['total'] = {'c6_entries': tot0, 'c6q_entries': totq, 'c6_entries_blocked': totb,
                        'share_blocked': totb / tot0 if tot0 else None, 'entry_count_drop': 1 - totq / tot0 if tot0 else None}
    res['qoi_coverage_2021_2024'] = cover
    res['entries_removed_2021_2024'] = removed

    # Standalone C6 vs C6q (perpetual, 2021-01-01 .. 2024-12-31).
    sa = {}
    for name in fc.CRYPTO:
        sa[name] = {'C6': standalone(c6p[name], c6p_tr[name]), 'C6q': standalone(c6q[name], c6q_tr[name])}
    sa['basket'] = {'C6': standalone(fb.basket(c6p, list(c6p)), sum(c6p_tr.values(), [])),
                    'C6q': standalone(fb.basket(c6q, list(c6q)), sum(c6q_tr.values(), []))}
    res['standalone'] = sa

    # P1 vs P1q.
    p1, p1q, tr_p1, tr_p1q, extra = {}, {}, {}, {}, {}
    for w in ('common', 'long'):
        r1, _, c6, _, data = sl[w]
        r1_trades = []
        for name in r1:   # R1 trades with timestamps (r51_lib keeps only PnLs); same r50 run
            ts, eq, acct = fb.r1_run(name, data[name])
            r1_trades += acct.trades
        p1[w] = {'R1': fb.basket(r1, list(r1)), 'C6': fb.basket(c6, list(c6))}
        if w == 'common':
            q_coin, q_tr = c6q, sum(c6q_tr.values(), [])
            c6_trades = sum(c6p_tr.values(), [])
        else:
            spot_tr = {}
            for name in fc.CRYPTO:
                d = data[name]
                _, spot_tr[name], _ = run_c6(name, d, np.ones(len(d['h4']), bool), lib._date(d['start_ms']))
            q_coin = {n: splice(c6[n], c6q[n]) for n in c6}
            # Diagnostic only: same splice without the filter, isolating QOI from the spot->perp switch.
            extra['C6_spliced_unfiltered'] = fb.basket({n: splice(c6[n], c6p[n]) for n in c6}, list(c6))
            pre = [t for n in spot_tr for t in spot_tr[n] if t['closed'] < SPLICE_MS]
            q_tr = pre + [t for n in c6q_tr for t in c6q_tr[n] if t['closed'] >= SPLICE_MS]
            u_tr = pre + [t for n in c6p_tr for t in c6p_tr[n] if t['closed'] >= SPLICE_MS]
            c6_trades = sum(spot_tr.values(), [])
        p1q[w] = {'R1': p1[w]['R1'], 'C6q': fb.basket(q_coin, list(q_coin))}
        tr_p1[w] = r1_trades + c6_trades
        tr_p1q[w] = r1_trades + q_tr
        if w == 'long':
            extra['trades'] = r1_trades + u_tr
    res['inclusion'] = compare(p1, p1q, tr_p1, tr_p1q)
    # Diagnostic: P1 with the unfiltered splice vs P1q on the long lens (filter effect alone).
    pd_ = {'R1': p1['long']['R1'], 'C6s': extra['C6_spliced_unfiltered']}
    start = max(int(cv[0][0]) for cv in list(p1['long'].values()) + list(p1q['long'].values())) + DAY_MS
    res['diag_long_spliced_unfiltered'] = {'from': lib._date(start),
                                           'P1_spliced': evaluate(pd_, extra['trades'], start),
                                           'note': 'not part of the rule; P1q minus this isolates the QOI filter'}
    res['diag_long_spliced_unfiltered']['d_sharpe_filter_only'] = (
        res['inclusion']['detail']['long']['P1q']['sharpe'] - res['diag_long_spliced_unfiltered']['P1_spliced']['sharpe'])

    np.save(os.path.join(OUT, 'c6q_components.npy'),
            {'P1q': p1q, 'P1': p1, 'C6q_coin_perp': c6q, 'C6_coin_perp': c6p,
             'note': 'full curves through 2025, unmeasured; days at 00:00 UTC, value at day end'}, allow_pickle=True)
    path = os.path.join(OUT, 'c6q.json')
    with open(path, 'w') as fh:
        json.dump(res, fh, indent=2, default=float)
    inc = res['inclusion']
    print(json.dumps({'reproduction_test': res['reproduction_test'],
                      'inclusion': {k: inc[k] for k in ('pass', 'd_sharpe_long', 'd_q_pos_long', 'd_sharpe_common')},
                      'P1_vs_P1q': {w: {k: {x: inc['detail'][w][k][x] for x in ('from', 'to', 'cagr', 'max_dd', 'sharpe', 'q_pos_count', 'n_quarters')}
                                        for k in ('P1', 'P1q')} for w in inc['detail']},
                      'diag_filter_only_long': res['diag_long_spliced_unfiltered']['d_sharpe_filter_only'],
                      'standalone': sa, 'removed': removed['total'], 'coverage': cover}, indent=1, default=float))
    print(path)


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
