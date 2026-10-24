import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def relative_beta(btc, eth):
    """240 paired returns from241 prior closes; current closes never fit beta."""
    own = np.diff(np.log(btc[-242:-1, 2]))
    external = np.diff(np.log(eth[-242:-1, 2]))
    assert len(own) == len(external) == 240
    xc, yc = external-np.mean(external), own-np.mean(own)
    denominator = float(np.dot(xc, xc))
    variance = denominator/(len(external)-1)
    if not math.isfinite(variance) or variance <= 0:
        return None
    beta = float(np.dot(xc, yc)/denominator)
    return beta if math.isfinite(beta) else None


def relative_level_state(btc, eth, fitted_beta, residual):
    """Use one current refit for all60 reference levels and the current level."""
    model_beta = fitted_beta if residual else 0.0
    levels = np.log(btc[-61:, 2])-model_beta*np.log(eth[-61:, 2])
    reference = levels[:-1]
    assert len(reference) == 60
    mean = float(np.mean(reference))
    sigma = float(np.std(reference, ddof=1))
    evidence = dict(fitted_beta=fitted_beta, model_beta=model_beta,
                    mean=mean, sigma=sigma, z=None, beta_returns=240, reference_levels=60)
    if not math.isfinite(mean) or not math.isfinite(sigma) or sigma <= 0:
        # Degenerate levels are neutral, with no epsilon/winsorization rescue.
        evidence["mean"] = mean if math.isfinite(mean) else None
        evidence["sigma"] = sigma if math.isfinite(sigma) else None
        return 0, evidence
    z = float((levels[-1]-mean)/sigma)
    if not math.isfinite(z):
        return 0, evidence
    evidence["z"] = z
    state = 1 if z <= -2 else -1 if z >= 2 else 0
    return state, evidence


class BtcResearchR17RelativeBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("RESIDUAL", "PRICE")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        btc = closed_window(self.get_candles(self.exchange, "BTC-USDT", "4h"), now, 242)
        eth = closed_window(self.get_candles(self.exchange, "ETH-USDT", "4h"), now, 242)
        if btc is None or eth is None or not np.array_equal(btc[:, 0], eth[:, 0]):
            self.vars["relative_state"] = 0
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(btc[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        # ETH validity and finite positive variance are shared by the PRICE arm.
        beta = relative_beta(btc, eth)
        if beta is None:
            self.vars["relative_state"] = 0
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        state, evidence = relative_level_state(btc, eth, beta, self.MODE == "RESIDUAL")
        previous = self.vars.get("relative_state", 0)
        self.vars["relative_state"] = state
        # Refit-induced transitions are intentionally part of this definition.
        direction = state if state and state != previous else 0
        if not direction or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(btc)
        if atr is None:
            return
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None or self.price+direction*2*plan["distance"] <= 0:
            return
        self.vars["plan"] = dict(plan, relative=dict(evidence))
        self.vars["direction"] = direction

    def on_open_position(self, order):
        # Reuse the unchanged R11 fee-risk assertion, actual-fill SL/TP and count.
        super().on_open_position(order)
        side = 1 if self.is_long else -1
        key = "long_fills" if side == 1 else "short_fills"
        self.vars[key] = self.vars.get(key, 0)+1
        self._log("R17_RELATIVE_OPEN", dict(time=int(self.time), mode=self.MODE,
            direction=side, evidence=self.vars["plan"]["relative"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R17_RELATIVE_STATS", dict(stage=stage, mode=self.MODE,
            long_fills=self.vars.get("long_fills", 0),
            short_fills=self.vars.get("short_fills", 0),
            signals=self.vars.get("signals", 0), occupied=self.vars.get("occupied", 0)))
