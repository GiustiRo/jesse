"""r51 F3-F5: run the preregistered trials and their diversifier gates.

PROTOCOL_R51.md (8ac56348). Trials: A1-A5 (F3), B1-B3 (F4), T1-T2 (F5). Each trial is one entry
in N whatever its asset count. Gates (protocol F6), all required for a diversifier:
1. basket Sharpe >= 0.3 in the decision lens;
2. PnL > 0 summed over the trial's bear windows (protocol section 1) inside the decision lens;
3. no veto in the long lens (Sharpe < 0, or DD worse than 1.5x the decision DD);
4. daily correlation with P1 <= 0.2 (decision lens, P1 long window);
5. discrete-trade sleeves (A3, A4, B1): >= 30 trades and top-5 < 60% of the PnL.

Implementation choices fixed before results (declared in the F3 report):
* multi-asset B3 uses the union of all core bear windows for gate 2;
* crypto daily sleeves in the 2021-25 lens use spot bars plus the perpetual's real funding
  (the perpetual has no 252-day history in 2020); B1 trades the 4h perpetual there;
* the bond's decision lens starts when its 252-day lookback exists (~2019-03).

    python research_scripts/r51_explore.py run A|B|T

writes research_scripts/data/r51/explore_<block>.json.
"""
import json
import os
import sys

import numpy as np

import r50_harness as hz
import r50_engines as en
import r50_f1b as fb
import r51_lib as lib
import r51_sleeves as sv
from r50_harness import T, C, DAY_MS
from r50_engines import simulate, calendar, daily_returns

N_BEFORE = 98
BLOCKS = {'A': ['A1', 'A2', 'A3', 'A4', 'A5'], 'B': ['B1', 'B2', 'B3'], 'T': ['T1', 'T2']}
ASSETS_OF = {'A1': ['WTI', 'GAS', 'BOND'], 'A2': ['BOND'], 'A3': ['WTI'], 'A4': ['BOND'], 'A5': ['WTI'],
             'B1': ['BTC', 'ETH'], 'B2': ['SPX', 'XAU', 'BTC'], 'B3': ['B3'],
             'T1': list(lib.FAMILY), 'T2': list(lib.FAMILY)}
DISCRETE = ('A3', 'A4', 'B1')
BEAR = {
    'BOND': [('2021-01-01', '2023-10-31')],
    'WTI': [('2018-10-01', '2018-12-31'), ('2022-06-01', '2023-05-31')],
    'GAS': [('2022-08-01', '2024-03-31')],
    'BTC': [('2018-01-01', '2018-12-31'), ('2021-11-01', '2022-12-31')],
    'ETH': [('2018-01-01', '2018-12-31'), ('2021-11-01', '2022-12-31')],
    'SPX': [('2018-10-01', '2018-12-31'), ('2020-02-01', '2020-03-31'), ('2022-01-01', '2022-10-31')],
    'XAU': [('2022-03-01', '2022-10-31')],
}
BEAR['B3'] = sorted({w for v in BEAR.values() for w in v})
C21_SIM_FROM = '2020-10-15'   # same simulation start as P1's common window


def sim_start(name, lens, bars):
    if lens == 'c21':
        return hz._ms(C21_SIM_FROM)
    first_full = int(bars[min(260, len(bars) - 1), T])
    if lens == 'veto':
        return first_full
    return max(hz._ms(sv.lens_from(name, lens)), first_full)


# B3 ranks the 7 core assets, so its lens starts are fixed by the protocol (decision from 2019-04,
# when the 7 have 252 days of history) and, for the veto, from 2013 (CFDs and TLT only).
B3_START = {'dec': '2019-04-01', 'c21': C21_SIM_FROM, 'veto': '2013-01-01'}


def daily_sleeve(trial, name, lens):
    """(calendar days, equity, trades) of one asset's sleeve in one lens."""
    if trial == 'B3':
        start = hz._ms(B3_START[lens])
        ts, eq = sv.b3_curve(lens, start)
        return calendar(ts, eq, lib._date(start), sv.END), [], start
    src = sv.lens_source(name, lens)
    bars = sv.daily(name, src)
    start = sim_start(name, lens, bars)
    fund = lens == 'c21' and name in sv.CRYPTO
    cfd = sv.is_cfd(name)
    if trial in ('A1', 'B2') or trial in ('T1', 'T2'):
        if trial == 'A1':
            x = sv.a1_x(bars, cfd)
        elif trial == 'B2':
            x = sv.b2_x(bars, cfd)
        else:
            x = sv.t_x(name, bars, attenuate=trial == 'T2')
        ts, eq, acct = simulate(bars, start, sv.continuous_decider(bars, x), name, fund)
    elif trial == 'A2':
        spx = sv.daily('SPX', 'cfd')
        ts, eq, acct = simulate(bars, start, sv.continuous_decider(bars, sv.a2_x(bars, spx)), name, fund)
    elif trial == 'A5':
        eur = sv.daily('EURUSD', 'eurusd')
        ts, eq, acct = simulate(bars, start, sv.continuous_decider(bars, sv.a5_x(bars, eur)), name, fund)
    elif trial == 'A4':
        ts, eq, acct = simulate(bars, start, sv.a4_decider(bars), name, fund)
    elif trial == 'A3':
        brent = sv.daily('BRENT', 'brent')
        ts, eq, trades = sv.a3_pair(brent, bars, start)
        return calendar(ts, eq, lib._date(start), sv.END), trades, start
    elif trial == 'B1':
        if lens == 'c21':
            ex, sym = sv.SOURCES[name]['perp']
        else:
            ex, sym = sv.SOURCES[name]['spot']
        m = hz._minutes(ex, sym, hz._ms('2017-01-01'), hz.RESERVED_FROM_MS)
        from jesse.services.candle_service import generate_completed_candles_from_observed_minutes
        h4 = generate_completed_candles_from_observed_minutes('4h', m, hz.RESERVED_FROM_MS)
        regime = sv.daily(name, 'spot')
        ts, eq, acct = simulate(h4, start, sv.b1_decider(h4, regime), name, fund, fb.H4_MS)
    else:
        raise ValueError(trial)
    last = bars[-1, C]
    trades = acct.trades + ([{'closed': int(ts[-1]), 'pnl': acct.upnl(last)}] if acct.is_open else [])
    return calendar(ts, eq, lib._date(start), sv.END), trades, start


def window_pnl(cv, windows, frm_ms):
    r = daily_returns(*cv)
    tot = 0.0
    for a, b in windows:
        lo, hi = max(hz._ms(a), frm_ms), hz._ms(b) + DAY_MS
        tot += sum(v for d, v in r.items() if lo <= d < hi)
    return tot


def evaluate(trial, p1_long_returns):
    names = ASSETS_OF[trial]
    out = {'trial': trial, 'assets': {}, 'basket': {}}
    curves = {lens: {} for lens in ('dec', 'c21', 'veto')}
    trades = {lens: [] for lens in curves}
    starts = {}
    for name in names:
        for lens in curves:
            cv, tr, start = daily_sleeve(trial, name, lens)
            curves[lens][name] = cv
            trades[lens] += tr
            starts[(name, lens)] = start
            m = en.metrics(cv[0], cv[1], tr, lib._date(start))
            out['assets'].setdefault(name, {})[lens] = m
    for lens in curves:
        b = fb.basket(curves[lens], list(curves[lens]))
        frm = min(starts[(n, lens)] for n in names)
        out['basket'][lens] = en.metrics(b[0], b[1], trades[lens], lib._date(frm))
        out['basket'][lens]['_curve'] = b
    dec = out['basket']['dec']
    veto = out['basket']['veto']
    # Gate 2: bear-window PnL of each asset's own sleeve inside the decision lens.
    g2 = sum(window_pnl(curves['dec'][n], BEAR[n], starts[(n, 'dec')]) for n in names)
    # Gate 4: correlation of the decision basket with P1 (long window) on common days.
    br = daily_returns(*dec['_curve'])
    days = sorted(set(br) & set(p1_long_returns))
    rho = float(np.corrcoef([br[d] for d in days], [p1_long_returns[d] for d in days])[0, 1]) if len(days) > 60 else None
    gates = {
        'g1_sharpe_ge_0_3': dec['sharpe'] >= 0.3,
        'g2_bear_pnl_pos': g2 > 0,
        'g3_no_veto': not (veto['sharpe'] < 0 or veto['max_dd'] < 1.5 * dec['max_dd']),
        'g4_rho_le_0_2': rho is not None and rho <= 0.2,
    }
    if trial in DISCRETE:
        gates['g5_trades_top5'] = dec['trades'] >= 30 and dec['top5_share'] is not None and dec['top5_share'] < 0.6
    out['gates'] = {k: bool(v) for k, v in gates.items()}
    out['pass'] = all(out['gates'].values())
    out['bear_pnl_dec'] = g2
    out['rho_p1'] = rho
    return out


def p1_long_returns():
    comps, trades, _ = lib.p1_components('long')
    days, vals, _, _ = lib.portfolio_attr(comps, ['R1', 'C6'])
    return daily_returns(np.asarray(days), np.asarray(vals))


def main():
    if len(sys.argv) < 3 or sys.argv[1] != 'run' or sys.argv[2] not in BLOCKS:
        print(__doc__)
        return 1
    block = sys.argv[2]
    p1r = p1_long_returns()
    res = {'protocol': 'RESEARCH_HUB/revisions/20261025-r51/PROTOCOL_R51.md', 'block': block,
           'n_before': N_BEFORE, 'trials': {}}
    for trial in BLOCKS[block]:
        r = evaluate(trial, p1r)
        res['trials'][trial] = r
        d, v, c21 = r['basket']['dec'], r['basket']['veto'], r['basket']['c21']
        print(f"{trial}: dec Sharpe {d['sharpe']:.2f} CAGR {d['cagr']:.3f} DD {d['max_dd']:.3f} Q+ {d['quarters_pos']:.2f} | "
              f"c21 Sharpe {c21['sharpe']:.2f} | veto Sharpe {v['sharpe']:.2f} DD {v['max_dd']:.3f} | "
              f"bear {r['bear_pnl_dec']:.3f} rho {r['rho_p1']} trades {d['trades']} | {r['gates']} pass={r['pass']}")
        for n, a in r['assets'].items():
            print('   ', n, {lens: (round(m['sharpe'], 2), round(m['max_dd'], 3), m['from']) for lens, m in a.items() if m})
    path = os.path.join(lib.OUT, f'explore_{block}.json')

    def strip(o):
        if isinstance(o, dict):
            return {k: strip(v) for k, v in o.items() if k != '_curve'}
        return o
    with open(path, 'w') as fh:
        json.dump(strip(res), fh, indent=2, default=float)
    # Curves for F6, kept apart from the summary.
    np.save(os.path.join(lib.OUT, f'explore_{block}_curves.npy'),
            {t: {lens: r['basket'][lens]['_curve'] for lens in ('dec', 'c21')} for t, r in res['trials'].items()},
            allow_pickle=True)
    print(path)
    return 0


if __name__ == '__main__':
    sys.exit(main())
