"""r55 F1: crypto engine by regime, E1-E3 against P1 (registered before running, N 125 -> 128).

PROTOCOL_R55.md F1 plus the post-F0 amendment (97bbc3da). All windows cut at 2024-12-31:
* E1, C6 as the core: P1 without R1/BTC and R1/ETH, r50 F2 construction recomputed;
* E2: daily returns of R1/BTC and R1/ETH multiplied by the B-state scalar (bull 1, lateral 0.5,
  bear 0) before the R1 basket is rebuilt; C6 untouched; fees saved are ignored, as for r52 J1;
* E3: fixed-weight overlay on P1, a BTC short sleeve at -0.25 * 0.17 / sigma30 (cap 0.5x, r49
  25% band, taker) only while the B state is bear. Same BTC series as the regimes (spot before
  2020-10-15, perpetual after) with the BTC perpetual's real funding wherever it exists (from
  2019-09, so it is also charged over the last spot year: declared, conservative for a short only
  when funding is negative).

Gates (regime ones on the A quarterly labels from F0):
1 bear quarters, 2018-09+: sum >= P1's and median >= 0;
2 lateral quarters, 2018-09+: sum >= P1's and median >= 0; and 2021-24 sum > P1's (amendment);
3 bull quarters, 2018-09+: sum >= 80% of P1's;
4 r51 inclusion rule, Sharpe never down more than 0.05 in either window.
E3 instead: DD better by >= 1.5 pp in both windows, gate 1, dSharpe >= -0.05 in both, gate 3.
Monthly-label tables are reported next to the gates (informative, amendment point 2).

    python research_scripts/r55_engine.py run

writes research_scripts/data/r55/f1_engine.json.
"""
import json
import os
import sys

import numpy as np

import r50_engines as en
import r50_f1b as fb
import r50_f2 as f2
import r51_lib as lib
import r51_sleeves as sv
import r51_f6 as f6
import r55_regimes as rg
from r50_harness import T, O, C, H, L, DAY_MS
from r50_engines import simulate, calendar, daily_returns

N_DECLARED = 128
E2_SCALE = {'alcista': 1.0, 'lateral': 0.5, 'bajista': 0.0}
E3_SIZE, E3_CAP = 0.25, 0.5
BULL_KEEP = 0.8
DD_GAIN = 0.015
CLASSES = rg.CLASSES


def scaled_curve(cv, factor):
    """Curve whose return of day d is multiplied by factor(d) (state applied on day d)."""
    days, vals = cv
    r = np.diff(vals) / vals[:-1]
    f = np.array([factor(int(d)) for d in days[1:]])
    return days, en.BALANCE * np.r_[1.0, np.cumprod(1 + r * f)]


def portfolio(comps, start):
    """r50 F2 construction on comps trimmed to start and cut at CUT; (days, vals)."""
    cut = {k: rg.cut_to(f6.trim(v, start), rg.CUT_MS) for k, v in comps.items()}
    days, vals, _, _ = lib.portfolio_attr(cut, list(cut))
    assert lib._date(days[-1]) == rg.CUT
    return days, vals


def overlay(days, vals, hedge_cv):
    """Portfolio daily returns plus the hedge sleeve's daily return (fixed weight 1)."""
    h = daily_returns(*hedge_cv)
    r = vals[1:] / vals[:-1] - 1 + np.array([h.get(int(d), 0.0) for d in days[1:]])
    return days, en.BALANCE * np.r_[1.0, np.cumprod(1 + r)]


def e3_sleeve(t, c, st, start_ms):
    """BTC short sleeve on the regime BTC series; x set at the close of day i from the state
    computed at that close (key t_i + 1 day), held through day i + 1."""
    # Daily close-only bars (T, O, C, H, L, V): the sleeve rebalances at the close and has no stops.
    bars = np.zeros((len(t), 6))
    bars[:, T] = t
    bars[:, [O, C, H, L]] = c[:, None]
    vol = en.ann_vol(c, False)
    x = np.full(len(t), np.nan)
    for i in range(len(t)):
        s = st.get(int(t[i]) + DAY_MS)
        if s is None or not np.isfinite(vol[i]) or vol[i] <= 0:
            continue
        x[i] = max(-E3_CAP, -E3_SIZE * sv.TARGET_VOL / vol[i]) if s[0] == 'bajista' else 0.0
    ts, eq, acct = simulate(bars, start_ms, sv.continuous_decider(bars, x), 'BTC', True)
    return calendar(ts, eq, lib._date(start_ms), '2025-01-01'), len(acct.trades)


def quarter_rets(days, vals):
    q = lib.quarterly(days, vals)
    first = lib.quarter_of(days[1])
    if sum(lib.quarter_of(d) == first for d in days[1:]) < 30:
        q.pop(first, None)
    return q


def month_rets(days, vals):
    pm = {}
    for d, v in zip(days, vals):
        pm[lib._date(d)[:7]] = v
    mv = [vals[0]] + list(pm.values())
    return dict(zip(pm, (np.array(mv[1:]) / np.array(mv[:-1]) - 1).tolist()))


def by_class(rets, labs):
    out = {}
    for c in CLASSES:
        v = [r for p, r in rets.items() if p in labs and labs[p]['label'] == c]
        out[c] = {'n': len(v), 'sum': float(np.sum(v)) if v else 0.0,
                  'median': float(np.median(v)) if v else None, 'pos': int(sum(x > 0 for x in v))}
    return out


def evaluate(days, vals, qlab, mlab):
    f2.N_DECLARED = N_DECLARED
    m = f2.r9(days, vals, [])
    keys = ('from', 'to', 'cagr', 'max_dd', 'sharpe', 'quarters_pos', 'n_quarters', 'by_year', 'dsr')
    out = {k: m[k] for k in keys}
    out['q_pos_count'] = int(round(m['quarters_pos'] * m['n_quarters']))
    out['quarters'] = by_class(quarter_rets(days, vals), qlab)
    out['months'] = by_class(month_rets(days, vals), mlab)
    return out


def gates(name, base, cand):
    L, Cm = 'long', 'common'
    bq, cq = base[L]['quarters'], cand[L]['quarters']
    dl = cand[L]['sharpe'] - base[L]['sharpe']
    dc = cand[Cm]['sharpe'] - base[Cm]['sharpe']
    dq = cand[L]['q_pos_count'] - base[L]['q_pos_count']
    g = {
        'g1_bear': cq['bajista']['sum'] >= bq['bajista']['sum'] and (cq['bajista']['median'] or 0) >= 0,
        'g3_bull': cq['alcista']['sum'] >= BULL_KEEP * bq['alcista']['sum'],
    }
    if name == 'E3':
        g['dd_long'] = cand[L]['max_dd'] - base[L]['max_dd'] >= DD_GAIN
        g['dd_common'] = cand[Cm]['max_dd'] - base[Cm]['max_dd'] >= DD_GAIN
        g['dsharpe_ge_-0.05'] = dl >= -0.05 and dc >= -0.05
    else:
        g['g2_lateral'] = (cq['lateral']['sum'] >= bq['lateral']['sum'] and (cq['lateral']['median'] or 0) >= 0
                           and cand[Cm]['quarters']['lateral']['sum'] > base[Cm]['quarters']['lateral']['sum'])
        g['g4_inclusion'] = ((dl >= f6.DS_MIN or (dq >= 1 and dl >= 0)) and dc >= -f6.DS_COMMON_MAX_DROP
                             and dl >= -0.05)
    return {'gates': g, 'pass': bool(all(g.values())),
            'deltas': {'d_sharpe_long': dl, 'd_sharpe_common': dc, 'd_q_pos_long': dq,
                       'd_cagr_long': cand[L]['cagr'] - base[L]['cagr'],
                       'd_cagr_common': cand[Cm]['cagr'] - base[Cm]['cagr'],
                       'd_dd_long': cand[L]['max_dd'] - base[L]['max_dd'],
                       'd_dd_common': cand[Cm]['max_dd'] - base[Cm]['max_dd']}}


def run():
    t, c = rg.btc_daily()
    qlab, mlab = rg.labels_a(t, c), rg.labels_a(t, c, monthly=True)
    st = rg.states_b(t, c)

    def e2_factor(d):
        s = st.get(d)
        return 1.0 if s is None else E2_SCALE[s[0]]

    res = {'protocol': 'RESEARCH_HUB/revisions/20261026-r55/PROTOCOL_R55.md F1 + enmienda 97bbc3da',
           'n_declared': N_DECLARED, 'measured_through': rg.CUT, 'windows': {}, 'checks': {}}
    ev = {n: {} for n in ('P1', 'E1', 'E2', 'E3')}
    e3_trades = {}
    for w in ('long', 'common'):
        comps, _, extra = lib.p1_components(w)
        start = max(int(cv[0][0]) for cv in comps.values()) + DAY_MS
        r1 = extra['r1']
        assert np.allclose(fb.basket(r1, list(r1))[1], comps['R1'][1]), 'R1 basket not reproduced'
        pd_, pv = portfolio(comps, start)
        # Reproduction: E2 with scalar 1 in every state is P1.
        ident = {n: (scaled_curve(cv, lambda d: 1.0) if n in ('BTC', 'ETH') else cv) for n, cv in r1.items()}
        _, iv = portfolio({'R1': fb.basket(ident, list(ident)), 'C6': comps['C6']}, start)
        res['checks'][f'e2_identity_{w}'] = bool(np.allclose(iv, pv))
        assert res['checks'][f'e2_identity_{w}'], 'E2 identity does not reproduce P1'
        ev['P1'][w] = evaluate(pd_, pv, qlab, mlab)

        r1_nc = {n: cv for n, cv in r1.items() if n not in ('BTC', 'ETH')}
        e1 = {'R1': fb.basket(r1_nc, list(r1_nc)), 'C6': comps['C6']}
        ev['E1'][w] = evaluate(*portfolio(e1, start), qlab, mlab)

        r1_e2 = {n: (scaled_curve(cv, e2_factor) if n in ('BTC', 'ETH') else cv) for n, cv in r1.items()}
        e2 = {'R1': fb.basket(r1_e2, list(r1_e2)), 'C6': comps['C6']}
        ev['E2'][w] = evaluate(*portfolio(e2, start), qlab, mlab)

        hedge, ntr = e3_sleeve(t, c, st, int(pd_[0]))
        e3_trades[w] = ntr
        hd, hv = rg.cut_to(hedge, rg.CUT_MS)
        ev['E3'][w] = evaluate(*overlay(pd_, pv, (hd, hv)), qlab, mlab)
        ev['E3'][w]['hedge_sleeve'] = {'sharpe': f2.r9(hd, hv, [])['sharpe'], 'return': float(hv[-1] / hv[0] - 1),
                                       'rebalances': ntr}
    res['P1'] = ev['P1']
    for n in ('E1', 'E2', 'E3'):
        res[n] = {'metrics': ev[n], **gates(n, ev['P1'], ev[n])}
    out = os.path.join(rg.OUT, 'f1_engine.json')
    with open(out, 'w') as fh:
        json.dump(res, fh, indent=2, default=float)

    print('checks', res['checks'])
    for n in ('P1', 'E1', 'E2', 'E3'):
        for w in ('long', 'common'):
            m = ev[n][w]
            q = m['quarters']
            print(f"{n:3} {w:6} {m['from']}..{m['to']} CAGR {m['cagr']:.3f} DD {m['max_dd']:.3f} "
                  f"S {m['sharpe']:.3f} Q+ {m['q_pos_count']}/{m['n_quarters']} | "
                  + ' '.join(f"{k[:4]} {v['sum']:+.3f}/{(v['median'] or 0):+.3f}/{v['pos']}of{v['n']}"
                             for k, v in q.items()))
    for n in ('E1', 'E2', 'E3'):
        print(n, 'PASS' if res[n]['pass'] else 'no', res[n]['gates'],
              {k: round(v, 4) for k, v in res[n]['deltas'].items()})
    print(out)


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
