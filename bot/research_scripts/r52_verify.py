"""r52 F0 checks: the downloaded universe against Jesse's own data, and the cross-sectional
simulator on synthetic rankings (PROTOCOL_R52.md verification).

1. BTC/ETH 1h closes from data.binance.vision vs 1h bars built from Jesse's stored 1m candles.
2. BTC/ETH funding from vision vs the Jesse datasets used since r50 (0ab14bc2, 22bd891c).
3. Synthetic: a perfect next-week ranking must earn a large positive return; a random one ~0
   minus costs.
4. Coverage: rows, first bar and gaps per symbol (from the download manifest).

    python research_scripts/r52_verify.py run
"""
import json
import os
import sys

import numpy as np
import pandas as pd
import jesse.models  # noqa: F401

import r50_harness as hz
import r50_engines as en
import r52_xs as xs

DATA = xs.DATA


def check_klines(sym):
    a = np.load(os.path.join(DATA, f'{sym}USDT_1h.npy'))
    v = pd.Series(a[:, 4], index=a[:, 0].astype(np.int64))
    m = hz._minutes('Binance Perpetual Futures', f'{sym}-USDT', hz._ms('2021-01-01'), hz._ms('2025-12-31'))
    hour = (m[:, hz.T].astype(np.int64) // 3_600_000) * 3_600_000
    j = pd.Series(m[:, hz.C], index=hour).groupby(level=0).last()
    common = v.index.intersection(j.index)
    rel = np.abs(v.loc[common].values / j.loc[common].values - 1)
    return {'hours': int(len(common)), 'max_rel': float(rel.max()), 'share_gt_1e6': float((rel > 1e-6).mean())}


def check_funding(sym):
    f = np.load(os.path.join(DATA, f'{sym}USDT_funding.npy'))
    mine = pd.Series(f[:, 1], index=(f[:, 0].astype(np.int64) // 60_000))
    eff, mark, rate = hz.load_funding(en.FUNDING[sym])
    theirs = pd.Series(rate, index=eff // 60_000)
    common = mine.index.intersection(theirs.index)
    common = common[common < hz._ms('2026-01-01') // 60_000]
    d = np.abs(mine.loc[common].values - theirs.loc[common].values)
    return {'events': int(len(common)), 'max_abs_diff': float(d.max()) if len(d) else None}


def synthetic():
    C, Q, I, F = xs.load_panel()
    feats, lr = xs.features(C, Q, I)
    elig = xs.eligibility(C, Q)
    S, names = xs.weekly_samples(C, feats, elig)
    S = S[S['day'] <= pd.Timestamp('2023-12-31', tz='UTC')]
    perfect = S['target']
    rng = np.random.default_rng(0)
    random = pd.Series(rng.random(len(S)), index=S.index)
    out = {}
    for name, sc in (('perfect', perfect), ('random', random)):
        r = xs.simulate(xs.weekly_weights(S, sc, 'ls', lr), C, F)
        out[name] = xs.stats(r, '2020-01-01', '2023-12-31')
    return out


def run():
    man = json.load(open(os.path.join(DATA, 'manifest.json')))
    res = {'klines': {s: check_klines(s) for s in ('BTC', 'ETH')},
           'funding': {s: check_funding(s) for s in ('BTC', 'ETH')},
           'synthetic': synthetic(),
           'coverage': man['symbols']}
    json.dump(res, open(os.path.join(DATA, 'verify.json'), 'w'), indent=1, default=float)
    print(json.dumps({k: v for k, v in res.items() if k != 'coverage'}, indent=1, default=float))
    short = [c for c in man['symbols'] if c['h1_rows'] < 20000]
    print('symbols with < 20000 1h rows:', [(c['symbol'], c['h1_rows']) for c in short])
    print('max 1h gap (h):', sorted(((c['h1_max_gap_h'], c['symbol']) for c in man['symbols']), reverse=True)[:5])


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
