import math

from jesse import utils
from jesse.strategies import Strategy
import jesse.indicators as ta


# 10% of balance as notional. A 1.2% stop on that size risks 0.12% of equity.
# Wider than that, the 5m ATR is too large for this allocation, so the trade is skipped.
ALLOCATION = 0.10
MAX_STOP_FRACTION = 0.012
MAX_HOLD_BARS = 48
HOUR_MS = 60 * 60_000


class H1Pullback5m(Strategy):
    """
    5m pullback in the direction of the last closed 1h trend.

    Trading route: BTC-USDT, 5m.
    Data route: same exchange and symbol, 1h, no strategy.
    Warm-up of 240 candles (or more) so the 1h EMA and ADX exist before the first entry.
    Shorts need a futures route.
    """

    def hyperparameters(self) -> list:
        # Ranges are the plateau to stress, not a search for a peak.
        return [
            {'name': 'adx_min', 'type': int, 'min': 18, 'max': 26, 'default': 22},
            {'name': 'hourly_ema', 'type': int, 'min': 40, 'max': 60, 'default': 50},
            {'name': 'stop_atr', 'type': float, 'min': 1.2, 'max': 2.0, 'default': 1.5, 'step': 0.1},
            {'name': 'reward_r', 'type': float, 'min': 2.0, 'max': 3.0, 'default': 2.5, 'step': 0.5},
        ]

    def should_long(self) -> bool:
        return self._hourly_regime() == 1 and self._pullback(1) and self._entry_qty() > 0

    def should_short(self) -> bool:
        return self._hourly_regime() == -1 and self._pullback(-1) and self._entry_qty() > 0

    def should_cancel_entry(self) -> bool:
        return True

    def go_long(self):
        self.vars['stop_distance'] = self._stop_distance()
        self.buy = self._entry_qty(), self.price

    def go_short(self):
        self.vars['stop_distance'] = self._stop_distance()
        self.sell = self._entry_qty(), self.price

    def on_open_position(self, order) -> None:
        distance = self.vars['stop_distance']
        reward = distance * float(self.hp['reward_r'])
        qty = self.position.qty
        entry = self.position.entry_price
        self.vars['entry_index'] = self.index

        if self.is_long:
            self.stop_loss = qty, entry - distance
            self.take_profit = qty, entry + reward
        elif self.is_short:
            self.stop_loss = qty, entry + distance
            self.take_profit = qty, entry - reward

    def update_position(self) -> None:
        if self.index - self.vars.get('entry_index', self.index) >= MAX_HOLD_BARS:
            self.liquidate()
            return

        # Exit when the last closed hour crosses its EMA against the position.
        # ADX fading is not an exit: the stop, target, or 4h time stop handles that.
        bias = self._hourly_bias()
        if self.is_long and bias == -1:
            self.liquidate()
        elif self.is_short and bias == 1:
            self.liquidate()

    def _hourly_regime(self) -> int:
        candles = self._closed_hourly_candles()
        period = int(self.hp['hourly_ema'])
        if len(candles) <= max(period, 28):
            return 0

        close = float(candles[-1, 2])
        hourly_ema = float(ta.ema(candles, period))
        adx = float(ta.adx(candles, 14))
        direction = ta.di(candles, 14)
        plus = float(direction.plus)
        minus = float(direction.minus)
        if not _finite(close, hourly_ema, adx, plus, minus):
            return 0
        if adx < self.hp['adx_min']:
            return 0
        if close > hourly_ema and plus > minus:
            return 1
        if close < hourly_ema and minus > plus:
            return -1
        return 0

    def _hourly_bias(self) -> int:
        candles = self._closed_hourly_candles()
        period = int(self.hp['hourly_ema'])
        if len(candles) <= period:
            return 0
        close = float(candles[-1, 2])
        hourly_ema = float(ta.ema(candles, period))
        if not _finite(close, hourly_ema):
            return 0
        if close > hourly_ema:
            return 1
        if close < hourly_ema:
            return -1
        return 0

    def _pullback(self, side: int) -> bool:
        candles = self.candles
        if len(candles) < 30:
            return False

        emas = ta.ema(candles, 20, sequential=True)
        ema_now = float(emas[-1])
        ema_prev = float(emas[-2])
        rsi = float(ta.rsi(candles, 14))
        if not _finite(ema_now, ema_prev, rsi):
            return False

        if side == 1:
            touched = self.low <= ema_now or float(candles[-2, 4]) <= ema_prev
            return touched and self.close > ema_now and 45 <= rsi <= 62

        touched = self.high >= ema_now or float(candles[-2, 3]) >= ema_prev
        return touched and self.close < ema_now and 38 <= rsi <= 55

    def _stop_distance(self) -> float:
        atr = float(ta.atr(self.candles, 14))
        if not _finite(atr) or atr <= 0 or self.price <= 0:
            return 0.0
        distance = atr * float(self.hp['stop_atr'])
        if distance / self.price > MAX_STOP_FRACTION:
            return 0.0
        return distance

    def _entry_qty(self) -> float:
        if self._stop_distance() <= 0:
            return 0.0
        return utils.size_to_qty(
            self.balance * ALLOCATION,
            self.price,
            fee_rate=self.fee_rate,
        )

    def _closed_hourly_candles(self):
        # get_candles('1h') includes the hour still forming from 5m bars already seen.
        # Drop that row unless its window has ended, so the regime uses a closed hour.
        candles = self.get_candles(self.exchange, self.symbol, '1h')
        if len(candles) == 0:
            return candles
        last_open = int(candles[-1, 0])
        if last_open + HOUR_MS <= int(self.time):
            return candles
        return candles[:-1]


def _finite(*values: float) -> bool:
    return all(math.isfinite(value) for value in values)
