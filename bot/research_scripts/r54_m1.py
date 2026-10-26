"""r54 M1: meta-labeling sizing of C6 (PROTOCOL_R54.md section M1, one trial).

* Events: every R2/R3 entry of the frozen C6 decider on the 50 U50 symbols (the 48 alts on
  vision 4h bars as in r54_v1, BTC/ETH on r51's perp bars of P1's common window), R = PnL over
  the 1% risk budget at entry, label R > 0.
* Features at the entry signal bar (data up to that bar's close only): z(QOI) 4h (r52_q), 7-day
  mean funding rate, 30-day realized vol (daily log returns), 4-week return, ADX14 (4h),
  (close - EMA80) / ATR14, BTC daily close > SMA200 (Binance spot), BTC 7-day return.
* Model: LogisticRegression(C=1, L2) on training-standardized features; refit at every calendar
  quarter start from 2022-01-01 on events CLOSED before it (pooled, both sleeves). Before
  2022-01-01 m = 1; after, risk per trade = 1% * m with m = clip(2p, 0.5, 1.5).
* Two passes: pass 1 (m == 1) produces the training events; pass 2 sizes with the walk-forward
  models. Entry/exit timing does not depend on size, so events are the same in both passes;
  only equity (hence the R normalization and compounding) changes. That second-order effect on
  labels is ignored (declared).
* Evaluation through 2024-12-31 only: (a) equal-weight 48-alt C6 basket, sized vs unsized,
  2022-01-01..2024-12-31; (b) P1 vs P1 with sized BTC/ETH C6 under the r51 inclusion rule
  (r51_f6.compare), both windows cut at 2024-12-31, N = 125. Gate: (b) passes and (a) Sharpe
  improves by >= 0.1. Curves through 2025 are saved, never measured.

    python research_scripts/r54_m1.py run

writes data/r52/m1.json and data/r52/m1_curves.npy.
"""
import json
import os
import sys
from datetime import datetime, timezone

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

import r50_engines as en
import r50_f1b as fb
import r50_f1c as fc
import r51_lib as lib
import r51_f6 as f6
import r51_sleeves as sv
import r52_q
import r54_v1 as v1
from r50_harness import T, O, C, H, L, DAY_MS
from r50_f1b import ta, stop_exit, chandelier, _trade, TAKER, MAKER, STOP_SLIP, MAX_X, RISK_PER_TRADE

DATA = v1.DATA
H4 = v1.H4
N_FINAL = 125                     # 123 + W1 + M1 (PROTOCOL_R54)
CUT = '2025-01-01'                # 2025 sealed: every metric stops at 2024-12-31
FIRST_PRED = '2022-01-01'
EVAL_FROM = '2022-01-01'
M_LO, M_HI = 0.5, 1.5
FEATURES = ['z_qoi', 'fund7', 'vol30', 'ret4w', 'adx14', 'dist_e80_atr', 'btc_regime', 'btc_ret7']


def _ms(s):
    return en.hz._ms(s)


def _date(t):
    return datetime.fromtimestamp(int(t) / 1000, tz=timezone.utc).date().isoformat()


def quarter_start(t):
    d = datetime.fromtimestamp(int(t) / 1000, tz=timezone.utc)
    return int(datetime(d.year, 3 * ((d.month - 1) // 3) + 1, 1, tzinfo=timezone.utc).timestamp() * 1000)


def quarter_starts(frm, to):
    out, t = [], _ms(frm)
    while t < _ms(to):
        out.append(t)
        d = datetime.fromtimestamp(t / 1000, tz=timezone.utc)
        y, m = (d.year + 1, 1) if d.month == 10 else (d.year, d.month + 3)
        t = int(datetime(y, m, 1, tzinfo=timezone.utc).timestamp() * 1000)
    return out


# ----------------------------------------------------------------------------------------------
# Sized copy of the frozen decider
# ----------------------------------------------------------------------------------------------
def sized_r2_r3_decider(bars, retest, m_fn, log, max_stop=0.055):
    """r50_f1b.r2_r3_decider unchanged except risk = RISK_PER_TRADE * m, with m = m_fn(i) taken at
    the entry signal bar i (R2: the breakout bar it fills on; R3: the bar that places the limit).
    Each opened position appends (signal bar, fill close ts, m) to `log`."""
    c, h, l, o = bars[:, C], bars[:, H], bars[:, L], bars[:, O]
    e20 = ta.ema(bars, period=20, sequential=True)
    e80 = ta.ema(bars, period=80, sequential=True)
    atr = ta.atr(bars, period=14, sequential=True)
    adx = ta.adx(bars, period=14, sequential=True)
    rsi = ta.rsi(bars, period=14, sequential=True)
    hh26 = en.prior_max(h, 26)
    st = {'limit': None}

    def risk_qty(acct, price, dist, m):
        eq = acct.equity(price)
        q = eq * (RISK_PER_TRADE * m) / (dist + 2 * acct.fee * price)
        return max(min(q, eq * MAX_X / price), 0.0)

    def setup(i):
        return (i >= 100 and np.isfinite([e20[i], e80[i], e80[i - 4], atr[i], adx[i], rsi[i], hh26[i]]).all()
                and atr[i] > 0 and c[i] > e80[i] and e20[i] > e80[i] > e80[i - 4] and adx[i] >= 26
                and 52 <= rsi[i] <= 76 and h[i] - l[i] <= 3 * atr[i])

    def open_pos(acct, i, price, dist, ts, fee, m, sig):
        q = risk_qty(acct, price, dist, m)
        if q > 0:
            _trade(acct, q, price, ts, fee)
            log.append((sig, ts, m))
            st.update(entry=price, r=dist, stop=price - dist, best_close=price, extreme=h[i], hi=h[i],
                      be_on_extreme=not retest)

    def decide(i, acct, ts):
        if acct.is_open:
            if stop_exit(acct, st, o, l, i, ts):
                return
            st['hi'] = h[i]
            chandelier(st, c[i], atr[i], 4.2, 2.25 if retest else 1.75, TAKER, True)
            return
        if retest and st['limit'] is not None:
            px, dist, m, sig = st['limit']
            st['limit'] = None
            if l[i] < px:
                open_pos(acct, i, px, dist, ts, MAKER, m, sig)
                if acct.is_open and l[i] <= st['stop']:  # same-bar stop after the fill
                    _trade(acct, -acct.qty, st['stop'] * (1 - STOP_SLIP), ts, TAKER)
                return
        if not setup(i):
            return
        if retest:
            entry = hh26[i]
            if entry < c[i] <= entry + atr[i] and 0 < 2 * atr[i] < entry:
                st['limit'] = (entry, 2 * atr[i], m_fn(i), i)
        elif c[i] > hh26[i]:
            frac = max(2 * atr[i] / c[i], 0.008)
            if max_stop is None or frac <= max_stop:
                open_pos(acct, i, c[i], frac * c[i], ts, TAKER, m_fn(i), i)
    return decide


# ----------------------------------------------------------------------------------------------
# Features per 4h bar (each row uses data up to that bar's close)
# ----------------------------------------------------------------------------------------------
_BTC = {}


def btc_daily():
    if not _BTC:
        d = sv.daily('BTC', 'spot')
        close_ts = d[:, T].astype(np.int64) + DAY_MS
        cl = d[:, C]
        _BTC.update(close_ts=close_ts, regime=np.where(np.isfinite(en.sma(cl, 200)), (cl > en.sma(cl, 200)).astype(float), np.nan),
                    ret7=np.r_[np.full(7, np.nan), cl[7:] / cl[:-7] - 1])
    return _BTC


def features(bars, sym):
    c = bars[:, C]
    close_ts = bars[:, T].astype(np.int64) + H4
    n = len(bars)
    X = np.full((n, len(FEATURES)), np.nan)
    # z(QOI), stamped at the 4h bar close.
    qdf, _ = r52_q.bars_4h(sym)
    z = pd.Series(qdf['z'].values, index=qdf.index.asi8 // 10**6)
    z = z[~z.index.duplicated()]
    X[:, 0] = z.reindex(close_ts).values
    # 7-day mean funding rate over settlements in (close - 7d, close].
    f = np.load(os.path.join(DATA, f'{sym}_funding.npy'))
    if len(f):
        ft, cs = f[:, 0].astype(np.int64), np.r_[0.0, np.cumsum(f[:, 1])]
        hi = np.searchsorted(ft, close_ts, side='right')
        lo = np.searchsorted(ft, close_ts - 7 * DAY_MS, side='right')
        cnt = hi - lo
        X[:, 1] = np.where(cnt > 0, (cs[hi] - cs[lo]) / np.maximum(cnt, 1), np.nan)
    # Daily-spaced closes ending at this bar (last close at or before close - k days).
    px = np.full((n, 31), np.nan)
    for k in range(31):
        idx = np.searchsorted(close_ts, close_ts - k * DAY_MS, side='right') - 1
        px[:, k] = np.where(idx >= 0, c[np.clip(idx, 0, None)], np.nan)
    lr = np.log(px[:, :-1] / px[:, 1:])
    full = ~np.isnan(lr).any(axis=1)
    X[full, 2] = lr[full].std(axis=1, ddof=1) * np.sqrt(365)
    X[:, 3] = px[:, 0] / px[:, 28] - 1
    X[:, 4] = ta.adx(bars, period=14, sequential=True)
    e80 = ta.ema(bars, period=80, sequential=True)
    atr = ta.atr(bars, period=14, sequential=True)
    X[:, 5] = np.where(atr > 0, (c - e80) / atr, np.nan)
    b = btc_daily()
    j = np.searchsorted(b['close_ts'], close_ts, side='right') - 1
    ok = j >= 0
    X[ok, 6] = b['regime'][j[ok]]
    X[ok, 7] = b['ret7'][j[ok]]
    return X


# ----------------------------------------------------------------------------------------------
# Runs
# ----------------------------------------------------------------------------------------------
class Sym:
    """One simulated instrument: bars, start, and how to simulate a decider on it."""

    def __init__(self, name, sym, bars, start, frm, sim):
        self.name, self.sym, self.bars, self.start, self.frm, self.sim = name, sym, bars, start, frm, sim
        self.X = None


def vision_sym(sym):
    bars, h1 = v1.h4_bars(sym)
    start = max(v1.SIM_FROM, int(bars[min(v1.WARM_BARS, len(bars) - 1), T]))
    if start >= _ms(v1.MEASURE[1]):
        return None

    def sim(dec):
        return v1.simulate(bars, start, dec, v1.funding_cursor(sym, h1, int(bars[0, T])))
    return Sym(sym, sym, bars, start, _date(start), sim)


def lib_sym(name, d):
    def sim(dec):
        return en.simulate(d['h4'], d['start_ms'], dec, name, d['funding'], fb.H4_MS)
    return Sym(name, f'{name}USDT', d['h4'], d['start_ms'], lib._date(d['start_ms']), sim)


def run_c6(s, m_fn):
    """Both sleeves of C6 with a sizing callback; returns C6 curve, sleeve curves and events."""
    sleeves, events = [], []
    for retest in (False, True):
        log = []
        ts, eq, acct = s.sim(sized_r2_r3_decider(s.bars, retest, m_fn, log))
        sleeves.append(en.calendar(ts, eq, s.frm, en.COMMON[1]))
        assert len(acct.trades) <= len(log) <= len(acct.trades) + 1
        for t, (sig, fill_ts, m) in zip(acct.trades, log):
            assert t['opened'] == fill_ts
            k = int(np.searchsorted(ts, t['opened'], side='left'))
            eq0 = eq[k - 1] if k > 0 else en.BALANCE
            events.append({'sym': s.sym, 'sleeve': 'R3' if retest else 'R2', 'sig_i': int(sig),
                           'sig_ts': int(s.bars[sig, T]) + H4, 'opened': int(t['opened']), 'closed': int(t['closed']),
                           'pnl': float(t['pnl']), 'R': float(t['pnl'] / (0.01 * eq0)), 'm': float(m),
                           'x': s.X[sig].tolist() if s.X is not None else None})
        # Entries still open at the end carry their m for the mean-m statistic only.
        for sig, fill_ts, m in log[len(acct.trades):]:
            events.append({'sym': s.sym, 'sleeve': 'R3' if retest else 'R2', 'sig_i': int(sig),
                           'sig_ts': int(s.bars[sig, T]) + H4, 'opened': int(fill_ts), 'closed': None, 'm': float(m)})
    return fc.mean_curve(sleeves), sleeves, events


def one(i):
    return 1.0


def frozen_c6_equity(s):
    out = []
    for retest in (False, True):
        ts, eq, _ = s.sim(fb.r2_r3_decider(s.bars, retest))
        out.append((ts, eq))
    return out


def assert_repro(s):
    """m == 1 copy reproduces the frozen decider's equity exactly on both sleeves."""
    for retest, (ts0, eq0) in zip((False, True), frozen_c6_equity(s)):
        ts1, eq1, _ = s.sim(sized_r2_r3_decider(s.bars, retest, one, []))
        assert np.array_equal(ts0, ts1) and np.array_equal(eq0, eq1), (s.name, retest)
    return True


def same_curve(a, b):
    return np.array_equal(a[0], b[0]) and np.array_equal(a[1], b[1])


def cut(cv, end=CUT):
    d, v = cv
    k = int(np.searchsorted(d, _ms(end)))
    return d[:k], v[:k]


class WalkForward:
    def __init__(self, events):
        self.qs = quarter_starts(FIRST_PRED, '2026-01-01')
        self.models, self.train_n = {}, {}
        tr = [e for e in events if e.get('closed') is not None]
        Xa = np.array([e['x'] for e in tr], dtype=float)
        ya = np.array([e['R'] > 0 for e in tr], dtype=int)
        closed = np.array([e['closed'] for e in tr], dtype=np.int64)
        for q in self.qs:
            sel = closed < q
            X, y = Xa[sel], ya[sel]
            mu = np.nanmean(X, axis=0)
            sd = np.nanstd(X, axis=0)
            sd = np.where(sd > 0, sd, 1.0)
            Z = np.nan_to_num((X - mu) / sd, nan=0.0)   # missing feature -> training mean
            lr = LogisticRegression(C=1.0, max_iter=1000).fit(Z, y)
            self.models[q] = (mu, sd, lr)
            self.train_n[_date(q)] = {'n': int(sel.sum()), 'pos_rate': float(y.mean())}

    def p(self, x, ts):
        q = quarter_start(ts)
        if ts < _ms(FIRST_PRED) or q not in self.models:
            return None
        mu, sd, lr = self.models[q]
        z = np.nan_to_num((np.asarray(x, dtype=float) - mu) / sd, nan=0.0)
        return float(lr.predict_proba(z[None, :])[0, 1])

    def m_fn(self, s):
        def f(i):
            p = self.p(s.X[i], int(s.bars[i, T]) + H4)
            return 1.0 if p is None else float(np.clip(2 * p, M_LO, M_HI))
        return f


def run():
    out = {'protocol': 'PROTOCOL_R54.md M1', 'n_final': N_FINAL, 'features': FEATURES, 'asserts': {},
           'declared': ['labels from pass 1 (m == 1); sizing changes equity and hence R normalization, ignored',
                        'missing features (e.g. z(QOI) before 540 bars of history) imputed with the training mean',
                        'R3 sizing uses the model/features of the bar that places the limit (signal bar)',
                        'quarter of a signal = quarter of its 4h bar close time',
                        'BTC/ETH long-window (spot) C6 is sized with features from its spot bars and perp funding/QOI files']}
    uni = [u['symbol'] for u in json.load(open(os.path.join(DATA, 'universe50.json')))]
    alts = [s for s in uni if s not in ('BTCUSDT', 'ETHUSDT')]
    syms = [s for s in (vision_sym(a) for a in alts) if s is not None]
    print('alts', len(syms), flush=True)
    # P1 and the r51 bars of BTC/ETH.
    p1, extra = {}, {}
    for w in ('long', 'common'):
        comps, _, ex = lib.p1_components(w)
        p1[w], extra[w] = comps, ex
    core = {w: [lib_sym(n, extra[w]['data'][n]) for n in extra[w]['c6']] for w in extra}
    # Reproduction asserts.
    out['asserts']['SOLUSDT_vision'] = assert_repro(next(s for s in syms if s.sym == 'SOLUSDT'))
    out['asserts']['BTCUSDT_vision'] = assert_repro(vision_sym('BTCUSDT'))
    for w in core:
        for s in core[w]:
            out['asserts'][f'{s.name}_{w}_r51'] = assert_repro(s)
    print('repro decider ok', flush=True)
    # Features.
    for s in syms + core['common'] + core['long']:
        s.X = features(s.bars, s.sym)
    print('features ok', flush=True)
    # Pass 1 (m == 1): training events and unsized curves.
    v1c = np.load(os.path.join(DATA, 'v1_curves.npy'), allow_pickle=True).item()
    unsized, events = {}, []
    for s in syms:
        cv, _, ev = run_c6(s, one)
        assert same_curve(cv, v1c[s.sym]), s.sym
        unsized[s.sym] = cv
        events += ev
    out['asserts']['alts_unsized_eq_v1_curves'] = True
    for w in core:
        for s in core[w]:
            cv, _, ev = run_c6(s, one)
            assert same_curve(cv, extra[w]['c6'][s.name]), (s.name, w)
            out['asserts'][f'{s.name}_{w}_c6_eq_r51'] = True
            if w == 'common':
                events += ev
    print('pass1 ok, events', len(events), flush=True)
    pool = [e for e in events if e['closed'] is not None]
    out['events'] = {'total_closed': len(pool), 'by_sleeve': {k: sum(e['sleeve'] == k for e in pool) for k in ('R2', 'R3')},
                     'btc_eth': sum(e['sym'] in ('BTCUSDT', 'ETHUSDT') for e in pool)}
    wf = WalkForward(pool)
    out['train_n_per_refit'] = wf.train_n
    # Out-of-sample AUC on 2022-2024 events (signal and close inside 2022-01-01..2024-12-31).
    oos = [e for e in pool if _ms(EVAL_FROM) <= e['sig_ts'] < _ms(CUT) and e['closed'] < _ms(CUT)]
    pp = np.array([wf.p(e['x'], e['sig_ts']) for e in oos])
    yy = np.array([e['R'] > 0 for e in oos], dtype=int)
    out['oos'] = {'n': len(oos), 'pos_rate': float(yy.mean()), 'auc': float(roc_auc_score(yy, pp)),
                  'mean_p': float(pp.mean()), 'mean_m': float(np.clip(2 * pp, M_LO, M_HI).mean())}
    # Pass 2: sized.
    sized, sized_ev = {}, []
    for s in syms:
        cv, _, ev = run_c6(s, wf.m_fn(s))
        sized[s.sym] = cv
        sized_ev += ev
    core_sized = {}
    for w in core:
        core_sized[w] = {}
        for s in core[w]:
            cv, _, ev = run_c6(s, wf.m_fn(s))
            core_sized[w][s.name] = cv
            if w == 'common':
                sized_ev += ev
    ms = [e['m'] for e in sized_ev if _ms(EVAL_FROM) <= e['sig_ts'] < _ms(CUT)]
    out['mean_m_2022_2024'] = {'n_entries': len(ms), 'mean': float(np.mean(ms)), 'min': float(np.min(ms)),
                               'max': float(np.max(ms)), 'share_at_floor': float(np.mean(np.array(ms) <= M_LO)),
                               'share_at_cap': float(np.mean(np.array(ms) >= M_HI))}
    # (a) 48-alt basket, 2022-01-01..2024-12-31.
    keep = ('from', 'to', 'sharpe', 'cagr', 'max_dd', 'quarters_pos')
    a = {}
    for k, cvs in (('unsized', unsized), ('sized', sized)):
        b = fb.basket({s: cut(cv) for s, cv in cvs.items()}, list(cvs))
        a[k] = {x: en.metrics(b[0], b[1], [], EVAL_FROM)[x] for x in keep}
    a['d_sharpe'] = a['sized']['sharpe'] - a['unsized']['sharpe']
    a['pass'] = bool(a['d_sharpe'] >= 0.1)
    out['a_alts_basket'] = a
    # (b) P1 vs P1 with sized BTC/ETH C6, windows cut at 2024-12-31.
    base = {w: {k: cut(v) for k, v in p1[w].items()} for w in p1}
    c6s = {w: fb.basket(core_sized[w], list(core_sized[w])) for w in core_sized}
    cand = {w: {'C6': cut(c6s[w])} for w in c6s}
    ok, info = f6.compare(base, cand, [], [], N_FINAL)
    keep_b = ('from', 'cagr', 'max_dd', 'sharpe', 'months_pos', 'quarters_pos', 'q_pos_count', 'n_quarters', 'dsr')
    out['b_p1'] = {'pass': bool(ok), 'd_sharpe_long': info['d_sharpe_long'], 'd_q_pos_long': info['d_q_pos_long'],
                   'd_sharpe_common': info['d_sharpe_common'],
                   'detail': {w: {k: {x: info['detail'][w][k][x] for x in keep_b if x in info['detail'][w][k]}
                                  for k in ('base', 'with')} | {'from': info['detail'][w]['from']} for w in info['detail']}}
    # Standalone BTC/ETH C6 component (2022-01-01..2024-12-31), information only.
    out['b_c6_component_2022_2024'] = {}
    for w in c6s:
        u = cut(p1[w]['C6'])
        s_ = cut(c6s[w])
        out['b_c6_component_2022_2024'][w] = {'unsized': {x: en.metrics(u[0], u[1], [], EVAL_FROM)[x] for x in keep},
                                              'sized': {x: en.metrics(s_[0], s_[1], [], EVAL_FROM)[x] for x in keep}}
    out['gate'] = {'b_pass': out['b_p1']['pass'], 'a_pass': a['pass'], 'pass': bool(out['b_p1']['pass'] and a['pass'])}
    json.dump(out, open(os.path.join(DATA, 'm1.json'), 'w'), indent=1, default=float)
    np.save(os.path.join(DATA, 'm1_curves.npy'),
            {'alts_sized': sized, 'btc_eth_sized': core_sized, 'C6_sized': c6s,
             'note': 'calendar curves through 2025-12-31; 2025 sealed, not measured'}, allow_pickle=True)
    print('asserts', json.dumps(out['asserts']))
    print('events', json.dumps(out['events']))
    print('train_n', json.dumps(out['train_n_per_refit']))
    print('oos', json.dumps(out['oos']))
    print('mean_m', json.dumps(out['mean_m_2022_2024']))
    print('a', json.dumps(a, default=float))
    print('b', json.dumps({k: out['b_p1'][k] for k in ('pass', 'd_sharpe_long', 'd_q_pos_long', 'd_sharpe_common')}))
    for w, d in out['b_p1']['detail'].items():
        print(w, d['from'], 'P1', {x: round(d['base'][x], 3) for x in ('cagr', 'max_dd', 'sharpe', 'quarters_pos')},
              'M1', {x: round(d['with'][x], 3) for x in ('cagr', 'max_dd', 'sharpe', 'quarters_pos')})
    print('c6comp', json.dumps(out['b_c6_component_2022_2024'], default=float))
    print('gate', json.dumps(out['gate']))


def main():
    if len(sys.argv) < 2 or sys.argv[1] != 'run':
        print(__doc__)
        return 1
    run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
