import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def return_forecast(rows, autoregressive):
    """240 observed (x,y) pairs, then six genuinely future recursive forecasts."""
    returns = np.diff(np.log(rows[-242:, 2]))
    x, y = returns[:-1], returns[1:]
    variance = float(np.mean((x-x.mean())**2))
    if not math.isfinite(variance) or variance <= 0:
        return None
    beta = float(np.mean((x-x.mean())*(y-y.mean()))/variance) if autoregressive else 0.
    intercept = float(y.mean()-beta*x.mean())
    value, forecast = float(returns[-1]), 0.
    for _ in range(6):
        value = intercept+beta*value
        forecast += value
    return forecast if math.isfinite(forecast) else None


class BtcResearchR12ArBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 242)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("AR1", "DRIFT")
        forecast = return_forecast(rows, self.MODE == "AR1")
        # Fixed signal hurdle inherited from R20, not simulated execution friction.
        if forecast is None or abs(forecast) <= .0019 or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        direction = 1 if forecast > 0 else -1
        atr = atr14(rows)
        if atr is None:
            return
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = direction

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        stop = entry-direction*plan["distance"]
        assert qty*(plan["distance"]+self.fee_rate*(entry+stop)) <= plan["risk_budget"]+1e-6
        self.stop_loss = qty, stop
        # Forecast horizon is24h; no fixed target clips the model's payoff.
        self.vars["entries"] = self.vars.get("entries", 0)+1
        self._observe("open")

    def update_position(self):
        if int(self.time) % BAR == 0 and int(self.time)-int(self.position.opened_at) >= 6*BAR:
            self.liquidate()
