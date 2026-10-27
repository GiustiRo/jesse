"""r57: continuous uses of the r56 forecasts on P-r55 (PROTOCOL_R57.md, 208ea238).

    python research_scripts/r57.py states   # F0: partitions per coin-day, written before any join
    python research_scripts/r57.py diag     # F1: attribution diagnostic (N + 0), decides F3 and F4
    python research_scripts/r57.py u1       # F2: U1, forecast vol in R1-BTC/ETH sizing (N 141)
    python research_scripts/r57.py c6sel    # F3: C6 on the alts with S1/S2 selection (N 143)
    python research_scripts/r57.py rev      # F4: M2a on the alts, Q1/Q2 (N 145)

Every forecast was stored by r56 with data through 2024-12-31; nothing here runs torch. A bar
closing at ts reads the forecast row floor(ts / day) - 1, the last day fully closed (asserted).
Outputs go to research_scripts/data/r57/.
"""
import json
import math
import os
import sys
import warnings

import numpy as np
import pandas as pd

import r56_eval as ev

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r57')
R56 = ev.OUT
DAY = ev.DAY
CUT_MS = ev.ms('2024-12-31') + DAY        # exclusive: nothing at or after 2025-01-01
U1_FROM = ev.ms('2021-01-01')
U1_CLIP = (0.5, 2.0)                      # safeguard against broken data only (protocol §2)
DIAG_FROM = ev.ms('2021-07-02')
SEED, N_BOOT = 57, 5000
HIGH = 2                                  # T3 class 'alta'
YEARS = ('2021', '2022', '2023', '2024')


def _load(name):
    return np.load(os.path.join(R56, name + '.npy')).astype(float)


def _merge(dev, hold, is_hold):
    """Development-coin predictions with the holdout columns (0-49 of panel70) filled in."""
    return np.where(is_hold[None, :, None], hold[:, :dev.shape[1]], dev)


def row_for(days, ts):
    """Forecast row usable by a decision at ts: the last day whose close is <= ts."""
    r = int(np.searchsorted(days, (int(ts) // DAY) * DAY)) - 1
    assert r < 0 or days[r] + DAY <= ts, (r, ts)
    return r


def ratio_bias(c, pred, h):
    """b_q per calendar quarter: mean(target - pred) on development-coin rows known at q0 (<= q0-40),
    as r56_eval.chronos_feats; returns (quarter start ms array, b array)."""
    days = c['days']
    qs = pd.date_range('2020-04-01', '2025-01-01', freq='QS', tz='UTC')
    starts, bs = [], []
    di = np.arange(len(days))[:, None]
    for q in qs:
        q0 = int(np.searchsorted(days, q.value // 10**6))
        tr = (c['P']['elig'] & c['is_dev'][None, :] & (di <= q0 - 2 * ev.H) & np.isfinite(pred)
              & np.isfinite(h['target']))
        starts.append(q.value // 10**6)
        bs.append(float(np.mean(h['target'][tr] - pred[tr])) if tr.sum() >= 200 else np.nan)
    return np.array(starts, dtype=np.int64), np.array(bs)


def log_ratio(c, pred, h, qstart, qb):
    """pred - l20 + b_q per (day, coin): log of forecast / trailing 20-day RV, bias-corrected."""
    q = np.searchsorted(qstart, c['days'], side='right') - 1
    b = np.where(q >= 0, qb[np.clip(q, 0, None)], np.nan)
    return pred - h['l_20'] + b[:, None]


# ----------------------------------------------------------------------------------------------
# F0: partitions
# ----------------------------------------------------------------------------------------------
def states():
    os.makedirs(OUT, exist_ok=True)
    ev.MODE70 = False
    ev._CTX.clear()
    c = ev.ctx()
    days, syms, is_hold, is_dev = c['days'].copy(), list(c['syms']), c['is_hold'].copy(), c['is_dev'].copy()
    assert days[-1] < CUT_MS
    picks = json.load(open(os.path.join(R56, 'f8.json')))['T3']['picks']['vol']
    P = _merge(_load('pred_T3_vol'), _load('pred_hold_T3_vol'), is_hold)
    s_t3 = ev.apply_picks(P, 'hyst', picks)
    persist = c['L']['persist_vol']
    R = _merge(_load('pred_P5_range40'), _load('pred_hold_P5_range40'), is_hold)
    p_rng = R[..., 1]                                     # class 1 = range (mean matches the label)
    dev_rows = (days >= ev.ms('2021-07-01')) & (days <= ev.ms('2023-12-31'))
    m = c['P']['elig'] & is_dev[None, :] & dev_rows[:, None] & np.isfinite(p_rng)
    cut = float(np.quantile(p_rng[m], 2 / 3))
    h = ev.har_inputs(20)
    pred = _load('chronos_chronos2cov')
    qstart, qb = ratio_bias(c, pred, h)
    lr = log_ratio(c, pred, h, qstart, qb)
    elig = c['P']['elig'].copy()      # ev.ctx() returns the module cache, which is cleared below

    # N2 (panel70 columns 50-69): T3 states with the same quarterly picks, P5, the ratio.
    ev.MODE70 = True
    ev._CTX.clear()
    c7 = ev.ctx()
    assert (c7['days'] == days).all() and c7['syms'][:50] == syms
    n2 = np.where(c7['is_n2'])[0]
    P7 = _load('pred_n2_T3_vol')
    s7 = ev.apply_picks(P7, 'hyst', picks)
    p7 = _load('pred_n2_P5_range40')[..., 1]
    h7 = ev.har_inputs(20)
    lr7 = log_ratio(c7, _load('chronos_chronos2cov_panel70'), h7, qstart, qb)
    n2_syms, n2_elig = [c7['syms'][j] for j in n2], c7['P']['elig'][:, n2].copy()
    ev.MODE70 = False
    ev._CTX.clear()

    np.savez_compressed(os.path.join(OUT, 'f0_states.npz'), days=days, syms=np.array(syms), s_t3=s_t3,
                        persist=persist, p_rng=p_rng, log_ratio=lr, elig=elig,
                        n2_syms=np.array(n2_syms), n2_s_t3=s7[:, n2], n2_p_rng=p7[:, n2],
                        n2_log_ratio=lr7[:, n2], n2_elig=n2_elig)
    ok = s_t3 >= 0
    info = {'protocol': 'PROTOCOL_R57.md §0 (208ea238)', 'p_range_cut_q2_3_dev': cut,
            't3_picks': picks, 'ratio_bias_by_quarter': {pd.Timestamp(int(s), unit='ms').strftime('%Y-%m-%d'): b
                                                         for s, b in zip(qstart, qb)},
            'coverage': {'t3_state_rows': int(ok.sum()), 't3_first_day': str(pd.Timestamp(int(days[np.argmax(ok.any(1))]), unit='ms').date()),
                         'n2_t3_state_rows': int((s7[:, n2] >= 0).sum()),
                         't3_class_share': [float(np.mean(s_t3[ok] == k)) for k in range(3)],
                         'p_range_high_share_all': float(np.mean(p_rng[np.isfinite(p_rng)] >= cut))}}
    json.dump(info, open(os.path.join(OUT, 'f0_cuts.json'), 'w'), indent=2)
    print(json.dumps(info, indent=1)[:1500])


def load_states():
    z = np.load(os.path.join(OUT, 'f0_states.npz'))
    s = {k: z[k] for k in z.files}
    s['syms'] = [str(x) for x in s['syms']]
    s['n2_syms'] = [str(x) for x in s['n2_syms']]
    s['cut'] = json.load(open(os.path.join(OUT, 'f0_cuts.json')))['p_range_cut_q2_3_dev']
    return s


# ----------------------------------------------------------------------------------------------
# F1: diagnostic
# ----------------------------------------------------------------------------------------------
def _week(ts):
    d = pd.Timestamp(int(ts), unit='ms', tz='UTC').isocalendar()
    return f'{d[0]}-{d[1]:02d}'


def _diff(R, grp):
    a, b = R[grp], R[~grp]
    return float(a.mean() - b.mean()) if len(a) and len(b) else float('nan')


def block_boot(keys, stat, rng):
    """Bootstrap over blocks (unique keys) with replacement; stat(index array) -> tuple of floats."""
    uk, inv = np.unique(keys, return_inverse=True)
    members = [np.flatnonzero(inv == i) for i in range(len(uk))]
    out = []
    for _ in range(N_BOOT):
        pick = rng.integers(0, len(uk), len(uk))
        out.append(stat(np.concatenate([members[i] for i in pick])))
    return np.array(out)


def diag_trades(s):
    ev_ = json.load(open(os.path.join(HERE, 'data', 'r52', 'v1_events.json')))
    col = {x: j for j, x in enumerate(s['syms'])}
    rows = []
    for e in ev_:
        if e['opened'] < DIAG_FROM or e['opened'] >= CUT_MS:
            continue
        r = row_for(s['days'], e['opened'])
        j = col[e['sym']]
        st, pe = int(s['s_t3'][r, j]), s['persist'][r, j]
        if st < 0 or not np.isfinite(pe):
            continue
        rows.append({'sym': e['sym'], 'sleeve': e['sleeve'], 'opened': e['opened'], 'R': e['R'], 't3': st,
                     'pers': int(pe), 'p_rng': float(s['p_rng'][r, j]),
                     'year': pd.Timestamp(e['opened'], unit='ms').strftime('%Y'), 'week': _week(e['opened'])})
    df = pd.DataFrame(rows)
    R = df['R'].values
    g_t3, g_pe = (df['t3'] == HIGH).values, (df['pers'] == HIGH).values
    g_rg = (df['p_rng'] >= s['cut']).values
    rng = np.random.default_rng(SEED)
    bs = block_boot(df['week'].values, lambda ix: (_diff(R[ix], g_t3[ix]), _diff(R[ix], g_pe[ix]),
                                                   _diff(R[ix], g_rg[ix])), rng)
    ci = lambda k: [float(np.nanpercentile(bs[:, k], 5)), float(np.nanpercentile(bs[:, k], 95))]
    d_t3, d_pe, d_rg = _diff(R, g_t3), _diff(R, g_pe), _diff(R, g_rg)
    by_year = {y: {'d_t3': _diff(R[(df['year'] == y).values], g_t3[(df['year'] == y).values]),
                   'd_pers': _diff(R[(df['year'] == y).values], g_pe[(df['year'] == y).values]),
                   'n': int((df['year'] == y).sum())} for y in YEARS}
    tab = lambda key: {int(k): {'n': int(len(g)), 'mean_R': float(g['R'].mean()), 'sum_R': float(g['R'].sum()),
                                'win': float((g['R'] > 0).mean())} for k, g in df.groupby(key)}
    diff_ci = np.nanpercentile(bs[:, 0] - bs[:, 1], [5, 95]).tolist()
    rule = {'d_t3_pos_ci': d_t3 > 0 and ci(0)[0] > 0,
            'years_pos_ge_3': sum(by_year[y]['d_t3'] > 0 for y in YEARS) >= 3,
            'd_t3_gt_d_pers': d_t3 > d_pe}
    return {'n_trades': int(len(df)), 'n_coins': int(df['sym'].nunique()), 'mean_R_all': float(R.mean()),
            'by_t3': tab('t3'), 'by_persistence': tab('pers'),
            'by_p_range': {'high': {'n': int(g_rg.sum()), 'mean_R': float(R[g_rg].mean())},
                           'low': {'n': int((~g_rg).sum()), 'mean_R': float(R[~g_rg].mean())}},
            'D_T3': d_t3, 'D_T3_ci90': ci(0), 'D_pers': d_pe, 'D_pers_ci90': ci(1),
            'D_T3_minus_D_pers_ci90': diff_ci, 'D_range_high': d_rg, 'D_range_high_ci90': ci(2),
            'by_year': by_year, 'rule_F3': rule, 'F3_go': bool(all(rule.values()))}


def diag_autocorr(s):
    """Sum over lags 1-5 of corr(r[d+1], r[d+1-k]) pooled over alt-days, split by p_range at row d."""
    ev.MODE70 = False
    ev._CTX.clear()
    c = ev.ctx()
    days = c['days']
    alts = [j for j, x in enumerate(s['syms']) if x not in ('BTCUSDT', 'ETHUSDT')]
    lr = np.diff(np.log(c['P']['c']), axis=0)
    r = np.vstack([np.full((1, lr.shape[1]), np.nan), lr])        # r[t] = log c[t] / c[t-1]
    rows = (days >= DIAG_FROM) & (days < CUT_MS - DAY)
    win = rows[:, None] & np.isfinite(r)
    mu = np.array([np.nanmean(np.where(win[:, j], r[:, j], np.nan)) for j in range(r.shape[1])])
    r = r - mu[None, :]
    D = len(days)
    recs = []
    for d in np.flatnonzero(rows):
        if d + 1 >= D or d - 4 < 1:
            continue
        for j in alts:
            p = s['p_rng'][d, j]
            y = r[d + 1, j]
            x = r[d - 4:d + 1, j][::-1]          # r[d], r[d-1], ..., r[d-4] = lags 1..5 of r[d+1]
            if not (np.isfinite(p) and np.isfinite(y) and np.isfinite(x).all() and c['P']['elig'][d, j]):
                continue
            recs.append((d, p >= s['cut'], y, *x))
    A = np.array(recs, dtype=float)
    dd, hi, y, X = A[:, 0].astype(int), A[:, 1].astype(bool), A[:, 2], A[:, 3:]
    weeks = np.array([_week(days[d]) for d in dd])

    def ac(ix):
        if len(ix) < 50:
            return float('nan')
        return float(sum(np.corrcoef(y[ix], X[ix, k])[0, 1] for k in range(5)))

    def stat(ix):
        h = ix[hi[ix]]
        l_ = ix[~hi[ix]]
        return ac(h), ac(l_)
    rng = np.random.default_rng(SEED)
    bs = block_boot(weeks, stat, rng)
    all_ix = np.arange(len(y))
    a_hi, a_lo = stat(all_ix)
    per_lag = {g: [float(np.corrcoef(y[m], X[m, k])[0, 1]) for k in range(5)]
               for g, m in (('high', hi), ('low', ~hi))}
    ci_hi = np.nanpercentile(bs[:, 0], [5, 95]).tolist()
    rule = {'ac_high_neg_ci': a_hi < 0 and ci_hi[1] < 0, 'ac_high_lt_low': a_hi < a_lo}
    return {'n_alt_days': int(len(y)), 'n_high': int(hi.sum()), 'AC_high': a_hi, 'AC_high_ci90': ci_hi,
            'AC_low': a_lo, 'AC_low_ci90': np.nanpercentile(bs[:, 1], [5, 95]).tolist(),
            'AC_high_minus_low_ci90': np.nanpercentile(bs[:, 0] - bs[:, 1], [5, 95]).tolist(),
            'per_lag': per_lag, 'rule_F4': rule, 'F4_go': bool(all(rule.values()))}


def diag_sleeves(s):
    """(b)+(c), descriptive: P-r55 BTC/ETH R1 and C6 trades by their coin's T3 state at the row before
    opening, and the daily returns of each sleeve by the previous row's state."""
    import r50_engines as en
    import r51_lib as lib
    r1, r1_tr, c6, c6_tr, data = lib.p1_sleeves('common')
    col = {'BTC': s['syms'].index('BTCUSDT'), 'ETH': s['syms'].index('ETHUSDT')}
    out = {'trades': {}, 'daily': {}}
    import r50_f1b as fb
    from r50_engines import simulate
    for name in ('BTC', 'ETH'):
        d = data[name]
        j = col[name]
        _, _, acct = fb.r1_run(name, d)
        trs = {'R1': acct.trades}
        c6t = []
        for retest in (False, True):
            _, _, a = simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], retest), name, d['funding'], fb.H4_MS)
            c6t += a.trades
        trs['C6'] = c6t
        for sl, tl in trs.items():
            g = {}
            for t in tl:
                if t['opened'] is None or t['opened'] < DIAG_FROM or t['opened'] >= CUT_MS:
                    continue
                st = int(s['s_t3'][row_for(s['days'], t['opened']), j])
                g.setdefault(st, []).append(t['pnl'])
            out['trades'][f'{sl}_{name}'] = {k: {'n': len(v), 'mean_pnl': float(np.mean(v)), 'sum_pnl': float(np.sum(v))}
                                             for k, v in sorted(g.items())}
        for sl, cv in (('R1', r1[name]), ('C6', c6[name])):
            rets = en.daily_returns(*cv)
            g = {}
            for day_ms, x in rets.items():
                if day_ms < DIAG_FROM or day_ms >= CUT_MS:
                    continue
                r = row_for(s['days'], day_ms)          # day_ms = close of the return's day
                if r < 0:
                    continue
                g.setdefault(int(s['s_t3'][r, j]), []).append(x)
            out['daily'][f'{sl}_{name}'] = {k: {'n': len(v), 'mean': float(np.mean(v)), 'vol_ann': float(np.std(v) * math.sqrt(365)),
                                                'sharpe': float(np.mean(v) / np.std(v) * math.sqrt(365)) if np.std(v) > 0 else None}
                                            for k, v in sorted(g.items())}
    return out


def diag():
    warnings.simplefilter('ignore')
    s = load_states()
    res = {'protocol': 'PROTOCOL_R57.md §1 (208ea238)', 'n_added': 0, 'p_range_cut': s['cut']}
    res['a_c6_alts'] = diag_trades(s)
    print('a', json.dumps({k: res['a_c6_alts'][k] for k in ('n_trades', 'D_T3', 'D_T3_ci90', 'D_pers', 'D_pers_ci90', 'rule_F3', 'F3_go')}))
    res['f4_autocorr'] = diag_autocorr(s)
    print('ac', json.dumps({k: res['f4_autocorr'][k] for k in ('n_alt_days', 'AC_high', 'AC_high_ci90', 'AC_low', 'rule_F4', 'F4_go')}))
    res['bc_p55_crypto'] = diag_sleeves(s)
    print('bc', json.dumps(res['bc_p55_crypto'])[:2000])
    json.dump(res, open(os.path.join(OUT, 'f1_diag.json'), 'w'), indent=2, default=float)


# ----------------------------------------------------------------------------------------------
# P-r55 base (shared by F2 and F4)
# ----------------------------------------------------------------------------------------------
def p55_base():
    """P-r55 components per window ({'R1', 'C6'}, start, sleeves) and the r55 quarterly labels."""
    import r50_f1b as fb
    import r51_lib as lib
    import r55_regimes as rg
    t, c = rg.btc_daily()
    qlab, mlab = rg.labels_a(t, c), rg.labels_a(t, c, monthly=True)
    base = {}
    for w in ('long', 'common'):
        r1, _, c6, _, data = lib.p1_sleeves(w)
        r1 = {n: cv for n, cv in r1.items() if n != 'BOND'}
        comps = {'R1': fb.basket(r1, list(r1)), 'C6': fb.basket(c6, list(c6))}
        start = max(int(cv[0][0]) for cv in comps.values()) + DAY
        base[w] = {'comps': comps, 'start': start, 'r1': r1, 'data': data}
    return base, qlab, mlab


def evaluate(comps, start, qlab, mlab):
    import r55_engine as eg
    return eg.evaluate(*eg.portfolio(comps, start), qlab, mlab)


P55_REF = {'long': 1.677, 'common': 1.723}      # P55_FREEZE.md


# ----------------------------------------------------------------------------------------------
# F2: U1
# ----------------------------------------------------------------------------------------------
def u1_engine_cls():
    import r50_harness as hz

    class DonchianU1(hz.DonchianEnsR49):
        """r49 ensemble whose sizing vol is sigma30 * m(day): m from the stored Chronos-2 + covariates
        forecast (protocol §2). Only _target changes; it repeats the parent's arithmetic."""

        def __init__(self, mult, **kw):
            super().__init__(**kw)
            self.mult = mult
            self.log = []

        def _target(self, allc, i, acct):
            self._update(allc, i)
            if not self.states:
                return 0.0
            frac = sum(self.states) / len(self.states)
            if frac <= 0:
                return 0.0
            closes = self._series(allc, i)[-self.vol_window - 1:, hz.C]
            rets = np.diff(np.log(closes))
            rv = float(np.std(rets, ddof=1)) * self.ann if len(rets) > 10 else float('nan')
            if not math.isfinite(rv) or rv <= 0:
                return 0.0
            m = self.mult(int(allc[i, hz.T]) + 4 * 3_600_000)
            self.log.append(m)
            price = allc[i, hz.C]
            notional_x = min(self.MAX_NOTIONAL_X, frac * self.TARGET_VOL / (rv * m))
            return max(acct.equity(price) * notional_x / price, 0.0)
    return DonchianU1


def make_mult(s, sym):
    j = s['syms'].index(sym)
    lr = s['log_ratio'][:, j]

    def mult(close_ts):
        if close_ts < U1_FROM or close_ts >= CUT_MS:
            return 1.0
        r = row_for(s['days'], close_ts)
        x = lr[r] if r >= 0 else np.nan
        if not np.isfinite(x):
            return 1.0
        return float(np.clip(math.sqrt(math.exp(x)), *U1_CLIP))
    return mult


def r1_curve(name, d, mult=None, fee_x=1.0):
    """fb.r1_run with an optional U1 multiplier and a fee multiplier; calendar curve as p1_sleeves."""
    import r50_engines as en
    import r50_f1b as fb
    import r50_harness as hz
    import r51_lib as lib
    h4 = d['h4']
    k = int(np.searchsorted(h4[:, hz.T], d['start_ms'], side='left'))
    warm, bars = h4[max(0, k - 1520):k], h4[k:]
    acct = fb.SlipAccount(en.BALANCE, en.TAKER * fee_x, 3, en.SLIP_BPS.get(name, 0.0))
    fund = hz.load_funding(en.FUNDING[name]) if d['funding'] and name in en.FUNDING else None
    eng = u1_engine_cls()(mult, **fb.R1_CFG[name]) if mult else hz.DonchianEnsR49(**fb.R1_CFG[name])
    ts, eq = hz.run(eng, warm, bars, fb.H4_MS, acct, fund)
    cv = en.calendar(ts, eq, lib._date(d['start_ms']), en.COMMON[1])
    return cv, acct, (eng.log if mult else None)


def u1():
    warnings.simplefilter('ignore')
    import r50_engines as en
    import r50_f1b as fb
    import r55_engine as eg
    eg.N_DECLARED = 141
    s = load_states()
    base, qlab, mlab = p55_base()
    res = {'protocol': 'PROTOCOL_R57.md §2 (208ea238)', 'n_declared': 141}
    ev_base, ev_u1, ev_b2, ev_u2, sleeves = {}, {}, {}, {}, {}
    for w, b in base.items():
        ev_base[w] = evaluate(b['comps'], b['start'], qlab, mlab)
        assert abs(ev_base[w]['sharpe'] - P55_REF[w]) < 0.0015, (w, ev_base[w]['sharpe'])
        r1u, r1b2, r1u2 = dict(b['r1']), dict(b['r1']), dict(b['r1'])
        for name, sym in (('BTC', 'BTCUSDT'), ('ETH', 'ETHUSDT')):
            d = b['data'][name]
            same, _, _ = r1_curve(name, d)
            assert np.allclose(same[1], b['r1'][name][1]), f'R1 {name} {w} not reproduced'
            cu, acct_u, log = r1_curve(name, d, make_mult(s, sym))
            c2, acct_b2, _ = r1_curve(name, d, fee_x=2.0)
            cu2, _, _ = r1_curve(name, d, make_mult(s, sym), fee_x=2.0)
            r1u[name], r1b2[name], r1u2[name] = cu, c2, cu2
            lg = np.array(log)
            act = lg[lg != 1.0]
            own_b = en.metrics(*b['r1'][name], [], d['mfrom'])
            own_u = en.metrics(*cu, [], d['mfrom'])
            sleeves[f'{name}_{w}'] = {'m_active_share': float(len(act) / max(len(lg), 1)),
                                      'm_median': float(np.median(act)) if len(act) else None,
                                      'm_p05_p95': np.percentile(act, [5, 95]).tolist() if len(act) else None,
                                      'm_clipped_share': float(np.mean((act <= U1_CLIP[0]) | (act >= U1_CLIP[1]))) if len(act) else None,
                                      'own_sharpe_base': own_b['sharpe'], 'own_sharpe_u1': own_u['sharpe'],
                                      'own_cagr_base': own_b['cagr'], 'own_cagr_u1': own_u['cagr'],
                                      'own_dd_base': own_b['max_dd'], 'own_dd_u1': own_u['max_dd'],
                                      'trades_base': None, 'trades_u1': len(acct_u.trades)}
        mk = lambda r1: {'R1': fb.basket(r1, list(r1)), 'C6': b['comps']['C6']}
        ev_u1[w] = evaluate(mk(r1u), b['start'], qlab, mlab)
        ev_b2[w] = evaluate(mk(r1b2), b['start'], qlab, mlab)
        ev_u2[w] = evaluate(mk(r1u2), b['start'], qlab, mlab)
    gt = eg.gates('U1', ev_base, ev_u1)
    gt['gates']['cost2_dsharpe_common_ge_0'] = ev_u2['common']['sharpe'] - ev_b2['common']['sharpe'] >= 0
    gt['gates']['dd_not_worse_1pp'] = all(ev_u1[w]['max_dd'] - ev_base[w]['max_dd'] >= -0.01 for w in ev_u1)
    gt['pass'] = bool(all(gt['gates'].values()))
    res.update({'P55': ev_base, 'U1': ev_u1, 'cost2': {'base': {w: ev_b2[w]['sharpe'] for w in ev_b2},
                                                       'u1': {w: ev_u2[w]['sharpe'] for w in ev_u2}},
                'sleeves': sleeves, **gt})
    print('U1', 'PASS' if gt['pass'] else 'no', gt['gates'], {k: round(x, 4) for k, x in gt['deltas'].items()})
    for w in ev_u1:
        print(' ', w, 'base', round(ev_base[w]['sharpe'], 3), 'u1', round(ev_u1[w]['sharpe'], 3),
              'cost2', round(ev_b2[w]['sharpe'], 3), round(ev_u2[w]['sharpe'], 3))
    print(json.dumps(sleeves, default=float)[:1500])
    json.dump(res, open(os.path.join(OUT, 'f2_u1.json'), 'w'), indent=2, default=float)


def main():
    cmds = {'states': states, 'diag': diag, 'u1': u1}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        return 1
    cmds[sys.argv[1]]()
    return 0


if __name__ == '__main__':
    sys.exit(main())
