"""r63: panel of alt tramos and the r62 evaluator adapted to it (PROTOCOL_R63 §2-§4).

`use()` swaps r62_eval's run_program / basket / folds for the r63 versions, so r62's Evaluator,
Archive, rotation placebo and SPA run unchanged on the alt panel:
* basket = mean over the assets *active* that day (eligible, or holding a position), not over
  every column: with hundreds of tramos listed at different times a plain column mean would dilute
  the book by the assets that do not exist yet;
* folds = year (2020-2024) x 3 fixed symbol groups (sha1 of the symbol, mod 3).
"""
import hashlib
import math
import os

import numpy as np

import r59  # noqa: F401  (installs the r59 holdout guard)
import r62_dsl as dsl
import r62_eval as ev
import r63
import r63_data as rd
import r63_dsl as d63

HERE = os.path.dirname(os.path.abspath(__file__))
DAY, HOUR = dsl.DAY, dsl.HOUR
START_MS = 1_577_836_800_000          # 2020-01-01: the development window (§2)
YEARS = range(2020, 2025)
N_GROUPS = 3
SEED = 63


def group_of_sym(sym):
    return int(hashlib.sha1(sym.encode()).hexdigest()[:8], 16) % N_GROUPS


def sym_of(name):
    return name.split('#')[0]


def daily_bars(h):
    """UTC-day bars [t, o, h, l, c, vol, qvol, taker] from an hourly tramo (partial edge days kept)."""
    day = h[:, 0].astype(np.int64) // DAY * DAY
    u, start = np.unique(day, return_index=True)
    stop = np.r_[start[1:], len(h)]
    out = np.zeros((len(u), 8))
    out[:, 0] = u
    out[:, 1] = h[start, 1]
    out[:, 2] = np.maximum.reduceat(h[:, 2], start)
    out[:, 3] = np.minimum.reduceat(h[:, 3], start)
    out[:, 4] = h[stop - 1, 4]
    for c in (5, 6, 7):
        out[:, c] = np.add.reduceat(h[:, c], start)
    return out


def tramo_src(x):
    """{name_suffix: dict} for every tramo of one loaded symbol (r63_data.load output)."""
    out = {}
    for k, g in enumerate(x['tramos']):
        di = (g[:, 0].astype(np.int64) // DAY * DAY - x['days'][0]) // DAY
        elig_h, med_h = x['elig'][di], x['med'][di]
        d1 = daily_bars(g)
        dd = (d1[:, 0].astype(np.int64) - x['days'][0]) // DAY
        delisted = int(g[-1, 0]) < rd.DELIST_BEFORE_MS
        out[k] = {'h1': g, 'd1': d1, 'funding': x['funding'] if len(x['funding']) else None,
                  'elig_h': elig_h, 'slip_h': rd.slip_of(med_h),
                  'elig_d': x['elig'][dd], 'slip_d': rd.slip_of(x['med'][dd]),
                  'end_slip': rd.DELIST_SLIP if delisted else 0.0, 'delisted': delisted}
    return out


def load_src(syms, loader=rd.load):
    src = {}
    for s in syms:
        x = loader(s)
        if x is None:
            continue
        for k, v in tramo_src(x).items():
            src[f'{s}#{k}'] = v
    return src


def btc_t90():
    st = np.load(os.path.join(HERE, 'data', 'r55', 'f0_states.npy'))
    return st[:, 0].astype(np.int64), st[:, 2]


class AltPanel:
    """Lazily built AltAssets per (tramo, tf); `src` may be real or synthetic (same layout)."""

    def __init__(self, src, t90=None):
        self.src = src
        self.btc_t90 = t90 if t90 is not None else btc_t90()
        self.group = {n: group_of_sym(sym_of(n)) for n in src}
        self._a = {}

    def names(self):
        return sorted(self.src)

    def asset(self, name, tf):
        key = (name, tf)
        if key not in self._a:
            s = self.src[name]
            bars = s['h1'] if tf == '1h' else s['d1']
            elig, slip = (s['elig_h'], s['slip_h']) if tf == '1h' else (s['elig_d'], s['slip_d'])
            a = d63.AltAsset(name, bars, tf, s['funding'], self.btc_t90, elig, slip, s['end_slip'])
            a.du, a.dinv = np.unique(a.day, return_inverse=True)
            # a day is "active" for the basket when the asset could open a position that day
            a.elig_day = np.zeros(len(a.du), bool)
            np.logical_or.at(a.elig_day, a.dinv, a.elig)
            self._a[key] = a
        return self._a[key]


def run_program(q, panel, cost_mult=1.0, cross=dsl.CROSS, rot=None, names=None):
    """Per-tramo daily returns {name: (days, rets)} on its active days, trades and unfilled count."""
    tf, assets = dsl.UNIVERSES[q['universe']]
    out, trades, unfilled = {}, {}, 0
    for name in names or assets:
        a = panel.asset(name, tf)
        e, d = d63.entry_events(a, q)
        if rot is not None:
            e, d = ev.rotate(a, e, d, rot)
            e &= a.elig
        e &= a.t >= START_MS
        br, tr, uf = d63.simulate(a, q, e, d, cost_mult, cross)
        r = np.bincount(a.dinv, weights=br, minlength=len(a.du))
        keep = (a.du >= START_MS) & (a.elig_day | (r != 0))
        out[name] = (a.du[keep], r[keep])
        trades[name] = tr
        unfilled += uf
    return out, trades, unfilled


def basket(per_asset):
    """Mean of the active assets' daily returns per UTC day (0 on a day with none active)."""
    parts = [x for x in per_asset.values() if len(x[0])]
    if not parts:
        return np.zeros(0, np.int64), np.zeros(0)
    days = np.concatenate([x[0] for x in parts])
    rets = np.concatenate([x[1] for x in parts])
    u, inv = np.unique(days, return_inverse=True)
    s = np.bincount(inv, weights=rets, minlength=len(u))
    n = np.bincount(inv, minlength=len(u))
    return u, s / np.maximum(n, 1)


def _year(ms):
    return np.asarray(ms, np.int64).astype('datetime64[ms]').astype('datetime64[Y]').astype(int) + 1970


def folds(per_asset, trades, panel, tf):
    """Year x symbol-group Sharpe of the group basket, with the trades entered in the fold."""
    out = {}
    by_g = {}
    for name in per_asset:
        by_g.setdefault(panel.group[name], []).append(name)
    for g in range(N_GROUPS):
        names = by_g.get(g, [])
        days, r = basket({n: per_asset[n] for n in names})
        yrs = _year(days)
        ty = [_year(panel.asset(n, tf).t[[x[1] for x in trades[n]]]) for n in names if trades[n]]
        ty = np.concatenate(ty) if ty else np.zeros(0, int)
        for y in YEARS:
            k = yrs == y
            out[f'g{g}:{y}'] = {'sharpe': ev.sharpe(r[k]) if k.sum() > 20 else float('nan'),
                                'trades': int((ty == y).sum())}
    return out


def use():
    """Route r62_eval's module functions to the r63 versions (Evaluator/rotation then use them)."""
    ev.run_program, ev.basket, ev.folds = run_program, basket, folds


def evaluator(src, names=None):
    """r62 Evaluator over an AltPanel, with the dsl tables pointed at `names` (default: all tramos)."""
    use()
    P = AltPanel(src)
    d63.configure(names or P.names())
    return ev.Evaluator(P, ev.load_bench('BENCH_P55_long'), ev.load_bench('BENCH_R1_long'))


def rot_p(E, q, mapper=None):
    """§4 e3 with the r63 seed."""
    return E.rotation_p(q, seed=SEED, mapper=mapper)


def dev_syms():
    return r63.load_partition()['D63']


def local_syms():
    return r63.load_partition()['L63']


def bar_sharpe_ann(r):
    r = np.asarray(r, float)
    return float(r.mean() / r.std(ddof=1) * math.sqrt(365)) if len(r) > 20 and r.std() > 0 else float('nan')
