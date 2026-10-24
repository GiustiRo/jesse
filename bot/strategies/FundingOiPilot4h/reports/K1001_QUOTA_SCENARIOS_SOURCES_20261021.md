# K1001 cuota: fuentes y cierres leídos antes de implementar

Estado documental. No son fuentes nuevas de estrategias. Protocolo normativo: K1001_QUOTA_SCENARIOS_PROTOCOL_20261021.md. Nombres previstos no creados. Las fuentes parent y configuración siguientes quedan congeladas; la futura base sólo sustituye admisión por allowlist y argumentos de sizing, más observación propia.

## Snapshot completo heredado de propuesta HOLD

El documento de ocupación se conserva como antecedente técnico de callbacks; su wrapper NO se implementa ni ejecuta. El siguiente snapshot reproduce su anexo existente íntegro, no adopta su medición de episodios:

# K1001 — Fuentes exactas para propuesta de medición de ocupación

Fecha: 2026-10-21. Sólo snapshots leídos por MCP. No es código de una wrapper nueva y no modifica el proyecto. Propuesta normativa: K1001_OCCUPANCY_MEASUREMENT_PROPOSAL_20261021.md.

La fuente R16Base actual coincide exactamente con el snapshot sources.BtcResearchR16LegacyBase1m en BTC_DISCOVERY_P_MANIFEST_20261021.json. Los snippets relevantes son los propios helpers legacy_long/short/supplement/plan y before/_prepare_entry/should_cancel_entry/on_open/on_close/_emit incluidos íntegros a continuación, sin reescritura. R11 se conserva para observar el orden de _observe y FINAL.

## BtcResearchR16LegacyBase1m

SHA256 UTF-8 de content MCP: `56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542`.

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

## BtcResearchR16LegacyK1001m

SHA256 UTF-8 de content MCP: `bf88cb663d8561e107446bfce32024ed87531d096362671f7aafce72a09f25ad`.

```python
from strategies.BtcResearchR16LegacyBase1m import BtcResearchR16LegacyBase1m


class BtcResearchR16LegacyK1001m(BtcResearchR16LegacyBase1m):
    MODE = "K1001"
```

## BtcResearchR11Base1m

SHA256 UTF-8 de content MCP: `be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87`.

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

## Formulario de control P, lectura del manifiesto previo al motor

Sesión de referencia: [K1001](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4). Este formulario es el de la referencia, no un draft nuevo. El futuro wrapper cambiaría únicamente strategy y metadatos de título/descripcion; su existencia/configuración no se inventa aquí.

```json
{
  "exchange": "Binance Perpetual Futures",
  "routes": [
    {
      "exchange": "Binance Perpetual Futures",
      "symbol": "BTC-USDT",
      "timeframe": "1m",
      "strategy": "BtcResearchR16LegacyK1001m"
    }
  ],
  "data_routes": [
    {
      "exchange": "Binance Perpetual Futures",
      "symbol": "BTC-USDT",
      "timeframe": "4h"
    }
  ],
  "start_date": "2020-10-15",
  "finish_date": "2026-01-01",
  "debug_mode": true,
  "export_csv": false,
  "export_json": false,
  "export_chart": true,
  "fast_mode": false,
  "benchmark": false,
  "config": {
    "logging": {
      "order_submission": true,
      "order_cancellation": true,
      "order_execution": true,
      "position_opened": true,
      "position_increased": true,
      "position_reduced": true,
      "position_closed": true,
      "shorter_period_candles": false,
      "trading_candles": false,
      "balance_update": true
    },
    "warm_up_candles": 240,
    "exchange": {
      "name": "Binance Perpetual Futures",
      "type": "futures",
      "balance": 10000,
      "fee": 0.00045,
      "futures_leverage_mode": "isolated",
      "futures_leverage": 3
    },
    "funding": {
      "mode": "historical",
      "dataset_id": "9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571"
    },
    "open_interest": {
      "mode": "disabled"
    }
  }
}
```

## Invariantes del diseño, no implementación

- Capturar previous_setup antes de super.before; el estado parent sólo se actualiza por ese super.
- Recomputar helper puro con ese valor anterior para el evento original; previous=False sólo descubre geometría ignorando latch en un resultado separado.
- Evaluar planes diagnósticos con el capital/margen REAL de cada fase y no almacenarlos en campos del padre.
- Interceptar _prepare_entry sólo cuando lo invoque el framework; no ejecutar el método para fabricar un universo de operaciones.
- Conservar cancelación TTL y rearmado en el mismo T según source framework/P, sin manualcancel/reentrada extra.
- R16 fija position_plan antes de _observe(open): el observador opcional puede comenzar allí sin alterar on_open. Antes de delegar on_close se conserva plan y precio de salida para finalizar registro propio; R16 después borra su plan y R11 puede emitir FINAL.
- Observación extra nunca llama _observe del padre una vez adicional, ni cambia indicadores, pending, planes, órdenes o gestión.
- No output económico de componentes independientes ni fills hipotéticos.


## BtcResearchR10Base4h: dependencia completa de R11, no política operativa seleccionada

SHA256 UTF8: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9. Su ATRsimple, entradas,TP/plazo y sizing NO sustituyen los helpers legacy R16.

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

## P FINAL completo: cierre y restricciones preservados

# Tanda P: K1001/N204, cuentas BTC individuales

Dos recetas legacy completas medidas en cuentas BTC individuales, sin candidata. Se resuelve la brecha entre contribuciones de cartera y retorno de una cuenta individual; no se atribuyen a BTC los CAGR de las carteras. K1001 yN204 fallanCAGR30%,M65activosyQ80, aun conPF/DD/mediana/concentración favorables. K37/58=63.7931% no65%; ambos15/20Q=75% no80%. No promoverporcercanía ni subirriesgo,retirarreserva,eliminarcomponentes o cambiarplazos para rescatar.

|Cuenta|N|CAGR neto|PF|DD M1+fills|M+activos|Q+|Mediana mensual|Neto sin2mejores meses|Sharpe diario|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[K1001](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4)|192|26.8148%|1.8489|16.5039%|37/58|15/20|1.1820%|15497.8805|1.4994|
|[N204](http://localhost:9200/#/backtest/ea5e1bd8-3ecd-4762-b03e-1f5d3e76ca61)|222|25.0358%|1.6530|17.8990%|36/60|15/20|1.1131%|13008.2229|1.3792|

## Receta y adaptaciones declaradas

LONG_RUNNER LIMITretsteoDonchian26/EMA20,80/ADX26/RSI52–76,SL2ATRta,BE2.25R/trail4.2ATRconajustesheredados,sinTP/plazo; CORE_SHORT STOPconmacroEMA120ascendente/RSI3<=20,TP1.5ATR,72h; suplementoN204MARKETcohorteVWAP yfallodeavance2R/48h,K1001añadeeficiencia<=1/3ySTOPestructural. Prioridadlong→shortoriginal→suplemento. Setupavanzaocupado; LIMIT/STOPpendientehasta4h,gestiónsólo4h, fill/proteccionesM1.

AislarBTCretira cuotaATRotrasrutas→100%BTC; cuenta/cantidades/funding/M1yúltimodía2025 incluido cambian frente a las anclas de cartera. No réplica idéntica ni ablationcausal de unasola diferencia. Capital10k,riesgo2%stop+fees+reserva.001desizing,6%capadmisiónnovinculanteconunaposición,aislado3x,margen90%confees,lot.001. Reserva.001REDUCEqty,no débito/PnL/slippage aplicado. No variar reserva/lote/capdespués. Feereal.00045porlado taker+fundinghistóricofrozenBTCaplicado/verificado,snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571,proxiesdeclarados,slippage0. Neto sólo después de costosefectivamentemodelados. BTC-USDTBinancePerpetualFutures,[2020-10-15,2026-01-01)UTCdesarrolloobservado;noeconomía2026nueva.

## Ledger y auditoría
[BtcResearchR16LegacyK1001m](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4):brutoprecio28115.585676,fees3176.475399,funding-410.421286,neto24528.688991(245.2869%),capitalfinal34528.688991USDT. DDdiarioframework-15.5129% distintoM1. Ledgerrealpororigen:{"LONG_RUNNER":{"fills":31,"closes":31,"net":10650.419092195123},"CORE_SHORT":{"fills":116,"closes":116,"net":4686.29849188876},"SUPPLEMENT":{"fills":45,"closes":45,"net":9191.971406577974}}. Planes313,fills192,cancelaciones121,eventossuplemento82.

[BtcResearchR16LegacyN2041m](http://localhost:9200/#/backtest/ea5e1bd8-3ecd-4762-b03e-1f5d3e76ca61):brutoprecio25902.273489,fees3518.650568,funding-308.065527,neto22075.557394(220.7556%),capitalfinal32075.557394USDT. DDdiarioframework-16.7707% distintoM1. Ledgerrealpororigen:{"LONG_RUNNER":{"fills":31,"closes":31,"net":10594.666156313726},"CORE_SHORT":{"fills":113,"closes":113,"net":4342.279629642518},"SUPPLEMENT":{"fills":78,"closes":78,"net":7138.611607679111}}. Planes318,fills222,cancelaciones96,eventossuplemento96.

Auditoría0aceae731d224b0585f7fe7ff6ac3d47 succeeded:414registrosentrepolíticasalternativas,noindependientes. Bruto−fees+funding=PNLsum=equityfinal−10000 a<1e−6USDT; fundingconciliado; suma ledger3orígenesconciliadaN/closes/neto. Todoslosorígenespositivosdentrodeambascuentas,noderivartresestrategiasindependientesniquitarelorigenpormétricaretrospectiva. Posicionesfinales0,PRETERMINALno pendiente económicofinal.

Telemetríaexactasegúnconvención:2.741.760marcasM1,63intervalosmensuales/62completos,20Q,invalid0; equitywallet+PnLabierto,DDM1+fillsnoextremosintraminuto; fronterasmensualesUTCpostfunding/predecisiónporfase. Mediana incluyecalendarioinactivo,M65sólomesescompletosactivos. History4hmin241/max11664enambas,compatibleconretencióndecrecimiento. No prueba deigualdadnuméricaconcarteras quenotienenlasmismascondiciones.

## Verificación técnica e intentos

Fuentespadres/R11/R10inmutables;CODES/readbacks/hashesenrecibotécnico. PrimercheckfallóSyntaxErrorenexpresiónVWAPnuevaantesdepruebas,corregido/registado; segundo5962asercionespassconmétodospadreembebidos/featuresartificiales. Checksnoimportanestrategiasrealesnidataobservadanibrokerreal. Auditoríaframeworkreadonlydelcheckoutbindmontado,resguardadaMCP,detectóque docsresumidassimplificaban cancelación: _checkcancela ypuede reevaluarentradasenmismociclo. LazyplanmemoizadoahorapreservarearmadopostTTL/margenliberado,perono tras cierreposición. Replayprocesaminutoexpiryantescancel; verificadaspolíticasdehistoria/taATRscalarúltimas240/EMAseqhistoriacompleta. No editarframework/config ni leerestrategiasporfilesystem,ningúnDockerrestart. Revisiónindependientefinalconforme ymanifiestodeformulariosrealesantesmotores.

Doseconómicascompletadas,0fallos/reemplazos/backteststécnicos. Doschecksprogramáticos,1fallotécnicoy1pass,noeconomíainterna. Desde r9:30económicascompletadas, no30muestrasindependientes;bloqueV1–V6209conservadoseparado. Ppresupuestocerrado,sin nuevosvecinos/ablaciones decomponentes,risk,prioridad,gestiónoplazos. Sinestrés,nuevos2026,live/paper/Pi,instalaciones,reinicios,configglobal. La autorización de contingenciaDockerlocal sólo aplica sifallaMCPdenuevo.

Control de repetición adicional:CROSS_P yaBTCindividual2%/3x/fundingconcapnocional1x,cupo1entrada/día,screen2020-09a2024-01CAGR21.3292%. No estuvo sinfunding ni sinriesgoactual;no nueva economía CROSS ni retirarcappararescatar. No selecciónnuevadefinalistasV5cerradas.

Continuidad:otra pregunta material,protocolo ypresupuestoantesdenuevaprueba;actualmente se contrasta inventario para residualBTC/ETHcontrarian vscontrolprecioBTC, sin estrategias/jobsaprobadosaún. Ningunapromoción ni autorizaciónoperativa/estrés.

## Años y ventanas móviles, descripción

Calculados aritméticamente desde los63intervalos R11 completos delreciboMCP (62mesescompletos para este resumen), usando productos de retornos M1/frontera declarada. Se excluye2020 incompleto de añosanuales;51ventanas12meses solapadas no son independientes ni OOS. No cambian gates/veredictos ni se usan para nuevos filtros.

K1001: añoscompletos={"2021":37.754599469109664,"2022":30.137400778791168,"2023":46.386546735302446,"2024":11.405045108153988,"2025":13.967847464097982};rolling12={"N":51,"positive":46,"min":{"start":"2023-07","finish":"2024-06","return_pct":-7.806699187854072},"max":{"start":"2022-07","finish":"2023-06","return_pct":67.37900185704851}}.

N204: añoscompletos={"2021":37.72403744564716,"2022":27.511781442433957,"2023":42.26544154555545,"2024":10.88869735715441,"2025":11.047192591105404};rolling12={"N":51,"positive":46,"min":{"start":"2023-08","finish":"2024-07","return_pct":-9.240395861709516},"max":{"start":"2022-03","finish":"2023-02","return_pct":69.32315922926566}}.


## Antecedente R14 completo en Hub r6

```json
{
  "id": "BTC_R14",
  "title": "BTC_R14: evidencia previa",
  "asset": "BTC",
  "family": "ablación / tendencia",
  "execution": "revisión intermedia completada",
  "evidence": "histórica; alcance del informe",
  "objective": "sin evaluar para el nuevo programa",
  "hypothesis": "Doce backtests nuevos y cuatro anclas reutilizadas; ninguna variante supera puertas congeladas.",
  "origin": "Investigación anterior al Hub; inventarios completos enlazados",
  "method": "Inventario y lectura de cierres existentes, sin nuevas ejecuciones.",
  "protocol": null,
  "budget": "No mezclar con conteos V1–V6",
  "versions": "Fuentes y configuración en reportes originales; proxies no equivalen a perpetual nativo.",
  "periods": [
    "2020–2025 reutilizado"
  ],
  "results": {
    "scope": "R14 al perfil2%/6%/3x,10k compartidos; no una rentabilidad BTC aislada.",
    "variants": "Quitar suplemento y eficiencia long redujeron neto;EMA120conpendiente dependió de una entrada y falló amplitud/Calmar. Ninguna pasó gates.",
    "incremental_case_correction": "La ventaja K1001 sobre Y902 del contrato históricoR10 procede de tres situaciones discordantes, no cinco casos independientes.",
    "fixed_profile_annual_C": {
      "source": "strategies/MultiAssetRetestBtcShort4h/reports/BTC_R14_SIN_FUNDING_RESULTS_20261020.md",
      "scope": "K1001 BASE_C annual MTM returns already reported;2020and2025partial",
      "nominal_pct": {
        "2021": 45.54,
        "2022": 18.1,
        "2023": 42.07,
        "2024": 32.47,
        "2020_partial": 7.14,
        "2025_partial": 36.13
      },
      "stress_pct": {
        "2021": 39.63,
        "2022": 15.38,
        "2023": 37.33,
        "2024": 26.26,
        "2020_partial": 6.19,
        "2025_partial": 16.81
      },
      "interpretation": "Historical CAGR does not imply20–30%every year; above30%is not rejected merely for exceeding an orientative target. Portfolio CAGR does not prove each component target."
    }
  },
  "limitations": [
    "Sin evaluación de la nueva línea.",
    "Correlaciones, pérdidas simultáneas y comparación con/sin pieza bajo riesgo comparable: sin evaluar en esta revisión.",
    "Leer los addenda y registros; no sumar curvas aisladas como cuenta compartida."
  ],
  "audit": "Revisión documental r5 por tres revisores con contraste de root; no nueva validación económica. Doce summaries y dos lecturas puntuales de cierre corroborados, sin reauditar todos los fills.",
  "decision": "R14 cerrado sin variante elegible. Conservar K1001/N204 como referencias; no retirar suplemento, apagar longs o retocar EMA a partir de2026. R5 no abre otra exploración.",
  "references": [
    {
      "label": "Resultados de la validación r5",
      "path": "strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261021-r6/VALIDATION_R5_RESULTS.md"
    },
    {
      "label": "BTC_R14_SIN_FUNDING_RESULTS_20261020.md",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/BTC_R14_SIN_FUNDING_RESULTS_20261020.md"
    },
    {
      "label": "Auditoría de tres situaciones discordantes",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/BTC_K1001_DISTINCT_CASE_AUDIT_20261019.md"
    }
  ],
  "sessions": []
}

```

## Antecedente preflight legacy completo en Hub r2

```json
{
  "id": "LEGACY",
  "title": "Causalidad y contabilidad legacy",
  "asset": "BTC",
  "family": "legacy",
  "execution": "auditado",
  "evidence": "técnica acotada",
  "objective": "sin evaluar",
  "hypothesis": "Reutilizar ideas exige causalidad y unidades correctas.",
  "origin": "Preflight legacy 2026-10-20",
  "method": "Extracción AST y microvalidaciones sintéticas; no backtests nuevos.",
  "protocol": null,
  "budget": {
    "economic_new": 0
  },
  "versions": "Hashes originales listados en el preflight",
  "periods": [
    "Ejemplos sintéticos; no ventana económica"
  ],
  "results": {
    "corrected_profitability": null,
    "findings": [
      "oi_price_divergence remapea último cierre del día corriente a velas anteriores.",
      "En trayectoria auditada, funding divide de nuevo por100 y usa tiempo desde entrada en lugar de liquidación exchange.",
      "No hay A/B limpio que atribuya la ventaja del modelo a funding."
    ]
  },
  "limitations": [
    "Falla localizada: no acusar a todas las variables OI.",
    "No se cuantificó rentabilidad corregida ni se reentrenó ML.",
    "Archivos legacy incluyen 2026: exposición previa declarada."
  ],
  "audit": "Preflight original por MCP",
  "decision": "No portar literalmente ni transferir resultados como evidencia económica.",
  "references": [
    {
      "label": "Preflight original",
      "path": "strategies/FundingIntegrationSmoke1m/reports/LEGACY_PREFLIGHT_AND_FUNDING_WALK_FORWARD_PILOT_20261020.md"
    }
  ],
  "sessions": []
}

```

## Referencias leídas adicionales y límites

BTC_DISCOVERY_P_PROTOCOL_20261021.md fue leído completo antes de este diseño; fija helpers/gestión/fuentes originales R12 y cuenta BTC100%. K1001_DEEP_DIAGNOSTIC_FINDINGS_20261021.md, JOIN_CODE_V3, MTM_ORIGIN_PROTOCOL_AND_CODE y ambosRESULT/MTM fueron leídos en la revisión independiente conservada. Sus tablas NO son cuentascomponentes ni control causal para este experimento.

Hub index actual leído:20261021-r26. Revisionr26 preserva48económicasdesder9,diagnóstico192trades sin motores y acuerdo humano de cuotas1%/2/3% sobre mismo BTCtotal. El siguiente paso antiguo de ocupación en esa revisión quedaHOLD por decisión posterior root, sin borrar revisión. R8revision leída:BTCindividualantescartera,regularidad/mediana distintas,noautorización de cuentascombinadas. No copiar como contrato vigente una pausa histórica r8 superada por la autorización humana actual; tampoco reabrir sus propuestas no aprobadas de cartera.

El anexo no pretende un censo global ni nulidad de resultados previos; no se consultó economía2026nueva,velas o datasets. No se pega literatura externa. El formularioP reproducido arriba debe clonarse genuinamente después delreview, conservando10000totales; la cuota1% se implementará sólo en los argumentos.5/.5delhelperlegacy.
