"""r52 J1: regime permission from a 2-state statistical jump model on BTC daily, applied to P1.

PROTOCOL_R52.md F3 (J1) and F4:
* features on BTC spot daily log returns r: EWMA downside deviation sqrt(EWMA(min(r, 0)^2)) and
  EWMA Sortino EWMA(r) / downside deviation, half-lives 5, 10 and 21 days (6 features);
* jump model (Nystrup; Shu, Yu and Mulvey 2024): minimise sum ||x_t - mu_s_t||^2 + lambda * #jumps,
  lambda = 50 fixed, by coordinate descent (Viterbi path given centres, centres = state means),
  k-means++ init with seed 0, 10 restarts of at most 50 iterations, best objective kept;
* refit at each month start on all data from the first valid feature day to the previous day,
  standardising with that sample's mean / std (no look-ahead); the state of day t is the last
  state of the optimal path up to t with the month's centres, applied with a 1-day delay;
* the risk state is the fitted state with the lower mean BTC daily return in the fit sample;
* on risk days the daily returns of R1/BTC, R1/ETH (inside the R1 basket) and of the whole C6
  basket are multiplied by 0.5 (fees saved are ignored, as declared);
* gate = r51 inclusion rule P1 vs P1-J1 in both P1 windows, measured only through 2024-12-31.
  2025 is sealed: no metric over 2025 is computed here.

    python research_scripts/r52_j1.py run

writes research_scripts/data/r52/j1.json, j1_states.npy and j1_components.npy.
"""
import json
import os
import sys

import numpy as np
import pandas as pd

import r50_engines as en
import r50_f1b as fb
import r50_f2 as f2
import r51_lib as lib
import r51_sleeves as sv
import r51_f6 as f6
from r50_harness import T, C, DAY_MS
from r50_engines import daily_returns

OUT = os.path.join(lib.HERE, 'data', 'r52')
HALF_LIVES = (5, 10, 21)
LAMBDA = 50.0
N_RESTARTS, MAX_ITER = 10, 50
SCALE = 0.5
# Burn-in: 3x the longest half-life so the EWMAs have forgotten their seed value.
BURN_DAYS = 63
# Minimum fit sample (not set by the protocol): half a year, so that the first state exists
# before the 2018-09 start of P1's long window.
MIN_FIT_DAYS = 180
N_DECLARED = 109
CUT = '2024-12-31'
CUT_MS = None  # set in run() from CUT


# ----------------------------------------------------------------------------------------------
# Features
# ----------------------------------------------------------------------------------------------
def features(bars):
    """Day stamps (bar open, 00:00 UTC), log returns and the 6 raw features; NaN in burn-in."""
    c = bars[:, C]
    r = np.r_[np.nan, np.diff(np.log(c))]
    s = pd.Series(r)
    cols = []
    for h in HALF_LIVES:
        dd = np.sqrt(s.clip(upper=0).pow(2).ewm(halflife=h, adjust=True).mean())
        mu = s.ewm(halflife=h, adjust=True).mean()
        cols += [dd.values, (mu / dd).values]
    X = np.column_stack(cols)
    X[:BURN_DAYS + 1] = np.nan
    return bars[:, T].astype(np.int64), r, X


# ----------------------------------------------------------------------------------------------
# Jump model
# ----------------------------------------------------------------------------------------------
def forward(X, mu, lam):
    """Viterbi forward pass: V[t, s] = best cost of a path ending in s at t, plus backpointers."""
    loss = ((X[:, None, :] - mu[None, :, :]) ** 2).sum(axis=2)
    n, k = loss.shape
    assert k == 2
    # Plain-float loop for the 2-state case: numpy per-step overhead dominates otherwise.
    l0, l1 = loss[:, 0].tolist(), loss[:, 1].tolist()
    V0, V1 = [l0[0]], [l1[0]]
    b0, b1 = [0], [1]
    a, b = l0[0], l1[0]
    for t in range(1, n):
        # Ties keep the current state (no jump).
        if a <= b + lam:
            n0, p0 = a, 0
        else:
            n0, p0 = b + lam, 1
        if b <= a + lam:
            n1, p1 = b, 1
        else:
            n1, p1 = a + lam, 0
        a, b = l0[t] + n0, l1[t] + n1
        V0.append(a); V1.append(b); b0.append(p0); b1.append(p1)
    return np.column_stack([V0, V1]), np.column_stack([b0, b1]).astype(np.int8)


def viterbi(X, mu, lam):
    V, back = forward(X, mu, lam)
    s = np.empty(len(X), dtype=np.int8)
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


def fit(X, k=2, lam=LAMBDA):
    """Coordinate descent from k-means++ starts (seed 0); the best objective over restarts."""
    rng = np.random.default_rng(0)
    best = None
    for _ in range(N_RESTARTS):
        mu = kmeanspp(X, k, rng)
        s_prev = None
        for _ in range(MAX_ITER):
            s, obj = viterbi(X, mu, lam)
            if s_prev is not None and np.array_equal(s, s_prev):
                break
            # A state left empty keeps its previous centre.
            mu = np.array([X[s == j].mean(axis=0) if (s == j).any() else mu[j] for j in range(k)])
            s_prev = s
        s, obj = viterbi(X, mu, lam)
        if best is None or obj < best[0]:
            best = (obj, mu, s)
    return best


def online_states(days, r, X):
    """Risk flag known at the close of each day (NaN before the first fit), monthly refits."""
    valid = ~np.isnan(X).any(axis=1)
    v0 = int(np.argmax(valid))
    months = pd.to_datetime(days, unit='ms', utc=True).strftime('%Y-%m').values
    risk = np.full(len(days), np.nan)
    fits = []
    starts = [i for i in range(v0 + 1, len(days)) if months[i] != months[i - 1]]
    for i in starts:
        if i - v0 < MIN_FIT_DAYS:
            continue
        fit_X = X[v0:i]
        m, sd = fit_X.mean(axis=0), fit_X.std(axis=0, ddof=1)
        obj, mu, s = fit((fit_X - m) / sd)
        means = [float(r[v0:i][s == j].mean()) if (s == j).any() else np.inf for j in range(2)]
        risk_state = int(np.argmin(means))
        end = i
        while end < len(days) and months[end] == months[i]:
            end += 1
        # The last state of the optimal path up to t is argmin of the forward value at t, so one
        # forward pass over the history up to the month end gives every day's online state.
        V, _ = forward((X[v0:end] - m) / sd, mu, LAMBDA)
        risk[i:end] = (V[i - v0:end - v0].argmin(axis=1) == risk_state).astype(float)
        fits.append({'month': months[i], 'obj': obj, 'risk_state_mean_ret': means[risk_state],
                     'other_mean_ret': means[1 - risk_state], 'fit_risk_share': float((s == risk_state).mean())})
    return risk, fits


# ----------------------------------------------------------------------------------------------
# P1-J1
# ----------------------------------------------------------------------------------------------
def scaled_curve(cv, risk_days):
    """Curve whose daily return on each risk day is multiplied by SCALE."""
    days, vals = cv
    r = np.diff(vals) / vals[:-1]
    r = np.where(np.isin(days[1:], risk_days), r * SCALE, r)
    return days, en.BALANCE * np.r_[1.0, np.cumprod(1 + r)]


def cut_to(cv, last_ms):
    days, vals = cv
    k = days <= last_ms
    return days[k], vals[k]


def metrics(comps, start):
    cut = {k: cut_to(f6.trim(v, start), CUT_MS) for k, v in comps.items()}
    days, vals, contrib, _ = lib.portfolio_attr(cut, list(cut))
    assert lib._date(days[-1]) == CUT
    f2.N_DECLARED = N_DECLARED
    # No trade list: pf_trades would include 2025 trades; it is not part of the J1 gate.
    m = f2.r9(days, vals, [])
    m['q_pos_count'] = int(round(m['quarters_pos'] * m['n_quarters']))
    return m


def run():
    global CUT_MS
    CUT_MS = int(pd.Timestamp(CUT, tz='UTC').value // 10**6)
    os.makedirs(OUT, exist_ok=True)
    bars = sv.daily('BTC', 'spot')
    bars = bars[bars[:, T] < pd.Timestamp('2026-01-01', tz='UTC').value // 10**6]
    days, r, X = features(bars)
    risk, fits = online_states(days, r, X)
    # 1-day delay: the state known at the close of day t scales the return of day t + 1 (a curve
    # return keyed d is the return earned during calendar day d).
    applied_days = days + DAY_MS
    risk_days = applied_days[risk == 1]

    known = ~np.isnan(risk) & (days <= CUT_MS)
    st = np.column_stack([days[known], risk[known]])
    np.save(os.path.join(OUT, 'j1_states.npy'), st)
    years = pd.to_datetime(st[:, 0], unit='ms', utc=True).year
    share = {int(y): float(st[years == y, 1].mean()) for y in np.unique(years)}
    switches = int((np.diff(st[:, 1]) != 0).sum())
    assert 0 < st[:, 1].mean() < 1, 'constant state series'

    out = {'protocol': 'RESEARCH_HUB/revisions/20261026-r52/PROTOCOL_R52.md F3', 'n_declared': N_DECLARED,
           'lambda': LAMBDA, 'half_lives': HALF_LIVES, 'burn_days': BURN_DAYS, 'min_fit_days': MIN_FIT_DAYS,
           'measured_through': CUT, 'first_state_day': lib._date(st[0, 0]),
           'risk_share_by_year': share, 'risk_share_total': float(st[:, 1].mean()), 'switches': switches,
           'n_fits': len([f for f in fits if f['month'] <= CUT[:7]]), 'windows': {}}
    comps_save = {}
    keys = ('from', 'to', 'cagr', 'max_dd', 'sharpe', 'quarters_pos', 'q_pos_count', 'n_quarters', 'by_year', 'dsr')
    for w in ('long', 'common'):
        comps, _, extra = lib.p1_components(w)
        rebuilt = fb.basket(extra['r1'], list(extra['r1']))
        assert np.allclose(rebuilt[1], comps['R1'][1]), 'R1 basket not reproduced'
        r1 = {n: (scaled_curve(cv, risk_days) if n in ('BTC', 'ETH') else cv) for n, cv in extra['r1'].items()}
        j1 = {'R1': fb.basket(r1, list(r1)), 'C6': scaled_curve(comps['C6'], risk_days)}
        comps_save[w] = j1
        start = max(int(cv[0][0]) for cv in comps.values()) + DAY_MS
        mb, mj = metrics(comps, start), metrics(j1, start)
        out['windows'][w] = {'from': lib._date(start), 'P1': {k: mb[k] for k in keys}, 'P1_J1': {k: mj[k] for k in keys}}
    L, Cm = out['windows']['long'], out['windows']['common']
    dl = L['P1_J1']['sharpe'] - L['P1']['sharpe']
    dq = L['P1_J1']['q_pos_count'] - L['P1']['q_pos_count']
    dc = Cm['P1_J1']['sharpe'] - Cm['P1']['sharpe']
    ok = (dl >= f6.DS_MIN or (dq >= 1 and dl >= 0)) and dc >= -f6.DS_COMMON_MAX_DROP
    out['deltas'] = {'d_sharpe_long': dl, 'd_q_pos_long': dq, 'd_sharpe_common': dc,
                     'd_cagr_long': L['P1_J1']['cagr'] - L['P1']['cagr'],
                     'd_max_dd_long': L['P1_J1']['max_dd'] - L['P1']['max_dd'],
                     'd_cagr_common': Cm['P1_J1']['cagr'] - Cm['P1']['cagr'],
                     'd_max_dd_common': Cm['P1_J1']['max_dd'] - Cm['P1']['max_dd']}
    out['pass'] = bool(ok)
    out['fits'] = [f for f in fits if f['month'] <= CUT[:7]]
    # Full curves (through 2025) are kept for the sealed F4 look; nothing is measured on them here.
    np.save(os.path.join(OUT, 'j1_components.npy'), comps_save, allow_pickle=True)
    path = os.path.join(OUT, 'j1.json')
    with open(path, 'w') as fh:
        json.dump(out, fh, indent=2, default=float)
    print(json.dumps({k: out[k] for k in ('first_state_day', 'risk_share_by_year', 'risk_share_total', 'switches',
                                          'deltas', 'pass')}, indent=1, default=float))
    for w in out['windows']:
        for p in ('P1', 'P1_J1'):
            m = out['windows'][w][p]
            print(w, p, m['from'], m['to'], {k: m[k] for k in ('cagr', 'max_dd', 'sharpe', 'q_pos_count', 'n_quarters')})
    print(path)


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
