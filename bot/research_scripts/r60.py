"""r60: L/S across the U50 alts with the short tail cut (PROTOCOL_R60.md, 20261028-r60).

Development = the 48 U50 alts (legs) + BTC (hedge); H = N2 ∪ N3 is only read through r59_oracle.

Research container (deps: numpy 1.26 / pandas 2.2 / sklearn 1.8, as r52 ran):
    python research_scripts/r60.py repro    # §1.1: rebuild X0/X1/X2 of r52 (cut at 2024), assert, save scores
    python research_scripts/r60.py diag     # §1.2: short-tail decomposition of r52's X1/X2 books + the F0 gate
    python research_scripts/r60.py halves   # §1.3: CV halves (liquidity-stratified, seed 60), no outcomes
    python research_scripts/r60.py f1       # §3: L0/L1/L2 with construction K, gates g1..g8, series
    python research_scripts/r60.py cv       # §3.3 p1: year x half folds (X1/X2 refit on the other half)
    python research_scripts/r60.py rotation # §3.3 p2: cross-sectional rotation + AR(1) placebos

Every panel is cut at 2024-12-31 on load (raw 1h rows and funding), asserted again on the days.
"""
import json
import math
import os
import sys

import numpy as np
import pandas as pd

import r59_holdout as hg

hg.install()

import r52_xs as xs  # noqa: E402

HERE = hg.HERE
U50_DIR = os.path.join(HERE, 'data', 'r52')
OUT = os.path.join(HERE, 'data', 'r60')
CUT = '2024-12-31'
CUT_MS = int(pd.Timestamp('2025-01-01', tz='UTC').value // 10**6)   # first ms that is sealed
DEV_FROM = '2021-05-24'
SEED = 60
STOP_K = 2.0                  # §3.1: short stop at entry x (1 + 2 sigma_week)
STOP_SLIP = 0.0005            # §3.1: 5 bp adverse slippage on the stop fill (r49 stress rule)
COST = xs.COST                # 0.045% taker + 2 bp, per unit of turnover (r52)
HEDGE = 'BTCUSDT'
TAIL_Q = (0.01, 0.02, 0.05)
GATE_TAIL, GATE_SHARE = 0.02, 0.50
BEAR_Q = ('2021Q2', '2022Q2', '2024Q2')   # r55 label A (k = 0.5) bear quarters inside D


def log(x):
    print(f'[{pd.Timestamp.now():%Y-%m-%d %H:%M:%S}] ==> {x}', flush=True)


# ----------------------------------------------------------------------------------------------
# Panel (r52_xs.load_panel with the cut applied to the raw rows)
# ----------------------------------------------------------------------------------------------
def load_panel(syms, src_of):
    days = pd.date_range('2020-01-01', CUT, freq='D', tz='UTC')
    close, qvol, imb, fund, hourly = {}, {}, {}, {}, {}
    for s in syms:
        a = np.load(os.path.join(src_of(s), f'{s}_1h.npy'))
        a = a[a[:, 0] + 3_600_000 <= CUT_MS] if len(a) else a
        if not len(a):
            continue
        df = pd.DataFrame(a, columns=['t', 'o', 'h', 'l', 'c', 'v', 'qv', 'tbv'])
        df['day'] = pd.to_datetime(df['t'], unit='ms', utc=True).dt.floor('D')
        g = df.groupby('day')
        close[s] = g['c'].last()
        qvol[s] = g['qv'].sum()
        imb[s] = (2 * g['tbv'].sum() / g['v'].sum().replace(0, np.nan) - 1)
        hourly[s] = (a[:, 0].astype(np.int64), a[:, 4].astype(float))
        f = np.load(os.path.join(src_of(s), f'{s}_funding.npy'))
        f = f[f[:, 0] < CUT_MS] if len(f) else f
        if len(f):
            fd = pd.Series(f[:, 1], index=pd.to_datetime(f[:, 0], unit='ms', utc=True).floor('D'))
            fund[s] = fd.groupby(level=0).sum()
    C = pd.DataFrame(close).reindex(days)
    Q = pd.DataFrame(qvol).reindex(days)
    I = pd.DataFrame(imb).reindex(days)
    F = pd.DataFrame(fund).reindex(days).reindex(columns=C.columns).fillna(0.0)
    assert C.index[-1] <= pd.Timestamp(CUT, tz='UTC')
    return C, Q, I, F, hourly


def u50():
    uni = json.load(open(os.path.join(U50_DIR, 'universe50.json')))
    return [u['symbol'] for u in uni], uni


def alts():
    return [s for s in u50()[0] if s not in ('BTCUSDT', 'ETHUSDT')]


class Panel:
    """Everything the books need, built once: daily closes/returns/funding, r52 features and weekly
    samples (cross-sectional ranks over every coin of the panel), eligibility, hourly closes."""

    def __init__(self, syms, src_of):
        self.C, self.Q, self.I, self.F, self.hourly = load_panel(syms, src_of)
        self.feats, self.lr = xs.features(self.C, self.Q, self.I)
        self.elig = xs.eligibility(self.C, self.Q)
        self.S, self.names = xs.weekly_samples(self.C, self.feats, self.elig)
        self.ret = self.C.pct_change(fill_method=None)
        self.fund7 = self.F.rolling(7, min_periods=1).sum()


# ----------------------------------------------------------------------------------------------
# §1.1 reproduction and frozen scores
# ----------------------------------------------------------------------------------------------
def scores_r52(P):
    sc = {'X0': xs.score_x0(P.S), 'X1': xs.predict_walk_forward(P.S, P.names, 'en'),
          'X2': xs.predict_walk_forward(P.S, P.names, 'gbm')}
    common = sc['X1'].notna() & sc['X2'].notna()
    sc = {k: v.where(common) for k, v in sc.items()}
    sc['L0'] = (-P.S['ret1w']).where(common)          # §3.2: reversal of the 1-week return rank
    return sc


def dev_panel():
    syms, _ = u50()
    return Panel(syms, lambda s: U50_DIR)


def repro():
    os.makedirs(OUT, exist_ok=True)
    P = dev_panel()
    sc = scores_r52(P)
    ref = json.load(open(os.path.join(U50_DIR, 'xs.json')))['trials']
    out = {}
    for t in ('X0', 'X1', 'X2'):
        w = xs.weekly_weights(P.S, sc[t], 'ls', P.lr)
        st = xs.stats(xs.simulate(w, P.C, P.F), '2020-01-01', xs.DEV_END)
        out[t] = {'sharpe': st['sharpe'], 'ref': ref[t]['dev']['sharpe'], 'from': st['from']}
        assert abs(st['sharpe'] - ref[t]['dev']['sharpe']) <= 0.005, (t, st['sharpe'], ref[t]['dev']['sharpe'])
    S = P.S
    np.savez_compressed(os.path.join(OUT, 'scores.npz'), k=S['k'].values, day=S['day'].astype('int64').values // 10**6,
                        sym=S['sym'].values.astype(str), **{t: sc[t].values for t in ('X0', 'X1', 'X2', 'L0')})
    json.dump({'protocol': 'PROTOCOL_R60.md §1.1', 'repro': out}, open(os.path.join(OUT, 'f0_repro.json'), 'w'), indent=1)
    log(json.dumps(out))


def load_scores(S):
    z = np.load(os.path.join(OUT, 'scores.npz'), allow_pickle=False)
    assert (z['k'] == S['k'].values).all() and (z['sym'] == S['sym'].values.astype(str)).all()
    return {t: pd.Series(z[t], index=S.index) for t in ('X0', 'X1', 'X2', 'L0')}


# ----------------------------------------------------------------------------------------------
# Short stops: per (formation, coin), precomputed from the 1h closes (they do not depend on weights)
# ----------------------------------------------------------------------------------------------
def stop_path(P, sym, d0, d1, entry, sigma_w):
    """First 1h close in days (d0, d1] at or above entry x (1 + k sigma_w): (day, exit price) or None."""
    if not (np.isfinite(entry) and np.isfinite(sigma_w)) or sym not in P.hourly:
        return None
    t, c = P.hourly[sym]
    lo = np.searchsorted(t, d0.value // 10**6 + 86_400_000)
    hi = np.searchsorted(t, d1.value // 10**6 + 86_400_000)
    hit = np.flatnonzero(c[lo:hi] >= entry * (1 + STOP_K * sigma_w))
    if not len(hit):
        return None
    j = lo + hit[0]
    return pd.Timestamp(t[j] // 86_400_000 * 86_400_000, unit='ms', tz='UTC'), c[j] * (1 + STOP_SLIP)


# ----------------------------------------------------------------------------------------------
# Construction K (§3.1) and its simulator
# ----------------------------------------------------------------------------------------------
class Book:
    """Weekly formations of one panel. `weights(score)` -> {k: (d0, {sym: w})} with construction K;
    `run(weights)` -> daily returns (constant equity fractions inside the week, like r52)."""

    def __init__(self, P, legs, hedge=HEDGE):
        self.P, self.legs, self.hedge = P, list(legs), hedge
        S = P.S[P.S['sym'].isin(self.legs)]
        self.S = S
        self.days = sorted(S['day'].unique())
        self.span = {}
        idx = P.C.index
        for j, d0 in enumerate(self.days):
            d1 = self.days[j + 1] if j + 1 < len(self.days) else idx[-1]
            self.span[d0] = (d1, idx[(idx > d0) & (idx <= d1)])
        self._stops = {}

    def stop(self, sym, d0):
        key = (sym, d0)
        if key not in self._stops:
            d1, _ = self.span[d0]
            P = self.P
            sig = P.feats['vol30'].at[d0, sym] * math.sqrt(7)
            self._stops[key] = stop_path(P, sym, d0, d1, P.C.at[d0, sym], sig)
        return self._stops[key]

    def weights(self, score, subset=None, crowded=True, beta=True):
        S = self.S if subset is None else self.S[self.S['sym'].isin(subset)]
        P = self.P
        out = {}
        for _, g in S.assign(score=score.reindex(S.index)).dropna(subset=['score']).groupby('day'):
            n = len(g)
            if n < 5:
                continue
            q = int(math.ceil(n / 5))
            g = g.sort_values('score', kind='mergesort')
            d0 = g['day'].iloc[0]
            vol = g['vol30_raw'].fillna(g['vol30_raw'].median()).clip(lower=1e-4)
            top, bot = g.tail(q), g.head(q)
            if crowded:
                f7 = P.fund7.loc[d0, bot['sym']].values
                bot = bot[~(f7 < 0)]
            w = {}
            for leg, sign in ((top, 1.0), (bot, -1.0)):
                if len(leg):
                    inv = 1 / vol.loc[leg.index]
                    for i, x in (inv / inv.sum() * 0.5).items():
                        w[g.at[i, 'sym']] = sign * float(x)
            if beta:
                b = sum(x * (P.feats['beta60'].at[d0, s] if np.isfinite(P.feats['beta60'].at[d0, s]) else 1.0)
                        for s, x in w.items())
                w[self.hedge] = w.get(self.hedge, 0.0) - b
            out[d0] = w
        return out

    def run(self, weights, cost_mult=1.0, stops=True):
        P = self.P
        rets, dlist = [], []
        prev = {}
        for d0 in sorted(weights):
            w = weights[d0]
            d1, span = self.span[d0]
            turn = sum(abs(w.get(s, 0) - prev.get(s, 0)) for s in set(w) | set(prev))
            stop_at = {}
            if stops:
                for s, x in w.items():
                    if x < 0 and s != self.hedge:
                        hit = self.stop(s, d0)
                        if hit is not None:
                            stop_at[s] = hit
            end = dict(w)
            for n, day in enumerate(span):
                r = 0.0
                for s, x in w.items():
                    if s in stop_at and day > stop_at[s][0]:
                        continue
                    if s in stop_at and day == stop_at[s][0]:
                        prevc = P.C.at[span[n - 1], s] if n > 0 else P.C.at[d0, s]
                        rr = stop_at[s][1] / prevc - 1
                        r -= abs(x) * COST * cost_mult
                        end[s] = 0.0
                    else:
                        rr = P.ret.at[day, s]
                        rr = rr if np.isfinite(rr) else 0.0
                    r += x * rr - x * P.F.at[day, s]
                if n == 0:
                    r -= turn * COST * cost_mult
                rets.append(r)
                dlist.append(day)
            prev = end
        return pd.Series(rets, index=pd.DatetimeIndex(dlist))


# ----------------------------------------------------------------------------------------------
# Metrics shared by F1/F2
# ----------------------------------------------------------------------------------------------
def sharpe(r):
    r = np.asarray(r, float)
    sd = r.std(ddof=1)
    return float(r.mean() / sd * math.sqrt(365)) if sd > 0 else 0.0


def window(r, frm=DEV_FROM, to=CUT):
    return r[(r.index >= pd.Timestamp(frm, tz='UTC')) & (r.index <= pd.Timestamp(to, tz='UTC'))]


def bench(tid):
    import r59
    d, v = r59.load_series(tid)
    return pd.Series(v, index=pd.to_datetime(d, unit='ms', utc=True))


def combo_delta(r, r1):
    """R1 + sleeve at equal risk (50/50 on series scaled to equal vol) minus R1 alone, common days."""
    j = pd.concat([r, r1], axis=1, join='inner').dropna()
    a, b = j.iloc[:, 0], j.iloc[:, 1]
    c = 0.5 * a / a.std() + 0.5 * b / b.std()
    return sharpe(c) - sharpe(b), sharpe(c), sharpe(b)


def rho(a, b):
    j = pd.concat([a, b], axis=1, join='inner').dropna()
    return float(j.corr().iloc[0, 1])


def quarter_of(ix):
    return np.array([f'{d.year}Q{(d.month - 1) // 3 + 1}' for d in ix])


# ----------------------------------------------------------------------------------------------
# §1.2 tail diagnostic and the F0 gate
# ----------------------------------------------------------------------------------------------
def diag():
    P = dev_panel()
    sc = load_scores(P.S)
    allsyms = list(P.C.columns)
    bk = Book(P, allsyms)          # r52 universe (50), only used for its spans and stop paths
    res = {'protocol': 'PROTOCOL_R60.md §1.2', 'window': [DEV_FROM, CUT], 'models': {}}
    pooled = []
    for t in ('X1', 'X2'):
        w = xs.weekly_weights(P.S, sc[t], 'ls', P.lr)
        r = window(xs.simulate(w, P.C, P.F))
        rows = []
        for k, (d0, ws) in w.items():
            if d0 < pd.Timestamp(DEV_FROM, tz='UTC') or d0 not in bk.span:
                continue
            d1, span = bk.span[d0]
            for s, x in ws.items():
                if x >= 0:
                    continue
                rr = P.ret.loc[span, s].fillna(0.0).sum()
                rows.append({'d0': d0, 'sym': s, 'w': x, 'c': x * rr, 'ret_final': P.C.at[d1, s] / P.C.at[d0, s] - 1,
                             'fund7': P.fund7.at[d0, s]})
        df = pd.DataFrame(rows)
        loss_total = -df.loc[df['c'] < 0, 'c'].sum()
        m = {'short_coin_weeks': int(len(df)), 'short_leg_pnl': float(df['c'].sum()),
             'short_leg_loss': float(loss_total), 'book_sharpe': sharpe(r), 'tails': {}}
        for q in TAIL_Q:
            n = max(1, int(round(q * len(df))))
            tail = df.nsmallest(n, 'c').copy()
            crd = []
            for _, row in tail.iterrows():
                hit = bk.stop(row['sym'], row['d0'])
                avoid = 0.0
                if hit is not None:
                    at = hit[1] / (1 + STOP_SLIP) / P.C.at[row['d0'], row['sym']] - 1
                    avoid = max(0.0, row['ret_final'] - at) * abs(row['w'])
                loss = -row['c']
                crowded = bool(row['fund7'] < 0)
                crd.append({'loss': loss, 'avoid': min(avoid, loss) if loss > 0 else 0.0, 'crowded': crowded,
                            'credit': loss if crowded else (min(avoid, loss) if loss > 0 else 0.0), 'hit': hit is not None})
            cd = pd.DataFrame(crd)
            # Descriptive only: the book with those coin-weeks worth 0 (their daily rows removed at weight).
            sub = {(row['d0'], row['sym']) for _, row in tail.iterrows()}
            r_wo = xs.simulate({k: (d0, {s: x for s, x in ws.items() if (d0, s) not in sub}) for k, (d0, ws) in w.items()},
                               P.C, P.F)
            m['tails'][str(q)] = {'n': int(n), 'share_of_short_loss': float(cd['loss'].sum() / loss_total),
                                  'stop_hit_frac': float(cd['hit'].mean()),
                                  'avoidable_share': float(cd['avoid'].sum() / cd['loss'].sum()),
                                  'crowded_share': float(cd.loc[cd['crowded'], 'loss'].sum() / cd['loss'].sum()),
                                  'credit_share': float(cd['credit'].sum() / cd['loss'].sum()),
                                  'book_sharpe_without_tail': sharpe(window(r_wo))}
            if q == GATE_TAIL:
                pooled.append(cd)
        # Funding by leg over D (descriptive): sum over days of -w * funding.
        fl = {'long': 0.0, 'short': 0.0}
        for k, (d0, ws) in w.items():
            if d0 < pd.Timestamp(DEV_FROM, tz='UTC') or d0 not in bk.span:
                continue
            span = bk.span[d0][1]
            for s, x in ws.items():
                fl['long' if x > 0 else 'short'] += float(-x * P.F.loc[span, s].sum())
        m['funding_pnl_by_leg'] = fl
        res['models'][t] = m
    cd = pd.concat(pooled)
    share = float(cd['credit'].sum() / cd['loss'].sum())
    res['gate'] = {'tail': GATE_TAIL, 'credit_share_pooled': share, 'threshold': GATE_SHARE,
                   'avoidable_share_pooled': float(cd['avoid'].sum() / cd['loss'].sum()),
                   'crowded_share_pooled': float(cd.loc[cd['crowded'], 'loss'].sum() / cd['loss'].sum()),
                   'continue': share >= GATE_SHARE}
    json.dump(res, open(os.path.join(OUT, 'f0_diag.json'), 'w'), indent=1, default=float)
    log(json.dumps(res['gate']))
    for t, m in res['models'].items():
        log(f"{t} book {m['book_sharpe']:.3f} " + json.dumps({q: {k: round(v, 3) for k, v in x.items()}
                                                              for q, x in m['tails'].items()}))


# ----------------------------------------------------------------------------------------------
# §1.3 CV halves
# ----------------------------------------------------------------------------------------------
def halves():
    _, uni = u50()
    a = sorted([u for u in uni if u['symbol'] not in ('BTCUSDT', 'ETHUSDT')], key=lambda u: -float(u['vol24h']))
    rng = np.random.default_rng(SEED)
    h = {0: [], 1: []}
    for i in range(0, len(a), 2):
        pair = a[i:i + 2]
        order = rng.permutation(len(pair))
        for j, o in enumerate(order):
            h[j].append(pair[o]['symbol'])
    json.dump({'protocol': 'PROTOCOL_R60.md §1.3', 'seed': SEED, 'halves': h}, open(os.path.join(OUT, 'cv_halves.json'), 'w'),
              indent=1)
    log({k: len(v) for k, v in h.items()})


# ----------------------------------------------------------------------------------------------
# Vectorised construction K (same rules as Book; asserted equal to it in f1 before any gate)
# ----------------------------------------------------------------------------------------------
class FastBook:
    """Construction K on numpy arrays. Scores come as an array aligned with `self.S` (the leg rows of
    the panel's weekly samples). Stops are precomputed for every eligible (formation, coin)."""

    def __init__(self, P, legs, hedge=HEDGE):
        ref = Book(P, legs, hedge)
        self.ref, self.P, self.S = ref, P, ref.S
        coins = list(legs) + [hedge]
        self.coins, ci = coins, {s: i for i, s in enumerate(coins)}
        self.hi = ci[hedge]
        idx = P.C.index
        self.days = idx
        self.R = np.nan_to_num(P.ret.reindex(columns=coins).values, nan=0.0)
        self.Fm = P.F.reindex(columns=coins).fillna(0.0).values
        S = self.S.reset_index()
        self.forms = []
        for d0, g in S.groupby('day', sort=True):
            d1, span = ref.span[d0]
            rows = idx.get_indexer(span)
            ix = np.array([ci[s] for s in g['sym']])
            vol = g['vol30_raw'].fillna(g['vol30_raw'].median()).clip(lower=1e-4).values
            f7 = P.fund7.loc[d0, g['sym']].values
            beta = np.array([P.feats['beta60'].at[d0, s] for s in g['sym']])
            beta = np.where(np.isfinite(beta), beta, 1.0)
            hit_row = np.full(len(ix), -1)
            hit_ret = np.zeros(len(ix))
            for j, s in enumerate(g['sym']):
                h = ref.stop(s, d0)
                if h is not None:
                    n = int(np.searchsorted(rows, idx.get_loc(h[0])))
                    prevc = P.C.at[span[n - 1], s] if n > 0 else P.C.at[d0, s]
                    hit_row[j], hit_ret[j] = n, h[1] / prevc - 1
            self.forms.append({'d0': d0, 'rows': rows, 'pos': g['index'].values, 'ix': ix, 'vol': vol,
                               'f7': f7, 'beta': beta, 'hit_row': hit_row, 'hit_ret': hit_ret,
                               'sym': g['sym'].values})
        self.pos_of = {p: i for i, p in enumerate(self.S.index)}

    def run(self, score, subset=None, cost_mult=1.0, crowded=True, beta=True, stops=True):
        """score: pd.Series on S's index (NaN = no score). Returns daily returns (pd.Series)."""
        sc_all = score.reindex(self.S.index).values
        keep_sym = None if subset is None else set(subset)
        out_r, out_d = [], []
        prev = np.zeros(len(self.coins))
        posmap = self.pos_of
        for f in self.forms:
            sc = sc_all[[posmap[p] for p in f['pos']]]
            ok = np.isfinite(sc)
            if keep_sym is not None:
                ok &= np.array([s in keep_sym for s in f['sym']])
            n = int(ok.sum())
            if n < 5:
                continue
            q = int(math.ceil(n / 5))
            cand = np.flatnonzero(ok)
            order = cand[np.argsort(sc[cand], kind='mergesort')]
            top, bot = order[-q:], order[:q]
            if crowded:
                bot = bot[~(f['f7'][bot] < 0)]
            w = np.zeros(len(self.coins))
            for leg, sign in ((top, 1.0), (bot, -1.0)):
                if len(leg):
                    inv = 1 / f['vol'][leg]
                    w[f['ix'][leg]] += sign * inv / inv.sum() * 0.5
            if beta:
                legs_ = np.r_[top, bot]
                w[self.hi] -= float((w[f['ix'][legs_]] * f['beta'][legs_]).sum())
            rows = f['rows']
            Rb = self.R[rows].copy()
            Fb = self.Fm[rows].copy()
            cost = np.zeros(len(rows))
            cost[0] += np.abs(w - prev).sum() * COST * cost_mult
            end = w.copy()
            if stops:
                for j in bot:
                    hr = f['hit_row'][j]
                    if hr >= 0:
                        c = f['ix'][j]
                        Rb[hr, c] = f['hit_ret'][j]
                        Rb[hr + 1:, c] = 0.0
                        Fb[hr + 1:, c] = 0.0
                        cost[hr] += abs(w[c]) * COST * cost_mult
                        end[c] = 0.0
            out_r.append(Rb @ w - Fb @ w - cost)
            out_d.append(self.days[rows])
            prev = end
        return pd.Series(np.concatenate(out_r), index=pd.DatetimeIndex(np.concatenate(out_d)))

    def weights_ref(self, score, subset=None):
        return self.ref.weights(score, subset)


VARIANTS = {'L0': 'L0', 'L1': 'X1', 'L2': 'X2'}


def old20(P):
    return [s for s in alts() if P.C[s].first_valid_index() <= pd.Timestamp('2020-07-01', tz='UTC')][:20]


def capacity(fb, score):
    """Capital at which every position is <= 1% of its 30-day median daily quote volume (§3.1)."""
    med = fb.P.Q.rolling(30, min_periods=20).median()
    caps = []
    w = fb.ref.weights(score)
    for d0, ws in w.items():
        if d0 < pd.Timestamp(DEV_FROM, tz='UTC'):
            continue
        c = [0.01 * med.at[d0, s] / abs(x) for s, x in ws.items() if abs(x) > 1e-9 and np.isfinite(med.at[d0, s])]
        if c:
            caps.append(min(c))
    return {'median_usdt': float(np.median(caps)), 'p10_usdt': float(np.percentile(caps, 10))}


def gates_of(r, r2, r24, rold, r1, p55):
    wk = r.resample('W-SUN').sum()
    pnl = float(wk.sum())
    top5 = float(wk.nlargest(5).sum() / pnl) if pnl > 0 else float('inf')
    q = quarter_of(r.index)
    bear = r[np.isin(q, BEAR_Q)]
    d, sc, s1 = combo_delta(r, r1)
    m = {'sharpe': sharpe(r), 'sharpe_cost2': sharpe(r2), 'sharpe_2024': sharpe(r24), 'sharpe_old20': sharpe(rold),
         'top5_share': top5, 'rho_r1': rho(r, r1), 'rho_p55': rho(r, p55), 'bear_sum': float(bear.sum()),
         'bear_rho_r1': rho(bear, r1), 'combo_sharpe': sc, 'r1_sharpe': s1, 'combo_delta': d,
         'cagr': float(np.prod(1 + r.values) ** (365 / len(r)) - 1),
         'max_dd': float((np.cumprod(1 + r.values) / np.maximum.accumulate(np.cumprod(1 + r.values)) - 1).min()),
         'vol': float(r.std() * math.sqrt(365)), 'from': str(r.index[0].date()), 'to': str(r.index[-1].date())}
    g = {'g1_sharpe_ge_0_8': m['sharpe'] >= 0.8, 'g2_cost2_ge_0_4': m['sharpe_cost2'] >= 0.4,
         'g3_2024_pos': m['sharpe_2024'] > 0, 'g4_old20_pos': m['sharpe_old20'] > 0, 'g5_top5_lt_0_6': top5 < 0.6,
         'g6_rho_le_0_3': m['rho_r1'] <= 0.3 and m['rho_p55'] <= 0.3,
         'g7_bear': m['bear_sum'] >= 0 and m['bear_rho_r1'] <= 0.3, 'g8_combo_ge_0_15': d >= 0.15}
    return m, g


def f1():
    import r59
    P = dev_panel()
    sc = load_scores(P.S)
    fb = FastBook(P, alts())
    # Equality check vector vs reference engine (L1), before any gate is computed.
    r_ref = window(fb.ref.run(fb.ref.weights(sc['X1'])))
    r_fast = window(fb.run(sc['X1']))
    assert np.allclose(r_ref.values, r_fast.reindex(r_ref.index).values, atol=1e-10), 'FastBook != Book'
    r1, p55 = bench('BENCH_R1_common'), bench('BENCH_P55_common')
    o20 = old20(P)
    pre = {}
    for nm in ('f1_cv.json', 'f1_rotation.json'):
        pth = os.path.join(OUT, nm)
        pre[nm] = json.load(open(pth)) if os.path.exists(pth) else None
    res = {'protocol': 'PROTOCOL_R60.md §3', 'window': [DEV_FROM, CUT], 'old20': o20, 'variants': {}}
    for L, t in VARIANTS.items():
        s = sc[t]
        r = window(fb.run(s))
        r2 = window(fb.run(s, cost_mult=2.0))
        rold = window(fb.run(s, subset=o20))
        m, g = gates_of(r, r2, window(r, '2024-01-01'), rold, r1, p55)
        # Attribution of K's pieces (descriptive, same variant, no extra N): each piece switched off alone.
        m['without'] = {'stop': sharpe(window(fb.run(s, stops=False))), 'crowded': sharpe(window(fb.run(s, crowded=False))),
                        'beta': sharpe(window(fb.run(s, beta=False))),
                        'all_K_off': sharpe(window(fb.run(s, stops=False, crowded=False, beta=False)))}
        m['capacity'] = capacity(fb, s)
        cvp = pre['f1_cv.json'] and pre['f1_cv.json']['variants'][L]
        rot = pre['f1_rotation.json'] and pre['f1_rotation.json']['variants'][L]
        g['p1_cv'] = bool(cvp and cvp['pass'])
        g['p2_rotation'] = bool(rot and rot['p'] < 0.10)
        res['variants'][L] = {'score': t, 'metrics': m, 'gates': {k: bool(v) for k, v in g.items()},
                              'pass': bool(all(g.values())),
                              'series': r59.save_series('r60', f'R60_F1_{L}', r.index.asi8 // 10**6, r.values,
                                                        'r60.py f1', f'{DEV_FROM}..{CUT}')}
        log(f"{L} " + json.dumps({k: (round(v, 3) if isinstance(v, float) else v) for k, v in m.items()
                                  if not isinstance(v, dict)}) + ' ' + json.dumps(m['without']))
        log(f"   gates {res['variants'][L]['gates']}")
    passing = [L for L, v in res['variants'].items() if v['pass']]
    res['selected'] = max(passing, key=lambda L: res['variants'][L]['metrics']['sharpe']) if passing else None
    json.dump(res, open(os.path.join(OUT, 'f1_results.json'), 'w'), indent=1, default=float)
    log(f"selected {res['selected']}")


# ----------------------------------------------------------------------------------------------
# §3.3 p1: CV year x half (X1/X2 refit walk-forward on the other half; L0 has no fit)
# ----------------------------------------------------------------------------------------------
def predict_wf_split(S, names, kind, train_mask, pred_mask):
    """r52_xs.predict_walk_forward with training rows restricted to train_mask and predictions only on
    pred_mask; same refit schedule, purge and models."""
    from sklearn.ensemble import HistGradientBoostingRegressor
    from sklearn.linear_model import ElasticNetCV
    from sklearn.model_selection import TimeSeriesSplit
    import warnings
    weeks = sorted(S['k'].unique())
    preds = pd.Series(np.nan, index=S.index)
    model = None
    for j, k in enumerate(weeks):
        train = S[train_mask & (S['k'] <= k - 2) & S['target'].notna()]
        if train['k'].nunique() < xs.TRAIN_MIN_WEEKS:
            continue
        if model is None or j % xs.REFIT_EVERY == 0:
            X, y = train[names].values, train['target'].values
            if kind == 'en':
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    model = ElasticNetCV(l1_ratio=[0.1, 0.5, 0.9], cv=TimeSeriesSplit(5), n_alphas=30,
                                         max_iter=5000).fit(X, y)
            else:
                model = HistGradientBoostingRegressor(max_depth=3, learning_rate=0.05, max_iter=200,
                                                      min_samples_leaf=50, l2_regularization=1.0,
                                                      random_state=0).fit(X, y)
        idx = S.index[(S['k'] == k) & pred_mask]
        if len(idx):
            preds.loc[idx] = model.predict(S.loc[idx, names].values)
    return preds


def cv():
    P = dev_panel()
    sc = load_scores(P.S)
    H = json.load(open(os.path.join(OUT, 'cv_halves.json')))['halves']
    fb = FastBook(P, alts())
    common = sc['X1'].notna() & sc['X2'].notna()
    res = {'protocol': 'PROTOCOL_R60.md §1.3/§3.3 p1', 'variants': {}}
    for L, t in VARIANTS.items():
        folds = []
        for h in ('0', '1'):
            mine = P.S['sym'].isin(H[h])
            if t == 'L0':
                s = sc['L0']
            else:
                s = predict_wf_split(P.S, P.names, 'en' if t == 'X1' else 'gbm', ~mine, mine).where(common)
            r = fb.run(s, subset=H[h])
            for y in ('2021', '2022', '2023', '2024'):
                ry = window(r, max(DEV_FROM, f'{y}-01-01'), f'{y}-12-31')
                folds.append({'half': h, 'year': y, 'sharpe': sharpe(ry), 'days': int(len(ry))})
        sh = [f['sharpe'] for f in folds]
        res['variants'][L] = {'folds': folds, 'median': float(np.median(sh)), 'n_pos': int(sum(x > 0 for x in sh)),
                              'pass': bool(np.median(sh) > 0 and sum(x > 0 for x in sh) >= 5)}
        log(f"{L} cv median {np.median(sh):.3f} pos {sum(x > 0 for x in sh)}/8 " +
            ' '.join(f"{f['half']}{f['year'][2:]}:{f['sharpe']:.2f}" for f in folds))
    json.dump(res, open(os.path.join(OUT, 'f1_cv.json'), 'w'), indent=1, default=float)


# ----------------------------------------------------------------------------------------------
# §3.3 p2: cross-sectional rotation and AR(1) placebos
# ----------------------------------------------------------------------------------------------
N_ROT, ROT_MIN_W = 1000, 13
N_PLACEBO, PLACEBO_ROT = 100, 200


def coin_rows(S, score):
    """sym -> positions (into S.index order) of rows with a finite score, sorted by week."""
    v = score.reindex(S.index)
    out = {}
    for s, g in S.assign(_v=v.values).groupby('sym'):
        g = g[np.isfinite(g['_v'])].sort_values('k')
        if len(g) > 2 * ROT_MIN_W + 1:
            out[s] = g.index.values
    return out


def rotate(score, rows, rng):
    new = score.copy()
    for s, ix in rows.items():
        n = len(ix)
        o = int(rng.integers(ROT_MIN_W, n - ROT_MIN_W + 1))
        new.loc[ix] = np.roll(score.loc[ix].values, o)
    return new


def rotation_p(fb, score, n_rot, rng):
    obs = sharpe(window(fb.run(score)))
    rows = coin_rows(fb.S, score)
    null = np.array([sharpe(window(fb.run(rotate(score, rows, rng)))) for _ in range(n_rot)])
    return obs, float((1 + (null >= obs).sum()) / (n_rot + 1)), null


def rotation():
    P = dev_panel()
    sc = load_scores(P.S)
    fb = FastBook(P, alts())
    rng = np.random.default_rng(SEED)
    res = {'protocol': 'PROTOCOL_R60.md §1.3/§3.3 p2', 'n_rot': N_ROT, 'variants': {}}
    # Placebos first (calibration): AR(1) scores with X1's mean weekly autocorrelation.
    x1 = sc['X1'].reindex(fb.S.index)
    rows = coin_rows(fb.S, x1)
    ac = [np.corrcoef(x1.loc[ix].values[:-1], x1.loc[ix].values[1:])[0, 1] for ix in rows.values()]
    phi = float(np.nanmean(ac))
    ps = []
    for i in range(N_PLACEBO):
        pl = pd.Series(np.nan, index=fb.S.index)
        for s, ix in rows.items():
            e = rng.normal(size=len(ix))
            z = np.empty(len(ix))
            z[0] = e[0]
            for t in range(1, len(ix)):
                z[t] = phi * z[t - 1] + math.sqrt(1 - phi ** 2) * e[t]
            pl.loc[ix] = z
        ps.append(rotation_p(fb, pl, PLACEBO_ROT, rng)[1])
        if (i + 1) % 20 == 0:
            log(f'placebo {i + 1}/{N_PLACEBO} frac p<0.10 so far {np.mean(np.array(ps) < 0.10):.3f}')
    frac = float(np.mean(np.array(ps) < 0.10))
    res['placebo'] = {'phi': phi, 'n': N_PLACEBO, 'rot_each': PLACEBO_ROT, 'frac_p_lt_0_10': frac,
                      'calibrated': bool(0.03 <= frac <= 0.17)}
    for L, t in VARIANTS.items():
        obs, p, null = rotation_p(fb, sc[t], N_ROT, rng)
        res['variants'][L] = {'obs_sharpe': obs, 'p': p, 'null_mean': float(null.mean()), 'null_p95': float(np.percentile(null, 95))}
        log(f'{L} rotation obs {obs:.3f} p {p:.4f} null mean {null.mean():.3f} p95 {np.percentile(null, 95):.3f}')
    json.dump(res, open(os.path.join(OUT, 'f1_rotation.json'), 'w'), indent=1, default=float)


# ----------------------------------------------------------------------------------------------
# §4 q2: the selected variant's book on a holdout bank (real H inside the oracle, or a fake one)
# ----------------------------------------------------------------------------------------------
Q2_FROM = '2021-07-02'
Q2_BOOT = 1000


def boot_stats(r, r2, r1, n_boot=Q2_BOOT, seed=SEED):
    """Stationary-bootstrap (block 20) SEs of Sharpe(r), Sharpe(r2), rho(r, r1) and the R1 combo delta,
    resampling the common days jointly."""
    import r59
    j = pd.concat([r, r2, r1], axis=1, join='inner').dropna()
    X = j.values
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(n_boot):
        ix = r59.stationary_idx(len(X), rng)
        a, b, c = X[ix, 0], X[ix, 1], X[ix, 2]
        comb = 0.5 * a / a.std() + 0.5 * c / c.std()
        out.append((sharpe(a), sharpe(b), float(np.corrcoef(a, c)[0, 1]), sharpe(comb) - sharpe(c)))
    return np.array(out).std(0, ddof=1)


def q2_compute(h_syms, h_src_of, train_syms, variant):
    """Book K of `variant` with legs on h_syms (BTC hedge, BTC/ETH in the panel like U50), scores from
    models fit walk-forward on train_syms' rows only. Returns the oracle's margins and stats."""
    t = VARIANTS[variant]
    Pu = Panel(train_syms, lambda s: U50_DIR)
    Ph = Panel(list(h_syms) + ['BTCUSDT', 'ETHUSDT'], lambda s: U50_DIR if s in ('BTCUSDT', 'ETHUSDT') else h_src_of(s))
    if t == 'L0':
        score = -Ph.S['ret1w']
    else:
        Su, Sh = Pu.S.copy(), Ph.S.copy()
        Sh.index = Sh.index + len(Su) + 10
        A = pd.concat([Su, Sh])
        tr = pd.Series(A.index.isin(Su.index), index=A.index)
        kind = 'en' if t == 'X1' else 'gbm'
        pr = predict_wf_split(A, Pu.names, kind, tr, ~tr)
        # The common-weeks rule of r52: both models must predict (they share the refit schedule).
        other = predict_wf_split(A, Pu.names, 'gbm' if kind == 'en' else 'en', tr, ~tr)
        score = pr.where(other.notna()).loc[Sh.index]
        score.index = Ph.S.index
    fb = FastBook(Ph, list(h_syms))
    r = window(fb.run(score), Q2_FROM)
    r2 = window(fb.run(score, cost_mult=2.0), Q2_FROM)
    r1 = bench('BENCH_R1_common')
    d, sc, s1 = combo_delta(r, r1)
    se = boot_stats(r, r2, r1)
    st = {'variant': variant, 'sharpe': sharpe(r), 'sharpe_cost2': sharpe(r2), 'rho_r1': rho(r, r1), 'combo_delta': d,
          'combo_sharpe': sc, 'r1_sharpe': s1, 'se': se.tolist(), 'days': int(len(r)), 'from': str(r.index[0].date()),
          'n_legs_coins': len(h_syms)}
    margins = [('a_sharpe_minus_0_4', st['sharpe'] - 0.4, float(se[0])),
               ('b_cost2_sharpe', st['sharpe_cost2'], float(se[1])),
               ('c_0_3_minus_rho', 0.3 - st['rho_r1'], float(se[2])),
               ('d_combo_delta_minus_0_1', d - 0.1, float(se[3]))]
    return {'margins': margins, 'stats': st}


def selected_variant():
    return json.load(open(os.path.join(OUT, 'f1_results.json')))['selected']


def q2_power():
    """§4: Lo (2002) SE of the annual Sharpe over H's window with the D book's daily skew/kurtosis."""
    from scipy.stats import norm, skew, kurtosis
    L = selected_variant()
    import r59
    d, v = r59.load_series(f'R60_F1_{L}')
    S_d = sharpe(v)
    n = int((pd.Timestamp(CUT, tz='UTC') - pd.Timestamp(Q2_FROM, tz='UTC')).days + 1)
    sr = S_d / math.sqrt(365)
    g3, g4 = float(skew(v)), float(kurtosis(v, fisher=False))
    se = math.sqrt((1 - g3 * sr + (g4 - 1) / 4 * sr ** 2) / n) * math.sqrt(365)
    power = float(norm.cdf((0.5 * S_d - 0.4) / se))
    out = {'variant': L, 'sharpe_D': S_d, 'skew': g3, 'kurt': g4, 'n_days_H': n, 'se_annual': se,
           'power_half_effect': power, 'power_full_effect': float(norm.cdf((S_d - 0.4) / se)), 'go': power >= 0.4}
    json.dump(out, open(os.path.join(OUT, 'f2_power.json'), 'w'), indent=1)
    log(json.dumps(out))
    return out


def q2_selftest():
    """Fake holdout = CV half 1 (24 U50 alts, seed 60); models fit on half 0 + BTC/ETH. Exercises the
    oracle mechanics of r59's selftest on q2's real computation. H and the real log are never touched."""
    import tempfile
    import r59_oracle as orc
    H = json.load(open(os.path.join(OUT, 'cv_halves.json')))['halves']
    fake, train = H['1'], H['0'] + ['BTCUSDT', 'ETHUSDT']
    L = selected_variant() or 'L1'
    ctx = {}
    crits = {'st_q2': {'fn': lambda c: q2_compute(fake, lambda s: U50_DIR, train, L), 'alpha': 0.05, 'desc': 'q2 fake'},
             'st_true': {'fn': lambda c: {'margins': [('t', 1.0, 1.0)], 'stats': {}}, 'alpha': 0.0, 'desc': 't'},
             'st_false': {'fn': lambda c: {'margins': [('f', -1.0, 1.0)], 'stats': {}}, 'alpha': 0.0, 'desc': 'f'},
             'st_x1': {'fn': lambda c: {'margins': [('t', 1.0, 1.0)], 'stats': {}}, 'alpha': 0.0, 'desc': 't'},
             'st_x2': {'fn': lambda c: {'margins': [('t', 1.0, 1.0)], 'stats': {}}, 'alpha': 0.0, 'desc': 't'}}
    direct = q2_compute(fake, lambda s: U50_DIR, train, L)
    tmp = tempfile.mkdtemp(prefix='r60_q2_selftest_')
    lp, sd = os.path.join(tmp, 'log.jsonl'), os.path.join(tmp, 'sealed')
    kw = dict(log_path=lp, sealed_dir=sd, commit='selftest', dirty_fn=lambda: '', sync=False)
    res = {'fake_holdout': fake, 'variant': L, 'direct_stats': direct['stats']}
    ans = {q: orc.run_query(q, crits, ctx, noise=0.0, **kw) for q in ('st_q2', 'st_true', 'st_false')}
    exp = {'st_q2': 'PASA' if all(m > 0 for _, m, _ in direct['margins']) else 'NO PASA', 'st_true': 'PASA',
           'st_false': 'NO PASA'}
    res['i_ok'] = ans == exp
    m = [('x', 0.01, 1.0)]
    res['ii_ok'] = orc.noisy(m, 'abc', 'q2') == orc.noisy(m, 'abc', 'q2')
    before = open(lp, 'rb').read()
    ref = {}
    for nm, call in (('repeated', lambda: orc.run_query('st_true', crits, ctx, **kw)),
                     ('dirty', lambda: orc.run_query('st_x1', crits, ctx, **{**kw, 'dirty_fn': lambda: ' M r60.py'}))):
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
    res['pass'] = bool(res['i_ok'] and res['ii_ok'] and res['iii_ok'] and res['iv_ok'] and res['real_log_untouched'])
    json.dump(res, open(os.path.join(OUT, 'f0_q2_selftest.json'), 'w'), indent=1, default=str)
    log(json.dumps({k: v for k, v in res.items() if k != 'direct_stats'}, default=str))


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fns = {'repro': repro, 'diag': diag, 'halves': halves, 'f1': f1, 'cv': cv, 'rotation': rotation,
           'q2_selftest': q2_selftest, 'q2_power': q2_power}
    if cmd not in fns:
        print(__doc__)
        return 1
    fns[cmd]()
    return 0


if __name__ == '__main__':
    sys.exit(main())
