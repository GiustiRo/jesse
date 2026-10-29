# R34 CROSS — nueva fuente implementada

Fecha local2026-10-22. Una única estrategia nueva BtcResearchR34Cross1m, heredada directamente de R11. Sin cambio de padres, R32, framework o configuración. Sin drafts/motores. Protocolo BTC_CROSS_ARCHIVE_REUSE_PROTOCOL_20261022.md y cap1x adicional conservado; no CLOCK_ONLY.

SHA256 fuente final 834dec643c69a5e9dd6ec1e51cd29a274117d0a99690677657556eba7b441c52. Readback completo idéntico. La primera versión efe504330c0c9894991fa108e2271ea1bce2bf9fa8038e3753dc32140d582d49 está conservada en BTC_R34_CROSS_SOURCE_INITIAL_SUPERSEDED_20261022.md; única correcciónFINISH antes de check. Nuevos logs neutros R34_PLAN/OPEN/CLOSE/SUMMARY y causas compactas<1800, ledger antes deFINAL. Cuota diaria sólo porfill, noreverse,3ATR/720h/sinTP/cruce de salida sinATR; helpersV5puros intactos. Campo reason sólo usa petición explícita o flagterminal/ordenSTOP; MARKET desconocida queda unclassified para auditoría.

Check proporcionado en BTC_R34_CROSS_SUPPLIED_CHECK_20261022.md, aún pendiente de job al escribir este reporte. Código SHA256 043decaecc74cb0fde3aad8b07f443594b5f865298c378ffa8e259a37f23b4b7. Arrays fabricados, AST y stubStrategy; R11 real suministrado enliteral, sin importar estrategia/framework real. No certifica broker/funding nativo. Refinamiento previo del harness a identidadflotante con tolerancia técnica no cambió fuente. No se volvió a copiar megasnapshots de antecedentes.

## Fuente nueva final completa

```python
import json
import math

from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR16LegacyBase1m import legacy_plan, LOT, RESERVE
from strategies.ResearchV5Base4h import BAR, DAY, closed_window, atr_window
from strategies.ResearchV5Base4h.cross_features import cross_state


class BtcResearchR34Cross1m(BtcResearchR11Base1m):
    """Archived CROSS_P rules with the current one-percent specialist contract.

    The signal and exit helpers, 3ATR stop and 180-bar maximum are frozen V5
    choices. Half-wallet sizing adds the current reserve/lot; the old 1x
    total-free-margin cap remains an additional ceiling, never a risk grid.
    """
    LABEL = "CROSS_ARCHIVED_R34"
    HOLD_HOURS = 720

    def _r34_counts(self):
        return self.vars.setdefault("r34_counts", dict(
            events=0, plans=0, occupied=0, rejected_geometry=0,
            opens=0, closes=0, long_opens=0, short_opens=0, net=0.0))

    def _r34_causes(self):
        return self.vars.setdefault("r34_causes", dict(
            decisions=0, invalid_price=0, no_cross=0, boundary=0,
            position=0, pending=0, same_exit=0, daily_quota=0,
            atr_invalid=0, plan_invalid=0, zero_after_cap=0,
            cap_1x_limited=0, exit_pricecross=0, exit_hold=0,
            exit_stop=0, exit_terminal=0, exit_unclassified=0))

    def _r34_log(self, label, payload):
        # Keep complete records below the reader's line cut. No truncation or
        # string slicing may silently discard evidence of a plan or execution.
        line = label + " " + json.dumps(payload, separators=(",", ":"), allow_nan=False)
        assert len(line) < 1800
        self._log(label, payload)

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate - .00045) < 1e-12
            assert abs(self.balance - 10000) < 1e-6
            self.vars["checked"] = True
            self._r34_log("R34_CONFIG", dict(
                label=self.LABEL, fast=20, slow=80, bars=81,
                stop_atr=3, hold_hours=720, tp_r=None,
                risk_total=.01, capital_fraction=.5, margin_fraction=.5,
                cap_1x_basis="total available_margin before order",
                reserve=RESERVE, lot=LOT, redistribution=False))
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        previous = self.vars.get("r34_decision_at")
        if previous is not None and now <= previous:
            return
        self.vars["r34_decision_at"] = now
        self.vars["r34_state"] = None
        counts, causes = self._r34_counts(), self._r34_causes()
        causes["decisions"] += 1
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        rows = closed_window(candles, now, 81)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            causes["invalid_price"] += 1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price),
                            rel_tol=1e-10, abs_tol=1e-8), "R34_ASOF_PRICE"
        state = cross_state(rows, now, 20, 80)
        self.vars["r34_state"] = state
        if not state["valid"]:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            causes["invalid_price"] += 1
            return
        direction = state["direction"]
        if direction == 0:
            causes["no_cross"] += 1
            return
        # Raw crosses, including those used to close, are consumed at this T.
        # A held/blocked cross never becomes a queued future entry.
        counts["events"] += 1
        self.vars["signals"] = self.vars.get("signals", 0) + 1
        self._r34_log("R34_CROSS", dict(
            label=self.LABEL, time=now, direction=direction, **state["details"]))
        if not self.START < now < self.FINISH:
            causes["boundary"] += 1
            return
        if self.vars.get("last_exit_at") == now:
            counts["occupied"] += 1
            causes["same_exit"] += 1
            return
        if self.is_open or self.entry_orders:
            counts["occupied"] += 1
            causes["position" if self.is_open else "pending"] += 1
            return
        day = now // DAY * DAY
        if self.vars.get("r34_entry_day") == day:
            causes["daily_quota"] += 1
            return
        atr = atr_window(rows, now, 0)
        if atr is None:
            counts["rejected_geometry"] += 1
            causes["atr_invalid"] += 1
            return
        entry, distance = float(self.price), 3 * atr["value"]
        capital, margin = max(0.0, float(self.balance)), float(self.available_margin)
        event = dict(origin=self.LABEL, direction=direction, entry=entry,
                     distance=distance, target_distance=None,
                     hold_hours=self.HOLD_HOURS, order_kind="MARKET")
        plan = legacy_plan(event, .5 * capital, .5 * margin,
                           float(self.leverage), float(self.fee_rate))
        if plan is None:
            counts["rejected_geometry"] += 1
            causes["plan_invalid"] += 1
            return
        # V5's separate 1x ceiling uses TOTAL free margin, not the allocated half.
        # Only floor qcap: re-flooring a pre-floored helper quantity can lose a
        # lot through binary rounding even when the cap is not binding.
        cap_qty = math.floor((margin / entry) / LOT) * LOT
        helper_qty = plan["qty"]
        qty = min(helper_qty, cap_qty)
        if qty <= 0:
            counts["rejected_geometry"] += 1
            causes["zero_after_cap"] += 1
            return
        capped = qty < helper_qty
        causes["cap_1x_limited"] += int(capped)
        stop = entry - direction * distance
        unit = distance + self.fee_rate * (entry + stop) + RESERVE * entry
        plan.update(qty=qty, planned_loss=qty * unit,
                    planned_stop_fees=qty * (distance + self.fee_rate * (entry + stop)),
                    signal_at=now, cap_1x_limited=capped)
        assert plan["planned_loss"] <= plan["risk_budget"] + 1e-6
        assert qty * entry <= margin + 1e-6
        meta = dict(state["details"], atr=atr["value"],
                    capital_total=capital, capital_scaled=.5 * capital,
                    margin_total=margin, margin_scaled=.5 * margin,
                    helper_qty=helper_qty, cap_qty=cap_qty, reserve=RESERVE)
        plan["meta"] = meta
        self.vars["plan"] = plan
        self.vars["direction"] = direction
        counts["plans"] += 1
        self._r34_log("R34_PLAN", dict(
            time=now, label=self.LABEL, direction=direction, entry=entry,
            qty=qty, distance=distance, risk_budget=plan["risk_budget"],
            planned_loss=plan["planned_loss"],
            planned_stop_fees=plan["planned_stop_fees"],
            meta=meta, cap_1x_limited=capped))

    def on_open_position(self, order):
        plan = self.vars["plan"]
        now, opened = int(self.time), int(self.position.opened_at)
        direction = 1 if self.is_long else -1
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        assert direction == plan["direction"]
        assert order.type == "MARKET"
        assert now == opened == plan["signal_at"], "R34_MARKET_CLOCK"
        assert math.isclose(entry, plan["entry"], rel_tol=1e-10, abs_tol=1e-8)
        assert abs(qty - plan["qty"]) < 1e-8
        stop = entry - direction * plan["distance"]
        unit = plan["distance"] + self.fee_rate * (entry + stop) + RESERVE * entry
        assert stop > 0 and math.isfinite(unit)
        assert qty * unit <= plan["risk_budget"] + 1e-6
        assert qty * entry <= plan["meta"]["margin_total"] + 1e-6
        self.stop_loss = qty, stop
        self.vars["r34_position_plan"] = dict(plan, filled_at=opened)
        # Quota is charged to the actual opening day, never to an unfilled cross.
        self.vars["r34_entry_day"] = opened // DAY * DAY
        self.vars.pop("r34_exit_requested_at", None)
        self.vars.pop("r34_exit_reason", None)
        self.vars.pop("r34_terminal_seen", None)
        self.vars["entries"] = self.vars.get("entries", 0) + 1
        counts = self._r34_counts()
        counts["opens"] += 1
        counts["long_opens" if direction == 1 else "short_opens"] += 1
        self._r34_log("R34_OPEN", dict(
            time=now, signal_at=plan["signal_at"], opened_at=opened,
            label=self.LABEL, direction=direction, entry=entry, qty=qty,
            distance=plan["distance"], risk_budget=plan["risk_budget"],
            stop=stop, target_distance=None, hold_hours=self.HOLD_HOURS))
        self._observe("open")

    def _r34_request_exit(self, reason):
        now = int(self.time)
        if not self.is_open or self.vars.get("r34_exit_requested_at") == now:
            return
        self.vars["r34_exit_requested_at"] = now
        self.vars["r34_exit_reason"] = reason
        self._r34_log("R34_EXIT_REQUEST", dict(
            time=now, label=self.LABEL, reason=reason))
        self.liquidate()

    def update_position(self):
        now, opened = int(self.time), int(self.position.opened_at)
        if now >= self.FINISH:
            return  # Native terminal liquidation has priority; do not relabel it.
        if now % BAR or now <= opened:
            return
        # The absolute deadline is independent of ATR or current price history.
        if now - opened >= 180 * BAR:
            self._r34_request_exit("hold")
            return
        state = self.vars.get("r34_state")
        if self.vars.get("r34_decision_at") != now or state is None or not state["valid"]:
            return
        if ((self.is_long and state["direction"] == -1)
                or (self.is_short and state["direction"] == 1)):
            # Record the exact cross before liquidation can emit a terminal log.
            self._r34_log("R34_EXIT_CROSS", dict(
                label=self.LABEL, time=now, **state["details"]))
            self._r34_request_exit("pricecross")

    def on_close_position(self, order, closed_trade):
        now, closed = int(self.time), int(closed_trade.closed_at)
        requested = self.vars.get("r34_exit_reason")
        if order.type == "STOP":
            reason = "stop"
        elif (order.type == "MARKET"
              and self.vars.get("r34_exit_requested_at") == closed
              and requested in ("pricecross", "hold")):
            reason = requested
        elif (order.type == "MARKET" and closed >= self.FINISH
              and self.vars.get("r34_terminal_seen") is not None):
            reason = "terminal"
        else:
            # Preserve the uncertainty for native order audit; MARKET alone is
            # not evidence of a timeout, indicator request or terminal close.
            reason = "unclassified"
        counts, causes = self._r34_counts(), self._r34_causes()
        net = float(closed_trade.pnl)
        assert math.isfinite(net)
        counts["closes"] += 1
        counts["net"] += net
        causes["exit_" + reason] += 1
        self.vars["direction"] = 0
        self.vars["r34_position_plan"] = None
        self._r34_log("R34_CLOSE", dict(
            time=now, label=self.LABEL, net=net, reason=reason))
        # Ledger must include this fill before R11 may emit FINAL post-fee.
        super().on_close_position(order, closed_trade)

    def before_terminate(self):
        if self.is_open and int(self.time) >= self.FINISH:
            self.vars["r34_terminal_seen"] = int(self.time)
        super().before_terminate()

    def _emit(self, stage):
        super()._emit(stage)
        self._r34_log("R34_SUMMARY", dict(
            stage=stage, label=self.LABEL, hold_hours=self.HOLD_HOURS, tp_r=None,
            risk_total=.01, capital_denominator="total BTC wallet",
            redistribution=False, **self._r34_counts()))
        self._r34_log("R34_COUNTS", dict(
            stage=stage, label=self.LABEL, **self._r34_causes()))
```
