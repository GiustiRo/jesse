# Y — fuentes implementadas y versiones técnicas preservadas

Fecha2026-10-21. Root autorizó implementación/checks tras leer protocolo y CODES antecedentes completos. Estado: check completo passed, pendiente revisión final de recibos antes de drafts/economía. Padres congelados. La fuente final es la única a usar; versiones previas son trazabilidad, nunca alternativas económicas.

## Base v1_before_reviews
SHA256 33d07c126221904118a4d564893e9140bfdec3b6312959b41513637d38f873f1; estado superseded_before_any_analysis.
Motivo: asof route price was checked only after TRAIN392, so a shorter valid window could wrongly mature/capture diagnostic observations.

```python
"""Y: temporal orientation of BTC volume/amplitude association, not order flow."""
import math
import numpy as np

from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def cell_key(values):
    return "/".join(str(int(v)) for v in values)


def all_cells():
    return {cell_key((s, q, d)): 0
            for s in (-1, 1) for q in (-1, 1) for d in (-1, 1)}


def volume_lag_features(rows):
    """One feature per endpoint from index25; each owns its25 paired samples."""
    assert rows.ndim == 2 and rows.shape[1] >= 6 and len(rows) >= 26
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        returns = np.diff(np.log(rows[:, 2]))
        magnitude = np.lib.stride_tricks.sliding_window_view(np.abs(returns), 25)
        log_volume = np.lib.stride_tricks.sliding_window_view(np.log(rows[1:, 5]), 25)
        # Same25 centers/scales in BOTH lag directions, independently per row.
        amean, vmean = magnitude.mean(axis=1), log_volume.mean(axis=1)
        asd, vsd = magnitude.std(axis=1, ddof=0), log_volume.std(axis=1, ddof=0)
        a = (magnitude-amean[:, None])/asd[:, None]
        v = (log_volume-vmean[:, None])/vsd[:, None]
        forward = np.mean(v[:, :-1]*a[:, 1:], axis=1)
        reverse = np.mean(a[:, :-1]*v[:, 1:], axis=1)
        symmetric, orientation = forward+reverse, forward-reverse
    raw = np.column_stack((returns[24:], symmetric, orientation))
    signs = np.where(np.isfinite(raw), np.sign(raw), 0).astype(np.int8)
    valid = (np.all(np.isfinite(magnitude), axis=1)
             & np.all(np.isfinite(log_volume), axis=1)
             & np.isfinite(asd) & (asd > 0)
             & np.isfinite(vsd) & (vsd > 0)
             & np.all(np.isfinite(raw), axis=1)
             & np.all(signs != 0, axis=1))
    # log of nonpositive volume is already nonfinite; no pseudocount/epsilon.
    return dict(valid=valid, signs=signs, forward=forward, reverse=reverse,
                symmetric=symmetric, orientation=orientation)


def current_volume_feature(rows):
    features = volume_lag_features(rows)
    assert len(rows) == 26 and len(features["valid"]) == 1
    if not features["valid"][0]:
        return None
    return dict(state=tuple(int(x) for x in features["signs"][0]),
                forward=float(features["forward"][0]), reverse=float(features["reverse"][0]),
                symmetric=float(features["symmetric"][0]),
                orientation=float(features["orientation"][0]))


def volume_lag_forecasts(rows):
    """Exactly360 slots, ages6..365; row0 padding is deliberately unused."""
    assert len(rows) == 392
    features = volume_lag_features(rows)
    # Feature index0 ends at row25; endpoints26..385 are indices1..360.
    states = features["signs"][1:361]
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        labels = np.log(rows[32:392, 2])-np.log(rows[26:386, 2])
    valid = features["valid"][1:361] & np.isfinite(labels)
    assert len(states) == len(labels) == len(valid) == 360
    support = all_cells()
    for values in support:
        key = tuple(int(x) for x in values.split("/"))
        support[values] = int(np.sum(valid & np.all(states == key, axis=1)))
    evidence = dict(reason="current_feature_invalid", slots=360,
                    valid_origins=int(np.sum(valid)), support=support,
                    n_state=0, n_control=0)
    if not features["valid"][-1]:
        return None, evidence
    current = features["signs"][-1]
    selected = valid & np.all(states == current, axis=1)
    # Both policies start with the SAME all-three-signs/nonzero mask.
    control = valid & np.all(states[:, :2] == current[:2], axis=1)
    n_state, n_control = int(np.sum(selected)), int(np.sum(control))
    evidence.update(n_state=n_state, n_control=n_control,
                    current_state=[int(x) for x in current])
    if n_state < 20:
        evidence["reason"] = "insufficient_cell"
        return None, evidence
    state_mean, control_mean = float(np.mean(labels[selected])), float(np.mean(labels[control]))
    if not math.isfinite(state_mean) or not math.isfinite(control_mean):
        evidence["reason"] = "mean_invalid"
        return None, evidence
    evidence.update(reason="valid", state_mean=state_mean, control_mean=control_mean,
                    bank_first=int(rows[26, 0])+BAR, bank_last=int(rows[385, 0])+BAR,
                    last_target=int(rows[391, 0])+BAR)
    return dict(STATE=state_mean, SYMMETRIC=control_mean), evidence


def empty_diagnostic():
    return dict(last=None, pending=[], registered=0, matured=0,
                censored_gap=0, censored_terminal=0, terminal=False,
                cells={key: dict(n=0, sum_y=0., sum_sy=0.) for key in all_cells()})


def diagnostic_step(state, now, bar, feature):
    """Math-only ledger: mature six actual OHLC bars before any training gate."""
    if state["last"] is not None and now <= state["last"]:
        return state
    assert not state["terminal"]
    result = dict(state, pending=[], cells={k: dict(v) for k, v in state["cells"].items()})
    pending = state["pending"]
    gap = state["last"] is not None and now != state["last"]+BAR
    if gap or bar is None:
        result["censored_gap"] += len(pending)
        pending = []
    if bar is not None:
        assert int(bar[0])+BAR == now
        for item in pending:
            observed = dict(item, steps=item["steps"]+1)
            assert observed["steps"] <= 6
            if observed["steps"] == 6:
                assert now == observed["deadline"]
                label = math.log(float(bar[2]))-math.log(observed["price"])
                assert math.isfinite(label)
                cell = result["cells"][cell_key(observed["state"])]
                cell["n"] += 1
                cell["sum_y"] += label
                cell["sum_sy"] += observed["state"][0]*label
                result["matured"] += 1
            else:
                assert now < observed["deadline"]
                result["pending"].append(observed)
        if feature is not None:
            result["pending"].append(dict(origin=now, price=float(bar[2]),
                state=feature["state"], deadline=now+6*BAR, steps=0))
            result["registered"] += 1
    else:
        assert feature is None
    result["last"] = now
    assert len(result["pending"]) <= 6
    return result


def diagnostic_finish(state):
    """PRETERMINAL/FINAL may repeat: censor each remaining origin only once."""
    if state["terminal"]:
        return state
    return dict(state, pending=[], terminal=True,
                censored_terminal=state["censored_terminal"]+len(state["pending"]))


class BtcResearchR25VolumeLagBase1m(BtcResearchR12ArBase1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("STATE", "SYMMETRIC")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        diagnostic = self.vars.get("volume_diagnostic", empty_diagnostic())
        # Do not rewind/censor/recount on duplicate or earlier callbacks.
        if diagnostic["last"] is not None and now <= diagnostic["last"]:
            return
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        current_bar = closed_window(candles, now, 1)
        feature_rows = closed_window(candles, now, 26)
        feature = current_volume_feature(feature_rows) if feature_rows is not None else None
        capture = feature if self.START < now < self.FINISH else None
        self.vars["volume_diagnostic"] = diagnostic_step(
            diagnostic, now, None if current_bar is None else current_bar[-1], capture)
        counts = self.vars.setdefault("volume_lag_counts", {})
        for reason in ("feature_valid" if feature is not None else "feature_invalid",):
            counts[reason] = counts.get(reason, 0)+1
        # Diagnostic above must not depend on this longer historical window.
        rows = closed_window(candles, now, 392)
        if rows is None:
            counts["train_window_invalid"] = counts.get("train_window_invalid", 0)+1
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        forecasts, evidence = volume_lag_forecasts(rows)
        self.vars["volume_train_last"] = evidence
        reason = evidence["reason"]
        counts[reason] = counts.get(reason, 0)+1
        if forecasts is None:
            return
        forecast = forecasts[self.MODE]
        if abs(forecast) <= .0019 or not self.START < now < self.FINISH:
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
        assert feature is not None
        self.vars["plan"] = dict(plan, volume_evidence=evidence, volume_feature=feature,
                                forecast=forecast, forecast_origin=now)
        self.vars["direction"] = direction

    def on_open_position(self, order):
        super().on_open_position(order)
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        self._log("R25_VOLUME_OPEN", dict(time=int(self.time), mode=self.MODE,
            forecast=plan["forecast"], forecast_origin=plan["forecast_origin"],
            forecast_deadline=plan["forecast_origin"]+6*BAR,
            opened_at=int(self.position.opened_at),
            hold_deadline=int(self.position.opened_at)+6*BAR,
            stop=float(self.position.entry_price)-direction*plan["distance"],
            distance=plan["distance"], risk_budget=plan["risk_budget"],
            feature=plan["volume_feature"], evidence=plan["volume_evidence"]))

    def _emit(self, stage):
        diagnostic = self.vars.get("volume_diagnostic", empty_diagnostic())
        if stage in ("PRETERMINAL", "FINAL"):
            diagnostic = diagnostic_finish(diagnostic)
            self.vars["volume_diagnostic"] = diagnostic
        super()._emit(stage)
        self._log("R25_TRAIN_STATS", dict(stage=stage, mode=self.MODE,
            counts=self.vars.get("volume_lag_counts", {}),
            last=self.vars.get("volume_train_last", {}),
            signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
            occupied=self.vars.get("occupied", 0)))
        self._log("R25_DIAG_STATS", dict(stage=stage, last=diagnostic["last"],
            registered=diagnostic["registered"], matured=diagnostic["matured"],
            censored_gap=diagnostic["censored_gap"],
            censored_terminal=diagnostic["censored_terminal"],
            pending=len(diagnostic["pending"]), terminal=diagnostic["terminal"]))
        # Bounded one-cell rows avoid truncating one large journal line.
        for key, values in diagnostic["cells"].items():
            self._log("R25_DIAG_CELL", dict(stage=stage, cell=key, **values))

```

## Base v2_after_asof_fix
SHA256 8113b462c3ff1a3a978f07707d3abb27b78f2d4bbbb0f39c0f0313591e1e83c5; estado superseded_after_numeric_probe.
Motivo: exact constant logV can acquire tiny nonzero std from mean rounding; V=2 yielded a spurious valid feature.

```python
"""Y: temporal orientation of BTC volume/amplitude association, not order flow."""
import math
import numpy as np

from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def cell_key(values):
    return "/".join(str(int(v)) for v in values)


def all_cells():
    return {cell_key((s, q, d)): 0
            for s in (-1, 1) for q in (-1, 1) for d in (-1, 1)}


def volume_lag_features(rows):
    """One feature per endpoint from index25; each owns its25 paired samples."""
    assert rows.ndim == 2 and rows.shape[1] >= 6 and len(rows) >= 26
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        returns = np.diff(np.log(rows[:, 2]))
        magnitude = np.lib.stride_tricks.sliding_window_view(np.abs(returns), 25)
        log_volume = np.lib.stride_tricks.sliding_window_view(np.log(rows[1:, 5]), 25)
        # Same25 centers/scales in BOTH lag directions, independently per row.
        amean, vmean = magnitude.mean(axis=1), log_volume.mean(axis=1)
        asd, vsd = magnitude.std(axis=1, ddof=0), log_volume.std(axis=1, ddof=0)
        a = (magnitude-amean[:, None])/asd[:, None]
        v = (log_volume-vmean[:, None])/vsd[:, None]
        forward = np.mean(v[:, :-1]*a[:, 1:], axis=1)
        reverse = np.mean(a[:, :-1]*v[:, 1:], axis=1)
        symmetric, orientation = forward+reverse, forward-reverse
    raw = np.column_stack((returns[24:], symmetric, orientation))
    signs = np.where(np.isfinite(raw), np.sign(raw), 0).astype(np.int8)
    valid = (np.all(np.isfinite(magnitude), axis=1)
             & np.all(np.isfinite(log_volume), axis=1)
             & np.isfinite(asd) & (asd > 0)
             & np.isfinite(vsd) & (vsd > 0)
             & np.all(np.isfinite(raw), axis=1)
             & np.all(signs != 0, axis=1))
    # log of nonpositive volume is already nonfinite; no pseudocount/epsilon.
    return dict(valid=valid, signs=signs, forward=forward, reverse=reverse,
                symmetric=symmetric, orientation=orientation)


def current_volume_feature(rows):
    features = volume_lag_features(rows)
    assert len(rows) == 26 and len(features["valid"]) == 1
    if not features["valid"][0]:
        return None
    return dict(state=tuple(int(x) for x in features["signs"][0]),
                forward=float(features["forward"][0]), reverse=float(features["reverse"][0]),
                symmetric=float(features["symmetric"][0]),
                orientation=float(features["orientation"][0]))


def volume_lag_forecasts(rows):
    """Exactly360 slots, ages6..365; row0 padding is deliberately unused."""
    assert len(rows) == 392
    features = volume_lag_features(rows)
    # Feature index0 ends at row25; endpoints26..385 are indices1..360.
    states = features["signs"][1:361]
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        labels = np.log(rows[32:392, 2])-np.log(rows[26:386, 2])
    valid = features["valid"][1:361] & np.isfinite(labels)
    assert len(states) == len(labels) == len(valid) == 360
    support = all_cells()
    for values in support:
        key = tuple(int(x) for x in values.split("/"))
        support[values] = int(np.sum(valid & np.all(states == key, axis=1)))
    evidence = dict(reason="current_feature_invalid", slots=360,
                    valid_origins=int(np.sum(valid)), support=support,
                    n_state=0, n_control=0)
    if not features["valid"][-1]:
        return None, evidence
    current = features["signs"][-1]
    selected = valid & np.all(states == current, axis=1)
    # Both policies start with the SAME all-three-signs/nonzero mask.
    control = valid & np.all(states[:, :2] == current[:2], axis=1)
    n_state, n_control = int(np.sum(selected)), int(np.sum(control))
    evidence.update(n_state=n_state, n_control=n_control,
                    current_state=[int(x) for x in current])
    if n_state < 20:
        evidence["reason"] = "insufficient_cell"
        return None, evidence
    state_mean, control_mean = float(np.mean(labels[selected])), float(np.mean(labels[control]))
    if not math.isfinite(state_mean) or not math.isfinite(control_mean):
        evidence["reason"] = "mean_invalid"
        return None, evidence
    evidence.update(reason="valid", state_mean=state_mean, control_mean=control_mean,
                    bank_first=int(rows[26, 0])+BAR, bank_last=int(rows[385, 0])+BAR,
                    last_target=int(rows[391, 0])+BAR)
    return dict(STATE=state_mean, SYMMETRIC=control_mean), evidence


def empty_diagnostic():
    return dict(last=None, pending=[], registered=0, matured=0,
                censored_gap=0, censored_terminal=0, terminal=False,
                cells={key: dict(n=0, sum_y=0., sum_sy=0.) for key in all_cells()})


def diagnostic_step(state, now, bar, feature):
    """Math-only ledger: mature six actual OHLC bars before any training gate."""
    if state["last"] is not None and now <= state["last"]:
        return state
    assert not state["terminal"]
    result = dict(state, pending=[], cells={k: dict(v) for k, v in state["cells"].items()})
    pending = state["pending"]
    gap = state["last"] is not None and now != state["last"]+BAR
    if gap or bar is None:
        result["censored_gap"] += len(pending)
        pending = []
    if bar is not None:
        assert int(bar[0])+BAR == now
        for item in pending:
            observed = dict(item, steps=item["steps"]+1)
            assert observed["steps"] <= 6
            if observed["steps"] == 6:
                assert now == observed["deadline"]
                label = math.log(float(bar[2]))-math.log(observed["price"])
                assert math.isfinite(label)
                cell = result["cells"][cell_key(observed["state"])]
                cell["n"] += 1
                cell["sum_y"] += label
                cell["sum_sy"] += observed["state"][0]*label
                result["matured"] += 1
            else:
                assert now < observed["deadline"]
                result["pending"].append(observed)
        if feature is not None:
            result["pending"].append(dict(origin=now, price=float(bar[2]),
                state=feature["state"], deadline=now+6*BAR, steps=0))
            result["registered"] += 1
    else:
        assert feature is None
    result["last"] = now
    assert len(result["pending"]) <= 6
    return result


def diagnostic_finish(state):
    """PRETERMINAL/FINAL may repeat: censor each remaining origin only once."""
    if state["terminal"]:
        return state
    return dict(state, pending=[], terminal=True,
                censored_terminal=state["censored_terminal"]+len(state["pending"]))


class BtcResearchR25VolumeLagBase1m(BtcResearchR12ArBase1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("STATE", "SYMMETRIC")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        diagnostic = self.vars.get("volume_diagnostic", empty_diagnostic())
        # Do not rewind/censor/recount on duplicate or earlier callbacks.
        if diagnostic["last"] is not None and now <= diagnostic["last"]:
            return
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        counts = self.vars.setdefault("volume_lag_counts", {})
        current_bar = closed_window(candles, now, 1)
        mismatch = current_bar is not None and not math.isclose(
            float(current_bar[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        # Route/as-of parity is integrity for diagnostic labels too, even when
        # the longer training history is unavailable. Never record stale prices.
        if mismatch:
            current_bar = None
            counts["price_alignment_invalid"] = counts.get("price_alignment_invalid", 0)+1
        feature_rows = None if mismatch else closed_window(candles, now, 26)
        feature = current_volume_feature(feature_rows) if feature_rows is not None else None
        capture = feature if self.START < now < self.FINISH else None
        self.vars["volume_diagnostic"] = diagnostic_step(
            diagnostic, now, None if current_bar is None else current_bar[-1], capture)
        for reason in ("feature_valid" if feature is not None else "feature_invalid",):
            counts[reason] = counts.get(reason, 0)+1
        if mismatch:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        # Diagnostic above must not depend on this longer historical window.
        rows = closed_window(candles, now, 392)
        if rows is None:
            counts["train_window_invalid"] = counts.get("train_window_invalid", 0)+1
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        forecasts, evidence = volume_lag_forecasts(rows)
        self.vars["volume_train_last"] = evidence
        reason = evidence["reason"]
        counts[reason] = counts.get(reason, 0)+1
        if forecasts is None:
            return
        forecast = forecasts[self.MODE]
        if abs(forecast) <= .0019 or not self.START < now < self.FINISH:
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
        assert feature is not None
        self.vars["plan"] = dict(plan, volume_evidence=evidence, volume_feature=feature,
                                forecast=forecast, forecast_origin=now)
        self.vars["direction"] = direction

    def on_open_position(self, order):
        super().on_open_position(order)
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        self._log("R25_VOLUME_OPEN", dict(time=int(self.time), mode=self.MODE,
            forecast=plan["forecast"], forecast_origin=plan["forecast_origin"],
            forecast_deadline=plan["forecast_origin"]+6*BAR,
            opened_at=int(self.position.opened_at),
            hold_deadline=int(self.position.opened_at)+6*BAR,
            stop=float(self.position.entry_price)-direction*plan["distance"],
            distance=plan["distance"], risk_budget=plan["risk_budget"],
            feature=plan["volume_feature"], evidence=plan["volume_evidence"]))

    def _emit(self, stage):
        diagnostic = self.vars.get("volume_diagnostic", empty_diagnostic())
        if stage in ("PRETERMINAL", "FINAL"):
            diagnostic = diagnostic_finish(diagnostic)
            self.vars["volume_diagnostic"] = diagnostic
        super()._emit(stage)
        self._log("R25_TRAIN_STATS", dict(stage=stage, mode=self.MODE,
            counts=self.vars.get("volume_lag_counts", {}),
            last=self.vars.get("volume_train_last", {}),
            signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
            occupied=self.vars.get("occupied", 0)))
        self._log("R25_DIAG_STATS", dict(stage=stage, last=diagnostic["last"],
            registered=diagnostic["registered"], matured=diagnostic["matured"],
            censored_gap=diagnostic["censored_gap"],
            censored_terminal=diagnostic["censored_terminal"],
            pending=len(diagnostic["pending"]), terminal=diagnostic["terminal"]))
        # Bounded one-cell rows avoid truncating one large journal line.
        for key, values in diagnostic["cells"].items():
            self._log("R25_DIAG_CELL", dict(stage=stage, cell=key, **values))

```

## Base final_exact_degeneracy_guard
SHA256 437833f8ab078a24843b0ce326a4cd556bae8cdcb755be420febe648165251b7; estado final_full_check_passed.
Motivo: asof checked before diagnostics/training; exact equal25 logV/magnitude rejected without epsilon or band.

```python
"""Y: temporal orientation of BTC volume/amplitude association, not order flow."""
import math
import numpy as np

from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def cell_key(values):
    return "/".join(str(int(v)) for v in values)


def all_cells():
    return {cell_key((s, q, d)): 0
            for s in (-1, 1) for q in (-1, 1) for d in (-1, 1)}


def volume_lag_features(rows):
    """One feature per endpoint from index25; each owns its25 paired samples."""
    assert rows.ndim == 2 and rows.shape[1] >= 6 and len(rows) >= 26
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        returns = np.diff(np.log(rows[:, 2]))
        magnitude = np.lib.stride_tricks.sliding_window_view(np.abs(returns), 25)
        log_volume = np.lib.stride_tricks.sliding_window_view(np.log(rows[1:, 5]), 25)
        # Same25 centers/scales in BOTH lag directions, independently per row.
        amean, vmean = magnitude.mean(axis=1), log_volume.mean(axis=1)
        asd, vsd = magnitude.std(axis=1, ddof=0), log_volume.std(axis=1, ddof=0)
        a = (magnitude-amean[:, None])/asd[:, None]
        v = (log_volume-vmean[:, None])/vsd[:, None]
        forward = np.mean(v[:, :-1]*a[:, 1:], axis=1)
        reverse = np.mean(a[:, :-1]*v[:, 1:], axis=1)
        symmetric, orientation = forward+reverse, forward-reverse
    raw = np.column_stack((returns[24:], symmetric, orientation))
    signs = np.where(np.isfinite(raw), np.sign(raw), 0).astype(np.int8)
    valid = (np.all(np.isfinite(magnitude), axis=1)
             & np.all(np.isfinite(log_volume), axis=1)
             # An exactly constant array can acquire a tiny std from mean
             # rounding (e.g. log(2)); reject mathematical degeneracy exactly.
             & ~np.all(magnitude == magnitude[:, :1], axis=1)
             & ~np.all(log_volume == log_volume[:, :1], axis=1)
             & np.isfinite(asd) & (asd > 0)
             & np.isfinite(vsd) & (vsd > 0)
             & np.all(np.isfinite(raw), axis=1)
             & np.all(signs != 0, axis=1))
    # log of nonpositive volume is already nonfinite; no pseudocount/epsilon.
    return dict(valid=valid, signs=signs, forward=forward, reverse=reverse,
                symmetric=symmetric, orientation=orientation)


def current_volume_feature(rows):
    features = volume_lag_features(rows)
    assert len(rows) == 26 and len(features["valid"]) == 1
    if not features["valid"][0]:
        return None
    return dict(state=tuple(int(x) for x in features["signs"][0]),
                forward=float(features["forward"][0]), reverse=float(features["reverse"][0]),
                symmetric=float(features["symmetric"][0]),
                orientation=float(features["orientation"][0]))


def volume_lag_forecasts(rows):
    """Exactly360 slots, ages6..365; row0 padding is deliberately unused."""
    assert len(rows) == 392
    features = volume_lag_features(rows)
    # Feature index0 ends at row25; endpoints26..385 are indices1..360.
    states = features["signs"][1:361]
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        labels = np.log(rows[32:392, 2])-np.log(rows[26:386, 2])
    valid = features["valid"][1:361] & np.isfinite(labels)
    assert len(states) == len(labels) == len(valid) == 360
    support = all_cells()
    for values in support:
        key = tuple(int(x) for x in values.split("/"))
        support[values] = int(np.sum(valid & np.all(states == key, axis=1)))
    evidence = dict(reason="current_feature_invalid", slots=360,
                    valid_origins=int(np.sum(valid)), support=support,
                    n_state=0, n_control=0)
    if not features["valid"][-1]:
        return None, evidence
    current = features["signs"][-1]
    selected = valid & np.all(states == current, axis=1)
    # Both policies start with the SAME all-three-signs/nonzero mask.
    control = valid & np.all(states[:, :2] == current[:2], axis=1)
    n_state, n_control = int(np.sum(selected)), int(np.sum(control))
    evidence.update(n_state=n_state, n_control=n_control,
                    current_state=[int(x) for x in current])
    if n_state < 20:
        evidence["reason"] = "insufficient_cell"
        return None, evidence
    state_mean, control_mean = float(np.mean(labels[selected])), float(np.mean(labels[control]))
    if not math.isfinite(state_mean) or not math.isfinite(control_mean):
        evidence["reason"] = "mean_invalid"
        return None, evidence
    evidence.update(reason="valid", state_mean=state_mean, control_mean=control_mean,
                    bank_first=int(rows[26, 0])+BAR, bank_last=int(rows[385, 0])+BAR,
                    last_target=int(rows[391, 0])+BAR)
    return dict(STATE=state_mean, SYMMETRIC=control_mean), evidence


def empty_diagnostic():
    return dict(last=None, pending=[], registered=0, matured=0,
                censored_gap=0, censored_terminal=0, terminal=False,
                cells={key: dict(n=0, sum_y=0., sum_sy=0.) for key in all_cells()})


def diagnostic_step(state, now, bar, feature):
    """Math-only ledger: mature six actual OHLC bars before any training gate."""
    if state["last"] is not None and now <= state["last"]:
        return state
    assert not state["terminal"]
    result = dict(state, pending=[], cells={k: dict(v) for k, v in state["cells"].items()})
    pending = state["pending"]
    gap = state["last"] is not None and now != state["last"]+BAR
    if gap or bar is None:
        result["censored_gap"] += len(pending)
        pending = []
    if bar is not None:
        assert int(bar[0])+BAR == now
        for item in pending:
            observed = dict(item, steps=item["steps"]+1)
            assert observed["steps"] <= 6
            if observed["steps"] == 6:
                assert now == observed["deadline"]
                label = math.log(float(bar[2]))-math.log(observed["price"])
                assert math.isfinite(label)
                cell = result["cells"][cell_key(observed["state"])]
                cell["n"] += 1
                cell["sum_y"] += label
                cell["sum_sy"] += observed["state"][0]*label
                result["matured"] += 1
            else:
                assert now < observed["deadline"]
                result["pending"].append(observed)
        if feature is not None:
            result["pending"].append(dict(origin=now, price=float(bar[2]),
                state=feature["state"], deadline=now+6*BAR, steps=0))
            result["registered"] += 1
    else:
        assert feature is None
    result["last"] = now
    assert len(result["pending"]) <= 6
    return result


def diagnostic_finish(state):
    """PRETERMINAL/FINAL may repeat: censor each remaining origin only once."""
    if state["terminal"]:
        return state
    return dict(state, pending=[], terminal=True,
                censored_terminal=state["censored_terminal"]+len(state["pending"]))


class BtcResearchR25VolumeLagBase1m(BtcResearchR12ArBase1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("STATE", "SYMMETRIC")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        diagnostic = self.vars.get("volume_diagnostic", empty_diagnostic())
        # Do not rewind/censor/recount on duplicate or earlier callbacks.
        if diagnostic["last"] is not None and now <= diagnostic["last"]:
            return
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        counts = self.vars.setdefault("volume_lag_counts", {})
        current_bar = closed_window(candles, now, 1)
        mismatch = current_bar is not None and not math.isclose(
            float(current_bar[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        # Route/as-of parity is integrity for diagnostic labels too, even when
        # the longer training history is unavailable. Never record stale prices.
        if mismatch:
            current_bar = None
            counts["price_alignment_invalid"] = counts.get("price_alignment_invalid", 0)+1
        feature_rows = None if mismatch else closed_window(candles, now, 26)
        feature = current_volume_feature(feature_rows) if feature_rows is not None else None
        capture = feature if self.START < now < self.FINISH else None
        self.vars["volume_diagnostic"] = diagnostic_step(
            diagnostic, now, None if current_bar is None else current_bar[-1], capture)
        for reason in ("feature_valid" if feature is not None else "feature_invalid",):
            counts[reason] = counts.get(reason, 0)+1
        if mismatch:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        # Diagnostic above must not depend on this longer historical window.
        rows = closed_window(candles, now, 392)
        if rows is None:
            counts["train_window_invalid"] = counts.get("train_window_invalid", 0)+1
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        forecasts, evidence = volume_lag_forecasts(rows)
        self.vars["volume_train_last"] = evidence
        reason = evidence["reason"]
        counts[reason] = counts.get(reason, 0)+1
        if forecasts is None:
            return
        forecast = forecasts[self.MODE]
        if abs(forecast) <= .0019 or not self.START < now < self.FINISH:
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
        assert feature is not None
        self.vars["plan"] = dict(plan, volume_evidence=evidence, volume_feature=feature,
                                forecast=forecast, forecast_origin=now)
        self.vars["direction"] = direction

    def on_open_position(self, order):
        super().on_open_position(order)
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        self._log("R25_VOLUME_OPEN", dict(time=int(self.time), mode=self.MODE,
            forecast=plan["forecast"], forecast_origin=plan["forecast_origin"],
            forecast_deadline=plan["forecast_origin"]+6*BAR,
            opened_at=int(self.position.opened_at),
            hold_deadline=int(self.position.opened_at)+6*BAR,
            stop=float(self.position.entry_price)-direction*plan["distance"],
            distance=plan["distance"], risk_budget=plan["risk_budget"],
            feature=plan["volume_feature"], evidence=plan["volume_evidence"]))

    def _emit(self, stage):
        diagnostic = self.vars.get("volume_diagnostic", empty_diagnostic())
        if stage in ("PRETERMINAL", "FINAL"):
            diagnostic = diagnostic_finish(diagnostic)
            self.vars["volume_diagnostic"] = diagnostic
        super()._emit(stage)
        self._log("R25_TRAIN_STATS", dict(stage=stage, mode=self.MODE,
            counts=self.vars.get("volume_lag_counts", {}),
            last=self.vars.get("volume_train_last", {}),
            signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
            occupied=self.vars.get("occupied", 0)))
        self._log("R25_DIAG_STATS", dict(stage=stage, last=diagnostic["last"],
            registered=diagnostic["registered"], matured=diagnostic["matured"],
            censored_gap=diagnostic["censored_gap"],
            censored_terminal=diagnostic["censored_terminal"],
            pending=len(diagnostic["pending"]), terminal=diagnostic["terminal"]))
        # Bounded one-cell rows avoid truncating one large journal line.
        for key, values in diagnostic["cells"].items():
            self._log("R25_DIAG_CELL", dict(stage=stage, cell=key, **values))

```

## strategies/BtcResearchR25VolumeLagState1m/__init__.py
SHA256 01c7aba73af2f10b5af06f46be016e0e90b34e9cb15aad494f97f64cb103b041

```python
from strategies.BtcResearchR25VolumeLagBase1m import BtcResearchR25VolumeLagBase1m


class BtcResearchR25VolumeLagState1m(BtcResearchR25VolumeLagBase1m):
    MODE = "STATE"

```

## strategies/BtcResearchR25VolumeLagSymmetric1m/__init__.py
SHA256 2913fee1da3cd5e219fcee4c6691d802716bdace2bccf07011c41537394261d1

```python
from strategies.BtcResearchR25VolumeLagBase1m import BtcResearchR25VolumeLagBase1m


class BtcResearchR25VolumeLagSymmetric1m(BtcResearchR25VolumeLagBase1m):
    MODE = "SYMMETRIC"

```

## Checks y lectura posterior

Fullcheck7a53cb54457e4d478247cfae6dd4155b PASSED13grupos materiales, primer intento,NumPy1.26.4. Probe bdc2d3c5c0294a7cbc97ca925e8c4894 SUCCEEDED antes del fix final, evidenció V=2constante/std1.11e−16/featureespuria; su NaN literal queda como STRING en receipt estricto. Códigos exactos, jobs y artifacts se preservan en BTC_DISCOVERY_Y_TECHNICAL_RECEIPT_20261021.json.

Se releían por MCP después del fullcheck R10/R11/R12AR y tres fuentes nuevas: seis readbacks exactos, padres intactos. No cambios de fuentes entre el fullcheck y ese readback. Sin drafts/economía. Antecedentes completos en BTC_DISCOVERY_Y_CODES_AND_ANTECEDENTS_20261021.md; contrato normativo en BTC_DISCOVERY_Y_PROTOCOL_20261021.md.
