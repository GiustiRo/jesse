"""r62: evaluator of DSL programs (PROTOCOL_R62 §3) and the fast SPA used by the funnel (§7.3).

score = Sharpe of the worst valid group x year fold - LAMBDA * complexity
eligible = e1 (costs x2 Sharpe > 0) and e2 (P55 + 15% marginal > 0) and e3 (rotation p < 0.10)
"""
import json
import math
import os

import numpy as np

import r62_dsl as dsl

HERE = os.path.dirname(os.path.abspath(__file__))
DAY = dsl.DAY
LAMBDA = 0.05                        # §3: score penalty per unit of complexity
MIN_FOLD_TRADES, MIN_FOLDS = 10, 5
W_MARG = 0.15                        # §3 e2 / §7.3: weight of the program next to P-r55
N_ROT, ROT_MIN_DAYS, ROT_P = 200, 90, 0.10
SEED = 62
YEARS = {'crypto': range(2020, 2025), 'commod': range(2019, 2025), 'eqbond': range(2019, 2025)}
WINDOW_FROM = {'crypto': 1_577_836_800_000, 'cfd': 1_538_352_000_000}   # 2020-01-01 / 2018-10-01


def sharpe(r):
    r = np.asarray(r, float)
    r = r[np.isfinite(r)]
    if len(r) < 20 or r.std(ddof=1) == 0:
        return float('nan')
    return float(r.mean() / r.std(ddof=1) * math.sqrt(365))


# ----------------------------------------------------------------------------------------------
# Panel: Asset objects per universe, built once per data source (real or synthetic)
# ----------------------------------------------------------------------------------------------
class Panel:
    """Assets keyed by name for '1h' and '1d', plus pair spreads; `src` maps name -> bars dict
    ({'h1','d1'[,'funding']}) so synthetic histories plug in the same way as real ones."""

    def __init__(self, src, btc_t90=None, oi=None):
        self.src, self.btc_t90, self.oi = src, btc_t90, oi or {}
        self._a = {}

    def asset(self, name, tf):
        key = (name, tf)
        if key not in self._a:
            if isinstance(name, tuple):
                self._a[key] = self._pair(name)
            else:
                s = self.src[name]
                bars = s['h1'] if tf == '1h' else s['d1']
                f = s.get('funding')
                oi = None
                if tf == '1h' and name in self.oi:
                    ht, z = self.oi[name]
                    idx = np.searchsorted(ht, bars[:, 0].astype(np.int64) + dsl.HOUR)
                    ok = (idx < len(ht)) & (ht[np.clip(idx, 0, len(ht) - 1)] == bars[:, 0] + dsl.HOUR)
                    oi = np.where(ok, z[np.clip(idx, 0, len(ht) - 1)], np.nan)
                self._a[key] = dsl.Asset(name, bars, tf, funding=f, oi=oi, btc_t90=self.btc_t90)
        return self._a[key]

    def _pair(self, pair):
        """Equal-vol log-spread on the common hourly stamps; O=H=L=C so pairs trade close to close."""
        a, b = (self.src[n]['h1'] for n in pair)
        ta, tb = a[:, 0].astype(np.int64), b[:, 0].astype(np.int64)
        common = np.intersect1d(ta, tb)
        ca = a[np.searchsorted(ta, common), 4]
        cb = b[np.searchsorted(tb, common), 4]
        ra, rb = np.r_[0, np.diff(np.log(ca))], np.r_[0, np.diff(np.log(cb))]
        sa, sb = dsl.rolling_std(ra, dsl.VOL_WIN), dsl.rolling_std(rb, dsl.VOL_WIN)
        # weights from sigma known at the previous close (no look-ahead into the bar's return)
        wa, wb = 1 / np.r_[np.nan, sa[:-1]], 1 / np.r_[np.nan, sb[:-1]]
        tot = wa + wb
        rs = np.nan_to_num((wa * ra - wb * rb) / tot)
        px = np.exp(np.cumsum(rs))
        bars = np.c_[common, px, px, px, px, np.zeros(len(common))]
        return dsl.Asset(pair, bars, '1h', btc_t90=self.btc_t90)


def group_of(name):
    n = name[0] if isinstance(name, tuple) else name
    return 'crypto' if n.endswith('USDT') else dsl.GROUP[n]       # alts of the q4 bank are crypto


# ----------------------------------------------------------------------------------------------
# Run one program
# ----------------------------------------------------------------------------------------------
def run_program(q, panel, cost_mult=1.0, cross=dsl.CROSS, rot=None, names=None):
    """Per-asset daily returns {name: (days, rets)} and trades; `rot` circularly shifts the entry
    events by a fraction of each asset's span (§3 e3); `names` overrides the universe's assets."""
    tf, assets = dsl.UNIVERSES[q['universe']]
    out, trades, unfilled = {}, {}, 0
    for name in names or assets:
        a = panel.asset(name, tf)
        ev, d = dsl.entry_events(a, q)
        if rot is not None:
            ev, d = rotate(a, ev, d, rot)
        start = WINDOW_FROM['crypto' if group_of(name) == 'crypto' else 'cfd']
        ev &= a.t >= start
        br, tr, uf = dsl.simulate(a, q, ev, d, cost_mult, cross)
        days, r = dsl.daily(a, br)
        keep = days >= start
        out[name] = (days[keep], r[keep])
        trades[name] = tr
        unfilled += uf
    return out, trades, unfilled


def rotate(a, ev, d, frac):
    """Shift event stamps by `frac` of the asset's span (wrapping), keeping each event's direction."""
    t = a.t
    span = t[-1] - t[0]
    idx = np.flatnonzero(ev)
    nt = t[0] + (t[idx] - t[0] + int(frac * span)) % span
    j = np.clip(np.searchsorted(t, nt), 0, len(t) - 1)
    ev2, d2 = np.zeros_like(ev), np.zeros_like(d)
    ev2[j] = True
    d2[j] = d[idx]
    return ev2, d2


def basket(per_asset):
    """Equal-weight average of the assets' daily returns on the union of UTC days (0 when absent)."""
    days = np.unique(np.concatenate([d for d, _ in per_asset.values()]))
    m = np.zeros((len(days), len(per_asset)))
    for i, (d, r) in enumerate(per_asset.values()):
        m[np.searchsorted(days, d), i] = r
    return days, m.mean(1)


def folds(per_asset, trades, panel, tf):
    """Group x year Sharpe of the group basket, with the number of trades entered in the fold."""
    out = {}
    groups = {}
    for name in per_asset:
        groups.setdefault(group_of(name), []).append(name)
    for g, names in groups.items():
        days, r = basket({n: per_asset[n] for n in names})
        yrs = (days // DAY * DAY).astype('datetime64[ms]').astype('datetime64[Y]').astype(int) + 1970
        tr_years = []
        for n in names:
            a = panel.asset(n, tf)
            tr_years += [int(np.datetime64(int(a.t[x[1]]), 'ms').astype('datetime64[Y]').astype(int) + 1970)
                         for x in trades[n]]
        tr_years = np.array(tr_years)
        for y in YEARS[g]:
            k = yrs == y
            nt = int((tr_years == y).sum()) if len(tr_years) else 0
            out[f'{g}:{y}'] = {'sharpe': sharpe(r[k]) if k.sum() > 20 else float('nan'), 'trades': nt}
    return out


def score_of(fl, q):
    valid = [v['sharpe'] for v in fl.values() if v['trades'] >= MIN_FOLD_TRADES and np.isfinite(v['sharpe'])]
    if len(valid) < MIN_FOLDS:
        return -math.inf, len(valid)
    return float(min(valid) - LAMBDA * dsl.complexity(q)), len(valid)


def align(days, r, bdays, br):
    """Values of (days, r) on bench days, 0 where the program has no day (flat)."""
    out = np.zeros(len(bdays))
    i = np.searchsorted(days, bdays)
    ok = (i < len(days)) & (days[np.clip(i, 0, len(days) - 1)] == bdays)
    out[ok] = r[np.clip(i, 0, len(days) - 1)[ok]]
    return out


def marginal(x, p55):
    """e2: Sharpe(0.85 P55 + 0.15 x~) - Sharpe(P55), x~ scaled to P55's vol, on P55's days."""
    if x.std() == 0:
        return float('nan')
    xs = x * p55.std() / x.std()
    return sharpe((1 - W_MARG) * p55 + W_MARG * xs) - sharpe(p55)


def descriptors(q, per_asset, trades, panel, r1):
    """MAP-Elites axes: rho with R1, mean holding (days), direction of net/gross exposure."""
    tf = dsl.UNIVERSES[q['universe']][0]
    bpd = 24 if tf == '1h' else 1
    hold, net, gross = [], 0.0, 0.0
    for n, tr in trades.items():
        for (_, j, k, dr, sz, *_r) in tr:
            hold.append((k - j + 1) / bpd)
            net += dr * sz * (k - j + 1)
            gross += sz * (k - j + 1)
    return {'rho_r1': float(np.corrcoef(*r1)[0, 1]) if np.std(r1[0]) > 0 else 0.0,
            'hold_days': float(np.mean(hold)) if hold else 0.0,
            # a pair is dollar-neutral whichever leg it is long, so it is always 'neutral'
            'dir': 0.0 if dsl._is_pair(q['universe']) or not gross else float(net / gross)}


def cell_of(desc):
    rho = desc['rho_r1']
    a = 0 if rho < 0.1 else 1 if rho <= 0.3 else 2
    h = desc['hold_days']
    b = 0 if h < 1 else 1 if h <= 5 else 2
    x = desc['dir']
    c = 'long' if x > 0.33 else 'short' if x < -0.33 else 'neutral'
    return f'rho{a}|hold{b}|{c}'


def blocked(cell):
    return cell.startswith('rho2') and cell.endswith('long')


class Evaluator:
    """Holds the panel and the benches; `evaluate(q)` gives the full record (no rotation), and
    `rotation_p(q)` the e3 placebo for programs that would win their cell."""

    def __init__(self, panel, p55, r1):
        self.panel, self.p55, self.r1 = panel, p55, r1          # (days, rets) each

    def evaluate(self, q):
        q = dsl.validate(q)
        tf = dsl.UNIVERSES[q['universe']][0]
        per, tr, uf = run_program(q, self.panel)
        days, r = basket(per)
        fl = folds(per, tr, self.panel, tf)
        sc, nvalid = score_of(fl, q)
        x = align(days, r, *self.p55)
        x1 = align(days, r, *self.r1)
        per2, _, _ = run_program(q, self.panel, cost_mult=2.0, cross=2 * dsl.CROSS)
        d2, r2 = basket(per2)
        n_tr = sum(len(v) for v in tr.values())
        pnl = np.array([_trade_pnl(t) for v in tr.values() for t in v])
        top5 = float(np.sort(pnl)[-5:].sum() / pnl.sum()) if len(pnl) >= 5 and pnl.sum() > 0 else float('nan')
        desc = descriptors(q, per, tr, self.panel, (x1, self.r1[1]))
        rec = {'hash': dsl.phash(q), 'program': q, 'score': sc, 'n_valid_folds': nvalid, 'folds': fl,
               'sharpe': sharpe(r), 'sharpe_cost2': sharpe(r2), 'marginal': marginal(x, self.p55[1]),
               'trades': n_tr, 'unfilled': uf, 'top5_share': top5, 'complexity': dsl.complexity(q),
               'desc': desc, 'cell': cell_of(desc)}
        rec['e1'] = bool(np.isfinite(rec['sharpe_cost2']) and rec['sharpe_cost2'] > 0)
        rec['e2'] = bool(np.isfinite(rec['marginal']) and rec['marginal'] > 0)
        rec['series'] = (days, r)
        return rec

    def rotation_p(self, q, n_rot=N_ROT, seed=SEED):
        q = dsl.validate(q)
        per, _, _ = run_program(q, self.panel)
        obs = sharpe(basket(per)[1])
        rng = np.random.default_rng(seed)
        span_days = 365 * 4.5
        lo = ROT_MIN_DAYS / span_days
        null = []
        for _ in range(n_rot):
            f = rng.uniform(lo, 1 - lo)
            pr, _, _ = run_program(q, self.panel, rot=f)
            null.append(sharpe(basket(pr)[1]))
        null = np.nan_to_num(np.array(null), nan=-np.inf)
        return float((1 + (null >= obs).sum()) / (1 + n_rot)), obs


def _trade_pnl(t):
    (_, j, k, dr, sz, pin, pout, fin, fout, _) = t
    return dr * sz * (pout / pin - 1) - sz * (fin + fout)


# ----------------------------------------------------------------------------------------------
# Fast SPA (same statistic as r59.spa_pvalue; bootstrap means through a counts matrix)
# ----------------------------------------------------------------------------------------------
def spa_fast(G, n_boot=2000, seed=SEED, block=20):
    """Hansen SPA_c p-value for H0: no column of G has a positive mean. Identical resampling to
    r59.spa_pvalue (same rng stream through r59.stationary_idx) but O(n_boot * n * k) via BLAS."""
    import r59
    G = G[np.isfinite(G).all(1)]
    n = len(G)
    rng = np.random.default_rng(seed)
    cnt = np.zeros((n_boot, n), dtype=np.float32 if G.shape[1] > 500 else float)
    for b in range(n_boot):
        np.add.at(cnt[b], r59.stationary_idx(n, rng, block), 1.0)
    gb = (cnt @ G) / n
    gbar = G.mean(0)
    sd = gb.std(0)
    omega = np.sqrt(n) * sd
    omega = np.where(omega > 0, omega, 1e-12)
    tstat = np.sqrt(n) * gbar / omega
    T = max(float(tstat.max()), 0.0)
    very_neg = tstat < -np.sqrt(2 * np.log(np.log(n)))
    Tb = np.maximum((np.sqrt(n) * (gb - gbar + gbar * very_neg) / omega).max(1), 0.0)
    return float((Tb >= T).mean()), int(np.argmax(gbar / np.where(sd > 0, sd, 1e-12))), Tb, tstat


def load_bench(tid):
    import r59
    d, r = r59.load_series(tid)
    return np.asarray(d, np.int64), np.asarray(r, float)


def real_panel(with_oi=True):
    import r62_data
    src = {n: r62_data.load(n) for n in r62_data.CORE + r62_data.VALID + list(r62_data.ETF)}
    st = np.load(os.path.join(HERE, 'data', 'r55', 'f0_states.npy'))
    btc_t90 = (st[:, 0].astype(np.int64), st[:, 2])       # applied day -> T90 (r55 states_b)
    oi = {}
    if with_oi:
        for n, sym in (('BTC', 'BTCUSDT'), ('ETH', 'ETHUSDT')):
            p = os.path.join(HERE, 'data', 'r62', f'oi_{sym}.npz')
            if os.path.exists(p):
                z = np.load(p)
                oi[n] = (z['ht'], z['z_doi'])
    return Panel(src, btc_t90, oi)


def cascade_gate():
    p = os.path.join(HERE, 'data', 'r62', 'liq_f0.json')
    if not os.path.exists(p):
        return False
    with open(p) as f:
        return bool(json.load(f).get('cascade_enabled'))
