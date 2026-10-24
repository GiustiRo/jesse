import math

import numpy as np

from jesse.strategies import Strategy
import jesse.indicators as ta


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
SHOCK_BARS = 6             # the flush must happen within 30 minutes
LOW_RECENT_BARS = 3        # and its extreme within the last 15, so the entry is near it
VOLUME_BASE_BARS = 288     # 24h of 5m bars as the normal-volume baseline
MAX_RETRACE = 0.4          # skip if price already recovered more than 40% of the flush
STOP_BUFFER_ATR = 0.25     # of the 1h ATR, beyond the flush extreme
# The first target must pay the round trip several times over and be worth most of the risk.
MIN_TARGET_FEES = 3
MIN_TARGET_R = 0.8
MAX_HOLD_BARS = 144        # 12h: a flush that has not reverted by then was a trend change
# Macro filter: 20-day trend on 4h candles (1-4 week time-series momentum is the most
# persistent effect in crypto). Only flushes against that trend are faded.
MACRO_EMA_BARS = 120
MACRO_SLOPE_BARS = 6
HOUR_MS = 60 * 60_000
DAY_MS = 24 * HOUR_MS


class RangeFade5m(Strategy):
    """
    Mean reversion: fade a 5m liquidation flush against the 20-day trend (buy a violent dip in an
    uptrend, sell a violent spike in a downtrend). Forced liquidations overshoot fair value, and
    the higher-timeframe trend makes the snap-back more likely than continuation.

    Trading route: BTC-USDT 5m (futures). Data routes: same exchange and symbol, 1h and 4h
    (the 4h route also stretches the warm-up to 40 days, which the macro EMA needs).
    Entry: within 30 minutes price fell at least shock_atr x 1h ATR on volume_mult x normal
    volume, the low is at most 15 minutes old, and the current 5m candle closes bullish while
    still in the lower 40% of the flush (mirror for shorts). One trade per flush.
    Stop below the flush low plus 0.25 1h ATR. Management: half off at a 50% retrace, stop to
    breakeven plus fees, the rest at the pre-flush high. Time stop of 12h.
    """

    def hyperparameters(self) -> list:
        return [
            {'name': 'risk_pct', 'type': float, 'min': 0.25, 'max': 2.0, 'step': 0.25, 'default': 1.0},
            {'name': 'shock_atr', 'type': float, 'min': 1.0, 'max': 3.0, 'step': 0.5, 'default': 1.5},
            {'name': 'volume_mult', 'type': float, 'min': 1.5, 'max': 3.0, 'step': 0.5, 'default': 2.0},
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
        qty = self.position.qty
        self.vars['entry_index'] = self.index
        half = _floor_step(qty / 2)
        self.stop_loss = qty, self.vars['stop_price']
        if 0 < half < qty:
            self.take_profit = [(half, self.vars['tp1']), (qty - half, self.vars['tp2'])]
        else:
            self.take_profit = qty, self.vars['tp1']

    def on_reduced_position(self, order) -> None:
        entry = self.position.entry_price
        fees = 2 * self.fee_rate * entry
        breakeven = entry + fees if self.is_long else entry - fees
        # Only move the stop if breakeven is still on the protective side of price.
        if (self.is_long and breakeven < self.price) or (self.is_short and breakeven > self.price):
            self.stop_loss = self.position.qty, breakeven

    def update_position(self) -> None:
        if self.index - self.vars['entry_index'] >= MAX_HOLD_BARS:
            self.liquidate()

    def on_close_position(self, order, closed_trade) -> None:
        _record_result(self, closed_trade.pnl)

    def watch_list(self) -> list:
        hourly = self._hourly()
        return [
            ('Macro 4h', hourly['macro']),
            ('ATR 1h', round(hourly['atr'], 1)),
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
        if hourly['macro'] == 0 or len(self.candles) < VOLUME_BASE_BARS + SHOCK_BARS or not _can_trade(self):
            return 0

        recent = self.candles[-SHOCK_BARS:]
        highs, lows = recent[:, 3], recent[:, 4]
        hi_idx, lo_idx = int(np.argmax(highs)), int(np.argmin(lows))
        flush_high, flush_low = float(highs[hi_idx]), float(lows[lo_idx])
        size = flush_high - flush_low
        if size < self.hp['shock_atr'] * hourly['atr']:
            return 0
        base_volume = float(self.candles[-VOLUME_BASE_BARS - SHOCK_BARS:-SHOCK_BARS, 5].mean()) * SHOCK_BARS
        if float(recent[:, 5].sum()) < self.hp['volume_mult'] * base_volume:
            return 0

        recent_limit = SHOCK_BARS - LOW_RECENT_BARS
        stop_buffer = STOP_BUFFER_ATR * hourly['atr']
        if (hourly['macro'] == 1 and hi_idx < lo_idx >= recent_limit and self.close > self.open
                and self.close <= flush_low + MAX_RETRACE * size):
            side, key = 1, int(recent[lo_idx, 0])
            stop = flush_low - stop_buffer
            tp1, tp2 = flush_low + 0.5 * size, flush_high
        elif (hourly['macro'] == -1 and lo_idx < hi_idx >= recent_limit and self.close < self.open
                and self.close >= flush_high - MAX_RETRACE * size):
            side, key = -1, int(recent[hi_idx, 0])
            stop = flush_high + stop_buffer
            tp1, tp2 = flush_high - 0.5 * size, flush_low
        else:
            return 0
        if key == self.vars.get('traded_flush') or not _plan_entry(self, side, stop):
            return 0

        reward = abs(tp1 - self.close)
        risk = abs(self.close - self.vars['planned_stop'])
        if reward < MIN_TARGET_FEES * 2 * self.fee_rate * self.close or reward < MIN_TARGET_R * risk:
            return 0
        self.vars.update(planned_tp1=tp1, planned_tp2=tp2, planned_flush=key)
        return side

    def _enter(self) -> None:
        self.vars['stop_price'] = self.vars['planned_stop']
        self.vars['entry_qty'] = self.vars['planned_qty']
        self.vars['risk_usd'] = self.vars['planned_risk_usd']
        self.vars['tp1'] = self.vars['planned_tp1']
        self.vars['tp2'] = self.vars['planned_tp2']
        self.vars['traded_flush'] = self.vars['planned_flush']

    def _hourly(self) -> dict:
        candles = _closed_candles(self, '1h', HOUR_MS)
        key = int(candles[-1, 0]) if len(candles) else -1
        if self.vars.get('hourly_key') != key:
            self.vars['hourly_key'] = key
            self.vars['hourly'] = self._read_hourly(candles[-HOURLY_LOOKBACK:])
        return self.vars['hourly']

    def _read_hourly(self, candles) -> dict:
        flat = {'macro': 0, 'atr': 0.0}
        if len(candles) < 30:
            return flat
        atr = float(ta.atr(candles, 14))
        if not _finite(atr):
            return flat
        return {'macro': _macro(self), 'atr': atr}


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
