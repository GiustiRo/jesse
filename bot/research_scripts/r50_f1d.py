"""r50 F1d: closed agenda (T1-T4, K1, X1, V1, P1, P2), exit gates, PBO over all r50 baskets.

Fixed in `strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r50/PHASE1D_PROTOCOL.md`
(commit 579fe3ee), written before this file. Engines from F1-F1c are imported unchanged; the
new ones are defined here. Exploration uses only the 7-asset core up to 2025-12-31.

    python research_scripts/r50_f1d.py run

writes research_scripts/data/r50/f1d_screen.json.
"""
import itertools
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
from r50_harness import T, O, C, H, L, DAY_MS, Account, DonchianEnsR49
from r50_engines import (ASSETS, COMMON, MEASURE_FROM, TAKER, TARGET_VOL, MAX_X, BAND, BALANCE, SLIP_BPS,
                         FUNDING, logret, ann_vol, rebalance, simulate, calendar, metrics, daily_returns)

N_DECLARED = 90
CORE, CRYPTO, CFD = fb.CORE, fc.CRYPTO, fc.CFD
SPLIT = '2018-01-01'          # halves of the long window (protocol section 3)
K1_SPLIT = '2023-01-01'       # K1 halves: 2020-22 / 2023-25
SPOT_FEE, PERP_FEE = 0.00075, 0.00045
UNIVERSE = {'M1': en.M1_BASKET, 'M2a': en.M2_BASKET, 'M2b': en.M2_BASKET, 'M3': CORE, 'R1': CORE,
            'R2': CORE, 'R3': CORE, 'R4': CORE, 'N1': CORE, 'N2': CORE, 'N3': CORE, 'C2': CORE,
            'C3': ['SPX', 'XAU'], 'C4': CFD, 'C5': CORE, 'C1': CRYPTO, 'C6': CRYPTO,
            'T1': CORE, 'T2': CORE, 'T3': CORE}
NEW_SLEEVES = ['T1', 'T2', 'T3', 'K1', 'X1', 'V1']


def _date(t):
    return datetime.fromtimestamp(t / 1000, tz=timezone.utc).date().isoformat()


# ----------------------------------------------------------------------------------------------
# New engines
# ----------------------------------------------------------------------------------------------
def parkinson_vol(bars, n, ann_days):
    """Parkinson range estimator: sqrt(mean(ln(H/L)^2) / (4 ln 2)), annualized."""
    x = np.log(bars[:, H] / bars[:, L]) ** 2
    out = np.full(len(bars), np.nan)
    c = np.cumsum(np.r_[0.0, x])
    out[n - 1:] = np.sqrt((c[n:] - c[:-n]) / n / (4 * math.log(2))) * math.sqrt(ann_days)
    return out


def t1_decider(bars, cfd, range_vol):
    c = bars[:, C]
    sd60 = en.rolling_std(logret(c), 60)
    vol = parkinson_vol(bars, 30, 252 if cfd else 365) if range_vol else ann_vol(c, cfd)
    band = 0.10 if range_vol else BAND
    sig = np.zeros(len(c))
    for n in (21, 63, 252):
        rn = np.r_[np.full(n, np.nan), np.log(c[n:] / c[:-n])]
        sig += np.nan_to_num(np.clip(rn / (sd60 * math.sqrt(n)), -2, 2) / 2) / 3
    sig = np.maximum(sig, 0)

    def decide(i, acct, ts):
        if i < 252 or not np.isfinite(vol[i]) or vol[i] <= 0:
            return
        target = acct.equity(c[i]) * min(MAX_X, sig[i] * TARGET_VOL / vol[i]) / c[i] if sig[i] > 0 else 0.0
        cur = acct.qty
        if target <= 0 or not acct.is_open or abs(target) > abs(cur) * (1 + band) or abs(target) < abs(cur) * (1 - band):
            if target <= 0:
                if acct.is_open:
                    fb._trade(acct, -cur, c[i], ts, TAKER)
            else:
                fb._trade(acct, target - cur, c[i], ts, TAKER)
    return decide


class DonchianEnsPark(DonchianEnsR49):
    """T3: R1 with the realized-vol input replaced by the Parkinson estimator on the same bars."""

    def _target(self, allc, i, acct):
        self._update(allc, i)
        if not self.states:
            return 0.0
        frac = sum(self.states) / len(self.states)
        if frac <= 0:
            return 0.0
        s = self._series(allc, i)[-self.vol_window:]
        if len(s) < 10:
            return 0.0
        rv = math.sqrt(float(np.mean(np.log(s[:, H] / s[:, L]) ** 2)) / (4 * math.log(2))) * self.ann
        if not math.isfinite(rv) or rv <= 0:
            return 0.0
        price = allc[i, C]
        return max(acct.equity(price) * min(self.MAX_NOTIONAL_X, frac * self.TARGET_VOL / rv) / price, 0.0)


def t3_run(name, d):
    h4 = d['h4']
    k = int(np.searchsorted(h4[:, T], d['start_ms'], side='left'))
    acct = fb.SlipAccount(BALANCE, TAKER, 3, SLIP_BPS.get(name, 0.0))
    fund = hz.load_funding(FUNDING[name]) if d['funding'] and name in FUNDING else None
    ts, eq = hz.run(DonchianEnsPark(**fb.R1_CFG[name]), h4[max(0, k - 1520):k], h4[k:], fb.H4_MS, acct, fund)
    return ts, eq, acct


def k1_carry(sym, frm):
    """Long spot / short perp funding harvest for one coin (protocol K1). Returns (days, vals)."""
    to = COMMON[1]
    perp = en.load_daily('Binance Perpetual Futures', f'{sym}-USDT', frm, to, False, warmup_days=60)
    spot = en.load_daily('Binance Spot', f'{sym}-USDT', frm, to, False, warmup_days=60)
    eff, mark, rate = hz.load_funding(FUNDING[sym])
    common = np.intersect1d(perp[:, T], spot[:, T])
    p = perp[np.isin(perp[:, T], common)][:, C]
    s = spot[np.isin(spot[:, T], common)][:, C]
    days = common.astype(np.int64)
    k0 = int(np.searchsorted(days, hz._ms(frm)))
    # Funding per UTC day (sum of settlements) and its trailing 21-day annualized mean.
    dd = (eff // DAY_MS) * DAY_MS
    per_day = {}
    for t, r in zip(dd, rate):
        per_day[int(t)] = per_day.get(int(t), 0.0) + r
    fday = np.array([per_day.get(int(t), 0.0) for t in days])
    trail = np.array([fday[max(0, i - 20):i + 1].mean() * 365 for i in range(len(days))])
    eq, q, vals, trades, open_eq = BALANCE, 0.0, [], [], None
    for i in range(k0, len(days)):
        if q > 0:
            eq += q * (s[i] - s[i - 1]) - q * (p[i] - p[i - 1]) + q * p[i] * fday[i]
        if q == 0 and trail[i] > 0.10:
            q = 0.75 * eq / p[i]
            eq -= q * (s[i] * SPOT_FEE + p[i] * PERP_FEE)
            open_eq = eq
        elif q > 0 and trail[i] < 0:
            eq -= q * (s[i] * SPOT_FEE + p[i] * PERP_FEE)
            trades.append(eq - open_eq)
            q = 0.0
        vals.append(eq)
    if q > 0:
        trades.append(eq - open_eq)
    ts = days[k0:] + DAY_MS
    return calendar(ts, np.array(vals), _date(hz._ms(frm)), to), trades


def xsec(data, mfrom, rule):
    """X1 (top-3 by 12-1 month return) and V1 (bottom-3 by 36-month return), monthly, shared book."""
    names = [n for n in data if data[n] is not None]
    to = COMMON[1]
    start = max(hz._ms(mfrom), min(int(data[n]['daily'][0, T]) for n in names))
    days = np.arange(start, hz._ms(to), DAY_MS)
    px, vols, rets, nbars = {}, {}, {}, {}
    for n in names:
        b = data[n]['daily']
        idx = np.searchsorted(b[:, T].astype(np.int64) + DAY_MS, days + DAY_MS, side='right') - 1
        px[n] = np.where(idx >= 0, b[np.clip(idx, 0, None), C], np.nan)
        rets[n] = np.r_[0.0, np.nan_to_num(px[n][1:] / px[n][:-1] - 1)]
        v = ann_vol(b[:, C], data[n]['cfd'])
        vols[n] = np.where(idx >= 0, v[np.clip(idx, 0, None)], np.nan)
        nbars[n] = idx
    fund_daily = {}
    for n in names:
        if data[n]['funding'] and n in FUNDING:
            eff, _, rate = hz.load_funding(FUNDING[n])
            s = {}
            for t, r in zip((eff // DAY_MS) * DAY_MS, rate):
                s[int(t)] = s.get(int(t), 0.0) + r
            fund_daily[n] = np.array([s.get(int(t), 0.0) for t in days])
    months = [_date(int(t))[:7] for t in days]
    w = {n: 0.0 for n in names}
    v_, vals, entries = BALANCE, [], 0
    for k in range(len(days)):
        if k > 0:
            v_ *= 1 + sum(w[n] * rets[n][k] for n in names) - sum(w[n] * fund_daily[n][k] for n in fund_daily)
        if k + 1 < len(days) and months[k + 1] != months[k]:
            scores = []
            for n in names:
                if rule == 'x1' and k >= 395 and np.isfinite(px[n][k - 395]) and np.isfinite(px[n][k - 30]):
                    scores.append((px[n][k - 30] / px[n][k - 395] - 1, n))
                elif rule == 'v1' and k >= 1095 and np.isfinite(px[n][k - 1095]):
                    scores.append((px[n][k] / px[n][k - 1095] - 1, n))
            ranked = sorted(scores, reverse=(rule == 'x1'))[:3]
            sel = [n for _, n in ranked if np.isfinite(vols[n][k]) and vols[n][k] > 0]
            new = {n: (min(MAX_X, TARGET_VOL / vols[n][k]) / 3 if n in sel else 0.0) for n in names}
            for n in names:
                dw = abs(new[n] - w[n])
                if dw > 0:
                    v_ *= 1 - dw * (TAKER + SLIP_BPS.get(n, 0.0) / 1e4)
                if new[n] > 0 and w[n] == 0:
                    entries += 1
            w = new
        vals.append(v_)
    return (days, np.array(vals)), entries


# ----------------------------------------------------------------------------------------------
# Sleeves for all r50 families (for PBO) and the new ones
# ----------------------------------------------------------------------------------------------
def sleeves(window):
    curves, trades, data = {}, {}, {}
    for name in CORE:
        if ASSETS[name][window] is None:
            continue
        d = fb.load_both(name, window)
        data[name] = d
        if d is None:
            continue
        cfd, frm = d['cfd'], _date(d['start_ms'])
        runs = {'R1': lambda: fb.r1_run(name, d), 'T3': lambda: t3_run(name, d),
                'R2': lambda: simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], False), name, d['funding'], fb.H4_MS),
                'R3': lambda: simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], True), name, d['funding'], fb.H4_MS),
                'C5': lambda: simulate(d['h4'], d['start_ms'], fc.c5_decider(d['h4'], d['daily'], cfd), name, d['funding'], fb.H4_MS),
                'M3': lambda: simulate(d['daily'], d['start_ms'], en.m3_decider(d['daily'], cfd, True), name, d['funding']),
                'R4': lambda: simulate(d['daily'], d['start_ms'], fb.r4_decider(d['daily']), name, d['funding']),
                'N1': lambda: simulate(d['daily'], d['start_ms'], fb.n1_decider(d['daily'], cfd), name, d['funding']),
                'N2': lambda: simulate(d['daily'], d['start_ms'], fb.n2_decider(d['daily']), name, d['funding']),
                'N3': lambda: simulate(d['daily'], d['start_ms'], fb.n3_decider(d['daily'], cfd), name, d['funding']),
                'C2': lambda: simulate(d['daily'], d['start_ms'], fc.monthly_decider(d['daily'], cfd, 'c2'), name, d['funding']),
                'T1': lambda: simulate(d['daily'], d['start_ms'], t1_decider(d['daily'], cfd, False), name, d['funding']),
                'T2': lambda: simulate(d['daily'], d['start_ms'], t1_decider(d['daily'], cfd, True), name, d['funding'])}
        if ASSETS[name]['m1']:
            runs['M1'] = lambda: simulate(d['daily'], d['start_ms'], en.m1_decider(d['daily'], cfd, ASSETS[name]['m1']), name, d['funding'])
        if name in en.M2_BASKET:
            runs['M2a'] = lambda: simulate(d['daily'], d['start_ms'], en.m2_decider(d['daily'], cfd, 'a'), name, d['funding'])
            runs['M2b'] = lambda: simulate(d['daily'], d['start_ms'], en.m2_decider(d['daily'], cfd, 'b'), name, d['funding'])
        if name in ('SPX', 'XAU'):
            runs['C3'] = lambda: simulate(d['daily'], d['start_ms'], fc.monthly_decider(d['daily'], cfd, 'c3'), name, d['funding'])
        if name in CFD:
            runs['C4'] = lambda: simulate(d['daily'], d['start_ms'], fb.r2_r3_decider(d['daily'], False, None), name, d['funding'])
        if name in CRYPTO:
            runs['C1'] = lambda: simulate(d['daily'], d['start_ms'], fc.c1_decider(d['daily'], cfd), name, d['funding'])
        last = d['daily'][-1, C]
        for s, fn in runs.items():
            ts, eq, acct = fn()
            curves[(s, name)] = calendar(ts, eq, frm, COMMON[1])
            tr = acct.trades + ([{'closed': int(ts[-1]), 'pnl': acct.upnl(last)}] if acct.is_open else [])
            trades[(s, name)] = [t['pnl'] for t in tr]
        if name in CRYPTO:
            curves[('C6', name)] = fc.mean_curve([curves[('R2', name)], curves[('R3', name)]])
            trades[('C6', name)] = trades[('R2', name)] + trades[('R3', name)]
        hz.jh.debug(f'{window} {name}: {len(runs)} sleeves')
    return curves, trades, data


def basket_of(curves, fam):
    keys = [(fam, n) for n in UNIVERSE[fam] if (fam, n) in curves]
    return fb.basket(curves, keys) if keys else None


def measure(cv, mfrom, trades=None, split=SPLIT):
    m = metrics(cv[0], cv[1], [], mfrom)
    if m is None:
        return None
    if trades:
        tot = sum(trades)
        m['top5_share'] = sum(sorted(trades, reverse=True)[:5]) / tot if tot > 0 else None
        m['trades'] = len(trades)
    half = {}
    for tag, lo, hi in (('h1', mfrom, split), ('h2', split, COMMON[1])):
        d0, d1 = hz._ms(lo), hz._ms(hi)
        sel = (cv[0] >= d0) & (cv[0] < d1)
        if sel.sum() > 60:
            v = cv[1][sel]
            r = np.diff(v) / v[:-1]
            half[tag] = float(r.mean() / r.std(ddof=1) * math.sqrt(365)) if r.std(ddof=1) > 0 else 0.0
    m['halves'] = half
    return m


# ----------------------------------------------------------------------------------------------
# PBO (CSCV, Bailey et al.)
# ----------------------------------------------------------------------------------------------
def pbo(matrix, s=16):
    t, n = matrix.shape
    blocks = np.array_split(np.arange(t), s)
    lam = []
    for combo in itertools.combinations(range(s), s // 2):
        is_idx = np.concatenate([blocks[j] for j in combo])
        os_idx = np.concatenate([blocks[j] for j in range(s) if j not in combo])
        def sr(x):
            sd = x.std(axis=0, ddof=1)
            return np.where(sd > 0, x.mean(axis=0) / sd, 0.0)
        is_sr, os_sr = sr(matrix[is_idx]), sr(matrix[os_idx])
        best = int(np.argmax(is_sr))
        rank = (os_sr < os_sr[best]).sum() + 0.5 * ((os_sr == os_sr[best]).sum() - 1)
        w = (rank + 1) / (n + 1)
        lam.append(math.log(w / (1 - w)))
    lam = np.array(lam)
    return float((lam <= 0).mean()), len(lam)


# ----------------------------------------------------------------------------------------------
# Portfolio with optional correlation factor (T4)
# ----------------------------------------------------------------------------------------------
def portfolio_cf(comp, names, use_cf):
    series = [daily_returns(*comp[n]) for n in names]
    days = sorted(set.intersection(*[set(s) for s in series]))
    R = np.array([[s[d] for s in series] for d in days])
    months = [_date(d)[:7] for d in days]
    w, k, cf_hist = None, None, []
    rets, used_from = [], None
    for t in range(len(days)):
        if w is not None:
            rets.append(k * float(w @ R[t]))
            used_from = used_from or days[t]
        if t + 1 < len(days) and months[t + 1] != months[t] and t + 1 >= f2.MIN_DAYS:
            hist = R[:t + 1]
            sd = hist.std(axis=0, ddof=1)
            if (sd > 0).all():
                w = (1 / sd) / (1 / sd).sum()
                cov = np.atleast_2d(np.cov(hist, rowvar=False))
                sp = math.sqrt(float(w @ cov @ w)) * math.sqrt(365)
                k = min(f2.K_MAX, f2.TARGET / sp) if sp > 0 else f2.K_MAX
                if use_cf and len(names) > 1:
                    cm = np.corrcoef(hist[-60:], rowvar=False)
                    rho = float((cm.sum() - len(names)) / (len(names) * (len(names) - 1)))
                    cf = math.sqrt(len(names) / (1 + (len(names) - 1) * rho))
                    cf_hist.append(cf)
                    k = min(f2.K_MAX, k * float(np.clip(cf / np.median(cf_hist), 0.5, 1.5)))
    vals = BALANCE * np.r_[1.0, np.cumprod(1 + np.array(rets))]
    return np.array([used_from - DAY_MS] + [d for d in days if d >= used_from]), vals


def port_eval(comps, names, trades, use_cf=False):
    out = {}
    for w in ('common', 'long'):
        days, vals = portfolio_cf(comps[w], names, use_cf)
        out[w] = f2.r9(days, vals, sum((trades[w].get(n, []) for n in names), []))
        out[w]['gates_r50'] = {k: out[w]['gates'][k] for k in ('cagr_ge_30', 'dd_le_20', 'pf_ge_1_2', 'median_month_pos',
                                                               'positive_without_best2', 'dsr_ge_0_95')}
        out[w]['pass_r50'] = all(out[w]['gates_r50'].values())
    return out


def run():
    f2.N_DECLARED = N_DECLARED  # portfolio DSR uses the F1d trial count (protocol section 6)
    res = {'protocol': 'RESEARCH_HUB/revisions/20261024-r50/PHASE1D_PROTOCOL.md', 'n_declared': N_DECLARED,
           'sleeves': {}, 'pbo': {}, 'portfolio': {}}
    comps, comp_tr = {}, {}
    long_baskets = {}
    for window in ('common', 'long'):
        curves, trades, data = sleeves(window)
        mfrom = MEASURE_FROM if window == 'common' else min(d['mfrom'] for d in data.values() if d)
        comps[window], comp_tr[window] = {}, {}
        for fam in UNIVERSE:
            bk = basket_of(curves, fam)
            if bk is None:
                continue
            tr = sum((trades[(fam, n)] for n in UNIVERSE[fam] if (fam, n) in trades), [])
            if fam in ('T1', 'T2', 'T3', 'R1', 'C6'):
                res['sleeves'].setdefault(fam, {})[window] = measure(bk, mfrom, tr)
            comps[window][fam] = bk
            comp_tr[window][fam] = tr
            if window == 'long':
                long_baskets[fam] = bk
        for rule in ('x1', 'v1'):
            cv, entries = xsec(data, mfrom, rule)
            key = rule.upper()
            m = measure(cv, mfrom)
            m['entries'] = entries
            res['sleeves'].setdefault(key, {})[window] = m
            comps[window][key], comp_tr[window][key] = cv, []
            if window == 'long':
                long_baskets[key] = cv
        # K1: 2020+ only (perpetual funding history); same curve for both lenses.
        k_frm = '2020-10-15' if window == 'common' else '2020-01-15'
        k_curves = [k1_carry(sym, k_frm) for sym in CRYPTO]
        kb = fb.basket({sym: kc[0] for sym, kc in zip(CRYPTO, k_curves)}, list(CRYPTO))
        k_tr = sum((kc[1] for kc in k_curves), [])
        res['sleeves'].setdefault('K1', {})[window] = measure(kb, MEASURE_FROM if window == 'common' else '2020-02-15',
                                                             k_tr, split=K1_SPLIT)
        comps[window]['K1'], comp_tr[window]['K1'] = kb, k_tr
        hz.jh.debug(f'{window}: sleeves done ' + json.dumps({k: round(v[window]['sharpe'], 2) for k, v in res['sleeves'].items()
                                                              if window in v and v[window]}))
    # Exit gates (protocol section 3).
    gates = {}
    r1_long = res['sleeves']['R1']['long']['sharpe']
    for s in NEW_SLEEVES:
        c, l = res['sleeves'][s]['common'], res['sleeves'][s]['long']
        g = {'sharpe_long_ge_0_5': bool(l['sharpe'] >= 0.5), 'sharpe_common_ge_0_5': bool(c['sharpe'] >= 0.5),
             'both_halves_pos': bool(len(l['halves']) == 2 and all(v > 0 for v in l['halves'].values())),
             'top5_lt_60': None if l.get('top5_share') is None else bool(l['top5_share'] < 0.6)}
        if s == 'T3':
            g['beats_r1_long'] = bool(l['sharpe'] > r1_long)
        g['pass'] = bool(all(v for k, v in g.items() if v is not None))
        gates[s] = g
    res['gates'] = gates
    # PBO over every multi-asset basket with a full long window.
    cols = [k for k, v in long_baskets.items() if k not in ('C1', 'C6')]
    ser = [daily_returns(*long_baskets[k]) for k in cols]
    days = sorted(set.intersection(*[set(s) for s in ser]))
    mat = np.array([[s[d] for s in ser] for d in days])
    p, ncomb = pbo(mat)
    cm = np.corrcoef(mat, rowvar=False)
    rho = float((cm.sum() - len(cols)) / (len(cols) * (len(cols) - 1)))
    res['pbo'] = {'columns': cols, 'from': _date(days[0]), 'to': _date(days[-1]), 'pbo': p, 'combinations': ncomb,
                  'mean_corr': rho, 'n_eff_estimate_registry': rho + (1 - rho) * N_DECLARED,
                  'proceed': bool(p < 0.3)}
    # Portfolios: P1 = R1 + C6; P2 greedy with passing sleeves ordered by long Sharpe; T4 on the final.
    p1 = ['R1', 'C6']
    res['portfolio']['P1'] = port_eval(comps, p1, comp_tr)
    chosen, base = list(p1), res['portfolio']['P1']
    log = []
    for s in sorted([s for s in NEW_SLEEVES if gates[s]['pass']], key=lambda s: -res['sleeves'][s]['long']['sharpe']):
        trial = port_eval(comps, chosen + [s], comp_tr)
        improves = (trial['common']['sharpe'] > base['common']['sharpe']
                    or trial['common']['quarters_pos'] > base['common']['quarters_pos'])
        vetoed = trial['long']['sharpe'] < 0 or trial['long']['max_dd'] < -0.25
        log.append({'add': s, 'improves': bool(improves), 'long_veto': bool(vetoed),
                    'sharpe_with': trial['common']['sharpe'], 'sharpe_without': base['common']['sharpe']})
        if improves and not vetoed:
            chosen.append(s)
            base = trial
    res['portfolio']['P2'] = {'components': chosen, 'log': log, 'eval': base}
    t4 = port_eval(comps, chosen, comp_tr, use_cf=True)
    t4_better = t4['long']['sharpe'] > base['long']['sharpe'] and t4['long']['max_dd'] >= base['long']['max_dd']
    res['portfolio']['T4'] = {'eval': t4, 'applied': bool(t4_better)}
    final = t4 if t4_better else base
    res['portfolio']['final'] = {'components': chosen, 'corr_cap': bool(t4_better), 'eval': final,
                                 'pass': bool(final['common']['pass_r50'] and final['long']['pass_r50'])}
    os.makedirs(hz.OUT_DIR, exist_ok=True)
    with open(os.path.join(hz.OUT_DIR, 'f1d_screen.json'), 'w') as fh:
        json.dump(res, fh, indent=2, default=float)
    hz.jh.debug(json.dumps({'gates': gates, 'pbo': res['pbo']['pbo'], 'final': {
        'components': chosen, 'corr_cap': bool(t4_better),
        **{w: {k: final[w][k] for k in ('cagr', 'max_dd', 'sharpe', 'months_pos', 'quarters_pos', 'dsr', 'pass_r50')}
           for w in ('common', 'long')}}}, default=float, indent=1))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        run()
    else:
        print(__doc__)


if __name__ == '__main__':
    sys.exit(main())
