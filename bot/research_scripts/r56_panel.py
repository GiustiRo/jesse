"""r56 F0: daily panel of the U50 perpetuals, regime labels, baselines and the coin holdout.

r56 treats regime detection as probabilistic state forecasting, judged without PnL (plan approved
by the user on 2026-10-26). This script builds everything the detectors are scored against and is
committed, with its output, before any detector is fitted.

Data: data/r52/<SYM>_1h.npy (t, o, h, l, c, v, qv, tbv) from r52_download.py. Hard cut at
2024-12-31 23:59 UTC: 2025 stays sealed, so no bar, label window or feature reaches past it.

Daily bars are UTC days built from 1h klines; a day needs >= 20 hourly bars, otherwise it is NaN.
RV_d = sum of squared 1h log returns inside the day (the first one against the previous hour's
close). ATR20 = simple 20-day mean of the daily true range.

Labels at the close of day t, horizon H = 20 days (window t+1..t+H, known at the close of t+H):
* Y_vol (3 classes, level): q = share of the coin's past 20-day RV sums (windows closed in the
  365 days up to t, at least 180) below RV(t+1..t+H); 0 compression if q <= 1/3, 2 high vol if
  q >= 2/3, 1 otherwise. Amendment F0-1 (2026-10-26, before any detector): the plan's ratio label
  ln(RV(t+1..t+H) / RV(t-H+1..t)) shares RV(t-H+1..t) with its own persistence baseline, which
  makes persistence anti-correlated by construction (dev balanced accuracy 0.23, below the 0.33 of
  chance) and turns "compression" into "vol will fall" rather than "vol is low". The ratio label is
  kept as y_volchg (thresholds +-a), reported and never decisive;
* Y_trend (2 classes): Kaufman efficiency of the window |c[t+H] - c[t]| / sum |c[i] - c[i-1]|;
  1 trend if >= e, 0 otherwise. Its direction is a reported sub-label that never decides;
* Y_range (2 classes): 1 if every high of t+1..t+H <= c[t] + k*ATR20[t] and every low
  >= c[t] - k*ATR20[t], 0 otherwise.
Sensitivities at H = 10 and 40 are stored and reported, never decisive.

Threshold rule, fixed here before any statistic is printed: each threshold is the grid point whose
pooled class share (development coins, eligible days, label windows closing by 2023-12-31) is
closest to its target. Y_vol uses fixed terciles and needs no grid. a (y_volchg only) in ln{1.15, 1.20, 1.25, 1.33, 1.50}, target 30% for each tail (mean of
the two tails); e in {0.25, 0.30, 0.35, 0.40, 0.45}, target 35% trend; k in {2.0, 2.5, 3.0, 3.5,
4.0}, target 40% range. The grids are centred on the plan's proposals (a = ln 1.25, e = 0.35,
k = 2.5), and the targets keep every class between 20% and 60%.

Baselines (no N_regime cost):
* persistence: the same label computed on the last closed window t-H+1..t (for Y_range the box is
  anchored at c[t-H] and ATR20[t-H]), known at t;
* climatology: class frequency of the coin's own labels known at t (windows closed by t) over the
  previous 365 days, with at least 60 known labels.

Eligibility (as r52): >= 90 days since the coin's first bar, 30-day median quote volume >= 10M
USDT, and a valid close.

Coin holdout: the 48 alts sorted by onboarding date form 16 consecutive triplets; one coin of each
triplet is drawn with numpy default_rng(56). That gives 16 holdout coins stratified by listing age.
BTC and ETH stay in development. The holdout is not touched until r56 F5.

    python research_scripts/r56_panel.py run

writes data/r56/panel.npz, labels.npz, holdout.json and f0_labels.json.
"""
import json
import math
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'data', 'r52')
OUT = os.path.join(HERE, 'data', 'r56')
FIRST_DAY, CUT = '2020-01-01', '2024-12-31'
CUT_MS = int(pd.Timestamp(CUT, tz='UTC').value // 10**6) + 86_400_000 - 1
DEV_LABEL_END = '2023-12-31'
H = 20
H_SENS = (10, 40)
MIN_HOURS = 20
ATR_N = 20
MIN_DAYS_LISTED = 90
MIN_MEDIAN_QVOL = 10e6
CLIM_DAYS, CLIM_MIN = 365, 60
VOL_DIST_DAYS, VOL_DIST_MIN = 365, 180
HOLDOUT_SEED = 56
GRID_A = tuple(math.log(x) for x in (1.15, 1.20, 1.25, 1.33, 1.50))
GRID_E = (0.25, 0.30, 0.35, 0.40, 0.45)
GRID_K = (2.0, 2.5, 3.0, 3.5, 4.0)
TARGET_TAIL, TARGET_TREND, TARGET_RANGE = 0.30, 0.35, 0.40
AXES = {'vol': 3, 'trend': 2, 'range': 2}
REPORTED = {'volchg': 3}  # reported, never decisive


# ----------------------------------------------------------------------------------------------
# Panel
# ----------------------------------------------------------------------------------------------
def universe():
    return json.load(open(os.path.join(SRC, 'universe50.json')))


def load_panel():
    """Daily (days x coins) arrays: O, H, L, C, RV, QV, ATR and the eligibility mask."""
    uni = universe()
    syms = [u['symbol'] for u in uni]
    days = pd.date_range(FIRST_DAY, CUT, freq='D', tz='UTC')
    fields = {f: {} for f in ('o', 'h', 'l', 'c', 'rv', 'qv')}
    for s in syms:
        a = np.load(os.path.join(SRC, f'{s}_1h.npy'))
        a = a[a[:, 0] <= CUT_MS]
        df = pd.DataFrame(a[:, :7], columns=['t', 'o', 'h', 'l', 'c', 'v', 'qv'])
        df['lr2'] = np.log(df['c']).diff() ** 2
        df['day'] = pd.to_datetime(df['t'], unit='ms', utc=True).dt.floor('D')
        g = df.groupby('day')
        ok = g.size() >= MIN_HOURS
        agg = pd.DataFrame({'o': g['o'].first(), 'h': g['h'].max(), 'l': g['l'].min(), 'c': g['c'].last(),
                            'rv': g['lr2'].sum(min_count=MIN_HOURS - 1), 'qv': g['qv'].sum()})
        agg[~ok] = np.nan
        for f in fields:
            fields[f][s] = agg[f]
    P = {f: pd.DataFrame(v).reindex(days).reindex(columns=syms).values.astype(float) for f, v in fields.items()}
    C = P['c']
    prev = np.vstack([np.full((1, C.shape[1]), np.nan), C[:-1]])
    tr = np.fmax(P['h'] - P['l'], np.fmax(np.abs(P['h'] - prev), np.abs(P['l'] - prev)))
    P['atr'] = pd.DataFrame(tr).rolling(ATR_N, min_periods=ATR_N).mean().values
    first = np.array([np.argmax(~np.isnan(C[:, j])) for j in range(C.shape[1])])
    age = np.arange(len(days))[:, None] - first[None, :]
    med_qv = pd.DataFrame(P['qv']).rolling(30, min_periods=20).median().values
    P['elig'] = (age >= MIN_DAYS_LISTED) & (med_qv >= MIN_MEDIAN_QVOL) & ~np.isnan(C) & ~np.isnan(P['atr'])
    day_ms = (days.asi8 // 10**6).astype(np.int64)
    assert day_ms[-1] <= CUT_MS and len(days) == C.shape[0], 'panel goes past the 2024 cut'
    return day_ms, syms, P


# ----------------------------------------------------------------------------------------------
# Labels
# ----------------------------------------------------------------------------------------------
def _roll_sum(x, n):
    """Sum over the trailing n rows (row t covers t-n+1..t); NaN if any value is missing."""
    cs = np.vstack([np.zeros((1, x.shape[1])), np.cumsum(np.nan_to_num(x), axis=0)])
    bad = np.vstack([np.zeros((1, x.shape[1])), np.cumsum(np.isnan(x), axis=0)])
    out = np.full(x.shape, np.nan)
    out[n - 1:] = cs[n:] - cs[:-n]
    nb = np.full(x.shape, 1.0)
    nb[n - 1:] = bad[n:] - bad[:-n]
    out[nb > 0] = np.nan
    return out


def _roll_ext(x, n, fn):
    return pd.DataFrame(x).rolling(n, min_periods=n).agg(fn).values


def _shift(x, k):
    """Row t of the result is row t+k of x (k > 0 looks ahead, k < 0 back); NaN outside."""
    out = np.full(x.shape, np.nan)
    if k > 0:
        out[:-k] = x[k:]
    elif k < 0:
        out[-k:] = x[:k]
    else:
        out[:] = x
    return out


def vol_level(rv, h):
    """Share of past window sums known at t (rv rows t-364..t) below the current and the next window."""
    from numpy.lib.stride_tricks import sliding_window_view
    n, m = rv.shape
    q_past, q_fut = np.full(rv.shape, np.nan), np.full(rv.shape, np.nan)
    fut = _shift(rv, h)
    w = VOL_DIST_DAYS
    for j in range(m):
        x = rv[:, j]
        win = sliding_window_view(x, w)  # row i covers x[i..i+w-1], i.e. it ends at t = i+w-1
        cnt = (~np.isnan(win)).sum(axis=1)
        ok = cnt >= VOL_DIST_MIN
        t = np.arange(w - 1, n)
        for target, out in ((x[t], q_past), (fut[t, j], q_fut)):
            below = (win < target[:, None]).sum(axis=1) / np.where(ok, cnt, np.nan)
            out[t, j] = np.where(ok & ~np.isnan(target), below, np.nan)
    return q_past, q_fut


def raw_scores(P, h):
    """Past-window scores at t (window t-h+1..t) and future-window scores at t (t+1..t+h)."""
    np.seterr(divide='ignore', invalid='ignore')
    C, Hh, Ll, RV, A = P['c'], P['h'], P['l'], P['rv'], P['atr']
    rv_past = _roll_sum(RV, h)
    z_past = np.log(rv_past / _shift(rv_past, -h))
    z_fut = np.log(_shift(rv_past, h) / rv_past)
    steps = _roll_sum(np.abs(C - _shift(C, -1)), h)
    net_past = C - _shift(C, -h)
    er_past = np.abs(net_past) / steps
    er_fut = np.abs(_shift(net_past, h)) / _shift(steps, h)
    dir_fut = np.sign(_shift(net_past, h))
    hi_past, lo_past = _roll_ext(Hh, h, 'max'), _roll_ext(Ll, h, 'min')
    # Box half-width in ATR units: how far the window strayed from the anchor close.
    dev_past = np.fmax(hi_past - _shift(C, -h), _shift(C, -h) - lo_past) / _shift(A, -h)
    dev_fut = np.fmax(_shift(hi_past, h) - C, C - _shift(lo_past, h)) / A
    q_past, q_fut = vol_level(rv_past, h)
    out = {'q_past': q_past, 'q_fut': q_fut, 'z_past': z_past, 'z_fut': z_fut, 'er_past': er_past, 'er_fut': er_fut, 'dir_fut': dir_fut,
            'dev_past': dev_past, 'dev_fut': dev_fut}
    # Zero-RV windows (exchange outages) and empty windows give inf/NaN; treat them as unknown.
    return {kk: np.where(np.isfinite(v), v, np.nan) for kk, v in out.items()}


def classify(S, a, e, k, which):
    q, z, er, dev = S[f'q_{which}'], S[f'z_{which}'], S[f'er_{which}'], S[f'dev_{which}']
    y_vol = np.where(np.isnan(q), np.nan, np.where(q <= 1 / 3, 0, np.where(q >= 2 / 3, 2, 1)))
    y_volchg = np.where(np.isnan(z), np.nan, np.where(z <= -a, 0, np.where(z >= a, 2, 1)))
    y_trend = np.where(np.isnan(er), np.nan, (er >= e).astype(float))
    y_range = np.where(np.isnan(dev), np.nan, (dev <= k).astype(float))
    return {'vol': y_vol, 'trend': y_trend, 'range': y_range, 'volchg': y_volchg}


def climatology(y, n_cls, day_ms, h):
    """Per coin, class frequencies of labels already known at t over the previous CLIM_DAYS days."""
    known = _shift(y, -h)  # label of day t-h, whose window closed at t
    out = np.full(y.shape + (n_cls,), np.nan)
    for c in range(n_cls):
        hit = np.where(np.isnan(known), np.nan, (known == c).astype(float))
        num = pd.DataFrame(hit).rolling(CLIM_DAYS, min_periods=CLIM_MIN).sum().values
        den = pd.DataFrame(~np.isnan(known)).rolling(CLIM_DAYS, min_periods=CLIM_MIN).sum().values
        out[..., c] = num / np.where(den >= CLIM_MIN, den, np.nan)
    return out


# ----------------------------------------------------------------------------------------------
# Holdout and scoring helpers (scoring lives in r56_eval.py; only baselines are scored here)
# ----------------------------------------------------------------------------------------------
def draw_holdout(uni):
    alts = sorted([u for u in uni if u['symbol'] not in ('BTCUSDT', 'ETHUSDT')], key=lambda u: u['onboard'])
    assert len(alts) == 48
    rng = np.random.default_rng(HOLDOUT_SEED)
    picks = [alts[3 * i + int(rng.integers(3))]['symbol'] for i in range(16)]
    return sorted(picks)


def onehot(y, n_cls):
    out = np.full(y.shape + (n_cls,), np.nan)
    ok = ~np.isnan(y)
    out[ok] = np.eye(n_cls)[y[ok].astype(int)]
    return out


def brier(p, y, n_cls):
    return np.nansum((p - onehot(y, n_cls)) ** 2, axis=-1)


def balanced_accuracy(pred, y, n_cls):
    recalls = [float((pred[y == c] == c).mean()) for c in range(n_cls) if (y == c).any()]
    return float(np.mean(recalls))


def switches_per_year(y, mask):
    """Mean over coins of label changes per 365 eligible days."""
    out = []
    for j in range(y.shape[1]):
        v = y[mask[:, j], j]
        v = v[~np.isnan(v)]
        if len(v) > 60:
            out.append(float((np.diff(v) != 0).sum() / len(v) * 365))
    return float(np.mean(out))


# ----------------------------------------------------------------------------------------------
# Run
# ----------------------------------------------------------------------------------------------
def nearest(grid, share_fn, target):
    shares = [share_fn(g) for g in grid]
    i = int(np.argmin([abs(s - target) for s in shares]))
    return grid[i], dict(zip([round(g, 4) for g in grid], [round(s, 4) for s in shares]))


def run():
    os.makedirs(OUT, exist_ok=True)
    day_ms, syms, P = load_panel()
    uni = universe()
    hold = draw_holdout(uni)
    dev_cols = np.array([s not in hold for s in syms])
    dates = pd.to_datetime(day_ms, unit='ms', utc=True)
    label_end_ms = int(pd.Timestamp(DEV_LABEL_END, tz='UTC').value // 10**6)
    # Development descriptive mask: dev coins, eligible, label window closed by 2023-12-31.
    dev_rows = (day_ms + H * 86_400_000) <= label_end_ms
    M = P['elig'] & dev_cols[None, :] & dev_rows[:, None]

    S = raw_scores(P, H)
    vf = M & ~np.isnan(S['z_fut'])
    a, sh_a = nearest(GRID_A, lambda g: 0.5 * ((S['z_fut'][vf] <= -g).mean() + (S['z_fut'][vf] >= g).mean()),
                      TARGET_TAIL)
    tf = M & ~np.isnan(S['er_fut'])
    e, sh_e = nearest(GRID_E, lambda g: (S['er_fut'][tf] >= g).mean(), TARGET_TREND)
    rf = M & ~np.isnan(S['dev_fut'])
    k, sh_k = nearest(GRID_K, lambda g: (S['dev_fut'][rf] <= g).mean(), TARGET_RANGE)

    Y = classify(S, a, e, k, 'fut')
    Yp = classify(S, a, e, k, 'past')
    labels = {f'y_{ax}': Y[ax] for ax in {**AXES, **REPORTED}}
    labels.update({f'persist_{ax}': Yp[ax] for ax in {**AXES, **REPORTED}})
    labels['trend_dir'] = S['dir_fut']
    report = {'thresholds': {'a': a, 'a_ratio': math.exp(a), 'e': e, 'k': k, 'H': H},
              'grid_shares': {'a': sh_a, 'e': sh_e, 'k': sh_k}, 'holdout': hold,
              'n_dev_coins': int(dev_cols.sum()), 'axes': {}}
    for ax, n in {**AXES, **REPORTED}.items():
        y, yp = Y[ax], Yp[ax]
        clim = climatology(y, n, day_ms, H)
        labels[f'clim_{ax}'] = clim
        m = M & ~np.isnan(y)
        mb = m & ~np.isnan(yp) & ~np.isnan(clim).any(axis=-1)
        pers_p = onehot(yp, n)
        share = {str(c): round(float((y[m] == c).mean()), 4) for c in range(n)}
        report['axes'][ax] = {
            'n_obs': int(m.sum()), 'class_share': share,
            'label_switches_per_year': round(switches_per_year(y, m), 2),
            'n_obs_baselines': int(mb.sum()),
            'persistence': {'balanced_accuracy': round(balanced_accuracy(yp[mb], y[mb], n), 4),
                            'brier': round(float(brier(pers_p, y, n)[mb].mean()), 4),
                            'switches_per_year': round(switches_per_year(yp, mb), 2)},
            'climatology': {'balanced_accuracy': round(balanced_accuracy(clim[mb].argmax(axis=-1).astype(float), y[mb], n), 4),
                            'brier': round(float(brier(clim, y, n)[mb].mean()), 4)},
            'by_year_share': {str(yr): {str(c): round(float((y[m & np.asarray(dates.year == yr)[:, None]] == c).mean()), 4)
                                        for c in range(n)} for yr in range(2020, 2024)
                              if (m & np.asarray(dates.year == yr)[:, None]).any()},
        }
        tr = m & (y == 1) if ax == 'trend' else None
        if tr is not None:
            report['axes'][ax]['up_share_of_trend'] = round(float((S['dir_fut'][tr] > 0).mean()), 4)
    # Sensitivities H = 10 and 40 with the same thresholds: class shares only.
    sens = {}
    for h in H_SENS:
        Sh = raw_scores(P, h)
        Yh = classify(Sh, a, e, k, 'fut')
        Mh = P['elig'] & dev_cols[None, :] & ((day_ms + h * 86_400_000) <= label_end_ms)[:, None]
        sens[h] = {}
        for ax, n in AXES.items():
            mm = Mh & ~np.isnan(Yh[ax])
            sens[h][ax] = {str(c): round(float((Yh[ax][mm] == c).mean()), 4) for c in range(n)}
            labels[f'y_{ax}_h{h}'] = Yh[ax]
    report['sensitivity_class_share'] = sens
    # 2025 guard: every label window must close by the cut.
    for ax in AXES:
        last = np.where(~np.isnan(Y[ax]).any(axis=1))[0].max()
        assert day_ms[last] + H * 86_400_000 <= CUT_MS, 'a label window passes the 2024 cut'
    np.savez_compressed(os.path.join(OUT, 'panel.npz'), day_ms=day_ms, syms=np.array(syms),
                        **{f: P[f] for f in ('o', 'h', 'l', 'c', 'rv', 'qv', 'atr', 'elig')})
    np.savez_compressed(os.path.join(OUT, 'labels.npz'), **labels)
    json.dump({'seed': HOLDOUT_SEED, 'holdout': hold, 'development': [s for s in syms if s not in hold]},
              open(os.path.join(OUT, 'holdout.json'), 'w'), indent=2)
    json.dump(report, open(os.path.join(OUT, 'f0_labels.json'), 'w'), indent=2)
    print(json.dumps(report, indent=2))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        run()
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
