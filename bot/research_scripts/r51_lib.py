"""r51 shared pieces: the frozen P1 rebuilt with its F1 correction, portfolio attribution and
daily data loaders for the new sleeves.

Everything economic is imported unchanged from the r50 code frozen at 5caf4a53. The only r51
change to P1 is the F1 ruling (PROTOCOL_R51.md F1, "gana Jesse"): in the common window the
R1/bond curve comes from the Jesse session 42cdf4a0 (minute replay), with the protocol's 15 bp
per-side bond slippage charged on its executed orders, because the harness reproduces Jesse
poorly on the sparse Dukascopy bond CFD.
"""
import csv
import math
import os
from datetime import datetime, timezone

import numpy as np
import jesse.models  # noqa: F401 - must load before candle_service (circular import otherwise)

import r50_harness as hz
import r50_engines as en
import r50_f1b as fb
import r50_f1c as fc
import r50_f2 as f2
from r50_harness import T, O, C, H, L, V, DAY_MS
from r50_engines import COMMON, ASSETS, simulate, calendar, daily_returns

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'r51')
BOND_JESSE_SESSION = '42cdf4a0-7b6b-4af1-9862-da3396821812'
FAMILY = {'BTC': 'cripto', 'ETH': 'cripto', 'XAU': 'metales', 'SPX': 'acciones', 'WTI': 'energía',
          'GAS': 'energía', 'BOND': 'bono'}
# P1's two reference windows (r50 close): common measured from 2021, long from 2018-09.
P1_FROM = {'common': '2021-01-01', 'long': '2018-09-01'}


def _date(t):
    return datetime.fromtimestamp(int(t) / 1000, tz=timezone.utc).date().isoformat()


# ----------------------------------------------------------------------------------------------
# P1 rebuilt
# ----------------------------------------------------------------------------------------------
def jesse_sleeve_curve(session_id, slip_bps, frm):
    """Calendar curve of a Jesse sleeve with extra slippage charged per executed order.

    Each order costs notional * slip_bps on its execution day; costs compound through the curve
    as a cumulative wallet deduction, the same way the harness books slippage as worse fills."""
    from jesse.models.BacktestSession import get_backtest_session_by_id
    pts, _ = hz.jesse_curve(session_id)
    s = get_backtest_session_by_id(session_id)
    orders = [(int(o['executed_at']), abs(float(o['qty'])) * float(o['price']))
              for t in s.trades_json for o in t['orders'] if o['status'] == 'EXECUTED']
    ts = np.array(sorted(pts), dtype=np.int64)
    # A Portfolio point sampled shortly after midnight closes the previous UTC day.
    close_ts = (ts - 5 * 3_600_000) // DAY_MS * DAY_MS + DAY_MS
    eq = np.array([pts[t] for t in ts])
    cost = np.zeros(len(ts))
    for t_exec, notional in orders:
        k = int(np.searchsorted(close_ts, t_exec, side='left'))
        if k < len(cost):
            cost[k:] += notional * slip_bps / 1e4
    return calendar(close_ts, eq - cost, frm, COMMON[1])


def p1_sleeves(window):
    """R1 curve per core asset and C6 curve per coin, from each window start, plus trade PnLs."""
    r1, r1_tr, c6, c6_tr, data = {}, {}, {}, {}, {}
    for name in fb.CORE:
        if ASSETS[name][window] is None:
            continue
        d = fb.load_both(name, window)
        if d is None:
            continue
        data[name] = d
        frm = _date(d['start_ms'])
        ts, eq, acct = fb.r1_run(name, d)
        last = d['daily'][-1, C]
        r1[name] = calendar(ts, eq, frm, COMMON[1])
        tr = acct.trades + ([{'closed': int(ts[-1]), 'pnl': acct.upnl(last)}] if acct.is_open else [])
        r1_tr[name] = [t['pnl'] for t in tr]
        if name in fc.CRYPTO:
            cur, trs = [], []
            for retest in (False, True):
                ts, eq, acct = simulate(d['h4'], d['start_ms'], fb.r2_r3_decider(d['h4'], retest), name,
                                        d['funding'], fb.H4_MS)
                cur.append(calendar(ts, eq, frm, COMMON[1]))
                trs += [t['pnl'] for t in acct.trades]
            c6[name] = fc.mean_curve(cur)
            c6_tr[name] = trs
    if window == 'common' and 'BOND' in r1:
        r1['BOND'] = jesse_sleeve_curve(BOND_JESSE_SESSION, en.SLIP_BPS['BOND'], _date(data['BOND']['start_ms']))
    return r1, r1_tr, c6, c6_tr, data


def p1_components(window):
    r1, r1_tr, c6, c6_tr, data = p1_sleeves(window)
    comps = {'R1': fb.basket(r1, list(r1)), 'C6': fb.basket(c6, list(c6))}
    trades = sum(r1_tr.values(), []) + sum(c6_tr.values(), [])
    return comps, trades, {'r1': r1, 'c6': c6, 'data': data}


# ----------------------------------------------------------------------------------------------
# Portfolio with attribution (same arithmetic as r50_f2.portfolio)
# ----------------------------------------------------------------------------------------------
def portfolio_attr(comp, names):
    """r50 F2 construction, also returning each component's daily contribution k * w_i * r_i."""
    series = [daily_returns(*comp[n]) for n in names]
    days = sorted(set.intersection(*[set(s) for s in series]))
    R = np.array([[s[d] for s in series] for d in days])
    months = [_date(d)[:7] for d in days]
    w, k = None, None
    rets, contrib, used = [], [], []
    for t in range(len(days)):
        if w is not None:
            c = k * w * R[t]
            contrib.append(c)
            rets.append(float(c.sum()))
            used.append(days[t])
        if t + 1 < len(days) and months[t + 1] != months[t] and t + 1 >= f2.MIN_DAYS:
            hist = R[:t + 1]
            sd = hist.std(axis=0, ddof=1)
            if (sd > 0).all():
                w = (1 / sd) / (1 / sd).sum()
                cov = np.atleast_2d(np.cov(hist, rowvar=False))
                sp = math.sqrt(float(w @ cov @ w)) * math.sqrt(365)
                k = min(f2.K_MAX, f2.TARGET / sp) if sp > 0 else f2.K_MAX
    vals = en.BALANCE * np.r_[1.0, np.cumprod(1 + np.array(rets))]
    pdays = np.array([used[0] - DAY_MS] + used)
    return pdays, vals, dict(zip(names, np.array(contrib).T)), np.array(used)


def quarter_of(t):
    d = _date(t)
    return f'{d[:4]}Q{(int(d[5:7]) - 1) // 3 + 1}'


def quarterly(days, vals):
    """Quarter -> compounded return, from a curve whose first value is the starting balance."""
    q_end = {}
    for d, v in zip(days, vals):
        q_end[quarter_of(d)] = v
    qv = [vals[0]] + list(q_end.values())
    return dict(zip(q_end, (np.array(qv[1:]) / np.array(qv[:-1]) - 1).tolist()))


# ----------------------------------------------------------------------------------------------
# Data for the new sleeves
# ----------------------------------------------------------------------------------------------
def etf_daily(ticker, folder='r50'):
    """Yahoo daily ETF bars (r50 downloader) in Jesse's layout, bars stamped at 00:00 UTC."""
    path = os.path.join(HERE, 'data', folder, 'etf', f'{ticker}_daily_2000-01-01_2025-12-31.csv')
    rows = []
    with open(path) as fh:
        for r in csv.DictReader(fh):
            t = hz._ms(r['date'])
            rows.append([t, float(r['open']), float(r['close']), float(r['high']), float(r['low']), float(r['volume'])])
    return np.array(rows)


def csv_minutes_daily(path, f_ms=hz.RESERVED_FROM_MS):
    """Daily CFD bars from a Dukascopy 1m CSV written by dukascopy_download_v3 (not imported)."""
    rows = np.loadtxt(path, delimiter=',', skiprows=1)
    m = np.column_stack([rows[:, 0], rows[:, 1], rows[:, 4], rows[:, 2], rows[:, 3], rows[:, 5]])
    m = m[m[:, T] < f_ms]
    return en.daily_from_minutes(m, True, f_ms)


def asset_daily(name, window):
    """Daily bars and measurement start for a core asset (r50 loader, unchanged)."""
    d = fb.load_both(name, window)
    return d
