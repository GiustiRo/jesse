import math
import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta

MAX_NOTIONAL_X = 4.4
MIN_STOP_FRACTION = 0.008
MAX_STOP_FRACTION = 0.055
QTY_STEP = 0.001


def _floor_step(qty: float) -> float:
    return math.floor(qty / QTY_STEP + 1e-9) * QTY_STEP


def _finite(*values: float) -> bool:
    return all(math.isfinite(v) for v in values)


class BtcMomentumCore4hR2(Strategy):
    """
    r49 Fase 0: copia congelada de BtcMomentumCore4h; solo cambia risk_pct (5 -> 2).
    El apalancamiento 3x se fija en la configuración de la sesión, no en el código.

    Single-route 4h Time-Series Momentum & Breakout Strategy for BTC-USDT Perpetual.
    Pure Donchian 4h trend breakout with EMA regime alignment, anti-climax range
    filter, breakeven shield, and closing-basis chandelier trailing stop.
    """

    def hyperparameters(self) -> list:
        return [
            {'name': 'risk_pct', 'type': float, 'min': 2.0, 'max': 5.0, 'step': 0.25, 'default': 2.0},
            {'name': 'donchian_len', 'type': int, 'min': 16, 'max': 26, 'step': 2, 'default': 26},
            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'step': 4, 'default': 20},
            {'name': 'ema_slow', 'type': int, 'min': 80, 'max': 140, 'step': 20, 'default': 80},
            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 26, 'step': 2, 'default': 26},
            {'name': 'stop_atr', 'type': float, 'min': 1.6, 'max': 2.6, 'step': 0.2, 'default': 2.0},
            {'name': 'trail_atr', 'type': float, 'min': 3.0, 'max': 4.4, 'step': 0.2, 'default': 4.2},
            {'name': 'be_r', 'type': float, 'min': 1.5, 'max': 2.5, 'step': 0.25, 'default': 1.75},
        ]

    def _plan_order(self, side: int, stop_dist: float, risk_mult: float = 1.0) -> bool:
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
        risk_pct = float(self.hp['risk_pct']) * risk_mult
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
        c = self.candles
        slow_len = int(self.hp['ema_slow'])
        if len(c) < slow_len + 20:
            return 0

        close = self.close
        ema_fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))
        ema_slow_seq = ta.ema(c, period=slow_len, sequential=True)
        ema_slow_now = float(ema_slow_seq[-1])
        ema_slow_prev = float(ema_slow_seq[-5])
        atr = float(ta.atr(c, period=14))
        adx = float(ta.adx(c, period=14))
        rsi = float(ta.rsi(c, period=14))
        if not _finite(close, ema_fast, ema_slow_now, ema_slow_prev, atr, adx, rsi) or atr <= 0:
            return 0

        d_len = int(self.hp['donchian_len'])
        prior = c[-d_len - 1:-1]
        if len(prior) < d_len:
            return 0
        hh = float(prior[:, 3].max())
        stop_dist = float(self.hp['stop_atr']) * atr
        bar_range = self.high - self.low

        if close > ema_slow_now and ema_fast > ema_slow_now and ema_slow_now > ema_slow_prev:
            if close > hh and adx >= self.hp['adx_min'] and 52 <= rsi <= 76 and bar_range <= 3.0 * atr:
                return 1 if self._plan_order(1, stop_dist, risk_mult=1.0) else 0

        return 0

    def _signal(self) -> int:
        if self.vars.get('sig_idx') != self.index:
            self.vars['sig_idx'] = self.index
            self.vars['sig_val'] = self._evaluate_signal()
        return self.vars['sig_val']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return False

    def should_cancel_entry(self) -> bool:
        return True

    def go_long(self) -> None:
        self.buy = self.vars['planned_qty'], self.price

    def go_short(self) -> None:
        pass

    def on_open_position(self, order) -> None:
        entry = self.position.entry_price
        qty = self.position.qty
        r = self.vars.get('planned_r', float(ta.atr(self.candles, period=14)) * float(self.hp['stop_atr']))
        self.vars['init_r'] = r
        self.vars['best_close'] = self.close
        self.vars['extreme'] = self.high
        self.stop_loss = qty, entry - r

    def update_position(self) -> None:
        if not self.is_open:
            return
        qty = self.position.qty
        entry = self.position.entry_price
        r = self.vars.get('init_r', entry * 0.02)
        atr = float(ta.atr(self.candles, period=14))
        if not math.isfinite(atr) or atr <= 0:
            return

        base_trail = float(self.hp['trail_atr'])
        if self.is_long:
            self.vars['best_close'] = max(self.vars.get('best_close', self.close), self.close)
            self.vars['extreme'] = max(self.vars.get('extreme', self.high), self.high)
            best_r = (self.vars['extreme'] - entry) / r if r > 0 else 0.0

            if best_r >= 8.0:
                mult = base_trail * 0.62
            elif best_r >= 5.0:
                mult = base_trail * 0.78
            else:
                mult = base_trail

            new_stop = self.vars['best_close'] - mult * atr
            if best_r >= float(self.hp['be_r']):
                new_stop = max(new_stop, entry + 2.5 * self.fee_rate * entry)
            if self.average_stop_loss < new_stop < self.price:
                self.stop_loss = qty, new_stop
