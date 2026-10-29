# Continuacion A: CODES previos y antecedentes
Fecha local2026-10-22. Normativa: BTC_CONTINUATION_A_PROTOCOL_20261022.md, version adaptada a R32 y leida de vuelta antes de este anexo. No contiene hojas nuevas, drafts, jobs o motores. Se conservan textos existentes completos obtenidos por MCP, sin mutar padres.

## Referencias normativas y de cierre
- strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261022-r31/HANDOFF.md.
- strategies/FundingOiPilot4h/reports/K1001_LONG_SUPPLEMENT_CLOSURE_FINAL_20261022.md.
- strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261021-r4/HANDOFF.md y EXPLORATION_HISTORY.md, completos.
- strategies/FundingOiPilot4h/reports/BTC_R32_COORDINATION_PROTOCOL_20261022.md, completo.
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_NEW_ANGLES_RESULTS_20261018.md: permanencia21shorts, net2138.67/PF2.28, insuficiente/descartada; estas cifras no son el control economico de A.
- strategies/FundingOiPilot4h/reports/RESEARCH_V1_IMPLEMENTATION_FINAL.md y cierres V1-V6. V1/V2 tienen price breakout/refpreviodia con gestion/costos/clock/sizing propios, no una ablationM1equivalente.
- strategies/FundingOiPilot4h/reports/K1001_LONG_MARKET_FINAL_20261021.md, leido completo: comparacioncerrada, no rescatar vecinos.

Las reglas antiguas de fundingOFF/riesgo3%/8%/5x y los estadoshistoricos2026reservado en esosreportes son HISTORICOS; no gobiernan A. Rigen cuota1%por alternativa delcapitalBTCtotal10k,legacyplanhalf,reserva/lote congelados,fundingON y prohibicion de nuevaeconomia2026 delprotocolo actual.

## Infraestructura root: BtcResearchR32SpecialistBase1m
Texto completo actual leido MCP,6263caracteres; padre aislado creado porroot. Hash de este nuevo padre se congelara en manifiesto antes de economia, no se inventa un digest ni se sustituye por hashdepadrelegacy. Es infraestructura de las treslineas, no hoja ni nuevo alpha de A.

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

## BtcResearchR10Base4h
Releido MCP en esta tarea e identidad exacta con freeze previo. SHA256 de textoUTF8 completo: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9.
Solo se usa R11observer/gestion baseR32, R10closed_window/atr14 y R16legacy_plan; no se heredan entradasCUSUM/K ni se ejecuta codigo de esteanexo.

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

## BtcResearchR11Base1m
Releido MCP en esta tarea e identidad exacta con freeze previo. SHA256 de textoUTF8 completo: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87.
Solo se usa R11observer/gestion baseR32, R10closed_window/atr14 y R16legacy_plan; no se heredan entradasCUSUM/K ni se ejecuta codigo de esteanexo.

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

## BtcResearchR16LegacyBase1m
Releido MCP en esta tarea e identidad exacta con freeze previo. SHA256 de textoUTF8 completo: 56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542.
Solo se usa R11observer/gestion baseR32, R10closed_window/atr14 y R16legacy_plan; no se heredan entradasCUSUM/K ni se ejecuta codigo de esteanexo.

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

## Antecedente completo: AngleCombinedBtcAcceptance4h
Texto MCP completo. Uso documental para deduplicacion; NO dependencia runtime y NO fuente a mutar. Su gate es ocupacion de tercioinferior del rango de PROPIAVELA, unicamente para shortoriginal K; no tiempo mas alla de nivelconocido antes de B. Que su resultado sea negativo no demuestra ausencia universal de aceptacion; tampoco autoriza ajustar su120/240. La nueva autorizacion humana/root permite esta variante distinta con comparacionprefijada.

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

## Antecedente V1: funcion price_direction exacta
Extraida literalmente del codigo completo en RESEARCH_V1_IMPLEMENTATION_FINAL.md leido por MCP. No dependencia runtime. Ilustra que el breakout previoexiste; el nuevo par no se llama descubrimiento de ruptura diaria. Familia1 usaba day=floor(now/DAY); al00UTC la barraactual pertenece al diareciencerrado y forma parte del propioH/L. A define D por apertura de B para evitar esa auto-inclusion y exige coincidencia de reloj en ambosmodelos.

```python
def price_direction(candles, now, family):
    rows = candles[candles[:, 0] + BAR <= now]
    if len(rows) < 2 or rows[-1, 0] != now - BAR or rows[-2, 0] != now - 2 * BAR:
        return 0
    c, prev = float(rows[-1, 2]), float(rows[-2, 2])
    if family == 3:
        ref = rows[rows[:, 0] == now - DAY - BAR]
        if len(ref) != 1:
            return 0
        old = float(ref[0, 2])
        return 1 if c > old and c > prev else -1 if c < old and c < prev else 0
    day = now // DAY * DAY
    previous = rows[(rows[:, 0] >= day - DAY) & (rows[:, 0] < day)]
    if len(previous) != 6 or len(set(previous[:, 0])) != 6:
        return 0
    high, low = float(np.max(previous[:, 3])), float(np.min(previous[:, 4]))
    if family == 1:
        return 1 if c > high else -1 if c < low else 0
    assert family == 2
    if low <= c <= high:
        return 1 if prev < low else -1 if prev > high else 0
    return 0

```

## Frontera de implementacion autorizable despues
Propuestas de nombre: BtcResearchR32DayAcceptanceBase1m, BtcResearchR32DayAccepted1m y BtcResearchR32DayCloseOnly1m. Aun NO creadas. BaseA hereda R32, sobreescribe solo _event/_invalid_event y constantes; wrappers flag/label. Helpersmodulares permitidos para validacionM1/consumodia, sin cuenta/ordenes. Gestion48h/TP2R comun y sourceparents intactos.

No reutilizar como control economico los resultados Angle/V1 por distinta receta/gestion/clock/contrato. Exactamente2motoresfuturos prefijados si rootaprueba fuentes/checks/manifiesto; no nuevo motor en esta entrega ni datacall avelas. Comprobar rawuniverse desde A_EVENT, no igualar signalsR32 que ya incorporan filtro. Nativeorders/funding/contabilidad solo se validaran despues en esos mismosmotores, no en preflighteconomico adicional.
