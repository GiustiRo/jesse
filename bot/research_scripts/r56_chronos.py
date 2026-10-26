"""r56 family T: zero-shot time-series foundation models forecasting 20-day volatility.

Runs in the isolated venv /opt/chronos-venv of the research container (torch CPU and
chronos-forecasting, installed with the user's authorisation of 2026-10-26), so the main research
environment stays untouched:

    /opt/chronos-venv/bin/python research_scripts/r56_chronos.py bolt     # T1, amazon/chronos-bolt-small
    /opt/chronos-venv/bin/python research_scripts/r56_chronos.py chronos2 # T2, amazon/chronos-2

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
MODELS = {'bolt': 'amazon/chronos-bolt-small', 'chronos2': 'amazon/chronos-2'}
CONTEXT, HORIZON, MIN_HIST, BATCH = 512, 20, 60, 256


def run(kind, limit=None):
    from chronos import BaseChronosPipeline
    torch.manual_seed(0)
    pipe = BaseChronosPipeline.from_pretrained(MODELS[kind], device_map='cpu', torch_dtype=torch.float32)
    z = np.load(os.path.join(OUT, 'panel.npz'))
    lrv = np.log(z['rv'])
    lrv[~np.isfinite(lrv)] = np.nan
    D, M = lrv.shape
    jobs = []
    for j in range(M):
        ok = np.isfinite(lrv[:, j])
        cnt = np.cumsum(ok)
        for t in range(D):
            if cnt[t] >= MIN_HIST and ok[t]:
                jobs.append((t, j))
    if limit:
        jobs = jobs[:limit]
    out = np.full((D, M), np.nan)
    t0 = time.time()
    for b in range(0, len(jobs), BATCH):
        chunk = jobs[b:b + BATCH]
        ctxs = [torch.tensor(lrv[max(0, t - CONTEXT + 1):t + 1, j], dtype=torch.float32) for t, j in chunk]
        q, mean = pipe.predict_quantiles(ctxs, prediction_length=HORIZON, quantile_levels=[0.5])
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
    np.save(os.path.join(OUT, f'chronos_{kind}.npy'), out.astype(np.float32))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in MODELS:
        run(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else None)
    else:
        print(__doc__)
