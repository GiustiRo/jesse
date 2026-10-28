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


# ----------------------------------------------------------------------------------------------
# r60 q2 (PROTOCOL_R60.md §4), committed before the query
# ----------------------------------------------------------------------------------------------
@register('q2', 0.05, 'r60 F2: libro K de la variante elegida en F1 sobre H = N2 ∪ N3, márgenes (a) Sharpe − 0,4, '
                      '(b) Sharpe con costos ×2, (c) 0,3 − ρ con R1, (d) ΔSharpe R1 + manga − 0,1 (PROTOCOL_R60 §4)')
def q2(ctx):
    import json
    import os
    import r59_holdout as hg
    import r60
    n2 = {u['symbol'] for u in json.load(open(hg._LIST_FILES[0]))['selected']}
    src_of = lambda s: r58.N2_DIR if s in n2 else r58.N3_DIR  # noqa: E731
    return r60.q2_compute(hg.holdout_syms(), src_of, r60.u50()[0], r60.selected_variant())


# ----------------------------------------------------------------------------------------------
# r61 q3 (PROTOCOL_R61.md §4), committed before the query
# ----------------------------------------------------------------------------------------------
@register('q3', 0.05, 'r61 F2: libro de asimetría neutral (variante elegida en F1) sobre H = N2 ∪ N3, márgenes '
                      '(a) Sharpe − 0,4, (b) Sharpe con costos ×2, (c) 0,3 − ρ con R1, (d) ΔSharpe R1 + manga − 0,1, '
                      '(e) ΔSharpe R1 + C6alts(H) + manga vs R1 + C6alts(H) − 0,05 (PROTOCOL_R61 §4)')
def q3(ctx):
    import json
    import r59_holdout as hg
    import r61
    n2 = {u['symbol'] for u in json.load(open(hg._LIST_FILES[0]))['selected']}
    src_of = lambda s: r58.N2_DIR if s in n2 else r58.N3_DIR  # noqa: E731
    return r61.q3_compute(hg.holdout_syms(), src_of, r61.selected_variant())


# ----------------------------------------------------------------------------------------------
# r62 q4 (PROTOCOL_R62.md §7.3.5), committed before the query. The program itself is read from
# data/r62/q4_program.json, which F3 writes and commits before calling the oracle.
# ----------------------------------------------------------------------------------------------
@register('q4', 0.05, 'r62 F3: finalista cripto de la fábrica (congelado en data/r62/q4_program.json) sobre las 50 '
                      'alts de H a 1 h, 2021-07-02 → 2024-12-31; márgenes (a) Sharpe − 0,3, (b) Sharpe con costos ×2, '
                      '(c) ΔSharpe 0,85·P55 + 0,15·x̃ contra P55 (PROTOCOL_R62 §7.3.5)')
def q4(ctx):
    import json
    import r59_holdout as hg
    import r62
    n2 = {u['symbol'] for u in json.load(open(hg._LIST_FILES[0]))['selected']}
    dir_of = lambda s: r58.N2_DIR if s in n2 else r58.N3_DIR  # noqa: E731
    with open(r62.Q4_PROGRAM, encoding='utf-8') as f:
        program = json.load(f)['program']
    return r62.q4_compute(hg.holdout_syms(), dir_of, program)
