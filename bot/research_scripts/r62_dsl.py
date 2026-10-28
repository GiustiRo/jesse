"""r62: bounded strategy language and its vectorised engine (PROTOCOL_R62 §2).

A program is a small JSON document; every piece and parameter must come from CATALOG, so each
evaluated program is one countable trial (no free Python). `run(program, panel)` returns per-asset
daily returns, the trade list and diagnostics; the evaluator (r62_eval) turns them into a score.

Causality: every signal and filter at bar t uses data up to the close of t; entries happen at t+1
or later (taker: next open; maker: a resting limit that must be crossed by a later bar).
"""
import copy
import hashlib
import json
import math

import numpy as np

T, O, H, L, C, V = range(6)
HOUR, DAY = 3_600_000, 86_400_000
VOL_WIN = 720                        # bars of causal sigma for z-scores (30 days of 1h bars)
TARGET_VOL = 0.10                    # §2 `voltgt`: 10% annual per asset while in a trade
MAX_LEV = 2.0                        # cap on the per-trade notional / equity
MAX_PIECES, MAX_PARAMS = 4, 6
TAKER_FEE, MAKER_FEE = 0.00045, 0.00018
CRYPTO_SLIP = 5e-4                   # §2: 5 bp per taker side on BTC/ETH perps
# r50_engines.SLIP_BPS for the thin Binance TradFi books; 2 bp for the rest of the CFDs.
CFD_SLIP = {'BOND': 15e-4, 'GAS': 5e-4, 'COPPER': 5e-4}
DEFAULT_CFD_SLIP = 2e-4
CROSS = 1e-4                         # a resting limit fills only if a later bar trades 1 bp through it
CRYPTO = ('BTC', 'ETH')
GROUP = {'BTC': 'crypto', 'ETH': 'crypto', 'XAU': 'commod', 'WTI': 'commod', 'GAS': 'commod',
         'SPX': 'eqbond', 'BOND': 'eqbond',
         # validation assets (transfer only, §7.3.5)
         'XAG': 'commod', 'COPPER': 'commod', 'NDX': 'eqbond', 'DEU': 'eqbond',
         'EWJ': 'eqbond', 'EWY': 'eqbond'}

UNIVERSES = {
    'core_1h': ('1h', ['BTC', 'ETH', 'XAU', 'SPX', 'WTI', 'GAS', 'BOND']),
    'core_1d': ('1d', ['BTC', 'ETH', 'XAU', 'SPX', 'WTI', 'GAS', 'BOND']),
    'crypto_1h': ('1h', ['BTC', 'ETH']),
    'cfd_1h': ('1h', ['XAU', 'SPX', 'WTI', 'GAS', 'BOND']),
    'pair_BTC_ETH': ('1h', [('BTC', 'ETH')]),
    'pair_WTI_GAS': ('1h', [('WTI', 'GAS')]),
    'pair_SPX_BOND': ('1h', [('SPX', 'BOND')]),
    'pair_XAU_SPX': ('1h', [('XAU', 'SPX')]),
}

# kind -> {param: grid}; `only` restricts where a piece is legal.
SIGNALS = {
    'zrev': {'k': [6, 24, 72], 'z': [1.5, 2.0, 2.5]},
    'rsi2': {'th': [5, 10, 20]},
    'shock': {'z': [2, 3, 4], 'mode': ['fade', 'follow']},
    'spread_z': {'k': [24, 120, 480], 'z': [1.5, 2.0, 2.5]},
    'voljump': {'ratio': [1.5, 2.0, 3.0], 'mode': ['fade', 'follow']},
    'clock': {'event': ['funding_hour', 'cme_gap', 'month_end'], 'mode': ['fade', 'follow']},
    'cascade': {'z_oi': [2, 3], 'z_ret': [2, 3], 'mode': ['fade', 'follow']},
}
FILTERS = {
    'volreg': {'band': ['low', 'mid', 'high']},
    'trendveto': {'k': [20, 60]},
    'session': {'s': ['asia', 'europe', 'us']},
    'btcstate': {'state': ['up', 'flat', 'down']},
}
EXITS = {
    'time': {'h': [1, 6, 24, 72, 120]},
    'atr': {'tgt': [1, 2], 'stop': [1, 2, 3]},
    'mean': {},
}
SIZES = {'voltgt': {'side': ['both', 'long', 'short']}}
EXECS = {'taker': {}, 'maker': {'off': [0.25, 0.5, 1.0], 'life': [1, 3, 6]}}
ATR_CAP, MEAN_CAP = 120, 72
CONFIRM_BARS = 6                     # second signal must have fired within this many bars
SESSIONS = {'asia': (0, 8), 'europe': (7, 15), 'us': (13, 21)}
CASCADE_ENABLED = None               # set by r62_eval from data/r62/liq_f0.json (§6.5)


class DslError(ValueError):
    pass


def _is_pair(universe):
    return universe.startswith('pair_')


def validate(p):
    """Raise DslError unless `p` uses only catalogue pieces/values; returns a normalised copy."""
    if not isinstance(p, dict) or set(p) - {'universe', 'signal', 'filters', 'exit', 'size', 'exec'}:
        raise DslError('unknown top-level keys')
    q = copy.deepcopy(p)
    q.setdefault('filters', [])
    q.setdefault('size', {'kind': 'voltgt', 'params': {'side': 'both'}})
    if q.get('universe') not in UNIVERSES:
        raise DslError(f'universe {q.get("universe")!r}')
    tf = UNIVERSES[q['universe']][0]
    pair = _is_pair(q['universe'])

    def piece(x, table, what):
        if not isinstance(x, dict) or x.get('kind') not in table:
            raise DslError(f'{what}: unknown kind {x!r}')
        prm = x.get('params', {}) or {}
        if set(prm) != set(table[x['kind']]):
            raise DslError(f'{what} {x["kind"]}: params {sorted(prm)} != {sorted(table[x["kind"]])}')
        for k, v in prm.items():
            if v not in table[x['kind']][k]:
                raise DslError(f'{what} {x["kind"]}.{k}={v!r} not in grid')
        return {'kind': x['kind'], 'params': {k: prm[k] for k in sorted(prm)}}

    if not isinstance(q.get('signal'), list) or not 1 <= len(q['signal']) <= 2:
        raise DslError('signal must hold 1-2 pieces')
    if not isinstance(q['filters'], list) or len(q['filters']) > 2:
        raise DslError('filters must hold 0-2 pieces')
    q['signal'] = [piece(s, SIGNALS, 'signal') for s in q['signal']]
    q['filters'] = sorted((piece(f, FILTERS, 'filter') for f in q['filters']),
                          key=lambda f: json.dumps(f, sort_keys=True))
    q['exit'] = piece(q.get('exit'), EXITS, 'exit')
    q['size'] = piece(q['size'], SIZES, 'size')
    q['exec'] = piece(q.get('exec'), EXECS, 'exec')
    kinds = [s['kind'] for s in q['signal']]
    if len(set(kinds)) != len(kinds):
        raise DslError('duplicate signal kind')
    if len({f['kind'] for f in q['filters']}) != len(q['filters']):
        raise DslError('duplicate filter kind')
    if ('spread_z' in kinds) != pair:
        raise DslError('spread_z is the (only) signal family of pair universes')
    if pair and len(kinds) > 1:
        raise DslError('pair universes take spread_z alone')
    if pair and q['exec']['kind'] != 'taker':
        # Two legs cannot be filled as one resting order; the spread has no intrabar range.
        raise DslError('pairs execute taker')
    if tf == '1d':
        bad = {'clock', 'cascade'} & set(kinds) or {'session'} & {f['kind'] for f in q['filters']}
        if bad:
            raise DslError(f'{sorted(bad)} need 1h bars')
    if 'cascade' in kinds:
        if q['universe'] != 'crypto_1h':
            raise DslError('cascade is crypto_1h only')
        if CASCADE_ENABLED is False:
            raise DslError('cascade disabled by the F0 data gate')
    if any(s['kind'] == 'clock' and s['params']['event'] in ('funding_hour', 'cme_gap') for s in q['signal']) \
            and q['universe'] != 'crypto_1h':
        raise DslError('funding_hour/cme_gap are crypto_1h only')
    n_pieces = len(q['signal']) + len(q['filters']) + 1 + 1        # + exit + size
    if n_pieces > MAX_PIECES + 1:                                    # size is mandatory, not counted
        raise DslError('too many pieces')
    if n_params(q) > MAX_PARAMS:
        raise DslError('too many params')
    return q


def n_params(q):
    return sum(len(x['params']) for x in q['signal'] + q['filters'] + [q['exit'], q['exec']])


def complexity(q):
    """§2: pieces (signals + filters + exit) + parameters; size and exec kind are not pieces."""
    return len(q['signal']) + len(q['filters']) + 1 + n_params(q)


def canon(q):
    return json.dumps(validate(q), sort_keys=True, separators=(',', ':'))


def phash(q):
    return hashlib.sha1(canon(q).encode()).hexdigest()


def random_program(rng, universe=None):
    """A uniformly drawn legal program (used for the seeds and the 'swap a piece' operator)."""
    for _ in range(1000):
        u = universe or rng.choice(sorted(UNIVERSES))
        tf = UNIVERSES[u][0]
        if _is_pair(u):
            sig = [{'kind': 'spread_z', 'params': _draw(SIGNALS['spread_z'], rng)}]
        else:
            pool = [k for k in SIGNALS if k != 'spread_z' and (tf == '1h' or k not in ('clock', 'cascade'))]
            ks = list(rng.choice(pool, size=1 + int(rng.random() < 0.25), replace=False))
            sig = [{'kind': k, 'params': _draw(SIGNALS[k], rng)} for k in ks]
        fpool = [k for k in FILTERS if tf == '1h' or k != 'session']
        nf = int(rng.choice([0, 0, 1, 1, 2]))
        fl = [{'kind': k, 'params': _draw(FILTERS[k], rng)} for k in rng.choice(fpool, size=nf, replace=False)]
        ex = rng.choice(sorted(EXITS))
        ec = 'taker' if _is_pair(u) else rng.choice(sorted(EXECS))
        p = {'universe': u, 'signal': sig, 'filters': fl,
             'exit': {'kind': ex, 'params': _draw(EXITS[ex], rng)},
             'size': {'kind': 'voltgt', 'params': {'side': str(rng.choice(SIZES['voltgt']['side']))}},
             'exec': {'kind': ec, 'params': _draw(EXECS[ec], rng)}}
        try:
            return validate(p)
        except DslError:
            continue
    raise RuntimeError('could not draw a legal program')


def _draw(table, rng):
    out = {}
    for k, grid in table.items():
        v = grid[int(rng.integers(len(grid)))]
        out[k] = v.item() if hasattr(v, 'item') else v
    return out


# ----------------------------------------------------------------------------------------------
# Indicators (causal)
# ----------------------------------------------------------------------------------------------
def rolling_std(x, w, minp=None):
    """Std of x[t-w+1..t] (inclusive of t), NaN until `minp` finite values."""
    minp = minp or w // 2
    x = np.asarray(x, float)
    f = np.isfinite(x)
    xs = np.where(f, x, 0.0)
    c1, c2, cn = (np.r_[0, np.cumsum(a)] for a in (xs, xs * xs, f.astype(float)))
    n = len(x)
    i = np.arange(n)
    lo = np.maximum(i - w + 1, 0)
    s1, s2, k = c1[i + 1] - c1[lo], c2[i + 1] - c2[lo], cn[i + 1] - cn[lo]
    with np.errstate(invalid='ignore', divide='ignore'):
        var = (s2 - s1 * s1 / k) / (k - 1)
    out = np.sqrt(np.maximum(var, 0))
    out[k < minp] = np.nan
    return out


def rolling_mean(x, w, minp=None):
    minp = minp or w // 2
    x = np.asarray(x, float)
    f = np.isfinite(x)
    c1, cn = np.r_[0, np.cumsum(np.where(f, x, 0.0))], np.r_[0, np.cumsum(f)]
    i = np.arange(len(x))
    lo = np.maximum(i - w + 1, 0)
    k = cn[i + 1] - cn[lo]
    with np.errstate(invalid='ignore', divide='ignore'):
        out = (c1[i + 1] - c1[lo]) / k
    out[k < minp] = np.nan
    return out


def _lag(x, k):
    out = np.full_like(x, np.nan, dtype=float)
    if k < len(x):
        out[k:] = x[:-k] if k else x
    return out


def _onset(cond):
    """True on the first bar of each run of `cond` (an entry event, not every bar in the zone)."""
    c = np.asarray(cond, bool)
    return c & ~np.r_[False, c[:-1]]


class Asset:
    """Bars of one tradable (or a synthetic pair spread) plus the causal features the pieces read."""

    def __init__(self, name, bars, tf, funding=None, oi=None, btc_t90=None, hourly_for_days=None):
        self.name, self.tf = name, tf
        self.b = np.asarray(bars, float)
        self.t = self.b[:, T].astype(np.int64)
        c = self.b[:, C]
        self.lr = np.r_[np.nan, np.diff(np.log(c))]
        self.bpy = 365 * 24 if tf == '1h' else 365            # bars per year for annualising
        win = VOL_WIN if tf == '1h' else 30
        self.sig = _lag(rolling_std(self.lr, win), 0)           # includes bar t: known at its close
        tr = np.maximum(self.b[:, H], np.r_[np.nan, c[:-1]]) - np.minimum(self.b[:, L], np.r_[np.nan, c[:-1]])
        self.atr = rolling_mean(tr, 24 if tf == '1h' else 14)
        # daily sigma for sizing: annualised from the bar sigma
        self.sig_ann = self.sig * math.sqrt(self.bpy)
        self.funding = funding
        self.oi = oi
        self.btc_t90 = btc_t90
        self.hour = (self.t // HOUR) % 24
        self.day = self.t // DAY * DAY
        crypto = name in CRYPTO or (isinstance(name, str) and name.endswith('USDT'))
        self.slip = CRYPTO_SLIP if crypto else CFD_SLIP.get(name, DEFAULT_CFD_SLIP)
        self.is_pair = isinstance(name, tuple)
        if self.is_pair:
            self.slip = 2 * max(CFD_SLIP.get(n, CRYPTO_SLIP if n in CRYPTO else DEFAULT_CFD_SLIP) for n in name)
        self._cache = {}

    def bars_per_day(self):
        return 24 if self.tf == '1h' else 1

    def vol_tercile(self):
        """§2 `volreg`: tercile (0/1/2) of the 30-day vol among the previous 365 daily values,
        computed on UTC days and applied from the next day on (causal); -1 when unknown."""
        if 'volt' not in self._cache:
            du, inv = np.unique(self.day, return_inverse=True)
            dr = np.zeros(len(du))
            np.add.at(dr, inv, np.nan_to_num(self.lr))
            s30 = rolling_std(dr, 30, minp=20)
            terc = np.full(len(du), -1)
            for i in range(200, len(du)):
                h = s30[max(0, i - 365):i]
                h = h[np.isfinite(h)]
                if len(h) >= 180 and np.isfinite(s30[i]):
                    lo, hi = np.quantile(h, [1 / 3, 2 / 3])
                    terc[i] = 0 if s30[i] < lo else 2 if s30[i] > hi else 1
            # the day's tercile is known at its close: it applies to the next day's bars
            self._cache['volt'] = np.r_[-1, terc[:-1]][inv]
        return self._cache['volt']

    def z_ret(self, k):
        key = ('zret', k)
        if key not in self._cache:
            c = np.log(self.b[:, C])
            self._cache[key] = (c - _lag(c, k)) / (self.sig * math.sqrt(k))
        return self._cache[key]


# ----------------------------------------------------------------------------------------------
# Pieces -> (events, direction)
# ----------------------------------------------------------------------------------------------
def signal_events(a, s):
    """Boolean entry events and +1/-1 direction arrays for one signal piece."""
    k, p = s['kind'], s['params']
    n = len(a.t)
    d = np.zeros(n)
    if k == 'zrev':
        z = a.z_ret(p['k'])
        ev = _onset(np.abs(z) > p['z'])
        d = -np.sign(z)
    elif k == 'rsi2':
        dl = np.r_[np.nan, np.diff(a.b[:, C])]
        up = _ema(np.where(dl > 0, dl, 0.0), 2)
        dn = _ema(np.where(dl < 0, -dl, 0.0), 2)
        with np.errstate(invalid='ignore', divide='ignore'):
            rsi = 100 - 100 / (1 + up / dn)
        lo, hi = rsi < p['th'], rsi > 100 - p['th']
        ev = _onset(lo) | _onset(hi)
        d = np.where(lo, 1.0, np.where(hi, -1.0, 0.0))
    elif k == 'shock':
        z = a.lr / _lag(a.sig, 1)                # sigma before the bar, so the shock is not in it
        ev = np.abs(z) > p['z']
        d = np.sign(z) * (1 if p['mode'] == 'follow' else -1)
    elif k == 'spread_z':
        x = np.log(a.b[:, C])
        m, sd = rolling_mean(x, p['k']), rolling_std(x, p['k'])
        z = (x - m) / sd
        ev = _onset(np.abs(z) > p['z'])
        d = -np.sign(z)
    elif k == 'voljump':
        s24 = rolling_std(a.lr, 24 if a.tf == '1h' else 5)
        r = s24 / _lag(a.sig, 24 if a.tf == '1h' else 5)
        ev = _onset(r > p['ratio'])
        mv = np.log(a.b[:, C]) - _lag(np.log(a.b[:, C]), 24 if a.tf == '1h' else 5)
        d = np.sign(mv) * (1 if p['mode'] == 'follow' else -1)
    elif k == 'clock':
        ev, mv = _clock(a, p['event'])
        d = np.sign(mv) * (1 if p['mode'] == 'follow' else -1)
    elif k == 'cascade':
        if a.oi is None:
            return np.zeros(n, bool), d
        zr = a.lr / _lag(a.sig, 1)
        ev = (a.oi < -p['z_oi']) & (np.abs(zr) > p['z_ret'])
        d = np.sign(zr) * (1 if p['mode'] == 'follow' else -1)
    else:
        raise DslError(k)
    ev = np.asarray(ev, bool) & np.isfinite(d) & (d != 0)
    return ev, np.nan_to_num(d)


def _ema(x, n):
    a = 1.0 / n                                   # Wilder smoothing for RSI(2)
    out = np.empty_like(x, dtype=float)
    acc = np.nan
    for i, v in enumerate(x):
        if not np.isfinite(v):
            out[i] = acc
            continue
        acc = v if not np.isfinite(acc) else acc + a * (v - acc)
        out[i] = acc
    return out


def _clock(a, event):
    """Clock events at the close of a bar, with the prior move that sets the direction."""
    lc = np.log(a.b[:, C])
    close_t = a.t + HOUR                          # 1h bars only
    hr = (close_t // HOUR) % 24
    if event == 'funding_hour':
        ev = np.isin(hr, (0, 8, 16))
        mv = lc - _lag(lc, 8)
    elif event == 'cme_gap':
        wd = ((close_t // DAY) + 3) % 7           # 0 = Monday
        ev = (wd == 6) & (hr == 23)               # Sunday 23:00 UTC: CME has reopened
        mv = lc - _lag(lc, 50)                    # since Friday ~21:00 UTC
    elif event == 'month_end':
        d = close_t // DAY
        import datetime as _dt
        dates = [_dt.date(1970, 1, 1) + _dt.timedelta(days=int(x)) for x in d]
        nxt = [x + _dt.timedelta(days=1 + (2 if x.weekday() == 4 else 0)) for x in dates]
        last_wd = np.array([x.weekday() < 5 and n.month != x.month for x, n in zip(dates, nxt)])
        ev = last_wd & (hr == 15)
        mv = lc - _lag(lc, 24 * 5)
    else:
        raise DslError(event)
    return ev, mv


def filter_mask(a, f, d):
    """True where an entry with direction d is allowed by filter f."""
    k, p = f['kind'], f['params']
    n = len(a.t)
    if k == 'volreg':
        band = a.vol_tercile()
        return band == {'low': 0, 'mid': 1, 'high': 2}[p['band']]
    if k == 'trendveto':
        kb = p['k'] * a.bars_per_day()
        z = a.z_ret(kb)
        bad = (np.abs(z) > 1) & (np.sign(z) == -d)
        return ~bad & np.isfinite(z)
    if k == 'session':
        lo, hi = SESSIONS[p['s']]
        return (a.hour >= lo) & (a.hour < hi)
    if k == 'btcstate':
        if a.btc_t90 is None:
            return np.zeros(n, bool)
        days, t90 = a.btc_t90
        idx = np.searchsorted(days, a.day, side='right') - 1
        v = np.where(idx >= 0, t90[np.clip(idx, 0, None)], np.nan)
        st = np.where(v >= 0.5, 'up', np.where(v <= -0.5, 'down', 'flat'))
        return (st == p['state']) & np.isfinite(v)
    raise DslError(k)


# ----------------------------------------------------------------------------------------------
# Execution and P&L
# ----------------------------------------------------------------------------------------------
def entry_events(a, q):
    ev, d = signal_events(a, q['signal'][0])
    for s in q['signal'][1:]:
        # two signals: the second must have fired in the same direction within the last
        # CONFIRM_BARS bars (same-bar coincidence of two onset events is too rare to be useful)
        e, dd = signal_events(a, s)
        recent = np.zeros(len(e))
        for lag in range(CONFIRM_BARS):
            recent += _lag(np.where(e, dd, 0.0), lag) if lag else np.where(e, dd, 0.0)
        ev = ev & (np.sign(np.nan_to_num(recent)) == np.sign(d)) & (np.nan_to_num(recent) != 0)
    side = q['size']['params']['side']
    if side == 'long':
        ev &= d > 0
    elif side == 'short':
        ev &= d < 0
    for f in q['filters']:
        ev &= filter_mask(a, f, d)
    ev &= np.isfinite(a.sig) & np.isfinite(a.atr)
    return ev, d


def simulate(a, q, ev, d, cost_mult=1.0, cross=CROSS):
    """Non-overlapping trades from entry events; returns (bar_ret, trades, n_unfilled).

    `cost_mult` scales fees and slippage (e1 stress); `cross` is the maker penetration."""
    b, n = a.b, len(a.t)
    ex = q['exit']
    mk = q['exec']['kind'] == 'maker'
    fee_in = (MAKER_FEE if mk else TAKER_FEE) * cost_mult
    slip = a.slip * cost_mult
    off = q['exec']['params'].get('off', 0)
    life = q['exec']['params'].get('life', 0)
    sma = rolling_mean(np.log(b[:, C]), 24 if a.tf == '1h' else 20)
    idx = np.flatnonzero(ev)
    trades, unfilled = [], 0
    nxt_free = 0
    for i in idx:
        if i < nxt_free or i + 1 >= n:
            continue
        dr = d[i]
        # --- entry
        if mk:
            lim = b[i, C] - dr * off * a.atr[i]
            j_end = min(i + life, n - 1)
            j = None
            for jj in range(i + 1, j_end + 1):
                if (dr > 0 and b[jj, L] < lim * (1 - cross)) or (dr < 0 and b[jj, H] > lim * (1 + cross)):
                    j = jj
                    break
            if j is None:
                unfilled += 1
                continue
            px_in, j_in = lim, j               # filled during bar j at the limit
        else:
            j_in = i + 1
            px_in = b[j_in, O] * (1 + dr * slip)
        size = min(TARGET_VOL / a.sig_ann[i], MAX_LEV) if a.sig_ann[i] > 0 else 0.0
        # --- exit decision bar k (decided at its close) or intrabar stop/target
        k, px_out, how = _exit(a, ex, j_in, px_in, dr, sma, mk, slip, cross)
        if k is None:
            break
        fee_out = (MAKER_FEE if how == 'maker' else TAKER_FEE) * cost_mult
        trades.append((i, j_in, k, dr, size, px_in, px_out, fee_in, fee_out, how))
        nxt_free = k + 1
    return _pnl(a, trades), trades, unfilled


def _exit(a, ex, j, px_in, dr, sma, mk, slip, cross):
    """Exit bar and price. Close-decided exits leave on the next bar (maker limit at the decision
    close, else taker at the next close); stops/targets fill intrabar."""
    b, n = a.b, len(a.t)
    kind, p = ex['kind'], ex['params']
    if kind == 'time':
        dec = j + p['h']
    elif kind == 'mean':
        dec = None
        for t in range(j + 1, min(j + MEAN_CAP, n - 1) + 1):
            x = np.log(b[t, C]) - sma[t]
            if np.isfinite(x) and np.sign(x) != dr:     # price is back across its 24-bar mean
                dec = t
                break
        if dec is None:
            dec = j + MEAN_CAP
    else:  # atr
        atr = a.atr[j] if np.isfinite(a.atr[j]) else a.atr[j - 1]
        tgt, stp = px_in + dr * p['tgt'] * atr, px_in - dr * p['stop'] * atr
        for t in range(j + 1, min(j + ATR_CAP, n - 1) + 1):
            hit_stop = b[t, L] <= stp if dr > 0 else b[t, H] >= stp
            hit_tgt = b[t, H] > tgt * (1 + cross) if dr > 0 else b[t, L] < tgt * (1 - cross)
            if hit_stop:                              # stop first when both are touched (conservative)
                px = min(stp, b[t, O]) if dr > 0 else max(stp, b[t, O])   # gap through the stop
                return t, px * (1 - dr * slip), 'taker'
            if hit_tgt:
                return t, tgt, 'maker'
        dec = j + ATR_CAP
    if dec + 1 >= n:
        return None, None, None
    px_dec = b[dec, C]
    nb = b[dec + 1]
    if mk and ((dr > 0 and nb[H] > px_dec * (1 + cross)) or (dr < 0 and nb[L] < px_dec * (1 - cross))):
        return dec + 1, px_dec, 'maker'
    return dec + 1, nb[C] * (1 - dr * slip), 'taker'


def _pnl(a, trades):
    """Per-bar returns of the account: mark to close, entry/exit at their prices, fees, funding."""
    b, n = a.b, len(a.t)
    c = b[:, C]
    r = np.zeros(n)
    pos = np.zeros(n + 1)                           # exposure held over bar t (from close t-1)
    for (_, j, k, dr, sz, pin, pout, fin, fout, _) in trades:
        w = dr * sz
        r[j] += w * (c[j] / pin - 1) - sz * fin
        if k > j + 1:
            pos[j + 1] += w
            pos[k] -= w
        r[k] += w * (pout / c[k - 1] - 1) - sz * fout
    hold = np.cumsum(pos)[:n]
    with np.errstate(invalid='ignore', divide='ignore'):
        cr = np.r_[0.0, c[1:] / c[:-1] - 1]
    r += hold * np.nan_to_num(cr)
    if a.funding is not None and len(trades):
        r -= _funding_cost(a, trades)
    return r


def _funding_cost(a, trades):
    """Funding paid at settlement stamps while a position is open (longs pay positive rates)."""
    ft, fr = a.funding[:, 0].astype(np.int64), a.funding[:, 1]
    out = np.zeros(len(a.t))
    for (_, j, k, dr, sz, *_r) in trades:
        lo, hi = a.t[j], a.t[k]
        m = (ft > lo) & (ft <= hi)
        if m.any():
            bars = np.searchsorted(a.t, ft[m], side='right') - 1
            np.add.at(out, bars, dr * sz * fr[m])
    return out


def daily(a, bar_ret):
    """Bar returns summed into UTC days (dict day_ms -> return)."""
    days = a.day
    u, inv = np.unique(days, return_inverse=True)
    s = np.zeros(len(u))
    np.add.at(s, inv, bar_ret)
    return u, s
