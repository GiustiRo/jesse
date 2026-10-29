"""V: joint one-lag returns vs the frozen G scalar forecast; no ETH orders."""
import math
import numpy as np

from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m, return_forecast
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def joint_forecasts(btc, eth):
    """Return both forecasts or common cash; B rows=predictors, columns=responses."""
    assert btc.shape[0] == eth.shape[0] == 242
    assert np.array_equal(btc[:, 0], eth[:, 0])
    evidence = dict(reason="returns_invalid", rank=None)
    # Callers validate OHLC; finite checks also guard log/difference arithmetic.
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        returns = np.column_stack((np.diff(np.log(btc[:, 2])),
                                   np.diff(np.log(eth[:, 2]))))
    if not np.all(np.isfinite(returns)):
        return None, evidence
    x, y = returns[:-1], returns[1:]
    assert x.shape == y.shape == (240, 2)
    own = x[:, 0]
    variance = float(np.mean((own-own.mean())**2))
    if not math.isfinite(variance) or variance <= 0:
        evidence["reason"] = "ar_variance_invalid"
        return None, evidence
    xmean, ymean = np.mean(x, axis=0), np.mean(y, axis=0)
    centered_x, centered_y = x-xmean, y-ymean
    if not np.all(np.isfinite(centered_x)) or not np.all(np.isfinite(centered_y)):
        return None, evidence
    try:
        # NumPy default numerical rank is the sole rank rule; no condition cutoff.
        b, _, rank, _ = np.linalg.lstsq(centered_x, centered_y, rcond=None)
    except np.linalg.LinAlgError:
        evidence["reason"] = "lstsq_numerical_error"
        return None, evidence
    evidence["rank"] = int(rank)
    if rank != 2:
        evidence["reason"] = "var_rank_invalid"
        return None, evidence
    intercept = ymean-xmean@b
    if not np.all(np.isfinite(b)) or not np.all(np.isfinite(intercept)):
        evidence["reason"] = "coefficients_invalid"
        return None, evidence
    # Frozen scalar G helper remains authoritative; do not replace it by lstsq.
    ar_forecast = return_forecast(btc, True)
    if ar_forecast is None:
        evidence["reason"] = "ar_forecast_invalid"
        return None, evidence
    ar_beta = float(np.mean((own-own.mean())*(y[:, 0]-y[:, 0].mean()))/variance)
    ar_intercept = float(y[:, 0].mean()-ar_beta*own.mean())
    ar_state = float(returns[-1, 0])
    state, var_forecast = returns[-1].copy(), 0.
    with np.errstate(over="ignore", invalid="ignore"):
        for _ in range(6):
            # Row-vector convention: B[1,0] is ETH lag -> next BTC; A=B.T.
            state = intercept+state@b
            ar_state = ar_intercept+ar_beta*ar_state
            if not np.all(np.isfinite(state)) or not math.isfinite(ar_state):
                evidence["reason"] = "recursive_state_invalid"
                return None, evidence
            var_forecast += float(state[0])
            if not math.isfinite(var_forecast):
                evidence["reason"] = "var_forecast_invalid"
                return None, evidence
    if not math.isfinite(ar_forecast):
        evidence["reason"] = "ar_forecast_invalid"
        return None, evidence
    evidence.update(reason="valid", matrix_b=b.tolist(), intercept=intercept.tolist(),
                    ar_beta=ar_beta, ar_intercept=ar_intercept,
                    var_forecast=var_forecast, ar_forecast=float(ar_forecast))
    return dict(VAR=var_forecast, AR=float(ar_forecast)), evidence


class BtcResearchR22JointBase1m(BtcResearchR12ArBase1m):
    """Inherit G no-TP/24h fill management and the unchanged R11 M1 observer."""
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("VAR", "AR")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        btc = closed_window(self.get_candles(self.exchange, "BTC-USDT", "4h"), now, 242)
        eth = closed_window(self.get_candles(self.exchange, "ETH-USDT", "4h"), now, 242)
        if btc is None or eth is None or not np.array_equal(btc[:, 0], eth[:, 0]):
            forecasts, evidence = None, dict(reason="windows_invalid", rank=None)
        else:
            assert math.isclose(float(btc[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
            forecasts, evidence = joint_forecasts(btc, eth)
        counts = self.vars.setdefault("joint_counts", {})
        reason = evidence["reason"]
        counts[reason] = counts.get(reason, 0)+1
        if forecasts is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        forecast = forecasts[self.MODE]
        # Hurdle inherited from G is a signal rule, not an extra execution charge.
        if abs(forecast) <= .0019 or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(btc)
        if atr is None:
            return
        direction = 1 if forecast > 0 else -1
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            return
        self.vars["plan"] = dict(plan, joint_evidence=evidence)
        self.vars["direction"] = direction

    def on_open_position(self, order):
        super().on_open_position(order)
        self._log("R22_JOINT_OPEN", dict(time=int(self.time), mode=self.MODE,
                  evidence=self.vars["plan"]["joint_evidence"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R22_JOINT_STATS", dict(stage=stage, mode=self.MODE,
                  counts=self.vars.get("joint_counts", {}),
                  signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
                  occupied=self.vars.get("occupied", 0)))
