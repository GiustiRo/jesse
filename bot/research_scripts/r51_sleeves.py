"""r51 F3-F5 sleeves, coded from PROTOCOL_R51.md (committed in 8ac56348 before any result).

Every rule below is the protocol's text in code; defaults come from the protocol (literature),
nothing is tuned. Costs, accounts and the bar loop are the frozen r50 ones (`r50_engines`).

Lenses (protocol section 1):
* `dec`  : decision lens. TradFi CFDs from 2018-09-01 (bond: from its first usable day); crypto
           Binance spot from 2018-01-01 (no funding, the r50 long lens).
* `c21`  : 2021-25 sub-window on the traded instruments (crypto perpetuals with real funding),
           used for P1's common window in F6.
* `veto` : longest history per asset (CFDs 2011-12+, crypto spot 2017-08+, bond = TLT daily).
"""
import math
import os

import numpy as np

import r50_harness as hz
import r50_engines as en
import r50_f1b as fb
import r51_lib as lib
from r50_harness import T, O, C, H, L, V, DAY_MS
from r50_engines import (TAKER, MAKER, STOP_SLIP, TARGET_VOL, MAX_X, ann_vol, logret, sma, rebalance,
                         _trade, simulate, calendar)

CACHE = os.path.join(lib.OUT, 'cache')
END = '2026-01-01'
DEC_FROM = {'cfd': '2018-09-01', 'crypto': '2018-01-01'}
C21_FROM = '2021-01-01'
CRYPTO = ('BTC', 'ETH')
SOURCES = {
    'BTC': {'spot': ('Binance Spot', 'BTC-USDT'), 'perp': ('Binance Perpetual Futures', 'BTC-USDT')},
    'ETH': {'spot': ('Binance Spot', 'ETH-USDT'), 'perp': ('Binance Perpetual Futures', 'ETH-USDT')},
    'XAU': {'cfd': ('Custom Data', 'XAU-USDT')}, 'SPX': {'cfd': ('Custom Data', 'SPXD-USDT')},
    'WTI': {'cfd': ('Custom Data', 'WTI-USDT')}, 'GAS': {'cfd': ('Custom Data', 'NATGAS-USDT')},
    'BOND': {'cfd': ('Custom Data', 'USTBOND-USDT')},
    'XAG': {'cfd': ('Custom Data', 'XAG-USDT')}, 'NDX': {'cfd': ('Custom Data', 'NDX-USDT')},
    'COPPER': {'cfd': ('Custom Data', 'COPPER-USDT')},
}
BRENT_CSV = os.path.join(lib.OUT, 'BRENTCMDUSD_1m_2010-01-01_2025-12-31.csv')
EURUSD_CSV = os.path.join(lib.OUT, 'EURUSD_1m_2010-01-01_2025-12-31.csv')


# ----------------------------------------------------------------------------------------------
# Daily data (cached: the minute reads are the slow part)
# ----------------------------------------------------------------------------------------------
def _cached(key, fn):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f'{key}.npy')
    if os.path.exists(path):
        return np.load(path)
    arr = fn()
    np.save(path, arr)
    return arr


def minutes_daily(exchange, symbol, cfd):
    m = hz._minutes(exchange, symbol, hz._ms('2009-01-01'), hz.RESERVED_FROM_MS)
    return en.daily_from_minutes(m, cfd, hz.RESERVED_FROM_MS)


def daily(name, src):
    """Daily bars of an asset from one source: 'cfd', 'spot', 'perp', 'tlt', 'brent', 'eurusd'."""
    if src == 'tlt':
        return _cached('TLT_tlt', lambda: lib.etf_daily('TLT'))
    if src in ('brent', 'eurusd'):
        path = BRENT_CSV if src == 'brent' else EURUSD_CSV
        return _cached(f'{name}_{src}', lambda: lib.csv_minutes_daily(path))
    ex, sym = SOURCES[name][src]
    return _cached(f'{name}_{src}', lambda: minutes_daily(ex, sym, src == 'cfd'))


def lens_source(name, lens):
    if name in CRYPTO:
        return 'perp' if lens == 'c21' else 'spot'
    if name == 'BOND' and lens == 'veto':
        return 'tlt'
    return 'cfd'


def lens_from(name, lens):
    if lens == 'c21':
        return C21_FROM
    if lens == 'dec':
        return DEC_FROM['crypto' if name in CRYPTO else 'cfd']
    return None  # veto: from the first bar with full lookback


def is_cfd(name):
    return name not in CRYPTO


# ----------------------------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------------------------
def ret_n(c, n):
    return np.r_[np.full(n, np.nan), np.log(c[n:] / c[:-n])]


def ema(x, n):
    a, out = 2.0 / (n + 1), np.full(len(x), np.nan)
    acc = None
    for i, v in enumerate(x):
        if not np.isfinite(v):
            continue
        acc = v if acc is None else acc + a * (v - acc)
        out[i] = acc
    return out


def align(src_bars, dst_bars, values):
    """Value of a daily series (indexed like src_bars) known at each dst bar's close."""
    idx = np.searchsorted(src_bars[:, T], dst_bars[:, T], side='right') - 1
    out = np.where(idx >= 0, values[np.clip(idx, 0, None)], np.nan)
    return out


def continuous_decider(bars, x_target, warm=252):
    """Rebalance to the signed exposure x_target[i] (multiples of equity), r49 25% band."""
    c = bars[:, C]

    def decide(i, acct, ts):
        if i < warm or not np.isfinite(x_target[i]):
            return
        rebalance(acct, acct.equity(c[i]) * float(x_target[i]) / c[i], c[i], ts)
    return decide


def vol_scaled(sig, vol):
    with np.errstate(invalid='ignore', divide='ignore'):
        x = sig * TARGET_VOL / vol
    return np.clip(np.where(np.isfinite(x), x, np.nan), -MAX_X, MAX_X)


# ----------------------------------------------------------------------------------------------
# Block A
# ----------------------------------------------------------------------------------------------
def a1_signal(c):
    s = (np.sign(ret_n(c, 63)) + np.sign(ret_n(c, 126)) + np.sign(ret_n(c, 252))) / 3
    return s


def a1_x(bars, cfd):
    return vol_scaled(a1_signal(bars[:, C]), ann_vol(bars[:, C], cfd))


def a2_x(bars, spx_bars):
    """A1 on the bond with the long side off unless corr126(SPX, bond) < 0."""
    x = a1_x(bars, True)
    rb = logret(bars[:, C])
    # SPX return of the same day as the bond bar; days without an SPX bar stay NaN and are
    # dropped from the window.
    spx_close = align(spx_bars, bars, spx_bars[:, C])
    rs = np.r_[np.nan, np.diff(np.log(spx_close))]
    corr = np.full(len(x), np.nan)
    for i in range(126, len(x)):
        a, b = rb[i - 125:i + 1], rs[i - 125:i + 1]
        ok = np.isfinite(a) & np.isfinite(b)
        if ok.sum() > 100 and a[ok].std() > 0 and b[ok].std() > 0:
            corr[i] = np.corrcoef(a[ok], b[ok])[0, 1]
    long_ok = np.isfinite(corr) & (corr < 0)
    return np.where((x > 0) & ~long_ok, 0.0, x)


def a5_x(bars, eur_bars):
    """A1 on WTI with the long side off when the dollar rose over 63 days (EURUSD fell)."""
    x = a1_x(bars, True)
    eur = align(eur_bars, bars, eur_bars[:, C])
    eur63 = np.r_[np.full(63, np.nan), np.log(eur[63:] / eur[:-63])]
    dollar_up = np.isfinite(eur63) & (eur63 < 0)
    return np.where((x > 0) & dollar_up, 0.0, x)


def a4_decider(bars):
    """Bond month-end: limit at the close of the 4th-last trading day (3 sessions left), valid one
    bar (maker, strict cross); exit at the close of the month's last trading day (taker)."""
    c, l = bars[:, C], bars[:, L]
    vol = ann_vol(c, True)
    months = np.array([lib._date(t)[:7] for t in bars[:, T]])
    last_of_month = np.r_[months[1:] != months[:-1], True]
    # Index of the month's last bar for every bar; the final month of the data counts as complete
    # only if it ends on December 31, which is the case for 2025-12.
    nxt = np.empty(len(c), dtype=int)
    j = len(c) - 1
    for i in range(len(c) - 1, -1, -1):
        if last_of_month[i]:
            j = i
        nxt[i] = j
    st = {'limit': None}

    def decide(i, acct, ts):
        if acct.is_open:
            if last_of_month[i]:
                _trade(acct, -acct.qty, c[i], ts, TAKER)
            return
        if st['limit'] is not None:
            px, qty = st['limit']
            st['limit'] = None
            if l[i] < px:
                _trade(acct, qty, px, ts, MAKER)
                if last_of_month[i]:
                    _trade(acct, -acct.qty, c[i], ts, TAKER)
                return
        if i >= 30 and nxt[i] - i == 3 and np.isfinite(vol[i]) and vol[i] > 0:
            st['limit'] = (c[i], acct.equity(c[i]) * min(MAX_X, TARGET_VOL / vol[i]) / c[i])
    return decide


def a3_pair(brent, wti, start_ms):
    """Brent-WTI spread sleeve on two half-balance accounts; returns (ts, equity, trades)."""
    common = np.intersect1d(brent[:, T], wti[:, T])
    b = brent[np.isin(brent[:, T], common)]
    w = wti[np.isin(wti[:, T], common)]
    x = np.log(b[:, C]) - np.log(w[:, C])
    mu = sma(x, 60)
    sd = en.rolling_std(x, 60)
    z = (x - mu) / sd
    dx_vol = en.rolling_std(np.r_[np.nan, np.diff(x)], 30) * math.sqrt(252)
    ab, aw = en.Account(en.BALANCE / 2, TAKER, en.LEVERAGE), en.Account(en.BALANCE / 2, TAKER, en.LEVERAGE)
    st = {'side': 0, 'held': 0}
    ts_out, eq_out, trades = [], [], []
    k0 = int(np.searchsorted(b[:, T], start_ms, side='left'))
    for i in range(k0, len(b)):
        ts = int(b[i, T]) + DAY_MS
        pb, pw = b[i, C], w[i, C]
        eq = ab.equity(pb) + aw.equity(pw)
        if st['side'] != 0:
            st['held'] += 1
            crossed = np.isfinite(z[i]) and np.sign(z[i]) != np.sign(st['z0'])
            if crossed or st['held'] >= 20 or (np.isfinite(z[i]) and abs(z[i]) > 4):
                _trade(ab, -ab.qty, pb, ts, TAKER)
                _trade(aw, -aw.qty, pw, ts, TAKER)
                trades.append({'closed': ts, 'pnl': ab.balance + aw.balance - st['bal0']})
                st.update(side=0, held=0)
        elif i >= 60 and np.isfinite(z[i]) and abs(z[i]) > 2 and np.isfinite(dx_vol[i]) and dx_vol[i] > 0:
            notional = eq * min(1.0, TARGET_VOL / dx_vol[i])
            side = -1 if z[i] > 2 else 1   # +1 = long Brent / short WTI
            st.update(side=side, held=0, z0=z[i], bal0=ab.balance + aw.balance)
            _trade(ab, side * notional / pb, pb, ts, TAKER)
            _trade(aw, -side * notional / pw, pw, ts, TAKER)
        ts_out.append(ts)
        eq_out.append(ab.equity(pb) + aw.equity(pw))
    return np.array(ts_out, dtype=np.int64), np.array(eq_out), trades


# ----------------------------------------------------------------------------------------------
# Block B
# ----------------------------------------------------------------------------------------------
B1_RISK = 0.005
B1_TRAIL = 3.0
B1_TIME_BARS = 60


def b1_decider(h4, daily_bars):
    """Crypto 4h short, mirror of R2, only in a daily bear regime (protocol B1)."""
    import jesse.indicators as ta
    c, h, l, o = h4[:, C], h4[:, H], h4[:, L], h4[:, O]
    e20 = ta.ema(h4, period=20, sequential=True)
    e80 = ta.ema(h4, period=80, sequential=True)
    atr = ta.atr(h4, period=14, sequential=True)
    adx = ta.adx(h4, period=14, sequential=True)
    rsi = ta.rsi(h4, period=14, sequential=True)
    ll26 = np.full(len(l), np.nan)
    for i in range(26, len(l)):
        ll26[i] = l[i - 26:i].min()
    dc = daily_bars[:, C]
    s200, s50 = sma(dc, 200), sma(dc, 50)
    bear_d = np.r_[np.zeros(5, dtype=bool), (dc[5:] < s200[5:]) & (s50[5:] < s50[:-5])]
    # A daily bar is usable once it has closed: its close time must be <= the 4h bar's close.
    d_close = daily_bars[:, T] + DAY_MS
    j = np.searchsorted(d_close, h4[:, T] + fb.H4_MS, side='right') - 1
    bear = np.where(j >= 0, bear_d[np.clip(j, 0, None)], False)
    st = {}

    def setup(i):
        vals = [e20[i], e80[i], e80[i - 4], atr[i], adx[i], rsi[i], ll26[i]]
        return (i >= 100 and bool(np.isfinite(vals).all()) and atr[i] > 0 and bear[i] and c[i] < e80[i]
                and e20[i] < e80[i] < e80[i - 4] and adx[i] >= 26 and 24 <= rsi[i] <= 48
                and h[i] - l[i] <= 3 * atr[i])

    def decide(i, acct, ts):
        if acct.is_open:
            if h[i] >= st['stop']:
                _trade(acct, -acct.qty, max(st['stop'], o[i]) * (1 + STOP_SLIP), ts, TAKER)
                return
            st['held'] += 1
            if st['held'] >= B1_TIME_BARS:
                _trade(acct, -acct.qty, c[i], ts, TAKER)
                return
            st['worst_close'] = min(st['worst_close'], c[i])
            st['extreme'] = min(st['extreme'], l[i])
            best_r = (st['entry'] - st['extreme']) / st['r']
            mult = B1_TRAIL * (0.62 if best_r >= 8 else (0.78 if best_r >= 5 else 1.0))
            new = st['worst_close'] + mult * atr[i]
            if best_r >= 1.75:
                new = min(new, st['entry'] * (1 - 2.5 * TAKER))
            if c[i] < new < st['stop']:
                st['stop'] = new
            return
        if setup(i) and c[i] < ll26[i]:
            frac = max(2 * atr[i] / c[i], 0.008)
            if frac <= 0.055:
                dist = frac * c[i]
                eq = acct.equity(c[i])
                q = min(eq * B1_RISK / (dist + 2 * acct.fee * c[i]), eq * MAX_X / c[i])
                if q > 0:
                    _trade(acct, -q, c[i], ts, TAKER)
                    st.update(entry=c[i], r=dist, stop=c[i] + dist, worst_close=c[i], extreme=l[i], held=0)
    return decide


def b2_x(bars, cfd):
    c = bars[:, C]
    s = np.where((ret_n(c, 252) < 0) & (c < sma(c, 200)), -1.0, 0.0)
    return vol_scaled(s, ann_vol(c, cfd))


B3_UNIVERSE = ('BTC', 'ETH', 'XAU', 'SPX', 'WTI', 'GAS', 'BOND')


def b3_curve(lens, start_ms):
    """Cross-asset 12-1 momentum among the 7 core assets: long top 2, short bottom 2, monthly.

    Weights are notional fractions of sleeve equity held constant between month ends (daily
    rebalanced to the same fractions, a declared simplification); costs are fee + per-asset
    slippage on the turnover at each rebalance; crypto perpetuals pay their real funding."""
    bars = {n: daily(n, lens_source(n, lens)) for n in B3_UNIVERSE}
    days = np.arange(hz._ms('2003-01-01'), hz._ms(END), DAY_MS)
    close = {}
    for n, b in bars.items():
        idx = np.searchsorted(b[:, T], days, side='right') - 1
        cl = np.where(idx >= 0, b[np.clip(idx, 0, None), C], np.nan)
        first = b[0, T]
        close[n] = np.where(days >= first, cl, np.nan)
    rets = {n: np.r_[np.nan, close[n][1:] / close[n][:-1] - 1] for n in close}
    vol60 = {n: en.rolling_std(np.log(close[n]) - np.log(np.r_[np.nan, close[n][:-1]]), 60)
             * math.sqrt(252 if is_cfd(n) else 365) for n in close}
    fund = {}
    if lens == 'c21':
        for n in CRYPTO:
            eff, mark, rate = hz.load_funding(en.FUNDING[n])
            dsum = np.zeros(len(days))
            k = np.searchsorted(days, eff, side='right') - 1
            for kk, r in zip(k, rate):
                if 0 <= kk < len(days):
                    dsum[kk] += r
            fund[n] = dsum
    months = np.array([lib._date(d)[:7] for d in days])
    w = {n: 0.0 for n in close}
    eq, out_ts, out_eq = en.BALANCE, [], []
    k0 = int(np.searchsorted(days, start_ms))
    for t in range(1, len(days)):
        if t >= k0:
            r = sum(w[n] * rets[n][t] for n in w if w[n] and np.isfinite(rets[n][t]))
            f = sum(w[n] * fund[n][t] for n in fund if w[n])
            eq *= 1 + r - f
            out_ts.append(int(days[t]) + DAY_MS)
            out_eq.append(eq)
        if t + 1 < len(days) and months[t + 1] != months[t]:
            score = {}
            for n in close:
                c = close[n]
                if t >= 252 and np.isfinite(c[t - 252]) and np.isfinite(c[t - 21]) and np.isfinite(vol60[n][t]):
                    score[n] = math.log(c[t - 21] / c[t - 252])
            new = {n: 0.0 for n in close}
            if len(score) >= 4:
                order = sorted(score, key=score.get, reverse=True)
                for n in order[:2]:
                    new[n] = 0.25 * min(MAX_X, TARGET_VOL / vol60[n][t])
                for n in order[-2:]:
                    new[n] = -0.25 * min(MAX_X, TARGET_VOL / vol60[n][t])
            if t >= k0:
                turn = sum(abs(new[n] - w[n]) * (TAKER + en.SLIP_BPS.get(n, 0.0) / 1e4) for n in close)
                eq *= 1 - turn
                if out_eq:
                    out_eq[-1] = eq
            w = new
    return np.array(out_ts, dtype=np.int64), np.array(out_eq)


# ----------------------------------------------------------------------------------------------
# Block T
# ----------------------------------------------------------------------------------------------
LONG_FLAT = ('BTC', 'ETH', 'XAU', 'SPX', 'XAG', 'NDX', 'EWJ', 'EWY')
EWMAC = ((16, 64, 3.75), (32, 128, 2.65), (64, 256, 1.87))
FDM = 1.2
CAP = 20.0


def t1_forecast(c):
    dp = np.r_[np.nan, np.diff(c)]
    sig_p = en.rolling_std(dp, 25)
    fs = []
    for f, s, scalar in EWMAC:
        raw = (ema(c, f) - ema(c, s)) / sig_p
        fs.append(np.clip(raw * scalar, -CAP, CAP))
    mean80 = sma(c, 80)
    mx = np.array([np.nan] * 79 + [c[i - 79:i + 1].max() for i in range(79, len(c))])
    mn = np.array([np.nan] * 79 + [c[i - 79:i + 1].min() for i in range(79, len(c))])
    with np.errstate(invalid='ignore', divide='ignore'):
        brk = 40 * (c - mean80) / (mx - mn)
    fs.append(np.clip(ema(brk, 20) * 0.75, -CAP, CAP))
    comb = np.clip(np.nanmean(np.vstack(fs), axis=0) * FDM, -CAP, CAP)
    return comb


def t_x(name, bars, attenuate=False):
    c = bars[:, C]
    f = t1_forecast(c)
    if name in LONG_FLAT:
        f = np.maximum(f, 0.0)
    vol = ann_vol(c, is_cfd(name))
    x = vol_scaled(f / 10.0, vol)
    if attenuate:
        q = np.full(len(c), np.nan)
        for i in range(252, len(c)):
            hist = vol[:i]
            hist = hist[np.isfinite(hist)]
            if len(hist) >= 252 and np.isfinite(vol[i]):
                q[i] = float((hist < vol[i]).mean())
        m = ema(np.where(np.isfinite(q), 2 - 1.5 * q, np.nan), 10)
        x = np.clip(x * m, -MAX_X, MAX_X)
    return x
