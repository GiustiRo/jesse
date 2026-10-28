"""r62: synthetic multi-asset histories (PROTOCOL_R62 §7.1).

Each generator returns `(src, oi)` in the same shape as the real panel (r62_data.load per asset
and the OI z-score feed), on the real calendar, so r62_eval.Panel runs unchanged on them.

  noise    real vol path x jointly shuffled standardised shocks: no predictable mean.
  planted  noise + P1 (reversal after 2.5-sigma 1h shocks on BTC/ETH) + P2 (OU log-spread WTI/GAS).
  regimes  stationary bootstrap of whole days (mean block 20) chained by BTC T90 states.
"""
import os

import numpy as np

import r62_data
import r62_dsl as dsl

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = r62_data.CORE
HOUR, DAY = dsl.HOUR, dsl.DAY
EWMA_SPAN = 24
P1_Z, P1_BARS = 2.5, 6
P2_HALF_LIFE = 120


def _ewma_sigma(lr, span=EWMA_SPAN):
    """Sigma known before each bar (EWMA of squared returns up to t-1)."""
    a = 2 / (span + 1)
    out = np.empty(len(lr))
    v = np.nanvar(lr[:500]) if np.isfinite(lr[:500]).any() else 1e-6
    for i, x in enumerate(lr):
        out[i] = np.sqrt(v)
        if np.isfinite(x):
            v = (1 - a) * v + a * x * x
    return out


def real_inputs():
    """Real bars, their log returns, prior-bar sigma and OI z, per core asset."""
    src = {n: r62_data.load(n) for n in ASSETS}
    oi = {}
    for n, sym in (('BTC', 'BTCUSDT'), ('ETH', 'ETHUSDT')):
        z = np.load(os.path.join(HERE, 'data', 'r62', f'oi_{sym}.npz'))
        oi[n] = (z['ht'], z['z_doi'])
    return src, oi


def _union_index(src):
    t = np.unique(np.concatenate([src[n]['h1'][:, 0].astype(np.int64) for n in ASSETS]))
    return t


def _rebuild(h, lr_new, src_rows):
    """Bars from new log returns: O = previous close, H/L keep the source bar's relative range."""
    c = h[0, 4] * np.exp(np.cumsum(np.nan_to_num(lr_new)))
    o = np.r_[h[0, 1], c[:-1]]
    sh = src_rows
    up = sh[:, 2] / np.maximum(sh[:, 1], sh[:, 4])
    dn = sh[:, 3] / np.minimum(sh[:, 1], sh[:, 4])
    hi = np.maximum(o, c) * np.where(np.isfinite(up) & (up >= 1), up, 1.0)
    lo = np.minimum(o, c) * np.where(np.isfinite(dn) & (dn <= 1), dn, 1.0)
    return np.c_[h[:, 0], o, hi, lo, c, h[:, 5]]


def noise(seed, real=None, planted=None):
    """§7.1 'ruido' (and 'plantado' when `planted` = {'kappa': .., 'alpha': ..})."""
    src, oi = real or real_inputs()
    rng = np.random.default_rng(seed)
    U = _union_index(src)
    perm = rng.permutation(len(U))
    out_src, out_oi = {}, {}
    zs = {}
    for n in ASSETS:
        h = src[n]['h1']
        t = h[:, 0].astype(np.int64)
        lr = np.r_[np.nan, np.diff(np.log(h[:, 4]))]
        sig = _ewma_sigma(lr)
        z = lr / sig
        z = z - np.nanmean(z)
        # shock of union slot u -> asset's bar at U[perm[u]] when it exists, else a random own bar
        pos = np.full(len(U), -1)
        pos[np.searchsorted(U, t)] = np.arange(len(t))
        my_u = np.searchsorted(U, t)
        srcpos = pos[perm[my_u]]
        miss = (srcpos < 0) | ~np.isfinite(z[np.clip(srcpos, 0, None)])
        srcpos[miss] = rng.choice(np.flatnonzero(np.isfinite(z)), miss.sum())
        srcpos[0] = 0
        zn = z[srcpos]
        zn[0] = 0.0                          # the first bar has no return (and NaN would poison P2)
        zs[n] = (zn, sig, srcpos)
    if planted:
        _plant(zs, src, planted)
    for n in ASSETS:
        h = src[n]['h1']
        zn, sig, srcpos = zs[n]
        lr_new = sig * zn
        lr_new[0] = 0.0
        bars = _rebuild(h, lr_new, h[srcpos])
        d = {'h1': bars, 'd1': r62_data.hours_to_days(bars, cfd=n not in dsl.CRYPTO)}
        if 'funding' in src[n]:
            d['funding'] = src[n]['funding']
        out_src[n] = d
        if n in oi:
            ht, zoi = oi[n]
            # the OI z of the same source bar travels with its shock (contemporaneous link kept)
            t = h[:, 0].astype(np.int64)
            j = np.searchsorted(ht, t + HOUR)
            ok = (j < len(ht)) & (ht[np.clip(j, 0, len(ht) - 1)] == t + HOUR)
            zoi_bar = np.where(ok, zoi[np.clip(j, 0, len(ht) - 1)], np.nan)
            out_oi[n] = ((t + HOUR).astype(np.int64), zoi_bar[srcpos])
    return out_src, out_oi


def _plant(zs, src, planted):
    """P1: after |z| > 2.5 on BTC/ETH, the next 6 bars drift back by kappa * z / 6 (in z units).
    P2: the WTI/GAS equal-vol spread becomes OU with a 120-bar half-life, strength alpha."""
    k = planted.get('kappa', 0.0)
    for n in ('BTC', 'ETH'):
        z, sig, sp = zs[n]
        z = z.copy()
        hit = np.flatnonzero(np.abs(z) > P1_Z)
        for i in hit:
            z[i + 1:i + 1 + P1_BARS] -= k * z[i] / P1_BARS
        zs[n] = (z, sig, sp)
    a = planted.get('alpha', 0.0)
    if a > 0:
        tw = src['WTI']['h1'][:, 0].astype(np.int64)
        tg = src['GAS']['h1'][:, 0].astype(np.int64)
        common, iw, ig = np.intersect1d(tw, tg, return_indices=True)
        zw, zg = zs['WTI'][0], zs['GAS'][0].copy()
        theta = 1 - 0.5 ** (1 / P2_HALF_LIFE)
        s = 0.0
        for kk in range(len(common)):
            dz = zw[iw[kk]] - zg[ig[kk]]
            pull = -a * theta * s               # alpha = 1 is an exact OU with a 120-bar half-life
            zg[ig[kk]] -= pull / 2
            zs['WTI'][0][iw[kk]] += pull / 2
            s = s + dz + pull
        zs['GAS'] = (zg, zs['GAS'][1], zs['GAS'][2])


def btc_t90_from(src):
    """r55 states_b on the (synthetic) BTC daily closes: applied day -> T90."""
    d = src['BTC']['d1']
    t, c = d[:, 0].astype(np.int64), d[:, 4]
    lc = np.log(c)
    lr = np.r_[np.nan, np.diff(lc)]
    out_t, out_v = [], []
    for i in range(90, len(t)):
        sd = np.std(lr[i - 89:i + 1], ddof=1)
        out_t.append(t[i] + DAY)
        out_v.append((lc[i] - lc[i - 90]) / (sd * np.sqrt(90)))
    return np.array(out_t, np.int64), np.array(out_v)


# ----------------------------------------------------------------------------------------------
# 'regimes': stationary bootstrap of whole days, chained by BTC T90 states (F3 filter)
# ----------------------------------------------------------------------------------------------
def regimes(seed, real=None, block=20):
    src, oi = real or real_inputs()
    rng = np.random.default_rng(seed)
    st = np.load(os.path.join(HERE, 'data', 'r55', 'f0_states.npy'))
    sday, sv = st[:, 0].astype(np.int64), st[:, 2]
    state = np.where(sv >= 0.5, 2, np.where(sv <= -0.5, 0, 1))
    first = max(int(src[n]['h1'][0, 0]) for n in ('BTC', 'ETH')) // DAY * DAY + DAY
    days = np.arange(first, 1_735_689_600_000, DAY)
    sd_idx = np.searchsorted(sday, days)
    ok = (sd_idx < len(sday)) & (sday[np.clip(sd_idx, 0, len(sday) - 1)] == days)
    dstate = np.where(ok, state[np.clip(sd_idx, 0, len(sday) - 1)], 1)
    P = np.ones((3, 3))
    for a, b in zip(dstate[:-1], dstate[1:]):
        P[a, b] += 1
    P /= P.sum(1, keepdims=True)
    by_state = [np.flatnonzero(dstate == s) for s in range(3)]
    # target timeline: the real calendar of each asset (CFDs from 2017-10, crypto from 2020-01)
    t0 = min(int(src[n]['h1'][0, 0]) for n in ASSETS) // DAY * DAY
    tdays = np.arange(t0, 1_735_689_600_000, DAY)
    pick = np.empty(len(tdays), int)
    cur = rng.choice(len(days))
    s = dstate[cur]
    for i in range(len(tdays)):
        if i == 0 or rng.random() < 1 / block or cur + 1 >= len(days):
            s = rng.choice(3, p=P[s])
            cur = rng.choice(by_state[s])
        else:
            cur += 1
            s = dstate[cur]
        pick[i] = cur
    shift = tdays - days[pick]                       # ms to add to a source day's stamps
    out_src, out_oi = {}, {}
    for n in ASSETS:
        h = src[n]['h1']
        hd = h[:, 0].astype(np.int64) // DAY * DAY
        lr = np.r_[0.0, np.diff(np.log(h[:, 4]))]
        rows, lrs, srows = [], [], []
        starts = np.searchsorted(hd, days[pick])
        ends = np.searchsorted(hd, days[pick] + DAY)
        for i, (a0, b0) in enumerate(zip(starts, ends)):
            if tdays[i] < int(h[0, 0]) // DAY * DAY:
                continue                              # before the asset's real history
            if b0 > a0:
                rows.append(h[a0:b0, 0] + shift[i])
                lrs.append(lr[a0:b0])
                srows.append(np.arange(a0, b0))
        t = np.concatenate(rows)
        lrn = np.concatenate(lrs)
        sr = np.concatenate(srows)
        lrn[0] = 0.0
        lrn = np.clip(lrn, -0.5, 0.5)
        base = h[sr].copy()
        base[:, 0] = t
        bars = _rebuild(base, lrn, h[sr])
        d = {'h1': bars, 'd1': r62_data.hours_to_days(bars, cfd=n not in dsl.CRYPTO)}
        if 'funding' in src[n]:
            f = src[n]['funding']
            fd = f[:, 0].astype(np.int64) // DAY * DAY
            fr = []
            for i in range(len(tdays)):
                a0, b0 = np.searchsorted(fd, [days[pick[i]], days[pick[i]] + DAY])
                if b0 > a0:
                    fr.append(np.c_[f[a0:b0, 0] + shift[i], f[a0:b0, 1]])
            d['funding'] = np.concatenate(fr)
        out_src[n] = d
        if n in oi:
            ht, zoi = oi[n]
            j = np.searchsorted(ht, h[sr, 0].astype(np.int64) + HOUR)
            okk = (j < len(ht)) & (ht[np.clip(j, 0, len(ht) - 1)] == h[sr, 0] + HOUR)
            out_oi[n] = ((t + HOUR).astype(np.int64), np.where(okk, zoi[np.clip(j, 0, len(ht) - 1)], np.nan))
    return out_src, out_oi


def panel(kind, seed, real=None, planted=None):
    """r62_eval.Panel on a synthetic history; BTC T90 recomputed from the synthetic BTC."""
    import r62_eval as ev
    if kind == 'regimes':
        s, o = regimes(seed, real)
    else:
        s, o = noise(seed, real, planted if kind == 'planted' else None)
    return ev.Panel(s, btc_t90_from(s), o)
