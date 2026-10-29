import math

import numpy as np

from jesse.strategies import Strategy
import jesse.indicators as ta
from jesse import utils


# Sizing: a stop-out loses risk_pct of the balance, fees included.
# utils.risk_to_qty caps size at 1x capital, which would waste the 5x account, so qty is computed here.
MAX_NOTIONAL_X = 4.0       # headroom inside a 5x account; keeps liquidation far from the stop
MIN_STOP_FRACTION = 0.005  # below this the 0.12% round trip eats more than a quarter of 1R
MAX_STOP_FRACTION = 0.03
QTY_STEP = 0.001           # Binance BTCUSDT lot step

# Circuit breakers: no new entries for the rest of the UTC day after -3R,
# and a 1h pause after 4 losses in a row.
DAILY_LOSS_R = -3.0
MAX_LOSS_STREAK = 4
COOLDOWN_BARS = 12

HOURLY_LOOKBACK = 240
KELTNER_MULT = 1.5
RELEASE_HOURS = 3          # the squeeze may have ended up to 3 closed hours ago
SLOPE_HOURS = 3
# Exits mirror TrendBreakout5m: in-sample, only releases held 12h+ paid, and earlier
# breakevens, partials and stall exits cut those winners short.
MIN_STOP_ATR = 2.0         # of the 1h ATR; tighter box stops were mostly noise stop-outs
TRAIL_ATR = 3.0
BREAKEVEN_R = 1.5
# Macro filter: 20-day trend on 4h candles (1-4 week time-series momentum is the most
# persistent effect in crypto). Counter-trend releases lost in both in-sample years.
MACRO_EMA_BARS = 120
MACRO_SLOPE_BARS = 6
HOUR_MS = 60 * 60_000
DAY_MS = 24 * HOUR_MS

# Approximate London and New York opening hours in UTC (weekdays), when releases follow
# through more often. Fixed UTC keeps backtest and live identical; DST shifts them by 1h.
ACTIVE_SESSIONS = {'timezone': 'UTC', 'hours': {'Mon-Fri': ['07:00-10:00', '13:00-16:00']}}


class SqueezeRelease5m(Strategy):
    """
    Trade the release of a 1h volatility squeeze (Bollinger inside Keltner) when the 20-day
    trend (4h EMA120) and the 1h EMA50 slope agree. Signals use closed candles; the 5m route
    times the breakout.

    Trading route: BTC-USDT 5m (futures). Data routes: same exchange and symbol, 1h and 4h
    (the 4h route also stretches the warm-up to 40 days, which the macro EMA needs).
    Entry: after at least squeeze_hours compressed hours, a 5m close crosses beyond the
    compression box. One trade per squeeze. Stop on the opposite side of the box, at least
    2 x 1h ATR away. Management: stop to breakeven plus fees at +1.5R and a chandelier trail
    of 3 x 1h ATR from the best price.
    """

    def hyperparameters(self) -> list:
        return [
            {'name': 'risk_pct', 'type': float, 'min': 0.25, 'max': 2.0, 'step': 0.25, 'default': 1.0},
            {'name': 'squeeze_hours', 'type': int, 'min': 4, 'max': 12, 'step': 2, 'default': 6},
            {'name': 'session_filter', 'type': int, 'min': 0, 'max': 1, 'default': 0},
        ]

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def should_cancel_entry(self) -> bool:
        return True

    def go_long(self):
        self._enter()
        self.buy = self.vars['entry_qty'], self.price

    def go_short(self):
        self._enter()
        self.sell = self.vars['entry_qty'], self.price

    def on_open_position(self, order) -> None:
        entry = self.position.entry_price
        self.vars.update(r=abs(entry - self.vars['stop_price']), extreme=entry)
        self.stop_loss = self.position.qty, self.vars['stop_price']

    def update_position(self) -> None:
        entry = self.position.entry_price
        r = self.vars['r']
        atr = self._hourly()['atr']
        fees = 2 * self.fee_rate * entry
        qty = self.position.qty

        if self.is_long:
            self.vars['extreme'] = max(self.vars['extreme'], self.high)
            target = self.vars['extreme'] - TRAIL_ATR * atr
            if self.vars['extreme'] >= entry + BREAKEVEN_R * r:
                target = max(target, entry + fees)
            if self.average_stop_loss < target < self.price:
                self.stop_loss = qty, target
        else:
            self.vars['extreme'] = min(self.vars['extreme'], self.low)
            target = self.vars['extreme'] + TRAIL_ATR * atr
            if self.vars['extreme'] <= entry - BREAKEVEN_R * r:
                target = min(target, entry - fees)
            if self.price < target < self.average_stop_loss:
                self.stop_loss = qty, target

    def on_close_position(self, order, closed_trade) -> None:
        _record_result(self, closed_trade.pnl)

    def watch_list(self) -> list:
        hourly = self._hourly()
        return [
            ('Slope 1h', hourly['slope']),
            ('Box high', round(hourly['box_high'], 1)),
            ('Box low', round(hourly['box_low'], 1)),
            ('Day R', round(self.vars.get('day_r', 0.0), 2)),
        ]

    def _signal(self) -> int:
        # should_long and should_short both ask on the same candle; evaluate once.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            self.vars['signal'] = self._evaluate_signal()
        return self.vars['signal']

    def _evaluate_signal(self) -> int:
        hourly = self._hourly()
        box_key = hourly['box_key']
        if box_key is None or box_key == self.vars.get('traded_box') or not _can_trade(self):
            return 0
        if self.hp['session_filter'] and not utils.is_in_trading_hours(self.closed_candle_open_time, ACTIVE_SESSIONS):
            return 0

        prev_close = float(self.candles[-2, 2])
        room = MIN_STOP_ATR * hourly['atr']
        if hourly['slope'] == 1 and self.close > hourly['box_high'] >= prev_close:
            side, stop = 1, min(hourly['box_low'], self.close - room)
        elif hourly['slope'] == -1 and self.close < hourly['box_low'] <= prev_close:
            side, stop = -1, max(hourly['box_high'], self.close + room)
        else:
            return 0
        if not _plan_entry(self, side, stop):
            return 0
        self.vars['planned_box'] = box_key
        return side

    def _enter(self) -> None:
        self.vars['stop_price'] = self.vars['planned_stop']
        self.vars['entry_qty'] = self.vars['planned_qty']
        self.vars['risk_usd'] = self.vars['planned_risk_usd']
        self.vars['traded_box'] = self.vars['planned_box']

    def _hourly(self) -> dict:
        candles = _closed_candles(self, '1h', HOUR_MS)
        key = int(candles[-1, 0]) if len(candles) else -1
        if self.vars.get('hourly_key') != key:
            self.vars['hourly_key'] = key
            self.vars['hourly'] = self._read_hourly(candles[-HOURLY_LOOKBACK:])
        return self.vars['hourly']

    def _read_hourly(self, candles) -> dict:
        flat = {'box_key': None, 'box_high': math.inf, 'box_low': -math.inf, 'slope': 0, 'atr': 0.0}
        if len(candles) < 120:
            return flat
        bands = ta.bollinger_bands(candles, 20, sequential=True)
        keltner = ta.keltner(candles, 20, KELTNER_MULT, sequential=True)
        squeezed = (bands.upperband < keltner.upperband) & (bands.lowerband > keltner.lowerband)
        ema50 = ta.ema(candles, 50, sequential=True)
        atr = float(ta.atr(candles, 14))
        slope_now, slope_before = float(ema50[-1]), float(ema50[-1 - SLOPE_HOURS])
        if not _finite(atr, slope_now, slope_before):
            return flat

        result = dict(flat, atr=atr)
        slope = 1 if slope_now > slope_before else -1 if slope_now < slope_before else 0
        result['slope'] = slope if slope == _macro(self) else 0
        box = _latest_squeeze(squeezed, int(self.hp['squeeze_hours']))
        if box is not None:
            start, end = box
            result['box_key'] = int(candles[start, 0])
            result['box_high'] = float(candles[start:end + 1, 3].max())
            result['box_low'] = float(candles[start:end + 1, 4].min())
        return result


def _latest_squeeze(squeezed: np.ndarray, min_hours: int):
    """(start, end) indexes of a squeeze run of at least min_hours ending in the last RELEASE_HOURS."""
    n = len(squeezed)
    for end in range(n - 1, n - 1 - RELEASE_HOURS, -1):
        if not squeezed[end]:
            continue
        start = end
        while start > 0 and squeezed[start - 1]:
            start -= 1
        return (start, end) if end - start + 1 >= min_hours else None
    return None


def _plan_entry(strategy: Strategy, side: int, stop: float) -> bool:
    """Widen the stop to the fee-driven minimum, size for risk_pct, and stash the plan for go_*."""
    price = strategy.close
    if side == 1:
        stop = min(stop, price * (1 - MIN_STOP_FRACTION))
    else:
        stop = max(stop, price * (1 + MIN_STOP_FRACTION))
    distance = abs(price - stop)
    if distance / price > MAX_STOP_FRACTION:
        return False

    balance = strategy.balance
    loss_per_qty = distance + 2 * strategy.fee_rate * price
    qty = balance * strategy.hp['risk_pct'] / 100 / loss_per_qty
    qty = min(qty, MAX_NOTIONAL_X * balance / price, 0.95 * strategy.leveraged_available_margin / price)
    qty = _floor_step(qty)
    if qty <= 0:
        return False

    strategy.vars['planned_stop'] = stop
    strategy.vars['planned_qty'] = qty
    strategy.vars['planned_risk_usd'] = qty * loss_per_qty
    return True


def _can_trade(strategy: Strategy) -> bool:
    if strategy.index < strategy.vars.get('cooldown_until', -1):
        return False
    today = strategy.time // DAY_MS
    return not (strategy.vars.get('day') == today and strategy.vars.get('day_r', 0.0) <= DAILY_LOSS_R)


def _record_result(strategy: Strategy, pnl: float) -> None:
    risk = strategy.vars.get('risk_usd', 0.0)
    r_multiple = pnl / risk if risk > 0 else 0.0
    today = strategy.time // DAY_MS
    if strategy.vars.get('day') != today:
        strategy.vars['day'] = today
        strategy.vars['day_r'] = 0.0
    strategy.vars['day_r'] += r_multiple

    streak = strategy.vars.get('loss_streak', 0) + 1 if r_multiple < 0 else 0
    if streak >= MAX_LOSS_STREAK:
        strategy.vars['cooldown_until'] = strategy.index + COOLDOWN_BARS
        streak = 0
    strategy.vars['loss_streak'] = streak


def _macro(strategy: Strategy) -> int:
    """+1 above a rising 20-day EMA on closed 4h candles, -1 below a falling one, else 0."""
    candles = _closed_candles(strategy, '4h', 4 * HOUR_MS)
    if len(candles) < MACRO_EMA_BARS + MACRO_SLOPE_BARS:
        return 0
    ema = ta.ema(candles, MACRO_EMA_BARS, sequential=True)
    close, now, before = float(candles[-1, 2]), float(ema[-1]), float(ema[-1 - MACRO_SLOPE_BARS])
    if close > now > before:
        return 1
    if close < now < before:
        return -1
    return 0


def _closed_candles(strategy: Strategy, timeframe: str, period_ms: int):
    # get_candles(tf) includes the bar still forming from 5m bars already seen.
    # Drop it unless its window has ended, so decisions use closed bars only.
    candles = strategy.get_candles(strategy.exchange, strategy.symbol, timeframe)
    if len(candles) == 0 or int(candles[-1, 0]) + period_ms <= int(strategy.time):
        return candles
    return candles[:-1]


def _floor_step(qty: float) -> float:
    return math.floor(qty / QTY_STEP + 1e-9) * QTY_STEP


def _finite(*values: float) -> bool:
    return all(math.isfinite(value) for value in values)
