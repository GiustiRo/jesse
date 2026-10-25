"""r50 F1b: ten all-terrain candidates (R1-R6 revalidations, N1-N4 new) on the 7-asset core.

Rules, defaults and gates are fixed in
`strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r50/PHASE1B_PROTOCOL.md`,
committed before this file was written. Shared conventions (data, costs, windows, metrics,
baskets) come unchanged from r50_engines / r50_harness, which F0 validated against Jesse.

    python research_scripts/r50_f1b.py screen

writes research_scripts/data/r50/f1b_screen.json and f1b_gates.json.
"""
import json
import math
import os
import sys
from datetime import datetime, timezone
from statistics import NormalDist

import numpy as np
import jesse.models  # noqa: F401 - must load before candle_service (circular import otherwise)
import jesse.indicators as ta
from jesse.services.candle_service import generate_completed_candles_from_observed_minutes

import r50_harness as hz
import r50_engines as en
from r50_harness import T, O, C, H, L, V, DAY_MS, Account, DonchianEnsR49
from r50_engines import (ASSETS, COMMON, MEASURE_FROM, TAKER, MAKER, STOP_SLIP, TARGET_VOL, MAX_X,
                         BAND, BALANCE, LEVERAGE, SLIP_BPS, FUNDING, logret, sma, rsi2, ann_vol,
                         rebalance, _trade, simulate, calendar, metrics, daily_returns)

H4_MS = 4 * 3_600_000
CORE = ['BTC', 'ETH', 'XAU', 'SPX', 'WTI', 'GAS', 'BOND']
RISK_PER_TRADE = 0.01      # stop-based candidates (protocol section 1)
N_DECLARED = 73
# R1 per-asset settings: the validated r49 null configurations (protocol R1).
R1_CFG = {'BTC': dict(candles_per_day=6, ann_days=365), 'ETH': dict(candles_per_day=6, ann_days=365),
          'XAU': dict(candles_per_day=6, ann_days=365),
          'SPX': dict(candles_per_day=5, ann_days=252, hours=en.SPX_HOURS),
          'WTI': dict(candles_per_day=6, ann_days=252, hours=en.ENERGY_HOURS),
          'GAS': dict(candles_per_day=6, ann_days=252, hours=en.ENERGY_HOURS),
          'BOND': dict(candles_per_day=6, ann_days=252, hours=en.ENERGY_HOURS)}
ROLE = {'R1': 'trend', 'R2': 'trend', 'R3': 'trend', 'R4': 'trend', 'R6': 'trend', 'N2': 'trend',
        'N3': 'trend', 'R5': 'diversifier', 'N1': 'diversifier', 'N4': 'combination'}


# ----------------------------------------------------------------------------------------------
# Data
# ----------------------------------------------------------------------------------------------
def load_both(name, window):
    """Daily and 4h bars from one read of the stored minutes, plus the measurement start.

    The start follows F1: the common window opens 2020-10-15 (metrics from 2021-01-01); the long
    window starts once ~260 daily bars of warmup exist."""
    spec = ASSETS[name]
    ex, sym = spec[window]
    frm = COMMON[0] if window == 'common' else spec['long_start']
    f_ms = hz._ms(COMMON[1])
    m = hz._minutes(ex, sym, hz._ms(frm) - 500 * DAY_MS, f_ms)
    daily = en.daily_from_minutes(m, spec['cfd'], f_ms)
    h4 = generate_completed_candles_from_observed_minutes('4h', m, f_ms)
    if len(daily) < 300:
        return None
    if window == 'common':
        start_ms = hz._ms(frm)
        mfrom = MEASURE_FROM
    else:
        start_ms = int(daily[min(260, len(daily) - 1), T])
        mfrom = datetime.fromtimestamp(start_ms / 1000, tz=timezone.utc).date().isoformat()
    fund = window == 'common' and ex.startswith('Binance Perp')
    return {'daily': daily, 'h4': h4, 'start_ms': start_ms, 'mfrom': mfrom, 'funding': fund,
            'source': f'{ex} / {sym}', 'cfd': spec['cfd']}


# ----------------------------------------------------------------------------------------------
# Shared pieces
# ----------------------------------------------------------------------------------------------
def risk_qty(acct, price, dist):
    """1% of sleeve equity at risk to the initial stop (fees included), capped at 2x notional."""
    eq = acct.equity(price)
    q = eq * RISK_PER_TRADE / (dist + 2 * acct.fee * price)
    return max(min(q, eq * MAX_X / price), 0.0)


def stop_exit(acct, st, o, l, i, ts):
    """Long stop check inside bar i: fills at the stop, or the open on a gap, minus 5 bp."""
    if acct.is_open and l[i] <= st['stop']:
        _trade(acct, -acct.qty, min(st['stop'], o[i]) * (1 - STOP_SLIP), ts, TAKER)
        return True
    return False


def chandelier(st, close, atr, trail_mult, be_r, fee, tighten):
    """K1001/Core4h trailing: best close - mult*ATR (tightened at 5R/8R), BE once best >= be_r."""
    st['best_close'] = max(st['best_close'], close)
    st['extreme'] = max(st.get('extreme', close), st.get('hi', close))
    ref = st['extreme'] if st.get('be_on_extreme') else st['best_close']
    best_r = (ref - st['entry']) / st['r'] if st['r'] > 0 else 0.0
    mult = trail_mult
    if tighten:
        mult *= 0.62 if best_r >= 8 else (0.78 if best_r >= 5 else 1.0)
    new = st['best_close'] - mult * atr
    if best_r >= be_r:
        new = max(new, st['entry'] * (1 + 2.5 * fee))
    if st['stop'] < new < close:
        st['stop'] = new


# ----------------------------------------------------------------------------------------------
# Candidates
# ----------------------------------------------------------------------------------------------
class SlipAccount(Account):
    """The validated r49 engine calls trade() without the slippage flag; F1b costs (amendment
    4b) still apply to every taker fill, so slippage defaults on here."""

    def trade(self, dqty, price, ts, slippage=True):
        return super().trade(dqty, price, ts, slippage)


def r1_run(name, d):
    """Validated r49 Donchian ensemble on 4h bars (hz.run), Jesse accounting."""
    h4 = d['h4']
    k = int(np.searchsorted(h4[:, T], d['start_ms'], side='left'))
    warm, bars = h4[max(0, k - 1520):k], h4[k:]
    acct = SlipAccount(BALANCE, TAKER, 3, SLIP_BPS.get(name, 0.0))
    fund = hz.load_funding(FUNDING[name]) if d['funding'] and name in FUNDING else None
    ts, eq = hz.run(DonchianEnsR49(**R1_CFG[name]), warm, bars, H4_MS, acct, fund)
    return ts, eq, acct


def r2_r3_decider(bars, retest):
    c, h, l, o = bars[:, C], bars[:, H], bars[:, L], bars[:, O]
    e20 = ta.ema(bars, period=20, sequential=True)
    e80 = ta.ema(bars, period=80, sequential=True)
    atr = ta.atr(bars, period=14, sequential=True)
    adx = ta.adx(bars, period=14, sequential=True)
    rsi = ta.rsi(bars, period=14, sequential=True)
    hh26 = en.prior_max(h, 26)
    st = {'limit': None}

    def setup(i):
        return (i >= 100 and np.isfinite([e20[i], e80[i], e80[i - 4], atr[i], adx[i], rsi[i], hh26[i]]).all()
                and atr[i] > 0 and c[i] > e80[i] and e20[i] > e80[i] > e80[i - 4] and adx[i] >= 26
                and 52 <= rsi[i] <= 76 and h[i] - l[i] <= 3 * atr[i])

    def open_pos(acct, i, price, dist, ts, fee):
        q = risk_qty(acct, price, dist)
        if q > 0:
            _trade(acct, q, price, ts, fee)
            # Core4h measures R progress on the highest high; K1001 on the best close.
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
            px, dist = st['limit']
            st['limit'] = None
            if l[i] < px:
                open_pos(acct, i, px, dist, ts, MAKER)
                if acct.is_open and l[i] <= st['stop']:  # same-bar stop after the fill
                    _trade(acct, -acct.qty, st['stop'] * (1 - STOP_SLIP), ts, TAKER)
                return
        if not setup(i):
            return
        if retest:
            entry = hh26[i]
            if entry < c[i] <= entry + atr[i] and 0 < 2 * atr[i] < entry:
                st['limit'] = (entry, 2 * atr[i])
        elif c[i] > hh26[i]:
            frac = max(2 * atr[i] / c[i], 0.008)
            if frac <= 0.055:
                open_pos(acct, i, c[i], frac * c[i], ts, TAKER)
    return decide


def r4_decider(bars):
    c, h, l, o = bars[:, C], bars[:, H], bars[:, L], bars[:, O]
    hh55 = en.prior_max(h, 55)
    a20 = ta.atr(bars, period=20, sequential=True)
    st = {}

    def decide(i, acct, ts):
        if acct.is_open:
            if stop_exit(acct, st, o, l, i, ts):
                return
            lo10 = l[max(0, i - 9):i + 1].min()
            if st['stop'] < lo10 < c[i]:
                st['stop'] = lo10
            return
        if i >= 56 and np.isfinite(hh55[i]) and np.isfinite(a20[i]) and a20[i] > 0 and c[i] > hh55[i]:
            dist = 2 * a20[i]
            q = risk_qty(acct, c[i], dist)
            if q > 0 and dist < c[i]:
                _trade(acct, q, c[i], ts, TAKER)
                st['stop'] = c[i] - dist
    return decide


def r5_decider(h4, daily, cfd):
    c, l = h4[:, C], h4[:, L]
    r2 = rsi2(c)
    s5 = sma(c, 5)
    d_close_ts = daily[:, T].astype(np.int64) + DAY_MS
    d_ok = daily[:, C] > sma(daily[:, C], 200)
    d_vol = ann_vol(daily[:, C], cfd)
    st = {'limit': None, 'held': 0}

    def dctx(i):
        j = int(np.searchsorted(d_close_ts, int(h4[i, T]) + H4_MS, side='right')) - 1
        return (bool(d_ok[j]), d_vol[j]) if j >= 200 else (False, np.nan)

    def exit_now(i):
        return st['held'] >= 30 or (np.isfinite(s5[i]) and c[i] > s5[i])

    def decide(i, acct, ts):
        if acct.is_open:
            st['held'] += 1
            if exit_now(i):
                _trade(acct, -acct.qty, c[i], ts, TAKER)
            return
        if st['limit'] is not None:
            px, qty = st['limit']
            st['limit'] = None
            if l[i] < px:
                _trade(acct, qty, px, ts, MAKER)
                st['held'] = 1
                if exit_now(i):
                    _trade(acct, -acct.qty, c[i], ts, TAKER)
                return
        ok, vol = dctx(i)
        if ok and np.isfinite(r2[i]) and r2[i] < 10 and np.isfinite(vol) and vol > 0:
            st['limit'] = (c[i], acct.equity(c[i]) * min(MAX_X, TARGET_VOL / vol) / c[i])
    return decide


def daily_ensemble_frac(bars):
    """Fraction of active components of the 20/55/120/250-bar Donchian ensemble on daily bars,
    advanced with the same step rule as the validated r49 engine."""
    eng = DonchianEnsR49(candles_per_day=1, ann_days=365)
    h, l, c = bars[:, H], bars[:, L], bars[:, C]
    states, out = [0] * 4, np.zeros(len(bars))
    for i in range(len(bars)):
        states = eng._step(states, h, l, c, i)
        out[i] = sum(states) / 4
    return out


def n1_decider(bars, cfd):
    c, l, h = bars[:, C], bars[:, L], bars[:, H]
    frac = daily_ensemble_frac(bars)
    r2, s5 = rsi2(c), sma(c, 5)
    vol = ann_vol(c, cfd)
    st = {'limit': None, 'held': 0}

    def exit_now(i):
        return st['held'] >= 5 or (np.isfinite(s5[i]) and c[i] > s5[i])

    def decide(i, acct, ts):
        if acct.is_open:
            st['held'] += 1
            if exit_now(i):
                _trade(acct, -acct.qty, c[i], ts, TAKER)
            return
        if st['limit'] is not None:
            px, qty = st['limit']
            st['limit'] = None
            if l[i] < px:
                _trade(acct, qty, px, ts, MAKER)
                st['held'] = 1
                if exit_now(i):
                    _trade(acct, -acct.qty, c[i], ts, TAKER)
                return
        if frac[i] >= 0.5 and np.isfinite(r2[i]) and r2[i] < 10 and np.isfinite(vol[i]) and vol[i] > 0:
            st['limit'] = (c[i], acct.equity(c[i]) * min(MAX_X, TARGET_VOL / vol[i]) / c[i])
    return decide


def n2_decider(bars):
    c, h, l, o = bars[:, C], bars[:, H], bars[:, L], bars[:, O]
    mid = sma(c, 20)
    sd = np.full(len(c), np.nan)
    for i in range(19, len(c)):
        sd[i] = np.std(c[i - 19:i + 1])  # population std, as Bollinger bands
    upper = mid + 2 * sd
    bw = 4 * sd / mid
    low_bw = np.zeros(len(c), dtype=bool)
    for j in range(250, len(c)):
        prior = bw[j - 250:j]
        prior = prior[np.isfinite(prior)]
        low_bw[j] = len(prior) > 200 and np.isfinite(bw[j]) and bw[j] <= np.percentile(prior, 20)
    a20 = ta.atr(bars, period=20, sequential=True)
    st = {}

    def decide(i, acct, ts):
        if acct.is_open:
            if stop_exit(acct, st, o, l, i, ts):
                return
            chandelier(st, c[i], a20[i], 4.2, 2.25, TAKER, False)
            return
        if i >= 256 and low_bw[i - 5:i].any() and np.isfinite(upper[i]) and c[i] > upper[i] \
                and np.isfinite(a20[i]) and a20[i] > 0:
            dist = 2 * a20[i]
            q = risk_qty(acct, c[i], dist)
            if q > 0 and dist < c[i]:
                _trade(acct, q, c[i], ts, TAKER)
                st.update(entry=c[i], r=dist, stop=c[i] - dist, best_close=c[i])
    return decide


def _month_end_flags(bars):
    months = [datetime.fromtimestamp(int(t) / 1000, tz=timezone.utc).strftime('%Y-%m') for t in bars[:, T]]
    return np.array([k + 1 < len(months) and months[k + 1] != months[k] for k in range(len(months))]), months


def n3_decider(bars, cfd):
    c = bars[:, C]
    vol = ann_vol(c, cfd)
    is_me, _ = _month_end_flags(bars)
    st = {'closes': []}

    def decide(i, acct, ts):
        if not is_me[i]:
            return
        st['closes'].append(c[i])
        if len(st['closes']) < 10 or not np.isfinite(vol[i]) or vol[i] <= 0:
            return
        long_ = c[i] > np.mean(st['closes'][-10:])
        target = acct.equity(c[i]) * min(MAX_X, TARGET_VOL / vol[i]) / c[i] if long_ else 0.0
        rebalance(acct, target, c[i], ts)
    return decide


def r6_rotation(data, window, mfrom):
    """Monthly 3-of-7 dual momentum on a shared book (protocol R6). Returns (days, vals, entries)."""
    names = [n for n in data if data[n] is not None]
    to = COMMON[1]
    start = max(hz._ms(mfrom), min(int(data[n]['daily'][0, T]) for n in names))
    days = np.arange(start, hz._ms(to), DAY_MS)
    closes, vols, rets, avail = {}, {}, {}, {}
    for n in names:
        b = data[n]['daily']
        idx = np.searchsorted(b[:, T].astype(np.int64) + DAY_MS, days + DAY_MS, side='right') - 1
        px = np.where(idx >= 0, b[np.clip(idx, 0, None), C], np.nan)
        closes[n] = px
        rets[n] = np.r_[0.0, np.nan_to_num(px[1:] / px[:-1] - 1)]
        v = ann_vol(b[:, C], data[n]['cfd'])
        vols[n] = np.where(idx >= 0, v[np.clip(idx, 0, None)], np.nan)
        r63 = np.r_[np.full(63, np.nan), b[63:, C] / b[:-63, C] - 1]
        avail[n] = (np.where(idx >= 0, r63[np.clip(idx, 0, None)], np.nan), idx)
    fund_daily = {}
    for n in names:
        if data[n]['funding'] and n in FUNDING:
            eff, _, rate = hz.load_funding(FUNDING[n])
            dd = (eff // DAY_MS) * DAY_MS
            s = {}
            for t, r in zip(dd, rate):
                s[int(t)] = s.get(int(t), 0.0) + r
            fund_daily[n] = np.array([s.get(int(t), 0.0) for t in days])
    w = {n: 0.0 for n in names}
    vals, entries, v_ = [], 0, BALANCE
    months = [datetime.fromtimestamp(int(t) / 1000, tz=timezone.utc).strftime('%Y-%m') for t in days]
    for k, t in enumerate(days):
        if k > 0:
            r = sum(w[n] * rets[n][k] for n in names)
            r -= sum(w[n] * fund_daily[n][k] for n in fund_daily)
            v_ *= 1 + r
        if k + 1 < len(days) and months[k + 1] != months[k]:
            scores = []
            for n in names:
                sc, idx = avail[n]
                if idx[k] >= 126 and np.isfinite(sc[k]) and sc[k] > 0 and np.isfinite(vols[n][k]) and vols[n][k] > 0:
                    scores.append((sc[k], n))
            top = [n for _, n in sorted(scores, reverse=True)[:3]]
            new = {n: (min(MAX_X, TARGET_VOL / vols[n][k]) / 3 if n in top else 0.0) for n in names}
            for n in names:
                dw = abs(new[n] - w[n])
                if dw > 0:
                    v_ *= 1 - dw * (TAKER + SLIP_BPS.get(n, 0.0) / 1e4)
                if new[n] > 0 and w[n] == 0:
                    entries += 1
            w = new
        vals.append(v_)
    return days, np.array(vals), entries


# ----------------------------------------------------------------------------------------------
# DSR and runner
# ----------------------------------------------------------------------------------------------
def dsr(vals, n_trials):
    """Deflated Sharpe (Bailey & Lopez de Prado) on daily returns; the expected max of n null
    Sharpe ratios uses an estimator variance of 1/T, as in r49."""
    r = np.diff(vals) / vals[:-1]
    t = len(r)
    if t < 30 or r.std(ddof=1) == 0:
        return None
    sr = r.mean() / r.std(ddof=1)
    z = (r - r.mean()) / r.std(ddof=0)
    skew, kurt = float((z ** 3).mean()), float((z ** 4).mean())
    nd, g = NormalDist(), 0.5772156649
    sr0 = math.sqrt(1 / t) * ((1 - g) * nd.inv_cdf(1 - 1 / n_trials) + g * nd.inv_cdf(1 - 1 / (n_trials * math.e)))
    den = math.sqrt(max(1 - skew * sr + (kurt - 1) / 4 * sr ** 2, 1e-12))
    return float(nd.cdf((sr - sr0) * math.sqrt(t - 1) / den))


def basket(curves, members):
    series = [daily_returns(*curves[m]) for m in members if m in curves]
    if not series:
        return None
    all_days = sorted(set().union(*[s.keys() for s in series]))
    r = np.array([np.mean([s[d] for s in series if d in s]) for d in all_days])
    v = BALANCE * np.r_[1.0, np.cumprod(1 + r)]
    dd = np.r_[all_days[0] - DAY_MS, all_days]
    return np.array(dd), v


def _quarter(t):
    dt = datetime.fromtimestamp(t / 1000, tz=timezone.utc)
    return f'{dt.year}Q{(dt.month - 1) // 3 + 1}'


def corr_in_losing(base, other):
    a, b = daily_returns(*base), daily_returns(*other)
    q = {}
    for t, x in a.items():
        q[_quarter(t)] = (1 + q.get(_quarter(t), 0.0)) * (1 + x) - 1
    lose = {k for k, x in q.items() if x < 0}
    ds = [t for t in a if t in b and _quarter(t) in lose]
    x, y = np.array([a[t] for t in ds]), np.array([b[t] for t in ds])
    return (float(np.corrcoef(x, y)[0, 1]) if len(ds) > 10 and x.std() > 0 and y.std() > 0 else None), len(lose)


def screen():
    out = {'protocol': 'RESEARCH_HUB/revisions/20261024-r50/PHASE1B_PROTOCOL.md', 'n_declared': N_DECLARED,
           'assets': {}, 'baskets': {}}
    curves, trades = {}, {}
    for window in ('common', 'long'):
        data = {}
        for name in CORE:
            if ASSETS[name][window] is None:
                out['assets'].setdefault(name, {})[window] = {'status': 'sin lente larga (límite declarado)'}
                continue
            d = load_both(name, window)
            data[name] = d
            if d is None:
                out['assets'].setdefault(name, {})[window] = {'error': 'insufficient data'}
                continue
            rec = {'source': d['source'], 'first_daily': hz._date(int(d['daily'][0, T])), 'funding': d['funding']}
            runs = {'R1': lambda: r1_run(name, d),
                    'R2': lambda: simulate(d['h4'], d['start_ms'], r2_r3_decider(d['h4'], False), name, d['funding'], H4_MS),
                    'R3': lambda: simulate(d['h4'], d['start_ms'], r2_r3_decider(d['h4'], True), name, d['funding'], H4_MS),
                    'R4': lambda: simulate(d['daily'], d['start_ms'], r4_decider(d['daily']), name, d['funding']),
                    'R5': lambda: simulate(d['h4'], d['start_ms'], r5_decider(d['h4'], d['daily'], d['cfd']), name, d['funding'], H4_MS),
                    'N1': lambda: simulate(d['daily'], d['start_ms'], n1_decider(d['daily'], d['cfd']), name, d['funding']),
                    'N2': lambda: simulate(d['daily'], d['start_ms'], n2_decider(d['daily']), name, d['funding']),
                    'N3': lambda: simulate(d['daily'], d['start_ms'], n3_decider(d['daily'], d['cfd']), name, d['funding'])}
            if name in en.M2_BASKET:  # M2a of F1, unchanged, only as the N4 ingredient
                runs['M2a'] = lambda: simulate(d['daily'], d['start_ms'], en.m2_decider(d['daily'], d['cfd'], 'a'), name, d['funding'])
            last = d['daily'][-1, C]
            for cand, fn in runs.items():
                ts, eq, acct = fn()
                days, vals = calendar(ts, eq, d['mfrom'], COMMON[1])
                tr = acct.trades + ([{'opened': 0, 'closed': int(ts[-1]), 'pnl': acct.upnl(last), 'side': 1.0}]
                                    if acct.is_open else [])
                mt = metrics(days, vals, tr, d['mfrom']) or {'error': 'too short'}
                mt.update(fees_paid=acct.fees_paid, funding_paid=acct.funding_paid)
                rec[cand] = mt
                curves[(cand, window, name)] = (days, vals)
                trades.setdefault((cand, window), []).extend(t['pnl'] for t in tr if t['closed'] >= hz._ms(d['mfrom']))
            out['assets'].setdefault(name, {})[window] = rec
            hz.jh.debug(f'{name} {window}: ' + json.dumps({k: round(v['sharpe'], 2) for k, v in rec.items()
                                                           if isinstance(v, dict) and 'sharpe' in v}))
        mfrom = MEASURE_FROM if window == 'common' else min(
            data[n]['mfrom'] for n in data if data[n] is not None)
        r6 = r6_rotation({n: data[n] for n in data}, window, mfrom)
        curves[('R6', window, 'BOOK')] = (r6[0], r6[1])
        trades[('R6', window)] = None
        r6_entries = r6[2]
        for cand in ['R1', 'R2', 'R3', 'R4', 'R5', 'N1', 'N2', 'N3', 'M2a']:
            members = [n for n in CORE if (cand, window, n) in curves]
            bk = basket(curves, [(cand, window, n) for n in members])
            if bk is None:
                continue
            curves[(cand, window, 'BASKET')] = bk
            m = metrics(bk[0], bk[1], [], datetime.fromtimestamp(bk[0][0] / 1000, tz=timezone.utc).date().isoformat())
            pnl = trades.get((cand, window), [])
            tot = sum(pnl)
            m.update(members=members, trades_per_year=sum(out['assets'][n][window][cand]['trades_per_year'] for n in members),
                     top5_share=(sum(sorted(pnl, reverse=True)[:5]) / tot) if tot > 0 else None,
                     dsr=dsr(bk[1], N_DECLARED))
            out['baskets'].setdefault(cand, {})[window] = m
        m6 = metrics(r6[0], r6[1], [], datetime.fromtimestamp(r6[0][0] / 1000, tz=timezone.utc).date().isoformat())
        m6.update(trades_per_year=r6_entries / (len(r6[0]) / 365), entries=r6_entries, top5_share=None, dsr=dsr(r6[1], N_DECLARED))
        out['baskets'].setdefault('R6', {})[window] = m6
        curves[('R6', window, 'BASKET')] = curves[('R6', window, 'BOOK')]
        if ('R1', window, 'BASKET') in curves and ('M2a', window, 'BASKET') in curves:
            n4 = basket({('R1', window, 'X'): curves[('R1', window, 'BASKET')],
                         ('M2a', window, 'X'): curves[('M2a', window, 'BASKET')]},
                        [('R1', window, 'X'), ('M2a', window, 'X')])
            curves[('N4', window, 'BASKET')] = n4
            m4 = metrics(n4[0], n4[1], [], datetime.fromtimestamp(n4[0][0] / 1000, tz=timezone.utc).date().isoformat())
            m4.update(dsr=dsr(n4[1], N_DECLARED), top5_share=None,
                      trades_per_year=out['baskets']['R1'][window]['trades_per_year'] + out['baskets']['M2a'][window]['trades_per_year'])
            out['baskets'].setdefault('N4', {})[window] = m4
        for cand in ['R2', 'R3', 'R4', 'R5', 'R6', 'N1', 'N2', 'N3', 'N4', 'M2a']:
            if (cand, window, 'BASKET') in curves and cand in out['baskets'] and window in out['baskets'][cand]:
                c_, nl = corr_in_losing(curves[('R1', window, 'BASKET')], curves[(cand, window, 'BASKET')])
                out['baskets'][cand][window]['corr_r1_losing_quarters'] = c_
                out['baskets'][cand][window]['r1_losing_quarters'] = nl
                a, b = daily_returns(*curves[('R1', window, 'BASKET')]), daily_returns(*curves[(cand, window, 'BASKET')])
                ds = [t for t in a if t in b]
                out['baskets'][cand][window]['corr_r1'] = float(np.corrcoef([a[t] for t in ds], [b[t] for t in ds])[0, 1])
    out['gates'] = gates(out['baskets'])
    os.makedirs(hz.OUT_DIR, exist_ok=True)
    with open(os.path.join(hz.OUT_DIR, 'f1b_screen.json'), 'w') as fh:
        json.dump(out, fh, indent=2, default=float)
    hz.jh.debug(json.dumps(out['gates'], indent=1, default=bool))
    return out


def gates(b):
    """PHASE1B_PROTOCOL.md section 3."""
    r1 = b['R1']['common']
    res = {}
    for cand, role in ROLE.items():
        if cand not in b or 'common' not in b[cand]:
            res[cand] = {'error': 'missing'}
            continue
        c, l = b[cand]['common'], b[cand].get('long')
        g = {'role': role}
        if role == 'trend':
            # Plain Python bools: a numpy bool_ False is not `False`, which silently skipped the
            # top-5 gate in the first F1b evaluation (technical correction, 2026-10-25).
            g['sharpe_ge_0_8'] = bool(c['sharpe'] >= 0.8)
            g['top5_lt_60pct'] = None if c.get('top5_share') is None else bool(c['top5_share'] < 0.6)
            g['beats_r1'] = True if cand == 'R1' else bool(c['sharpe'] > r1['sharpe'] or c['quarters_pos'] > r1['quarters_pos'])
            core = g['sharpe_ge_0_8'] and g['top5_lt_60pct'] is not False and g['beats_r1']
        elif role == 'diversifier':
            g['sharpe_ge_0_5'] = c['sharpe'] >= 0.5
            g['trades_ge_50'] = c['trades_per_year'] >= 50
            cr = c.get('corr_r1_losing_quarters')
            g['corr_losing_le_0_2'] = cr is not None and cr <= 0.2
            core = g['sharpe_ge_0_5'] and g['trades_ge_50'] and g['corr_losing_le_0_2']
        else:
            g['sharpe_gt_r1'] = c['sharpe'] > r1['sharpe']
            g['q_ge_r1'] = c['quarters_pos'] >= r1['quarters_pos']
            core = g['sharpe_gt_r1'] and g['q_ge_r1']
        g['long_veto'] = (l is None) or l['sharpe'] < 0 or l['max_dd'] < -0.25
        g['pass'] = bool(core and not g['long_veto'])
        res[cand] = g
    return res


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'screen':
        screen()
    else:
        print(__doc__)


if __name__ == '__main__':
    sys.exit(main())
