# Y — CODES y antecedentes documentales completos

Fecha2026-10-21. Snapshots leídos mediante MCP, preservados antes de nuevas clases o jobs. Estado: protocolo normativo aprobado por root para revisión documental, implementación NO autorizada todavía. No se consultaron resultados económicos W. Estos bloques Markdown son evidencia, no código para importar/ejecutar desde un análisis. Ninguna fuente padre fue modificada. Las limitaciones y el contrato están en BTC_DISCOVERY_Y_PROTOCOL_20261021.md; X HOLD sigue separado.

## Fuentes completas

### strategies/BtcResearchR10Base4h/__init__.py
SHA256 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9, 8100 caracteres.

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

### strategies/BtcResearchR11Base1m/__init__.py
SHA256 be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87, 10150 caracteres.

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

### strategies/BtcResearchR12ArBase1m/__init__.py
SHA256 1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343, 3347 caracteres.

```python
import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def return_forecast(rows, autoregressive):
    """240 observed (x,y) pairs, then six genuinely future recursive forecasts."""
    returns = np.diff(np.log(rows[-242:, 2]))
    x, y = returns[:-1], returns[1:]
    variance = float(np.mean((x-x.mean())**2))
    if not math.isfinite(variance) or variance <= 0:
        return None
    beta = float(np.mean((x-x.mean())*(y-y.mean()))/variance) if autoregressive else 0.
    intercept = float(y.mean()-beta*x.mean())
    value, forecast = float(returns[-1]), 0.
    for _ in range(6):
        value = intercept+beta*value
        forecast += value
    return forecast if math.isfinite(forecast) else None


class BtcResearchR12ArBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 242)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("AR1", "DRIFT")
        forecast = return_forecast(rows, self.MODE == "AR1")
        # Fixed signal hurdle inherited from R20, not simulated execution friction.
        if forecast is None or abs(forecast) <= .0019 or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        direction = 1 if forecast > 0 else -1
        atr = atr14(rows)
        if atr is None:
            return
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = direction

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        stop = entry-direction*plan["distance"]
        assert qty*(plan["distance"]+self.fee_rate*(entry+stop)) <= plan["risk_budget"]+1e-6
        self.stop_loss = qty, stop
        # Forecast horizon is24h; no fixed target clips the model's payoff.
        self.vars["entries"] = self.vars.get("entries", 0)+1
        self._observe("open")

    def update_position(self):
        if int(self.time) % BAR == 0 and int(self.time)-int(self.position.opened_at) >= 6*BAR:
            self.liquidate()

```

### strategies/BtcResearchR13GeometryBase1m/__init__.py
SHA256 3968e9a2733fbe9e4a22b32ba71d023defcefa79eae65e992833f1810fb82b97, 5882 caracteres.

```python
import math
import numpy as np

from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan

# Fixed before economic results: two natural half-range bins, sixty days of
# mature origins, one-day label and a shared minimum count for either policy.
LOOKBACK = 367
TRAINING_ORIGINS = 360
LABEL_BARS = 6
MIN_BIN_COUNT = 30
ADVANCE_BOUNDARY = 0.5
FORECAST_HURDLE = 0.0019  # Admission threshold; never additional modeled friction.


def geometry_forecast(rows, conditional):
    """Estimate only outcomes whose complete six-bar horizon is already observed."""
    if len(rows) < LOOKBACK:
        return None
    window = rows[-LOOKBACK:]
    close = window[:, 2]
    origins = window[1:TRAINING_ORIGINS+1]
    previous = close[:TRAINING_ORIGINS]
    step = close[1:TRAINING_ORIGINS+1]-previous
    true_range = np.maximum(
        origins[:, 3]-origins[:, 4],
        np.maximum(abs(origins[:, 3]-previous), abs(origins[:, 4]-previous)),
    )
    valid = (true_range > 0) & (step != 0)
    advance = np.divide(abs(step), true_range, out=np.zeros_like(step), where=true_range > 0)
    bins = advance >= ADVANCE_BOUNDARY
    # Origins1..360 label at7..366. Log differences avoid overflow of ratios.
    labels = np.sign(step)*(np.log(close[1+LABEL_BARS:])-np.log(close[1:TRAINING_ORIGINS+1]))
    valid &= np.isfinite(labels)

    current_step = float(close[-1]-close[-2])
    current_range = max(float(window[-1, 3]-window[-1, 4]),
                        abs(float(window[-1, 3]-close[-2])),
                        abs(float(window[-1, 4]-close[-2])))
    if current_range <= 0 or current_step == 0:
        return None
    current_advance = abs(current_step)/current_range
    current_bin = bool(current_advance >= ADVANCE_BOUNDARY)
    group = valid & (bins == current_bin)
    count_bin, count_all = int(group.sum()), int(valid.sum())
    # GLOBAL shares this gate, so the treatment cannot gain by a different
    # minimum-history calendar rather than by its conditional mean.
    if count_bin < MIN_BIN_COUNT:
        return None
    mean_conditional = float(np.mean(labels[group]))
    mean_global = float(np.mean(labels[valid]))
    mean = mean_conditional if conditional else mean_global
    if not math.isfinite(mean):
        return None
    response = 1 if mean > FORECAST_HURDLE else -1 if mean < -FORECAST_HURDLE else 0
    current_sign = 1 if current_step > 0 else -1
    return dict(direction=current_sign*response, response=response, mean=mean,
                mean_conditional=mean_conditional, mean_global=mean_global,
                current_bin=int(current_bin), current_advance=current_advance,
                count_bin=count_bin, count_all=count_all,
                first_origin_close=int(window[1, 0])+BAR,
                last_origin_close=int(window[TRAINING_ORIGINS, 0])+BAR,
                latest_label_close=int(window[-1, 0])+BAR)


class BtcResearchR13GeometryBase1m(BtcResearchR12ArBase1m):
    """Online two-mean estimator; frozen parent supplies no-TP/24h execution."""
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, LOOKBACK)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("COND", "GLOBAL")
        forecast = geometry_forecast(rows, self.MODE == "COND")
        self.vars["forecasts"] = self.vars.get("forecasts", 0)+1
        if forecast is None:
            self.vars["insufficient_forecasts"] = self.vars.get("insufficient_forecasts", 0)+1
            return
        assert forecast["latest_label_close"] == now
        if not forecast["direction"] or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(rows)
        if atr is None:
            return
        direction = forecast["direction"]
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            return
        self.vars["plan"] = plan
        self.vars["admitted_forecast"] = forecast
        self.vars["direction"] = direction
        self._log("R13_GEOMETRY_ADMISSION", dict(time=now, mode=self.MODE, **forecast))

    def on_open_position(self, order):
        super().on_open_position(order)
        # Count actual fills, not forecasts blocked by an existing position.
        forecast = self.vars["admitted_forecast"]
        key = "follow_fills" if forecast["response"] == 1 else "fade_fills"
        self.vars[key] = self.vars.get(key, 0)+1

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R13_GEOMETRY_STATS", dict(
            stage=stage, mode=self.MODE,
            forecasts=self.vars.get("forecasts", 0),
            insufficient_forecasts=self.vars.get("insufficient_forecasts", 0),
            follow_fills=self.vars.get("follow_fills", 0),
            fade_fills=self.vars.get("fade_fills", 0)))

```

### strategies/BtcResearchR11ClockBase1m/__init__.py
SHA256 26440c3d83c60fcc96bd7066740dffcd7024778814e1be2f224af71e2ef6cdf5, 4171 caracteres.

```python
import math

import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan

DAY = 86400000


def clock_signal(rows, state, volume_clock):
    """Whole4h bars form activity buckets; no split or invented intra-bar fill."""
    row = rows[-1]
    if not np.all(np.isfinite(rows[:, 5])) or np.any(rows[:, 5] < 0):
        return 0, {}
    previous = list(state.get("closed", []))
    active = dict(state["active"]) if state.get("active") else None
    if active is None:
        # Calendar comparator uses whole UTC days even after an invalid-data reset.
        if not volume_clock and int(row[0]) % DAY != 0:
            return 0, dict(active=None, closed=previous)
        threshold = 6 * float(np.mean(rows[-25:-1, 5]))
        if volume_clock and (not math.isfinite(threshold) or threshold <= 0):
            return 0, {}
        active = dict(volume=0.0, bars=0, high=float(row[3]), low=float(row[4]),
                      threshold=threshold, start=int(row[0]))
    active["volume"] += float(row[5])
    active["bars"] += 1
    active["high"] = max(active["high"], float(row[3]))
    active["low"] = min(active["low"], float(row[4]))
    completed = active["volume"] >= active["threshold"] if volume_clock else active["bars"] == 6
    if not completed:
        return 0, dict(active=active, closed=previous)
    direction = 0
    if len(previous) == 3:
        if row[2] > max(p["high"] for p in previous):
            direction = 1
        elif row[2] < min(p["low"] for p in previous):
            direction = -1
    # Consume the full overshoot and the event, including when a trade is occupied.
    previous.append(dict(high=active["high"], low=active["low"],
                         start=active["start"], finish=int(row[0]) + BAR))
    return direction, dict(active=None, closed=previous[-3:])


class BtcResearchR11ClockBase1m(BtcResearchR11Base1m):
    """Compare activity sampling against a fixed-calendar channel."""
    MODE = "abstract"

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
        count = 25
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        rows = closed_window(candles, now, count)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            self.vars["bucket_state"] = {}
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("VOLUME_CLOCK", "FIXED_CLOCK")
        direction, state = clock_signal(rows, self.vars.get("bucket_state", {}),
                                        self.MODE == "VOLUME_CLOCK")
        self.vars["bucket_state"] = state
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


```

### strategies/BtcResearchR12ParticipationBase1m/__init__.py
SHA256 3928d2b3fd4ba9ffab43b89e134e982fb65e941cccaba9ba38e3c845bf9acfba, 3057 caracteres.

```python
import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def participation_event(rows, require_phase):
    """Same-UTC baselines are strictly prior to S, even for B's time slot."""
    window = rows[-170:]
    volume = window[:, 5]
    if not np.all(np.isfinite(volume)) or np.any(volume <= 0):
        return None
    setup, confirmation = window[-2], window[-1]
    previous = float(window[-3, 2])
    atr = atr14(window[:-2])
    displacement = float(setup[2])-previous
    if atr is None or abs(displacement) < atr:
        return None
    fraction = (float(confirmation[2])-float(setup[2]))/(-displacement)
    if not .5 <= fraction < 1:
        return None
    # The170-row exact4h window makes these28 prior daily observations
    # of each distinct UTC slot. Neither event bar enters either baseline.
    setup_reference = volume[np.arange(0, 168, 6)]
    confirmation_reference = volume[np.arange(1, 169, 6)]
    setup_median = float(np.median(setup_reference))
    confirmation_median = float(np.median(confirmation_reference))
    if require_phase and not (setup[5] <= .5*setup_median and confirmation[5] >= confirmation_median):
        return None
    return dict(direction=-1 if displacement > 0 else 1, distance=2*atr)


class BtcResearchR12ParticipationBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 170)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("PHASE", "PRICE")
        event = participation_event(rows, self.MODE == "PHASE")
        if event is None or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        direction = event["direction"]
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, event["distance"])
        if plan is None or self.price+direction*2*plan["distance"] <= 0:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = direction

```

### strategies/BtcResearchR12JumpBase1m/__init__.py
SHA256 631377b49a213511ca5d08f63e50cf08aa38e18fcec303479b89e3a9fc0b81a6, 3384 caracteres.

```python
import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan

HOUR = 3600000


def closed_hours(candles, now):
    """Exact 25 closed hourly prices; no US-session filter on continuous BTC."""
    rows = candles[candles[:, 0]+HOUR <= now][-25:]
    if len(rows) != 25 or rows[-1, 0] != now-HOUR:
        return None
    if not np.all(np.diff(rows[:, 0]) == HOUR):
        return None
    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):
        return None
    if np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2])) or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2])):
        return None
    return rows


def jump_state(hourly, atr, price):
    """Finite-window RV/BV heuristic, never an asymptotic jump significance test."""
    increments = np.diff(np.log(hourly[:, 2]))
    rv = float(np.square(increments).sum())
    if not math.isfinite(rv) or rv <= 0 or atr is None:
        return 0
    bv = (math.pi/2)*(24/23)*float(np.abs(increments[1:]*increments[:-1]).sum())
    fraction = max(rv-bv, 0.)/rv
    total = float(increments.sum())
    if fraction < 1/3 or abs(total) < .5*atr/price:
        return 0
    return 1 if total > 0 else -1 if total < 0 else 0


class BtcResearchR12JumpBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 15)
        hourly = closed_hours(self.get_candles(self.exchange, self.symbol, "1h"), now)
        if rows is None or hourly is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self.vars["jump_state"] = 0
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert math.isclose(float(hourly[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        atr = atr14(rows)
        state = jump_state(hourly, atr, float(self.price))
        previous = self.vars.get("jump_state", 0)
        self.vars["jump_state"] = state
        if not state or state == previous or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        assert self.MODE in ("FADE", "FOLLOW")
        direction = -state if self.MODE == "FADE" else state
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None or self.price+direction*2*plan["distance"] <= 0:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = direction

```

### strategies/BtcResearchR16LegacyBase1m/__init__.py
SHA256 56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542, 14948 caracteres.

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

### strategies/BtcResearchR21ExternalClockBase1m/__init__.py
SHA256 caa81c408d261e5d802203d8fdf4b9926a616ae1def52e174c481450faa75ebc, 9945 caracteres.

```python
import math
import numpy as np
import jesse.indicators as ta

from strategies.BtcResearchR16LegacyBase1m import BtcResearchR16LegacyBase1m, legacy_history
from strategies.BtcResearchR10Base4h import BAR

MINUTE = 60000


def external_clock_context(btc_minutes, eth_minutes, now, btc_close):
    """Both past M1 windows/cutoffs share validity; ETH sets time only."""
    start = now - BAR
    windows = []
    for raw in (btc_minutes, eth_minutes):
        if raw.ndim != 2 or raw.shape[1] < 6:
            return None, "shape"
        # Runtime M1 timestamps are sorted (P framework audit). Binary bounds
        # avoid scanning/copying a growing multi-year history for each decision.
        times = raw[:, 0]
        left = int(np.searchsorted(times, start, side="left"))
        right = int(np.searchsorted(times, now, side="left"))
        rows = raw[left:right]
        if (len(rows) != 240
                or not np.array_equal(rows[:, 0], start + np.arange(240) * MINUTE)):
            return None, "clock"
        if (not np.all(np.isfinite(rows[:, :6]))
                or not np.all(rows[:, 1:5] > 0) or np.any(rows[:, 5] < 0)
                or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2]))
                or np.any(np.maximum(rows[:, 1], rows[:, 2]) > rows[:, 3])):
            return None, "ohlcv"
        windows.append(rows)
    btc, eth = windows
    if float(btc[-1, 2]) != float(btc_close):
        return None, "btc_close"
    cutoffs, fractions = [], []
    for rows in windows:
        # Preserve X805 raw arithmetic, including side='left' at exact half.
        # Normalization is conceptual; near-half floating sums need not scale
        # identically and are never repaired with an economic epsilon.
        volume = rows[:, 5]
        with np.errstate(over="ignore", invalid="ignore"):
            total = float(np.sum(volume))
            cumulative = np.cumsum(volume)
        if not math.isfinite(total) or total <= 0 or not np.all(np.isfinite(cumulative)):
            return None, "total"
        cutoff = int(np.searchsorted(cumulative, .5 * total, side="left"))
        if not 0 <= cutoff < 239:
            return None, "empty_partition"
        cutoffs.append(cutoff)
        fractions.append(float(cumulative[cutoff] / total))
    contexts = []
    for cutoff in cutoffs:
        first, second = btc[:cutoff+1], btc[cutoff+1:]
        # ETH second-group volume is allowed to be zero. Only BTC weights price.
        costs = []
        for group in (first, second):
            with np.errstate(over="ignore", invalid="ignore"):
                weight = float(np.sum(group[:, 5]))
                typical = np.mean(group[:, [3, 4, 2]], axis=1)
                products = typical * group[:, 5]
                weighted = float(np.sum(products))
            if (not math.isfinite(weight) or weight <= 0
                    or not np.all(np.isfinite(typical))
                    or not np.all(np.isfinite(products)) or not math.isfinite(weighted)):
                return None, "btc_weight_or_cost"
            cost = weighted / weight
            if not math.isfinite(cost) or cost <= 0:
                return None, "btc_cost"
            costs.append(cost)
        contexts.append(dict(cutoff=cutoff, time=int(btc[cutoff, 0]),
                             first_cost=costs[0], second_cost=costs[1],
                             first_low=float(np.min(first[:, 4]))))
    return dict(start=int(start), finish=int(now), btc=contexts[0], eth=contexts[1],
                btc_first_fraction=fractions[0], eth_first_fraction=fractions[1]), None


def clock_setups(c, context):
    """The ORIGINAL short-only X805 setup, differing only at chosen boundary."""
    w = c[-14:]
    if (context is None or len(w) != 14 or not np.all(np.isfinite(w))
            or not np.all(w[:, 1:] > 0) or not np.all(w[:, 3] >= w[:, 4])):
        return None
    s, t = c[-2], c[-1]
    base = bool(s[2] > c[-14, 2] and t[2] < t[1])
    values = {}
    for key in ("btc", "eth"):
        part = context[key]
        values[key] = bool(base and part["second_cost"] < part["first_cost"]
                           and t[2] < part["first_low"])
    return dict(base=base, **values)


def clock_supplement_event(c, context):
    """Called only AFTER selected full setup has consumed its false->true latch."""
    atr = float(ta.atr(c))  # Real legacy Wilder14/default with exposed history.
    if not math.isfinite(atr) or atr <= 0:
        return None
    s, t = c[-2], c[-1]
    distance = float(max(s[3], t[3]) + .25 * atr - t[2])
    if not atr <= distance <= 3 * atr:
        return None
    entry = float(t[2])
    # Exact physical TP guard, common to both clocks, AFTER latch consumption.
    if not (math.isfinite(distance) and 0 < distance < entry and entry - 2*distance > 0):
        return None
    return dict(origin="SUPPLEMENT", direction=-1, entry=entry, distance=distance,
                target_distance=2*distance, hold_hours=48, order_kind="MARKET",
                clock_evidence=context)


class BtcResearchR21ExternalClockBase1m(BtcResearchR16LegacyBase1m):
    MODE = "abstract"

    def _clock_count(self, label, value=1):
        if self.START < int(self.time) < self.FINISH:
            counts = self.vars.setdefault("clock_counts", {})
            counts[label] = counts.get(label, 0) + value

    def _clock_invalid(self, reason):
        self.vars["previous_setup"] = False
        self.vars["supplement_event"] = None
        self._clock_count("invalid:" + reason)

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("BTC_CLOCK", "ETH_CLOCK")
            self.vars["checked"] = True
            self._log("R21_CLOCK_CONFIG", dict(mode=self.MODE, fraction=.5,
                      minutes=240, original_setup="X805", branches=3,
                      risk=.02, aggregate=.06, leverage=3, fee=.00045,
                      reserve=.001, lot=.001))
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        self.vars["decision_at"] = now
        self.vars["supplement_event"] = None
        rows = legacy_history(self.get_candles(self.exchange, self.symbol, "4h"), now)
        self.vars["legacy_rows"] = rows
        if rows is None:
            self.vars["previous_setup"] = False
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self._clock_count("btc4h_invalid")
            return
        self.vars["history_min"] = min(self.vars.get("history_min", len(rows)), len(rows))
        self.vars["history_max"] = max(self.vars.get("history_max", len(rows)), len(rows))
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        self._clock_count("btc4h_valid")
        if self.is_open or self.entry_orders:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
        context, reason = external_clock_context(
            self.get_candles(self.exchange, self.symbol, "1m"),
            self.get_candles(self.exchange, "ETH-USDT", "1m"), now, float(rows[-1, 2]))
        if context is None:
            # Missing external data suppresses ONLY supplement, never original
            # core/runner candidates or their valid BTC history/trailing.
            self._clock_invalid(reason)
            return
        self._clock_count("input_valid")
        self._clock_count("same_cut", int(context["btc"]["cutoff"] == context["eth"]["cutoff"]))
        self._clock_count("cut_distance_sum", abs(context["btc"]["cutoff"]-context["eth"]["cutoff"]))
        self._clock_count("btc_cut_sum", context["btc"]["cutoff"])
        self._clock_count("eth_cut_sum", context["eth"]["cutoff"])
        self._clock_count("btc_first_fraction_sum", context["btc_first_fraction"])
        self._clock_count("eth_first_fraction_sum", context["eth_first_fraction"])
        setups = clock_setups(rows, context)
        if setups is None:
            self._clock_invalid("supplement4h")
            return
        self._clock_count("base", int(setups["base"]))
        self._clock_count("btc_setup", int(setups["btc"]))
        self._clock_count("eth_setup", int(setups["eth"]))
        self._clock_count("disagreement", int(setups["btc"] != setups["eth"]))
        if self.is_open or self.entry_orders:
            self._clock_count("occupied_disagreement", int(setups["btc"] != setups["eth"]))
        chosen = "eth" if self.MODE == "ETH_CLOCK" else "btc"
        setup = setups[chosen]
        previous = self.vars.get("previous_setup", False)
        # Update full setup BEFORE taATR, geometry, monetary and occupation gates.
        self.vars["previous_setup"] = setup
        if not setup or previous:
            return
        self._clock_count("selected_transition")
        evidence = dict(context, chosen=chosen, setup_btc=setups["btc"], setup_eth=setups["eth"])
        event = clock_supplement_event(rows, evidence)
        if event is None:
            self._clock_count("geometry_or_physical_rejection")
            return
        self.vars["supplement_event"] = event
        self.vars["supplement_events"] = self.vars.get("supplement_events", 0)+1
        self._clock_count("event")

    def on_open_position(self, order):
        super().on_open_position(order)
        plan = self.vars["position_plan"]
        if plan["origin"] == "SUPPLEMENT":
            self._log("R21_CLOCK_OPEN", dict(mode=self.MODE, time=int(self.time),
                      evidence=plan["clock_evidence"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R21_CLOCK_STATS", dict(stage=stage, mode=self.MODE,
                  counts=self.vars.get("clock_counts", {})))

```

### strategies/BTCExploreR804/__init__.py
SHA256 86bcb4297fed564346c949b7f02886a062134b20a75db32d35c657b6184c6692, 21328 caracteres.

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


class BTCExploreR804(Strategy):
    """Frozen R8 X804 alternative supplement; original branches retained.

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
        jh.debug('BTC_EXPLORE ' + json.dumps({'recipe': 'X804',
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
        entry, distance = float(self.price), float(event['distance'])
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
        setup = bool(self._research_setup(c))
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
        self.vars['explore_event'] = {'side': 'short', 'kind': 'X804',
            'distance': distance, 'target_distance': 2 * distance, 'hold_hours': 48}
        audit = self.vars.setdefault('explore_audit', {})
        audit['events'] = audit.get('events', 0) + 1
        audit['events_occupied'] = audit.get('events_occupied', 0) + int(self.is_open)

    @staticmethod
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

### strategies/BTCExploreR801/__init__.py
SHA256 3ce523dd958a8dbee3e1f96cca92b24a89d19b619343a67e1ab2b7a678a29861, 21318 caracteres.

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


class BTCExploreR801(Strategy):
    """Frozen R8 X801 alternative supplement; original branches retained.

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
        jh.debug('BTC_EXPLORE ' + json.dumps({'recipe': 'X801',
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
        entry, distance = float(self.price), float(event['distance'])
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
        setup = bool(self._research_setup(c))
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
        self.vars['explore_event'] = {'side': 'short', 'kind': 'X801',
            'distance': distance, 'target_distance': 2 * distance, 'hold_hours': 48}
        audit = self.vars.setdefault('explore_audit', {})
        audit['events'] = audit.get('events', 0) + 1
        audit['events_occupied'] = audit.get('events_occupied', 0) + int(self.is_open)

    @staticmethod
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

### strategies/AngleCombinedBtcVolume4h/__init__.py
SHA256 4672a72f60a506c7dec8fdb018849bca1072a6d2ea0289820b46c2cc804c116a, 16626 caracteres.

```python
import math
import json
from datetime import datetime, timezone
from jesse import helpers as jh
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

# User-approved research limits; risk is not an optimization parameter.
TRADE_RISK = 0.03
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.
SLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.


class AngleCombinedBtcVolume4h(Strategy):
    """Baseline combined strategy plus a BTC-only relative-volume participation gate.

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
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {
            'qty': qty, 'entry': entry, 'distance': distance,
            'risk': qty * unit_risk, 'notional': qty * entry,
        }
        return True

    def _volume_audit(self) -> dict:
        # Counts are flat decision bars, not hypothetical missed trades. Rejected
        # plans are deliberately not evaluated against a different future account.
        year = str(datetime.fromtimestamp(self.time / 1000, timezone.utc).year)
        return self.vars.setdefault('btc_volume_audit', {}).setdefault(year, {
            'decision_bars': 0, 'pass': 0, 'below_median': 0,
            'missing_dates': 0, 'invalid_volume': 0, 'stale_signal': 0,
            'long_admitted': 0, 'short_admitted': 0,
        })

    def _btc_volume_gate(self) -> bool:
        if self.symbol != 'BTC-USDT':
            return True
        audit = self._volume_audit()
        audit['decision_bars'] += 1
        c = self.signal_candles
        day = 86400000
        if not len(c) or int(c[-1, 0]) != int(self.closed_candle_open_time):
            audit['stale_signal'] += 1
            return False
        current = int(c[-1, 0])
        # Four complete weeks of the same UTC 4h block. Explicit timestamps
        # reject missing daily observations instead of quietly shifting the clock.
        required = current - day * np.arange(28, 0, -1, dtype=np.int64)
        timestamps = c[:, 0].astype(np.int64)
        indexes = np.searchsorted(timestamps, required)
        if (np.any(indexes >= len(c))
                or not np.array_equal(timestamps[indexes], required)):
            audit['missing_dates'] += 1
            return False
        if (np.any(required >= current)
                or np.any(required % day != current % day)):
            raise AssertionError('Volume history must be strictly past at the same UTC block')
        volumes = c[indexes, 5]
        current_volume = float(c[-1, 5])
        if (not math.isfinite(current_volume) or current_volume <= 0
                or not np.all(np.isfinite(volumes)) or np.any(volumes <= 0)):
            audit['invalid_volume'] += 1
            return False
        median = float(np.median(volumes))
        self.vars['btc_volume_latest'] = {
            'signal_open': current, 'oldest_reference': int(required[0]),
            'latest_reference': int(required[-1]), 'reference_count': 28,
            'current_volume': current_volume, 'reference_median': median,
        }
        passed = current_volume >= median
        audit['pass' if passed else 'below_median'] += 1
        return passed

    def _signal(self) -> int:
        # Gate the entire BTC decision before resolving the inherited long
        # priority. A rejected long must not fall through into a new short.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            if not self._btc_volume_gate():
                self.vars['signal_value'] = 0
            else:
                self.vars['signal_value'] = 1 if self._plan() else (-1 if self._short_plan() else 0)
                if self.symbol == 'BTC-USDT' and self.vars['signal_value']:
                    key = 'long_admitted' if self.vars['signal_value'] == 1 else 'short_admitted'
                    self._volume_audit()[key] += 1
        return self.vars['signal_value']

    def after(self) -> None:
        if self.symbol != 'BTC-USDT':
            return
        year = datetime.fromtimestamp(self.time / 1000, timezone.utc).year
        previous = self.vars.get('btc_volume_logged_year')
        if previous is not None and previous != year:
            # An annual summary keeps diagnostics bounded even in a six-year run.
            jh.debug('BTC_VOLUME_AUDIT_ANNUAL ' + json.dumps({
                str(previous): self.vars.get('btc_volume_audit', {}).get(str(previous), {})
            }, sort_keys=True))
        self.vars['btc_volume_logged_year'] = year

    def before_terminate(self) -> None:
        if self.symbol == 'BTC-USDT':
            # Final counts include the last year without anticipating any exit.
            jh.debug('BTC_VOLUME_AUDIT_FINAL ' + json.dumps(
                self.vars.get('btc_volume_audit', {}), sort_keys=True))

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

### strategies/AngleCombinedBtcAcceptance4h/__init__.py
SHA256 8e41a80a82180a8ad2193b6105bbd2173008e76e89ac4318e9cf774511148ae4, 16790 caracteres.

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

### strategies/ResearchV4Base1h/shock_features.py
SHA256 0ebf34769d0ad821e19773dfe5f6494398a0727ec5d1a93fc42c84472650a43b, 6809 caracteres.

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
SHA256 d6652607f3a667bcadaf10d2d64eed2af42864784f05c00123f1f429d5345bde, 9796 caracteres.

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

### strategies/ResearchV4Base1h/oscillator_features.py
SHA256 20aa757e423d6105c3276b92ad16ac154f51edae040243551de5662249521c72, 9567 caracteres.

```python
"""Finite RSI2 pullbacks; this module has no engine state or IO."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV4Base1h import BAR, closed_window

RSI_BARS = 32
TREND_BARS = 200
TREND_OFFSET = 24


def _digest(rows):
    return hashlib.sha256(json.dumps(rows[:, :5].tolist(),
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def rsi32(candles, now):
    """Each decision seeds its own 32 closes, never an unbounded persistent RSI."""
    rows = closed_window(candles, now, RSI_BARS)
    if rows is None:
        return dict(valid=False, value=None, reason="rsi_window_invalid")
    closes = [float(x) for x in rows[:, 2]]
    differences = [b - a for a, b in zip(closes, closes[1:])]
    if not all(math.isfinite(x) for x in differences):
        return dict(valid=False, value=None, reason="rsi_arithmetic_invalid")
    gains = [max(x, 0.) for x in differences]
    losses = [max(-x, 0.) for x in differences]
    # Period two: arithmetic seed over exactly two deltas, then 29 Wilder updates.
    # Half first avoids overflowing a finite seed when two large changes agree.
    gain = seed_gain = .5 * gains[0] + .5 * gains[1]
    loss = seed_loss = .5 * losses[0] + .5 * losses[1]
    for up, down in zip(gains[2:], losses[2:]):
        gain = .5 * gain + .5 * up
        loss = .5 * loss + .5 * down
    total = gain + loss
    if not all(math.isfinite(x) and x >= 0 for x in (gain, loss, total)):
        return dict(valid=False, value=None, reason="rsi_arithmetic_invalid")
    # A flat window is neutral; no epsilon alters threshold comparisons.
    value = 50. if total == 0 else 100. * (gain / total)
    return dict(valid=True, value=float(value), seed_gain=float(seed_gain),
        seed_loss=float(seed_loss), final_gain=float(gain), final_loss=float(loss),
        first=int(rows[0, 0]), last=int(rows[-1, 0]), bars=RSI_BARS,
        updates=29, sha256=_digest(rows))


def _cross_direction(current, previous, entry_level):
    """Strict prior/inclusive current inequalities encode a fresh extreme."""
    if previous > entry_level and current <= entry_level:
        return 1
    if previous < 100. - entry_level and current >= 100. - entry_level:
        return -1
    return 0


def features(candles, now, atr, entry_level=10.0):
    details = dict(reason="window_invalid")
    invalid = dict(valid=False, direction=0, reason="window_invalid", details=details)
    if not isinstance(entry_level, (int, float)) or not math.isfinite(entry_level) or not 0 < entry_level < 50:
        return dict(valid=False, direction=0, reason="entry_level_invalid",
                    details=dict(reason="entry_level_invalid"))
    rows = closed_window(candles, now, TREND_BARS + TREND_OFFSET)
    if rows is None:
        return invalid
    try:
        atr_valid = isinstance(atr, dict) and math.isfinite(atr["value"]) and atr["value"] > 0
    except (KeyError, TypeError, ValueError):
        atr_valid = False
    if not atr_valid:
        return dict(valid=False, direction=0, reason="atr_invalid",
                    details=dict(reason="atr_invalid"))
    current = rsi32(candles, now)
    # The previous RSI has its OWN seed/window, exactly as at the previous close.
    previous = rsi32(candles, now - BAR)
    if not current["valid"] or not previous["valid"]:
        return dict(valid=False, direction=0, reason="rsi_invalid",
                    details=dict(reason="rsi_invalid", current=current, previous=previous))
    close = float(rows[-1, 2])
    average = float(np.mean(rows[-TREND_BARS:, 2]))
    old_average = float(np.mean(rows[:TREND_BARS, 2]))
    if not all(math.isfinite(x) for x in (close, average, old_average)):
        return dict(valid=False, direction=0, reason="trend_arithmetic_invalid",
                    details=dict(reason="trend_arithmetic_invalid"))
    trend = 1 if close > average > old_average else -1 if close < average < old_average else 0
    crossing = _cross_direction(current["value"], previous["value"], float(entry_level))
    direction = crossing if crossing == trend else 0
    reason = "setup" if direction else "regime_reject" if crossing else "no_setup"
    details = dict(reason=reason, rsi_now=current, rsi_previous=previous,
        entry_level=float(entry_level), short_entry_level=float(100. - entry_level),
        close=close, sma200=average, sma200_24h_ago=old_average, trend=trend,
        crossing=crossing, first=int(rows[0, 0]), last=int(rows[-1, 0]),
        bars=TREND_BARS + TREND_OFFSET, sha256=_digest(rows))
    return dict(valid=True, direction=int(direction), reason=reason, details=details)


def self_checks():
    """Deterministic algebra, boundaries, prefixes and future mutation; no IO."""
    count = 0

    def check(value):
        nonlocal count
        assert bool(value)
        count += 1

    def candles(closes, first=0):
        closes = np.asarray(closes, dtype=float)
        return np.column_stack((np.arange(len(closes)) * BAR + first,
            closes, closes, closes + .05, closes - .05, np.ones(len(closes))))

    def oracle(values):
        # Closed-form weights are independent of the recurrence implementation.
        delta = [float(b - a) for a, b in zip(values, values[1:])]
        up = [max(x, 0.) for x in delta]
        down = [max(-x, 0.) for x in delta]
        def weighted(changes):
            seed = (changes[0] + changes[1]) / 2
            return seed * 2. ** -29 + math.fsum(changes[j] * 2. ** -(31 - j) for j in range(2, 31))
        gain, loss = weighted(up), weighted(down)
        return 50. if gain + loss == 0 else 100 * gain / (gain + loss)

    now = 224 * BAR
    base = candles(100. + np.arange(224) * .1)
    long = base.copy()
    long[-2, 1:5] = (121.6, 121.6, 121.65, 121.55)
    long[-1, 1:5] = (120.6, 120.6, 120.65, 120.55)
    # Reflection preserves a positive OHLC window and swaps highs/lows.
    short = long.copy()
    short[:, 1] = 400. - long[:, 1]
    short[:, 2] = 400. - long[:, 2]
    short[:, 3] = 400. - long[:, 4]
    short[:, 4] = 400. - long[:, 3]
    atr = dict(value=.2)
    for case, expected in ((long, 1), (short, -1)):
        result = features(case, now, atr)
        check(result["valid"])
        check(result["direction"] == expected)
        check(result["reason"] == "setup")
        check(len(json.dumps(result, allow_nan=False)) < 1700)
        for offset in (0, 1):
            r = rsi32(case, now - offset * BAR)
            values = case[-32-offset:len(case)-offset if offset else None, 2]
            check(abs(r["value"] - oracle(values)) < 1e-12)
            check(r["updates"] == 29)
            check(r["last"] + BAR == now - offset * BAR)
            # Older prefixes must not influence either finite RSI window.
            mutated = case.copy()
            mutated[:len(case)-32-offset, 1:5] *= 1.1
            check(rsi32(mutated, now - offset * BAR) == r)
        # Replaying the previous prefix gives its independently seeded prior RSI.
        check(rsi32(case[:-1], now - BAR) == rsi32(case, now - BAR))
        future = candles([99., 98.], first=now)
        appended = np.vstack((case, future))
        check(features(appended, now, atr) == result)
        appended[-2:, 1:5] *= 10.
        check(features(appended, now, atr) == result)
        prefix = candles(np.arange(40) + 60., first=-40 * BAR)
        extended = np.vstack((prefix, case))
        check(features(extended, now, atr) == result)
        extended[:40, 1:5] *= 2.
        check(features(extended, now, atr) == result)
        check(features(case[:-1], now, atr)["valid"] is False)
        check(features(case, now + BAR // 2, atr)["valid"] is False)
        for level in (9., 10., 11.):
            check(features(case, now, atr, level)["direction"] == expected)
    for values, expected in ((np.ones(32)*100, 50.), (np.arange(32)+100, 100.),
                             (200.-np.arange(32), 0.)):
        check(rsi32(candles(values), 32*BAR)["value"] == expected)
    alternating = 100. + np.cumsum(np.tile([1., -2.], 16))
    check(abs(rsi32(candles(alternating), 32*BAR)["value"] - oracle(alternating)) < 1e-12)
    for level in (9., 10., 11.):
        check(_cross_direction(level, level+1., level) == 1)
        check(_cross_direction(level, level, level) == 0)
        check(_cross_direction(100-level, 99-level, level) == -1)
        check(_cross_direction(100-level, 100-level, level) == 0)
        check(_cross_direction(level+1., level+2., level) == 0)
    flat = candles(np.ones(224)*100)
    check(features(flat, now, atr)["direction"] == 0)
    check(features(flat, now, atr)["valid"])
    check(features(long, now, None)["valid"] is False)
    for bad in (0., -1., float("nan"), float("inf")):
        check(features(long, now, dict(value=bad))["valid"] is False)
    for level in (0., 50., float("nan"), float("inf"), None):
        check(features(long, now, atr, level)["valid"] is False)
    for column, value in ((2, float("nan")), (3, 1.), (4, 1000.), (1, 0.)):
        broken = long.copy()
        broken[-1, column] = value
        check(features(broken, now, atr)["valid"] is False)
        check(rsi32(broken, now)["valid"] is False)
    broken = long.copy()
    broken[-10, 0] -= BAR
    check(features(broken, now, atr)["valid"] is False)
    check(rsi32(long[-31:], now)["valid"] is False)
    # Exit RSI remains usable without the 224 bars required for new exposure.
    check(rsi32(long[-32:], now)["valid"])
    check(features(long[-32:], now, atr)["valid"] is False)
    return dict(status="passed", assertions=count)

```

## Cierres y límites íntegros

### strategies/MultiAssetRetestBtcShort4h/reports/BTC_R1_RESULTS_20261019.md
SHA256 c2c00db9e4f0deb2a09a5439afebdd4eac5efea87b244b5a575b7000a739e9f2, 16617 caracteres.

```markdown
# BTC R1 — resultados auditados — 2026-10-19

Encontramos **un candidato de investigación: BtcExploreR103**, probado en B y C. Mejora beneficio y CAGR en la muestra reutilizada de desarrollo y conserva una ventaja neta bajo costes adicionales. Su regularidad mensual/trimestral **no resiste +5bps RT**, por lo que no se promueve ni se declara cumplido el objetivo de robustez. Las otras ocho hipótesis no ofrecen una mejora conjunta; algunas reducen DD a cambio de rendimiento o regularidad.

## Contrato y ejecución

Tres agentes nuevos: selecciónshort, gestiónshort y mecanismos alternativos. Tres hipótesis distintas por agente, evaluadas por separado, cada una en B y C: **18 full backtests finished sin errores**, en pares B/C simultáneos, máximo4global. Nueve reglas congeladas antes de implementar; raíz leyó fuentes antes de tickets. No grid, combinaciones, rescates de ceros, ni segunda ronda automática.

2020-10-15→2025-12-31 **exclusivo** (último día de datos2025-12-30); 2026 cerrado. 10000USDT compartidos, riesgo1%trade/8%agregado, isolated5x, capnocional4.4, fee.00045lado para todos los tipos, reserve.001 sólo sizing. 4h/240warmup, M1auxiliares BTC/PAXG/SPY, debugtrue/fastfalse. PAXG/SPY congelados y proxies aceptados. Sin funding ni datos nuevos. Comparación con controles **1%**, no cartera histórica3%.

Controles: [B](http://localhost:9200/#/backtest/29387384-c48c-4ac9-94bd-632a2ec3bb7f), SPYSecond; [C](http://localhost:9200/#/backtest/30ab3788-51bb-4435-8c21-9b12c45f8835), SPYMarket. PAXGMarket y BTCbase iguales. B/C comparten muestra y mecanismo BTC: no son dos validaciones independientes.

Root verificó18formularios y54snapshots de fuentes3rutas, todos exactos a versiones congeladas. Cuatro originales re-leídos intactos. Sólo un comentario heredado sobre persistencia de logs se corrigió después en las tres copias Entry; executable inalterado, snapshots conservados y reversión byte-exacta verificada. QA sintética229checks PASS, más auditorías de órdenes reales Payoff sin violaciones detectadas. Estas QA prueban implementación/cronología, no capacidad predictiva.

## Matriz completa

Neto y estrés expresados en USDT sobre cuenta inicial10k; M=meses positivos/meses activos, Q=trimestres positivos/todos. Completo=61meses calendario/19Q; conparciales=63meses/21Q. Los meses inactivos se muestran además abajo y en auditorías exactas. DDmotor negativo. +10 es coste adicional estático de10bps RT sobre mismos fills y cantidades, sin reejecución ni sizing adaptado.

| Hipótesis/cartera | N | Neto | Δnet vscontrol | CAGR | DDmotor | Mcompletos | Qcompletos | Mconparciales | Qconparciales | Neto+10bps |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [E01B](http://localhost:9200/#/backtest/9de1ae4d-ef15-4d8f-9022-20ee1a830ec6) | 202 | 8869.03 | -365.17 | 12.95% | -7.51% | 36/57 | 15/19 | 36/59 | 16/21 | 7411.31 |
| [E01C](http://localhost:9200/#/backtest/1a62497a-7609-4bfd-9153-15c8640cf67a) | 209 | 9028.42 | -379.41 | 13.13% | -8.17% | 37/57 | 16/19 | 37/59 | 17/21 | 7469.53 |
| [E02B](http://localhost:9200/#/backtest/97d654d0-5917-4a26-b151-11ef396591e6) | 143 | 7157.31 | -2076.89 | 10.91% | -9.47% | 30/54 | 14/19 | 30/56 | 15/21 | 6116.78 |
| [E02C](http://localhost:9200/#/backtest/a9b5fe7e-9fb3-47bc-9c1c-25155d7929c3) | 150 | 7323.18 | -2084.64 | 11.11% | -9.15% | 31/54 | 15/19 | 31/56 | 16/21 | 6187.91 |
| [E03B](http://localhost:9200/#/backtest/20ca6dae-a6c9-44ed-8349-5877e2d3827c) | 125 | 7628.67 | -1605.52 | 11.49% | -6.20% | 36/55 | 16/19 | 36/57 | 17/21 | 6566.63 |
| [E03C](http://localhost:9200/#/backtest/f551da25-c6c9-4a31-8ad9-7fc4f71ad823) | 132 | 7791.00 | -1616.83 | 11.68% | -6.92% | 34/55 | 16/19 | 34/57 | 17/21 | 6628.70 |
| [P01B](http://localhost:9200/#/backtest/17867dbb-3676-46e9-a427-d60694384528) | 208 | 9186.89 | -47.30 | 13.31% | -6.98% | 39/57 | 15/19 | 39/59 | 16/21 | 7653.86 |
| [P01C](http://localhost:9200/#/backtest/dc50d6e4-8799-437a-8d1e-8b81e22cf8ee) | 215 | 9342.08 | -65.75 | 13.49% | -7.01% | 39/57 | 14/19 | 39/59 | 15/21 | 7705.32 |
| [P02B](http://localhost:9200/#/backtest/85a2fe07-0f26-4271-88d0-4ebdcd8814f1) | 207 | 8658.49 | -575.71 | 12.71% | -7.87% | 37/57 | 15/19 | 37/59 | 16/21 | 7175.90 |
| [P02C](http://localhost:9200/#/backtest/b91112c0-e3f3-4c31-8dea-abf184cf2d40) | 214 | 8829.62 | -578.21 | 12.91% | -8.72% | 38/57 | 15/19 | 38/59 | 16/21 | 7247.12 |
| [P03B](http://localhost:9200/#/backtest/6eea0aa5-84fa-45b1-9e44-86d1e2c29a18) | 211 | 7599.73 | -1634.46 | 11.45% | -6.74% | 35/57 | 12/19 | 35/59 | 13/21 | 6122.93 |
| [P03C](http://localhost:9200/#/backtest/5652bfcb-64b2-4131-a757-3c5fcde4f886) | 218 | 7761.18 | -1646.64 | 11.65% | -6.74% | 35/57 | 14/19 | 35/59 | 15/21 | 6185.94 |
| [X01B](http://localhost:9200/#/backtest/77a80211-701a-4af4-9fb6-b77130b7b4c8) | 206 | 9234.19 | 0.00 | 13.37% | -7.50% | 37/57 | 16/19 | 37/59 | 17/21 | 7720.95 |
| [X01C](http://localhost:9200/#/backtest/9b5cbe51-91ee-4361-b080-c28c0cd38fdb) | 213 | 9407.83 | 0.00 | 13.56% | -8.17% | 38/57 | 16/19 | 38/59 | 17/21 | 7792.53 |
| [X02B](http://localhost:9200/#/backtest/56c48468-10dd-489e-b921-fa948dbd34ae) | 177 | 6279.08 | -2955.11 | 9.80% | -12.85% | 32/58 | 14/19 | 32/60 | 15/21 | 5176.79 |
| [X02C](http://localhost:9200/#/backtest/dd5b6e8d-6207-4e01-9bce-8a18c5d416e4) | 184 | 6418.73 | -2989.09 | 9.98% | -9.55% | 34/59 | 15/19 | 34/61 | 16/21 | 5222.25 |
| [X03B](http://localhost:9200/#/backtest/53937852-34a3-48c7-ab35-fac586341127) | 273 | 11964.24 | 2730.04 | 16.29% | -8.25% | 41/61 | 16/19 | 41/63 | 17/21 | 9878.12 |
| [X03C](http://localhost:9200/#/backtest/3935efb3-2b27-4ada-86ce-94123d7a6e2c) | 280 | 12135.88 | 2728.05 | 16.46% | -9.01% | 42/61 | 16/19 | 42/63 | 17/21 | 9942.01 |

### Lectura de las nueve hipótesis

- E01 Volumen direccional24h: pierde365–379USDT y regularidad. Shorts121; gate retiene120entradas de125, desplaza5 y habilita1distinta por ocupación. No mejora.
- E02 Caída distribuida sin vela dominante: shorts62, neto propio negativo y pérdida incluso antes de fees en ambas. La caída distribuida que selecciona no conserva el edge observado. No generalizar esta conclusión a todas las tendencias BTC.
- E03 Target sobre mínimo previo5d: reduceDD a6.20%/6.92%, pero pierde1606–1617USDT vscontrol; quedan44shorts con neto y bruto negativos. B pasa65% sólo con meses completos; conparciales36/57=63.16%; C falla ambas. No aceptación por redondeo.
- P01 Stopshort EMA20 descendente: DD6.98%/7.01% y39/57meses positivos; Q15/19B y14/19C, ambos bajo80%. Tradeoff útil para diagnóstico, sin promoción.
- P02 BEfee tras medio target: neto yDD peores.22latches/stopupdates, sólo4stopsBE modificados finalmente ejecutados por cartera. Shorts+10bps apenas104.90/87.41USDT.
- P03 Salida RSI3neutral: DDmenor pero shorts netos25.98/18.32, convertidos en −715.81/−724.74USDT con+10bps; regularidad peor.
- X01 Long tras shock/rechazo/recuperación: cero eventos elegibles completos contados, cero fills suplementarios; reproduce exactamente economía de controles. Los contadores no distinguen causas del cero. No relajar parámetros.
- X02 Sustituirshort por semivarianza persistente: sustituye los125shorts originales por96nuevos; neto−1319.89/−1324.64 y bruto negativo. Regla de varianza no aporta aquí.
- X03 Shortsuplementario desacuerdo precio/volumen+VWAP: candidato detallado a continuación.

## Candidato X03: qué hace

Mantiene runners long originales y prioridad de planes originales. Añade short tras dos barras cerradas:
1. En s=t−1, precio por encima del de12barras atrás, pero suma negativa de volumen ponderado por ubicación del cierre en el rango. q=V(2C−H−L)/(H−L), cero si rango0. Es proxy OHLCV, no flujo agresor observado.
2. Cierre_s>=VWAP12_s (HLC3); en t, vela bajista y cierre<VWAP12_s congelada al origen.
3. Primer false→true del setup completo, estado avanza aunque ocupado; MARKET al cierre, stop max(high_s,high_t)+.25ATR, distancia1..3ATR, TP2R, timeout48h. Sin trailing/BE ni cola retrospectiva.

No se eligieron12/2R/48h después del resultado. Fuente causal revisada y QA de estado antes de ejecución. Mantenerla congelada para validación posterior.

### Comparación nominal y denominadores

| Cartera | Neto | CAGR | PFtrades | Sharpe | DDmotor | Mfull activos | Mfull todos | Mparciales activos | Mparciales todos | Qfull | Qparciales |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bcontrol | 9234.19 | 13.37% | 1.796 | 1.324 | -7.50% | 37/57 (64.91%) | 37/61 | 37/59 (62.71%) | 37/63 | 16/19 | 17/21 |
| X03B | 11964.24 | 16.29% | 1.760 | 1.491 | -8.25% | 41/61 (67.21%) | 41/61 | 41/63 (65.08%) | 41/63 | 16/19 | 17/21 |
| Ccontrol | 9407.83 | 13.56% | 1.776 | 1.315 | -8.17% | 38/57 (66.67%) | 38/61 | 38/59 (64.41%) | 38/63 | 16/19 | 17/21 |
| X03C | 12135.88 | 16.46% | 1.745 | 1.480 | -9.01% | 42/61 (68.85%) | 42/61 | 42/63 (66.67%) | 42/63 | 16/19 | 17/21 |

Con fee base, X03 cumple65%meses activos y80%Q tanto completos como incluyendo parciales. B está sólo41/63=65.0794%, margen estrecho. El objetivo aspiracional70%meses y20–30%CAGR sigue sin alcanzarse. DD bajo25% en todos estos runs, pero X03 lo empeora frente a sus controles; no domina todas las dimensiones.

### Aporte, ocupación y concentración

- Cada X03 tiene79shorts suplementarios MARKET y113shorts originales STOP, total192shorts vs125control: **67más netos**, no79más netos. Se retienen112entradas shortbase, se desplazan13 y aparece1entrada original diferente. Los31long BTC conservan todos sus horarios de entrada y salida; las cantidades yPNL cambian con el capital.
- Neto suplemento:2107.76B/2087.17C, fees465.82/464.40. Con+10bps:1590.19/1571.17. Excluyendo3mejores suplementos:1069.65/1033.94; además+10bps:578.67/544.93. No depende sólo de sus3mejores trades.
- Aproximadamente80% del neto suplementario procede de2022+2025;2024 y el parcial2020 son negativos. Cuatro años completos positivos antes y después de+10bps, con2023 muy pequeño después de estrés. No presentar estabilidad uniforme ni años como OOS.
- Incremento neto de cartera2730.04B/2728.05C. Atribución cerrada BTC+2406.80/+2375.46, PAXG+187.56/+190.42, SPY+135.69/+162.17. La mejora de otras patas refleja sizing/capital endógenos; no es nueva señal en ellas.
- Tiempo con alguna posición:34.49→38.52%B y36.96→40.85%C. Notional×time/equityinicial:.3620→.4224B y.4118→.4763C. Más actividad/exposición bajo mismos límites; no afirmar igual camino económico o beneficio fijo por trade.
- Fees totales1361.92→1877.50B y1453.77→1974.48C; PF baja1.796→1.760B y1.776→1.745C aunque Sharpe sube. El mejor neto convive con costes yDD mayores.
- Excluir3mejores trades de cartera deja7640.01B/7807.60C; además+10bps deja5589.09/5649.10, vs3794.72/3859.92en controles. Eliminaciones mantienen resto de fills/cantidades; no son replay de capital.
- Peor Qnominal X03−3.9043%B/−4.7159%C, peores que controles−2.9682%/−3.8299%. DDdayclose−8.3135%/−9.0683% difiere del DDmotor−8.2540%/−9.0094%; no mezclarlos.
- Co-loss en61meses completos BTC/PAXG3, BTC/SPY0B/2C, PAXG/SPY0B/2C. Son descripciones de muestra reutilizada, sin inferir diversificación futura. Episodio DDdayclose2021-03-13→2021-06-17: BTC−770.17/PAXG−207.31/SPY0B; BTC−755.66/PAXG−204.50/SPY−95.96C.

## Validación adicional: regularidad bajo fricción

Se reconstruyó otra vez MTM por fill con+5/+10bps RT de coste proporcional adicional aplicado en sus timestamps, cantidades y precios congelados. No nuevos backtests ni modelo de ejecución, spread, gaps, latencia, funding o resizing. Las curvas no heredan el CAGRmotor nominal: CAGRoverlay se calcula de equity final estresada. B/Cbase yX03 se someten al mismo procedimiento.

| Cartera | Coste extraRT | Neto | Mfull | Qfull | Mparciales | Qparciales |
|---|---:|---:|---:|---:|---:|---:|
| B | 0bps | 9234.19 | 37/57 | 16/19 | 37/59 | 17/21 |
| B | 5bps | 8477.57 | 36/57 | 13/19 | 36/59 | 14/21 |
| B | 10bps | 7720.95 | 36/57 | 13/19 | 36/59 | 14/21 |
| C | 0bps | 9407.83 | 38/57 | 16/19 | 38/59 | 17/21 |
| C | 5bps | 8600.18 | 38/57 | 15/19 | 38/59 | 16/21 |
| C | 10bps | 7792.53 | 38/57 | 15/19 | 38/59 | 16/21 |
| X03B | 0bps | 11964.24 | 41/61 | 16/19 | 41/63 | 17/21 |
| X03B | 5bps | 10921.18 | 40/61 | 15/19 | 40/63 | 16/21 |
| X03B | 10bps | 9878.12 | 37/61 | 14/19 | 37/63 | 15/21 |
| X03C | 0bps | 12135.88 | 42/61 | 16/19 | 42/63 | 17/21 |
| X03C | 5bps | 11038.94 | 40/61 | 15/19 | 40/63 | 16/21 |
| X03C | 10bps | 9942.01 | 38/61 | 15/19 | 38/63 | 16/21 |

La ventaja de neto persiste:+10bps X03−control=+2157.17B/+2149.48C. **La regularidad objetivo no es robusta**: con+5bps, X03 queda40/63=63.49%meses y16/21=76.19%Q incluyendo parciales; incluso con periodos completos Q15/19=78.95%. Con+10bps X03C tiene38/61meses completos y38/63conparciales. Los controles también fallan parte de estos objetivos bajo coste extra. Beneficio resistente a un overlay de coste no equivale a regularidad resistente.

Meses pequeños que cambian signo están documentados en el informe de costes: X03C con+5bps noviembre2020 yseptiembre2025; con+10bps también marzo2023 yjulio2025. No modificar reglas para eliminar esos meses.

## Decisión y límite de evidencia

**Conservar X03B yX03C como candidatos congelados de desarrollo**, con B como variante de menorDD y C como variante de algo más beneficio/meses nominales. No elegir C sólo por máximo neto: ventajaC−B nominal171.64USDT y con+10bps63.89USDT, a cambio de másDD. Sin combinación conEMA20 ni otros filtros en esta ronda.

Las ocho alternativas se archivan o se conservan como tradeoffs diagnósticos descritos, no como promociones. No avanzar a despliegue ni declarar la cartera robustamente validada. Muestra2020–2025 intensamente reutilizada, selección entre9nuevas y muchas recetas anteriores, B/C no independientes,79suplementos, concentración temporal importante. Que sobreviva ex3 y coste adicional no corrige selección múltiple ni prueba edge fuera de muestra.2026 permanece cerrado.

Siguiente trabajo acotado sugerido: someter X03sin cambiar sus reglas a validación temporal y ejecución más realista, con criterios congelados; controlar estabilidad alrededor de ventanas/TP/timeout como sensibilidad, sin elegir el mejor vecino. Cualquier tramo reservado requiere acordar su apertura antes de consultarlo. Esta ronda finaliza sin nuevas pruebas económicas adaptativas.

## Evidencia persistida y reproducción

Todos los archivos siguientes están dentro del proyecto Jesse en la máquina que ejecuta Jesse, bajo strategies/MultiAssetRetestBtcShort4h/reports/:
- BTC_R1_FROZEN_PROTOCOL_20261019.md
- BTC_R1_ROOT_SOURCE_REVIEW_20261019.md
- BTC_R1_SESSION_REGISTRY_20261019.md (18dashboardlinks y checks)
- BTC_R1_AUDIT_BATCH1_20261019.md, BATCH2 yBATCH3 (fills/MTM/stress/rutas/co-loss/cohortes/path)
- BTC_R1_AUDITOR_SOURCE_20261019.md (código inline run_analysis)
- BTC_R1_COST_CALENDAR_20261019.md y BTC_R1_COST_CALENDAR_SOURCE_20261019.md
- PHASE2_HANDOFF_BTC_R1_20261019.md

Auditorías principales: ad66331f9c894766a156a4b6cd75d216, 831bac3de3cb4ff1953bd28756787b33, 46f434f9e40d46289f61102144344722; coste calendario:b103dc4be3a245e4a4c0f1b135b9a91b. QAExplore128checks job135ee4ae7efb43a6b12555be15de34b6; Payoff101checks1a560d1ce7e840f39c8fa5aa73fdef1b, P01órdenes6206e139bf2c40c9a706512b1773e76a, P02/P03órdenesf48bbd1e42684a9e8c00a2074f499bb9. Informes de cada agente bajo sus respectivas clases y referencias en registry. Las QA con stubs no recalculan indicadores históricos; snapshots de trades sólo contienen órdenes ejecutadas, no historial de modificaciones/cancelaciones. No se afirma revisión individual de379ratchets cancelados.

Contadores de capacidad: no se registran intentos con capacidad0, lotround0 o restricción de margen/riesgoagregado; sí recortes de tamaño por roomnocional/cuota de volatilidad. Se observan sólo planes que llegan a sizing, no señales mientras ocupado. events_occupied mide estado en before, no rechazos: el motor puede cerrar y reentrar con señal fresca en la misma barra. Cierres forzados al límite temporal conciliados porfills/fees/wallet; contador preterminaciónopen1 no es posición residual ni prueba de liquidez nativa al último precio.

## Revisión independiente final
El agente Entry leyó el informe completo sin nuevos datos, jobs ni backtests. Corrigió la expresión «hipótesis independientes» para evitar sugerir independencia estadística; se evalúan por separado, pero comparten muestra y base. No detectó errores materiales en denominadores, aritmética, conteos de desplazamiento o decisión. Root incorporó la corrección. Todos los18backtests y todos los análisis de esta ronda concluyeron; no queda proceso de investigación pendiente.

```

### strategies/MultiAssetRetestBtcShort4h/reports/N204_R4_FINAL_RESULTS_20261019.md
SHA256 b073ee832160a3f5c3d3379b9da24ec9a65e87dd1115a5f2fb90a8c333a88800, 12310 caracteres.

```markdown
# BTC N204 — resultados finales de la investigación R4

La ronda no encontró un reemplazo elegible para N204. Se completaron doce hipótesis, cuatro de entradas, cuatro de salidas y cuatro experimentales. Las doce reducen el neto nominal de la cartera frente a N204 tanto en B como en C. Se conserva N204 como referencia de investigación y no se promueve ninguna receta.

2026 permaneció cerrado, incluso a inspección. La ventana usada fue 2020-10-15 → 2025-12-31 exclusiva, con último día de precios 2025-12-30. Es una muestra de desarrollo intensamente reutilizada; esta búsqueda no es OOS ni demuestra ausencia de sobreajuste.

## Resultado económico

Referencias: [N204 B](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142) y [N204 C](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794). Neto nominal: **13.056,61 / 13.239,44 USDT**. Cuenta inicial compartida de 10.000 USDT. Los números siguientes son del conjunto BTC/PAXG/SPY, después de comisiones nominales, no un supuesto alfa aislado de BTC.

|Hipótesis|Neto B, USDT — sesión|Neto C, USDT — sesión|Diferencia frente a N204, B / C|
|---|---:|---:|---:|
|E401 — Descenso de dos días UTC completos|[12.978,15](http://localhost:9200/#/backtest/a7f6ad5a-2cad-472b-a64d-04891efe2bb9)|[13.170,12](http://localhost:9200/#/backtest/31212719-83db-441c-9ee3-47831a918911)|-78,47 / -69,32|
|E402 — Presión vendedora en ambas mitades del patrón|[9807,36](http://localhost:9200/#/backtest/3c3ce364-65cc-4884-aa65-2a352376f1db)|[10.034,74](http://localhost:9200/#/backtest/8af24c45-cc64-4849-979d-7f257b791495)|-3249,25 / -3204,70|
|E403 — Mínimo descendente dentro del patrón|[10.603,42](http://localhost:9200/#/backtest/60611316-45f2-41de-81ab-fea3da810395)|[10.801,21](http://localhost:9200/#/backtest/8f1f15a5-aa3a-482e-a17d-1b1866cb52fe)|-2453,19 / -2438,23|
|E404 — Dominio del volumen de las velas con presión negativa|[11.945,57](http://localhost:9200/#/backtest/41656a8c-f89d-4066-825e-18fbf0716652)|[12.129,88](http://localhost:9200/#/backtest/a89b7159-58e9-4b23-ac39-976d2dbb96b5)|-1111,04 / -1109,56|
|T401 — Salida ante tres mínimos crecientes y ruptura alcista|[12.132,73](http://localhost:9200/#/backtest/6380d800-6891-4e12-9594-0d426aca366b)|[12.323,27](http://localhost:9200/#/backtest/51d79034-9d7e-44e8-aed9-084f8ea95538)|-923,89 / -916,17|
|T402 — Salida sin progreso favorable en seis velas completas|[12.217,28](http://localhost:9200/#/backtest/53d8a9f6-0c62-4f67-b2ba-8e098a09856f)|[12.440,76](http://localhost:9200/#/backtest/acf3f8be-7d9d-4b33-82f2-03024940fabc)|-839,34 / -798,68|
|T403 — Salida al recuperar la entrada tras adversidad de 0,5R|[12.996,09](http://localhost:9200/#/backtest/9014f7d9-fa7e-4af7-94b7-dc98940f21b8)|[13.175,12](http://localhost:9200/#/backtest/bd5f78dd-b730-48ad-ab01-e4c3f4726d29)|-60,53 / -64,32|
|T404 — Mitad a 1R y remanente a 2R, con precisión corregida|[11.712,87](http://localhost:9200/#/backtest/58c9d1be-26e6-4da5-b601-3d84128b3333)|[11.877,89](http://localhost:9200/#/backtest/ef7502ca-94d8-40ae-91fa-90df6d396fc0)|-1343,74 / -1361,56|
|X401 — Máximo menor confirmado y ruptura de soporte|[7731,93](http://localhost:9200/#/backtest/97c7fc93-a002-445a-b18d-43d33a4d31e6)|[7922,55](http://localhost:9200/#/backtest/a2555538-0233-44d2-974c-9ab78aefe7af)|-5324,69 / -5316,90|
|X402 — Fallo de aceptación por encima de un rango|[9159,75](http://localhost:9200/#/backtest/225f6073-dcee-4a04-856b-b0d448f9dc74)|[9330,52](http://localhost:9200/#/backtest/277a6cf9-8801-4cb2-9306-f68f211089e2)|-3896,86 / -3908,92|
|X403 — Dos velas interiores y ruptura de la vela madre|[7786,57](http://localhost:9200/#/backtest/9e5f78d7-5f2f-4e2a-8a03-05226769cdb5)|[8007,00](http://localhost:9200/#/backtest/21deebfc-94b5-48e0-9660-18fe1e206de4)|-5270,04 / -5232,45|
|X404 — Invalidación inmediata de un intervalo alcista sin solapamiento|[7577,45](http://localhost:9200/#/backtest/5c1c5772-7b01-4970-aea5-1677abd79af6)|[7775,43](http://localhost:9200/#/backtest/b1cad85f-ba07-4931-a6e1-2d9703b53584)|-5479,16 / -5464,01|

El más cercano, T403, pierde 60,53 / 64,32 USDT. Tampoco mejora el neto bajo overlay de +10 bps RT. En B baja de 16/19 a 15/19 trimestres completos positivos bajo +5 bps, y de 17/21 a 16/21 incluyendo los parciales. No es una mejora de regularidad.

E401 reduce el drawdown nominal a −8,34% / −8,28% y mejora ligeramente el neto estático con +10 bps, pero pierde neto nominal y falla la regularidad trimestral. E404 mejora algunas proporciones mensuales: bajo +5 bps B tiene 42/59 meses activos completos y 42/61 activos incluidos; C, 41/59 y 41/61. Sin embargo pierde unos 1.110 USDT por cartera, y B falla la regularidad trimestral. Ninguna compensación se convierte retrospectivamente en un criterio nuevo.

Las cuatro sustituciones experimentales del suplemento también pierden neto. X401 sólo produjo nueve suplementos por cartera: su resultado desfavorable no permite concluir que la idea sea universalmente inválida. Ninguna rama se rescató con otros parámetros, filtros combinados ni nuevas variantes.

La [matriz completa](N204_R4_RESULTS_MATRIX_20261019.md) conserva neto, +10, drawdown, meses activos y de calendario, trimestres, puertas y diagnósticos de recorridos para las24 sesiones válidas.

## Contrato y decisión congelados

Se mantuvieron los 10.000 USDT compartidos, riesgo de 1% por operación y 8% agregado, isolated5x, cap4,4, reserva0,001 sólo para sizing y sin piramidación. BTC/PAXG/SPY4h con tres feeds1m, warmup240, debug=true, fast=false y chart=true. PAXG mantiene PortComparePaxgMarket4h con su BE dependiente de fee original. B usa SPY Second; C, SPY Market. N204 y las fuentes anteriores permanecen intactas. Las nuevas clases son autocontenidas.

Fee nominal0,00045 por lado, 9bpsRT. Los overlays añaden5/10bpsRT por cada fill real conservando precio, cantidad y momento: no son reruns ni slippage puro. Se auditaron órdenes ejecutadas, cantidades, fees, PNL, wallet y liquidación terminal; el MTM diario UTC valora cada remanente de los parciales. El drawdown del motor y el de cierres diarios se distinguen.

Para ser elegible se exigía, en ambas carteras: neto nominal mayor a N204; al overlay+5, al menos65% de meses activos y80% de trimestres positivos tanto completos como incluidos; neto+10 no inferior; y DDmotor no peor que−25%. Se comparó sin redondear. El ranking predefinido sólo aplica a elegibles: mínimo margen de regularidad, mínimo incremento neto+10, menor peorDD e ID.

La selección es vacía. Por ello no correspondían los dos reruns con fee0,00070 ni los cuatro vecinos de target0,9/1,1. No se ejecutaron y no se eligió un segundo candidato.

Mantener N204 tampoco resuelve el objetivo de costes reales: las referencias previas [B con fee0,00070](http://localhost:9200/#/backtest/9a6c7c24-8847-42d1-aadb-206f21723c1f) y [C con fee0,00070](http://localhost:9200/#/backtest/541d2bf4-ffca-4f2d-969b-c25165e7b960), auditadas en R3, tenían39/61 meses completos positivos y39/63 incluidos en ambas. Son63,93% /61,90%, inferiores al65%. Se citan como antecedentes, no como pruebas nuevas ni como equivalentes a un overlay.

## Qué aportó el diagnóstico de N204

El observador reprodujo exactamente las273/280 operaciones de las referencias, incluidos fills, cantidades, fechas, precios, fees y PNL: máximoΔPNL0. Se recuperaron79 trayectorias del suplemento en cada cartera y se unieron por entrada a los trades reales; se verificaron también cierre, precio y cantidad. No se detectaron huecos entre los minutos elegibles. Son79 eventos compartidos por B/C, no158 observaciones independientes.

Hay19 objetivos2R,21 stops1R y39 cierres48h. Son42 operaciones positivas netas y37 no positivas. La MFE mediana observada es0,777R, frente a1,519R entre ganadoras y0,316R entre no positivas. La MAE mediana es0,583R. Las excursiones son cotas inferiores: se excluyen minutos parciales de entrada/salida y se desconoce el orden intraminuto.

Los horizontes6/12/24h sólo tienen74/66/51 supervivientes observables;5/13/28 operaciones habían cerrado. Clasificar por resultado final y condicionar a supervivencia es retrospectivo, no una regla disponible en la entrada. Ningún umbral de T se escogió después de ver el diagnóstico.

En T404 corregida se verificaron79 suplementos y34 operaciones con parciales por cartera:19 recorridos TP1→TP2 y15 TP1→timeout;21 stops y24 timeouts sin parcial. En esta muestra no apareció TP1→SL. El reparto de beneficios recortó las operaciones que llegaban a2R sin rescatar aquellas que acababan en el stop. Es una descripción de estas ejecuciones, no una ley para otros mercados o periodos.

Las reglas originales conservaron su código y prioridad, pero su ejecución puede desplazarse por ocupación: X402 y X404 retienen30/31 entradas largas BTC de N204. El resultado completo de cartera incluye esos efectos y el capital compartido; no se atribuye toda diferencia al suplemento por separado.

## Reparaciones técnicas y conteo transparente

Se realizaron **30 backtests**:24 originales de variantes +2 reruns T404 por precisión +2 diagnósticos originales +2 reruns de diagnóstico por corte de logs. La matriz definitiva tiene24 resultados válidos:22 originales y2 T404 reparados. Los dos T404 raw se conservan apartados. No son treinta hipótesis.

La API cortaba las líneas largas del journal cerca de2000caracteres. Se cambió únicamente su formato a una fila compacta por línea, sin modificar observación ni reglas, y se repitió B/C. Paridad económica exacta y79 filas completas confirmadas.

En [T404 raw C](http://localhost:9200/#/backtest/1eb1db8f-a2cc-466e-aba4-4c3e111911b7) quedó un residuo7e−18 después del TP2. Su valor era despreciable, pero mantuvo ocupada la ruta hasta48h y bloqueó un short original. Que la contabilidad cuadrara no probaba que la estrategia hubiera quedado plana.

La única reparación fue el guard0<qty<0,001 dentro del callback del suplemento: registrar y liquidar residuos menores al lote, sin mover entradas, objetivos, stop o deadline. QA41PASS y dos revisiones de fuente; un fallo previo del fixture está documentado. En [T404 corregida C](http://localhost:9200/#/backtest/ef7502ca-94d8-40ae-91fa-90df6d396fc0), TP2 y el cierre del residuo ocurren realmente en1646405340000, y closed_at coincide. Reaparece el STOP original abierto1646410260000. B conserva exactamente el neto anterior; C sube de11.692,96 a11.877,89 por el recorrido corregido. Sigue perdiendo frente a N204.

No se modificó el framework, no hubo ejecución live/paper, instalaciones, funding ni nuevos datos.

## Cierre y continuación

Se cierra R4 sin reemplazo ni combinación de ganadores. El avance es una comparación reproducible de doce hipótesis, un diagnóstico de trayectorias y la detección de un defecto material de estado tras parciales. No es una mejora económica ni una nueva validación contra sobreajuste.

Antes de otra búsqueda sobre esta misma muestra, conviene formular una hipótesis distinta y un criterio falsable que atienda la regularidad bajo costes reales. Repetir filtros hasta conseguir un neto mayor aumentaría la presión de selección. N204 queda congelada y2026 sigue sin abrir. No se inició otra ronda.

## Evidencia y handoff

- [Protocolo anterior a resultados](N204_R4_FROZEN_PROTOCOL_20261019.md).
- [Matriz de24 resultados válidos](N204_R4_RESULTS_MATRIX_20261019.md).
- [Registro de30 sesiones, fuentes y QA](N204_R4_FINAL_SESSION_REGISTRY_20261019.md).
- [Código reproducible del auditor y ranking](N204_R4_AUDITOR_SOURCE_20261019.md).
- [Diagnóstico validado y límites](N204_R4_PATH_DIAGNOSTIC_INTERPRETATION_20261019.md).
- [Cuarentena T404 raw](N204_R4_T404_DUST_QUARANTINE_20261019.md).
- [QA real de reparación T404](N204_R4_T404_REPAIR_C_REAL_QA_20261019.md).
- [Familia de salidas](N204_R4_EXIT_FAMILY_FINAL_20261019.md).
- [Familia experimental](N204_R4_X_FINAL_QA_20261019.md).
- [Revisión independiente final de las24 filas](N204_R4_INDEPENDENT_FINAL_REVIEW_20261019.md).
- [Revisión independiente de fuentes y trayectorias](../../N204EntryR401/reports/N204_R4_INDEPENDENT_SOURCE_PATH_REVIEW_20261019.md).

Las auditorías por lote están en N204_R4_AUDIT_<lote>_20261019.md; T404_REPAIRED es autoritativo para la receta parcial, y T404 preserva el raw. Todos los backtests y trabajos de auditoría terminaron; no quedaron ejecuciones activas.

```

### strategies/MultiAssetRetestBtcShort4h/reports/N204_T403_R5_FINAL_RESULTS_20261019.md
SHA256 ed7c9bfa10a65eab0cfce04be4ebb7a34da5f5430da135423d3f16caa8f04af4, 13771 caracteres.

```markdown
# BTC N204 / T403 — resultados finales de la ronda R5

Completamos diez hipótesis con dos agentes nuevos: cinco desde la referencia N204 y cinco desde la candidata T403. Se ejecutaron veinte backtests nominales, de a dos por agente y con máximo cuatro simultáneos. Todos finalizaron sin errores del motor y pasaron la auditoría contable y de MTM.

**Hay dos mejoras nominales, N503 y C504, pero ninguna receta cumple todos los criterios en ambas carteras.** N204 sigue congelada como referencia de investigación. No se promociona una sustituta ni se abre2026.

N503 aporta el hallazgo más útil: mayor resultado de cartera al reducir ocupación del suplemento y permitir otras operaciones originales. La mejora no significa que el suplemento aislado se haya vuelto más rentable. Todo procede de una muestra de desarrollo muy reutilizada; no constituye validación fuera de muestra ni prueba contra sobreajuste.

## Resultados de las diez hipótesis

Referencias [N204 B](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142) y [N204 C](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794): neto13.056,61 /13.239,44 USDT. Semilla candidata [T403 B](http://localhost:9200/#/backtest/9014f7d9-fa7e-4af7-94b7-dc98940f21b8) y [T403 C](http://localhost:9200/#/backtest/bd5f78dd-b730-48ad-ab01-e4c3f4726d29):12.996,09 /13.175,12. T403 no estaba promovida.

Los netos siguientes corresponden a la cartera completa BTC/PAXG/SPY después del fee nominal. La mejora se exige frente a N204; batir sólo a T403 no basta.

|Receta|Neto B — sesión, USDT|Neto C — sesión, USDT|Δ frente a N204, B / C|Resultado|
|---|---:|---:|---:|---|
|N501 — Separación de precio entre cohortes de volumen|[9498,02](http://localhost:9200/#/backtest/16ce69b3-da09-4bc4-9eb4-be31b7e5d39d)|[9654,29](http://localhost:9200/#/backtest/febab2e7-f15f-4260-b9c0-8d92c669ac10)|-3558,59 / -3585,15|Neto inferior a N204|
|N502 — Contracción y expansión de true range|[10.708,85](http://localhost:9200/#/backtest/8e4fd64f-49c6-4049-b6da-abafede9cb8e)|[10.916,22](http://localhost:9200/#/backtest/d492f34b-8a1e-4099-8ec3-eae1b3b5d284)|-2347,77 / -2323,22|Neto inferior a N204|
|N503 — Avance ineficiente: ER ≤ 1/3|[13.328,71](http://localhost:9200/#/backtest/a0db99e9-2638-4a58-a407-11fa8442f752)|[13.536,90](http://localhost:9200/#/backtest/fd459b54-ea49-44ce-8dd1-290e2c2c4a65)|272,10 / 297,46|Mejora neto; falla M en C|
|N504 — Cuerpo envolvente bajista en 12h completas|[8759,05](http://localhost:9200/#/backtest/e3201a9a-3ac0-47f5-94f5-6f16feeee8ab)|[8925,80](http://localhost:9200/#/backtest/72d9e745-e4e1-4e09-99eb-e550f2560206)|-4297,56 / -4313,64|Neto inferior a N204|
|N505 — Ocho de doce cierres sobre A|[9785,31](http://localhost:9200/#/backtest/6a2cc667-11cf-4467-b1a4-0c8e84f2b792)|[9988,39](http://localhost:9200/#/backtest/8e693681-095b-4db9-affb-053f19085948)|-3271,30 / -3251,05|Neto inferior a N204|
|C501 — Dos cierres consecutivos de recuperación|[13.022,39](http://localhost:9200/#/backtest/e798f4aa-2793-4900-95b7-94b0b44d3fb0)|[13.209,73](http://localhost:9200/#/backtest/b8b318ea-c2ca-4269-b602-e1e3f97ab06c)|-34,22 / -29,71|Neto inferior a N204|
|C502 — Ruptura posterior del máximo de recuperación|[13.056,61](http://localhost:9200/#/backtest/4ac5e198-139d-4f17-8c8f-de1c8aa6a67f)|[13.239,44](http://localhost:9200/#/backtest/7e4411c6-6d8c-4bb8-9092-343f8089cc3d)|0,00 / 0,00|Identidad con N204|
|C503 — Salida sólo ante recuperación débil|[13.010,41](http://localhost:9200/#/backtest/57634d6a-96a9-480f-b4f4-2e5546c8693e)|[13.192,41](http://localhost:9200/#/backtest/cf4808de-d32d-46ec-98cf-2e453b486b85)|-46,21 / -47,03|Neto inferior a N204|
|C504 — Recuperación bajo A congelado|[13.083,10](http://localhost:9200/#/backtest/2ce5ecba-4ae6-4fd1-9917-4bf8117b09c8)|[13.267,12](http://localhost:9200/#/backtest/6c7b3c72-9096-4004-bac4-ef61c251c082)|26,48 / 27,67|Mejora neto; falla Q en B|
|C505 — Desactivar rescate tras progreso previo de 1R|[12.996,09](http://localhost:9200/#/backtest/8b0b2376-126b-4918-806e-d63aa0fec3f1)|[13.175,12](http://localhost:9200/#/backtest/ddac5c97-6655-417d-855a-fac467e06c6d)|-60,53 / -64,32|Identidad con T403|

|Receta|Operaciones de cartera B / C|Sharpe motor B / C|DD motor% B / C|Suplementos BTC por cartera|
|---|---:|---:|---:|---:|
|N501|239 / 246|1,32 / 1,31|-8,21 / -9,06|37|
|N502|238 / 245|1,43 / 1,42|-8,87 / -9,05|40|
|N503|264 / 271|1,61 / 1,60|-8,78 / -9,05|67|
|N504|214 / 221|1,27 / 1,26|-7,61 / -8,17|8|
|N505|221 / 228|1,36 / 1,35|-8,28 / -8,27|21|
|C501|273 / 280|1,58 / 1,57|-8,78 / -9,06|79|
|C502|273 / 280|1,58 / 1,57|-8,78 / -9,06|79|
|C503|273 / 280|1,58 / 1,57|-8,78 / -9,06|79|
|C504|274 / 281|1,59 / 1,57|-8,79 / -9,06|80|
|C505|274 / 281|1,58 / 1,56|-8,79 / -9,06|80|

N504 sólo produjo ocho suplementos por cartera. Su resultado desfavorable no invalida universalmente la lectura12h. C504, por su parte, sólo cambió cinco salidas frente a N204 y añadió una entrada; una ventaja de26–28USDT en ese conjunto es pequeña y sensible al contexto.

C502 no activó su nueva salida:15 activaciones adversas,3 recuperaciones y0 rupturas posteriores del máximo. Reprodujo exactamente las273/280 operaciones económicas de N204. C505 conserva exactamente las274/281 operaciones de T403. Ninguna identidad es evidencia independiente ni una mejora.

## N503: qué mejoró y qué no

Regla fijada antes de resultados: conservar el setup N204 y exigir0<ER≤1/3, donde ER es el avance neto de doce cierres dividido por la suma de sus doce cambios absolutos. No se probaron otros umbrales para rescatarla.

Neto nominal13.328,71 /13.536,90 USDT: incremento de272,10 /297,46. Bajo overlay estático de+10bpsRT, neto11.220,15 /11.314,25: incremento de288,94 /310,83 respecto a N204 con el mismo overlay. El drawdown nominal queda en−8,78% /−9,05%, muy parecido al de la referencia.

La regularidad de B cumple las puertas: con+5bpsRT tiene41/61 meses completos positivos y41/63 incluidos; trimestres17/19 y18/21. C tiene40/61 meses completos positivos, pero sólo40/63 incluidos: **63,49%, inferior al65%**. Sus trimestres17/19 y18/21 pasan. Por esa falta en C, N503 no es elegible para las seis verificaciones adicionales.

Enero2021 cambia de aproximadamente+61,95USDT a−9,16 bajo+5bps en ambas carteras. B rescata mayo2023 de−125,51 a+32,20; C no rescata otro mes. No se excluyó enero ni se cambiaron el65%, los denominadores o los periodos parciales.

La atribución importa:
- El suplemento MARKET pasa de79 a67 operaciones. Su neto BAJA de2856,51 a2599,41 en B y de2836,63 a2577,79 en C.
- Los cortos originales STOP pasan de113 a116. El neto de ese grupo sube433,80 /431,35 USDT, incluyendo diferencias de sizing en operaciones compartidas.
- Las tres entradas STOP añadidas se ejecutan en intervalos en que N204 estaba ocupada con otros MARKET BTC. Hay además un nuevo MARKET por el latch del setup modificado.
- PAXG y SPY también cambian cantidades y PNL por el capital compartido. No cambiaron sus reglas.
- Los31 largos BTC originales mantienen sus aperturas y cierres. No se infiere que sus cantidades o beneficios sean idénticos.

Esto sugiere investigar la convivencia temporal de señales, no afirmar una mejora aislada del alfa del suplemento. Las coincidencias de intervalos y las ejecuciones observadas no identifican por sí solas un contrafactual causal de cambiar una única operación.

Como diagnóstico estático, al retirar los tres mejores trades de cada cartera y añadir+10bpsRT quedan6708,03 /6796,75USDT. Ese cálculo no reejecuta el sizing ni valida otro periodo. El [informe de atribución](N204_T403_R5_N503_ATTRIBUTION_20261019.md) preserva grupos, recorridos y meses afectados.

## C504: segunda mejora, otra limitación

C504 conserva la entrada N204 y la activación adversa de T403. Congela el A original del evento y, en una vela4h completa estrictamente posterior a la adversidad, sale si el cierre cae bajo ese A. No es un breakeven ajustado por comisiones.

Obtiene+26,48 /+27,67USDT nominales y+26,01 /+27,03 bajo overlay+10 respecto a N204. Sin embargo, en B y con+5bps sólo tiene15/19 trimestres completos positivos y16/21 incluidos:78,95% y76,19%, inferiores al80%. C cumple la regularidad, pero el protocolo exige ambas carteras. Tampoco es elegible.

## Contrato, auditoría y selección

Ventana2020-10-15 →2025-12-31 exclusiva, último día de precios2025-12-30. **2026 cerrado incluso a inspección.** No se importaron nuevos datos, no se ejecutaron live/paper, no se cambió la configuración global ni el framework.

Cuenta compartida10.000USDT, riesgo1% por operación y8% agregado, isolated5x, sin piramidar, cap4,4 y reserva0,001 sólo para sizing. BTC/PAXG/SPY4h con tres feeds1m; warmup240, debug=true, fast=false, chart=true. PAXG mantiene su BE dependiente del fee original; SPY usa Second en B y Market en C. Se preservaron las fuentes originales y los métodos protegidos de riesgo, sizing, reservas y prioridad. Las diez variantes son clases propias.

Fee nominal0,00045 por lado. Los overlays añaden5/10bpsRT por cada fill conservando precio, cantidad y momento: no son reruns ni una simulación de slippage puro. Se conciliaron fills, cantidades, fees, PNL, wallet y liquidación terminal; MTM diario UTC con cuatro anclas congeladas. Se distinguieron61meses/19Q completos y63/21 incluidos, denominadores activos y de calendario, cohortes de trades y MTM. DD del motor y de cierre diario no se confunden.

Puertas congeladas, todas exigidas en B y C: incremento nominal frente a N204>1e−7USDT; con+5bps, meses positivos/activos≥65% y trimestres positivos≥80%, completos e incluidos; neto+10 no inferior a N204, tolerancia contable1e−7; DDmotor no peor que−25%. Los positivos mensuales/trimestrales se cuentan sin redondear. La tolerancia de neto se fijó antes de resultados para no vender ruido de floats como un avance.

Ranking predefinido sólo para elegibles: mayor mínimo margen de regularidad, mayor mínimoΔneto+10, menor peorDD e ID. **Elegibles vacíos, selección vacía.** No se hicieron los dos reruns con fee0,00070 ni los cuatro vecinos de target1,8R/2,2R. Tampoco se combinó N503 con C504 después de ver sus resultados.

## QA y revisión independiente

N204:250 comprobaciones de implementación aprobadas. Un fixture inicial calculaba incorrectamente una frontera de ER; se corrigió el fixture sin cambiar la fuente ni el umbral. T403:304 comprobaciones finales, incluyendo reinicio del contador C501 cuando falta adyacencia entre evaluaciones de4h; aclaración de “consecutivas” aplicada antes del primer backtest C501. Ninguna prueba de implementación se cuenta como observación de mercado.

Las20 formas y60 snapshots de fuentes fueron comprobados, y17 fuentes actuales relevantes y anteriores permanecen byteidénticas a sus versiones esperadas. La revisión cruzada de los agentes comprobó las reglas de la otra familia. Una revisión independiente adicional contrastó los20 resúmenes, el overlay+10 y los gates/márgenes de la matriz. Aplicó los conteos MTM auditados; no se presenta como una segunda reconstrucción independiente del MTM.

No hubo errores económicos que exigieran repeticiones. Fueron exactamente20 backtests nominales y10 hipótesis; no veinte hipótesis. Los diez trabajos de auditoría terminaron correctamente y no quedan ejecuciones activas.

## Conclusión y handoff

Esta ronda sí encuentra una mejora económica exploratoria, N503, pero no una sustituta que satisfaga el contrato completo. C504 también mejora marginalmente el neto y falla la regularidad en otra cartera. Se conserva N204 como referencia, N503 como línea de investigación y ambas fuentes nuevas sin promoción.

La siguiente investigación debería distinguir explícitamente el valor de la señal y el coste de ocupar la ruta BTC que necesitan los cortos originales. Cualquier hipótesis nueva o combinación requiere otro protocolo fijado antes de consultar resultados; aquí no se inició otra ronda. Las ventajas observadas siguen expuestas a selección múltiple sobre2020–2025 y no prueban ausencia de sobreajuste. La regularidad con costes reales continúa pendiente.

## Evidencia

- [Protocolo previo a resultados](N204_T403_R5_FROZEN_PROTOCOL_20261019.md).
- [Matriz completa, gates y recorridos](N204_T403_R5_RESULTS_MATRIX_20261019.md).
- [Registro de20 sesiones, QA y snapshots](N204_T403_R5_FINAL_SESSION_REGISTRY_20261019.md).
- [Auditor y selección reproducibles](N204_T403_R5_AUDITOR_SOURCE_20261019.md).
- [Atribución detallada de N503](N204_T403_R5_N503_ATTRIBUTION_20261019.md).
- [Revisión root de las fuentes](N204_T403_R5_ROOT_SOURCE_REVIEW_20261019.md).
- [Familia N204](../../N204ExploreR501/reports/N204_R5_FINAL_FAMILY_RESULTS_20261019.md).
- [Revisión independiente de las20 filas](../../N204ExploreR501/reports/N204_R5_INDEPENDENT_FINAL_MATRIX_REVIEW_20261019.md).
- [Revisión independiente de las cinco fuentes T403](../../N204ExploreR501/reports/N204_R5_INDEPENDENT_T403_SOURCE_REVIEW_20261019.md).
- [Familia T403: cinco variantes y diez backtests](../../T403ExploreR501/reports/N204_T403_R5_C_FAMILY_FINAL_20261019.md).
- [Revisión independiente de las cinco fuentes N204](../../T403ExploreR501/reports/N204_T403_R5_INDEPENDENT_N_SOURCE_REVIEW_20261019.md).

Las auditorías por lote están en N204_R5_AUDIT_N501..N505/C501..C505_20261019.md. Cada una conserva métricas nominales, costes estáticos, cohortes, concentraciones, meses, exposición y conciliación terminal.


Cierre operativo: ambos agentes completaron sus cinco variantes y sus informes, sin nuevas ejecuciones. Última comprobación root:20/20finished,10/10jobs de auditoría succeeded,0backtests/0análisisactivos,17fuentesbyteidénticas,selecciónvacía. Las métricas open_count previas a liquidación no se interpretan como posiciones residuales: los fills y la conciliación terminal son autoritativos.

```

### strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_FINAL_RESULTS_20261019.md
SHA256 07b1a7e356cf69975c881d5ea4b0826d6363d8ea7b7e128bf25c616a64ca78f5, 11109 caracteres.

```markdown
# BTC — cierre de la ronda R6

## Decisión

Se completaron 20 backtests nominales: diez hipótesis, cada una en las carteras B y C, con dos agentes nuevos y dos backtests simultáneos por agente. Ninguna supera todos los criterios congelados. N204 continúa como referencia; N503 y P604 son candidatos de investigación, sin promoción. No se activan las seis verificaciones condicionales: el protocolo las reservaba para una única receta elegible después de los veinte resultados. No se escoge otra regla ni se flexibilizan umbrales tras ver resultados.

N204: neto B 13056.61, C 13239.44 USDT.

N503: neto B 13328.71, C 13536.90 USDT.

La mayor mejora nominal de la ronda es P604. Frente a N204 suma 291.35 / 322.77 USDT; frente a N503 suma 19.25 / 25.31. En C, sus 40 meses positivos de 63 activos bajo +5 bps adicionales de coste por ida y vuelta son 63,49%, por debajo del 65% exigido. No alcanza la regularidad necesaria.

## Diseño y lectura de los resultados

B usa SPY Second: segunda oportunidad exacta del episodio y precio estructural original. C usa SPY Market: desde la segunda oportunidad y repricing a precio actual. Ambas usan el mismo BTC, PAXG y capital compartido; no son dos muestras independientes.

Todas las reglas parten de N503, con ER original fijado en 0<ER<=1/3. Cinco filtros nuevos o combinaciones explícitas de mecanismos ya probados; cinco reglas para estudiar la convivencia del suplemento MARKET con el corto STOP original. Fuentes, hipótesis, prioridad, fechas, puertas y ranking quedaron fijados antes de los resultados. No se modificó la operativa original, el dimensionamiento ni el contrato de cartera. La ocupación y el capital sí pueden cambiar las ejecuciones observadas.

|Hipótesis|Idea|Neto B|Neto C|Δ N204 B / C|+5 meses activos B / C, incluidos|Resultado|
|---|---|---:|---:|---:|---|---|
|E601|Volumen del gatillo superior a la mediana|[12139.28](http://localhost:9200/#/backtest/9a11306e-c60c-4453-800a-34cac602dbdc)|[12329.38](http://localhost:9200/#/backtest/b12c2e5d-2a3b-4036-be2a-3de93ee3b359)|-917.34 / -910.06|39/62 / 39/62|Falla nominal, calendar, plus10|
|E602|Mecha superior dominante en la vela previa|[12229.55](http://localhost:9200/#/backtest/19a83d39-c77e-41a4-a0b7-0edabd14b136)|[12426.75](http://localhost:9200/#/backtest/4da71fcf-5806-4aaa-9f52-5c7a62761040)|-827.06 / -812.69|41/61 / 42/61|Falla nominal, calendar, plus10|
|E603|Cuerpo compuesto de 8 horas bajista|[12378.55](http://localhost:9200/#/backtest/0fff0dca-c5c4-4745-a1f7-1926300d7867)|[12551.14](http://localhost:9200/#/backtest/aabc659d-e33f-472b-942a-e9b2adcc0abe)|-678.06 / -688.30|41/63 / 40/63|Falla nominal, calendar, plus10|
|E604|Espacio hasta soporte para el objetivo de 2R|[9055.47](http://localhost:9200/#/backtest/3a0b72cf-183b-4920-a863-845b77a9443e)|[9206.39](http://localhost:9200/#/backtest/a20faa2e-315a-4319-8138-44a12b84d49b)|-4001.15 / -4033.05|36/59 / 38/59|Falla nominal, calendar, plus10|
|E605|Cierre de última hora rompe mínimos de las primeras tres|[11674.38](http://localhost:9200/#/backtest/fbae9638-daef-4a34-ba29-5fdfd1c796e6)|[11883.70](http://localhost:9200/#/backtest/adfde635-9272-4a1c-ad63-347d7a0cd826)|-1382.24 / -1355.74|41/61 / 42/61|Falla nominal, calendar, plus10|
|P601|Reservar espacio si existe contexto técnico original|[13123.60](http://localhost:9200/#/backtest/7fc34b8d-bbc4-48c0-9dd9-ef1751ed3bf5)|[13307.81](http://localhost:9200/#/backtest/4c23dbbc-ea56-4709-9835-e2e2b332214f)|66.99 / 68.37|40/63 / 39/63|Falla calendar|
|P602|Vetar si hubo preparación técnica en tres prefijos previos|[13328.71](http://localhost:9200/#/backtest/35c8f77f-e7fa-4c12-b9cc-8a6141192096)|[13536.90](http://localhost:9200/#/backtest/7df75aa0-a2c1-456e-b196-d96a9d00c3c7)|272.10 / 297.46|41/63 / 40/63|Falla calendar|
|P603|Liberar al aparecer preparación técnica original|[12143.86](http://localhost:9200/#/backtest/b667d009-bcec-425f-8120-ac7fd24ea523)|[12310.79](http://localhost:9200/#/backtest/60c0e24b-cd8e-42e0-be3c-b915104fab92)|-912.76 / -928.65|43/63 / 41/63|Falla nominal, plus10|
|P604|Liberar tras confirmación del precio en la vela siguiente|[13347.96](http://localhost:9200/#/backtest/bf8cf6df-8055-4e88-a52d-5cb3d12d8b52)|[13562.22](http://localhost:9200/#/backtest/e312a439-4afb-4be4-af3b-4d08325d47bb)|291.35 / 322.77|41/63 / 40/63|Falla calendar|
|P605|Liberar estancamiento desde seis velas con contexto original|[13328.71](http://localhost:9200/#/backtest/49c13ad1-4802-4c9f-99f8-fffec43fdac9)|[13536.90](http://localhost:9200/#/backtest/12d3aae7-b298-4afc-aa6a-e46f6fc24a2f)|272.10 / 297.46|41/63 / 40/63|Falla calendar|

`nominal`: superar N204 en neto por más de 1e-7 USDT en ambas carteras; `calendar`: bajo +5 bps adicionales, meses positivos/activos>=65% y trimestres positivos>=80%, tanto periodos completos como incluidos; `plus10`: neto con +10 bps no inferior a N204 con el mismo recargo, tolerancia 1e-7; `dd`: drawdown del motor no peor que -25%. Positivos estrictamente >0, sin redondeo. Matriz completa: `strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_RESULTS_MATRIX_20261019.md`.

## Qué se aprendió

P602 y P605 son económicamente idénticas a N503 en las dos carteras: mismos tiempos, tipos de entrada, precios, cantidades, comisiones y PNL, con tolerancia 1e-7; cero diferencia máxima. El veto de P602 y la salida de P605 nunca se activaron. Repetir esa trayectoria no añade evidencia independiente.

P603 efectuó 13 liberaciones y el conteo agregado de STOP subió de 116 a 125 por cartera; ambas cohortes de cortos ganaron menos. Cumple la regularidad +5 de ambas carteras, a costa de perder aproximadamente 913 / 929 USDT frente a N204. No se puede identificar cada liberación con una entrada adicional ni interpretar preparación técnica como orden realmente ejecutable.

P604 hizo cuatro liberaciones; el conteo STOP subió de 116 a 118. El suplemento siguió en 67 operaciones, su neto mejoró, mientras el neto de los STOP bajó ligeramente frente a N503. La cartera mejora poco y sigue fallando el criterio mensual de C. El shadow STOP sólo fija una condición de salida al cierre de la vela siguiente; no se contabiliza como ejecución hipotética de un STOP.

E602 reduce drawdown, pero pierde rentabilidad; E604 descarta demasiadas oportunidades y se aleja notablemente de la referencia. E605 tuvo 115 evaluaciones M1 válidas: 46 pasaron y 69 no; cero faltantes de reloj, datos corruptos o diferencias entre el cierre M1 y el 4h. Generó29 operaciones por cartera. Su caída de rentabilidad no se explica por falta de cobertura en esas evaluaciones. E604 produjo sólo una operación del suplemento; E602 produjo24. Estos recuentos pequeños limitan cualquier conclusión universal sobre sus mecanismos. El informe de la familia exploratoria conserva los contadores. No se mezclaron a posteriori filtros y salidas ganadores ni se ajustaron fechas problemáticas.

## Alcance, costes y verificación

Ventana 2020-10-15 hasta 2025-12-31 exclusiva. 2026 permaneció cerrado incluso a inspección. Es una muestra de desarrollo reutilizada en numerosas rondas; no constituye OOS, prueba contra sobreajuste ni validación para operar. La multiplicidad de búsqueda acumulada sigue pendiente.

Contrato: 10000 USDT compartidos; 1% por operación / 8% agregado; isolated 5x; sin piramidación; cap nocional 4.4; reserva .001 sólo para sizing; fee nominal .00045 por lado. PAXG mantiene su break-even dependiente del fee. Tres rutas 4h y tres feeds 1m; warmup240, debug true, fast false, chart true. No se implementó funding.

Los recargos +5/+10 bps por ida y vuelta se aplican a fills, cantidades, precios y tiempos fijos. No simulan cambios de sizing, prioridad ni break-even dependiente del fee; no son una corrida con mayor fee real. Al no haber candidata elegible no se ejecutaron las dos corridas engine .00070 por lado ni las cuatro sensibilidades TP1.8R/2.2R previstas condicionalmente.

Auditoría de los veinte: fills, cantidades, comisiones, PNL, wallet, liquidación terminal y MTM diario UTC reconciliados, cuatro anclas históricas congeladas. Se distinguen drawdown del motor, drawdown diario y cohortes de trades. Los contadores de posiciones abiertas previos a liquidación final no se interpretan como posiciones restantes después del cierre; el auditor reconcilia la frontera. Conteos full: 61 meses /19 trimestres; incluidos63/21; meses activos variables y calendario completo se muestran por separado.

QA de código: 196 comprobaciones finales exploratorias y311 de convivencia; revisión cruzada independiente de las dos familias; lectura final exacta de17 fuentes;20 formularios y60 snapshots coinciden. Se preservan las31 entradas largas de BTC y sus tiempos de salida en cada corrida; pueden variar cantidades por capital. Verificaciones y fuentes de auditor/ranking están archivadas en reportes R6. No hubo operaciones live/paper ni cambios de configuración global.

## Continuación recomendada

Conservar N204 como referencia y P604 como pequeño avance nominal pendiente. Antes de sumar otra batería, estudiar si la mejora de P604 depende de muy pocas operaciones y cuantificar la selección acumulada. Una siguiente investigación debe fijar de antemano una hipótesis económica de convivencia, con pocos grados de libertad y criterios de estabilidad bajo costes; conservar 2026 cerrado hasta decidir por escrito el protocolo final de evaluación. No buscar una regla para rescatar un mes o una fecha concretos.

## Trazabilidad

Protocolo: `strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_FROZEN_PROTOCOL_20261019.md`.

Auditor/ranking: `strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_AUDITOR_SOURCE_20261019.md`.

Revisión root: `strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_ROOT_SOURCE_REVIEW_20261019.md`.

Revisiones cruzadas: `strategies/N503ExploreR601/reports/N503_R6_INDEPENDENT_CAPACITY_SOURCE_REVIEW_20261019.md` y `strategies/N503CapacityR601/reports/N503_R6_INDEPENDENT_EXPLORE_SOURCE_REVIEW_20261019.md`.

Auditorías financieras por pareja: `strategies/MultiAssetRetestBtcShort4h/reports/N204_R6_AUDIT_<E601..E605 o P601..P605>_20261019.md`.

El registro adjunto conserva URLs, IDs, estado, fee y fuente; el manifiesto de cierre conserva formularios, snapshots, jobs y paridades económicas.

## Revisión independiente de cierre

El agente de convivencia recalculó las puertas y ranking de la matriz final: 351 comprobaciones aprobadas. Contrastó los20 resúmenes MCP de sesiones finalizadas sin error, neto, DD y número de operaciones, con concordancia menor de1e-7. Selección vacía confirmada; P604 falla C40/63 y P603 falla nominal/+10. Esta revisión verifica el ranking y su trazabilidad; no es una segunda reconstrucción independiente del MTM.

Revisión: `strategies/N503CapacityR601/reports/N503_R6_INDEPENDENT_FINAL_MATRIX_REVIEW_20261019.md`.

Informes familiares: `strategies/N503CapacityR601/reports/N503_R6_CAPACITY_FINAL_FAMILY_RESULTS_20261019.md` y `strategies/N503ExploreR601/reports/N503_R6_E_FINAL_FAMILY_RESULTS_20261019.md`.

Manifiesto y registro completo: `strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_FINAL_REGISTRY_AND_MANIFEST_20261019.md`.

```

### strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_FINAL_RESEARCH_RESULTS_20261019.md
SHA256 4066e53cf744efc6166d59abdae26ebaf6dc7842f8c6d81b45a6e75e7b691f7f, 10807 caracteres.

```markdown
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

### strategies/MultiAssetRetestBtcShort4h/reports/ORCHESTRATION_ROUND3_REJECTIONS_20261018.md
SHA256 b6a64c2e5a421118476df3fbad44a531fa7b26dfb5e5ccf7d158e8c523deee91, 2957 caracteres.

```markdown
# Tercera ronda: dos rechazos económicos y controles de regularidad
Fecha2026-10-18. Fuente y umbrales congelados antes de cada prueba. Desarrollo común2020-10-15 a2025-12-31 exclusivo.2026 no evaluado.

| Caso | Trades | Neto USDT | CAGR | DD motor | Meses activos positivos | Todos los meses positivos | Trimestres positivos |
|---|---:|---:|---:|---:|---:|---:|---:|
|[BTC reversión rápida](http://localhost:9200/#/backtest/df044178-559e-4d34-848f-820825479701)|258long|−72.23|−0.139%|−5.213%|31/53|31/63|11/21|
|[BTC ruptura tras baja volatilidad](http://localhost:9200/#/backtest/c4514079-275c-4586-b773-ea464d5cf1bf)|123short|−239.93|−0.465%|−26.660%|19/53|19/63|8/21|

Ambos rechazados. No reajustar RSI, ventanas o ratio después de ver el fallo.
FastMR:67.83% acierto y payout0.466; beneficio antes de fees519.98 frente592.20fees. Acierto alto no demuestra esperanza neta positiva. +10bps RT sobre los mismos fills implica−730.23, sin atribuirle nuevoCAGR/DD ni llamarlo backtest.
QuietChannel:buffer>=722bars validado en cada callback conwarmup800. No se confunde fallo técnico con cero trades; la prueba sí se ejecutó y falló económicamente. DD MTM al cierre diario−26.708%, también sobre límite.
V4 reconcilió fills, fees y wallet terminal de ambos. Conteos incluyen bordes parciales; reportar completos al evaluar candidatura.

## Investigación retirada antes de ejecutar
OvernightSPY no justifica un run: prima publicada de una franja nocturna pequeña frente9bpsRT, proxiesBID sinspread y cobertura irregular de horas16NY en invierno. Esto no es medición del PnL de una estrategia overnight propia. Informe detallado del agente documenta fuente primaria y limita esa inferencia.

## Incertidumbre de regularidad
Referencia33/61 meses activos; FixedR5 39/61; parcial35/61. Wilson95 nominal respectivamente41.72–65.99%,51.39–74.83%,44.90–68.98%. Dependencia temporal y selección adaptativa hacen esas bandas meramente descriptivas.
En63meses pareados FixedR5 rescata10yestropea4 respecto a referencia;pMcNemar nominal.1796. Parcial rescata3yestropea1;p.625. No se declaran mejoras confirmadas ni se añaden nuevas restricciones de p/CI.
En períodos COMPLETOS hay61meses y19trimestres: referencia33/59activos y14/19quarters; FixedR5 38/59 y14/19; parcial35/59 y13/19. El aparente avance trimestral de FixedR5 al incluir bordes desaparece en períodos completos. Principales conteos originales se conservan, sin seleccionar el denominador favorable.
Ver informe del agente: strategies/OrchManageFixedR54h/reports/ORCH_REGULARITY_UNCERTAINTY_20261018.md.

Total económico de orquestación:13 pruebas. Smoke técnico y fallo por datos se registran por separado. No hay candidata aceptada. Próximos trabajos: rotación mensual simple BTC/PAXG/SPY/cash con stop10% y exposición reducida para respetar3%riesgo, y pares BTC/ETH pendiente de cobertura histórica. No sumar curvas como cartera ejecutable; Binance one-way requiere una decisión neta por símbolo.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_C_FINAL_20261021.md
SHA256 d29555ddcfe88120f2c3bbf3c80806e3c56c1e9d71e89ab74c2cc4f76ad580c2, 3251 caracteres.

```markdown
# Cierre C: acumulación de sorpresas y volumen sin progreso
2026-10-21. Dos backtests terminados, sin candidata ni fallos técnicos.

| Receta | CAGR neto | PF | DD M1 + eventos | Meses activos positivos | Trimestres positivos | Trades |
|---|---:|---:|---:|---:|---:|---:|
| [CUSUM BTC](http://localhost:9200/#/backtest/2664ba2b-b192-47ae-95aa-18fd2e6a4d9e) |8,98%|1,153|−19,27%|33/62 (53,23%)|12/20 (60%)|310|
| [Volumen sin progreso y escape](http://localhost:9200/#/backtest/e8af10d8-200f-4d21-b5dd-b59daa7b116b) |−1,12%|0,838|−13,53%|13/29 (44,83%)|4/20 (20%)|40|

Ventana[2020-10-15,2026-01-01)UTC,desarrollo observado. Perfil2%/6%/3x,10kporcuenta,fee0.00045porlado yfunding aplicado;slippage0modelado,sin estrés ni nuevaeconomía2026. Neto no incluye todosloscostosreales.
CUSUM fue transferencia explícita de un mecanismo R40 PAXG negativo a BTC, no método inédito. Absorción fue la hipótesis creativa, sin atribuir flujo real a OHLCV. Protocolos C y addendum de actividad se guardaron antes de ejecutar; no se cambiaron umbrales por resultados.

## Decisión
CUSUM no alcanza CAGR30,PF1.2,M65 oQ80. Absorción falla retorno/PF/regularidad y mediana;ademásN40<100operativo. No descartar sólo por muestra pequeña: hay fallos económicos decisivos. No rescatar quitando shorts ni variando drift/umbral/volumen. Presupuesto C cerrado.

## Medición y contabilidad
Cada ruta observó2.741.760minutos y eventos de ejecución. Se obtuvieron63intervalos mensuales (octubre2020parcial) y62mesescompletos,20trimestrescompletos. Equity=wallet+position.pnl,sinvolveramultiplicarporapalancamiento; las nuevas estrategias no usan portfolio_value abierto.
Cortes00:00UTC después del funding y antes de decisiones. Es una convención exacta por fase: fundingde00:00se asignaalintervaloqueacaba,noPnL porfecha[a,b)estricta. Actividadincluyeexposición ymesdeejecuciónconcriterioconservador;ceroscalendarionoseocultan. DDdeM1+eventosno sonextremosintraminuto.
Mediansmensualesde62meses: CUSUM+0,1714%,absorción0%. Netoaritmético sin2mejoresmeses:+2179,50/−1465,11USDT. Cumplir una puerta no rescata fallos en otras.
Contabilidad mediante run_analysis d4409ec183fe4e2cb54a3b10696f2dd3 con310/40tradescompletos. Bruto−fees+funding=sumPNL=saldo−10000,tolerancia1e−6;error máximo1,37e−11USDT. Funding−199,90/−14,72USDT,fees2543,02/236,92USDT;appliedtrue ydatasetcorrecto. Pagosconmarcaproxy777/81,provenanceconservada. Ambosrawopencounter0 ytelemetríafinalreconciliada.
Los summaries de telemetría son resultados emitidos por la estrategia y las63filas por cuenta se recuperaron completas delbloquefinal, aunque haya logs anteriores no incluidos en esa página;no son totales de trades calculados desde página parcial. Se conservanlosreciboscompletos ycontabilidadindependiente de snapshots.

## Continuidad
Se registró D,otra pregunta concontrol: canal en bloques de volumen frente a bloques calendario. No se usan CUSUM/absorción como finalistas. DnoesunavecindaddeCniunasegundapruebaciega;permisoautónomo vigente,riesgo/costos fijos.
Fuentes: BTC_DISCOVERY_C_PROTOCOL_20261021.md, ACTIVITY_ADDENDUM, MANIFEST, ACCOUNTING y archivos TELEMETRY por estrategia, todos bajo reports/. Clases nuevas y helpers anteriores congelados. No tocarframework,globalconfig,Pi,paper/live.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_H_FINAL_20261021.md
SHA256 9d6b1a61a90ae3f4e0aad994edb7d83b0f123d9ce42d63b16bd60235c94672d0, 2451 caracteres.

```markdown
# Tanda H cerrada: mechas y localización del cierre, sin candidata

Se compararon dos geometrías en ocho velas, sin agregar filtros retrospectivos. Las mechas miden O+C−H−L; el control de cierre mide2C−H−L, mismo rango total. Displacement<=ATRprebloque, transición de estado±.20, stop2ATRprevio/TP3ATRprevio/48h. Transferencia explícita de WickBalancePAXG, con ATR14simpleBTC adaptado desde Wilder original; no atribuir diferencias sólo al activo o mechas. N204E404 previo es presión ponderada porvolumen/cohorteVWAP ysuplementoshort, distinto. BTC-USDT Binance,[2020-10-15,2026-01-01),2%/6%/3x,10k,fee.00045+fundingconproxy,slippage0,sinestres/nuevaeconomía2026.

## BtcResearchR12Wicks1m
Dashboard: http://localhost:9200/#/backtest/77ec643b-9761-492d-aca0-01681e0cd203

CAGR 5.5565%; neto 3258.92USDT; PF 1.2170; Sharpe 0.5550; DD M1+eventos 20.0736%; 193 trades; meses activos positivos 34/61; trimestres 14/20. Mediana calendario 0.5723%; neto sin mejores2meses 1374.15USDT. NO_CUMPLE.

## BtcResearchR12CloseLocation1m
Dashboard: http://localhost:9200/#/backtest/658d7534-0034-49f3-8f12-f3271002b2f7

CAGR 5.4949%; neto 3218.57USDT; PF 1.1125; Sharpe 0.4529; DD M1+eventos 18.4378%; 297 trades; meses activos positivos 38/62; trimestres 10/20. Mediana calendario 0.8059%; neto sin mejores2meses 927.25USDT. NO_CUMPLE.

Ambas fallanCAGR30 yregularidad;mechasPFacredita1.2pero no basta. La diferencia de retorno entre controles es pequeña en este histórico, sin evidencia de que se logre el objetivo. No combinar las dos trasverresultado para llamar nueva hipótesis ni afinar8/.20/ATR/target. Presupuesto2corridascerrado,sinreemplazos. CreatividadIdefinida por otra pregunta económica, no rescateH.

Checksc7f47bc011ab4d8abb116833b5b70836 passed, sourcehashc77445df205346aea015162dc049e9aa299dea92776933d6d162b5319e3fadad; revisión independiente sin erroresmateriales. Auditoría4a5ae769d6c443a691a291bd398cee02 completa193/297trades:bruto−fees+funding=PNLsum=finishing−10k a1e−6. TelemetríaM1/63intervalos/62meses/20Q verificada,sumaPnL/equityfinalreconciliadas;DDM1noextremosintraminuto,fronteraspostfunding/predecisiónporfaseR11. Fundingaplicado/proxiesdeclarados;sinposicionesfinales.

Evidencias BTC_DISCOVERY_H_PROTOCOL_20261021.md, BTC_DISCOVERY_H_MANIFEST_20261021.json, BTC_DISCOVERY_H_ACCOUNTING_20261021.json ytelemetríasporreceta. Framework/configglobalintactos,sinpaper/live/Pi. Objetivo noalcanzado,ningunapromoción;autonomía vigente.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_I_FINAL_20261021.md
SHA256 3f4335eebf72ddfdc9e783567fb6fac05385de027609e3a5f825c869d19a14c0, 3392 caracteres.

```markdown
# Tanda I: participación secuencial y reparación de precios

La receta creativa produjo una sola operación. Su control de precios produjo 121 y perdió. Ninguna cumple el objetivo; una operación no permite estimar una ventaja ni refutar la familia económica.

## Diseño

Se registraron dos políticas antes de ejecutar: impulso de al menos un ATR seguido por recuperación entre 50% y menos de 100%. PHASE exige además poco volumen durante el impulso y recuperación a volumen normal; PRICE conserva el mismo patrón de precios sin esa condición. Las medianas usan 28 observaciones anteriores del mismo bloque UTC y están disponibles antes de S. Stop 2ATR previo, objetivo 2R y vencimiento 48h comunes. El objetivo supera la reparación inicial: se prueba persistencia después de esa recuperación.

BTC-USDT, Binance Perpetual Futures, [2020-10-15,2026-01-01), desarrollo reutilizado. Capital virtual 10.000 USDT; riesgo 2%/6%/3x; comisión 0,00045 por lado y funding histórico aplicado con marcas proxy declaradas; slippage modelado cero. Sin estrés, cambios de riesgo ni pruebas económicas nuevas de 2026.

## Resultados

### BtcResearchR12Participation1m
Dashboard: http://localhost:9200/#/backtest/17494d8a-eaf8-437e-8b7d-fac709a8d092

1 operaciones; neto -199.45 USDT; CAGR -0.3855%; PF 0.0000; Sharpe -0.4622; DD M1 y ejecuciones 2.4984%. Meses activos positivos 0/1; trimestres positivos 0/20; mediana calendario 0.0000%; neto sin dos mejores meses -199.45 USDT. NO_CUMPLE; muestra insuficiente para estimar una ventaja.

### BtcResearchR12RepairPrice1m
Dashboard: http://localhost:9200/#/backtest/a091d445-a502-4214-b153-182eb3d2af8d

121 operaciones; neto -1777.49 USDT; CAGR -3.6823%; PF 0.8689; Sharpe -0.3386; DD M1 y ejecuciones 39.8695%. Meses activos positivos 22/56; trimestres positivos 9/20; mediana calendario -0.3682%; neto sin dos mejores meses -3289.46 USDT. NO_CUMPLE; cumple sólo el mínimo preliminar de conteo, sin confianza estadística implícita.

## Auditoría y decisión

Check 29ddfe3edf6046fb8d02e16eff4cb3cb pasó antes de ejecutar, fuente SHA256 3928d2b3fd4ba9ffab43b89e134e982fb65e941cccaba9ba38e3c845bf9acfba. Revisión independiente sin errores materiales. Auditoría c330fae100fc4c0bbd271a07bee69348 sobre snapshots completos: bruto − fees + funding = suma de PnL = equity final − 10.000, tolerancia 1e−6 USDT. Las dos registraron 2.741.760 marcas M1, 63 intervalos mensuales, 62 meses completos y 20 trimestres, con fronteras y suma de contribuciones reconciliadas.

DD representa muestras M1 y ejecuciones, no todos los extremos intraminuto. Fronteras mensuales según convención R11: después del funding y antes de las decisiones; no agrupación estricta de eventos por fecha. Meses inactivos incluidos en mediana. No hubo errores económicos ni reemplazos.

Cerrar las dos corridas sin candidata y sin suavizar los límites de volumen después de observar su baja frecuencia. El control negativo no demuestra el efecto del filtro con sólo una operación del tratamiento. Conservar el resultado negativo y la insuficiencia de muestra como hechos distintos. Continuar con otra pregunta material dentro de la autorización autónoma vigente.

Fuentes, configuración y versiones: BTC_DISCOVERY_I_PROTOCOL_20261021.md y BTC_DISCOVERY_I_MANIFEST_20261021.json; contabilidad y telemetrías en archivos de esta tanda. Framework y configuración global intactos; sin live/paper/Pi.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_M_FINAL_20261021.md
SHA256 3d1017140c83746e4e23495d986f21dfd992b8b42e20981d1dba57e342884e18, 3376 caracteres.

```markdown
# Tanda M: respuesta condicional frente a global, ambas negativas

La distinción entre avance del cierre y recorrido no mejoró esta formulación. COND perdió más que GLOBAL; ninguna cumple los objetivos. Las dos ejercieron respuestas de continuación y reversión, no sólo un lado del modelo. No se selecciona retrospectivamente un bin, signo de media o tipo de respuesta para rescatarla.

Se usaron367OHLC4h,360orígenes con etiquetas24h maduras antes de decidir, binsE=.5 deabs(C-Cprev)/TR,mediasCONDvsGLOBAL ygatecompartido de30observacionesdelbinactual. Ambosdescartaron dos pronósticos por insuficiencia/validez del evento, no por falta de ventanas. Labels describen precio sinstop: el motor evaluó su payoff conSLyfees/funding. Entrenamiento online dentro de backtest continuo, no WF posthoc ni OOS nuevo.

BTC-USDT Binance Perpetual Futures,[2020-10-15,2026-01-01),10k,2%/6%/3x,fee.00045porlado yfunding aplicado/proxiesdeclarados,slippage0;warmup4004h,stop2ATR14simple/sinTP/24h. Sin estrés,2026nuevo/importaciones/framework/configglobal/live/paper/Pi.

| Política | CAGR neto | DD M1 y ejecuciones | PF | Meses positivos/activos | Trimestres positivos | N |
|---|---:|---:|---:|---:|---:|---:|
| [BtcResearchR13GeometryConditional1m](http://localhost:9200/#/backtest/d0f70f5f-e12d-400c-957a-59fb9112b3f6) | -16.25% | 67.09% | 0.857 | 17/58 | 6/20 | 857 |
| [BtcResearchR13GeometryGlobal1m](http://localhost:9200/#/backtest/5a437423-be6d-4f13-a9de-32631ef3c66d) | -3.07% | 34.18% | 0.931 | 14/32 | 6/20 | 361 |

Dashboard: http://localhost:9200/#/backtest/d0f70f5f-e12d-400c-957a-59fb9112b3f6

Neto-6034.18USDT;bruto-2745.02,fees3103.90,funding-185.26;Sharpe-0.7552. Fills siguiendo361,revirtiendo496,total=857. Mediana calendario-1.5267%;netosinmejores2meses-8197.75USDT.

Dashboard: http://localhost:9200/#/backtest/5a437423-be6d-4f13-a9de-32631ef3c66d

Neto-1501.88USDT;bruto-5.50,fees1452.48,funding-43.89;Sharpe-0.1636. Fills siguiendo141,revirtiendo220,total=361. Mediana calendario0.0000%;netosinmejores2meses-3035.91USDT.

Ambas fallanCAGR/PF/DD/M65/Q80/mediana/concentración. Conteos no acreditan confianza estadística. Cerrar las dos políticas, cero errores económicos/reemplazos; no cambiarbins/ventana/hurdle/labels después de observar pérdidas. AntecedentesPathAnalogue/RunDuration/FreshStructurearchivado preservados, M no rescata sus recetas.

Check800fc7c5eeb54250b472a89e7f0ec017 pasó125aserciones en un intento antes de economía;fuenteSHA2563968e9a2733fbe9e4a22b32ba71d023defcefa79eae65e992833f1810fb82b97. Root y revisión independiente confirmaron360targets<=T y exclusión de etiqueta del origen actual. Análisisfinanciero4b56c117c61643f5836c34665e1dd3b9completo857/361trades:bruto−fees+funding=PNLsum=finishing−10k a1e−6USDT. Telemetría2.741.760M1/63intervalos/62meses/20Q,sumaPnL/equityfinal,fronteras ycontadoresfollow+fade=Nreconciliados. CondusaFINALdespuésdelaliquidaciónterminalconfee; nocontarPRETERMINALcomoresultadofinal. DD M1noextremosintraminuto;fronteraspostfunding/predecisiónporfaseR11.

Fuentes/configprevios BTC_DISCOVERY_M_PROTOCOL_20261021.md yMANIFEST;recibostécnicos TECHNICAL_CHECK.json/TECHNICAL_PREPARATION.md;contabilidadytelemetrías guardadas. Objetivo pendiente. Continuar otra pregunta material; antes de composición se analizan intervalos completos de controles positivos, sin sumar curvas ni presumir entradas bloqueadas.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_O_FINAL_20261021.md
SHA256 2d6473c73fc6cda419c69f213097abfc26d97f6a2fae15b1cd29bb6fc5d91889, 3827 caracteres.

```markdown
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

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_D_FINAL_20261021.md
SHA256 26fe4f3940e85e7561d64d0a12309b2da5979ed0316abf537ec8146f6ebf2643, 5663 caracteres.

```markdown
# Investigación BTC: cierre de tandas C y D

Cuatro backtests económicos nuevos completados; ninguna candidata. Tres hipótesis y un control, con reglas registradas antes de ejecutar cada tanda. No son cuatro muestras independientes ni validación fuera de muestra.

## Resultados

| Prueba | CAGR neto base | DD M1 + ejecuciones | PF | Meses activos positivos | Trimestres positivos | Operaciones |
|---|---:|---:|---:|---:|---:|---:|
| [Detección acumulativa CUSUM](http://localhost:9200/#/backtest/2664ba2b-b192-47ae-95aa-18fd2e6a4d9e) | 8.98% | 19.27% | 1.153 | 33/62 | 12/20 | 310 |
| [Absorción y escape](http://localhost:9200/#/backtest/e8af10d8-200f-4d21-b5dd-b59daa7b116b) | -1.12% | 13.53% | 0.838 | 13/29 | 4/20 | 40 |
| [Reloj de volumen](http://localhost:9200/#/backtest/72326aa5-947f-410b-b7d7-f2ccadaf3c57) | 4.49% | 22.33% | 1.057 | 32/62 | 11/20 | 424 |
| [Control calendario](http://localhost:9200/#/backtest/696277c8-e897-4528-8327-dc1b5b621a2e) | -4.96% | 38.96% | 0.921 | 24/62 | 6/20 | 386 |

Ventana común: 2020-10-15 inclusivo a 2026-01-01 exclusivo. Capital virtual 10.000 USDT; riesgo objetivo 2% por trade, límite agregado 6%, 3x aislado. Neto de fee 0,00045 por lado y funding histórico aplicado/verificado; slippage modelado cero. El dataset de funding incluye marcas proxy declaradas. No se hicieron pruebas económicas nuevas de 2026 ni estrés de costos o variantes de riesgo.

## Qué preguntamos y qué aprendimos

C probó una transferencia CUSUM desde el antecedente PAXG y una idea creativa de absorción: volumen alto sin desplazamiento, seguido por escape del rango. El control de antecedentes distinguió esta última de shock contrarian, NR7, filtros de volumen y presión ya explorados. CUSUM obtuvo retorno positivo pero insuficiente y poca regularidad; absorción perdió y sólo produjo 40 operaciones. No convertir la atribución long/short observada en una selección retrospectiva de dirección.

D preguntó si medir el tiempo por volumen acumulado mejora una misma señal de ruptura de tres bloques previos. Se comparó con bloques calendario de seis velas 4h. El objetivo de volumen se fija al iniciar cada bloque con información previa; el exceso se consume sin repartir ni arrastrar. Ambas políticas mantienen protección y riesgo iguales. El reloj de volumen mejoró al calendario en este histórico, pero su CAGR 4,49%, PF 1,057 y regularidad no cumplen los objetivos. Al retirar sus dos mejores meses el resultado aritmético es negativo: −1.679,58 USDT. Superar el control no basta para promover.

Las cuatro incumplen CAGR mínimo 30%, PF mínimo 1,2, 65% de meses activos positivos y 80% de trimestres completos positivos. El control calendario además supera el DD máximo 25%. El reloj de volumen queda dentro del techo de 25% pero excede el objetivo de 20%. Medianas mensuales calendario: CUSUM +0,1714%, absorción 0%, volumen +0,0886%, calendario −0,7363%; incluyen meses inactivos. Diagnóstico sin los dos mejores meses: CUSUM +2.179,50 USDT; absorción −1.465,11; volumen −1.679,58; calendario −4.364,11. El mínimo operativo preliminar N=100 no constituye potencia estadística ni confianza por sí mismo.

## Medición y auditoría

Cada corrida registró 2.741.760 marcas M1 más ejecuciones, 63 intervalos mensuales contiguos (62 completos) y 20 trimestres completos; cero ventanas de señal inválidas. Equity se calcula como wallet + PnL abierto, sin multiplicarlo otra vez por apalancamiento. No se cambió el framework. DD representa muestras M1 y eventos, no todos los extremos intraminuto.

Las fronteras mensuales son a 00:00 UTC después del funding efectivo y antes de decisiones nuevas; el funding de esa frontera pertenece al intervalo que termina según esta convención. No equivale a agrupar cada evento en meses estrictamente [inicio,fin). Actividad se determina por exposición y ejecución, no por PnL distinto de cero. Los cuatro acabaron sin posiciones abiertas.

La auditoría completa de 310/40/424/386 operaciones reconcilió PnL bruto − comisiones + funding con PnL de trades y equity final; error máximo inferior a 1e−6 USDT. También se verificó que la suma de contribuciones mensuales coincide con el resultado final. Job de auditoría: 2eac4d059f45473f98ed4d832f068309. Esto acredita contabilidad, no rentabilidad futura.

## Decisión y continuidad

Cerrar los presupuestos C/D sin candidata y sin búsqueda de parámetros vecinos, filtros retrospectivos o eliminación de shorts para rescatar curvas. Desde r9 se completaron siete corridas económicas nuevas: A/B tres y C/D cuatro. El bloque histórico V1–V6 conserva sus 209 económicas; no es un censo global del proyecto ni se suma como muestras independientes.

La autorización autónoma sigue vigente. La siguiente tanda requiere otra pregunta material, contraste con antecedentes y protocolo con presupuesto previo. El contraste D aporta una diferencia histórica que puede orientar preguntas, pero no demuestra ventaja económica suficiente ni autoriza repetir sus vecinos. Mantener BTC individual y costos/riesgo acordados; estrés queda para candidatas y acuerdo conjunto. PAXG/SPY/cartera son fases eventuales.

## Evidencia

Protocolos y manifiestos: BTC_DISCOVERY_C_PROTOCOL_20261021.md, BTC_DISCOVERY_C_ACTIVITY_ADDENDUM_20261021.md, BTC_DISCOVERY_C_MANIFEST_20261021.json, BTC_DISCOVERY_D_PROTOCOL_20261021.md y BTC_DISCOVERY_D_MANIFEST_20261021.json. Fuentes y hashes en manifiestos; telemetría completa y recibos en los cuatro archivos TELEMETRY. Contabilidad completa: BTC_DISCOVERY_CD_ACCOUNTING_20261021.json. Contrato de medición: BTC_RESEARCH_M1_MEASUREMENT_20261021.md. Resultados estructurados de este cierre: BTC_DISCOVERY_CD_RESULTS_20261021.json.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_F_FINAL_20261021.md
SHA256 fe2423c14314fe4b6a7a505befb77bca7e9b6436aff8805a0ca0f0f1bc3916df, 2175 caracteres.

```markdown
# Tanda F cerrada: seguir supera a revertir, sin candidata

Pregunta registrada: mismo evento de desplazamiento24h concentrado según RV/BV, dos direcciones contrarias con misma protección. No test estadístico certificado de saltos. BTC24/7, ruta1m ydatos1h/4h, sinhorariobursátil heredado del antecedenteSPY. Ventana[2020-10-15,2026-01-01), desarrollo reutilizado;2%/6%/3x,10k,fee.00045+fundingaplicado/proxiesdeclarados,slippage0,sinestres/2026nuevo.

## BtcResearchR12JumpFade1m
Dashboard: http://localhost:9200/#/backtest/80fa4bf7-d510-4c9a-967c-88b75cc49752

CAGR -22.0969%; neto -7281.67USDT; PF 0.6681; Sharpe -1.4277; DD M1+eventos 74.2029%; 382 trades; meses activos positivos 18/62; trimestres 4/20. Mediana calendario -2.0241%; neto sin mejores2meses -8193.84USDT. NO_CUMPLE.

## BtcResearchR12JumpFollow1m
Dashboard: http://localhost:9200/#/backtest/8b78a705-a8f3-4656-9705-e56300623ddf

CAGR 13.1558%; neto 9054.71USDT; PF 1.2556; Sharpe 0.7915; DD M1+eventos 24.2427%; 381 trades; meses activos positivos 32/62; trimestres 13/20. Mediana calendario 0.0997%; neto sin mejores2meses 5469.24USDT. NO_CUMPLE.

Las dos fallanCAGR30 yregularidadM65/Q80. Follow cumplePFpero ganaralcontrolno cumplemetasabsolutas. DD M1seusaenpuerta,noDDdiariomenor. No seleccionar lados,años o umbralesJposteriores para rescatar. Presupuesto2corridascerrado,cero reemplazos ni técnicas económicas. Continuar con otra preguntaGautorizada yprerregistrada.

Checks job11aa61fd2bc3458c987a7c63f104233e passed; fuentehash631377b49a213511ca5d08f63e50cf08aa38e18fcec303479b89e3a9fc0b81a6. Revisión independiente sin errores materiales. Auditoría completa jobf1aa6ed658934d40b573af21da372858:382/381trades,bruto−fees+funding=PNLsum=finishing−10k a1e−6. Telemetría2.741.760M1/63intervalos/62meses/20Q,cero ventanasinválidas,fronteras/sumaPnL/equityfinal reconciliadas. FronterasUTCporfasepostfunding/predecisión,no agrupaciónestricta deeventosporfecha;DDM1noextremostick.

Evidencias: BTC_DISCOVERY_F_PROTOCOL_20261021.md, BTC_DISCOVERY_F_MANIFEST_20261021.json, BTC_DISCOVERY_F_ACCOUNTING_20261021.json ytelemetríasporreceta. Configglobal/frameworkintactos,sinpaper/live/Pi. Ningunapromoción.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_T_FINAL_20261021.md
SHA256 bffd21029e606b79547f568e023a51f68e4d27c7536a2cf870513dafeb87bca6, 3492 caracteres.

```markdown
# BTC Discovery T — cierre

Pregunta predeclarada antes del resultadoS: ¿medias del retorno4h condicionadas a seis fasesUTC aportan utilidad frente a driftGLOBAL?541closes/540labels90días/90porfase,asofmaduro;mediascongeladas00UTC,sinrefitintradía/fallback/ranking. TransferenciaPAXG reconocida,antecedentenegativo y sesgoselecciónhistórico preservados. Desarrollo ampliamente observado,noOOS.

Contrato:[2020-10-15,2026-01-01)UTC,10k,2%/6%/3xaislado,fee.00045/lado,fundingBTC históricoON/aplicado/verificado(proxiesdeclarados),slippage0.Neto=fees+fundingmodelados. Stop2ATR14simple/noTP/plazo1BAR4h desdeopened_at,ejecución/observadorM1,mismoadmisibilidadambosplanesflat,sinbuffersnuevos.600warmup4h sólo margen técnico,training90días.

|Modelo|N|CAGR%|PF|DD M1+fills%|Meses activos positivos|Q positivos|Mediana mensual%|Neto sin2mejores meses|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[PHASE](http://localhost:9200/#/backtest/a958beca-1611-4f88-bc96-d5cb62e33da6)|1411|-17.629452|0.786506|71.283806|11/48|1/20|-1.033131|-7862.982604|
|[GLOBAL](http://localhost:9200/#/backtest/6b0c5fca-4634-47e8-8de8-50e24288f7c6)|118|0.144022|1.027724|6.346677|2/3|1/20|0.000000|-341.346703|

PHASE: bruto precio -1193.6780147095335; fees 4494.398625742648; funding -675.8753489589292; neto -6363.951989411119; equity final 3636.0480105888496. Añoscompletos{"2021":-46.49796645841071,"2022":-21.3017671036263,"2023":-12.05675528820258,"2024":-13.578813905414922,"2025":-6.7430293158677435}; peor/mejor12m-46.49796645841071/-6.7430293158677435%.

GLOBAL: bruto precio 468.148285307258; fees 294.8429760765848; funding -97.94883764515173; neto 75.35647158552153; equity final 10075.356471585521. Añoscompletos{"2021":0.7535647158551928,"2022":0,"2023":0,"2024":0,"2025":0}; peor/mejor12m-0.17501434134826743/3.319250310006927%.

GLOBAL alcanzaM65aritmético(2/3), pero sólo3mesesactivos de62 completos;118trades no son118regímenes independientes. Su pequeña ganancia y DD bajo no bastan: CAGR/PF/Q/mediana/sin2mejores incumplen. PHASE pierde incluso antes de costos. No seleccionar horas/lados/años pararescatar.

Ambas1903freezesdiariosválidos,0invalidaciones/0planrejections,0invalidwindows,2741760marcasM1/63intervalos/62mesescompletos/20Q. Primer día sinfreeze hasta próxima medianoche permanececashcomún. PRETERMINALfinalsinabiertas. DD M1+fills,noextremosintraminuto; corte mensual por fase postfunding/predecisión; medianacalendarioincluyeinactivos. Ventanas12m solapadas,noindependientes.

Auditoría7d5c776f8eb94ca0a92a29291eeb2322 succeeded, snapshots completos: gross−fees+funding=PNLsum=equityfinal−10k,error<1e-6. No totales desdepáginasparciales. N>=100 es suficienciaoperativapreliminar, no potencia. Check9b18b8dc8a064c56acc2ab8206020bd2 PASS155; primerharnessfailed porfalso research/BtcResearch,corregidosólopredicate,padres/fuentesintactos. Dos económicos completos,0fallos/reemplazos/backteststécnicos.

Decisión:NO_CUMPLE enambas;ningunacandidata. Tcerradasinvecinosde90d/bins/hurdle/freeze/signo/horizonte/ATR/gestión,seleccióndehoras/días/años/lados/pesos/refits.Noestrés/riesgonuevo/2026/imports/live/paper/Pi.

Continuidad:38económicasdesde r9,209legacyV1–V6 aparte,nocensoglobalniindependencia. Carryfundingdireccionalnoesbrecha:V4/V5/pilotos yA_EVENTyacerrados;verBTC_NEXT_QUESTION_DEDUP_FUNDING_20261021.md. Revisiónsiguientepreguntasólolectura(duraciónprimerpasaje/volumenexterno),sinprotocolo,código,draftnieconomíaautorizados. Objetivonoalcanzado,continuarautónomamente.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_R_FINAL_20261021.md
SHA256 beffb2ddf1ca02385248217794623b8130b5eb90320f077998477a2a32f05e00, 2928 caracteres.

```markdown
# BTC Discovery R — cierre

Pregunta: similitud de seis retornos normalizados L2, KNN20 coseno frente a media global de los mismos 360 orígenes maduros, para pronosticar retorno de precio a24h. Protocolo previo, dos corridas completas, ninguna sustitución económica.

Ventana UTC [2020-10-15,2026-01-01), desarrollo reutilizado. Capital10000; riesgo2%/6%/aislado3x; comisión taker0.00045 por lado; funding histórico aplicado y reconciliado, con marcas proxy declaradas; slippage0. Neto=fees+funding modelados. Stop2ATR14simple, sinTP, timeout24h. No estrés ni variantes de riesgo.

|Modelo|N|CAGR%|PF|DD M1+fills%|Meses activos positivos|Trimestres positivos|Mediana mensual%|Neto sin2mejores meses|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[KNN](http://localhost:9200/#/backtest/e9f4b1d0-277a-4ef7-b10d-c72365d1809e)|1751|-18.963571|0.941229|83.138366|25/62|7/20|-0.707490|-10656.139018|
|[GLOBAL](http://localhost:9200/#/backtest/ca8c8f66-8fe0-460a-a3ac-142c565b4961)|1265|-6.824291|0.962141|57.175057|22/58|8/20|-1.773945|-7173.250998|

KNN: bruto precio 4701.021658605742; comisiones 9948.266673171467; funding -1413.6015183596885; neto -6660.846532925419; equity final 3339.1534670745136. Años completos: {"2021":16.63716600808669,"2022":-22.378583620187133,"2023":-28.484899927751172,"2024":-46.389541736351866,"2025":-25.94236968672027}. Peor ventana móvil12m -46.90821269679664%; mejor 64.84593144335804%.

GLOBAL: bruto precio 5849.171266847794; comisiones 7018.0481513692275; funding -1914.8927447151261; neto -3083.769629236552; equity final 6916.230370763464. Años completos: {"2021":-7.939920017396518,"2022":-18.40805561046753,"2023":-19.45835468464412,"2024":9.187526351732078,"2025":-19.14598573194839}. Peor ventana móvil12m -37.62939107167723%; mejor 40.855837110551164%.

Auditoría financiera de snapshots completos: job f16a68a6f6cd49108af72f2fc0fa458c succeeded; errores de reconciliación <1e-6. No totales inferidos de páginas parciales. Telemetría63filas mensuales/62meses completos/20trimestres,2741760marcas M1 por receta,0ventanas inválidas. GLOBAL usa FINAL tras liquidación terminal; contador rawopen1 es metadato previo, no exposición final. DD observa M1+fills, no todos extremos intraminuto. Frontera mensual por fase postfunding/predecisión. Ventanas móviles solapadas, no OOS ni muestras independientes.

Chequeo técnico final1169PASS, job98cb30b8d9ac40a292e01402524fef09; primer intento tuvo SyntaxError del fake harness, corregido antes de economía. N>=100 sólo suficiencia operativa preliminar, no potencia estadística.

Decisión: ninguna candidata. Se cierra R sin ajustar K, dimensión, lookback, horizonte, distancia, hurdle ni signo. El beneficio bruto no cubre costos base. Otra pregunta material puede estudiar utilidad realizable con stop, preservando modelo y parámetros; requiere protocolo y revisión de antecedentes antes de implementación. No es aprobación ni ejecución de S.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_S_FINAL_20261021.md
SHA256 de4443371df6c39fbe733a523741f1b24e7b74c8b846c0af030b3dcbf4ed3bab, 3312 caracteres.

```markdown
# BTC Discovery S — cierre

Pregunta material: KNN20/cosenoL2 sobre seis retornos frente a GLOBAL de los mismos360orígenes, aprendiendo dos payoffs fee-only con stop2ATR/noTP24h. Cambio de target respectoR, no ablación causal pura ni evidenciaOOS. Antecedente Angle de labels monetarios preservado sin relajar sus gates.

Ventana[2020-10-15,2026-01-01)UTC,10k,2%/6%/3xaislado,fee.00045/lado,slippage0,funding históricoBTC ON/aplicado/verificado con proxiesdeclarados. Neto real incluye fees y funding; labels sólo fees por nocional, no neto completo ni órdenes contrafactuales ejecutadas.

|Modelo|N|CAGR%|PF|DD M1+fills%|Meses activos positivos|Q positivos|Mediana mensual%|Neto sin2mejores meses|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[KNN](http://localhost:9200/#/backtest/97da0472-42e2-4f1a-b5be-b63f02e44318)|1643|-7.729306|0.967591|61.601500|28/62|7/20|-0.693118|-6553.473222|
|[GLOBAL](http://localhost:9200/#/backtest/1709388d-cc36-411b-bac0-7102b3fceb7e)|902|-2.061120|0.984002|45.289492|22/51|8/20|0.000000|-5221.973347|

KNN: bruto precio 8033.446762119682; fees 9937.80305348834; funding -1522.7381478642626; neto -3427.094439232939; capital final 6572.905560767034. Años completos {"2021":13.76937060504475,"2022":-32.731322578714504,"2023":-24.641796751558466,"2024":10.815320884566093,"2025":-22.00274004431979}; peor/mejor12m -40.72059174553348/35.95913156432082%.

GLOBAL: bruto precio 6014.539956064877; fees 5097.655771779939; funding -1946.3559332292652; neto -1029.471748944319; capital final 8970.528251055617. Años completos {"2021":-16.528798692063063,"2022":11.31917374924667,"2023":-19.46630366742482,"2024":-3.062729372668871,"2025":-5.675761671102153}; peor/mejor12m -26.973113346761224/28.5827735700936%.

Verificación real: en ambas recetas11424decisiones4h,360orígenesválidosmínimo/máximo,11783paresmaduroscalculados,4100857cachehits,11423purges,0featureinvalid/0missinglabels. Cada path1440M1exactoscerrados/deadline24h; esto acredita cobertura de esta ejecución, no ventaja predictiva. Forecasterfee-only no representa funding/margen y puede diferir del fill real; gestiónrealheredada desdeopened_at sin modificar.

Medición63intervalos/62meses completos/20trimestres,2741760M1marks cada cuenta,0invalidwindows; PRETERMINAL=finalsinposiciónabierta. DD M1+fills, no todos extremosintraminuto; corte mensual por fase postfunding/predecisión; mediana incluye inactivos. Ventanas12m solapadas, no independientes.

Auditoría financiera dbe601b37bc44b4fb350504abba12147 succeeded de snapshots completos: gross−fees+funding=PNLsum=equityfinal−10000,error<1e-6. N>=100 es suficiencia operativa preliminar, no confianza. Checktécnico suppliedsource/sintéticos1a13343c98ea41adbf0ee4bb6d97ab74,1900PASS primerintento; padres sin cambios. Dos económicos completos,0fallos/reemplazos/backtests técnicos.

Decisión: NO_CUMPLE,ninguna candidata. Se cierra S sin vecinos deK/d/lookback/horizonte/distancia/hurdle/signo/costlabels/fundinglabels/stop/shrink ni selección retrospectiva long-only. Bruto positivo no cubre costos. Sin estrés/riesgo nuevo/2026/live/paper/imports.

Continuidad: T, faseUTC4h frente a driftGLOBAL, protocolo fijado antesdelresultadoS. Todavía requiere recibos técnicos, manifiesto y preflightantesmotores. Objetivoeconómiconoalcanzado; continuarautónomamente.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_U_FINAL_20261021.md
SHA256 6c72fc715862379d5f9807a029abaf6c34e5bc82a5bb1183ac6be94a7f755352, 4568 caracteres.

```markdown
# BTC Discovery U — cierre

Se compararon dos libros BTC completos, con las tres ramas legacy conservadas. La única diferencia entre políticas fue qué volumen fija la frontera temporal del suplemento X805: BTC o ETH. Los precios, HLC3, pesos de volumen y estructura siempre fueron BTC. No se reabrieron P/J/Q ni el ranking R8. X805 histórico negativo sigue como antecedente; el contrato actual, validez compartida y guard físico de TP impiden llamarlo réplica histórica literal.

Contrato UTC [2020-10-15,2026-01-01), capital10000, riesgo2%/6%, aislado3x, fee.00045 por lado, funding BTC histórico aplicado/verificado con proxies declarados, slippage0. Reserva legacy.001 sólo en sizing, LOT.001, mismos valores en ambos. ATR Wilder real y lifecycle R16 conservados; ETH sólo dato auxiliar. Desarrollo ampliamente observado, no OOS.

|Política|N|CAGR%|PF|DD M1+fills%|Meses activos positivos|Trimestres positivos|Mediana mensual%|Neto sin dos mejores meses|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[BTC_CLOCK](http://localhost:9200/#/backtest/3cd02a5c-4275-49fa-8a0c-fa7e9528d604)|536|3.859745|1.031535|44.502762|31/62|11/20|-0.098729|-2429.751038|
|[ETH_CLOCK](http://localhost:9200/#/backtest/81bf2f14-98ad-48f2-a6c2-2151c11512c8)|537|6.274067|1.052468|42.658798|33/62|10/20|0.146945|-963.970162|

BTC_CLOCK: bruto de precio 7214.607093135738; comisiones 5706.126775729788; funding 675.6934126488663; neto 2184.1737300548198; capital final 12184.173730054858. Años completos: {"2021":60.107586045176696,"2022":-13.056408133610697,"2023":21.158885223012458,"2024":-9.72762906976542,"2025":-14.330024120352036}. Peor/mejor ventana12m: -24.441176779606977/74.43843811006272%. Ledger por rama: {"LONG_RUNNER":{"fills":30,"closes":30,"net":7925.40886030179},"CORE_SHORT":{"fills":86,"closes":86,"net":3174.040000436401},"SUPPLEMENT":{"fills":420,"closes":420,"net":-8915.275130683383}}.

ETH_CLOCK: bruto de precio 8888.735350665738; comisiones 5892.35354673626; funding 739.4950400590908; neto 3735.8768439885503; capital final 13735.87684398853. Años completos: {"2021":54.34736488070793,"2022":-4.11018065601546,"2023":20.35491800104039,"2024":-10.151180083909884,"2025":-8.124309285975285}. Peor/mejor ventana12m: -24.823456692167913/68.15060462447178%. Ledger por rama: {"LONG_RUNNER":{"fills":30,"closes":30,"net":8195.35949730576},"CORE_SHORT":{"fills":86,"closes":86,"net":2567.8023146166006},"SUPPLEMENT":{"fills":421,"closes":421,"net":-7027.284967933809}}.

Ambas políticas tuvieron11423 ventanas M1 completas y válidas; los contadores comunes de observación son idénticos. Cortes iguales645 veces y distintos10778; setups distintos151. La distribución temporal externa sí modificó la representación, sin demostrar causalidad de ETH ni alpha aislado. Mismo corte actual no implica misma transición si los latches históricos difieren. Las diferencias del libro incluyen ocupación, selección y capital endógenos; los aportes por rama no son cuentas independientes.

Ambas usan FINAL tras liquidación terminal. R16 ledger: fills=closes=N, suma de ramas=neto, reconciliado a1e-6. total_open_trades1/open_pl son metadatos previos a esa liquidación, no exposición residual. R11:2741760 marcas M1,63intervalos/62meses completos/20Q,0ventanas inválidas. Historia4h241..11664. DD observa M1+fills, no todos extremos intraminuto. Corte mensual por fase postfunding/predecisión; mediana calendario incluye inactivos. 51ventanas móviles solapadas, no independientes.

Auditoría financiera b8962441b3fd486e89b177a8ecd8af98 succeeded sobre snapshots completos: gross−fees+funding=PNLsum=equityfinal−10000,error<1e-6. No totales de páginas parciales. Check técnico2d9df9fc38ef470f983d39e1a3f17acc PASS172; corregido un formato de fuente antes de jobs y dos fallos del harness antes de PASS. Fuentes sin cambios entre los tres análisis; padres intactos. CODES/recibos preservan todo. Fakes no prueban semillas Wilder reales o paridad completa del broker.

Decisión: NO_CUMPLE en ambas, ninguna candidata. Mejor resultado relativo no alcanza CAGR/PF/DD/M/Q/concentración. Cerrar sin vecinos de50%/240/setup/horas/otros activos reloj/gestión/riesgo, sin quitar ramas/lados ni operar sólo desacuerdos. Sin estrés ni nuevas pruebas2026/live/paper/imports/Pi.

40económicas desde r9;209legacy V1–V6 aparte, sin afirmar censo global o independencia. V fue documentada antes del resultado U: dinámica conjunta BTC/ETH frente AR1 con admisibilidad común. Sólo implementación/checks autorizados por root por ahora, aún sin economía. Objetivo pendiente; continuar autónomamente.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_V_FINAL_20261021.md
SHA256 19318495e08784852eb6ecc04d12c6293906dc5245e147f358e39842454c6b36, 4161 caracteres.

```markdown
# BTC Discovery V — cierre

Se comparó VAR1 conjunto BTC/ETH con AR1 BTC exacto de G, bajo admisión compartida.242 cierres sincronizados,240 pares maduros,OLS centrado rank2 según NumPy default, seis pasos recursivos con ETH predicho. B usa filas predictor/columnas respuesta; no se usó ETH futuro. Sin regularización, clipping, filtros de estabilidad ni otro horizonte. El contraste comprende ambas ecuaciones y feedback; no aísla causalidad ETH→BTC.

Contrato UTC [2020-10-15,2026-01-01),10k,2%/6%/3x,fee.00045 por lado, funding BTC histórico aplicado/verificado con proxies, slippage0. R10 sizing, stop2ATRsimple, sinTP, timeout24h desde fill en primer cierre4h elegible; R11 M1 intacto. Forecast bruto de precio, no payoff neto. Warmup3004h. Desarrollo observado, no OOS.

|Política|N|CAGR%|PF|DD M1+fills%|Meses activos positivos|Trimestres positivos|Mediana mensual%|Neto sin dos mejores meses|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[VAR](http://localhost:9200/#/backtest/abab7a82-4df9-489a-8528-e5ec8607f43e)|1533|-7.342609|0.967405|66.051916|25/62|7/20|-1.055285|-7652.471521|
|[AR](http://localhost:9200/#/backtest/01af3d1f-a881-468e-ab1a-5b67460591d3)|1481|-7.444034|0.968755|62.035364|27/62|8/20|-2.391767|-8850.377776|

VAR: bruto precio 7490.732181093577; fees 8634.453674758912; funding -2138.403656693383; neto -3282.125150358702; capital final 6717.874849641259. Años completos: {"2021":-6.819840348620643,"2022":-44.175767389881415,"2023":0.6145842419797987,"2024":0.26037308551167815,"2025":-16.66935237168311}. Peor/mejor12m: -48.10335250027398/32.43979210983709%.

AR: bruto precio 8047.125197941238; fees 9127.724066540486; funding -2239.797078290056; neto -3320.395946889291; capital final 6679.604053110798. Años completos: {"2021":-8.48446180932484,"2022":-34.88775759048261,"2023":6.4622502197481335,"2024":-8.9613052825667,"2025":-24.71978011505609}. Peor/mejor12m: -38.69394314966218/28.429765273779537%.

El nuevo control AR reproduce económicamente [G original](http://localhost:9200/#/backtest/c72b53d8-c986-4131-814b-788cdc0f49e2):1481 trades, mismos type/opened_at/closed_at y error0 en entry/exit/qty/fee/PNL/funding por fila, ignorando IDs/nombres. La admisión conjunta fue válida11424 veces en ambas políticas, por lo que no alteró G en esta trayectoria. No se presenta esa reproducción como evidencia independiente ni mejora. Se conservaron las dos ejecuciones nuevas por ID y la replicación se identifica separadamente; no se deduce un número de hipótesis independientes de los conteos.

Auditoría4967b36eb26749938cafc6ce0303a1f2 succeeded con snapshots completos VAR/AR y G sólo lectura: gross−fees+funding=PNLsum=equityfinal−10000,error<1e-6. Artefacto audit.json incluye comparación G. AR usa FINAL tras liquidación terminal; rawopen1 era metadato previo. VAR PRETERMINAL coincide con final sin abiertas.63intervalos/62meses completos/20Q,2741760marcasM1 por cuenta,0invalidwindows; rank/forecasts válidos11424 de11424. DD M1+fills,no extremos intraminuto; corte mensual por fase postfunding/predecisión; mediana incluye inactivos.51ventanas12m solapadas,no independientes.

Check9f08bcad89ec485a8757da1d6650e9be PASS primer intento,12grupos materiales,NumPy1.26.4; padres intactos. Dos económicos completos,0fallos/reemplazos/backtests técnicos. No stress ni variantes de riesgo. N>=100 sólo suficiencia operativa preliminar.

Decisión: NO_CUMPLE ambas, ninguna candidata. La diferencia pequeña de neto no justifica conservar esta dinámica conjunta. Cerrar sin vecinos de240/horizonte/lag/rcond/regularización/clipping/hurdle/lado/estabilidad/gestión/coupling; no aislar segmentos o coeficientes ganadores. Sin nuevas pruebas2026/imports/live/paper/Pi.

42ejecuciones económicas desde r9 por ID; una reproduce trayectoria G ya medida.209legacy V1–V6 aparte, no censo global ni muestras independientes. W sólo protocolo en preparación, fijado antes del resultado V: estado de dos primeros pasajes con barreras competidoras, type+fast frente type. Overshoot y distancia residual impiden llamarlo velocidad pura. Sin fuentes/jobs/drafts/economía W hasta revisión root. Objetivo pendiente, continuar autónomamente.

```

### strategies/AngleCombinedBtcAcceptance4h/reports/ANGLE_BTC_ACCEPTANCE_RESULTS_20261018.md
SHA256 898fa137d069ee38291d8c9509787b3969a1543341f287f28358c11e6bffca5d, 3738 caracteres.

```markdown
# BTC intrabar acceptance — result and limitations — 2026-10-18

[Combined acceptance run](http://localhost:9200/#/backtest/b1c63c4c-ddc9-40d9-b289-d01915073041), compared with the immutable [reference](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).

## Verdict

Not an accepted candidate: it fails the65–70% positive active months and80% positive quarters objectives. The fixed intrabar gate reduces drawdown and produces a small, profitable short sample, but calendar regularity is insufficient and2022 deteriorates. Do not grid occupancy thresholds, increase risk, or promote21shorts on winrate alone. No further acceptance test is authorized.

## Validated operational effect

The run finishes without error and with zero open-position counter. Final logs verify327 baseline structural/distance candidates,327exact contiguousM1 windows and327matching aggregate4h close/high/low checks. The gate rejects300 and accepts27;21short positions actually fill. Acceptance is only admission before portfolio sizing and STOP execution, not a guarantee of an order/fill. There are no missing/parity-invalid candidate windows. Thus the new observable is accessible and causal under this dataset.

Logs2025 alone:52candidates,52validcoverage/parity,48rejected,4accepted and4shortfills. Diagnostics use helpers.debug and remain in the session logs.

Source scope was checked by mechanically removing the added imports, class/docstring rename, diagnostic hooks and the single gate: the remainder exactly equals the original12917-character baseline. No other economic rule was changed. Longs/PAXG/SPY nevertheless change cash PnL through the shared cash and compounding path; they are not fixed independent sleeves.

## Overall performance and components

Stored engine metrics:118trades=97long+21short; finalbalance33326.3298 from10000; net23326.3298; fees3169.1625; annualreturn25.9714%; maximumdrawdown−13.72495%; overallWR48.3051%, longWR44.3299%, shortWR66.6667%.

Root analysis46be126036194c67857c0f30fdce3982/V4 verifies:
- BTCshort:21trades, net2138.669524, fees258.959008, grosspricePnL2397.628532,PF2.27837,WR66.6667%.
- BTClong net13598.72514;SPYlong3473.11536;PAXGlong4115.81976.
- The profitable short cohort is only21observations; correlated/regime-dependent trades and development selection preclude a robustness conclusion.

## True MTM regularity from Root V4

All calendar months:34/63positive=53.9683%.
Active months:34/60positive=56.6667%.
Calendar quarters:15/21positive=71.4286%, matching the reference count rather than meeting80%.

For complete periods:34/61calendar monthspositive=55.74%;34/58active monthspositive=58.62%;14/19quarterspositive=73.68%.

Relative to reference it rescues5months and spoils4. This small net change is insufficient.2022MTM becomes−5.056% versus reference+2.674%; worstquarter−6.017% versus−4.236%. These results weigh against judging the lower headline drawdown/shortprofitfactor in isolation. Annual comparisons remain development diagnostics, not clean OOS evidence.

## Research bookkeeping

One economic change and one run, no tuning. Root V4+components succeeded under46be126036194c67857c0f30fdce3982. Child component-only analysisa940680d01b2483c940651e437d909e7 had already been submitted immediately before the root warning against duplication; it creates no new hypothesis or backtest, and no additional jobs were submitted afterward. Root results are the accounting authority here.

2026 remains reserved, no external data imported, no research scripts or framework changes. Reference source remains intact. The causal probability recipe is separately closed as genuine economic abstention; its zero trades were not used to choose this gate's fixed partitions.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_W_PROTOCOL_20261021.md
SHA256 6ab0ad4a3235a1228057cfd9fade8dca40dbb21d94970d511b9ee5887e2b6afa, 20631 caracteres.

```markdown
# BTC Discovery W — dos pasajes con barreras competidoras: estado observado frente a tipo

## Estado y pregunta previa
2026-10-21. Root aprobó posteriormente IMPLEMENTACIÓN y checks sintéticos únicamente. CERO drafts/economía o consultas de velas observadas. Nombres BtcResearchR23PassageBase1m/BtcResearchR23PassageState1m/BtcResearchR23PassageType1m. Revisión root e independiente de fuentes/check antes de borradores. Diseño fijado antes del resultado económico V; no depende de su PnL. Guardar este archivo no autoriza motores ni obliga a gastar presupuesto.

Pregunta: ¿añadir FAST/SLOW observado al tipo REV/CONT de un episodio causal de dos pasajes mejora una predicción BTC24h frente al tipo solo, manteniendo las mismas etiquetas/eventos/admisibilidad/costos/gestión? Es comparación predictiva de políticas y representación del estado observado, NO velocidad pura, causalidad económica, información temporal aislada, test de significancia ni promesa de rentabilidad.

El mecanismo permite que después del primer pasaje compitan retorno y continuación. Así cambia estructuralmente la condición de terminación frente a esperar exclusivamente retorno. No añadir TTL, corte diario, otra resolución ni filtros de overshoot para fabricar eventos/muestra. No garantiza terminación si el precio permanece dentro de bandas; incompletos se conservan como censurados, no SLOW. Las propuestas previas de ancla indefinida o reseteo diario fueron descartes de diseño, no nuevas económicas W que se oculten.

## Inventario exacto y cierres
Se leyeron completos por MCP los nueve textos de fuentes siguientes; CODES completo y hashes guardados ANTES de cualquier implementación:
- BtcResearchR10Base4h: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9
- BtcResearchR11Base1m: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87
- BtcResearchR12ArBase1m: 1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343
- R20PaxgStaircase4h: 9a2a8cda79a41ea1839c46757495e910a4ef18ff9361c29879ce6f0cb050e8c0
- R20PaxgDirectionalOvershoot1h: b422f3ecf6dc7f66fccce8bba0e25e3d83df0e14c724dc408b530a9db7f9ca90
- R40SpyRepeatedBarrierPressure: 01d84640b6d7accfcf259526d35015cd99aa2e881481d955bb9e49aaf90622da
- R40SpyRunDurationResponse: 4d3460d0924855009f3da18e4a871205921716a3e5e818e379c88c1bf8a04907
- AngleBtcProbability4h: d4add40c46e6c46210e77b976e93759da8ee368d182ec5343c453a7dc7ab47c1
- AngleCombinedBtcEventClock1m: 038554637216a164f0e16b6f01d5063fc78cc70442cea34ee324979c7f92cb70

Diferencias:
- R20PaxgStaircase4h: seis cambios monotónicos, límites individuales .75ATR y avance1.5ATR; no dos pasajes/duración relativa.
- R20PaxgDirectionalOvershoot1h: extremos móviles y umbral2ATR congelado por fase; no ancla absoluta con retorno o2d competidores. PAXG, no resultado BTC trasladable.
- AngleCombinedBtcEventClock1m: cambios1ATR desde extremos M1 para habilitar shorts filtrados de una cartera; descartada y no ajustar amplitud/ATR/STOP/inicialización/timeout/años. W no modifica esa fuente ni receta.
- R40SpyRepeatedBarrierPressure: dos pruebas de una barrera, retrocesos y breakout con caducidad; no competencia de barreras ni media aprendida por tiempos.
- R40SpyRunDurationResponse: signo/longitud de racha diaria cap4,252 casos,shrink20; antecedente de aprendizaje sobre duración, no equivalente exacto. No declarar nueva la idea genérica de aprender por estado.
- AngleBtcProbability4h: cuatro estados por dos signos,labels stop3ATR/4h/costos/haircut y gate1SE. Negativo con aprendizaje completo y cero señales; cierre prohíbe relajar gate, retirar fricción o añadir control incondicional para fabricar trades. W no rescata ese modelo; tiene estado/evento y contraste por tipo distintos, sin borrar su antecedente.
- R/G/S/V tienen modelos/targets/inputs y cierres propios; W no cambia sus ventanas/horizontes/regularización ni retira componentes/lados.

Cierres completos consultados/guardados:
- strategies/AngleBtcProbability4h/reports/ANGLE_BTC_PROBABILITY_PROTOCOL_20261018.md
- strategies/AngleBtcProbability4h/reports/ANGLE_BTC_PROBABILITY_INITIAL_RESULT_20261018.md
- strategies/MultiAssetRetestBtcShort4h/reports/BTC_NEW_ANGLES_RESULTS_20261018.md

Dashboards históricos, no corridas nuevas W:
http://localhost:9200/#/backtest/ab8e72a8-f81f-41d8-8d95-8681d27e1b9c
http://localhost:9200/#/backtest/f58458c2-605a-41b4-af24-45712590c967

No equivalente exacto encontrado en inventario acotado; no afirmar censo universal ni independencia respecto a búsqueda global. 2020–25 ampliamente explorado: desarrollo adaptativo, no OOS limpio. No inferir fracaso de toda duración/estructura ni aprobar W por obligación.

## Datos y reloj
BTC-USDT Binance Perpetual Futures, una ruta trading1m para ejecución/observador y data-only BTC4h. Sin ETH u otros activos. Datos existentes, ninguna importación/feed nuevo, preinspección de cobertura, get_candles por herramientas, exportación ni2026 económico nuevo. No scripts o backtests anidados. El motor es autoridad de faltantes: registrar limitación y detener/evaluar insuficiencia, sin importar ni ampliar warmup por PnL.

B=14.400.000ms; decisiones/eventos sólo cierres UTC4h T. Excluir toda vela con open+B>T; últimaopen=T-B. OHLC finito/positivo/coherente, timestamps consecutivos/alineados UTC; no interpolación ni sustitución de filas inválidas por otras más viejas. Close BTC4h coincide con precio route1m actual con tolerancia técnica heredada R12AR. Volumen/funding no son features ni filtros.

Warmup fijo1000 del mayor timeframe4h. La cobertura/retención1000 previa NO está acreditada: no consultar datos para demostrarla antes del motor. Primer T4h con EXACTAS últimas1000 filas cerradas consecutivas válidas permite bootstrap. Si aún no hay ventana válida1000, cash; no usar1000 últimas válidas dispersas ni ampliar lookback. Una vez bootstrap efectuado, no volver a hacerlo aunque haya gaps: recuperación requiere formar nuevos eventos/labels online.

## ATR, guard físico y máquina causal exacta
ATR14 SIMPLE conocida al cerrar T: media de14 true ranges de15OHLC consecutivas, cada TR respecto a su cierre anterior. Reutilizar atr14 de R10 para matemática/modelo y sizing; NO taATR Wilder ni memoria retrospectiva de extremos. Ancla nueva sólo si a=C_T finito>0,d=ATR_T finita>0 y referencias a-2d y a+2d finitas estrictamente positivas. Guard físico sin buffer/epsilon ni filtro económico. Si ATR/guard impide ancla, mantener máquina sin ancla e intentar iniciar una en un cierre posterior válido, sin evento; no borrar banco por sólo ese guard. Protecciones/deadlines de posiciones reales siguen activos.

Estado inicial de episodio: a,d,T0 congelados. Al crear ancla no procesar un cruce en ese mismo cierre.

Primer pasaje, cada cierre posterior T>T0:
- Si a-d<C_T<a+d, esperar.
- Primer C_T>=a+d establece s=+1;primer C_T<=a-d establece s=-1, fecha T1=T.
- Si ese primer cruce ya cumple s*(C_T-a)>=2d, incluido exactamente2d, episodio DEGENERADO: no evento,no label/no FAST/SLOW. Intentar reset ancla en C_T con ATR actual/guard; no procesar de nuevo ese mismo cierre.
- Si d<=s*(C_T-a)<2d, guardar s,T1 y u=T1-T0>0. Congelar a,d: no moverlos a extremos ni ajustar con ATR posterior.

Segundo pasaje, sólo cierre T>T1:
- Si s*(C_T-a)<=0: tipoREV,r=-s.
- Si s*(C_T-a)>=2d: tipoCONT,r=s.
- Si0<s*(C_T-a)<2d: esperar.
Las dos barreras no se satisfacen simultáneamente con d>0. Evento observado completo en T2=T: v=T2-T1>0,fast=(v<u),igualdad v==u =>SLOW. Usar tiempos enteros/bar count, sin interpolar cruce intrabar, ni high/low para fabricar T1/T2, ni dos eventos en un cierre.

Después de completar: guardar evento y reset a=C_T2,d=ATRactual si válido,para procesar recién un cierre posterior. Si nueva ATR/guard inválido queda sin ancla; no reclasificar el evento previo ni alterar su pending label por ese solo motivo. Cada episodio usa d conocida en su propio T0, y el siguiente usa nueva escala. Ninguna cola de señales reales por incompletos.

Overshoots se aceptan/declararán como precios observados de cierres: primer cruce no degenerado puede superar d, segundo puede superar a o2d. No ejecutar trades en barreras históricas ni interpolar un fill en ellas. Si REV cruza mucho más allá de a, sigue siendo REV de ese episodio; el reset no cuenta como otro pasaje.

## Bootstrap matemático UNA vez
En el primer T4h admisible con1000 filas exactas, índices0…999, todos cierres<=T:
1. Rows0…14 suministran las15OHLC de la primera ATR. Intentar primera ancla en close_time(row14), usando sólo rows0…14.
2. Replay cronológico rows15…999, UNA nueva barra por paso y mismas reglas de máquina/ATR causal que runtime. Para ATR de rowj usar rows[j-14:j+1],sin mirar posteriores.
3. Madurar etiquetas previas antes del evento de cada paso. Sólo labels cuyo deadline<=tiempo de ese paso pueden entrar al banco. Al terminar, todos labels en banco están realmente conocidos en T.
4. Mantener máquina/pendientes/banco producidos por replay y último timestamp procesado. NO emitir órdenes ni señales negociables durante replay ni en T de inicialización. Aunque el último row complete evento y banco ya tenga240, ese evento es bootstrap no negociable; su label puede quedar pending matemático.
5. Primer evento negociable debe completarse en T posterior al T de inicialización; no encolar el de inicialización para cuando quede flat.

No entrenamiento precalculado desde futuro, replay financiero, órdenes ficticias, simulación de cuenta o backtest anidado. Sólo características/labels matemáticas con cierres ya disponibles. Todo cash inicial real permanece en calendario/R11. El máximo de eventos es limitado por mínimo dos cierres por episodio y burn-inATR;1000 filas no garantizan240 labels ni20 casos por celda.

Después del bootstrap procesar exactamente una barra NUEVA por T4h, con timestamp estrictamente creciente; no reprocesar barras, reiniciar desde ventana móvil1000 ni consultar pasado para rellenar banco. Ventanas auxiliares de15OHLC sólo sirven a la ATR/validación actual. Un gap o timestamp repetido/atrasado/invalidez se maneja según reset común, no continuación artificial.

## Labels y reset de integridad
Cada evento completo e=(T2,type,fast,r,C_T2,a,d,u,v) genera pending con deadline=T2+6B y seis barras futuras requeridas, no un resultado inmediato. Degenerados/incompletos no generan pending. Al llegar seis cierres futuros consecutivos válidos:
y_e=r*[log(C_(T2+6B))-log(C_T2)].
Precio bruto sin stop/costos/funding de forecast. No dividir por d ni ATR, no target stop-aware S, no cambio de horizonte, no ajustar etiqueta porque se habría cerrado un trade real. Label no es trade ni retorno de cuenta.

En cada nuevo T4h, madurar pendientes antiguas ANTES de crear evento actual. Un label con deadline==T es conocido y puede entrenar forecast actual. Evento actual entra sólo a pending hastaT+6B y jamás entrena su propio forecast. Maduración no se adelanta por tocar alguna barrera o stop real. Pendientes conservan origen/precio/r/tipo/celda; nada se reetiqueta por refit.

Cada label exige las seis futuras barras consecutivas válidas, no sólo target final. Ante gap/OHLC inválido/asof desalineado: reset COMÚN de máquina, pendientes y banco de ambos modelos,neutralidad/cash nuevas entradas. No clasificar gaps como SLOW, no imputar label,guardar banco anterior,backfill con casos viejos ni replay del bootstrap. Recuperación: esperar15OHLC válidas consecutivas para ancla nueva y formar online240 labels nuevos. No repetir warmup1000. Stops y timeout de posiciones reales siguen en el motor/reloj4h; invalidar feature no cancela protección ni extiende plazo.

Censura terminal: episodio abierto a FINISH es incompleto/no label,no SLOW; eventos completos con deadline>FINISH quedan pendientes censurados,no entrenan. No consultar2026 para madurarlos. No equivaler número de eventos a número de labels o trades.

## Dos estimadores y dominio COMPARTIDO
Banco rolling de exactamente los últimos240 eventos con labels maduros válidos desde última inicialización/reset; igual orden temporal/labels para ambos modelos. Hasta que tenga240 COMPLETOS,ambos cash. Después,al madurar otro,retirar el más viejo: no extender ventana para llenar celdas. No filtrar por signo,r,subperíodo,PnL,tamaño de overshoot o duración.

Para evento ACTUAL completo con tipo q y fast f:
STATE:media simple de y de los eventos del banco con(type=q,fast=f).
TYPE_CONTROL:media simple de y de todos eventos del MISMO banco contype=q, sin subdividir por fast.
Exigir n_(q,f)>=20 en AMBOS modelos,además banco240/medias finitas y datos comunes; no permitir que TYPE opere mientras STATE carece de soporte. Si falla,ambos cash aunque control tenga más casos por tipo. No rellenar20 con observaciones fuera de las240. Muestreo/validez idénticos, pero señales/ocupación/capital posteriores pueden diferir.

Sin shrinkage,SE,prior,regresión,kNN,pesos,regímenes,SEgate o modelsearch. El control por tipo evita confundir una mezcla distinta REV/CONT con el añadidoFAST; no usar GLOBAL de ambos tipos como sustituto ni ganador adicional.

Para CADA modelo: scoreBTC=r_actual*media_label. Score>.0019 LONG;score<-.0019 SHORT;igualdad/banda[-.0019,.0019]cash. Esto preserva orientación: media_label positiva significa seguir segundo pasaje r;negativa ir contra él. No interpretar media positiva directamente como long. r sólo es signo observado del segundo pasaje; sin dirección futura.

El hurdle.0019 es regla fija de señal heredada,NO fee extra debitado en PnL ni garantía de rentabilidad. Calcular/consumir evento aun ocupado/pendiente/sameexit; no esperar a quedar flat, encolar,reversa ni entrar tras salir de posición en el mismo T. No nuevo forecast entre eventos sólo porque una label madura o cuenta queda libre. Todos usan calendario/M1observer; decisión económica sólo al evento completo posterior al bootstrap.

## Ejecución, gestión y cuenta congelados
BTC individual,10k,2%por operación/6%agregado/3x aislado;una posición,sin pirámides. Ventana[2020-10-15,2026-01-01)UTC;START<decisión<FINISH. FundingBTC históricoON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 aplicado/verificado,marcasproxy declaradas. Fee.00045porlado takerdescuento,slippage aplicado0. Sin variantes riesgo/comisiones ni estrés; sin reservas legacy.001/LOT.001 deU/P por accidente.

Reutilizar entry_plan R10 y on_open/update_position R12AR,observador/cierre R11 SINCAMBIOS:
- Capitalmax(0,balance)flat,available_margin,feeaware2%,margen90%/floor8.
- MARKET precioBTC actual conocido,enT2,NO precio barrera a/2d.
- SL inicial2ATR14SIMPLE BTC ACTUAL de15OHLC enT2,congelado desde plan y relativo al fill real. D del ancla antigua sólo feature,NO distancia de stop si escala actual difiere.
- SinTP/BE/trailing/parciales;timeout24h=6B desde opened_at real,evaluado primeras fronteras4h elegibles;stop brokerM1.
- No guarda de TP ficticio ni ajuste por tipo,fast,duración/forecast;plan inválido=>noentrada,sin alterar banco/máquina.
- Gap/OHLC inválido resetea todo estado predictivo común, sin detener protecciones/deadlines reales. OHLC válido con ATR actual0/None NO impide madurar pending ni procesar episodio con d antigua válida; sólo impide nueva ancla/plan de entrada. Ningún early-return por ATR antes de maduraciones/evento. No heredar TP2R/48h R11 accidentalmente: R12AR override obligatorio.

Labels precio bruto vs ledger real con fees/funding son objetos distintos. Predecir retorno relativo al segundo pasaje no garantiza utilidad con SL/costos o distribución mensual. No corregir target/protección tras PnL.

R11 equitywallet+PnLabierto M1/fills y fronteras00UTC postfunding/predecisión porfase,no agrupación estricta evento por mes;DDM1+fills,no todos extremos intraminuto. Activity/fillcounters reales separados de eventos/labels/replay. Cierre terminal postfee reemplaza PRETERMINAL con FINAL como padre. No modificar framework/config global.

## Telemetría y viabilidad documental
Contadores limitados por etapa bootstrap/runtime y por ventana evaluada: barras válidas/invalid/reset,anclas físicas/ATRrechazadas,primerospasajes,degenerados,REV/CONTFAST/SLOW,empates,censurados,labels pendientes/maduros,banklen/celln,insuficiencia240/20,signals/occupied/sameexit/fills. Guardar en fill real T0/T1/T2,a,d,u/v,r,type,fast,medias/state/type,ncelda/ntipo,bankfirst/last/deadlines,score y SLactual. Historial de eventos no es universo de órdenes hipotéticas. Evitar logporM1;resúmenes bounded y evidencia de fillsreales.

Modelo finito viable con estado de ancla/fase,cola de pendientes madurados por reloj,deque240 y contadores por4celdas/2tipos. Replay1000una vez +procesamiento incremental porbarra,no barridos recursivos del histórico creciente. No necesita MLframework,datos externos,instalaciones o scripts. Estado matemático común debe ser idéntico entre políticas TODA la trayectoria; órdenes/ocupación jamás retroalimentan anclas,features,pendientes o banco. No se implementa nada ahora.

Objeciones que NO se eliminan con filtros:
- T1 puede sobrepasar d sin llegar2d: distancia restanteCONT<d yREV>d. FAST mezcla tiempo,overshoot/distancia,volatilidad y selección;no velocidad pura.
- u=1barra implica siempreSLOW porquev>=1barra;duraciones discretas no comparan oportunidades equivalentes.
- Condicionar porTYPE no aísla efecto causalFAST ni desequilibrios de dirección/regímenes;forecast es descriptivo,score usa orientaciónr.
- Ancla congelada puede quedar vieja;competingbarriers ayudan a terminar tendencias pero no garantizan completitud en rangos. NoTTL/corte diario/resoluciónrescates.
- Ventana240 por EVENTOS cubre tiempo variable;labels24h se solapan y estados persisten,>=20 no da potencia ni ensayos independientes.
- Bootstrap parcial al comenzar1000 puede cambiar trayectoria de anclas frente a historia infinita;su semilla/burn-in están fijados exante,no se escogerán por resultados.

## Verificación futura, presupuesto y gates
Este protocolo requiere revisión root ANTES de código. Si autoriza más tarde: nuevas fuentes separadas,no tocar padres,readback/hash/CODES y revisión independiente;checks temporales suppliedsourceAST/stubs sin imports de estrategias reales/framework/datos observados/backtests anidados. Oráculos sintéticos de barrerasinclusive/deterioro físico,primercruce>=2ddegenerado,unpasoporcierre,REV/CONT ysignos espejo,overshoots,tieSLOW/u1,anclaATRfrozen/nuevadactual;replay1000row14once/nothingatinit/no currentlabel,rolling240full/shared20/typecontrol/score=r*mu;seisconsecutivas/maturitybeforeevent/gapresetall/no backfill;occupiedconsumption/noqueue/sameexit y R10/R11/R12ARSL24h/terminalfee. Registrar todos fallos,fuentes/códigos/checks/versiones,sin claims runtime de fakes.

Presupuesto FUTUROexactamente2económicas STATE/TYPE_CONTROL,máximo2reemplazos exclusivamente técnicosdocumentados,no porPnL. Máximo2backtests globales/1análisispropio coordinado;ninguna sesión/check/draft autorizado por guardar este documento. Root revisa fuentes/check luego antes de manifest/drafts/motores. No vecinos240/20/1000/.0019/d/2d/u-vtie/TTL/resolución/overshoot/horizonte/stop/target/shrink/SE/dirección/riesgo ni aislar REV/CONT/FAST/lados después. Si insuficiente/cerooperaciones no relajar mínimos ni prometer nuevo ensayo.

Gatesr9 para CADA cuenta:CAGRnetobase>=30%,PF>=1.2,DD<=25%(objetivo20%),M65mesesactivoscompletos positivos,Q80completos,mediana mensual calendario>0inclinactivos,netoaritmético sin2mejoresmeses>0,N>=100preliminar operativo sinconfianza/potencia porconteo;aspiración40–50%+/M70. Superarcontrol no basta;control no ganador sustituto automático. NO_CUMPLE alfallar economía;INCONCLUSA si economía favorable sinmedición/suficiencia.

Auditoría futura completa gross-fees+funding=PNLsum=equityfinal-10k a1e-6USDT,funding aplicado/conciliado,2.741.760M1,63intervalos/62meses/20Q yterminalfee. Reportar bootstrap/cash/coverage,completos/parciales,eventosvslabels/trades. Sin promociónoperativa/estrésautomático. Sin nueva economía2026,imports,descargas,live/paper/Pi,install/restart/framework/globalconfig,research_scripts oportfolio. ReportesMCP yHub archivosprimero/índiceúltimo sólo cuando corresponda y se autorice.

## Precisión posterior a revisión root/independiente
ATR actual inválida con OHLC válido es distinta de integridad de datos: pendientes maduran y episodios previamente anclados procesan su cierre con d congelada aunque ATRactual0/None; al completar se puede generar evento/label, pero no nueva ancla ni entrada hasta ATR válida. Gap/OHLC inválido sí borra máquina,pending y banco. Estado matemático idéntico entre modelos durante TODA trayectoria, sin retroalimentación de órdenes/ocupación. Estas precisiones se fijaron antes de fuentes.

```

## Lectura vigente del Hub sin incorporar resultados W

### strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261021-r22/HANDOFF.md
SHA256 04f22045303a8ee5867cb4c9b789ad71feef20f713a8132617df7e3a534fb8f9

```markdown
# Continuidad r22

V cerrada: VAR1533/CAGR−7.342609/PF.967405/DDM166.051916/M25de62/Q7de20; AR1481/CAGR−7.444034/PF.968755/DDM162.035364/M27de62/Q8de20. Medianas y sinbest2 negativas ambas. No candidata ni vecinos de lag/window/horizonte/rcond/regularización/coupling/gestión/lados.11424 admisiones comunes válidas,0invalidwindows. AR FINAL tras terminal;VAR PRETERMINAL ya flat.2741760M1marks/62meses/20Q.

Auditoría4967b36eb26749938cafc6ce0303a1f2 succeeded,3snapshots VAR/AR y G sólo lectura. AR replica G c72b53d8-c986-4131-814b-788cdc0f49e2:1481 filas type/open/close iguales,entry/exit/qty/fee/PNL/funding error0. No evidencia independiente nueva.42 ejecuciones porID desde r9,209legacy aparte,no censo global ni hipótesis independientes. Dos V nuevas terminadas,0fallos/reemplazos/backtests técnicos. Check12grupos materialesPASSprimero/NumPy1.26.4. Fuentes padres intactos. Reporteseach+anchor/accountingcode+job+artefacto persistidos/readback.

W sólo protocolo en preparación agent reversion_history, fijado antes resultadoV,NO fuentes/jobs/drafts/economía. Máquina4h dos pasajes con barreras competidoras ancla a/dATR14simple: primerclose±d, primercruce>=2d degenera/reset sin evento; luego retornoa a o continuacióna+2s*d completaREV/CONT. u/v,fastv<u,overshoot/distancia residual y u1 no-fast impiden interpretación velocidadpura. Score r*media(y),y=r*log(C_T2+24h/C_T2),MODE(type,fast) vs(type),MISMO bancoCOMPLETO240maduros/celdaactual>=20 ambos. Bootstrapúltimos1000closed4h una vez,anchorrow14ATR15,mathonly/ningunatradeeninitT. Luego1barra/4h;madurarlabelsantesnuevoevento;pendinghasta6BAR,exigir6consecutivas.Gap/OHLCinvalid reseteamáquina+pending+banco,no backfill;ATRinvalid no nuevaancla,protecciones siguen. Estado censurado nuncaSLOW. Contratoactual/SL2ATRsimple/noTP24h/R11;warmup1000,dataBTC4h/BTCroute1m,sinimports ni precheckcoverage. Rootdeberevisarprotocolo+antecedentesantescode. Sourceforecastsbrutosfundingledgerreal. Presupuestofuturo2econ+2repl técnicas, aún sin autorización.

Todosmotores/analysisrootterminales,slotslibres. MCPfunciona,sinDockerrestart. Goaltoolesblockedoutageprevio(noAPIresume),usuarioexplicitoreanudó;seguirmanual,nocomplete/noduplicargoal. Objetivo pendiente,continuarautónomo. No estrés/riskvariants/2026/imports/live/paper/Pi.

```

### strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261021-r22/DISCOVERY_RESULTS.md
SHA256 19318495e08784852eb6ecc04d12c6293906dc5245e147f358e39842454c6b36

```markdown
# BTC Discovery V — cierre

Se comparó VAR1 conjunto BTC/ETH con AR1 BTC exacto de G, bajo admisión compartida.242 cierres sincronizados,240 pares maduros,OLS centrado rank2 según NumPy default, seis pasos recursivos con ETH predicho. B usa filas predictor/columnas respuesta; no se usó ETH futuro. Sin regularización, clipping, filtros de estabilidad ni otro horizonte. El contraste comprende ambas ecuaciones y feedback; no aísla causalidad ETH→BTC.

Contrato UTC [2020-10-15,2026-01-01),10k,2%/6%/3x,fee.00045 por lado, funding BTC histórico aplicado/verificado con proxies, slippage0. R10 sizing, stop2ATRsimple, sinTP, timeout24h desde fill en primer cierre4h elegible; R11 M1 intacto. Forecast bruto de precio, no payoff neto. Warmup3004h. Desarrollo observado, no OOS.

|Política|N|CAGR%|PF|DD M1+fills%|Meses activos positivos|Trimestres positivos|Mediana mensual%|Neto sin dos mejores meses|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[VAR](http://localhost:9200/#/backtest/abab7a82-4df9-489a-8528-e5ec8607f43e)|1533|-7.342609|0.967405|66.051916|25/62|7/20|-1.055285|-7652.471521|
|[AR](http://localhost:9200/#/backtest/01af3d1f-a881-468e-ab1a-5b67460591d3)|1481|-7.444034|0.968755|62.035364|27/62|8/20|-2.391767|-8850.377776|

VAR: bruto precio 7490.732181093577; fees 8634.453674758912; funding -2138.403656693383; neto -3282.125150358702; capital final 6717.874849641259. Años completos: {"2021":-6.819840348620643,"2022":-44.175767389881415,"2023":0.6145842419797987,"2024":0.26037308551167815,"2025":-16.66935237168311}. Peor/mejor12m: -48.10335250027398/32.43979210983709%.

AR: bruto precio 8047.125197941238; fees 9127.724066540486; funding -2239.797078290056; neto -3320.395946889291; capital final 6679.604053110798. Años completos: {"2021":-8.48446180932484,"2022":-34.88775759048261,"2023":6.4622502197481335,"2024":-8.9613052825667,"2025":-24.71978011505609}. Peor/mejor12m: -38.69394314966218/28.429765273779537%.

El nuevo control AR reproduce económicamente [G original](http://localhost:9200/#/backtest/c72b53d8-c986-4131-814b-788cdc0f49e2):1481 trades, mismos type/opened_at/closed_at y error0 en entry/exit/qty/fee/PNL/funding por fila, ignorando IDs/nombres. La admisión conjunta fue válida11424 veces en ambas políticas, por lo que no alteró G en esta trayectoria. No se presenta esa reproducción como evidencia independiente ni mejora. Se conservaron las dos ejecuciones nuevas por ID y la replicación se identifica separadamente; no se deduce un número de hipótesis independientes de los conteos.

Auditoría4967b36eb26749938cafc6ce0303a1f2 succeeded con snapshots completos VAR/AR y G sólo lectura: gross−fees+funding=PNLsum=equityfinal−10000,error<1e-6. Artefacto audit.json incluye comparación G. AR usa FINAL tras liquidación terminal; rawopen1 era metadato previo. VAR PRETERMINAL coincide con final sin abiertas.63intervalos/62meses completos/20Q,2741760marcasM1 por cuenta,0invalidwindows; rank/forecasts válidos11424 de11424. DD M1+fills,no extremos intraminuto; corte mensual por fase postfunding/predecisión; mediana incluye inactivos.51ventanas12m solapadas,no independientes.

Check9f08bcad89ec485a8757da1d6650e9be PASS primer intento,12grupos materiales,NumPy1.26.4; padres intactos. Dos económicos completos,0fallos/reemplazos/backtests técnicos. No stress ni variantes de riesgo. N>=100 sólo suficiencia operativa preliminar.

Decisión: NO_CUMPLE ambas, ninguna candidata. La diferencia pequeña de neto no justifica conservar esta dinámica conjunta. Cerrar sin vecinos de240/horizonte/lag/rcond/regularización/clipping/hurdle/lado/estabilidad/gestión/coupling; no aislar segmentos o coeficientes ganadores. Sin nuevas pruebas2026/imports/live/paper/Pi.

42ejecuciones económicas desde r9 por ID; una reproduce trayectoria G ya medida.209legacy V1–V6 aparte, no censo global ni muestras independientes. W sólo protocolo en preparación, fijado antes del resultado V: estado de dos primeros pasajes con barreras competidoras, type+fast frente type. Overshoot y distancia residual impiden llamarlo velocidad pura. Sin fuentes/jobs/drafts/economía W hasta revisión root. Objetivo pendiente, continuar autónomamente.

```

