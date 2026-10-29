"""r61: neutral asymmetry book, the deterministic limit of r60's construction K (PROTOCOL_R61.md).

Variants (§0): A = intraweek breakout continuation only; B = A + long all week in alts with 7-day
funding < 0 (r49 amended for this sleeve only). Both are beta-hedged with the BTC perp.
Development = the 48 U50 alts + BTC; H = N2 ∪ N3 is only read through r59_oracle (q3).

Research container (same deps as r60):
    python research_scripts/r61.py assert_limit   # §2.2: limit form == mean of K over random legs
    python research_scripts/r61.py overlap        # §2.3: BENCH_C6ALTS and overlap with C6 (descriptive)
    python research_scripts/r61.py q3_selftest    # §2.4: oracle mechanics of q3 on a fake holdout
    python research_scripts/r61.py placebo        # §3 p2': timing placebo + mechanical control
    python research_scripts/r61.py f1             # §3: gates p1, g1..g10 (+ p2' from placebo), series
    python research_scripts/r61.py q3_power       # §4: Lo (2002) power of the selected variant
    python research_scripts/r61.py f3             # §5: SPA/PBO over the C6-in-alts family + A/B
"""
import json
import math
import os
import sys

import numpy as np
import pandas as pd

import r60
from r60 import (COST, CUT, DEV_FROM, HEDGE, STOP_K, STOP_SLIP, U50_DIR, Book, FastBook, Panel, alts, bench,
                 combo_delta, gates_of, log, old20, rho, sharpe, window)

HERE = r60.HERE
OUT = os.path.join(HERE, 'data', 'r61')
SEED = 61
DAY = 86_400_000
HOUR = 3_600_000
N_LIMIT = 400                 # §2.2: random-leg K runs averaged against the limit form
LIMIT_RHO, LIMIT_MEAN_TOL = 0.95, 0.10
N_WEIGHT_DRAWS = 20000        # E1: leg-membership draws per formation for the exact expected weights
N_PLACEBO = 500               # §3 p2'
CAL_BOOKS, CAL_DRAWS = 100, 200
P2_ALPHA = 0.10
N_DSR = 11                    # §3 g10: 9 C6-in-alts trials of the registry + A + B
Q3_FROM = r60.Q2_FROM         # 2021-07-02, H's common window (r60 §4)
Q3_BOOT = 1000
VARIANTS = ('A', 'B')
C6_FAMILY = ['R54_W1', 'R54_M1', 'R55_F2_ML3', 'R55_F2_ML4', 'R57_Q1', 'R57_Q2', 'R58_F3_I1']


# ----------------------------------------------------------------------------------------------
# The book (§1)
# ----------------------------------------------------------------------------------------------
def trigger(P, sym, d0, d1):
    """r60.stop_path's trigger with its hour: first 1h close in (d0, d1] at or above C_d0 (1 + 2 sigma_w).
    Returns (hour open ms, close) or None."""
    entry = P.C.at[d0, sym]
    sig = P.feats['vol30'].at[d0, sym] * math.sqrt(7)
    if not (np.isfinite(entry) and np.isfinite(sig)) or sym not in P.hourly:
        return None
    t, c = P.hourly[sym]
    lo = np.searchsorted(t, d0.value // 10**6 + DAY)
    hi = np.searchsorted(t, d1.value // 10**6 + DAY)
    hit = np.flatnonzero(c[lo:hi] >= entry * (1 + STOP_K * sig))
    if not len(hit):
        return None
    j = lo + hit[0]
    return int(t[j]), float(c[j])


class AsymBook:
    """Weekly formations over every eligible leg row of the panel (no score). Per formation it keeps the
    week's daily closes/returns/funding, an hourly close grid of the legs and of BTC, sizes u, betas,
    the crowded flag and each leg's breakout trigger (hour index into the grid)."""

    def __init__(self, P, legs, hedge=HEDGE):
        ref = Book(P, legs, hedge)
        self.P, self.ref, self.legs, self.hedge = P, ref, list(legs), hedge
        coins = list(legs) + [hedge]
        self.coins, ci = coins, {s: i for i, s in enumerate(coins)}
        self.hi = ci[hedge]
        idx = P.C.index
        self.days = idx
        Cv = P.C.reindex(columns=coins).values
        R = np.nan_to_num(P.ret.reindex(columns=coins).values, nan=0.0)
        Fm = P.F.reindex(columns=coins).fillna(0.0).values
        bt, bc = P.hourly[hedge]
        self.forms = []
        for d0, g in ref.S.groupby('day', sort=True):
            n = len(g)
            if n < 5:
                continue
            d1, span = ref.span[d0]
            rows = idx.get_indexer(span)
            r0 = idx.get_loc(d0)
            L = len(rows)
            assert (np.diff(np.r_[r0, rows]) == 1).all(), 'daily index must be contiguous'
            t0 = d0.value // 10**6 + DAY
            grid = t0 + HOUR * np.arange(24 * L)
            syms = g['sym'].values
            ix = np.array([ci[s] for s in syms])
            vol = g['vol30_raw'].fillna(g['vol30_raw'].median()).clip(lower=1e-4).values
            inv = 1 / vol
            q = int(math.ceil(n / 5))
            u = 0.5 * inv / (q * inv.mean())                      # §1: typical size inside a K leg
            beta = np.array([P.feats['beta60'].at[d0, s] for s in syms])
            beta = np.where(np.isfinite(beta), beta, 1.0)
            crowded = P.fund7.loc[d0, syms].values < 0
            Hc = np.full((n, len(grid)), np.nan)
            for j, s in enumerate(syms):
                t, c = P.hourly[s]
                k = np.searchsorted(t, grid, side='right') - 1
                ok = (k >= 0) & (t[np.clip(k, 0, None)] >= t0 - HOUR * 24)   # ffill only within the week
                Hc[j, ok] = c[k[ok]]
            kb = np.searchsorted(bt, grid, side='right') - 1
            Hb = np.where(kb >= 0, bc[np.clip(kb, 0, None)], np.nan)
            trig = np.full(n, -1)
            for j, s in enumerate(syms):
                h = trigger(P, s, d0, d1)
                if h is not None:
                    trig[j] = (h[0] - t0) // HOUR
                    assert Hc[j, trig[j]] == h[1]
            self.forms.append({'d0': d0, 'rows': rows, 'L': L, 'sym': syms, 'ix': ix, 'u': u, 'inv': inv, 'beta': beta,
                               'crowded': crowded, 'trig': trig, 'q_over_n': q / n,
                               'Cw': Cv[np.r_[r0, rows]][:, ix].T,          # (n, L+1), column 0 = C_d0
                               'Rw': R[rows][:, ix].T, 'Fw': Fm[rows][:, ix].T,   # (n, L)
                               'Cb': Cv[np.r_[r0, rows], self.hi], 'Rb': R[rows, self.hi], 'Fb': Fm[rows, self.hi],
                               'Hc': Hc, 'Hb': Hb, 'hday': np.arange(24 * L) // 24})

    # -------------------------------------------------------------------------------------------
    @staticmethod
    def legs_of(f, variant):
        """(funding-leg rows, breakout-leg rows that triggered)."""
        fund = np.flatnonzero(f['crowded']) if variant == 'B' else np.array([], int)
        brk = np.flatnonzero(f['trig'] >= 0)
        if variant == 'B':
            brk = brk[~f['crowded'][brk]]
        return fund, brk

    @staticmethod
    def entry_paths(f, j, h, slip=STOP_SLIP):
        """Daily alt and BTC returns (…, L) of positions in rows j entered at grid hour h (broadcast
        arrays), plus the entry-day index; NaN entry prices give a zero path (no entry)."""
        L = f['L']
        e = f['hday'][h]
        p = f['Hc'][j, h] * (1 + slip)
        pb = f['Hb'][h]
        k = np.arange(L)
        Cn = f['Cw'][j][..., 1:]                                   # (…, L) close of each week day
        Rw = f['Rw'][j]
        ee = e[..., None]
        alt = np.where(k == ee, Cn / p[..., None] - 1, np.where(k > ee, Rw, 0.0))
        btc = np.where(k == ee, f['Cb'][1:][k] / pb[..., None] - 1, np.where(k > ee, f['Rb'][k], 0.0))
        live = k >= ee
        ok = np.isfinite(p) & np.isfinite(pb)
        alt = np.where(ok[..., None], np.nan_to_num(alt), 0.0)
        btc = np.where(ok[..., None], np.nan_to_num(btc), 0.0)
        return alt, btc, live & ok[..., None], e

    # -------------------------------------------------------------------------------------------
    def run(self, variant, cost_mult=1.0, hedge=True, legs=('fund', 'brk')):
        """Operable book (§1), exact engine: formation turnover nets against last week's end weights."""
        out_r, out_d = [], []
        prev = np.zeros(len(self.coins))
        for f in self.forms:
            fund, brk = self.legs_of(f, variant)
            fund = fund if 'fund' in legs else fund[:0]
            brk = brk if 'brk' in legs else brk[:0]
            L = f['L']
            w0 = np.zeros(len(self.coins))
            w0[f['ix'][fund]] += f['u'][fund]
            if hedge:
                w0[self.hi] -= float((f['u'][fund] * f['beta'][fund]).sum())
            r = np.zeros(L)
            r += f['Rw'][fund].T @ f['u'][fund] - f['Fw'][fund].T @ f['u'][fund]
            hb0 = w0[self.hi]
            r += hb0 * (f['Rb'] - f['Fb'])
            cost = np.zeros(L)
            cost[0] += np.abs(w0 - prev).sum() * COST * cost_mult
            end = w0.copy()
            if len(brk):
                alt, btc, live, e = self.entry_paths(f, brk, f['trig'][brk])
                u, b = f['u'][brk], f['beta'][brk]
                r += alt.T @ u - (f['Fw'][brk] * live).T @ u
                for i, j in enumerate(brk):
                    end[f['ix'][j]] += u[i]
                    cost[e[i]] += u[i] * COST * cost_mult
                if hedge:
                    hb = u * b
                    r -= btc.T @ hb - (f['Fb'][None, :] * live).T @ hb
                    end[self.hi] -= float(hb.sum())
                    for i in range(len(brk)):
                        cost[e[i]] += abs(hb[i]) * COST * cost_mult
            out_r.append(r - cost)
            out_d.append(self.days[f['rows']])
            prev = end
        return pd.Series(np.concatenate(out_r), index=pd.DatetimeIndex(np.concatenate(out_d)))

    def run_limit(self, variant):
        """§1 limit form, amended by E1: expected K weights over random legs, no COST, slip kept.
        Long leg: E[w_l,i] = 0.5 inv_i / sum_all inv on every coin, all week. Short leg: K renormalises
        the short leg over the non-crowded coins it keeps, so E[w_s,i] = 0.5 inv_i / sum_noncrowded inv
        on non-crowded coins (= E[w_l,i] when nothing is excluded, i.e. A), held until the 2 sigma stop
        (hit-day return hit_ret, funding received that day, flat after). Hedge fixed at d0 on both legs."""
        out_r, out_d = [], []
        rng = np.random.default_rng(SEED)
        for f in self.forms:
            inv, b, L = f['inv'], f['beta'], f['L']
            nc = ~f['crowded'] if variant == 'B' else np.ones(len(inv), bool)
            wl, ws = expected_weights(inv, nc, rng)
            R, F = f['Rw'], f['Fw']
            r = (R - F).T @ wl
            r += (-float((wl * b).sum()) + float((ws * b).sum())) * (f['Rb'] - f['Fb'])
            k = np.arange(L)
            for j in np.flatnonzero(nc):
                if f['trig'][j] < 0:
                    path = R[j] - F[j]
                else:
                    e = f['hday'][f['trig'][j]]
                    hit_ret = f['Hc'][j, f['trig'][j]] * (1 + STOP_SLIP) / f['Cw'][j, e] - 1
                    path = np.where(k < e, R[j] - F[j], np.where(k == e, hit_ret - F[j], 0.0))
                r = r - ws[j] * path
            out_r.append(r)
            out_d.append(self.days[f['rows']])
        return pd.Series(np.concatenate(out_r), index=pd.DatetimeIndex(np.concatenate(out_d)))

    # -------------------------------------------------------------------------------------------
    def week_draws(self, f, variant, rng, D, mode='coin_hour'):
        """Simplified engine (§3 p2'), D draws of one formation -> (D, L) daily returns. Entry and exit
        costs per position, no netting across weeks. mode: 'real' (D = 1, the book itself),
        'coin_hour' (random coins and hours) or 'hour' (the book's coins, random hours)."""
        fund, brk = self.legs_of(f, variant)
        n, L, H = len(f['sym']), f['L'], 24 * f['L']
        nf, nb = len(fund), len(brk)
        k = np.arange(L)
        if mode == 'real':
            F = np.broadcast_to(fund, (D, nf))
            Bj = np.broadcast_to(brk, (D, nb))
            Bh = np.broadcast_to(f['trig'][brk], (D, nb))
        else:
            if mode == 'coin_hour':
                perm = np.argsort(rng.random((D, n)), axis=1)
                F = perm[:, :nf] if variant == 'B' else np.zeros((D, 0), int)
                Bj = perm[:, nf:nf + nb]
            else:
                F = np.broadcast_to(fund, (D, nf))
                Bj = np.broadcast_to(brk, (D, nb))
            Bh = rng.integers(0, H, size=(D, nb))
        r = np.zeros((D, L))
        c_unit = COST * (1 + np.abs(f['beta']))                    # entry or exit of alt + its hedge
        if nf:
            u, b = f['u'][F], f['beta'][F]                          # (D, nf)
            r += np.einsum('dm,dmk->dk', u, f['Rw'][F] - f['Fw'][F])
            r -= np.einsum('dm,k->dk', u * b, f['Rb'] - f['Fb'])
            cu = (f['u'] * c_unit)[F].sum(1)
            r[:, 0] -= cu
            r[:, -1] -= cu
        if nb:
            alt, btc, live, e = self.entry_paths(f, Bj, Bh)          # (D, nb, L)
            u, b = f['u'][Bj], f['beta'][Bj]
            ok = live.any(-1)
            r += np.einsum('dm,dmk->dk', u, alt - f['Fw'][Bj] * live)
            r -= np.einsum('dm,dmk->dk', u * b, btc - f['Fb'][None, None, :] * live)
            cu = (f['u'] * c_unit)[Bj] * ok
            np.add.at(r, (np.repeat(np.arange(D), nb), e.ravel()), -cu.ravel())
            r[:, -1] -= cu.sum(1)
        return r

    def draws(self, variant, D, rng, mode='coin_hour', frm=DEV_FROM):
        """(D, days) matrix of the simplified engine over the formations, days from `frm` to CUT."""
        keep = [f for f in self.forms if self.days[f['rows'][-1]] >= pd.Timestamp(frm, tz='UTC')]
        M = np.concatenate([self.week_draws(f, variant, rng, D, mode) for f in keep], axis=1)
        d = pd.DatetimeIndex(np.concatenate([self.days[f['rows']] for f in keep]))
        m = (d >= pd.Timestamp(frm, tz='UTC')) & (d <= pd.Timestamp(CUT, tz='UTC'))
        return M[:, m], d[m]

    def n_entries(self, variant):
        return {str(f['d0'].date()): [int(len(x)) for x in self.legs_of(f, variant)] for f in self.forms}


def expected_weights(inv, nc, rng, D=N_WEIGHT_DRAWS):
    """E1: exact expected K weights over uniformly random legs, by sampling leg membership only (no
    returns). 1/sum is convex, so with few non-crowded coins left in a random short leg (2022: ~30 of
    45 crowded) the closed form 0.5 inv_i / sum_noncrowded inv understates the short weight."""
    n = len(inv)
    q = int(math.ceil(n / 5))
    perm = np.argsort(rng.random((D, n)), axis=1)
    top, bot = np.zeros((D, n), bool), np.zeros((D, n), bool)
    np.put_along_axis(top, perm[:, -q:], True, axis=1)
    np.put_along_axis(bot, perm[:, :q], True, axis=1)
    bot &= nc[None, :]

    def leg(m):
        x = m * inv[None, :]
        s = x.sum(1, keepdims=True)
        return (0.5 * np.divide(x, s, out=np.zeros_like(x), where=s > 0)).mean(0)
    return leg(top), leg(bot)


def sharpe_rows(M):
    sd = M.std(1, ddof=1)
    return np.where(sd > 0, M.mean(1) / np.where(sd > 0, sd, 1) * math.sqrt(365), 0.0)


def dev_book(legs=None):
    P = r60.dev_panel()
    return P, AsymBook(P, alts() if legs is None else legs)


# ----------------------------------------------------------------------------------------------
# §2.2 the limit assertion
# ----------------------------------------------------------------------------------------------
def assert_limit():
    os.makedirs(OUT, exist_ok=True)
    P, bk = dev_book()
    fb = FastBook(P, alts())
    # The trigger equals r60's stop on every (formation, coin) of the book (day and price).
    nchk = 0
    for f in bk.forms:
        for j, s in enumerate(f['sym']):
            h = bk.ref.stop(s, f['d0'])
            if f['trig'][j] < 0:
                assert h is None
            else:
                t = f['trig'][j]
                day = f['d0'] + pd.Timedelta(days=1 + int(f['hday'][t]))
                assert h is not None and h[0] == day and abs(h[1] - f['Hc'][j, t] * (1 + STOP_SLIP)) < 1e-9 * h[1]
                nchk += 1
    rng = np.random.default_rng(SEED)
    res = {'protocol': 'PROTOCOL_R61.md §2.2', 'n_runs': N_LIMIT, 'triggers_checked': nchk, 'variants': {}}
    for V, crowded in (('A', False), ('B', True)):
        acc = None
        for i in range(N_LIMIT):
            sc = pd.Series(rng.random(len(fb.S)), index=fb.S.index)
            r = fb.run(sc, cost_mult=0.0, crowded=crowded)
            acc = r if acc is None else acc + r.reindex(acc.index).fillna(0.0)
        meanK = window(acc / N_LIMIT)
        lim = window(bk.run_limit(V)).reindex(meanK.index).fillna(0.0)
        c = float(np.corrcoef(meanK.values, lim.values)[0, 1])
        dm = float((meanK - lim).mean() * 365)
        lm = float(lim.mean() * 365)
        ok = c >= LIMIT_RHO and abs(dm) <= LIMIT_MEAN_TOL * abs(lm)
        res['variants'][V] = {'corr': c, 'ann_mean_diff': dm, 'ann_mean_limit': lm, 'ann_mean_meanK': float(meanK.mean() * 365),
                              'sharpe_meanK': sharpe(meanK), 'sharpe_limit': sharpe(lim), 'pass': bool(ok)}
        log(f'{V} limit corr {c:.4f} mean diff {dm:.5f} vs {lm:.5f} pass {ok}')
    res['pass'] = all(v['pass'] for v in res['variants'].values())
    json.dump(res, open(os.path.join(OUT, 'f0_limit.json'), 'w'), indent=1)
    assert res['pass'], 'limit assertion failed: fix the code, not the bound (§2.2)'


# ----------------------------------------------------------------------------------------------
# §2.3 C6 basket and overlap
# ----------------------------------------------------------------------------------------------
def c6_basket(syms, src_of):
    """Frozen C6 (R2 + R3) per coin, data cut at 2024-12-31 (r58.c6_bank loop without a gate), and
    its equal-weight daily basket as a pd.Series of daily returns. Also returns the trades."""
    import r50_engines as en
    import r50_f1b as f1b
    import r50_f1c as fc
    import r54_v1 as v1
    import r58
    from r50_harness import T
    curves, events = {}, []
    v1_data = v1.DATA
    try:
        for sym in syms:
            src = src_of(sym)
            v1.DATA = src
            bars, _, h1 = r58.h4_bars(src, sym)
            start = max(r58.SIM_FROM, int(bars[min(v1.WARM_BARS, len(bars) - 1), T]))
            if start >= r58.CUT_MS:
                continue
            sleeves = []
            for retest in (False, True):
                dec = f1b.r2_r3_decider(bars, retest)
                ts, eq, acct = v1.simulate(bars, start, dec, v1.funding_cursor(sym, h1, int(bars[0, T])))
                sleeves.append(en.calendar(ts, eq, r58.pd_date(start), '2025-01-01'))
                events += [{'sym': sym, 'opened': int(t['opened']), 'closed': int(t['closed'])} for t in acct.trades]
            curves[sym] = fc.mean_curve(sleeves)
    finally:
        v1.DATA = v1_data
    d, v = f1b.basket(curves, list(curves))
    r = pd.Series(np.diff(v) / v[:-1], index=pd.to_datetime(d[1:], unit='ms', utc=True))
    return window(r, '2020-01-01'), events


def overlap():
    import r59
    P, bk = dev_book()
    c6, ev = c6_basket(alts(), lambda s: U50_DIR)
    ser = r59.save_series('r61', 'BENCH_C6ALTS', c6.index.asi8 // 10**6, c6.values, 'r61.py overlap', f'..{CUT}')
    r1, p55 = bench('BENCH_R1_common'), bench('BENCH_P55_common')
    ev = pd.DataFrame(ev)
    res = {'protocol': 'PROTOCOL_R61.md §2.3', 'c6_series': ser, 'c6_sharpe_D': sharpe(window(c6)), 'variants': {}}
    for V in VARIANTS:
        r = window(bk.run(V))
        hits, n = 0, 0
        for f in bk.forms:
            if f['d0'] < pd.Timestamp(DEV_FROM, tz='UTC'):
                continue
            _, brk = bk.legs_of(f, V)
            a = f['d0'].value // 10**6 + DAY
            b = a + f['L'] * DAY
            for j in brk:
                n += 1
                e = ev[ev['sym'] == f['sym'][j]]
                hits += bool(((e['opened'] < b) & (e['closed'] > a)).any())
        res['variants'][V] = {'rho_c6alts': rho(r, c6), 'rho_r1': rho(r, r1), 'rho_p55': rho(r, p55),
                              'breakouts': n, 'share_with_c6_trade_same_coin_week': hits / n if n else None}
        log(f"{V} " + json.dumps(res['variants'][V]))
    json.dump(res, open(os.path.join(OUT, 'f0_overlap.json'), 'w'), indent=1, default=float)


# ----------------------------------------------------------------------------------------------
# §3 p2' timing placebo and its mechanical control
# ----------------------------------------------------------------------------------------------
def placebo():
    P, bk = dev_book()
    rng = np.random.default_rng(SEED)
    res = {'protocol': "PROTOCOL_R61.md §3 p2'", 'n': N_PLACEBO, 'variants': {}}
    for V in VARIANTS:
        real, _ = bk.draws(V, 1, rng, 'real')
        obs = float(sharpe_rows(real)[0])
        null = sharpe_rows(bk.draws(V, N_PLACEBO, rng, 'coin_hour')[0])
        hour = sharpe_rows(bk.draws(V, N_PLACEBO, rng, 'hour')[0])
        p = float((1 + (null >= obs).sum()) / (N_PLACEBO + 1))
        ph = float((1 + (hour >= obs).sum()) / (N_PLACEBO + 1))
        # Mechanical control: CAL_BOOKS placebo books, each ranked against its own CAL_DRAWS draws.
        ps = []
        for i in range(CAL_BOOKS):
            sh = sharpe_rows(bk.draws(V, CAL_DRAWS + 1, rng, 'coin_hour')[0])
            ps.append((1 + (sh[1:] >= sh[0]).sum()) / (CAL_DRAWS + 1))
        frac = float(np.mean(np.array(ps) < P2_ALPHA))
        res['variants'][V] = {'obs_simplified': obs, 'p': p, 'null_mean': float(null.mean()),
                              'null_p95': float(np.percentile(null, 95)), 'hour_only_p': ph,
                              'hour_only_mean': float(hour.mean()), 'control_frac_p_lt_0_10': frac,
                              'control_ok': bool(0.03 <= frac <= 0.17), 'pass': bool(p < P2_ALPHA)}
        log(f"{V} " + json.dumps(res['variants'][V]))
    json.dump(res, open(os.path.join(OUT, 'f1_placebo.json'), 'w'), indent=1)


# ----------------------------------------------------------------------------------------------
# §3 F1
# ----------------------------------------------------------------------------------------------
def combo3_delta(r, r1, c6):
    """R1 + C6alts + sleeve (thirds of equal-vol series) minus R1 + C6alts (halves), common days."""
    j = pd.concat([r, r1, c6], axis=1, join='inner').dropna()
    a, b, c = (j.iloc[:, i] for i in range(3))
    three = (a / a.std() + b / b.std() + c / c.std()) / 3
    two = (b / b.std() + c / c.std()) / 2
    return sharpe(three) - sharpe(two), sharpe(three), sharpe(two)


def dsr_of(r, n):
    import r50_f1b as f1b
    return f1b.dsr(np.r_[1.0, np.cumprod(1 + r.values)], n)


def capacity(bk, V):
    med = bk.P.Q.rolling(30, min_periods=20).median()
    caps = []
    for f in bk.forms:
        if f['d0'] < pd.Timestamp(DEV_FROM, tz='UTC'):
            continue
        fund, brk = bk.legs_of(f, V)
        c = [0.01 * med.at[f['d0'], f['sym'][j]] / f['u'][j] for j in np.r_[fund, brk]
             if np.isfinite(med.at[f['d0'], f['sym'][j]])]
        if c:
            caps.append(min(c))
    return {'median_usdt': float(np.median(caps)), 'p10_usdt': float(np.percentile(caps, 10))}


def cv_folds(P, V):
    H = json.load(open(os.path.join(r60.OUT, 'cv_halves.json')))['halves']
    folds = []
    for h in ('0', '1'):
        r = AsymBook(P, H[h]).run(V)
        for y in ('2021', '2022', '2023', '2024'):
            ry = window(r, max(DEV_FROM, f'{y}-01-01'), f'{y}-12-31')
            folds.append({'half': h, 'year': y, 'sharpe': sharpe(ry), 'days': int(len(ry))})
    sh = [f['sharpe'] for f in folds]
    return {'folds': folds, 'median': float(np.median(sh)), 'n_pos': int(sum(x > 0 for x in sh)),
            'pass': bool(np.median(sh) > 0 and sum(x > 0 for x in sh) >= 5)}


def f1():
    import r59
    P, bk = dev_book()
    bk_old = AsymBook(P, old20(P))
    r1, p55 = bench('BENCH_R1_common'), bench('BENCH_P55_common')
    c6 = bench('BENCH_C6ALTS')
    pl = json.load(open(os.path.join(OUT, 'f1_placebo.json')))
    res = {'protocol': 'PROTOCOL_R61.md §3', 'window': [DEV_FROM, CUT], 'n_dsr': N_DSR, 'variants': {}}
    for V in VARIANTS:
        r = window(bk.run(V))
        r2 = window(bk.run(V, cost_mult=2.0))
        m, g = gates_of(r, r2, window(r, '2024-01-01'), window(bk_old.run(V)), r1, p55)
        d3, s3, s2 = combo3_delta(r, r1, c6)
        m.update({'combo3_delta_c6': d3, 'combo3_sharpe': s3, 'r1_c6_sharpe': s2, 'rho_c6alts': rho(r, c6),
                  'dsr': dsr_of(r, N_DSR), 'capacity': capacity(bk, V)})
        m['legs'] = {'breakout_only': sharpe(window(bk.run(V, legs=('brk',)))),
                     'funding_only': sharpe(window(bk.run(V, legs=('fund',)))) if V == 'B' else None,
                     'no_hedge': sharpe(window(bk.run(V, hedge=False)))}
        cvr = cv_folds(P, V)
        p2 = pl['variants'][V]
        g['p1_cv'] = cvr['pass']
        g['p2_timing'] = p2['pass'] if p2['control_ok'] else True    # §3: descriptive if the control fails
        g['g9_c6_combo_ge_0_10'] = d3 >= 0.10
        g['g10_dsr_ge_0_9'] = (m['dsr'] or 0.0) >= 0.90
        res['variants'][V] = {'metrics': m, 'cv': cvr, 'placebo': p2, 'gates': {k: bool(v) for k, v in g.items()},
                              'pass': bool(all(g.values())),
                              'series': r59.save_series('r61', f'R61_F1_{V}', r.index.asi8 // 10**6, r.values,
                                                        'r61.py f1', f'{DEV_FROM}..{CUT}')}
        log(f"{V} " + json.dumps({k: (round(v, 3) if isinstance(v, float) else v) for k, v in m.items()
                                  if not isinstance(v, dict)}) + ' legs ' + json.dumps(m['legs']))
        log(f"   cv median {cvr['median']:.3f} pos {cvr['n_pos']}/8; gates {res['variants'][V]['gates']}")
    passing = [V for V, v in res['variants'].items() if v['pass']]
    res['selected'] = max(passing, key=lambda V: res['variants'][V]['metrics']['combo3_delta_c6']) if passing else None
    json.dump(res, open(os.path.join(OUT, 'f1_results.json'), 'w'), indent=1, default=float)
    log(f"selected {res['selected']}")


def selected_variant():
    return json.load(open(os.path.join(OUT, 'f1_results.json')))['selected']


# ----------------------------------------------------------------------------------------------
# §4 q3
# ----------------------------------------------------------------------------------------------
def boot_q3(r, r2, r1, c6, n_boot=Q3_BOOT, seed=SEED):
    """Joint stationary-bootstrap (block 20) SEs of Sharpe(r), Sharpe(r2), rho(r, R1), the R1 combo
    delta and the R1 + C6alts combo delta, over the common days."""
    import r59
    X = pd.concat([r, r2, r1, c6], axis=1, join='inner').dropna().values
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(n_boot):
        ix = r59.stationary_idx(len(X), rng)
        a, b, c, e = (X[ix, i] for i in range(4))
        two = 0.5 * a / a.std() + 0.5 * c / c.std()
        d3 = sharpe((a / a.std() + c / c.std() + e / e.std()) / 3) - sharpe((c / c.std() + e / e.std()) / 2)
        out.append((sharpe(a), sharpe(b), float(np.corrcoef(a, c)[0, 1]), sharpe(two) - sharpe(c), d3))
    return np.array(out).std(0, ddof=1)


def q3_compute(h_syms, h_src_of, variant):
    """§4: the variant's book with legs on h_syms (BTC of U50 as hedge, BTC/ETH in the panel like U50)
    and the frozen C6 basket on the same coins."""
    Ph = Panel(list(h_syms) + ['BTCUSDT', 'ETHUSDT'],
               lambda s: U50_DIR if s in ('BTCUSDT', 'ETHUSDT') else h_src_of(s))
    bk = AsymBook(Ph, list(h_syms))
    r = window(bk.run(variant), Q3_FROM)
    r2 = window(bk.run(variant, cost_mult=2.0), Q3_FROM)
    c6, _ = c6_basket(list(h_syms), h_src_of)
    c6 = window(c6, Q3_FROM)
    r1 = bench('BENCH_R1_common')
    d, s2, s1 = combo_delta(r, r1)
    d3, s3, s32 = combo3_delta(r, r1, c6)
    se = boot_q3(r, r2, r1, c6)
    st = {'variant': variant, 'sharpe': sharpe(r), 'sharpe_cost2': sharpe(r2), 'rho_r1': rho(r, r1), 'combo_delta': d,
          'combo3_delta_c6': d3, 'c6_sharpe': sharpe(c6), 'rho_c6': rho(r, c6), 'se': se.tolist(), 'days': int(len(r)),
          'from': str(r.index[0].date()), 'n_legs_coins': len(h_syms)}
    margins = [('a_sharpe_minus_0_4', st['sharpe'] - 0.4, float(se[0])),
               ('b_cost2_sharpe', st['sharpe_cost2'], float(se[1])),
               ('c_0_3_minus_rho', 0.3 - st['rho_r1'], float(se[2])),
               ('d_combo_delta_minus_0_1', d - 0.1, float(se[3])),
               ('e_c6_combo_delta_minus_0_05', d3 - 0.05, float(se[4]))]
    return {'margins': margins, 'stats': st}


def q3_power():
    from scipy.stats import kurtosis, norm, skew
    import r59
    V = selected_variant()
    out = {'variant': V}
    if V is not None:
        _, v = r59.load_series(f'R61_F1_{V}')
        S_d = sharpe(v)
        n = int((pd.Timestamp(CUT, tz='UTC') - pd.Timestamp(Q3_FROM, tz='UTC')).days + 1)
        sr = S_d / math.sqrt(365)
        g3, g4 = float(skew(v)), float(kurtosis(v, fisher=False))
        se = math.sqrt((1 - g3 * sr + (g4 - 1) / 4 * sr ** 2) / n) * math.sqrt(365)
        out.update({'sharpe_D': S_d, 'skew': g3, 'kurt': g4, 'n_days_H': n, 'se_annual': se,
                    'power_half_effect': float(norm.cdf((0.5 * S_d - 0.4) / se)),
                    'power_full_effect': float(norm.cdf((S_d - 0.4) / se))})
        out['go'] = out['power_half_effect'] >= 0.4
    else:
        out['go'] = False
    json.dump(out, open(os.path.join(OUT, 'f2_power.json'), 'w'), indent=1)
    log(json.dumps(out))
    return out


def q3_selftest():
    """Fake holdout = CV half 1 of r60 (24 U50 alts, seed 60). Exercises r59's four oracle checks on
    q3's real computation; H and the real log are never touched."""
    import tempfile
    import r59_oracle as orc
    os.makedirs(OUT, exist_ok=True)
    fake = json.load(open(os.path.join(r60.OUT, 'cv_halves.json')))['halves']['1']
    V = 'B'      # the computation is the same for both variants; B exercises both legs
    ctx = {}
    direct = q3_compute(fake, lambda s: U50_DIR, V)
    crits = {'st_q3': {'fn': lambda c: q3_compute(fake, lambda s: U50_DIR, V), 'alpha': 0.05, 'desc': 'q3 fake'},
             'st_true': {'fn': lambda c: {'margins': [('t', 1.0, 1.0)], 'stats': {}}, 'alpha': 0.0, 'desc': 't'},
             'st_false': {'fn': lambda c: {'margins': [('f', -1.0, 1.0)], 'stats': {}}, 'alpha': 0.0, 'desc': 'f'},
             'st_x1': {'fn': lambda c: {'margins': [('t', 1.0, 1.0)], 'stats': {}}, 'alpha': 0.0, 'desc': 't'},
             'st_x2': {'fn': lambda c: {'margins': [('t', 1.0, 1.0)], 'stats': {}}, 'alpha': 0.0, 'desc': 't'}}
    tmp = tempfile.mkdtemp(prefix='r61_q3_selftest_')
    lp, sd = os.path.join(tmp, 'log.jsonl'), os.path.join(tmp, 'sealed')
    kw = dict(log_path=lp, sealed_dir=sd, commit='selftest', dirty_fn=lambda: '', sync=False)
    res = {'fake_holdout': fake, 'variant': V, 'direct_stats': direct['stats'],
           'direct_margins': [(n, m, s) for n, m, s in direct['margins']]}
    ans = {q: orc.run_query(q, crits, ctx, noise=0.0, **kw) for q in ('st_q3', 'st_true', 'st_false')}
    exp = {'st_q3': 'PASA' if all(m > 0 for _, m, _ in direct['margins']) else 'NO PASA', 'st_true': 'PASA',
           'st_false': 'NO PASA'}
    res['i_ok'] = ans == exp
    m = [('x', 0.01, 1.0)]
    res['ii_ok'] = orc.noisy(m, 'abc', 'q3') == orc.noisy(m, 'abc', 'q3')
    before = open(lp, 'rb').read()
    ref = {}
    for nm, call in (('repeated', lambda: orc.run_query('st_true', crits, ctx, **kw)),
                     ('dirty', lambda: orc.run_query('st_x1', crits, ctx, **{**kw, 'dirty_fn': lambda: ' M r61.py'}))):
        try:
            call()
            ref[nm] = 'ran (FAIL)'
        except SystemExit as e:
            ref[nm] = str(e)
    orc.run_query('st_x1', crits, ctx, **kw)
    orc.run_query('st_x2', crits, ctx, **kw)
    crits['st_over'] = crits['st_true']
    try:
        orc.run_query('st_over', crits, ctx, **kw)
        ref['budget'] = 'ran (FAIL)'
    except SystemExit as e:
        ref['budget'] = str(e)
    res['iii_refusals'] = ref
    res['iii_ok'] = all('FAIL' not in v for v in ref.values())
    after = open(lp, 'rb').read()
    res['iv_ok'] = after.startswith(before) and len(orc.read_log(lp)) == orc.BUDGET
    res['real_log_untouched'] = all(r['qid'][:3] != 'st_' for r in orc.read_log(orc.LOG))
    res['tracked'] = all(p in orc.TRACKED for p in ('bot/research_scripts/r61.py',
                         'bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261028-r61/PROTOCOL_R61.md'))
    res['pass'] = bool(res['i_ok'] and res['ii_ok'] and res['iii_ok'] and res['iv_ok'] and res['real_log_untouched']
                       and res['tracked'])
    json.dump(res, open(os.path.join(OUT, 'f0_q3_selftest.json'), 'w'), indent=1, default=str)
    log(json.dumps({k: v for k, v in res.items() if k not in ('direct_stats', 'direct_margins', 'fake_holdout')},
                   default=str))


# ----------------------------------------------------------------------------------------------
# §5 F3
# ----------------------------------------------------------------------------------------------
def f3():
    import r59
    ids = C6_FAMILY + [f'R61_F1_{V}' for V in VARIANTS]
    cols = [bench(t) for t in ids]
    r1 = bench('BENCH_R1_common')
    J = pd.concat(cols + [r1], axis=1, join='inner').dropna()
    J = J[J.index <= pd.Timestamp(CUT, tz='UTC')]
    M, b = J.values[:, :-1], J.values[:, -1]
    sd = M.std(0, ddof=1)
    sh = M.mean(0) / sd * math.sqrt(365)
    G_r1 = M - b[:, None] * (sd / b.std(ddof=1))[None, :]
    comb = 0.5 * M / sd[None, :] + 0.5 * (b / b.std(ddof=1))[:, None]
    comb = comb / comb.std(0, ddof=1)[None, :] * b.std(ddof=1)
    G_c = comb - b[:, None]
    p_cash, k_cash = r59.spa_pvalue(M)
    p_r1, k_r1 = r59.spa_pvalue(G_r1)
    p_c, k_c = r59.spa_pvalue(G_c)
    pb, nc = r60.pbo_cscv(M) if M.shape[1] >= 8 else (None, 0)
    res = {'protocol': 'PROTOCOL_R61.md §5', 'window': [str(J.index[0].date()), str(J.index[-1].date())],
           'days': int(len(J)), 'members': ids,
           'sharpe': {t: round(float(x), 4) for t, x in sorted(zip(ids, sh), key=lambda z: -z[1])},
           'spa_cash': {'p': p_cash, 'best': ids[k_cash]}, 'spa_r1': {'p': p_r1, 'best': ids[k_r1]},
           'spa_combo_vs_r1': {'p': p_c, 'best': ids[k_c]}, 'pbo': pb, 'pbo_combinations': nc,
           'r1_sharpe': float(b.mean() / b.std(ddof=1) * math.sqrt(365))}
    json.dump(res, open(os.path.join(OUT, 'f3_spa.json'), 'w'), indent=1, default=float)
    log(json.dumps(res, default=float))


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fns = {'assert_limit': assert_limit, 'overlap': overlap, 'q3_selftest': q3_selftest, 'placebo': placebo,
           'f1': f1, 'q3_power': q3_power, 'f3': f3}
    if cmd not in fns:
        print(__doc__)
        return 1
    os.makedirs(OUT, exist_ok=True)
    fns[cmd]()
    return 0


if __name__ == '__main__':
    sys.exit(main())
