# R38 — CODES y manifiesto de fuente previo a check

Fuentes completas suministradas por MCP. Readback exacto antes del harness. No hay job, draft ni motor de R38. Primera versión preservada debajo: nunca ejecutada. Correcciones técnicas precheck: 27OHLC fijadas antes de crear fuentes; al revisar V1 root exigió terminación NATIVA sin liquidate de estrategia, evidencia estructural en EXIT_REQUEST y order_type en CLOSE. Sin cambios económicos, PnL ni precios observados.

- BtcResearchR10Base4h: 8100 caracteres; SHA256 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9.
- BtcResearchR11Base1m: 10150 caracteres; SHA256 be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87.
- BtcResearchR16LegacyBase1m: 14948 caracteres; SHA256 56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542.
- BtcResearchR38OrdinalBase1m: 10663 caracteres; SHA256 626310f698fb3e74c6f166173c9a6aa0c31dcdd48d1418cf915e26d16e3a4eb4.
- BtcResearchR38First1m: 179 caracteres; SHA256 7827e83d63ed68a5aa77e2c289c7aadc5364772c64433e1d32fd4d782319815b.
- BtcResearchR38Second1m: 181 caracteres; SHA256 bf946c5d91a01309776240538452ada27ee7a16cf54542e5f1c65ee1c8806595.

## Fuentes congeladas completas

### BtcResearchR10Base4h

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
### BtcResearchR11Base1m

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
### BtcResearchR16LegacyBase1m

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
### BtcResearchR38OrdinalBase1m

```python
import math

from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14
from strategies.BtcResearchR16LegacyBase1m import legacy_plan


def ordinal_structure(rows):
    """Prior26 excludes current extremes; flat valid ranges retain a midpoint."""
    prior = rows[-27:-1]
    upper, lower = max(float(x) for x in prior[:, 3]), min(float(x) for x in prior[:, 4])
    midpoint = upper/2.+lower/2.
    current = float(rows[-1, 2])
    if not all(math.isfinite(x) and x > 0 for x in (upper, lower, midpoint, current)):
        return None
    return dict(upper=upper, lower=lower, midpoint=midpoint, current=current)


class BtcResearchR38OrdinalBase1m(BtcResearchR11Base1m):
    """Ordinal of extreme closes, not independent attempts or failed-break learning."""
    LABEL = "abstract"
    ORDINAL = None

    def _counts(self):
        return self.vars.setdefault("r38_counts", dict(
            raw=0, raw_up=0, raw_down=0, events=0, plans=0, occupied=0,
            rejected_geometry=0, opens=0, closes=0, long_opens=0,
            short_opens=0, net=0.0, invalid_resets=0, midpoint_resets=0))

    def _machine(self):
        return self.vars.setdefault("r38_machine", dict(
            up=dict(seen=False, count=0), down=dict(seen=False, count=0)))

    def _invalidate(self, now, reason):
        for state in self._machine().values():
            state.update(seen=False, count=0)
        self.vars["r38_structure"] = None
        if not self.vars.get("r38_invalid", False):
            self._counts()["invalid_resets"] += 1
            self._log("R38_RESET", dict(label=self.LABEL, time=now,
                reason=reason, side="both", seen=False, count=0))
        self.vars["r38_invalid"] = True

    def _advance(self, structure, now):
        machine, counts = self._machine(), self._counts()
        current, midpoint = structure["current"], structure["midpoint"]
        # Reset BOTH sides at equality, before counting this close.
        for side, reset in (("up", current <= midpoint),
                            ("down", current >= midpoint)):
            state = machine[side]
            if reset:
                changed = not state["seen"] or state["count"] != 0
                state.update(seen=True, count=0)
                if changed:
                    counts["midpoint_resets"] += 1
                    self._log("R38_RESET", dict(label=self.LABEL, time=now,
                        reason="midpoint", side=side, seen=True, count=0,
                        **structure))
        side = ("up" if current > structure["upper"] else
                "down" if current < structure["lower"] else None)
        if side is None or not machine[side]["seen"]:
            return None
        state = machine[side]
        state["count"] += 1
        direction = 1 if side == "up" else -1
        counts["raw"] += 1
        counts["raw_up" if direction == 1 else "raw_down"] += 1
        selected = state["count"] == self.ORDINAL
        meta = dict(ordinal=state["count"], source_side=side,
                    signal_at=now, prior_end=now-BAR, **structure)
        self._log("R38_RAW", dict(label=self.LABEL, time=now,
            direction=direction, selected=selected, **meta))
        return dict(direction=direction, meta=meta) if selected else None

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.LABEL != "abstract" and self.ORDINAL in (1, 2)
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        if now <= self.vars.get("r38_pre_at", -1):
            return
        self.vars["r38_pre_at"] = now
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        self.vars["r38_structure_at"] = now
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 27)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self._invalidate(now, "invalid_window")
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price),
                            rel_tol=1e-10, abs_tol=1e-8), "R38_CURRENT_PRICE_PARITY"
        structure = ordinal_structure(rows)
        if structure is None:
            self._invalidate(now, "invalid_structure")
            return
        self.vars["r38_invalid"] = False
        self.vars["r38_structure"] = structure
        event = self._advance(structure, now)
        if event is None:
            return
        counts = self._counts()
        counts["events"] += 1
        self.vars["signals"] = self.vars.get("signals", 0)+1
        # Ordinal is consumed even when account eligibility rejects this event.
        if not self.START < now < self.FINISH:
            return
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            counts["occupied"] += 1
            return
        atr = atr14(rows)
        if atr is None:
            counts["rejected_geometry"] += 1
            return
        candidate = dict(origin=self.LABEL, direction=event["direction"],
            entry=float(self.price), distance=2*atr, target_distance=None,
            hold_hours=None, order_kind="MARKET")
        plan = legacy_plan(candidate, .5*max(0.0, float(self.balance)),
                           .5*float(self.available_margin),
                           float(self.leverage), float(self.fee_rate))
        if plan is None:
            counts["rejected_geometry"] += 1
            return
        plan.update(signal_at=now, meta=event["meta"])
        self.vars["plan"] = plan
        self.vars["direction"] = plan["direction"]
        counts["plans"] += 1
        self._log("R38_PLAN", dict(label=self.LABEL, time=now,
            direction=plan["direction"], entry=plan["entry"], qty=plan["qty"],
            distance=plan["distance"], risk_budget=plan["risk_budget"],
            planned_loss=plan["planned_loss"], meta=plan["meta"]))

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        assert direction == plan["direction"]
        assert math.isclose(entry, plan["entry"], rel_tol=1e-10, abs_tol=1e-8)
        distance = plan["distance"]
        stop = entry-direction*distance
        actual_loss = qty*(distance+self.fee_rate*(entry+stop)+.001*entry)
        assert stop > 0 and math.isfinite(actual_loss)
        assert actual_loss <= plan["risk_budget"]+1e-6
        self.stop_loss = qty, stop
        self.vars["r38_active"] = dict(plan, actual_entry=entry,
            opened_at=int(self.position.opened_at), stop=stop)
        self.vars.pop("r38_exit_reason", None)
        self.vars.pop("r38_exit_at", None)
        counts = self._counts()
        counts["opens"] += 1
        counts["long_opens" if direction == 1 else "short_opens"] += 1
        self.vars["entries"] = self.vars.get("entries", 0)+1
        self._log("R38_OPEN", dict(label=self.LABEL, time=int(self.time),
            signal_at=plan["signal_at"], opened_at=int(self.position.opened_at),
            direction=direction, entry=entry, qty=qty, distance=distance,
            risk_budget=plan["risk_budget"], actual_loss=actual_loss, stop=stop,
            target=None, target_distance=None, hold_hours=None,
            ordinal=plan["meta"]["ordinal"], origin=plan["origin"]))
        self._observe("open")

    def _request_exit(self, reason):
        now = int(self.time)
        if not self.is_open or self.vars.get("r38_exit_at") == now:
            return
        self.vars["r38_exit_at"] = now
        self.vars["r38_exit_reason"] = reason
        self._log("R38_EXIT_REQUEST", dict(label=self.LABEL, time=now, reason=reason,
            direction=1 if self.is_long else -1,
            opened_at=int(self.position.opened_at),
            **self.vars["r38_structure"]))
        self.liquidate()

    def update_position(self):
        if not self.is_open:
            return
        now = int(self.time)
        if now >= self.FINISH:
            # Leave liquidation to the native terminal path; do not counterfeit
            # its origin/counters with a strategy MARKET request.
            return
        if now % BAR or now <= int(self.position.opened_at):
            return
        structure = self.vars.get("r38_structure")
        if self.vars.get("r38_structure_at") != now or structure is None:
            return
        # ATR is exclusively an entry metric: valid structure is sufficient.
        reset = (structure["current"] <= structure["midpoint"] if self.is_long
                 else structure["current"] >= structure["midpoint"])
        if reset:
            self._request_exit("reset")

    def on_close_position(self, order, closed_trade):
        identity = str(closed_trade.id)
        seen = self.vars.setdefault("r38_closed_ids", set())
        if identity in seen:
            return
        seen.add(identity)
        pnl = float(closed_trade.pnl)
        assert math.isfinite(pnl)
        counts = self._counts()
        counts["closes"] += 1
        counts["net"] += pnl
        submitted_via = getattr(order, "submitted_via", None)
        # Audited native enum spelling; unknown closes remain visibly unclassified.
        reason = self.vars.get("r38_exit_reason") or (
            "stop" if submitted_via == "stop-loss" else "native_unclassified")
        self._log("R38_CLOSE", dict(label=self.LABEL, time=int(self.time),
            trade_id=identity, net=pnl, reason=reason, submitted_via=submitted_via,
            order_type=getattr(order, "type", None)))
        self.vars["direction"] = 0
        self.vars["r38_active"] = None
        # Source ledger includes this trade before R11 may emit FINAL.
        super().on_close_position(order, closed_trade)

    def before_terminate(self):
        if self.is_open:
            self.vars.setdefault("r38_exit_reason", "terminal")
        super().before_terminate()

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R38_SUMMARY", dict(stage=stage, label=self.LABEL,
            selected_ordinal=self.ORDINAL, hold_hours=None, tp_r=None, target=None,
            exit_mode="current channel midpoint reset",
            risk_total=.01, capital_denominator="total BTC wallet",
            redistribution=False, **self._counts()))

```
### BtcResearchR38First1m

```python
from strategies.BtcResearchR38OrdinalBase1m import BtcResearchR38OrdinalBase1m


class BtcResearchR38First1m(BtcResearchR38OrdinalBase1m):
    LABEL = "R38_FIRST"
    ORDINAL = 1

```
### BtcResearchR38Second1m

```python
from strategies.BtcResearchR38OrdinalBase1m import BtcResearchR38OrdinalBase1m


class BtcResearchR38Second1m(BtcResearchR38OrdinalBase1m):
    LABEL = "R38_SECOND"
    ORDINAL = 2

```

## Base V1 no ejecutada

SHA256 32b728c5228633a0115efbbad541c65cd71fd43b927c2dbab8993d84e4139f65

```python
import math

from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14
from strategies.BtcResearchR16LegacyBase1m import legacy_plan


def ordinal_structure(rows):
    """Prior26 excludes current extremes; flat valid ranges retain a midpoint."""
    prior = rows[-27:-1]
    upper, lower = max(float(x) for x in prior[:, 3]), min(float(x) for x in prior[:, 4])
    midpoint = upper/2.+lower/2.
    current = float(rows[-1, 2])
    if not all(math.isfinite(x) and x > 0 for x in (upper, lower, midpoint, current)):
        return None
    return dict(upper=upper, lower=lower, midpoint=midpoint, current=current)


class BtcResearchR38OrdinalBase1m(BtcResearchR11Base1m):
    """Ordinal of extreme closes, not independent attempts or failed-break learning."""
    LABEL = "abstract"
    ORDINAL = None

    def _counts(self):
        return self.vars.setdefault("r38_counts", dict(
            raw=0, raw_up=0, raw_down=0, events=0, plans=0, occupied=0,
            rejected_geometry=0, opens=0, closes=0, long_opens=0,
            short_opens=0, net=0.0, invalid_resets=0, midpoint_resets=0))

    def _machine(self):
        return self.vars.setdefault("r38_machine", dict(
            up=dict(seen=False, count=0), down=dict(seen=False, count=0)))

    def _invalidate(self, now, reason):
        for state in self._machine().values():
            state.update(seen=False, count=0)
        self.vars["r38_structure"] = None
        if not self.vars.get("r38_invalid", False):
            self._counts()["invalid_resets"] += 1
            self._log("R38_RESET", dict(label=self.LABEL, time=now,
                reason=reason, side="both", seen=False, count=0))
        self.vars["r38_invalid"] = True

    def _advance(self, structure, now):
        machine, counts = self._machine(), self._counts()
        current, midpoint = structure["current"], structure["midpoint"]
        # Reset BOTH sides at equality, before counting this close.
        for side, reset in (("up", current <= midpoint),
                            ("down", current >= midpoint)):
            state = machine[side]
            if reset:
                changed = not state["seen"] or state["count"] != 0
                state.update(seen=True, count=0)
                if changed:
                    counts["midpoint_resets"] += 1
                    self._log("R38_RESET", dict(label=self.LABEL, time=now,
                        reason="midpoint", side=side, seen=True, count=0,
                        **structure))
        side = ("up" if current > structure["upper"] else
                "down" if current < structure["lower"] else None)
        if side is None or not machine[side]["seen"]:
            return None
        state = machine[side]
        state["count"] += 1
        direction = 1 if side == "up" else -1
        counts["raw"] += 1
        counts["raw_up" if direction == 1 else "raw_down"] += 1
        selected = state["count"] == self.ORDINAL
        meta = dict(ordinal=state["count"], source_side=side,
                    signal_at=now, prior_end=now-BAR, **structure)
        self._log("R38_RAW", dict(label=self.LABEL, time=now,
            direction=direction, selected=selected, **meta))
        return dict(direction=direction, meta=meta) if selected else None

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.LABEL != "abstract" and self.ORDINAL in (1, 2)
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        if now <= self.vars.get("r38_pre_at", -1):
            return
        self.vars["r38_pre_at"] = now
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        self.vars["r38_structure_at"] = now
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 27)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self._invalidate(now, "invalid_window")
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price),
                            rel_tol=1e-10, abs_tol=1e-8), "R38_CURRENT_PRICE_PARITY"
        structure = ordinal_structure(rows)
        if structure is None:
            self._invalidate(now, "invalid_structure")
            return
        self.vars["r38_invalid"] = False
        self.vars["r38_structure"] = structure
        event = self._advance(structure, now)
        if event is None:
            return
        counts = self._counts()
        counts["events"] += 1
        self.vars["signals"] = self.vars.get("signals", 0)+1
        # Ordinal is consumed even when account eligibility rejects this event.
        if not self.START < now < self.FINISH:
            return
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            counts["occupied"] += 1
            return
        atr = atr14(rows)
        if atr is None:
            counts["rejected_geometry"] += 1
            return
        candidate = dict(origin=self.LABEL, direction=event["direction"],
            entry=float(self.price), distance=2*atr, target_distance=None,
            hold_hours=None, order_kind="MARKET")
        plan = legacy_plan(candidate, .5*max(0.0, float(self.balance)),
                           .5*float(self.available_margin),
                           float(self.leverage), float(self.fee_rate))
        if plan is None:
            counts["rejected_geometry"] += 1
            return
        plan.update(signal_at=now, meta=event["meta"])
        self.vars["plan"] = plan
        self.vars["direction"] = plan["direction"]
        counts["plans"] += 1
        self._log("R38_PLAN", dict(label=self.LABEL, time=now,
            direction=plan["direction"], entry=plan["entry"], qty=plan["qty"],
            distance=plan["distance"], risk_budget=plan["risk_budget"],
            planned_loss=plan["planned_loss"], meta=plan["meta"]))

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        assert direction == plan["direction"]
        assert math.isclose(entry, plan["entry"], rel_tol=1e-10, abs_tol=1e-8)
        distance = plan["distance"]
        stop = entry-direction*distance
        actual_loss = qty*(distance+self.fee_rate*(entry+stop)+.001*entry)
        assert stop > 0 and math.isfinite(actual_loss)
        assert actual_loss <= plan["risk_budget"]+1e-6
        self.stop_loss = qty, stop
        self.vars["r38_active"] = dict(plan, actual_entry=entry,
            opened_at=int(self.position.opened_at), stop=stop)
        self.vars.pop("r38_exit_reason", None)
        self.vars.pop("r38_exit_at", None)
        counts = self._counts()
        counts["opens"] += 1
        counts["long_opens" if direction == 1 else "short_opens"] += 1
        self.vars["entries"] = self.vars.get("entries", 0)+1
        self._log("R38_OPEN", dict(label=self.LABEL, time=int(self.time),
            signal_at=plan["signal_at"], opened_at=int(self.position.opened_at),
            direction=direction, entry=entry, qty=qty, distance=distance,
            risk_budget=plan["risk_budget"], actual_loss=actual_loss, stop=stop,
            target=None, target_distance=None, hold_hours=None,
            ordinal=plan["meta"]["ordinal"], origin=plan["origin"]))
        self._observe("open")

    def _request_exit(self, reason):
        now = int(self.time)
        if not self.is_open or self.vars.get("r38_exit_at") == now:
            return
        self.vars["r38_exit_at"] = now
        self.vars["r38_exit_reason"] = reason
        self._log("R38_EXIT_REQUEST", dict(label=self.LABEL, time=now, reason=reason))
        self.liquidate()

    def update_position(self):
        if not self.is_open:
            return
        now = int(self.time)
        if now >= self.FINISH:
            self._request_exit("terminal")
            return
        if now % BAR or now <= int(self.position.opened_at):
            return
        structure = self.vars.get("r38_structure")
        if self.vars.get("r38_structure_at") != now or structure is None:
            return
        # ATR is exclusively an entry metric: valid structure is sufficient.
        reset = (structure["current"] <= structure["midpoint"] if self.is_long
                 else structure["current"] >= structure["midpoint"])
        if reset:
            self._request_exit("reset")

    def on_close_position(self, order, closed_trade):
        identity = str(closed_trade.id)
        seen = self.vars.setdefault("r38_closed_ids", set())
        if identity in seen:
            return
        seen.add(identity)
        pnl = float(closed_trade.pnl)
        assert math.isfinite(pnl)
        counts = self._counts()
        counts["closes"] += 1
        counts["net"] += pnl
        submitted_via = getattr(order, "submitted_via", None)
        # Audited native enum spelling; unknown closes remain visibly unclassified.
        reason = self.vars.get("r38_exit_reason") or (
            "stop" if submitted_via == "stop-loss" else "native_unclassified")
        self._log("R38_CLOSE", dict(label=self.LABEL, time=int(self.time),
            trade_id=identity, net=pnl, reason=reason, submitted_via=submitted_via))
        self.vars["direction"] = 0
        self.vars["r38_active"] = None
        # Source ledger includes this trade before R11 may emit FINAL.
        super().on_close_position(order, closed_trade)

    def before_terminate(self):
        if self.is_open:
            self.vars.setdefault("r38_exit_reason", "terminal")
        super().before_terminate()

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R38_SUMMARY", dict(stage=stage, label=self.LABEL,
            selected_ordinal=self.ORDINAL, hold_hours=None, tp_r=None, target=None,
            exit_mode="current channel midpoint reset",
            risk_total=.01, capital_denominator="total BTC wallet",
            redistribution=False, **self._counts()))

```
