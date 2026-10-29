"""r50 F1: engines M1-M4 and the screening runner, on top of the validated r50_harness.

The rules, defaults and falsification gates are fixed in
`strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r50/PHASE1_PROTOCOL.md`
(committed before any screening result). Nothing here may be tuned after looking at F1 output;
a changed rule is a new variant that counts in N.

    python research_scripts/r50_engines.py screen [--assets BTC,XAU,...]

writes `research_scripts/data/r50/f1_screen.json` with per engine x asset and basket metrics in
the common and long windows.
"""
import argparse
import json
import math
import os
import sys
from datetime import datetime, timezone

import numpy as np

import r50_harness as hz
from r50_harness import T, O, C, H, L, V, DAY_MS, Account, DonchianEnsR49

# ----------------------------------------------------------------------------------------------
# Protocol constants (PHASE1_PROTOCOL.md section 1)
# ----------------------------------------------------------------------------------------------
TAKER = 0.00045
MAKER = 0.00018
STOP_SLIP = 5e-4          # 5 bps adverse on stop fills
TARGET_VOL = 0.17
MAX_X = 2.0
BAND = 0.25
VOL_BARS = 30
BALANCE = 10_000.0
LEVERAGE = 5.0            # isolated 5x ceiling of r49; MAX_X keeps real exposure <= 2x
COMMON = ('2020-10-15', '2026-01-01')
MEASURE_FROM = '2021-01-01'
FUNDING = {'BTC': '0ab14bc27fbc9a76ac754bb351f220fc5ac89d874cc062baf17cd690983b86ca',
           'ETH': '22bd891cf5f5e4eccbcaa33e60a607a1c5f16e6ae917845b92a827e32b72893b'}
ENERGY_HOURS = {'timezone': 'America/New_York',
                'hours': {'Sun': '18:00-24:00', 'Mon-Thu': ['00:00-17:00', '18:00-24:00'], 'Fri': '00:00-17:00'}}
SPX_HOURS = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}

# Asset table. `cfd` assets merge weekend minutes into Monday and annualize vol with 252 bars;
# crypto keeps calendar days and 365. `long` is the veto-lens source (spot for crypto).
ASSETS = {
    'BTC': dict(common=('Binance Perpetual Futures', 'BTC-USDT'), long=('Binance Spot', 'BTC-USDT'),
                long_start='2017-08-17', cfd=False, m1='long', null=dict(candles_per_day=6, ann_days=365)),
    'ETH': dict(common=('Binance Perpetual Futures', 'ETH-USDT'), long=('Binance Spot', 'ETH-USDT'),
                long_start='2017-08-17', cfd=False, m1=None, null=None),
    'XAU': dict(common=('Custom Data', 'XAU-USDT'), long=('Custom Data', 'XAU-USDT'),
                long_start='2011-01-01', cfd=True, m1='long', null=dict(candles_per_day=6, ann_days=365)),
    'SPX': dict(common=('Custom Data', 'SPXD-USDT'), long=('Custom Data', 'SPXD-USDT'),
                long_start='2012-01-16', cfd=True, m1='long',
                null=dict(candles_per_day=5, ann_days=252, hours=SPX_HOURS)),
    'WTI': dict(common=('Custom Data', 'WTI-USDT'), long=('Custom Data', 'WTI-USDT'),
                long_start='2011-12-01', cfd=True, m1='ls',
                null=dict(candles_per_day=6, ann_days=252, hours=ENERGY_HOURS)),
    'GAS': dict(common=('Custom Data', 'NATGAS-USDT'), long=('Custom Data', 'NATGAS-USDT'),
                long_start='2010-01-01', cfd=True, m1='ls',
                null=dict(candles_per_day=6, ann_days=252, hours=ENERGY_HOURS)),
    # Dukascopy USTBOND only has data from 2018-03; by the user's decision the bond has no long
    # lens (it cannot be vetoed by long history, reported as a limit).
    'BOND': dict(common=('Custom Data', 'USTBOND-USDT'), long=None,
                 long_start=None, cfd=True, m1='ls',
                 null=dict(candles_per_day=6, ann_days=252, hours=ENERGY_HOURS)),
}
# Extra adverse slippage per side on taker fills and stops (protocol amendment 4b, measured
# Binance books: TMF/TBT 3-6k depth at +-0.2%, NATGAS 0.09-0.14 M). Maker fills carry none.
SLIP_BPS = {'BOND': 15.0, 'GAS': 5.0, 'COPPER': 5.0, 'EWJ': 10.0, 'XPT': 10.0}
M2_BASKET = ['XAU', 'SPX', 'WTI', 'GAS', 'BOND']
M3_BASKET = ['BTC', 'ETH', 'XAU', 'SPX', 'WTI', 'GAS', 'BOND']
M1_BASKET = ['BTC', 'XAU', 'SPX', 'WTI', 'GAS', 'BOND']


# ----------------------------------------------------------------------------------------------
# Daily bars
# ----------------------------------------------------------------------------------------------
def load_daily(exchange, symbol, start, finish, cfd, warmup_days=400):
    """UTC daily bars [ts, o, c, h, l, v]; CFD weekend minutes join Monday's bar.

    Returns bars opening in [start - warmup_days, finish); the caller measures from `start`.
    """
    s_ms, f_ms = hz._ms(start) - warmup_days * DAY_MS, hz._ms(finish)
    if f_ms > hz.RESERVED_FROM_MS:
        raise ValueError('r50: data after 2025-12-31 is reserved')
    return daily_from_minutes(hz._minutes(exchange, symbol, s_ms, f_ms), cfd, f_ms)


def daily_from_minutes(m, cfd, f_ms):
    """Aggregate 1m rows into UTC daily bars; CFD Saturday/Sunday minutes join Monday."""
    if not len(m):
        return np.zeros((0, 6))
    day = (m[:, T].astype(np.int64) // DAY_MS) * DAY_MS
    if cfd:
        wd = ((day // DAY_MS) + 3) % 7  # 0 = Monday (1970-01-01 was a Thursday)
        day = np.where(wd == 5, day + 2 * DAY_MS, np.where(wd == 6, day + DAY_MS, day))
        # The trailing weekend of the final week has no Monday inside the window.
        keep = day < f_ms
        m, day = m[keep], day[keep]
    cut = np.flatnonzero(np.diff(day)) + 1
    starts, stops = np.r_[0, cut], np.r_[cut, len(m)]
    out = np.empty((len(starts), 6))
    out[:, T] = day[starts]
    out[:, O] = m[starts, O]
    out[:, C] = m[stops - 1, C]
    out[:, H] = np.maximum.reduceat(m[:, H], starts)
    out[:, L] = np.minimum.reduceat(m[:, L], starts)
    out[:, V] = np.add.reduceat(m[:, V], starts)
    return out


# ----------------------------------------------------------------------------------------------
# Indicators (causal: value at i uses bars <= i)
# ----------------------------------------------------------------------------------------------
def sma(x, n):
    out = np.full(len(x), np.nan)
    if len(x) >= n:
        c = np.cumsum(np.r_[0.0, x])
        out[n - 1:] = (c[n:] - c[:-n]) / n
    return out


def rolling_std(x, n):
    out = np.full(len(x), np.nan)
    for i in range(n - 1, len(x)):
        out[i] = np.std(x[i - n + 1:i + 1], ddof=1)
    return out


def logret(c):
    return np.r_[np.nan, np.diff(np.log(c))]


def rsi2(c):
    """Wilder RSI(2)."""
    d = np.diff(c)
    up, dn = np.maximum(d, 0), np.maximum(-d, 0)
    out = np.full(len(c), np.nan)
    if len(d) < 2:
        return out
    au, ad = up[:2].mean(), dn[:2].mean()
    for k in range(2, len(d) + 1):
        if k > 2:
            au = (au * 1 + up[k - 1]) / 2
            ad = (ad * 1 + dn[k - 1]) / 2
        out[k] = 100.0 if ad == 0 else 100 - 100 / (1 + au / ad)
    return out


def atr(b, n=20):
    prev = np.r_[b[0, C], b[:-1, C]]
    tr = np.maximum(b[:, H] - b[:, L], np.maximum(abs(b[:, H] - prev), abs(b[:, L] - prev)))
    return sma(tr, n)


def prior_max(x, n):
    out = np.full(len(x), np.nan)
    for i in range(n, len(x)):
        out[i] = x[i - n:i].max()
    return out


def prior_min(x, n):
    out = np.full(len(x), np.nan)
    for i in range(n, len(x)):
        out[i] = x[i - n:i].min()
    return out


def ann_vol(c, cfd):
    return rolling_std(logret(c), VOL_BARS) * math.sqrt(252 if cfd else 365)


# ----------------------------------------------------------------------------------------------
# Simulation helpers
# ----------------------------------------------------------------------------------------------
def _trade(acct, dqty, price, ts, fee):
    acct.fee = fee
    acct.trade(dqty, price, ts, slippage=fee != MAKER)
    acct.fee = TAKER


def rebalance(acct, target, price, ts):
    """Move to a signed target quantity with the r49 25% band; sign flips close first."""
    cur = acct.qty
    if abs(target) < 1e-12:
        if acct.is_open:
            _trade(acct, -cur, price, ts, TAKER)
        return
    if not acct.is_open or np.sign(target) != np.sign(cur):
        if acct.is_open:
            _trade(acct, -cur, price, ts, TAKER)
        _trade(acct, target, price, ts, TAKER)
        return
    if abs(target) > abs(cur) * (1 + BAND) or abs(target) < abs(cur) * (1 - BAND):
        _trade(acct, target - cur, price, ts, TAKER)


def _funding_cursor(name, bars):
    if name not in FUNDING:
        return None
    eff, mark, rate = hz.load_funding(FUNDING[name])
    return [eff, mark, rate, int(np.searchsorted(eff, bars[0, T], side='left'))]


def _pay(acct, fc, close_ts):
    if fc is None:
        return
    eff, mark, rate, i = fc
    while i < len(eff) and eff[i] <= close_ts and eff[i] < hz.RESERVED_FROM_MS:
        acct.pay_funding(mark[i], rate[i])
        i += 1
    fc[3] = i


def simulate(bars, start_ms, decide, name=None, use_funding=False, tf_ms=DAY_MS):
    """Bar loop (daily by default) from the first bar opening at/after start_ms.
    `decide(i, acct, close_ts)` places orders. Returns (close_ts array, equity array, Account)."""
    acct = Account(BALANCE, TAKER, LEVERAGE, SLIP_BPS.get(name, 0.0))
    k0 = int(np.searchsorted(bars[:, T], start_ms, side='left'))
    fc = _funding_cursor(name, bars[k0:]) if use_funding and k0 < len(bars) else None
    ts_out, eq_out = [], []
    for i in range(k0, len(bars)):
        close_ts = int(bars[i, T]) + tf_ms
        _pay(acct, fc, close_ts)
        decide(i, acct, close_ts)
        ts_out.append(close_ts)
        eq_out.append(acct.equity(bars[i, C]))
    return np.array(ts_out, dtype=np.int64), np.array(eq_out), acct


# ----------------------------------------------------------------------------------------------
# Engines (PHASE1_PROTOCOL.md section 2)
# ----------------------------------------------------------------------------------------------
def m1_decider(bars, cfd, side):
    c = bars[:, C]
    lr = logret(c)
    sd60 = rolling_std(lr, 60)
    vol = ann_vol(c, cfd)
    sig = np.zeros(len(c))
    for n in (15, 60, 250):
        rn = np.r_[np.full(n, np.nan), np.log(c[n:] / c[:-n])]
        s = np.clip(rn / (sd60 * math.sqrt(n)), -2, 2) / 2
        sig += np.nan_to_num(s) / 3
    if side == 'long':
        sig = np.maximum(sig, 0)

    def decide(i, acct, ts):
        if not np.isfinite(vol[i]) or vol[i] <= 0 or i < 250:
            return
        x = sig[i] * min(MAX_X / max(abs(sig[i]), 1e-12), TARGET_VOL / vol[i]) if sig[i] else 0.0
        rebalance(acct, acct.equity(c[i]) * x / c[i], c[i], ts)
    return decide


def m2_decider(bars, cfd, variant):
    c, h, l = bars[:, C], bars[:, H], bars[:, L]
    s200, s5 = sma(c, 200), sma(c, 5)
    r2 = rsi2(c)
    rng = np.where(h > l, h - l, np.nan)
    ibs = (c - l) / rng
    vol = ann_vol(c, cfd)
    st = {'limit': None, 'held': 0}

    def signal(i):
        if not (np.isfinite(s200[i]) and c[i] > s200[i]):
            return False
        if variant == 'a':
            return np.isfinite(r2[i]) and r2[i] < 10
        return np.isfinite(ibs[i]) and ibs[i] < 0.2

    def exit_now(i):
        if st['held'] >= 5:
            return True
        if variant == 'a':
            return np.isfinite(s5[i]) and c[i] > s5[i]
        return (np.isfinite(ibs[i]) and ibs[i] > 0.8) or c[i] > h[i - 1]

    def decide(i, acct, ts):
        if acct.is_open:
            st['held'] += 1
            if exit_now(i):
                _trade(acct, -acct.qty, c[i], ts, TAKER)
            return
        if st['limit'] is not None:
            px, qty = st['limit']
            st['limit'] = None
            if l[i] < px:  # maker fill strictly through the limit
                _trade(acct, qty, px, ts, MAKER)
                st['held'] = 1
                if exit_now(i):  # exits are judged from the fill bar's close
                    _trade(acct, -acct.qty, c[i], ts, TAKER)
                return
        if signal(i) and np.isfinite(vol[i]) and vol[i] > 0:
            x = min(MAX_X, TARGET_VOL / vol[i])
            st['limit'] = (c[i], acct.equity(c[i]) * x / c[i])
    return decide


def m3_decider(bars, cfd, regime=True):
    c, h, l, o = bars[:, C], bars[:, H], bars[:, L], bars[:, O]
    s200, s50 = sma(c, 200), sma(c, 50)
    lo20, hi10 = prior_min(l, 20), prior_max(h, 10)
    a20 = atr(bars, 20)
    vol = ann_vol(c, cfd)
    st = {'stop': None, 'held': 0}

    def decide(i, acct, ts):
        if acct.is_open:
            st['held'] += 1
            stop = st['stop']
            if h[i] >= stop:
                px = max(stop, o[i]) * (1 + STOP_SLIP)
                _trade(acct, -acct.qty, px, ts, TAKER)
            elif (np.isfinite(hi10[i]) and c[i] > hi10[i]) or st['held'] >= 20:
                _trade(acct, -acct.qty, c[i], ts, TAKER)
            return
        reg = (np.isfinite(s200[i]) and c[i] < s200[i] and i >= 5 and np.isfinite(s50[i - 5])
               and s50[i] < s50[i - 5]) if regime else True
        if reg and np.isfinite(lo20[i]) and c[i] < lo20[i] and np.isfinite(vol[i]) and vol[i] > 0 \
                and np.isfinite(a20[i]):
            x = min(MAX_X, TARGET_VOL / vol[i])
            _trade(acct, -acct.equity(c[i]) * x / c[i], c[i], ts, TAKER)
            st['stop'] = c[i] + 2 * a20[i]
            st['held'] = 0
    return decide


def run_m4(eth, btc, start_ms, use_funding):
    """Two legs on a shared 10k: short ETH / long BTC equal notional when the ratio's
    4/8/12-week momentum is negative (exposure = fraction of the three)."""
    common = np.intersect1d(eth[:, T], btc[:, T])
    e = eth[np.isin(eth[:, T], common)]
    b = btc[np.isin(btc[:, T], common)]
    ratio = e[:, C] / b[:, C]
    spread = logret(e[:, C]) - logret(b[:, C])
    svol = rolling_std(spread, VOL_BARS) * math.sqrt(365)
    expo = np.zeros(len(ratio))
    for n in (28, 56, 84):
        rn = np.r_[np.full(n, np.nan), np.log(ratio[n:] / ratio[:-n])]
        expo += (np.nan_to_num(rn, nan=0.0) < 0) / 3
    ae, ab = Account(BALANCE / 2, TAKER, LEVERAGE), Account(BALANCE / 2, TAKER, LEVERAGE)
    k0 = int(np.searchsorted(e[:, T], start_ms, side='left'))
    fe = _funding_cursor('ETH', e[k0:]) if use_funding else None
    fb = _funding_cursor('BTC', b[k0:]) if use_funding else None
    ts_out, eq_out, trades = [], [], 0
    for i in range(k0, len(e)):
        ts = int(e[i, T]) + DAY_MS
        _pay(ae, fe, ts)
        _pay(ab, fb, ts)
        eq = ae.equity(e[i, C]) + ab.equity(b[i, C])
        if np.isfinite(svol[i]) and svol[i] > 0 and i >= 84:
            notional = eq * expo[i] * min(MAX_X, TARGET_VOL / svol[i])
            before = ae.orders + ab.orders
            rebalance(ae, -notional / e[i, C], e[i, C], ts)
            rebalance(ab, notional / b[i, C], b[i, C], ts)
        ts_out.append(ts)
        eq_out.append(ae.equity(e[i, C]) + ab.equity(b[i, C]))
    # Trades: a cycle is one open/close of the ETH short leg (BTC leg mirrors it).
    return np.array(ts_out, dtype=np.int64), np.array(eq_out), ae, ab


# ----------------------------------------------------------------------------------------------
# Metrics on calendar-daily curves
# ----------------------------------------------------------------------------------------------
def calendar(ts, eq, frm, to):
    """Equity per UTC calendar day in [frm, to), forward-filled through days without a bar."""
    days = np.arange(hz._ms(frm), hz._ms(to), DAY_MS)
    idx = np.searchsorted(ts, days + DAY_MS, side='right') - 1  # last close <= day end
    vals = np.where(idx >= 0, eq[np.clip(idx, 0, None)], BALANCE)
    return days, vals


def metrics(days, vals, trades, frm):
    m0 = int(np.searchsorted(days, hz._ms(frm)))
    d, v = days[m0:], vals[m0:]
    if len(v) < 30:
        return None
    r = np.diff(v) / v[:-1]
    sd = r.std(ddof=1)
    dates = [datetime.fromtimestamp(t / 1000, tz=timezone.utc).date().isoformat() for t in d]
    years = len(v) / 365.0
    closed = [t for t in trades if t['closed'] >= d[0]]
    pnl = sum(t['pnl'] for t in closed)
    top5 = sum(sorted((t['pnl'] for t in closed), reverse=True)[:5])
    top3 = sum(sorted((t['pnl'] for t in closed), reverse=True)[:3])
    return {
        'from': dates[0], 'to': dates[-1],
        'sharpe': float(r.mean() / sd * math.sqrt(365)) if sd > 0 else 0.0,
        'cagr': float((v[-1] / v[0]) ** (1 / years) - 1) if v[0] > 0 and v[-1] > 0 else -1.0,
        'max_dd': hz.max_dd(v),
        'quarters_pos': hz.quarters_positive(dates, v),
        'trades': len(closed), 'trades_per_year': len(closed) / years,
        'top5_share': float(top5 / pnl) if pnl > 0 else None,
        'top3_share': float(top3 / pnl) if pnl > 0 else None,
        'net_pnl_trades': float(pnl),
    }


def daily_returns(days, vals):
    return dict(zip(days[1:].tolist(), (np.diff(vals) / vals[:-1]).tolist()))


# ----------------------------------------------------------------------------------------------
# Screening runner
# ----------------------------------------------------------------------------------------------
def _null_curve(name, spec, frm, to, exch_sym):
    """r49 null (validated Donchian ensemble, 4h) on the same asset/window."""
    warm, bars, tf_ms = hz.load_bars(exch_sym[0], exch_sym[1], '4h', frm, to, 1520, lookback_days=500)
    if not len(bars):
        return None
    acct = Account(BALANCE, TAKER, 3)
    fund = hz.load_funding(FUNDING[name]) if (name in FUNDING and exch_sym[0].startswith('Binance Perp')) else None
    ts, eq = hz.run(DonchianEnsR49(**spec['null']), warm, bars, tf_ms, acct, fund)
    return ts, eq, acct


def screen(names):
    out = {'protocol': 'RESEARCH_HUB/revisions/20261024-r50/PHASE1_PROTOCOL.md', 'n_declared': 63,
           'assets': {}, 'baskets': {}}
    curves = {}  # (engine, window, asset) -> (days, vals)
    for name in names:
        spec = ASSETS[name]
        rec = {}
        for window in ('common', 'long'):
            exch_sym = spec[window]
            if exch_sym is None:
                rec[window] = {'status': 'sin lente larga (límite declarado)'}
                continue
            frm = COMMON[0] if window == 'common' else spec['long_start']
            to = COMMON[1]
            bars = load_daily(exch_sym[0], exch_sym[1], frm, to, spec['cfd'])
            if len(bars) < 300:
                rec[window] = {'error': f'insufficient data ({len(bars)} daily bars)'}
                continue
            # Long lens: measure only once the 250 d warmup is complete.
            first = max(hz._ms(frm), int(bars[0, T]))
            start_ms = first if window == 'common' else int(bars[min(260, len(bars) - 1), T])
            mfrom = MEASURE_FROM if window == 'common' else \
                datetime.fromtimestamp(start_ms / 1000, tz=timezone.utc).date().isoformat()
            fund = window == 'common' and exch_sym[0].startswith('Binance Perp')
            w = {'source': f'{exch_sym[0]} / {exch_sym[1]}', 'first_bar': hz._date(int(bars[0, T])),
                 'funding': bool(fund)}
            engines = {}
            if spec['m1']:
                engines['M1'] = m1_decider(bars, spec['cfd'], spec['m1'])
            if name in M2_BASKET:
                engines['M2a'] = m2_decider(bars, spec['cfd'], 'a')
                engines['M2b'] = m2_decider(bars, spec['cfd'], 'b')
            if name in M3_BASKET:
                engines['M3'] = m3_decider(bars, spec['cfd'], True)
                engines['M3nr'] = m3_decider(bars, spec['cfd'], False)
            for eng, dec in engines.items():
                ts, eq, acct = simulate(bars, start_ms, dec, name, fund)
                days, vals = calendar(ts, eq, mfrom, to)
                trades = acct.trades + ([{'opened': 0, 'closed': int(ts[-1]), 'pnl': acct.upnl(bars[-1, C])}]
                                        if acct.is_open else [])
                mt = metrics(days, vals, trades, mfrom)
                if mt and eng == 'M1' and spec['m1'] == 'ls':
                    mt['short_leg_pnl'] = float(sum(t['pnl'] for t in acct.trades if t.get('side', 0) < 0))
                mt = mt or {'error': 'too short'}
                mt['funding_paid'] = acct.funding_paid
                mt['fees_paid'] = acct.fees_paid
                w[eng] = mt
                curves[(eng, window, name)] = (days, vals)
            if spec['null']:
                nc = _null_curve(name, spec, frm if window == 'common' else mfrom, to, exch_sym)
                if nc:
                    days, vals = calendar(nc[0], nc[1], mfrom, to)
                    w['NULL_R49'] = metrics(days, vals, nc[2].trades, mfrom)
                    curves[('NULL', window, name)] = (days, vals)
            rec[window] = w
            hz.jh.debug(f'{name} {window} done: ' + json.dumps({k: (v.get('sharpe') if isinstance(v, dict) else v)
                                                                  for k, v in w.items()}))
        out['assets'][name] = rec
    # M4 needs both crypto assets.
    if 'BTC' in names and 'ETH' in names:
        for window in ('common', 'long'):
            frm = COMMON[0] if window == 'common' else ASSETS['ETH']['long_start']
            ex = ASSETS['ETH'][window][0]
            e = load_daily(ex, 'ETH-USDT', frm, COMMON[1], False)
            b = load_daily(ex, 'BTC-USDT', frm, COMMON[1], False)
            if min(len(e), len(b)) < 300:
                continue
            start_ms = max(hz._ms(frm), int(e[0, T]), int(b[0, T])) if window == 'common' else int(e[100, T])
            mfrom = MEASURE_FROM if window == 'common' else \
                datetime.fromtimestamp(start_ms / 1000, tz=timezone.utc).date().isoformat()
            ts, eq, ae, ab = run_m4(e, b, start_ms, window == 'common')
            days, vals = calendar(ts, eq, mfrom, COMMON[1])
            mt = metrics(days, vals, ae.trades, mfrom)
            btc_days, btc_vals = calendar(b[:, T].astype(np.int64) + DAY_MS, b[:, C], mfrom, COMMON[1])
            rm, rb = np.diff(vals) / vals[:-1], np.diff(btc_vals) / btc_vals[:-1]
            mt['corr_btc_daily'] = float(np.corrcoef(rm, rb)[0, 1]) if rm.std() > 0 else 0.0
            mt['funding_paid'] = ae.funding_paid + ab.funding_paid
            mt['fees_paid'] = ae.fees_paid + ab.fees_paid
            out['baskets'].setdefault('M4', {})[window] = mt
            curves[('M4', window, 'ETHBTC')] = (days, vals)
    # Baskets: equal-weight average of the vol-targeted sleeves' daily returns (no estimation).
    groups = {'M1': M1_BASKET, 'M2a': M2_BASKET, 'M2b': M2_BASKET, 'M3': M3_BASKET, 'M3nr': M3_BASKET,
              'NULL': M1_BASKET}
    for window in ('common', 'long'):
        for eng, members in groups.items():
            keys = [(eng, window, a) for a in members if (eng, window, a) in curves]
            if not keys:
                continue
            series = [daily_returns(*curves[k]) for k in keys]
            all_days = sorted(set().union(*[s.keys() for s in series]))
            r = np.array([np.mean([s[d] for s in series if d in s]) for d in all_days])
            v = BALANCE * np.r_[1.0, np.cumprod(1 + r)]
            dd = np.r_[all_days[0] - DAY_MS, all_days]
            b = metrics(np.array(dd), v, [], datetime.fromtimestamp(dd[0] / 1000, tz=timezone.utc).date().isoformat())
            b['members'] = [k[2] for k in keys]
            b['trades_per_year'] = sum(out['assets'][k[2]][window][eng]['trades_per_year']
                                       for k in keys if eng != 'NULL' and 'trades_per_year' in out['assets'][k[2]][window].get(eng, {}))
            out['baskets'].setdefault(eng, {})[window] = b
            curves[(eng, window, 'BASKET')] = (np.array(dd), v)
    # Correlations with the M1 basket, overall and in M1-losing quarters.
    for window in ('common', 'long'):
        if ('M1', window, 'BASKET') not in curves:
            continue
        m1 = daily_returns(*curves[('M1', window, 'BASKET')])
        qret = {}
        for t, x in m1.items():
            dt = datetime.fromtimestamp(t / 1000, tz=timezone.utc)
            q = f'{dt.year}Q{(dt.month - 1) // 3 + 1}'
            qret[q] = (1 + qret.get(q, 0.0)) * (1 + x) - 1
        losing = {q for q, x in qret.items() if x < 0}
        for eng in ('M2a', 'M2b', 'M3', 'M3nr', 'M4', 'NULL'):
            key = (eng, window, 'BASKET') if eng != 'M4' else ('M4', window, 'ETHBTC')
            if key not in curves:
                continue
            other = daily_returns(*curves[key])
            common_days = [t for t in m1 if t in other]
            lose_days = [t for t in common_days
                         if f'{datetime.fromtimestamp(t / 1000, tz=timezone.utc).year}Q'
                            f'{(datetime.fromtimestamp(t / 1000, tz=timezone.utc).month - 1) // 3 + 1}' in losing]

            def corr(ds):
                a, b = np.array([m1[t] for t in ds]), np.array([other[t] for t in ds])
                return float(np.corrcoef(a, b)[0, 1]) if len(ds) > 10 and a.std() > 0 and b.std() > 0 else None
            out['baskets'][eng][window]['corr_m1'] = corr(common_days)
            out['baskets'][eng][window]['corr_m1_losing_quarters'] = corr(lose_days)
            out['baskets'][eng][window]['m1_losing_quarters'] = len(losing)
    os.makedirs(hz.OUT_DIR, exist_ok=True)
    with open(os.path.join(hz.OUT_DIR, 'f1_screen.json'), 'w') as fh:
        json.dump(out, fh, indent=2, default=float)
    hz.jh.debug('baskets: ' + json.dumps({k: {w: (x.get('sharpe'), x.get('quarters_pos')) for w, x in v.items()}
                                           for k, v in out['baskets'].items()}))
    return out


def inventory():
    """Coverage of each stored source (first/last daily bar, bars), for the F0 inventory."""
    rows = {}
    for name, spec in ASSETS.items():
        for window in ('common', 'long'):
            if spec[window] is None:
                continue
            ex, sym = spec[window]
            b = load_daily(ex, sym, '2010-01-01', COMMON[1], spec['cfd'], warmup_days=0)
            rows[f'{name} {window} {ex}/{sym}'] = ({'first': hz._date(int(b[0, T])), 'last': hz._date(int(b[-1, T])),
                                                    'daily_bars': len(b)} if len(b) else {'first': None})
    hz.jh.debug(rows)
    with open(os.path.join(hz.OUT_DIR, 'inventory.json'), 'w') as fh:
        json.dump(rows, fh, indent=2)


def selftest():
    """Synthetic sign checks (no market data): a linearly falling series must pay a short,
    including the funding a short collects when rates are positive."""
    n = 400
    t0 = hz._ms('2021-01-01')
    c = np.linspace(200.0, 100.0, n)
    bars = np.column_stack([t0 + np.arange(n) * DAY_MS, c, c, c * 1.001, c * 0.999, np.ones(n)])
    acct = Account(BALANCE, TAKER, LEVERAGE)
    acct.trade(-50.0, c[0], int(bars[0, T]))
    for i in range(1, n):
        acct.pay_funding(c[i], 0.0001)  # positive funding: longs pay, shorts receive
    acct.trade(50.0, c[-1], int(bars[-1, T]))
    short_pnl, short_funding = acct.trades[-1]['pnl'], acct.funding_paid
    ts, eq, a2 = simulate(bars, t0, m1_decider(bars, False, 'ls'), None, False)
    res = {'short_trade_pnl': short_pnl, 'short_funding_received': short_funding,
           'expected_price_pnl': 50 * 100.0, 'm1_ls_final_equity': float(eq[-1]),
           'm1_ls_exposure_end': float(a2.qty * c[-1] / a2.equity(c[-1]))}
    res['pass'] = short_pnl > 0 and short_funding > 0 and eq[-1] > BALANCE and a2.qty < 0
    hz.jh.debug(res)
    return res


def audit(name):
    """Sanity audit of one asset in the common window: yearly price path and M1 trades by side.
    Diagnostic only; it changes no rule and is not a variant."""
    spec = ASSETS[name]
    ex, sym = spec['common']
    bars = load_daily(ex, sym, COMMON[0], COMMON[1], spec['cfd'])
    lr = logret(bars[:, C])
    big = np.argsort(-np.nan_to_num(abs(lr)))[:8]
    hz.jh.debug(f'{name} largest daily moves: ' + ', '.join(
        f'{hz._date(int(bars[k, T]))[:10]} {lr[k]:+.4f}' for k in sorted(big)))
    for y in range(2019, 2026):
        yb = bars[(bars[:, T] >= hz._ms(f'{y}-01-01')) & (bars[:, T] < hz._ms(f'{y + 1}-01-01'))]
        if len(yb):
            hz.jh.debug(f'{name} {y}: first {yb[0, C]:.3f} last {yb[-1, C]:.3f} min {yb[:, L].min():.3f} '
                        f'max {yb[:, H].max():.3f} bars {len(yb)} max |daily ret| {np.nanmax(abs(logret(yb[:, C]))):.4f}')
    if spec['m1']:
        dec = m1_decider(bars, spec['cfd'], spec['m1'])
        expo = {}

        def traced(i, acct, ts):
            dec(i, acct, ts)
            m = datetime.fromtimestamp(int(bars[i, T]) / 1000, tz=timezone.utc).strftime('%Y-%m')
            expo.setdefault(m, []).append((acct.qty * bars[i, C] / acct.equity(bars[i, C]), acct.equity(bars[i, C])))
        ts, eq, acct = simulate(bars, hz._ms(COMMON[0]), traced, name, False)
        for m in sorted(expo):
            if m.startswith('2022') or m.startswith('2021-1'):
                x = expo[m]
                hz.jh.debug(f'{name} {m}: mean exposure {np.mean([e for e, _ in x]):+.2f}x equity {x[-1][1]:.0f}')
        by = {}
        for t in acct.trades:
            y = datetime.fromtimestamp(t['closed'] / 1000, tz=timezone.utc).year
            k = (y, 'short' if t['side'] < 0 else 'long')
            by[k] = (by.get(k, (0, 0.0))[0] + 1, by.get(k, (0, 0.0))[1] + t['pnl'])
        hz.jh.debug(f'{name} M1 trades by (year, side): {sorted(by.items())}; fees {acct.fees_paid:.0f}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('command', choices=['screen', 'inventory', 'audit', 'selftest'])
    ap.add_argument('--assets', default=','.join(ASSETS))
    args = ap.parse_args()
    if args.command == 'screen':
        screen([a for a in args.assets.split(',') if a])
    elif args.command == 'selftest':
        selftest()
    elif args.command == 'audit':
        for a in args.assets.split(','):
            audit(a)
    else:
        inventory()


if __name__ == '__main__':
    sys.exit(main())
