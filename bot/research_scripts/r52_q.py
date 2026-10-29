"""r52 F2: the quarter-hour order-flow clock (Q1-Q3).

PROTOCOL_R52.md (840747c3) section F2, after arXiv 2607.09426. Data: data/r52/<SYM>_q15.npy
(quarter-hour rows from 1m klines: bucket ms, opening-minute volume, opening-minute taker-buy
volume, bucket volume, bucket close) and <SYM>_funding.npy.

* QOI of a 4h bar = sum over its 16 quarter-hour openings of (2 * taker buy - volume) / sum of
  their volume; z-scored against the 540 previous 4h bars (90 days).
* Q1: Spearman IC between QOI at each 4h close and the next 8h return, 2021-01..2023-12, with a
  Newey-West (12 lags) t on the rank regression; BTC, ETH and their average.
* Q2: long when z > +1, short when z < -1, exit after 2 bars (8h); size 0.17/sigma30 capped at
  2x; taker + 2 bp per side; real funding while held. Sign as in the paper.
* Q3: Q2 frozen on the 20 largest U50 alts (download manifest).
* 2025 sealed: curves saved for F4, metrics stop at 2024-12-31.

    python research_scripts/r52_q.py run

writes data/r52/q.json and data/r52/q_curves.npy.
"""
import json
import math
import os
import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data', 'r52')
H4_MS = 4 * 3_600_000
Z_BARS = 540
HOLD = 2
TARGET_VOL, MAX_X = 0.17, 2.0
COST = 0.00045 + 0.0002
DEV = ('2021-01-01', '2023-12-31')
VAL = ('2024-01-01', '2024-12-31')


def bars_4h(sym):
    q = np.load(os.path.join(DATA, f'{sym}_q15.npy'))
    df = pd.DataFrame(q, columns=['t', 'ov', 'otb', 'v', 'c'])
    df['b'] = (df['t'] // H4_MS * H4_MS).astype(np.int64)
    g = df.groupby('b')
    signed = (2 * df['otb'] - df['ov']).groupby(df['b']).sum()
    out = pd.DataFrame({'close': g['c'].last(), 'qoi': signed / g['ov'].sum().replace(0, np.nan),
                        'n_open': g['ov'].count()})
    out.index = pd.to_datetime(out.index + H4_MS, unit='ms', utc=True)   # stamped at bar close
    lr = np.log(out['close']).diff()
    m = out['qoi'].shift(1).rolling(Z_BARS, min_periods=Z_BARS // 2).mean()
    s = out['qoi'].shift(1).rolling(Z_BARS, min_periods=Z_BARS // 2).std()
    out['z'] = (out['qoi'] - m) / s
    out['fwd8h'] = np.log(out['close'].shift(-HOLD) / out['close'])
    out['vol'] = lr.rolling(180).std() * math.sqrt(6 * 365)
    f = np.load(os.path.join(DATA, f'{sym}_funding.npy'))
    fund = pd.Series(f[:, 1], index=pd.to_datetime(f[:, 0], unit='ms', utc=True)) if len(f) else pd.Series(dtype=float)
    return out, fund


def window(df, w):
    return df[(df.index >= pd.Timestamp(w[0], tz='UTC')) & (df.index <= pd.Timestamp(w[1], tz='UTC') + pd.Timedelta(days=1))]


def ic_test(frames):
    """Rank IC and Newey-West t of the rank regression, per asset and for the average."""
    out, xs, ys = {}, [], []
    for name, df in frames.items():
        d = window(df, DEV).dropna(subset=['qoi', 'fwd8h'])
        x = d['qoi'].rank(pct=True) - 0.5
        y = d['fwd8h'].rank(pct=True) - 0.5
        fit = sm.OLS(y.values, sm.add_constant(x.values)).fit(cov_type='HAC', cov_kwds={'maxlags': 12})
        out[name] = {'ic': float(x.corr(y)), 't_nw': float(fit.tvalues[1]), 'n': int(len(d))}
        xs.append(x.rename(name))
        ys.append(y.rename(name))
    X = pd.concat(xs, axis=1).dropna().mean(axis=1)
    Y = pd.concat(ys, axis=1).dropna().mean(axis=1)
    j = pd.concat([X, Y], axis=1, join='inner')
    fit = sm.OLS(j.iloc[:, 1].values, sm.add_constant(j.iloc[:, 0].values)).fit(cov_type='HAC', cov_kwds={'maxlags': 12})
    out['basket'] = {'ic': float(j.iloc[:, 0].corr(j.iloc[:, 1])), 't_nw': float(fit.tvalues[1]), 'n': int(len(j))}
    return out


def rule(df, fund):
    """Daily returns of the Q2 rule on one asset (positions held exactly HOLD bars)."""
    c = df['close'].values
    z = df['z'].values
    vol = df['vol'].values
    idx = df.index
    ft = fund.index.asi8 // 10**6 if len(fund) else np.array([], dtype=np.int64)
    fr = fund.values if len(fund) else np.array([])
    bar_ret = np.zeros(len(df))
    i = 0
    trades = 0
    while i < len(df) - HOLD:
        if np.isfinite(z[i]) and np.isfinite(vol[i]) and vol[i] > 0 and abs(z[i]) > 1:
            side = 1.0 if z[i] > 1 else -1.0
            x = side * min(MAX_X, TARGET_VOL / vol[i])
            t0, t1 = idx[i].value // 10**6, idx[i + HOLD].value // 10**6
            f = fr[(ft > t0) & (ft <= t1)].sum() if len(ft) else 0.0
            for k in range(1, HOLD + 1):
                bar_ret[i + k] += x * (c[i + k] / c[i + k - 1] - 1)
            bar_ret[i + 1] -= abs(x) * COST
            bar_ret[i + HOLD] -= abs(x) * COST + x * f
            trades += 1
            i += HOLD
        else:
            i += 1
    s = pd.Series(bar_ret, index=idx)
    daily = (1 + s).groupby(s.index.floor('D')).prod() - 1
    return daily, trades


def stats(r, w):
    x = r[(r.index >= pd.Timestamp(w[0], tz='UTC')) & (r.index <= pd.Timestamp(w[1], tz='UTC'))]
    if len(x) < 30:
        return None
    eq = np.cumprod(1 + x.values)
    sd = x.std(ddof=1)
    return {'sharpe': float(x.mean() / sd * math.sqrt(365)) if sd > 0 else 0.0,
            'cagr': float(eq[-1] ** (365 / len(x)) - 1), 'max_dd': float((eq / np.maximum.accumulate(eq) - 1).min()),
            't_stat': float(x.mean() / sd * math.sqrt(len(x))) if sd > 0 else 0.0}


def run():
    import r52_xs as xs
    p1 = xs.p1_returns()
    man = json.load(open(os.path.join(DATA, 'manifest.json')))
    alts = man['q_basket_alts']
    frames, funds = {}, {}
    for s in ['BTCUSDT', 'ETHUSDT'] + alts:
        df, f = bars_4h(s)
        frames[s], funds[s] = df, f
    res = {'Q1': ic_test({s: frames[s] for s in ('BTCUSDT', 'ETHUSDT')})}
    res['Q1']['pass'] = res['Q1']['basket']['t_nw'] >= 2
    curves = {}
    q2 = {}
    for s in ('BTCUSDT', 'ETHUSDT'):
        r, n = rule(frames[s], funds[s])
        curves[s] = r
        q2[s] = {'dev': stats(r, DEV), 'val2024': stats(r, VAL), 'trades': n}
    b2 = pd.concat([curves['BTCUSDT'], curves['ETHUSDT']], axis=1).fillna(0).mean(axis=1)
    curves['Q2'] = b2
    q2['basket'] = {'dev': stats(b2, DEV), 'val2024': stats(b2, VAL), 'rho_p1': xs.rho(b2, p1, DEV[1])}
    q2['gates'] = {'sharpe_ge_0_5': q2['basket']['dev']['sharpe'] >= 0.5,
                   'rho_le_0_3': q2['basket']['rho_p1'] is not None and q2['basket']['rho_p1'] <= 0.3,
                   'val2024_pos': q2['basket']['val2024']['sharpe'] > 0}
    q2['pass'] = all(q2['gates'].values())
    res['Q2'] = q2
    q3 = {}
    alt_curves = []
    for s in alts:
        r, n = rule(frames[s], funds[s])
        alt_curves.append(r.rename(s))
        q3[s] = {'dev': stats(r, DEV), 'trades': n}
    b3 = pd.concat(alt_curves, axis=1).fillna(0).mean(axis=1)
    curves['Q3'] = b3
    pos = sum(1 for s in alts if q3[s]['dev'] and q3[s]['dev']['sharpe'] > 0)
    q3['basket'] = {'dev': stats(b3, DEV), 'val2024': stats(b3, VAL), 'rho_p1': xs.rho(b3, p1, DEV[1]),
                    'alts_positive': pos, 'alts': len(alts)}
    q3['gates'] = {'majority_pos': pos > len(alts) / 2, 't_ge_1_28': q3['basket']['dev']['t_stat'] >= 1.28}
    q3['pass'] = all(q3['gates'].values())
    res['Q3'] = q3
    json.dump(res, open(os.path.join(DATA, 'q.json'), 'w'), indent=1, default=float)
    np.save(os.path.join(DATA, 'q_curves.npy'), {k: (v.index.asi8 // 10**6, v.values) for k, v in curves.items()},
            allow_pickle=True)
    print('Q1', json.dumps(res['Q1']))
    print('Q2', json.dumps({k: v for k, v in q2.items()}, default=float))
    print('Q3 basket', json.dumps(q3['basket'], default=float), q3['gates'])


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
