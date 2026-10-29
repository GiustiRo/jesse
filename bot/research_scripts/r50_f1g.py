"""r50 F1g: decorrelated equity-class sleeves (G1 turn of month, G2 US-index reversal,
G3 volatility-panic buying) and portfolio P5 = P1 + passing sleeves.

Fixed in `strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r50/PHASE1G_PROTOCOL.md`
(commit 33e038be), written before this file.

    python research_scripts/r50_f1g.py run

writes research_scripts/data/r50/f1g_screen.json.
"""
import json
import math
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
import r50_f1d as fd
import r50_f1e as fe
import r50_f1f as ff
from r50_harness import T, C, L, DAY_MS
from r50_engines import COMMON, MEASURE_FROM, TAKER, TARGET_VOL, MAX_X, simulate, calendar, daily_returns, ann_vol, sma, logret

N_DECLARED = 98
EQUITIES = ['SPX', 'NDX', 'IWM', 'SMH', 'EWJ', 'EWY', 'EWZ', 'EWT']
US_INDICES = ['SPX', 'NDX', 'IWM', 'SMH']
UNIV = {'G1': EQUITIES, 'G2': US_INDICES, 'G3': EQUITIES}


def _date(t):
    return datetime.fromtimestamp(t / 1000, tz=timezone.utc).date().isoformat()


def load(name, window):
    if name == 'SPX':
        return fb.load_both('SPX', window)
    if name in ('NDX', 'EWJ', 'EWY'):
        return f3.load(name, window)
    en.SLIP_BPS[name] = ff.NEW_SLIP_BPS
    return ff.etf_load(name, window)


def g1_decider(bars):
    """Long from the close of the penultimate trading day of a month to the close of the
    third trading day of the next month (days -1..+3)."""
    c = bars[:, C]
    vol = ann_vol(c, True)
    months = [_date(int(t))[:7] for t in bars[:, T]]
    from_start = np.zeros(len(c), dtype=int)
    from_end = np.zeros(len(c), dtype=int)
    for i in range(len(c)):
        from_start[i] = 1 if i == 0 or months[i] != months[i - 1] else from_start[i - 1] + 1
    for i in range(len(c) - 1, -1, -1):
        from_end[i] = 1 if i == len(c) - 1 or months[i] != months[i + 1] else from_end[i + 1] + 1

    def decide(i, acct, ts):
        if acct.is_open:
            if from_start[i] == 3:
                fb._trade(acct, -acct.qty, c[i], ts, TAKER)
            return
        if from_end[i] == 2 and np.isfinite(vol[i]) and vol[i] > 0:
            fb._trade(acct, acct.equity(c[i]) * min(MAX_X, TARGET_VOL / vol[i]) / c[i], c[i], ts, TAKER)
    return decide


def g3_decider(bars):
    c = bars[:, C]
    vol = ann_vol(c, True)
    v10 = en.rolling_std(logret(c), 10) * math.sqrt(252)
    med = np.full(len(c), np.nan)
    for i in range(262, len(c)):
        w = v10[i - 251:i + 1]
        med[i] = np.nanmedian(w)
    lo20 = en.prior_min(c, 20)
    s20 = sma(c, 20)
    st = {'held': 0}

    def decide(i, acct, ts):
        if acct.is_open:
            st['held'] += 1
            if st['held'] >= 20 or (np.isfinite(s20[i]) and c[i] > s20[i]):
                fb._trade(acct, -acct.qty, c[i], ts, TAKER)
            return
        if (np.isfinite(med[i]) and np.isfinite(v10[i]) and v10[i] > 2 * med[i] and np.isfinite(lo20[i])
                and c[i] < lo20[i] and np.isfinite(vol[i]) and vol[i] > 0):
            fb._trade(acct, acct.equity(c[i]) * min(MAX_X, TARGET_VOL / vol[i]) / c[i], c[i], ts, TAKER)
            st['held'] = 0
    return decide


def run():
    f2.N_DECLARED = N_DECLARED
    res = {'protocol': 'RESEARCH_HUB/revisions/20261024-r50/PHASE1G_PROTOCOL.md', 'n_declared': N_DECLARED,
           'sleeves': {}, 'per_asset': {}, 'portfolio': {}}
    comps, comp_tr = {}, {}
    for window in ('common', 'long'):
        curves, trades, mf = {}, {}, {}
        for name in EQUITIES:
            d = load(name, window)
            if d is None:
                continue
            b = d['daily']
            runs = {'G1': lambda: simulate(b, d['start_ms'], g1_decider(b), name, False),
                    'G3': lambda: simulate(b, d['start_ms'], g3_decider(b), name, False)}
            if name in US_INDICES:
                runs['G2'] = lambda: simulate(b, d['start_ms'], en.m2_decider(b, True, 'a'), name, False)
            last = b[-1, C]
            for g, fn in runs.items():
                ts, eq, acct = fn()
                curves[(g, name)] = calendar(ts, eq, _date(d['start_ms']), COMMON[1])
                tr = acct.trades + ([{'closed': int(ts[-1]), 'pnl': acct.upnl(last)}] if acct.is_open else [])
                trades[(g, name)] = [t['pnl'] for t in tr if t['closed'] >= hz._ms(d['mfrom'])]
                m = en.metrics(*curves[(g, name)], tr, d['mfrom'])
                res['per_asset'].setdefault(f'{g}/{name}', {})[window] = (
                    {k: m[k] for k in ('sharpe', 'cagr', 'max_dd', 'trades_per_year')} if m else None)
            mf[name] = d['mfrom']
        mfrom = MEASURE_FROM if window == 'common' else min(mf.values())
        tc, ttr = fe.trend_components(window)
        p1d, p1v, _ = f2.portfolio(tc, ['R1', 'C6'])
        p1 = (p1d, p1v)
        comps[window], comp_tr[window] = dict(tc), {'R1': ttr['R1'], 'C6': ttr['C6']}
        for g, members in UNIV.items():
            keys = [(g, n) for n in members if (g, n) in curves]
            bk = fb.basket(curves, keys)
            tr = sum((trades[k] for k in keys), [])
            m = fd.measure(bk, mfrom, tr)
            a, bb = daily_returns(*p1), daily_returns(*bk)
            ds = [t for t in a if t in bb]
            m['corr_p1'] = float(np.corrcoef([a[t] for t in ds], [bb[t] for t in ds])[0, 1]) if len(ds) > 30 else None
            m['corr_p1_losing_quarters'], m['p1_losing_quarters'] = fb.corr_in_losing(p1, bk)
            m['trades_per_year'] = m['trades'] / (len(bk[0]) / 365) if m.get('trades') else 0
            m['members'] = [k[1] for k in keys]
            res['sleeves'].setdefault(g, {})[window] = m
            comps[window][g], comp_tr[window][g] = bk, tr
        hz.jh.debug(f'{window}: ' + json.dumps({g: round(v[window]['sharpe'], 2) for g, v in res['sleeves'].items()}))
    gates = {}
    for g in UNIV:
        c, l = res['sleeves'][g]['common'], res['sleeves'][g]['long']
        cl = [x for x in (c.get('corr_p1'), c.get('corr_p1_losing_quarters'), l.get('corr_p1'), l.get('corr_p1_losing_quarters'))]
        gg = {'sharpe_long_ge_0_5': l['sharpe'] >= 0.5, 'sharpe_common_ge_0_5': c['sharpe'] >= 0.5,
              'both_halves_pos': len(l['halves']) == 2 and all(v > 0 for v in l['halves'].values()),
              'top5_lt_60': l.get('top5_share') is not None and l['top5_share'] < 0.6,
              'decorrelated_le_0_3': all(x is not None and x <= 0.3 for x in cl)}
        gg = {k: bool(v) for k, v in gg.items()}
        gg['pass'] = all(gg.values())
        gates[g] = gg
    res['gates'] = gates
    chosen, log = ['R1', 'C6'], []
    base = fd.port_eval(comps, chosen, comp_tr)
    res['portfolio']['P1'] = base
    for g in sorted([g for g in UNIV if gates[g]['pass']], key=lambda g: -res['sleeves'][g]['long']['sharpe']):
        trial = fd.port_eval(comps, chosen + [g], comp_tr)
        improves = (trial['common']['sharpe'] > base['common']['sharpe']
                    or trial['common']['quarters_pos'] > base['common']['quarters_pos'])
        vetoed = trial['long']['sharpe'] < 0 or trial['long']['max_dd'] < -0.25
        log.append({'add': g, 'improves': bool(improves), 'long_veto': bool(vetoed),
                    'sharpe_with': trial['common']['sharpe'], 'sharpe_without': base['common']['sharpe'],
                    'q_with': trial['common']['quarters_pos'], 'q_without': base['common']['quarters_pos']})
        if improves and not vetoed:
            chosen.append(g)
            base = trial
    res['portfolio']['P5'] = {'components': chosen, 'log': log, 'eval': base,
                              'pass': bool(base['common']['pass_r50'] and base['long']['pass_r50'])}
    os.makedirs(hz.OUT_DIR, exist_ok=True)
    with open(os.path.join(hz.OUT_DIR, 'f1g_screen.json'), 'w') as fh:
        json.dump(res, fh, indent=2, default=float)
    hz.jh.debug(json.dumps({'gates': gates, 'P5': chosen, 'log': log}, default=float, indent=1))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        run()
    else:
        print(__doc__)


if __name__ == '__main__':
    sys.exit(main())
