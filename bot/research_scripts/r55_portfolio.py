"""r55 F4: marginal assets into R1 and R1 without the bond, over P1 (N 133 -> 139).

PROTOCOL_R55.md F4 and its F4 amendment (f569df80). No F1-F3 piece passed, so the base is P1.
* Marginal assets, one at a time in the fixed order NDX, XAG, COPPER, EWY, EWJ: the r50 R1 curve
  (`r50_f3.load` + `r1_4h_run` / `r1_daily_run`, r50 configuration) joins the R1 basket of the
  current portfolio. Enters if its own long-lens Sharpe (window `long` from mfrom, cut at
  2024-12-31) >= 0.3, it passes the r51 inclusion rule, and the portfolio DD is not worse by more
  than 1 pp in either window.
* R1 without the bond: removal from the current portfolio, decided on 2021-24 only (Sharpe
  +0.05, or +1 positive quarter without a lower Sharpe), since P1's 2018-09+ window has no bond.
Both P1 windows cut at 2024-12-31; 2025 sealed.

    python research_scripts/r55_portfolio.py run

writes research_scripts/data/r55/f4_portfolio.json.
"""
import json
import os
import sys

import numpy as np

import r50_engines as en
import r50_f1b as fb
import r50_f3 as f3
import r51_lib as lib
import r51_f6 as f6
import r55_regimes as rg
import r55_engine as eg
from r50_harness import C, DAY_MS
from r50_engines import calendar, COMMON

N_DECLARED = 139
ORDER = ('NDX', 'XAG', 'COPPER', 'EWY', 'EWJ')
OWN_MIN = 0.3
DD_TOL = 0.01


def val_curve(name, window):
    d = f3.load(name, window)
    spec = f3.VAL[name]
    ts, eq, acct = f3.r1_4h_run(name, d, spec['r1']) if d['h4'] is not None else f3.r1_daily_run(name, d)
    return calendar(ts, eq, lib._date(d['start_ms']), COMMON[1]), d['mfrom']


def run():
    eg.N_DECLARED = N_DECLARED
    t, c = rg.btc_daily()
    qlab, mlab = rg.labels_a(t, c), rg.labels_a(t, c, monthly=True)
    base = {}
    for w in ('long', 'common'):
        comps, _, extra = lib.p1_components(w)
        start = max(int(cv[0][0]) for cv in comps.values()) + DAY_MS
        assert np.allclose(fb.basket(extra['r1'], list(extra['r1']))[1], comps['R1'][1])
        base[w] = {'start': start, 'C6': comps['C6'], 'r1': dict(extra['r1'])}

    def ev(members):
        out = {}
        for w in ('long', 'common'):
            r1 = {n: cv for n, cv in members[w].items()}
            comps = {'R1': fb.basket(r1, list(r1)), 'C6': base[w]['C6']}
            out[w] = eg.evaluate(*eg.portfolio(comps, base[w]['start']), qlab, mlab)
        return out

    cur = {w: dict(base[w]['r1']) for w in base}
    cur_ev = ev(cur)
    res = {'protocol': 'RESEARCH_HUB/revisions/20261026-r55/PROTOCOL_R55.md F4 + enmienda f569df80',
           'n_declared': N_DECLARED, 'measured_through': rg.CUT, 'P1': cur_ev, 'steps': [], 'members_in': []}
    print('P1', {w: (round(cur_ev[w]['sharpe'], 3), round(cur_ev[w]['max_dd'], 3), cur_ev[w]['q_pos_count'])
                 for w in cur_ev})
    for name in ORDER:
        lc, mfrom = val_curve(name, 'long')
        cc, _ = val_curve(name, 'common')
        d, v = rg.cut_to(lc, rg.CUT_MS)
        own = en.metrics(d, v, [], mfrom)
        cand = {'long': {**cur['long'], name: lc}, 'common': {**cur['common'], name: cc}}
        cev = ev(cand)
        dl = cev['long']['sharpe'] - cur_ev['long']['sharpe']
        dc = cev['common']['sharpe'] - cur_ev['common']['sharpe']
        dq = cev['long']['q_pos_count'] - cur_ev['long']['q_pos_count']
        g = {'own_long_sharpe_ge_0_3': own['sharpe'] >= OWN_MIN,
             'inclusion_r51': bool((dl >= f6.DS_MIN or (dq >= 1 and dl >= 0)) and dc >= -f6.DS_COMMON_MAX_DROP),
             'dd_not_worse_1pp': all(cev[w]['max_dd'] - cur_ev[w]['max_dd'] >= -DD_TOL for w in cev)}
        ok = all(g.values())
        step = {'trial': name, 'own_long': {k: own[k] for k in ('from', 'to', 'sharpe', 'cagr', 'max_dd')},
                'with': cev, 'gates': g, 'pass': bool(ok),
                'deltas': {'d_sharpe_long': dl, 'd_sharpe_common': dc, 'd_q_pos_long': dq,
                           'd_q_pos_common': cev['common']['q_pos_count'] - cur_ev['common']['q_pos_count'],
                           'd_cagr_long': cev['long']['cagr'] - cur_ev['long']['cagr'],
                           'd_cagr_common': cev['common']['cagr'] - cur_ev['common']['cagr'],
                           'd_dd_long': cev['long']['max_dd'] - cur_ev['long']['max_dd'],
                           'd_dd_common': cev['common']['max_dd'] - cur_ev['common']['max_dd']}}
        res['steps'].append(step)
        print(name, 'IN' if ok else 'no', g, 'own', round(own['sharpe'], 3), own['from'],
              {k: round(x, 4) for k, x in step['deltas'].items()})
        if ok:
            cur, cur_ev = cand, cev
            res['members_in'].append(name)

    # R1 without the bond (common window only has it).
    assert 'BOND' not in cur['long'] and 'BOND' in cur['common']
    cand = {'long': dict(cur['long']), 'common': {n: cv for n, cv in cur['common'].items() if n != 'BOND'}}
    cev = ev(cand)
    dl = cev['long']['sharpe'] - cur_ev['long']['sharpe']
    dc = cev['common']['sharpe'] - cur_ev['common']['sharpe']
    dqc = cev['common']['q_pos_count'] - cur_ev['common']['q_pos_count']
    g = {'common_rule': bool(dc >= f6.DS_MIN or (dqc >= 1 and dc >= 0)), 'long_not_worse': bool(dl >= -1e-12)}
    ok = all(g.values())
    res['steps'].append({'trial': 'NOBOND', 'with': cev, 'gates': g, 'pass': bool(ok),
                         'deltas': {'d_sharpe_long': dl, 'd_sharpe_common': dc, 'd_q_pos_common': dqc,
                                    'd_cagr_common': cev['common']['cagr'] - cur_ev['common']['cagr'],
                                    'd_dd_common': cev['common']['max_dd'] - cur_ev['common']['max_dd']}})
    print('NOBOND', 'IN' if ok else 'no', g, {k: round(x, 4) for k, x in res['steps'][-1]['deltas'].items()})
    if ok:
        cur, cur_ev = cand, cev
        res['members_in'].append('-BOND')
    res['final'] = {'members': {w: sorted(cur[w]) for w in cur}, 'metrics': cur_ev,
                    'equals_P1': not res['members_in']}
    for w in ('long', 'common'):
        m = cur_ev[w]
        print('final', w, f"CAGR {m['cagr']:.3f} DD {m['max_dd']:.3f} S {m['sharpe']:.3f} Q+ {m['q_pos_count']}/{m['n_quarters']} DSR {m['dsr']:.3f}",
              {k: (round(x['sum'], 3), round(x['median'] or 0, 4), x['pos'], x['n']) for k, x in m['quarters'].items()})
    path = os.path.join(rg.OUT, 'f4_portfolio.json')
    with open(path, 'w') as fh:
        json.dump(res, fh, indent=2, default=float)
    print(path)


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
