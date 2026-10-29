"""r63 F1: synthetic alt panels with the real panel's layout (PROTOCOL_R63 §6).

* noise: each tramo's real causal 1h vol (EWMA 24) x standardized shocks. The shocks come from one
  permutation of the union of hours shared by every tramo, so contemporaneous cross-correlation
  survives where two tramos both have the source hour; a tramo without a bar at its source hour
  draws one of its own shocks at random. Mean 0, so nothing is predictable in the mean.
* planted: noise + P1 (fade after a shock) on 20% of the D63 symbols only: after |z| > 2.5 the
  next 6 bars drift back by kappa * z / 6 (in z units).
Volume, funding, eligibility, slippage tiers and tramo ends are the real ones, so the synthetic
book trades exactly the assets and costs the real one does.
"""
import numpy as np

import r62_synth as s62
import r63_eval as E6

P1_SHARE, P1_SEED = 0.20, 6300
P1_Z, P1_BARS = 2.5, 6
# Oracle program of §6: shock fade z 3, no filters, time exit 6 bars, both sides, maker off 0.25 life 1.
ORACLE = {'universe': 'alts_1h', 'signal': [{'kind': 'shock', 'params': {'mode': 'fade', 'z': 3}}],
          'filters': [], 'exit': {'kind': 'time', 'params': {'h': 6}},
          'size': {'kind': 'voltgt', 'params': {'side': 'both'}},
          'exec': {'kind': 'maker', 'params': {'off': 0.25, 'life': 1}}}


def planted_syms(names):
    syms = sorted({E6.sym_of(n) for n in names})
    rng = np.random.default_rng(P1_SEED)
    k = int(round(P1_SHARE * len(syms)))
    return set(rng.choice(syms, size=k, replace=False).tolist())


def panel_src(real_src, seed, kappa=0.0):
    """Synthetic src dict (same keys and layout as real_src); kappa > 0 plants P1."""
    rng = np.random.default_rng(seed)
    names = sorted(real_src)
    U = np.unique(np.concatenate([real_src[n]['h1'][:, 0].astype(np.int64) for n in names]))
    perm = rng.permutation(len(U))
    plant = planted_syms(names) if kappa > 0 else set()
    out = {}
    for n in names:
        s = real_src[n]
        h = s['h1']
        t = h[:, 0].astype(np.int64)
        lr = np.r_[np.nan, np.diff(np.log(h[:, 4]))]
        sig = s62._ewma_sigma(lr)
        with np.errstate(invalid='ignore', divide='ignore'):
            z = lr / sig
        ok = np.isfinite(z)
        z = z - z[ok].mean()
        my_u = np.searchsorted(U, t)
        src_t = U[perm[my_u]]
        srcpos = np.searchsorted(t, src_t)
        have = (srcpos < len(t)) & (t[np.clip(srcpos, 0, len(t) - 1)] == src_t)
        srcpos = np.where(have, srcpos, -1)
        miss = (srcpos < 0) | ~ok[np.clip(srcpos, 0, None)]
        srcpos[miss] = rng.choice(np.flatnonzero(ok), int(miss.sum()))
        zn = z[srcpos]
        zn[0] = 0.0
        if E6.sym_of(n) in plant:
            for i in np.flatnonzero(np.abs(zn) > P1_Z):
                zn[i + 1:i + 1 + P1_BARS] -= kappa * zn[i] / P1_BARS
        lr_new = np.nan_to_num(sig * zn)
        lr_new[0] = 0.0
        bars = s62._rebuild(h[:, :6], lr_new, h[srcpos])
        g = h.copy()
        g[:, 1:5] = bars[:, 1:5]
        d = dict(s)
        d['h1'] = g
        d['d1'] = E6.daily_bars(g)
        out[n] = d
    return out
