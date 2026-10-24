import math
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils

# r49 Fase 2c: copia de R49NullDonchianEnsBtc para WTI-USDT (proxy Dukascopy LIGHTCMDUSD, CFD
# continuo de WTI). Diferencias exigidas por el instrumento, las mismas que en la manga SPY:
#  1. trading_hours(): sesión de CFD de energía, domingo 18:00 a viernes 17:00 hora de Nueva
#     York con pausa diaria 17:00-18:00 (deja 6 velas de 4h por día hábil).
#  2. Los estados Donchian y la volatilidad se calculan sobre velas de sesión, y la entrada
#     se habilita solo si la vela cerrada es de sesión. Rebalanceo y salidas no se limitan.
#  3. "Día" significa día hábil: 6 velas de sesión por día y anualización con 252 días.
#     Los lookbacks 20/55/120/250 y la ventana de 30 días se mantienen en días hábiles.
#  4. Los estados avanzan solo cuando aparece una vela de sesión nueva.

# Lookbacks fijos en días hábiles (20/55/120/250), sin optimizar, en velas de sesión de 4h.
CANDLES_PER_DAY = 6
LOOKBACK_DAYS = (20, 55, 120, 250)
# Salida clásica Donchian: canal de mínimos de la mitad del lookback de entrada.
EXIT_FRACTION = 0.5
# Volatilidad objetivo anual de la manga (punto medio del rango r49 16–18%).
TARGET_VOL = 0.17
# Ventana fija de volatilidad realizada: 30 días hábiles de velas de sesión.
VOL_WINDOW = 30 * CANDLES_PER_DAY
ANNUALIZATION = math.sqrt(252 * CANDLES_PER_DAY)
# Techo de exposición nocional sobre equity pedido por r49 para el nulo.
MAX_NOTIONAL_X = 2.0
# Banda de no-rebalanceo: solo se ajusta si el nocional objetivo se aleja >25% del actual,
# para que el nulo no pague fees por ruido de la estimación de volatilidad.
REBALANCE_BAND = 0.25
MARGIN_USE = 0.92
QTY_STEP = 0.001


def _floor_step(qty: float) -> float:
    return math.floor(qty / QTY_STEP + 1e-9) * QTY_STEP


class R49NullDonchianEnsWti(Strategy):
    """
    r49 Fase 2c, manga WTI del motor nulo: ensamble Donchian multi-lookback long/flat.
    Cada componente entra con cierre > máximo de N velas de sesión previas y sale con
    cierre < mínimo de N/2. La exposición es la fracción de componentes activos, escalada
    a volatilidad objetivo 17% y limitada a 2x nocional. Sin stops.
    """

    def trading_hours(self):
        # Sesión de CFD de energía (WTI): domingo 18:00 a viernes 17:00 hora de Nueva York,
        # con pausa diaria 17:00-18:00. Se filtra por hora de apertura de la vela de 4h.
        return {'timezone': 'America/New_York',
                'hours': {'Sun': '18:00-24:00', 'Mon-Thu': ['00:00-17:00', '18:00-24:00'], 'Fri': '00:00-17:00'}}

    @property
    @cached
    def session_candles(self) -> np.ndarray:
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    def _lookbacks(self) -> list:
        return [d * CANDLES_PER_DAY for d in LOOKBACK_DAYS]

    def _update_states(self) -> None:
        """Avanza el estado de cada componente con la última vela de sesión cerrada.

        En la primera llamada reconstruye los estados recorriendo el calentamiento,
        para que el ensamble no arranque artificialmente plano.
        """
        c = self.session_candles
        if len(c) == 0:
            return
        last_ts = int(c[-1, 0])
        if 'states' in self.vars and self.vars.get('state_ts') == last_ts:
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
        self.vars['state_ts'] = last_ts

    @staticmethod
    def _step(states: list, highs, lows, closes, i: int, lbs: list) -> list:
        out = []
        for s, n in zip(states, lbs):
            m = max(int(n * EXIT_FRACTION), 1)
            if i - n < 0:
                out.append(0)
                continue
            hh = highs[i - n:i].max()
            ll = lows[i - m:i].min()
            if s == 0 and closes[i] > hh:
                s = 1
            elif s == 1 and closes[i] < ll:
                s = 0
            out.append(s)
        return out

    def before(self) -> None:
        # Avanza los estados en cada vela, haya o no posición abierta.
        self._update_states()

    def _target_qty(self) -> float:
        self._update_states()
        states = self.vars.get('states')
        if not states:
            return 0.0
        frac = sum(states) / len(states)
        if frac <= 0:
            return 0.0
        closes = self.session_candles[-VOL_WINDOW - 1:, 2]
        rets = np.diff(np.log(closes))
        rv = float(np.std(rets, ddof=1)) * ANNUALIZATION if len(rets) > 10 else float('nan')
        if not math.isfinite(rv) or rv <= 0:
            return 0.0
        equity = self.balance + (self.position.pnl if self.is_open else 0.0)
        notional_x = min(MAX_NOTIONAL_X, frac * TARGET_VOL / rv)
        return max(equity * notional_x / self.price, 0.0)

    def should_long(self) -> bool:
        if not self.is_trading_hours:
            return False
        qty = _floor_step(min(self._target_qty(), self.leveraged_available_margin * MARGIN_USE / self.price))
        self.vars['entry_qty'] = qty
        return qty > 0

    def should_short(self) -> bool:
        return False

    def should_cancel_entry(self) -> bool:
        return True

    def go_long(self) -> None:
        self.buy = self.vars['entry_qty'], self.price

    def go_short(self) -> None:
        pass

    def update_position(self) -> None:
        if not self.is_open:
            return
        target = self._target_qty()
        cur = self.position.qty
        if target <= 0:
            self.liquidate()
            return
        if target > cur * (1 + REBALANCE_BAND):
            add = _floor_step(min(target - cur, self.leveraged_available_margin * MARGIN_USE / self.price))
            if add > 0:
                self.buy = add, self.price
        elif target < cur * (1 - REBALANCE_BAND):
            cut = _floor_step(cur - target)
            if 0 < cut < cur:
                self.take_profit = cut, self.price
