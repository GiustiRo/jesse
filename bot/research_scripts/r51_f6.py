"""r51 F6: portfolio construction, greedy inclusion and frozen validation.

PROTOCOL_R51.md F6 (8ac56348):
* construction = r50 F2 (inverse vol, 17% target, k <= 8, monthly), via r51_lib.portfolio_attr;
* T1 / T2 replace R1 only if their portfolio beats P1 under the inclusion rule;
* a diversifier that passed its gates enters greedily if it raises the 2018-09+ Sharpe by
  >= 0.05, or adds >= 1 positive quarter without lowering that Sharpe, and does not lower the
  2021-25 Sharpe by more than 0.05;
* comparisons are made on the same days: every portfolio in a comparison is cut to the latest
  start among its components (a later component would otherwise shorten only one side);
* frozen validation of the included sleeves on silver, Nasdaq, copper, EWJ and EWY.

    python research_scripts/r51_f6.py run

writes research_scripts/data/r51/f6_portfolio.json.
"""
import json
import math
import os
import sys

import numpy as np

import r50_harness as hz
import r50_engines as en
import r50_f1b as fb
import r50_f2 as f2
import r51_lib as lib
import r51_sleeves as sv
import r51_explore as ex
from r50_harness import T, C, DAY_MS
from r50_engines import simulate, calendar

LENS_OF_WINDOW = {'long': 'dec', 'common': 'c21'}
DS_MIN, DS_COMMON_MAX_DROP = 0.05, 0.05
VALIDATION = {'A1': ['COPPER'], 'B2': ['NDX', 'EWJ', 'EWY', 'XAG'],
              'T1': ['XAG', 'NDX', 'COPPER', 'EWJ', 'EWY'], 'T2': ['XAG', 'NDX', 'COPPER', 'EWJ', 'EWY']}


def trim(cv, from_ms):
    days, vals = cv
    k = max(int(np.searchsorted(days, from_ms - DAY_MS)), 0)
    return days[k:], vals[k:]


def evaluate(comps, trades, n_final):
    start = max(int(cv[0][0]) for cv in comps.values()) + DAY_MS
    cut = {k: trim(v, start) for k, v in comps.items()}
    days, vals, contrib, used = lib.portfolio_attr(cut, list(cut))
    f2.N_DECLARED = n_final
    m = f2.r9(days, vals, trades)
    m['q_pos_count'] = int(round(m['quarters_pos'] * m['n_quarters']))
    m['contrib_sum'] = {k: float(v.sum()) for k, v in contrib.items()}
    return m, start


def compare(base, cand, trades_b, trades_c, n_final):
    """Base vs base+candidate in both windows, each on its own common days."""
    out = {}
    for w in ('long', 'common'):
        both = {**base[w], **cand[w]}
        start = max(int(cv[0][0]) for cv in both.values()) + DAY_MS
        mb, _ = evaluate({k: trim(v, start) for k, v in base[w].items()}, trades_b, n_final)
        mc, _ = evaluate({k: trim(v, start) for k, v in both.items()}, trades_b + trades_c, n_final)
        out[w] = {'base': mb, 'with': mc, 'from': lib._date(start)}
    dl = out['long']['with']['sharpe'] - out['long']['base']['sharpe']
    dq = out['long']['with']['q_pos_count'] - out['long']['base']['q_pos_count']
    dc = out['common']['with']['sharpe'] - out['common']['base']['sharpe']
    ok = (dl >= DS_MIN or (dq >= 1 and dl >= 0)) and dc >= -DS_COMMON_MAX_DROP
    return ok, {'d_sharpe_long': dl, 'd_q_pos_long': dq, 'd_sharpe_common': dc, 'detail': out}


def replace_compare(p1, alt, trades_p1, n_final):
    """P1 vs P1 with R1 swapped for a T basket, same rule as an addition."""
    out = {}
    for w in ('long', 'common'):
        alt_c = {'R1': alt[w], 'C6': p1[w]['C6']}
        start = max(int(cv[0][0]) for cv in list(p1[w].values()) + [alt[w]]) + DAY_MS
        mb, _ = evaluate({k: trim(v, start) for k, v in p1[w].items()}, trades_p1, n_final)
        ma, _ = evaluate({k: trim(v, start) for k, v in alt_c.items()}, trades_p1, n_final)
        out[w] = {'p1': mb, 'alt': ma, 'from': lib._date(start)}
    dl = out['long']['alt']['sharpe'] - out['long']['p1']['sharpe']
    dq = out['long']['alt']['q_pos_count'] - out['long']['p1']['q_pos_count']
    dc = out['common']['alt']['sharpe'] - out['common']['p1']['sharpe']
    ok = (dl >= DS_MIN or (dq >= 1 and dl >= 0)) and dc >= -DS_COMMON_MAX_DROP
    return ok, {'d_sharpe_long': dl, 'd_q_pos_long': dq, 'd_sharpe_common': dc, 'detail': out}


# ----------------------------------------------------------------------------------------------
# Frozen validation
# ----------------------------------------------------------------------------------------------
def validation_bars(name):
    if name in ('EWJ', 'EWY'):
        return sv._cached(f'{name}_etf', lambda: lib.etf_daily(name))
    return sv.daily(name, 'cfd')


def validate(trial):
    rows = {}
    curves = {}
    for name in VALIDATION.get(trial, []):
        bars = validation_bars(name)
        start = max(hz._ms('2018-09-01'), int(bars[min(260, len(bars) - 1), T]))
        en.SLIP_BPS.setdefault(name, 10.0 if name == 'EWJ' else (5.0 if name in ('COPPER', 'EWY') else 0.0))
        if trial == 'A1':
            x = sv.a1_x(bars, True)
        elif trial == 'B2':
            x = sv.b2_x(bars, True)
        else:
            x = sv.t_x(name, bars, attenuate=trial == 'T2')
        ts, eq, acct = simulate(bars, start, sv.continuous_decider(bars, x), name, False)
        cv = calendar(ts, eq, lib._date(start), sv.END)
        curves[name] = cv
        m = en.metrics(cv[0], cv[1], acct.trades, lib._date(start))
        m['collapse'] = m['sharpe'] < -0.5 or m['max_dd'] < -0.30
        rows[name] = m
    if not rows:
        return None
    b = fb.basket(curves, list(curves))
    bm = en.metrics(b[0], b[1], [], lib._date(int(b[0][0])))
    years = len(b[1]) / 365
    t_stat = bm['sharpe'] * math.sqrt(years)
    passes = (sum(r['sharpe'] > 0 for r in rows.values()) > len(rows) / 2
              and not any(r['collapse'] for r in rows.values()) and bm['sharpe'] > 0 and t_stat >= 1.28)
    return {'assets': rows, 'basket': bm, 't_stat': t_stat, 'pass': bool(passes)}


def load_trials():
    res, curves = {}, {}
    for block in ex.BLOCKS:
        p = os.path.join(lib.OUT, f'explore_{block}.json')
        if not os.path.exists(p):
            continue
        res.update(json.load(open(p))['trials'])
        curves.update(np.load(os.path.join(lib.OUT, f'explore_{block}_curves.npy'), allow_pickle=True).item())
    return res, curves


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    trials, curves = load_trials()
    # The trials themselves; a P2 different from P1 would add one more (protocol F6).
    n_final = ex.N_BEFORE + len(trials)
    p1, p1_tr = {}, []
    for w in ('long', 'common'):
        comps, trades, _ = lib.p1_components(w)
        p1[w] = comps
        if w == 'long':
            p1_tr = trades
    out = {'n_final': n_final, 'trials_considered': sorted(trials), 'replacement': {}, 'inclusion': [],
           'validation': {}}
    base = {w: dict(p1[w]) for w in p1}
    # 1) R1 vs T1/T2.
    best_t, best_dl = None, None
    for t in ('T1', 'T2'):
        if t not in curves:
            continue
        alt = {w: curves[t][LENS_OF_WINDOW[w]] for w in p1}
        ok, info = replace_compare(p1, alt, p1_tr, n_final)
        out['replacement'][t] = {'ok': ok, **{k: v for k, v in info.items() if k != 'detail'},
                                 'detail': {w: {k: {x: info['detail'][w][k][x] for x in ('cagr', 'max_dd', 'sharpe', 'quarters_pos', 'q_pos_count')}
                                                for k in ('p1', 'alt')} for w in info['detail']}}
        if ok and (best_dl is None or info['d_sharpe_long'] > best_dl):
            best_t, best_dl = t, info['d_sharpe_long']
    if best_t:
        for w in base:
            base[w]['R1'] = curves[best_t][LENS_OF_WINDOW[w]]
    out['r1_choice'] = best_t or 'R1'
    # 2) Greedy additions among the diversifiers that passed their gates.
    pool = [t for t, r in trials.items() if t[0] in 'AB' and r['pass']]
    added = []
    while pool:
        scored = []
        for t in pool:
            cand = {w: {t: curves[t][LENS_OF_WINDOW[w]]} for w in base}
            ok, info = compare(base, cand, p1_tr, [], n_final)
            scored.append((ok, info['d_sharpe_long'], t, info))
        scored.sort(key=lambda s: (s[0], s[1]), reverse=True)
        ok, dl, t, info = scored[0]
        out['inclusion'].append({'step': len(added) + 1, 'evaluated': {s[2]: {'ok': s[0], 'd_sharpe_long': s[1],
                                 'd_q_pos_long': s[3]['d_q_pos_long'], 'd_sharpe_common': s[3]['d_sharpe_common']}
                                 for s in scored}})
        if not ok:
            break
        for w in base:
            base[w][t] = curves[t][LENS_OF_WINDOW[w]]
        added.append(t)
        pool.remove(t)
    out['added'] = added
    # 3) Final portfolio vs P1 on each window, plus validation of every included rule.
    final = {}
    for w in base:
        m, start = evaluate(base[w], p1_tr, n_final)
        mp, _ = evaluate({k: trim(v, start) for k, v in p1[w].items()}, p1_tr, n_final)
        final[w] = {'P2': {k: m[k] for k in ('from', 'cagr', 'max_dd', 'sharpe', 'pf_trades', 'months_pos', 'quarters_pos',
                                             'q_pos_count', 'n_quarters', 'median_month', 'without_best2_months', 'dsr',
                                             'by_year', 'gates', 'contrib_sum')},
                    'P1_same_days': {k: mp[k] for k in ('cagr', 'max_dd', 'sharpe', 'months_pos', 'quarters_pos', 'q_pos_count', 'dsr')}}
    out['final'] = final
    for t in added + ([best_t] if best_t else []):
        v = validate(t)
        if v is not None:
            out['validation'][t] = v
    path = os.path.join(lib.OUT, 'f6_portfolio.json')
    with open(path, 'w') as fh:
        json.dump(out, fh, indent=2, default=float)
    print(json.dumps({'r1_choice': out['r1_choice'], 'added': added,
                      'replacement': {k: {x: v[x] for x in ('ok', 'd_sharpe_long', 'd_q_pos_long', 'd_sharpe_common')} for k, v in out['replacement'].items()},
                      'final': {w: {'P2': {x: final[w]['P2'][x] for x in ('cagr', 'max_dd', 'sharpe', 'quarters_pos', 'dsr')},
                                    'P1': final[w]['P1_same_days']} for w in final},
                      'validation': {t: {'pass': v['pass'], 't': v['t_stat']} for t, v in out['validation'].items()}},
                     indent=1, default=float))
    print(path)
    return 0


if __name__ == '__main__':
    sys.exit(main())
