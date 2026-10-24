import math

import numpy as np
from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, DAY, closed_window, atr14, entry_plan


def season_model(candles, now):
    """Exactly90 complete UTC days; bin is interval START, not close hour."""
    if now % DAY:
        return None
    rows = closed_window(candles, now, 541)
    if rows is None or not np.all(rows[:, 0] % BAR == 0):
        return None
    labels = np.diff(np.log(rows[:, 2]))
    phases = ((rows[1:, 0].astype(np.int64) % DAY) // BAR)
    counts = [int(np.sum(phases == k)) for k in range(6)]
    if counts != [90] * 6 or not np.all(np.isfinite(labels)):
        return None
    means = [float(np.mean(labels[phases == k])) for k in range(6)]
    global_mean = float(np.mean(labels))
    if not all(math.isfinite(v) for v in means + [global_mean]):
        return None
    return dict(day=int(now), phase_means=means, global_mean=global_mean,
                counts=counts, labels=540,
                first_origin=int(rows[1, 0]), last_target=int(rows[-1, 0]) + BAR)


def season_forecast(model, now, phase_policy):
    """A valid midnight snapshot is immutable for its own UTC day only."""
    if model is None or not model["day"] <= now < model["day"] + DAY:
        return None
    if now % BAR:
        return None
    k = int((now % DAY) // BAR)
    value = model["phase_means"][k] if phase_policy else model["global_mean"]
    return float(value) if math.isfinite(value) else None


class BtcResearchR20SeasonBase1m(BtcResearchR12ArBase1m):
    """Phase-conditioned mean versus global mean; R11 M1 accounting intact."""
    MODE = "abstract"

    def _season_invalidate(self, reason):
        self.vars["season_model"] = None
        if self.START <= int(self.time) < self.FINISH:
            counts = self.vars.setdefault("season_invalidations", {})
            counts[reason] = counts.get(reason, 0) + 1

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate - .00045) < 1e-12
            assert abs(self.balance - 10000) < 1e-6
            assert self.MODE in ("PHASE", "GLOBAL")
            self.vars["checked"] = True
            self._log("R20_SEASON_CONFIG", dict(mode=self.MODE, labels=540,
                      days=90, bins=6, per_bin=90, freeze="00UTC",
                      horizon_hours=4, stop_atr=2, target=None,
                      risk=.02, aggregate=.06, leverage=3, fee=.00045))
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR or not self.START <= now < self.FINISH:
            return
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        rows = closed_window(candles, now, 15)
        if rows is None or not np.all(rows[:, 0] % BAR == 0):
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            self._season_invalidate("decision_ohlc")
            return
        if not math.isclose(float(rows[-1, 2]), float(self.price),
                            rel_tol=1e-10, abs_tol=1e-8):
            self._season_invalidate("asof_price")
            return
        if now % DAY == 0:
            model = season_model(candles, now)
            if model is None:
                self._season_invalidate("midnight_window")
            else:
                self.vars["season_model"] = model
                self.vars["season_freezes"] = self.vars.get("season_freezes", 0) + 1
        model = self.vars.get("season_model")
        forecast = season_forecast(model, now, self.MODE == "PHASE")
        atr = atr14(rows)
        if atr is None:
            self._season_invalidate("atr")
            return
        if forecast is None or abs(forecast) <= .0019 or not self.START < now:
            return
        self.vars["signals"] = self.vars.get("signals", 0) + 1
        # Occupied margin is irrelevant to model validity; discard, never queue.
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0) + 1
            return
        price = float(self.price)
        capital = max(0., float(self.balance))
        margin, leverage, fee = (float(self.available_margin),
                                 float(self.leverage), float(self.fee_rate))
        # Both directions share ex-ante admissibility at the SAME flat account.
        # No fictitious profit target or additional physical buffer is imposed.
        plans = {side: entry_plan(price, capital, margin, leverage, fee, side, 2*atr)
                 for side in (1, -1)}
        if any(p is None or not math.isfinite(p["qty"]) or p["qty"] <= 0
               for p in plans.values()):
            self.vars["season_plan_rejections"] = self.vars.get("season_plan_rejections", 0) + 1
            return
        if plans[1]["stop"] <= 0:
            return
        direction = 1 if forecast > 0 else -1
        self.vars["direction"] = direction
        self.vars["plan"] = plans[direction]
        self.vars["season_evidence"] = dict(
            freeze=model["day"], phase=int((now % DAY)//BAR),
            forecast=forecast, global_mean=model["global_mean"],
            phase_means=list(model["phase_means"]), counts=list(model["counts"]),
            first_origin=model["first_origin"], last_target=model["last_target"])

    def on_open_position(self, order):
        super().on_open_position(order)
        self._log("R20_SEASON_OPEN", dict(time=int(self.time),
                  direction=1 if self.is_long else -1,
                  entry=float(self.position.entry_price),
                  evidence=self.vars["season_evidence"]))

    def update_position(self):
        # Parent AR holds6BAR. T's preregistered forecast/timeout are BOTH1BAR;
        # protective stop remains M1 and no other exit rule is changed.
        if int(self.time) % BAR == 0 and int(self.time)-int(self.position.opened_at) >= BAR:
            self.liquidate()

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R20_SEASON_STATS", dict(stage=stage,
                  freezes=self.vars.get("season_freezes", 0),
                  invalidations=self.vars.get("season_invalidations", {}),
                  occupied=self.vars.get("occupied", 0),
                  plan_rejections=self.vars.get("season_plan_rejections", 0)))
