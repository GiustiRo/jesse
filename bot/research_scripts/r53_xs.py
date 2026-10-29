"""r53 F1: tail-robust portfolios on the r52 ranker, weekly reversal and the QOI feature (Y1-Y6).

PROTOCOL_R53.md (4fb64775). The panel, features, eligibility, walk-forward, costs and
simulator are r52's (`r52_xs`, unchanged); only the portfolio construction (Y1-Y4), the score
(Y5) and the feature set or target (Y3, Y6) change, one at a time.

* Tail filter: coins whose |1-week return| is above the week's cross-sectional 90th percentile
  are left out of the formation (the short-leg blow-ups that cancel X1's rank IC).
* Rank weights: weight proportional to the centred rank, gross 1.0 (0.5 per side).
* Y2 holds 4 staggered sub-portfolios, each rebalanced every 4 weeks with 1/4 of the capital.
* 2025 sealed: curves are saved through 2025, metrics stop at 2024-12-31.

    python research_scripts/r53_xs.py run [Y6]

writes data/r52/r53_xs.json and data/r52/r53_xs_curves.npy (Y6 into r53_xs_y6.json).
"""
import json
import math
import os
import sys
import warnings

import numpy as np
import pandas as pd

import r52_xs as xs

DATA = xs.DATA
TAIL_PCT = 0.90
REV_TOP = 25
X1_DEV_SHARPE = None   # read from r52's xs.json at run time


def add_raw(S, feats, Q):
    """Raw 1-week return and 30-day median volume next to each (week, symbol) row."""
    med = Q.rolling(30, min_periods=20).median()
    S = S.copy()
    S['raw_ret1w'] = [feats['ret1w'].at[d, s] for d, s in zip(S['day'], S['sym'])]
    S['qvol_med'] = [med.at[d, s] for d, s in zip(S['day'], S['sym'])]
    return S


def tail_ok(g):
    a = g['raw_ret1w'].abs()
    return a <= a.quantile(TAIL_PCT)


def rank_ls(g, score):
    r = score.rank(pct=True)
    r = r - r.mean()
    tot = r.abs().sum()
    return {} if tot <= 0 else {s: float(x / tot) for s, x in zip(g['sym'], r)}


def weights_rank(S, score, tail=True, top=None):
    out = {}
    for k, g in S.assign(score=score).dropna(subset=['score']).groupby('k'):
        if top is not None:
            g = g.sort_values('qvol_med', ascending=False).head(top)
        if tail:
            g = g[tail_ok(g)]
        if len(g) < xs.MIN_ELIGIBLE:
            continue
        out[k] = (g['day'].iloc[0], rank_ls(g, g['score']))
    return out


def weights_long_hedged(S, score, lr):
    out = {}
    for k, g in S.assign(score=score).dropna(subset=['score']).groupby('k'):
        g = g[tail_ok(g)]
        if len(g) < xs.MIN_ELIGIBLE:
            continue
        q = max(1, int(math.ceil(len(g) / 5)))
        top = g.sort_values('score').tail(q)
        r = top['score'].rank()
        longw = {s: float(x / r.sum()) for s, x in zip(top['sym'], r)}
        d = g['day'].iloc[0]
        hist = lr.loc[:d].tail(60)
        lb = sum(hist[s].fillna(0) * x for s, x in longw.items())
        bench = (hist['BTCUSDT'] + hist['ETHUSDT']) / 2
        beta = float(np.cov(lb, bench)[0, 1] / bench.var()) if bench.var() > 0 else 1.0
        w = dict(longw)
        for h in ('BTCUSDT', 'ETHUSDT'):
            w[h] = w.get(h, 0) - beta / 2
        out[k] = (d, w)
    return out


def staggered(weekly, n=4):
    """n sub-portfolios, sub j re-forms on weeks with index % n == j and holds n weeks."""
    ks = sorted(weekly)
    subs = [dict() for _ in range(n)]
    out = {}
    for j, k in enumerate(ks):
        subs[j % n] = weekly[k][1]
        tot = {}
        for sub in subs:
            for s, x in sub.items():
                tot[s] = tot.get(s, 0) + x / n
        out[k] = (weekly[k][0], tot)
    return out


def evaluate(name, weights, C, F, p1, extra=None):
    r = xs.simulate(weights, C, F)
    r2 = xs.simulate(weights, C, F, 2.0)
    turn = np.mean([sum(abs(weights[b][1].get(s, 0) - weights[a][1].get(s, 0))
                        for s in set(weights[a][1]) | set(weights[b][1]))
                    for a, b in zip(sorted(weights)[:-1], sorted(weights)[1:])])
    v = {'dev': xs.stats(r, '2020-01-01', xs.DEV_END), 'dev_cost2': xs.stats(r2, '2020-01-01', xs.DEV_END),
         'val2024': xs.stats(r, '2024-01-01', xs.VAL_END), 'rho_p1_dev': xs.rho(r, p1, xs.DEV_END),
         'weekly_turnover': float(turn)}
    if extra:
        v.update(extra)
    g = {'sharpe_ge_0_5': v['dev']['sharpe'] >= 0.5, 'cost2_pos': v['dev_cost2']['sharpe'] > 0,
         'rho_le_0_3': v['rho_p1_dev'] is not None and v['rho_p1_dev'] <= 0.3,
         'val2024_pos': v['val2024'] is not None and v['val2024']['sharpe'] > 0}
    if name != 'Y5':
        g['beats_x1_0_2'] = v['dev']['sharpe'] - X1_DEV_SHARPE >= 0.2
    v['gates'] = g
    v['pass'] = all(g.values())
    return v, r


def qoi_weekly(C):
    """7- and 30-day mean of the quarter-hour opening imbalance per symbol, daily index."""
    q7, q30 = {}, {}
    for s in C.columns:
        p = os.path.join(DATA, f'{s}_q15.npy')
        if not os.path.exists(p):
            continue
        a = np.load(p)
        if not len(a):
            continue
        df = pd.DataFrame(a, columns=['t', 'ov', 'otb', 'v', 'c'])
        df['day'] = pd.to_datetime(df['t'], unit='ms', utc=True).dt.floor('D')
        g = df.groupby('day')
        daily = (2 * g['otb'].sum() - g['ov'].sum()) / g['ov'].sum().replace(0, np.nan)
        daily = daily.reindex(C.index)
        q7[s], q30[s] = daily.rolling(7, min_periods=4).mean(), daily.rolling(30, min_periods=15).mean()
    return pd.DataFrame(q7).reindex(columns=C.columns), pd.DataFrame(q30).reindex(columns=C.columns)


def run(only_y6=False):
    global X1_DEV_SHARPE
    X1_DEV_SHARPE = json.load(open(os.path.join(DATA, 'xs.json')))['trials']['X1']['dev']['sharpe']
    warnings.simplefilter('ignore')
    C, Q, I, F = xs.load_panel()
    feats, lr = xs.features(C, Q, I)
    elig = xs.eligibility(C, Q)
    p1 = xs.p1_returns()
    res, curves = {'x1_dev_sharpe_r52': X1_DEV_SHARPE, 'trials': {}}, {}
    if only_y6:
        q7, q30 = qoi_weekly(C)
        feats = dict(feats, qoi7=q7, qoi30=q30)
        S, names = xs.weekly_samples(C, feats, elig)
        S = add_raw(S, feats, Q)
        sc = xs.predict_walk_forward(S, names, 'en')
        v, r = evaluate('Y6', weights_rank(S, sc), C, F, p1, {'features': names})
        res['trials']['Y6'], curves['Y6'] = v, r
        out_json, out_npy = 'r53_xs_y6.json', 'r53_xs_y6_curves.npy'
    else:
        S, names = xs.weekly_samples(C, feats, elig)
        S = add_raw(S, feats, Q)
        x1 = xs.predict_walk_forward(S, names, 'en')
        live = x1.notna()
        y1w = weights_rank(S, x1)
        for name, w in (('Y1', y1w), ('Y2', staggered(y1w)), ('Y4', weights_long_hedged(S, x1, lr))):
            v, r = evaluate(name, w, C, F, p1)
            res['trials'][name], curves[name] = v, r
        # Y3: risk-adjusted target, same features and walk-forward.
        S3 = S.copy()
        S3['target'] = S3['fwd'] / S3['vol30_raw'].replace(0, np.nan)
        S3['target'] = S3.groupby('k')['target'].rank(pct=True) - 0.5
        y3 = xs.predict_walk_forward(S3, names, 'en')
        v, r = evaluate('Y3', weights_rank(S3, y3), C, F, p1)
        res['trials']['Y3'], curves['Y3'] = v, r
        # Y5: weekly reversal among the 25 most liquid eligible coins, only on weeks the ML
        # trials trade, so every trial covers the same period.
        rev = (-S['raw_ret1w']).where(live)
        v, r = evaluate('Y5', weights_rank(S, rev, tail=False, top=REV_TOP), C, F, p1)
        res['trials']['Y5'], curves['Y5'] = v, r
        out_json, out_npy = 'r53_xs.json', 'r53_xs_curves.npy'
    json.dump(res, open(os.path.join(DATA, out_json), 'w'), indent=1, default=float)
    np.save(os.path.join(DATA, out_npy), {k: (v.index.asi8 // 10**6, v.values) for k, v in curves.items()},
            allow_pickle=True)
    for t, v in res['trials'].items():
        print(t, json.dumps({'dev': round(v['dev']['sharpe'], 3), 'cagr': round(v['dev']['cagr'], 3),
                             'dd': round(v['dev']['max_dd'], 3), 'cost2': round(v['dev_cost2']['sharpe'], 3),
                             'val2024': round(v['val2024']['sharpe'], 3) if v['val2024'] else None,
                             'rho': v['rho_p1_dev'], 'turn': round(v['weekly_turnover'], 3), 'pass': v['pass']}),
              v['gates'])


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    run(only_y6=len(sys.argv) > 2 and sys.argv[2] == 'Y6')
    return 0


if __name__ == '__main__':
    sys.exit(main())
