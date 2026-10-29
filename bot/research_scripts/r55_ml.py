"""r55 F2: ways to cash the X1 ranking (ML1-ML4), registered before running (N 128 -> 132).

PROTOCOL_R55.md F2 and the F2 implementation amendment (dad565de). The X1 score is r52's
(elastic net, walk-forward, unchanged); panel, costs and simulator are r52's (`r52_xs`).

* ML1: long the top 10 by X1 after excluding the week's top vol30 decile and the r53 tail filter,
  weights proportional to rank, 15% cap per coin (iterative, proportional redistribution), gross
  1.0, hedged with BTC only by the long basket's 60-day beta; weekly.
* ML2: ML1, flat while the B state at the rebalance close is bear.
* ML3: frozen C6 on the 48 U50 alts, an entry only if the coin is in that week's X1 top 10.
* ML4: frozen C6 on the 48 alts, risk per trade 1% * clip(1 + 2r, 0.5, 1.5), r the centred rank.
  ML3/ML4 replace half of C6's risk inside P1: C6' = 0.5 C6 + 0.5 alts * sigma_C6 / sigma_alts.

Development 2021-05..2023-12 (r52 dev), 2024 control, 2025 sealed: no metric past 2024-12-31.

    python research_scripts/r55_ml.py run

writes research_scripts/data/r55/f2_ml.json and f2_curves.npy.
"""
import json
import math
import os
import sys
import warnings

import numpy as np
import pandas as pd

import r50_engines as en
import r50_f1b as fb
import r50_f1c as fc
import r51_lib as lib
import r52_xs as xs
import r53_xs as y3
import r54_v1 as v1
import r55_regimes as rg
import r55_engine as eg
from r50_harness import T, DAY_MS

N_DECLARED = 132
TOP_K = 10
CAP = 0.15
VOL_DECILE = 0.90
BETA_DAYS = 60
SIGMA_MIN_DAYS = 90
TOP5_MAX = 0.60
ALT_GAIN = 0.10


# ----------------------------------------------------------------------------------------------
# ML1 / ML2 books
# ----------------------------------------------------------------------------------------------
def cap_weights(w, cap):
    """Iteratively clip weights at cap and hand the excess to the uncapped ones, proportionally."""
    w = dict(w)
    for _ in range(50):
        over = {s: x for s, x in w.items() if x > cap + 1e-12}
        if not over:
            break
        excess = sum(x - cap for x in over.values())
        free = {s: x for s, x in w.items() if x < cap - 1e-12}
        for s in over:
            w[s] = cap
        tot = sum(free.values())
        if tot <= 0:
            break
        for s, x in free.items():
            w[s] = x + excess * x / tot
    return w


def ml_weights(S, score, lr, st=None):
    out = {}
    for k, g in S.assign(score=score).dropna(subset=['score']).groupby('k'):
        d = g['day'].iloc[0]
        g = g[g['vol30_raw'].fillna(g['vol30_raw'].median()) <= g['vol30_raw'].quantile(VOL_DECILE)]
        g = g[y3.tail_ok(g)]
        if len(g) < xs.MIN_ELIGIBLE:
            continue
        if st is not None:
            s = st.get(int(d.value // 10**6) + DAY_MS)
            if s is not None and s[0] == 'bajista':
                out[k] = (d, {})
                continue
        top = g.sort_values('score').tail(TOP_K)
        r = top['score'].rank()
        longw = cap_weights({s: float(x / r.sum()) for s, x in zip(top['sym'], r)}, CAP)
        hist = lr.loc[:d].tail(BETA_DAYS)
        lb = sum(hist[s].fillna(0) * x for s, x in longw.items())
        btc = hist['BTCUSDT']
        beta = float(np.cov(lb, btc)[0, 1] / btc.var()) if btc.var() > 0 else 1.0
        w = dict(longw)
        w['BTCUSDT'] = w.get('BTCUSDT', 0.0) - beta
        out[k] = (d, w)
    return out


def period_rets(r, monthly=False):
    """Compounded return per calendar quarter (or month) of a daily series; partial periods
    with fewer than 30 (10) days are dropped."""
    key = r.index.strftime('%Y-%m') if monthly else [f'{t.year}Q{(t.month - 1) // 3 + 1}' for t in r.index]
    g = (1 + r).groupby(np.asarray(key))
    n = g.size()
    out = (g.prod() - 1)[n >= (10 if monthly else 30)]
    return {str(p): float(v) for p, v in out.items()}


def book_eval(name, w, S_old, score, lr, st, C, F, p1, qlab, mlab):
    r = xs.simulate(w, C, F)
    dev = r[r.index <= pd.Timestamp(xs.DEV_END, tz='UTC')]
    dev = dev[dev.index >= dev[dev != 0].index[0]] if (dev != 0).any() else dev
    old = xs.simulate(ml_weights(S_old, score.loc[S_old.index], lr, st), C, F)
    wk = (1 + dev).resample('W-SUN').prod() - 1
    tot = float(wk.sum())
    top5 = float(wk.nlargest(5).sum() / tot) if tot > 0 else float('inf')
    v = {'dev': xs.stats(r, '2020-01-01', xs.DEV_END), 'dev_cost2': xs.stats(xs.simulate(w, C, F, 2.0), '2020-01-01', xs.DEV_END),
         'val2024': xs.stats(r, '2024-01-01', xs.VAL_END), 'old20_dev': xs.stats(old, '2020-01-01', xs.DEV_END),
         'rho_p1_dev': xs.rho(r, p1, xs.DEV_END), 'top5_weeks_share': top5,
         'quarters_dev': eg.by_class(period_rets(dev), qlab), 'months_dev': eg.by_class(period_rets(dev, True), mlab),
         'weeks_flat': int(sum(1 for _, x in w.values() if not x)),
         'avg_hedge_btc': float(np.mean([x.get('BTCUSDT', 0.0) for _, x in w.values() if x]))}
    q = v['quarters_dev']
    v['gates'] = {'sharpe_ge_0_5': v['dev']['sharpe'] >= 0.5, 'cost2_pos': v['dev_cost2']['sharpe'] > 0,
                  'rho_le_0_3': v['rho_p1_dev'] is not None and v['rho_p1_dev'] <= 0.3,
                  'val2024_pos': v['val2024'] is not None and v['val2024']['sharpe'] > 0,
                  'old20_pos': v['old20_dev'] is not None and v['old20_dev']['sharpe'] > 0,
                  'bear_sum_ge_0': q['bajista']['sum'] >= 0, 'lateral_sum_ge_0': q['lateral']['sum'] >= 0,
                  'top5_lt_0_6': top5 < TOP5_MAX}
    v['pass'] = bool(all(v['gates'].values()))
    return v, r


# ----------------------------------------------------------------------------------------------
# ML3 / ML4: C6 on the alts with an entry multiplier
# ----------------------------------------------------------------------------------------------
def score_table(S, score):
    """Week start (Monday 00:00 UTC, ms) array and {(week index, sym): (in_top10, centred rank)}."""
    starts, tab = [], {}
    for j, (k, g) in enumerate(S.assign(score=score).dropna(subset=['score']).groupby('k')):
        starts.append(int(g['day'].iloc[0].value // 10**6) + DAY_MS)
        top = set(g.sort_values('score').tail(TOP_K)['sym'])
        rk = g['score'].rank(pct=True) - 0.5
        for s, r in zip(g['sym'], rk):
            tab[(j, s)] = (s in top, float(r))
    return np.array(starts, dtype=np.int64), tab


def make_mult(kind, starts, tab):
    def mult(sym, ts):
        j = int(np.searchsorted(starts, ts, side='right')) - 1
        hit = tab.get((j, sym)) if j >= 0 else None
        if kind == 'id':
            return 1.0
        if kind == 'ML3':
            return 1.0 if hit and hit[0] else 0.0
        return 1.0 if hit is None else float(np.clip(1 + 2 * hit[1], 0.5, 1.5))
    return mult


def c6_alts(mult):
    """r54 V1 loop with risk_qty scaled at entry by mult(sym, fill bar close ts)."""
    uni = [u['symbol'] for u in json.load(open(os.path.join(v1.DATA, 'universe50.json')))]
    alts = [s for s in uni if s not in ('BTCUSDT', 'ETHUSDT')]
    orig = fb.risk_qty
    curves, n_trades = {}, 0
    try:
        for sym in alts:
            bars, h1 = v1.h4_bars(sym)
            start = max(v1.SIM_FROM, int(bars[min(v1.WARM_BARS, len(bars) - 1), T]))
            if start >= en.hz._ms(v1.MEASURE[1]):
                continue
            frm = lib._date(start)
            sleeves = []
            for retest in (False, True):
                dec = fb.r2_r3_decider(bars, retest)
                ctx = {'ts': 0}

                def wrapped(i, acct, ts, dec=dec, ctx=ctx):
                    ctx['ts'] = ts
                    return dec(i, acct, ts)
                fb.risk_qty = (lambda acct, price, dist, ctx=ctx, sym=sym:
                               orig(acct, price, dist) * mult(sym, ctx['ts']))
                ts, eq, acct = v1.simulate(bars, start, wrapped, v1.funding_cursor(sym, h1, int(bars[0, T])))
                n_trades += len(acct.trades)
                sleeves.append(en.calendar(ts, eq, frm, '2026-01-01'))
            curves[sym] = fc.mean_curve(sleeves)
    finally:
        fb.risk_qty = orig
    return curves, n_trades


def alt_basket(curves):
    meas = {s: v1.trim(cv, v1.MEASURE[1]) for s, cv in curves.items()}
    return fb.basket(meas, list(meas))


def c6_prime(c6, alts, alts_from):
    """C6' = 0.5 C6 + 0.5 alts * sigma_C6 / sigma_alts (expanding daily std at the previous month
    end, >= SIGMA_MIN_DAYS of alts since alts_from); C6 alone before that."""
    rc, ra = en.daily_returns(*c6), en.daily_returns(*alts)
    days = c6[0]
    out, scales, month, scale = [], [], None, None
    for d in days[1:]:
        d = int(d)
        m = lib._date(d)[:7]
        if m != month:
            month = m
            hist = [x for x in rc if x < d]
            ha = [x for x in ra if alts_from <= x < d]
            scale = None
            if len(ha) >= SIGMA_MIN_DAYS:
                sa = np.std([ra[x] for x in ha], ddof=1)
                sc = np.std([rc[x] for x in hist], ddof=1)
                scale = sc / sa if sa > 0 else None
            if scale is not None:
                scales.append(scale)
        r = rc.get(d, 0.0)
        out.append(r if scale is None or d not in ra else 0.5 * r + 0.5 * ra[d] * scale)
    vals = en.BALANCE * np.r_[1.0, np.cumprod(1 + np.array(out))]
    return (days, vals), scales


def run():
    warnings.simplefilter('ignore')
    os.makedirs(rg.OUT, exist_ok=True)
    eg.N_DECLARED = N_DECLARED
    t, c = rg.btc_daily()
    qlab, mlab = rg.labels_a(t, c), rg.labels_a(t, c, monthly=True)
    st = rg.states_b(t, c)

    C, Q, I, F = xs.load_panel()
    feats, lr = xs.features(C, Q, I)
    elig = xs.eligibility(C, Q)
    S, names = xs.weekly_samples(C, feats, elig)
    S = y3.add_raw(S, feats, Q)
    x1 = xs.predict_walk_forward(S, names, 'en')
    # Reproduction: X1's dev IC must equal r52's.
    d = S.assign(score=x1).dropna(subset=['score', 'target'])
    d = d[d['day'] <= pd.Timestamp(xs.DEV_END, tz='UTC')]
    ic = d.groupby('k').apply(lambda g: g['score'].corr(g['target'], method='spearman'))
    ic_r52 = json.load(open(os.path.join(xs.DATA, 'xs.json')))['trials']['X1']['ic_dev_mean']
    res = {'protocol': 'RESEARCH_HUB/revisions/20261026-r55/PROTOCOL_R55.md F2 + enmienda dad565de',
           'n_declared': N_DECLARED, 'measured_through': rg.CUT,
           'checks': {'x1_ic_dev': float(ic.mean()), 'x1_ic_dev_r52': ic_r52}}
    assert abs(ic.mean() - ic_r52) < 1e-9, 'X1 score not reproduced'

    p1 = xs.p1_returns()
    old20 = [s for s in C.columns if C[s].first_valid_index() <= pd.Timestamp('2020-07-01', tz='UTC')][:20]
    S_old = S[S['sym'].isin(old20)]
    curves = {}
    for name, stt in (('ML1', None), ('ML2', st)):
        w = ml_weights(S, x1, lr, stt)
        v, r = book_eval(name, w, S_old, x1, lr, stt, C, F, p1, qlab, mlab)
        res[name], curves[name] = v, (r.index.asi8 // 10**6, r.values)
        print(name, 'PASS' if v['pass'] else 'no', v['gates'],
              {k: round(v[k]['sharpe'], 3) for k in ('dev', 'dev_cost2', 'val2024', 'old20_dev') if v[k]},
              'cagr', round(v['dev']['cagr'], 3), 'dd', round(v['dev']['max_dd'], 3), 'rho', v['rho_p1_dev'],
              'top5', round(v['top5_weeks_share'], 3), 'flat', v['weeks_flat'])

    starts, tab = score_table(S, x1)
    first_score = int(starts[0])
    res['first_score_week'] = lib._date(first_score)
    id_curves, n_id = c6_alts(make_mult('id', starts, tab))
    saved = np.load(os.path.join(v1.DATA, 'v1_curves.npy'), allow_pickle=True).item()
    same = all(np.allclose(id_curves[s][1], saved[s][1]) for s in saved) and set(saved) == set(id_curves)
    res['checks']['v1_identity'] = bool(same)
    assert same, 'C6 alts identity does not reproduce V1'
    v1_b = alt_basket(id_curves)
    m_v1 = en.metrics(v1_b[0], v1_b[1], [], res['first_score_week'])

    base = {}
    for w in ('long', 'common'):
        comps, _, _ = lib.p1_components(w)
        start = max(int(cv[0][0]) for cv in comps.values()) + DAY_MS
        base[w] = (comps, start, eg.evaluate(*eg.portfolio(comps, start), qlab, mlab))
    res['P1'] = {w: base[w][2] for w in base}
    for name in ('ML3', 'ML4'):
        cur, ntr = c6_alts(make_mult(name, starts, tab))
        b = alt_basket(cur)
        m = en.metrics(b[0], b[1], [], res['first_score_week'])
        ev, scales = {}, []
        for w in ('long', 'common'):
            comps, start, _ = base[w]
            c6p, sc = c6_prime(comps['C6'], b, first_score)
            scales += sc
            ev[w] = eg.evaluate(*eg.portfolio({'R1': comps['R1'], 'C6': c6p}, start), qlab, mlab)
        gt = eg.gates(name, res['P1'], ev)
        gt['gates']['alt_basket_ge_v1_plus_0_1'] = m['sharpe'] >= m_v1['sharpe'] + ALT_GAIN
        gt['pass'] = bool(all(gt['gates'].values()))
        res[name] = {'metrics': ev, 'alt_basket': {k: m[k] for k in ('from', 'to', 'sharpe', 'cagr', 'max_dd')},
                     'v1_basket_same_window': {k: m_v1[k] for k in ('from', 'to', 'sharpe', 'cagr', 'max_dd')},
                     'trades': ntr, 'trades_v1': n_id,
                     'scale_c6_over_alts': {'min': float(min(scales)), 'median': float(np.median(scales)),
                                            'max': float(max(scales))} if scales else None, **gt}
        curves[name] = b
        print(name, 'PASS' if gt['pass'] else 'no', gt['gates'], {k: round(x, 4) for k, x in gt['deltas'].items()},
              'alts', round(m['sharpe'], 3), 'v1', round(m_v1['sharpe'], 3), 'trades', ntr, '/', n_id)
        for w in ('long', 'common'):
            e = ev[w]
            print('  ', w, f"CAGR {e['cagr']:.3f} DD {e['max_dd']:.3f} S {e['sharpe']:.3f} Q+ {e['q_pos_count']}/{e['n_quarters']}",
                  {k: (round(x['sum'], 3), round(x['median'] or 0, 4), x['pos'], x['n']) for k, x in e['quarters'].items()})
    path = os.path.join(rg.OUT, 'f2_ml.json')
    with open(path, 'w') as fh:
        json.dump(res, fh, indent=2, default=float)
    np.save(os.path.join(rg.OUT, 'f2_curves.npy'), curves, allow_pickle=True)
    print('checks', res['checks'])
    print(path)


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
