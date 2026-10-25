"""r50 F1e: realistic funding carry (K1r), its audit and stresses, and the P3 portfolio.

Fixed in `strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r50/PHASE1E_PROTOCOL.md`
(commit 0dcebff3), written before this file.

    python research_scripts/r50_f1e.py run

writes research_scripts/data/r50/f1e_screen.json.
"""
import json
import math
import os
import sys
from datetime import datetime, timezone

import numpy as np
import jesse.models  # noqa: F401 - must load before candle_service (circular import otherwise)

import r50_harness as hz
import r50_engines as en
import r50_f1b as fb
import r50_f1c as fc
import r50_f2 as f2
from r50_harness import T, H, C, DAY_MS
from r50_engines import COMMON, ASSETS, FUNDING, BALANCE, simulate, calendar, daily_returns

N_DECLARED = 92
SPOT_FEE, PERP_FEE, SLIP = 0.0010, 0.00045, 0.0002   # protocol section 1
LEG_FRACTION = 1 / 1.5          # 2x isolated perp: spot paid in full + 1/2 notional margin
REHEDGE_MOVE = 0.40             # forced re-hedge when the perp high is 40% above the short entry
OPEN_ANN, CLOSE_ANN = 0.10, 0.0
K1R_K_CAP = 1.5
K1R_FROM, K1R_SPLIT = '2020-02-15', '2023-01-01'


def _date(t):
    return datetime.fromtimestamp(t / 1000, tz=timezone.utc).date().isoformat()


def k1r(sym, frm, fund_mult=1.0):
    to = COMMON[1]
    perp = en.load_daily('Binance Perpetual Futures', f'{sym}-USDT', frm, to, False, warmup_days=60)
    spot = en.load_daily('Binance Spot', f'{sym}-USDT', frm, to, False, warmup_days=60)
    eff, mark, rate = hz.load_funding(FUNDING[sym])
    rate = rate * fund_mult
    common = np.intersect1d(perp[:, T], spot[:, T])
    P = perp[np.isin(perp[:, T], common)]
    S = spot[np.isin(spot[:, T], common)]
    days = common.astype(np.int64)
    k0 = int(np.searchsorted(days, hz._ms(frm)))
    eday = (eff // DAY_MS) * DAY_MS
    rate_day, cash_day = {}, {}
    for t, r, mk in zip(eday, rate, mark):
        rate_day[int(t)] = rate_day.get(int(t), 0.0) + r
        cash_day[int(t)] = cash_day.get(int(t), 0.0) + r * mk   # per unit of short qty
    fday = np.array([rate_day.get(int(t), 0.0) for t in days])
    cday = np.array([cash_day.get(int(t), 0.0) for t in days])
    trail = np.array([fday[max(0, i - 20):i + 1].mean() * 365 for i in range(len(days))])
    p, s, ph = P[:, C], S[:, C], P[:, H]
    eq, q, entry = BALANCE, 0.0, 0.0
    vals, trades, open_eq = [], [], None
    funding_total, fees_total, rehedges, in_pos = 0.0, 0.0, 0, 0
    audit_rows = []

    def cost(qty, i):
        return qty * (s[i] * (SPOT_FEE + SLIP) + p[i] * (PERP_FEE + SLIP))

    for i in range(k0, len(days)):
        if q > 0:
            fc_ = q * cday[i]
            eq += q * (s[i] - s[i - 1]) - q * (p[i] - p[i - 1]) + fc_
            funding_total += fc_
            audit_rows.append((i, q))
            in_pos += 1
            if ph[i] >= entry * (1 + REHEDGE_MOVE):
                c_ = 2 * cost(q, i)
                eq -= c_
                fees_total += c_
                q = eq * LEG_FRACTION / p[i]
                entry = p[i]
                rehedges += 1
        if q == 0 and trail[i] > OPEN_ANN:
            q = eq * LEG_FRACTION / p[i]
            c_ = cost(q, i)
            eq -= c_
            fees_total += c_
            entry, open_eq = p[i], eq
        elif q > 0 and trail[i] < CLOSE_ANN:
            c_ = cost(q, i)
            eq -= c_
            fees_total += c_
            trades.append(eq - open_eq)
            q = 0.0
        vals.append(eq)
    if q > 0:
        trades.append(eq - open_eq)
    # Audit: funding recomputed directly from the raw events of the held days.
    held = {int(days[i]): qq for i, qq in audit_rows}
    direct = sum(held[int(t)] * r * mk for t, r, mk in zip(eday, rate, mark) if int(t) in held)
    ts = days[k0:] + DAY_MS
    curve = calendar(ts, np.array(vals), _date(hz._ms(frm)), to)
    return curve, trades, {'funding_total': funding_total, 'fees_total': fees_total, 'rehedges': rehedges,
                           'days_in_position': in_pos, 'days_total': len(days) - k0,
                           'audit_funding_direct': direct,
                           'audit_rel_diff': abs(direct - funding_total) / abs(direct) if direct else 0.0}


def carry_metrics(cv, frm):
    days, vals = cv
    m = en.metrics(days, vals, [], frm)
    dates = [_date(int(d)) for d in days]
    me = {}
    for d, v in zip(dates, vals):
        me[d[:7]] = v
    mv = [vals[0]] + list(me.values())
    mret = np.array(mv[1:]) / np.array(mv[:-1]) - 1
    m['months_pos'] = float((mret > 0).mean())
    r30 = vals[30:] / vals[:-30] - 1
    m['worst_30d'] = float(r30.min())
    half = {}
    for tag, lo, hi in (('h1', frm, K1R_SPLIT), ('h2', K1R_SPLIT, COMMON[1])):
        sel = (days >= hz._ms(lo)) & (days < hz._ms(hi))
        v = vals[sel]
        r = np.diff(v) / v[:-1]
        half[tag] = float(r.mean() / r.std(ddof=1) * math.sqrt(365)) if len(r) > 30 and r.std(ddof=1) > 0 else 0.0
    m['halves'] = half
    y = {}
    for d, v in zip(dates, vals):
        y[d[:4]] = v
    yv = [vals[0]] + list(y.values())
    m['by_year'] = dict(zip(y, (np.array(yv[1:]) / np.array(yv[:-1]) - 1).round(4).tolist()))
    return m


def k1r_basket(frm, fund_mult=1.0):
    out = {sym: k1r(sym, frm, fund_mult) for sym in fc.CRYPTO}
    bk = fb.basket({sym: o[0] for sym, o in out.items()}, list(out))
    return bk, sum((o[1] for o in out.values()), []), {sym: o[2] for sym, o in out.items()}


def trend_components(window):
    """R1 basket (7 assets) and C6 basket (BTC, ETH R2+R3), same code as F1b/F1c/F2."""
    curves, trades = {}, {}
    for name in fb.CORE:
        if ASSETS[name][window] is None:
            continue
        d = fb.load_both(name, window)
        if d is None:
            continue
        frm = _date(d['start_ms'])
        runs = {'R1': lambda: fb.r1_run(name, d)}
        if name in fc.CRYPTO:
            runs['R2'] = lambda: simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], False), name, d['funding'], fb.H4_MS)
            runs['R3'] = lambda: simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], True), name, d['funding'], fb.H4_MS)
        last = d['daily'][-1, C]
        for s, fn in runs.items():
            ts, eq, acct = fn()
            curves[(s, name)] = calendar(ts, eq, frm, COMMON[1])
            tr = acct.trades + ([{'closed': int(ts[-1]), 'pnl': acct.upnl(last)}] if acct.is_open else [])
            trades[(s, name)] = [t['pnl'] for t in tr]
    r1 = fb.basket(curves, [k for k in curves if k[0] == 'R1'])
    c6 = fb.basket({n: fc.mean_curve([curves[('R2', n)], curves[('R3', n)]]) for n in fc.CRYPTO},
                   list(fc.CRYPTO))
    return {'R1': r1, 'C6': c6}, {'R1': sum((v for k, v in trades.items() if k[0] == 'R1'), []),
                                  'C6': sum((v for k, v in trades.items() if k[0] in ('R2', 'R3')), [])}


def portfolio_kcap(comp, names, capped='K1r'):
    """F2 construction, with the multiplier applied to the carry sleeve capped at 1.5."""
    series = [daily_returns(*comp[n]) for n in names]
    days = sorted(set.intersection(*[set(s) for s in series]))
    R = np.array([[s[d] for s in series] for d in days])
    months = [_date(d)[:7] for d in days]
    ci = names.index(capped) if capped in names else None
    w, k, rets, ks, used_from = None, None, [], [], None
    for t in range(len(days)):
        if w is not None:
            mult = np.full(len(names), k)
            if ci is not None:
                mult[ci] = min(k, K1R_K_CAP)
            rets.append(float((w * mult) @ R[t]))
            ks.append(k)
            used_from = used_from or days[t]
        if t + 1 < len(days) and months[t + 1] != months[t] and t + 1 >= f2.MIN_DAYS:
            hist = R[:t + 1]
            sd = hist.std(axis=0, ddof=1)
            if (sd > 0).all():
                w = (1 / sd) / (1 / sd).sum()
                cov = np.atleast_2d(np.cov(hist, rowvar=False))
                sp = math.sqrt(float(w @ cov @ w)) * math.sqrt(365)
                k = min(f2.K_MAX, f2.TARGET / sp) if sp > 0 else f2.K_MAX
    vals = BALANCE * np.r_[1.0, np.cumprod(1 + np.array(rets))]
    pdays = np.array([used_from - DAY_MS] + [d for d in days if d >= used_from])
    return pdays, vals, {'k_mean': float(np.mean(ks)), 'weights_last': dict(zip(names, w.tolist()))}


def run():
    f2.N_DECLARED = N_DECLARED
    res = {'protocol': 'RESEARCH_HUB/revisions/20261024-r50/PHASE1E_PROTOCOL.md', 'n_declared': N_DECLARED}
    bk, tr, stats = k1r_basket(K1R_FROM)
    m = carry_metrics(bk, K1R_FROM)
    bk_half, _, _ = k1r_basket(K1R_FROM, 0.5)
    m_half = carry_metrics(bk_half, K1R_FROM)
    gates = {'sharpe_ge_1': m['sharpe'] >= 1.0, 'months_pos_ge_70': m['months_pos'] >= 0.70,
             'dd_le_10': m['max_dd'] >= -0.10, 'both_halves_pos': all(v > 0 for v in m['halves'].values()),
             'funding_half_sharpe_ge_0_5': m_half['sharpe'] >= 0.5, 'worst_30d_ge_m5': m['worst_30d'] >= -0.05,
             'audit_ok': all(st['audit_rel_diff'] < 0.001 for st in stats.values())}
    gates = {k: bool(v) for k, v in gates.items()}
    gates['pass'] = all(gates.values())
    res['K1r'] = {'metrics': m, 'stress_funding_x0_5': {k: m_half[k] for k in ('sharpe', 'cagr', 'max_dd', 'months_pos')},
                  'stats': stats, 'gates': gates, 'trades': len(tr)}
    hz.jh.debug(json.dumps({'K1r': {k: m[k] for k in ('sharpe', 'cagr', 'max_dd', 'months_pos', 'worst_30d', 'halves', 'by_year')},
                            'half_funding': res['K1r']['stress_funding_x0_5'], 'stats': stats, 'gates': gates},
                           default=float, indent=1))
    # P3 portfolio, evaluated even if K1r fails (reported), passes only with K1r passing.
    out = {}
    for window in ('common', 'long'):
        comps, trs = trend_components(window)
        kb, ktr, _ = k1r_basket('2020-10-15' if window == 'common' else K1R_FROM)
        comps['K1r'] = kb
        trs['K1r'] = ktr
        days, vals, info = portfolio_kcap(comps, ['R1', 'C6', 'K1r'])
        r9 = f2.r9(days, vals, sum(trs.values(), []))
        r9.update(info)
        r9['gates_r50'] = {k: r9['gates'][k] for k in ('cagr_ge_30', 'dd_le_20', 'pf_ge_1_2', 'median_month_pos',
                                                       'positive_without_best2', 'dsr_ge_0_95')}
        r9['pass_r50'] = all(r9['gates_r50'].values())
        out[window] = r9
    res['P3'] = out
    res['pass'] = bool(gates['pass'] and out['common']['pass_r50'] and out['long']['pass_r50'])
    os.makedirs(hz.OUT_DIR, exist_ok=True)
    with open(os.path.join(hz.OUT_DIR, 'f1e_screen.json'), 'w') as fh:
        json.dump(res, fh, indent=2, default=float)
    hz.jh.debug(json.dumps({w: {k: out[w][k] for k in ('from', 'cagr', 'max_dd', 'sharpe', 'months_pos', 'quarters_pos',
                                                       'dsr', 'k_mean', 'weights_last', 'pass_r50')} for w in out},
                           default=float, indent=1))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        run()
    else:
        print(__doc__)


if __name__ == '__main__':
    sys.exit(main())
