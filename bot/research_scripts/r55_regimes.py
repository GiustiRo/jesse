"""r55 F0: BTC regimes and the descriptive map of P1 by regime (no trial, N unchanged).

PROTOCOL_R55.md F0, one common parameter k = 0.5, BTC spot up to 2020-10-15 and perpetual after:
* A, evaluation label (ex post, quarterly): r_q = simple close-to-close BTC return of the calendar
  quarter; u_q = k * sigma_a * sqrt(0.25), sigma_a = std of the daily log returns of the 365 days
  before the quarter's first day, annualised with sqrt(365); bull if r_q >= +u_q, bear if
  r_q <= -u_q, lateral otherwise. Monthly sensitivity with sqrt(1/12), reported, never decisive;
* B, tradable state (causal, daily): T90 = ln(P_t / P_t-90) / (sigma_d * sqrt(90)) with sigma_d the
  std of the same 90 daily log returns; bull if T90 >= +0.5, bear if <= -0.5, lateral otherwise;
  computed at the UTC daily close and applied from the next day, no hysteresis.

Allowed description (all cut at 2024-12-31, 2025 stays sealed): the A labels and B states, the
confusion between the two layers, and P1's attribution by A quarter class (r51 F2 method). P1's
return split by B state is deliberately NOT computed: scaling R1 crypto by B state is trial E2, so
that split would reveal E2's result before it is registered.

    python research_scripts/r55_regimes.py run

writes research_scripts/data/r55/f0_regimes.json and f0_states.npy (day, applied B state).
"""
import json
import math
import os
import sys

import numpy as np
import pandas as pd

import r50_engines as en
import r50_f2 as f2
import r51_lib as lib
import r51_sleeves as sv
import r51_f6 as f6
from r50_harness import T, C, DAY_MS
from r50_engines import daily_returns

OUT = os.path.join(lib.HERE, 'data', 'r55')
K = 0.5
T90_DAYS = 90
SIGMA_A_DAYS = 365
PERP_FROM = '2020-10-15'
CUT = '2024-12-31'
CUT_MS = int(pd.Timestamp(CUT, tz='UTC').value // 10**6)
N_DECLARED = 125
CLASSES = ('alcista', 'bajista', 'lateral')
# P1 components grouped as in the protocol's attribution: R1 crypto per coin, C6, gold, SPX, rest.
GROUPS = {'R1/BTC': 'R1/BTC', 'R1/ETH': 'R1/ETH', 'C6/BTC': 'C6', 'C6/ETH': 'C6', 'R1/XAU': 'R1/oro',
          'R1/SPX': 'R1/SPX'}


def ms(day):
    return int(pd.Timestamp(day, tz='UTC').value // 10**6)


def btc_daily():
    """Day stamps (bar open) and closes: spot before PERP_FROM, perpetual from it, cut at CUT."""
    spot, perp = sv.daily('BTC', 'spot'), sv.daily('BTC', 'perp')
    p0 = ms(PERP_FROM)
    bars = np.vstack([spot[spot[:, T] < p0], perp[perp[:, T] >= p0]])
    bars = bars[bars[:, T] <= CUT_MS]
    t, c = bars[:, T].astype(np.int64), bars[:, C].astype(float)
    assert (np.diff(t) > 0).all() and t[-1] <= CUT_MS, 'BTC series out of order or past the cut'
    return t, c


def period_of(t, monthly):
    d = lib._date(t)
    return d[:7] if monthly else lib.quarter_of(t)


def labels_a(t, c, monthly=False):
    """Period -> {r, u, sigma_a, label}; a period needs a full prior period and 365 prior returns."""
    lr = np.r_[np.nan, np.diff(np.log(c))]
    per = np.array([period_of(x, monthly) for x in t])
    out = {}
    starts = [i for i in range(1, len(t)) if per[i] != per[i - 1]]
    scale = math.sqrt(1 / 12) if monthly else math.sqrt(0.25)
    for a, b in zip(starts, starts[1:] + [len(t)]):
        if a - 1 < SIGMA_A_DAYS:
            continue
        if b == len(t) and lib._date(t[-1]) != CUT:
            continue
        sig = float(np.std(lr[a - SIGMA_A_DAYS:a], ddof=1) * math.sqrt(365))
        r = float(c[b - 1] / c[a - 1] - 1)  # close of the period's last day vs prior period's last
        u = K * sig * scale
        lab = 'alcista' if r >= u else 'bajista' if r <= -u else 'lateral'
        out[per[a]] = {'r': r, 'u': u, 'sigma_a': sig, 'label': lab}
    return out


def states_b(t, c):
    """Applied day -> state; the T90 known at the close of day t applies to day t + 1."""
    lc = np.log(c)
    lr = np.r_[np.nan, np.diff(lc)]
    st = {}
    for i in range(T90_DAYS, len(t)):
        sd = float(np.std(lr[i - T90_DAYS + 1:i + 1], ddof=1))
        t90 = (lc[i] - lc[i - T90_DAYS]) / (sd * math.sqrt(T90_DAYS))
        s = 'alcista' if t90 >= K else 'bajista' if t90 <= -K else 'lateral'
        st[int(t[i]) + DAY_MS] = (s, float(t90))
    return st


def cut_to(cv, last_ms):
    days, vals = cv
    k = days <= last_ms
    return days[k], vals[k]


def p1_attribution(window, qlab, mlab):
    """P1 cut at CUT (r52 J1 cut), per-component daily contributions as in r51 F2."""
    comps, _, extra = lib.p1_components(window)
    start = max(int(cv[0][0]) for cv in comps.values()) + DAY_MS
    cut = {k: cut_to(f6.trim(v, start), CUT_MS) for k, v in comps.items()}
    days, vals, contrib, used = lib.portfolio_attr(cut, ['R1', 'C6'])
    assert lib._date(days[-1]) == CUT and used[-1] <= CUT_MS
    f2.N_DECLARED = N_DECLARED
    summ = f2.r9(days, vals, [])
    sleeves = {}
    for fam, key in (('R1', 'r1'), ('C6', 'c6')):
        rs = {n: daily_returns(*cv) for n, cv in extra[key].items()}
        for j, d in enumerate(used):
            avail = [n for n in rs if d in rs[n]]
            basket_r = np.mean([rs[n][d] for n in avail]) if avail else 0.0
            scale = contrib[fam][j] / basket_r if basket_r else 0.0
            for n in avail:
                sleeves.setdefault(f'{fam}/{n}', {})[d] = scale * rs[n][d] / len(avail)
    groups = {}
    for s, v in sleeves.items():
        g = GROUPS.get(s, 'resto R1')
        for d, x in v.items():
            groups.setdefault(g, {}).setdefault(d, 0.0)
            groups[g][d] += x

    def by_class(per_fn, labs, ret):
        rows = {c: {'n': 0, 'periods': [], 'p1_sum': 0.0, 'p1_median': None, 'p1_pos': 0, 'groups': {}}
                for c in CLASSES}
        vals_by = {c: [] for c in CLASSES}
        for p, r in ret.items():
            if p not in labs:
                continue
            c = labs[p]['label']
            rows[c]['n'] += 1
            rows[c]['periods'].append(p)
            rows[c]['p1_sum'] += r
            rows[c]['p1_pos'] += int(r > 0)
            vals_by[c].append(r)
        for c in CLASSES:
            if vals_by[c]:
                rows[c]['p1_median'] = float(np.median(vals_by[c]))
                rows[c]['p1_mean'] = float(np.mean(vals_by[c]))
            ps = set(rows[c]['periods'])
            rows[c]['groups'] = {g: float(sum(x for d, x in v.items() if per_fn(d) in ps))
                                 for g, v in groups.items()}
        return rows

    pq = lib.quarterly(days, vals)
    # A stub first quarter (2018Q3 is one day long in the long window) is excluded, as in r51 F2.
    first_q = lib.quarter_of(start)
    if sum(lib.quarter_of(d) == first_q for d in used) < 30:
        pq.pop(first_q, None)
    pm = {}
    for d, v in zip(days, vals):
        pm[lib._date(d)[:7]] = v
    mv = [vals[0]] + list(pm.values())
    pmr = dict(zip(pm, (np.array(mv[1:]) / np.array(mv[:-1]) - 1).tolist()))
    return {'from': summ['from'], 'to': summ['to'],
            'summary': {k: summ[k] for k in ('cagr', 'max_dd', 'sharpe', 'quarters_pos', 'n_quarters')},
            'quarter_returns': pq,
            'by_quarter_class': by_class(lib.quarter_of, qlab, pq),
            'by_month_class_sensitivity': by_class(lambda d: lib._date(d)[:7], mlab, pmr),
            'group_totals': {g: float(sum(v.values())) for g, v in groups.items()}}


def run():
    os.makedirs(OUT, exist_ok=True)
    t, c = btc_daily()
    qlab, mlab = labels_a(t, c), labels_a(t, c, monthly=True)
    st = states_b(t, c)
    eval_from = ms('2018-09-01')
    q_in = {q: v for q, v in qlab.items() if q >= '2018Q4'}
    m_in = {m: v for m, v in mlab.items() if m >= '2018-09'}

    # B states from 2018-09-01 through CUT: shares by year, switches, confusion with A.
    days_b = sorted(d for d in st if eval_from <= d <= CUT_MS)
    seq = [st[d][0] for d in days_b]
    years = sorted({lib._date(d)[:4] for d in days_b})
    share = {y: {s: float(np.mean([st[d][0] == s for d in days_b if lib._date(d)[:4] == y])) for s in CLASSES}
             for y in years}
    switches = int(sum(a != b for a, b in zip(seq[:-1], seq[1:])))
    conf = {}
    for a in CLASSES:
        dd = [d for d in days_b if q_in.get(lib.quarter_of(d), {}).get('label') == a]
        conf[a] = {'days': len(dd), **{b: (float(np.mean([st[d][0] == b for d in dd])) if dd else None)
                                       for b in CLASSES}}
    np.save(os.path.join(OUT, 'f0_states.npy'),
            np.array([(d, CLASSES.index(st[d][0]), st[d][1]) for d in sorted(st)]))

    out = {'protocol': 'RESEARCH_HUB/revisions/20261026-r55/PROTOCOL_R55.md F0', 'n_added': 0,
           'n_declared': N_DECLARED, 'k': K, 'measured_through': CUT,
           'btc_series': {'spot_until': PERP_FROM, 'perp_from': PERP_FROM, 'first': lib._date(t[0]),
                          'last': lib._date(t[-1])},
           'labels_quarterly': q_in,
           'label_counts_quarterly': {s: sum(v['label'] == s for v in q_in.values()) for s in CLASSES},
           'label_counts_monthly': {s: sum(v['label'] == s for v in m_in.values()) for s in CLASSES},
           'labels_monthly': m_in,
           'states_b': {'from': lib._date(days_b[0]), 'to': lib._date(days_b[-1]), 'switches': switches,
                        'share_total': {s: float(np.mean([x == s for x in seq])) for s in CLASSES},
                        'share_by_year': share},
           'confusion_b_given_a': conf,
           'p1': {w: p1_attribution(w, qlab, mlab) for w in ('long', 'common')}}
    path = os.path.join(OUT, 'f0_regimes.json')
    with open(path, 'w') as fh:
        json.dump(out, fh, indent=2, default=float)

    print('A quarterly:', out['label_counts_quarterly'], 'monthly:', out['label_counts_monthly'])
    for q, v in q_in.items():
        print(f"  {q} r {v['r']:+.3f} u {v['u']:.3f} {v['label']}")
    print('B:', out['states_b']['share_total'], 'switches', switches)
    print('confusion B|A:', json.dumps(conf))
    for w, p in out['p1'].items():
        s = p['summary']
        print(w, p['from'], p['to'], f"CAGR {s['cagr']:.4f} DD {s['max_dd']:.4f} Sharpe {s['sharpe']:.3f}")
        for cl, r in p['by_quarter_class'].items():
            print(f"  {cl}: n {r['n']} sum {r['p1_sum']:+.3f} med {r['p1_median']} pos {r['p1_pos']}",
                  {g: round(x, 4) for g, x in r['groups'].items()})
    print(path)


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
