"""r50 F0: research harness (bars, account simulator, portfolio and metrics).

Purpose: iterate engines M1-M4 without spending Jesse runs. Before it may be used to decide
anything it must reproduce the r49 Jesse sessions (BTC b4792187, PAXG 02a484b6, SPY 21063c59)
with daily equity error < 0.5%; `python research_scripts/r50_harness.py repro` does that and
writes `research_scripts/data/r50/repro.json`.

Design choices, all copied from Jesse rather than re-invented, so a mismatch means a harness bug:
* Bars come from stored 1m candles aggregated with Jesse's own
  `generate_completed_candles_from_observed_minutes` (nonempty clock buckets only), and warmup is
  counted in observed bars like `is_for_jesse=True`.
* Decisions happen at a bar's close and market orders fill at that close; fee = notional * fee.
* Funding uses Jesse's content-addressed datasets: a settlement at T is paid by the position held
  before the decision at T (`FundingState.settle` boundary policy), amount = -qty * mark * rate.
* Equity is wallet balance + unrealized PnL, sampled daily like Jesse's Portfolio curve.

Rule r50: nothing after 2025-12-31 is read. `load_bars` refuses a later finish.
"""
import argparse
import json
import math
import os
import sys
from datetime import datetime, timezone

import numpy as np
import jesse.models  # Opens Jesse's database for the Candle / BacktestSession models.
from jesse import helpers as jh
from jesse.models.Candle import Candle
from jesse.services.candle_service import generate_completed_candles_from_observed_minutes
from jesse import utils as jutils

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, 'data', 'r50')
DAY_MS = 86_400_000
# 2026 is reserved by definition (r50 plan). Bars may close at 2026-01-01 00:00 at most.
RESERVED_FROM_MS = 1767225600000

# Candle column layout used by Jesse: timestamp, open, close, high, low, volume.
T, O, C, H, L, V = range(6)


def _ms(date_str: str) -> int:
    return int(datetime.fromisoformat(date_str).replace(tzinfo=timezone.utc).timestamp() * 1000)


def _minutes(exchange: str, symbol: str, start_ms: int, finish_ms: int) -> np.ndarray:
    rows = (Candle.select(Candle.timestamp, Candle.open, Candle.close, Candle.high, Candle.low, Candle.volume)
            .where((Candle.exchange == exchange) & (Candle.symbol == symbol)
                   & ((Candle.timeframe == '1m') | Candle.timeframe.is_null())
                   & (Candle.timestamp >= start_ms) & (Candle.timestamp < finish_ms))
            .order_by(Candle.timestamp).tuples())
    arr = np.array(list(rows), dtype=float)
    return arr if len(arr) else np.zeros((0, 6))


def load_bars(exchange: str, symbol: str, timeframe: str, start: str, finish: str,
              warmup_bars: int = 0, lookback_days: int = 900):
    """Return (warmup, trading) bar arrays in Jesse's layout.

    Trading bars open in [start, finish); warmup is the last `warmup_bars` observed bars that
    close at or before `start` (bounded by `lookback_days` of history, like Jesse's observed
    warmup, which simply returns fewer bars when the stored history is shorter).
    """
    start_ms, finish_ms = _ms(start), _ms(finish)
    if finish_ms > RESERVED_FROM_MS:
        raise ValueError('r50: data after 2025-12-31 is reserved until the user approves it')
    tf_ms = jh.timeframe_to_one_minutes(timeframe) * 60_000
    mins = _minutes(exchange, symbol, start_ms - lookback_days * DAY_MS, finish_ms)
    warm_m, trade_m = mins[mins[:, T] < start_ms], mins[mins[:, T] >= start_ms]
    warm = generate_completed_candles_from_observed_minutes(timeframe, warm_m, start_ms)
    trade = generate_completed_candles_from_observed_minutes(timeframe, trade_m, finish_ms)
    warm = warm[-warmup_bars:] if warmup_bars else warm[:0]
    load_bars.last_minutes = trade_m  # kept for Jesse-style daily marks in the reproduction
    return warm, trade, tf_ms


# ----------------------------------------------------------------------------------------------
# Account: one isolated futures position, Jesse accounting.
# ----------------------------------------------------------------------------------------------
class Account:
    def __init__(self, balance: float, fee: float, leverage: float, slippage_bps: float = 0.0):
        self.balance = balance  # wallet: realized PnL, fees and funding
        self.fee = fee
        self.leverage = leverage
        self.slip = slippage_bps / 1e4
        self.qty = 0.0  # signed
        self.entry = 0.0
        self.fees_paid = 0.0
        self.funding_paid = 0.0
        self.orders = 0
        self.order_log = []  # (ts, signed qty, price) for order-level reconciliation with Jesse
        self.state_log = []  # (bar close ts, balance, qty, entry) after each decision
        self.trades = []  # closed trades: pnl incl. fees and funding
        self._trade_pnl = 0.0
        self._trade_open_ts = None

    @property
    def is_open(self) -> bool:
        return abs(self.qty) > 1e-12

    def upnl(self, price: float) -> float:
        return self.qty * (price - self.entry) if self.is_open else 0.0

    def equity(self, price: float) -> float:
        return self.balance + self.upnl(price)

    def leveraged_available_margin(self, price: float) -> float:
        # Isolated margin locked at entry notional / leverage; what is left, times leverage.
        used = abs(self.qty) * self.entry / self.leverage if self.is_open else 0.0
        return max(self.balance - used, 0.0) * self.leverage

    def trade(self, dqty: float, price: float, ts: int, slippage: bool = False) -> None:
        """Market fill of a signed quantity at `price` (optionally worsened by slippage)."""
        if abs(dqty) < 1e-12:
            return
        px = price * (1 + self.slip * np.sign(dqty)) if slippage else price
        fee = abs(dqty) * px * self.fee
        self.balance -= fee
        self.fees_paid += fee
        self._trade_pnl -= fee
        self.orders += 1
        self.order_log.append((ts, dqty, px))
        if not self.is_open:
            self._trade_open_ts = ts
            self.qty, self.entry = dqty, px
            return
        if np.sign(dqty) == np.sign(self.qty):  # increase: weighted average entry
            new = self.qty + dqty
            self.entry = (self.entry * self.qty + px * dqty) / new
            self.qty = new
            return
        side = float(np.sign(self.qty))
        close = min(abs(dqty), abs(self.qty)) * np.sign(dqty)
        realized = -close * (px - self.entry)
        self.balance += realized
        self._trade_pnl += realized
        self.qty += close
        rest = dqty - close
        if not self.is_open:
            self.qty, self.entry = 0.0, 0.0
            self.trades.append({'opened': self._trade_open_ts, 'closed': ts, 'pnl': self._trade_pnl, 'side': side})
            self._trade_pnl = 0.0
            if abs(rest) > 1e-12:  # flip
                self.trade(rest, price, ts, slippage)

    def pay_funding(self, mark: float, rate: float) -> None:
        if self.is_open:
            amount = -self.qty * mark * rate
            self.balance += amount
            self.funding_paid += amount
            self._trade_pnl += amount


def load_funding(dataset_id: str):
    """(effective_at_ms, mark, rate) arrays from a Jesse funding dataset (storage/funding)."""
    from jesse.services.funding import load_dataset
    ev = load_dataset(dataset_id)['events']
    eff = np.array([e['settled_at'] - e['settled_at'] % 60_000 for e in ev], dtype=np.int64)
    return eff, np.array([e['mark_price'] for e in ev]), np.array([e['rate_decimal'] for e in ev])


def run(engine, warm: np.ndarray, bars: np.ndarray, tf_ms: int, acct: Account, funding=None):
    """Bar loop. Returns per-bar close-time equity (ms, equity) after each decision."""
    allc = np.vstack([warm, bars]) if len(warm) else bars
    n0 = len(warm)
    fi = 0
    finish = int(bars[-1, T]) + tf_ms
    if funding is not None:
        eff, mark, rate = funding
        # Jesse skips settlements before the start and treats the finish as exclusive.
        fi = int(np.searchsorted(eff, bars[0, T], side='left'))
    out_t, out_e = [], []
    for k in range(len(bars)):
        i = n0 + k
        close_ts = int(allc[i, T]) + tf_ms
        if funding is not None:
            # Settlements in (previous close, this close] use the pre-decision position.
            while fi < len(eff) and eff[fi] <= close_ts and eff[fi] < finish:
                acct.pay_funding(mark[fi], rate[fi])
                fi += 1
        engine.on_bar(allc, i, acct, close_ts)
        out_t.append(close_ts)
        out_e.append(acct.equity(allc[i, C]))
        acct.state_log.append((close_ts, acct.balance, acct.qty, acct.entry))
    return np.array(out_t, dtype=np.int64), np.array(out_e)


def jesse_marks(acct: Account, minutes: np.ndarray, times_ms: list) -> dict:
    """Equity at Jesse's own Portfolio sample instants: the account state after the last
    decision at or before t, marked at the close of the last minute that ends by t.

    Jesse samples once a day, but when: 1m simulation (e.g. any run with historical funding)
    samples at start + 1 d + 1 min, i.e. 00:01 UTC; fast mode samples only on its 4h skip
    boundaries, i.e. 04:00 UTC, and on sparse feeds (SPY CFD) at the next boundary with data.
    Illiquid 1m feeds such as PAXG spot can move a lot inside those minutes, so a daily bar
    close is not an exact substitute for reproduction (it is for screening)."""
    st = np.array(acct.state_log)
    mts, mclose = minutes[:, T].astype(np.int64), minutes[:, C]
    out = {}
    for t in times_ms:
        k = int(np.searchsorted(st[:, 0], t, side='right')) - 1
        j = int(np.searchsorted(mts, t - 60_000, side='right')) - 1
        if k < 0 or j < 0:
            continue
        _, bal, qty, entry = st[k]
        out[t] = float(bal + qty * (mclose[j] - entry))
    return out


# ----------------------------------------------------------------------------------------------
# r49 null engine: Donchian ensemble 20/55/120/250 d, vol target 17%, long/flat (Jesse copy).
# ----------------------------------------------------------------------------------------------
class DonchianEnsR49:
    """Line-by-line port of R49NullDonchianEns{Btc,Paxg,Spy}; `hours` enables the SPY variant."""
    LOOKBACK_DAYS = (20, 55, 120, 250)
    EXIT_FRACTION = 0.5
    TARGET_VOL = 0.17
    MAX_NOTIONAL_X = 2.0
    REBALANCE_BAND = 0.25
    MARGIN_USE = 0.92
    QTY_STEP = 0.001

    def __init__(self, candles_per_day: int, ann_days: int, hours: dict = None):
        self.cpd = candles_per_day
        self.lbs = [d * candles_per_day for d in self.LOOKBACK_DAYS]
        self.vol_window = 30 * candles_per_day
        self.ann = math.sqrt(ann_days * candles_per_day)
        self.hours = hours
        self.states = None
        self.state_key = None
        self._sess_idx = None

    def _floor(self, q):
        return math.floor(q / self.QTY_STEP + 1e-9) * self.QTY_STEP

    def _step(self, states, h, l, c, i):
        out = []
        for s, n in zip(states, self.lbs):
            m = max(int(n * self.EXIT_FRACTION), 1)
            if i - n < 0:
                out.append(0)
                continue
            hh, ll = h[i - n:i].max(), l[i - m:i].min()
            if s == 0 and c[i] > hh:
                s = 1
            elif s == 1 and c[i] < ll:
                s = 0
            out.append(s)
        return out

    def _series(self, allc, i):
        """Candles the strategy sees at bar i: all of them, or session candles for SPY."""
        if self.hours is None:
            return allc[:i + 1]
        if self._sess_idx is None:
            sess = jutils.filter_candles_by_hours(allc, self.hours)
            self._sess_ts = set(sess[:, T].astype(np.int64).tolist())
            self._sess_idx = np.flatnonzero(np.isin(allc[:, T].astype(np.int64), sess[:, T].astype(np.int64)))
        k = int(np.searchsorted(self._sess_idx, i, side='right'))
        return allc[self._sess_idx[:k]]

    def _update(self, allc, i):
        c = self._series(allc, i)
        if len(c) == 0:
            return
        key = int(c[-1, T]) if self.hours is not None else i
        if self.states is not None and self.state_key == key:
            return
        h, l, cl = c[:, H], c[:, L], c[:, C]
        if self.states is None:
            st = [0] * len(self.lbs)
            for j in range(max(self.lbs) + 1, len(c)):
                st = self._step(st, h, l, cl, j)
            self.states = st
        else:
            self.states = self._step(self.states, h, l, cl, len(c) - 1)
        self.state_key = key

    def _target(self, allc, i, acct):
        self._update(allc, i)
        if not self.states:
            return 0.0
        frac = sum(self.states) / len(self.states)
        if frac <= 0:
            return 0.0
        closes = self._series(allc, i)[-self.vol_window - 1:, C]
        rets = np.diff(np.log(closes))
        rv = float(np.std(rets, ddof=1)) * self.ann if len(rets) > 10 else float('nan')
        if not math.isfinite(rv) or rv <= 0:
            return 0.0
        price = allc[i, C]
        notional_x = min(self.MAX_NOTIONAL_X, frac * self.TARGET_VOL / rv)
        return max(acct.equity(price) * notional_x / price, 0.0)

    def on_bar(self, allc, i, acct, ts):
        price = allc[i, C]
        self._update(allc, i)  # before()
        if not acct.is_open:
            if self.hours is not None and not jutils.is_in_trading_hours(int(allc[i, T]), self.hours):
                return
            qty = self._floor(min(self._target(allc, i, acct),
                                  acct.leveraged_available_margin(price) * self.MARGIN_USE / price))
            if qty > 0:
                acct.trade(qty, price, ts)
            return
        target = self._target(allc, i, acct)
        cur = acct.qty
        if target <= 0:
            acct.trade(-cur, price, ts)
        elif target > cur * (1 + self.REBALANCE_BAND):
            add = self._floor(min(target - cur, acct.leveraged_available_margin(price) * self.MARGIN_USE / price))
            if add > 0:
                acct.trade(add, price, ts)
        elif target < cur * (1 - self.REBALANCE_BAND):
            cut = self._floor(cur - target)
            if 0 < cut < cur:
                acct.trade(-cut, price, ts)


# ----------------------------------------------------------------------------------------------
# Metrics
# ----------------------------------------------------------------------------------------------
def daily(ts_ms: np.ndarray, eq: np.ndarray) -> dict:
    """Last equity of each UTC day, keyed by the day's date (bars closing at 00:00 count for the
    previous day, matching Jesse's Portfolio point stamped at 00:01 of the next day)."""
    out = {}
    for t, e in zip(ts_ms, eq):
        day = datetime.fromtimestamp((int(t) - 1) / 1000, tz=timezone.utc).date().isoformat()
        out[day] = float(e)
    return out


def sharpe(values: np.ndarray, periods: int = 365) -> float:
    r = np.diff(values) / values[:-1]
    sd = r.std(ddof=1)
    return float(r.mean() / sd * math.sqrt(periods)) if sd > 0 else float('nan')


def max_dd(values: np.ndarray) -> float:
    return float((values / np.maximum.accumulate(values) - 1).min())


def cagr(values: np.ndarray, days: float) -> float:
    return float((values[-1] / values[0]) ** (365.0 / days) - 1)


def quarters_positive(dates: list, values: np.ndarray) -> float:
    last = {}
    for d, v in zip(dates, values):
        q = f'{d[:4]}Q{(int(d[5:7]) - 1) // 3 + 1}'
        last[q] = v
    qs = list(last.values())
    first = values[0]
    rets = [(b / a - 1) for a, b in zip([first] + qs[:-1], qs)]
    return float(np.mean([r > 0 for r in rets]))


# ----------------------------------------------------------------------------------------------
# Reproduction of the r49 sessions
# ----------------------------------------------------------------------------------------------
REPRO = [
    {'name': 'BTC', 'session': 'b4792187-8847-450d-9f52-320edb4a61dd', 'symbol': 'BTC-USDT', 'warmup': 1520,
     'engine': dict(candles_per_day=6, ann_days=365),
     'funding': '9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571'},
    {'name': 'PAXG', 'session': '02a484b6-a237-4ffb-a283-7db32354a61e', 'symbol': 'PAXG-USDT', 'warmup': 280,
     'engine': dict(candles_per_day=6, ann_days=365), 'funding': None},
    {'name': 'SPY', 'session': '21063c59-f0f5-4a07-a66a-040f75e3f475', 'symbol': 'SPY-USDT', 'warmup': 840,
     'engine': dict(candles_per_day=5, ann_days=252,
                    hours={'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}), 'funding': None},
]


def jesse_curve(session_id: str) -> dict:
    from jesse.models.BacktestSession import get_backtest_session_by_id
    s = get_backtest_session_by_id(session_id)
    series = next(x for x in s.equity_curve_json if x['name'] == 'Portfolio')
    points = series['data'] if 'data' in series else series['points']
    # Keyed by the real sample instant in ms; the first point is the starting balance.
    out = {int(round(p['time'] * 1000)): float(p['value']) for p in points[1:]}
    return out, s.metrics_json


def _date(t_ms: int) -> str:
    return datetime.fromtimestamp(t_ms / 1000, tz=timezone.utc).isoformat()


def repro() -> dict:
    os.makedirs(OUT_DIR, exist_ok=True)
    rows = []
    for spec in REPRO:
        warm, bars, tf_ms = load_bars('Binance Perpetual Futures', spec['symbol'], '4h',
                                      '2020-10-15', '2026-01-01', spec['warmup'])
        acct = Account(10_000, 0.00045, 3)
        fund = load_funding(spec['funding']) if spec['funding'] else None
        ts, eq = run(DonchianEnsR49(**spec['engine']), warm, bars, tf_ms, acct, fund)
        theirs, metrics = jesse_curve(spec['session'])
        # Bar-close daily curve (what screening uses) and the Jesse-style 00:00-minute marks.
        close_curve = daily(ts, eq)
        mine = jesse_marks(acct, load_bars.last_minutes, sorted(theirs))
        common = sorted(set(mine) & set(theirs))
        a = np.array([mine[d] for d in common])
        b = np.array([theirs[d] for d in common])
        rel = np.abs(a / b - 1)
        # Same Jesse points against the plain bar-close daily curve: a sample at 00:01 or 04:00
        # is compared with the previous day's 00:00 close (5 h back lands on that day).
        by_day = {datetime.fromtimestamp((t - 5 * 3_600_000) / 1000, tz=timezone.utc).date().isoformat(): v
                  for t, v in theirs.items()}
        cc = [d for d in by_day if d in close_curve]
        rel_close = np.abs(np.array([close_curve[d] for d in cc]) / np.array([by_day[d] for d in cc]) - 1)
        # Jesse closes any open position at the finish (one extra order and its fee).
        open_close_fee = abs(acct.qty) * bars[-1, C] * acct.fee if acct.is_open else 0.0
        row = {
            'asset': spec['name'], 'session': spec['session'], 'warmup_bars': len(warm), 'bars': len(bars),
            'common_days': len(common), 'jesse_days': len(theirs), 'harness_days': len(mine),
            'max_abs_rel_err': float(rel.max()), 'mean_abs_rel_err': float(rel.mean()),
            'worst_point_utc': _date(common[int(rel.argmax())]),
            'final_equity_harness': float(a[-1]), 'final_equity_jesse': float(b[-1]),
            'final_rel_err': float(a[-1] / b[-1] - 1),
            'sharpe_harness_daily365': sharpe(a), 'sharpe_jesse_curve_daily365': sharpe(b),
            'sharpe_jesse_engine': metrics.get('sharpe_ratio'),
            'maxdd_harness': max_dd(a), 'maxdd_jesse': max_dd(b),
            'trades_harness': len(acct.trades) + (1 if acct.is_open else 0), 'trades_jesse': metrics.get('total', 0) + metrics.get('total_open_trades', 0),
            'max_abs_rel_err_barclose_sampling': float(rel_close.max()),
            'mean_abs_rel_err_barclose_sampling': float(rel_close.mean()),
            'orders_harness': acct.orders, 'fees_harness': acct.fees_paid + open_close_fee,
            'fees_jesse': metrics.get('fee'), 'final_close_order_added': bool(acct.is_open),
            'funding_harness': acct.funding_paid,
            'funding_jesse': (metrics.get('funding') or {}).get('cashflow'),
            'pass_lt_0p5pct': bool(rel.max() < 0.005),
        }
        rows.append(row)
        jh.debug(row)
    with open(os.path.join(OUT_DIR, 'repro.json'), 'w') as fh:
        json.dump(rows, fh, indent=2)
    return rows


def diff_orders(name: str) -> None:
    """Print the first orders where the harness and the Jesse session disagree."""
    from jesse.models.BacktestSession import get_backtest_session_by_id
    spec = next(s for s in REPRO if s['name'] == name)
    warm, bars, tf_ms = load_bars('Binance Perpetual Futures', spec['symbol'], '4h',
                                  '2020-10-15', '2026-01-01', spec['warmup'])
    acct = Account(10_000, 0.00045, 3)
    fund = load_funding(spec['funding']) if spec['funding'] else None
    run(DonchianEnsR49(**spec['engine']), warm, bars, tf_ms, acct, fund)
    theirs, _ = jesse_curve(spec['session'])
    mine = jesse_marks(acct, load_bars.last_minutes, sorted(theirs))
    worst = sorted(mine, key=lambda t: -abs(mine[t] / theirs[t] - 1))[:6]
    for t in sorted(worst):
        jh.debug(f'{_date(t)} harness {mine[t]} jesse {theirs[t]}')
    jes = sorted((int(o['executed_at']), float(o['qty']), float(o['price']))
                 for t in get_backtest_session_by_id(spec['session']).trades_json for o in t['orders']
                 if o['status'] == 'EXECUTED')
    jh.debug(f'{name}: warm {len(warm)} first warm {warm[0, T] if len(warm) else None} '
             f'orders harness {len(acct.order_log)} jesse {len(jes)}')
    shown = 0
    for k in range(max(len(jes), len(acct.order_log))):
        a = acct.order_log[k] if k < len(acct.order_log) else None
        b = jes[k] if k < len(jes) else None
        same = a and b and a[0] == b[0] and abs(a[1] - b[1]) < 1e-9 and abs(a[2] - b[2]) < 1e-6
        if not same:
            jh.debug(f'#{k} harness {a} jesse {b}')
            shown += 1
            if shown >= 8:
                break


def probe(name: str, frm: str, to: str) -> None:
    """Per-bar engine internals in a window, to explain an order-level mismatch."""
    spec = next(s for s in REPRO if s['name'] == name)
    warm, bars, tf_ms = load_bars('Binance Perpetual Futures', spec['symbol'], '4h',
                                  '2020-10-15', '2026-01-01', spec['warmup'])
    acct = Account(10_000, 0.00045, 3)
    eng = DonchianEnsR49(**spec['engine'])
    allc = np.vstack([warm, bars])
    lo, hi = _ms(frm), _ms(to)
    for i in range(len(warm), len(allc)):
        ts = int(allc[i, T]) + tf_ms
        if lo <= ts <= hi:
            eng._update(allc, i)
            s = eng._series(allc, i)
            closes = s[-eng.vol_window - 1:, C]
            rv = float(np.std(np.diff(np.log(closes)), ddof=1)) * eng.ann
            tgt = eng._target(allc, i, acct)
            near = allc[(allc[:, T] >= ts - 5 * DAY_MS) & (allc[:, T] < ts)]
            for b in near:
                jh.debug(f'   bar {_date(int(b[T]))} o {b[O]} h {b[H]} l {b[L]} c {b[C]} '
                         f'session {jutils.is_in_trading_hours(int(b[T]), eng.hours) if eng.hours else True}')
            for n in eng.lbs[:2]:
                w = s[-n - 1:-1]
                a = int(np.argmax(w[:, H]))
                jh.debug(f'   n={n} sess_len {len(s)} hh {w[a, H]} at {_date(int(w[a, T]))} window from {_date(int(w[0, T]))}')
            jh.debug(f'{_date(ts)} open {_date(int(allc[i, T]))} close {allc[i, C]} vol {allc[i, V]:.1f} '
                     f'last_sess {_date(int(s[-1, T]))} states {eng.states} rv {rv:.6f} '
                     f'eq {acct.equity(allc[i, C]):.4f} cur {acct.qty} tgt {tgt:.4f} ratio {tgt / acct.qty if acct.qty else 0:.5f}')
        eng.on_bar(allc, i, acct, ts)
        if ts > hi:
            break


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('command', choices=['repro', 'diff', 'probe'])
    ap.add_argument('--asset', default='PAXG')
    ap.add_argument('--frm', default='2021-06-10')
    ap.add_argument('--to', default='2021-06-16')
    args = ap.parse_args()
    if args.command == 'repro':
        repro()
    elif args.command == 'diff':
        diff_orders(args.asset)
    elif args.command == 'probe':
        probe(args.asset, args.frm, args.to)


if __name__ == '__main__':
    sys.exit(main())
