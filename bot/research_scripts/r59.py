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


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = {'groups': groups, 'cv': cv, 'rotation': rotation, 'series_test': series_test}.get(cmd)
    if fn is None:
        print(__doc__)
        return 1
    os.makedirs(OUT, exist_ok=True)
    fn()
    return 0


if __name__ == '__main__':
    sys.exit(main())
