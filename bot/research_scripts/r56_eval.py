"""r56 evaluation engine: walk-forward fitting, scores, inference, registry and phases (PROTOCOL_R56).

* Rows: coin-days with a label, both baselines, eligibility and day >= 2021-07-01. Development coins
  only until F5; holdout coins are scored once, in F5, by models trained on development coins.
* Walk-forward: one model per test quarter (2021Q3..2024Q4), trained on development-coin rows whose
  label window closed at least H days before the quarter (row day <= quarter start - 2H).
* Each configuration is a pooled regularised multinomial logistic (C = 1) over its own features;
  missing values take the training median, values are clipped to the training 1-99% range and
  standardised (G2 is the fixed gradient boosting of the protocol).
* Primary score: Brier skill score against the better of persistence and climatology on the same
  rows. Inference: Diebold-Mariano on the daily cross-sectional mean of the Brier improvement with
  a stationary bootstrap (mean block 20 days, 2000 draws) and Hansen's SPA over the configurations.

    python research_scripts/r56_eval.py register F1   # write the phase's specs to the registry
    python research_scripts/r56_eval.py run F1        # fit, score, save data/r56/<phase>.json
    python research_scripts/r56_eval.py spa           # SPA over every configuration scored so far
"""
import json
import os
import sys
import time
import warnings

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

import r56_feats as ft
import r56_panel as pn

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r56')
REG = os.path.join(HERE, '..', 'strategies', 'FundingOiPilot4h', 'reports', 'TRIAL_REGISTRY.json')
DAY = 86_400_000
H = pn.H
EVAL_FROM, DEV_TO, VAL_FROM = '2021-07-01', '2023-12-31', '2024-01-01'
EMBARGO = 2 * H
AXES = pn.AXES
TARGET = {'vol': 2, 'trend': 1, 'range': 0}   # transition class for the lead-time metric
N_BOOT, BLOCK = 2000, 20
TRUNC_DATES, TRUNC_COINS = 20, 6

warnings.filterwarnings('ignore')
np.seterr(divide='ignore', invalid='ignore')
_CTX = {}


# ----------------------------------------------------------------------------------------------
# Data
# ----------------------------------------------------------------------------------------------
def ms(day):
    return int(pd.Timestamp(day, tz='UTC').value // 10**6)


def ctx():
    if _CTX:
        return _CTX
    z = np.load(os.path.join(OUT, 'panel.npz'))
    P = {k: z[k] for k in ('o', 'h', 'l', 'c', 'rv', 'qv', 'atr')}
    P['elig'] = z['elig']
    days, syms = z['day_ms'], [str(s) for s in z['syms']]
    L = dict(np.load(os.path.join(OUT, 'labels.npz')))
    hold = json.load(open(os.path.join(OUT, 'holdout.json')))['holdout']
    is_hold = np.array([s in hold for s in syms])
    q = pd.date_range(EVAL_FROM, '2024-10-01', freq='QS', tz='UTC')
    qidx = [int(np.searchsorted(days, t.value // 10**6)) for t in q] + [len(days)]
    years = pd.to_datetime(days, unit='ms', utc=True).year.values
    _CTX.update(P=P, days=days, syms=syms, L=L, is_hold=is_hold, qidx=qidx, years=years)
    return _CTX


def eval_mask(axis, coins='dev'):
    c = ctx()
    L = c['L']
    m = (c['P']['elig'] & np.isfinite(L[f'y_{axis}']) & np.isfinite(L[f'persist_{axis}'])
         & np.isfinite(L[f'clim_{axis}']).all(-1) & (c['days'] >= ms(EVAL_FROM))[:, None])
    cm = ~c['is_hold'] if coins == 'dev' else c['is_hold']
    return m & cm[None, :]


def period_rows(period):
    d = ctx()['days']
    if period == 'dev':
        return (d >= ms(EVAL_FROM)) & (d <= ms(DEV_TO))
    if period == 'val':
        return d >= ms(VAL_FROM)
    return d >= ms(EVAL_FROM)


# ----------------------------------------------------------------------------------------------
# Walk-forward fitting
# ----------------------------------------------------------------------------------------------
def _prep(Xtr):
    med = np.nanmedian(Xtr, axis=0)
    med = np.where(np.isfinite(med), med, 0.0)
    lo, hi = np.nanpercentile(Xtr, 1, axis=0), np.nanpercentile(Xtr, 99, axis=0)
    lo, hi = np.where(np.isfinite(lo), lo, 0.0), np.where(np.isfinite(hi), hi, 0.0)

    def f(X):
        X = np.where(np.isfinite(X), X, med)
        return np.clip(X, lo, hi)
    Z = f(Xtr)
    m, s = Z.mean(0), Z.std(0)
    s = np.where(s > 0, s, 1.0)
    return lambda X: (f(X) - m) / s


def _model(kind, n_cls):
    if kind == 'gbm':
        from sklearn.ensemble import HistGradientBoostingClassifier
        return HistGradientBoostingClassifier(max_iter=200, learning_rate=0.05, max_leaf_nodes=15,
                                              min_samples_leaf=200, l2_regularization=1.0, random_state=0)
    return LogisticRegression(C=1.0, max_iter=3000)


def fit_predict(feats, axis, coins='dev', kind='logit'):
    """feats: callable(qi, q0) -> (D, M, f) array for that fold. Returns (D, M, n_cls) predictions."""
    c = ctx()
    n_cls = AXES[axis] if axis in AXES else 2
    y = c['L'][f'y_{axis}'] if axis in AXES else c['L'][axis]
    D, M = y.shape
    preds = np.full((D, M, n_cls), np.nan)
    test_all = eval_mask(axis, coins) if axis in AXES else xmask(coins)
    train_base = c['P']['elig'] & np.isfinite(y) & (~c['is_hold'])[None, :]
    di = np.arange(D)[:, None]
    for qi in range(len(c['qidx']) - 1):
        q0, q1 = c['qidx'][qi], c['qidx'][qi + 1]
        F = feats(qi, q0)
        tr = train_base & (di <= q0 - EMBARGO)
        te = test_all & (di >= q0) & (di < q1)
        if not te.any():
            continue
        prep = _prep(F[tr])
        mdl = _model(kind, n_cls)
        mdl.fit(prep(F[tr]), y[tr].astype(int))
        p = np.zeros((int(te.sum()), n_cls))
        p[:, mdl.classes_.astype(int)] = mdl.predict_proba(prep(F[te]))
        preds[te] = p
    return preds


def static(fam_fn, name):
    """Cache a static family to data/r56/feat_<name>.npz; returns (array, names)."""
    path = os.path.join(OUT, f'feat_{name}.npz')
    if os.path.exists(path):
        z = np.load(path)
        names = [str(s) for s in z['names']]
        return z['X'], names
    cols = fam_fn(ctx()['P'])
    X, names = ft._stack(cols)
    X = np.where(np.isfinite(X), X, np.nan).astype(np.float32)
    np.savez_compressed(path, X=X, names=np.array(names))
    return X, names


def truncation_test(fam_fn, seed=56):
    """Recompute the family on panels cut at random days (6 development coins) and compare."""
    c = ctx()
    P = c['P']
    rng = np.random.default_rng(seed)
    dev_cols = np.where(~c['is_hold'])[0]
    cols = np.sort(rng.choice(dev_cols, TRUNC_COINS, replace=False))
    D = len(c['days'])
    taus = np.sort(rng.choice(np.arange(400, D), TRUNC_DATES, replace=False))
    sub = {k: v[:, cols] for k, v in P.items()}
    full = fam_fn(sub)
    worst = 0.0
    for tau in taus:
        cut = fam_fn({k: v[:tau + 1] for k, v in sub.items()})
        for k, v in full.items():
            a, b = v[tau], cut[k][tau]
            same_nan = np.isnan(a) == np.isnan(b)
            if not same_nan.all():
                return False, f'{k}: NaN pattern differs at row {tau}'
            ok = ~np.isnan(a)
            if ok.any():
                worst = max(worst, float(np.max(np.abs(a[ok] - b[ok]) / (1 + np.abs(a[ok])))))
    return worst < 1e-8, f'max relative gap {worst:.2e} over {TRUNC_DATES} cut dates'


# ----------------------------------------------------------------------------------------------
# Scores and inference
# ----------------------------------------------------------------------------------------------
def onehot(y, n):
    return pn.onehot(y, n)


def stationary_idx(n, rng):
    idx = np.empty(n, dtype=int)
    idx[0] = rng.integers(n)
    jump = rng.random(n) < 1 / BLOCK
    starts = rng.integers(n, size=n)
    for t in range(1, n):
        idx[t] = starts[t] if jump[t] else (idx[t - 1] + 1) % n
    return idx


_BOOT = {}


def boot_indices(n):
    if n not in _BOOT:
        rng = np.random.default_rng(560)
        _BOOT[n] = np.array([stationary_idx(n, rng) for _ in range(N_BOOT)])
    return _BOOT[n]


def dm_pvalue(g):
    """One-sided p of mean(g) <= 0 by the recentred stationary bootstrap of the mean."""
    g = g[np.isfinite(g)]
    I = boot_indices(len(g))
    m = g.mean()
    mb = g[I].mean(axis=1)
    return float(((mb - m) >= m).mean())


def spa_pvalue(G):
    """Hansen (2005) SPA_c p-value; G is (days x configurations) of Brier improvements."""
    G = G[np.isfinite(G).all(1)]
    n = len(G)
    I = boot_indices(n)
    gbar = G.mean(0)
    gb = np.stack([G[I[:, :], k].mean(1) for k in range(G.shape[1])], axis=1)   # (B, K)
    omega = np.sqrt(n) * gb.std(0)
    omega = np.where(omega > 0, omega, 1e-12)
    T = max(float((np.sqrt(n) * gbar / omega).max()), 0.0)
    # Z* = d* - g_c(dbar): configurations that are not clearly worse are recentred at the null
    # boundary (zero); clearly worse ones keep their negative mean and barely enter the maximum.
    very_neg = np.sqrt(n) * gbar / omega < -np.sqrt(2 * np.log(np.log(n)))
    Tb = np.maximum((np.sqrt(n) * (gb - gbar + gbar * very_neg) / omega).max(1), 0.0)
    return float((Tb >= T).mean())


def _lead(y, s, tgt, mask):
    """Median lead (days) of the state s entering class tgt against label transitions into tgt."""
    leads = []
    D, M = y.shape
    for j in range(M):
        for i in range(1, D):
            if not (mask[i, j] and mask[i - 1, j] and y[i, j] == tgt and y[i - 1, j] != tgt):
                continue
            a, b = max(i - 20, 0), min(i + 21, D)
            hit = np.where(mask[a:b, j] & (s[a:b, j] == tgt))[0]
            if not len(hit):
                leads.append(-21)
                continue
            jj = a + hit[0]
            if jj == i - 20 and i - 21 >= 0 and mask[i - 21, j] and s[i - 21, j] == tgt:
                leads.append(20)
            else:
                leads.append(i - jj)
    return float(np.median(leads)) if leads else float('nan'), len(leads)


def _switches(s, mask):
    out = []
    for j in range(s.shape[1]):
        v = s[mask[:, j], j]
        if len(v) > 60:
            out.append((np.diff(v) != 0).sum() / len(v) * 365)
    return float(np.mean(out)) if out else float('nan')


def evaluate(preds, axis, coins='dev', period='dev'):
    c = ctx()
    L = c['L']
    n = AXES[axis]
    m = eval_mask(axis, coins) & period_rows(period)[:, None] & np.isfinite(preds).all(-1)
    y = L[f'y_{axis}']
    oh = onehot(y, n)
    pers = onehot(L[f'persist_{axis}'], n)
    clim = L[f'clim_{axis}']
    Bm = ((preds - oh) ** 2).sum(-1)
    Bp = ((pers - oh) ** 2).sum(-1)
    Bc = ((clim - oh) ** 2).sum(-1)
    best_name = 'persistence' if Bp[m].mean() < Bc[m].mean() else 'climatology'
    Bb = Bp if best_name == 'persistence' else Bc
    bss = 1 - Bm[m].mean() / Bb[m].mean()
    yi = np.where(m, y, 0).astype(int)
    pt = np.take_along_axis(np.where(m[..., None], preds, 1.0), yi[..., None], -1)[..., 0]
    logloss = float(-np.log(np.clip(pt[m], 1e-12, 1)).mean())
    s = np.where(m, np.nanargmax(np.where(m[..., None], preds, 0), -1), -1)
    ba = pn.balanced_accuracy(s[m].astype(float), y[m], n)
    slopes = []
    for k in range(n):
        x, t = preds[..., k][m], oh[..., k][m]
        vx = x.var()
        slopes.append(float(((x - x.mean()) * (t - t.mean())).mean() / vx) if vx > 0 else float('nan'))
    tgt = TARGET[axis]
    lead_m, n_tr = _lead(y, s, tgt, m)
    sp = np.where(m, L[f'persist_{axis}'], -1)
    lead_p, _ = _lead(y, sp, tgt, m)
    g = np.where(m, Bb - Bm, np.nan)
    with np.errstate(all='ignore'):
        gd = np.nanmean(g, axis=1)
    gd = gd[np.isfinite(gd)]
    years = c['years']
    by_year = {}
    for yr in np.unique(years[m.any(1)]):
        mm = m & (years == yr)[:, None]
        by_year[str(int(yr))] = round(float(1 - Bm[mm].mean() / Bb[mm].mean()), 4)
    coin_bss = []
    for j in range(m.shape[1]):
        mj = m[:, j]
        if mj.sum() >= 100:
            coin_bss.append(1 - Bm[mj, j].mean() / Bb[mj, j].mean())
    return {
        'n_rows': int(m.sum()), 'best_baseline': best_name,
        'brier': {'model': round(float(Bm[m].mean()), 4), 'persistence': round(float(Bp[m].mean()), 4),
                  'climatology': round(float(Bc[m].mean()), 4)},
        'bss': round(float(bss), 4), 'logloss': round(logloss, 4), 'balanced_accuracy': round(ba, 4),
        'calibration_slopes': [round(x, 3) for x in slopes],
        'switches_per_year': round(_switches(s, m), 2),
        'lead_median': {'model': lead_m, 'persistence': lead_p, 'n_transitions': n_tr},
        'bss_by_year': by_year,
        'coin_bss_pos_share': round(float(np.mean(np.array(coin_bss) > 0)), 4) if coin_bss else None,
        'dm_p': round(dm_pvalue(gd), 4), 'mean_daily_gain': float(gd.mean()),
    }, gd


# ----------------------------------------------------------------------------------------------
# Configurations
# ----------------------------------------------------------------------------------------------
def static_feats(*fams):
    Xs = [static(f, n)[0] for f, n in fams]
    X = np.concatenate(Xs, axis=2)
    return lambda qi, q0: X


SPECS = {
    'T90': {'phase': 'F1', 'baseline': True, 'axes': list(AXES),
            'spec': 'Vara r55 (sin costo): logística sobre T90 firmado y absoluto.',
            'feats': lambda: static_feats((ft.fam_T90, 'T90'))},
    'A1': {'phase': 'F1', 'axes': list(AXES),
           'spec': 'Logística sobre ADX(14, Wilder), eficiencia de Kaufman 10/20/60 y T-score ln(P/P-n)/(sd_n*sqrt(n)) a 20/60/90, firmados y absolutos (10 variables).',
           'feats': lambda: static_feats((ft.fam_A1, 'A1'))},
    'A2': {'phase': 'F1', 'axes': list(AXES),
           'spec': 'Logística sobre ancho de Bollinger(20, 2) y su percentil de 252 días, squeeze = ancho BB / ancho Keltner(1,5 ATR20), Donchian20/ATR20, choppiness(14), percentil de la RV20 en el año de la moneda y ln(RV5/RV20) (7 variables).',
           'feats': lambda: static_feats((ft.fam_A2, 'A2'))},
    'A3': {'phase': 'F1', 'axes': list(AXES),
           'spec': 'Logística sobre A1 + A2 (17 variables).',
           'feats': lambda: static_feats((ft.fam_A1, 'A1'), (ft.fam_A2, 'A2'))},
    'B1': {'phase': 'F1', 'axes': list(AXES),
           'spec': 'Logística sobre VR(5) y VR(10) en 60 días, autocorrelación lag 1 de retornos (20 y 60 días) y de |retornos| (60 días) (5 variables).',
           'feats': lambda: static_feats((ft.fam_B1, 'B1'))},
    'B2': {'phase': 'F1', 'axes': list(AXES),
           'spec': 'Logística sobre Hurst DFA-1 de 128 días (escalas 4/8/16/32) de retornos y de |retornos| (2 variables).',
           'feats': lambda: static_feats((ft.fam_B2, 'B2'))},
}
# ----------------------------------------------------------------------------------------------
# Fitted families (F2): state models refitted at each fold on development coins before d0
# ----------------------------------------------------------------------------------------------
LAM_GRID = (10.0, 50.0, 200.0)
LAM_DEFAULT = 50.0
INNER_DAYS = 365
CJM_STEP = {2: 0.05, 3: 0.1}
FOLD_LOG = {}


def _fold_cache(cid, qi, build):
    path = os.path.join(OUT, f'fold_{cid}_{qi}.npy')
    if os.path.exists(path):
        return np.load(path)
    X = build().astype(np.float32)
    np.save(path, X)
    return X


def _panel_inputs(name, fn):
    """Stacked (D, M, p) inputs and their names, computed once per process."""
    if name not in _CTX:
        _CTX[name] = ft._stack(fn(ctx()['P']))
    return _CTX[name]


def _cjm_probs(X, fit_valid, all_valid, k, lam, w=None):
    obj, mu, s = ft.jm_fit_panel(X, fit_valid, k, lam, w=w)
    return ft.cjm_online_panel(X, all_valid, mu, lam, CJM_STEP[k], w=w)


def _inner_lambda(Xs, valid, k, q0):
    """Pick lambda by summed log-loss over the three axes on the year before the embargo."""
    c = ctx()
    D = len(c['days'])
    di = np.arange(D)[:, None]
    split = q0 - INNER_DAYS
    first = int(np.argmax(valid.any(1)))
    if split - first < 365:
        return LAM_DEFAULT, None
    dev = (~c['is_hold'])[None, :]
    scores = {}
    for lam in LAM_GRID:
        Pk = _cjm_probs(Xs, valid & dev & (di < split), valid, k, lam)
        tot = 0.0
        for axis in AXES:
            y = c['L'][f'y_{axis}']
            base = c['P']['elig'] & np.isfinite(y) & dev & np.isfinite(Pk).all(-1)
            tr = base & (di <= split - EMBARGO)
            va = base & (di > split) & (di <= q0 - EMBARGO)
            prep = _prep(Pk[tr])
            mdl = LogisticRegression(C=1.0, max_iter=3000).fit(prep(Pk[tr]), y[tr].astype(int))
            pr = np.full((int(va.sum()), AXES[axis]), 1e-12)
            pr[:, mdl.classes_.astype(int)] = mdl.predict_proba(prep(Pk[va]))
            tot += float(-np.log(np.clip(pr[np.arange(len(pr)), y[va].astype(int)], 1e-12, 1)).mean())
        scores[str(lam)] = round(tot, 5)
    return float(min(scores, key=scores.get)), scores


def cjm_feats(cid, k):
    def f(qi, q0):
        def build():
            c = ctx()
            X, _ = _panel_inputs('jm_X', ft.jm_inputs)
            di = np.arange(X.shape[0])[:, None]
            valid = np.isfinite(X).all(-1)
            fit = valid & (~c['is_hold'])[None, :] & (di < q0)
            Xs = np.where(valid[..., None], ft.standardise(X, fit), 0.0)
            lam, sc = _inner_lambda(Xs, valid, k, q0)
            FOLD_LOG[f'{cid}_{qi}'] = {'lambda': lam, 'inner_logloss': sc}
            return _cjm_probs(Xs, fit, valid, k, lam)
        return _fold_cache(cid, qi, build)
    return f


SJM_LAM, SJM_KAPPA, SJM_ROUNDS = 50.0, 3.0, 5


def sjm_feats(cid, k=3):
    def f(qi, q0):
        def build():
            c = ctx()
            X, names = _panel_inputs('sjm_X', ft.sjm_inputs)
            p = X.shape[2]
            di = np.arange(X.shape[0])[:, None]
            valid = np.isfinite(X).all(-1)
            fit = valid & (~c['is_hold'])[None, :] & (di < q0)
            Xs = np.where(valid[..., None], ft.standardise(X, fit), 0.0)
            w = np.ones(p) / np.sqrt(p)
            for _ in range(SJM_ROUNDS):
                obj, mu, s = ft.jm_fit_panel(Xs, fit, k, SJM_LAM, w=w)
                w = ft.sparse_weights(Xs, fit, s, k, SJM_KAPPA)
            obj, mu, s = ft.jm_fit_panel(Xs, fit, k, SJM_LAM, w=w)
            FOLD_LOG[f'{cid}_{qi}'] = {'weights': {n: round(float(x), 4) for n, x in zip(names, w) if x > 0}}
            return ft.cjm_online_panel(Xs, valid, mu, SJM_LAM, CJM_STEP[k], w=w)
        return _fold_cache(cid, qi, build)
    return f


def returns_4h():
    """(D, M, 6) 4h log returns per UTC day from the r52 1h klines, cut at 2024-12-31."""
    if 'r4' in _CTX:
        return _CTX['r4']
    c = ctx()
    D, M = len(c['days']), len(c['syms'])
    t0 = int(c['days'][0])
    out = np.full((D * 6, M), np.nan)
    for j, sname in enumerate(c['syms']):
        a = np.load(os.path.join(pn.SRC, f'{sname}_1h.npy'))
        a = a[(a[:, 0] >= t0) & (a[:, 0] <= pn.CUT_MS)]
        hr = ((a[:, 0] - t0) // 3_600_000).astype(int)
        cl = np.full(D * 24, np.nan)
        cl[hr] = a[:, 4]
        c4 = cl.reshape(D * 6, 4)[:, -1]
        out[1:, j] = np.diff(np.log(c4))
    _CTX['r4'] = out.reshape(D, 6, M).transpose(0, 2, 1)
    return _CTX['r4']


WK_K, WK_DAYS, WK_EVERY = 3, 20, 5


def wk_windows():
    """(D, M, 120) vol-normalised 4h returns of days t-19..t (NaN rows where any is missing)."""
    if 'wk' in _CTX:
        return _CTX['wk']
    c = ctx()
    r4 = returns_4h()
    D, M, _ = r4.shape
    sd = ft._shift(ft._std(ft._lr(c['P']), 365, 90), -1) / np.sqrt(6)
    z = r4 / sd[..., None]
    W = np.full((D, M, WK_DAYS * 6), np.nan, dtype=np.float32)
    for t in range(WK_DAYS - 1, D):
        W[t] = z[t - WK_DAYS + 1:t + 1].transpose(1, 0, 2).reshape(M, -1)
    _CTX['wk'] = W
    return W


def wk_feats(cid):
    import r56_models as md

    def f(qi, q0):
        def build():
            c = ctx()
            W = wk_windows()
            D = W.shape[0]
            valid = np.isfinite(W).all(-1)
            di = np.arange(D)[:, None]
            fit = valid & (~c['is_hold'])[None, :] & (di < q0) & (di % WK_EVERY == 0)
            lab, C = md.wk_means(np.clip(W[fit], -10, 10), WK_K)
            Q = np.sort(np.clip(np.where(valid[..., None], W, 0), -10, 10), axis=-1)
            d2 = np.stack([((Q - C[j]) ** 2).mean(-1) for j in range(WK_K)], axis=-1)
            d2[~valid] = np.nan
            return d2
        return _fold_cache(cid, qi, build)
    return f


def hmm_feats(cid, k=3):
    from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression

    def f(qi, q0):
        def build():
            c = ctx()
            z = np.clip(ft._vol_norm_returns(c['P']), -10, 10)
            D, M = z.shape
            segs = []
            for j in np.where(~c['is_hold'])[0]:
                x = z[:q0, j]
                ok = np.where(np.isfinite(x))[0]
                if len(ok) > 60:
                    segs.append(np.nan_to_num(x[ok[0]:]))
            mdl = MarkovRegression(np.concatenate(segs), k_regimes=k, trend='c', switching_variance=True)
            res = mdl.fit(disp=False, maxiter=300, search_reps=5)
            params = np.asarray(res.params)
            FOLD_LOG[f'{cid}_{qi}'] = {'params': [round(float(x), 5) for x in params]}
            out = np.full((D, M, k), np.nan)
            for j in range(M):
                x = z[:, j]
                ok = np.where(np.isfinite(x))[0]
                if len(ok) < 30:
                    continue
                a = ok[0]
                fm = MarkovRegression(np.nan_to_num(x[a:]), k_regimes=k, trend='c', switching_variance=True)
                pr = np.asarray(fm.filter(params).filtered_marginal_probabilities)
                out[a:, j] = pr if pr.shape[-1] == k else pr.T
            # Regimes sorted by variance so the columns mean the same in every fold.
            return out[..., np.argsort(params[-k:])]
        return _fold_cache(cid, qi, build)
    return f


SPECS.update({
    'C1a': {'phase': 'F2', 'axes': list(AXES),
            'spec': 'Jump model continuo, 2 estados, agrupado sobre las monedas de desarrollo con datos < inicio del pliegue. Entradas (estandarizadas en el ajuste): sobre retornos normalizados por la vol de 365 días, EWMA de retorno, log-vol y log-downside con vida media 5 y 21, más drawdown desde el máximo de 60 días (7 variables). Centros por coordinate descent (JM discreto, 3 reinicios k-means++, 20 iteraciones). Probabilidades filtradas por el DP del CJM (grilla del símplex con paso 0,05). λ en {10, 50, 200} por log-loss sumada de los tres ejes en el año previo al embargo (λ = 50 si no hay un año de ajuste interno). Logística sobre las probabilidades.',
            'feats': lambda: cjm_feats('C1a', 2)},
    'C1b': {'phase': 'F2', 'axes': list(AXES),
            'spec': 'Igual que C1a con 3 estados (grilla del símplex con paso 0,1).',
            'feats': lambda: cjm_feats('C1b', 3)},
    'C2': {'phase': 'F2', 'axes': list(AXES),
           'spec': 'Sparse jump model, 3 estados, sobre las entradas de C1 más ADX, ER20/60, T20/60, percentil de ancho BB, squeeze, Donchian/ATR, choppiness, percentil de RV20, VR5 y AC1_60 (19 variables). Pesos Witten–Tibshirani (norma 2 ≤ 1, norma 1 ≤ κ = 3) alternados con el ajuste del JM 5 veces. λ = 50 fijo. Probabilidades filtradas por el CJM con los pesos (paso 0,1). Logística sobre las probabilidades.',
           'feats': lambda: sjm_feats('C2', 3)},
    'C3': {'phase': 'F2', 'axes': list(AXES),
           'spec': 'Wasserstein k-means 1D (p = 2), k = 3, sobre ventanas de 20 días de retornos de 4h normalizados por la vol diaria de 365 días/√6 (120 observaciones, recortadas a ±10). Ajuste sobre ventanas de las monedas de desarrollo antes del pliegue, una cada 5 días (10 reinicios). Variables: distancias W2² de la ventana actual a los 3 centroides. Logística sobre las distancias.',
           'feats': lambda: wk_feats('C3')},
    'C4': {'phase': 'F2', 'axes': list(AXES),
           'spec': 'Vara: HMM gaussiano de 3 regímenes (statsmodels MarkovRegression, media y varianza conmutadas, search_reps = 5), ajustado sobre los retornos normalizados (±10) concatenados de las monedas de desarrollo antes del pliegue. Probabilidades solo filtradas por moneda con los parámetros ajustados, ordenadas por varianza. Logística sobre las probabilidades.',
           'feats': lambda: hmm_feats('C4', 3)},
    'D1': {'phase': 'F2', 'axes': list(AXES),
           'spec': 'BOCPD (Adams–MacKay, Normal–Gamma, hazard 1/60, run length truncado en 400) sobre retornos normalizados por la vol de 365 días y sobre la log-RV diaria estandarizada con media/desvío de 365 días: log(1 + run length esperado) y masa posterior en run lengths < 5 (4 variables). Logística.',
           'feats': lambda: static_feats((ft.fam_D1, 'D1'))},
})

STATIC_FAMS = {'T90': [ft.fam_T90], 'A1': [ft.fam_A1], 'A2': [ft.fam_A2], 'A3': [], 'B1': [ft.fam_B1],
               'B2': [ft.fam_B2], 'D1': [ft.fam_D1]}


# ----------------------------------------------------------------------------------------------
# Registry and phases
# ----------------------------------------------------------------------------------------------
def _reg_load():
    return json.loads(open(REG, encoding='utf-8').read())


def _reg_save(d):
    open(REG, 'w', encoding='utf-8').write(json.dumps(d, indent=2, ensure_ascii=False))


def register(phase):
    d = _reg_load()
    rt = d['regime_trials']
    done = {t['id'] for t in rt['trials']}
    for cid, sp in SPECS.items():
        if sp['phase'] != phase or sp.get('baseline') or cid in done:
            continue
        rt['n_regime'] += 1
        assert rt['n_regime'] <= rt['ceiling'], 'N_regime ceiling exceeded'
        rt['trials'].append({'id': cid, 'phase': phase, 'n_regime_after': rt['n_regime'],
                             'registered': time.strftime('%Y-%m-%d', time.gmtime()),
                             'axes': sp['axes'], 'model': sp.get('model', 'logit'), 'spec': sp['spec'],
                             'status': 'registrada, sin resultado'})
        for x in rt['declared_plan']:
            if x['id'] == cid:
                x['status'] = 'especificada en trials'
    _reg_save(d)
    print('N_regime =', rt['n_regime'])


def run(phase):
    os.makedirs(OUT, exist_ok=True)
    res_path = os.path.join(OUT, f'{phase.lower()}.json')
    res = json.load(open(res_path)) if os.path.exists(res_path) else {}
    reg = _reg_load()
    registered = {t['id'] for t in reg['regime_trials']['trials']}
    for cid, sp in SPECS.items():
        if sp['phase'] != phase or cid in res:
            continue
        assert sp.get('baseline') or cid in registered, f'{cid} is not registered'
        t0 = time.time()
        trunc = {}
        for fam in STATIC_FAMS.get(cid, []):
            ok, msg = truncation_test(fam)
            trunc[fam.__name__] = msg
            assert ok, f'truncation test failed for {fam.__name__}: {msg}'
        feats = sp['feats']()
        out = {'truncation': trunc, 'axes': {}}
        series = {}
        for axis in sp['axes']:
            preds = fit_predict(feats, axis, kind=sp.get('model', 'logit'))
            np.save(os.path.join(OUT, f'pred_{cid}_{axis}.npy'), preds.astype(np.float32))
            ev = {}
            for period in ('dev', 'val'):
                ev[period], gd = evaluate(preds, axis, 'dev', period)
                series[f'{axis}_{period}'] = gd
            out['axes'][axis] = ev
        out['fold_log'] = {k: v for k, v in FOLD_LOG.items() if k.startswith(cid + '_')}
        out['seconds'] = round(time.time() - t0, 1)
        np.savez(os.path.join(OUT, f'gain_{cid}.npz'), **series)
        res[cid] = out
        json.dump(res, open(res_path, 'w'), indent=2)
        print(cid, json.dumps({a: {p: (v[p]['bss'], v[p]['balanced_accuracy']) for p in v}
                               for a, v in out['axes'].items()}), out['seconds'], 's', flush=True)
        if not sp.get('baseline'):
            d = _reg_load()
            for t in d['regime_trials']['trials']:
                if t['id'] == cid:
                    t['status'] = 'evaluada'
                    t['result'] = {a: {p: {'bss': v[p]['bss'], 'dm_p': v[p]['dm_p']} for p in v}
                                   for a, v in out['axes'].items()}
            _reg_save(d)


def spa(period='dev'):
    """SPA per axis over every registered configuration scored so far (baselines excluded)."""
    d = _reg_load()
    ids = [t['id'] for t in d['regime_trials']['trials'] if t['status'] == 'evaluada']
    out = {}
    for axis in AXES:
        cols, names = [], []
        for cid in ids:
            p = os.path.join(OUT, f'gain_{cid}.npz')
            if os.path.exists(p):
                z = np.load(p)
                if f'{axis}_{period}' in z:
                    cols.append(z[f'{axis}_{period}'])
                    names.append(cid)
        if not cols:
            continue
        n = min(len(x) for x in cols)
        G = np.stack([x[:n] for x in cols], axis=1)
        out[axis] = {'configs': names, 'spa_p': round(spa_pvalue(G), 4)}
    json.dump(out, open(os.path.join(OUT, f'spa_{period}.json'), 'w'), indent=2)
    print(json.dumps(out, indent=2))
    return out


def main():
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == 'register':
        register(a[1])
    elif len(a) >= 2 and a[0] == 'run':
        run(a[1])
    elif a and a[0] == 'spa':
        spa(a[1] if len(a) > 1 else 'dev')
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
