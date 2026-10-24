import math
import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta
from jesse import utils

MAX_NOTIONAL_X = 4.2
MIN_STOP_FRACTION = 0.006
MAX_STOP_FRACTION = 0.05
QTY_STEP = 0.001
FOUR_HOUR_MS = 4 * 60 * 60_000


def _floor_step(qty: float) -> float:
    return math.floor(qty / QTY_STEP + 1e-9) * QTY_STEP


def _finite(*values: float) -> bool:
    return all(math.isfinite(v) for v in values)


def _efficiency_ratio(candles: np.ndarray, period: int = 10) -> float:
    if len(candles) <= period:
        return 0.0
    closes = candles[-period - 1:, 2]
    net = abs(float(closes[-1] - closes[0]))
    path = float(np.abs(np.diff(closes)).sum())
    return net / path if path > 0 else 0.0


class BtcAdaptiveTrend2h(Strategy):
    """
    2h Adaptive Trend Strategy using Keltner + SuperTrend + Efficiency Ratio with 4h Macro Filter.
    Trading route: 2h. Data route: 4h.
    """

    def hyperparameters(self) -> list:
        return [
            {'name': 'risk_pct', 'type': float, 'min': 1.0, 'max': 3.0, 'step': 0.25, 'default': 2.0},
            {'name': 'st_period', 'type': int, 'min': 8, 'max': 16, 'step': 2, 'default': 10},
            {'name': 'st_factor', 'type': float, 'min': 2.0, 'max': 4.0, 'step': 0.25, 'default': 2.75},
            {'name': 'kelt_mult', 'type': float, 'min': 1.4, 'max': 2.6, 'step': 0.2, 'default': 1.8},
            {'name': 'stop_atr', 'type': float, 'min': 1.8, 'max': 3.6, 'step': 0.2, 'default': 2.4},
            {'name': 'trail_atr', 'type': float, 'min': 2.5, 'max': 5.0, 'step': 0.25, 'default': 3.5},
            {'name': 'allow_shorts', 'type': int, 'min': 0, 'max': 1, 'step': 1, 'default': 1},
        ]

    def _closed_4h(self) -> np.ndarray:
        candles = self.get_candles(self.exchange, self.symbol, '4h')
        if len(candles) == 0:
            return candles
        if int(candles[-1, 0]) + FOUR_HOUR_MS <= int(self.time):
            return candles
        return candles[:-1]

    def _macro_regime(self) -> int:
        c4 = self._closed_4h()
        if len(c4) < 110:
            return 0
        close = float(c4[-1, 2])
        ema80 = ta.ema(c4, period=80, sequential=True)
        now, prev = float(ema80[-1]), float(ema80[-4])
        if not _finite(close, now, prev):
            return 0
        if close > now and now > prev:
            return 1
        if int(self.hp['allow_shorts']) == 1 and close < now and now < prev:
            return -1
        return 0

    def _plan_order(self, side: int, stop_dist: float) -> bool:
        price = self.close
        if price <= 0 or not math.isfinite(stop_dist) or stop_dist <= 0:
            return False
        frac = max(stop_dist / price, MIN_STOP_FRACTION)
        if frac > MAX_STOP_FRACTION:
            return False
        actual_dist = frac * price
        stop_price = price - actual_dist if side == 1 else price + actual_dist
        if stop_price <= 0:
            return False

        balance = self.balance
        risk_pct = float(self.hp['risk_pct']) * (0.8 if side == -1 else 1.0)
        loss_per_qty = actual_dist + 2.0 * self.fee_rate * price
        qty = (balance * (risk_pct / 100.0)) / loss_per_qty
        max_notional_qty = (balance * MAX_NOTIONAL_X) / price
        max_margin_qty = (self.leveraged_available_margin * 0.92) / price
        qty = _floor_step(min(qty, max_notional_qty, max_margin_qty))
        if qty <= 0:
            return False

        self.vars['planned_qty'] = qty
        self.vars['planned_stop'] = stop_price
        self.vars['planned_r'] = actual_dist
        return True

    def _evaluate_signal(self) -> int:
        if len(self.candles) < 160:
            return 0
        macro = self._macro_regime()
        if macro == 0:
            return 0

        c = self.candles
        st = ta.supertrend(c, period=int(self.hp['st_period']), factor=float(self.hp['st_factor']))
        kc = ta.keltner(c, period=20, multiplier=float(self.hp['kelt_mult']))
        atr = float(ta.atr(c, period=14))
        adx = float(ta.adx(c, period=14))
        er = _efficiency_ratio(c, period=10)
        if not _finite(atr, adx, er, kc.upperband, kc.lowerband, float(st.trend)) or atr <= 0:
            return 0

        stop_dist = float(self.hp['stop_atr']) * atr

        if macro == 1 and self.close > float(st.trend) and self.close > kc.upperband and adx >= 18 and er >= 0.22:
            return 1 if self._plan_order(1, stop_dist) else 0

        if macro == -1 and self.close < float(st.trend) and self.close < kc.lowerband and adx >= 22 and er >= 0.25:
            return -1 if self._plan_order(-1, stop_dist) else 0

        return 0

    def _signal(self) -> int:
        if self.vars.get('sig_idx') != self.index:
            self.vars['sig_idx'] = self.index
            self.vars['sig_val'] = self._evaluate_signal()
        return self.vars['sig_val']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def should_cancel_entry(self) -> bool:
        return True

    def go_long(self) -> None:
        self.buy = self.vars['planned_qty'], self.price

    def go_short(self) -> None:
        self.sell = self.vars['planned_qty'], self.price

    def on_open_position(self, order) -> None:
        entry = self.position.entry_price
        qty = self.position.qty
        r = self.vars.get('planned_r', float(ta.atr(self.candles, period=14)) * float(self.hp['stop_atr']))
        self.vars['init_r'] = r
        self.vars['extreme'] = self.high if self.is_long else self.low
        stop = entry - r if self.is_long else entry + r
        self.stop_loss = qty, stop

    def update_position(self) -> None:
        if not self.is_open:
            return
        qty = self.position.qty
        entry = self.position.entry_price
        r = self.vars.get('init_r', entry * 0.015)
        atr = float(ta.atr(self.candles, period=14))
        st = ta.supertrend(self.candles, period=int(self.hp['st_period']), factor=float(self.hp['st_factor']))
        if not math.isfinite(atr) or atr <= 0:
            return

        base_trail = float(self.hp['trail_atr'])
        if self.is_long:
            if self.close < float(st.trend):
                self.liquidate()
                return
            self.vars['extreme'] = max(self.vars.get('extreme', self.high), self.high)
            best_r = (self.vars['extreme'] - entry) / r if r > 0 else 0.0
            mult = base_trail * 0.65 if best_r >= 4.0 else base_trail
            new_stop = self.vars['extreme'] - mult * atr
            if best_r >= 2.0:
                new_stop = max(new_stop, entry + 2.5 * self.fee_rate * entry)
            if self.average_stop_loss < new_stop < self.price:
                self.stop_loss = qty, new_stop
        elif self.is_short:
            if self.close > float(st.trend):
                self.liquidate()
                return
            self.vars['extreme'] = min(self.vars.get('extreme', self.low), self.low)
            best_r = (entry - self.vars['extreme']) / r if r > 0 else 0.0
            mult = base_trail * 0.60 if best_r >= 3.0 else base_trail * 0.85
            new_stop = self.vars['extreme'] + mult * atr
            if best_r >= 1.8:
                new_stop = min(new_stop, entry - 2.5 * self.fee_rate * entry)
            if self.price < new_stop < self.average_stop_loss:
                self.stop_loss = qty, new_stop
