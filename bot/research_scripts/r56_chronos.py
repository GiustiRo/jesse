"""r56 family T: zero-shot time-series foundation models forecasting 20-day volatility.

Runs in the isolated venv /opt/chronos-venv of the research container (torch CPU and
chronos-forecasting, installed with the user's authorisation of 2026-10-26), so the main research
environment stays untouched:

    /opt/chronos-venv/bin/python research_scripts/r56_chronos.py bolt     # T1, amazon/chronos-bolt-small
    /opt/chronos-venv/bin/python research_scripts/r56_chronos.py chronos2 # T2, amazon/chronos-2
    /opt/chronos-venv/bin/python research_scripts/r56_chronos.py chronos2cov  # T3 (r56-B), covariates
    ... [panel70]    # same forecasts on the 70-coin panel (U50 + N2) for r56 F10
    ... panel70 n2only  # only the N2 columns; the first 50 are copied from chronos_<model>.npy
                        # (panel70's first 50 columns equal panel.npz and the covariates use
                        # only them, so those forecasts would be identical; checked in run)

T3 gives Chronos-2 two past covariates over the same context: BTC's daily log RV and the global
vol, the mean daily log RV over the U50 coins with data that day (always the first 50 columns, so
the covariate is identical with or without N2).

For every coin and day t with at least 60 valid days of history, the context is the coin's daily
log RV (from 1h returns) over the last 512 days up to and including t (missing days as NaN), and
the model forecasts the next 20 daily values zero-shot. The output is the log of the summed
median path, log sum_k exp(q50_k): the forecast of log RV(t+1..t+20) that r56_eval turns into the
same tercile z-distances as V1. Nothing is fitted here; data stops at 2024-12-31 (panel.npz).

writes data/r56/chronos_<model>.npy (days x coins, NaN where no forecast).
"""
import os
import sys
import time

import numpy as np
import torch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r56')
MODELS = {'bolt': 'amazon/chronos-bolt-small', 'chronos2': 'amazon/chronos-2', 'chronos2cov': 'amazon/chronos-2',
          'bolt40': 'amazon/chronos-bolt-small'}
HORIZONS = {'bolt40': 40}    # r56-B F9: the 40-day label needs a 40-step path
CONTEXT, HORIZON, MIN_HIST, BATCH = 512, 20, 60, 256


def run(kind, limit=None, panel='panel', n2only=False):
    from chronos import BaseChronosPipeline
    torch.manual_seed(0)
    pipe = BaseChronosPipeline.from_pretrained(MODELS[kind], device_map='cpu', torch_dtype=torch.float32)
    z = np.load(os.path.join(OUT, f'{panel}.npz'))
    lrv = np.log(z['rv'])
    lrv[~np.isfinite(lrv)] = np.nan
    syms = [str(x) for x in z['syms']]
    btc = lrv[:, syms.index('BTCUSDT')]
    glob = np.nanmean(lrv[:, :50], axis=1)
    D, M = lrv.shape
    jobs = []
    for j in range(50 if n2only else 0, M):
        ok = np.isfinite(lrv[:, j])
        cnt = np.cumsum(ok)
        for t in range(D):
            if cnt[t] >= MIN_HIST and ok[t]:
                jobs.append((t, j))
    if limit:
        jobs = jobs[:limit]
    out = np.full((D, M), np.nan)
    if n2only:
        base = np.load(os.path.join(HERE, 'data', 'r56', 'panel.npz'))
        assert [str(x) for x in base['syms']] == syms[:50] and np.array_equal(base['rv'], z['rv'][:, :50], equal_nan=True)
        out[:, :50] = np.load(os.path.join(OUT, f'chronos_{kind}.npy'))
    t0 = time.time()
    for b in range(0, len(jobs), BATCH):
        chunk = jobs[b:b + BATCH]
        if kind == 'chronos2cov':
            ctxs = []
            for t, j in chunk:
                a = max(0, t - CONTEXT + 1)
                ctxs.append({'target': lrv[a:t + 1, j].astype(np.float32),
                             'past_covariates': {'btc': btc[a:t + 1].astype(np.float32),
                                                 'glob': glob[a:t + 1].astype(np.float32)}})
        else:
            ctxs = [torch.tensor(lrv[max(0, t - CONTEXT + 1):t + 1, j], dtype=torch.float32) for t, j in chunk]
        q, mean = pipe.predict_quantiles(ctxs, prediction_length=HORIZONS.get(kind, HORIZON), quantile_levels=[0.5],
                                         **({'limit_prediction_length': False} if kind in HORIZONS else {}))
        # Chronos-Bolt returns one (batch, horizon, q) tensor; Chronos-2 a list of
        # (variates, horizon, q) tensors, one per series.
        med = (np.stack([x[0, :, 0].numpy() for x in q]) if isinstance(q, list) else q[..., 0].numpy())
        agg = np.log(np.exp(med).sum(axis=1))
        for (t, j), v in zip(chunk, agg):
            out[t, j] = v
        if b // BATCH % 20 == 0:
            print(f'{b + len(chunk)}/{len(jobs)} {time.time() - t0:.0f}s', flush=True)
    if limit:
        print('timing only:', len(jobs), 'forecasts in', round(time.time() - t0, 1), 's')
        return
    sfx = '' if panel == 'panel' else f'_{panel}'
    np.save(os.path.join(OUT, f'chronos_{kind}{sfx}.npy'), out.astype(np.float32))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in MODELS:
        extra = sys.argv[2:]
        if extra and extra[0].startswith('panel'):
            run(sys.argv[1], panel=extra[0], n2only='n2only' in extra)
        else:
            run(sys.argv[1], int(extra[0]) if extra else None)
    else:
        print(__doc__)
