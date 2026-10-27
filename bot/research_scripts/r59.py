"""r59: reusable validation on the fixed universe (PROTOCOL_R59.md). Development = the 48 U50 alts;
H = N2 ∪ N3 is only read by r59_oracle (r59_holdout guard installed at import).

Research container:
    python research_scripts/r59.py groups      # F0 §1.3: 6 liquidity-stratified coin groups (seed 59), no outcomes
    python research_scripts/r59.py cv          # F0 §1.3: r58's selection procedure in 24 coin-group x year folds
    python research_scripts/r59.py rotation    # F0 §1.4: rotation p of V1..V6 on U50 + 200 Markov placebos
    python research_scripts/r59.py series_test # F0 §1.5: write/read/verify round trip of the series store

Every array stops at 2024-12-31 (r58's files are already cut; asserted again on load).
"""
import hashlib
import json
import math
import os
import sys
import tempfile

import numpy as np

import r59_holdout as hg

hg.install()

import r57  # noqa: E402  (after the guard, so their loaders are wrapped)
import r58  # noqa: E402

OUT = hg.OUT
SEED = 59
YEARS = ('2021', '2022', '2023', '2024')
N_GROUPS = 6
CV_BOOT = 1000                      # §1.3: 1,000 replicas per fold so 24 sweeps stay tractable
CV_MIN_CLASS = 10                   # test folds need >= 10 trades in each class to enter the summary
AND_MIN_RETAIN = 0.25               # r58 §3: below this the best single variable replaces the AND
N_ROT, ROT_MIN_DAYS = 2000, 90
N_PLACEBO, PLACEBO_ROT = 200, 500
DAY, H4 = r58.DAY, r58.H4


def log(x):
    print(x, flush=True)


def u50_trades():
    import pandas as pd
    df = pd.read_csv(os.path.join(r58.OUT, 'f1_trades_u50.csv'))
    assert (df['opened'] < r58.CUT_MS).all() and (df['closed'] <= r58.CUT_MS).all()
    df['year'] = df['year'].astype(str)
    return df


# ----------------------------------------------------------------------------------------------
# §1.3 coin groups and the coin-group x year cross-validation
# ----------------------------------------------------------------------------------------------
def groups():
    """Alts sorted by vol24h (liquidity proxy from universe50.json, no outcomes); each consecutive
    sextet sends one coin to each group through a seeded permutation."""
    u = [x for x in json.load(open(os.path.join(r58.U50_DIR, 'universe50.json'))) if x['symbol'] not in ('BTCUSDT', 'ETHUSDT')]
    u.sort(key=lambda x: -x['vol24h'])
    rng = np.random.default_rng(SEED)
    g = {k: [] for k in range(N_GROUPS)}
    for i in range(0, len(u), N_GROUPS):
        chunk = u[i:i + N_GROUPS]
        for c, k in zip(chunk, rng.permutation(N_GROUPS)):
            g[int(k)].append(c['symbol'])
    on = {x['symbol']: x['onboard'] for x in u}
    out = {'protocol': 'PROTOCOL_R59.md §1.3', 'seed': SEED, 'groups': {str(k): sorted(v) for k, v in g.items()},
           'onboard_median_utc_day': {str(k): int(np.median([on[s] for s in v]) // DAY) for k, v in g.items()}}
    out['sha256'] = hashlib.sha256(json.dumps(out['groups'], sort_keys=True).encode()).hexdigest()
    os.makedirs(OUT, exist_ok=True)
    json.dump(out, open(os.path.join(OUT, 'cv_groups.json'), 'w'), indent=1)
    log(json.dumps(out))
    return out


def load_groups():
    return {int(k): set(v) for k, v in json.load(open(os.path.join(OUT, 'cv_groups.json')))['groups'].items()}


def select(train, seed):
    """r58 F1's selection as code (§2 eligibility, top 3 by score, AND or the best single), with
    rule 2 adapted to the training years present: D > 0 in >= 2 of the 3 training years."""
    yrs = tuple(y for y in YEARS if (train['year'] == y).any())
    saved = r58.YEARS, r58.N_BOOT, r58.SEED
    r58.YEARS, r58.N_BOOT, r58.SEED = yrs, CV_BOOT, seed
    try:
        sw = r58.sweep(train.reset_index(drop=True), r58.CANDIDATES)
    finally:
        r58.YEARS, r58.N_BOOT, r58.SEED = saved
    need = 2 if len(yrs) == 3 else 3
    for v, e in sw.items():
        e['rule']['2_years_pos'] = sum(1 for x in e['D_by_year'].values() if x == x and x > 0) >= need
        e['rule'].pop('2_years_pos_ge_3', None)
        e['eligible'] = bool(all(e['rule'].values()))
    el = sorted((v for v in r58.CANDIDATES if sw[v]['eligible']), key=lambda v: -sw[v]['score'])
    sel = el[:3]
    rule = sel
    if len(sel) > 1:
        ok = train[sel].notna().all(axis=1)
        if (train.loc[ok, sel] == 1).all(axis=1).mean() < AND_MIN_RETAIN:
            rule = sel[:1]
    return {'eligible': el, 'selected': sel, 'rule': rule}


def rule_d(test, rule):
    if not rule:
        return {'n': 0, 'n_keep': 0, 'D': None}
    ok = test[rule].notna().all(axis=1).values
    sub = test[ok]
    keep = (sub[rule] == 1).all(axis=1).values
    R = sub['R'].values
    n_k, n_r = int(keep.sum()), int((~keep).sum())
    return {'n': int(ok.sum()), 'n_keep': n_k, 'D': r58._d(R, keep) if n_k and n_r else None,
            'counts': n_k >= CV_MIN_CLASS and n_r >= CV_MIN_CLASS}


def cv():
    import warnings
    warnings.simplefilter('ignore')
    df = u50_trades()
    G = load_groups()
    assert set(df['sym'].unique()) <= set().union(*G.values())
    folds = []
    for g, members in G.items():
        for k, y in enumerate(YEARS):
            fi = g * len(YEARS) + k
            in_g = df['sym'].isin(members).values
            tr = df[~in_g & (df['year'].values != y)]
            te = df[in_g & (df['year'].values == y)]
            s = select(tr, SEED + fi)
            r = rule_d(te, s['rule'])
            folds.append({'fold': fi, 'group': g, 'year': y, 'n_train': int(len(tr)), 'n_test': int(len(te)), **s, 'test': r})
            log(f"fold {fi:2d} g{g} {y}: train {len(tr)} test {len(te)} eligible {s['eligible']} rule {s['rule']} "
                f"test D {r['D'] if r['D'] is None else round(r['D'], 3)} n_keep {r['n_keep']}/{r['n']}")
    freq = {v: sum(v in f['selected'] for f in folds) / len(folds) for v in r58.CANDIDATES}
    elig = {v: sum(v in f['eligible'] for f in folds) / len(folds) for v in r58.CANDIDATES}
    ds = np.array([f['test']['D'] for f in folds if f['test'].get('counts')], float)
    summary = {'folds': len(folds), 'folds_in_summary': int(len(ds)), 'selected_freq': freq, 'eligible_freq': elig,
               'rule_freq': _count([tuple(f['rule']) for f in folds]),
               'test_D_median': float(np.median(ds)) if len(ds) else None, 'test_D_mean': float(ds.mean()) if len(ds) else None,
               'test_D_pos_share': float((ds > 0).mean()) if len(ds) else None,
               'tool_check_V1_or_V2_selected_share': sum(('V1' in f['selected']) or ('V2' in f['selected']) for f in folds) / len(folds)}
    summary['tool_check_pass'] = summary['tool_check_V1_or_V2_selected_share'] >= 0.5
    out = {'protocol': 'PROTOCOL_R59.md §1.3', 'n_added': 0, 'cv_boot': CV_BOOT, 'summary': summary, 'folds': folds}
    json.dump(out, open(os.path.join(OUT, 'f0_cv.json'), 'w'), indent=1, default=float)
    log(json.dumps(summary, default=float))


def _count(xs):
    c = {}
    for x in xs:
        c['∧'.join(x) or '(none)'] = c.get('∧'.join(x) or '(none)', 0) + 1
    return c


# ----------------------------------------------------------------------------------------------
# §1.4 rotation test
# ----------------------------------------------------------------------------------------------
class Grid:
    """Per coin, a label series on its native grid restricted to the span where it exists, and the
    position of every trade's signal on that grid. rotate(k) relabels trades with the series shifted
    circularly by k_j steps inside each coin's span."""

    def __init__(self, df, coin_series, coin_ts, steps_min):
        self.syms = sorted(coin_series)
        self.n = len(df)
        self.idx = np.full(self.n, -1)
        self.coin = np.full(self.n, -1)
        self.a, self.L, self.S = [], [], []
        sig = df['opened'].values - np.where(df['sleeve'].values == 'R3', H4, 0)
        sym = df['sym'].values
        off = 0
        flat = []
        for j, s in enumerate(self.syms):
            x, ts = coin_series[s], coin_ts[s]
            fin = np.flatnonzero(np.isfinite(x))
            a, b = (fin[0], fin[-1]) if len(fin) else (0, -1)
            L = b - a + 1
            self.a.append(off)
            self.L.append(max(L, 0))
            flat.append(x[a:b + 1] if L > 0 else np.array([]))
            m = sym == s
            pos = ts(sig[m])
            inside = (pos >= a) & (pos <= b)
            ii = np.flatnonzero(m)
            self.idx[ii[inside]] = pos[inside] - a
            self.coin[ii[inside]] = j
            off += max(L, 0)
        self.S = np.concatenate(flat) if flat else np.array([])
        self.a, self.L = np.array(self.a), np.array(self.L)
        self.kmin = steps_min
        self.valid = self.coin >= 0

    def labels(self, k=None):
        out = np.full(self.n, np.nan)
        c, i = self.coin[self.valid], self.idx[self.valid]
        if k is not None:
            i = (i - k[c]) % self.L[c]
        out[self.valid] = self.S[self.a[c] + i]
        return out

    def draw(self, rng):
        lo = self.kmin
        hi = np.maximum(self.L - self.kmin, lo + 1)
        return rng.integers(lo, hi)


def day_grid(df, key):
    """V1 (persist == 0) or V2 (p_rng < cut) from f0_days u50 columns, on the daily grid."""
    d = np.load(os.path.join(r58.OUT, 'f0_days.npz'))
    days = d['u50__days']
    syms = r58.banks()['u50'][0]
    cut = json.load(open(os.path.join(r58.OUT, 'f0_cuts.json')))['p_range_cut']
    raw = d['u50__persist'] if key in ('V1', 'persist') else d['u50__p_rng']
    series = {}
    for j, s in enumerate(syms):
        v = raw[:, j].astype(float)
        if key == 'V1':
            series[s] = np.where(np.isfinite(v), (v == 0).astype(float), np.nan)
        elif key == 'V2':
            series[s] = np.where(np.isfinite(v), (v < cut).astype(float), np.nan)
        else:
            series[s] = v
    pos = lambda sig: np.array([r57.row_for(days, t) for t in sig], int)
    return Grid(df, series, {s: pos for s in syms}, ROT_MIN_DAYS)


def bar_grid(df, key):
    """V3..V6 from f0_bars_u50 columns with r58's cuts, on each coin's 4h grid."""
    z = np.load(os.path.join(r58.OUT, 'f0_bars_u50.npz'))
    cuts = json.load(open(os.path.join(r58.OUT, 'f0_cuts.json')))
    c = cuts['tercile_cuts_u50_alt_bars']
    col = {'V3': (0, lambda v: v >= c['relvol'][1]), 'V4': (1, lambda v: v >= c['taker'][1]),
           'V5a': (7, lambda v: v < r58.FUND_SAT), 'V6': (5, lambda v: v >= r58.ROUND_ATR)}[key]
    series, tsf = {}, {}
    for s in r58.banks()['u50'][0]:
        ts, x = z[f'{s}__ts'], z[f'{s}__x']
        assert ts[-1] <= r58.CUT_MS
        v = x[:, col[0]]
        series[s] = np.where(np.isfinite(v), col[1](v).astype(float), np.nan)
        tsf[s] = (lambda t, ts=ts: np.searchsorted(ts, t))
    return Grid(df, series, tsf, ROT_MIN_DAYS * 6)


def stat_d(R, lab):
    ok = np.isfinite(lab)
    return r58._d(R[ok], lab[ok] == 1)


def stat_cond(R, lab, strata):
    ok = np.isfinite(lab) & np.isfinite(strata)
    return r58._cond(R[ok], lab[ok] == 1, strata[ok])


def rotation_p(grid, R, n_rot, seed, strata=None):
    """One-sided p of the observed statistic against circular rotations of the label series."""
    f = (lambda lab: stat_d(R, lab)) if strata is None else (lambda lab: stat_cond(R, lab, strata))
    obs = f(grid.labels())
    rng = np.random.default_rng(seed)
    null = np.array([f(grid.labels(grid.draw(rng))) for _ in range(n_rot)])
    null = null[np.isfinite(null)]
    return obs, float((1 + (null >= obs).sum()) / (1 + len(null))), null


def placebo_grid(df, rho, pi1, rng):
    """Two-state Markov chain per coin on the daily grid with V1's lag-1 autocorrelation and share."""
    base = day_grid(df, 'V1')
    a, b = (1 - pi1) * (1 - rho), pi1 * (1 - rho)          # P(1->0), P(0->1): stationary pi1, autocorr rho
    S = np.empty_like(base.S)
    for j in range(len(base.syms)):
        L = base.L[j]
        if L == 0:
            continue
        u = rng.random(L)
        x = np.empty(L)
        x[0] = float(u[0] < pi1)
        for t in range(1, L):
            x[t] = (u[t] >= a) if x[t - 1] == 1 else (u[t] < b)
        S[base.a[j]:base.a[j] + L] = x
    base.S = S
    return base


def rotation():
    import warnings
    warnings.simplefilter('ignore')
    df = u50_trades()
    R = df['R'].values
    f1 = json.load(open(os.path.join(r58.OUT, 'f1_diag.json')))['variables']
    res = {'protocol': 'PROTOCOL_R59.md §1.4', 'n_added': 0, 'n_rot': N_ROT, 'seed': SEED, 'variables': {}}
    persist = df['persist'].values.astype(float)
    for i, v in enumerate(r58.CANDIDATES):
        g = day_grid(df, v) if v in ('V1', 'V2') else bar_grid(df, v)
        lab = g.labels()
        csv_lab = df[v].values.astype(float)
        both = np.isfinite(lab) & np.isfinite(csv_lab)
        agree = float((lab[both] == csv_lab[both]).mean())
        obs, p, null = rotation_p(g, R, N_ROT, SEED + i)
        e = {'label_agreement_with_r58': agree, 'n_labelled': int(np.isfinite(lab).sum()), 'D': obs,
             'D_r58': f1[v]['D'], 'p_rotation': p, 'null_p5_p95': np.percentile(null, [5, 95]).tolist()}
        log(f"{v}: agree {agree:.4f} D {obs:+.3f} (r58 {f1[v]['D']:+.3f}) p {p:.4f} null90 {np.round(e['null_p5_p95'], 3)}")
        res['variables'][v] = e
    # Placebos: Markov chains with V1's persistence; the p-values must be ~uniform (§1.4).
    g1 = day_grid(df, 'V1')
    x = g1.S
    pi1 = float(np.nanmean(x))
    rhos = []
    for j in range(len(g1.syms)):
        s = x[g1.a[j]:g1.a[j] + g1.L[j]]
        ok = np.isfinite(s[1:]) & np.isfinite(s[:-1])
        if ok.sum() > 30 and s[:-1][ok].std() > 0 and s[1:][ok].std() > 0:
            rhos.append(np.corrcoef(s[:-1][ok], s[1:][ok])[0, 1])
    rho = float(np.mean(rhos))
    rng = np.random.default_rng(SEED + 100)
    ps = []
    for k in range(N_PLACEBO):
        pg = placebo_grid(df, rho, pi1, rng)
        _, p, _ = rotation_p(pg, R, PLACEBO_ROT, SEED + 1000 + k)
        ps.append(p)
    ps = np.array(ps)
    res['placebo'] = {'n': N_PLACEBO, 'rot_each': PLACEBO_ROT, 'rho': rho, 'pi1': pi1,
                      'share_p_lt_0_10': float((ps < 0.10).mean()), 'share_p_lt_0_05': float((ps < 0.05).mean()),
                      'deciles': np.percentile(ps, np.arange(10, 100, 10)).tolist()}
    res['placebo']['pass'] = 0.05 <= res['placebo']['share_p_lt_0_10'] <= 0.15
    log(f"placebo rho {rho:.3f} pi1 {pi1:.3f}: share p<0.10 {res['placebo']['share_p_lt_0_10']:.3f} "
        f"p<0.05 {res['placebo']['share_p_lt_0_05']:.3f} pass {res['placebo']['pass']}")
    json.dump(res, open(os.path.join(OUT, 'f0_rotation.json'), 'w'), indent=1, default=float)


# ----------------------------------------------------------------------------------------------
# §1.5 series store
# ----------------------------------------------------------------------------------------------
SERIES = os.path.join(OUT, 'series')


def save_series(rnd, trial_id, days, rets, script, window, root=SERIES):
    """Adds (or replaces) one daily return series in <root>/<rnd>.npz and updates the manifest."""
    days, rets = np.asarray(days, np.int64), np.asarray(rets, float)
    assert days.ndim == rets.ndim == 1 and len(days) == len(rets) and (np.diff(days) > 0).all()
    assert days[-1] < r58.CUT_MS, 'series must stop at 2024-12-31'
    os.makedirs(root, exist_ok=True)
    path = os.path.join(root, f'{rnd}.npz')
    cur = dict(np.load(path)) if os.path.exists(path) else {}
    cur[f'{trial_id}__days'], cur[f'{trial_id}__ret'] = days, rets
    np.savez_compressed(path, **cur)
    mpath = os.path.join(root, 'manifest.json')
    man = json.load(open(mpath)) if os.path.exists(mpath) else {'format': 'daily simple returns, days in ms UTC', 'files': {}, 'series': {}}
    man['files'][f'{rnd}.npz'] = hashlib.sha256(open(path, 'rb').read()).hexdigest()
    man['series'][trial_id] = {'file': f'{rnd}.npz', 'script': script, 'window': window, 'n_days': int(len(days)),
                               'sha256': hashlib.sha256(days.tobytes() + rets.tobytes()).hexdigest()}
    json.dump(man, open(mpath, 'w'), indent=1)
    return man['series'][trial_id]


def load_series(trial_id, root=SERIES):
    man = json.load(open(os.path.join(root, 'manifest.json')))
    m = man['series'][trial_id]
    z = np.load(os.path.join(root, m['file']))
    days, rets = z[f'{trial_id}__days'], z[f'{trial_id}__ret']
    assert hashlib.sha256(days.tobytes() + rets.tobytes()).hexdigest() == m['sha256'], trial_id
    return days, rets


def series_test():
    root = tempfile.mkdtemp(prefix='r59_series_')
    days = np.arange(r58.ms('2021-01-01'), r58.ms('2021-03-01'), DAY)
    rets = np.random.default_rng(SEED).normal(0, 0.01, len(days))
    save_series('rtest', 'T1', days, rets, 'r59.py series_test', '2021-01..02', root)
    save_series('rtest', 'T2', days, -rets, 'r59.py series_test', '2021-01..02', root)
    d1, r1 = load_series('T1', root)
    d2, r2 = load_series('T2', root)
    late = False
    try:
        save_series('rtest', 'T3', np.array([r58.CUT_MS]), np.array([0.0]), 'x', 'x', root)
    except AssertionError:
        late = True
    ok = (d1 == days).all() and (r1 == rets).all() and (r2 == -rets).all() and late
    out = {'protocol': 'PROTOCOL_R59.md §1.5', 'round_trip': bool(ok), 'refuses_2025': late}
    json.dump(out, open(os.path.join(OUT, 'f0_series_test.json'), 'w'), indent=1)
    log(json.dumps(out))


# ----------------------------------------------------------------------------------------------
# §2 SPA (Hansen 2005, SPA_c) and PBO (CSCV)
# ----------------------------------------------------------------------------------------------
SPA_BLOCK, SPA_BOOT = 20, 2000              # stationary bootstrap: mean block 20 days, 2,000 draws (§2)


def stationary_idx(n, rng, block=SPA_BLOCK):
    idx = np.empty(n, dtype=int)
    idx[0] = rng.integers(n)
    jump = rng.random(n) < 1 / block
    starts = rng.integers(n, size=n)
    for t in range(1, n):
        idx[t] = starts[t] if jump[t] else (idx[t - 1] + 1) % n
    return idx


def spa_pvalue(G, n_boot=SPA_BOOT, seed=SEED):
    """Hansen's SPA_c p-value for H0: no column of G (days x models of benchmark differentials) has a
    positive mean. Same recentring as r56_eval.spa_pvalue, with r59's seed."""
    G = G[np.isfinite(G).all(1)]
    n = len(G)
    rng = np.random.default_rng(seed)
    I = np.array([stationary_idx(n, rng) for _ in range(n_boot)])
    gbar = G.mean(0)
    gb = np.stack([G[I, k].mean(1) for k in range(G.shape[1])], axis=1)
    omega = np.sqrt(n) * gb.std(0)
    omega = np.where(omega > 0, omega, 1e-12)
    T = max(float((np.sqrt(n) * gbar / omega).max()), 0.0)
    very_neg = np.sqrt(n) * gbar / omega < -np.sqrt(2 * np.log(np.log(n)))
    Tb = np.maximum((np.sqrt(n) * (gb - gbar + gbar * very_neg) / omega).max(1), 0.0)
    return float((Tb >= T).mean()), int(np.argmax(gbar / np.where(gb.std(0) > 0, gb.std(0), 1e-12)))


def pbo(M, s=16):
    import r50_f1d
    return r50_f1d.pbo(M, s)


def spa_test():
    """§2 verification on synthetic families of known outcome."""
    # Amendment E2: one draw of a null family is a coin flip (SPA p ~ uniform, PBO of one dataset is
    # noisy), so the check runs 20 replicas and tests the rates instead of a single value.
    n, reps = 1461, 20                                 # 2021-01-01..2024-12-31
    rows = []
    for k in range(reps):
        rng = np.random.default_rng(SEED + k)
        noise = rng.normal(0, 0.01, (n, 30))
        p_noise, _ = spa_pvalue(noise, n_boot=500, seed=SEED + k)
        pbo_noise, _ = pbo(noise)
        strong = noise.copy()
        strong[:, 0] = rng.normal(2.0 * 0.01 / math.sqrt(365), 0.01, n)   # Sharpe 2 (annualised over 365 days)
        p_strong, best = spa_pvalue(strong, n_boot=500, seed=SEED + k)
        rows.append((p_noise, pbo_noise, p_strong, best))
    A = np.array(rows, float)
    out = {'protocol': 'PROTOCOL_R59.md §2 (verification, amendment E2)', 'reps': reps, 'n_boot': 500,
           'noise30': {'share_spa_p_lt_0_10': float((A[:, 0] < 0.10).mean()), 'pbo_mean': float(A[:, 1].mean()),
                       'pbo_range': [float(A[:, 1].min()), float(A[:, 1].max())]},
           'sharpe2_plus_29_noise': {'share_spa_p_lt_0_05': float((A[:, 2] < 0.05).mean()), 'share_best_is_col0': float((A[:, 3] == 0).mean())}}
    out['pass'] = bool(out['noise30']['share_spa_p_lt_0_10'] <= 0.20 and 0.35 <= out['noise30']['pbo_mean'] <= 0.65
                       and out['sharpe2_plus_29_noise']['share_spa_p_lt_0_05'] >= 0.8)
    json.dump(out, open(os.path.join(OUT, 'f1_spa_test.json'), 'w'), indent=1)
    log(json.dumps(out))


def f1_q():
    """R57_Q1 / R57_Q2 inside P-r55, rebuilt from U50 only. r57.rev builds the N2 book before it
    evaluates the U50 one, so a capture of it stops at the guard; this repeats its U50 steps
    (same functions, same order) and checks the committed in_p55 Sharpes (pre-2025) to 1e-4."""
    import r50_engines as en
    import r54_v1 as v1
    import r55_ml as ml
    import r55_engine as eg
    ev = r57.ev
    s = r57.load_states()                     # U50 fields only; the n2_* arrays are not read here
    base, qlab, mlab = r57.p55_base()
    out = {}
    for w, bb in base.items():                # §2 assertion, and the R1 benchmark (P-r55 without C6)
        days, vals = eg.portfolio(bb['comps'], bb['start'])
        m = eg.evaluate(days, vals, qlab, mlab)
        assert abs(m['sharpe'] - r57.P55_REF[w]) < 0.0015, (w, m['sharpe'])
        out[f'P55_{w}'] = (days, vals)
        out[f'R1_{w}'] = eg.portfolio({'R1': bb['comps']['R1']}, bb['start'])
    uni = [u['symbol'] for u in json.load(open(os.path.join(v1.DATA, 'universe50.json')))]
    alts = [x for x in uni if x not in ('BTCUSDT', 'ETHUSDT')]
    gate_u50 = r57.p_gate(s['days'], s['p_rng'], s['syms'], s['cut'])
    ref = json.load(open(os.path.join(r57.OUT, 'f4_rev.json')))
    for name, gated in (('Q1', False), ('Q2', True)):
        cur, _ = r57.rev_book(alts, v1.DATA, gate_u50, gated)
        b = r57.basket_from(cur, r57.REV_FROM)
        mb = en.metrics(b[0], b[1], [], r57.REV_FROM)
        assert abs(mb['sharpe'] - ref[name]['basket_u50']['sharpe']) < 1e-4, (name, mb['sharpe'])
        out[f'{name}_book'] = b
        for w, bb in base.items():
            c6p, _ = ml.c6_prime(bb['comps']['C6'], b, ev.ms(r57.REV_FROM))
            days, vals = eg.portfolio({'R1': bb['comps']['R1'], 'C6': c6p}, bb['start'])
            m = eg.evaluate(days, vals, qlab, mlab)
            assert abs(m['sharpe'] - ref[name]['in_p55'][w]['sharpe']) < 1e-4, (name, w, m['sharpe'])
            out[f'{name}_{w}'] = (days, vals)
    np.savez_compressed(os.path.join(OUT, 'capture', 'r59_q.npz'),
                        **{f'{k}__days': v[0] for k, v in out.items()}, **{f'{k}__vals': v[1] for k, v in out.items()})
    log('f1_q: Q1/Q2 in P-r55 reproduced (U50 only) ' + ', '.join(out))


# ----------------------------------------------------------------------------------------------
# §2 F1: trial -> captured curve, series store, SPA/PBO
# ----------------------------------------------------------------------------------------------
# Each family member maps to its captured curves (data/r59/capture/<tag>.npz, written by
# r59_capture.py; r59_q.npz by f1_q). A source is (tag, i, check): i is a curve index, a list of
# indexes joined in time (the books measured as dev 2021-05..2023 plus validation 2024), or a
# key of r59_q.npz. check is either the Sharpe the capture logged for that call (pre-2025 metrics
# only; it must match the trial's committed number) or ctx pairs the call's locals must carry.
# Indexes were read from the call logs (loop variables), never from series values.
def _pv(tag, c, l, sc=None, sl=None):
    return {'common': (tag, c, sc), 'long': None if l is None else (tag, l, sl)}


F1_P = {
    'R50_F2_PORTFOLIO': _pv('r50_f2', 6, 7, {'n': 'C6', 'w': 'common'}, {'n': 'C6', 'w': 'long'}),
    'R50_F1D_P1': _pv('r50_f1d', 16, 17, {'w': 'common', 's': 'V1'}, {'w': 'long', 's': 'V1'}),
    'R50_F1D_T4': _pv('r50_f1d', 20, 21, {'w': 'common'}, {'w': 'long'}),
    'R50_F1E_P3': _pv('r50_f1e', 2, 3, {'window': 'common'}, {'window': 'long'}),
    'R50_F1F_P4': _pv('r50_f1f', 24, 48, {'window': 'common'}, {'window': 'long'}),
    'R51_F5_T1': _pv('r51_f6', 3, 1, {'w': 'common', 't': 'T1'}, {'w': 'long', 't': 'T1'}),
    'R51_F5_T2': _pv('r51_f6', 5, 4, {'w': 'common', 't': 'T2'}, {'w': 'long', 't': 'T2'}),
    'R52_F3_J1': _pv('r52_j1', 3, 1, 1.6203, 1.6133),
    'R53_F2_C6q': _pv('r53_c6q', 9, 7, 1.399, 1.555),
    'R54_W1': _pv('r54_w1', 3, None, 1.536),            # its "long" lens also starts 2021-02-28
    'R55_F1_E1': _pv('r55_engine', 6, 1, 1.672, 1.541),
    'R55_F1_E2': _pv('r55_engine', 7, 2, 1.645, 1.721),
    'R55_F1_E3': _pv('r55_engine', 8, 3, 1.563, 1.658),
    'R55_F2_ML3': _pv('r55_ml', 13, 12, 1.774, 1.736),
    'R55_F2_ML4': _pv('r55_ml', 16, 15, 1.554, 1.637),
    'R55_F4_NDX': _pv('r55_portfolio', 4, 3, 1.690, 1.695),
    'R55_F4_XAG': _pv('r55_portfolio', 7, 6, 1.500, 1.618),
    'R55_F4_COPPER': _pv('r55_portfolio', 10, 9, 1.553, 1.671),
    'R55_F4_EWY': _pv('r55_portfolio', 13, 12, 1.461, 1.628),
    'R55_F4_EWJ': _pv('r55_portfolio', 16, 15, 1.506, 1.604),
    'R55_F4_NOBOND': _pv('r55_portfolio', 17, 0, 1.723, 1.677),
    'R55_F4_PFINAL': _pv('r55_portfolio', 17, 0, 1.723, 1.677),   # = NOBOND by construction (P55_FREEZE)
    'R57_U1': _pv('r57_u1', 13, 5, 1.685, 1.648),
    'R57_Q2': _pv('r59_q', 'Q2_common', 'Q2_long'),
    'R58_F3_I1': _pv('r58_integrate', 4, 3, 1.682, 1.638),
}
_ENG = {'M1': (68, 74), 'M2a': (69, 75), 'M2b': (70, 76), 'M3': (71, 77), 'M3nr': (72, 78)}
_F1B = {'R1': (61, 124), 'R2': (62, 125), 'R3': (63, 126), 'R4': (64, 127), 'R5': (65, 128),
        'N1': (66, 129), 'N2': (67, 130), 'N3': (68, 131)}
_F1C = {'C0': (49, 95), 'C1': (39, 85), 'C2': (41, 87), 'C3': (43, 89), 'C4': (45, 91), 'C5': (47, 93),
        'C6': (48, 94)}
F1_S = {
    **{f'R50_F1_{e}': _pv('r50_engines', c, l, {'eng': e, 'window': 'common'}, {'eng': e, 'window': 'long'})
       for e, (c, l) in _ENG.items()},
    'R50_F1_M4': _pv('r50_engines', 66, 67, {'window': 'common'}, {'window': 'long'}),
    **{f'R50_F1B_{k}': _pv('r50_f1b', c, l, {'cand': k, 'window': 'common'}, {'cand': k, 'window': 'long'})
       for k, (c, l) in _F1B.items()},
    'R50_F1B_R6': _pv('r50_f1b', 70, 133, {'window': 'common'}, {'window': 'long'}),
    'R50_F1B_N4': _pv('r50_f1b', 71, 134, {'window': 'common'}, {'window': 'long'}),
    **{f'R50_F1C_{k}': _pv('r50_f1c', c, l, {'cand': k, 'window': 'common'}, {'cand': k, 'window': 'long'})
       for k, (c, l) in _F1C.items()},
    **{f'R50_F1D_{k}': _pv('r50_f1d', c, l, {'window': 'common'}, {'window': 'long'})
       for k, (c, l) in {'T1': (2, 10), 'T2': (3, 11), 'T3': (4, 12), 'K1': (7, 15), 'X1': (5, 13),
                         'V1': (6, 14)}.items()},
    'R50_F1E_K1r': _pv('r50_f1e', 0, None, {'frm': '2020-02-15'}),
    'R50_F1F_R1_BROAD': _pv('r50_f1f', 22, 46, {'window': 'common'}, {'window': 'long'}),
    **{f'R50_F1G_{g}': _pv('r50_f1g', c, l, {'g': g, 'window': 'common'}, {'g': g, 'window': 'long'})
       for g, (c, l) in {'G1': (20, 43), 'G2': (21, 44), 'G3': (22, 45)}.items()},
    # r51 explore: the decision lens (2018-09-01 -> 2024-12-31) serves both windows.
    **{f'R51_F3_{t}': _pv('r51_A', i, i, {'trial': t, 'lens': 'dec'}, {'trial': t, 'lens': 'dec'})
       for t, i in {'A1': 9, 'A2': 15, 'A3': 21, 'A4': 27, 'A5': 33}.items()},
    **{f'R51_F4_{t}': _pv('r51_B', i, i, {'trial': t, 'lens': 'dec'}, {'trial': t, 'lens': 'dec'})
       for t, i in {'B1': 4, 'B2': 14, 'B3': 20}.items()},
    **{f'R52_F1_{t}': _pv('r52_xs', ij, None, s) for t, ij, s in (
        ('X0', [0, 2], -0.372), ('X1', [4, 6], -0.016), ('X2', [8, 10], 0.170), ('X3', [12, 14], 0.151))},
    'R52_F2_Q2': _pv('r52_q', [4, 5], None, -0.473),
    'R52_F2_Q3': _pv('r52_q', [26, 27], None, -1.722),
    **{f'R53_F1_{t}': _pv('r53_xs', ij, None, s) for t, ij, s in (
        ('Y1', [0, 2], -0.017), ('Y2', [3, 5], -0.194), ('Y3', [9, 11], 0.417), ('Y4', [6, 8], 0.492),
        ('Y5', [12, 14], -0.538))},
    'R53_F1_Y6': _pv('r53_xs_y6', [0, 2], None, -0.045),
    'R54_M1': _pv('r54_m1', 1, None, 0.557),
    'R55_F2_ML1': _pv('r55_ml', [0, 2], None, 0.241),
    'R55_F2_ML2': _pv('r55_ml', [4, 6], None, -0.455),
    'R55_F3_A3v2': _pv('r55_a3', 0, None, {'lens': 'dec', 'tag': 'v2'}),
    'R57_Q1': _pv('r59_q', 'Q1_book', None),
}
F1_SCOPE_OUT = ('R50_F1E_P3', 'R50_F1D_K1', 'R50_F1E_K1r')     # registry: fuera_de_alcance_spot
F1_MISSING = {'R52_F2_Q1': 'prueba de IC del QOI: no tiene serie de retornos'}
CAPTURE = os.path.join(OUT, 'capture')
W_COMMON, W_LONG = ('2021-01-01', '2024-12-31'), ('2018-09-01', '2024-12-31')


def _day(ms_):
    return np.datetime_as_string(np.datetime64(int(ms_), 'ms'), unit='D')


def _cap(tag):
    z = np.load(os.path.join(CAPTURE, f'{tag}.npz'))
    if tag == 'r59_q':
        return z, None
    idx = json.load(open(os.path.join(CAPTURE, f'{tag}.json')))
    return z, {c['i']: c for c in idx['calls'] if 'i' in c}


def _merged_ctx(call):
    out = {}
    for fr in call['ctx']:                        # innermost frame first: it wins
        for k, v in fr.items():
            out.setdefault(k, v)
    return out


def _source_returns(src):
    """(days, simple returns) of one source after its checks; first day of each curve is the base."""
    tag, sel, chk = src
    z, calls = _cap(tag)
    parts = sel if isinstance(sel, list) else [sel]
    days, rets = [], []
    for k, i in enumerate(parts):
        d, v = (z[f'{i}__days'], z[f'{i}__vals']) if calls is None else (z[f'c{i}__days'], z[f'c{i}__vals'])
        if calls is not None:
            c = calls[i]
            if k == 0 and isinstance(chk, float):
                assert c['sharpe'] is not None and abs(c['sharpe'] - chk) < 6e-4, (tag, i, c['sharpe'], chk)
            if isinstance(chk, dict):
                ctx = _merged_ctx(c)
                assert all(ctx.get(a) == b for a, b in chk.items()), (tag, i, chk, ctx)
            if c['kind'] in ('xs_stats', 'q_stats'):  # equity = cumprod(1 + r): the first value holds a return
                days.append(d), rets.append(v / np.r_[1.0, v[:-1]] - 1)
                continue
            if c['kind'] == 'metrics' and c['extra']:
                # en.metrics measures from its frm (e.g. R54_M1 from 2022-01-01, after its training
                # year; F1d sleeves from 2021-01-01 on a curve built from 2020-10-15): same days here.
                m0 = int(np.searchsorted(d, r58.ms(c['extra'][0])))
                d, v = d[m0:], v[m0:]
        days.append(d[1:]), rets.append(v[1:] / v[:-1] - 1)
    d, r = np.concatenate(days), np.concatenate(rets)
    assert (np.diff(d) > 0).all(), (tag, sel)
    keep = d < r58.CUT_MS
    return d[keep], r[keep]


def f1_build():
    """Writes every family member's series to the store and data/r59/f1_series.json (coverage)."""
    fam = json.load(open(os.path.join(OUT, 'spa_families.json')))
    maps = {**F1_P, **F1_S}
    assert set(maps) | set(F1_MISSING) == set(fam['P']) | set(fam['S']), 'map differs from the committed families'
    cov = {}
    for tid, spec in maps.items():
        rnd = tid.split('_')[0].lower()
        for lens, src in spec.items():
            if src is None:
                continue
            d, r = _source_returns(src)
            key = tid if lens == 'common' else f'{tid}@long'
            meta = save_series(rnd, key, d, r, f'r59.py f1_build <- capture/{src[0]}', lens)
            cov[key] = {'from': _day(int(d[0])), 'n_days': meta['n_days'],
                        'sharpe': float(r.mean() / r.std(ddof=1) * math.sqrt(365))}
    z = np.load(os.path.join(CAPTURE, 'r59_q.npz'))
    for k in ('P55_common', 'P55_long', 'R1_common', 'R1_long'):
        d, v = z[f'{k}__days'], z[f'{k}__vals']
        d, r = d[1:], v[1:] / v[:-1] - 1
        keep = d < r58.CUT_MS
        save_series('r59', f'BENCH_{k}', d[keep], r[keep], 'r59.py f1_q (r57.p55_base)', k.split('_')[1])
    out = {'protocol': 'PROTOCOL_R59.md §2', 'families': {'P': len(fam['P']), 'S': len(fam['S'])},
           'with_series': len(maps), 'missing': F1_MISSING, 'excluded': {**fam['excluded_duplicates'], **fam['excluded_holdout']},
           'coverage_of_N145': f'{len(maps)} de 145 ensayos con serie', 'series': cov}
    json.dump(out, open(os.path.join(OUT, 'f1_series.json'), 'w'), indent=1)
    log(f'f1_build: {len(cov)} series ({len(maps)} trials), missing {list(F1_MISSING)}')


def _matrix(ids, lens, window, fill):
    """days x members of daily returns in window. fill=False: days every member has (intersection);
    fill=True: union of days with a missing member's day set to 0 (out of the market = cash)."""
    lo, hi = r58.ms(window[0]), r58.ms(window[1]) + DAY
    ser = {}
    for tid in ids:
        key = tid if lens == 'common' else f'{tid}@long'
        try:
            d, r = load_series(key)
        except KeyError:
            continue
        m = (d >= lo) & (d < hi)
        ser[tid] = dict(zip(d[m].tolist(), r[m].tolist()))
    if lens == 'long':                               # long window: only members that cover it
        ser = {t: s for t, s in ser.items() if s and min(s) <= lo + 31 * DAY}
    sets = [set(s) for s in ser.values()]
    days = sorted(set.union(*sets) if fill else set.intersection(*sets))
    cols = list(ser)
    M = np.array([[ser[t].get(x, 0.0) for t in cols] for x in days])
    return np.array(days), cols, M


def _bench(days, lens):
    d, r = load_series(f'BENCH_R1_{lens}')
    s = dict(zip(d.tolist(), r.tolist()))
    return np.array([s.get(x, np.nan) for x in days.tolist()])


def f1_audit():
    fam = json.load(open(os.path.join(OUT, 'spa_families.json')))
    res = {'protocol': 'PROTOCOL_R59.md §2 + amendment E3', 'seed': SEED, 'n_boot': SPA_BOOT, 'block': SPA_BLOCK,
           'runs': {}}
    plan = [('P', 'common', W_COMMON, False), ('P', 'long', W_LONG, False),
            ('S', 'common', W_COMMON, False), ('S', 'common', W_COMMON, True), ('S', 'long', W_LONG, False)]
    plan += [(f, lens, w, fill, True) for f, lens, w, fill in plan]   # E3: without the out-of-scope trials
    for f, lens, window, fill, *noscope in plan:
        ids = [t for t in fam[f] if not (noscope and t in F1_SCOPE_OUT)]
        days, cols, M = _matrix(ids, lens, window, fill)
        # R1 benchmark: P members use the R1 of their own lens; S members the long-lens R1, which
        # covers both windows (the common-lens R1 starts 2021-02-28).
        b = _bench(days, lens if f == 'P' else 'long')
        ok = np.isfinite(b)
        days, M, b = days[ok], M[ok], b[ok]
        sd = M.std(0, ddof=1)
        sharpe = M.mean(0) / np.where(sd > 0, sd, np.nan) * math.sqrt(365)
        G_r1 = M - b[:, None] * (sd / b.std(ddof=1))[None, :]
        p_cash, best_cash = spa_pvalue(M)
        p_r1, best_r1 = spa_pvalue(G_r1)
        order = list(np.argsort(-np.nan_to_num(sharpe, nan=-9)))
        run = {'family': f, 'lens': lens, 'window': [_day(int(days[0])), _day(int(days[-1]))],
               'days': int(len(days)), 'fill_cash': fill, 'members': len(cols),
               'spa_cash': {'p': p_cash, 'best': cols[best_cash]}, 'spa_r1': {'p': p_r1, 'best': cols[best_r1]},
               'r1_sharpe': float(b.mean() / b.std(ddof=1) * math.sqrt(365)),
               'sharpe': {cols[k]: round(float(sharpe[k]), 4) for k in order}}
        if 'R55_F4_PFINAL' in cols:
            run['pfinal_rank'] = 1 + order.index(cols.index('R55_F4_PFINAL'))
        if f == 'P':
            run['pbo'], run['pbo_combinations'] = pbo(M)
        name = f'{f}_{lens}' + ('_fill' if fill else '') + ('_inscope' if noscope else '')
        res['runs'][name] = run
        log(f"{name}: {len(cols)} x {len(days)} SPA cash p={p_cash:.3f} "
            f"({cols[best_cash]}), vs R1 p={p_r1:.3f} ({cols[best_r1]})" + (f", PBO {run['pbo']:.3f}" if f == 'P' else ''))
    json.dump(res, open(os.path.join(OUT, 'f1_audit.json'), 'w'), indent=1)


# ----------------------------------------------------------------------------------------------
# §3 + E1 F2 prefilter (D only, no oracle query) and q1's power
# ----------------------------------------------------------------------------------------------
P1_MIN_SAT = 5                      # E1: test folds need >= 5 saturated-funding trades (V5a = 0, 7% of trades)
P2_ALPHA = 0.20
Q1_BOOT = 5000                      # §3 (a): 5,000 weekly-block draws
Z95 = 1.6448536269514722            # one-sided 5%: (a) asks the bootstrap p5 > 0


def f2_prefilter():
    import math as m_
    import warnings
    warnings.simplefilter('ignore')
    import r59_oracle as orc
    df = u50_trades()
    R, v5, pe = df['R'].values, df['V5a'].values.astype(float), df['persist'].values.astype(float)
    ok = np.isfinite(v5) & np.isfinite(pe)
    f1 = json.load(open(os.path.join(r58.OUT, 'f1_diag.json')))['variables']['V5a']
    obs = stat_cond(R, v5, pe)
    assert abs(obs - f1['D_cond_V1']) < 1e-9, (obs, f1['D_cond_V1'])    # E1: this is r58's +0.79
    res = {'protocol': 'PROTOCOL_R59.md §3 + E1', 'n_added': 0, 'D_cond_V1_u50': obs, 'n_valid_u50': int(ok.sum())}
    # (p1) the fixed statistic in each coin-group x year test fold (no selection: the hypothesis is set).
    G, folds = load_groups(), []
    for g, members in G.items():
        for y in YEARS:
            te = df['sym'].isin(members).values & (df['year'].values == y) & ok
            n_sat, n_ok = int((v5[te] == 0).sum()), int((v5[te] == 1).sum())
            d = stat_cond(R[te], v5[te], pe[te]) if n_sat >= P1_MIN_SAT and n_ok >= P1_MIN_SAT else None
            folds.append({'group': g, 'year': y, 'n': int(te.sum()), 'n_sat': n_sat,
                          'D_cond': None if d is None or not np.isfinite(d) else float(d)})
    ds = np.array([f['D_cond'] for f in folds if f['D_cond'] is not None], float)
    res['p1'] = {'folds': folds, 'folds_qualifying': int(len(ds)), 'median': float(np.median(ds)) if len(ds) else None,
                 'pos_share': float((ds > 0).mean()) if len(ds) else None}
    res['p1']['pass'] = bool(len(ds) and np.median(ds) > 0)
    log(f"p1: {len(ds)} folds with >= {P1_MIN_SAT} saturated; median D_cond {res['p1']['median']}, "
        f"positive {res['p1']['pos_share']}")
    # (p2) rotation of V5a's 4h series per coin, persist_vol held at each trade's own value.
    grid = bar_grid(df, 'V5a')
    lab = grid.labels()
    both = np.isfinite(lab) & np.isfinite(v5)
    agree = float((lab[both] == v5[both]).mean())
    o2, p2, null = rotation_p(grid, R, N_ROT, SEED + 59, strata=pe)
    res['p2'] = {'label_agreement_with_r58': agree, 'D_cond_grid': o2, 'p_rotation': p2,
                 'null_p5_p95': np.percentile(null, [5, 95]).tolist(), 'pass': bool(p2 < P2_ALPHA)}
    log(f"p2: agree {agree:.4f} D_cond {o2:+.3f} p {p2:.4f}")
    res['prefilter_pass'] = bool(res['p1']['pass'] and res['p2']['pass'])
    # Power (E1): U50 bootstrap SE of D_cond scaled by sqrt(n_U50 / n_H expected); n_H from the U50
    # trade rate per compression-labelled coin-day (2021-07-02..2024) times H's labelled coin-days,
    # which the oracle counts from daily states only (no trades, prices or returns of H).
    week = df['week'].values
    old = r57.N_BOOT
    r57.N_BOOT = Q1_BOOT
    try:
        bs = r57.block_boot(week[ok], lambda ix: (r58._cond(R[ok][ix], v5[ok][ix] == 1, pe[ok][ix]),),
                            np.random.default_rng(SEED + 591))[:, 0]
    finally:
        r57.N_BOOT = old
    se = float(np.nanstd(bs, ddof=1))
    cnt = orc.count_q1()
    conf = df['opened'].values >= r58.CONF_FROM
    rate = (ok & conf).sum() / cnt['u50']['v1_days']
    n_h = rate * (cnt['n2']['v1_days'] + cnt['n3']['v1_days'])
    se_h = se * m_.sqrt(ok.sum() / n_h)
    phi = lambda x: 0.5 * (1 + m_.erf(x / m_.sqrt(2)))
    res['power'] = {'se_u50': se, 'se_r58': f1['D_cond_V1_se'], 'counts': cnt, 'u50_rate_per_v1_day': float(rate),
                    'n_h_expected': float(n_h), 'se_h': se_h,
                    'power_full_effect': phi(obs / se_h - Z95), 'power_half_effect': phi(obs / 2 / se_h - Z95)}
    res['power']['report_before_query'] = bool(res['power']['power_half_effect'] < 0.4)
    log(f"power: se U50 {se:.3f}, n_H ~{n_h:.0f}, se_H {se_h:.3f}; full {res['power']['power_full_effect']:.2f} "
        f"half {res['power']['power_half_effect']:.2f}; prefilter {'PASA' if res['prefilter_pass'] else 'NO PASA'}")
    json.dump(res, open(os.path.join(OUT, 'f2_prefilter.json'), 'w'), indent=1, default=float)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = {'groups': groups, 'cv': cv, 'rotation': rotation, 'series_test': series_test, 'spa_test': spa_test,
          'f1_q': f1_q, 'f1_build': f1_build, 'f1_audit': f1_audit,
          'f2_prefilter': f2_prefilter}.get(cmd)
    if fn is None:
        print(__doc__)
        return 1
    os.makedirs(OUT, exist_ok=True)
    fn()
    return 0


if __name__ == '__main__':
    sys.exit(main())
