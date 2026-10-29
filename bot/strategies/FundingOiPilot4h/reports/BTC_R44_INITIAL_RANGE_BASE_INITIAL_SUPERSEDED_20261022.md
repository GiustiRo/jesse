# R44 — primera base supersedida antes de checks/motores

SHA256 6a9b9cf9adcc8486df10d4313f259810c21e19900a3e72ea4523aac1191f5391. Revisión independiente pidió validar que el buffer4h tenga timestamps finitos y estrictamente crecientes antes de searchsorted, sin ordenar ni reparar. No hubo jobs propios ni motores con esta versión. Hojas y padres permanecen intactos.

```python
import json
import math
from datetime import datetime, timedelta, timezone

import numpy as np
from jesse import utils
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR16LegacyBase1m import legacy_plan, RESERVE

MINUTE = 60000
BAR = 14400000
DAY = 86400000
FULL_HOURS = {"timezone": "UTC", "hours": {"Mon-Sun": "00:00-24:00"}}


def cycle_clock(candle_open_time, phase_hour):
    """Calendar anchor from the closed candle's OPEN, not its decision close."""
    assert phase_hour in (0, 12)
    stamp = datetime.fromtimestamp(candle_open_time/1000, timezone.utc)
    anchor = stamp.replace(hour=phase_hour, minute=0, second=0, microsecond=0)
    if stamp < anchor:
        anchor -= timedelta(days=1)
    start = int(anchor.timestamp()*1000)
    return dict(anchor=start, formation=start+2*BAR, deadline=start+DAY)


def minute_integrity(row, now, price):
    """M1 integrity failures are fatal technical failures, never cash observations."""
    row = np.asarray(row)
    if row.ndim != 1 or len(row) < 5:
        return "m1_shape"
    if not all(math.isfinite(float(v)) for v in row[:5]):
        return "m1_nonfinite"
    if float(row[0]) != now-MINUTE or now % MINUTE:
        return "m1_clock"
    opening, close, high, low = map(float, row[1:5])
    if min(opening, close, high, low) <= 0:
        return "m1_nonpositive"
    if high < max(opening, close) or low > min(opening, close):
        return "m1_geometry"
    if not math.isfinite(price) or not math.isclose(close, price, rel_tol=1e-10, abs_tol=1e-8):
        return "m1_price_asof"
    return None


def formation_range(candles4h, anchor, now, window):
    """Two exact closed formation bars, filtered by the declared UTC schedule.

    Returns (range, reason). range contains upper/lower and both OHLC snapshots.
    It never retries an invalid range or selects a later pair of bars.
    """
    if now != anchor+2*BAR:
        return None, "formation_clock"
    rows = np.asarray(candles4h)
    if rows.ndim != 2 or rows.shape[1] < 5:
        return None, "formation_shape"
    end = int(np.searchsorted(rows[:, 0], now-BAR, side="right"))
    start = int(np.searchsorted(rows[:, 0], anchor, side="left"))
    selected = rows[start:end]
    if len(selected) != 2:
        return None, "formation_missing"
    if selected[0, 0] != anchor or selected[1, 0] != anchor+BAR:
        return None, "formation_timestamps"
    # Same schedule as the runtime formation gate; do not filter the full buffer.
    selected = utils.filter_candles_by_hours(selected, window)
    if len(selected) != 2:
        return None, "formation_hours"
    if not np.all(np.isfinite(selected[:, :5])) or np.any(selected[:, 1:5] <= 0):
        return None, "formation_ohlc"
    if (np.any(selected[:, 3] < np.maximum(selected[:, 1], selected[:, 2]))
            or np.any(selected[:, 4] > np.minimum(selected[:, 1], selected[:, 2]))):
        return None, "formation_geometry"
    upper, lower = float(np.max(selected[:, 3])), float(np.min(selected[:, 4]))
    if upper <= lower:
        return None, "formation_zero_range"
    return dict(upper=upper, lower=lower,
                bars=selected[:, :5].astype(float).tolist(),
                final_close=float(selected[-1, 2])), None


class BtcResearchR44InitialRangeBase1m(BtcResearchR11Base1m):
    """Initial 8h range; first M1 close outside it, structural stop and cycle exit."""
    LABEL = "abstract"
    PHASE_HOUR = -1

    def trading_hours(self):
        return FULL_HOURS

    def _formation_window(self):
        hours = "00:00-08:00" if self.PHASE_HOUR == 0 else "12:00-20:00"
        return dict(timezone="UTC", hours={"Mon-Sun": hours})

    def _entry_window(self):
        hours = "08:00-24:00" if self.PHASE_HOUR == 0 else "20:00-12:00"
        return dict(timezone="UTC", hours={"Mon-Sun": hours})

    def _log(self, label, payload):
        encoded = label+" "+json.dumps(payload, separators=(",", ":"), allow_nan=False)
        assert len(encoded) < 1800, "R44_LOG_TOO_LARGE"
        self.log(encoded)

    def _counts(self):
        return self.vars.setdefault("r44_counts", dict(
            cycles=0, partial_cycles=0, ranges=0, invalid_ranges=0,
            finalized_cycles=0, noevent_cycles=0,
            events=0, plans=0, occupied=0, rejected_geometry=0,
            opens=0, closes=0, long_opens=0, short_opens=0, net=0.))

    def _finish_cycle(self, now, stage):
        cycle = self.vars.get("r44_cycle")
        if cycle is None or cycle["finalized"]:
            return
        cycle["finalized"] = True
        counts = self._counts()
        if cycle["eligible_anchor"]:
            counts["finalized_cycles"] += 1
            if cycle["status"] == "valid" and not cycle["consumed"]:
                counts["noevent_cycles"] += 1
        self._log("R44_CYCLE", dict(label=self.LABEL, time=now, stage=stage,
            phase_hour=self.PHASE_HOUR, anchor=cycle["anchor"],
            formation=cycle["formation"], deadline=cycle["deadline"],
            eligible_anchor=cycle["eligible_anchor"], status=cycle["status"],
            consumed=cycle["consumed"], upper=cycle.get("upper"), lower=cycle.get("lower"),
            evaluated=cycle["evaluated"], inside_evaluated=cycle["inside_evaluated"],
            inside_min=cycle["inside_min"], inside_max=cycle["inside_max"],
            event_at=cycle["event_at"], event_direction=cycle["event_direction"],
            event_prior_evaluated=cycle["event_prior_evaluated"]))

    def _new_cycle(self, clock):
        eligible = clock["anchor"] >= self.START
        self._counts()["cycles" if eligible else "partial_cycles"] += 1
        cycle = dict(clock, eligible_anchor=eligible, status="forming" if eligible else "initial_partial",
            consumed=False, finalized=False, evaluated=0, inside_evaluated=0,
            inside_min=None, inside_max=None, event_at=None, event_direction=0,
            event_prior_evaluated=None)
        self.vars["r44_cycle"] = cycle
        return cycle

    def before(self):
        now = int(self.time)
        assert self.START < now <= self.FINISH, "R44_M1_OUTSIDE_WINDOW"
        if not self.vars.get("checked"):
            assert self.LABEL != "abstract" and self.PHASE_HOUR in (0, 12)
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        previous = self.vars.get("r44_last_minute", self.START)
        assert now == previous+MINUTE, "R44_M1_CALLBACK_GAP_OR_DUPLICATE"
        price = float(self.price)
        reason = minute_integrity(self.current_candle, now, price)
        assert reason is None, "R44_FATAL_"+str(reason)
        candle_open = int(self.closed_candle_open_time)
        assert candle_open == now-MINUTE, "R44_CANDLE_OPEN_PROPERTY"
        self.vars["r44_last_minute"] = now
        self._observe("pre")
        self.vars["direction"] = 0
        clock = cycle_clock(candle_open, self.PHASE_HOUR)
        cycle = self.vars.get("r44_cycle")
        if cycle is None or cycle["anchor"] != clock["anchor"]:
            if cycle is not None:
                self._finish_cycle(now, "roll")
            cycle = self._new_cycle(clock)
        if now >= cycle["deadline"]:
            self._finish_cycle(now, "deadline")
        if not cycle["eligible_anchor"]:
            return
        if now == cycle["formation"]:
            assert cycle["status"] == "forming"
            if not utils.is_in_trading_hours(candle_open, self._formation_window()):
                result, reason = None, "formation_decision_hours"
            else:
                result, reason = formation_range(
                    self.get_candles(self.exchange, self.symbol, "4h"),
                    cycle["anchor"], now, self._formation_window())
            if result is not None and not math.isclose(result["final_close"], price,
                                                        rel_tol=1e-10, abs_tol=1e-8):
                result, reason = None, "formation_price_asof"
            if result is None:
                cycle["status"] = "invalid"
                self._counts()["invalid_ranges"] += 1
                self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
                self._log("R44_FORM_INVALID", dict(label=self.LABEL, time=now,
                    anchor=cycle["anchor"], formation=cycle["formation"],
                    deadline=cycle["deadline"], reason=reason))
            else:
                cycle.update(result)
                cycle["status"] = "valid"
                self._counts()["ranges"] += 1
                self._log("R44_RANGE", dict(label=self.LABEL, time=now,
                    anchor=cycle["anchor"], formation=cycle["formation"],
                    deadline=cycle["deadline"], upper=result["upper"],
                    lower=result["lower"], bars=result["bars"]))
        if (now >= self.FINISH or cycle["status"] != "valid" or cycle["consumed"]
                or not cycle["formation"] < now < cycle["deadline"]):
            return
        if not utils.is_in_trading_hours(candle_open, self._entry_window()):
            return
        prior_evaluated = cycle["evaluated"]
        cycle["evaluated"] += 1
        direction = 1 if price > cycle["upper"] else -1 if price < cycle["lower"] else 0
        if not direction:
            cycle["inside_evaluated"] += 1
            cycle["inside_min"] = price if cycle["inside_min"] is None else min(cycle["inside_min"], price)
            cycle["inside_max"] = price if cycle["inside_max"] is None else max(cycle["inside_max"], price)
            return
        # The first opportunity is consumed even when its account cannot trade.
        cycle["consumed"] = True
        cycle["event_at"], cycle["event_direction"] = now, direction
        cycle["event_prior_evaluated"] = prior_evaluated
        counts = self._counts()
        counts["events"] += 1
        self.vars["signals"] = self.vars.get("signals", 0)+1
        self._log("R44_EVENT", dict(label=self.LABEL, time=now,
            anchor=cycle["anchor"], formation=cycle["formation"], deadline=cycle["deadline"],
            upper=cycle["upper"], lower=cycle["lower"], price=price, direction=direction,
            remaining_minutes=(cycle["deadline"]-now)//MINUTE,
            prior_evaluated=prior_evaluated,
            prior_inside_min=cycle["inside_min"], prior_inside_max=cycle["inside_max"]))
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            counts["occupied"] += 1
            return
        stop = cycle["lower"] if direction == 1 else cycle["upper"]
        distance = direction*(price-stop)
        candidate = dict(origin=self.LABEL, direction=direction, entry=price,
            distance=distance, target_distance=None, hold_hours=None, order_kind="MARKET",
            stop=stop, upper=cycle["upper"], lower=cycle["lower"],
            anchor=cycle["anchor"], formation=cycle["formation"], deadline=cycle["deadline"])
        plan = legacy_plan(candidate, .5*max(0., float(self.balance)),
                           .5*float(self.available_margin), float(self.leverage),
                           float(self.fee_rate))
        if plan is None:
            counts["rejected_geometry"] += 1
            return
        plan["signal_at"] = now
        self.vars["plan"] = plan
        self.vars["direction"] = direction
        counts["plans"] += 1
        self._log("R44_PLAN", dict(label=self.LABEL, time=now, direction=direction,
            entry=price, distance=distance, qty=plan["qty"],
            risk_budget=plan["risk_budget"], planned_loss=plan["planned_loss"],
            anchor=plan["anchor"], deadline=plan["deadline"],
            margin_limited=plan["margin_limited"], gross_limited=plan["gross_limited"]))

    def should_long(self):
        return (self.vars.get("direction") == 1 and self.is_trading_hours
                and utils.is_in_trading_hours(self.closed_candle_open_time, self._entry_window()))

    def should_short(self):
        return (self.vars.get("direction") == -1 and self.is_trading_hours
                and utils.is_in_trading_hours(self.closed_candle_open_time, self._entry_window()))

    def _submit(self, direction):
        now = int(self.time)
        plan = self.vars["plan"]
        assert self.vars.get("r44_submitted_at") != now, "R44_DUPLICATE_SUBMISSION"
        assert plan["signal_at"] == now and plan["direction"] == direction
        assert self.START < now < min(plan["deadline"], self.FINISH)
        assert not self.is_open and not self.entry_orders
        self.vars["r44_submitted_at"] = now
        self.vars["pending_plan"] = dict(plan)
        if direction == 1:
            self.buy = plan["qty"], self.price
        else:
            self.sell = plan["qty"], self.price

    def go_long(self):
        self._submit(1)

    def go_short(self):
        self._submit(-1)

    def on_open_position(self, order):
        plan = self.vars["pending_plan"]
        now = int(self.time)
        assert plan is not None and self.vars.get("position_plan") is None
        assert plan["signal_at"] == now == int(self.position.opened_at), "R44_MARKET_FILL_CLOCK"
        direction = 1 if self.is_long else -1
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        assert direction == plan["direction"]
        assert math.isclose(entry, plan["entry"], rel_tol=1e-10, abs_tol=1e-8)
        assert abs(qty-plan["qty"]) < 1e-8
        stop = float(plan["lower"] if direction == 1 else plan["upper"])
        distance = direction*(entry-stop)
        loss = qty*(distance+self.fee_rate*(entry+stop)+RESERVE*entry)
        assert distance > 0 and stop > 0 and math.isfinite(loss)
        assert loss <= plan["risk_budget"]+1e-6
        assert now < plan["deadline"]
        self.stop_loss = qty, stop
        # This snapshot is never mutated by a later signal cycle or exit request.
        self.vars["position_plan"] = dict(plan, actual_entry=entry,
            actual_distance=distance, actual_loss=loss, filled_at=int(self.position.opened_at))
        self.vars["pending_plan"] = None
        self.vars["r44_exit_requested_at"] = None
        self.vars["entries"] = self.vars.get("entries", 0)+1
        counts = self._counts()
        counts["opens"] += 1
        counts["long_opens" if direction == 1 else "short_opens"] += 1
        self._observe("open")
        self._log("R44_OPEN", dict(label=self.LABEL, time=now,
            signal_at=plan["signal_at"], opened_at=int(self.position.opened_at),
            direction=direction, entry=entry, qty=qty, distance=distance,
            risk_budget=plan["risk_budget"], stop=stop, target_distance=None,
            hold_hours=None, anchor=plan["anchor"], deadline=plan["deadline"],
            upper=plan["upper"], lower=plan["lower"]))

    def update_position(self):
        now = int(self.time)
        if now >= self.FINISH:
            return
        plan = self.vars["position_plan"]
        assert plan is not None
        if now >= plan["deadline"]:
            assert self.vars.get("r44_exit_requested_at") != now
            self.vars["r44_exit_requested_at"] = now
            self._log("R44_EXIT_REQUEST", dict(label=self.LABEL, time=now,
                anchor=plan["anchor"], deadline=plan["deadline"], reason="deadline"))
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        now = int(self.time)
        plan = self.vars["position_plan"]
        assert plan is not None
        pnl = float(closed_trade.pnl)
        assert math.isfinite(pnl)
        counts = self._counts()
        counts["closes"] += 1
        counts["net"] += pnl
        native_type = getattr(order, "type", None)
        submitted_via = getattr(order, "submitted_via", None)
        native_type = str(native_type) if native_type is not None else None
        submitted_via = str(submitted_via) if submitted_via is not None else None
        # MARKET alone does not prove terminal/deadline; native tags are observations.
        reason = "unclassified"
        if native_type == "STOP":
            reason = "native_stop"
        elif native_type == "MARKET" and self.vars.get("r44_terminating"):
            reason = "terminal"
        elif native_type == "MARKET" and self.vars.get("r44_exit_requested_at") == now:
            reason = "deadline"
        self._log("R44_CLOSE", dict(label=self.LABEL, time=now, net=pnl,
            anchor=plan["anchor"], deadline=plan["deadline"], reason=reason,
            native_type=native_type, submitted_via=submitted_via))
        self.vars["position_plan"] = None
        self.vars["pending_plan"] = None
        self.vars["direction"] = 0
        # R11 may emit FINAL during super; totals above must include this close.
        super().on_close_position(order, closed_trade)

    def before_terminate(self):
        assert self.vars.get("r44_last_minute") == self.FINISH, "R44_INCOMPLETE_M1_LEDGER"
        self._finish_cycle(int(self.time), "terminal")
        self.vars["r44_terminating"] = True
        super().before_terminate()

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R44_SUMMARY", dict(stage=stage, label=self.LABEL,
            phase_hour=self.PHASE_HOUR, hold_hours=None, tp_r=None,
            risk_total=.01, redistribution=False, capital_denominator="total BTC wallet",
            wallet=float(self.balance), position_qty=float(self.position.qty),
            **self._counts()))
```
