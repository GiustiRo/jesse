import math
import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta
from jesse import utils

MAX_NOTIONAL_X = 3.6
QTY_STEP = 0.001


def _floor_step(qty: float) -> float:
    return math.floor(qty / QTY_STEP + 1e-9) * QTY_STEP


def _finite(*values: float) -> bool:
    return all(math.isfinite(v) for v in values)


class BtcRegimeBreakout1h(Strategy):
    """
    Iter 2B: Multi-Timeframe (1h + 4h) TEMA Impulse Pullback-Limit Strategy with
    Macro Regime Gating, Controlled Risk Sizing, and Active Position Management.
    """

    def hyperparameters(self) -> list:
        return [
            {'name': 'risk_pct', 'type': float, 'min': 2.0, 'max': 6.0, 'step': 0.5, 'default': 4.5},
            {'name': 'tema_fast_1h', 'type': int, 'min': 6, 'max': 18, 'step': 2, 'default': 10},
            {'name': 'tema_slow_1h', 'type': int, 'min': 50, 'max': 110, 'step': 10, 'default': 80},
            {'name': 'tema_fast_4h', 'type': int, 'min': 12, 'max': 28, 'step': 4, 'default': 20},
            {'name': 'tema_slow_4h', 'type': int, 'min': 50, 'max': 90, 'step': 10, 'default': 70},
            {'name': 'adx_min', 'type': int, 'min': 30, 'max': 46, 'step': 2, 'default': 40},
            {'name': 'cmo_min', 'type': int, 'min': 30, 'max': 48, 'step': 2, 'default': 40},
            {'name': 'entry_atr', 'type': float, 'min': 0.5, 'max': 1.3, 'step': 0.1, 'default': 1.0},
            {'name': 'stop_atr', 'type': float, 'min': 2.4, 'max': 4.4, 'step': 0.2, 'default': 3.4},
            {'name': 'tp_atr', 'type': float, 'min': 2.4, 'max': 4.4, 'step': 0.2, 'default': 3.2},
        ]

    def _compute_signals(self) -> int:
        c1h = self.candles
        c4h = self.get_candles(self.exchange, self.symbol, '4h')
        if len(c1h) < 120 or len(c4h) < 120:
            return 0

        tema_f_1h = float(ta.tema(c1h, int(self.hp['tema_fast_1h'])))
        tema_s_1h = float(ta.tema(c1h, int(self.hp['tema_slow_1h'])))
        tema_f_4h = float(ta.tema(c4h, int(self.hp['tema_fast_4h'])))
        tema_s_4h = float(ta.tema(c4h, int(self.hp['tema_slow_4h'])))
        ema_macro_4h = float(ta.ema(c4h, 100))
        close_4h = float(c4h[-1, 2])

        adx = float(ta.adx(c1h, 14))
        cmo = float(ta.cmo(c1h, 14))
        atr = float(ta.atr(c1h, 14))
        if not _finite(tema_f_1h, tema_s_1h, tema_f_4h, tema_s_4h, ema_macro_4h, adx, cmo, atr) or atr <= 0:
            return 0

        self.vars['sig_atr'] = atr
        adx_min = float(self.hp['adx_min'])
        cmo_min = float(self.hp['cmo_min'])

        # Long: 1h & 4h TEMA bullish + 4h price above macro EMA100 (avoids 2022 bear market traps)
        if tema_f_1h > tema_s_1h and tema_f_4h > tema_s_4h and close_4h > ema_macro_4h * 0.985:
            if adx > adx_min and cmo > cmo_min:
                self.vars['risk_mult'] = 1.15 if close_4h > ema_macro_4h else 0.75
                return 1

        # Short: 1h & 4h TEMA bearish + momentum confirmation
        if tema_f_1h < tema_s_1h and tema_f_4h < tema_s_4h:
            if adx > adx_min and cmo < -cmo_min:
                # Full size in macro bear (close_4h < ema_macro_4h), reduced size in macro bull pullbacks
                self.vars['risk_mult'] = 1.10 if close_4h < ema_macro_4h else 0.70
                return -1

        return 0

    def _signal(self) -> int:
        if self.vars.get('sig_idx') != self.index:
            self.vars['sig_idx'] = self.index
            self.vars['sig_val'] = self._compute_signals()
        return self.vars['sig_val']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def should_cancel_entry(self) -> bool:
        return True

    def _calc_qty(self, entry_price: float, stop_dist: float) -> float:
        balance = self.balance
        risk_pct = float(self.hp['risk_pct']) * float(self.vars.get('risk_mult', 1.0))
        loss_per_qty = stop_dist + 2.0 * self.fee_rate * entry_price
        qty = (balance * (risk_pct / 100.0)) / loss_per_qty
        max_notional_qty = (balance * MAX_NOTIONAL_X) / entry_price
        max_margin_qty = (self.leveraged_available_margin * 0.90) / entry_price
        return _floor_step(min(qty, max_notional_qty, max_margin_qty))

    def go_long(self) -> None:
        atr = float(self.vars.get('sig_atr', ta.atr(self.candles, 14)))
        entry_price = self.price - float(self.hp['entry_atr']) * atr
        stop_dist = float(self.hp['stop_atr']) * atr
        if entry_price <= stop_dist:
            return
        qty = self._calc_qty(entry_price, stop_dist)
        if qty > 0:
            self.vars['entry_atr_val'] = atr
            self.buy = qty, entry_price

    def go_short(self) -> None:
        atr = float(self.vars.get('sig_atr', ta.atr(self.candles, 14)))
        entry_price = self.price + float(self.hp['entry_atr']) * atr
        stop_dist = float(self.hp['stop_atr']) * atr
        qty = self._calc_qty(entry_price, stop_dist)
        if qty > 0:
            self.vars['entry_atr_val'] = atr
            self.sell = qty, entry_price

    def on_open_position(self, order) -> None:
        atr = float(self.vars.get('entry_atr_val', ta.atr(self.candles, 14)))
        stop_dist = float(self.hp['stop_atr']) * atr
        tp_dist = float(self.hp['tp_atr']) * atr
        self.vars['open_atr'] = atr
        self.vars['open_idx'] = self.index
        if self.is_long:
            self.stop_loss = self.position.qty, self.position.entry_price - stop_dist
            self.take_profit = self.position.qty, self.position.entry_price + tp_dist
        elif self.is_short:
            self.stop_loss = self.position.qty, self.position.entry_price + stop_dist
            self.take_profit = self.position.qty, self.position.entry_price - tp_dist

    def update_position(self) -> None:
        if not self.is_open:
            return
        atr = float(self.vars.get('open_atr', ta.atr(self.candles, 14)))
        entry = self.position.entry_price
        qty = self.position.qty
        bars_held = self.index - int(self.vars.get('open_idx', self.index))

        # Protect winning trades once they reach +2.0 ATR and cut stale reversals
        if self.is_long:
            if self.high - entry >= 2.0 * atr:
                be_stop = entry + 0.3 * atr
                if self.average_stop_loss < be_stop < self.price:
                    self.stop_loss = qty, be_stop
            if bars_held >= 48:
                c4h = self.get_candles(self.exchange, self.symbol, '4h')
                if float(ta.tema(c4h, int(self.hp['tema_fast_4h']))) < float(ta.tema(c4h, int(self.hp['tema_slow_4h']))):
                    if float(ta.tema(self.candles, int(self.hp['tema_fast_1h']))) < float(ta.tema(self.candles, int(self.hp['tema_slow_1h']))):
                        self.liquidate()
        elif self.is_short:
            if entry - self.low >= 2.0 * atr:
                be_stop = entry - 0.3 * atr
                if self.price < be_stop < self.average_stop_loss:
                    self.stop_loss = qty, be_stop
            if bars_held >= 48:
                c4h = self.get_candles(self.exchange, self.symbol, '4h')
                if float(ta.tema(c4h, int(self.hp['tema_fast_4h']))) > float(ta.tema(c4h, int(self.hp['tema_slow_4h']))):
                    if float(ta.tema(self.candles, int(self.hp['tema_fast_1h']))) > float(ta.tema(self.candles, int(self.hp['tema_slow_1h']))):
                        self.liquidate()
