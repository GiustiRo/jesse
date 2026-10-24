"""AA: conditional price response to participation, not identified order flow."""
import math
import numpy as np

from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def interaction_inputs(rows):
    """Origins42..401/current407; every surprise owns42 strictly prior volumes."""
    if rows.ndim != 2 or rows.shape[0] != 408 or rows.shape[1] < 6:
        return None
    if (not np.all(np.isfinite(rows[:, :6])) or np.any(rows[:, 1:6] <= 0)
            or not np.all(np.diff(rows[:, 0]) == BAR)
            or np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2]))
            or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2]))):
        return None
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        close = np.log(rows[:, 2])
        volume = np.log(rows[:, 5])
        # Last sliding window includes V407 and has no following current volume:
        # discard it. Remaining366 windows end one bar BEFORE each origin42..407.
        prior = np.lib.stride_tricks.sliding_window_view(volume, 42)[:-1]
        r = np.diff(close)[41:]
        v = volume[42:]-np.mean(prior, axis=1)
        # RAW product is prescribed for interpretable coefficient conversion.
        # Products after affine centering can span the same model with main effects.
        raw = np.column_stack((r, v, r*v))
        labels = close[48:408]-close[42:402]
    if not np.all(np.isfinite(raw)) or not np.all(np.isfinite(labels)):
        return None
    return raw[:360], labels, raw[-1]


def interaction_fit(raw, labels, current):
    """Two nested OLS models share all360 rows, scalers and numerical admission."""
    if raw.shape != (360, 3) or labels.shape != (360,) or current.shape != (3,):
        return None, dict(reason="shape_invalid")
    if not all(np.all(np.isfinite(x)) for x in (raw, labels, current)):
        return None, dict(reason="arithmetic_invalid")
    # Exact constants can yield a tiny positive std after a rounded mean. Detect
    # equality first; no near-zero threshold or dropping a column for MAIN.
    if np.any(np.all(raw == raw[:1], axis=0)):
        return None, dict(reason="constant_column")
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        center = raw.mean(axis=0)
        scale = raw.std(axis=0, ddof=0)
        scaled = (raw-center)/scale
        point = (current-center)/scale
    if (not np.all(np.isfinite(center)) or not np.all(np.isfinite(scale))
            or np.any(scale <= 0) or not np.all(np.isfinite(scaled))
            or not np.all(np.isfinite(point))):
        return None, dict(reason="scale_invalid")
    full = np.column_stack((np.ones(360), scaled))
    main = full[:, :3]
    try:
        # None is NumPy's dtype/shape-dependent default numerical-rank cutoff,
        # frozen ex ante. Deficient rank rejects BOTH; no ridge or fallback.
        bf, _, rankf, sf = np.linalg.lstsq(full, labels, rcond=None)
        bm, _, rankm, sm = np.linalg.lstsq(main, labels, rcond=None)
    except np.linalg.LinAlgError:
        return None, dict(reason="solver_error")
    if rankf != 4 or rankm != 3:
        return None, dict(reason="rank_invalid", ranks=[int(rankf), int(rankm)])
    if not all(np.all(np.isfinite(x)) for x in (bf, bm, sf, sm)):
        return None, dict(reason="coefficient_invalid")
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        x = np.r_[1., point]
        ff = float(x @ bf)
        fm = float(x[:3] @ bm)
        g = float(bf[3]/scale[2])
    if not all(math.isfinite(x) for x in (ff, fm, g)):
        return None, dict(reason="forecast_or_g_invalid")
    evidence = dict(reason="valid", n=360, origins=[42, 401], current_index=407,
        target_indices=[48, 407], current_raw=current.tolist(),
        center=center.tolist(), scale=scale.tolist(),
        coefficients_full=bf.tolist(), coefficients_main=bm.tolist(),
        ranks=[int(rankf), int(rankm)], singular_full=sf.tolist(),
        singular_main=sm.tolist(), g_raw=g,
        forecast_full=ff, forecast_main=fm)
    return (ff, fm), evidence


def interaction_forecasts(rows):
    values = interaction_inputs(rows)
    if values is None:
        return None, dict(reason="data_invalid")
    return interaction_fit(*values)


def empty_interaction_diagnostic():
    return dict(last=None, n=0, g_negative=0, g_zero=0, g_positive=0,
        means={key: dict(available=True, value=None)
               for key in ("g_raw", "forecast_full", "forecast_main")},
        aggregation_errors=0, latest=None)


def interaction_diagnostic(state, now, evidence):
    """O(1), once per valid fit, independent of mode, hurdle, ATR and occupation."""
    if state["last"] is not None and now <= state["last"]:
        return state
    result = dict(state)
    result["last"], result["n"] = int(now), state["n"]+1
    g = evidence["g_raw"]
    key = "g_negative" if g < 0 else "g_positive" if g > 0 else "g_zero"
    result[key] += 1
    result["latest"] = {key: evidence[key]
                        for key in ("g_raw", "forecast_full", "forecast_main")}
    result["means"] = {}
    for key, old in state["means"].items():
        item = dict(old)
        if old["available"]:
            value = evidence[key]
            mean = value if state["n"] == 0 else old["value"]+(value-old["value"])/result["n"]
            if math.isfinite(mean):
                item["value"] = mean
            else:
                # An unavailable descriptive aggregate cannot affect any forecast
                # or the accepted fit. Do not serialize Infinity or invent a mean.
                item.update(available=False, value=None)
                result["aggregation_errors"] += 1
        result["means"][key] = item
    return result


class BtcResearchR27VolumeInteractionBase1m(BtcResearchR12ArBase1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("INTERACTION", "MAIN_EFFECTS")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        last = self.vars.get("interaction_last")
        if last is not None and now <= last:
            return
        self.vars["interaction_last"] = now
        if not self.START < now < self.FINISH:
            return
        counts = self.vars.setdefault("interaction_counts", {})
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 408)
        if rows is None:
            counts["window_invalid"] = counts.get("window_invalid", 0)+1
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        if not math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8):
            # As-of route mismatch is shared invalid data, before either model or
            # diagnostic. It is cash, not a framework invariant that halts a run.
            counts["price_alignment_invalid"] = counts.get("price_alignment_invalid", 0)+1
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        forecasts, evidence = interaction_forecasts(rows)
        reason = evidence["reason"]
        counts[reason] = counts.get(reason, 0)+1
        self.vars["interaction_latest_fit"] = evidence
        if forecasts is None:
            return
        evidence.update(origin=now, window_first=int(rows[0, 0]), window_last=int(rows[-1, 0]))
        # Record BOTH forecasts and raw gamma before all trading gates. MODE and
        # wallet/order state never enter any mathematical/diagnostic helper.
        diagnostic = self.vars.get("interaction_diagnostic", empty_interaction_diagnostic())
        self.vars["interaction_diagnostic"] = interaction_diagnostic(diagnostic, now, evidence)
        forecast = forecasts[0 if self.MODE == "INTERACTION" else 1]
        if abs(forecast) <= .0019:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(rows)
        if atr is None:
            counts["atr_invalid"] = counts.get("atr_invalid", 0)+1
            return
        direction = 1 if forecast > 0 else -1
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            counts["plan_invalid"] = counts.get("plan_invalid", 0)+1
            return
        self.vars["plan"] = dict(plan, interaction_evidence=evidence,
                                forecast=forecast, forecast_origin=now)
        self.vars["direction"] = direction

    def on_open_position(self, order):
        super().on_open_position(order)
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        self._log("R27_OPEN", dict(time=int(self.time), mode=self.MODE,
            forecast=plan["forecast"], forecast_origin=plan["forecast_origin"],
            forecast_deadline=plan["forecast_origin"]+6*BAR,
            opened_at=int(self.position.opened_at),
            hold_deadline=int(self.position.opened_at)+6*BAR,
            entry=float(self.position.entry_price), qty=abs(float(self.position.qty)),
            stop=float(self.position.entry_price)-direction*plan["distance"],
            distance=plan["distance"], risk_budget=plan["risk_budget"]))
        self._log("R27_OPEN_FIT", plan["interaction_evidence"])

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R27_COUNTS", dict(stage=stage, mode=self.MODE,
            counts=self.vars.get("interaction_counts", {}),
            signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
            occupied=self.vars.get("occupied", 0)))
        self._log("R27_DIAGNOSTIC", dict(stage=stage,
            **self.vars.get("interaction_diagnostic", empty_interaction_diagnostic())))
        self._log("R27_LAST_FIT", dict(stage=stage,
            **self.vars.get("interaction_latest_fit", {})))
