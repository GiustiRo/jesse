"""r54 W1: P1 + "C6alts" (frozen C6 on the 48 U50 alts, curves from r54_v1) under the r51
inclusion rule, both P1 windows cut at 2024-12-31 (PROTOCOL_R54.md amendment 2026-10-26).

The sealed 2025 look is a separate command (`seal`), allowed by the protocol only if W1 passes.

    python research_scripts/r54_w1.py run
    python research_scripts/r54_w1.py seal

writes data/r52/w1.json (and w1_seal.json).
"""
import json
import os
import sys

import numpy as np

import r50_engines as en
import r50_f1b as fb
import r50_f2 as f2
import r51_lib as lib
import r51_f6 as f6

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'r52')
N_FINAL = 125      # 123 + W1 + M1
CUT = '2025-01-01'


def cut(cv, end=CUT):
    d, v = cv
    k = int(np.searchsorted(d, en.hz._ms(end)))
    return d[:k], v[:k]


def c6alts(end=CUT):
    curves = np.load(os.path.join(DATA, 'v1_curves.npy'), allow_pickle=True).item()
    meas = {s: cut(cv, end) for s, cv in curves.items()}
    return fb.basket(meas, list(meas))


def run():
    base = {}
    for w in ('long', 'common'):
        comps, _, _ = lib.p1_components(w)
        base[w] = {k: cut(v) for k, v in comps.items()}
    alt = c6alts()
    cand = {w: {'C6alts': alt} for w in base}
    ok, info = f6.compare(base, cand, [], [], N_FINAL)
    keep = ('from', 'cagr', 'max_dd', 'sharpe', 'months_pos', 'quarters_pos', 'q_pos_count', 'n_quarters', 'dsr', 'by_year')
    out = {'pass': bool(ok), 'd_sharpe_long': info['d_sharpe_long'], 'd_q_pos_long': info['d_q_pos_long'],
           'd_sharpe_common': info['d_sharpe_common'],
           'detail': {w: {k: {x: info['detail'][w][k][x] for x in keep if x in info['detail'][w][k]}
                          for k in ('base', 'with')} | {'from': info['detail'][w]['from']} for w in info['detail']}}
    # Contribution and weights of the new sleeve in the 2021+ window.
    m, _ = f6.evaluate({**base['common'], 'C6alts': alt}, [], N_FINAL)
    out['contrib_common'] = m['contrib_sum']
    json.dump(out, open(os.path.join(DATA, 'w1.json'), 'w'), indent=1, default=float)
    print(json.dumps({k: out[k] for k in ('pass', 'd_sharpe_long', 'd_q_pos_long', 'd_sharpe_common')}))
    for w, d in out['detail'].items():
        print(w, d['from'], 'P1', {x: round(d['base'][x], 3) for x in ('cagr', 'max_dd', 'sharpe', 'quarters_pos')},
              'W1', {x: round(d['with'][x], 3) for x in ('cagr', 'max_dd', 'sharpe', 'quarters_pos')})


def seal():
    """Single sealed look at 2025 for the included sleeve (protocol F3 gates)."""
    if not json.load(open(os.path.join(DATA, 'w1.json')))['pass']:
        raise SystemExit('W1 did not pass: 2025 stays sealed')
    alt = c6alts('2026-01-01')
    m = en.metrics(alt[0], alt[1], [], '2025-01-01')
    m['gates'] = {'sharpe_pos': m['sharpe'] > 0, 'no_collapse': not (m['sharpe'] < -0.5 or m['max_dd'] < -0.30)}
    m['pass'] = all(m['gates'].values())
    base = {}
    for w in ('long', 'common'):
        comps, _, _ = lib.p1_components(w)
        base[w] = comps
    f2.N_DECLARED = N_FINAL
    res = {'C6alts_2025': m, 'portfolios_2025': {}}
    for name, comps in (('P1', base['common']), ('W1', {**base['common'], 'C6alts': alt})):
        start = max(int(cv[0][0]) for cv in comps.values()) + en.DAY_MS
        cutc = {k: f6.trim(v, start) for k, v in comps.items()}
        days, vals, _, _ = lib.portfolio_attr(cutc, list(cutc))
        k = int(np.searchsorted(days, en.hz._ms('2025-01-01')))
        d, v = days[k - 1:], vals[k - 1:]
        r = np.diff(v) / v[:-1]
        res['portfolios_2025'][name] = {'return': float(v[-1] / v[0] - 1), 'max_dd': en.hz.max_dd(v),
                                        'sharpe': float(r.mean() / r.std(ddof=1) * np.sqrt(365))}
    json.dump(res, open(os.path.join(DATA, 'w1_seal.json'), 'w'), indent=1, default=float)
    print(json.dumps(res, default=float, indent=1))


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('run', 'seal'):
        print(__doc__)
        return 1
    run() if sys.argv[1] == 'run' else seal()
    return 0


if __name__ == '__main__':
    sys.exit(main())
