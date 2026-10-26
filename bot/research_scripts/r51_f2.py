"""r51 F2: descriptive diagnosis of P1 (no trial, N unchanged).

PROTOCOL_R51.md F2: P1 (with the F1 bond correction) broken down by sleeve and asset; the target
quarters (P1 return <= 0) with each underlying's buy-and-hold return and each sleeve's
contribution; an ideal short bound per family (informative ceiling, not a rule); and the P1 PnL
by family and direction.

    python research_scripts/r51_f2.py run

writes research_scripts/data/r51/f2_diagnosis.json.
"""
import json
import math
import os
import sys

import numpy as np

import r50_harness as hz
import r50_engines as en
import r50_f2 as f2
import r51_lib as lib
from r50_harness import T, C, DAY_MS
from r50_engines import daily_returns

# Ideal short bound: the family is shorted at the r49 sleeve vol target with the 2x cap,
# sized from the 60 trading days before the quarter (no look-ahead in the size, only in the
# direction, which is what makes it a ceiling).
TARGET_VOL, MAX_X, VOL_DAYS = 0.17, 2.0, 60


def asset_quarters(daily):
    """Quarter -> buy-and-hold return of the close, and the prior-60-day vol at quarter start."""
    t, c = daily[:, T].astype(np.int64), daily[:, C]
    q_last, q_first_idx = {}, {}
    for i, ts in enumerate(t):
        q = lib.quarter_of(ts)
        q_last[q] = c[i]
        q_first_idx.setdefault(q, i)
    qs = list(q_last)
    out = {}
    for a, b in zip(qs[:-1], qs[1:]):
        i0 = q_first_idx[b]
        lr = np.diff(np.log(c[max(0, i0 - VOL_DAYS - 1):i0]))
        vol = float(lr.std(ddof=1) * math.sqrt(252)) if len(lr) > 20 else float('nan')
        out[b] = {'bh': float(q_last[b] / q_last[a] - 1), 'vol': vol}
    return out


def run(window):
    comps, trades, extra = lib.p1_components(window)
    days, vals, contrib, used = lib.portfolio_attr(comps, ['R1', 'C6'])
    # Same numbers as r50_f2.portfolio (checked against r50 close for the long window).
    f2.N_DECLARED = 98
    summary = f2.r9(days, vals, trades)
    pq = lib.quarterly(days, vals)
    # Per-asset contributions inside the R1 basket: the basket return is the mean of the sleeves
    # that have a return that day, so each asset contributes k*w_R1*r_asset/n_available.
    r1 = {n: daily_returns(*cv) for n, cv in extra['r1'].items()}
    c6 = {n: daily_returns(*cv) for n, cv in extra['c6'].items()}
    r1_k = {}
    for j, d in enumerate(used):
        avail = [n for n in r1 if d in r1[n]]
        basket_r = np.mean([r1[n][d] for n in avail]) if avail else 0.0
        scale = contrib['R1'][j] / basket_r if basket_r else 0.0
        for n in avail:
            r1_k.setdefault(n, {})[d] = scale * r1[n][d] / len(avail)
    c6_k = {}
    for j, d in enumerate(used):
        avail = [n for n in c6 if d in c6[n]]
        basket_r = np.mean([c6[n][d] for n in avail]) if avail else 0.0
        scale = contrib['C6'][j] / basket_r if basket_r else 0.0
        for n in avail:
            c6_k.setdefault(n, {})[d] = scale * c6[n][d] / len(avail)
    sleeves = {f'R1/{n}': v for n, v in r1_k.items()}
    sleeves.update({f'C6/{n}': v for n, v in c6_k.items()})

    def q_sum(series, q):
        return float(sum(v for d, v in series.items() if lib.quarter_of(d) == q))

    under = {n: asset_quarters(d['daily']) for n, d in extra['data'].items()}
    targets = [q for q, r in pq.items() if r <= 0]
    rows = []
    for q in targets:
        row = {'quarter': q, 'p1': pq[q], 'sleeves': {s: q_sum(v, q) for s, v in sleeves.items()},
               'underlying_bh': {n: under[n].get(q, {}).get('bh') for n in under}, 'ideal_short_by_family': {}}
        fam = {}
        for n, u in under.items():
            x = u.get(q)
            if not x or not np.isfinite(x['vol']) or x['vol'] <= 0:
                continue
            size = min(MAX_X, TARGET_VOL / x['vol'])
            fam.setdefault(lib.FAMILY[n], []).append(-x['bh'] * size if x['bh'] < 0 else 0.0)
        row['ideal_short_by_family'] = {f: float(np.mean(v)) for f, v in fam.items()}
        rows.append(row)
    # PnL by family and direction over the whole window (sum of daily contributions). P1 has no
    # short leg, so the direction split is 100% long by construction; it is reported anyway.
    by_family = {}
    for s, v in sleeves.items():
        f = lib.FAMILY[s.split('/')[1]] if s.startswith('R1') else 'cripto'
        by_family[f] = by_family.get(f, 0.0) + float(sum(v.values()))
    by_sleeve = {s: float(sum(v.values())) for s, v in sleeves.items()}
    return {'window': window, 'from': summary['from'], 'to': summary['to'],
            'summary': {k: summary[k] for k in ('cagr', 'max_dd', 'sharpe', 'months_pos', 'quarters_pos',
                                                'n_quarters', 'dsr', 'by_year')},
            'quarters': pq, 'target_quarters': rows, 'pnl_by_family_sum_daily': by_family,
            'pnl_by_sleeve_sum_daily': by_sleeve, 'direction': {'long': 1.0, 'short': 0.0}}


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    os.makedirs(lib.OUT, exist_ok=True)
    res = {'protocol': 'RESEARCH_HUB/revisions/20261025-r51/PROTOCOL_R51.md F2', 'n_added': 0,
           'windows': {w: run(w) for w in ('common', 'long')}}
    path = os.path.join(lib.OUT, 'f2_diagnosis.json')
    with open(path, 'w') as fh:
        json.dump(res, fh, indent=2, default=float)
    for w, r in res['windows'].items():
        s = r['summary']
        print(w, r['from'], r['to'], f"CAGR {s['cagr']:.4f} DD {s['max_dd']:.4f} Sharpe {s['sharpe']:.3f} "
              f"Q+ {s['quarters_pos']:.2f} targets {[t['quarter'] for t in r['target_quarters']]}")
    print(path)
    return 0


if __name__ == '__main__':
    sys.exit(main())
