"""r59: oracle criteria, one per query id (PROTOCOL_R59.md §1.2). A criterion is committed here
before its query runs. It receives the oracle context and returns
    {'margins': [(name, statistic - threshold, scale), ...], 'stats': {...}}
The query passes when every noisy margin is > 0. Only r59_oracle calls these on H.
"""
import numpy as np

import r57
import r58

CRITERIA = {}


def register(qid, alpha, desc):
    def deco(fn):
        assert qid not in CRITERIA, qid
        CRITERIA[qid] = {'fn': fn, 'alpha': alpha, 'desc': desc}
        return fn
    return deco


def d_boot(df, keep, n_boot, seed):
    """D = mean R (keep) - mean R (rest) with its weekly-block bootstrap draws (r58 F1/F2 recipe)."""
    R, g = df['R'].values, np.asarray(keep, bool)
    old = r57.N_BOOT
    r57.N_BOOT = n_boot
    try:
        bs = r57.block_boot(df['week'].values, lambda ix: (r58._d(R[ix], g[ix]),), np.random.default_rng(seed))[:, 0]
    finally:
        r57.N_BOOT = old
    return r58._d(R, g), bs
