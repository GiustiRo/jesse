import math
import numpy as np
from jesse.strategies import Strategy

# r49 Fase 2b (protocolo B5): motor Donchian solo-corto para ETH-USDT (componentes -1/0). Misma lógica que R49NullDonchianEnsBtc
# con cada componente en -1/0/+1 en vez de 0/+1. Lookbacks, vol objetivo, ventana de vol,
# banda y techo sin cambios.

# Lados habilitados del ensamble (B3: ambos; B5 ETH: solo corto).
ALLOW_LONG = False
ALLOW_SHORT = True
# Lookbacks fijos en días (20/55/120/250), sin optimizar, convertidos a velas de 4h.
CANDLES_PER_DAY = 6
LOOKBACK_DAYS = (20, 55, 120, 250)
# Salida clásica Donchian: canal opuesto de la mitad del lookback de entrada.
EXIT_FRACTION = 0.5
# Volatilidad objetivo anual de la manga (punto medio del rango r49 16–18%).
TARGET_VOL = 0.17
# Ventana fija de volatilidad realizada: 30 días de velas de 4h.
VOL_WINDOW = 30 * CANDLES_PER_DAY
ANNUALIZATION = math.sqrt(365 * CANDLES_PER_DAY)
# Techo de exposición nocional sobre equity pedido por r49 para el nulo.
MAX_NOTIONAL_X = 2.0
# Banda de no-rebalanceo: solo se ajusta si el nocional objetivo se aleja >25% del actual,
# para que el nulo no pague fees por ruido de la estimación de volatilidad.
REBALANCE_BAND = 0.25
MARGIN_USE = 0.92
QTY_STEP = 0.001


def _floor_step(qty: float) -> float:
    return math.floor(qty / QTY_STEP + 1e-9) * QTY_STEP


class R49DonchianShortEth(Strategy):
    """
    r49 Fase 2b, motor Donchian L/S. Cada componente entra largo con cierre > máximo de N
    velas previas (sale con cierre < mínimo de N/2) y corto con cierre < mínimo de N (sale con
    cierre > máximo de N/2); si en la misma vela sale de un lado y cumple la entrada del otro,
    cambia de lado. La exposición es la media de componentes en [-1, 1], escalada a vol
    objetivo 17% y limitada a 2x nocional. Sin stops.
    """

    def _lookbacks(self) -> list:
        return [d * CANDLES_PER_DAY for d in LOOKBACK_DAYS]

    def _history(self) -> np.ndarray:
        return self.candles

    def _new_bar_key(self, c: np.ndarray):
        return self.index

    def _update_states(self) -> None:
        """Avanza el estado de cada componente con la vela cerrada actual.

        En la primera llamada reconstruye los estados recorriendo el calentamiento,
        para que el ensamble no arranque artificialmente plano.
        """
        c = self._history()
        if len(c) == 0:
            return
        key = self._new_bar_key(c)
        if 'states' in self.vars and self.vars.get('state_key') == key:
            return
        highs, lows, closes = c[:, 3], c[:, 4], c[:, 2]
        lbs = self._lookbacks()
        if 'states' not in self.vars:
            states = [0] * len(lbs)
            start = max(lbs) + 1
            for i in range(start, len(c)):
                states = self._step(states, highs, lows, closes, i, lbs)
            self.vars['states'] = states
        else:
            self.vars['states'] = self._step(self.vars['states'], highs, lows, closes, len(c) - 1, lbs)
        self.vars['state_key'] = key

    @staticmethod
    def _step(states: list, highs, lows, closes, i: int, lbs: list) -> list:
        out = []
        for s, n in zip(states, lbs):
            m = max(int(n * EXIT_FRACTION), 1)
            if i - n < 0:
                out.append(0)
                continue
            if s == 1 and closes[i] < lows[i - m:i].min():
                s = 0
            elif s == -1 and closes[i] > highs[i - m:i].max():
                s = 0
            if s == 0:
                if ALLOW_LONG and closes[i] > highs[i - n:i].max():
                    s = 1
                elif ALLOW_SHORT and closes[i] < lows[i - n:i].min():
                    s = -1
            out.append(s)
        return out

    def before(self) -> None:
        # Avanza los estados en cada vela, haya o no posición abierta.
        self._update_states()

    def _target_signed_qty(self) -> float:
        self._update_states()
        states = self.vars.get('states')
        if not states:
            return 0.0
        frac = sum(states) / len(states)
        if frac == 0:
            return 0.0
        closes = self._history()[-VOL_WINDOW - 1:, 2]
        rets = np.diff(np.log(closes))
        rv = float(np.std(rets, ddof=1)) * ANNUALIZATION if len(rets) > 10 else float('nan')
        if not math.isfinite(rv) or rv <= 0:
            return 0.0
        equity = self.balance + (self.position.pnl if self.is_open else 0.0)
        notional_x = min(MAX_NOTIONAL_X, abs(frac) * TARGET_VOL / rv)
        return math.copysign(max(equity * notional_x / self.price, 0.0), frac)

    def _entry_allowed(self) -> bool:
        return True

    def _entry_qty(self) -> float:
        t = self._target_signed_qty()
        qty = _floor_step(min(abs(t), self.leveraged_available_margin * MARGIN_USE / self.price))
        self.vars['entry_qty'] = qty
        return math.copysign(qty, t) if qty > 0 else 0.0

    def should_long(self) -> bool:
        return self._entry_allowed() and self._entry_qty() > 0

    def should_short(self) -> bool:
        return self._entry_allowed() and self._entry_qty() < 0

    def should_cancel_entry(self) -> bool:
        return True

    def go_long(self) -> None:
        self.buy = self.vars['entry_qty'], self.price

    def go_short(self) -> None:
        self.sell = self.vars['entry_qty'], self.price

    def update_position(self) -> None:
        if not self.is_open:
            return
        target = self._target_signed_qty()
        cur = abs(self.position.qty)
        side = 1 if self.is_long else -1
        # Objetivo plano o del lado opuesto: se cierra; la entrada opuesta llega por should_*.
        if target == 0 or math.copysign(1, target) != side:
            self.liquidate()
            return
        t = abs(target)
        if t > cur * (1 + REBALANCE_BAND):
            add = _floor_step(min(t - cur, self.leveraged_available_margin * MARGIN_USE / self.price))
            if add > 0:
                if side == 1:
                    self.buy = add, self.price
                else:
                    self.sell = add, self.price
        elif t < cur * (1 - REBALANCE_BAND):
            cut = _floor_step(cur - t)
            if 0 < cut < cur:
                self.take_profit = cut, self.price
