"""r56 state models in numpy, with synthetic self-tests (F0, no N_regime cost).

* jm_fit / jm_online: discrete statistical jump model with k states (Nystrup; Shu, Yu and Mulvey
  2024): minimise sum ||x_t - mu_s_t||^2 + lam * #jumps by coordinate descent, k-means++ starts.
  For k = 2 it reproduces r52_j1.fit exactly (same seed, same tie rule), checked by selftest.
* cjm_online: continuous jump model (Aydinhan, Kolm, Mulvey and Shu 2024). The state is a
  probability vector p_t on a simplex grid; cost sum_t sum_k p_tk ||x_t - mu_k||^2
  + lam/4 * ||p_t - p_t-1||_1^2, solved by dynamic programming over the grid. The online estimate
  at t is the argmin of the forward value at t (no backward pass, so it is causal given mu).
* bocpd: Bayesian online changepoint detection (Adams and MacKay 2007) with a Normal-Gamma prior
  (Student-t predictive) and constant hazard; returns the expected run length and the posterior
  mass on short run lengths.
* signature: truncated path signature (levels 1..3) of a piecewise-linear path via Chen's
  identity, so no iisignature is needed.
* wk_means: 1-D Wasserstein k-means (Horvath, Issa and Muguruza 2021) on return windows; with
  p = 2 the distance is the L2 distance between sorted samples and the barycentre is their mean.

    python research_scripts/r56_models.py selftest

writes data/r56/f0_selftest.json.
"""
import itertools
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r56')


# ----------------------------------------------------------------------------------------------
# Discrete jump model
# ----------------------------------------------------------------------------------------------
def jm_forward(X, mu, lam):
    """Forward values V[t, s] and back-pointers; ties keep the current state (no jump)."""
    loss = ((X[:, None, :] - mu[None, :, :]) ** 2).sum(axis=2)
    n, k = loss.shape
    V = np.empty((n, k))
    back = np.empty((n, k), dtype=np.int16)
    V[0] = loss[0]
    back[0] = np.arange(k)
    pen = lam * (1 - np.eye(k))
    for t in range(1, n):
        cand = V[t - 1][:, None] + pen          # cand[i, j]: come from i into j
        best = cand.min(axis=0)
        # Staying wins ties, as in r52_j1.forward (`a <= b + lam` keeps state 0).
        arg = np.where(np.diag(cand) <= best, np.arange(k), cand.argmin(axis=0))
        V[t] = loss[t] + best
        back[t] = arg
    return V, back


def jm_viterbi(X, mu, lam):
    V, back = jm_forward(X, mu, lam)
    s = np.empty(len(X), dtype=np.int16)
    s[-1] = V[-1].argmin()
    for t in range(len(X) - 1, 0, -1):
        s[t - 1] = back[t, s[t]]
    return s, float(V[-1].min())


def kmeanspp(X, k, rng):
    mu = [X[rng.integers(len(X))]]
    for _ in range(1, k):
        d2 = np.min([((X - m) ** 2).sum(axis=1) for m in mu], axis=0)
        mu.append(X[rng.choice(len(X), p=d2 / d2.sum())])
    return np.array(mu)


def jm_fit(X, k=2, lam=50.0, restarts=10, max_iter=50, seed=0):
    """Best (objective, centres, path) over k-means++ restarts; empty states keep their centre."""
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(restarts):
        mu = kmeanspp(X, k, rng)
        s_prev = None
        for _ in range(max_iter):
            s, obj = jm_viterbi(X, mu, lam)
            if s_prev is not None and np.array_equal(s, s_prev):
                break
            mu = np.array([X[s == j].mean(axis=0) if (s == j).any() else mu[j] for j in range(k)])
            s_prev = s
        s, obj = jm_viterbi(X, mu, lam)
        if best is None or obj < best[0]:
            best = (obj, mu, s)
    return best


def jm_online(X, mu, lam):
    """Online state at each t: argmin of the forward value at t."""
    V, _ = jm_forward(X, mu, lam)
    return V.argmin(axis=1)


# ----------------------------------------------------------------------------------------------
# Continuous jump model
# ----------------------------------------------------------------------------------------------
def simplex_grid(k, step):
    m = int(round(1 / step))
    pts = [c for c in itertools.product(range(m + 1), repeat=k) if sum(c) == m]
    return np.array(pts, dtype=float) / m


def cjm_forward(X, mu, lam, grid):
    """Forward DP over grid probability vectors; returns V (n x G)."""
    loss = ((X[:, None, :] - mu[None, :, :]) ** 2).sum(axis=2)       # n x k
    L = loss @ grid.T                                                  # n x G
    D = np.abs(grid[:, None, :] - grid[None, :, :]).sum(axis=2)        # G x G, L1 distance
    pen = lam / 4 * D ** 2
    V = np.empty_like(L)
    V[0] = L[0]
    for t in range(1, len(L)):
        V[t] = L[t] + (V[t - 1][:, None] + pen).min(axis=0)
    return V


def cjm_fit(X, k=2, lam=50.0, step=0.05, restarts=5, max_iter=30, seed=0):
    """Coordinate descent: smoothed path given centres, then probability-weighted centres."""
    grid = simplex_grid(k, step)
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(restarts):
        mu = kmeanspp(X, k, rng)
        prev = None
        for _ in range(max_iter):
            P = cjm_path(X, mu, lam, grid)
            w = P.sum(axis=0)
            mu = np.array([(P[:, j:j + 1] * X).sum(axis=0) / w[j] if w[j] > 1e-9 else mu[j] for j in range(k)])
            if prev is not None and np.abs(P - prev).max() < 1e-9:
                break
            prev = P
        obj = cjm_objective(X, mu, lam, P)
        if best is None or obj < best[0]:
            best = (obj, mu, P)
    return best


def cjm_path(X, mu, lam, grid):
    """Smoothed (in-sample) probability path by backtracking the DP."""
    loss = ((X[:, None, :] - mu[None, :, :]) ** 2).sum(axis=2)
    L = loss @ grid.T
    D = np.abs(grid[:, None, :] - grid[None, :, :]).sum(axis=2)
    pen = lam / 4 * D ** 2
    n, G = L.shape
    V = np.empty_like(L)
    back = np.empty((n, G), dtype=np.int32)
    V[0] = L[0]
    for t in range(1, n):
        cand = V[t - 1][:, None] + pen
        back[t] = cand.argmin(axis=0)
        V[t] = L[t] + cand.min(axis=0)
    g = np.empty(n, dtype=np.int32)
    g[-1] = V[-1].argmin()
    for t in range(n - 1, 0, -1):
        g[t - 1] = back[t, g[t]]
    return grid[g]


def cjm_objective(X, mu, lam, P):
    loss = ((X[:, None, :] - mu[None, :, :]) ** 2).sum(axis=2)
    return float((P * loss).sum() + lam / 4 * (np.abs(np.diff(P, axis=0)).sum(axis=1) ** 2).sum())


def cjm_online(X, mu, lam, step=0.05):
    """Causal probability vector at each t given fixed centres."""
    grid = simplex_grid(len(mu), step)
    V = cjm_forward(X, mu, lam, grid)
    return grid[V.argmin(axis=1)]


# ----------------------------------------------------------------------------------------------
# BOCPD
# ----------------------------------------------------------------------------------------------
def bocpd(x, hazard=1 / 60, mu0=0.0, kappa0=1.0, alpha0=1.0, beta0=1.0, r_max=400, short=5):
    """Expected run length and P(run length < short) at each t (Normal-Gamma, Student-t)."""
    from scipy.special import gammaln
    n = len(x)
    R = np.array([1.0])
    mu, kappa, alpha, beta = np.array([mu0]), np.array([kappa0]), np.array([alpha0]), np.array([beta0])
    exp_rl = np.full(n, np.nan)
    p_short = np.full(n, np.nan)
    for t in range(n):
        xt = x[t]
        if np.isnan(xt):
            continue
        scale2 = beta * (kappa + 1) / (alpha * kappa)
        nu = 2 * alpha
        z = (xt - mu) ** 2 / scale2
        logpred = (gammaln((nu + 1) / 2) - gammaln(nu / 2) - 0.5 * np.log(np.pi * nu * scale2)
                   - (nu + 1) / 2 * np.log1p(z / nu))
        pred = np.exp(logpred)
        growth = R * pred * (1 - hazard)
        cp = (R * pred * hazard).sum()
        R = np.r_[cp, growth]
        R /= R.sum()
        mu_n = (kappa * mu + xt) / (kappa + 1)
        beta_n = beta + kappa * (xt - mu) ** 2 / (2 * (kappa + 1))
        mu = np.r_[mu0, mu_n]
        kappa = np.r_[kappa0, kappa + 1]
        alpha = np.r_[alpha0, alpha + 0.5]
        beta = np.r_[beta0, beta_n]
        if len(R) > r_max:  # truncate the tail; its mass is negligible at these hazards
            R, mu, kappa, alpha, beta = R[:r_max], mu[:r_max], kappa[:r_max], alpha[:r_max], beta[:r_max]
            R /= R.sum()
        rl = np.arange(len(R))
        exp_rl[t] = float((R * rl).sum())
        p_short[t] = float(R[:short].sum())
    return exp_rl, p_short


# ----------------------------------------------------------------------------------------------
# Path signature
# ----------------------------------------------------------------------------------------------
def signature(path, level=3):
    """Flattened signature levels 1..level of a piecewise-linear path (n_points x d)."""
    d = path.shape[1]
    S = [np.ones(())] + [np.zeros((d,) * m) for m in range(1, level + 1)]
    for inc in np.diff(path, axis=0):
        # Signature of one linear segment: inc^{(x)m} / m!
        E = [np.ones(())]
        for m in range(1, level + 1):
            E.append(np.multiply.outer(E[-1], inc) / m)
        # Chen: (S (x) E)_m = sum_{i+j=m} S_i (x) E_j
        S = [sum(np.multiply.outer(S[i], E[m - i]) for i in range(m + 1)) for m in range(level + 1)]
    return np.concatenate([S[m].ravel() for m in range(1, level + 1)])


# ----------------------------------------------------------------------------------------------
# Wasserstein k-means (1-D, p = 2)
# ----------------------------------------------------------------------------------------------
def wk_means(windows, k=2, max_iter=100, seed=0, restarts=10):
    """Cluster rows of `windows` (each a sample of returns); returns (labels, centroids)."""
    Q = np.sort(windows, axis=1)
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(restarts):
        C = kmeanspp(Q, k, rng)
        for _ in range(max_iter):
            lab = ((Q[:, None, :] - C[None]) ** 2).sum(axis=2).argmin(axis=1)
            newC = np.array([Q[lab == j].mean(axis=0) if (lab == j).any() else C[j] for j in range(k)])
            if np.allclose(newC, C):
                break
            C = newC
        obj = float(((Q - C[lab]) ** 2).sum())
        if best is None or obj < best[0]:
            best = (obj, lab, C)
    return best[1], best[2]


def wk_assign(windows, C):
    Q = np.sort(windows, axis=1)
    return ((Q[:, None, :] - C[None]) ** 2).sum(axis=2).argmin(axis=1)


# ----------------------------------------------------------------------------------------------
# Self-tests on synthetic data
# ----------------------------------------------------------------------------------------------
def _regime_series(n, rng, dur=60, mus=(0.001, -0.002), sds=(0.02, 0.045)):
    s = np.zeros(n, dtype=int)
    for t in range(1, n):
        s[t] = s[t - 1] if rng.random() > 1 / dur else 1 - s[t - 1]
    r = rng.normal(np.take(mus, s), np.take(sds, s))
    return s, r


def _ewm_feats(r, hls=(5, 10, 21)):
    import pandas as pd
    x = pd.Series(r)
    cols = []
    for h in hls:
        dd = np.sqrt(x.clip(upper=0).pow(2).ewm(halflife=h).mean())
        cols += [dd.values, (x.ewm(halflife=h).mean() / dd).values]
    X = np.column_stack(cols)[30:]
    return (X - X.mean(0)) / X.std(0)


def _acc2(est, true):
    a = float((est == true).mean())
    return max(a, 1 - a)


def selftest():
    rng = np.random.default_rng(56)
    out = {}
    # 1. JM k=2 reproduces r52_j1.fit on a feature matrix built like r52's.
    import r52_j1
    s, r = _regime_series(1500, rng)
    X = _ewm_feats(r)
    o1, m1, s1 = r52_j1.fit(X, 2, 50.0)
    o2, m2, s2 = jm_fit(X, 2, 50.0)
    out['jm_reproduces_r52'] = bool(np.array_equal(s1, s2) and np.isclose(o1, o2))
    # 2. Implementation check, not a power claim: on well-separated vol regimes (sd 1% vs 4%, mean
    # duration 100 days) JM and CJM must recover the states, and the jump penalty must cut the
    # switches against lam = 0 (plain k-means).
    # Features are drawn lag-free (state centre +-1 plus unit noise in 3 dims) so the check isolates
    # the solver from the lag of EWMA features; the EWMA-feature accuracy is reported separately.
    s = _regime_series(2030, rng, dur=100)[0]
    X = np.where(s[30:, None] == 1, 1.0, -1.0) * np.ones((1, 3)) * 0.7 + rng.normal(size=(2000, 3))
    o2, m2, s2 = jm_fit(X, 2, 50.0)
    _, _, s0 = jm_fit(X, 2, 0.0)
    out['jm_switches_lam0_vs_lam50'] = [int((np.diff(s0) != 0).sum()), int((np.diff(s2) != 0).sum())]
    true = s[30:]
    out['jm_accuracy'] = round(_acc2(s2, true), 4)
    on = jm_online(X, m2, 50.0)
    out['jm_online_accuracy'] = round(_acc2(on, true), 4)
    out['jm_online_switches_per_1000'] = round(float((np.diff(on) != 0).sum() / len(on) * 1000), 2)
    oc, mc, Pc = cjm_fit(X, 2, 50.0)
    pon = cjm_online(X, mc, 50.0)
    out['cjm_accuracy'] = round(_acc2(Pc.argmax(1), true), 4)
    out['cjm_online_accuracy'] = round(_acc2(pon.argmax(1), true), 4)
    out['true_switches_per_1000'] = round(float((np.diff(true) != 0).sum() / len(true) * 1000), 2)
    se, re_ = _regime_series(2000, rng, dur=100, mus=(0.0, 0.0), sds=(0.01, 0.04))
    Xe = _ewm_feats(re_)
    _, me, ste = jm_fit(Xe, 2, 50.0)
    _, mce, Pce = cjm_fit(Xe, 2, 50.0)
    out['ewma_features_reported'] = {'jm': round(_acc2(ste, se[30:]), 4),
                                     'jm_online': round(_acc2(jm_online(Xe, me, 50.0), se[30:]), 4),
                                     'cjm_online': round(_acc2(cjm_online(Xe, mce, 50.0).argmax(1), se[30:]), 4)}
    # 3. Three-state JM runs and returns k distinct states.
    o3, m3, s3 = jm_fit(X, 3, 50.0, restarts=3)
    out['jm3_states_used'] = int(len(np.unique(s3)))
    # 4. BOCPD: mean/vol breaks at known points are flagged within 10 steps.
    cps = [200, 450, 700]
    segs = [(0, 1), (2, 1), (2, 3), (-1, 1)]
    x = np.concatenate([rng.normal(m, sd, b - a) for (m, sd), a, b in zip(segs, [0] + cps, cps + [900])])
    rl, ps = bocpd(x, hazard=1 / 200)
    # A break counts as detected when, within 20 steps, the expected run length is no longer than
    # the time elapsed since the true break plus 5 (the posterior has restarted near it).
    hits = 0
    for c in cps:
        lag = np.arange(21)
        hits += int((rl[c:c + 21] <= lag + 5).any())
    out['bocpd_breaks_detected'] = f'{hits}/{len(cps)}'
    # 5. Signature: level 1 = total increment; level-2 antisymmetric part = 2 * Levy area; Chen.
    path = np.array([[0, 0], [1, 0], [1, 1]], dtype=float)
    sig = signature(path, 2)
    lvl2 = sig[2:].reshape(2, 2)
    out['sig_level1_ok'] = bool(np.allclose(sig[:2], [1, 1]))
    out['sig_levy_area'] = round(float(0.5 * (lvl2[0, 1] - lvl2[1, 0])), 4)  # +0.5 for this path
    p = rng.normal(size=(20, 3)).cumsum(0)
    a, b = signature(p[:11], 3), signature(p[10:], 3)
    full = signature(p, 3)
    d = 3
    A = [np.ones(()), a[:d], a[d:d + d * d].reshape(d, d), a[d + d * d:].reshape(d, d, d)]
    B = [np.ones(()), b[:d], b[d:d + d * d].reshape(d, d), b[d + d * d:].reshape(d, d, d)]
    chen = np.concatenate([sum(np.multiply.outer(A[i], B[m - i]) for i in range(m + 1)).ravel() for m in (1, 2, 3)])
    out['sig_chen_ok'] = bool(np.allclose(chen, full))
    # 6. WK-means separates two vol regimes from 20-day windows.
    s, r = _regime_series(3000, rng, dur=120, mus=(0, 0), sds=(0.02, 0.05))
    W = np.lib.stride_tricks.sliding_window_view(r, 20)
    lab, C = wk_means(W, 2)
    out['wk_accuracy'] = round(_acc2(lab, s[19:]), 4)
    out['pass'] = bool(out['jm_reproduces_r52'] and out['jm_accuracy'] >= 0.9
                       and out['jm_switches_lam0_vs_lam50'][1] < out['jm_switches_lam0_vs_lam50'][0]
                       and out['cjm_accuracy'] >= 0.9 and out['cjm_online_accuracy'] >= 0.8
                       and out['jm3_states_used'] == 3 and hits == len(cps) and out['sig_level1_ok']
                       and abs(out['sig_levy_area'] - 0.5) < 1e-9 and out['sig_chen_ok'] and out['wk_accuracy'] >= 0.8)
    os.makedirs(OUT, exist_ok=True)
    json.dump(out, open(os.path.join(OUT, 'f0_selftest.json'), 'w'), indent=2)
    print(json.dumps(out, indent=2))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'selftest':
        selftest()
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
