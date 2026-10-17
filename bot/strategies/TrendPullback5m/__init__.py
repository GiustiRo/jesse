import math

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
EMA_SLOPE_HOURS = 6
TOUCH_BARS = 6             # the pullback must have reached the 1h EMA50 within the last 30 minutes
TOUCH_ZONE_ATR = 0.25      # "reached" = within a quarter 1h ATR of the EMA50
SWING_BARS = 12            # the stop goes below the last hour of 5m lows
STOP_BUFFER_ATR = 0.5
MIN_STOP_ATR = 2.0         # in-sample, stops tighter than 2 x 1h ATR were mostly noise stop-outs
BREAKEVEN_R = 1.5
REENTRY_BARS = 72          # 6h: one attempt per pullback
# Macro filter: 20-day trend on 4h candles (1-4 week time-series momentum is the most
# persistent effect in crypto).
MACRO_EMA_BARS = 120
MACRO_SLOPE_BARS = 6
HOUR_MS = 60 * 60_000
DAY_MS = 24 * HOUR_MS


class TrendPullback5m(Strategy):
    """
    Trend pullback: in a 20-day uptrend, buy the 5m reversal after price pulls back to the
    rising 1h EMA50 (mirror for shorts). Entering at value instead of at a breakout gives a
    better price for the same trend exposure. Signals use closed 1h/4h candles.

    Trading route: BTC-USDT 5m (futures). Data routes: same exchange and symbol, 1h and 4h
    (the 4h route also stretches the warm-up to 40 days, which the macro EMA needs).
    Regime: 4h close above a rising 20-day EMA, 1h EMA50 > EMA200 and EMA50 rising.
    Entry: a 5m low reached the 1h EMA50 zone in the last 30 minutes and the current 5m candle
    closes bullish above the EMA50. Stop below the last hour's low, at least 2 x 1h ATR away.
    Management: stop to breakeven plus fees at +1.5R and a chandelier trail of trail_atr x 1h
    ATR from the best price.
    """

    def hyperparameters(self) -> list:
        return [
            {'name': 'risk_pct', 'type': float, 'min': 0.25, 'max': 2.0, 'step': 0.25, 'default': 1.0},
            {'name': 'trail_atr', 'type': float, 'min': 2.0, 'max': 4.0, 'step': 0.5, 'default': 3.0},
            {'name': 'allow_shorts', 'type': int, 'min': 0, 'max': 1, 'default': 1},
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
            target = self.vars['extreme'] - self.hp['trail_atr'] * atr
            if self.vars['extreme'] >= entry + BREAKEVEN_R * r:
                target = max(target, entry + fees)
            if self.average_stop_loss < target < self.price:
                self.stop_loss = qty, target
        else:
            self.vars['extreme'] = min(self.vars['extreme'], self.low)
            target = self.vars['extreme'] + self.hp['trail_atr'] * atr
            if self.vars['extreme'] <= entry - BREAKEVEN_R * r:
                target = min(target, entry - fees)
            if self.price < target < self.average_stop_loss:
                self.stop_loss = qty, target

    def on_close_position(self, order, closed_trade) -> None:
        self.vars['last_exit_index'] = self.index
        _record_result(self, closed_trade.pnl)

    def watch_list(self) -> list:
        hourly = self._hourly()
        return [
            ('Regime', hourly['regime']),
            ('EMA50 1h', round(hourly['ema50'], 1)),
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
        if hourly['regime'] == 0 or not _can_trade(self):
            return 0
        if self.index - self.vars.get('last_exit_index', -REENTRY_BARS) < REENTRY_BARS:
            return 0

        ema50, atr = hourly['ema50'], hourly['atr']
        zone = TOUCH_ZONE_ATR * atr
        touch = self.candles[-TOUCH_BARS:]
        swing = self.candles[-SWING_BARS:]
        if (hourly['regime'] == 1 and float(touch[:, 4].min()) <= ema50 + zone
                and self.close > ema50 and self.close > self.open):
            side = 1
            stop = min(float(swing[:, 4].min()) - STOP_BUFFER_ATR * atr, self.close - MIN_STOP_ATR * atr)
        elif (hourly['regime'] == -1 and float(touch[:, 3].max()) >= ema50 - zone
                and self.close < ema50 and self.close < self.open):
            side = -1
            stop = max(float(swing[:, 3].max()) + STOP_BUFFER_ATR * atr, self.close + MIN_STOP_ATR * atr)
        else:
            return 0
        return side if _plan_entry(self, side, stop) else 0

    def _enter(self) -> None:
        self.vars['stop_price'] = self.vars['planned_stop']
        self.vars['entry_qty'] = self.vars['planned_qty']
        self.vars['risk_usd'] = self.vars['planned_risk_usd']

    def _hourly(self) -> dict:
        candles = _closed_candles(self, '1h', HOUR_MS)
        key = int(candles[-1, 0]) if len(candles) else -1
        if self.vars.get('hourly_key') != key:
            self.vars['hourly_key'] = key
            self.vars['hourly'] = self._read_hourly(candles[-HOURLY_LOOKBACK:])
        return self.vars['hourly']

    def _read_hourly(self, candles) -> dict:
        flat = {'regime': 0, 'ema50': 0.0, 'atr': 0.0}
        if len(candles) < 210:
            return flat
        ema_fast = ta.ema(candles, 50, sequential=True)
        ema_slow = float(ta.ema(candles, 200))
        atr = float(ta.atr(candles, 14))
        fast_now, fast_before = float(ema_fast[-1]), float(ema_fast[-1 - EMA_SLOPE_HOURS])
        if not _finite(fast_now, fast_before, ema_slow, atr):
            return flat

        regime = 0
        macro = _macro(self)
        if macro == 1 and fast_now > ema_slow and fast_now > fast_before:
            regime = 1
        elif self.hp['allow_shorts'] and macro == -1 and fast_now < ema_slow and fast_now < fast_before:
            regime = -1
        return {'regime': regime, 'ema50': fast_now, 'atr': atr}


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
