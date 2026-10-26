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
    python research_scripts/r56_eval.py f5            # one-time holdout scoring and the bridge
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
NCLS = {**AXES, 'exit': 2}   # 'exit' is the F4 range-exit direction label (X1)
TARGET = {'vol': 2, 'trend': 1, 'range': 0, 'exit': 1}   # transition class for the lead-time metric
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
    L.update(exit_labels(P, L, days))
    _CTX.update(P=P, days=days, syms=syms, L=L, is_hold=is_hold, qidx=qidx, years=years)
    return _CTX


def exit_labels(P, L, days):
    """X1 label: on days whose past window was a range (persist_range = 1, box c[t-20] +- k*ATR20[t-20]),
    the direction of the first close outside that box in t+1..t+20 (1 up, 0 down, NaN without exit).
    Baselines: the coin's last exit direction known at t (window closed by t) and its climatology."""
    k = json.load(open(os.path.join(OUT, 'f0_labels.json')))['thresholds']['k']
    C, A = P['c'], P['atr']
    box = L['persist_range'] == 1
    anchor, half = pn._shift(C, -H), k * pn._shift(A, -H)
    hi, lo = anchor + half, anchor - half
    y = np.full(C.shape, np.nan)
    for s in range(1, H + 1):
        fut = pn._shift(C, s)
        new = box & np.isnan(y)
        y = np.where(new & (fut > hi), 1.0, np.where(new & (fut < lo), 0.0, y))
    known = pd.DataFrame(pn._shift(y, -H)).ffill().values
    return {'y_exit': y, 'persist_exit': known, 'clim_exit': pn.climatology(y, 2, days, H)}


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
    n_cls = NCLS[axis]
    y = c['L'][f'y_{axis}']
    D, M = y.shape
    preds = np.full((D, M, n_cls), np.nan)
    test_all = eval_mask(axis, coins)
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
    n = NCLS[axis]
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

# ----------------------------------------------------------------------------------------------
# F3: volatility forecasts (V), geometry (E) and signatures (S)
# ----------------------------------------------------------------------------------------------
def har_inputs():
    """Log daily, weekly (5) and monthly (22) mean RV; the target log RV(t+1..t+20); the coin's
    1/3 and 2/3 quantiles of past 20-day RV sums (windows ending in the last 365 days, min 180)."""
    if 'har' in _CTX:
        return _CTX['har']
    P = ctx()['P']
    rv = P['rv']
    rv20 = pn._roll_sum(rv, 20)
    out = {'l_d': np.log(rv), 'l_w': np.log(pn._roll_sum(rv, 5) / 5), 'l_m': np.log(pn._roll_sum(rv, 22) / 22),
           'l_20': np.log(rv20)}
    R = ft._df(rv20).rolling(365, min_periods=180)
    out['thr_lo'], out['thr_hi'] = np.log(R.quantile(1 / 3).values), np.log(R.quantile(2 / 3).values)
    out['target'] = np.log(pn._shift(rv20, 20))
    _CTX['har'] = {k: np.where(np.isfinite(v), v, np.nan) for k, v in out.items()}
    return _CTX['har']


def _har_z(q0, extra=None):
    """Pooled HAR OLS on development rows with a closed target window before the embargo; returns
    the forecast's z-distance to the coin's tercile thresholds and the forecast minus log RV20."""
    c = ctx()
    h = har_inputs()
    cols = [h['l_d'], h['l_w'], h['l_m']] + (extra or [])
    X = np.stack(cols, -1)
    D = X.shape[0]
    di = np.arange(D)[:, None]
    tr = (c['P']['elig'] & (~c['is_hold'])[None, :] & (di <= q0 - EMBARGO) & np.isfinite(X).all(-1)
          & np.isfinite(h['target']))
    A = np.column_stack([np.ones(int(tr.sum())), X[tr]])
    beta, *_ = np.linalg.lstsq(A, h['target'][tr], rcond=None)
    sig = float(np.std(h['target'][tr] - A @ beta))
    pred = beta[0] + (X * beta[1:]).sum(-1)
    return np.stack([(h['thr_lo'] - pred) / sig, (h['thr_hi'] - pred) / sig, pred - h['l_20']], -1), beta


def har_feats(cid):
    def f(qi, q0):
        def build():
            Z, beta = _har_z(q0)
            FOLD_LOG[f'{cid}_{qi}'] = {'beta': [round(float(b), 4) for b in beta]}
            return Z
        return _fold_cache(cid, qi, build)
    return f


def xs_inputs():
    """Cross-section (same value for every coin) and coin flow features, causal:
    BTC log RV22, 20-day mean cross-sectional std of daily returns, 60-day mean pairwise
    correlation proxy var(mean r) / mean(var r), cross-sectional median of 7-day funding sums,
    the coin's 7-day funding sum and its 7-day taker buy imbalance 2*tbv/v - 1."""
    if 'xs' in _CTX:
        return _CTX['xs']
    c = ctx()
    P = c['P']
    D, M = P['c'].shape
    r = ft._lr(P)
    elig = P['elig']
    re = np.where(elig, r, np.nan)
    h = har_inputs()
    btc = c['syms'].index('BTCUSDT')
    disp = ft._df(np.nanstd(re, axis=1)[:, None]).rolling(20, min_periods=15).mean().values[:, 0]
    mean_r = np.nanmean(re, axis=1)
    var_mean = ft._df(mean_r[:, None]).rolling(60, min_periods=40).var().values[:, 0]
    mean_var = np.nanmean(ft._df(re).rolling(60, min_periods=40).var().values, axis=1)
    t0 = int(c['days'][0])
    fund = np.zeros((D, M))
    imb_num, imb_den = np.full((D, M), np.nan), np.full((D, M), np.nan)
    for j, s in enumerate(c['syms']):
        f = np.load(os.path.join(pn.SRC, f'{s}_funding.npy'))
        if len(f):
            f = f[f[:, 0] <= pn.CUT_MS]
            d = ((f[:, 0] - t0) // DAY).astype(int)
            ok = (d >= 0) & (d < D)
            np.add.at(fund[:, j], d[ok], f[ok, 1])
        a = np.load(os.path.join(pn.SRC, f'{s}_1h.npy'))
        a = a[(a[:, 0] >= t0) & (a[:, 0] <= pn.CUT_MS)]
        d = ((a[:, 0] - t0) // DAY).astype(int)
        v, tb = np.zeros(D), np.zeros(D)
        np.add.at(v, d, a[:, 5])
        np.add.at(tb, d, a[:, 7])
        has = np.bincount(d, minlength=D) > 0
        imb_num[has, j], imb_den[has, j] = tb[has], v[has]
    fund = np.where(np.isfinite(P['c']), fund, np.nan)
    fund7 = pn._roll_sum(fund, 7)
    imb7 = 2 * pn._roll_sum(imb_num, 7) / pn._roll_sum(imb_den, 7) - 1
    med_f7 = np.nanmedian(np.where(elig, fund7, np.nan), axis=1)
    rep = lambda v: np.repeat(np.asarray(v, dtype=float)[:, None], M, axis=1)
    out = {'btc_lrv22': rep(h['l_m'][:, btc]), 'xs_disp20': rep(disp), 'xs_corr60': rep(var_mean / mean_var),
           'xs_fund7_med': rep(med_f7), 'fund7': fund7, 'imb7': imb7}
    _CTX['xs'] = {k: np.where(np.isfinite(v), v, np.nan) for k, v in out.items()}
    return _CTX['xs']


def har_xs_feats(cid):
    def f(qi, q0):
        def build():
            Z, beta = _har_z(q0)
            xs = xs_inputs()
            FOLD_LOG[f'{cid}_{qi}'] = {'beta': [round(float(b), 4) for b in beta]}
            return np.concatenate([Z, np.stack([xs[k] for k in sorted(xs)], -1)], -1)
        return _fold_cache(cid, qi, build)
    return f


def ms_har_feats(cid):
    from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression

    def f(qi, q0):
        def build():
            c = ctx()
            h = har_inputs()
            lrv = h['l_d']
            m365 = ft._shift(ft._df(lrv).rolling(365, min_periods=90).mean().values, -1)
            s365 = ft._shift(ft._std(lrv, 365, 90), -1)
            z = np.clip((lrv - m365) / s365, -6, 6)
            D, M = z.shape
            segs = []
            for j in np.where(~c['is_hold'])[0]:
                x = z[:q0, j]
                ok = np.where(np.isfinite(x))[0]
                if len(ok) > 60:
                    xx = np.nan_to_num(x[ok[0]:])
                    segs.append(xx)
            endog = np.concatenate([s[1:] for s in segs])
            lag = np.concatenate([s[:-1] for s in segs])
            res = MarkovRegression(endog, k_regimes=2, exog=lag[:, None], switching_exog=False,
                                   switching_variance=True).fit(disp=False, maxiter=300, search_reps=5)
            params = np.asarray(res.params)
            FOLD_LOG[f'{cid}_{qi}'] = {'params': [round(float(x), 5) for x in params]}
            hi = int(np.argmax(params[:2]))   # regime with the higher intercept = high-vol state
            prob = np.full((D, M), np.nan)
            for j in range(M):
                x = z[:, j]
                ok = np.where(np.isfinite(x))[0]
                if len(ok) < 30:
                    continue
                xx = np.nan_to_num(x[ok[0]:])
                fm = MarkovRegression(xx[1:], k_regimes=2, exog=xx[:-1, None], switching_exog=False,
                                      switching_variance=True)
                pr = np.asarray(fm.filter(params).filtered_marginal_probabilities)
                pr = pr if pr.shape[-1] == 2 else pr.T
                prob[ok[0] + 1:, j] = pr[:, hi]
            Z, beta = _har_z(q0)
            return np.concatenate([Z, prob[..., None]], -1)
        return _fold_cache(cid, qi, build)
    return f


SPECS.update({
    'V1': {'phase': 'F3', 'axes': ['vol'],
           'spec': 'HAR-RV agrupado: MCO de log RV(t+1..t+20) sobre constante, log RV diaria, log media de 5 días y log media de 22 días (RV desde 1h), en filas de desarrollo con ventana cerrada antes del embargo. Variables: (umbral_tercil_bajo − pronóstico)/σ, (umbral_tercil_alto − pronóstico)/σ y pronóstico − log RV20; los umbrales son los cuantiles 1/3 y 2/3 de las sumas de RV de 20 días del año previo de la moneda. Logística. Solo Y_vol.',
           'feats': lambda: har_feats('V1')},
    'V2': {'phase': 'F3', 'axes': ['vol'],
           'spec': 'V1 más sección transversal y flujo: log RV22 de BTC, desvío transversal de retornos (media de 20 días), proxy de correlación media de 60 días var(media r)/media(var r), mediana transversal del funding de 7 días, funding de 7 días de la moneda y desbalance agresor de 7 días 2·tbv/v − 1 (9 variables). Logística. Solo Y_vol.',
           'feats': lambda: har_xs_feats('V2')},
    'V3': {'phase': 'F3', 'axes': ['vol'],
           'spec': 'V1 más la probabilidad filtrada del régimen de vol alta de un modelo de Markov de 2 regímenes (statsmodels MarkovRegression, intercepto y varianza conmutados, rezago 1 no conmutado, search_reps = 5) sobre la log-RV diaria estandarizada con media/desvío de 365 días (±6), ajustado sobre las monedas de desarrollo antes del pliegue (4 variables). Logística. Solo Y_vol.',
           'feats': lambda: ms_har_feats('V3')},
    'E1': {'phase': 'F3', 'axes': list(AXES),
           'spec': 'Canal: pendiente de la regresión de log-precio a 20 y 50 días dividida por el desvío diario, y R². Caja: Donchian50/ATR20, toques de la banda de ±0,25 ATR del máximo/mínimo de 20 días en los últimos 20 días, posición en la caja de 20 días (7 variables). Logística.',
           'feats': lambda: static_feats((ft.fam_E1, 'E1'))},
    'E2': {'phase': 'F3', 'axes': list(AXES),
           'spec': 'Banderín: impulso (C[t−10] − C[t−20])/ATR[t−10], razón de consolidación (rango de 10 días / rango de los 10 previos), bandera = (|impulso| ≥ 2 y razón < 0,5) con el signo del impulso, pendiente del rango diario/ATR en 10 días. Wyckoff-lite: drawdown desde el máximo de 90 días, caja (Donchian20/ATR ≤ 4), spring (mínimo de los últimos 3 días bajo el piso de 20 días previo y cierre por encima), wyckoff = drawdown ≤ −25% y caja y spring, días desde el último spring (tope 20) (9 variables). Logística.',
           'feats': lambda: static_feats((ft.fam_E2, 'E2'))},
    'S1': {'phase': 'F3', 'axes': list(AXES),
           'spec': 'Signatures truncadas en nivel 3 (Chen, numpy) de caminos de 20 y 60 días de (tiempo en [0, 1], log-precio desde el inicio / (desvío diario de la ventana·√n), log-RV diaria menos su media en la ventana): 39 variables por ventana, 78 en total. Logística.',
           'feats': lambda: static_feats((ft.fam_S1, 'S1'))},
})

# ----------------------------------------------------------------------------------------------
# F4: global models, range-exit direction and zero-shot foundation models
# ----------------------------------------------------------------------------------------------
G_STATIC = (('A1', ft.fam_A1), ('A2', ft.fam_A2), ('B1', ft.fam_B1), ('B2', ft.fam_B2), ('D1', ft.fam_D1),
            ('E1', ft.fam_E1), ('E2', ft.fam_E2), ('S1', ft.fam_S1))
G_FOLD = ('C1a', 'C1b', 'C2', 'C3', 'C4', 'V2', 'V3')


def global_feats(qi, q0):
    """Every family: the static ones plus the fold-fitted state probabilities, BOCPD and the HAR
    forecasts (V2 carries V1's z-distances and the cross-section; V3 adds its Markov probability)."""
    if 'g_static' not in _CTX:
        _CTX['g_static'] = np.concatenate([static(f, n)[0] for n, f in G_STATIC], axis=2)
    folds = []
    for cid in G_FOLD:
        X = np.load(os.path.join(OUT, f'fold_{cid}_{qi}.npy'))
        folds.append(X[..., -1:] if cid == 'V3' else X)
    return np.concatenate([_CTX['g_static']] + folds, axis=2)


def chronos_feats(cid, kind):
    def f(qi, q0):
        def build():
            c = ctx()
            h = har_inputs()
            pred = np.load(os.path.join(OUT, f'chronos_{kind}.npy')).astype(float)
            di = np.arange(pred.shape[0])[:, None]
            tr = (c['P']['elig'] & (~c['is_hold'])[None, :] & (di <= q0 - EMBARGO) & np.isfinite(pred)
                  & np.isfinite(h['target']))
            sig = float(np.std(h['target'][tr] - pred[tr]))
            FOLD_LOG[f'{cid}_{qi}'] = {'sigma': round(sig, 4), 'bias': round(float(np.mean(h['target'][tr] - pred[tr])), 4)}
            return np.stack([(h['thr_lo'] - pred) / sig, (h['thr_hi'] - pred) / sig, pred - h['l_20']], -1)
        return _fold_cache(cid, qi, build)
    return f


SPECS.update({
    'G1': {'phase': 'F4', 'axes': list(AXES),
           'spec': 'Global: logística (C = 1) sobre todas las variables: estáticas A1, A2, B1, B2, D1, E1, E2 y S1, más las del pliegue C1a, C1b, C2, C3, C4, V2 (z de HAR y sección transversal) y la probabilidad de Markov de V3 (~148 variables).',
           'feats': lambda: global_feats},
    'G2': {'phase': 'F4', 'axes': list(AXES), 'model': 'gbm',
           'spec': 'Global: HistGradientBoostingClassifier con hiperparámetros fijos (200 iteraciones, learning rate 0,05, 15 hojas como máximo, mínimo 200 por hoja, L2 = 1, random_state 0, sin tuning) sobre las mismas variables que G1.',
           'feats': lambda: global_feats},
    'X1': {'phase': 'F4', 'axes': ['exit'],
           'spec': 'Y_exit: en los días cuya ventana pasada fue rango (persistencia de Y_range = 1, caja c[t−20] ± 3·ATR20[t−20]), la etiqueta es la dirección del primer cierre fuera de esa caja en t+1..t+20 (1 arriba, 0 abajo; sin salida queda excluido). Varas: climatología de las salidas conocidas de la moneda (365 días) y la última dirección de salida conocida (persistencia). Modelo: la logística de G1 sobre las mismas variables. Transición objetivo para la anticipación: salida hacia arriba.',
           'feats': lambda: global_feats},
    'T1': {'phase': 'F4', 'axes': ['vol'],
           'spec': 'Chronos-Bolt small (amazon/chronos-bolt-small), zero-shot: contexto de hasta 512 días de log-RV diaria hasta t, pronóstico de 20 días; log de la suma de la trayectoria mediana como pronóstico de log RV(t+1..t+20) (r56_chronos.py). σ = desvío de los residuos en las filas de entrenamiento del pliegue. Variables como V1: z a los terciles y pronóstico − log RV20. Logística. Solo Y_vol.',
           'feats': lambda: chronos_feats('T1', 'bolt')},
    'T2': {'phase': 'F4', 'axes': ['vol'],
           'spec': 'Igual que T1 con Chronos-2 (amazon/chronos-2).',
           'feats': lambda: chronos_feats('T2', 'chronos2')},
})

STATIC_FAMS = {'T90': [ft.fam_T90], 'A1': [ft.fam_A1], 'A2': [ft.fam_A2], 'A3': [], 'B1': [ft.fam_B1],
               'B2': [ft.fam_B2], 'D1': [ft.fam_D1],
               'E1': [ft.fam_E1], 'E2': [ft.fam_E2], 'S1': [ft.fam_S1]}


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
    for axis in NCLS:
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

# ----------------------------------------------------------------------------------------------
# F5: one-time holdout scoring and the bridge to r57 (PROTOCOL_R56 sections 5 and 6)
# ----------------------------------------------------------------------------------------------
def select_f5():
    """Best configuration per bridge axis by the mean of development and 2024 BSS, both > 0 (at most
    one per axis, so at most 3; amendment F5-1). Baselines and X1 (not a bridge axis) are excluded."""
    picks = {}
    for ph in ('F1', 'F2', 'F3', 'F4'):
        p = os.path.join(OUT, f'{ph.lower()}.json')
        if not os.path.exists(p):
            continue
        for cid, r in json.load(open(p)).items():
            if SPECS.get(cid, {}).get('baseline'):
                continue
            for axis, ev in r['axes'].items():
                if axis not in AXES:
                    continue
                d, v = ev['dev']['bss'], ev['val']['bss']
                if d > 0 and v > 0 and (axis not in picks or (d + v) / 2 > picks[axis][1]):
                    picks[axis] = (cid, (d + v) / 2)
    return {a: c for a, (c, _) in picks.items()}


def bridge(axis, cid, dev_ev, val_ev, hold_ev, spa_p):
    lead = hold_ev['lead_median']
    slopes = hold_ev['calibration_slopes']
    yrs = [v for k, v in hold_ev['bss_by_year'].items() if k in ('2021', '2022', '2023', '2024')]
    checks = {
        '1_dev_bss>=0.05': dev_ev['bss'] >= 0.05, '1_spa_p<0.05': spa_p < 0.05,
        '2_val_bss>0': val_ev['bss'] > 0, '2_hold_bss>0': hold_ev['bss'] > 0, '2_hold_dm_p<0.10': hold_ev['dm_p'] < 0.10,
        '3_hold_coins_pos>=0.6': (hold_ev['coin_bss_pos_share'] or 0) >= 0.6,
        '3_years_pos>=3of4': sum(x > 0 for x in yrs) >= 3,
        '4_switches<=12': hold_ev['switches_per_year'] <= 12,
        '4_lead>=persist+3': (lead['model'] - lead['persistence']) >= 3,
        '4_calibration_0.7-1.3': all(0.7 <= x <= 1.3 for x in slopes),
    }
    return {'config': cid, 'axis': axis, 'checks': checks, 'passes': all(checks.values())}


def run_f5():
    picks = select_f5()
    spa_dev = spa('dev')
    res = {'selection': picks, 'spa_dev': spa_dev, 'axes': {}}
    for axis, cid in picks.items():
        sp = SPECS[cid]
        feats = sp['feats']()
        preds = fit_predict(feats, axis, coins='hold', kind=sp.get('model', 'logit'))
        np.save(os.path.join(OUT, f'pred_hold_{cid}_{axis}.npy'), preds.astype(np.float32))
        hold = {p: evaluate(preds, axis, 'hold', p)[0] for p in ('all', 'dev', 'val')}
        res_ph = json.load(open(os.path.join(OUT, f"{sp['phase'].lower()}.json")))[cid]['axes'][axis]
        b = bridge(axis, cid, res_ph['dev'], res_ph['val'], hold['all'], spa_dev[axis]['spa_p'])
        res['axes'][axis] = {'config': cid, 'holdout': hold, 'bridge': b}
        print(axis, cid, json.dumps(b), flush=True)
    json.dump(res, open(os.path.join(OUT, 'f5.json'), 'w'), indent=2)
    return res


def main():
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == 'register':
        register(a[1])
    elif len(a) >= 2 and a[0] == 'run':
        run(a[1])
    elif a and a[0] == 'f5':
        run_f5()
    elif a and a[0] == 'spa':
        spa(a[1] if len(a) > 1 else 'dev')
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
