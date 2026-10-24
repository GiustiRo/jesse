import math

from jesse.strategies import Strategy
import jesse.indicators as ta


# Sizing: a stop-out loses risk_pct of the balance, fees included.
# utils.risk_to_qty caps size at 1x capital, which would waste the 5x account, so qty is computed here.
MAX_NOTIONAL_X = 4.0       # headroom inside a 5x account; keeps liquidation far from the stop
MIN_STOP_FRACTION = 0.005  # below this the ~0.09% taker round trip eats about a fifth of 1R
MAX_STOP_FRACTION = 0.03
QTY_STEP = 0.001           # Binance BTCUSDT lot step

# Circuit breakers: no new entries for the rest of the UTC day after -3R,
# and a 1h pause after 4 losses in a row.
DAILY_LOSS_R = -3.0
MAX_LOSS_STREAK = 4
COOLDOWN_BARS = 12

HOURLY_LOOKBACK = 240
EMA_SLOPE_HOURS = 6
BREAKEVEN_R = 1.5          # trend trades need room; earlier breakeven exits were mostly noise
# Macro filter: 20-day trend on 4h candles (1-4 week time-series momentum is the most
# persistent effect in crypto). Counter-trend breakouts lost in both in-sample years.
MACRO_EMA_BARS = 120
MACRO_SLOPE_BARS = 6
HOUR_MS = 60 * 60_000
DAY_MS = 24 * HOUR_MS


class TrendBreakout5m(Strategy):
    """
    Trend following: buy a fresh breakout_hours high while the 1h trend is aligned and strong
    (the mirrored short side exists but is off by default). The 5m route only times the entry;
    signals use closed 1h candles.

    Trading route: BTC-USDT 5m (futures). Data routes: same exchange and symbol, 1h and 4h
    (the 4h route also stretches the warm-up to 40 days, which the macro EMA needs).
    Regime: 4h close above a rising 20-day EMA, 1h close > EMA50 > EMA200, EMA50 rising,
    ADX >= adx_min (mirror for shorts).
    Stop: stop_atr x 1h ATR. Management: stop to breakeven plus fees at +1.5R, optional partial
    take-profit at tp1_r, and a chandelier trail of trail_atr x 1h ATR from the best price.
    """

    def hyperparameters(self) -> list:
        return [
            # 2% chosen by the user: 2020-2025 gave ~12%/year with a -19% max drawdown.
            {'name': 'risk_pct', 'type': float, 'min': 0.25, 'max': 4.0, 'step': 0.25, 'default': 2.0},
            {'name': 'adx_min', 'type': int, 'min': 15, 'max': 30, 'step': 5, 'default': 20},
            {'name': 'breakout_hours', 'type': int, 'min': 24, 'max': 120, 'step': 24, 'default': 72},
            {'name': 'stop_atr', 'type': float, 'min': 2.0, 'max': 4.0, 'step': 0.5, 'default': 3.0},
            {'name': 'trail_atr', 'type': float, 'min': 2.0, 'max': 4.0, 'step': 0.5, 'default': 3.0},
            # 0 disables the partial take-profit; trend edges live in the right tail.
            {'name': 'tp1_r', 'type': float, 'min': 0.0, 'max': 3.0, 'step': 1.0, 'default': 0.0},
            # Breakout shorts lost money over 2020-2025 as a whole, even in the 2022 bear market.
            {'name': 'allow_shorts', 'type': int, 'min': 0, 'max': 1, 'default': 0},
        ]

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def should_cancel_entry(self) -> bool:
        return True

    # Market entries on purpose: a limit resting at the broken level for 15-60 minutes only filled
    # the breakouts that came back, and 2020-2025 net fell from +42% to +1..10% despite maker fees.
    def go_long(self):
        self._enter()
        self.buy = self.vars['entry_qty'], self.price

    def go_short(self):
        self._enter()
        self.sell = self.vars['entry_qty'], self.price

    def on_open_position(self, order) -> None:
        entry = self.position.entry_price
        qty = self.position.qty
        stop = self.vars['stop_price']
        self.vars.update(r=abs(entry - stop), extreme=entry, at_breakeven=False)
        self.stop_loss = qty, stop

        tp1_r = float(self.hp['tp1_r'])
        half = _floor_step(qty / 2)
        if tp1_r > 0 and half > 0:
            r = self.vars['r']
            self.take_profit = half, (entry + tp1_r * r if self.is_long else entry - tp1_r * r)

    def update_position(self) -> None:
        entry = self.position.entry_price
        r = self.vars['r']
        atr = self._hourly()['atr']
        fees = 2 * self.fee_rate * entry
        qty = self.position.qty

        if self.is_long:
            self.vars['extreme'] = max(self.vars['extreme'], self.high)
            target = self.vars['extreme'] - self.hp['trail_atr'] * atr
            if not self.vars['at_breakeven'] and self.vars['extreme'] >= entry + BREAKEVEN_R * r:
                self.vars['at_breakeven'] = True
                target = max(target, entry + fees)
            if self.average_stop_loss < target < self.price:
                self.stop_loss = qty, target
        else:
            self.vars['extreme'] = min(self.vars['extreme'], self.low)
            target = self.vars['extreme'] + self.hp['trail_atr'] * atr
            if not self.vars['at_breakeven'] and self.vars['extreme'] <= entry - BREAKEVEN_R * r:
                self.vars['at_breakeven'] = True
                target = min(target, entry - fees)
            if self.price < target < self.average_stop_loss:
                self.stop_loss = qty, target

    def on_reduced_position(self, order) -> None:
        # The partial take-profit filled: keep the stop on the remaining size.
        self.stop_loss = self.position.qty, self.average_stop_loss

    def on_close_position(self, order, closed_trade) -> None:
        _record_result(self, closed_trade.pnl)

    def watch_list(self) -> list:
        hourly = self._hourly()
        return [
            ('Regime 1h', hourly['regime']),
            ('ADX 1h', round(hourly['adx'], 1)),
            ('Breakout high', round(hourly['high'], 1)),
            ('Breakout low', round(hourly['low'], 1)),
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
        prev_close = float(self.candles[-2, 2])
        # Fresh cross only: a breakout that already ran is a late, wide-stop entry.
        if hourly['regime'] == 1 and self.close > hourly['high'] >= prev_close:
            side, stop = 1, self.close - self.hp['stop_atr'] * hourly['atr']
        elif hourly['regime'] == -1 and self.close < hourly['low'] <= prev_close:
            side, stop = -1, self.close + self.hp['stop_atr'] * hourly['atr']
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
        flat = {'regime': 0, 'adx': 0.0, 'atr': 0.0, 'high': math.inf, 'low': -math.inf}
        if len(candles) < 210:
            return flat
        close = float(candles[-1, 2])
        ema_fast = ta.ema(candles, 50, sequential=True)
        ema_slow = float(ta.ema(candles, 200))
        adx = float(ta.adx(candles, 14))
        atr = float(ta.atr(candles, 14))
        fast_now, fast_before = float(ema_fast[-1]), float(ema_fast[-1 - EMA_SLOPE_HOURS])
        if not _finite(close, fast_now, fast_before, ema_slow, adx, atr):
            return flat

        regime = 0
        macro = _macro(self)
        if adx >= self.hp['adx_min']:
            if macro == 1 and close > fast_now > ema_slow and fast_now > fast_before:
                regime = 1
            elif self.hp['allow_shorts'] and macro == -1 and close < fast_now < ema_slow and fast_now < fast_before:
                regime = -1
        window = candles[-int(self.hp['breakout_hours']):]
        return {
            'regime': regime, 'adx': adx, 'atr': atr,
            'high': float(window[:, 3].max()), 'low': float(window[:, 4].min()),
        }


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
