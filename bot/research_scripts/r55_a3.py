"""r55 F3: A3 v2, the r51 Brent-WTI spread with a structural-break veto (N 132 -> 133).

PROTOCOL_R55.md F3. The A3 rule of PROTOCOL_R51.md is unchanged (z60 of x = ln Brent - ln WTI,
entry at |z| > 2, exit at the zero cross, 20 days or |z| > 4, size by the 30-day vol of dx, taker
on both legs). The veto: a new entry is allowed only if an OLS AR(1), dx_t = a + b x_{t-1} + e_t
over the 252 trading days up to the decision close, gives t(b) <= -2 and a half-life
-ln 2 / ln(1 + b) in (0, 60] days. Open positions exit by their normal rules.

Gates (r51 F6 diversifier, unchanged), every series cut at 2024-12-31 and the input bars trimmed
there, so no 2025 data enters: g1 decision-lens Sharpe >= 0.3; g2 PnL > 0 over the WTI bear
windows; g3 no long-lens veto (Sharpe < 0 or DD worse than 1.5x the decision DD); g4 daily rho with
P1 (long window) <= 0.2; g5 >= 30 trades and top-5 < 60% of the PnL. The rule was chosen knowing
A3's history, so the long lens is no longer an independent test (declared in the protocol).

    python research_scripts/r55_a3.py run

writes research_scripts/data/r55/f3_a3.json.
"""
import json
import math
import os
import sys

import numpy as np

import r50_engines as en
import r51_lib as lib
import r51_sleeves as sv
import r51_explore as ex
import r55_regimes as rg
from r50_harness import T, C, DAY_MS
from r50_engines import calendar, daily_returns, _trade

AR_DAYS = 252
T_MAX = -2.0
HALF_LIFE_MAX = 60.0
END = '2025-01-01'   # calendar end (exclusive): last day 2024-12-31


def trim(bars):
    return bars[bars[:, T] <= rg.CUT_MS]


def break_ok(x):
    """allow[i]: AR(1) on the AR_DAYS days up to i says the spread mean-reverts (t <= -2, 0 < HL <= 60)."""
    dx = np.r_[np.nan, np.diff(x)]
    allow = np.zeros(len(x), dtype=bool)
    hl_out = np.full(len(x), np.nan)
    for i in range(AR_DAYS, len(x)):
        y, xl = dx[i - AR_DAYS + 1:i + 1], x[i - AR_DAYS:i]
        ok = np.isfinite(y) & np.isfinite(xl)
        if ok.sum() < AR_DAYS * 0.9:
            continue
        X = np.column_stack([np.ones(ok.sum()), xl[ok]])
        beta, *_ = np.linalg.lstsq(X, y[ok], rcond=None)
        resid = y[ok] - X @ beta
        s2 = resid @ resid / (ok.sum() - 2)
        se = math.sqrt(s2 * np.linalg.inv(X.T @ X)[1, 1])
        b = beta[1]
        if se <= 0 or not (-1 < b < 0):
            continue
        hl = -math.log(2) / math.log(1 + b)
        hl_out[i] = hl
        allow[i] = b / se <= T_MAX and 0 < hl <= HALF_LIFE_MAX
    return allow, hl_out


def a3_pair_v2(brent, wti, start_ms, veto=True):
    """sv.a3_pair (r51) with the entry also requiring the break check; veto=False is r51's A3."""
    common = np.intersect1d(brent[:, T], wti[:, T])
    b = brent[np.isin(brent[:, T], common)]
    w = wti[np.isin(wti[:, T], common)]
    x = np.log(b[:, C]) - np.log(w[:, C])
    mu = sv.sma(x, 60)
    sd = en.rolling_std(x, 60)
    z = (x - mu) / sd
    dx_vol = en.rolling_std(np.r_[np.nan, np.diff(x)], 30) * math.sqrt(252)
    allow, hl = break_ok(x) if veto else (np.ones(len(x), dtype=bool), None)
    ab, aw = en.Account(en.BALANCE / 2, sv.TAKER, en.LEVERAGE), en.Account(en.BALANCE / 2, sv.TAKER, en.LEVERAGE)
    st = {'side': 0, 'held': 0}
    ts_out, eq_out, trades, blocked = [], [], [], 0
    k0 = int(np.searchsorted(b[:, T], start_ms, side='left'))
    for i in range(k0, len(b)):
        ts = int(b[i, T]) + DAY_MS
        pb, pw = b[i, C], w[i, C]
        eq = ab.equity(pb) + aw.equity(pw)
        gap = i + 1 < len(b) and b[i + 1, T] - b[i, T] > sv.MAX_GAP_DAYS * DAY_MS
        if st['side'] != 0:
            st['held'] += 1
            crossed = np.isfinite(z[i]) and np.sign(z[i]) != np.sign(st['z0'])
            if crossed or gap or st['held'] >= 20 or (np.isfinite(z[i]) and abs(z[i]) > 4):
                _trade(ab, -ab.qty, pb, ts, sv.TAKER)
                _trade(aw, -aw.qty, pw, ts, sv.TAKER)
                trades.append({'closed': ts, 'pnl': ab.balance + aw.balance - st['bal0']})
                st.update(side=0, held=0)
        elif not gap and i >= 60 and np.isfinite(z[i]) and abs(z[i]) > 2 and np.isfinite(dx_vol[i]) and dx_vol[i] > 0:
            if not allow[i]:
                blocked += 1
            else:
                notional = eq * min(1.0, sv.TARGET_VOL / dx_vol[i])
                side = -1 if z[i] > 2 else 1   # +1 = long Brent / short WTI
                st.update(side=side, held=0, z0=z[i], bal0=ab.balance + aw.balance)
                _trade(ab, side * notional / pb, pb, ts, sv.TAKER)
                _trade(aw, -side * notional / pw, pw, ts, sv.TAKER)
        ts_out.append(ts)
        eq_out.append(ab.equity(pb) + aw.equity(pw))
    info = {'blocked_signals': blocked, 'allow_share': float(allow[k0:].mean()) if len(allow) > k0 else None}
    if hl is not None:
        days = b[k0:, T]
        years = np.array([lib._date(d)[:4] for d in days])
        info['allow_share_by_year'] = {y: float(allow[k0:][years == y].mean()) for y in np.unique(years)}
    return np.array(ts_out, dtype=np.int64), np.array(eq_out), trades, info


def sleeve(lens, veto=True):
    brent = trim(sv.daily('BRENT', 'brent'))
    wti = trim(sv.daily('WTI', 'cfd'))
    start = ex.sim_start('WTI', lens, wti)
    ts, eq, trades, info = a3_pair_v2(brent, wti, start, veto)
    assert ts[-1] <= rg.CUT_MS + DAY_MS
    return calendar(ts, eq, lib._date(start), END), trades, start, info


def run():
    os.makedirs(rg.OUT, exist_ok=True)
    res = {'protocol': 'RESEARCH_HUB/revisions/20261026-r55/PROTOCOL_R55.md F3', 'n_declared': 133,
           'measured_through': rg.CUT, 'checks': {}, 'lenses': {}}
    # Reproduction: veto off equals r51's A3 decision curve through 2024-12-31.
    r51c = np.load(os.path.join(lib.OUT, 'explore_A_curves.npy'), allow_pickle=True).item()['A3']['dec']
    off, _, _, _ = sleeve('dec', veto=False)
    k = r51c[0] <= rg.CUT_MS
    res['checks']['veto_off_equals_r51'] = bool(len(off[0]) == k.sum() and np.allclose(off[1], r51c[1][k]))
    assert res['checks']['veto_off_equals_r51'], 'A3 not reproduced'

    curves, trades, starts = {}, {}, {}
    for lens in ('dec', 'c21', 'veto'):
        for tag, veto in (('v2', True), ('r51', False)):
            cv, tr, start, info = sleeve(lens, veto)
            m = en.metrics(cv[0], cv[1], tr, lib._date(start))
            res['lenses'].setdefault(lens, {})[tag] = {**{kk: m[kk] for kk in ('from', 'to', 'cagr', 'max_dd', 'sharpe',
                                                                                 'quarters_pos', 'trades', 'top5_share', 'by_year')
                                                          if kk in m}, **info}
            if tag == 'v2':
                curves[lens], trades[lens], starts[lens] = cv, tr, start
    dec, veto_l = res['lenses']['dec']['v2'], res['lenses']['veto']['v2']
    bear = ex.window_pnl(curves['dec'], ex.BEAR['WTI'], starts['dec'])
    p1r = {d: v for d, v in ex.p1_long_returns().items() if d <= rg.CUT_MS}
    br = daily_returns(*curves['dec'])
    days = sorted(set(br) & set(p1r))
    rho = float(np.corrcoef([br[d] for d in days], [p1r[d] for d in days])[0, 1])
    g = {'g1_sharpe_ge_0_3': dec['sharpe'] >= 0.3, 'g2_bear_pnl_pos': bear > 0,
         'g3_no_veto': not (veto_l['sharpe'] < 0 or veto_l['max_dd'] < 1.5 * dec['max_dd']),
         'g4_rho_le_0_2': rho <= 0.2,
         'g5_trades_top5': dec['trades'] >= 30 and dec['top5_share'] is not None and dec['top5_share'] < 0.6}
    res.update({'bear_pnl_dec': bear, 'rho_p1': rho, 'gates': {kk: bool(v) for kk, v in g.items()},
                'pass': bool(all(g.values()))})
    path = os.path.join(rg.OUT, 'f3_a3.json')
    with open(path, 'w') as fh:
        json.dump(res, fh, indent=2, default=float)
    print('checks', res['checks'])
    for lens, d in res['lenses'].items():
        for tag, m in d.items():
            print(lens, tag, m['from'], m['to'], f"S {m['sharpe']:.2f} CAGR {m['cagr']:.3f} DD {m['max_dd']:.3f} "
                  f"Q+ {m['quarters_pos']:.2f} trades {m['trades']} top5 {m.get('top5_share')} blocked {m.get('blocked_signals')}")
    print('v2 veto lens by year', {y: round(r, 3) for y, r in veto_l.get('by_year', {}).items()})
    print('allow by year', {y: round(r, 2) for y, r in veto_l.get('allow_share_by_year', {}).items()})
    print('bear', round(bear, 4), 'rho', round(rho, 3), res['gates'], 'PASS' if res['pass'] else 'no')
    print(path)


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
