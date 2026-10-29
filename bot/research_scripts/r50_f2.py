"""r50 F2: portfolio construction and r9 gates for the F1b/F1c survivors (N4, C0, C6).

Construction, inclusion rule and gates are fixed in
`strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r50/PHASE2_PROTOCOL.md`,
committed before this file was written. Components are rebuilt with the same F1b/F1c code;
nothing inside a component is re-weighted.

    python research_scripts/r50_f2.py run

writes research_scripts/data/r50/f2_portfolio.json.
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
import r50_f1c as fc
from r50_harness import C, DAY_MS
from r50_engines import ASSETS, COMMON, simulate, calendar, daily_returns

TARGET = 0.17
K_MAX = 8.0          # r49 8% aggregate open risk with 1%-risk sleeves (protocol section 2)
MIN_DAYS = 120
N_DECLARED = 81
ORDER = ['C0', 'C6', 'N4']   # by common-window Sharpe in F1b/F1c


def _date(t):
    return datetime.fromtimestamp(t / 1000, tz=timezone.utc).date().isoformat()


def components(window):
    """Daily equity curves (from the window start) and trade PnLs of C0, C6 and N4."""
    curves, trades = {}, {}
    for name in fb.CORE:
        if ASSETS[name][window] is None:
            continue
        d = fb.load_both(name, window)
        if d is None:
            continue
        frm = _date(d['start_ms'])
        runs = {'R1': lambda: fb.r1_run(name, d)}
        if name in fc.CRYPTO:
            runs['R2'] = lambda: simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], False), name, d['funding'], fb.H4_MS)
            runs['R3'] = lambda: simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], True), name, d['funding'], fb.H4_MS)
        if name in en.M2_BASKET:
            runs['M2a'] = lambda: simulate(d['daily'], d['start_ms'], en.m2_decider(d['daily'], d['cfd'], 'a'), name, d['funding'])
        if name in ('WTI', 'GAS'):
            runs['N1'] = lambda: simulate(d['daily'], d['start_ms'], fb.n1_decider(d['daily'], d['cfd']), name, d['funding'])
        last = d['daily'][-1, C]
        for s, fn in runs.items():
            ts, eq, acct = fn()
            curves[(s, name)] = calendar(ts, eq, frm, COMMON[1])
            tr = acct.trades + ([{'closed': int(ts[-1]), 'pnl': acct.upnl(last)}] if acct.is_open else [])
            trades[(s, name)] = [t['pnl'] for t in tr]
        hz.jh.debug(f'{window} {name}: sleeves {sorted(runs)}')
    comp, comp_tr = {}, {}
    # C0: per-asset class sleeve, then the 7-asset equal-weight basket.
    per = {}
    for name, parts in fc.C0_MAP.items():
        ps = [p for p in parts if (p, name) in curves]
        if ps:
            per[name] = fc.mean_curve([curves[(p, name)] for p in ps])
            comp_tr.setdefault('C0', []).extend(sum((trades[(p, name)] for p in ps), []))
    comp['C0'] = fb.basket({k: v for k, v in per.items()}, list(per))
    # C6: crypto R2+R3.
    c6 = {n: fc.mean_curve([curves[('R2', n)], curves[('R3', n)]]) for n in fc.CRYPTO if ('R2', n) in curves}
    comp['C6'] = fb.basket(c6, list(c6))
    comp_tr['C6'] = sum((trades[(s, n)] for n in c6 for s in ('R2', 'R3')), [])
    # N4: 50/50 of the R1 basket (7) and the M2a basket (5).
    r1 = fb.basket(curves, [k for k in curves if k[0] == 'R1'])
    m2 = fb.basket(curves, [k for k in curves if k[0] == 'M2a'])
    comp['N4'] = fb.basket({'r1': r1, 'm2': m2}, ['r1', 'm2'])
    comp_tr['N4'] = sum((trades[k] for k in trades if k[0] in ('R1', 'M2a')), [])
    return comp, comp_tr


def portfolio(comp, names):
    """Inverse-vol weights and 17% vol target from expanding covariance, monthly, k <= 8."""
    series = [daily_returns(*comp[n]) for n in names]
    days = sorted(set.intersection(*[set(s) for s in series]))
    R = np.array([[s[d] for s in series] for d in days])
    months = [_date(d)[:7] for d in days]
    w, k = None, None
    rets, ks, used_from = [], [], None
    for t in range(len(days)):
        if w is not None:
            rets.append(k * float(w @ R[t]))
            ks.append(k)
            if used_from is None:
                used_from = days[t]
        if t + 1 < len(days) and months[t + 1] != months[t] and t + 1 >= MIN_DAYS:
            hist = R[:t + 1]
            sd = hist.std(axis=0, ddof=1)
            if (sd > 0).all():
                w = (1 / sd) / (1 / sd).sum()
                cov = np.atleast_2d(np.cov(hist, rowvar=False))
                sp = math.sqrt(float(w @ cov @ w)) * math.sqrt(365)
                k = min(K_MAX, TARGET / sp) if sp > 0 else K_MAX
    vals = en.BALANCE * np.r_[1.0, np.cumprod(1 + np.array(rets))]
    pdays = np.array([used_from - DAY_MS] + [d for d in days if d >= used_from])
    return pdays, vals, {'k_mean': float(np.mean(ks)), 'k_max_hit_share': float(np.mean(np.array(ks) >= K_MAX - 1e-9)),
                         'weights_last': dict(zip(names, (w.tolist() if w is not None else [])))}


def r9(days, vals, trade_pnls):
    r = np.diff(vals) / vals[:-1]
    years = len(r) / 365
    dates = [_date(d) for d in days]
    month_end = {}
    for d, v in zip(dates, vals):
        month_end[d[:7]] = v
    mv = [vals[0]] + list(month_end.values())
    mret = np.array(mv[1:]) / np.array(mv[:-1]) - 1
    q_end = {}
    for d, v in zip(dates, vals):
        q_end[f'{d[:4]}Q{(int(d[5:7]) - 1) // 3 + 1}'] = v
    qv = [vals[0]] + list(q_end.values())
    qret = np.array(qv[1:]) / np.array(qv[:-1]) - 1
    y_end = {}
    for d, v in zip(dates, vals):
        y_end[d[:4]] = v
    yv = [vals[0]] + list(y_end.values())
    by_year = dict(zip(y_end, (np.array(yv[1:]) / np.array(yv[:-1]) - 1).round(4).tolist()))
    pos = sum(p for p in trade_pnls if p > 0)
    neg = -sum(p for p in trade_pnls if p < 0)
    without2 = float(np.prod(1 + np.sort(mret)[:-2]) - 1) if len(mret) > 2 else None
    out = {
        'from': dates[0], 'to': dates[-1],
        'cagr': float((vals[-1] / vals[0]) ** (1 / years) - 1),
        'max_dd': hz.max_dd(vals),
        'sharpe': float(r.mean() / r.std(ddof=1) * math.sqrt(365)),
        'vol_realized': float(r.std(ddof=1) * math.sqrt(365)),
        'pf_trades': float(pos / neg) if neg > 0 else None,
        'months_pos': float((mret > 0).mean()), 'quarters_pos': float((qret > 0).mean()),
        'n_quarters': int(len(qret)), 'median_month': float(np.median(mret)),
        'without_best2_months': without2, 'dsr': fb.dsr(vals, N_DECLARED), 'by_year': by_year,
    }
    out['gates'] = {
        'cagr_ge_30': out['cagr'] >= 0.30, 'dd_le_20': out['max_dd'] >= -0.20, 'dd_le_25_ceiling': out['max_dd'] >= -0.25,
        'pf_ge_1_2': out['pf_trades'] is not None and out['pf_trades'] >= 1.2,
        'months_ge_65': out['months_pos'] >= 0.65, 'quarters_ge_80': out['quarters_pos'] >= 0.80,
        'median_month_pos': out['median_month'] > 0,
        'positive_without_best2': without2 is not None and without2 > 0, 'dsr_ge_0_95': (out['dsr'] or 0) >= 0.95}
    out['gates'] = {k: bool(v) for k, v in out['gates'].items()}
    out['all_r9_pass'] = all(v for k, v in out['gates'].items() if k != 'dd_le_25_ceiling')
    return out


def run():
    res = {'protocol': 'RESEARCH_HUB/revisions/20261024-r50/PHASE2_PROTOCOL.md', 'n_declared': N_DECLARED,
           'single': {}, 'inclusion': {}}
    comps = {w: components(w) for w in ('common', 'long')}

    def evaluate(names, window):
        comp, tr = comps[window]
        days, vals, info = portfolio(comp, names)
        out = r9(days, vals, sum((tr[n] for n in names), []))
        out.update(info)
        return out

    for n in ORDER:
        res['single'][n] = {w: evaluate([n], w) for w in ('common', 'long')}
    chosen = [ORDER[0]]
    log = []
    base = res['single'][ORDER[0]]['common']
    for n in ORDER[1:]:
        trial = {w: evaluate(chosen + [n], w) for w in ('common', 'long')}
        improves = trial['common']['sharpe'] > base['sharpe'] or trial['common']['quarters_pos'] > base['quarters_pos']
        vetoed = trial['long']['sharpe'] < 0 or trial['long']['max_dd'] < -0.25
        log.append({'add': n, 'to': list(chosen), 'improves': bool(improves), 'long_veto': bool(vetoed),
                    'sharpe_with': trial['common']['sharpe'], 'sharpe_without': base['sharpe'],
                    'q_with': trial['common']['quarters_pos'], 'q_without': base['quarters_pos']})
        if improves and not vetoed:
            chosen.append(n)
            base = trial['common']
            res['inclusion']['_last'] = trial
    final = {w: evaluate(chosen, w) for w in ('common', 'long')}
    res['inclusion'] = {'log': log, 'final_components': chosen, 'final': final}
    os.makedirs(hz.OUT_DIR, exist_ok=True)
    with open(os.path.join(hz.OUT_DIR, 'f2_portfolio.json'), 'w') as fh:
        json.dump(res, fh, indent=2, default=float)
    hz.jh.debug(json.dumps({'final_components': chosen, 'log': log,
                            'final_common': {k: final['common'][k] for k in ('cagr', 'max_dd', 'sharpe', 'months_pos', 'quarters_pos', 'dsr', 'k_mean')},
                            'final_long': {k: final['long'][k] for k in ('cagr', 'max_dd', 'sharpe', 'months_pos', 'quarters_pos', 'dsr', 'k_mean')}},
                           default=float, indent=1))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        run()
    else:
        print(__doc__)


if __name__ == '__main__':
    sys.exit(main())
