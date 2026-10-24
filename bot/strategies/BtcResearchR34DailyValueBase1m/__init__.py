import math
import numpy as np
import jesse.helpers as jh

from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, DAY, closed_window, atr14
from strategies.BtcResearchR16LegacyBase1m import legacy_plan

MINUTE = 60000
ENTRY_HOURS = (8, 12, 16, 20)


def daily_value(minutes, rows, day, cutoff):
    """M1 HLC3/volume proxy on [day,cutoff); the recovery bar is excluded."""
    count = (cutoff-day)//MINUTE
    if cutoff-day not in (BAR, 2*BAR, 3*BAR, 4*BAR):
        return None, "reference_maturity"
    if minutes is None or np.ndim(minutes) != 2 or minutes.shape[1] < 6:
        return None, "M1_shape"
    left = int(np.searchsorted(minutes[:, 0], day, side="left"))
    right = int(np.searchsorted(minutes[:, 0], cutoff, side="left"))
    ref = minutes[left:right]
    if len(ref) != count or not np.array_equal(
            ref[:, 0], day+np.arange(count, dtype=np.int64)*MINUTE):
        return None, "M1_timestamps"
    if (not np.all(np.isfinite(ref[:, :6])) or np.any(ref[:, 1:5] <= 0)
            or np.any(ref[:, 5] < 0)
            or np.any(ref[:, 3] < np.maximum(ref[:, 1], ref[:, 2]))
            or np.any(ref[:, 4] > np.minimum(ref[:, 1], ref[:, 2]))):
        return None, "M1_OHLCV"
    required = day+np.arange((cutoff-day)//BAR, dtype=np.int64)*BAR
    indexes = np.searchsorted(rows[:, 0], required)
    if (np.any(indexes >= len(rows))
            or not np.array_equal(rows[indexes, 0], required)):
        return None, "4h_reference"
    for k, index in enumerate(indexes):
        block = ref[k*240:(k+1)*240]
        aggregate = np.array([block[0, 1], block[-1, 2],
                              np.max(block[:, 3]), np.min(block[:, 4])])
        # Representation tolerance does not soften any trading inequality.
        if not np.allclose(aggregate, rows[index, 1:5], rtol=1e-10, atol=1e-8):
            return None, "M1_4h_parity"
    maximum = float(np.max(ref[:, 5]))
    if maximum <= 0:
        return None, "volume_zero"
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        weights = ref[:, 5]/maximum
        weights = weights/np.sum(weights)
        typical = ref[:, 3]/3.+ref[:, 4]/3.+ref[:, 2]/3.
        value = float(np.sum(weights*typical))
    if not math.isfinite(value) or value <= 0:
        return None, "value_nonfinite"
    return dict(value=value, count=int(count), cutoff=int(cutoff),
                reference_close=float(ref[-1, 2])), None


def recovery_direction(previous, current, value, atr_previous):
    if not all(math.isfinite(x) and x > 0
               for x in (previous, current, value, atr_previous)):
        return 0
    if previous <= value-2*atr_previous and previous < current < value:
        return 1
    if previous >= value+2*atr_previous and value < current < previous:
        return -1
    return 0


def target_valid(entry, target, direction, fee):
    if (direction not in (-1, 1)
            or not all(math.isfinite(x) and x > 0 for x in (entry, target))
            or not math.isfinite(fee) or fee < 0):
        return False, "nonfinite_or_nonpositive"
    profit = direction*(target-entry)
    if profit <= 0:
        return False, "wrong_side"
    # Use Jesse's exact native comparison. Its docstring mentions rounding,
    # but the audited body does NOT round and defaults to .00015.
    if jh.is_price_near(target, entry):
        return False, "native_near"
    fees = fee*(entry+target)
    if not math.isfinite(profit) or not math.isfinite(fees) or profit <= fees:
        return False, "base_fees"
    return True, "valid"


def shared_targets(entry, distance, value, direction, fee):
    fixed = entry+direction*2*distance
    value_ok, value_reason = target_valid(entry, value, direction, fee)
    fixed_ok, fixed_reason = target_valid(entry, fixed, direction, fee)
    return dict(value=value, fixed=fixed, value_ok=value_ok, fixed_ok=fixed_ok,
                value_reason=value_reason, fixed_reason=fixed_reason,
                valid=bool(value_ok and fixed_ok))


class BtcResearchR34DailyValueBase1m(BtcResearchR11Base1m):
    """One daily recovery attempt; only the frozen TP destination differs."""
    LABEL = "abstract"
    TARGET_MODE = "abstract"

    def _counts(self):
        return self.vars.setdefault("r34_counts", dict(events=0, plans=0,
            occupied=0, rejected_geometry=0, opens=0, closes=0,
            long_opens=0, short_opens=0, net=0.0,
            invalid_days=0, after_fill_invalid=0))

    def _day(self, now):
        day = now//DAY*DAY
        state = self.vars.setdefault("r34_day", dict(
            day=day, consumed=False, invalid_logged=False))
        if day != state["day"]:
            state.update(day=day, consumed=False, invalid_logged=False)
        return state

    def _invalidate(self, state, now, reason):
        state["consumed"] = True
        if not state["invalid_logged"]:
            state["invalid_logged"] = True
            self._counts()["invalid_days"] += 1
            self._log("R34_INVALID", dict(label=self.LABEL, time=now,
                day=state["day"], reason=reason))

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.LABEL != "abstract" and self.TARGET_MODE in ("VALUE", "R2")
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        # An engine callback is one M1 phase; duplicate/backward calls do not
        # duplicate observation, day state, or economic opportunities.
        if now <= self.vars.get("r34_pre_at", -1):
            return
        self.vars["r34_pre_at"] = now
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR or (now % DAY)//3600000 not in ENTRY_HOURS:
            return
        state = self._day(now)
        if state["consumed"]:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"),
                             now, 64)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self._invalidate(state, now, "4h_window")
            return
        # This is current-route infrastructure, unlike missing/invalid anchor
        # data: a mismatch must fail technically, never select a quiet day.
        assert math.isclose(float(rows[-1, 2]), float(self.price),
                            rel_tol=1e-10, abs_tol=1e-8), "R34_CURRENT_PRICE_PARITY"
        cutoff = now-BAR
        reference, reason = daily_value(self.candles, rows, state["day"], cutoff)
        if reference is None:
            self._invalidate(state, now, reason)
            return
        previous, current = float(rows[-2, 2]), float(rows[-1, 2])
        if not math.isclose(reference["reference_close"], previous,
                            rel_tol=1e-10, abs_tol=1e-8):
            self._invalidate(state, now, "previous_close_parity")
            return
        atr_previous, atr_current = atr14(rows[:-1]), atr14(rows)
        if (atr_previous is None or atr_current is None
                or not all(math.isfinite(x) and x > 0
                           for x in (atr_previous, atr_current))
                or not all(math.isfinite(x) for x in
                           (reference["value"]-2*atr_previous,
                            reference["value"]+2*atr_previous))):
            self._invalidate(state, now, "ATR_or_band")
            return
        if not self.vars.get("r34_data_ready"):
            self.vars["r34_data_ready"] = True
            self._log("R34_DATA_READY", dict(label=self.LABEL, time=now,
                cutoff=cutoff, count=reference["count"]))
        direction = recovery_direction(previous, current, reference["value"],
                                       atr_previous)
        if not direction:
            return
        # Raw pattern consumes BEFORE targets, sizing, occupancy or same-exit.
        state["consumed"] = True
        counts = self._counts()
        counts["events"] += 1
        self.vars["signals"] = self.vars.get("signals", 0)+1
        value, entry, distance = reference["value"], float(self.price), 2*atr_current
        guards = shared_targets(entry, distance, value, direction, self.fee_rate)
        self._log("R34_RAW", dict(label=self.LABEL, time=now, day=state["day"],
            cutoff=cutoff, direction=direction, value=value,
            previous=previous, current=current,
            atr_previous=atr_previous, atr_current=atr_current))
        self._log("R34_TARGET_GUARD", dict(label=self.LABEL, time=now, **guards))
        if not guards["valid"]:
            counts["rejected_geometry"] += 1
            return
        if not self.START < now < self.FINISH:
            return
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            counts["occupied"] += 1
            return
        target = value if self.TARGET_MODE == "VALUE" else guards["fixed"]
        candidate = dict(origin=self.LABEL, direction=direction, entry=entry,
            distance=distance, target_distance=direction*(target-entry),
            hold_hours=None, order_kind="MARKET")
        plan = legacy_plan(candidate, .5*max(0.0, float(self.balance)),
                           .5*float(self.available_margin),
                           float(self.leverage), float(self.fee_rate))
        if plan is None:
            counts["rejected_geometry"] += 1
            return
        meta = dict(value=value, deadline=state["day"]+DAY,
                    policy=self.TARGET_MODE, targetlevel=target,
                    previous=previous, cutoff=cutoff)
        plan.update(signal_at=now, meta=meta)
        self.vars["plan"] = plan
        self.vars["direction"] = direction
        counts["plans"] += 1
        self._log("R34_PLAN", dict(label=self.LABEL, time=now,
            direction=direction, entry=entry, qty=plan["qty"],
            distance=distance, risk_budget=plan["risk_budget"],
            planned_loss=plan["planned_loss"], meta=meta))

    def _request_exit(self, reason):
        now = int(self.time)
        if not self.is_open or self.vars.get("r34_exit_at") == now:
            return
        self.vars["r34_exit_at"] = now
        self.vars["r34_exit_reason"] = reason
        self._log("R34_EXIT_REQUEST", dict(label=self.LABEL, time=now, reason=reason))
        self.liquidate()

    def on_open_position(self, order):
        plan = self.vars["plan"]
        self.vars.pop("r34_exit_reason", None)
        self.vars.pop("r34_exit_at", None)
        direction = 1 if self.is_long else -1
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        distance, meta = plan["distance"], plan["meta"]
        stop = entry-direction*distance
        checks = shared_targets(entry, distance, meta["value"],
                                direction, float(self.fee_rate))
        target = meta["value"] if self.TARGET_MODE == "VALUE" else checks["fixed"]
        unit = distance+self.fee_rate*(entry+stop)+.001*entry
        actual_loss = qty*unit
        safe = (direction == plan["direction"] and qty > 0
                and math.isfinite(entry) and entry > 0
                and math.isfinite(stop) and stop > 0
                and math.isfinite(actual_loss)
                and actual_loss <= plan["risk_budget"]+1e-6
                and checks["valid"])
        # Protect any physically valid stop even if a target/fill guard failed.
        # Do not call a parent fill-parity assertion before this safety path.
        if math.isfinite(stop) and stop > 0 and math.isfinite(qty) and qty > 0:
            self.stop_loss = qty, stop
        if safe:
            self.take_profit = qty, target
        counts = self._counts()
        counts["opens"] += 1
        counts["long_opens" if direction == 1 else "short_opens"] += 1
        self.vars["entries"] = self.vars.get("entries", 0)+1
        self.vars["r34_active"] = dict(deadline=meta["deadline"],
            opened_at=int(self.position.opened_at), stop=stop, target=target,
            direction=direction, invalid=not safe)
        if not safe:
            counts["after_fill_invalid"] += 1
        self._log("R34_OPEN", dict(label=self.LABEL, time=int(self.time),
            signal_at=plan["signal_at"], opened_at=int(self.position.opened_at),
            direction=direction, entry=entry, qty=qty, distance=distance,
            risk_budget=plan["risk_budget"],
            stop=stop if math.isfinite(stop) else None,
            target_distance=direction*(target-entry) if math.isfinite(target) else None,
            deadline=meta["deadline"], policy=self.TARGET_MODE,
            after_fill_invalid=not safe, target_submitted=bool(safe),
            actual_loss=actual_loss if math.isfinite(actual_loss) else None))
        self._observe("open")
        if not safe:
            self._request_exit("after_fill_invalid")

    def update_position(self):
        # Deadline is checked on EVERY M1, with no feature/calendar/volume veto.
        if not self.is_open:
            return
        active = self.vars.get("r34_active")
        if active is None:
            self._request_exit("after_fill_invalid")
        elif int(self.time) >= active["deadline"]:
            self._request_exit("finish" if self.time >= self.FINISH else "deadline")

    def on_close_position(self, order, closed_trade):
        identity = str(closed_trade.id)
        seen = self.vars.setdefault("r34_closed_ids", set())
        if identity in seen:
            return
        seen.add(identity)
        pnl = float(closed_trade.pnl)
        assert math.isfinite(pnl)
        counts = self._counts()
        counts["closes"] += 1
        counts["net"] += pnl
        reason = self.vars.get("r34_exit_reason") or getattr(order, "submitted_via", None) or "native_exit"
        self._log("R34_CLOSE", dict(label=self.LABEL, time=int(self.time),
            trade_id=identity, net=pnl, reason=reason))
        self.vars["direction"] = 0
        self.vars["r34_active"] = None
        # Financial counters precede R11 close observation and any FINAL.
        super().on_close_position(order, closed_trade)

    def before_terminate(self):
        if self.is_open:
            self.vars.setdefault("r34_exit_reason", "finish")
        super().before_terminate()

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R34_SUMMARY", dict(stage=stage, label=self.LABEL,
            risk_total=.01, capital_denominator="total BTC wallet",
            redistribution=False, target_mode=self.TARGET_MODE,
            deadline_mode="next UTC midnight", **self._counts()))
