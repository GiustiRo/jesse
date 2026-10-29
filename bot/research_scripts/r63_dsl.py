"""r63: the r62 DSL on the alt universe (PROTOCOL_R63 §3).

`configure(names)` narrows r62_dsl's module tables in place: universes `alts_1h`/`alts_1d` over the
given tramo names; no `spread_z` (no pairs), no `cascade` (no OI), no `cme_gap` (alts have no CME
gap). r62's parser, hash, random programs and GA operators then work on the r63 catalogue unchanged.

The engine differs from r62 in three places (§2): entries need the asset to be eligible that day,
taker slippage comes from the 30-day volume tier at the entry bar, and a position still open when
a tramo ends is closed at its last close (taker fee + 100 bp after a delisting; normal costs at the
2024-12-31 cut) instead of being dropped as r62 did.
"""
import copy
import json

import numpy as np

import r62_dsl as dsl

C, H, L, O = dsl.C, dsl.H, dsl.L, dsl.O
UNIVERSE_TF = {'alts_1h': '1h', 'alts_1d': '1d'}
_R62_SIGNAL_EVENTS = dsl.signal_events


def configure(names):
    """Point r62_dsl at the r63 catalogue and universe (idempotent; `names` = tramo ids)."""
    names = list(names)
    dsl.UNIVERSES.clear()
    dsl.UNIVERSES.update({u: (tf, names) for u, tf in UNIVERSE_TF.items()})
    for k in ('spread_z', 'cascade'):
        dsl.SIGNALS.pop(k, None)
    dsl.SIGNALS['clock'] = {'event': ['funding_hour', 'month_end'], 'mode': ['fade', 'follow']}
    dsl.CASCADE_ENABLED = False
    dsl.validate = validate
    dsl.signal_events = cached_signal_events
    dsl._funding_cost = funding_cost


def cached_signal_events(a, s):
    """r62 signal_events memoised per asset and piece. A piece's events do not depend on the rest
    of the program, and RSI(2) / month_end are Python loops, so recomputing them for every program
    dominated the run time. Kept sparse (event index + direction) to bound memory per worker."""
    key = ('sig', json.dumps(s, sort_keys=True))
    hit = a._cache.get(key)
    if hit is None:
        ev, d = _R62_SIGNAL_EVENTS(a, s)
        idx = np.flatnonzero(ev)
        hit = a._cache[key] = (idx.astype(np.int32), d[idx].astype(np.int8))
    n = len(a.t)
    ev, d = np.zeros(n, bool), np.zeros(n)
    ev[hit[0]] = True
    d[hit[0]] = hit[1]
    return ev, d


def funding_cost(a, trades):
    """r62_dsl._funding_cost with searchsorted instead of a mask over every funding row per trade."""
    out = np.zeros(len(a.t))
    if a.funding is None or not len(a.funding) or not trades:
        return out
    ft, fr = a.funding[:, 0].astype(np.int64), a.funding[:, 1]
    bar = np.searchsorted(a.t, ft, side='right') - 1
    for (_, j, k, dr, sz, *_r) in trades:
        lo, hi = np.searchsorted(ft, a.t[j], side='right'), np.searchsorted(ft, a.t[k], side='right')
        if hi > lo:
            np.add.at(out, bar[lo:hi], dr * sz * fr[lo:hi])
    return out


def validate(p):
    """r62's parser rules for single-asset universes, with the r63 universe restrictions (§3)."""
    if not isinstance(p, dict) or set(p) - {'universe', 'signal', 'filters', 'exit', 'size', 'exec'}:
        raise dsl.DslError('unknown top-level keys')
    q = copy.deepcopy(p)
    q.setdefault('filters', [])
    q.setdefault('size', {'kind': 'voltgt', 'params': {'side': 'both'}})
    if q.get('universe') not in dsl.UNIVERSES:
        raise dsl.DslError(f'universe {q.get("universe")!r}')
    tf = dsl.UNIVERSES[q['universe']][0]

    def piece(x, table, what):
        if not isinstance(x, dict) or x.get('kind') not in table:
            raise dsl.DslError(f'{what}: unknown kind {x!r}')
        prm = x.get('params', {}) or {}
        if set(prm) != set(table[x['kind']]):
            raise dsl.DslError(f'{what} {x["kind"]}: params {sorted(prm)} != {sorted(table[x["kind"]])}')
        for k, v in prm.items():
            if v not in table[x['kind']][k]:
                raise dsl.DslError(f'{what} {x["kind"]}.{k}={v!r} not in grid')
        return {'kind': x['kind'], 'params': {k: prm[k] for k in sorted(prm)}}

    if not isinstance(q.get('signal'), list) or not 1 <= len(q['signal']) <= 2:
        raise dsl.DslError('signal must hold 1-2 pieces')
    if not isinstance(q['filters'], list) or len(q['filters']) > 2:
        raise dsl.DslError('filters must hold 0-2 pieces')
    q['signal'] = [piece(s, dsl.SIGNALS, 'signal') for s in q['signal']]
    q['filters'] = sorted((piece(f, dsl.FILTERS, 'filter') for f in q['filters']),
                          key=lambda f: json.dumps(f, sort_keys=True))
    q['exit'] = piece(q.get('exit'), dsl.EXITS, 'exit')
    q['size'] = piece(q['size'], dsl.SIZES, 'size')
    q['exec'] = piece(q.get('exec'), dsl.EXECS, 'exec')
    kinds = [s['kind'] for s in q['signal']]
    if len(set(kinds)) != len(kinds):
        raise dsl.DslError('duplicate signal kind')
    if len({f['kind'] for f in q['filters']}) != len(q['filters']):
        raise dsl.DslError('duplicate filter kind')
    if tf == '1d':
        bad = {'clock'} & set(kinds) or {'session'} & {f['kind'] for f in q['filters']}
        if bad:
            raise dsl.DslError(f'{sorted(bad)} need 1h bars')
    if len(q['signal']) + len(q['filters']) + 2 > dsl.MAX_PIECES + 1:
        raise dsl.DslError('too many pieces')
    if dsl.n_params(q) > dsl.MAX_PARAMS:
        raise dsl.DslError('too many params')
    return q


class AltAsset(dsl.Asset):
    """One tramo of one symbol: r62 Asset plus per-bar eligibility, taker slippage and end kind."""

    def __init__(self, name, bars, tf, funding, btc_t90, elig, slip, end_slip):
        super().__init__(name, bars[:, :6], tf, funding=funding, btc_t90=btc_t90)
        self.elig = np.asarray(elig, bool)
        self.slip_bar = np.asarray(slip, float)
        self.end_slip = float(end_slip)          # slippage of the forced close at the tramo's last bar


def entry_events(a, q):
    ev, d = dsl.entry_events(a, q)
    return ev & a.elig, d


def simulate(a, q, ev, d, cost_mult=1.0, cross=dsl.CROSS):
    """r62_dsl.simulate with the per-entry slippage tier and the forced close at the tramo's end."""
    b, n = a.b, len(a.t)
    ex = q['exit']
    mk = q['exec']['kind'] == 'maker'
    fee_in = (dsl.MAKER_FEE if mk else dsl.TAKER_FEE) * cost_mult
    off = q['exec']['params'].get('off', 0)
    life = q['exec']['params'].get('life', 0)
    sma = dsl.rolling_mean(np.log(b[:, C]), 24 if a.tf == '1h' else 20)
    trades, unfilled = [], 0
    nxt_free = 0
    for i in np.flatnonzero(ev):
        if i < nxt_free or i + 1 >= n:
            continue
        dr = d[i]
        slip = a.slip_bar[i] * cost_mult
        if mk:
            lim = b[i, C] - dr * off * a.atr[i]
            j = None
            for jj in range(i + 1, min(i + life, n - 1) + 1):
                if (dr > 0 and b[jj, L] < lim * (1 - cross)) or (dr < 0 and b[jj, H] > lim * (1 + cross)):
                    j = jj
                    break
            if j is None:
                unfilled += 1
                continue
            px_in, j_in = lim, j
        else:
            j_in = i + 1
            px_in = b[j_in, O] * (1 + dr * slip)
        if j_in >= n - 1:                         # no bar left to hold or leave the position
            break
        size = min(dsl.TARGET_VOL / a.sig_ann[i], dsl.MAX_LEV) if a.sig_ann[i] > 0 else 0.0
        k, px_out, how = dsl._exit(a, ex, j_in, px_in, dr, sma, mk, slip, cross)
        if k is None:
            # §2: the tramo ends with the position open -> close at the last close, taker
            k, how = n - 1, 'end'
            px_out = b[k, C] * (1 - dr * max(a.end_slip * cost_mult, slip))
        fee_out = (dsl.MAKER_FEE if how == 'maker' else dsl.TAKER_FEE) * cost_mult
        trades.append((i, j_in, k, dr, size, px_in, px_out, fee_in, fee_out, how))
        nxt_free = k + 1
    return dsl._pnl(a, trades), trades, unfilled
