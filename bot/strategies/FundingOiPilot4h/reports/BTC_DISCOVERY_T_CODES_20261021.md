# T sources before implementation / economics

DOCS.md and bot/AGENTS.md read through the environment as authorized; strategy sources MCP only. No observed candles, jobs or drafts. New source text below is prepared, not yet economically executed. Parent texts read completely by MCP immediately before this preparation. Synthetic checks remain pending slot coordination.

## BtcResearchR10Base4h
SHA256 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9

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
SHA256 be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87

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

## BtcResearchR12ArBase1m
SHA256 1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343

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

## R40PaxgLearnedSeason4h
SHA256 42088a3527f0efd80e1713f11523feca7797a97c789696dfb710d230cfb9181e

```python
import math
from datetime import datetime
from zoneinfo import ZoneInfo
import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta

TRADE_RISK = 0.01
NOTIONAL_CAP = 4.4
SLIPPAGE_RESERVE = 0.001  # Sizing only; fills do not simulate these extra costs.
NEW_YORK = ZoneInfo('America/New_York')
HOUR_MS = 3600000


class R40PaxgLearnedSeason4h(Strategy):
    """PAXG40-02: predeclared price-only development, not independent validation."""

    def _fresh_quote(self, symbol=None):
        symbol = self.symbol if symbol is None else symbol
        c = self.get_candles(self.exchange, symbol, '1m')
        if not len(c) or int(c[-1, 0]) != int(self.time)-60000:
            return None
        price = float(c[-1, 2])
        if not (math.isfinite(price) and price > 0):
            return None
        if symbol == self.symbol and not math.isclose(
                price, float(self.price), rel_tol=1e-10, abs_tol=1e-8):
            return None
        return price

    def _atr(self, c=None):
        c = self.candles if c is None else c
        if len(c) < 30:
            return None
        value = float(ta.atr(c))
        return value if math.isfinite(value) and value > 0 else None

    def _fourhour_atr(self):
        c = self.get_candles(self.exchange, self.symbol, '4h')
        c = c[c[:, 0]+4*HOUR_MS <= int(self.time)]
        return self._atr(c)

    def _local_time(self):
        return datetime.fromtimestamp(int(self.time)/1000, tz=NEW_YORK)

    def _paired_fix(self):
        local = self._local_time()
        if local.weekday() > 4 or local.hour != 16 or local.minute != 0:
            return None
        own, spy = self._fresh_quote(), self._fresh_quote('SPY-USDT')
        if own is None or spy is None:
            return None
        fixes = self.vars.setdefault('paired_fixes', [])
        day = local.date().isoformat()
        if fixes and fixes[-1]['date'] == day:
            return None
        fixes.append({'date': day, 'time': int(self.time), 'own': own, 'spy': spy})
        # Keep paired observations; models exclude the newly appended fixing in training.
        self.vars['paired_fixes'] = fixes[-200:]
        return self.vars['paired_fixes']

    def before(self) -> None:
        if self.vars.get('processed_index') == self.index:
            return
        self.vars['processed_index'] = self.index
        # State and episode consumption run even when a position is open.
        # An occupied event is discarded on the next bar, never queued.
        self.vars['r40_custom_exit'] = False
        self.vars['r40_event'] = self._model_event()

    def _signal(self) -> int:
        if self.vars.get('signal_index') == self.index:
            return self.vars['signal_value']
        self.vars['signal_index'] = self.index
        self.vars['signal_value'] = 0
        event = self.vars.get('r40_event')
        if (self.symbol != 'PAXG-USDT' or not event or self.vars.get('r40_custom_exit')
                or self._fresh_quote() is None):
            return 0
        entry = float(self.price)
        distance = float(event['distance'])
        direction = int(event['direction'])
        if not (math.isfinite(distance) and 0 < distance < entry and direction in (-1, 1)):
            return 0
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        stop = entry-direction*distance
        unit_risk = distance+self.fee_rate*(entry+stop)+SLIPPAGE_RESERVE*entry
        room = min(capital*NOTIONAL_CAP,
                   max(0.0, float(self.leveraged_available_margin)*0.90))
        qty = min(capital*TRADE_RISK/unit_risk, room/entry)
        # Existing PAXG research precision, not proof of native contract lot rules.
        qty = math.floor(qty/0.0001)*0.0001
        if qty <= 0:
            return 0
        self.vars['r40_plan'] = dict(event, qty=qty, entry=entry)
        self.vars['signal_value'] = direction
        return direction

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        self.buy = self.vars['r40_plan']['qty'], self.price

    def go_short(self) -> None:
        self.sell = self.vars['r40_plan']['qty'], self.price

    def should_cancel_entry(self) -> bool:
        # Entries are MARKET; unexpected pending entries cannot persist.
        return True

    def on_open_position(self, order) -> None:
        plan = self.vars['r40_plan']
        self.vars['r40_opened'] = int(self.position.opened_at)
        self.vars['r40_hours'] = float(plan['hours'])
        self.vars['r40_exit_debt'] = False
        # Frozen exit coefficients belong to the actual fill, not later event models.
        self.vars['r40_open_plan'] = dict(plan)
        entry = float(self.position.entry_price)
        direction = 1 if self.is_long else -1
        self.stop_loss = abs(self.position.qty), entry-direction*plan['distance']
        if plan.get('fixed_target') is not None:
            # Kalman price target is a frozen predictive level, never shifted by fill.
            self.take_profit = abs(self.position.qty), plan['fixed_target']
        elif plan.get('tp') is not None:
            self.take_profit = abs(self.position.qty), entry+direction*plan['tp']

    def update_position(self) -> None:
        elapsed = int(self.time)-self.vars['r40_opened']
        due = elapsed >= self.vars['r40_hours']*HOUR_MS
        due = due or self.vars.get('r40_custom_exit', False) or self.vars.get('r40_exit_debt', False)
        # A stale quote cannot erase an already-triggered model or time exit.
        self.vars['r40_exit_debt'] = bool(due)
        if due and self._fresh_quote() is not None:
            self.liquidate()

    def _regime_event(self, key, state):
        prior = self.vars.get(key, 0)
        self.vars[key] = state
        return bool(state and state != prior)

    def _event(self, direction, atr, hours, stop=2.0, target=None, **extra):
        if atr is None or not math.isfinite(atr) or atr <= 0:
            return None
        event = dict(direction=int(direction), distance=stop*atr, hours=hours)
        if target is not None:
            event['tp'] = target*atr
        event.update(extra)
        return event

    def _aggregate(self, c, span, offset=0):
        # Only exact, contiguous complete OHLC blocks enter higher-timeframe features.
        groups = {}
        for row in c:
            ts = int(row[0])
            bucket = ((ts-offset)//span)*span+offset
            if bucket+span <= int(self.time):
                groups.setdefault(bucket, []).append(row)
        out = []
        expected = span//(4*HOUR_MS)
        for ts, rows in sorted(groups.items()):
            if len(rows) != expected:
                continue
            a = np.asarray(rows)
            if not np.array_equal(a[:, 0], ts+np.arange(expected)*4*HOUR_MS):
                continue
            out.append([ts, a[0, 1], a[-1, 2], np.max(a[:, 3]),
                        np.min(a[:, 4]), np.sum(a[:, 5])])
        return np.asarray(out, dtype=float).reshape((-1, 6))

    def _model_event(self):
        """Ninety mature labels per UTC bucket estimate a rolling season. Top/bottom ranking uses all buckets and freezes at midnight."""
        c = self.candles
        now = datetime.fromtimestamp(int(self.time)/1000, tz=ZoneInfo('UTC'))
        if now.hour == 0 and len(c) >= 541:
            # Mature close-to-close labels align with the previous close entry.
            values = {h: [] for h in (0, 4, 8, 12, 16, 20)}
            # Collect the latest 90 VALID observations per bucket, without an arbitrary bar cap.
            for i in range(len(c)-1, 0, -1):
                if int(c[i, 0]-c[i-1, 0]) != 4*HOUR_MS:
                    continue
                h = datetime.fromtimestamp(int(c[i, 0])/1000,
                                           tz=ZoneInfo('UTC')).hour
                if h in values and len(values[h]) < 90 and c[i, 2] > 0 and c[i-1, 2] > 0:
                    values[h].append(math.log(c[i, 2]/c[i-1, 2]))
                if all(len(v) >= 90 for v in values.values()):
                    break
            if all(len(v) >= 90 for v in values.values()):
                means = {h: float(np.mean(v[-90:])) for h, v in values.items()}
                if max(means.values()) > min(means.values()):
                    best = sorted(means, key=lambda h: (-means[h], h))[0]
                    worst = sorted(means, key=lambda h: (means[h], h))[0]
                    self.vars['season_rank'] = (now.date().isoformat(), best, worst, means)
        rank = self.vars.get('season_rank')
        if not rank or rank[0] != now.date().isoformat():
            return None
        _, best, worst, means = rank
        direction = 1 if now.hour == best and means[best] > 0 else (
            -1 if now.hour == worst and means[worst] < 0 else 0)
        return self._event(direction, self._atr(), 4) if direction else None

```

## BtcResearchR20SeasonBase1m
SHA256 101e8cb82259af2b303275c19c0810b35a4cd9e5f9210f559df95ba51b39742c

```python
import math

import numpy as np
from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, DAY, closed_window, atr14, entry_plan


def season_model(candles, now):
    """Exactly90 complete UTC days; bin is interval START, not close hour."""
    if now % DAY:
        return None
    rows = closed_window(candles, now, 541)
    if rows is None or not np.all(rows[:, 0] % BAR == 0):
        return None
    labels = np.diff(np.log(rows[:, 2]))
    phases = ((rows[1:, 0].astype(np.int64) % DAY) // BAR)
    counts = [int(np.sum(phases == k)) for k in range(6)]
    if counts != [90] * 6 or not np.all(np.isfinite(labels)):
        return None
    means = [float(np.mean(labels[phases == k])) for k in range(6)]
    global_mean = float(np.mean(labels))
    if not all(math.isfinite(v) for v in means + [global_mean]):
        return None
    return dict(day=int(now), phase_means=means, global_mean=global_mean,
                counts=counts, labels=540,
                first_origin=int(rows[1, 0]), last_target=int(rows[-1, 0]) + BAR)


def season_forecast(model, now, phase_policy):
    """A valid midnight snapshot is immutable for its own UTC day only."""
    if model is None or not model["day"] <= now < model["day"] + DAY:
        return None
    if now % BAR:
        return None
    k = int((now % DAY) // BAR)
    value = model["phase_means"][k] if phase_policy else model["global_mean"]
    return float(value) if math.isfinite(value) else None


class BtcResearchR20SeasonBase1m(BtcResearchR12ArBase1m):
    """Phase-conditioned mean versus global mean; R11 M1 accounting intact."""
    MODE = "abstract"

    def _season_invalidate(self, reason):
        self.vars["season_model"] = None
        if self.START <= int(self.time) < self.FINISH:
            counts = self.vars.setdefault("season_invalidations", {})
            counts[reason] = counts.get(reason, 0) + 1

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate - .00045) < 1e-12
            assert abs(self.balance - 10000) < 1e-6
            assert self.MODE in ("PHASE", "GLOBAL")
            self.vars["checked"] = True
            self._log("R20_SEASON_CONFIG", dict(mode=self.MODE, labels=540,
                      days=90, bins=6, per_bin=90, freeze="00UTC",
                      horizon_hours=4, stop_atr=2, target=None,
                      risk=.02, aggregate=.06, leverage=3, fee=.00045))
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR or not self.START <= now < self.FINISH:
            return
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        rows = closed_window(candles, now, 15)
        if rows is None or not np.all(rows[:, 0] % BAR == 0):
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            self._season_invalidate("decision_ohlc")
            return
        if not math.isclose(float(rows[-1, 2]), float(self.price),
                            rel_tol=1e-10, abs_tol=1e-8):
            self._season_invalidate("asof_price")
            return
        if now % DAY == 0:
            model = season_model(candles, now)
            if model is None:
                self._season_invalidate("midnight_window")
            else:
                self.vars["season_model"] = model
                self.vars["season_freezes"] = self.vars.get("season_freezes", 0) + 1
        model = self.vars.get("season_model")
        forecast = season_forecast(model, now, self.MODE == "PHASE")
        atr = atr14(rows)
        if atr is None:
            self._season_invalidate("atr")
            return
        if forecast is None or abs(forecast) <= .0019 or not self.START < now:
            return
        self.vars["signals"] = self.vars.get("signals", 0) + 1
        # Occupied margin is irrelevant to model validity; discard, never queue.
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0) + 1
            return
        price = float(self.price)
        capital = max(0., float(self.balance))
        margin, leverage, fee = (float(self.available_margin),
                                 float(self.leverage), float(self.fee_rate))
        # Both directions share ex-ante admissibility at the SAME flat account.
        # No fictitious profit target or additional physical buffer is imposed.
        plans = {side: entry_plan(price, capital, margin, leverage, fee, side, 2*atr)
                 for side in (1, -1)}
        if any(p is None or not math.isfinite(p["qty"]) or p["qty"] <= 0
               for p in plans.values()):
            self.vars["season_plan_rejections"] = self.vars.get("season_plan_rejections", 0) + 1
            return
        if plans[1]["stop"] <= 0:
            return
        direction = 1 if forecast > 0 else -1
        self.vars["direction"] = direction
        self.vars["plan"] = plans[direction]
        self.vars["season_evidence"] = dict(
            freeze=model["day"], phase=int((now % DAY)//BAR),
            forecast=forecast, global_mean=model["global_mean"],
            phase_means=list(model["phase_means"]), counts=list(model["counts"]),
            first_origin=model["first_origin"], last_target=model["last_target"])

    def on_open_position(self, order):
        super().on_open_position(order)
        self._log("R20_SEASON_OPEN", dict(time=int(self.time),
                  direction=1 if self.is_long else -1,
                  entry=float(self.position.entry_price),
                  evidence=self.vars["season_evidence"]))

    def update_position(self):
        # Parent AR holds6BAR. T's preregistered forecast/timeout are BOTH1BAR;
        # protective stop remains M1 and no other exit rule is changed.
        if int(self.time) % BAR == 0 and int(self.time)-int(self.position.opened_at) >= BAR:
            self.liquidate()

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R20_SEASON_STATS", dict(stage=stage,
                  freezes=self.vars.get("season_freezes", 0),
                  invalidations=self.vars.get("season_invalidations", {}),
                  occupied=self.vars.get("occupied", 0),
                  plan_rejections=self.vars.get("season_plan_rejections", 0)))
```

## BtcResearchR20SeasonPhase1m
SHA256 0e060208a7346413cb65f28d668074a999b629a543b8834ff2ae9e38077441ec

```python
from strategies.BtcResearchR20SeasonBase1m import BtcResearchR20SeasonBase1m


class BtcResearchR20SeasonPhase1m(BtcResearchR20SeasonBase1m):
    MODE = "PHASE"
```

## BtcResearchR20SeasonGlobal1m
SHA256 062d9ac4382fc734005d1995b4e3cbc8cceb195e9f685d62db6f3f6df097b5f6

```python
from strategies.BtcResearchR20SeasonBase1m import BtcResearchR20SeasonBase1m


class BtcResearchR20SeasonGlobal1m(BtcResearchR20SeasonBase1m):
    MODE = "GLOBAL"
```
