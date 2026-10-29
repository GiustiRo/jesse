# K1001 LONG MARKET: CODES y antecedentes congelados

Fecha documental: 2026-10-21. Protocolo normativo: K1001_LONG_MARKET_PROTOCOL_20261021.md. Sólo snapshots completos de fuentes existentes leídas por MCP antes de implementar. No contiene una clase nueva creada ni autoriza escribir padres.

## Referencia y formulario genuino

Control reutilizado: [LONG_ONLY LIMIT](http://localhost:9200/#/backtest/5c29961d-419a-4207-ae3c-58ad6ccb318c), estado finished recuperado por get_backtest_session. Su strategy_codes embebido coincide exactamente con el wrapper LONG_ONLY leído. Los padres/dependencias completos siguientes se congelan por contenido; no inferir que el snapshot de sesión incluye todos los padres (sólo incluye wrapper).

Formulario de state.form recuperado íntegro del control, no inventado ni draft nuevo. Cambiar solamente nombre de estrategia y metadatos identificativos después de revisión y autorización:

```json
{
  "exchange": "Binance Perpetual Futures",
  "routes": [
    {
      "exchange": "Binance Perpetual Futures",
      "symbol": "BTC-USDT",
      "timeframe": "1m",
      "strategy": "BtcResearchR16K1001LongOnly1m"
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

## BtcResearchR16K1001LongOnly1m

SHA256 de texto UTF8 completo: 703a63b968d532e57527fd485c83493685ed77c39a486c9dff97674f6e6a3289.

```python
from strategies.BtcResearchR16K1001QuotaBase1m import BtcResearchR16K1001QuotaBase1m


class BtcResearchR16K1001LongOnly1m(BtcResearchR16K1001QuotaBase1m):
    GROUP = "LONG_ONLY"

```

## BtcResearchR16K1001QuotaBase1m

SHA256 de texto UTF8 completo: 5f41d87af1eeb629a381d6bcc63de8595897646357864f9e28a913b3e631c884.

```python
import math
from datetime import datetime, timezone

from strategies.BtcResearchR16LegacyK1001m import BtcResearchR16LegacyK1001m
from strategies.BtcResearchR16LegacyBase1m import legacy_long, legacy_short, legacy_plan
from strategies.BtcResearchR10Base4h import BAR

# The account still starts at10000. Both halves are fixed allocations of its
# current wallet/free margin, not a second account or a redistribution rule.
QUOTA = .5


def quota_counts():
    return dict(fills=0, closes=0, net=0.0, trace_completed=0, trace_missing=0)


def quota_year(timestamp):
    return str(datetime.fromtimestamp(timestamp / 1000, timezone.utc).year)


class BtcResearchR16K1001QuotaBase1m(BtcResearchR16LegacyK1001m):
    """Original K1001 groups with1% total-account risk; observational trace only.

    before, supplement latch, indicators, order lifetime and management remain
    inherited. Only the permitted group and the .5/.5 sizing arguments change.
    Observed R uses open0, later closed M1 marks and the actual exit fill; it is
    neither intraminute MFE/MAE nor a counterfactual path after the real exit.
    """
    GROUP = "abstract"

    def _quota_state(self):
        state = self.vars.get("k1001_quota")
        if state is None:
            assert self.GROUP in ("LONG_ONLY", "SHORT_BOOK")
            state = dict(active=None, trade_sequence=0, last_fill_identity=None, errors={},
                         sources={name: quota_counts() for name in
                                  ("LONG_RUNNER", "CORE_SHORT", "SUPPLEMENT")},
                         open_years={}, close_years={})
            self.vars["k1001_quota"] = state
            self._log("K1001_QUOTA_CONFIG", dict(
                group=self.GROUP, mode=self.MODE, account_start=10000,
                capital_fraction=QUOTA, margin_fraction=QUOTA,
                target_risk_total=.01, aggregate_limit=.06, leverage=3,
                reserve=.001, lot=.001, redistribution=False,
                price_trace="open0_pre_strictly_after_open_exit_fill"))
        return state

    def _quota_error(self, reason):
        state = self._quota_state()
        count = state["errors"].get(reason, 0) + 1
        state["errors"][reason] = count
        # Record the first example; counters expose repeated failures without
        # producing one error line per M1 callback.
        if count == 1:
            self._log("K1001_QUOTA_TRACE_ERROR", dict(
                reason=reason, time=int(self.time), group=self.GROUP))

    def _prepare_entry(self):
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
        # Use only the event generated by inherited before. In particular, no
        # second supplement evaluation or previous_setup write is permitted.
        if self.GROUP == "LONG_ONLY":
            candidates = (legacy_long(rows),)
        else:
            assert self.GROUP == "SHORT_BOOK"
            candidates = (legacy_short(rows), self.vars.get("supplement_event"))
        capital = max(0.0, float(self.balance))
        margin = float(self.available_margin)
        for candidate in candidates:
            if candidate is None:
                continue
            # Keep the frozen .02 helper: .02*.5 ==.01 of this account's wallet.
            # Its .90 buffer on half free margin leaves the other half unused.
            plan = legacy_plan(candidate, QUOTA*capital, QUOTA*margin,
                               float(self.leverage), float(self.fee_rate))
            if plan is not None:
                self.vars["plan"] = dict(plan, signal_at=now, expiry=now+BAR)
                self.vars["direction"] = plan["direction"]
                self.vars["signals"] = self.vars.get("signals", 0)+1
                self._log("K1001_QUOTA_PLAN", dict(
                    time=now, group=self.GROUP, origin=plan["origin"],
                    qty=plan["qty"], risk_budget=plan["risk_budget"],
                    capital_total=capital, capital_scaled=QUOTA*capital,
                    margin_total=margin, margin_scaled=QUOTA*margin,
                    planned_loss=plan["planned_loss"],
                    planned_stop_fees=plan["planned_stop_fees"],
                    reserve=plan["reserve"], gross_limited=plan["gross_limited"],
                    margin_limited=plan["margin_limited"], expiry=now+BAR))
                return plan["direction"]
        return 0

    @staticmethod
    def _quota_identity(plan):
        return (plan["origin"], int(plan["signal_at"]), int(plan["filled_at"]),
                float(plan["actual_entry"]), float(plan["qty"]),
                float(plan["distance"]), int(plan["direction"]))

    def _quota_start_trace(self):
        state = self._quota_state()
        plan = self.vars.get("position_plan")
        if plan is None:
            self._quota_error("open_without_position_plan")
            return
        identity = self._quota_identity(plan)
        if state["last_fill_identity"] == identity:
            return  # Same open hook, not a second executed fill.
        state["last_fill_identity"] = identity
        state["trade_sequence"] += 1
        state["sources"][plan["origin"]]["fills"] += 1
        year = quota_year(identity[2])
        rows = state["open_years"].setdefault(year, {})
        rows.setdefault(plan["origin"], quota_counts())["fills"] += 1
        # Execution counts are independent of whether its observational trace
        # can be completed. A trace failure must not erase a real native fill.
        active = state["active"]
        if active is not None:
            active["broken"] = True
            self._quota_error("overlapping_trace_identity")
            return
        entry, distance = identity[3], identity[5]
        if not (math.isfinite(entry) and entry > 0
                and math.isfinite(distance) and distance > 0):
            self._quota_error("invalid_open_price_or_distance")
            return
        opened = identity[2]
        state["active"] = dict(
            identity=identity, trace_id=state["trade_sequence"],
            origin=plan["origin"], signal_at=int(plan["signal_at"]),
            opened_at=opened, entry=entry, qty=float(plan["qty"]),
            distance=distance, direction=int(plan["direction"]),
            min_r=0.0, max_r=0.0, min_at=opened, max_at=opened,
            min_stage="open", max_stage="open", first_at=opened,
            last_at=opened, last_stage="open", last_pre_at=None,
            marks=1, m1_marks=0, broken=False)

    def _quota_mark(self, trace, price, timestamp, stage):
        if stage == "pre":
            if timestamp <= trace["opened_at"]:
                return False  # A close at the fill timestamp is not post-fill.
            previous = trace["last_pre_at"]
            if previous is not None and timestamp <= previous:
                if timestamp < previous:
                    trace["broken"] = True
                    self._quota_error("backward_pre_timestamp")
                return False
        if not math.isfinite(price) or price <= 0:
            trace["broken"] = True
            self._quota_error("nonfinite_or_nonpositive_mark")
            return False
        if timestamp < trace["last_at"]:
            trace["broken"] = True
            self._quota_error("backward_mark_timestamp")
            return False
        value = trace["direction"]*(price-trace["entry"])/trace["distance"]
        if not math.isfinite(value):
            trace["broken"] = True
            self._quota_error("nonfinite_price_r")
            return False
        # Strict changes retain the first phase/time on ties. Open and exit
        # remain distinct even when a real trade has zero holding time.
        if value < trace["min_r"]:
            trace.update(min_r=value, min_at=timestamp, min_stage=stage)
        if value > trace["max_r"]:
            trace.update(max_r=value, max_at=timestamp, max_stage=stage)
        trace.update(last_at=timestamp, last_stage=stage, marks=trace["marks"]+1)
        if stage == "pre":
            trace["last_pre_at"] = timestamp
            trace["m1_marks"] += 1
        return True

    def _observe(self, stage):
        value = super()._observe(stage)
        # Never call the parent observer twice or alter its returned equity.
        state = self._quota_state()
        if stage == "open":
            self._quota_start_trace()
        elif stage == "pre" and self.is_open:
            trace = state["active"]
            plan = self.vars.get("position_plan")
            if trace is None or plan is None:
                self._quota_error("pre_without_trace_or_plan")
            elif trace["identity"] != self._quota_identity(plan):
                trace["broken"] = True
                self._quota_error("pre_identity_mismatch")
            else:
                # self.price here is the same already-closed M1 close supplied
                # to R11's pre observer. Do not use high/low or later prices.
                self._quota_mark(trace, float(self.price), int(self.time), "pre")
        return value

    def on_close_position(self, order, closed_trade):
        # Complete our observer before R16 clears its plan and R11 can emit FINAL.
        state = self._quota_state()
        plan = self.vars["position_plan"]
        origin = plan["origin"]
        trace = state["active"]
        complete = False
        if trace is not None and trace["identity"] == self._quota_identity(plan):
            marked = self._quota_mark(
                trace, float(closed_trade.exit_price),
                int(closed_trade.closed_at), "exit")
            complete = marked and not trace["broken"]
        else:
            self._quota_error("close_identity_missing_or_mismatch")
        net = float(closed_trade.pnl)
        opened_year = quota_year(int(plan["filled_at"]))
        closed_year = quota_year(int(closed_trade.closed_at))
        open_rows = state["open_years"].setdefault(opened_year, {})
        close_rows = state["close_years"].setdefault(closed_year, {})
        # All three ledgers refer to executed trades, never signal cohorts.
        for row in (state["sources"][origin],
                    open_rows.setdefault(origin, quota_counts()),
                    close_rows.setdefault(origin, dict(
                        closes=0, net=0.0, trace_completed=0, trace_missing=0))):
            row["closes"] += 1
            row["net"] += net
            row["trace_completed" if complete else "trace_missing"] += 1
        payload = dict(
            group=self.GROUP, origin=origin, trade_id=str(closed_trade.id),
            signal_at=int(plan["signal_at"]), opened_at=int(plan["filled_at"]),
            closed_at=int(closed_trade.closed_at), entry=float(plan["actual_entry"]),
            exit=float(closed_trade.exit_price), qty=float(plan["qty"]),
            distance=float(plan["distance"]), net=net, trace_complete=complete,
            exit_order_id=str(order.id), exit_order_type=order.type,
            exit_submitted_via=order.submitted_via)
        if trace is not None and trace["identity"] == self._quota_identity(plan):
            payload.update({key: trace[key] for key in (
                "trace_id", "min_r", "max_r", "min_at", "max_at", "min_stage",
                "max_stage", "first_at", "last_at", "last_stage", "marks", "m1_marks")})
        self._log("K1001_QUOTA_PRICE_TRACE", payload)
        state["active"] = None
        super().on_close_position(order, closed_trade)

    def _emit(self, stage):
        super()._emit(stage)
        state = self._quota_state()
        self._log("K1001_QUOTA_STATS", dict(
            stage=stage, group=self.GROUP, sources=state["sources"],
            open_years=state["open_years"], close_years=state["close_years"],
            trace_errors=state["errors"],
            open_trace=state["active"] is not None))

```

## BtcResearchR16LegacyK1001m

SHA256 de texto UTF8 completo: bf88cb663d8561e107446bfce32024ed87531d096362671f7aafce72a09f25ad.

```python
from strategies.BtcResearchR16LegacyBase1m import BtcResearchR16LegacyBase1m


class BtcResearchR16LegacyK1001m(BtcResearchR16LegacyBase1m):
    MODE = "K1001"

```

## BtcResearchR16LegacyBase1m

SHA256 de texto UTF8 completo: 56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542.

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

## BtcResearchR11Base1m

SHA256 de texto UTF8 completo: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87.

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

## BtcResearchR10Base4h

SHA256 de texto UTF8 completo: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9.

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

## Cierre completo de los dos escenarios: referencia, no permiso para vecinos

# K1001: diagnóstico primero y dos escenarios originales con cuota1%

[Long original](http://localhost:9200/#/backtest/5c29961d-419a-4207-ae3c-58ad6ccb318c) y [libro short original](http://localhost:9200/#/backtest/aa79608f-70fd-42aa-8047-ed6bc31133c2). Ambas ejecuciones terminaron y conciliaron. Ninguna alcanza el objetivo económico. El diagnóstico de192 trades del [K1001 original](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4) se completó ANTES de diseñar estos escenarios.

## Qué se midió

Dos mundos alternativos, cada uno con cuenta BTC total10.000USDT y sólo su cuota1% activa; la otra cuota queda inactiva. Se conservan señales, indicadores, latch, prioridad core→suplemento, órdenes, stops, targets y gestión originales. Único cambio económico: grupo permitido y legacy_plan con.5balance/.5available_margin. No subcuenta5.000, no2%por derivada ni redistribución.

BTC-USDT Binance Perpetual Futures, UTC[2020-10-15,2026-01-01),desarrollo ya observado, cuota1%,3xaislado,fee.00045por lado y funding histórico aplicado/verificado con proxies explícitos. Slippage modelado0, reserva.001 sólo sizing. No estrés ni nueva economía2026. No son posiciones simultáneas ni simulación conjunta; NO sumar curvas/CAGR/netos como una cuenta financiada.

|Escenario|N|CAGR neto sobre10.000|PF neto USDT|DD M1+fills|Meses activos positivos|Trimestres positivos|Mediana mes calendario|
|---|---:|---:|---:|---:|---:|---:|---:|
|LONG_ONLY|31|6.7079%|3.5520|8.4730%|13/28=46.43%|8/20=40%|0%|
|SHORT_BOOK|172|5.9247%|1.5277|8.6080%|38/58=65.52%|16/20=80%|0.5191%|

Long neto4030.903490,final14030.903490; short neto3501.965680,final13501.965680. Cada importe pertenece a SU trayectoria alternativa. Neto aritmético sin los dos mejores meses:1397.792214 y2735.482375, respectivamente. El long falla CAGR/M65/Q80/mediana y N100; su muestra es además limitada. El short supera todas las puertas prefijadas salvo CAGR30%. No es candidata por cercanía, PF, regularidad o menor DD. N100 es mínimo operativo preliminar, no potencia ni confianza estadística.

## Preguntas respondidas

**¿Separarlos produce más fills long?** En esta ejecución, no: las31 entradas long coinciden exactamente por origen+signal_at+opened_at con el original; las31 salidas coinciden en tiempo y precio. Diferencia máxima Rneto común1.42e−13. No aparecieron fills long adicionales al retirar los shorts bajo estas reglas/ventana; esto no reconstruye todos los candidatos raw bloqueados. No es una conclusión universal sobre otro diseño.

**¿Qué cambia en short?** Hay158 entradas originales comunes,14 nuevas y3 originales ausentes:172 frente a161 shorts del Koriginal. Las158 salidas comunes conservan tiempo/precio y Rneto, diferencia máxima2.87e−14. La secuencia y disponibilidad importan: no es simplemente añadir11 trades a una lista fija. Los14 nuevos tuvieron neto descriptivo−112.414048 a los tamaños de esta trayectoria; no es efecto causal incremental de cartera ni prueba significativa sobre señales. No rescatar excluyéndolos.

**¿Cada pieza muestra un perfil distinto?** Sí en estos escenarios, sin acreditar diversificación conjunta: long muestra payoff asimétrico y pocas operaciones/meses positivos; short tiene regularidad cercana a las puertas pero una ventaja por operación modesta. CORE_SHORT124trades,net1115.043286,PF1.2075,mediaRneto.08350; SUPPLEMENT48trades,net2386.922394,PF2.8900,mediaRneto.50779. Conservar todo el libro short; no quitar core tras atribución.

**¿El mayor PF long significa mejor señal?** No: el PF enUSDT subió respecto al original pese a ser exactamente las mismas31 trayectorias de precio yRneto. Cambió su ponderación monetaria por cuota/capitalización propia. Las mejoras de PF monetario no son por sí solas mejoras de señal.

**¿Las pérdidas long nunca avanzan favorablemente?** Los18 perdedores tuvieron mediana del máximo M1+fill observado.9205R y medianaRneto−.9817. Los13ganadores,medianas máximo5.9106R yRneto3.4013. Hay devolución observada, pero no demuestra salida mejor: estos máximos se conocen después, no son precios ejecutables, y el trailing opera con cierres4h. No diseñar un target desde los máximos ni llamar al trace MFE/MAE intraminuto. Las salidas originales censuran toda trayectoria posterior.

## Años completos de cada cuenta

|Año|LONG_ONLY|SHORT_BOOK|
|---|---:|---:|
|2021|16.0912%|−0.3930%|
|2022|−1.4756%|16.2705%|
|2023|13.9989%|8.8734%|
|2024|3.1153%|5.5485%|
|2025|−0.0899%|5.0129%|

Son retornos MTM de cuentas alternativas, derivados de fronteras mensualesR11; no cohortes de trades por año. No sumarlos ni escalar cuota para fabricar objetivo30%.

## Auditoría y límites técnicos

203operaciones entre escenarios alternativos,203OPEN/CLOSE/traces únicos,658+520pagos de funding completos. Gross−fees+funding=PNL=equityfinal−10.000 a<1e−6USDT en cada cuenta.31campos funding ausentes(1long/30short) se comprobaron sin pagos por sus ledgers completos, nunca se imputaron ceros por ausencia. Formulario/fuentes/hashes congelados antes de motores y68outcomes sintéticosPASS en primer job. Dos motores económicos nuevos,0fallos/reemplazos/backtests técnicos.50IDs económicos ejecutados y completados desde r9, sin independencia implícita ni sumar con V1–V6.

R11 validó2.741.760marcasM1,63intervalos mensuales/62completos,20trimestres,invalid_windows0; DD es M1+fills, no todos los extremos intraminuto. Trazas203/203 completas, geometría/fills/netos unidos1:1; fuentes/planes/riesgo1% y ledgers conciliados. Comparaciones monetarias contra Koriginal2% no son ablation causal de ocupación porque cuota/capitalización también cambian.

El auditor mecánicoV1 pasólong y falló al parsear una línea K1001_QUOTA_STATSshort: MCP recorta líneas a2000caracteres+[line cut]. Línea original y fallo conservados. V2 recupera sólo prefijo íntegro stage/group/sources/open_years etiquetado PARCIAL; close_years se reconstruye de ejecuciones, no se presenta como campo nativo recuperado. Ausencia de errores diagnósticos inferida bajo logging completo/código congelado que emite primera ocurrencia; tracefinalcerrado inferido de cobertura1:1 y métricaopen0. Nada se inventó del sufijo perdido. No rerun económico por telemetría redundante.

El archivo metadata del análisis incluía pagos completos y superaba el transporte del lector: no se pidió ni parseó truncado. Se usaron los12exports acotados completos de trades y summaries/ledgersMCP. Recibos/fuentes/códigosV1/V2/resultados completos guardados y leídos íntegros.

## Decisión

Dos escenarios cerrados sin candidata. La separación por sí sola no resolvió el objetivo; no modificar cuota ni criterios para aprobar. Original K1001 queda referencia, no ganadora operativa. Una combinación conjunta sigue sin probarse.

Continuar autónomamente con otra pregunta material sustentada en estos datos y contrastada con antecedentes: distinguir la escasez de follow-through de una supuesta mala captura, y conservar el bloque creativo sobre selección de fills. El siguiente diagnóstico/protocolo debe cambiar una decisión real; no reabrir filtrosR14, optimizar extremos retrospectivos ni repetir cuentas por nombre.

## Descriptivos posteriores de periodo y embudo existente

Cohortes por AÑO DE ENTRADA,2021–2023 frente a2024–2025;2020incompleto excluido de esta comparación. No son retornos anuales MTM ni prueba causal, y los tamaños son pequeños. LongN13/14: mediaRneto2.3759→.2422,mediana máximoM1+fill2.6251→1.3271R,mediana devolución1.7672→1.5488R. Menor recorrido favorable observado acompaña el deterioro; no se observa una mayor devolución mediana reciente. No justificar un parche del trailing desde la caída global.

SuplementoN24/23: mediaRneto.8044→.2641,máximo observado mediano1.4191→.5830R,devoluciónmediana.1916→.4771R; señal mixta entre recorrido y captura observados. CoreN73/43: mediaRneto.09495→.14080,máximomediano.7082→.7296R,devoluciónmediana≈0ambos; no todo componente empeoró. Estas cohortes siguen censuradas por las salidas originales; no identifican causalidad ni la ventaja de otra entrada/salida.

Embudo de órdenes long ADMITIDAS en el escenario existente:45planes,31fills,14cancelaciones. No son todas las señales raw, ni14episodios independientes. Dos cancelaciones están separadas exactamente por el TTL4h; la agrupación cronológica no es muestra estadística.45tampoco es techo de trades de otra política, que cambiaría ocupación. Los contadores YA están disponibles y no justifican por sí solos otro replay. La siguiente decisión de valor de información contrasta una medición de trayectorias con una posible comparación económica directa, revisando antecedentes antes de definir un motor.

Recibos y crítica independiente de cierre documentan alcance: revisión nativa de summaries/terminales y códigos, sin segunda auditoría independiente de203filas/1178pagos. El campo estructurado sources.*.observed_max_R del JSON se define como MEDIANA de máximos por trade; no máximo global.


## Deduplicación independiente íntegra y límites de evidencia

SHA256 del informe recibido: efa037ec85c24ac292cc9203194e23aefe7a75e1abe10a76385f1b80055bb0c8. Sus fuentes y búsquedas corresponden a su autor; este anexo no afirma haber reejecutado cada búsqueda. Se leyó el informe completo y se conserva con alcance acotado, comentarios históricos no reauditados y grupos cronológicos no independientes.

# K1001 LONG MARKET vs LIMIT: deduplicacion y valor de informacion

Fecha: 2026-10-21. Revision independiente documental, sin codigo de estrategia, drafts, jobs, motores ni consultas nuevas de velas. Root acepta preparar una sola comparacion economica; este informe registra el fundamento y los limites, no sustituye su protocolo posterior.

## Recomendacion unica y decision que cambia

Preparar UN contraste de politica LONG_ONLY MARKET frente al LONG_ONLY LIMIT de cuota1% ya ejecutado y congelado. No gastar primero un motor replicando el original para un diagnostico observacional de45cohortes: los contadores ya existen y ese estudio no decide el resultado economico de la politica alternativa.

Pregunta: bajo el mismo setup long K y la misma gestion, compensa comprar la ruptura confirmada frente a esperar el retesteo? La regla original incluye una apuesta adicional: exige cierre por encima del maximo previo26, pero coloca LIMIT en ese maximo por cuatro horas. El contraste no inventa una familia MARKET breakout: identifica el valor de esa pieza concreta de K bajo el contrato actual.

Si la politica completa no mejora materialmente retorno/regularidad con riesgo compatible y no alcanza las puertas, cerrar esta comparacion sin offsets MARKET, TTL alternativos, reclaim, BE, trailing o filtros vecinos. Mejor PF monetario, mas fills o una cancelacion favorable no justifican promocion. Una mejora que siga incumpliendo puertas tampoco cumple el objetivo ni autoriza automaticamente mas vecinos.

## Evidencia que motivo la pregunta

Fuente principal leida completa:
- strategies/FundingOiPilot4h/reports/K1001_QUOTA_SCENARIOS_FINAL_20261021.md.
- Fuentes congeladas BtcResearchR16LegacyBase1m, BtcResearchR16LegacyK1001m, BtcResearchR16K1001QuotaBase1m y wrappers LONG_ONLY/SHORT_BOOK, previamente leidas completas.

[LONG_ONLY congelado](http://localhost:9200/#/backtest/5c29961d-419a-4207-ae3c-58ad6ccb318c):31trades, CAGR6.7079%,13/28meses activos positivos,8/20trimestres,mediana calendario0%. Sus entradas/salidas y R coinciden con el long del K original. El PF monetario mayor resulta de ponderaciones y capitalizacion distintas, no de mejor senal.

Root extrajo despues de logs completos45planes LONG=31fills+14cancelaciones. Estas cancelaciones forman13GRUPOS CRONOLOGICOS contiguos4h, NO13episodios independientes ni13muestras estadisticas. Corrijo expresamente mi mensaje anterior que los llamo episodios. Son planes bajo la politica LIMIT original, no el universo exogeno de otra politica ni upper bound de sus entradas: ocupacion, reentradas, fill y capital posterior pueden cambiar.

Los maximos M1+fills de los31trades no son MFE/MAE intraminuto ni precios ejecutables. Las salidas originales censuran el camino posterior. La devolucion retrospectiva no demuestra una salida mejor y no motiva targets/BE/trailing. El contraste propuesto responde directamente el valor de esperar el retesteo, sin inferirlo de esos maximos.

## Deduplicacion amplia: antecedentes encontrados

| Antecedente leido | Coincidencia | Diferencia material frente al contraste exacto pendiente |
|---|---|---|
| TrendBreakout5m, fuente completa por MCP | Ya usa MARKET y documenta comparacion antigua con LIMIT al nivel roto15-60min. La propia fuente afirma deterioro del neto2020-25 con retesteo. Esa cifra es afirmacion historica del codigo; no reaudite aqui sus sesiones ni encontre recibo en su carpeta reports. | Senales1h y timing5m, canal72h por defecto, EMA50/200 y macroEMA120, SL3ATR, trail3/BE1.5R, guardas diarias/rachas; no setup ni gestion K. No es evidencia independiente ni novedad de mecanismo. |
| BtcMomentumCore4h y BtcMomentumBaseline3, ambas fuentes completas | MARKET Donchian26, EMA20/80 y pendiente, ADX26, RSI52-76 y rango<=3ATR: antecedente muy cercano de la misma familia long. | Sin cota K close<=maximo+ATR; stop con floor.8% y max5.5%; BEdefault1.75R y triggers de tightening basados en HIGH, no solo mejor cierre; inicializacion best_close y sizing/margen distintos, riesgo3/5%, ventana y funding diferentes. No es control exacto de entrada. |
| MultiAssetBreakout4h y MultiAssetBreakoutNear4h, fuentes completas | STOP Donchian4h y gestion emparentada. | Arman ANTES de la ruptura; Near exige high<frontera y distancia<=.5ATR. Cambian admision temporal ademas del tipo de orden. No son MARKET tras cierre confirmado del mismo setup K. |
| Phase2BtcLongContext4h, fuente completa, y atribucion comparable | Long Donchian26 retest LIMIT y gestion ancestral de K. | Es LIMIT, no MARKET. El informe comparable excluye expresamente BTCMomentumBaseline3 como control por reglas diferentes. |
| BTC_NEW_ANGLES_RESULTS_20261018.md, leido | Ya existe experimento negativo de entrada long MARKET tras toque M1 y recuperacion en M1 estrictamente posterior, dentro4h. | Requiere retesteo y confirmacion adicional. La pregunta actual es NO esperar retesteo; no rescatar latencia/reclaim. |
| V1-V2: implementacion V1, FundingWfPilotBase4h/ResearchV2Core4h y cierres | Breakout de limites del dia previo y/o reglas de precio/funding; entradas MARKET. | Senal y gestion fija24h/targets distintas; no ablacion del retest K. |
| V3: ResearchV3Base4h, ResearchV3ChannelP4h y channel_features.py, completos | MARKET tras ruptura de canal con filtro tendencial. | Canal20, SMA120 pendiente6, dos direcciones, gestion trail3/max42barras y restricciones propias; no Donchian26/EMA20-80/ADX/RSI/gestion K. |
| V4-V6: inventarios y cierres consolidados, antecedentes ya revisados | Shock/oscillator/funding/cross/VWAP/deleverage/NR7/eficiencia. | Distintas senales; no se identifico control exacto K LONG LIMIT frente MARKET con gestion preservada. No se reabren sus vecinos ni selectores. |
| Discovery C: protocolo y BtcResearchR11Base1m/Cusum completos | CUSUM entra MARKET tras evento tendencial. | Evento de acumulacion de retornos normalizados, no setup K; ATRsimple/TP2R/48h, gestion distinta. |
| P/U/cuotas posteriores y R14, fuentes/protocolos revisados | P/U/cuotas conservan LONG original; R14 cambia filtros long o ablate suplemento. | No cambian exclusivamente LONG LIMIT a MARKET. R14 ER12>1/3, EMA120/pendiente y ablacion suplemento estan cerrados; progreso24h/1R tambien cerrado. |

Documentos concretos consultados o releidos:
- strategies/BtcMomentumCore4h/reports/BTCUSDT_MomentumCore4h_Report.md.
- strategies/BtcMomentumBaseline3/reports/PHASE2_RISK3_CONTROL_20261018.md.
- strategies/MultiAssetBreakout4h/reports/PHASE2_PROGRESS_20261018.md.
- strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_COMPARABLE_ATTRIBUTION_RESULTS_20261018.md.
- strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_ATTRIBUTION_ORDER_COST_PROTOCOL_20261018.md.
- strategies/MultiAssetRetestBtcShort4h/reports/PHASE2_RESEARCH_HANDOFF_20261018.md.
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_NEW_ANGLES_RESULTS_20261018.md.
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R1_FROZEN_PROTOCOL_20261019.md.
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R14_SIN_FUNDING_PROTOCOL_20261020.md.
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_R14_SIN_FUNDING_RESULTS_20261020.md.
- strategies/OrchManageTurtleDaily/reports/ORCH_GLOBAL_MECHANISM_INVENTORY_20261018.md.
- strategies/FundingOiPilot4h/reports/RESEARCH_V1_IMPLEMENTATION_FINAL.md.
- strategies/FundingOiPilot4h/reports/RESEARCH_CONSOLIDATED_DECISION_20261020.md.
- strategies/FundingOiPilot4h/reports/RESEARCH_WALK_FORWARD_HANDOFF_FINAL_V6_20261020.md.
- strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_C_PROTOCOL_20261021.md.
- Protocolos/fuentes posteriores A-W/Y/AA y P/U/cuotas ya revisados en esta tarea prolongada, sin encontrar esta ablacion exacta.

El informe Core4h contiene afirmaciones antiguas de campeona/OOS ciego/MonteCarlo que fueron corregidas por handoffs posteriores. Aqui se usa como evidencia de existencia y estructura de la politica historica, NUNCA para revivir certificaciones antiguas ni comparar su CAGR con K actual.

Conclusion acotada de la busqueda: no encontre el contraste EXACTO propuesto entre las fuentes/documentos revisados. No es una prueba universal de ausencia en cada sesion historica. El mecanismo generico de comprar rupturas MARKET ya esta ampliamente explorado; la novedad defendible es el control de una sola pieza en K congelado, ahora sustentado por diagnostico y autorizacion humana para estudiar sus fortalezas.

## Alcance que debe preservar el protocolo posterior

Mantener setup K original, incluida cota de extension<=1ATR, ATR de senal/stop inicial2ATR relativo al fill, gestion original, cuota1% de wallet10k y cuota de margen fija, sin redistribuir inactividad. BTC-USDT unico, funding historico ON y mismo snapshot, fee.00045 por lado, reserva.001 solo sizing, slippage modelado0,3x aislado. Mismo historico de desarrollo observado, sin nueva economia2026, estres o variantes de riesgo. Reusar control LONG_ONLY sin rerun economico; preservar sus fuentes/resultados.

Comparar trayectorias economicas nativas completas. MARKET cambia precio y momento de entrada, ocupacion, stops absolutos anclados al fill y capitalizacion: el contraste es de POLITICA COMPLETA bajo el simulador. No convertir las14canceladas en una lista de trades anadidos a31, no sumar PnL de cohortes como efecto incremental ni prometer45trades en MARKET.

La diferencia entre fills y no-fills esta seleccionada por la trayectoria futura. No identifica causalidad economica, flujo, toxicidad del order book o precio ejecutable real. Cualquier resultado conserva dependencia entre episodios/planes, seleccion adaptativa y muestra limitada. Evaluar puertas originales, concentracion y regularidad sin escoger fechas, horizontes o filtros por PnL.

El valor de informacion de un solo contraste supera aqui al replay observacional previo porque decide si conservar o cerrar la espera de retest bajo este setup. No garantiza encontrar una candidata, resolver toda la escasez de long ni justificar integrar long y short en una cuenta conjunta.


## Cierres previos y jerarquía de instrucciones

BTC_DISCOVERY_P_FINAL_20261021.md ya fue leído completo y se conserva sin edición: prohibía vecinos/ablaciones de componente/riesgo/gestión para rescate. La autorización posterior humana/root admite sólo este contraste acotado de entrada, sin borrar el cierre. R14 y V1–V6 conservan sus veredictos. No se copian cifras antiguas de campeona, OOS o Monte Carlo como validación actual.

La propuesta de medir ocupación continúa HOLD, sin wrapper ni motor. El bloque creativo de selección adversa es motivación de pregunta, no selector ni señal. Esta comparación no supone identificar liquidez, causalidad de mercado o PnL contrafactual de canceladas.

## Nuevo código futuro, aún ausente

Nombre propuesto: BtcResearchR16K1001LongMarket1m, heredado de BtcResearchR16K1001LongOnly1m. Únicas modificaciones previstas: _prepare_entry equivalente con validación legacy_long ANTES del clone MARKET y replan .5/.5; log de policy/trigger; _emit observacional con super exactamente una vez y filas MARKET_SUMMARY/SOURCE/COHORT menores de1900 caracteres. Ningún cambio a _observe, gestión, before, latch, broker o padres.

Al implementarse, fuente nueva/readback/hash y revisión del diff deberán guardarse aparte, sin sustituir este CODES previo. El runtime de indicadores/framework se conserva; hashes aquí corresponden a fuentes de estrategia, no a un supuesto hash del kernel Rust o del entorno.

## Precisión normativa posterior antes del único motor: política nominal y tipos nativos

La auditoría estática root del framework y las órdenes completas de las cuotas verifican que Strategy clasifica primero mediante helpers.is_price_near: tolerancia fraccional.00015=0.015%. Por ello, el control LONG_ONLY es una POLÍTICA LIMIT con conversión nativa por cercanía:27entradasLIMIT y4MARKET reales, no31LIMIT estrictas. SHORT_BOOK tiene171STOP+1MARKET. Se conservan fuentes, resultados, comisiones taker y geometría; no es fallo financiero ni motivo de repetir motores. Esta precisión gobierna cualquier frase anterior que pudiera entenderse como espera de retesteo estricta en todos los fills.

Nueva MARKET: precio exacto self.price, por lo que el runtime debe crear todas las entradas como MARKET. La revisión estática/read-only precede al único motor; verificar sus órdenes reales DESPUÉS de ese motor, nunca mediante un preflight económico adicional. order_kind documenta intención y no demuestra ejecución. Preservar este control nativo como contrafactual completo; no forzar ahora27/4 a31LIMIT ni modificar el helper, broker o fuentes frozen.

Evidencia primaria con órdenes, OPENlogs, proporciones trigger/entry y hashes de siete archivos framework: strategies/FundingOiPilot4h/reports/K1001_LONG_MARKET_FRAMEWORK_AND_ENTRY_TYPES_20261021.json y Markdown homónimo. Mercado Sandbox usa current_price del cierreM1 y cola procesada después de estrategia en el mismo paso; self.price cacheado, slippage default0 confirmado en perfil. Prueba estática no es certificación de los futuros fills ni de ejecución real de exchange.
