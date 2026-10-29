import math
import numpy as np

from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan

# Fixed before economic results: two natural half-range bins, sixty days of
# mature origins, one-day label and a shared minimum count for either policy.
LOOKBACK = 367
TRAINING_ORIGINS = 360
LABEL_BARS = 6
MIN_BIN_COUNT = 30
ADVANCE_BOUNDARY = 0.5
FORECAST_HURDLE = 0.0019  # Admission threshold; never additional modeled friction.


def geometry_forecast(rows, conditional):
    """Estimate only outcomes whose complete six-bar horizon is already observed."""
    if len(rows) < LOOKBACK:
        return None
    window = rows[-LOOKBACK:]
    close = window[:, 2]
    origins = window[1:TRAINING_ORIGINS+1]
    previous = close[:TRAINING_ORIGINS]
    step = close[1:TRAINING_ORIGINS+1]-previous
    true_range = np.maximum(
        origins[:, 3]-origins[:, 4],
        np.maximum(abs(origins[:, 3]-previous), abs(origins[:, 4]-previous)),
    )
    valid = (true_range > 0) & (step != 0)
    advance = np.divide(abs(step), true_range, out=np.zeros_like(step), where=true_range > 0)
    bins = advance >= ADVANCE_BOUNDARY
    # Origins1..360 label at7..366. Log differences avoid overflow of ratios.
    labels = np.sign(step)*(np.log(close[1+LABEL_BARS:])-np.log(close[1:TRAINING_ORIGINS+1]))
    valid &= np.isfinite(labels)

    current_step = float(close[-1]-close[-2])
    current_range = max(float(window[-1, 3]-window[-1, 4]),
                        abs(float(window[-1, 3]-close[-2])),
                        abs(float(window[-1, 4]-close[-2])))
    if current_range <= 0 or current_step == 0:
        return None
    current_advance = abs(current_step)/current_range
    current_bin = bool(current_advance >= ADVANCE_BOUNDARY)
    group = valid & (bins == current_bin)
    count_bin, count_all = int(group.sum()), int(valid.sum())
    # GLOBAL shares this gate, so the treatment cannot gain by a different
    # minimum-history calendar rather than by its conditional mean.
    if count_bin < MIN_BIN_COUNT:
        return None
    mean_conditional = float(np.mean(labels[group]))
    mean_global = float(np.mean(labels[valid]))
    mean = mean_conditional if conditional else mean_global
    if not math.isfinite(mean):
        return None
    response = 1 if mean > FORECAST_HURDLE else -1 if mean < -FORECAST_HURDLE else 0
    current_sign = 1 if current_step > 0 else -1
    return dict(direction=current_sign*response, response=response, mean=mean,
                mean_conditional=mean_conditional, mean_global=mean_global,
                current_bin=int(current_bin), current_advance=current_advance,
                count_bin=count_bin, count_all=count_all,
                first_origin_close=int(window[1, 0])+BAR,
                last_origin_close=int(window[TRAINING_ORIGINS, 0])+BAR,
                latest_label_close=int(window[-1, 0])+BAR)


class BtcResearchR13GeometryBase1m(BtcResearchR12ArBase1m):
    """Online two-mean estimator; frozen parent supplies no-TP/24h execution."""
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
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, LOOKBACK)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("COND", "GLOBAL")
        forecast = geometry_forecast(rows, self.MODE == "COND")
        self.vars["forecasts"] = self.vars.get("forecasts", 0)+1
        if forecast is None:
            self.vars["insufficient_forecasts"] = self.vars.get("insufficient_forecasts", 0)+1
            return
        assert forecast["latest_label_close"] == now
        if not forecast["direction"] or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(rows)
        if atr is None:
            return
        direction = forecast["direction"]
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            return
        self.vars["plan"] = plan
        self.vars["admitted_forecast"] = forecast
        self.vars["direction"] = direction
        self._log("R13_GEOMETRY_ADMISSION", dict(time=now, mode=self.MODE, **forecast))

    def on_open_position(self, order):
        super().on_open_position(order)
        # Count actual fills, not forecasts blocked by an existing position.
        forecast = self.vars["admitted_forecast"]
        key = "follow_fills" if forecast["response"] == 1 else "fade_fills"
        self.vars[key] = self.vars.get(key, 0)+1

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R13_GEOMETRY_STATS", dict(
            stage=stage, mode=self.MODE,
            forecasts=self.vars.get("forecasts", 0),
            insufficient_forecasts=self.vars.get("insufficient_forecasts", 0),
            follow_fills=self.vars.get("follow_fills", 0),
            fade_fills=self.vars.get("fade_fills", 0)))
