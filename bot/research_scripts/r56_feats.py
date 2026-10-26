"""r56 feature families (PROTOCOL_R56 section 5). Every array is (days x coins) and causal: the value
at row t uses data up to the close of day t only. r56_eval.truncation_test checks this for every
static family by recomputing on a panel cut at random days.

Static families take the panel dict P (from r56_eval.load) and return {name: array}. Fitted families
(C, V3) take the panel, the fold start index d0 and the development-coin mask: their models are fitted
on rows before d0 (development coins only) and then run forward (filtered) over the whole history.
"""
import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import sliding_window_view

import r56_models as md
from r56_panel import _roll_sum, _shift

np.seterr(divide='ignore', invalid='ignore')


def _df(x):
    return pd.DataFrame(x)


def _lr(P):
    return np.log(P['c']) - np.log(_shift(P['c'], -1))


def _std(x, n, minp=None):
    return _df(x).rolling(n, min_periods=minp or n).std().values


def _true_range(P):
    prev = _shift(P['c'], -1)
    return np.fmax(P['h'] - P['l'], np.fmax(np.abs(P['h'] - prev), np.abs(P['l'] - prev)))


def _vol_norm_returns(P):
    """Daily log returns over their trailing 365-day std (min 90): pools coins of different vol."""
    r = _lr(P)
    return r / _shift(_std(r, 365, 90), -1)


# ----------------------------------------------------------------------------------------------
# A. Classics
# ----------------------------------------------------------------------------------------------
def fam_A1(P):
    """Trend: ADX(14), Kaufman efficiency 10/20/60, T-scores 20/60/90 (signed and absolute)."""
    Hh, Ll, C = P['h'], P['l'], P['c']
    up, dn = Hh - _shift(Hh, -1), _shift(Ll, -1) - Ll
    pdm = np.where((up > dn) & (up > 0), up, 0.0)
    mdm = np.where((dn > up) & (dn > 0), dn, 0.0)
    tr = _true_range(P)
    bad = np.isnan(tr)
    pdm[bad], mdm[bad] = np.nan, np.nan
    w = lambda x: _df(x).ewm(alpha=1 / 14, adjust=False, min_periods=14).mean().values
    atr = w(tr)
    pdi, mdi = 100 * w(pdm) / atr, 100 * w(mdm) / atr
    dx = 100 * np.abs(pdi - mdi) / (pdi + mdi)
    out = {'adx14': w(dx)}
    steps = np.abs(C - _shift(C, -1))
    for n in (10, 20, 60):
        out[f'er{n}'] = np.abs(C - _shift(C, -n)) / _roll_sum(steps, n)
    r = _lr(P)
    for n in (20, 60, 90):
        t = (np.log(C) - np.log(_shift(C, -n))) / (_std(r, n) * np.sqrt(n))
        out[f't{n}'], out[f'abs_t{n}'] = t, np.abs(t)
    return out


def fam_T90(P):
    """Baseline from r55: the T90 score, signed and absolute (no N_regime cost)."""
    a = fam_A1(P)
    return {'t90': a['t90'], 'abs_t90': a['abs_t90']}


def fam_A2(P):
    """Compression: Bollinger width and its 252-day percentile, BB/KC squeeze ratio, Donchian/ATR,
    choppiness(14), 20-day RV percentile in the coin's year, short over long RV."""
    C, Hh, Ll, A = P['c'], P['h'], P['l'], P['atr']
    sd20 = _std(C, 20)
    sma20 = _df(C).rolling(20).mean().values
    bbw = 4 * sd20 / sma20
    out = {'bbw': bbw, 'bbw_pct252': _df(bbw).rolling(252, min_periods=126).rank(pct=True).values}
    out['squeeze'] = (4 * sd20) / (3 * A)          # BB(2 sd) width over Keltner(1.5 ATR) width
    hi20, lo20 = _df(Hh).rolling(20).max().values, _df(Ll).rolling(20).min().values
    out['donch20_atr'] = (hi20 - lo20) / A
    tr = _true_range(P)
    hi14, lo14 = _df(Hh).rolling(14).max().values, _df(Ll).rolling(14).min().values
    out['chop14'] = 100 * np.log10(_roll_sum(tr, 14) / (hi14 - lo14)) / np.log10(14)
    import r56_panel as pn
    rv20 = _roll_sum(P['rv'], 20)
    out['rv20_pct365'] = pn.vol_level(rv20, 20)[0]
    out['rv5_rv20'] = np.log(_roll_sum(P['rv'], 5) / 5) - np.log(rv20 / 20)
    return out


def fam_A3(P):
    return {**fam_A1(P), **fam_A2(P)}


# ----------------------------------------------------------------------------------------------
# B. Memory
# ----------------------------------------------------------------------------------------------
def fam_B1(P):
    """Variance ratios VR(5), VR(10) over 60 days; lag-1 autocorrelation of returns (20, 60 days)
    and of absolute returns (60 days)."""
    r = _lr(P)
    var60 = _df(r).rolling(60).var().values
    out = {}
    for q in (5, 10):
        rq = _roll_sum(r, q)
        out[f'vr{q}'] = _df(rq).rolling(60).var().values / (q * var60)
    R, R1 = _df(r), _df(_shift(r, -1))
    out['ac1_20'] = R.rolling(20).corr(R1).values
    out['ac1_60'] = R.rolling(60).corr(R1).values
    A, A1 = _df(np.abs(r)), _df(np.abs(_shift(r, -1)))
    out['acabs_60'] = A.rolling(60).corr(A1).values
    return out


def dfa_hurst(x, win=128, scales=(4, 8, 16, 32)):
    """Rolling DFA-1 Hurst exponent over `win` days (NaN if any value in the window is missing)."""
    D, M = x.shape
    out = np.full(x.shape, np.nan)
    ls = np.log(scales)
    lc = ls - ls.mean()
    for j in range(M):
        w = sliding_window_view(x[:, j], win)
        ok = ~np.isnan(w).any(axis=1)
        w = np.where(ok[:, None], w, 0.0)
        prof = np.cumsum(w - w.mean(axis=1, keepdims=True), axis=1)
        logF = []
        for s in scales:
            seg = prof.reshape(len(w), win // s, s)
            tc = np.arange(s) - (s - 1) / 2
            slope = (seg * tc).sum(-1) / (tc ** 2).sum()
            fit = seg.mean(-1, keepdims=True) + slope[..., None] * tc
            logF.append(0.5 * np.log(((seg - fit) ** 2).mean(axis=(1, 2))))
        logF = np.stack(logF, axis=1)
        H = (logF * lc).sum(1) / (lc ** 2).sum()
        out[win - 1:, j] = np.where(ok, H, np.nan)
    return out


def fam_B2(P):
    r = _lr(P)
    return {'hurst_r128': dfa_hurst(r), 'hurst_absr128': dfa_hurst(np.abs(r))}


# ----------------------------------------------------------------------------------------------
# D. BOCPD
# ----------------------------------------------------------------------------------------------
def fam_D1(P):
    """BOCPD (hazard 1/60) on vol-normalised returns and on standardised log daily RV: log expected
    run length and the posterior mass on run lengths < 5."""
    z = _vol_norm_returns(P)
    lrv = np.log(P['rv'])
    m365 = _shift(_df(lrv).rolling(365, min_periods=90).mean().values, -1)
    s365 = _shift(_std(lrv, 365, 90), -1)
    zv = (lrv - m365) / s365
    out = {k: np.full(z.shape, np.nan) for k in ('bo_r_rl', 'bo_r_ps', 'bo_v_rl', 'bo_v_ps')}
    for j in range(z.shape[1]):
        for x, pre in ((z[:, j], 'bo_r'), (zv[:, j], 'bo_v')):
            x = np.where(np.isfinite(x), x, np.nan)
            rl, ps = md.bocpd(x, hazard=1 / 60)
            out[f'{pre}_rl'][:, j] = np.log1p(rl)
            out[f'{pre}_ps'][:, j] = ps
    return out


# ----------------------------------------------------------------------------------------------
# E. Geometry with fixed definitions
# ----------------------------------------------------------------------------------------------
def _rolling_reg(y, n):
    """Rolling OLS of y on 0..n-1: slope and R^2 at the window's last row."""
    D, M = y.shape
    slope, r2 = np.full(y.shape, np.nan), np.full(y.shape, np.nan)
    x = np.arange(n) - (n - 1) / 2
    sxx = (x ** 2).sum()
    for j in range(M):
        w = sliding_window_view(y[:, j], n)
        b = (w * x).sum(1) / sxx
        res = w - w.mean(1, keepdims=True) - b[:, None] * x
        tss = ((w - w.mean(1, keepdims=True)) ** 2).sum(1)
        slope[n - 1:, j] = b
        r2[n - 1:, j] = 1 - (res ** 2).sum(1) / tss
    return slope, r2


def fam_E1(P):
    """Channel (log-price regression slope over daily vol and R^2, 20 and 50 days) and range box
    (Donchian 50 / ATR, touches of the 20-day high/low band, position inside the 20-day box)."""
    C, Hh, Ll, A = P['c'], P['h'], P['l'], P['atr']
    r = _lr(P)
    out = {}
    for n in (20, 50):
        b, r2 = _rolling_reg(np.log(C), n)
        out[f'ch_slope{n}'] = b / _std(r, n)
        out[f'ch_r2_{n}'] = r2
    hi20, lo20 = _df(Hh).rolling(20).max().values, _df(Ll).rolling(20).min().values
    hi50, lo50 = _df(Hh).rolling(50).max().values, _df(Ll).rolling(50).min().values
    out['donch50_atr'] = (hi50 - lo50) / A
    near = (Hh >= hi20 - 0.25 * A) | (Ll <= lo20 + 0.25 * A)
    out['touches20'] = _df(np.where(np.isnan(A), np.nan, near.astype(float))).rolling(20).sum().values
    out['box_pos20'] = (C - lo20) / (hi20 - lo20)
    return out


def fam_E2(P):
    """Flag (impulse >= 2 ATR over days t-19..t-10 followed by a consolidation under half its range)
    and Wyckoff-lite (box after a >= 25% drop from the 90-day high plus a spring: a low under the
    prior 20-day floor in the last 3 days with a close back above it)."""
    C, Hh, Ll, A = P['c'], P['h'], P['l'], P['atr']
    imp = (_shift(C, -10) - _shift(C, -20)) / _shift(A, -10)
    hi10, lo10 = _df(Hh).rolling(10).max().values, _df(Ll).rolling(10).min().values
    prev_rng = _shift(hi10, -10) - _shift(lo10, -10)
    cons = (hi10 - lo10) / prev_rng
    flag = ((np.abs(imp) >= 2) & (cons < 0.5)).astype(float) * np.sign(imp)
    rng_n = (Hh - Ll) / A
    rs, _ = _rolling_reg(rng_n, 10)
    dd90 = C / _df(Hh).rolling(90, min_periods=60).max().values - 1
    hi20, lo20 = _df(Hh).rolling(20).max().values, _df(Ll).rolling(20).min().values
    base = ((hi20 - lo20) / A <= 4).astype(float)
    floor = _shift(_df(Ll).rolling(20).min().values, -3)
    low3 = _df(Ll).rolling(3).min().values
    spring = ((low3 < floor) & (C > floor)).astype(float)
    wyck = ((dd90 <= -0.25) & (base > 0) & (spring > 0)).astype(float)
    since = np.full(C.shape, 20.0)
    for j in range(C.shape[1]):
        last = -10 ** 9
        for t in range(C.shape[0]):
            if spring[t, j] > 0:
                last = t
            since[t, j] = min(20, t - last)
    nanm = np.isnan(A) | np.isnan(floor)
    out = {'impulse': imp, 'cons_ratio': cons, 'flag': flag, 'rng_slope10': rs, 'dd90': dd90,
           'base_box': base, 'spring': spring, 'wyckoff': wyck, 'since_spring': since}
    for k in ('flag', 'base_box', 'spring', 'wyckoff', 'since_spring'):
        out[k] = np.where(nanm, np.nan, out[k])
    return out


# ----------------------------------------------------------------------------------------------
# S. Path signatures
# ----------------------------------------------------------------------------------------------
def _batched_sig3(paths):
    """Level 1..3 signatures of N piecewise-linear paths (N x points x d), Chen's identity."""
    N, n, d = paths.shape
    S1, S2, S3 = np.zeros((N, d)), np.zeros((N, d, d)), np.zeros((N, d, d, d))
    for i in range(n - 1):
        e1 = paths[:, i + 1] - paths[:, i]
        e2 = np.einsum('ni,nj->nij', e1, e1) / 2
        e3 = np.einsum('nij,nk->nijk', e2, e1) / 3
        S3 = S3 + np.einsum('nij,nk->nijk', S2, e1) + np.einsum('ni,njk->nijk', S1, e2) + e3
        S2 = S2 + np.einsum('ni,nj->nij', S1, e1) + e2
        S1 = S1 + e1
    return np.concatenate([S1, S2.reshape(N, -1), S3.reshape(N, -1)], axis=1)


def fam_S1(P):
    """Level-3 signatures over 20 and 60 days of (time, log price / window vol, log RV relative to
    its window mean), each path starting at the window's first day."""
    C, RV = P['c'], P['rv']
    D, M = C.shape
    lc, lrv = np.log(C), np.log(RV)
    r = _lr(P)
    out = {}
    for n in (20, 60):
        sd = _std(r, n)
        rows = [(t, j) for t in range(n, D) for j in range(M)]
        T = np.array([t for t, _ in rows])
        J = np.array([j for _, j in rows])
        idx = T[:, None] + np.arange(-n, 1)[None, :]
        p_lc = lc[idx, J[:, None]]
        p_lv = lrv[idx, J[:, None]]
        ok = np.isfinite(p_lc).all(1) & np.isfinite(p_lv).all(1) & np.isfinite(sd[T, J]) & (sd[T, J] > 0)
        time = np.broadcast_to(np.linspace(0, 1, n + 1), p_lc.shape)
        x1 = (p_lc - p_lc[:, :1]) / np.where(ok, sd[T, J], 1)[:, None] / np.sqrt(n)
        x2 = p_lv - np.nanmean(np.where(np.isfinite(p_lv), p_lv, np.nan), axis=1, keepdims=True)
        paths = np.stack([time, np.where(ok[:, None], x1, 0), np.where(ok[:, None], x2, 0)], axis=2)
        sig = _batched_sig3(paths)
        for k in range(sig.shape[1]):
            a = np.full((D, M), np.nan)
            a[T[ok], J[ok]] = sig[ok, k]
            out[f'sig{n}_{k}'] = a
    return out


# ----------------------------------------------------------------------------------------------
# Fitted families: state models (C) and Markov HAR (V3)
# ----------------------------------------------------------------------------------------------
def jm_inputs(P):
    """Jump-model inputs: EWMA return / vol (half-lives 5, 21), EWMA downside deviation, EWMA log
    vol, drawdown from the 60-day high, all on vol-normalised returns (pooled across coins)."""
    z = _vol_norm_returns(P)
    Z = _df(z)
    cols = {}
    for h in (5, 21):
        mu = Z.ewm(halflife=h, min_periods=h).mean().values
        vol = np.sqrt((Z ** 2).ewm(halflife=h, min_periods=h).mean().values)
        dd = np.sqrt((Z.clip(upper=0) ** 2).ewm(halflife=h, min_periods=h).mean().values)
        cols[f'mu{h}'], cols[f'lvol{h}'], cols[f'dd{h}'] = mu, np.log(vol), np.log(dd + 1e-6)
    C = P['c']
    cols['dd60'] = C / _df(C).rolling(60, min_periods=30).max().values - 1
    return cols


def sjm_inputs(P):
    """Broad set for the sparse jump model: jm_inputs plus trend, compression and memory features."""
    a1, a2, b1 = fam_A1(P), fam_A2(P), fam_B1(P)
    extra = {k: a1[k] for k in ('adx14', 'er20', 'er60', 't20', 't60')}
    extra.update({k: a2[k] for k in ('bbw_pct252', 'squeeze', 'donch20_atr', 'chop14', 'rv20_pct365')})
    extra.update({k: b1[k] for k in ('vr5', 'ac1_60')})
    return {**jm_inputs(P), **extra}


def _stack(cols):
    names = sorted(cols)
    return np.stack([cols[k] for k in names], axis=2), names


def _vec_forward(L, lam):
    """Discrete JM forward over all coins at once. L: (D, M, k) losses (0 where no data)."""
    D, M, k = L.shape
    V = np.empty_like(L)
    back = np.empty((D, M, k), dtype=np.int8)
    V[0] = L[0]
    back[0] = np.arange(k)
    pen = lam * (1 - np.eye(k))
    for t in range(1, D):
        cand = V[t - 1][:, :, None] + pen[None]           # (M, from, to)
        best = cand.min(axis=1)
        # Staying wins ties, as in r52_j1 and r56_models.jm_forward.
        diag = cand[:, np.arange(k), np.arange(k)]
        back[t] = np.where(diag <= best, np.arange(k)[None, :], cand.argmin(axis=1))
        V[t] = L[t] + best
    return V, back


def _vec_viterbi(L, lam):
    V, back = _vec_forward(L, lam)
    D, M, k = L.shape
    s = np.empty((D, M), dtype=np.int8)
    s[-1] = V[-1].argmin(1)
    for t in range(D - 1, 0, -1):
        s[t - 1] = back[t, np.arange(M), s[t]]
    return s, float(V[-1].min(1).sum())


def _losses(X, valid, mu, w=None):
    d = (X[:, :, None, :] - mu[None, None]) ** 2
    if w is not None:
        d = d * w
    L = d.sum(-1)
    L[~valid] = 0.0
    return L


def jm_fit_panel(X, valid, k, lam, restarts=3, max_iter=20, seed=0, w=None):
    """Pooled JM over the panel (each coin is its own path; rows without data carry no loss)."""
    rng = np.random.default_rng(seed)
    pts = X[valid]
    best = None
    for _ in range(restarts):
        mu = md.kmeanspp(pts[rng.choice(len(pts), min(len(pts), 20000), replace=False)], k, rng)
        prev = None
        for _ in range(max_iter):
            s, obj = _vec_viterbi(_losses(X, valid, mu, w), lam)
            mu = np.array([X[valid & (s == j)].mean(0) if (valid & (s == j)).any() else mu[j] for j in range(k)])
            if prev is not None and np.array_equal(s[valid], prev):
                break
            prev = s[valid].copy()
        s, obj = _vec_viterbi(_losses(X, valid, mu, w), lam)
        if best is None or obj < best[0]:
            best = (obj, mu, s)
    return best


def cjm_online_panel(X, valid, mu, lam, step, w=None):
    """CJM filtered probability vectors for every coin and day (NaN where no data)."""
    k = len(mu)
    grid = md.simplex_grid(k, step)
    L = _losses(X, valid, mu, w) @ grid.T                      # (D, M, G)
    Dm = np.abs(grid[:, None, :] - grid[None, :, :]).sum(-1)
    pen = lam / 4 * Dm ** 2
    D, M, G = L.shape
    V = np.empty_like(L)
    V[0] = L[0]
    for t in range(1, D):
        V[t] = L[t] + (V[t - 1][:, :, None] + pen[None]).min(axis=1)
    P = grid[V.argmin(-1)]
    P[~valid] = np.nan
    return P


def standardise(X, train_rows):
    m, s = np.nanmean(X[train_rows], axis=0), np.nanstd(X[train_rows], axis=0)
    return (X - m) / np.where(s > 0, s, 1)


def sparse_weights(X, valid, s, k, kappa):
    """Witten-Tibshirani weights: maximise sum w_j BCSS_j with ||w||_2 <= 1 and ||w||_1 <= kappa."""
    pts, lab = X[valid], s[valid]
    tot = ((pts - pts.mean(0)) ** 2).sum(0)
    wcss = sum(((pts[lab == j] - pts[lab == j].mean(0)) ** 2).sum(0) for j in range(k) if (lab == j).any())
    b = np.maximum(tot - wcss, 0)

    def w_of(delta):
        a = np.maximum(b - delta, 0)
        return a / np.linalg.norm(a) if a.any() else a
    w = w_of(0.0)
    if np.abs(w).sum() > kappa:
        lo, hi = 0.0, b.max()
        for _ in range(60):
            mid = (lo + hi) / 2
            if np.abs(w_of(mid)).sum() > kappa:
                lo = mid
            else:
                hi = mid
        w = w_of(hi)
    return w
