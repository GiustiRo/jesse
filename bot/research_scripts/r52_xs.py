"""r52 F1: weekly cross-sectional ranker on the U50 perpetuals (X0-X3).

PROTOCOL_R52.md (840747c3) sections 0, 1 and F1. Data: data/r52/<SYM>_1h.npy and _funding.npy
from r52_download.py (data.binance.vision, checksum-verified).

* Daily bars are built from 1h klines (UTC days); features are computed at each Sunday close and
  ranked cross-sectionally into [-0.5, 0.5]; the target is next week's return rank.
* Walk-forward: refit every 4 weeks on weeks whose target was already known one week before the
  prediction (purge + 1-week embargo); first prediction after 52 training weeks.
* Portfolio: top quintile long / bottom quintile short, inverse 30-day vol inside each leg, 0.5
  gross per leg; X3 is the long leg alone (gross 1.0) hedged 50/50 with BTC and ETH by its
  60-day beta. Weekly weights are held as constant equity fractions through the week (declared
  simplification). Costs: (0.045% + 2 bp) on turnover; real funding per symbol.
* 2025 is sealed (PROTOCOL F4): curves are saved through 2025 for that single look, but every
  metric printed or stored here stops at 2024-12-31.

    python research_scripts/r52_xs.py run

writes data/r52/xs.json and data/r52/xs_curves.npy.
"""
import json
import math
import os
import sys
import warnings

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.linear_model import ElasticNetCV
from sklearn.model_selection import TimeSeriesSplit

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data', 'r52')
DAY_MS = 86_400_000
COST = 0.00045 + 0.0002           # taker fee + 2 bp slippage, per unit of turnover
MIN_DAYS_LISTED = 90
MIN_MEDIAN_QVOL = 10e6            # USDT per day, 30-day median
MIN_ELIGIBLE = 10
TRAIN_MIN_WEEKS = 52
REFIT_EVERY = 4
DEV_END, VAL_END = '2023-12-31', '2024-12-31'
SMA_N = (3, 5, 10, 20, 50, 100, 200)
VSMA_N = (3, 5, 10, 20, 50)
RET_W = (1, 2, 4, 8, 12, 26)


# ----------------------------------------------------------------------------------------------
# Panel
# ----------------------------------------------------------------------------------------------
def load_panel():
    uni = json.load(open(os.path.join(DATA, 'universe50.json')))
    syms = [u['symbol'] for u in uni]
    days = pd.date_range('2020-01-01', '2025-12-31', freq='D', tz='UTC')
    close, qvol, imb, fund = {}, {}, {}, {}
    for s in syms:
        a = np.load(os.path.join(DATA, f'{s}_1h.npy'))
        if not len(a):
            continue
        df = pd.DataFrame(a, columns=['t', 'o', 'h', 'l', 'c', 'v', 'qv', 'tbv'])
        df['day'] = pd.to_datetime(df['t'], unit='ms', utc=True).dt.floor('D')
        g = df.groupby('day')
        close[s] = g['c'].last()
        qvol[s] = g['qv'].sum()
        imb[s] = (2 * g['tbv'].sum() / g['v'].sum().replace(0, np.nan) - 1)
        f = np.load(os.path.join(DATA, f'{s}_funding.npy'))
        if len(f):
            fd = pd.Series(f[:, 1], index=pd.to_datetime(f[:, 0], unit='ms', utc=True).floor('D'))
            fund[s] = fd.groupby(level=0).sum()
    C = pd.DataFrame(close).reindex(days)
    Q = pd.DataFrame(qvol).reindex(days)
    I = pd.DataFrame(imb).reindex(days)
    F = pd.DataFrame(fund).reindex(days).reindex(columns=C.columns).fillna(0.0)
    return C, Q, I, F


def rsi(c, n=14):
    d = c.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn)


def features(C, Q, I):
    lr = np.log(C).diff()
    feats = {}
    for n in SMA_N:
        feats[f'p_sma{n}'] = C / C.rolling(n).mean() - 1
    v200 = Q.rolling(200, min_periods=100).mean()
    for n in VSMA_N:
        feats[f'v_sma{n}'] = Q.rolling(n).mean() / v200
    for w in RET_W:
        feats[f'ret{w}w'] = C / C.shift(7 * w) - 1
    feats['vol7'] = lr.rolling(7).std()
    feats['vol30'] = lr.rolling(30).std()
    feats['imb7'] = I.rolling(7).mean()
    feats['imb30'] = I.rolling(30).mean()
    feats['rsi14'] = C.apply(rsi)
    feats['macd'] = (C.ewm(span=12, adjust=False).mean() - C.ewm(span=26, adjust=False).mean()) / C
    btc = lr['BTCUSDT']
    cov = lr.rolling(60).cov(btc)
    feats['beta60'] = cov.div(btc.rolling(60).var(), axis=0)
    return feats, lr


def eligibility(C, Q):
    first = C.apply(lambda s: s.first_valid_index())
    age = pd.DataFrame({c: (C.index - first[c]).days for c in C.columns}, index=C.index)
    med = Q.rolling(30, min_periods=20).median()
    return (age >= MIN_DAYS_LISTED) & (med >= MIN_MEDIAN_QVOL) & C.notna()


def weekly_samples(C, feats, elig):
    """Rows (week, symbol) with ranked features, the raw score inputs and next-week target."""
    sundays = C.index[C.index.dayofweek == 6]
    rows = []
    names = sorted(feats)
    for k, d in enumerate(sundays[:-1]):
        e = elig.loc[d]
        e = e[e].index
        if len(e) < MIN_ELIGIBLE:
            continue
        nxt = sundays[k + 1]
        fwd = C.loc[nxt, e] / C.loc[d, e] - 1
        block = pd.DataFrame({n: feats[n].loc[d, e] for n in names})
        ranked = block.rank(pct=True) - 0.5
        ranked = ranked.fillna(0.0)
        tgt = fwd.rank(pct=True) - 0.5
        for s in e:
            rows.append((k, d, s, *ranked.loc[s].tolist(), float(tgt.get(s, np.nan)), float(fwd.get(s, np.nan)),
                         float(feats['vol30'].loc[d, s])))
    cols = ['k', 'day', 'sym', *names, 'target', 'fwd', 'vol30_raw']
    return pd.DataFrame(rows, columns=cols), names


# ----------------------------------------------------------------------------------------------
# Models
# ----------------------------------------------------------------------------------------------
def predict_walk_forward(S, names, kind):
    weeks = sorted(S['k'].unique())
    preds = pd.Series(np.nan, index=S.index)
    model = None
    for j, k in enumerate(weeks):
        train = S[(S['k'] <= k - 2) & S['target'].notna()]
        if train['k'].nunique() < TRAIN_MIN_WEEKS:
            continue
        if model is None or j % REFIT_EVERY == 0:
            X, y = train[names].values, train['target'].values
            if kind == 'en':
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    model = ElasticNetCV(l1_ratio=[0.1, 0.5, 0.9], cv=TimeSeriesSplit(5), n_alphas=30,
                                         max_iter=5000).fit(X, y)
            else:
                model = HistGradientBoostingRegressor(max_depth=3, learning_rate=0.05, max_iter=200,
                                                      min_samples_leaf=50, l2_regularization=1.0,
                                                      random_state=0).fit(X, y)
        idx = S.index[S['k'] == k]
        preds.loc[idx] = model.predict(S.loc[idx, names].values)
    return preds


def score_x0(S):
    return (S['ret1w'] + S['ret4w'] + S['ret12w']) / 3


# ----------------------------------------------------------------------------------------------
# Portfolio
# ----------------------------------------------------------------------------------------------
def weekly_weights(S, score, mode, lr):
    """Signed weights per week index k (dict sym -> weight)."""
    out = {}
    for k, g in S.assign(score=score).dropna(subset=['score']).groupby('k'):
        n = len(g)
        q = max(1, int(math.ceil(n / 5)))
        g = g.sort_values('score')
        inv = 1 / g['vol30_raw'].clip(lower=1e-4)
        top, bot = g.tail(q), g.head(q)
        w = {}
        if mode == 'ls':
            wt = inv.loc[top.index] / inv.loc[top.index].sum() * 0.5
            wb = inv.loc[bot.index] / inv.loc[bot.index].sum() * 0.5
            for i in top.index:
                w[g.at[i, 'sym']] = w.get(g.at[i, 'sym'], 0) + wt[i]
            for i in bot.index:
                w[g.at[i, 'sym']] = w.get(g.at[i, 'sym'], 0) - wb[i]
        else:  # long top quintile hedged with BTC/ETH by 60-day beta
            wt = inv.loc[top.index] / inv.loc[top.index].sum()
            longw = {g.at[i, 'sym']: float(wt[i]) for i in top.index}
            d = g['day'].iloc[0]
            hist = lr.loc[:d].tail(60)
            lb = sum(hist[s].fillna(0) * x for s, x in longw.items())
            bench = (hist['BTCUSDT'] + hist['ETHUSDT']) / 2
            beta = float(np.cov(lb, bench)[0, 1] / bench.var()) if bench.var() > 0 else 1.0
            w = dict(longw)
            for h in ('BTCUSDT', 'ETHUSDT'):
                w[h] = w.get(h, 0) - beta / 2
        out[k] = (g['day'].iloc[0], w)
    return out


def simulate(weights, C, F, cost_mult=1.0):
    """Daily returns from the weekly weights: price return minus funding, minus turnover cost
    on the rebalance day."""
    ret = C.pct_change()
    days, rets = [], []
    prev = {}
    ks = sorted(weights)
    for j, k in enumerate(ks):
        d0, w = weights[k]
        d1 = weights[ks[j + 1]][0] if j + 1 < len(ks) else C.index[-1]
        turn = sum(abs(w.get(s, 0) - prev.get(s, 0)) for s in set(w) | set(prev))
        span = C.index[(C.index > d0) & (C.index <= d1)]
        for n, day in enumerate(span):
            r = sum(x * (ret.at[day, s] if np.isfinite(ret.at[day, s]) else 0.0) for s, x in w.items())
            f = sum(x * F.at[day, s] for s, x in w.items())
            r -= f
            if n == 0:
                r -= turn * COST * cost_mult
            days.append(day)
            rets.append(r)
        prev = w
    return pd.Series(rets, index=pd.DatetimeIndex(days))


def stats(r, frm, to):
    x = r[(r.index >= pd.Timestamp(frm, tz='UTC')) & (r.index <= pd.Timestamp(to, tz='UTC'))]
    if len(x) < 30:
        return None
    eq = np.cumprod(1 + x.values)
    sd = x.std(ddof=1)
    yrs = len(x) / 365
    q = (1 + x).groupby(x.index.to_period('Q')).prod() - 1
    return {'from': str(x.index[0].date()), 'to': str(x.index[-1].date()),
            'sharpe': float(x.mean() / sd * math.sqrt(365)) if sd > 0 else 0.0,
            'cagr': float(eq[-1] ** (1 / yrs) - 1), 'max_dd': float((eq / np.maximum.accumulate(eq) - 1).min()),
            'quarters_pos': float((q > 0).mean()), 't_stat': float(x.mean() / sd * math.sqrt(len(x))) if sd > 0 else 0.0}


def p1_returns():
    import r51_lib as lib
    comps, _, _ = lib.p1_components('long')
    days, vals, _, _ = lib.portfolio_attr(comps, ['R1', 'C6'])
    idx = pd.to_datetime(np.asarray(days)[1:], unit='ms', utc=True)
    return pd.Series(np.diff(vals) / vals[:-1], index=idx)


def rho(a, b, to):
    j = pd.concat([a, b], axis=1, join='inner').dropna()
    j = j[j.index <= pd.Timestamp(to, tz='UTC')]
    return float(j.corr().iloc[0, 1]) if len(j) > 60 else None


def run():
    C, Q, I, F = load_panel()
    feats, lr = features(C, Q, I)
    elig = eligibility(C, Q)
    S, names = weekly_samples(C, feats, elig)
    p1 = p1_returns()
    old20 = [s for s in C.columns if C[s].first_valid_index() <= pd.Timestamp('2020-07-01', tz='UTC')][:20]
    scores = {'X0': score_x0(S), 'X1': predict_walk_forward(S, names, 'en'),
              'X2': predict_walk_forward(S, names, 'gbm')}
    # Comparisons use the same weeks: those where the ML models already predict.
    common = scores['X1'].notna() & scores['X2'].notna()
    res, curves = {'n_weeks': int(S['k'].nunique()), 'features': names, 'trials': {}}, {}
    for t in ('X0', 'X1', 'X2'):
        sc = scores[t].where(common)
        w = weekly_weights(S, sc, 'ls', lr)
        r = simulate(w, C, F)
        r2 = simulate(w, C, F, 2.0)
        curves[t] = r
        sub = S['sym'].isin(old20)
        r_old = simulate(weekly_weights(S[sub], sc[sub], 'ls', lr), C, F)
        res['trials'][t] = {'dev': stats(r, '2020-01-01', DEV_END), 'dev_cost2': stats(r2, '2020-01-01', DEV_END),
                            'val2024': stats(r, '2024-01-01', VAL_END), 'old20_dev': stats(r_old, '2020-01-01', DEV_END),
                            'rho_p1_dev': rho(r, p1, DEV_END),
                            'avg_names': float(np.mean([len(v[1]) for v in w.values()]))}
    best = max(('X1', 'X2'), key=lambda t: res['trials'][t]['dev']['sharpe'])
    w3 = weekly_weights(S, scores[best].where(common), 'hedged', lr)
    r3 = simulate(w3, C, F)
    curves['X3'] = r3
    res['trials']['X3'] = {'base_model': best, 'dev': stats(r3, '2020-01-01', DEV_END),
                           'dev_cost2': stats(simulate(w3, C, F, 2.0), '2020-01-01', DEV_END),
                           'val2024': stats(r3, '2024-01-01', VAL_END), 'rho_p1_dev': rho(r3, p1, DEV_END)}
    x0s = res['trials']['X0']['dev']['sharpe']
    for t, v in res['trials'].items():
        g = {'sharpe_ge_0_5': v['dev']['sharpe'] >= 0.5, 'cost2_pos': v['dev_cost2']['sharpe'] > 0,
             'rho_le_0_3': v['rho_p1_dev'] is not None and v['rho_p1_dev'] <= 0.3,
             'val2024_pos': v['val2024'] is not None and v['val2024']['sharpe'] > 0}
        if t != 'X0':
            g['beats_x0_0_2'] = v['dev']['sharpe'] - x0s >= 0.2
        v['gates'] = g
        v['pass'] = all(g.values())
    # Monthly IC of each score against the next-week return rank (dev only), as a diagnostic.
    for t in ('X0', 'X1', 'X2'):
        d = S.assign(score=scores[t].where(common)).dropna(subset=['score', 'target'])
        d = d[d['day'] <= pd.Timestamp(DEV_END, tz='UTC')]
        ic = d.groupby('k').apply(lambda g: g['score'].corr(g['target'], method='spearman'))
        res['trials'][t]['ic_dev_mean'] = float(ic.mean())
        res['trials'][t]['ic_dev_t'] = float(ic.mean() / ic.std(ddof=1) * math.sqrt(len(ic)))
    json.dump(res, open(os.path.join(DATA, 'xs.json'), 'w'), indent=1, default=float)
    np.save(os.path.join(DATA, 'xs_curves.npy'), {k: (v.index.asi8 // 10**6, v.values) for k, v in curves.items()},
            allow_pickle=True)
    for t, v in res['trials'].items():
        print(t, json.dumps({k: (round(x, 3) if isinstance(x, float) else x) for k, x in
                             {'dev_sharpe': v['dev']['sharpe'], 'dev_cagr': v['dev']['cagr'], 'dev_dd': v['dev']['max_dd'],
                              'dev_from': v['dev']['from'], 'cost2': v['dev_cost2']['sharpe'],
                              'val2024': v['val2024']['sharpe'] if v['val2024'] else None,
                              'rho': v['rho_p1_dev'], 'ic': v.get('ic_dev_mean'), 'ic_t': v.get('ic_dev_t'),
                              'old20': v.get('old20_dev', {}) and v['old20_dev']['sharpe'], 'pass': v['pass']}.items()}))
        print('   gates', v['gates'])


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
