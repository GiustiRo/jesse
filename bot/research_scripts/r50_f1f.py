"""r50 F1f: R1 on the broad universe of Binance-tradable futures, plus crypto breakouts (P4).

Fixed in `strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r50/PHASE1F_PROTOCOL.md`
(commit 0ca8b769), written before the new data was downloaded or this file was written.

    python research_scripts/r50_f1f.py run

writes research_scripts/data/r50/f1f_screen.json.
"""
import json
import os
import sys
from datetime import datetime, timezone

import numpy as np
import jesse.models  # noqa: F401 - must load before candle_service (circular import otherwise)

import r50_harness as hz
import r50_engines as en
import r50_f1b as fb
import r50_f2 as f2
import r50_f3 as f3
import r50_f1e as fe
import r50_f1d as fd
from r50_harness import T, C, DAY_MS
from r50_engines import COMMON, MEASURE_FROM, ASSETS, calendar

N_DECLARED = 94
NEW_ETF = ['IWM', 'EWZ', 'EWT', 'GDX', 'SMH', 'XLE', 'XBI', 'BNO', 'PPLT', 'PALL']
NEW_SLIP_BPS = 5.0   # unmeasured liquidity of the new TradFi perps (protocol section 3)


def _date(t):
    return datetime.fromtimestamp(t / 1000, tz=timezone.utc).date().isoformat()


def etf_load(ticker, window):
    daily = f3._etf_daily(f'{ticker}_daily_2000-01-01_2025-12-31.csv')
    if len(daily) < 300:
        return None
    if window == 'common':
        start_ms, mfrom = hz._ms(COMMON[0]), MEASURE_FROM
    else:
        start_ms = int(daily[260, T])
        mfrom = _date(start_ms)
    return {'daily': daily, 'h4': None, 'start_ms': start_ms, 'mfrom': mfrom}


def r1_sleeves(window):
    """R1 curves (from the window start) and trades for every market of the broad universe."""
    curves, trades, info = {}, {}, {}

    def add(name, ts, eq, acct, d, last):
        curves[name] = calendar(ts, eq, _date(d['start_ms']), COMMON[1])
        tr = acct.trades + ([{'closed': int(ts[-1]), 'pnl': acct.upnl(last)}] if acct.is_open else [])
        trades[name] = [t['pnl'] for t in tr if t['closed'] >= hz._ms(d['mfrom'])]
        info[name] = {'mfrom': d['mfrom'], 'first': hz._date(int(d['daily'][0, T]))[:10]}

    for name in fb.CORE:
        if ASSETS[name][window] is None:
            continue
        d = fb.load_both(name, window)
        if d is None:
            continue
        ts, eq, acct = fb.r1_run(name, d)
        add(name, ts, eq, acct, d, d['daily'][-1, C])
    for name, spec in f3.VAL.items():
        d = f3.load(name, window)
        if d is None:
            continue
        ts, eq, acct = f3.r1_4h_run(name, d, spec['r1']) if d['h4'] is not None else f3.r1_daily_run(name, d)
        add(name, ts, eq, acct, d, d['daily'][-1, C])
    for t in NEW_ETF:
        en.SLIP_BPS[t] = NEW_SLIP_BPS
        d = etf_load(t, window)
        if d is None:
            continue
        ts, eq, acct = f3.r1_daily_run(t, d)
        add(t, ts, eq, acct, d, d['daily'][-1, C])
    hz.jh.debug(f'{window}: R1 sleeves {sorted(curves)}')
    return curves, trades, info


def run():
    f2.N_DECLARED = N_DECLARED
    res = {'protocol': 'RESEARCH_HUB/revisions/20261024-r50/PHASE1F_PROTOCOL.md', 'n_declared': N_DECLARED,
           'per_market': {}, 'R1_broad': {}, 'R1_broad_scaled': {}, 'P4': {}}
    for window in ('common', 'long'):
        curves, trades, info = r1_sleeves(window)
        mfrom = MEASURE_FROM if window == 'common' else min(v['mfrom'] for v in info.values())
        for n, cv in curves.items():
            m = en.metrics(cv[0], cv[1], [], info[n]['mfrom'])
            res['per_market'].setdefault(n, {})[window] = {k: m[k] for k in ('sharpe', 'cagr', 'max_dd', 'quarters_pos')} if m else None
        bk = fb.basket(curves, list(curves))
        res['R1_broad'][window] = fd.measure(bk, mfrom, sum(trades.values(), []))
        res['R1_broad'][window]['markets'] = len(curves)
        days, vals, inf = f2.portfolio({'R1x': bk}, ['R1x'])
        res['R1_broad_scaled'][window] = dict(f2.r9(days, vals, sum(trades.values(), [])), **inf)
        comps, trs = fe.trend_components(window)
        comps['R1x'] = bk
        days, vals, inf = f2.portfolio(comps, ['R1x', 'C6'])
        r9 = f2.r9(days, vals, sum(trades.values(), []) + trs['C6'])
        r9.update(inf)
        r9['gates_r50'] = {k: r9['gates'][k] for k in ('cagr_ge_30', 'dd_le_20', 'pf_ge_1_2', 'median_month_pos',
                                                       'positive_without_best2', 'dsr_ge_0_95')}
        r9['pass_r50'] = all(r9['gates_r50'].values())
        res['P4'][window] = r9
        hz.jh.debug(f'{window}: R1_broad sharpe {res["R1_broad"][window]["sharpe"]:.2f}; P4 sharpe {r9["sharpe"]:.2f} cagr {r9["cagr"]:.3f}')
    c, l = res['R1_broad']['common'], res['R1_broad']['long']
    g = {'sharpe_long_ge_0_5': l['sharpe'] >= 0.5, 'sharpe_common_ge_0_5': c['sharpe'] >= 0.5,
         'both_halves_pos': len(l['halves']) == 2 and all(v > 0 for v in l['halves'].values()),
         'top5_lt_60': l.get('top5_share') is not None and l['top5_share'] < 0.6}
    g = {k: bool(v) for k, v in g.items()}
    g['pass'] = all(g.values())
    res['R1_broad_gates'] = g
    res['pass'] = bool(g['pass'] and res['P4']['common']['pass_r50'] and res['P4']['long']['pass_r50'])
    os.makedirs(hz.OUT_DIR, exist_ok=True)
    with open(os.path.join(hz.OUT_DIR, 'f1f_screen.json'), 'w') as fh:
        json.dump(res, fh, indent=2, default=float)
    hz.jh.debug(json.dumps({'gates': g, 'pass': res['pass']}, default=float))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        run()
    else:
        print(__doc__)


if __name__ == '__main__':
    sys.exit(main())
