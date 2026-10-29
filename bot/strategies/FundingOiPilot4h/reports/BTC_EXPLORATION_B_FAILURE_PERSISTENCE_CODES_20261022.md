# Línea B — CODES y evidencia documental congelada

Fecha local2026-10-22. Anexo a BTC_EXPLORATION_B_FAILURE_PERSISTENCE_PROTOCOL_20261022.md. Sólo snapshots recibidos mediante MCP; NO fuentes nuevas B ni jobs/drafts/economía. Padres intactos. El protocolo registra reglas, diferencia limitada respecto de V1H2 y máximo2 motores. No novedad universal ni búsqueda global exhaustiva. Esta entrega no acredita nuevas pruebas.

## Fuentes completas de infraestructura y antecedentes directos

### strategies/BtcResearchR32SpecialistBase1m/__init__.py

SHA256 205407530bc40ea95131a0e6f2ed3e997b7bb5616bb5c573f170a772317307e3; 6263 caracteres. Fuente completa recibida mediante read_strategy.

```python
import math

from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14
from strategies.BtcResearchR16LegacyBase1m import legacy_plan


class BtcResearchR32SpecialistBase1m(BtcResearchR11Base1m):
    """Frozen one-percent specialist execution; leaves define causal events only."""
    LABEL = "abstract"
    HOLD_HOURS = 48
    TP_R = 2.0

    def _event(self, rows, now):
        raise NotImplementedError

    def _invalid_event(self, now):
        # Stateful leaves may invalidate an episode; rolling leaves need no state.
        pass

    def _r32_counts(self):
        return self.vars.setdefault("r32_counts", dict(events=0, plans=0,
            occupied=0, rejected_geometry=0, opens=0, closes=0,
            long_opens=0, short_opens=0, net=0.0))

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.LABEL != "abstract"
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate - .00045) < 1e-12
            assert abs(self.balance - 10000) < 1e-6
            assert self.HOLD_HOURS in (24, 48)
            assert self.TP_R in (None, 2.0)
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"),
                             now, 64)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            self._invalid_event(now)
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price),
                            rel_tol=1e-10, abs_tol=1e-8)
        # Evaluate/consume before occupancy and account guards, identically in
        # both leaves of a comparison. Never defer an occupied event to later.
        event = self._event(rows, now)
        if event is None:
            return
        direction = event["direction"]
        assert direction in (-1, 1)
        counts = self._r32_counts()
        counts["events"] += 1
        self.vars["signals"] = self.vars.get("signals", 0) + 1
        if not self.START < now < self.FINISH:
            return
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            counts["occupied"] += 1
            return
        atr = atr14(rows)
        if atr is None:
            counts["rejected_geometry"] += 1
            return
        entry = float(self.price)
        distance = 2 * atr
        target_distance = None if self.TP_R is None else self.TP_R * distance
        if target_distance is not None and entry + direction * target_distance <= 0:
            counts["rejected_geometry"] += 1
            return
        candidate = dict(origin=self.LABEL, direction=direction, entry=entry,
            distance=distance, target_distance=target_distance,
            hold_hours=self.HOLD_HOURS, order_kind="MARKET")
        plan = legacy_plan(candidate, .5 * max(0.0, float(self.balance)),
                           .5 * float(self.available_margin),
                           float(self.leverage), float(self.fee_rate))
        if plan is None:
            counts["rejected_geometry"] += 1
            return
        plan.update(signal_at=now, meta=event.get("meta", {}))
        self.vars["plan"] = plan
        self.vars["direction"] = direction
        counts["plans"] += 1
        self._log("R32_PLAN", dict(label=self.LABEL, time=now,
            direction=direction, entry=entry, distance=distance,
            qty=plan["qty"], risk_budget=plan["risk_budget"],
            planned_loss=plan["planned_loss"], meta=plan["meta"]))

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        assert direction == plan["direction"]
        assert math.isclose(entry, plan["entry"], rel_tol=1e-10, abs_tol=1e-8)
        stop = entry - direction * plan["distance"]
        unit = plan["distance"] + self.fee_rate * (entry + stop) + .001 * entry
        assert stop > 0 and qty * unit <= plan["risk_budget"] + 1e-6
        self.stop_loss = qty, stop
        if plan["target_distance"] is not None:
            target = entry + direction * plan["target_distance"]
            assert target > 0
            self.take_profit = qty, target
        self.vars["entries"] = self.vars.get("entries", 0) + 1
        counts = self._r32_counts()
        counts["opens"] += 1
        counts["long_opens" if direction == 1 else "short_opens"] += 1
        self._log("R32_OPEN", dict(label=self.LABEL, time=int(self.time),
            signal_at=plan["signal_at"], opened_at=int(self.position.opened_at),
            direction=direction, entry=entry, qty=qty,
            distance=plan["distance"], risk_budget=plan["risk_budget"],
            stop=stop, target_distance=plan["target_distance"],
            hold_hours=plan["hold_hours"]))
        self._observe("open")

    def update_position(self):
        # Management remains on closed four-hour clocks; MARKET entry at that
        # same clock cannot trigger its own time exit.
        now = int(self.time)
        if now % BAR == 0 and now - int(self.position.opened_at) >= self.HOLD_HOURS * 3600000:
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        counts = self._r32_counts()
        pnl = float(closed_trade.pnl)
        assert math.isfinite(pnl)
        counts["closes"] += 1
        counts["net"] += pnl
        self.vars["direction"] = 0
        self._log("R32_CLOSE", dict(label=self.LABEL, time=int(self.time), net=pnl))
        # Source totals must precede any terminal observer emission.
        super().on_close_position(order, closed_trade)

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R32_SUMMARY", dict(stage=stage, label=self.LABEL,
            hold_hours=self.HOLD_HOURS, tp_r=self.TP_R,
            risk_total=.01, capital_denominator="total BTC wallet",
            redistribution=False, **self._r32_counts()))
```

### strategies/BtcResearchR11Base1m/__init__.py

SHA256 be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87; 10150 caracteres. Fuente completa recibida mediante read_strategy.

```python
import json
import math
from datetime import datetime, timezone

import numpy as np
from jesse.strategies import Strategy
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def cusum_step(rows, accumulators):
    """Transfer the R40 design:60 past log returns, drift0.25, boundary4."""
    returns = np.diff(np.log(rows[-62:, 2]))
    sigma = float(np.std(returns[:-1], ddof=1))
    if not math.isfinite(sigma) or sigma <= 0:
        return 0, (0.0, 0.0)
    z = float((returns[-1] - np.mean(returns[:-1])) / sigma)
    if not math.isfinite(z):
        return 0, (0.0, 0.0)
    up = max(0.0, accumulators[0] + z - 0.25)
    down = max(0.0, accumulators[1] - z - 0.25)
    if up >= 4 or down >= 4:
        direction = 0 if up >= 4 and down >= 4 else 1 if up >= 4 else -1
        return direction, (0.0, 0.0)
    return 0, (up, down)


def absorption_signal(rows):
    """Large volume but small body, followed by escape of that closed bar."""
    window, setup, confirmation = rows[-26:-2], rows[-2], rows[-1]
    if not np.all(np.isfinite(rows[-26:, 5])) or np.any(rows[-26:, 5] < 0):
        return 0
    average_volume = float(np.mean(window[:, 5]))
    prior_atr = atr14(window)
    if not math.isfinite(average_volume) or average_volume <= 0 or prior_atr is None:
        return 0
    if setup[5] < 2 * average_volume or abs(setup[2] - setup[1]) > 0.25 * prior_atr:
        return 0
    if confirmation[2] > setup[3]:
        return 1
    if confirmation[2] < setup[4]:
        return -1
    return 0


def month_name(timestamp):
    return datetime.fromtimestamp(timestamp / 1000, timezone.utc).strftime("%Y-%m")


def monthly_summary(boundaries, active_months):
    """Declared post-settlement/pre-decision UTC cuts; no00:01 approximation."""
    points = sorted(boundaries.items())
    months = []
    for (start, before), (finish, after) in zip(points, points[1:]):
        stamp = datetime.fromtimestamp(start / 1000, timezone.utc)
        month = stamp.strftime("%Y-%m")
        complete = stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0
        if before <= 0:
            continue
        months.append(dict(month=month, start=start, finish=finish,
                           complete=complete, active=month in active_months,
                           pnl=after-before, return_fraction=after/before-1))
    complete = [m for m in months if m["complete"]]
    active = [m for m in complete if m["active"]]
    quarter_groups = {}
    for m in months:
        quarter = m["month"][:4] + "Q" + str((int(m["month"][5:])-1)//3+1)
        quarter_groups.setdefault(quarter, []).append(m)
    quarters = [q for q in quarter_groups.values()
                if len(q) == 3 and all(m["complete"] for m in q)]
    returns = [m["return_fraction"] for m in complete]
    contributions = sorted([m["pnl"] for m in months], reverse=True)
    return dict(months=months, complete_months=len(complete), active_months=len(active),
                positive_active=sum(m["pnl"] > 0 for m in active),
                positive_calendar=sum(m["pnl"] > 0 for m in complete),
                median_return=float(np.median(returns)) if returns else None,
                complete_quarters=len(quarters),
                positive_quarters=sum(sum(m["pnl"] for m in q) > 0 for q in quarters),
                pnl_without_best_two=sum(m["pnl"] for m in months)-sum(contributions[:2]))


class BtcResearchR11Base1m(Strategy):
    """M1 accounting observer; signal and management decisions remain4h."""
    MODE = "abstract"
    START = 1602720000000
    FINISH = 1767225600000

    def _log(self, label, payload):
        # Event logs stay small; monthly history is emitted as separate rows.
        self.log(label + " " + json.dumps(payload, separators=(",", ":"), allow_nan=False))

    def _observe(self, stage):
        now = int(self.time)
        # BTC-only futures equity. portfolio_value multiplies open PnL by
        # leverage in this checkout, so it is deliberately not used here.
        equity = float(self.balance) + (float(self.position.pnl) if self.is_open else 0.0)
        assert math.isfinite(equity)
        self.vars["peak"] = max(self.vars.get("peak", 10000.0), equity)
        drawdown = equity / self.vars["peak"] - 1
        self.vars["dd"] = min(self.vars.get("dd", 0.0), drawdown)
        self.vars["sequence"] = self.vars.get("sequence", 0) + 1
        self.vars["last_equity"] = equity
        active = self.vars.setdefault("active_months", set())
        if self.is_open:
            # Pre marks describe exposure during the minute that just closed;
            # an opening fill at T instead belongs to the new interval.
            active.add(month_name(now if stage == "open" else now-1))
        boundaries = self.vars.setdefault("boundaries", {self.START: 10000.0})
        if stage == "pre":
            self.vars["minute_marks"] = self.vars.get("minute_marks", 0) + 1
            stamp = datetime.fromtimestamp(now / 1000, timezone.utc)
            if stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0:
                boundaries[now] = equity
        if now >= self.FINISH:
            # A later terminal close callback replaces the mark with post-fee equity.
            boundaries[self.FINISH] = equity
        return equity

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate - 0.00045) < 1e-12
            assert abs(self.balance - 10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        # This is signal alignment, not a market-session/calendar filter.
        if now % BAR != 0:
            return
        count = 62 if self.MODE == "CUSUM" else 26
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        rows = closed_window(candles, now, count)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            self.vars["cusum"] = (0.0, 0.0)
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        if self.MODE == "CUSUM":
            direction, state = cusum_step(rows, self.vars.get("cusum", (0.0, 0.0)))
            self.vars["cusum"] = state
        else:
            assert self.MODE == "ABSORPTION"
            direction = absorption_signal(rows)
        if not direction or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0) + 1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0) + 1
            return
        atr = atr14(rows)
        if atr is None:
            return
        # Flat BTC account: wallet equals equity. Reuse the frozen2% fee-aware
        # plan, eight-decimal research precision and90% margin ceiling.
        capital = max(0.0, float(self.balance))
        plan = entry_plan(float(self.price), capital, float(self.available_margin),
                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)
        if plan is None or self.price + direction * 2 * plan["distance"] <= 0:
            return
        self.vars["direction"] = direction
        self.vars["plan"] = plan

    def should_long(self):
        return self.vars.get("direction") == 1

    def should_short(self):
        return self.vars.get("direction") == -1

    def go_long(self):
        self.buy = self.vars["plan"]["qty"], self.price

    def go_short(self):
        self.sell = self.vars["plan"]["qty"], self.price

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        stop = entry - direction * plan["distance"]
        target = entry + direction * 2 * plan["distance"]
        assert qty * (plan["distance"] + self.fee_rate * (entry + stop)) <= plan["risk_budget"] + 1e-6
        self.stop_loss = qty, stop
        self.take_profit = qty, target
        self.vars["entries"] = self.vars.get("entries", 0) + 1
        self._observe("open")

    def update_position(self):
        # Preserve the four-hour management clock despite the M1 observer.
        if int(self.time) % BAR == 0 and int(self.time) - int(self.position.opened_at) >= 12 * BAR:
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        now = int(self.time)
        active = self.vars.setdefault("active_months", set())
        active.add(month_name(now-1))
        # At a month boundary, retain both the held interval and any fee-only
        # execution month. Terminal liquidation belongs to the final interval.
        if now < self.FINISH:
            active.add(month_name(now))
        self.vars["last_exit_at"] = now
        self._observe("close")
        if now >= self.FINISH and self.vars.get("emitted"):
            self._emit("FINAL")

    def _emit(self, stage):
        summary = monthly_summary(self.vars["boundaries"], self.vars.get("active_months", set()))
        # Emit rows at the end, so one bounded log page can retrieve all months.
        for item in summary.pop("months"):
            self._log("R11_MONTH", dict(stage=stage, **item))
        summary.update(stage=stage, equity=self.vars["last_equity"],
                       dd_m1_events=self.vars.get("dd", 0),
                       minute_marks=self.vars.get("minute_marks", 0),
                       sequence=self.vars.get("sequence", 0),
                       signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
                       invalid_windows=self.vars.get("invalid_windows", 0))
        self._log("R11_SUMMARY", summary)

    def before_terminate(self):
        self._observe("terminal")
        self.vars["emitted"] = True
        self._emit("PRETERMINAL")
```

### strategies/BtcResearchR10Base4h/__init__.py

SHA256 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9; 8100 caracteres. Fuente completa recibida mediante read_strategy.

```python
import json
import math

import numpy as np
from jesse.strategies import Strategy

BAR = 14400000
DAY = 86400000


def closed_window(candles, now, count):
    """Use only consecutive, closed 4h bars; no synthetic gap repair."""
    rows = candles[candles[:, 0] + BAR <= now][-count:]
    if len(rows) != count or rows[-1, 0] != now - BAR:
        return None
    if not np.all(np.diff(rows[:, 0]) == BAR):
        return None
    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):
        return None
    if np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2])):
        return None
    if np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2])):
        return None
    return rows


def atr14(rows):
    previous = rows[-15:-1, 2]
    current = rows[-14:]
    tr = np.maximum(current[:, 3] - current[:, 4],
                    np.maximum(abs(current[:, 3] - previous), abs(current[:, 4] - previous)))
    value = float(np.mean(tr))
    return value if math.isfinite(value) and value > 0 else None


def breadth_state(closes):
    changes = np.diff(closes)
    positive = changes > 0
    negative = changes < 0
    if int(positive[-6:].sum()) >= 4 and int(positive[-24:].sum()) >= 16:
        return 1
    if int(negative[-6:].sum()) >= 4 and int(negative[-24:].sum()) >= 16:
        return -1
    return 0


def breadth_signal(rows):
    """Count sign persistence, not return magnitudes; consume only new states."""
    now_state = breadth_state(rows[-25:, 2])
    old_state = breadth_state(rows[-26:-1, 2])
    return now_state if now_state != old_state else 0


def funding_failure_signal(rows, now, events):
    """Observe a full post-payment bar; never know or collect the next payment."""
    event_start = now - BAR
    matching = []
    for event in events:
        raw = int(event["settled_at"])
        effective = raw // 60000 * 60000
        if effective == event_start and 0 <= raw - effective <= 1000:
            if int(event["available_at"]) <= now and int(event["available_at"]) > raw:
                matching.append(event)
    if len(matching) != 1:
        return 0, None
    event = matching[0]
    rate = float(event["rate_decimal"])
    if not math.isfinite(rate):
        return 0, None
    pre, post = rows[-2], rows[-1]
    if rate > 0 and pre[2] > pre[1] and post[2] < pre[1]:
        return -1, dict(settled_at=int(event["settled_at"]), available_at=int(event["available_at"]), rate=rate)
    if rate < 0 and pre[2] < pre[1] and post[2] > pre[1]:
        return 1, dict(settled_at=int(event["settled_at"]), available_at=int(event["available_at"]), rate=rate)
    return 0, None


def entry_plan(price, capital, margin, leverage, fee, direction, distance):
    stop = price - direction * distance
    values = (price, capital, margin, leverage, distance, stop)
    if direction not in (-1, 1) or not all(math.isfinite(v) and v > 0 for v in values):
        return None
    if not math.isfinite(fee) or fee < 0:
        return None
    unit_loss = distance + fee * (price + stop)
    # 2% includes both execution fees. The 90% margin ceiling retains the
    # historical reserve and does not increase the stop's monetary risk.
    risk_qty = 0.02 * capital / unit_loss
    margin_qty = 0.90 * margin * leverage / (price * (1 + fee * leverage))
    qty = math.floor(min(risk_qty, margin_qty) * 1e8) / 1e8
    if qty <= 0:
        return None
    assert qty * unit_loss <= 0.02 * capital + 1e-6
    return dict(qty=qty, price=price, capital=capital, distance=distance,
                stop=stop, risk_budget=0.02 * capital,
                planned_loss=qty * unit_loss, margin_capped=margin_qty < risk_qty)


class BtcResearchR10Base4h(Strategy):
    """R10 discovery harness: one BTC position, fixed risk and base costs only."""
    MODE = "abstract"
    START = 1602720000000
    FINISH = 1767225600000

    def _log(self, label, value):
        self.log(label + " " + json.dumps(value, separators=(",", ":"), allow_nan=False))

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT"
            assert self.leverage == 3
            assert abs(self.fee_rate - 0.00045) < 1e-12
            self.vars["checked"] = True
            self._log("R10_CONFIG", dict(mode=self.MODE, risk=0.02, aggregate=0.06,
                                        leverage=self.leverage, fee=self.fee_rate,
                                        margin_buffer=0.90, stop_atr=2, target_r=2, hold_hours=48))
        self.vars["direction"] = 0
        rows = closed_window(self.candles, now, 26)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            return
        if self.MODE == "BREADTH":
            direction = breadth_signal(rows)
            evidence = None
        else:
            assert self.MODE == "POST_FUNDING"
            events = self.get_funding_history(count=6)
            assert all(int(e["available_at"]) <= now for e in events)
            direction, evidence = funding_failure_signal(rows, now, events)
        if not direction or not self.START < now < self.FINISH:
            return
        # Signals are evaluated and consumed while occupied as well. No deferred
        # order or re-entry from a previously blocked funding/breadth event.
        self.vars["signals"] = self.vars.get("signals", 0) + 1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0) + 1
            return
        atr = atr14(rows)
        if atr is None:
            return
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        plan = entry_plan(float(self.price), capital, float(self.available_margin),
                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)
        if plan is None or float(self.price) + direction * 2 * plan["distance"] <= 0:
            return
        self.vars["direction"] = direction
        self.vars["plan"] = plan
        self.vars["evidence"] = evidence

    def should_long(self):
        return self.vars.get("direction") == 1

    def should_short(self):
        return self.vars.get("direction") == -1

    def go_long(self):
        plan = self.vars["plan"]
        self.buy = plan["qty"], self.price

    def go_short(self):
        plan = self.vars["plan"]
        self.sell = plan["qty"], self.price

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        distance = plan["distance"]
        stop = entry - direction * distance
        target = entry + direction * 2 * distance
        assert qty * (distance + self.fee_rate * (entry + stop)) <= plan["risk_budget"] + 1e-6
        self.stop_loss = qty, stop
        self.take_profit = qty, target
        self.vars["entries"] = self.vars.get("entries", 0) + 1
        self._log("R10_ENTRY", dict(time=int(self.time), direction=direction, entry=entry,
                                   qty=qty, stop=stop, target=target, plan=plan,
                                   evidence=self.vars.get("evidence")))

    def update_position(self):
        # No ratchet, discretionary exit or same-close reversal. Funding applies
        # continuously to actual held quantity, independently of signal inputs.
        if int(self.time) - int(self.position.opened_at) >= 12 * BAR:
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        self.vars["last_exit_at"] = int(self.time)

    def before_terminate(self):
        self._log("R10_COUNTERS", dict(signals=self.vars.get("signals", 0),
                                     occupied=self.vars.get("occupied", 0),
                                     entries=self.vars.get("entries", 0),
                                     invalid_windows=self.vars.get("invalid_windows", 0)))
```

### strategies/BtcResearchR16LegacyBase1m/__init__.py

SHA256 56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542; 14948 caracteres. Fuente completa recibida mediante read_strategy.

```python
import math
import numpy as np
import jesse.indicators as ta

from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR

# Frozen legacy recipe values, not optimizer ranges. The 10bp reserve sizes
# conservatively; it is never charged as cash or simulated execution friction.
HP = dict(donchian_len=26, ema_fast=20, ema_slow=80, adx_min=26,
          stop_atr=2.0, trail_atr=4.2, be_r=2.25)
RESERVE = .001
LOT = .001


def legacy_history(candles, now):
    """Keep exposed closed history; cross-route seed parity needs framework audit."""
    rows = candles[candles[:, 0]+BAR <= now]
    if len(rows) < 14 or rows[-1, 0] != now-BAR:
        return None
    if (not np.all(np.diff(rows[:, 0]) == BAR)
            or not np.all(np.isfinite(rows[:, :5]))
            or not np.all(rows[:, 1:5] > 0)
            or np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2]))
            or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2]))):
        return None
    return rows


def legacy_long(c):
    if len(c) < 100:
        return None
    price = float(c[-1, 2])
    fast = float(ta.ema(c, period=20))
    slow = ta.ema(c, period=80, sequential=True)
    atr, adx, rsi = float(ta.atr(c)), float(ta.adx(c)), float(ta.rsi(c))
    entry = float(np.max(c[-27:-1, 3]))
    if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):
        return None
    if not (atr > 0 and entry < price <= entry+atr and price > slow[-1]
            and fast > slow[-1] > slow[-5] and adx >= 26
            and 52 <= rsi <= 76 and c[-1, 3]-c[-1, 4] <= 3*atr):
        return None
    distance = 2*atr
    if not 0 < distance < entry:
        return None
    return dict(origin="LONG_RUNNER", direction=1, entry=entry,
                distance=distance, target_distance=None, hold_hours=None,
                order_kind="LIMIT")


def legacy_short(c):
    if len(c) < 140:
        return None
    price = float(c[-1, 2])
    macro = ta.ema(c, period=120, sequential=True)
    fast, atr, rsi = float(ta.ema(c, period=20)), float(ta.atr(c)), float(ta.rsi(c, period=3))
    if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, rsi)):
        return None
    if not (atr > 0 and macro[-1] > macro[-10] and price > macro[-1]-atr and rsi <= 20):
        return None
    entry = min(float(c[-1, 4]), price-.25*atr)
    distance = fast-entry
    if not (atr <= distance <= 3*atr and distance >= 6*.00045*entry):
        return None
    return dict(origin="CORE_SHORT", direction=-1, entry=entry,
                distance=distance, target_distance=1.5*atr, hold_hours=72,
                order_kind="STOP")


def legacy_supplement(c, mode, previous):
    """Consume setup before ATR/geometry/account tests, as in each frozen parent."""
    assert mode in ("K1001", "N204")
    w = c[-14:]
    if (len(w) < 14 or not np.all(np.isfinite(w))
            or not np.all(w[:, 1:] > 0) or not np.all(w[:, 3] >= w[:, 4])):
        return None, False
    s, t, window = c[-2], c[-1], c[-13:-1]
    spans = window[:, 3]-window[:, 4]
    q = np.divide(window[:, 5]*(2*window[:, 2]-window[:, 3]-window[:, 4]),
                  spans, out=np.zeros(12), where=spans > 0)
    cohort = window[q > 0]
    vwap = (float(np.sum(cohort[:, 5]*np.mean(cohort[:, [3, 4, 2]], axis=1))
                  / np.sum(cohort[:, 5])) if len(cohort) else float("nan"))
    setup = bool(s[2] > c[-14, 2] and np.sum(q) < 0
                 and s[2] >= vwap and t[2] < t[1] and t[2] < vwap)
    if mode == "K1001" and setup:
        changes = c[-13:-1, 2]-c[-14:-2, 2]
        path = float(np.sum(np.abs(changes)))
        efficiency = float(s[2]-c[-14, 2])/path if path > 0 else float("nan")
        setup = bool(path > 0 and 0 < efficiency <= 1/3)
    if not setup or previous:
        return None, setup
    atr = float(ta.atr(c))
    if not math.isfinite(atr) or atr <= 0:
        return None, setup
    distance = float(max(s[3], t[3])+.25*atr-t[2])
    if not atr <= distance <= 3*atr:
        return None, setup
    entry = float(min(s[4], t[4])) if mode == "K1001" else float(t[2])
    if mode == "K1001" and not (math.isfinite(entry) and entry > 2*distance and entry < t[2]):
        return None, setup
    if not (math.isfinite(entry) and math.isfinite(distance) and 0 < distance < entry):
        return None, setup
    return dict(origin="SUPPLEMENT", direction=-1, entry=entry,
                distance=distance, target_distance=2*distance, hold_hours=48,
                order_kind="STOP" if mode == "K1001" else "MARKET",
                anchor=vwap), setup


def legacy_plan(event, capital, margin, leverage, fee):
    """BTC100%; preserve reserve/lot, with the common 90%-margin fee buffer."""
    entry, distance, direction = event["entry"], event["distance"], event["direction"]
    stop = entry-direction*distance
    if (direction not in (-1, 1)
            or not all(math.isfinite(v) and v > 0 for v in
                       (entry, distance, stop, capital, margin, leverage))
            or not math.isfinite(fee) or fee < 0):
        return None
    unit = distance+fee*(entry+stop)+RESERVE*entry
    budget = .02*capital
    risk_qty = budget/unit
    gross_qty = 4.4*capital/entry  # Legacy ceiling; 3x margin prevents 4.4x exposure.
    margin_qty = .90*margin*leverage/(entry*(1+fee*leverage))
    qty = math.floor(min(risk_qty, gross_qty, margin_qty)/LOT)*LOT
    if qty <= 0:
        return None
    assert qty*unit <= budget+1e-6
    return dict(event, qty=qty, risk_budget=budget, planned_loss=qty*unit,
                planned_stop_fees=qty*(distance+fee*(entry+stop)),
                margin_limited=margin_qty < risk_qty,
                gross_limited=gross_qty < risk_qty,
                reserve=RESERVE)


class BtcResearchR16LegacyBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def _ledger(self):
        return self.vars.setdefault("legacy_ledger", {
            name: dict(fills=0, closes=0, net=0.0)
            for name in ("LONG_RUNNER", "CORE_SHORT", "SUPPLEMENT")})

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("K1001", "N204")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        # Advance the price machine once, independently of occupancy. Actual
        # framework cancellation may re-enter should_* in this same4h cycle.
        self.vars["decision_at"] = now
        rows = legacy_history(self.get_candles(self.exchange, self.symbol, "4h"), now)
        self.vars["legacy_rows"] = rows
        if rows is None:
            self.vars["previous_setup"] = False
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        self.vars["history_min"] = min(self.vars.get("history_min", len(rows)), len(rows))
        self.vars["history_max"] = max(self.vars.get("history_max", len(rows)), len(rows))
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        event, setup = legacy_supplement(rows, self.MODE, self.vars.get("previous_setup", False))
        self.vars["previous_setup"] = setup
        self.vars["supplement_event"] = event
        self.vars["supplement_events"] = self.vars.get("supplement_events", 0)+int(event is not None)
        if self.is_open or self.entry_orders:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1

    def _prepare_entry(self):
        """Memoize after broker cancellation releases margin; preserve one plan."""
        now = int(self.time)
        if (now % BAR or self.vars.get("decision_at") != now
                or self.is_open or self.entry_orders
                or self.vars.get("last_exit_at") == now
                or not self.START < now < self.FINISH):
            return 0
        if self.vars.get("prepared_at") == now:
            return self.vars.get("direction", 0)
        self.vars["prepared_at"] = now
        rows = self.vars.get("legacy_rows")
        if rows is None:
            return 0
        # Priority includes account eligibility: if a higher recipe cannot size,
        # the next original recipe is considered, exactly as the frozen parents.
        for candidate in (legacy_long(rows), legacy_short(rows),
                          self.vars.get("supplement_event")):
            if candidate is None:
                continue
            plan = legacy_plan(candidate, max(0.0, float(self.balance)),
                               float(self.available_margin), float(self.leverage),
                               float(self.fee_rate))
            if plan is not None:
                self.vars["plan"] = dict(plan, signal_at=now, expiry=now+BAR)
                self.vars["direction"] = plan["direction"]
                self.vars["signals"] = self.vars.get("signals", 0)+1
                return plan["direction"]
        return 0

    def should_long(self):
        return self._prepare_entry() == 1

    def should_short(self):
        return self._prepare_entry() == -1

    def _submit(self, direction):
        plan = self.vars["plan"]
        assert self.vars.get("submitted_at") != int(self.time), "P_DUPLICATE_SUBMISSION"
        assert self.vars.get("direction") == direction
        assert int(self.time) == plan["signal_at"] and not self.is_open and not self.entry_orders
        self.vars["submitted_at"] = int(self.time)
        self.vars["pending_plan"] = dict(plan)
        if direction == 1:
            self.buy = plan["qty"], plan["entry"]
        else:
            self.sell = plan["qty"], plan["entry"]

    def go_long(self):
        self._submit(1)

    def go_short(self):
        self._submit(-1)

    def should_cancel_entry(self):
        plan = self.vars.get("pending_plan")
        assert plan is not None, "P_PENDING_WITHOUT_PLAN"
        due = int(self.time) % BAR == 0 and int(self.time) >= plan["expiry"]
        if due:
            self.vars["pending_plan"] = None
            self.vars["cancellations"] = self.vars.get("cancellations", 0)+1
        return due

    def on_open_position(self, order):
        plan = self.vars["pending_plan"]
        assert plan is not None and self.vars.get("position_plan") is None
        now = int(self.time)
        assert plan["signal_at"] <= now <= plan["expiry"], "P_FILL_OUTSIDE_ORDER_LIFE"
        assert plan["signal_at"] <= int(self.position.opened_at) <= plan["expiry"]
        direction = 1 if self.is_long else -1
        assert direction == plan["direction"]
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        stop = entry-direction*plan["distance"]
        target = (entry+direction*plan["target_distance"]
                  if plan["target_distance"] is not None else None)
        loss = qty*(plan["distance"]+self.fee_rate*(entry+stop)+RESERVE*entry)
        assert math.isfinite(loss) and stop > 0 and (target is None or target > 0)
        assert loss <= plan["risk_budget"]+1e-6, "P_ACTUAL_FILL_RISK"
        assert abs(qty-plan["qty"]) < 1e-8, "P_UNEXPECTED_FILL_QUANTITY"
        # Frozen geometry is placed relative to actual fill, never order price.
        self.stop_loss = qty, stop
        if target is not None:
            self.take_profit = qty, target
        self.vars["position_plan"] = dict(plan, actual_entry=entry, actual_loss=loss,
                                          filled_at=int(self.position.opened_at))
        self.vars["pending_plan"] = None
        self.vars["best_close"] = entry
        self._ledger()[plan["origin"]]["fills"] += 1
        self.vars["entries"] = self.vars.get("entries", 0)+1
        self._observe("open")
        self._log("R16_LEGACY_OPEN", dict(mode=self.MODE, origin=plan["origin"], time=now,
            opened_at=int(self.position.opened_at), signal_at=plan["signal_at"],
            expiry=plan["expiry"], order_kind=plan["order_kind"],
            requested_entry=plan["entry"], actual_entry=entry, qty=qty,
            distance=plan["distance"], stop=stop, target=target,
            risk_budget=plan["risk_budget"], actual_loss=loss,
            planned_loss=plan["planned_loss"], planned_stop_fees=plan["planned_stop_fees"],
            margin_limited=plan["margin_limited"], reserve=RESERVE))

    def update_position(self):
        now = int(self.time)
        if now % BAR:
            return
        plan = self.vars["position_plan"]
        opened = plan["filled_at"]
        if plan["hold_hours"] is not None:
            if now-opened >= plan["hold_hours"]*3600000:
                self.liquidate()
            return
        # A close completed before the fill cannot improve its trailing stop.
        if now <= opened:
            return
        rows = self.vars.get("legacy_rows")
        if rows is None or self.vars.get("decision_at") != now:
            return
        atr = float(ta.atr(rows))
        if not math.isfinite(atr) or atr <= 0:
            return
        entry = plan["actual_entry"]
        self.vars["best_close"] = max(self.vars["best_close"], float(rows[-1, 2]))
        best_r = (self.vars["best_close"]-entry)/plan["distance"]
        mult = 4.2
        if best_r >= 8:
            mult *= .62
        elif best_r >= 5:
            mult *= .78
        stop = self.vars["best_close"]-mult*atr
        if best_r >= 2.25:
            stop = max(stop, entry*(1+2.5*self.fee_rate))
        if self.average_stop_loss < stop < self.price:
            self.stop_loss = abs(float(self.position.qty)), stop

    def on_close_position(self, order, closed_trade):
        plan = self.vars["position_plan"]
        row = self._ledger()[plan["origin"]]
        pnl = float(closed_trade.pnl)
        assert math.isfinite(pnl)
        row["closes"] += 1
        row["net"] += pnl
        self.vars["position_plan"] = None
        self.vars["pending_plan"] = None
        self._log("R16_LEGACY_CLOSE", dict(time=int(self.time), origin=plan["origin"], net=pnl))
        # R11 can emit FINAL here; source totals must already include this close.
        super().on_close_position(order, closed_trade)

    def _emit(self, stage):
        super()._emit(stage)
        rows = self._ledger()
        self._log("R16_LEGACY_STATS", dict(stage=stage, mode=self.MODE, sources=rows,
            fills=sum(r["fills"] for r in rows.values()),
            closes=sum(r["closes"] for r in rows.values()),
            net=sum(r["net"] for r in rows.values()),
            supplement_events=self.vars.get("supplement_events", 0),
            cancellations=self.vars.get("cancellations", 0),
            history_min=self.vars.get("history_min"), history_max=self.vars.get("history_max")))
```

### strategies/OrchLateralFailedRange4h/__init__.py

SHA256 622769223702154ffa01ea33c00bcbbbb0c7ce38e2d0f7acd9fd970d0c7a23e1; 7820 caracteres. Fuente completa recibida mediante read_strategy.

```python
import math
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

# New, unvalidated reversal logic starts below the user-approved maximum risk.
TRADE_RISK = 0.01
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4  # Buffer within configured isolated5x.
SLIPPAGE_RESERVE = 0.001  # Sizing only, not fill friction.

class OrchLateralFailedRange4h(Strategy):
    """Symmetric market-entry reversals of rejected range extensions.

    Exploratory economic hypothesis, not validated complementarity or live-ready.
    """

    def trading_hours(self):
        if self.symbol == 'SPY-USDT':
            # The fixed UTC whole-bar intersection excludes the US index daily
            # break in both DST regimes. This is an intentional common window,
            # not an assertion that the source's full session ends at 20:00 UTC.
            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}
        return None

    @property
    @cached
    def signal_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    def _entry_window(self) -> bool:
        if self.symbol != 'SPY-USDT':
            return True
        # Retain the reference's conservative SPY decision intersection: the
        # last eligible bar opens at12:00 and decides at16:00. These MARKET
        # entries do not rely on a pending order surviving a session boundary.
        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}
        return self.is_trading_hours and utils.is_in_trading_hours(
            self.closed_candle_open_time, window)

    def _ledger(self) -> dict:
        return self.shared_vars.setdefault('phase2_reservations', {})

    def _key(self) -> str:
        return self.exchange + ':' + self.symbol

    def _capital(self) -> float:
        # Floating gains do not enlarge the risk budget; floating losses reduce it.
        return max(0.0, min(float(self.balance), float(self.portfolio_value)))

    def _committed(self) -> tuple:
        risk, notional = 0.0, 0.0
        ledger = self._ledger()
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            strategy = route.strategy
            if strategy.is_open:
                qty = abs(float(strategy.position.qty))
                entry = float(strategy.position.entry_price)
                # Risk is measured from the current mark, so protected floating PnL
                # is not silently treated as free capacity for another trade.
                value = abs(float(strategy.position.value))
                mark = value / qty if qty else entry
                stop = float(strategy.average_stop_loss)
                distance = max(0.0, mark - stop) if strategy.is_long else max(0.0, stop - mark)
                risk += qty * (distance + mark * (self.fee_rate + SLIPPAGE_RESERVE))
                notional += value
            else:
                reservation = ledger.get(route.exchange + ':' + route.symbol)
                if reservation:
                    # Includes not-yet-filled STOP/LIMIT entries, not only open positions.
                    risk += reservation['risk']
                    notional += reservation['notional']
        return risk, notional


    def _signal(self) -> int:
        # Cache both decisions together so the second direction cannot overwrite a plan.
        if self.vars.get('signal_index') == self.index:
            return self.vars['signal_value']
        self.vars['signal_index'] = self.index
        self.vars['signal_value'] = 0
        if not self._entry_window():
            return 0
        c = self.signal_candles
        if len(c) < 100:
            return 0
        atr = float(ta.atr(c))
        close = c[-21:, 2]
        noise = float(np.sum(np.abs(np.diff(close))))
        efficiency = abs(float(close[-1] - close[0])) / noise if noise > 0 else 0.0
        # Twenty 4h observations represent several days of local auction context;
        # low efficiency distinguishes an oscillating auction from directional drift.
        if not math.isfinite(atr) or atr <= 0 or efficiency > 0.25:
            return 0
        lower = float(np.min(c[-21:-1, 4]))
        upper = float(np.max(c[-21:-1, 3]))
        middle = 0.5 * (lower + upper)
        side = 0
        if float(c[-1, 4]) < lower < self.price < middle:
            side = 1
            stop = float(c[-1, 4]) - 0.25 * atr
        elif float(c[-1, 3]) > upper > self.price > middle:
            side = -1
            stop = float(c[-1, 3]) + 0.25 * atr
        if side == 0:
            return 0
        entry = float(self.price)
        distance = abs(entry - stop)
        reward = side * (middle - entry)
        # Eligibility uses fixed BASE fees so effective-fee stresses leave signals fixed.
        # Minimum1R avoids a consumed reversal; ATR bounds reject tiny/noisy or huge stops.
        if not (atr <= distance <= 3 * atr and reward >= distance
                and reward >= 8 * 0.00045 * entry):
            return 0
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (entry + stop) + SLIPPAGE_RESERVE * entry
        # Equal route caps avoid comparing session ATR with continuous crypto ATR.
        route_count = sum(route.exchange == self.exchange for route in self.routes)
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP / max(1, route_count))
        qty = min(budget / unit_risk, room / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        # Research precision: native target-venue lot/min-notional remain unverified.
        step = 0.0001 if self.symbol == 'PAXG-USDT' else 0.001
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return 0
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry,
                             'target': middle, 'side': side}
        self.vars['signal_value'] = side
        return side

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], plan['entry']

    def go_short(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        # MARKET should fill immediately; never retain an unexpected entry.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:
        plan = self.vars['plan']
        entry = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        self.vars['opened_time'] = int(self.time)
        if self.is_long:
            self.stop_loss = qty, entry - plan['distance']
        else:
            self.stop_loss = qty, entry + plan['distance']
        self.take_profit = qty, plan['target']
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:
        # A failed reversal must resolve within two days. Exits remain active
        # outside entry hours; missing SPY quotes can postpone actual liquidation.
        if self.time - self.vars['opened_time'] >= 48 * 60 * 60 * 1000:
            self.liquidate()

    def on_close_position(self, order, closed_trade) -> None:
        self._ledger().pop(self._key(), None)
```

### strategies/AngleCombinedBtcAcceptance4h/__init__.py

SHA256 8e41a80a82180a8ad2193b6105bbd2173008e76e89ac4318e9cf774511148ae4; 16790 caracteres. Fuente completa recibida mediante read_strategy.

```python
import math
from datetime import datetime, timezone
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta
import jesse.helpers as jh

# User-approved research limits; risk is not an optimization parameter.
TRADE_RISK = 0.03
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.
SLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.


class AngleCombinedBtcAcceptance4h(Strategy):
    """Baseline clone; only BTC shorts add a closed-M1 lower-third occupancy gate.

    Shared risk and margin reservations; exploratory research, not approved live.
    SPY uses a session-filtered SPX CFD proxy; holidays and native parity remain
    unverified. Parameter-neighbour variants are sensitivity controls, not winners.
    """


    def _acceptance_counts(self):
        return self.vars.setdefault('btc_acceptance_counts', {
            'year': None, 'annual': {}, 'total': {},
        })

    def _acceptance_bump(self, key):
        counts = self._acceptance_counts()
        for bucket in ('annual', 'total'):
            counts[bucket][key] = counts[bucket].get(key, 0) + 1

    def _acceptance_log(self, label, counts):
        # Jesse helpers retain the standard timestamped diagnostic format.
        jh.debug('ANGLE_BTC_ACCEPTANCE ' + label + ' ' + repr(counts))

    def before(self):
        if self.symbol != 'BTC-USDT':
            return
        assert self.timeframe == '4h', 'ACCEPTANCE_REQUIRES_BTC_4H'
        counts = self._acceptance_counts()
        year = datetime.fromtimestamp(self.time / 1000, timezone.utc).year
        if counts['year'] is not None and year != counts['year']:
            self._acceptance_log('year_' + str(counts['year']), counts['annual'])
            counts['annual'] = {}
        counts['year'] = year

    def _accepted_lower_third(self, candle):
        """Check observed time spent low; this is not an order-flow measure."""
        self._acceptance_bump('baseline_structure_candidates')
        minutes = self.get_candles(self.exchange, self.symbol, '1m')
        if len(minutes) < 240:
            self._acceptance_bump('invalid_m1_coverage')
            return False
        minutes = minutes[-240:]
        start = int(candle[0])
        expected = start + np.arange(240, dtype=np.int64) * 60000
        # The complete last CLOSED four-hour bar only; never fill data gaps.
        if (start + 4 * 60 * 60 * 1000 != int(self.time)
                or not np.array_equal(minutes[:, 0].astype(np.int64), expected)
                or not np.all(minutes[:, 0] < self.time)
                or not np.isfinite(minutes[:, :5]).all()
                or np.any(minutes[:, 1:5] <= 0)):
            self._acceptance_bump('invalid_m1_coverage')
            return False
        self._acceptance_bump('valid_m1_coverage')
        aggregate = np.array([minutes[-1, 2], np.max(minutes[:, 3]), np.min(minutes[:, 4])])
        # Numerical equality tolerances accommodate float representation only;
        # they are not a trading threshold or permission for a different bar.
        if not np.allclose(aggregate, candle[[2, 3, 4]], rtol=1e-10, atol=1e-8):
            self._acceptance_bump('invalid_4h_parity')
            return False
        self._acceptance_bump('valid_4h_parity')
        low, high = float(candle[4]), float(candle[3])
        if high <= low:
            self._acceptance_bump('zero_range')
            return False
        # Natural ex-ante partitions: lower price third, at least half the time.
        # The final 4h extrema are fully observed now, not known earlier intrabar.
        threshold = low + (high - low) / 3
        occupied = int(np.count_nonzero(minutes[:, 2] <= threshold))
        accepted = occupied >= 120
        self._acceptance_bump('gate_accepted' if accepted else 'gate_rejected')
        return accepted

    def before_terminate(self):
        if self.symbol != 'BTC-USDT':
            return
        counts = self._acceptance_counts()
        self._acceptance_log('year_' + str(counts['year']), counts['annual'])
        self._acceptance_log('final_cumulative', counts['total'])
        # A wholly inaccessible minute window must be a technical failure,
        # never passed off as an economically successful zero-trade filter.
        if counts['total'].get('baseline_structure_candidates', 0) > 0:
            assert counts['total'].get('valid_4h_parity', 0) > 0, 'ACCEPTANCE_NO_VALID_M1_WINDOWS'

    def hyperparameters(self) -> list:
        return [
            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},
            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},
            {'name': 'ema_slow', 'type': int, 'min': 80, 'max': 140, 'default': 80},
            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},
            {'name': 'stop_atr', 'type': float, 'min': 1.6, 'max': 3.0, 'default': 2.0},
            {'name': 'trail_atr', 'type': float, 'min': 3.0, 'max': 5.0, 'default': 4.2},
            {'name': 'be_r', 'type': float, 'min': 1.75, 'max': 3.0, 'default': 2.25},
        ]

    def trading_hours(self):
        if self.symbol == 'SPY-USDT':
            # The fixed UTC whole-bar intersection excludes the US index daily
            # break in both DST regimes. This is an intentional common window,
            # not an assertion that the source's full session ends at 20:00 UTC.
            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}
        return None

    @property
    @cached
    def signal_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    def _entry_window(self) -> bool:
        if self.symbol != 'SPY-USDT':
            return True
        # A closed bar opening at 12:00 triggers at 16:00. Its order expires
        # at 20:00, before the excluded 20:00-24:00 bucket. A 16:00-open bar
        # must not arm a new order at 20:00. Pending orders still cancel then.
        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}
        return self.is_trading_hours and utils.is_in_trading_hours(
            self.closed_candle_open_time, window)

    def _ledger(self) -> dict:
        return self.shared_vars.setdefault('phase2_reservations', {})

    def _key(self) -> str:
        return self.exchange + ':' + self.symbol

    def _capital(self) -> float:
        # Floating gains do not enlarge the risk budget; floating losses reduce it.
        return max(0.0, min(float(self.balance), float(self.portfolio_value)))

    def _committed(self) -> tuple:
        risk, notional = 0.0, 0.0
        ledger = self._ledger()
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            strategy = route.strategy
            if strategy.is_open:
                qty = abs(float(strategy.position.qty))
                entry = float(strategy.position.entry_price)
                # Risk is measured from the current mark, so protected floating PnL
                # is not silently treated as free capacity for another trade.
                value = abs(float(strategy.position.value))
                mark = value / qty if qty else entry
                stop = float(strategy.average_stop_loss)
                distance = max(0.0, mark - stop) if strategy.is_long else max(0.0, stop - mark)
                risk += qty * (distance + mark * (self.fee_rate + SLIPPAGE_RESERVE))
                notional += value
            else:
                reservation = ledger.get(route.exchange + ':' + route.symbol)
                if reservation:
                    # Includes not-yet-filled STOP/LIMIT entries, not only open positions.
                    risk += reservation['risk']
                    notional += reservation['notional']
        return risk, notional

    def _volatility_share(self) -> float:
        """Reserve a common gross-exposure budget using inverse ATR fractions.

        All configured assets receive an ex-ante share, even while their signal
        is idle. This prevents the first route from consuming all shared margin.
        It is a capital-efficiency tradeoff to test, not an optimal allocation.
        """
        weights = {}
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            c = utils.filter_candles_by_hours(route.strategy.candles, route.strategy.trading_hours())
            if len(c) < int(self.hp['ema_slow']) + 20:
                return 0.0
            atr = float(ta.atr(c))
            price = float(c[-1, 2])
            if not math.isfinite(atr) or atr <= 0 or price <= 0:
                return 0.0
            # Stops use a common ATR multiple. Equal risk therefore needs
            # notional proportional to price/ATR before gross-leverage scaling.
            weights[route.symbol] = price / atr
        return weights.get(self.symbol, 0.0) / sum(weights.values()) if weights else 0.0

    def _plan(self) -> bool:
        if self.symbol not in ('BTC-USDT', 'PAXG-USDT', 'SPY-USDT') or not self._entry_window():
            return False
        c = self.signal_candles
        n = int(self.hp['donchian_len'])
        slow_n = int(self.hp['ema_slow'])
        if len(c) < max(slow_n + 20, n):
            return False
        fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))
        slow = ta.ema(c, period=slow_n, sequential=True)
        atr = float(ta.atr(c))
        adx = float(ta.adx(c))
        rsi = float(ta.rsi(c))
        # The closed bar has broken the PRIOR channel. A passive LIMIT at that
        # boundary can fill only on a future retest within one 4h order lifetime.
        entry = float(np.max(c[-n-1:-1, 3]))
        if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):
            return False
        if not (atr > 0 and entry < self.price <= entry + atr and self.price > slow[-1]
                and fast > slow[-1] > slow[-5] and adx >= self.hp['adx_min']
                and 52 <= rsi <= 76 and self.high - self.low <= 3 * atr):
            return False
        distance = float(self.hp['stop_atr']) * atr
        if not 0 < distance < entry:
            return False
        capital = self._capital()
        committed_risk, committed_notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - committed_risk))
        # Fees at both planned entry and stop, plus an explicit adverse-fill reserve.
        unit_risk = distance + self.fee_rate * (entry + entry - distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - committed_notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        # Historical research precision only. Native symbol lot/min-notional
        # constraints must be verified before any live use.
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {
            'qty': qty, 'entry': entry, 'distance': distance,
            'risk': qty * unit_risk, 'notional': qty * entry,
        }
        return True

    def _signal(self) -> int:
        # Compute exactly one plan per bar, with long priority. Checking
        # should_short after go_long must never overwrite a queued long plan.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            self.vars['signal_value'] = 1 if self._plan() else (-1 if self._short_plan() else 0)
        return self.vars['signal_value']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], plan['entry']

    def _short_plan(self) -> bool:
        """Test selloff continuation instead of buying an oversold dip.

        A rising slow regime can still suffer a fast liquidation leg. This
        exploratory hypothesis came from the failed long mean-reversion sleeve;
        it is development evidence, not an independent validation.
        """
        if self.symbol != 'BTC-USDT' or not self._entry_window():
            return False
        c = self.signal_candles
        if len(c) < 140:
            return False
        macro = ta.ema(c, period=120, sequential=True)
        fast = float(ta.ema(c, period=20))
        atr = float(ta.atr(c))
        quick_rsi = float(ta.rsi(c, period=3))
        if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, quick_rsi)):
            return False
        if not (atr > 0 and macro[-1] > macro[-10]
                and self.price > macro[-1] - atr and quick_rsi <= 20):
            return False
        entry = min(float(c[-1, 4]), self.price - 0.25 * atr)
        distance = fast - entry
        if not (atr <= distance <= 3 * atr and distance >= 6 * self.fee_rate * entry):
            return False
        if not self._accepted_lower_third(c[-1]):
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry + distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        qty = min(budget / unit_risk, room / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry,
                             'target_distance': 1.5 * atr}
        return True

    def go_short(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.
        # Jesse processes cancellation before evaluating the next route.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        self.vars['initial_distance'] = distance
        # An intrabar fill must not inherit highs/closes from before its entry.
        self.vars['best_close'] = entry
        if self.is_short:
            self._acceptance_bump('short_positions_filled')
            self.vars['opened_time'] = int(self.time)
            self.stop_loss = abs(self.position.qty), entry + distance
            self.take_profit = abs(self.position.qty), entry - self.vars['plan']['target_distance']
        else:
            self.stop_loss = abs(self.position.qty), entry - distance
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:
        if self.is_short:
            if self.time - self.vars['opened_time'] >= 72 * 60 * 60 * 1000:
                self.liquidate()
            return
        history = self.signal_candles
        atr = float(ta.atr(history))
        if not math.isfinite(atr) or atr <= 0:
            return
        entry = float(self.position.entry_price)
        distance = self.vars['initial_distance']
        self.vars['best_close'] = max(self.vars['best_close'], float(history[-1, 2]))
        best_r = (self.vars['best_close'] - entry) / distance
        mult = float(self.hp['trail_atr'])
        # Inherited late-trend tightening; retained as a controlled baseline choice.
        if best_r >= 8:
            mult *= 0.62
        elif best_r >= 5:
            mult *= 0.78
        stop = self.vars['best_close'] - mult * atr
        if best_r >= float(self.hp['be_r']):
            stop = max(stop, entry * (1 + 2.5 * self.fee_rate))
        if self.average_stop_loss < stop < self.price:
            self.stop_loss = abs(self.position.qty), stop

    def on_close_position(self, order, closed_trade) -> None:
        self._ledger().pop(self._key(), None)
```

### strategies/AngleCombinedBtcReclaim1m/__init__.py

SHA256 cd24c8cffcf57bb2436a05205ab123b3482df8e8832206cb582fffbde8d90ae1; 22695 caracteres. Fuente completa recibida mediante read_strategy.

```python
import math
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

# User-approved research limits; risk is not an optimization parameter.
TRADE_RISK = 0.03
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.
SLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.
BAR_MS = 4 * 60 * 60 * 1000  # Preserve the baseline decision and order-lifetime clock.


class AngleCombinedBtcReclaim1m(Strategy):
    """Combined baseline with causal BTC long touch-and-reclaim MARKET execution.

    Shared risk and margin reservations; exploratory research, not approved live.
    SPY uses a session-filtered SPX CFD proxy; holidays and native parity remain
    unverified. Parameter-neighbour variants are sensitivity controls, not winners.
    """

    def hyperparameters(self) -> list:
        return [
            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},
            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},
            {'name': 'ema_slow', 'type': int, 'min': 80, 'max': 140, 'default': 80},
            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},
            {'name': 'stop_atr', 'type': float, 'min': 1.6, 'max': 3.0, 'default': 2.0},
            {'name': 'trail_atr', 'type': float, 'min': 3.0, 'max': 5.0, 'default': 4.2},
            {'name': 'be_r', 'type': float, 'min': 1.75, 'max': 3.0, 'default': 2.25},
        ]

    def trading_hours(self):
        if self.symbol == 'SPY-USDT':
            # The fixed UTC whole-bar intersection excludes the US index daily
            # break in both DST regimes. This is an intentional common window,
            # not an assertion that the source's full session ends at 20:00 UTC.
            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}
        return None

    def _closed_btc_4h(self, strategy):
        # Auxiliary snapshots may contain a forming 4h row. Retain every closed
        # historical row, as the original store does; never truncate to warmup.
        raw = strategy.get_candles(strategy.exchange, strategy.symbol, '4h')
        return raw[raw[:, 0] + BAR_MS <= self.time]

    @property
    @cached
    def signal_candles(self):
        if self.symbol == 'BTC-USDT':
            return self._closed_btc_4h(self)
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    def _entry_window(self) -> bool:
        if self.symbol == 'BTC-USDT':
            # The 1m route is an execution clock, not a new signal frequency.
            return self.time % BAR_MS == 0
        if self.symbol != 'SPY-USDT':
            return True
        # A closed bar opening at 12:00 triggers at 16:00. Its order expires
        # at 20:00, before the excluded 20:00-24:00 bucket. A 16:00-open bar
        # must not arm a new order at 20:00. Pending orders still cancel then.
        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}
        return self.is_trading_hours and utils.is_in_trading_hours(
            self.closed_candle_open_time, window)

    def _ledger(self) -> dict:
        return self.shared_vars.setdefault('phase2_reservations', {})

    def _key(self) -> str:
        return self.exchange + ':' + self.symbol

    def _capital(self) -> float:
        # Floating gains do not enlarge the risk budget; floating losses reduce it.
        return max(0.0, min(float(self.balance), float(self.portfolio_value)))

    def _committed(self) -> tuple:
        risk, notional = 0.0, 0.0
        ledger = self._ledger()
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            strategy = route.strategy
            if strategy.is_open:
                qty = abs(float(strategy.position.qty))
                entry = float(strategy.position.entry_price)
                # Risk is measured from the current mark, so protected floating PnL
                # is not silently treated as free capacity for another trade.
                value = abs(float(strategy.position.value))
                mark = value / qty if qty else entry
                stop = float(strategy.average_stop_loss)
                distance = max(0.0, mark - stop) if strategy.is_long else max(0.0, stop - mark)
                risk += qty * (distance + mark * (self.fee_rate + SLIPPAGE_RESERVE))
                notional += value
            else:
                reservation = ledger.get(route.exchange + ':' + route.symbol)
                if reservation:
                    # Includes not-yet-filled STOP/LIMIT entries, not only open positions.
                    risk += reservation['risk']
                    notional += reservation['notional']
        return risk, notional

    def _volatility_share(self) -> float:
        """Reserve a common gross-exposure budget using inverse ATR fractions.

        All configured assets receive an ex-ante share, even while their signal
        is idle. This prevents the first route from consuming all shared margin.
        It is a capital-efficiency tradeoff to test, not an optimal allocation.
        """
        weights = {}
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            if route.symbol == 'BTC-USDT':
                # Read raw auxiliary data at the caller's current clock. Another
                # route's @cached property can still belong to its previous step.
                c = self._closed_btc_4h(route.strategy)
            else:
                c = utils.filter_candles_by_hours(route.strategy.candles, route.strategy.trading_hours())
            if len(c) < int(self.hp['ema_slow']) + 20:
                return 0.0
            atr = float(ta.atr(c))
            price = float(c[-1, 2])
            if not math.isfinite(atr) or atr <= 0 or price <= 0:
                return 0.0
            # Stops use a common ATR multiple. Equal risk therefore needs
            # notional proportional to price/ATR before gross-leverage scaling.
            weights[route.symbol] = price / atr
        return weights.get(self.symbol, 0.0) / sum(weights.values()) if weights else 0.0

    def _plan(self) -> bool:
        if self.symbol not in ('BTC-USDT', 'PAXG-USDT', 'SPY-USDT') or not self._entry_window():
            return False
        c = self.signal_candles
        n = int(self.hp['donchian_len'])
        slow_n = int(self.hp['ema_slow'])
        if len(c) < max(slow_n + 20, n):
            return False
        fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))
        slow = ta.ema(c, period=slow_n, sequential=True)
        atr = float(ta.atr(c))
        adx = float(ta.adx(c))
        rsi = float(ta.rsi(c))
        # The closed bar has broken the PRIOR channel. A passive LIMIT at that
        # boundary can fill only on a future retest within one 4h order lifetime.
        entry = float(np.max(c[-n-1:-1, 3]))
        if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):
            return False
        # self.high/low refer to M1 on BTC; the baseline range test remains 4h.
        signal_range = (float(c[-1, 3]) - float(c[-1, 4])
                        if self.symbol == 'BTC-USDT' else self.high - self.low)
        if not (atr > 0 and entry < self.price <= entry + atr and self.price > slow[-1]
                and fast > slow[-1] > slow[-5] and adx >= self.hp['adx_min']
                and 52 <= rsi <= 76 and signal_range <= 3 * atr):
            return False
        distance = float(self.hp['stop_atr']) * atr
        if not 0 < distance < entry:
            return False
        capital = self._capital()
        committed_risk, committed_notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - committed_risk))
        # Fees at both planned entry and stop, plus an explicit adverse-fill reserve.
        unit_risk = distance + self.fee_rate * (entry + entry - distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - committed_notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        # Historical research precision only. Native symbol lot/min-notional
        # constraints must be verified before any live use.
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {
            'qty': qty, 'entry': entry, 'distance': distance,
            'risk': qty * unit_risk, 'notional': qty * entry,
        }
        return True

    def before(self) -> None:
        if self.symbol != 'BTC-USDT':
            return
        if self.timeframe != '1m':
            raise AssertionError('BTC reclaim execution requires its reviewed 1m trading route')
        armed = self.vars.get('reclaim_setup')
        if armed is None:
            return
        if self.is_open:
            raise AssertionError('A filled BTC long must release its reclaim setup')
        armed['ready'] = False
        if self.time >= armed['expiry']:
            self.vars.pop('reclaim_setup')
            self._ledger().pop(self._key(), None)
            # Original cancellation consumes this callback; do not arm another
            # 4h signal at exactly the old order's expiration boundary.
            self.vars['reclaim_expired_index'] = self.index
            return
        # This completed minute must belong to the period AFTER setup creation;
        # the setup's own 4h bar cannot retrospectively supply a touch.
        if (self.closed_candle_open_time < armed['setup_time']
                or self.time <= armed['setup_time']):
            return
        boundary = armed['plan']['entry']
        if armed['touch_close'] is None:
            if self.low <= boundary:
                armed['touch_close'] = int(self.time)
            return
        # A later M1 adds the preregistered persistence confirmation and latency;
        # same-minute low/close ordering alone would not require this delay.
        if self.time > armed['touch_close'] and self.price > boundary:
            armed['ready'] = True

    def _reclaim_quantity(self, armed) -> tuple:
        frozen = armed['plan']
        price = float(self.price)
        distance = frozen['distance']
        ledger = self._ledger()
        own = ledger.pop(self._key(), None)
        if own is None:
            raise AssertionError('An armed BTC setup must keep its reservation')
        try:
            # Callbacks are sequential. Excluding only this internal reservation
            # prevents double counting without freeing another route's capital.
            risk, notional = self._committed()
            capital = self._capital()
            budget = min(frozen['risk'], capital * TRADE_RISK,
                         max(0.0, capital * PORTFOLIO_RISK - risk))
            room = min(frozen['notional'],
                       max(0.0, capital * NOTIONAL_CAP - notional))
            margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
            if not math.isfinite(price) or not 0 < distance < price:
                return 0.0, 0.0
            unit_risk = distance + self.fee_rate * (2 * price - distance) + SLIPPAGE_RESERVE * price
            qty = min(frozen['qty'], budget / unit_risk, room / price, margin_room / price)
            # The original BTC research precision is retained. A smaller budget
            # can only reduce quantity; zero leaves the setup alive until expiry.
            qty = math.floor(qty / 0.001) * 0.001
            return qty, unit_risk
        finally:
            ledger[self._key()] = own

    def _signal(self) -> int:
        # Preserve the proven control verbatim on PAXG/SPY and on BTC shorts.
        # An armed BTC long owns priority until its fill or original 4h expiry.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            if self.symbol == 'BTC-USDT':
                self.vars.pop('reclaim_execution', None)
                armed = self.vars.get('reclaim_setup')
                if self.vars.get('reclaim_expired_index') == self.index:
                    self.vars['signal_value'] = 0
                elif armed is not None:
                    self.vars['signal_value'] = 0
                    if armed['ready']:
                        qty, unit_risk = self._reclaim_quantity(armed)
                        # Jesse requires should_long=True to result in an order.
                        # Zero size keeps the reservation and long priority, but
                        # never declares a signal whose go_long would be empty.
                        if qty > 0:
                            self.vars['reclaim_execution'] = {
                                'qty': qty, 'unit_risk': unit_risk,
                                'price': float(self.price), 'timestamp': int(self.time),
                                'index': self.index,
                            }
                            self.vars['signal_value'] = 1
                elif self.time % BAR_MS != 0:
                    self.vars['signal_value'] = 0
                else:
                    if not self.vars.get('clock_warmup_checked'):
                        if len(self.signal_candles) < 240:
                            raise AssertionError('BTC reclaim requires the proven 240 closed 4h warmup rows')
                        self.vars['clock_warmup_checked'] = True
                    if self._plan():
                        frozen = dict(self.vars['plan'])
                        self.vars['reclaim_setup'] = {
                            'plan': frozen, 'setup_time': int(self.time),
                            'expiry': int(self.time) + BAR_MS,
                            'touch_close': None, 'ready': False,
                        }
                        # No broker order exists yet, but other routes must see
                        # the same capital reservation as the original LIMIT.
                        self._ledger()[self._key()] = dict(frozen)
                        self.vars['signal_value'] = 0
                    else:
                        self.vars['signal_value'] = -1 if self._short_plan() else 0
            else:
                self.vars['signal_value'] = 1 if self._plan() else (-1 if self._short_plan() else 0)
        return self.vars['signal_value']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        if self.symbol == 'BTC-USDT':
            armed = self.vars['reclaim_setup']
            if not (armed['ready'] and self.time < armed['expiry']
                    and self.time > armed['touch_close']):
                raise AssertionError('BTC MARKET entry must follow a later reclaim before expiry')
            execution = self.vars.pop('reclaim_execution')
            if not (execution['qty'] > 0 and execution['unit_risk'] > 0
                    and execution['timestamp'] == int(self.time)
                    and execution['index'] == self.index
                    and execution['price'] == float(self.price)):
                raise AssertionError('BTC MARKET execution must consume a positive same-callback quote plan')
            qty, unit_risk = execution['qty'], execution['unit_risk']
            price = execution['price']
            frozen = armed['plan']
            self.vars['plan'] = {
                'qty': qty, 'entry': price, 'distance': frozen['distance'],
                'risk': qty * unit_risk, 'notional': qty * price,
            }
            self._ledger()[self._key()] = dict(self.vars['plan'])
            # Jesse treats an order at the current price as MARKET. The higher
            # reclaim close is paid explicitly, never the old channel boundary.
            self.buy = qty, price
            return
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], plan['entry']

    def _short_plan(self) -> bool:
        """Test selloff continuation instead of buying an oversold dip.

        A rising slow regime can still suffer a fast liquidation leg. This
        exploratory hypothesis came from the failed long mean-reversion sleeve;
        it is development evidence, not an independent validation.
        """
        if self.symbol != 'BTC-USDT' or not self._entry_window():
            return False
        c = self.signal_candles
        if len(c) < 140:
            return False
        macro = ta.ema(c, period=120, sequential=True)
        fast = float(ta.ema(c, period=20))
        atr = float(ta.atr(c))
        quick_rsi = float(ta.rsi(c, period=3))
        if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, quick_rsi)):
            return False
        if not (atr > 0 and macro[-1] > macro[-10]
                and self.price > macro[-1] - atr and quick_rsi <= 20):
            return False
        entry = min(float(c[-1, 4]), self.price - 0.25 * atr)
        distance = fast - entry
        if not (atr <= distance <= 3 * atr and distance >= 6 * self.fee_rate * entry):
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry + distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        qty = min(budget / unit_risk, room / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry,
                             'target_distance': 1.5 * atr}
        return True

    def go_short(self) -> None:
        plan = self.vars['plan']
        if self.symbol == 'BTC-USDT':
            self.vars['entry_deadline'] = int(self.time) + BAR_MS
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        if self.symbol == 'BTC-USDT':
            # Pending entries keep their risk/notional reservation for the full
            # original 4h lifetime, despite 1m cancellation callbacks.
            if self.time < self.vars['entry_deadline']:
                return False
        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.
        # Jesse processes cancellation before evaluating the next route.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:
        if self.symbol == 'BTC-USDT' and self.is_long:
            armed = self.vars.get('reclaim_setup')
            if armed is None:
                raise AssertionError('BTC long fill must originate from the reserved reclaim setup')
            frozen = armed['plan']
            fill = float(self.position.entry_price)
            qty = abs(float(self.position.qty))
            actual_risk = qty * (frozen['distance'] + self.fee_rate * (2 * fill - frozen['distance'])
                                 + SLIPPAGE_RESERVE * fill)
            # This is floating arithmetic tolerance, not an economic oversizing allowance.
            if (qty > frozen['qty'] + 1e-8 or qty * fill > frozen['notional'] + 1e-8
                    or actual_risk > frozen['risk'] + 1e-8):
                raise AssertionError('BTC reclaim fill exceeds a frozen setup ceiling')
            self.vars.pop('reclaim_setup')
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        self.vars['initial_distance'] = distance
        # An intrabar fill must not inherit highs/closes from before its entry.
        self.vars['best_close'] = entry
        if self.is_short:
            self.vars['opened_time'] = int(self.time)
            self.stop_loss = abs(self.position.qty), entry + distance
            self.take_profit = abs(self.position.qty), entry - self.vars['plan']['target_distance']
        else:
            self.stop_loss = abs(self.position.qty), entry - distance
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:
        if self.symbol == 'BTC-USDT' and self.time % BAR_MS != 0:
            # Protective broker orders remain active at M1; trailing and the
            # inherited 72h short time exit are evaluated only on the 4h clock.
            return
        if self.is_short:
            if self.time - self.vars['opened_time'] >= 72 * 60 * 60 * 1000:
                self.liquidate()
            return
        history = self.signal_candles
        atr = float(ta.atr(history))
        if not math.isfinite(atr) or atr <= 0:
            return
        entry = float(self.position.entry_price)
        distance = self.vars['initial_distance']
        self.vars['best_close'] = max(self.vars['best_close'], float(history[-1, 2]))
        best_r = (self.vars['best_close'] - entry) / distance
        mult = float(self.hp['trail_atr'])
        # Inherited late-trend tightening; retained as a controlled baseline choice.
        if best_r >= 8:
            mult *= 0.62
        elif best_r >= 5:
            mult *= 0.78
        stop = self.vars['best_close'] - mult * atr
        if best_r >= float(self.hp['be_r']):
            stop = max(stop, entry * (1 + 2.5 * self.fee_rate))
        if self.average_stop_loss < stop < self.price:
            self.stop_loss = abs(self.position.qty), stop

    def before_terminate(self) -> None:
        # Mirror cancellation of an unfilled broker order at simulation end:
        # release only the internal pending reservation, without a synthetic fill.
        if self.symbol == 'BTC-USDT' and self.vars.pop('reclaim_setup', None) is not None:
            self._ledger().pop(self._key(), None)

    def on_close_position(self, order, closed_trade) -> None:
        self._ledger().pop(self._key(), None)
```

### strategies/BTCNovelR901/__init__.py

SHA256 5c2b9f91b097adc57ef2c9a061fc567f497974e94c4643862a3ae4d44994233a; 23016 caracteres. Fuente completa recibida mediante read_strategy.

```python
import math
import json
import jesse.helpers as jh
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

# User-approved research limits; risk is not an optimization parameter.
TRADE_RISK = 0.01
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.
SLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.


class BTCNovelR901(Strategy):
    """Y901 frozen R8 creative experiment from N503; original routes retained.

    Shared risk and margin reservations; exploratory research, not approved live.
    SPY uses a session-filtered SPX CFD proxy; holidays and native parity remain
    unverified. Parameter-neighbour variants are sensitivity controls, not winners.
    """

    def hyperparameters(self) -> list:
        return [
            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},
            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},
            {'name': 'ema_slow', 'type': int, 'min': 80, 'max': 140, 'default': 80},
            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},
            {'name': 'stop_atr', 'type': float, 'min': 1.6, 'max': 3.0, 'default': 2.0},
            {'name': 'trail_atr', 'type': float, 'min': 3.0, 'max': 5.0, 'default': 4.2},
            {'name': 'be_r', 'type': float, 'min': 1.75, 'max': 3.0, 'default': 2.25},
        ]

    def trading_hours(self):
        if self.symbol == 'SPY-USDT':
            # The fixed UTC whole-bar intersection excludes the US index daily
            # break in both DST regimes. This is an intentional common window,
            # not an assertion that the source's full session ends at 20:00 UTC.
            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}
        return None

    @property
    @cached
    def signal_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    def _entry_window(self) -> bool:
        if self.symbol != 'SPY-USDT':
            return True
        # A closed bar opening at 12:00 triggers at 16:00. Its order expires
        # at 20:00, before the excluded 20:00-24:00 bucket. A 16:00-open bar
        # must not arm a new order at 20:00. Pending orders still cancel then.
        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}
        return self.is_trading_hours and utils.is_in_trading_hours(
            self.closed_candle_open_time, window)

    def _ledger(self) -> dict:
        return self.shared_vars.setdefault('phase2_reservations', {})

    def _key(self) -> str:
        return self.exchange + ':' + self.symbol

    def _capital(self) -> float:
        # Floating gains do not enlarge the risk budget; floating losses reduce it.
        return max(0.0, min(float(self.balance), float(self.portfolio_value)))

    def _committed(self) -> tuple:
        risk, notional = 0.0, 0.0
        ledger = self._ledger()
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            strategy = route.strategy
            if strategy.is_open:
                qty = abs(float(strategy.position.qty))
                entry = float(strategy.position.entry_price)
                # Risk is measured from the current mark, so protected floating PnL
                # is not silently treated as free capacity for another trade.
                value = abs(float(strategy.position.value))
                mark = value / qty if qty else entry
                stop = float(strategy.average_stop_loss)
                distance = max(0.0, mark - stop) if strategy.is_long else max(0.0, stop - mark)
                risk += qty * (distance + mark * (self.fee_rate + SLIPPAGE_RESERVE))
                notional += value
            else:
                reservation = ledger.get(route.exchange + ':' + route.symbol)
                if reservation:
                    # Includes not-yet-filled STOP/LIMIT entries, not only open positions.
                    risk += reservation['risk']
                    notional += reservation['notional']
        return risk, notional

    def _volatility_share(self) -> float:
        """Reserve a common gross-exposure budget using inverse ATR fractions.

        All configured assets receive an ex-ante share, even while their signal
        is idle. This prevents the first route from consuming all shared margin.
        It is a capital-efficiency tradeoff to test, not an optimal allocation.
        """
        weights = {}
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            c = utils.filter_candles_by_hours(route.strategy.candles, route.strategy.trading_hours())
            if len(c) < int(self.hp['ema_slow']) + 20:
                return 0.0
            atr = float(ta.atr(c))
            price = float(c[-1, 2])
            if not math.isfinite(atr) or atr <= 0 or price <= 0:
                return 0.0
            # Stops use a common ATR multiple. Equal risk therefore needs
            # notional proportional to price/ATR before gross-leverage scaling.
            weights[route.symbol] = price / atr
        return weights.get(self.symbol, 0.0) / sum(weights.values()) if weights else 0.0

    def _plan(self) -> bool:
        if self.symbol not in ('BTC-USDT', 'PAXG-USDT', 'SPY-USDT') or not self._entry_window():
            return False
        c = self.signal_candles
        n = int(self.hp['donchian_len'])
        slow_n = int(self.hp['ema_slow'])
        if len(c) < max(slow_n + 20, n):
            return False
        fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))
        slow = ta.ema(c, period=slow_n, sequential=True)
        atr = float(ta.atr(c))
        adx = float(ta.adx(c))
        rsi = float(ta.rsi(c))
        # The closed bar has broken the PRIOR channel. A passive LIMIT at that
        # boundary can fill only on a future retest within one 4h order lifetime.
        entry = float(np.max(c[-n-1:-1, 3]))
        if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):
            return False
        if not (atr > 0 and entry < self.price <= entry + atr and self.price > slow[-1]
                and fast > slow[-1] > slow[-5] and adx >= self.hp['adx_min']
                and 52 <= rsi <= 76 and self.high - self.low <= 3 * atr):
            return False
        distance = float(self.hp['stop_atr']) * atr
        if not 0 < distance < entry:
            return False
        capital = self._capital()
        committed_risk, committed_notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - committed_risk))
        # Fees at both planned entry and stop, plus an explicit adverse-fill reserve.
        unit_risk = distance + self.fee_rate * (entry + entry - distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - committed_notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        # Historical research precision only. Native symbol lot/min-notional
        # constraints must be verified before any live use.
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        self._record_capacity('long', capital, budget, unit_risk, entry,
                              room, margin_room, qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {
            'qty': qty, 'entry': entry, 'distance': distance,
            'risk': qty * unit_risk, 'notional': qty * entry,
        }
        return True

    def _signal(self) -> int:
        # Compute exactly one plan per bar, with long priority. Checking
        # should_short after go_long must never overwrite a queued long plan.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            if self._plan():
                signal = 1
            elif self._short_plan():
                signal = -1
            else:
                event = self.vars.get('explore_event')
                signal = (-1 if event and self._explore_size(event) else 0)
            self.vars['signal_value'] = signal
        return self.vars['signal_value']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], plan['entry']

    def _short_plan(self) -> bool:
        """Test selloff continuation instead of buying an oversold dip.

        A rising slow regime can still suffer a fast liquidation leg. This
        exploratory hypothesis came from the failed long mean-reversion sleeve;
        it is development evidence, not an independent validation.
        """
        if self.symbol != 'BTC-USDT' or not self._entry_window():
            return False
        c = self.signal_candles
        if len(c) < 140:
            return False
        macro = ta.ema(c, period=120, sequential=True)
        fast = float(ta.ema(c, period=20))
        atr = float(ta.atr(c))
        quick_rsi = float(ta.rsi(c, period=3))
        if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, quick_rsi)):
            return False
        if not (atr > 0 and macro[-1] > macro[-10]
                and self.price > macro[-1] - atr and quick_rsi <= 20):
            return False
        entry = min(float(c[-1, 4]), self.price - 0.25 * atr)
        distance = fast - entry
        if not (atr <= distance <= 3 * atr and distance >= 6 * self.fee_rate * entry):
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry + distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        qty = min(budget / unit_risk, room / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        self._record_capacity('short', capital, budget, unit_risk, entry,
                              room, max(0.0, float(self.leveraged_available_margin) * 0.90), qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry,
                             'target_distance': 1.5 * atr}
        return True

    def go_short(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.
        # Jesse processes cancellation before evaluating the next route.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:

        plan = self.vars['plan']
        self.vars['explore_kind'] = plan.get('kind')
        if self.vars['explore_kind']:
            # Geometry is frozen at signal; protection is relative to actual fill.
            entry = float(self.position.entry_price)
            distance = plan['distance']
            self.vars['initial_distance'] = distance
            self.vars['opened_time'] = int(self.time)
            self.vars['explore_deadline'] = int(self.time) + plan['hold_hours'] * 3600000
            qty = abs(float(self.position.qty))
            if self.is_long:
                self.stop_loss = qty, entry - distance
                self.take_profit = qty, entry + plan['target_distance']
            else:
                self.stop_loss = qty, entry + distance
                self.take_profit = qty, entry - plan['target_distance']
            self._ledger().pop(self._key(), None)
            audit = self.vars.setdefault('explore_audit', {})
            audit['fills'] = audit.get('fills', 0) + 1
            jh.debug('BTC_EXPLORE_FILL ' + json.dumps({
                'recipe': self.vars['explore_kind'], 'time': int(self.time),
                'side': 'long' if self.is_long else 'short',
                'entry': entry, 'qty': qty, 'distance': distance,
                'requested_entry': float(plan['novel_requested_entry']),
                'signal_anchor': float(plan['novel_anchor']),
                'target_distance': plan['target_distance'],
                'deadline': self.vars['explore_deadline']}, sort_keys=True))
            return
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        self.vars['initial_distance'] = distance
        # An intrabar fill must not inherit highs/closes from before its entry.
        self.vars['best_close'] = entry
        if self.is_short:
            self.vars['opened_time'] = int(self.time)
            self.stop_loss = abs(self.position.qty), entry + distance
            self.take_profit = abs(self.position.qty), entry - self.vars['plan']['target_distance']
        else:
            self.stop_loss = abs(self.position.qty), entry - distance
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:

        if self.vars.get('explore_kind'):
            # Only the first closed 4h decision at/after the fill-based deadline.
            if int(self.time) >= self.vars['explore_deadline']:
                self.liquidate()
            return
        if self.is_short:
            if self.time - self.vars['opened_time'] >= 72 * 60 * 60 * 1000:
                self.liquidate()
            return
        history = self.signal_candles
        atr = float(ta.atr(history))
        if not math.isfinite(atr) or atr <= 0:
            return
        entry = float(self.position.entry_price)
        distance = self.vars['initial_distance']
        self.vars['best_close'] = max(self.vars['best_close'], float(history[-1, 2]))
        best_r = (self.vars['best_close'] - entry) / distance
        mult = float(self.hp['trail_atr'])
        # Inherited late-trend tightening; retained as a controlled baseline choice.
        if best_r >= 8:
            mult *= 0.62
        elif best_r >= 5:
            mult *= 0.78
        stop = self.vars['best_close'] - mult * atr
        if best_r >= float(self.hp['be_r']):
            stop = max(stop, entry * (1 + 2.5 * self.fee_rate))
        if self.average_stop_loss < stop < self.price:
            self.stop_loss = abs(self.position.qty), stop

    def on_close_position(self, order, closed_trade) -> None:
        if self.vars.get('explore_kind'):
            audit = self.vars.setdefault('explore_audit', {})
            audit['closes'] = audit.get('closes', 0) + 1
        self.vars['explore_kind'] = None
        self._ledger().pop(self._key(), None)

    def _record_capacity(self, side, capital, budget, unit_risk, entry,
                         room, margin_room, raw_qty, step) -> None:
        """Observe existing sizing only; never gates signals or changes quantities.

        Counts plans reaching sizing while flat and without a pending entry.
        It does not infer trades that would have filled or signals while occupied.
        Quantity tolerances below classify numerical ties, not trading thresholds.
        """
        audit = self.vars.setdefault('portfolio_capacity_audit', {})
        row = audit.setdefault(side, {'eligible_sizing_attempts': 0,
                                     'risk_budget_limited': 0,
                                     'notional_or_weight_limited': 0,
                                     'margin_limited': 0,
                                     'sized_below_trade_target': 0,
                                     'capacity_zero': 0,
                                     'zero_after_lot_rounding': 0})
        row['eligible_sizing_attempts'] += 1
        target_qty = capital * TRADE_RISK / unit_risk
        tolerance = max(1e-8, abs(target_qty) * 1e-10)
        row['risk_budget_limited'] += int(budget / unit_risk + tolerance < target_qty)
        row['notional_or_weight_limited'] += int(room / entry + tolerance < target_qty)
        row['margin_limited'] += int(margin_room / entry + tolerance < target_qty)
        row['sized_below_trade_target'] += int(raw_qty + tolerance < target_qty)
        row['capacity_zero'] += int(raw_qty <= 0 < target_qty)
        row['zero_after_lot_rounding'] += int(math.floor(raw_qty / step) * step <= 0 < raw_qty)

    def terminate(self) -> None:
        jh.debug('BTC_NOVEL ' + json.dumps({'recipe': 'Y901',
            'counts': self.vars.get('novel_audit', {})}, sort_keys=True))
        jh.debug('BTC_EXPLORE ' + json.dumps({'recipe': 'Y901',
            'counts': self.vars.get('explore_audit', {})}, sort_keys=True))
        # One compact persisted record per route, after engine final liquidation.
        # The runner requires debug_mode=True to persist these diagnostic logs.
        jh.debug('PORT_CAPACITY ' + json.dumps({
            'symbol': self.symbol, 'strategy': self.__class__.__name__,
            'trade_risk': TRADE_RISK, 'portfolio_risk': PORTFOLIO_RISK,
            'notional_cap': NOTIONAL_CAP,
            'counts': self.vars.get('portfolio_capacity_audit', {})
        }, sort_keys=True))

    def _explore_window(self, n):
        """Require the exact closed 4h clock; invalid input cannot create an event."""
        c = self.signal_candles
        if len(c) < n:
            return None
        w = c[-n:]
        if (not np.all(np.isfinite(w))
                or int(w[-1, 0]) != int(self.closed_candle_open_time)
                or w[-1, 0] + 14400000 > self.time
                or not np.all(np.diff(w[:, 0]) == 14400000)
                or not np.all(w[:, 1:] > 0)
                or not np.all(w[:, 3] >= w[:, 4])):
            return None
        return c

    def _explore_size(self, event):
        """Use the original budget, reservations, fees and volatility quota."""
        side = event['side']
        entry, distance = float(event['novel_requested_entry']), float(event['distance'])
        # Change only execution price; signal geometry remains frozen from trigger close.
        # Positive TP is a physical constraint, not a searched price-distance cut.
        if not (math.isfinite(entry) and entry > 2 * distance
                and entry > float(self.price)):
            audit = self.vars.setdefault('novel_audit', {})
            audit['invalid_candidate'] = audit.get('invalid_candidate', 0) + 1
            return False
        if not (math.isfinite(entry) and math.isfinite(distance)
                and 0 < distance < entry):
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        stop = entry - distance if side == 'long' else entry + distance
        unit_risk = distance + self.fee_rate * (entry + stop) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        step = 0.001
        self._record_capacity(side, capital, budget, unit_risk, entry,
                              room, margin_room, qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = dict(event, qty=qty, entry=entry,
                                risk=qty * unit_risk, notional=qty * entry)
        return True

    def before(self) -> None:
        # Event state is price-only and advances even while occupied or pending.
        if self.vars.get('explore_clock') == int(self.closed_candle_open_time):
            return
        self.vars['explore_event'] = None
        self.vars['explore_clock'] = int(self.closed_candle_open_time)
        c = self._explore_window(14)
        if c is None:
            self.vars['explore_previous'] = False
            return
        s, t = c[-2], c[-1]
        window = c[-13:-1]
        spans = window[:, 3] - window[:, 4]
        q = np.divide(window[:, 5] * (2 * window[:, 2] - window[:, 3] - window[:, 4]),
                      spans, out=np.zeros(12), where=spans > 0)
        cohort = window[q > 0]
        # No positive-pressure cohort means no reference cost and a false setup.
        vwap = (float(np.sum(cohort[:, 5] * np.mean(cohort[:, [3, 4, 2]], axis=1))
                      / np.sum(cohort[:, 5])) if len(cohort) else float('nan'))
        # The positive close-location cohort defines cost; an empty cohort is not a setup.
        # OHLCV pressure is a proxy, not observed taker flow.
        setup = bool(s[2] > c[-14, 2] and np.sum(q) < 0
                     and s[2] >= vwap and t[2] < t[1] and t[2] < vwap
                     and self._research_gate(c, window, q, vwap,
                         int(self.closed_candle_open_time) + 14400000))
        previous = self.vars.get('explore_previous', False)
        self.vars['explore_previous'] = setup
        if not setup or previous:
            return
        atr = float(ta.atr(c))
        if not (math.isfinite(atr) and atr > 0):
            return
        distance = float(max(s[3], t[3]) + 0.25 * atr - t[2])
        if not atr <= distance <= 3 * atr:
            return
        self.vars['explore_event'] = {'side': 'short', 'kind': 'Y901',
            'distance': distance, 'target_distance': 2 * distance, 'hold_hours': 48,
            'novel_anchor': float(vwap), 'novel_requested_entry': float(vwap)}
        audit = self.vars.setdefault('explore_audit', {})
        audit['events'] = audit.get('events', 0) + 1
        audit['events_occupied'] = audit.get('events_occupied', 0) + int(self.is_open)

    @staticmethod
    def _research_gate(c, window, q, vwap, decision_close):
        # One third separates a circuitous advance from a direct trend.
        # It is a single broad development cut, not a searched optimum.
        changes = c[-13:-1, 2] - c[-14:-2, 2]
        path = float(np.sum(np.abs(changes)))
        if path <= 0:
            return False
        efficiency = float(c[-2, 2] - c[-14, 2]) / path
        return bool(0 < efficiency <= 1 / 3)
```

### strategies/BTCNovelR902/__init__.py

SHA256 5860be5f546d8f355c621f3ca68581bb92022c2019e806e635e26e06605f140d; 23016 caracteres. Fuente completa recibida mediante read_strategy.

```python
import math
import json
import jesse.helpers as jh
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

# User-approved research limits; risk is not an optimization parameter.
TRADE_RISK = 0.01
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.
SLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.


class BTCNovelR902(Strategy):
    """Y902 frozen R8 creative experiment from N503; original routes retained.

    Shared risk and margin reservations; exploratory research, not approved live.
    SPY uses a session-filtered SPX CFD proxy; holidays and native parity remain
    unverified. Parameter-neighbour variants are sensitivity controls, not winners.
    """

    def hyperparameters(self) -> list:
        return [
            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},
            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},
            {'name': 'ema_slow', 'type': int, 'min': 80, 'max': 140, 'default': 80},
            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},
            {'name': 'stop_atr', 'type': float, 'min': 1.6, 'max': 3.0, 'default': 2.0},
            {'name': 'trail_atr', 'type': float, 'min': 3.0, 'max': 5.0, 'default': 4.2},
            {'name': 'be_r', 'type': float, 'min': 1.75, 'max': 3.0, 'default': 2.25},
        ]

    def trading_hours(self):
        if self.symbol == 'SPY-USDT':
            # The fixed UTC whole-bar intersection excludes the US index daily
            # break in both DST regimes. This is an intentional common window,
            # not an assertion that the source's full session ends at 20:00 UTC.
            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}
        return None

    @property
    @cached
    def signal_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    def _entry_window(self) -> bool:
        if self.symbol != 'SPY-USDT':
            return True
        # A closed bar opening at 12:00 triggers at 16:00. Its order expires
        # at 20:00, before the excluded 20:00-24:00 bucket. A 16:00-open bar
        # must not arm a new order at 20:00. Pending orders still cancel then.
        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}
        return self.is_trading_hours and utils.is_in_trading_hours(
            self.closed_candle_open_time, window)

    def _ledger(self) -> dict:
        return self.shared_vars.setdefault('phase2_reservations', {})

    def _key(self) -> str:
        return self.exchange + ':' + self.symbol

    def _capital(self) -> float:
        # Floating gains do not enlarge the risk budget; floating losses reduce it.
        return max(0.0, min(float(self.balance), float(self.portfolio_value)))

    def _committed(self) -> tuple:
        risk, notional = 0.0, 0.0
        ledger = self._ledger()
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            strategy = route.strategy
            if strategy.is_open:
                qty = abs(float(strategy.position.qty))
                entry = float(strategy.position.entry_price)
                # Risk is measured from the current mark, so protected floating PnL
                # is not silently treated as free capacity for another trade.
                value = abs(float(strategy.position.value))
                mark = value / qty if qty else entry
                stop = float(strategy.average_stop_loss)
                distance = max(0.0, mark - stop) if strategy.is_long else max(0.0, stop - mark)
                risk += qty * (distance + mark * (self.fee_rate + SLIPPAGE_RESERVE))
                notional += value
            else:
                reservation = ledger.get(route.exchange + ':' + route.symbol)
                if reservation:
                    # Includes not-yet-filled STOP/LIMIT entries, not only open positions.
                    risk += reservation['risk']
                    notional += reservation['notional']
        return risk, notional

    def _volatility_share(self) -> float:
        """Reserve a common gross-exposure budget using inverse ATR fractions.

        All configured assets receive an ex-ante share, even while their signal
        is idle. This prevents the first route from consuming all shared margin.
        It is a capital-efficiency tradeoff to test, not an optimal allocation.
        """
        weights = {}
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            c = utils.filter_candles_by_hours(route.strategy.candles, route.strategy.trading_hours())
            if len(c) < int(self.hp['ema_slow']) + 20:
                return 0.0
            atr = float(ta.atr(c))
            price = float(c[-1, 2])
            if not math.isfinite(atr) or atr <= 0 or price <= 0:
                return 0.0
            # Stops use a common ATR multiple. Equal risk therefore needs
            # notional proportional to price/ATR before gross-leverage scaling.
            weights[route.symbol] = price / atr
        return weights.get(self.symbol, 0.0) / sum(weights.values()) if weights else 0.0

    def _plan(self) -> bool:
        if self.symbol not in ('BTC-USDT', 'PAXG-USDT', 'SPY-USDT') or not self._entry_window():
            return False
        c = self.signal_candles
        n = int(self.hp['donchian_len'])
        slow_n = int(self.hp['ema_slow'])
        if len(c) < max(slow_n + 20, n):
            return False
        fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))
        slow = ta.ema(c, period=slow_n, sequential=True)
        atr = float(ta.atr(c))
        adx = float(ta.adx(c))
        rsi = float(ta.rsi(c))
        # The closed bar has broken the PRIOR channel. A passive LIMIT at that
        # boundary can fill only on a future retest within one 4h order lifetime.
        entry = float(np.max(c[-n-1:-1, 3]))
        if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):
            return False
        if not (atr > 0 and entry < self.price <= entry + atr and self.price > slow[-1]
                and fast > slow[-1] > slow[-5] and adx >= self.hp['adx_min']
                and 52 <= rsi <= 76 and self.high - self.low <= 3 * atr):
            return False
        distance = float(self.hp['stop_atr']) * atr
        if not 0 < distance < entry:
            return False
        capital = self._capital()
        committed_risk, committed_notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - committed_risk))
        # Fees at both planned entry and stop, plus an explicit adverse-fill reserve.
        unit_risk = distance + self.fee_rate * (entry + entry - distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - committed_notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        # Historical research precision only. Native symbol lot/min-notional
        # constraints must be verified before any live use.
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        self._record_capacity('long', capital, budget, unit_risk, entry,
                              room, margin_room, qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {
            'qty': qty, 'entry': entry, 'distance': distance,
            'risk': qty * unit_risk, 'notional': qty * entry,
        }
        return True

    def _signal(self) -> int:
        # Compute exactly one plan per bar, with long priority. Checking
        # should_short after go_long must never overwrite a queued long plan.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            if self._plan():
                signal = 1
            elif self._short_plan():
                signal = -1
            else:
                event = self.vars.get('explore_event')
                signal = (-1 if event and self._explore_size(event) else 0)
            self.vars['signal_value'] = signal
        return self.vars['signal_value']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], plan['entry']

    def _short_plan(self) -> bool:
        """Test selloff continuation instead of buying an oversold dip.

        A rising slow regime can still suffer a fast liquidation leg. This
        exploratory hypothesis came from the failed long mean-reversion sleeve;
        it is development evidence, not an independent validation.
        """
        if self.symbol != 'BTC-USDT' or not self._entry_window():
            return False
        c = self.signal_candles
        if len(c) < 140:
            return False
        macro = ta.ema(c, period=120, sequential=True)
        fast = float(ta.ema(c, period=20))
        atr = float(ta.atr(c))
        quick_rsi = float(ta.rsi(c, period=3))
        if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, quick_rsi)):
            return False
        if not (atr > 0 and macro[-1] > macro[-10]
                and self.price > macro[-1] - atr and quick_rsi <= 20):
            return False
        entry = min(float(c[-1, 4]), self.price - 0.25 * atr)
        distance = fast - entry
        if not (atr <= distance <= 3 * atr and distance >= 6 * self.fee_rate * entry):
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry + distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        qty = min(budget / unit_risk, room / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        self._record_capacity('short', capital, budget, unit_risk, entry,
                              room, max(0.0, float(self.leveraged_available_margin) * 0.90), qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry,
                             'target_distance': 1.5 * atr}
        return True

    def go_short(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.
        # Jesse processes cancellation before evaluating the next route.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:

        plan = self.vars['plan']
        self.vars['explore_kind'] = plan.get('kind')
        if self.vars['explore_kind']:
            # Geometry is frozen at signal; protection is relative to actual fill.
            entry = float(self.position.entry_price)
            distance = plan['distance']
            self.vars['initial_distance'] = distance
            self.vars['opened_time'] = int(self.time)
            self.vars['explore_deadline'] = int(self.time) + plan['hold_hours'] * 3600000
            qty = abs(float(self.position.qty))
            if self.is_long:
                self.stop_loss = qty, entry - distance
                self.take_profit = qty, entry + plan['target_distance']
            else:
                self.stop_loss = qty, entry + distance
                self.take_profit = qty, entry - plan['target_distance']
            self._ledger().pop(self._key(), None)
            audit = self.vars.setdefault('explore_audit', {})
            audit['fills'] = audit.get('fills', 0) + 1
            jh.debug('BTC_EXPLORE_FILL ' + json.dumps({
                'recipe': self.vars['explore_kind'], 'time': int(self.time),
                'side': 'long' if self.is_long else 'short',
                'entry': entry, 'qty': qty, 'distance': distance,
                'requested_entry': float(plan['novel_requested_entry']),
                'signal_anchor': float(plan['novel_anchor']),
                'target_distance': plan['target_distance'],
                'deadline': self.vars['explore_deadline']}, sort_keys=True))
            return
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        self.vars['initial_distance'] = distance
        # An intrabar fill must not inherit highs/closes from before its entry.
        self.vars['best_close'] = entry
        if self.is_short:
            self.vars['opened_time'] = int(self.time)
            self.stop_loss = abs(self.position.qty), entry + distance
            self.take_profit = abs(self.position.qty), entry - self.vars['plan']['target_distance']
        else:
            self.stop_loss = abs(self.position.qty), entry - distance
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:

        if self.vars.get('explore_kind'):
            # Only the first closed 4h decision at/after the fill-based deadline.
            if int(self.time) >= self.vars['explore_deadline']:
                self.liquidate()
            return
        if self.is_short:
            if self.time - self.vars['opened_time'] >= 72 * 60 * 60 * 1000:
                self.liquidate()
            return
        history = self.signal_candles
        atr = float(ta.atr(history))
        if not math.isfinite(atr) or atr <= 0:
            return
        entry = float(self.position.entry_price)
        distance = self.vars['initial_distance']
        self.vars['best_close'] = max(self.vars['best_close'], float(history[-1, 2]))
        best_r = (self.vars['best_close'] - entry) / distance
        mult = float(self.hp['trail_atr'])
        # Inherited late-trend tightening; retained as a controlled baseline choice.
        if best_r >= 8:
            mult *= 0.62
        elif best_r >= 5:
            mult *= 0.78
        stop = self.vars['best_close'] - mult * atr
        if best_r >= float(self.hp['be_r']):
            stop = max(stop, entry * (1 + 2.5 * self.fee_rate))
        if self.average_stop_loss < stop < self.price:
            self.stop_loss = abs(self.position.qty), stop

    def on_close_position(self, order, closed_trade) -> None:
        if self.vars.get('explore_kind'):
            audit = self.vars.setdefault('explore_audit', {})
            audit['closes'] = audit.get('closes', 0) + 1
        self.vars['explore_kind'] = None
        self._ledger().pop(self._key(), None)

    def _record_capacity(self, side, capital, budget, unit_risk, entry,
                         room, margin_room, raw_qty, step) -> None:
        """Observe existing sizing only; never gates signals or changes quantities.

        Counts plans reaching sizing while flat and without a pending entry.
        It does not infer trades that would have filled or signals while occupied.
        Quantity tolerances below classify numerical ties, not trading thresholds.
        """
        audit = self.vars.setdefault('portfolio_capacity_audit', {})
        row = audit.setdefault(side, {'eligible_sizing_attempts': 0,
                                     'risk_budget_limited': 0,
                                     'notional_or_weight_limited': 0,
                                     'margin_limited': 0,
                                     'sized_below_trade_target': 0,
                                     'capacity_zero': 0,
                                     'zero_after_lot_rounding': 0})
        row['eligible_sizing_attempts'] += 1
        target_qty = capital * TRADE_RISK / unit_risk
        tolerance = max(1e-8, abs(target_qty) * 1e-10)
        row['risk_budget_limited'] += int(budget / unit_risk + tolerance < target_qty)
        row['notional_or_weight_limited'] += int(room / entry + tolerance < target_qty)
        row['margin_limited'] += int(margin_room / entry + tolerance < target_qty)
        row['sized_below_trade_target'] += int(raw_qty + tolerance < target_qty)
        row['capacity_zero'] += int(raw_qty <= 0 < target_qty)
        row['zero_after_lot_rounding'] += int(math.floor(raw_qty / step) * step <= 0 < raw_qty)

    def terminate(self) -> None:
        jh.debug('BTC_NOVEL ' + json.dumps({'recipe': 'Y902',
            'counts': self.vars.get('novel_audit', {})}, sort_keys=True))
        jh.debug('BTC_EXPLORE ' + json.dumps({'recipe': 'Y902',
            'counts': self.vars.get('explore_audit', {})}, sort_keys=True))
        # One compact persisted record per route, after engine final liquidation.
        # The runner requires debug_mode=True to persist these diagnostic logs.
        jh.debug('PORT_CAPACITY ' + json.dumps({
            'symbol': self.symbol, 'strategy': self.__class__.__name__,
            'trade_risk': TRADE_RISK, 'portfolio_risk': PORTFOLIO_RISK,
            'notional_cap': NOTIONAL_CAP,
            'counts': self.vars.get('portfolio_capacity_audit', {})
        }, sort_keys=True))

    def _explore_window(self, n):
        """Require the exact closed 4h clock; invalid input cannot create an event."""
        c = self.signal_candles
        if len(c) < n:
            return None
        w = c[-n:]
        if (not np.all(np.isfinite(w))
                or int(w[-1, 0]) != int(self.closed_candle_open_time)
                or w[-1, 0] + 14400000 > self.time
                or not np.all(np.diff(w[:, 0]) == 14400000)
                or not np.all(w[:, 1:] > 0)
                or not np.all(w[:, 3] >= w[:, 4])):
            return None
        return c

    def _explore_size(self, event):
        """Use the original budget, reservations, fees and volatility quota."""
        side = event['side']
        entry, distance = float(event['novel_requested_entry']), float(event['distance'])
        # Change only execution price; signal geometry remains frozen from trigger close.
        # Positive TP is a physical constraint, not a searched price-distance cut.
        if not (math.isfinite(entry) and entry > 2 * distance
                and entry < float(self.price)):
            audit = self.vars.setdefault('novel_audit', {})
            audit['invalid_candidate'] = audit.get('invalid_candidate', 0) + 1
            return False
        if not (math.isfinite(entry) and math.isfinite(distance)
                and 0 < distance < entry):
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        stop = entry - distance if side == 'long' else entry + distance
        unit_risk = distance + self.fee_rate * (entry + stop) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        step = 0.001
        self._record_capacity(side, capital, budget, unit_risk, entry,
                              room, margin_room, qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = dict(event, qty=qty, entry=entry,
                                risk=qty * unit_risk, notional=qty * entry)
        return True

    def before(self) -> None:
        # Event state is price-only and advances even while occupied or pending.
        if self.vars.get('explore_clock') == int(self.closed_candle_open_time):
            return
        self.vars['explore_event'] = None
        self.vars['explore_clock'] = int(self.closed_candle_open_time)
        c = self._explore_window(14)
        if c is None:
            self.vars['explore_previous'] = False
            return
        s, t = c[-2], c[-1]
        window = c[-13:-1]
        spans = window[:, 3] - window[:, 4]
        q = np.divide(window[:, 5] * (2 * window[:, 2] - window[:, 3] - window[:, 4]),
                      spans, out=np.zeros(12), where=spans > 0)
        cohort = window[q > 0]
        # No positive-pressure cohort means no reference cost and a false setup.
        vwap = (float(np.sum(cohort[:, 5] * np.mean(cohort[:, [3, 4, 2]], axis=1))
                      / np.sum(cohort[:, 5])) if len(cohort) else float('nan'))
        # The positive close-location cohort defines cost; an empty cohort is not a setup.
        # OHLCV pressure is a proxy, not observed taker flow.
        setup = bool(s[2] > c[-14, 2] and np.sum(q) < 0
                     and s[2] >= vwap and t[2] < t[1] and t[2] < vwap
                     and self._research_gate(c, window, q, vwap,
                         int(self.closed_candle_open_time) + 14400000))
        previous = self.vars.get('explore_previous', False)
        self.vars['explore_previous'] = setup
        if not setup or previous:
            return
        atr = float(ta.atr(c))
        if not (math.isfinite(atr) and atr > 0):
            return
        distance = float(max(s[3], t[3]) + 0.25 * atr - t[2])
        if not atr <= distance <= 3 * atr:
            return
        self.vars['explore_event'] = {'side': 'short', 'kind': 'Y902',
            'distance': distance, 'target_distance': 2 * distance, 'hold_hours': 48,
            'novel_anchor': float(vwap), 'novel_requested_entry': float(t[4])}
        audit = self.vars.setdefault('explore_audit', {})
        audit['events'] = audit.get('events', 0) + 1
        audit['events_occupied'] = audit.get('events_occupied', 0) + int(self.is_open)

    @staticmethod
    def _research_gate(c, window, q, vwap, decision_close):
        # One third separates a circuitous advance from a direct trend.
        # It is a single broad development cut, not a searched optimum.
        changes = c[-13:-1, 2] - c[-14:-2, 2]
        path = float(np.sum(np.abs(changes)))
        if path <= 0:
            return False
        efficiency = float(c[-2, 2] - c[-14, 2]) / path
        return bool(0 < efficiency <= 1 / 3)
```

## Features V3–V6 completas para deduplicación

### strategies/ResearchV3Base4h/range_features.py

SHA256 281583938ef90880f4fbbc05fee685245c4f173c7d9d122ebacb5615c64811d4.

```python
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV3Base4h import BAR, closed_window

# Frozen RANGE design: two 120-close means separated by 24 four-hour bars.
WINDOW = 144
BAND_PERIOD = 20
SLOW_PERIOD = 120
SLOW_LAG = 24
Z_LIMIT = 2.
REGIME_LIMIT = .5


def _invalid(reason):
    return dict(valid=False, direction=0, mean_target=None, reason=reason,
                details=dict(reason=reason))


def features(candles, now, atr):
    """Fresh outward band crossing, admitted only when slow drift is small."""
    rows = closed_window(candles, now, WINDOW)
    if rows is None:
        return _invalid("history_invalid")
    if atr is None:
        return _invalid("atr_invalid")
    a = float(atr["value"])
    if not math.isfinite(a) or a <= 0:
        return _invalid("atr_invalid")
    closes = rows[:, 2]
    current, previous = closes[-BAND_PERIOD:], closes[-BAND_PERIOD - 1:-1]
    # Each band includes its own closed bar, not a later band's threshold.
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        mean, prior_mean = float(np.mean(current)), float(np.mean(previous))
        sigma, prior_sigma = float(np.std(current, ddof=0)), float(np.std(previous, ddof=0))
        slow = float(np.mean(closes[-SLOW_PERIOD:]))
        slow_lag = float(np.mean(closes[-WINDOW:-SLOW_LAG]))
    if not all(math.isfinite(v) for v in (mean, prior_mean, sigma, prior_sigma, slow, slow_lag)):
        return _invalid("statistics_nonfinite")
    if sigma <= 0 or prior_sigma <= 0:
        return _invalid("std_invalid")
    z, prior_z = (float(closes[-1]) - mean) / sigma, (float(closes[-2]) - prior_mean) / prior_sigma
    regime = abs(slow - slow_lag) / a
    if not all(math.isfinite(v) for v in (z, prior_z, regime)):
        return _invalid("statistics_nonfinite")
    passed = regime <= REGIME_LIMIT
    direction = 0
    if passed:
        if prior_z >= -Z_LIMIT and z < -Z_LIMIT:
            direction = 1
        elif prior_z <= Z_LIMIT and z > Z_LIMIT:
            direction = -1
    # Canonical OHLC hash preserves the complete 144-bar signal provenance.
    digest = hashlib.sha256(json.dumps(rows[:, :5].tolist(), separators=(",", ":"),
                                      allow_nan=False).encode()).hexdigest()
    reason = "signal" if direction else "no_setup" if passed else "regime_reject"
    return dict(valid=True, direction=direction, mean_target=mean, reason=reason,
                details=dict(mean20=mean, std20=sigma, z=z, mean20_prev=prior_mean,
                             std20_prev=prior_sigma, z_prev=prior_z,
                             slow_mean=slow, slow_mean_lag24=slow_lag,
                             regime_ratio=regime, regime_passed=passed, atr=a,
                             first_open=int(rows[0, 0]), last_open=int(rows[-1, 0]),
                             bars=WINDOW, window_sha256=digest, reason=reason))


def _fixture(closes):
    """Synthetic OHLC encloses each chosen close; one-unit wicks keep it coherent."""
    return np.array([[i * BAR, c, c, c + 1., c - 1., 1.] for i, c in enumerate(closes)], dtype=float)


def self_checks():
    checks = 0

    def check(condition):
        nonlocal checks
        assert condition
        checks += 1

    base = [99.9 if i % 2 == 0 else 100.1 for i in range(160)]
    now = WINDOW * BAR
    atr = dict(value=2.)
    for direction, shock in ((1, 95.), (-1, 105.)):
        values = list(base)
        values[143] = shock
        rows = _fixture(values)
        result = features(rows, now, atr)
        # Hand-counted last20: ten 99.9, nine 100.1 and the shock.
        mean = (10 * 99.9 + 9 * 100.1 + shock) / 20
        variance = (10 * (99.9 - mean) ** 2 + 9 * (100.1 - mean) ** 2 + (shock - mean) ** 2) / 20
        check(result["valid"] and result["direction"] == direction)
        check(math.isclose(result["mean_target"], mean, abs_tol=1e-12))
        check(math.isclose(result["details"]["std20"], math.sqrt(variance), abs_tol=1e-12))
        check(math.isclose(result["details"]["mean20_prev"], 100., abs_tol=1e-12))
        check(math.isclose(result["details"]["z_prev"], -1., abs_tol=1e-10))
        check(math.isclose(result["details"]["slow_mean_lag24"], 100., abs_tol=1e-12))
        check(math.isclose(result["details"]["regime_ratio"], abs(shock - 100.1) / 120 / 2, abs_tol=1e-12))
        check(direction * (result["mean_target"] - shock) > 0)
        check(result["details"]["last_open"] + BAR == now)
        check(result["details"]["last_open"] - result["details"]["first_open"] == 143 * BAR)
        for cutoff in (144 * BAR, 145 * BAR, 150 * BAR):
            prefix = rows[rows[:, 0] + BAR <= cutoff]
            changed = rows.copy()
            changed[changed[:, 0] + BAR > cutoff, 1:5] = np.nan
            check(features(prefix, cutoff, atr) == features(rows, cutoff, atr))
            check(features(changed, cutoff, atr) == features(prefix, cutoff, atr))
        # An adverse volatility gate is a neutral valid signal, not invalid provider data.
        blocked = features(rows, now, dict(value=.001))
        check(blocked["valid"] and blocked["direction"] == 0 and blocked["reason"] == "regime_reject")
        # The target is the same past mean, irrespective of which ATR passed the gate.
        check(features(rows, now, dict(value=3.))["mean_target"] == result["mean_target"])

    trend = _fixture([100. + i for i in range(160)])
    boundary = features(trend, now, dict(value=48.))
    check(boundary["valid"] and boundary["details"]["regime_ratio"] == .5)
    check(boundary["details"]["regime_passed"])
    check(not features(trend, now, dict(value=47.9))["details"]["regime_passed"])

    persistent = list(base)
    persistent[142], persistent[143] = 95., 94.
    result = features(_fixture(persistent), now, atr)
    check(result["valid"] and result["details"]["z_prev"] < -2 and result["direction"] == 0)
    reentry = list(base)
    reentry[142], reentry[143] = 95., 100.
    check(features(_fixture(reentry), now, atr)["direction"] == 0)

    flat = _fixture([100.] * 160)
    check(features(flat, now, atr)["reason"] == "std_invalid")
    previous_flat = [100.] * 160
    previous_flat[143] = 95.
    check(features(_fixture(previous_flat), now, atr)["reason"] == "std_invalid")
    rows = _fixture(base)
    check(not features(rows[:143], now, atr)["valid"])
    check(not features(rows, now + 60000, atr)["valid"])
    check(not features(np.delete(rows, 20, axis=0), now, atr)["valid"])
    duplicate = rows.copy()
    duplicate[20, 0] = duplicate[19, 0]
    check(not features(duplicate, now, atr)["valid"])
    for field, value in ((1, float("nan")), (2, 0.), (3, 90.), (4, 110.)):
        invalid = rows.copy()
        invalid[20, field] = value
        check(not features(invalid, now, atr)["valid"])
    for a in (None, dict(value=0.), dict(value=-1.), dict(value=float("nan")), dict(value=float("inf"))):
        check(not features(rows, now, a)["valid"])
    check(features(rows, now, atr)["direction"] == 0)
    check(all(k not in features(rows, now, atr) for k in ("time", "line")))
    return dict(status="passed", assertions=checks)
```

### strategies/ResearchV3Base4h/channel_features.py

SHA256 3c49769786b7d6a50a11bfc4e063de54e4ffc92bdf4b08b60e48179469b78590.

```python
import math

import numpy as np

from strategies.ResearchV3Base4h import closed_window
from strategies.ResearchV2Core4h import BAR


def features(candles, now, atr):
    """Channel excludes the signal bar; the two SMA120 windows end six bars apart."""
    rows = closed_window(candles, now, 126)
    if rows is None or atr is None:
        return dict(valid=False, direction=0, details=dict(quality="history_or_atr_invalid"))
    value = float(atr["value"])
    if not math.isfinite(value) or value <= 0:
        return dict(valid=False, direction=0, details=dict(quality="atr_invalid"))
    close = float(rows[-1, 2])
    high = float(np.max(rows[-21:-1, 3]))
    low = float(np.min(rows[-21:-1, 4]))
    mean = float(np.mean(rows[-120:, 2]))
    old_mean = float(np.mean(rows[-126:-6, 2]))
    breakout = 1 if close > high else -1 if close < low else 0
    trend_long = close > mean and mean > old_mean
    trend_short = close < mean and mean < old_mean
    direction = breakout if (breakout == 1 and trend_long) or (breakout == -1 and trend_short) else 0
    details = dict(first=int(rows[0, 0]), last=int(rows[-1, 0]), close=close,
                   high20=high, low20=low, sma120=mean, sma120_6=old_mean,
                   breakout=breakout, trend_long=bool(trend_long), trend_short=bool(trend_short))
    return dict(valid=True, direction=direction, details=details,
                reason="regime_reject" if breakout and not direction else "no_setup")


def post_entry_extremes(candles, now, entry_at, previous_high, previous_low):
    """Ignore pre-fill/partial bars; incomplete post-entry history never resets extremes."""
    # Entry is normally aligned. Ceil also excludes the partial bar of an off-grid fill.
    first_open = ((int(entry_at) + BAR - 1) // BAR) * BAR
    count = (int(now) - first_open) // BAR
    if count <= 0:
        return previous_high, previous_low
    rows = closed_window(candles, now, count)
    if rows is None or rows[0, 0] != first_open:
        return None
    return max(previous_high, float(np.max(rows[:, 3]))), min(previous_low, float(np.min(rows[:, 4])))


def trailing_level(direction, high_water, low_water, atr_value, old_stop, multiplier=3.):
    """ATR may expand, but the protection can only ratchet in the favorable direction."""
    if direction not in (-1, 1) or not all(math.isfinite(x) and x > 0 for x in
                                         (high_water, low_water, atr_value, old_stop, multiplier)):
        return None
    if high_water < low_water:
        return None
    return max(old_stop, high_water - multiplier * atr_value) if direction == 1 else min(
        old_stop, low_water + multiplier * atr_value)


def self_checks():
    checks = 0
    def check(condition):
        nonlocal checks
        assert condition
        checks += 1

    # Known channel 99..101; the signal's own new high/low must be excluded.
    rows = np.array([[i * BAR, 100., 100., 101., 99., 1.] for i in range(150)])
    now = 126 * BAR
    atr = dict(value=2.)
    for side in (-1, 1):
        changed = rows.copy()
        changed[125, 2] = 120. if side == 1 else 80.
        changed[125, 3:5] = [121., 79.]
        result = features(changed, now, atr)
        check(result["direction"] == side)
        check(result["details"]["high20"] == 101. and result["details"]["low20"] == 99.)
        expected = (119 * 100 + changed[125, 2]) / 120
        check(math.isclose(result["details"]["sma120"], expected, abs_tol=1e-12))
        check(result["details"]["sma120_6"] == 100.)
        # Prefix and future mutations must leave the complete result identical.
        prefix = changed[changed[:, 0] + BAR <= now]
        check(features(prefix, now, atr) == result)
        future = changed.copy()
        future[future[:, 0] + BAR > now, 1:5] = np.nan
        check(features(future, now, atr) == result)
        old = changed.copy()
        old[0, 2] = changed[125, 2]
        old[0, 3:5] = [121., 79.]
        tied = features(old, now, atr)
        check(tied["direction"] == 0 and tied["reason"] == "regime_reject")
        against = changed.copy()
        against[:6, 1:5] = [200., 200., 201., 199.] if side == 1 else [50., 50., 51., 49.]
        rejected = features(against, now, atr)
        check(rejected["direction"] == 0 and rejected["reason"] == "regime_reject")
    check(features(rows, now, atr)["direction"] == 0)
    check(not features(rows[:125], now, atr)["valid"])
    check(not features(rows, now + 60000, atr)["valid"])
    check(not features(rows, now, None)["valid"])
    check(not features(rows, now, dict(value=0.))["valid"])
    missing = np.delete(rows, 80, axis=0)
    check(not features(missing, now, atr)["valid"])
    duplicate = rows.copy()
    duplicate[80, 0] = duplicate[79, 0]
    check(not features(duplicate, now, atr)["valid"])
    for field, value in ((1, np.nan), (2, 0.), (3, 99.), (4, 102.)):
        invalid = rows.copy()
        invalid[80, field] = value
        check(not features(invalid, now, atr)["valid"])
    # Earlier history is outside both finite SMA windows and cannot change the signal.
    shifted = rows.copy()
    shifted[131, 2:5] = [120., 121., 99.]
    before = features(shifted, 132 * BAR, atr)
    shifted[0, 1] = np.nan
    check(features(shifted, 132 * BAR, atr) == before)
    # A breakout with positive SMA slope still fails when price is below the mean.
    level = rows.copy()
    level[:6, 1:5] = [50., 50., 51., 49.]
    level[6:105, 1:5] = [180., 180., 181., 179.]
    level[125, 2:5] = [120., 121., 99.]
    rejected = features(level, now, atr)
    check(rejected["details"]["breakout"] == 1 and rejected["details"]["sma120"] > 120.)
    check(rejected["details"]["sma120"] > rejected["details"]["sma120_6"] and rejected["direction"] == 0)
    # Exact equality to a previous channel boundary does not count as a breakout.
    boundary = rows.copy()
    boundary[125, 2] = 101.
    check(features(boundary, now, atr)["direction"] == 0)

    path = rows.copy()
    path[39, 3] = 1000.  # Before entry: including this high would cause a false ratchet.
    path[40, 3:5] = [111., 98.]
    path[41, 3:5] = [112., 97.]
    check(post_entry_extremes(path, 40 * BAR, 40 * BAR, 105., 105.) == (105., 105.))
    check(post_entry_extremes(path, 41 * BAR, 40 * BAR, 105., 105.) == (111., 98.))
    check(post_entry_extremes(path, 42 * BAR, 40 * BAR, 105., 105.) == (112., 97.))
    # A fill just after an open cannot use that partial bar.
    check(post_entry_extremes(path, 41 * BAR, 40 * BAR + 1, 105., 105.) == (105., 105.))
    check(post_entry_extremes(path, 42 * BAR, 40 * BAR + 1, 105., 105.) == (112., 97.))
    future = path.copy()
    future[42:, 3] = 1e9
    check(post_entry_extremes(future, 42 * BAR, 40 * BAR, 105., 105.) == (112., 97.))
    absent = np.delete(path, 40, axis=0)
    check(post_entry_extremes(absent, 42 * BAR, 40 * BAR, 105., 105.) is None)
    check(post_entry_extremes(path, 42 * BAR, 40 * BAR, 120., 90.) == (120., 90.))
    check(trailing_level(1, 111., 98., 2., 101.) == 105.)
    check(trailing_level(-1, 111., 97., 2., 109.) == 103.)
    check(trailing_level(1, 111., 98., 3., 105.) == 105.)
    check(trailing_level(-1, 111., 97., 3., 103.) == 103.)
    check(trailing_level(1, 111., 98., 2., 101.) >= 104.)
    check(trailing_level(-1, 111., 97., 2., 109.) <= 104.)
    check(trailing_level(1, 111., 98., float("nan"), 101.) is None)
    check(trailing_level(-1, 111., 97., 0., 109.) is None)
    return dict(status="passed", assertions=checks)
```

### strategies/ResearchV3Base4h/pullback_features.py

SHA256 14abd2aedf9497bf3d4fd8cb2767211a1c9116e1a3db9b1859b0e90840804809.

```python
import hashlib
import json
import math

import numpy as np

BAR = 14400000
HISTORY = 126


def features(candles, now, atr):
    """Three closed bars form the pattern; ATR controls risk only in the shared base."""
    rows = candles[candles[:, 0] + BAR <= now][-HISTORY:]
    if len(rows) != HISTORY or rows[-1, 0] != now - BAR:
        return dict(valid=False, direction=0, details=dict(reason="history_short"))
    if not np.all(np.diff(rows[:, 0]) == BAR):
        return dict(valid=False, direction=0, details=dict(reason="history_gap"))
    prices = rows[:, 1:5]
    if not np.all(np.isfinite(rows[:, :5])) or np.any(prices <= 0):
        return dict(valid=False, direction=0, details=dict(reason="ohlc_invalid"))
    opens, closes, highs, lows = (rows[:, i] for i in (1, 2, 3, 4))
    if np.any(highs < np.maximum(opens, closes)) or np.any(lows > np.minimum(opens, closes)) or np.any(highs < lows):
        return dict(valid=False, direction=0, details=dict(reason="ohlc_invalid"))
    # Exact slices preserve each historical SMA's own closed-bar endpoint.
    fast = float(np.mean(closes[-20:]))
    fast_previous = float(np.mean(closes[-21:-1]))
    fast_older = float(np.mean(closes[-22:-2]))
    slow = float(np.mean(closes[-120:]))
    slow_previous_day = float(np.mean(closes[-126:-6]))
    if not np.all(np.isfinite([fast, fast_previous, fast_older, slow, slow_previous_day])):
        return dict(valid=False, direction=0, details=dict(reason="sma_invalid"))
    touch = bool(lows[-2] <= fast_previous <= highs[-2])
    long_regime = bool(closes[-1] > slow and slow > slow_previous_day)
    short_regime = bool(closes[-1] < slow and slow < slow_previous_day)
    long_pattern = bool(closes[-3] > fast_older and touch and closes[-1] > highs[-2] and closes[-1] > fast)
    short_pattern = bool(closes[-3] < fast_older and touch and closes[-1] < lows[-2] and closes[-1] < fast)
    go_long, go_short = long_regime and long_pattern, short_regime and short_pattern
    assert not (go_long and go_short)
    direction = 1 if go_long else -1 if go_short else 0
    # Window hash is the same canonical timestamp/OHLC format used for ATR provenance.
    window_hash = hashlib.sha256(json.dumps(rows[:, :5].tolist(), separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    result = dict(valid=True, direction=direction, details=dict(
        fast=fast, fast_previous=fast_previous, fast_older=fast_older,
        slow=slow, slow_previous_day=slow_previous_day, touch=touch,
        long_regime=long_regime, short_regime=short_regime,
        long_pattern=long_pattern, short_pattern=short_pattern,
        first=int(rows[0, 0]), last=int(rows[-1, 0]), sha256=window_hash,
        pattern=rows[-3:, :5].tolist()))
    if direction == 0:
        result["reason"] = "regime_reject" if not (long_regime or short_regime) else "no_setup"
    return result


def self_checks():
    checks = 0

    def check(condition):
        nonlocal checks
        assert condition
        checks += 1

    # Linear closes make all SMA values independently calculable by arithmetic series.
    rows = np.array([[i * BAR, 100. + i, 100. + i, 101. + i, 99. + i, 1.] for i in range(126)])
    rows[-2, 4] = 213.
    rows[-1, 1:5] = [228., 228., 229., 227.]
    now = 126 * BAR
    result = features(rows, now, None)
    check(result["valid"] and result["direction"] == 1)
    expected = dict(fast=215.65, fast_previous=214.5, fast_older=213.5,
                    slow=165.525, slow_previous_day=159.5)
    for key, value in expected.items():
        check(math.isclose(result["details"][key], value, rel_tol=0, abs_tol=1e-12))
    check(result["details"]["first"] == 0 and result["details"]["last"] == now - BAR)

    # Reflection exchanges long/short while preserving the wick-touch geometry.
    mirror = rows.copy()
    mirror[:, 1] = 500 - rows[:, 1]
    mirror[:, 2] = 500 - rows[:, 2]
    mirror[:, 3] = 500 - rows[:, 4]
    mirror[:, 4] = 500 - rows[:, 3]
    check(features(mirror, now, None)["direction"] == -1)

    future = np.vstack([rows, [[now, 1e9, 1e9, 1e9, 1e9, 1.],
                             [now + BAR, 1e9, 1e9, 1e9, 1e9, 1.]]])
    check(features(future, now, None) == result)
    future[-2:, 1:5] = np.nan
    check(features(future, now, None) == result)
    older = np.vstack([[[-BAR, float("nan"), float("nan"), float("nan"), float("nan"), 1.]], rows])
    check(features(older, now, None) == result)

    changed_current = rows.copy()
    changed_current[-1, 1:5] = [100000., 100000., 100001., 99999.]
    changed = features(changed_current, now, None)
    for key in ("fast_previous", "fast_older", "slow_previous_day"):
        check(changed["details"][key] == result["details"][key])
    check(changed["details"]["fast"] != result["details"]["fast"])
    check(changed["details"]["slow"] != result["details"]["slow"])

    equal_touch = rows.copy()
    equal_touch[-2, 4] = expected["fast_previous"]
    check(features(equal_touch, now, None)["direction"] == 1)
    no_touch = rows.copy()
    no_touch[-2, 4] = 215.
    check(features(no_touch, now, None)["direction"] == 0)
    whole_below = rows.copy()
    whole_below[-2, 1:5] = [211., 211., 212., 210.]
    check(features(whole_below, now, None)["valid"])
    check(features(whole_below, now, None)["direction"] == 0)
    no_resumption = rows.copy()
    no_resumption[-1, 1:5] = [225., 225., 226., 224.]
    check(features(no_resumption, now, None)["direction"] == 0)
    flat = rows.copy()
    flat[:, 1:5] = [100., 100., 101., 99.]
    check(features(flat, now, None)["direction"] == 0)

    check(not features(rows[:125], now, None)["valid"])
    check(not features(np.delete(rows, 10, axis=0), now, None)["valid"])
    duplicate = rows.copy()
    duplicate[10, 0] = duplicate[9, 0]
    check(not features(duplicate, now, None)["valid"])
    check(not features(rows, now + 60000, None)["valid"])
    for field, value in ((1, float("nan")), (2, 0.), (3, 1.), (4, 1e6)):
        broken = rows.copy()
        broken[10, field] = value
        check(not features(broken, now, None)["valid"])
    # ATR does not gate the price signal; the shared base alone validates its risk input.
    check(features(rows, now, dict(value=9., first=0, last=now - BAR, bars=[])) == result)
    return dict(status="passed", assertions=checks)
```

### strategies/ResearchV4Base1h/shock_features.py

SHA256 0ebf34769d0ad821e19773dfe5f6494398a0727ec5d1a93fc42c84472650a43b.

```python
"""Causal hourly shock reversal; thresholds are frozen before economic testing."""

import json
import math

import numpy as np

from strategies.ResearchV4Base1h import BAR, atr_window, closed_window


def features(candles, now, atr, shock_multiplier=2.0, volume_multiplier=2.0):
    # Twenty-four prior volumes plus the event; no future confirmation or latch.
    rows = closed_window(candles, now, 25)
    invalid = dict(valid=False, direction=0, reason="shock_data_invalid", details={})
    if rows is None or rows.shape[1] < 6:
        return invalid
    volumes = rows[:, 5]
    if not np.all(np.isfinite(volumes)) or np.any(volumes < 0):
        return invalid
    try:
        if (not math.isfinite(shock_multiplier) or shock_multiplier <= 0 or
                not math.isfinite(volume_multiplier) or volume_multiplier <= 0):
            return invalid
        # Reject a current-bar ATR accidentally supplied by another sector.
        if (atr is None or atr["offset_bars"] != 1 or
                atr["first"] != now - 16 * BAR or atr["last"] != now - 2 * BAR or
                not math.isfinite(atr["value"]) or atr["value"] <= 0):
            return dict(valid=False, direction=0, reason="shock_atr_invalid", details={})
    except (KeyError, TypeError, ValueError):
        return invalid
    average_volume = float(np.mean(volumes[:-1]))
    displacement = float(rows[-1, 2] - rows[-2, 2])
    current_volume = float(volumes[-1])
    # A finite input sum can still overflow; reject rather than emit NaN/Infinity.
    if (not math.isfinite(average_volume) or average_volume <= 0 or
            not math.isfinite(displacement)):
        return invalid
    price_threshold = float(shock_multiplier * atr["value"])
    volume_threshold = float(volume_multiplier * average_volume)
    if not math.isfinite(price_threshold) or not math.isfinite(volume_threshold):
        return invalid
    price_event = bool(abs(displacement) >= price_threshold)
    volume_event = bool(current_volume >= volume_threshold)
    direction = (-1 if displacement > 0 else 1) if price_event and volume_event else 0
    # Only Python scalars: source windows live in bounded ATR/provenance logs.
    details = dict(first=int(rows[0, 0]), last=int(rows[-1, 0]),
        displacement=displacement, atr_previous=float(atr["value"]),
        volume=current_volume, volume_mean_previous=average_volume,
        shock_multiplier=float(shock_multiplier), volume_multiplier=float(volume_multiplier),
        price_event=price_event, volume_event=volume_event)
    reason = "shock_setup" if direction else "shock_price_below" if not price_event else "shock_volume_below"
    return dict(valid=True, direction=int(direction), reason=reason, details=details)


def self_checks():
    """Pure deterministic surfaces; these checks make no claims about broker fills."""
    count = 0

    def check(condition):
        nonlocal count
        assert condition
        count += 1

    def fixture(sign=1):
        # Prior14 true ranges are exactly2; minimum shock is4 and volume20.
        rows = np.array([[i * BAR, 100., 100., 101., 99., 10.] for i in range(25)])
        rows[-1, 2] = 100. + sign * 4.
        rows[-1, 3] = max(101., rows[-1, 2] + 1.)
        rows[-1, 4] = min(99., rows[-1, 2] - 1.)
        rows[-1, 5] = 20.
        return rows

    now = 25 * BAR
    up, down = fixture(), fixture(-1)
    atr = atr_window(up, now, 1)
    check(atr["value"] == 2.)
    check(atr["first"] == 9 * BAR and atr["last"] == 23 * BAR)
    check(len(atr["bars"]) == 15 and atr["offset_bars"] == 1)
    short, long = features(up, now, atr), features(down, now, atr_window(down, now, 1))
    check(short["valid"] and short["direction"] == -1)
    check(long["valid"] and long["direction"] == 1)
    check(short["details"]["displacement"] == -long["details"]["displacement"])
    check(short["details"]["volume_mean_previous"] == 10.)
    check(short["details"]["volume"] == 20.)
    check(short["reason"] == long["reason"] == "shock_setup")
    check(len(json.dumps(short, allow_nan=False)) < 1000)
    before = up.copy()
    features(up, now, atr)
    check(np.array_equal(up, before))
    below = up.copy()
    below[-1, 2] = 103.999
    check(features(below, now, atr)["direction"] == 0)
    check(features(below, now, atr)["reason"] == "shock_price_below")
    below = up.copy()
    below[-1, 5] = 19.999
    check(features(below, now, atr)["direction"] == 0)
    check(features(below, now, atr)["reason"] == "shock_volume_below")
    check(features(up, now, atr, 1.8, 1.8)["direction"] == -1)
    check(features(up, now, atr, 2.2, 2.2)["direction"] == 0)
    wide_event = up.copy()
    wide_event[-1, 3], wide_event[-1, 4] = 200., 1.
    check(atr_window(wide_event, now, 1)["value"] == 2.)
    check(features(wide_event, now, atr)["direction"] == -1)
    huge_volume = up.copy()
    huge_volume[-1, 5] = 10000.
    check(features(huge_volume, now, atr)["details"]["volume_mean_previous"] == 10.)
    check(not features(up, now, atr_window(up, now, 0))["valid"])
    check(not features(up, now, None)["valid"])
    malformed_atr = dict(atr, value=float("nan"))
    check(not features(up, now, malformed_atr)["valid"])
    malformed_atr = dict(atr, first=0)
    check(not features(up, now, malformed_atr)["valid"])
    future = np.array([[now, 100., 100., 101., 99., float("nan")]])
    check(features(np.vstack((up, future)), now, atr) == short)
    # More history cannot seed a different value: only the last25 closed rows matter.
    older = up.copy()
    older[:, 0] -= 25 * BAR
    check(features(np.vstack((older, up)), now, atr) == short)
    check(not features(up[:-1], now, atr)["valid"])
    check(not features(up, now + 1, atr)["valid"])
    gap = up.copy()
    gap[2, 0] += 1
    check(not features(gap, now, atr)["valid"])
    for column, value in ((1, 0.), (2, float("nan")), (3, 90.), (4, 110.),
                          (5, -1.), (5, float("nan")), (5, float("inf"))):
        bad = up.copy()
        bad[5, column] = value
        check(not features(bad, now, atr)["valid"])
    zero_mean = up.copy()
    zero_mean[:-1, 5] = 0.
    check(not features(zero_mean, now, atr)["valid"])
    zero_event = up.copy()
    zero_event[-1, 5] = 0.
    check(features(zero_event, now, atr)["valid"] and features(zero_event, now, atr)["direction"] == 0)
    check(not features(up[:, :5], now, atr)["valid"])
    for parameter in (0., -1., float("nan"), float("inf")):
        check(not features(up, now, atr, parameter, 2.)["valid"])
        check(not features(up, now, atr, 2., parameter)["valid"])
    # A zero prior candle volume is allowed when its24-hour average remains positive.
    one_zero = up.copy()
    one_zero[0, 5] = 0.
    check(features(one_zero, now, atr)["valid"])
    return dict(status="passed", assertions=count)
```

### strategies/ResearchV5Base1h/vwap_features.py

SHA256 d6652607f3a667bcadaf10d2d64eed2af42864784f05c00123f1f429d5345bde.

```python
"""Finite rolling24 HLC3/volume reversal; this is not anchored-day/tick VWAP."""

import hashlib
import json
import math

import numpy as np

from strategies.ResearchV5Base1h import BAR, atr_window, closed_window


def vwap_state(candles, now, dispersion=True):
    """Exit may use mean alone even when variance/ATR cannot be evaluated."""
    rows = closed_window(candles, now, 24)
    if rows is None or rows.shape[1] < 6:
        return None
    volume = rows[:, 5]
    if not np.all(np.isfinite(volume)) or np.any(volume < 0):
        return None
    maximum = float(np.max(volume))
    if maximum <= 0:
        return None
    # Scaling weights prevents overflow in a sum of otherwise finite large volumes.
    with np.errstate(over="ignore", invalid="ignore"):
        weights = volume / maximum
        weights = weights / np.sum(weights)
        typical = rows[:, 3] / 3. + rows[:, 4] / 3. + rows[:, 2] / 3.
        mean = float(np.sum(weights * typical))
    if not math.isfinite(mean) or mean <= 0:
        return None
    state = dict(mean=mean, close=float(rows[-1, 2]), first=int(rows[0, 0]),
                 last=int(rows[-1, 0]), zero_volumes=int(np.sum(volume == 0)))
    if dispersion:
        with np.errstate(over="ignore", invalid="ignore"):
            variance = float(np.sum(weights * (typical - mean) ** 2))
        if not math.isfinite(variance) or variance < 0:
            return None
        state["sigma"] = math.sqrt(variance)
    state["sha256"] = hashlib.sha256(json.dumps(
        rows[:, :6].tolist(), separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    return state


def entry_direction(c0, c1, m0, m1, s0, s1, multiplier):
    """Closed reentry includes outer equality but never enters past the mean."""
    values = (c0, c1, m0, m1, s0, s1, multiplier)
    if not all(math.isfinite(v) for v in values) or min(s0, s1, multiplier) <= 0:
        return 0
    lower0, upper0 = m0 - multiplier * s0, m0 + multiplier * s0
    lower1, upper1 = m1 - multiplier * s1, m1 + multiplier * s1
    if not all(math.isfinite(v) for v in (lower0, upper0, lower1, upper1)):
        return 0
    if c1 < lower1 and lower0 <= c0 < m0 and c0 > c1:
        return 1
    if c1 > upper1 and m0 < c0 <= upper0 and c0 < c1:
        return -1
    return 0


def features(candles, now, atr, band_multiplier=2.0):
    invalid = dict(valid=False, direction=0, reason="vwap_data_invalid", details={})
    rows = closed_window(candles, now, 25)
    if rows is None or rows.shape[1] < 6:
        return invalid
    try:
        if not math.isfinite(band_multiplier) or band_multiplier <= 0:
            return invalid
        if (atr is None or atr["offset_bars"] != 0 or
                atr["first"] != now - 15 * BAR or atr["last"] != now - BAR or
                not math.isfinite(atr["value"]) or atr["value"] <= 0):
            return invalid
    except (KeyError, TypeError, ValueError):
        return invalid
    current = vwap_state(candles, now)
    previous = vwap_state(candles, now - BAR)
    atr_previous = atr_window(candles, now, 1)
    if current is None or previous is None or atr_previous is None:
        return invalid
    scale0 = max(current["sigma"], float(atr["value"]))
    scale1 = max(previous["sigma"], atr_previous["value"])
    # Reject overflow instead of allowing an unbounded band to produce a false reentry.
    if not all(math.isfinite(v) for v in (
            current["mean"] - band_multiplier * scale0,
            current["mean"] + band_multiplier * scale0,
            previous["mean"] - band_multiplier * scale1,
            previous["mean"] + band_multiplier * scale1)):
        return invalid
    direction = entry_direction(current["close"], previous["close"], current["mean"],
        previous["mean"], scale0, scale1, band_multiplier)
    details = dict(close=current["close"], close_previous=previous["close"],
        mean=current["mean"], mean_previous=previous["mean"],
        sigma=current["sigma"], sigma_previous=previous["sigma"],
        atr=float(atr["value"]), atr_previous=atr_previous["value"],
        scale=scale0, scale_previous=scale1, band_multiplier=float(band_multiplier),
        first=int(rows[0, 0]), last=int(rows[-1, 0]),
        current_sha256=current["sha256"], previous_sha256=previous["sha256"],
        zero_volumes=current["zero_volumes"], zero_volumes_previous=previous["zero_volumes"])
    return dict(valid=True, direction=int(direction),
                reason="vwap_reentry" if direction else "vwap_no_reentry", details=details)


def exit_state(candles, now, direction):
    """State condition; no ATR, dispersion, fresh crossing or previous25th row."""
    state = vwap_state(candles, now, dispersion=False)
    if state is None or direction not in (-1, 1):
        return dict(valid=False, exit=False, details={})
    return dict(valid=True, exit=bool(direction * (state["close"] - state["mean"]) >= 0),
                details=state)


def self_checks():
    """Pure algebra/window checks; broker/time priorities remain common checks."""
    count = 0

    def check(value):
        nonlocal count
        assert value
        count += 1

    now = 25 * BAR
    flat = np.array([[i * BAR, 100., 100., 101., 99., 1.] for i in range(25)])
    state = vwap_state(flat, now)
    check(abs(state["mean"] - 100.) < 1e-12)
    check(state["sigma"] < 1e-12)
    check(state["first"] == BAR and state["last"] == 24 * BAR)
    weighted = flat.copy()
    for i in range(25):
        p = 100. + i
        weighted[i, 1:5] = [p, p, p + 1., p - 1.]
        weighted[i, 5] = i + 1.
    oracle_mean = sum((i + 1.) * (100. + i) for i in range(1, 25)) / sum(range(2, 26))
    oracle_var = sum((i + 1.) * (100. + i - oracle_mean) ** 2 for i in range(1, 25)) / sum(range(2, 26))
    result = vwap_state(weighted, now)
    check(abs(result["mean"] - oracle_mean) < 1e-12)
    check(abs(result["sigma"] - math.sqrt(oracle_var)) < 1e-12)
    scaled = weighted.copy()
    scaled[:, 5] *= 8.
    scaled_result = vwap_state(scaled, now)
    check(result["mean"] == scaled_result["mean"])
    check(result["sigma"] == scaled_result["sigma"])
    large = flat.copy()
    large[:, 5] = 1e308
    check(vwap_state(large, now) is not None)
    single = flat.copy()
    single[:, 5] = 0.
    single[-1, 5] = 3.
    check(vwap_state(single, now)["mean"] == 100.)
    check(vwap_state(single, now)["sigma"] == 0.)
    check(vwap_state(single, now)["zero_volumes"] == 23)
    all_zero = single.copy()
    all_zero[-1, 5] = 0.
    check(vwap_state(all_zero, now) is None)
    # One prior outlier then a recovering close; volume stays positive and unchanged.
    setup = flat.copy()
    setup[-2, 1:5] = [80., 80., 81., 79.]
    setup[-1, 1:5] = [90., 90., 91., 89.]
    atr = atr_window(setup, now)
    signal = features(setup, now, atr)
    check(signal["valid"] and signal["direction"] == 1)
    mirror = setup.copy()
    mirror[:, 1] = 200. - setup[:, 1]
    mirror[:, 2] = 200. - setup[:, 2]
    mirror[:, 3] = 200. - setup[:, 4]
    mirror[:, 4] = 200. - setup[:, 3]
    check(features(mirror, now, atr_window(mirror, now))["direction"] == -1)
    check(signal["details"]["atr_previous"] == atr_window(setup, now - BAR)["value"])
    check(signal["details"]["mean_previous"] == vwap_state(setup[:-1], now - BAR)["mean"])
    check(entry_direction(96., 95., 100., 100., 2., 2., 2.) == 1)
    check(entry_direction(104., 105., 100., 100., 2., 2., 2.) == -1)
    check(entry_direction(96., 96., 100., 100., 2., 2., 2.) == 0)
    check(entry_direction(100., 95., 100., 100., 2., 2., 2.) == 0)
    check(entry_direction(100., 105., 100., 100., 2., 2., 2.) == 0)
    check(entry_direction(95., 94., 100., 100., 2., 2., 2.) == 0)
    check(entry_direction(105., 106., 100., 100., 2., 2., 2.) == 0)
    check(entry_direction(96., 95., 100., 110., 2., 2., 2.) == 1)
    check(entry_direction(95., 95., 100., 110., 3., 2., 2.) == 0)
    check(features(setup, now, atr, 1.8)["valid"])
    check(features(setup, now, atr, 2.2)["valid"])
    future = np.array([[now, 100., 100., 101., 99., float("nan")]])
    check(features(np.vstack((setup, future)), now, atr) == signal)
    older = flat.copy()
    older[:, 0] -= 25 * BAR
    check(features(np.vstack((older, setup)), now, atr) == signal)
    original = setup.copy()
    features(setup, now, atr)
    check(np.array_equal(setup, original))
    check(not features(setup[-24:], now, atr)["valid"])
    check(exit_state(flat[-24:], now, 1)["valid"])
    check(exit_state(single[-24:], now, 1)["exit"])
    check(exit_state(single[-24:], now, -1)["exit"])
    check(not exit_state(setup[-24:], now, 1)["exit"])
    check(exit_state(setup[-24:], now, -1)["exit"])
    check(not exit_state(flat[-23:], now, 1)["valid"])
    check(not features(setup, now + 1, atr)["valid"])
    check(not features(setup, now, None)["valid"])
    check(not features(setup, now, atr_window(setup, now, 1))["valid"])
    check(not features(setup[:, :5], now, atr)["valid"])
    for column, value in ((0, 3 * BAR), (1, 0.), (2, float("nan")),
                          (3, 50.), (4, 150.), (5, -1.), (5, float("inf"))):
        bad = setup.copy()
        bad[2, column] = value
        check(not features(bad, now, atr)["valid"])
    bad = setup.copy()
    bad[:, 5] = 0.
    check(not features(bad, now, atr)["valid"])
    bad = setup.copy()
    bad[-1, 5] = 0.
    check(features(bad, now, atr)["valid"])
    for k in (0., -1., float("nan"), float("inf")):
        check(not features(setup, now, atr, k)["valid"])
    check(len("V5_FEATURES " + json.dumps(dict(time=int(now), line="VWAP", **signal),
                                        allow_nan=False, separators=(",", ":"))) <= 1900)
    check("sigma" not in exit_state(flat, now, 1)["details"])
    return dict(status="passed", assertions=count)
```

### strategies/ResearchV5Base4h/cross_features.py

SHA256 5df66fdb107fe3f16484ee5cd1ca91c121c4c8bea0095e3fd95799a354f5e1e0.

```python
"""Finite four-hour SMA crosses; no state, engine IO, ATR or OI in exit signals."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV5Base4h import BAR, closed_window


def _periods_valid(fast_period, slow_period):
    return (isinstance(fast_period, int) and not isinstance(fast_period, bool) and
            isinstance(slow_period, int) and not isinstance(slow_period, bool) and
            0 < fast_period < slow_period)


def _mean(values):
    # Scale before summation: a finite mean need not have a representable raw sum.
    value = math.fsum(float(x) / len(values) for x in values)
    return value if math.isfinite(value) else None


def _direction(fast_now, fast_previous, slow_now, slow_previous):
    """Equality is allowed on the prior bar, never on the current bar."""
    if fast_previous <= slow_previous and fast_now > slow_now:
        return 1
    if fast_previous >= slow_previous and fast_now < slow_now:
        return -1
    return 0


def cross_state(candles, now, fast_period=20, slow_period=80):
    """ATR-independent entry/exit cross; each average has its own finite window."""
    if not _periods_valid(fast_period, slow_period):
        return dict(valid=False, direction=0, reason="periods_invalid",
                    details=dict(reason="periods_invalid"))
    rows = closed_window(candles, now, slow_period + 1)
    if rows is None:
        return dict(valid=False, direction=0, reason="window_invalid",
                    details=dict(reason="window_invalid"))
    closes = rows[:, 2]
    try:
        fast_now = _mean(closes[-fast_period:])
        fast_previous = _mean(closes[-fast_period-1:-1])
        slow_now = _mean(closes[-slow_period:])
        slow_previous = _mean(closes[:-1])
    except (OverflowError, ValueError):
        # Invalid arithmetic blocks a signal; it is never converted to a trend.
        fast_now = fast_previous = slow_now = slow_previous = None
    if any(x is None for x in (fast_now, fast_previous, slow_now, slow_previous)):
        return dict(valid=False, direction=0, reason="mean_invalid",
                    details=dict(reason="mean_invalid"))
    direction = _direction(fast_now, fast_previous, slow_now, slow_previous)
    reason = "setup" if direction else "no_setup"
    digest = hashlib.sha256(json.dumps(rows[:, :5].tolist(),
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    details = dict(reason=reason, fast_period=fast_period, slow_period=slow_period,
        fast_now=fast_now, fast_previous=fast_previous,
        slow_now=slow_now, slow_previous=slow_previous,
        first=int(rows[0, 0]), last=int(rows[-1, 0]), bars=slow_period + 1,
        bar_ms=BAR, sha256=digest)
    return dict(valid=True, direction=int(direction), reason=reason, details=details)


def features(candles, now, atr, fast_period=20, slow_period=80):
    result = cross_state(candles, now, fast_period, slow_period)
    if not result["valid"]:
        return result
    value = atr.get("value") if isinstance(atr, dict) else None
    if (isinstance(value, bool) or not isinstance(value, (int, float, np.integer, np.floating)) or
            not math.isfinite(value) or value <= 0):
        # This check belongs only to new exposure. Exit crosses remain usable.
        return dict(valid=False, direction=0, reason="atr_invalid",
                    details=dict(reason="atr_invalid"))
    return result


def self_checks():
    """Deterministic algebra, sign symmetry and window/future independence; no IO."""
    count = 0

    def check(value):
        nonlocal count
        assert bool(value)
        count += 1

    def candles(closes, first=0):
        closes = np.asarray(closes, dtype=float)
        return np.column_stack((np.arange(len(closes)) * BAR + first,
            closes, closes, closes + .01, closes - .01, np.ones(len(closes))))

    def reflection(rows):
        result = rows.copy()
        result[:, 1] = 400. - rows[:, 1]
        result[:, 2] = 400. - rows[:, 2]
        result[:, 3] = 400. - rows[:, 4]
        result[:, 4] = 400. - rows[:, 3]
        return result

    atr = dict(value=2.)
    for fast_period, slow_period in ((20, 80), (18, 72), (22, 88)):
        # Flat long history, twenty (or neighboring count) weak closes, then a
        # positive close: the current fast/slow cross is fresh, not a state entry.
        prices = [100.] * (slow_period - fast_period) + [99.] * fast_period + [130.]
        rows = candles(prices)
        now = len(rows) * BAR
        original = rows.copy()
        for data, side in ((rows, 1), (reflection(rows), -1)):
            state = cross_state(data, now, fast_period, slow_period)
            result = features(data, now, atr, fast_period, slow_period)
            check(state["valid"])
            check(state["direction"] == side)
            check(result == state)
            detail = state["details"]
            check(detail["bars"] == slow_period + 1)
            check(detail["last"] + BAR == now)
            check(detail["last"] - detail["first"] == slow_period * BAR)
            for key, values in (("fast_now", data[-fast_period:, 2]),
                                ("fast_previous", data[-fast_period-1:-1, 2]),
                                ("slow_now", data[-slow_period:, 2]),
                                ("slow_previous", data[:-1, 2])):
                check(abs(detail[key] - sum(float(x) for x in values) / len(values)) < 1e-12)
            check(len(json.dumps(result, allow_nan=False)) < 1700)
            future = np.vstack((data, candles([150., 151.], first=now)))
            check(cross_state(future, now, fast_period, slow_period) == state)
            future[-2:, 1:5] *= 10.
            check(cross_state(future, now, fast_period, slow_period) == state)
            prefix = candles([90.] * 10, first=-10 * BAR)
            extended = np.vstack((prefix, data))
            check(cross_state(extended, now, fast_period, slow_period) == state)
            extended[:10, 1:5] *= 2.
            check(cross_state(extended, now, fast_period, slow_period) == state)
            prior = cross_state(extended[:-1], now - BAR, fast_period, slow_period)
            check(prior["valid"])
            check(abs(prior["details"]["fast_now"] - detail["fast_previous"]) < 1e-12)
            check(abs(prior["details"]["slow_now"] - detail["slow_previous"]) < 1e-12)
            check(cross_state(data[:-1], now, fast_period, slow_period)["valid"] is False)
            check(cross_state(data, now + 1, fast_period, slow_period)["valid"] is False)
            # ATR can prevent an entry, never the independently evaluated exit.
            check(features(data, now, None, fast_period, slow_period)["valid"] is False)
            check(cross_state(data, now, fast_period, slow_period) == state)
        check(np.array_equal(rows, original))
        flat = candles([100.] * (slow_period + 1))
        flat_state = cross_state(flat, now, fast_period, slow_period)
        check(flat_state["valid"] and flat_state["direction"] == 0)
        rising = candles(100. + np.arange(slow_period + 1))
        falling = reflection(rising)
        check(cross_state(rising, now, fast_period, slow_period)["direction"] == 0)
        check(cross_state(falling, now, fast_period, slow_period)["direction"] == 0)
    check(_direction(2., 1., 1., 1.) == 1)
    check(_direction(1., 2., 2., 2.) == -1)
    check(_direction(1., 0., 1., 1.) == 0)
    check(_direction(1., 2., 1., 1.) == 0)
    check(_direction(2., 2., 1., 1.) == 0)
    check(_direction(1., 1., 2., 2.) == 0)
    nominal = candles([100.] * 60 + [99.] * 20 + [130.])
    now = 81 * BAR
    detail = cross_state(nominal, now)["details"]
    check(abs(detail["fast_previous"] - 99.) < 1e-12)
    check(abs(detail["slow_previous"] - 99.75) < 1e-12)
    check(abs(detail["fast_now"] - 100.55) < 1e-12)
    check(abs(detail["slow_now"] - 100.125) < 1e-12)
    for value in (None, 0., -1., True, float("nan"), float("inf")):
        check(features(nominal, now, dict(value=value))["valid"] is False)
    for fast_period, slow_period in ((0, 80), (20, 20), (80, 20), (20., 80), (True, 80)):
        check(cross_state(nominal, now, fast_period, slow_period)["valid"] is False)
    for column, value in ((2, float("nan")), (2, float("inf")), (3, 1.), (4, 1000.), (1, 0.)):
        broken = nominal.copy()
        broken[-1, column] = value
        check(cross_state(broken, now)["valid"] is False)
        check(features(broken, now, atr)["valid"] is False)
    broken = nominal.copy()
    broken[-10, 0] -= BAR
    check(cross_state(broken, now)["valid"] is False)
    check(cross_state(nominal[-80:], now)["valid"] is False)
    # The raw sum would overflow; scaled finite arithmetic must remain JSON-safe.
    huge = np.tile([0., 1e308, 1e308, 1e308, 1e308, 1.], (81, 1))
    huge[:, 0] = np.arange(81) * BAR
    large_state = cross_state(huge, now)
    check(large_state["valid"])
    check(large_state["direction"] == 0)
    check(len(json.dumps(large_state, allow_nan=False)) < 1700)
    return dict(status="passed", assertions=count)
```

### strategies/ResearchV6Base4h/efficiency_features.py

SHA256 ecfcc5fe4b77a2faee9edcdaea1bd391e33ec7fe73112e48718a2a8b90790bcf.

```python
"""Finite directional path efficiency; pure algebra, with no engine state or IO."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV6Base4h import BAR, closed_window


def _digest(rows):
    return hashlib.sha256(json.dumps(rows[:, :5].tolist(),
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def efficiency24(candles, now):
    """Twenty-four deltas use exactly25closed prices; a flat path is neutral."""
    rows = closed_window(candles, now, 25)
    if rows is None:
        return dict(valid=False, value=None, reason="efficiency_window_invalid")
    closes = [float(value) for value in rows[:, 2]]
    deltas = [right - left for left, right in zip(closes, closes[1:])]
    displacement = closes[-1] - closes[0]
    if not math.isfinite(displacement) or not all(math.isfinite(x) for x in deltas):
        return dict(valid=False, value=None, reason="efficiency_arithmetic_invalid")
    scale = max(abs(x) for x in deltas)
    # Common normalization preserves the ratio while avoiding an overflowing raw sum.
    if scale == 0:
        normalized_path = normalized_displacement = value = 0.
    else:
        normalized_path = math.fsum(abs(x) / scale for x in deltas)
        normalized_displacement = displacement / scale
        if (not math.isfinite(normalized_path) or normalized_path <= 0 or
                not math.isfinite(normalized_displacement)):
            return dict(valid=False, value=None, reason="efficiency_arithmetic_invalid")
        value = normalized_displacement / normalized_path
    if not math.isfinite(value):
        return dict(valid=False, value=None, reason="efficiency_arithmetic_invalid")
    return dict(valid=True, value=float(value),
        reason="efficiency_flat" if scale == 0 else "efficiency_valid",
        displacement=float(displacement), step_scale=float(scale),
        normalized_displacement=float(normalized_displacement),
        normalized_path=float(normalized_path), first=int(rows[0, 0]),
        last=int(rows[-1, 0]), bars=25, sha256=_digest(rows))


def _cross_direction(current, previous, threshold):
    if previous <= threshold and current > threshold:
        return 1
    if previous >= -threshold and current < -threshold:
        return -1
    return 0


def features(candles, now, atr, threshold=.35):
    if (isinstance(threshold, (bool, str)) or
            not isinstance(threshold, (int, float, np.integer, np.floating)) or
            not math.isfinite(threshold) or not 0 < threshold < 1):
        return dict(valid=False, direction=0, reason="efficiency_threshold_invalid", details={})
    # A fresh crossing needs two independent25-close windows: their union is26.
    rows = closed_window(candles, now, 26)
    if rows is None:
        return dict(valid=False, direction=0, reason="efficiency_window_invalid", details={})
    try:
        atr_valid = (isinstance(atr, dict) and math.isfinite(atr["value"]) and atr["value"] > 0)
    except (KeyError, TypeError, ValueError):
        atr_valid = False
    if not atr_valid:
        return dict(valid=False, direction=0, reason="efficiency_atr_invalid", details={})
    current = efficiency24(candles, now)
    previous = efficiency24(candles, now - BAR)
    if not current["valid"] or not previous["valid"]:
        return dict(valid=False, direction=0, reason="efficiency_arithmetic_invalid", details={})
    direction = _cross_direction(current["value"], previous["value"], float(threshold))
    reason = "efficiency_setup" if direction else "efficiency_no_cross"
    details = dict(threshold=float(threshold), current=current, previous=previous,
        first=int(rows[0, 0]), last=int(rows[-1, 0]), bars=26, sha256=_digest(rows))
    return dict(valid=True, direction=int(direction), reason=reason, details=details)


def self_checks():
    """Independent finite-path oracles, boundaries and causal mutation checks."""
    count = 0

    def check(condition):
        nonlocal count
        assert bool(condition)
        count += 1

    def candles(closes, first=0):
        closes = np.asarray(closes, dtype=float)
        return np.column_stack((np.arange(len(closes))*BAR + first,
            closes, closes, closes*1.001, closes*.999, np.ones(len(closes))))

    def oracle(values):
        # Raw unnormalized arithmetic is independent of the scaled implementation.
        changes = [float(right - left) for left, right in zip(values, values[1:])]
        total = math.fsum(abs(x) for x in changes)
        return 0. if total == 0 else (float(values[-1]) - float(values[0])) / total

    closes = 100. + np.cumsum([0.] + [1., -1.]*12 + [14.])
    long = candles(closes)
    now = 26*BAR
    atr = dict(value=2.)
    short = long.copy()
    short[:, 1] = 400. - long[:, 1]
    short[:, 2] = 400. - long[:, 2]
    short[:, 3] = 400. - long[:, 4]
    short[:, 4] = 400. - long[:, 3]
    for case, expected in ((long, 1), (short, -1)):
        result = features(case, now, atr)
        check(result["valid"] and result["direction"] == expected)
        check(result["reason"] == "efficiency_setup")
        check(result["details"]["bars"] == 26)
        check(result["details"]["current"]["bars"] == 25)
        check(result["details"]["previous"]["bars"] == 25)
        check(len("V6_FEATURES " + json.dumps(dict(time=now, line="EFFICIENCY", **result),
              separators=(",", ":"), allow_nan=False)) <= 1900)
        for offset in (0, 1):
            state = efficiency24(case, now-offset*BAR)
            values = case[-25-offset:len(case)-offset if offset else None, 2]
            check(abs(state["value"] - oracle(values)) < 1e-12)
            check(state["last"]+BAR == now-offset*BAR)
            check(state["first"] == now-(25+offset)*BAR)
            mutated = case.copy()
            mutated[:len(case)-25-offset, 1:5] *= 1.1
            check(efficiency24(mutated, now-offset*BAR) == state)
        check(efficiency24(case[:-1], now-BAR) == efficiency24(case, now-BAR))
        check(features(case, now, atr, .315)["direction"] == expected)
        check(features(case, now, atr, .385)["direction"] == 0)
        check(features(case[-25:], now, atr)["valid"] is False)
        check(efficiency24(case[-25:], now)["valid"])
        future = candles([500., 600.], first=now)
        appended = np.vstack((case, future))
        check(features(appended, now, atr) == result)
        appended[-2:, 1:5] = float("nan")
        check(features(appended, now, atr) == result)
        older = candles(np.arange(40)+30., first=-40*BAR)
        extended = np.vstack((older, case))
        check(features(extended, now, atr) == result)
        extended[:40, 1:5] *= 2.
        check(features(extended, now, atr) == result)
        scaled = case.copy()
        scaled[:, 1:5] *= 2.
        check(abs(efficiency24(scaled, now)["value"] - result["details"]["current"]["value"]) < 1e-12)
        translated = case.copy()
        translated[:, 1:5] += 50.
        check(abs(efficiency24(translated, now)["value"] - result["details"]["current"]["value"]) < 1e-12)
        check(features(translated, now, atr)["direction"] == expected)
    check(abs(efficiency24(long, now)["value"] - 13./37.) < 1e-12)
    flat = candles([100.]*26)
    check(efficiency24(flat, now)["value"] == 0.)
    check(efficiency24(flat, now)["reason"] == "efficiency_flat")
    check(features(flat, now, atr)["valid"])
    check(features(flat, now, atr)["direction"] == 0)
    for values, expected in ((np.arange(26)+100., 1.), (200.-np.arange(26), -1.)):
        case = candles(values)
        check(efficiency24(case, now)["value"] == expected)
        check(features(case, now, atr)["direction"] == 0)
    zigzag = candles([100.] + [110., 100.]*11 + [110., 124.])
    straight = candles(np.arange(25)+100.)
    check(zigzag.shape[0] == 25)
    check(efficiency24(zigzag, 25*BAR)["displacement"] == efficiency24(straight, 25*BAR)["displacement"])
    check(efficiency24(zigzag, 25*BAR)["value"] < efficiency24(straight, 25*BAR)["value"])
    for h in (.315, .35, .385):
        check(_cross_direction(h+.01, h, h) == 1)
        check(_cross_direction(h, h-.01, h) == 0)
        check(_cross_direction(h+.01, h+.01, h) == 0)
        check(_cross_direction(-h-.01, -h, h) == -1)
        check(_cross_direction(-h, -h+.01, h) == 0)
        check(_cross_direction(-h-.01, -h-.01, h) == 0)
    for threshold in (0., 1., -.35, float("nan"), float("inf"), None, True, "0.35"):
        check(features(long, now, atr, threshold)["valid"] is False)
    for risk in (None, {}, dict(value=0.), dict(value=float("nan")), dict(value=float("inf"))):
        check(features(long, now, risk)["valid"] is False)
    for column, value in ((2, float("nan")), (1, 0.), (3, 1.), (4, 1000.), (0, now-2*BAR)):
        broken = long.copy()
        broken[-1, column] = value
        check(features(broken, now, atr)["valid"] is False)
        check(efficiency24(broken, now)["valid"] is False)
    check(features(long[:-1], now, atr)["valid"] is False)
    check(features(long, now+1, atr)["valid"] is False)
    check(efficiency24(long[-24:], now)["valid"] is False)
    # The raw path sum would overflow; scaling preserves a finite neutral result.
    large = candles([1e307 if i%2 == 0 else 9e307 for i in range(25)])
    large_state = efficiency24(large, 25*BAR)
    check(large_state["valid"] and large_state["value"] == 0.)
    check(large_state["normalized_path"] == 24.)
    check(len(json.dumps(large_state, allow_nan=False)) < 1000)
    original = long.copy()
    features(long, now, atr)
    check(np.array_equal(original, long))
    return dict(status="passed", assertions=count)
```

### strategies/ResearchV6Base4h/nr7_features.py

SHA256 7eb379f9934be3d544736c68a1ae4c73864f907212c0b9ad9efcffe91afea512.

```python
"""Causal NR7 contraction and next-close expansion; no engine state or IO."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV6Base4h import BAR, atr_window, closed_window


def features(candles, now, atr, narrow_window=7):
    """Rank only prior bars; current close determines the exclusive direction."""
    invalid = dict(valid=False, direction=0, reason="nr7_data_invalid", details={})
    if (isinstance(narrow_window, bool) or not isinstance(narrow_window, int) or
            narrow_window < 2):
        return dict(valid=False, direction=0, reason="nr7_parameter_invalid", details={})
    rows = closed_window(candles, now, narrow_window + 1)
    if rows is None:
        return invalid
    try:
        # Risk must use current arithmetic14TR, not the pre-expansion offset.
        if (atr is None or atr["offset_bars"] != 0 or
                atr["first"] != now - 15 * BAR or atr["last"] != now - BAR or
                not math.isfinite(atr["value"]) or atr["value"] <= 0):
            return dict(valid=False, direction=0, reason="nr7_atr_invalid", details={})
    except (KeyError, TypeError, ValueError):
        return dict(valid=False, direction=0, reason="nr7_atr_invalid", details={})
    prior = rows[:-1]
    ranges = prior[:, 3] - prior[:, 4]
    if not np.all(np.isfinite(ranges)) or np.any(ranges < 0):
        return invalid
    setup_range = float(ranges[-1])
    comparison_min = float(np.min(ranges[:-1]))
    narrow = bool(setup_range < comparison_min)
    close, upper, lower = (float(rows[-1, 2]), float(prior[-1, 3]), float(prior[-1, 4]))
    direction = (1 if close > upper else -1 if close < lower else 0) if narrow else 0
    # Zero range may qualify strictly; equal minima do not. No epsilon changes ranking.
    reason = "nr7_breakout" if direction else "nr7_no_breakout" if narrow else "nr7_not_narrow"
    digest = hashlib.sha256(json.dumps(rows[:, :5].tolist(),
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    details = dict(narrow_window=narrow_window, first=int(rows[0, 0]),
        last=int(rows[-1, 0]), bars=narrow_window + 1, sha256=digest,
        setup_time=int(prior[-1, 0]), setup_high=upper, setup_low=lower,
        setup_range=setup_range, comparison_min=comparison_min,
        prior_ranges=[float(x) for x in ranges], narrow=narrow, close=close)
    return dict(valid=True, direction=direction, reason=reason, details=details)


def self_checks():
    """Synthetic algebra and clock checks; no claim about simulated broker fills."""
    count = 0

    def check(condition):
        nonlocal count
        assert condition
        count += 1

    def fixture():
        rows = np.array([[i*BAR, 100., 100., 102., 98., 1.] for i in range(15)])
        rows[-2, 3:5] = (100.5, 99.5)
        rows[-1, 2:5] = (103., 104., 99.)
        return rows

    now = 15 * BAR
    long = fixture()
    short = long.copy()
    short[:, 1] = 400. - long[:, 1]
    short[:, 2] = 400. - long[:, 2]
    short[:, 3] = 400. - long[:, 4]
    short[:, 4] = 400. - long[:, 3]
    for rows, expected in ((long, 1), (short, -1)):
        original = rows.copy()
        atr = atr_window(rows, now)
        result = features(rows, now, atr)
        check(result["valid"] and result["direction"] == expected)
        check(result["reason"] == "nr7_breakout")
        check(result["details"]["narrow"])
        check(result["details"]["setup_range"] == 1.)
        check(result["details"]["comparison_min"] == 4.)
        check(result["details"]["prior_ranges"] == [4.]*6 + [1.])
        check(result["details"]["first"] == now - 8*BAR)
        check(result["details"]["last"] == now - BAR)
        check(result["details"]["setup_time"] == now - 2*BAR)
        check(np.array_equal(rows, original))
        check(len("V6_FEATURES " + json.dumps(dict(time=now, line="NR7", **result),
              separators=(",", ":"), allow_nan=False)) <= 1900)
        for n in (6, 7, 8):
            item = features(rows, now, atr, n)
            check(item["direction"] == expected)
            check(item["details"]["bars"] == n + 1)
        prefix = rows[:4].copy()
        prefix[:, 0] -= 19 * BAR
        extended = np.vstack((prefix, rows))
        check(features(extended, now, atr) == result)
        extended[:4, 1:5] *= 1.5
        check(features(extended, now, atr) == result)
        future = np.array([[now, 1., float("nan"), float("inf"), -1., 0.]])
        extended = np.vstack((rows, future))
        check(features(extended, now, atr) == result)
        # Pattern depends on eight bars; ATR's independently frozen15-bar provenance stays supplied.
        check(features(rows[-8:], now, atr) == result)
        check(features(rows[-7:], now, atr)["valid"] is False)
        check(features(rows, now + 1, atr)["valid"] is False)
        check(features(rows[:-1], now, atr)["valid"] is False)
        changed = rows.copy()
        changed[-3, 3:5] = (100.5 if expected == 1 else 300.5,
                                  99.5 if expected == 1 else 299.5)
        check(features(changed, now, atr)["reason"] == "nr7_not_narrow")
    atr = atr_window(long, now)
    for value in (100.5, 99.5, 100.):
        changed = long.copy()
        changed[-1, 2] = value
        check(features(changed, now, atr)["direction"] == 0)
        check(features(changed, now, atr)["reason"] == "nr7_no_breakout")
    # B0 can traverse both previous extrema; only its final close decides, without retrofill.
    check(long[-1, 3] > long[-2, 3] and long[-1, 4] < long[-2, 4])
    check(features(long, now, atr)["direction"] == 1)
    changed = long.copy()
    changed[-1, 2] = 99.
    check(features(changed, now, atr)["direction"] == -1)
    changed[-1, 2] = 100.
    check(features(changed, now, atr)["direction"] == 0)
    # The expansion bar is never allowed to disqualify the prior NR7 contraction.
    changed = long.copy()
    changed[-1, 1:5] = (103., 103., 103.1, 102.9)
    check(features(changed, now, atr)["direction"] == 1)
    changed = long.copy()
    changed[-8, 3:5] = (100.25, 99.75)
    check(features(changed, now, atr, 6)["direction"] == 1)
    check(features(changed, now, atr, 7)["reason"] == "nr7_not_narrow")
    changed = long.copy()
    changed[-9, 3:5] = (100.25, 99.75)
    check(features(changed, now, atr, 7)["direction"] == 1)
    check(features(changed, now, atr, 8)["reason"] == "nr7_not_narrow")
    changed = long.copy()
    changed[-2, 1:5] = (100., 100., 100., 100.)
    check(features(changed, now, atr)["direction"] == 1)
    flat = np.array([[i*BAR, 100., 100., 100., 100., 1.] for i in range(15)])
    check(features(flat, now, atr)["reason"] == "nr7_not_narrow")
    check(atr_window(flat, now) is None)
    for column, value in ((0, now-3*BAR), (2, float("nan")), (3, 99.),
                          (4, 101.), (1, 0.)):
        changed = long.copy()
        changed[-2, column] = value
        check(features(changed, now, atr)["valid"] is False)
    for value in (0., -1., float("nan"), float("inf")):
        bad_atr = dict(atr, value=value)
        check(features(long, now, bad_atr)["reason"] == "nr7_atr_invalid")
    for key, value in (("offset_bars", 1), ("first", atr["first"]+BAR),
                       ("last", atr["last"]+BAR)):
        check(features(long, now, dict(atr, **{key:value}))["valid"] is False)
    check(features(long, now, None)["valid"] is False)
    for n in (0, 1, 7., True, None):
        check(features(long, now, atr, n)["reason"] == "nr7_parameter_invalid")
    # ATR supplied to entries is causal and includes the expansion's true range.
    previous_atr = atr_window(long, now, 1)
    check(previous_atr is None)
    sixteen = np.vstack((long[:1], long))
    sixteen[0, 0] -= BAR
    previous_atr = atr_window(sixteen, now, 1)
    check(previous_atr["value"] != atr["value"])
    check(features(sixteen, now, previous_atr)["reason"] == "nr7_atr_invalid")
    return dict(status="passed", assertions=count)
```

## R8 X801–X805: extractos exactos, NO fuentes completas

Los hashes identifican el contenido completo recibido; se reproduce sólo cada helper de setup y, para X805, su helper M1. No presentar estos extractos como snapshots íntegros; las hojas B no importarán estas recetas.

### BTCExploreR801

SHA256 fuente completa 3ce523dd958a8dbee3e1f96cca92b24a89d19b619343a67e1ab2b7a678a29861. Extracto exacto desde _research_setup hasta EOF:

```python
    def _research_setup(c):
        # A single dominant-volume auction replaces the dispersed cohort cost.
        s, t = c[-2], c[-1]
        window = c[-13:-1]
        k = len(window) - 1 - int(np.argmax(window[::-1, 5]))
        anchor = window[k]
        cost = float(np.mean(anchor[[3, 4, 2]]))
        return bool(anchor[2] > anchor[1] and s[2] > c[-14, 2]
                    and s[2] >= cost and t[2] < t[1] and t[2] < cost)
```

### BTCExploreR802

SHA256 fuente completa f9f4bb32b870d1a53bdf031f32c73582610cbadb0e1dac79b7994e9a23216064. Extracto exacto desde _research_setup hasta EOF:

```python
    def _research_setup(c):
        # Intersection of six traded ranges is a consensus zone, not one inside bar.
        s, t = c[-2], c[-1]
        window = c[-7:-1]
        lower, upper = float(np.max(window[:, 4])), float(np.min(window[:, 3]))
        return bool(lower < upper and lower <= s[2] <= upper
                    and t[2] < t[1] and t[2] < lower)
```

### BTCExploreR803

SHA256 fuente completa 3ba39ad64e63accf6af6dc2c0003fe59ba63e7526162d76aff2118f0b1c15e2e. Extracto exacto desde _research_setup hasta EOF:

```python
    def _research_setup(c):
        # A failed recovery of the strongest red body anchors the entire sequence.
        s, t = c[-2], c[-1]
        window = c[-13:-1]
        bodies = window[:, 2] - window[:, 1]
        k = len(window) - 1 - int(np.argmin(bodies[::-1]))
        impulse = window[k]
        if impulse[2] >= impulse[1] or k == len(window) - 1:
            return False
        midpoint = float((impulse[1] + impulse[2]) / 2)
        recovered = window[k + 1:, 2]
        return bool(np.any(recovered >= midpoint) and not np.any(recovered > impulse[1])
                    and s[2] >= midpoint and t[2] < t[1] and t[2] < midpoint)
```

### BTCExploreR804

SHA256 fuente completa 86bcb4297fed564346c949b7f02886a062134b20a75db32d35c657b6184c6692. Extracto exacto desde _research_setup hasta EOF:

```python
    def _research_setup(c):
        # Ordered close innovations test a leadership change, unlike close location.
        s, t = c[-2], c[-1]
        window = c[-13:-1]
        innovations = window[:, 2] - c[-14:-2, 2]
        pressure = window[:, 5] * innovations
        return bool(np.sum(pressure[:6]) > 0 and np.sum(pressure[6:]) < 0
                    and s[2] > c[-14, 2] and t[2] < t[1]
                    and t[2] < min(s[2], s[1]))
```

### BTCExploreR805

SHA256 fuente completa 246150464d5636e3a107ba8ad69eb63d3ca98de4d1410d75e12044ef0d36e08a. Extracto exacto desde _research_setup hasta EOF:

```python
    def _research_setup(self, c):
        s, t = c[-2], c[-1]
        if not (s[2] > c[-14, 2] and t[2] < t[1]):
            return False
        minute = self.get_candles(self.exchange, self.symbol, '1m')
        valid, reason, fraction = self._volume_clock_setup(
            minute, int(t[0]), int(t[0]) + 14400000, float(t[2]))
        audit = self.vars.setdefault('research_m1_audit', {})
        audit[reason] = audit.get(reason, 0) + 1
        if fraction is not None:
            # Aggregate diagnostics only; never used to accept or reject a setup.
            audit['partition_count'] = audit.get('partition_count', 0) + 1
            audit['fraction_sum'] = audit.get('fraction_sum', 0.0) + fraction
            audit['fraction_min'] = min(audit.get('fraction_min', fraction), fraction)
            audit['fraction_max'] = max(audit.get('fraction_max', fraction), fraction)
        return valid

    @staticmethod
    def _volume_clock_setup(minute, start, end, close):
        # The boundary minute belongs wholly to group one. Its OHLC is not split.
        if minute.ndim != 2 or minute.shape[1] < 6:
            return False, 'missing_shape', None
        rows = minute[(minute[:, 0] >= start) & (minute[:, 0] < end)]
        if (len(rows) != 240 or int(rows[0, 0]) != start
                or int(rows[-1, 0]) + 60000 != end
                or not np.all(np.diff(rows[:, 0]) == 60000)):
            return False, 'missing_clock', None
        if (not np.all(np.isfinite(rows[:, :6]))
                or not np.all(rows[:, 1:5] > 0) or not np.all(rows[:, 5] >= 0)
                or not np.all(rows[:, 4] <= np.minimum(rows[:, 1], rows[:, 2]))
                or not np.all(np.maximum(rows[:, 1], rows[:, 2]) <= rows[:, 3])):
            return False, 'corrupt', None
        if float(rows[-1, 2]) != close:
            return False, 'close_mismatch', None
        volume = rows[:, 5]
        total = float(np.sum(volume))
        if total <= 0:
            return False, 'zero_volume', None
        boundary = int(np.searchsorted(np.cumsum(volume), 0.5 * total, side='left'))
        first, second = rows[:boundary + 1], rows[boundary + 1:]
        v1, v2 = float(np.sum(first[:, 5])), float(np.sum(second[:, 5]))
        if len(first) == 0 or len(second) == 0 or v1 <= 0 or v2 <= 0:
            return False, 'empty_partition', None
        a1 = float(np.sum(np.mean(first[:, [3, 4, 2]], axis=1) * first[:, 5]) / v1)
        a2 = float(np.sum(np.mean(second[:, [3, 4, 2]], axis=1) * second[:, 5]) / v2)
        return bool(a2 < a1 and close < np.min(first[:, 4])), 'valid', v1 / total
```

## Cierres y protocolo V1 completos recibidos

No trasladar cifras de cartera u otro riesgo como rendimiento del nuevo especialista. Estos documentos no constituyen una reauditación de todos los fills históricos ni autorizan vecinos por decepción.

### strategies/FundingOiPilot4h/reports/RESEARCH_PROTOCOL_V1.md

SHA256 8262d7f10435ae44a4ca2faea7bc61bed501a7ed2b24b8cf04a0f4cb4b77c717.

```text
# Research protocol V1 — 2026-10-20
Estado: **especificación económica congelada antes de nuevas pruebas; fase0 cerrada APTO CON LÍMITES por addendum del freeze**. No es una confirmación de implementación. No consultar resultados de estas nuevas configuraciones2024–2025 hasta congelar shortlist. No abrir2026.
El freeze técnico y registry.json de esta carpeta son parte del protocolo. La recarga local/MCP y la comprobación de fills deben cerrar fase0 antes de iniciar el lote. No cambiar reglas al implementar: cualquier ambigüedad material exige registrar una versión antes de resultados.

## Universo y convenciones comunes
Sólo BTC-USDT Binance Perpetual Futures. Datos históricos y hashes exactos del freeze, nunca sustitución automática. Intervalo común [2020-09-01,2026-01-01). Velas ejecución1m; decisión4h UTC sobre vela ya cerrada. Sin ML, random chunks, pyramiding ni exposición fuera de una ruta.
Capital10000USDT inicial PLANO por sesión; isolated3x; fee nominal .00045 por lado. Funding contable ON en TODAS las ablaciones, incluso P. Slippage nominal0bps, estrés de fills5/10bps según matriz abajo. No presentar el nominal sin slippage como una estimación exhaustiva de costes reales.
Warmup240velas4h sin operar; rango UTC previo y retornos pueden usar esas velas. Funding history sólo eventos publicados. OI24h se inicializa mediante las decisiones del período de evaluación: primeras seis observaciones4h no tienen referencia24h. No backfill ficticio, ni usar un archivo anterior a septiembre2020.
Se permite una entrada efectiva por día UTC y sólo si plano/sin entrada pendiente. Gate de entrada explícito start<T<finish con T=reloj de decisión; no abrir en el borde final. Gestión protectora siempre activa. El cierre final forzado corresponde al fold, con fees y slippage de market si aplica.
Stop a2% del precio realmente ejecutado; target4%; market exit al primer cierre4h donde edad>=24h. No mover stops/TP, no parciales ni piramidar. En el modelo5m/4h cerrado la resolución temporal debe declararse; no prometer salida subminuto.
Sizing idéntico al piloto: C=available_margin antes de entrar, p=precio de decisión, d=+1long/−1short, stop_pre=p(1−d*.02), L=abs(p−stop_pre)+fee*(p+stop_pre).
notional=min(C, .02*C/L*p); qty=floor8(notional/p). No multiplicar por leverage. Funding y slippage no están dentro del presupuesto2%; reportar pérdidas reales al stop y exceso por fricción. Con slippage, stop/target basados en fill pueden cambiar riesgo y trayectoria: no restaurar retrospectivamente el sizing nominal.

## Variables causales
En T usar sólo velas con open_time+4h<=T. c=cierre de la última; c_prev=cierre de la anterior; c24=cierre de la barra terminada exactamente T−24h. Si falta una barra/referencia exigida no habilitar entrada de esa familia.
D=floorUTCday(T). H/L=máximo high/mínimo low de las seis velas4h únicas del día[D−24h,D). Si son incompletas, no señal.
Funding visible: eventos con available_at<=T, ordenados por timestamp original. r0=último, r−1=anterior.
z0=(r0−mean(30previos))/std(30previos,ddof0); actual excluido. z−1 usa los30anteriores a r−1 y lo excluye. Requerir ptp>0, std positiva finita y z finito; H1/H2 necesitan31eventos; H3 necesita32. No usar funding estimado próximo ni signo de feature importance ML.
OI0=valor causal disponible en T bajo lag6m/max_age10m; OI24=valor efectivamente observado en la decisión T−24h. Requiere valor>0 en ambos y timestamp de referencia exacto, sin rellenar huecos. Gate OI=OI0>OI24, igual para long y short. No interpreta OI como dirección.
Un gate de señal apagado no exige datos de esa señal. La contabilidad funding permanece obligatoria.

## Tres mecanismos; exactamente12especificaciones
Cada familia tiene cuatro ablaciones P,PF,POI,PFOI. PF añade sólo gate funding a P; POI añade sólo OI; PFOI ambos. Las salidas/sizing/calendario son idénticos.

| Familia | Dirección de precio P | Gate funding F |
|---|---|---|
| H1 continuación | long c>H; short c<L; en otro caso0 | bloquear long si r0>0 y z0>2; bloquear short si r0<0 y z0<−2. Datos/statística inválidos: no entrar en variantes F |
| H2 reversión de ruptura | long si c_prev<L y L<=c<=H; short si c_prev>H y L<=c<=H; otro caso0 | long sólo r0<0,z0<−2; short sólo r0>0,z0>2 |
| H3 normalización y régimen | long si c>c24 y c>c_prev; short si c<c24 y c<c_prev; otro caso0 | long si r−1<0,z−1<−2,r−1<r0<=0,abs(z0)<=2; short si r−1>0,z−1>2,0<=r0<r−1,abs(z0)<=2 |

IDs: H1_P,H1_PF,H1_POI,H1_PFOI; H2_P,H2_PF,H2_POI,H2_PFOI; H3_P,H3_PF,H3_POI,H3_PFOI.
No se agregan thresholds, transformaciones OI ni otro timeframe.30eventos,2z y OI24h son elecciones informadas por legacy/pilotos ya vistos, no estimaciones independientes. H2/H3 son hipótesis nuevas, aún sin evidencia.
No deduplicar por nombre o similitud: sólo reutilizar si código completo, lógica, warmup, boundary gate, config, datos y ventana son exactamente equivalentes. H1 no reutiliza automáticamente los pilotos: la instrumentación y gate de borde se deben comparar. Otras familias P no son iguales.
Antes de cada primer resultado capturar implementación completa e inmutable de padre/helpers/subclase, config completa, hashes, datasets, runtime y pruebas de prefijos/mutación futura. registry.json empieza SPECIFIED; no fingir hashes de código aún no escrito. El único cambio permitido sin versión es completar código que implementa literalmente estas fórmulas y su trazabilidad, antes de probarlo.

## Instrumentación obligatoria antes del lote
Persistir por mes, dirección y total: barras, oportunidades precio estando plano/con cupo diario, funding ausente, funding varianza nula/no finita, funding gate económico, OI ausente, OI stale, cero actual, inicialización, referencia inválida, gate OI no creciente, entradas y salidas; anotar denominadores. Mantener flags de causas simultáneas y una partición exclusiva de rechazo con prioridad documentada (precio→funding calidad→funding económico→OI actual→inicialización→referencia→OI económico). No sumar causas simultáneas como si fueran trades distintos.
Entradas: guardar timestamp, margen antes de orden, qty, precio de decisión/fill, stop/TP, funding/OI y sus observed/available timestamps. Fuente de cada feature, unidad y parámetros. Logs <=2000caracteres por línea, debug_mode=true. Validar conservación de conteos en un smoke técnico antes del primer lote.
Nuevas H2/H3 y sensibilidades deben pasar prefijos/mutación futura, rolling statistics y alineación4h/UTC. Las pruebas de fase0 cubren sólo funciones allí identificadas.

## Walk-forward y selección
Train empieza siempre2020-09-01 y termina al inicio de la evaluación; fin exclusivo. Cada sesión independiente,10000,plana.
Exploración E1eval2022-01-01→2022-07-01; E2eval2022-07-01→2023-01-01; E3eval2023-01-01→2023-07-01; E4eval2023-07-01→2024-01-01.
Máximo12×4×2=96sesiones económicas nominales. Un backtest activo; subir a2sólo tras respuesta estable, nunca arrancar ciegamente otra sesión ante timeout.
En cada corte ejecutar/consultar train primero. Elegible:>=30trades,neto>0,PF>=1.2,absDD<=25%. Orden: menor absDD,mayorPF,menor turnover (suma notional de fills ejecutados /10000),menor complejidad (P,PF,POI,PFOI),ID lexicográfico.
Registrar selección antes de ejecutar o consultar evaluación siguiente. Si ninguna cumple: SIN_CANDIDATA; selector plano, retorno0 durante ese semestre. Las demás ablaciones siguen siendo research diagnóstico.
Después de E1–E4 elegir como máximo2finalistas entre configuraciones seleccionadas al menos una vez y con suma de netos de sus cuatro evaluaciones>0, al menos2semestres positivos y>=30trades únicos de evaluación. Si ninguna cumple, cerrar SIN_CANDIDATA, sin fase3. Orden de shortlist: menor peor absDD entre cuatro evaluaciones,luego mayorPF agregado de trades únicos,luego menor turnover,luego simplicidad/ID. Esta selección usa desarrollo visto y se declara como tal.
Guardar FROZEN_SHORTLIST_V1.md y registry completo ANTES de abrir métricas2024–2025 de nuevas configuraciones.

Confirmación C1eval2024-01-01→2024-07-01; C2eval2024-07-01→2025-01-01; C3eval2025-01-01→2025-07-01; C4eval2025-07-01→2026-01-01.
Máximo2×4×2=16nominales. Elegir en cada train entre shortlist con el MISMO selector; pasado evaluado puede entrar en train siguiente. Sin intervención posterior ni cambio de umbrales.
No sumar resultados de train ni trades repetidos. No presentar la ganadora posterior de cada eval como seleccionada antes.2022–2023es exploración ya vista;2024–2025reserva interna del ciclo, no independencia absoluta frente al historial del usuario.

## Índice y reportes
Guardar retornos/DD por fold,meses completos,dirección,exposición,turnover,duraciones,rachas,bloqueos,precio bruto,fees,funding y saldo.
Índice del selector: iniciar10000, escalar cada curva de evaluación seleccionada por índice al comienzo/10000; si SIN_CANDIDATA, índice plano. Incluye cierres/costes de borde y supone reinversión proporcional al comienzo del siguiente semestre. No es replay continuo: cada sesión dimensionó con10000. No sumar balances ni USDTfees como si fueran una cuenta real.
Declarar resolución disponible del índice (curvas almacenadas normalmente diarias), no llamar a su DD un máximo intraminuto. Informar también DD de motor por fold. PF agregado de trades únicos seleccionados: convención nominal de sesiones reseteadas, separar de índice reescalado. Si no hay curvas o trades suficientes, inconcluso, sin fabricar valores.
Describir meses negativos,mediana,peor mes,rachas y concentración por mejor trade/semestre. Retirar mejor semestre y reportar si cambia el signo. Meta20–30%anual sólo con convención válida y tiempo completo; sin cuota mensual.

## Robustez preregistrada: hasta48sesiones
Valores de slippage5/10bps por lado son escenarios deterministas de estrés, no una medición calibrada de fills Binance. No buscar el mínimo coste que salva candidata. Se requiere la integración real de fills descrita en freeze; un haircut posterior no sustituye estas pruebas.
Para cada uno de hasta2finalistas y cada uno de4folds confirmación:
S1 fee.0009,slip0;
S2 fee.00045,slip5;
S3 fee.0009,slip10;
S4 fee.00045,slip0,OI entregado con UN cierre4h adicional de retraso.
Total32. S4 conserva la observación causal obtenida en T−4h y la entrega en T; la frescura se evalúa en el reloj original T−4h y no se prolonga el stale original ni se consulta el futuro. OI24h usa las observaciones igualmente retrasadas. Primeras siete decisiones4h sin referencia suficiente; registrar la inicialización adicional. Si no usa OI es prueba equivalente y se reutiliza, no otro intento económico.
Vecindad: cada finalista, sólo C1 y C4 (fechas fijadas ahora),stop/target1.8%/3.6% y2.2%/4.4%,hold24h y gates intactos:8sesiones.
Máscara común diagnóstico: para cada finalista/fold, ejecutar su contraparte de precio P con la MISMA máscara de calidad/disponibilidad de las features exigidas por el finalista, pero sin sus gates económicos:8sesiones. Comparar contra finalista original, que ya exige esa máscara. Si finalista es P, equivalente sin ejecución adicional. Sin seleccionar la contraparte ni trasladarla a shortlist.
Máximo48; los slots reutilizados NO se convierten en nuevos parámetros libres.

Sensibilidad proxy de marcas funding: run_analysis sobre snapshots para cashflows×0.5 y×1.5, ambos sentidos, con y sin mejor semestre. Es una aproximación contable SIN recálculo de fills/sizing/compounding; no denominarla replay. No atribuir exactitud histórica a una marca proxy.
Ceros/huecos: exclusión operativa siempre; tabla de máscara común y S4 miden sensibilidad, nunca borrar meses afectados.
Bootstrap complementario opcional sólo de retornos mensuales del selector, bloques contiguos3meses,2000muestras,seed42, preservando meses planos; descriptivo, sin elegir reglas, sin sustituir gates ni afirmar significancia estadística. No usar candle MC que desalinearía señales funding/OI salvo diseño específico nuevo.
No hay simulación de latencia ni garantía de ejecución real; queda explícitamente fuera de este soporte. S2/S3miden fills adversos, S1fees.

## Gates de confirmación, sin relajarlos
Neto del índice selector>0;PF de trades únicos seleccionados>=1.2;DD del índice muestreado<=25%;>=100trades seleccionados;mayoría de cuatro semestres positivos (>=3).
Neto agregado positivo bajo S1 y S3, reportando bajo estrés todos los demás límites y tamaño de muestra. Si faltan curvas o simulación de ejecución aplicada, INCONCLUSO, no aprobado por fee duplicada sola.
Comprobar degradación suave de vecinos, concentración y contribución repetida de cada feature frente a comparables; una feature sin aporte puede omitirse únicamente mediante shortlist/selector ya definidos, no crear una configuración nueva tras confirmación. No promover por un mejor fold.100trades no acredita significancia.
Un fallo final implica rechazo o V2declarada; no retuning de esta V1. Si reglas cambian tras confirmación, esa ventana es desarrollo para la nueva versión.

## Presupuesto, incidentes y continuación
Máximo160sesiones económicas=96exploración+16confirmación+48robustez. Intentos técnicos de fase0 separados y todos registrados. Cancelados/retries registran motivo,config,datos,timestamps,duración y dashboard_url real. Retrys sólo por errores técnicos con lógica y datos idénticos.
Al prerregistrar:0sesiones de búsqueda económica V1,4intentos técnicos iniciales fase0; los adicionales se registran en registry.json; ninguno autoriza promoción ni consulta2026.
2026sigue cerrado a nuevas consultas; autorización K1001no se extiende a estas estrategias. Una futura evaluación2026requiere propuesta y autorización específica tras estrategia/protocolo inmutables. No live/paper ni órdenes.
Próximo paso concreto: renovación controlada del servicio/MCP local con permiso según handoff/AGENTS,smoke de propagación5bps,conciliación y cierre de instrumentación/nuevas funciones. Luego trainE1,registro previo de selección y evaluaciónE1.
```

### strategies/FundingOiPilot4h/reports/FINAL_DECISION_V1.md

SHA256 169d7eb87a1b473dc3a203b7c407d9c62588b83f2fe932d3a4a6137053adb3f8.

```text
# Decisión final V1 — SIN_CANDIDATA
Fecha: 2026-10-20. Ciclo cerrado conforme al protocolo. No se promueve ninguna estrategia.

## Resultado económico
Se completaron las 96 sesiones previstas de exploración: 12 configuraciones, cuatro cortes cronológicos y una sesión de train/evaluación por corte. Todas terminaron. Los entrenamientos comienzan en septiembre de 2020 y las evaluaciones cubren los cuatro semestres de 2022–2023.

Ninguna configuración cumplió simultáneamente los criterios de train: al menos 30 trades, neto positivo, PF ≥ 1,2 y drawdown absoluto ≤ 25%. Las cuatro decisiones fueron SIN_CANDIDATA y se guardaron antes de iniciar la evaluación correspondiente. Ningún resultado posterior modificó esas decisiones.

El selector permaneció plano durante los 24 meses: cero trades, retorno del índice convencional 0%, DD 0% por ausencia de exposición y PF indefinido. Ese resultado no supera los criterios económicos ni acredita la meta orientativa de 20–30% anual.

## Hallazgos de las ablaciones
H1+OI redujo el DD de evaluación frente al control de precio en los cuatro semestres, pero su PF agregado fue 1,042 y falló todos los entrenamientos. Añadir funding a esa variante redujo el PF agregado a 1,016.

H3+OI ganó 40,19% en enero–junio de 2023, pero perdió los otros tres semestres y su PF agregado fue 1,018. Al retirar su mejor semestre, la suma nominal de los otros tres netos queda en −33,38 puntos porcentuales. Esta suma describe sesiones independientes con capital reiniciado; no representa la rentabilidad de una cuenta continua.

Las tres configuraciones con suma nominal positiva cambian de signo al retirar su mejor semestre. Las señales de funding en H2/H3 también produjeron muestras pequeñas: 2 y 0 trades de evaluación para H2 con funding y combinada; 28 y 15 para H3. Un DD bajo por operar poco no demuestra robustez.

Estos resultados rechazan las reglas V1 bajo sus criterios. No demuestran que toda información de funding u OI carezca de utilidad.

## Cierre técnico
El servicio local de investigación se reinició con autorización del usuario. Se verificaron el puerto 9200, el directorio /src/bot y la ausencia de backtests y sesiones live/paper activas antes de actuar. Las lecturas autenticadas por MCP posteriores fueron exitosas. Postgres, Pi y cuentas no se intervinieron.

El slippage adverso optativo quedó implementado y probado: 279 tests aprobados y Pyrefly sin errores. El [smoke efectivo de 5 bps](http://localhost:9200/#/backtest/65ed1148-59cb-477e-9143-75fee5de93f9) verificó cinco fills ajustados en tres trades, con error contable cero. Esto valida la implementación técnica; no prueba robustez económica de las estrategias.

La auditoría OI identificó 560.390 muestras, 634 ausencias en 156 intervalos y 473 ceros. Se preservaron el dataset, la exclusión de ceros y los límites de disponibilidad y stale. El archivo sigue siendo retrospectivo y no está certificado point-in-time.

Los 96 backtests conciliaron precio bruto − fees + funding = PnL y saldo final. El error máximo observado fue 5,093 × 10⁻¹¹ USDT. Sus contadores persistidos concilian barras, causas y entradas; los cierres forzados posteriores al resumen se registran aparte.

Código común, subclases, configuraciones, datasets, hashes, 12 snapshots de framework, duraciones y dashboard_url reales quedaron preservados. Los cinco archivos de integración conservaron los hashes de fase 0. Los cambios preexistentes no se revirtieron.

Los timeouts de arranque se resolvieron consultando las mismas sesiones, sin duplicar runs. Una página de logs insuficiente se amplió sólo para lectura. Los incidentes están en registry.json y el freeze.

## Fases no ejecutadas
La shortlist está vacía conforme a la regla predefinida. No se ejecutan la confirmación de 2024–2025 ni las 48 sesiones de robustez, y sus slots no se reasignan a tuning posterior. Se utilizaron 96 de las 160 sesiones económicas máximas, más siete intentos técnicos registrados.

No se afirma supervivencia de una candidata a fees duplicadas, slippage, retraso OI, vecinos, máscara común, proxy de marcas o bootstrap. El nominal usa fee 0,00045, slippage cero y funding activo con marcas históricas proxy; los importes de financiación no son exactos certificados. No se simulan latencia ni liquidez real.

No hubo nuevas consultas económicas de 2024–2025 para estas configuraciones ni consultas/backtests de 2026. Tampoco ML, live/paper, órdenes, Pi, commit o push. El backend local queda disponible y no hay backtests activos.

## Evidencia dentro del proyecto Jesse
- RESEARCH_DATA_AND_EXECUTION_FREEZE.md: cierre de fase 0 y límites.
- RESEARCH_PROTOCOL_V1.md: reglas, selección, fricción y presupuesto prerregistrados.
- RESEARCH_V1_IMPLEMENTATION_FINAL.md y registry.json: fuentes, hashes, configuraciones, ventanas e incidentes.
- WALK_FORWARD_EXPLORATION_V1.md: tablas, concentración, las 96 sesiones y sus duraciones.
- Los ocho WALK_FORWARD_*_RESULTS.md: meses, costes, exposición, long/short y selección previa por etapa.
- WALK_FORWARD_COMPARISON_V1.json: comparación MCP de las 48 evaluaciones.
- AUDIT_<strategy>.json: contadores completos por sesión, mes y dirección.
- FROZEN_SHORTLIST_V1.md: shortlist vacía.
- WALK_FORWARD_CONFIRMATION_AND_STRESS_V1.md: fases no ejecutadas y motivo.

## Condición de un eventual ciclo siguiente
V1 se rechaza bajo sus reglas. Un ciclo V2 deberá declarar una hipótesis distinta, sus criterios y presupuesto antes de ejecutar. Los años 2022–2023 ya son desarrollo observado; la reserva interna de 2024–2025 no ofrece independencia absoluta frente a investigaciones antiguas del workspace.

2026 permanece cerrado para esta línea hasta una autorización específica posterior a una candidata inmutable. No se relajan los criterios de V1 para promover retrospectivamente un semestre ganador.
```

### strategies/FundingOiPilot4h/reports/FINAL_DECISION_V2.md

SHA256 ead50b514e06b47b44b9695a1a9a3be045fc52889a24941f8307ffb04f0ee83a.

```text
# Decisión final V2 — SIN_CANDIDATA
Fecha: 2026-10-20. Investigación cerrada conforme al protocolo. No se promueve ninguna estrategia.

## Qué se completó
Se ejecutaron las 16 sesiones ATR previstas y se reutilizaron 16 controles fijos V1 previamente verificados: 32 slots nominales, cuatro configuraciones y cuatro folds con train/evaluación. Todas las sesiones terminaron. Los cuatro smokes técnicos previos quedan separados.

El trabajo se distribuyó entre tres subagentes: ATR sin OI, ATR con OI y auditoría independiente. Inicialmente cada rama pudo gestionar dos backtests simultáneos. Tras errores de respuesta de la API/MCP se redujo a uno por rama, dos en total. Los timeouts se resolvieron leyendo los mismos IDs; no hubo duplicados, cambios de reglas ni reinicios.

## Decisión económica
Las cuatro selecciones E1–E4 fueron SIN_CANDIDATA. Ningún entrenamiento cumplió simultáneamente:
- al menos 30 trades;
- neto positivo;
- PF ≥ 1,2;
- drawdown absoluto ≤ 25%.

La selección de cada fold se guardó antes de solicitar cualquiera de sus dos evaluaciones ATR. La auditoría independiente verificó los ocho timestamps y los reportes previos. Los controles fijos y sus evaluaciones ya eran conocidos de V1; no se presentan como una muestra nueva.

La shortlist queda vacía porque ninguna configuración fue seleccionada al menos una vez. El selector permaneció plano durante los 24 meses de 2022–2023: cero trades, índice convencional de 10.000 constante, retorno 0%, DD 0% por ausencia de exposición y PF indefinido. No se acreditó la meta orientativa de rentabilidad anual.

## Qué mejoró en la exploración
La comparación diagnóstica de las cuatro evaluaciones muestra:

| Variante | Trades únicos | PF agregado | Semestres positivos |
|---|---:|---:|---:|
| Fija sin OI | 342 | 0,975 | 1/4 |
| ATR sin OI | 332 | 1,093 | 3/4 |
| Fija con OI | 228 | 1,042 | 2/4 |
| ATR con OI | 223 | 1,172 | 4/4 |

ATR redujo DD y turnover frente al control fijo correspondiente en los cuatro semestres, tanto con OI como sin él. Mejoró el neto en tres de cuatro; rindió menos en enero–junio de 2023. La intervención cambia protección, tamaño, ocupación y entradas posteriores, de modo que no identifica un efecto aislado del stop entre operaciones idénticas.

ATR con OI obtuvo +10,81%, +3,08%, +7,96% y +2,88% por semestre. Son retornos de cuatro sesiones independientes, cada una reiniciada con 10.000 USDT; no se suman ni anualizan como rentabilidad de una cuenta continua.
Su PF agregado fue 1,17171 y el peor DD de evaluación fue −10,94%. La suma nominal de sus netos fue +2.474,37 USDT y siguió positiva, +1.392,89, al retirar el mejor semestre. Es una atribución descriptiva sobre sesiones con capital reiniciado.

Esto representa una mejora exploratoria respecto a V1, pero no permite promoción retrospectiva. ATR con OI tuvo en los entrenamientos:
- E1: neto −0,20%, PF 0,999 y DD −29,08%;
- E2: neto +10,59%, PF 1,059 y DD −30,65%;
- E3: neto +14,01%, PF 1,063 y DD −30,65%;
- E4: neto +23,08%, PF 1,087 y DD −30,65%.

Sus cuatro semestres positivos convivieron con 11 meses negativos y una racha de tres meses negativos. El peor mes fue −5,89%, ligeramente peor que el control fijo con OI (−5,78%). No todas las métricas mejoran. Su PF agregado tampoco alcanza 1,2; no se redondea para aprobar.

## Integridad y límites
La conciliación de las 32 sesiones nominales verificó precio bruto − fees + funding = PNL y saldo final. El error máximo fue 5,093 × 10⁻¹¹ USDT, frente a tolerancia de 10⁻⁶. Las 16 auditorías ATR conservan contadores mensuales, entradas, salidas y cierres forzados posteriores al resumen. Algunos indicadores open_trades/open_pl son previos a ese cierre; el ledger, trades y saldo finales conciliaron, sin inferir una posición residual activa.

Código, parámetros, datasets y configuración permanecieron congelados. Se preservaron fuentes, hashes, fechas, dashboard_url reales, duraciones y respuestas de error en el registry y los progresos de rama. Los 16 backtests nuevos aparecen una sola vez en el listado MCP y no queda ninguno activo. Su suma de duración de motor fue 216,11 segundos; no es el tiempo de pared de orquestación.

El nominal usa slippage cero; funding conserva marcas proxy y OI es un archivo retrospectivo sin certificación point-in-time. Las ventanas 2022–2023 son desarrollo observado. Las curvas mensuales tienen resolución diaria aproximada, y las sesiones con capital reiniciado no sustituyen un replay continuo. La validación técnica previa no demuestra supervivencia económica a fricción.

## Fases no ejecutadas
Con shortlist vacía no se ejecutaron las ocho sesiones de confirmación de 2024–2025 ni las 24 de robustez. Se consumieron 32 de los 64 slots nominales V2, contando las 16 reutilizaciones; los restantes no se reasignan a tuning.

No se afirma que una candidata sobreviva fees duplicadas, slippage, vecinos, retraso OI o cambios de proxy. Tampoco se abrió 2026. No hubo ML, RST, live/paper, órdenes, Pi, cambios globales, instalaciones, reinicio, commit o push.

## Continuidad
V2 queda cerrada. La escala por volatilidad y OI dejan una hipótesis exploratoria más consistente que el esquema fijo, pero no una estrategia aprobada. Un ciclo siguiente debe definir una pregunta distinta y un presupuesto antes de probarla, declarando todos estos datos como observados. No corresponde ajustar direcciones, ventanas o criterios hasta que esta misma variante pase.

La reserva interna 2024–2025 no se abrió en V2, aunque otras investigaciones antiguas ya usaron esos años. 2026 sigue cerrado y requeriría una autorización específica para un examen posterior con candidata y reglas inmutables. Este cierre no autoriza operar.

## Evidencia guardada dentro del proyecto Jesse
- WALK_FORWARD_EXPLORATION_V2.md: tablas, meses, las 32 sesiones y límites.
- REGISTRY_V2.json: fuentes, hashes, configuración, datasets, sesiones, selecciones, incidentes y estado final.
- WALK_FORWARD_E1_SELECTION_V2.md a WALK_FORWARD_E4_SELECTION_V2.md y V2_AUDIT_CHRONOLOGY.json: decisiones previas verificadas.
- Los ocho WALK_FORWARD_*_RESULTS_V2.md y auditorías por sesión/etapa.
- V2_FINAL_COMPARISON.json y V2_INDEPENDENT_AUDIT_20261020.md: agregados y auditoría independiente.
- FROZEN_SHORTLIST_V2.md: lista vacía.
- WALK_FORWARD_CONFIRMATION_AND_STRESS_V2.md: fases no ejecutadas y motivo.
- V2_BRANCH_P_PROGRESS.json y V2_BRANCH_POI_PROGRESS.json: trazabilidad de los subagentes.
```

### strategies/FundingOiPilot4h/reports/FINAL_DECISION_V3.md

SHA256 7c8eb02338ec78b7ee6e8f5b0f4169f412697964bcbc6644ee40ec7d1090062b.

```text
# V3 — SIN_CANDIDATA, avance parcial

El mejor acercamiento financiero es CHANNEL_P en replay continuo2024–25: CAGR17.5435%,PF1.34851,DDmotor18.41396%,neto38.22586%,95trades y3/4semestres positivos. Sobrevive S1/S3 yambos vecinos según gates fijados. No se promueve:95<100.2025 quedó−0.0899%, por lo que el CAGR combina principalmente el buen2024. No bajar el mínimo ni elegir vecino para rescatarlo.

CHANNEL_POI: CAGR10.84025%,PF1.25979,DD17.16844%,84trades; falla tamaño/CAGR y pierde2.3070% enS3. EstadoFRÁGIL. El selectortrain-only eligióOI en los cuatrofolds, de modo que su resultado no se reemplaza retrospectivamente porP. P es finalista individual predeclarada, no la selección global.

Screening rechazó PULLBACK/RANGE. Presupuesto completo:36slots económicos nominales,33runs únicos y3smokes;sin duplicados. Contabilidad, costes ycalendarios conciliados, máximoerror4.92e−11USDT. Tresreutilizaciones documentadas. Matriz completa, años, semestres, sensibilidades, límites y URLs en WALK_FORWARD_CONFIRMATION_AND_STRESS_V3.md yV3_FINAL_METRICS.json.

Se conservaP como avance parcial para referencia, no como candidata aprobada ni autorización de operar. La siguiente etapa seráV4 con hipótesis nuevas de oscilador horario, shock precio/volumen yfunding reset; cada sector tiene dueño y propuesta previa. No código/economíaV4 hasta protocolo,fuentes,config ypresupuesto propios.2026sigue cerrado;sinML/live/paper/Pi/cuentas. El objetivo de investigación permanece activo.```

### strategies/FundingOiPilot4h/reports/FINAL_DECISION_V4.md

SHA256 d04a1a6790b5084cc9f94c779081a359372225cbc5091f731f851f43a00b007e.

```text
# Decisión final V4 — SIN_CANDIDATA

Fecha local: 20 de octubre de 2026. Cierre económico de las seis configuraciones. No se promueve ninguna estrategia.

## Resultado

Se investigaron tres mecanismos nuevos en BTC-USDT de una hora: RSI2 extremo dentro de una tendencia, reversión de shocks de precio y volumen, y normalización de funding con confirmación de precio. Cada uno tuvo una variante con filtro OI y otra sin él. Un subagente se dedicó a cada sector; trabajaron con hasta dos backtests propios y un límite global de dos motores.

El período continuo de screening fue del 1 de septiembre de 2020 al 1 de enero de 2024. Cada sesión comenzó con 10.000 USDT y registró 29.208 decisiones. Estos retornos corresponden al período completo de 40 meses, no a un año.

| Variante | Operaciones | Neto del período | PF | Drawdown | Años positivos 2021–2023 |
|---|---:|---:|---:|---:|---:|
| [ResearchV4OscillatorP1h](http://localhost:9200/#/backtest/29dd9e7e-c785-4763-abd3-2aff1e649661) | 774 | -8.61% | 0.960 | -26.86% | 1/3 |
| [ResearchV4OscillatorOi1h](http://localhost:9200/#/backtest/a1070e6a-ef44-4f9e-8c9f-34be95ca8f11) | 464 | -27.29% | 0.796 | -33.67% | 0/3 |
| [ResearchV4ShockPV1h](http://localhost:9200/#/backtest/02499a0c-1bc8-45ad-8f3a-bf4df11c404b) | 461 | -65.90% | 0.528 | -68.23% | 0/3 |
| [ResearchV4ShockPVOi1h](http://localhost:9200/#/backtest/2980adc0-9379-4f04-bb2a-0a6b931c1af0) | 279 | -51.81% | 0.475 | -53.09% | 0/3 |
| [ResearchV4FundingFP1h](http://localhost:9200/#/backtest/fa6ee4dd-4ea8-434d-84a1-dbe0249c9068) | 26 | -6.93% | 0.590 | -12.71% | 0/3 |
| [ResearchV4FundingFPOi1h](http://localhost:9200/#/backtest/786b270b-f497-4f48-b254-648ab7ea63af) | 12 | -7.66% | 0.268 | -8.55% | 0/3 |

Todas fallan neto positivo y PF ≥ 1,2. Oscilador y shocks también superan el máximo de drawdown del 25%. Las variantes funding tienen 26 y 12 operaciones, por debajo de las 30 mínimas. Ninguna alcanza dos años positivos de los tres años completos 2021–2023; 2020 parcial queda excluido. Los criterios se mantuvieron sin cambios.

La shortlist vacía está fijada en FROZEN_SHORTLIST_V4.md. Se consumieron seis de los 40 slots económicos y tres de los seis técnicos. Los 34 slots de confirmación, replay, costes, vecinos y retraso OI se omiten conforme al protocolo. No se reasignan a ajustes para rescatar resultados.

No hubo confirmación económica V4 de 2024–2025. No existe una curva de selector V4 para esos años y no se fabrica una rentabilidad de 0% por no haber ejecutado esa fase. 2026 continúa cerrado.

## Qué aprendimos

El oscilador sin OI obtuvo 5.567,52 USDT brutos por movimientos de precio, pero pagó 6.274,27 en comisiones y 153,99 en funding. Su resultado neto fue −860,73 USDT. La actividad no aportó una ventaja suficiente para cubrir el coste nominal. Con OI quedaron menos operaciones y peor rentabilidad.

Las dos variantes de shocks tuvieron pérdidas incluso antes de comisiones y funding. El problema observado incluye la dirección y evolución posterior de la señal; no se explica sólo por fricción.

Funding produjo 27 setups después de la confirmación de precio. Sin OI se ejecutaron 26 y uno quedó bloqueado por posición abierta. Con OI se ejecutaron 12 y se rechazaron 15 por OI no creciente. El filtro redujo exposición y drawdown, pero no creó rentabilidad ni una muestra suficiente. Un drawdown menor por operar poco no permite promoción.

Estas conclusiones rechazan las reglas nominales estudiadas. No demuestran que todos los osciladores, shocks, funding u OI carezcan de utilidad.

## Validación y trazabilidad

Las 14 fuentes compilaron y pasaron 248 comprobaciones deterministas: 61 comunes, 87 de oscilador, 48 de shocks y 52 de funding. Las revisiones cruzadas se realizaron antes de los screenings. La única corrección productiva previa fue rechazar medias no finitas por desborde numérico en funding; no cambió parámetros económicos.

Se completaron tres smokes de siete días, con 168 decisiones cada uno. El smoke funding no operó; no se le atribuye cobertura de fills o cierres. Los otros dos ejercieron callbacks reales de cierre, incluido el cierre final forzado.

Las seis sesiones económicas concilian precio bruto − comisiones + funding = PNL y saldo final. El error máximo es 1.000444171950221e-11 USDT, inferior a la tolerancia de 0,000001. Las curvas tienen cobertura diaria completa y 40 meses; el drawdown del motor gobierna los filtros.

Los subagentes recorrieron los logs completos. Se verificaron 2.016 planes de entrada y sus cierres, contando por configuración. Esta suma no representa operaciones independientes de una cartera combinada. Las seis sesiones económicas no necesitaron cierre forzado final. Oscilador ejerció salidas RSI y stops; shocks ejerció stops, objetivos y máximo de seis horas; funding ejerció salidas SMA24 y stops. Las ramas de calendario y máximo de 72 horas de funding quedaron cubiertas por comprobaciones deterministas, sin fills reales que acrediten esas ramas.

En cada variante funding se verificaron los 3.651 eventos y sus 7.302 bloques canónicos, con 3.651 hashes correctos, sin discrepancias del timestamp público. El recálculo independiente de pares normalizables, sigma cero y confirmación de precio coincidió. Las auditorías persistidas guardan todos los contadores, planes y cierres, más ventanas seleccionadas de inicio, medio, final y entradas. Las ventanas restantes permanecen en los logs originales de cada sesión.

Al cierre, las 14 fuentes coinciden exactamente con el snapshot congelado. La dependencia ResearchV2Core4h conserva su fuente. El listado devuelve nueve sesiones V4 únicas y terminadas: seis económicas y tres técnicas. No quedan motores V4 activos. Los timeouts se resolvieron leyendo el mismo ID, sin duplicar arranques.

## Límites y cierre

El nominal usa fee 0,00045, slippage cero, funding histórico y riesgo previsto del 2% incluyendo ambos fees, con tope nocional de una vez el capital. Stops, gaps y costes reales pueden exceder ese riesgo previsto. No se acredita robustez económica a slippage o fees duplicadas porque ninguna variante pasó el screening.

OI procede de un archivo retrospectivo, con disponibilidad asumida de etiqueta + seis minutos y freshness de diez minutos; no está certificado point-in-time. Funding de este período incluye marcas proxy. Los datos ya observados en ciclos anteriores no constituyen una prueba independiente. Las sensibilidades de funding con cantidades fijas son descriptivas y no sustituyen un replay.

V4 no modificó el framework ni las reglas V1–V3. No hubo instalaciones, reinicios, ML, live/paper, órdenes reales, Pi, cambios de cuentas, commits o push. La validación técnica demuestra consistencia de implementación; no rentabilidad futura.

Con este resultado se agotan las tres líneas nuevas previstas para el ciclo final V4. Se cierra este conjunto de hipótesis y se conserva la evidencia parcial de V3 por separado. No se alcanzó una candidata aprobada para la meta orientativa de 20–30% anual.

## Evidencia principal

- RESEARCH_PROTOCOL_V4_20261020.md y las tres propuestas sectoriales.
- REGISTRY_V4.json y V4_FINAL_METRICS.json: configuración, datasets, fuentes, sesiones, métricas y estado.
- V4_IMPLEMENTATION_SOURCE_FINAL_20261020.md y V4_STATIC_VERIFICATION_FINAL.json.
- V4_FINAL_SOURCE_AND_SESSION_VERIFICATION.json.
- V4_TECHNICAL_GATE.md y auditorías de los tres smokes.
- WALK_FORWARD_EXPLORATION_V4.md y las cinco auditorías centrales de las seis sesiones económicas.
- V4_OSCILLATOR_SCREEN_REPORT.md, V4_SHOCK_SCREEN_RESULT_20261020.md y V4_FUNDING_SCREEN_FINAL_REPORT.md.
- V4_FUNDING_FINAL_COUNTERS.json y las auditorías de logs por sesión.
- FROZEN_SHORTLIST_V4.md y WALK_FORWARD_CONFIRMATION_AND_STRESS_V4.md.
```

### strategies/FundingOiPilot4h/reports/FINAL_DECISION_V5.md

SHA256 5c870d2475bc57dde0fa982f03acfae842217fd99d25cf4aed989e2817f03520.

```text
# V5 — decisión final: sin candidata

Fecha local: 20 de octubre de 2026. Ciclo completo; auditoría independiente económica final PASS, sin discrepancias materiales. Ninguna finalista supera los requisitos nominales ni la robustez conjunta. El objetivo de 20–30% anual no se alcanzó.

## Replays continuos, 2024–2025

Cuenta inicial de 10000 USDT por variante, 2024-01-01 → 2026-01-01, 731 días; capital, historia OI y cuotas continuos. Cuatro ventanas semestrales separadas y cuatro bordes, sin reinicios de saldo.

| Variante | Neto total | CAGR 365/731 | PF | DD del motor | Trades | Semestres positivos |
|---|---:|---:|---:|---:|---:|---:|
| [Funding + OI](http://localhost:9200/#/backtest/46f4c14a-1ac2-4cc0-b347-5d6bff007051) | −6,866518% | −3,489614% | 0,853912 | 17,669256% | 84 | 1/4 |
| [Funding sin OI](http://localhost:9200/#/backtest/ff2f12bf-1faf-4bec-808f-800a778421a4) | −2,079607% | −1,043844% | 0,960575 | 14,311619% | 107 | 2/4 |

Nominal exige neto > 0, PF ≥ 1,2, DD ≤ 25%, N ≥ 100, al menos 3/4 semestres positivos y CAGR ≥ 15%; la meta orientativa es 20–30%. OI falla cinco de seis requisitos; FP falla cuatro. Tener 107 trades no compensa una expectativa negativa. No se suman operaciones entre variantes ni se reduce el umbral para aprobar N84.

Semestres del replay, por equity:

- OI: 2024 H1 −2,753076%; H2 +2,047041%; 2025 H1 −2,934627%; H2 −3,313638%.
- FP: 2024 H1 −2,717045%; H2 +0,435760%; 2025 H1 +1,379702%; H2 −1,145370%.

## Selección congelada y alcance real

Seis SCREEN de tres mecanismos nuevos. VWAP PV/PVOI fallaron neto/PF/DD. CROSS P/POI y FUNDING FP/FPOI sí fueron elegibles según N30/neto/PF/DD y al menos dos de los tres años completos 2021–2023 positivos.

El ranking prefijado priorizaba menor DD absoluto, luego PF, turnover, cantidad de features OI e ID. Con un máximo de dos finalistas, seleccionó Funding FPOI (DD 13,02295%) y FP (15,72361%) antes que CROSS P (17,69554%) y POI (22,66619%). Shortlist documentada antes de economía 2024–2025.

**CROSS no falló una confirmación futura: no fue confirmado por el límite y ranking.** CROSS P tenía CAGR de desarrollo 21,3292%, neto 90,5292% y PF1,7118; ese resultado de entrenamiento no es una aprobación histórica 2024–2025. No se cambia el ranking al observar que Funding pierde.

Las cuatro decisiones TRAIN se guardaron antes de sus evaluaciones. Ambas finalistas cumplieron N30/neto/PF/DD en C1–C4; el selector global eligió OI en los cuatro por menor DD. No se agregó CAGR o filtro anual al TRAIN. FP siguió como diagnóstico individual, sin cambiar retrospectivamente la política global.

| Corte | PF train OI | PF train FP | Elegibles | Selector |
|---|---:|---:|---|---|
| C1 |1,505844|1,362704|Ambas|OI|
| C2 |1,367147|1,267817|Ambas|OI|
| C3 |1,374710|1,264905|Ambas|OI|
| C4 |1,267955|1,234976|Ambas|OI|

El índice hipotético encadenando evaluaciones reseteadas dio −4,9980%/N83 para OI y −2,0831%/N107 para FP. **No es el replay.** La cuenta continua OI ejecutó N84 y terminó −6,8665%. La confrontación V5_REPLAY_VS_WF_ENTRY_COMPARISON.json encuentra las 83 entradas WF en replay y exactamente una extra: short 2025-01-01 04:00 UTC, stop 2025-01-03 18:45 UTC, PNL −195,5020 USDT. El replay conserva la referencia OI 2024-12-31 04:00 UTC (90681,416 frente a actual 91170,567). C3V independiente inicia sin esa observación T−24h y no hace backfill. Las 83 entradas comunes conservan precios y cierres dentro de 1e−6. La continuidad de historia cambia las condiciones iniciales; no se fuerza igualdad de trades, PNL o capital ni se reemplaza el motor por una multiplicación de retornos.

## Costes, vecinos y lag: todas las pruebas completadas

Las celdas muestran neto / DD del motor, con enlace a cada sesión.

| Escenario | OI: neto / DD | FP: neto / DD | Resultado |
|---|---:|---:|---|
| NOMINAL | [-6.8665%](http://localhost:9200/#/backtest/46f4c14a-1ac2-4cc0-b347-5d6bff007051) / 17.6693% | [-2.0796%](http://localhost:9200/#/backtest/ff2f12bf-1faf-4bec-808f-800a778421a4) / 14.3116% | Ambas rechazadas |
| S1 | [-10.1436%](http://localhost:9200/#/backtest/61c51f03-91d9-4142-8ad5-3f52f19cf4cb) / 19.6391% | [-6.6435%](http://localhost:9200/#/backtest/12b33663-1fd7-4883-bb74-519549664e21) / 17.0251% | Ambas fallan neto > 0 |
| S2 | [-10.4184%](http://localhost:9200/#/backtest/e7846d15-86e3-4c78-a5c4-c34122b0d8f5) / 20.0301% | [-7.0322%](http://localhost:9200/#/backtest/ef49d5d4-f4b7-4754-a91d-ec13cc6b51c4) / 17.4835% | Informativo; ambas negativas |
| S3 | [-16.7205%](http://localhost:9200/#/backtest/3733bd0f-ab2d-4ef8-b520-8455c1ecb44f) / 24.0812% | [-15.6613%](http://localhost:9200/#/backtest/0d37d117-ee67-4dcb-a3bf-44e16ccd32ad) / 22.9697% | Ambas fallan neto > 0 |
| R09 | [-6.0348%](http://localhost:9200/#/backtest/8d8a26f8-89dc-4afb-818e-1a9b02093d04) / 18.5177% | [-0.4087%](http://localhost:9200/#/backtest/f7c84508-165c-4788-83fc-52a9bd048e19) / 14.4059% | Ambas fallan neto > 0 |
| R11 | [-6.6011%](http://localhost:9200/#/backtest/65d8ecaa-5769-45cd-a0d1-8ce5eac88c50) / 16.2159% | [-1.3897%](http://localhost:9200/#/backtest/bd499d4f-5b7f-4ae1-882b-fac50e6becf3) / 12.5209% | Ambas fallan neto > 0 |
| A09 | [-8.7738%](http://localhost:9200/#/backtest/37f3b888-9751-4521-96a1-1711768f37f6) / 19.5419% | [-1.5062%](http://localhost:9200/#/backtest/ec1db1af-39f4-4ad3-83b7-f481566578a6) / 12.1670% | Ambas fallan neto > 0 |
| A11 | [-9.9388%](http://localhost:9200/#/backtest/26d1d710-e190-40c2-ab35-c49622e8bca7) / 18.6664% | [-5.7669%](http://localhost:9200/#/backtest/f81ccfbc-4887-419a-9a5b-2d341b75c93e) / 16.5291% | Ambas fallan neto > 0 |
| LAG4H | [-10.9430%](http://localhost:9200/#/backtest/08c43974-9ebf-4015-a3bf-f31481bcadfa) / 20.6085% | [-2.0796%](http://localhost:9200/#/backtest/ff2f12bf-1faf-4bec-808f-800a778421a4) / 14.3116% (reuse) | Ambas fallan neto > 0 |

S1: fee 0,0009 / slip 0; S2: fee 0,00045 / slip 5 bps; S3: fee 0,0009 / slip 10 bps. S2 es informativo. S1/S3, cada uno de los cuatro vecinos y lag aplicable deben conservar neto positivo y DD ≤ 25%.

R09/R11 cambian sólo stop de 3 ATR a 2,7 / 3,3 ATR. A09/A11 cambian SMA120/C30 de precio a 108/27 y 132/33; conservan los tres pagos publicados, hold de 180 barras, ATR14 offset0, sin TP/trailing. Lag OI agrega una barra de 4h al par de observaciones: target T−4h / ref T−28h, con calidad original. No retrasa precio/funding ni amplía freshness.

Calendario idéntico al nominal en todos los escenarios. Fee estresada entra en sizing; slippage usa fills adversos del motor y puede cambiar la secuencia. No hay descuento fijo ni selección de vecino ganador. **Todos los costes y los ocho vecinos fueron negativos; lag OI también negativo.** FP sin OI reutiliza nominal para el slot lag: no es otro motor.

Se ejecutaron las 17 corridas completas incluso cuando los nominales ya fallaban N, CAGR o semestres. Ninguna prueba pendiente ni variante rescatada.

## Diagnóstico económico

| Componente, USDT | OI | FP |
|---|---:|---:|
| Bruto |−455,927688|+115,914597|
| Fees |371,879079|491,457040|
| Funding |+141,154922|+167,581792|
| Neto |−686,651845|−207,960651|

FP obtiene un pequeño bruto positivo, insuficiente para cubrir fees incluso con funding favorable. OI presenta bruto negativo y los costes agravan la pérdida. Cortos:77/84 trades OI,98/107 FP; sus netos son −553,16/−342,17 USDT. No se construyen variantes long-only ni nuevos filtros a partir de esta descomposición.

Sensibilidades proxy-only/global funding ×0,5/1,5 están en los accountings completos, con cantidades originales. No son replays ni reparan las señales. Concentración y curva comparativa: V5_V6_REPLAY_COMPARISON.json; la eliminación descriptiva de ganadores no es una estrategia alternativa.

## Verificación, presupuesto y evidencia

- **37 motores económicos nuevos +3 slots reutilizados =40 slots**: SCREEN 6, TRAIN 8/EVAL 8, REPLAY 2, COST 6, NEIGHBOR 8, LAG 2. Reusos: dos TRAIN C1 y lag FP. Tres smokes técnicos separados; 40 motores nuevos en total, todos finished/errornull.
- 412 checks iniciales core/sectores; 14 wrappers WF; 11 wrappers replay con readback exacto y 1002 checks compile/AST/hash/fixtures. Auditoría independiente global 67/67 fuentes, ocho selecciones y 12 starts de evaluación PASS.
- 17 auditorías de ejecución y nueve accountings completos de fase C; todos PASS técnicos. Los 37 resultados económicos se concilian con snapshots completos, no paginaciones parciales. Error máximo 3,64e−11 USDT, tolerancia1e−6.
- Fechas/asof/qty/fees/cap 1x/riesgo 2%/fills/callbacks/calendarios/funding/24 meses/732 puntos diarios/4 semestres revisados. Estáticos no acreditan fills del broker ni ramas que el motor no ejercitó.
- Timeouts de start conservados y recuperados leyendo el mismo ID; ninguna repetición económica. Reparación del artefacto estático a output/ documentada, sin cambios de fuente ni parámetros.
- REGISTRY_V5.json; V5_FINAL_SESSION_INVENTORY.json; V5_FINAL_ACCOUNTING_INDEX.json; V5_FUNDING_WF_FINAL_REPORT.md; V5_FUNDING_REPLAY_STRESS_FINAL_REPORT.md; V5_REPLAY_STRESS_BRANCH_SUMMARY.json; V5_REPLAY_VS_WF_ENTRY_COMPARISON.json; V5_REPLAY_STRESS_BRANCH_PROGRESS.json; nueve V5_REPLAY_*_ACCOUNTING.json; V5_REPLAY_SOURCE_VERIFICATION.json; V5_V6_WF_CALENDAR_FINAL_INDEPENDENT_AUDIT.md; V5_V6_FINAL_ECONOMIC_INDEPENDENT_AUDIT.md.

![Cuentas continuas comparadas](V5_V6_REPLAY_EQUITY.svg)

2024–2025 ya se usó en ciclos anteriores: es confirmación histórica adaptativa, no una muestra prospectiva virgen. 2026 sigue cerrado; FINISH 2026-01-01 excluye velas/funding de 2026. Sin ML/live/paper/cuentas/Pi, cambios de backend o paquetes. Conclusión: se completa V5 con evidencia negativa y ninguna candidata aprobada.
```

### strategies/FundingOiPilot4h/reports/FINAL_DECISION_V6.md

SHA256 d4ee0ef9eb98384d0cc7aca6e53bf1e714d33482a00deddf0feb77a0f76587e2.

```text
# V6 — decisión final: sin candidata

Fecha local: 20 de octubre de 2026. Ciclo completo; auditoría independiente económica final PASS, sin discrepancias materiales. Objetivo del 20–30% anual no alcanzado. Ninguna variante se aprueba ni se habilita para trading.

## Resultado nominal continuo

[Replay Efficiency P](http://localhost:9200/#/backtest/f6f075f2-e7da-4f7b-ba2b-937456d5d127), cuenta inicial de 10000 USDT,2024-01-01→2026-01-01,731 días, capital continuo:

- Neto: **+0,278594%**; saldo final de 10027,85940464 USDT.
- CAGR 365/731: **+0,139010%**; PF **1,006229**; DD del motor **17,553569%**.
- **44 operaciones**, frente a 100 exigidas; **1/4 semestres positivos**, frente a 3 exigidos.
- Cumple neto > 0 y DD≤25%; falla PF≥1,2,N≥100,3 semestres positivos yCAGR≥15%. Meta orientativa20–30% tampoco se aproxima.

El denominador delCAGR incluye 2025 en efectivo. No se anualiza sólo el año activo ni se suman las 46 operaciones diagnósticas de los semestres inhabilitados.

## Screening y decisiones previas

Seis screenings de tres mecanismos nuevos, dos variantes cada uno. Sólo EFFICIENCY_P pasó N ≥ 30/neto/PF/DD y 2/3 años completos 2021–2023 positivos. EFFICIENCY_POI yNR7 fallaron PF/DD; deleveraging ambas variantes fallaron neto/PF/DD. Shortlist única congelada enFROZEN_SHORTLIST_V6.md antes de economía2024–2025.

| Corte | N de train | PF de train | DD de train | Calendario individual | Diagnóstico del semestre |
|---|---:|---:|---:|---|---:|
| C1 |148|1,247768|21,869573%|ON|+9,207450%|
| C2 |167|1,288431|21,869573%|ON|−8,176050%|
| C3 |192|1,180278|21,869573%|OFF porPF|−16,662574%|
| C4 |216|1,064928|31,494458%|OFF porPF/DD|+7,732447%|

Cada SELECTION_V6_Cn.json precede el start de su evaluación. Train sólo exige N ≥ 30/neto/PF/DD, sin añadir CAGR o filtros anuales. C1 reutiliza SCREEN exacto. C4 sigue OFF aunque su diagnóstico posterior resulte positivo. Calendario congelado en V6_REPLAY_CALENDAR.json: 2024 H1/H2 separados; 2025 sin exposición; cuatro bordes forzados,10000continuos sin reinicio de capital/historia. Saldo en 2025 constante dentro de tolerancia contable.

Semestres del replay: 2024 H1+9,207450%; 2024 H2−8,176050%; 2025 H1/H2~0%. El último residuo aritmético (~1e−13%) no constituye actividad económica.

## Robustez completa, calendario fijo

| Escenario | N | Neto | PF | DD del motor | Decisión |
|---|---:|---:|---:|---:|---|
| [NOMINAL](http://localhost:9200/#/backtest/f6f075f2-e7da-4f7b-ba2b-937456d5d127) | 44 | 0.2786% | 1.0062 | 17.5536% | Rechazado,4/6requisitos fallan |
| [S1](http://localhost:9200/#/backtest/f10942a7-0c80-4824-a972-7d3b284b05cf) | 44 | -1.9203% | 0.9570 | 18.6276% | Falla neto>0 |
| [S2](http://localhost:9200/#/backtest/445894c0-a830-45f8-8214-fe1454fc56ce) | 45 | -4.0276% | 0.9153 | 20.8753% | Informativo, negativo |
| [S3](http://localhost:9200/#/backtest/b7019ab0-8ade-4606-997f-1ccbfd618cc6) | 45 | -7.8957% | 0.8360 | 23.1713% | Falla neto>0 |
| [R09](http://localhost:9200/#/backtest/22d643fb-40aa-4425-b2b6-34c4e7df062c) | 45 | -0.4546% | 0.9910 | 20.2235% | Falla neto>0 |
| [R11](http://localhost:9200/#/backtest/f140ce43-60a0-49d1-a390-2e89f722b78a) | 44 | -0.5059% | 0.9877 | 16.4359% | Falla neto>0 |
| [A09](http://localhost:9200/#/backtest/90239e02-4fc6-420a-80f5-b9a57d843138) | 50 | 10.3288% | 1.2190 | 14.8855% | Pasa neto/DD; no promoción |
| [A11](http://localhost:9200/#/backtest/67851216-8941-4fbe-a0ea-ee8ff6bf5e63) | 41 | -2.5714% | 0.9371 | 19.8583% | Falla neto>0 |

S1: fee0,0009 / slip 0; S2: fee0,00045 / slip 5 bps; S3: fee0,0009 / slip 10 bps. R09/R11: stop2,25/2,75ATR; A09/A11: umbral0,315/0,385. Nominal: stop2,5ATR / umbral0,35 / hold de 60 barras, sin TP/trailing. Todos mantienen calendario y config restantes; nuevas cantidades/fills/capital en cada motor.

S1/S3, cada vecino y lag aplicable deben conservar neto>0/DD≤25. **Robustez conjunta falla** en S1/S3/R09/R11/A11. A09 pasa sólo ese gate local, pero no reemplaza al nominal: su CAGR 5,0304% / N50 tampoco cumplen los requisitos nominales. Lag sin OI reutiliza nominal; no genera otra sesión.

Costes entran en sizing: primera cantidad nominal de 0,14083594 BTC frente a 0,13695228 con fee doble. Slippage cambia también la secuencia (45 trades frente a 44), no es un descuento contable aplicado después. Evidencia: V6_REPLAY_COST_QUANTITY_COMPARISON.json.

## Diagnóstico contable y concentración

Bruto 508,137162 − fees 235,338240 − funding 244,939517 = neto 27,859405 USDT. Ledger de 532 cashflows, todos con mark exacto fundingRate.settlement_mark, sin proxy ni fuente desconocida en este replay.

Con cantidades fijas, multiplicar funding global × 0,5 deja +1,503292%; × 1,5 cambia el signo a −0,946104%. Sensibilidad proxy-only no cambia este replay porque no haymarksproxy. Son sensibilidades descriptivas, no nuevas ejecuciones.

Largos: 26 trades/neto+1007,36 USDT y cortos: 18/neto−979,50: se compensan casi totalmente. No se construye ni se promueve una variante long-only a partir de esta descomposición. Los cinco mejores trades representan el 77,15% del PNL positivo; excluir el mejor deja −909,42 USDT con cantidades fijas (diagnóstico, no estrategia).

## Verificación y presupuesto

- **21 motores económicos nuevos + 2 slots reutilizados = 23 slots**: SCREEN 6, TRAIN 4/EVAL 4, REPLAY 1, COST 3, NEIGHBOR 4, LAG 1. Reusos: C1 train y lag sin OI. Los 17 slots económicos restantes no se reasignan a tuning. Tres smokes técnicos separados;24 motores nuevos en total, todosfinished/errornull.
- 338 checks iniciales de core/sectores, 7 wrappers WF verificados, 5 wrappers de replay/readback y 606 checks. Auditoría independiente global: 67/67 fuentes y 8 selecciones/12 starts de evaluación PASS.
- Ocho replays/escenarios con snapshots completos y logs separados; 8126 verificaciones de ejecución PASS. Error contable máximo de fase C: 2,91e−11 USDT, tolerancia de 1e−6. Capital/fees/funding/qty/asof/24 meses/732 puntos diarios/4 semestres conciliados.
- Smokes y estáticos acreditan sólo las ramas ejercitadas. Cierres de borde con posición no observados en un motor no se dan por probados sólo por mocks.
- Starts con timeout guardados y recuperados por lectura del mismo ID; sin start duplicado. Ninguna modificación de fuentes congeladas, paquetes, framework o backend.

## Evidencia y límites

REGISTRY_V6.json;V6_FINAL_SESSION_INVENTORY.json;V6_WF_FINAL_REPORT.md;V6_REPLAY_STRESS_FINAL_REPORT.md;V6_REPLAY_STRESS_ROWS.json;V6_REPLAY_CONSISTENCY_AUDIT.json;V6_REPLAY_SOURCE_VERIFICATION.json;V5_V6_WF_CALENDAR_FINAL_INDEPENDENT_AUDIT.md;V5_V6_FINAL_ECONOMIC_INDEPENDENT_AUDIT.md;V5_V6_REPLAY_COMPARISON.json.

![Comparación de cuentas continuas](V5_V6_REPLAY_EQUITY.svg)

2024–2025 fue examinado en ciclos previos: esta confirmación histórica adaptativa no constituye una muestra prospectiva virgen ni demuestra rentabilidad futura. 2026 permanece cerrado; finish 2026-01-01 excluye velas/funding de 2026. No ML/live/paper/cuentas/Pi. La investigación V6 está completa y su conclusión económica es negativa; el resultado positivo de un vecino no cambia esa decisión.
```

### strategies/MultiAssetRetestBtcShort4h/reports/ORCHESTRATION_ROUND1_RESULTS_20261018.md

SHA256 1edfe0a6c23f94ffb9df26633e616aea0e72ed5901bb837a6103644fc2b4eedd.

```text
# Orquestación — resultados de primera ronda
Cinco hipótesis nuevas, con protocolos previos. Ventana común de desarrollo 2020-10-15 a 2025-12-31 exclusivo; capital 10.000 USDT; comisión .00045 por lado. 2026 no se evaluó.

| Caso | CAGR | Drawdown del motor | Meses activos positivos | Trimestres positivos |
|---|---:|---:|---:|---:|
|reference|28.83%|-14.89%|54.10% (61 activos)|71.43%|
|alloc_common|23.14%|-14.17%|54.10% (61 activos)|61.90%|
|alloc_risk|31.76%|-17.68%|55.74% (61 activos)|66.67%|
|lateral|0.33%|-13.53%|46.43% (56 activos)|42.86%|
|short_rr|23.43%|-13.30%|58.62% (58 activos)|61.90%|
|short_reclaim|27.29%|-15.00%|54.10% (61 activos)|61.90%|

[Referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb),
[reloj común](http://localhost:9200/#/backtest/9bbd9545-2154-4842-8902-8c926c7a4a56),
[presupuesto igual de riesgo](http://localhost:9200/#/backtest/72996434-7c02-4589-9400-42a23229ae02),
[fallo de rango](http://localhost:9200/#/backtest/acae5bd3-7f00-439d-991b-7eabbf86b903),
[short mínimo1R](http://localhost:9200/#/backtest/1f0b9301-0754-4044-ab29-9c9d9c979696),
[short invalidación por máximo](http://localhost:9200/#/backtest/2168b24e-632b-4dca-be9c-48677c7b5a58).

## Decisiones
Ninguna alcanza los objetivos 65–70% de meses activos y 80% de trimestres. No se promueve ninguna.
- Repartir exposición con reloj común mejora coherencia temporal del estimador, pero no la regularidad: mismos33meses positivos, menos trimestres.
- Presupuesto igual de riesgo suma un mes positivo y más retorno/exposición, pero pierde un trimestre positivo respecto a referencia.
- Reversión de rango: neto174,55 frente1160,54 de fees; sensible a fricción. No aumentar riesgo ni escoger retrospectivamente BTC long.
- Short mínimo1R: solo+190,65 netos en51shorts,PF1,033; mejor geometría planificada no generó mejor ventaja predictiva.
- Invalidación del máximo: shorts+3500,50/PF1,230, menor aporte y sin mejora mensual. La salida se activó en trades reales; no atribuir diferencias a simple ausencia de uso.

## Auditoría
AnálisisMCP8e2908d962b145dfac0918048ec57aba completado correctamente. AutocontrolesMTMv3,fees por trade,saldos terminales y contribuciones reconciliados. Artefactos temporales: orchestration_round1.json,monthly_matrix.csv y contribuciones por variante.
Los casos tienen63meses de calendario,con distintos activos: no comparar porcentajes activos sin sus denominadores. Ninguno es OOS limpio; no usar2026.
Pruebas anteriores a esta orquestación también existen y deben contarse al valorar selección adaptativa. No calcular una confianza estadística ignorando hipótesis descartadas.

## Próxima ronda
Cambiar premisas en vez de barrer umbrales locales:
- régimen diario bajista y recuperación fallida como componente shortBTC;
- salida long completa a3R/5R como familia predeclarada, con riesgo de perder tendencias;
- reversión de shocks relativos BTC/ETH con beta causal y control explícito de dos piernas (sin asumir cointegración ni atomicidad).
Las tres líneas requieren protocolos y verificación; ninguna se considera rentable o complementaria de antemano. Referencia inmutable, objetivo activo.
```

### strategies/MultiAssetRetestBtcShort4h/reports/BTC_NEW_ANGLES_RESULTS_20261018.md

SHA256 2c51d2eb2debb30679c0c628db6e6e7eae1a07e84aaf576f9bd80d220039ba63.

```text
# Exploración BTC sobre la combinada — 18/10/2026

Estado: ninguna candidata aceptada. La referencia y los objetivos permanecen intactos. Recuperación del retest y reloj por eventos terminaron y se descartaron. La prueba de gestión long BTC por falta de progreso también terminó y fue auditada sin inconsistencias: no mejora la regularidad y reduce mucho la rentabilidad.

## Alcance vigente

El usuario descartó funding, VIX y COT y sus descargadores. No quedan solicitudes de autorización pendientes para esas líneas. Autorizó seguir con BTC, velas, volumen y estructura, conservando PAXG/SPY, y dedicar una línea a investigación experimental.

Desarrollo: 2020-10-15 a 2025-12-31 exclusivo. El histórico 2020–2025 ya se ha usado ampliamente; no es OOS limpio. 2026 permanece reservado. Cuenta compartida de 10.000 USDT, 5x aislado, fee 0,00045 por lado en TODAS las órdenes. Riesgo máximo planificado 3% por trade / 8% agregado y techo bruto 4,4x. Funding y slippage efectivo siguen fuera; la reserva de sizing no los simula.

Objetivos: 65–70% de meses activos positivos, 80% de trimestres positivos, drawdown no peor que −25% y rentabilidad útil resistente a costes. También se muestran todos los meses y períodos completos.

## Resultados de la primera tanda

| Variante | CAGR | DD motor | Meses activos positivos | Todos los meses positivos | Trimestres positivos | Decisión |
|---|---:|---:|---:|---:|---:|---|
| [Referencia](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb) | 28,83% | −14,89% | 33/61 (54,10%) | 33/63 (52,38%) | 15/21 (71,43%) | Referencia intacta |
| [Volumen BTC](http://localhost:9200/#/backtest/fabf8e7d-438b-4690-a7af-92544858b435) | 25,91% | −14,49% | 32/61 (52,46%) | 32/63 (50,79%) | 14/21 (66,67%) | Descartada |
| [Estructura short BTC](http://localhost:9200/#/backtest/e632b3d1-9998-4c25-85c9-0b96bc1c4792) | 22,07% | −14,95% | 30/57 (52,63%) | 30/63 (47,62%) | 14/21 (66,67%) | Descartada |
| [Permanencia intrabar](http://localhost:9200/#/backtest/b1c63c4c-ddc9-40d9-b289-d01915073041) | 25,97% | −13,72% | 34/60 (56,67%) | 34/63 (53,97%) | 15/21 (71,43%) | Comparación útil; no aceptada |
| [Recuperación del retest](http://localhost:9200/#/backtest/7068c1f7-f9d2-4d10-a8df-95e760a19c8b) | 26,91% | −15,01% | 32/61 (52,46%) | 32/63 (50,79%) | 15/21 (71,43%) | Descartada |
| [Reloj por eventos](http://localhost:9200/#/backtest/f58458c2-605a-41b4-af24-45712590c967) | 17,60% | −15,67% | 28/58 (48,28%) | 28/63 (44,44%) | 11/21 (52,38%) | Descartada |
| [Falta de progreso long](http://localhost:9200/#/backtest/c6e326d6-5e63-4489-be8d-741d0f83f43a) | 11,86% | −18,27% | 33/61 (54,10%) | 33/63 (52,38%) | 14/21 (66,67%) | Descartada |

En períodos completos: referencia 33/59 meses activos y 14/19 trimestres; volumen 32/59 y 13/19; estructura 30/55 y 13/19; permanencia 34/58 y 14/19. Los 61 meses completos se conservan como denominador calendario, además del denominador activo.

El auditor V4 reconcilió órdenes ejecutadas, fees, wallet y MTM UTC. Sus self-tests pasaron; escalas de las fuentes verificadas con múltiples fills MARKET independientes a medianoche. Jobs b3de8216d2f64b1ea409501db66a1ac5 y 46be126036194c67857c0f30fdce3982 finalizaron succeeded. Los controles antiguos se usan sólo como anclas de precio de la misma serie, no para reciclar rendimiento de un motor anterior.

## Qué cambió y qué aprendimos

- Volumen: requiere volumen BTC 4h >= mediana de las 28 fechas anteriores del mismo bloque UTC. No modifica PAXG/SPY ni posiciones abiertas. Shorts: 107, neto 3.572,18, PF 1,29 frente a 123 / 5.287,02 / 1,36 de referencia. Rescata cuatro meses y estropea cinco. No se abre una rejilla de volumen.
- Estructura: reemplaza sólo RSI3<=20 del short por H1–L1–H2 confirmado, máximo menor y primera pérdida del soporte; dos barras a cada lado y memoria 60. Shorts: 17, neto −904,96, fees 160,90, PF 0,60; pierde también antes de fees sobre esos fills. Rescata cuatro meses y estropea siete. No se cambia pivots/memoria tras el fallo.
- Permanencia: conserva el short original, pero exige 120/240 cierres M1 en el tercio inferior de la vela señal. Logs: 327 candidatos, 327 ventanas M1 completas y con paridad 4h, 300 rechazados, 27 admitidos, 21 shorts ejecutados. Shorts: neto 2.138,67, fees 258,96, PF 2,28 y WR 66,67%; muestra pequeña. Mejora un mes positivo neto (rescata cinco y estropea cuatro) y el DD, pero no los trimestres; 2022 pasa de +2,67% a −5,06% y el peor trimestre empeora de −4,24% a −6,02%. No sustituye la referencia ni se ajusta el umbral.

Las reglas long y de otros activos permanecen iguales; sus cantidades y PnL pueden cambiar por el capital y la ocupación compartidos. No se suman curvas independientes.

## Laboratorio probabilístico cerrado

[Primera corrida](http://localhost:9200/#/backtest/8fb36f9a-ead7-41cd-9341-bc95de116f5a): cuatro estados por signos de dos retornos 4h, aprendizaje causal de etiquetas M1 de una política de una barra, shrinkage y gate heurístico de expectativa neta. No añade información externa ni demuestra una teoría nueva. Usa 1% de riesgo.

[Repetición técnica con debug](http://localhost:9200/#/backtest/ab8e72a8-f81f-41d8-8d95-8681d27e1b9c), sin cambiar política: 11.297 etiquetas válidas, cero ausencias, ventana 1.080 y conteos [264,272,273,271]. Las 10.218 decisiones evaluables no superaron el gate. Cero señales long/short y cero trades. El saldo de diagnóstico termina en 10.000; el motor no guardó métricas ni curva: no fabricar CAGR/Sharpe/DD. El guard de stop descartó 120 contextos; no sumar ese contador a skip_window como poblaciones independientes.

La abstención no fue un fallo total de datos ni entrenamiento incompleto. No se relajan umbrales ni se ejecuta un control incondicional para rescatar el resultado. El margen de una SE es una heurística, no significancia ni garantía bajo dependencia.

## Nueva ejecución: control técnico verificado

[Control BTC 1m](http://localhost:9200/#/backtest/9f2d190c-111d-4db4-af19-39ad2a7331d1) conserva decisiones, trailing y gestión 4h, órdenes originales y los otros activos. El auxiliar BTC 4h excluye velas en formación y la cancelación conserva cuatro horas de vigencia.

Comparación del job 3e58c073425c45a5ba8ef163147f54d7, succeeded: 220 trades, 440 órdenes registradas asociadas a esos trades y 1.904 puntos Portfolio equivalentes. Campos económicos, cantidades, precios, tiempos, fees y wallet coinciden; 45 métricas coinciden con tolerancia numérica. Diferencia máxima de curva 3,64e−12. Se excluyen sólo IDs aleatorios y nombre de estrategia. No prueba identidad de cada orden sin fill que no está en el snapshot.

Sólo después de esta equivalencia se autorizó preparar una variante de ejecución: armar el setup long BTC original, observar toque real en M1 y recuperar el nivel en una M1 estrictamente posterior, antes de cuatro horas. Entrada MARKET al precio real de confirmación, más cara explícitamente. Reservas y techos originales congelados; revalidación de riesgo/notional/margen al ejecutar. Shorts, PAXG/SPY y gestión 4h se conservan. Fuente revisada por dos agentes, contrato de tamaño cero corregido antes de ejecutar, sin cambios de alpha. La corrida terminó: 219 trades, 96 longs y 123 shorts, neto 24.643,53 y fees 4.213,33. Calendario: 32/61 meses activos y 15/21 trimestres; completos 32/59 activos y 14/19 trimestres. Rescata cero meses y estropea uno frente a referencia. Los 30 longs BTC fueron MARKET; 29 comparten setup con fills de referencia y uno corresponde a un setup sin fill de referencia. En los comunes, mediana +4,79 bps de precio, un minuto de demora y ratio de cantidad 0,9165; selección y capital posterior también cambian. Auditoría 8ea448f4be70443cb2614e988c970bf9 succeeded. Receta descartada sin cambiar la latencia.

La reserva interna no reserva margen real del broker mientras no existe orden; el tope de cartera y revalidación se comprobaron sobre la simulación conjunta. Corrección de explicación: exigir una M1 posterior es una confirmación adicional de persistencia predeclarada, no una necesidad matemática para ordenar mínimo y cierre. El cierre es el último precio de la vela; esta aclaración no cambia la regla ejecutada ni autoriza probar otra latencia tras ver el resultado.

## Conteo y continuidad

A las 18 pruebas económicas anteriores se añaden seis variantes combinadas y una receta probabilística sin operaciones. El repeat debug y el control de reloj son verificaciones técnicas, no dos hipótesis de alpha adicionales. La búsqueda global previa es mucho mayor y no se reinicia la selección. No hubo scripts nuevos, descargas, cambios de framework, instalaciones, fondos, live/paper o Pi.


## Reloj de eventos BTC — receta descartada

[Combinada por eventos](http://localhost:9200/#/backtest/f58458c2-605a-41b4-af24-45712590c967): terminada, 266,17 s, 185 trades (96 longs y 89 shorts). CAGR 17,5996%, DD −15,6699%, Sharpe 0,9103, neto 13.284,891739 USDT, fees 3.097,647678. Sustituye RSI short por fases alternantes de una ATR4h congelada desde extremos de cierres M1; cambia cadencia y adapta STOP al low de M1. Es una política conjunta; no aísla el aporte del reloj. Longs y PAXG/SPY conservan reglas, no necesariamente tamaños/fills.

Auditor V4 cabb99082ffd47ec99028fcd2d1c8d6d succeeded, self-tests y reconciliación de fills/fees/wallet aprobados. Meses activos 28/58 =48,28%; todos 28/63 =44,44%; trimestres 11/21 =52,38%. Periodos completos:28/56 activos,28/61 todos,10/19 trimestres. Rescata2 meses y estropea7 frente a referencia. Peor mes −6,3219%; peor trimestre −8,9991%. Año2022 −8,9323%.

ShortsBTC:89, neto −3.848,835196, fees831,283090, PF0,671347, winrate41,57%; precio antes de fees también pierde −3.017,552106. LongBTC30 neto11.091,505475; SPY31 neto2.874,645447; PAXG35 neto3.167,576013. No confundir menores cantidades de los otros activos con cambios de sus reglas: cuenta compartida y trayectoria de capital.

Cobertura exacta del full:2.740.320 callbacks M1, desde2020-10-15T00:01Z hasta2025-12-31T00:00Z; inicialización neutral primera frontera4h,2020-10-15T04:00Z. DOWN2009 =open316 +pending1 +prioridadlong0 +rechazados1582 +planes110. Armed110, fills89, UP2008. Sin guard failures. El smoke técnico Q1-2021 tuvo125.340 callbacks; su menor cobertura efectiva no tiene una causa verificada, no se inventa. La corrida común completa sí coincide con todos los minutos esperados.

No se ajustan amplitud, ATR, STOP, inicialización, timeout ni años para rescatar esta receta. No demuestra que toda representación por eventos carezca de utilidad. El objetivo económico sigue sin lograrse y 2026 permanece cerrado.

## Gestión por falta de progreso — receta descartada

[Full terminado](http://localhost:9200/#/backtest/c6e326d6-5e63-4489-be8d-741d0f83f43a), 277,2 s, sin error: 241 trades, 111 longs y 130 shorts. CAGR 11,861636%, DD −18,265016%, Sharpe 0,738878, neto 7.939,441908 USDT y fees 2.426,185507.

Clon de referencia, sin mezclar experimentos. Sólo long BTC: en el primer cierre 4h con edad real ≥24 h, cerrar MARKET si ningún cierre estrictamente posterior al fill alcanzó entry+1R inicial, congelada con el stop original. Revisión efectiva entre 24 y 28 h; el milestone puede alcanzarse hasta esa revisión. Si pasa, conserva el trailing original. Fuente revisada por root y agente independiente: 17 métodos originales idénticos; sólo cambian hooks de gestión y se añaden helpers/counters.

V4 job 55d0ba2d94654a4394feedbe850bd4d9 succeeded; self-tests, fills, fees, wallet y MTM reconciliados. 33/61 meses activos positivos (54,10%), 33/63 todos y 14/21 trimestres. Completos: 33/59 activos, 33/61 todos y 14/19 trimestres. Rescata dos meses y estropea dos, sin avance neto de regularidad. Peor mes −6,79269%; peor trimestre −8,30382%. Años: 2020 parcial −3,33427%; 2021 −5,24177%; 2022 +6,31889%; 2023 +8,59928%; 2024 +34,3312%; 2025 +26,27145%.

Long BTC: 45 trades, neto 1.722,628222, fees 303,76636 y PF 1,608713; referencia 31 trades y neto 13.881,758924. Short BTC: 130, neto 2.155,808727, fees 807,98926 y PF 1,250446. SPY: 31, neto 2.001,440573; PAXG: 35, neto 2.059,564387. Reentradas y capital compartido alteran exposición posterior: la diferencia no se atribuye sólo a una salida aislada.

Auditoría independiente de logs y órdenes: 39 revisiones únicas emparejadas con 45 longs BTC. Edades entre 24,000 y 27,9833 h; cada revisión coincide con la primera frontera 4h elegible tras fill+24h. Los 34 fallos cerraron íntegramente MARKET exactamente en la revisión; los cinco pases tenían milestone posterior al fill y anterior o igual a la revisión. Seis posiciones cerraron antes de revisión. Best-close concuerda con cada clasificación. Counters finales: 45 fills y 45 cierres =6 previos +34 fallos +5 pases; sin posición terminal. Cero inconsistencias. Neto de cohortes descriptivas: fallos −326,54; pases +3.398,90; previos −1.349,73. No son contrafactuales ni base para retocar la regla.

Receta descartada sin cambiar plazo o R. No demuestra que toda gestión temporal falle. La referencia y 2026 permanecen intactos. Ninguna candidata nueva cumple los objetivos; no se rebajan criterios.

## Cierre de la tanda

Seis variantes combinadas y una receta probabilística se añaden a las 18 pruebas económicas previas de la orquestación, sin reiniciar el historial global de selección. Repetición debug, control de reloj y smoke son verificaciones técnicas, no nuevas hipótesis de alpha. Resultados negativos conservados; ninguna receta se promovió a producción ni se evaluó en 2026. No se hicieron descargas, scripts nuevos, cambios de framework, instalaciones, reinicios ni operaciones live/paper.

Lo aprendido: seleccionar menos shorts no garantiza más regularidad conjunta; cambiar a eventos con estos niveles destruye la contribución short; exigir progreso rápido con esta regla recorta la principal contribución long. Estas conclusiones se limitan a las recetas ejecutadas y a este histórico de desarrollo, ampliamente reutilizado. No certifican imposibilidad de mejorar BTC ni justifican una nueva rejilla de umbrales.

## Experimento adicional terminado: calendario semanal BTC

Candidata: añadir long BTC sábado 00:00 UTC hasta lunes 00:00 UTC, sólo si está flat y no hay plan original long ni short. Control descriptivo no seleccionable: martes 00:00 → jueves 00:00 UTC. Antes de código o rendimiento se fija régimen común EMA20 > EMA80 > EMA80[-5] y close > EMA80, ATR14, stop 2ATR, riesgo máximo 1%, duración 48h y caps de cartera originales. Planes originales conservan reglas y prioridad en la decisión, pero la nueva posición puede bloquear señales posteriores y modificar capital: no se afirma que sus fills permanezcan intactos.

Ambas fuentes fueron revisadas por root y un agente independiente antes de ejecutar; 16 métodos originales idénticos y clones que sólo difieren en clase, descripción y día. Las dos corridas terminaron sin error. El control debe separar mejor exposición bull de posible efecto de calendario; es contraste descriptivo bajo estados de cuenta endógenos, no inferencia causal. Un control mejor no se promoverá como ganador ni habilitará probar más días. El borrador del agente sugería miércoles–viernes; root fijó martes–jueves antes de código/datos/rendimiento, sin selección estadística. No se barren ventanas.

### Resultados de calendario y decisión

| Configuración | CAGR | DD motor | Meses activos positivos | Todos los meses | Trimestres positivos |
|---|---:|---:|---:|---:|---:|
| [Candidata sábado–lunes](http://localhost:9200/#/backtest/b3157b7b-1745-4e0a-8314-77205763f58c) | 23,25% | −14,72% | 34/61 (55,74%) | 34/63 (53,97%) | 14/21 (66,67%) |
| [Control martes–jueves](http://localhost:9200/#/backtest/dd37b90d-f28b-460d-9354-81122f7a4b0b) | 30,63% | −16,49% | 33/62 (53,23%) | 33/63 (52,38%) | 14/21 (66,67%) |

Periodos completos: candidata 34/59 activos y 13/19 trimestres; control 32/60 activos y 13/19 trimestres. Candidata rescata tres meses y estropea dos; control rescata cuatro y estropea cuatro. Candidata: 295 trades, neto 19.745,835839 y fees 3.981,314336. Control: 298 trades, neto 30.272,040985 y fees 5.360,317581.

Leg nuevo candidato: 81 trades, neto +747,794704, fees 376,496926, 42 ganadores, 3.748,4833 horas de exposición; 71 salidas MARKET y diez STOP. Control: 95, neto +283,291325, fees 733,861167, 39 ganadores y 3.400,6 horas; 50 MARKET y 45 STOP. No son patas independientes ejecutables fuera de la cuenta observada. El resultado de toda la cuenta depende además del bloqueo de entradas y capital posterior, no sólo del PnL nuevo.

Auditoría final 6767173c23d84f06bb9f7af287b9ab6f succeeded: V4, fills, fees, wallet, calendario y tipos/timestamps de entradas y salidas reconciliados. Contadores de fills/cierres coinciden con 81 y 95; no retrasos, quotes ausentes ni cierres terminales BTC observados. Las entradas del suplemento son MARKET en su slot exacto, created=executed=opened; MARKET de salida a deadline, STOP antes o igual. La primera auditoría a4c07e227e9c4d8183029236090532e5 falló por una suposición del analista: MARKET por sí solo no distingue el suplemento, pues también hay cuatro entradas MARKET originales fuera del slot por sesión. Se corrigió el clasificador para exigir tipo+slot y reconciliar los contadores independientes; no se cambió ni repitió estrategia para arreglar rendimiento.

Los contadores occupied/pending/baseline_priority/evaluated no son una partición aditiva de slots; no inferir señales futuras bloqueadas a partir de su suma. Evaluated sí coincide con rechazos de régimen/riesgo y planes. Counters son preterminales; en estas corridas todos los suplementos ya estaban cerrados antes de terminar. La posibilidad de cierre terminal del control fue un riesgo predeclarado, no un suceso ocurrido.

Se descarta la candidata. El mayor CAGR del control no mejora regularidad ni DD y no se promueve como ganador, tal como se fijó antes de resultados. No se prueban otros días. Total añadido a las 18 pruebas económicas previas: ocho configuraciones combinadas (siete candidatas y un control) y una receta probabilística; controles técnicos aparte. Ninguna candidata aprobada.

## Cambio de dirección solicitado por el usuario

El usuario cuestiona estancamiento. Se cierra esta tanda y no se abren más variantes locales. Diagnóstico guardado en strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_PORTFOLIO_DIAGNOSIS_20261018.md: 13 de 28 meses negativos tienen contribución BTC no negativa y PAXG/SPY conjunta negativa; ocho el caso contrario y siete ambos negativos. Tres mejores longs BTC representan 82,4% del neto de esa pata. No es una prueba de imposibilidad ni motivo para eliminar activos retrospectivamente.

Se recomienda estudiar complementariedad de las tres patas con velas ya disponibles, objetivos y riesgo iguales y 2026 reservado. El usuario AUTORIZÓ ampliar el alcance a BTC/PAXG/SPY como cartera. Se prepara el diseño fijo de roles descrito en PORTFOLIO_ROLES_STAGE_PROTOCOL_20261018.md. Funding/VIX/COT siguen descartados.
```

### strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_FINAL_RESEARCH_RESULTS_20261019.md

SHA256 4066e53cf744efc6166d59abdae26ebaf6dc7842f8c6d81b45a6e75e7b691f7f.

```text
# BTC R8 — resultado final y candidata Y902 retenida

## Decisión y alcance

Se completaron13recetas en26backtests nominales:5contextuales,5experimentales y3del agente creativo adicional solicitado. Se conserva N204 como referencia operativa y Y902 como candidata de investigación prometedora. Ninguna receta cumple simultáneamente todas las puertas congeladas en B y C; por eso no se activan las6verificaciones condicionales ni se elige un ganador alternativo. Esto no equivale a descartar Y902 ni demuestra sobreajuste.

2026 permaneció cerrado incluso a inspección. Misma muestra de desarrollo2020-10-15 inclusiva→2025-12-31 exclusiva, cuatro años calendario completos2021–24 y2025parcial; no validación fuera de muestra. B/C son configuraciones relacionadas de SPY, no dos muestras independientes. Neto de cartera BTC/PAXG/SPY con capital compartido10000USDT y riesgo1% por operación/8% agregado; aislado5x, capnocional4.4 yfee.00045porlado. Reserva.001es dimensionamiento, no slippage ejecutado. No se añadió funding. Se mantuvieron PAXG original y las variantes SPY BSecond/CMarket.

## Resultados nominales

N204 referencia: B13056.614915 y C13239.442380USDT. N503 semilla de la familia creativa: B13328.711713 y C13536.902513USDT. Cada enlace lleva al registro de backtest devuelto por Jesse.

|Receta|Neto B USDT|Neto C USDT|Δ N204 B/C|Conclusión|
|---|---:|---:|---|---|
|V801|[13328.71](http://localhost:9200/#/backtest/b0c5ce4f-ed64-4b07-bdca-f708aae2d445)|[13536.90](http://localhost:9200/#/backtest/5de86562-4ba7-4f2f-b9fb-f647ed2a8b70)|272.10 / 297.46|Identidad económica con N503; no nueva observación independiente. C falla calendario bajo +5.|
|V802|[12838.90](http://localhost:9200/#/backtest/876feccb-b93c-4fb0-a6ea-3a4b58c642c7)|[13013.55](http://localhost:9200/#/backtest/8e889155-eabc-4187-acc5-748f98dc5378)|-217.71 / -225.89|Menor neto; cambios demasiado escasos.|
|V803|[13056.61](http://localhost:9200/#/backtest/e7ef94a6-5249-44ea-b0bc-8c3cb7e3c531)|[13239.44](http://localhost:9200/#/backtest/1d818489-9707-43ab-8106-98cacdbf0a56)|0.00 / 0.00|Identidad económica con N204.|
|V804|[13123.60](http://localhost:9200/#/backtest/b481d1da-f0b2-4c9c-b663-b4a4a8c44896)|[13307.81](http://localhost:9200/#/backtest/b042558a-4ea4-41f1-a2de-7d51d8d53b56)|66.99 / 68.37|Pequeña mejora nominal; falla calendario, distribución y omisión del mejor mes.|
|V805|[13056.61](http://localhost:9200/#/backtest/0af9be29-c28a-490b-a7d7-6a481660a950)|[13239.44](http://localhost:9200/#/backtest/ec8d524e-d8c0-4b55-8dbe-da6ae8051918)|0.00 / 0.00|Identidad económica con N204.|
|X801|[4947.13](http://localhost:9200/#/backtest/f660ef63-d7c6-4792-9f21-06c1d7ebd85f)|[5129.70](http://localhost:9200/#/backtest/4e432aac-71c2-4023-a978-6d8a618aa660)|-8109.48 / -8109.74|Ancla en vela de máximo volumen; menor neto.|
|X802|[7971.10](http://localhost:9200/#/backtest/261696a9-33ee-4504-a310-b8a44c63dcd3)|[8181.46](http://localhost:9200/#/backtest/07a45656-81e2-4fd8-9851-3aa16a782c2e)|-5085.51 / -5057.98|Ruptura de compresión común de seis velas; menor neto.|
|X803|[8013.23](http://localhost:9200/#/backtest/5208fe79-c420-4328-b5dd-1a67177f1ccf)|[8180.37](http://localhost:9200/#/backtest/a86de192-2f0d-4b34-a4ae-ce4f686d4757)|-5043.39 / -5059.08|Readmisión y pérdida del punto medio de vela bajista; menor neto.|
|X804|[5040.50](http://localhost:9200/#/backtest/ed50a692-6ce7-4014-baea-eb7b6b5acad9)|[5213.66](http://localhost:9200/#/backtest/09421154-a313-480c-9ab0-6c28cdcf810d)|-8016.11 / -8025.78|Cambio de presión de volumen/retornos; menor neto.|
|X805|[3846.19](http://localhost:9200/#/backtest/22b632fe-7fa2-450a-9f34-47c6e13efec8)|[3967.02](http://localhost:9200/#/backtest/69c41479-2763-4150-ad60-68e1fd605b41)|-9210.43 / -9272.42|Reloj de volumen M1; sobreoperación y menor neto.|
|Y901|[11046.64](http://localhost:9200/#/backtest/ee4ecf79-a83d-4388-b4de-3f2e44d62fd2)|[11228.81](http://localhost:9200/#/backtest/fc3f7e80-a6a0-4d61-8bc1-11ef693aac9c)|-2009.97 / -2010.63|Retesteo LIMIT; menor neto.|
|Y902|[13446.23](http://localhost:9200/#/backtest/cb305a17-1312-463e-bbf1-c8173dfae22c)|[13680.35](http://localhost:9200/#/backtest/b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff)|389.62 / 440.91|Candidata prometedora retenida; B falla únicamente concentración nominal del mejor mes.|
|Y903|[10679.17](http://localhost:9200/#/backtest/99393647-2bca-405b-b3f3-6c2b1a0bed33)|[10898.84](http://localhost:9200/#/backtest/745952c3-9fef-4c4c-8450-9fe8b6d142ff)|-2377.44 / -2340.60|Invalidación adversa; menor neto pese a recortar algunas salidas.|

V801 reproduce económicamente N503; V803 y V805 reproducen N204 (tolerancia1e-7, tiempos/tipos exactos). Son comprobaciones de equivalencia en esta muestra, no tres mejoras independientes. Las fuentes originales no cambian; la ocupación sí puede cambiar ejecuciones: X805 retiene30de31largos originales, no31. Todos los experimentos deben evaluarse por cartera y coste de oportunidad, no sólo por rendimiento aislado de su suplemento.

## Y902: qué aporta y qué queda incierto

Usa el mismo evento N503 pero solicita un SELL STOP en el mínimo de la vela de señal, válido sólo durante la siguiente4h. Distancia técnica congelada desde la señal, SL1R/TP2R desde fill y48h desde fill real; misma fórmula de sizing evaluada en el precio candidato, prioridad original y cancelación existentes. No hay reintentos de la misma señal. Se ejecutaron46suplementos frente a67N503. Los logs completos identifican45STOP y1MARKET por cartera; tipo STOP no significa corto original. El motor puede seleccionar MARKET cuando su regla de proximidad lo determina.

Mejora frente a N204: +389.619610/+440.906791USDT; frente a N503: +117.522813/+143.446658. Bajo overlay de10bps adicionales por round trip, mejora frente a N204 +546.100683/+591.583164. Son costes estáticos sobre fills/cantidades fijados, no un backtest con comisión elevada ni una prueba de liquidez real.

Bajo +5bpsRT:
- B:41de63meses calendario positivos (41/62activos), igual número calendario que N204.
- C:42de63positivos (42/62activos), un mes más que N204.
- Trimestres17/21en ambas, igual a N204B y uno menos que N204C.
- Sólo meses completos: B41/61calendario y C42/61, sobre60activos en Y902.
- Mejora MTM en4de5bloques2021–25 frente a N204;2025no es año completo.

Hay un coste: DDmotor−9.6941%/−9.6301%, frente a−8.7768%/−9.0579%N204. No mejora todas las dimensiones.

Enero2022 aporta +409.380189/+400.581645USDT de ventaja incremental. Al descontarlo aritméticamente, el resto suma−19.760578/+40.325146 frente a N204. Es el único fallo de B bajo el contrato de selección; C cumple todas las condiciones. Los−19.76no son una pérdida de un escenario de2022. La cercanía al cero, el mejor neto bajo costes y4/5bloques favorables justifican retener la candidata. La concentración justifica prudencia antes de sustituir la referencia; no diagnostica por sí sola sobreajuste.

## Consulta posterior: regularidad quitando enero2022 de ambas

Se realizó un análisis descriptivo adicional a petición del usuario, sin nuevos backtests, sin ajustar fuentes ni puertas y sin abrir2026. Entre los62meses calendario restantes:
- Nominal: B41/62positivos en ambas; C42/62en ambas.
- +5bpsRT: B N20441/62 frente aY90240/62; C41/62en ambas.
- +10bpsRT: B38/62en ambas; C39/62en ambas.

Y902 tiene un mes plano/inactivo; sus porcentajes sobre meses activos usan61, frente a62N204. El denominador activo puede elevar su porcentaje sin agregar un mes ganador. Sólo meses completos (60calendario tras retirar enero) da la misma conclusión relativa. No es un replay de capital sin enero ni una validación fuera de muestra.

Bajo +5 estático, la ventaja monetaria restante es +54.33/+111.64USDT; bajo+10,+128.43/+182.95. La casi igualdad nominal restante no agota la comparación, pero tampoco prueba mejora uniforme de regularidad. Detalle y código: BTC_R8_Y902_WITHOUT_JAN2022_MONTHLY_REGULARITY_20261019.md, job3025c86117854b62ac3e9b8f5581e7d6.

## Validación y trazabilidad

26formularios y78snapshots finales coherentes;37fuentes exactas (bases y rondas preservadas);13auditorías financieras de pares con4anclas inmutables, conciliando fills/qty/fees/PNL/wallet/terminal/MTM. Todos los targets pasan. Metadatos de Y901/Y902/Y903 conciliados contra logs MCP paginados completos:33/46/70suplementos por cartera. Y903modifica29salidas del suplemento emparejadas contra N503; se conservó el diagnóstico de toda la cartera separado para evitar atribuir cambios ajenos al mecanismo.

QA:102contextual,184experimental,201creativa final; hay200checks creativos previos a añadir telemetría. Estas comprobaciones se solapan y no son observaciones estadísticas independientes. Revisión independiente final310comprobacionesPASS, incluyendo puertas de26filas y trazabilidad Y903. Fuentes económicas congeladas; cambios de fixtures QA anteriores a las corridas no se presentan como backtests. La telemetría creativa se refrescó en los mismos6drafts antes de sus corridas mediante snapshots nuevos.

Hubo una respuesta MCP noJSON en el tramo previo y se suspendieron herramientas; al recuperar, se comprobaron estados existentes y se continuó el draft sin duplicar corridas. Límites lógicos de capacidad de análisis se gestionaron esperando trabajos existentes. No hubo purgas, borrados, reinicios ni cambios en framework o live/paper. Figuras PNG no se descargaron por el fallo de integridad conocido; artefactos textuales y cálculos sí se verificaron.

## Continuidad propuesta

Retener N204 y Y902 con sus fuentes actuales. La próxima fase útil es validar causalmente el cambio de ejecución Y902: qué entradas pierde/gana, cuánto depende la mejora de selección frente a precio y cuánto cambia la disponibilidad del corto original y el capital compartido. Diseñar cualquier validación de fee endógeno/bloques antes de correrla, sin afinar la receta para rescatar el margen de−19.76 ni abrir2026. No se ejecutó esa fase en esta ronda.

## Índice de evidencia

- BTC_R8_FROZEN_PROTOCOL_20261019.md y BTC_R8_CREATIVE_Y_FROZEN_ADDENDUM_20261019.md: hipótesis/gates/budget previos.
- BTC_R8_RESULTS_MATRIX_20261019.md: matriz26filas completa, elegibilidad y URLs.
- BTC_R8_FINAL_MANIFEST_20261019.md:26sesiones/78snapshots/37fuentes/13jobs y conciliaciones.
- BTC_R8_AUDIT_<receta>_20261019.md:13auditorías financieras.
- BTC_R8_Y901/902/903_SLEEVE_IDENTIFICATION_20261019.md: conciliación completa.
- BTC_R8_Y903_EXIT_ATTRIBUTION_CLARIFICATION_20261019.md y BTC_R8_Y903_SUPPLEMENT_EXIT_TRACE_20261019.md: atribución conservadora antes de resultados y29pares después.
- BTC_R8_FINAL_SELECTION_AND_METADATA_SOURCE_20261019.md: helpers finales.
- ../BTCExploreR801/reports/BTC_R8_INDEPENDENT_FINAL_GATE_REVIEW_20261019.md: dictamen independiente.
- ../BTCNovelR901/reports/BTC_R8_Y_FAMILY_RESULTS_20261019.md: informe del agente creativo.
```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_O_FINAL_20261021.md

SHA256 2d6473c73fc6cda419c69f213097abfc26d97f6a2fae15b1cd29bb6fc5d91889.

```text
# Tanda O: orden de extremos intradiarios, cierre

Dos políticas prefijadas sin candidata. REPAIR supera al controlBODY dentro del desarrollo, pero falla CAGR30%,M65yQ80. BODYpierde y falla economía. No se cambian dirección, resolución, empates, tamaño delcuerpo o protección ni se combinan retrospectivamente conN. PresupuestoOcerrado, sinvecinos locales.

|Política|N|CAGR|PF|DD M1+fills|M+ activos|Q+|Mediana mensual|Neto sin2mejores|Sharpe diario|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[repair](http://localhost:9200/#/backtest/964af419-18ca-40e4-acad-cb8bb3ba8630)|156|9.2614%|1.4185|13.9383%|34/60|14/20|0.3052%|3663.5716|0.8430|
|[body](http://localhost:9200/#/backtest/fae557b4-7b60-411f-a92b-8d213b009152)|850|-13.7700%|0.9045|61.7234%|24/62|8/20|-1.6914%|-7521.1448|-0.4584|

## Diseño preservado

En cada00:00UTC se toma el día cerrado,6bloques4h; admisibilidad común: signo diario no0, H/Lúnicos en bloques distintos, datosválidos/exactos. BODYopera signo diario; REPAIRsólo(HantesL+bodypositivo)o(LantesH+bodynegativo). MismoSL2ATR14simple4h,TP2R,48hgestión4h,unaposición2%feeaware. Ventana[2020-10-15,2026-01-01)UTC, BinancePerpetualFuturesBTC-USDT,10k/2%/6%/3x,fee.00045lado,fundingONhistóricoaplicado/verificado,slippage0. Neto cubre esos costosmodelados; no ejecuciónreal ni todosloscostos.

## Recibos y cuentas

[BtcResearchR15Repair1m](http://localhost:9200/#/backtest/964af419-18ca-40e4-acad-cb8bb3ba8630):brutoprecio7301.822403,fee1261.149008,funding-167.649768,neto5873.023627(58.7302%),equityfinal15873.023627USDT. DD diarioframework-12.2311% esdistintodelM1. Estadísticas:{"stage":"PRETERMINAL","counts":{"repair":187,"body_only":1638},"signals":187,"entries":156,"occupied":31}.

[BtcResearchR15Body1m](http://localhost:9200/#/backtest/fae557b4-7b60-411f-a92b-8d213b009152):brutoprecio-1259.000552,fee3732.991163,funding-390.931821,neto-5382.923535(-53.8292%),equityfinal4617.076465USDT. DD diarioframework-60.4847% esdistintodelM1. Estadísticas:{"stage":"FINAL","counts":{"repair":187,"body_only":1638},"signals":1825,"entries":850,"occupied":975}.

Ambas observaron1825díasadmisibles,187repair y1638body_only; porocupación REPAIRllenó156de187 yBODY850de1825. Diferencias enPnL no son efecto puro de un filtro sobre tradesiguales: ocupación, capital y tamaños cambian. El controlador no representa todoslosdíasBTC, sino días con admisibilidadcompartida. No hay selección deañosolados después delresultado.

Auditoríac3b0d733a5634abb815ce3b549bbcdbf succeeded:1006tradescompletos entre políticas alternativas, no muestrasindependientes; bruto−fees+funding=PnL=equityfinal−10000 error<1e−6USDT. Fundingcuadra,mismofrozenBTCdataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571,proxiesdeclarados. Telemetríacompleta2.741.760marcasM1,63meses/62completos,20Q,invalid0; telescopíacuadra. BODYusaFINALpostliquidación/cierrecomisión; total_open_trades1 escontadorpreterminal,no pendiente económico. REPAIRPRETERMINALsinposición.

Equitywallet+PnLabierto/M1+fills no todosextremosintraminuto; cortesmensualespostfunding/predecisiónporfase, no agrupación estrictaporfecha. Mediana incluye mesescalendarioinactivos; M65denominadormesescompletosactivos. N>=100espreliminaroperativo, no potenciaestadística. Historiaintensamentereutilizada, noOOSnuevo.

Checksintético118PASS,revisiónindependiente/rootconforme; protocolofijadoantesresultadoN ymanifiestoantesmotores. Recibotécnico faltante trasinterrupciónMCP confirmadoausente y recuperadodeljobexistente, sinrerun.2economíasnuevas,0errores/reemplazos/backteststécnicos. Totaldesde r9:28completadas, bloque209V1–V6 separado,sinindependencia. Sin estrés/riesgovariantes/nuevaeconomía2026/live/paper/Pi/global/instalaciones. Continuar pregunta materialP: aislarBTCdeK1001/N204,protocoloenpreparación; ningunaautorizaciónoperativa.
```

## Revisión documental anterior a implementación

El primer borrador usaba R11 directo y un adapter; root proveyó R32 común. El protocolo normativo usa ahora rows64 validados/últimos29 para fórmula y logs compactos por fallo bruto, sin callbacks económicos nuevos en hojas. Patrón, filtro y gestión no cambian. Se conserva el primer borrador SUPERSEDIDO, no normativo:

```text
# Línea B — persistencia de un fallo de ruptura por cierres

Fecha local: 2026-10-22. Estado: PROPUESTA para revisión de root, antes de implementación. Cero estrategias nuevas, drafts, jobs, motores o precios observados. Autorización de esta ronda: exploración documental con especialistas; no autorización económica automática. CODES flat acompaña las fuentes congeladas.

## Pregunta y motivación económica

Tras un cierre fuera de un rango previo y un regreso inmediato al interior, ¿exigir que el siguiente cierre todavía permanezca dentro mejora la política de reversión frente a revertir todos esos fallos en el mismo momento tardío?

Una ruptura puede atraer entradas de continuación y después regresar al rango. Si el precio vuelve pronto fuera por el lado original, la interpretación de rechazo ha quedado debilitada ANTES de entrar; si permanece dentro una barra adicional, el fallo ha persistido bajo una definición observable. Es una hipótesis predictiva de selección, no flujo observado, identificación de traders atrapados ni causalidad económica demostrada. Un cierre interior no prueba aceptación de una subasta en sentido microestructural. También puede llegar tarde y perder las mejores reversiones o seleccionar retrocesos sin continuación: esa es la explicación rival.

No se construye un STATE que compre recuperaciones. Ambos casos sólo revierten; recuperación se usa para abstenerse en el tratamiento. No se modifica ninguna posición en función de otra señal después de entrar. No deriva del suplemento K, no usa volumen, funding como señal, RSI, EMA, ADX, VWAP ni etiqueta futura TP/STOP.

## Antecedentes y diferencia material limitada

V1 H2 YA investigó reversión de ruptura: c_prev fuera del H/L del díaUTC anterior y c actual dentro, con fronteras dependientes del día, límite diario, stop2%/TP4%/24h, riesgo2%, cuatro variantes de gates funding/OI. V1 terminó sin candidata. No se presenta esta idea como una familia inédita.

OrchLateralFailedRange4h investigó barrido intrabar de rango20 y close dentro, gate eficiencia<=.25 y target al medio, bajo cuenta multiasset con otro riesgo y sin funding. Su cierre fue negativo. Aquí se exige cierre exterior real y dos cierres posteriores, sin eficiencia, targetmedio o gestor distinto entre brazos.

AngleCombinedBtcAcceptance4h añadió120/240 cierresM1 en tercio inferior a shorts originales, descartado. AngleCombinedBtcReclaim1m esperó touch y un cierreM1 posterior de recuperación para el long K original, descartado. Esta propuesta no cambia sus umbrales/latencia: clasifica tres cierres4h frente al MISMO rango congelado antes de la ruptura, y opera reversión simétrica.

R8 X801–X805 sustituyeron referencias de coste/cohorte/compresión/cuerpo/volumen; Y901 LIMIT y Y902 STOP conservaron evento N503 por presiónOHLCV/cohortVWAP/eficiencia. R8 no aprobó todos los gates; Y902 continuó por R9/K y no queda pendiente virgen. No se rescata esa ejecución, su helper de setup ni sus vecinos.

V3 RANGE vendió el cruce exterior z20 en bajo drift, no su regreso y permanencia; CHANNEL opera continuidad del breakout con SMA120, y PULLBACK touchSMA20/reanudación con régimen, sin esta secuencia. V4 shocks revierte desplazamiento>=2ATR y volumen>=2media1h; oscilador RSI2 y funding reset tampoco son la pregunta. V5 VWAP entra al volver a bandas cambiantes de media ponderada24h, sin rango congelado o permanencia extra; CROSS es SMA20/80. V6 eficiencia cruza un ratio de trayectoria, NR7 expande una vela estrecha y deleveraging añade datosOI. Sus cierres se conservan negativos/sin candidata; CROSS_P sin confirmación por ranking no se declara fallida en una fase que no se ejecutó.

O REPAIR usa orden de extremos de seis barras dentro del día; cierre sin candidata y sin vecinos. B no cambia su orden, resolución, dirección o umbrales: pregunta sobre fallo exterior de un nivel conocido y permanencia posterior, sin extremos intradiarios. La nueva observación no consiste en inventar un indicador o cambiar sólo el nombre.

Decisión previa: comparación nueva y pequeña justificada por el filtro temporal de permanencia, con control al mismo momento. No hay sesión archivada acreditada con ESTA receta y contrato exactamente equivalentes entre las fuentes revisadas. No se afirma búsqueda global exhaustiva ni novedad universal. La historia es ampliamente reutilizada/adaptativa; no OOS.

## Regla exacta de precio

BAR=14.400.000ms. En cada T múltiploUTC de4h se toman exactamente29 OHLC cerrados consecutivos con último open=T−BAR, mediante closed_window de R10. Todas las29 filas deben ser finitas/coherentes y positivas en OHLC. No usar volumen; no exigirlo positivo ni imputarlo. Cerrar29 excluye velas futuras/en formación; requerir close final igual a self.price con tolerancias numéricas heredadas rel1e−10/abs1e−8, no bandas de decisión.

Índices cero: contexto w[0:26]; ruptura b=w[26]; fallo f=w[27]; resolución r=w[28]. Equivalente slices: contexto rows[-29:-3], b[-3], f[-2], r[-1].
L=min(low contexto), H=max(high contexto). Requerir L<H. Fronteras congeladas antes de b: ni b, f o r las redefinen. No elegir otro lookback según resultado.26 es el canal ya usado por la infraestructura histórica; no duración económica estimada. No escoger horaUTC o fase favorable.

s=+1 si close_b>H; s=−1 si close_b<L; otro caso no patrón. Igualdad a cualquier frontera en b NO rompe.
Hay fallo sólo si L<close_f<H. Debe ser la barra inmediatamente siguiente a b; igualdad no vuelve al interior. Si f permanece fuera o retorna más tarde, esta ruptura no se opera bajo esta receta.
Al cierre inmediatamente siguiente r, el control ALL revierte con dirección−s, independientemente de dónde cierre r.
Tratamiento PERSIST sólo revierte dirección−s si L<close_r<H. Si r iguala cualquiera de las fronteras, recupera fuera del lado original o atraviesa la frontera opuesta, tratamiento cash. El control conserva esos casos: excluirlos en común sería cambiar su definición y esconder parte del filtro.
No epsilon económico ni ancho mínimo, extensión, color de vela, amplitud/volumen o distancia al centro como gates adicionales.

Partición diagnóstica EXCLUSIVA de las resoluciones de un fallo:
- interior: L<C_r<H;
- recuperación original: s=+1 y C_r>H, o s=−1 y C_r<L;
- atravesó extremo opuesto: s=+1 y C_r<L, o s=−1 y C_r>H;
- frontera: C_r=H o C_r=L.
No llamar recuperación al cruce opuesto. El tratamiento selecciona sólo interior; no permite separar categorías después y rescatar una mediante tercer motor.

## Caducidad, consumo y ausencia de cola

No se necesita una máquina armada durante días: cada tripleta b/f/r exacta se resuelve una vez en T, ocho horas después del cierre b y cuatro después del cierre f. La confirmación es una sola barra adicional, la mínima observación4h posterior; no se buscará1/2/3barras. La señal caduca en esa T: jamás se espera otra entrada, retest o recuperación posterior.

El patrón se calcula y registra antes de ocupación y sizing, para ambos brazos, también mientras existe posición o pending. Se consume aunque no se ejecute. No cola, pirámide ni reentrada en last_exit_at=T. Sólo un nuevo patrón con distinto timestamp b puede generar otra oportunidad posterior; no se rearma la misma ruptura porque el precio siga dentro. El diseño por ventanas permite patrones distintos que compartan barras, no muestras independientes ni episodios completamente disjuntos.

T<=last_decision no vuelve a calcular ni duplicar conteos/admisión. En cada nueva4h limpiar dirección/plan de decisión; rows inválidas, gaps, asof mismatch, L>=H o ATR inválido => cash, sin rescatar eventos anteriores ni rellenar velas. Mismatch es bloqueo técnico visible; no ocultarlo como ausencia rentable de señales. Protecciones de posiciones existentes continúan bajo la gestión heredada.

## Entrada, gestión y cuota idénticas

Ambos casos ejecutan BTC MARKET a float(self.price) en la resolución r, sólo si START<T<FINISH, plano, sin pending y sin cierre en esa T. No entrada retrospectiva en f ni en el nivel H/L. El tipo real MARKET y created/executed/opened deben auditarse en órdenes nativas; metadata sola no basta.

ATR14 arithmeticTR=atr14(rows) de R10, actual al cierre r, positivo y finito. D=2ATR para ambos. Stop desde fill real E−direction*D; TP desde fill E+direction*2D; salida MARKET en primer cierre4h cuya edad real sea>=48h. No BE/trailing/parciales/otra salida por recuperación o señal opuesta. R11 update_position ya implementa12BAR48h y su observación M1+fills. SL/TP están activos intrabar; las reglas del broker y gaps quedan las nativas. No variar stop, TP o plazo.

Reutilizar exclusivamente legacy_plan(event,.5*max(0,balance),.5*available_margin,leverage,fee), de R16LegacyBase, como helper de sizing, NO su señal/gestión ni herencia K. event conserva origin propio FAILURE_REVERSAL, direction−s, entry=self.price, distanceD, target_distance=2D, hold_hours48 y order_kindMARKET. Exigir stop y target positivos antes de planificar, igual para ambos. Herencia prevista directa R11, con adapter pequeño para el patrón/sizing/logs; no crear estrategia en este documento.

Esto significa cuenta alternativa BTC inicial10000 y riesgo objetivo1% del capital TOTAL, otra mitad ociosa, sin redistribución. Helper.02*.5, reserva.001 sólo dimensionamiento, floor lote.001, techo nocional4.4del capital escalado y buffer90% sobre la mitad del margen.3x aislado;6%global. No es una subcuenta de5000 ni dos cuentas sumables ni book conjunto2% ya demostrado.

Auditar qty y pérdida planificada incluyendo fees y reserva; en apertura verificar riesgo al fill real y qty antes de atribuir conformidad. R11 observer se llama exactamente una vez en cada hook heredado, equity=wallet+PnLabierto, sin portfolio_value apalancado. Nada de backtest virtual ni órdenes ficticias. El helper de sizing no agrega slippage cobrado ni limita gaps/funding a1% garantizado.

## Datos y contrato fijo

BTC-USDT, Binance Perpetual Futures; ruta1m/data4h; UTC[2020-10-15,2026-01-01) exclusivo; warmup2404h predeclarado, holgado para29 y heredado del contrato sin indicador recursivo nuevo.10000,3xaislado,fee.00045takercon descuento porlado, funding históricoON/applied dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571, proxies explícitos, slippage modelado0. No importar/preinspeccionar cobertura; faltantes los expone motor. No featuresETH/OI/nuevosdatasets, 2026nuevo, USDC, cartera, estrés/riskgrids, live/paper/Pi, installs/configglobal/framework.

## Instrumentación acotada y auditoría

Denominadores comunes por cierre4h: total/evaluable/invalid/asofmisaligned/zero_range/no_breakout/no_return/failed_patterns; estos últimos por s y categoría exclusiva de r. Dos políticas deben coincidir en patrones brutos/clasificación antes de ocupación. Contar filtro, señales seleccionadas, occupied, pending, same_exit, ATR/plan inválidos y fills reales con nombres explícitos; causas de bloqueo que se solapan no se suman como partición. No confundir oportunidades con operaciones independientes.

Log compacto por plan admitido: T, identidadb/f/r, L/H, tres closes, breakoutside, categoría, entrydirection, policy, precio solicitado, ATR/D, qty/riskbudget/planned_loss/reserva. OPEN luego del callback parent una sola vez: fill/qty, origen, Tsignal, distancia congelada, SL/TP reales y presupuesto; auditoría del riesgo completo antes de afirmar conformidad. CLOSE con closed_trade.pnl/gross/fees/funding verificable y exitorder, actualizando ledger antes de super si puede emitir FINAL. R11 meses/summary heredados y contadores propios por filas compactas<1900caracteres, sin logsM1 ni miles de candidatos en una línea. No añadir traceRprecio nuevo: el observador financiero R11 basta para esta pregunta.

Root congela nueva fuente+dependencias/hash/formulario/runtime y manifiesto antes de ejecutar. Reconciliar gross−fees+funding=PnL=final−10000 tolerancia1e−6, funding ausente sólo0 cuando ledger completo lo acredita, posiciones/cierres finales, ordenrealMARKET, protección y sizing, R11M1+fills/calendar/asof. PRETERMINAL yFINAL son snapshots, no sumandos; flatPRETERMINAL puede ser final económico. No fabricar métrica con registros truncados.

## Evaluación y falsación prefijadas

Puertas r9 intactas: CAGR neto>=30%, PF netoUSDT>=1.2, DD M1+fills<=25%(objetivo20%), meses completos activos positivos>=65%, trimestres completos positivos>=80%, mediana mensual calendario>0 incluyendo inactivos, neto aritmético sin dos mejores meses>0 y N>=100 mínimo operativo preliminar, no confianza/potencia. Informar cuenta total/cuota1%; no anualizar sólo meses activos ni trasladar automáticamente30% a cada pieza como promesa. También todos los meses positivos/denominadores, años2021–25 y ventanas12m descriptivas, concentración, lados, tiempo expuesto, bruto/fees/funding/neto, DD diario separado.

Contraste descriptivo de políticas completas: si tratamiento mejora por operar menos, no concluir información nueva sólo desde menor DD. Comparar retorno, PF, regularidad y riesgo conjuntamente, sin puntaje/cutoff de mejora material posterior. Si no domina, describir intercambio; no proclamar winner por una sola métrica ni quitar el control porque gane. Si tratamiento no aporta o empeora, rechaza este filtro bajo este contrato; no refuta toda reversión. Si ambos fallan gates, sin candidata aunque exista mejora relativa. Muestra escasa se declara insuficiente; no subir riesgo para obtenerCAGR.

Los trades comunes y categorías pueden describirse después, pero no son efectos causales aislados: el filtro modifica ocupación, capital y entradas posteriores. No reconstruir PnL de una cuenta eliminando trades del control ni inferir candidatos perdidos desde los fills. No separar por tipo de salida futuro como señal.

## Presupuesto y secuencia

Exactamente dos políticas futuras, ALL y PERSIST, máximo2motores económicos y0reemplazos automáticos. Un fallo técnico vuelve a root con causa; no consume un permiso abierto de reruns. No tercer motor de continuación/recuperación, ni vecinos de lookback, confirmación, igualdades, extensión, ATR, TP, plazo o cuota después delPnL. La recuperación como futura dirección es hipótesis aparte no autorizada por este presupuesto.

Concurrencia global vigente máximo2backtests+1analysis coordinado por root. Ahora sólo protocolo+CODES; después revisiónroot/independiente, luego autorización de fuentes y checks supplied-source/AST/stubs (sin frameworkimports/estrategias reales/precios), nueva revisión y recién draft/manifiesto/motores. Esta entrega no reserva ni ocupa slots.

Checks materiales previstos: oráculo índices29/26/3, fronteras excluyendo b/f/r y congeladas, long/short espejo, equality, retorno inmediato/caducidad, persist/recuperación/opuesto/frontera disjuntos, prefix/futuremutation, gaps/asof, ocupación/memo/noqueue/sameexit, .5/.5/lote/reserva, SL/TP48h y hooksR11/terminal sin duplicación. No confundir mocks con ejecución nativa acreditada. No volver a pedir permiso humano rutinario para documentación dentro de autonomía concedida; root decide revisión y prioridad de motores.

## Incidentes de esta preparación

Primer inventario list_project_files solicitó max_entries4000 y fue rechazado por límite1..1000; corregido a1000, sin mutación/job. El inventario de FundingOiPilot4h/reports truncó a1000 y no se afirma censo completo. strategies raíz sí se leyó sin truncar; búsqueda dirigida de antecedentes y sus fuentes/cierres. No incidente económico, código o conectividad. CODES preserva exactos las fuentes recibidas; no se reinterpretan pendientes antiguos como no ejecutados.
```

## Referencias adicionales completas leídas

- strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261022-r31/HANDOFF.md; SHA256 033c8a30fd214deaa2b88ca833597018bb3c544090eb72d7f926abb7e6a8cdd8; contenido completo leído, no duplicado aquí.
- strategies/FundingOiPilot4h/reports/K1001_LONG_SUPPLEMENT_CLOSURE_FINAL_20261022.md; SHA256 41feb1147c0e0ad222ea15e9bbe08b9b8d1ffc6be878dbe3f3e1b2eae59723c8; contenido completo leído, no duplicado aquí.
- strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261021-r4/HANDOFF.md; SHA256 230eab84e4aa058250e215d1939bdb937166a1fb6b598e7d7398ab2042f55216; contenido completo leído, no duplicado aquí.
- strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261021-r4/EXPLORATION_HISTORY.md; SHA256 5a579011d1cca4e8b90a6d8e3d1ea862c26e469fe7780f50d20c107ae38a2210; contenido completo leído, no duplicado aquí.
- strategies/FundingOiPilot4h/reports/BTC_R32_COORDINATION_PROTOCOL_20261022.md; SHA256 772bac97961871b3af80fa97d0c46fd8d28ba6a2fe5bb768a0bdfe7d358018f8; contenido completo leído, no duplicado aquí.

Incidentes: list_project_files max_entries4000 rechazado/corregido a1000; FundingOiPilot4h truncado, raíz strategies no truncada. Primer ensamblado de este anexo falló por clave de memoria incompleta para RESEARCH_PROTOCOL_V1; corregido a la clave con ruta completa, sin llamada de escritura ni job en ese intento. No fallo económico ni conectividad. Cero nuevas velas/imports/datasets/estrategias/jobs/drafts/motores en esta línea.
