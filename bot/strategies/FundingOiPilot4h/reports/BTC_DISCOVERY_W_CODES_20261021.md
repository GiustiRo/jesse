# W — complete source and closure inventory before implementation

2026-10-21. Protocol/documentary feasibility only. No new strategy sources, jobs, drafts, economics or observed candle queries. Frozen before V economics are known to this agent. DOCS.md/bot AGENTS previously read from authorized environment; strategy/report sources MCP only. Exact full source texts read by MCP below. Hashes refer to these texts, not Rust/framework runtime implementations. Negative Angle/eventclock closures preserved; W is not permission to reopen them.

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

## R20PaxgStaircase4h
SHA256 9a2a8cda79a41ea1839c46757495e910a4ef18ff9361c29879ce6f0cb050e8c0

```python
import math
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta

TRADE_RISK = 0.01
NOTIONAL_CAP = 4.4
SLIPPAGE_RESERVE = 0.001  # Sizing only; fills do not simulate these extra costs.
FEE_FORECAST_HURDLE = 0.0019  # Fixed 9 bps modeled round trip plus 10 bps reserve.
NEW_YORK = ZoneInfo('America/New_York')
HOUR_MS = 3600000


class R20PaxgStaircase4h(Strategy):
    """PAXG20-07: predeclared price-only development, not independent validation."""

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
        # These models need at most 22 observations; retain a wider history for gaps.
        self.vars['paired_fixes'] = fixes[-200:]
        return self.vars['paired_fixes']

    def before(self) -> None:
        if self.vars.get('processed_index') == self.index:
            return
        self.vars['processed_index'] = self.index
        # State and episode consumption run even when a position is open.
        # An occupied event is discarded on the next bar, never queued.
        self.vars['r20_event'] = self._model_event()

    def _signal(self) -> int:
        if self.vars.get('signal_index') == self.index:
            return self.vars['signal_value']
        self.vars['signal_index'] = self.index
        self.vars['signal_value'] = 0
        event = self.vars.get('r20_event')
        if self.symbol != 'PAXG-USDT' or not event or self._fresh_quote() is None:
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
        self.vars['r20_plan'] = dict(event, qty=qty, entry=entry)
        self.vars['signal_value'] = direction
        return direction

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        self.buy = self.vars['r20_plan']['qty'], self.price

    def go_short(self) -> None:
        self.sell = self.vars['r20_plan']['qty'], self.price

    def should_cancel_entry(self) -> bool:
        # Entries are MARKET; unexpected pending entries cannot persist.
        return True

    def on_open_position(self, order) -> None:
        plan = self.vars['r20_plan']
        self.vars['r20_opened'] = int(self.position.opened_at)
        self.vars['r20_hours'] = float(plan['hours'])
        self.vars['r20_month_exit'] = bool(plan.get('month_exit', False))
        self.vars['r20_open_month'] = self._local_time().strftime('%Y-%m')
        self.vars['r20_exit_fixings'] = 0
        entry = float(self.position.entry_price)
        direction = 1 if self.is_long else -1
        self.stop_loss = abs(self.position.qty), entry-direction*plan['distance']
        if plan.get('tp') is not None:
            self.take_profit = abs(self.position.qty), entry+direction*plan['tp']

    def update_position(self) -> None:
        elapsed = int(self.time)-self.vars['r20_opened']
        due = elapsed >= self.vars['r20_hours']*HOUR_MS
        if self.vars.get('r20_month_exit'):
            due = due or self.vars.get('r20_exit_fixings', 0) >= 3
        if due and self._fresh_quote() is not None:
            self.liquidate()

    def _model_event(self):
        c = self.candles
        if len(c) < 37:
            return None
        changes = np.diff(c[-7:, 2].astype(float))
        latest = 1 if changes[-1] > 0 else (-1 if changes[-1] < 0 else 0)
        consumed = self.vars.get('stair_consumed_sign', 0)
        if consumed and latest and latest != consumed:
            consumed = 0
            self.vars['stair_consumed_sign'] = 0
        atr = self._atr(c[:-6])
        if atr is None:
            return None
        sign = 1 if np.all(changes > 0) else (-1 if np.all(changes < 0) else 0)
        if not sign or consumed == sign:
            return None
        if np.any(np.abs(changes) > 0.75*atr) or abs(float(changes.sum())) < 1.5*atr:
            return None
        self.vars['stair_consumed_sign'] = sign
        return {'direction': sign, 'distance': 2*atr, 'tp': 3*atr, 'hours': 24}

```

## R20PaxgDirectionalOvershoot1h
SHA256 b422f3ecf6dc7f66fccce8bba0e25e3d83df0e14c724dc408b530a9db7f9ca90

```python
import math
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta

TRADE_RISK = 0.01
NOTIONAL_CAP = 4.4
SLIPPAGE_RESERVE = 0.001  # Sizing only; fills do not simulate these extra costs.
FEE_FORECAST_HURDLE = 0.0019  # Fixed 9 bps modeled round trip plus 10 bps reserve.
NEW_YORK = ZoneInfo('America/New_York')
HOUR_MS = 3600000


class R20PaxgDirectionalOvershoot1h(Strategy):
    """PAXG20-04: predeclared price-only development, not independent validation."""

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
        # These models need at most 22 observations; retain a wider history for gaps.
        self.vars['paired_fixes'] = fixes[-200:]
        return self.vars['paired_fixes']

    def before(self) -> None:
        if self.vars.get('processed_index') == self.index:
            return
        self.vars['processed_index'] = self.index
        # State and episode consumption run even when a position is open.
        # An occupied event is discarded on the next bar, never queued.
        self.vars['r20_event'] = self._model_event()

    def _signal(self) -> int:
        if self.vars.get('signal_index') == self.index:
            return self.vars['signal_value']
        self.vars['signal_index'] = self.index
        self.vars['signal_value'] = 0
        event = self.vars.get('r20_event')
        if self.symbol != 'PAXG-USDT' or not event or self._fresh_quote() is None:
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
        self.vars['r20_plan'] = dict(event, qty=qty, entry=entry)
        self.vars['signal_value'] = direction
        return direction

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        self.buy = self.vars['r20_plan']['qty'], self.price

    def go_short(self) -> None:
        self.sell = self.vars['r20_plan']['qty'], self.price

    def should_cancel_entry(self) -> bool:
        # Entries are MARKET; unexpected pending entries cannot persist.
        return True

    def on_open_position(self, order) -> None:
        plan = self.vars['r20_plan']
        self.vars['r20_opened'] = int(self.position.opened_at)
        self.vars['r20_hours'] = float(plan['hours'])
        self.vars['r20_month_exit'] = bool(plan.get('month_exit', False))
        self.vars['r20_open_month'] = self._local_time().strftime('%Y-%m')
        self.vars['r20_exit_fixings'] = 0
        entry = float(self.position.entry_price)
        direction = 1 if self.is_long else -1
        self.stop_loss = abs(self.position.qty), entry-direction*plan['distance']
        if plan.get('tp') is not None:
            self.take_profit = abs(self.position.qty), entry+direction*plan['tp']

    def update_position(self) -> None:
        elapsed = int(self.time)-self.vars['r20_opened']
        due = elapsed >= self.vars['r20_hours']*HOUR_MS
        if self.vars.get('r20_month_exit'):
            due = due or self.vars.get('r20_exit_fixings', 0) >= 3
        if due and self._fresh_quote() is not None:
            self.liquidate()

    def _model_event(self):
        atr = self._atr()
        if atr is None:
            return None
        price = float(self.price)
        state = self.vars.get('dc_state')
        if state is None:
            self.vars['dc_state'] = {'direction': 0, 'extreme': price, 'h': 2*atr}
            return None
        direction, extreme, h = state['direction'], state['extreme'], state['h']
        new_direction = None
        if direction == 0:
            if price >= extreme+h:
                new_direction = 1
            elif price <= extreme-h:
                new_direction = -1
        elif direction == 1:
            extreme = max(extreme, price)
            if price <= extreme-h:
                new_direction = -1
        else:
            extreme = min(extreme, price)
            if price >= extreme+h:
                new_direction = 1
        if new_direction is None:
            state['extreme'] = extreme
            return None
        # The event uses the old, precommitted threshold; the next leg gets a new H.
        self.vars['dc_state'] = {'direction': new_direction, 'extreme': price, 'h': 2*atr}
        return {'direction': new_direction, 'distance': h, 'tp': 2*h, 'hours': 24}

```

## R40SpyRepeatedBarrierPressure
SHA256 01d84640b6d7accfcf259526d35015cd99aa2e881481d955bb9e49aaf90622da

```python
import math
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

NY = ZoneInfo('America/New_York')
MINUTE = 60000
HALF = 30 * MINUTE
RISK = 0.01
GROSS = 4.4
RESERVE = 0.001  # Sizing reserve only; fills do not include this slippage.
HURDLE = 0.0019  # 9bps modeled roundtrip fee plus10bps reserve, fixed before results.


class R40SpyRepeatedBarrierPressure(Strategy):
    """R40 price experiment with daily sessions and closed2h RTH blocks.

    Absences are not imputed. Complete M1 timestamps do not certify the
    upstream provider's treatment of gaps. No volume or live parity is inferred.
    """

    def trading_hours(self):
        return {'timezone': 'America/New_York', 'hours': {'Mon-Fri': '09:30-16:00'}}

    @property
    @cached
    def session_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    @staticmethod
    def _local(stamp):
        return datetime.fromtimestamp(stamp/1000, timezone.utc).astimezone(NY)

    @staticmethod
    def _civil_previous(day):
        d = datetime.fromisoformat(day).date()
        return (d-timedelta(days=3 if d.weekday() == 0 else 1)).isoformat()

    def _fix(self):
        c = self.get_candles(self.exchange, self.symbol, '1m')
        if not len(c):
            return None
        i = int(np.searchsorted(c[:, 0], self.time-MINUTE, side='right'))-1
        if i < 0 or int(c[i, 0])+MINUTE != int(self.time):
            return None
        price = float(c[i, 2])
        if not math.isfinite(price) or price <= 0:
            return None
        assert math.isclose(price, self.price, rel_tol=1e-10, abs_tol=1e-8), 'R40_PRICE_NOT_FRESH'
        return price

    def _complete_bar(self):
        c = self.get_candles(self.exchange, self.symbol, '1m')
        lo = int(np.searchsorted(c[:, 0], self.closed_candle_open_time, side='left'))
        hi = int(np.searchsorted(c[:, 0], self.time, side='left'))
        b = c[lo:hi]
        return (len(b) == 30 and int(b[0, 0]) == self.closed_candle_open_time
                and int(b[-1, 0])+MINUTE == self.time
                and bool(np.all(np.diff(b[:, 0]) == MINUTE)) and self._fix() is not None)

    @staticmethod
    def _atr(h):
        if len(h) < 15:
            return None
        ranges = [max(v['high']-v['low'], abs(v['high']-p['close']),
                      abs(v['low']-p['close'])) for p, v in zip(h[:-1], h[1:])]
        a = float(np.mean(ranges[-14:]))
        return a if math.isfinite(a) and a > 0 else None

    @staticmethod
    def _entropy(closes):
        counts = {}
        for i in range(len(closes)-2):
            triple = closes[i:i+3]
            if len(set(triple)) != 3:
                return None
            key = tuple(int(v) for v in np.argsort(triple))
            counts[key] = counts.get(key, 0)+1
        total = sum(counts.values())
        entropy = -sum((n/total)*math.log(n/total) for n in counts.values())/math.log(6)
        return {'h': entropy, 'up': counts.get((0, 1, 2), 0), 'down': counts.get((2, 1, 0), 0)}

    def _record_event(self, event):
        if event is not None:
            self.vars['events'] = self.vars.get('events', 0)+1
            if self.is_open:
                self.vars['occupied_events'] = self.vars.get('occupied_events', 0)+1
        self.vars['event'] = event

    def before(self):
        self.vars.update(event=None, phase_exit=False, daily_completed=False)
        self.vars.setdefault('history', [])
        self.vars.setdefault('blocks', [])
        self.vars.setdefault('d_seq', 0)
        self.vars.setdefault('b_seq', 0)
        opened = self._local(self.closed_candle_open_time)
        day = opened.date().isoformat()
        minute = opened.hour*60+opened.minute
        if self.vars.get('session_day') != day:
            self.vars.update(session_day=day, day_bars=[], day_invalid=True,
                             block_key=None, block_rows=[], block_invalid=True)
        if not self.is_trading_hours:
            return
        c = self.session_candles
        if not len(c) or int(c[-1, 0]) != self.closed_candle_open_time:
            return
        # Each2h group has an independent completeness gate. A missing early
        # bar invalidates daily OHLC, not an unrelated complete afternoon block.
        if minute < 930:
            group = (minute-570)//120
            key = (day, group)
            if self.vars['block_key'] != key:
                self.vars.update(block_key=key, block_rows=[],
                                 block_invalid=(minute != 570+120*group))
        if minute == 570:
            self.vars.update(day_bars=[], day_invalid=False)
        if not self._complete_bar():
            self.vars['day_invalid'] = True
            self.vars['block_invalid'] = True
            self.vars['missing_bars'] = self.vars.get('missing_bars', 0)+1
            return
        bar = c[-1].copy()
        day_bars = self.vars['day_bars']
        if day_bars and int(bar[0]-day_bars[-1][0]) != HALF:
            self.vars['day_invalid'] = True
        day_bars.append(bar)
        h = self.vars['history']
        a = self._atr(h)
        if minute == 570 and a:
            self._record_event(self._opening_signal(h, bar, day, a))
        if minute < 930:
            rows = self.vars['block_rows']
            if rows and int(bar[0]-rows[-1][0]) != HALF:
                self.vars['block_invalid'] = True
            rows.append(bar)
            if len(rows) == 4 and not self.vars['block_invalid']:
                block = np.array([rows[0][0], rows[0][1], rows[-1][2],
                                  max(v[3] for v in rows), min(v[4] for v in rows), 0.])
                blocks = self.vars['blocks']
                blocks.append(block)
                self.vars['blocks'] = blocks[-300:]
                self.vars['b_seq'] += 1
                if a:
                    self._record_event(self._block_signal(self.vars['blocks'], h, a))
        decision = self._local(self.time)
        if (decision.hour, decision.minute) != (16, 0) or self.vars['day_invalid'] or len(day_bars) != 13:
            return
        closes = [float(v[2]) for v in day_bars]
        self.vars['d_seq'] += 1
        d = {'day': day, 'time': int(self.time), 'seq': self.vars['d_seq'],
             'open': float(day_bars[0][1]), 'close': closes[-1],
             'high': max(float(v[3]) for v in day_bars),
             'low': min(float(v[4]) for v in day_bars), 'closes30': closes,
             'a_prev': a, 'entropy': self._entropy(closes)}
        previous = h[-1] if h else None
        d['gap'] = (math.log(d['open']/previous['close'])
                    if previous and previous['day'] == self._civil_previous(day) else None)
        d['cash'] = math.log(d['close']/d['open'])
        # The partition telescopes to cash return, including interbar jumps.
        d['intraday_returns'] = np.log(np.array(closes)/np.array([d['open']]+closes[:-1])).tolist()
        change = d['close']-previous['close'] if previous else 0.
        sign = 1 if change > 0 else (-1 if change < 0 else 0)
        run = previous['run']+1 if previous and sign and previous['run_sign'] == sign else (1 if sign else 0)
        d.update(run_sign=sign, run=run)
        h.append(d)
        self.vars['history'] = h[-400:]  # Technical retention exceeds252/180D lookbacks.
        self.vars['daily_completed'] = True
        if a:
            self._record_event(self._daily_signal(self.vars['history'], a))

    def _opening_signal(self, h, bar, day, a):
        return None

    def _block_signal(self, blocks, h, a):
        return None

    def _daily_signal(self, h, a):
        return None

    def _event(self, side, a, hours, target=None, next_daily=False):
        if target is not None and side*(target-self.price) <= 0:
            return None
        distance = 2*a
        if not 0 < distance < self.price:
            return None
        return {'side': side, 'distance': distance, 'hours': hours,
                'target': target, 'next_daily': next_daily}

    def _plan(self):
        event = self.vars.get('event')
        if self.symbol != 'SPY-USDT' or len(self.routes) != 1 or not event or self._fix() is None:
            return 0
        entry = float(self.price)
        stop = entry-event['side']*event['distance']
        capital = max(0., min(float(self.balance), float(self.portfolio_value)))
        unit = event['distance']+self.fee_rate*(entry+stop)+RESERVE*entry
        qty = min(capital*RISK/unit, capital*GROSS/entry,
                  max(0., self.leveraged_available_margin*0.90)/entry)
        qty = math.floor(qty/0.001)*0.001  # Research precision, not venue-lot certification.
        if qty <= 0:
            return 0
        self.vars['plan'] = dict(event, qty=qty)
        return event['side']

    def _signal(self):
        if self.vars.get('signal_index') != self.index:
            self.vars.update(signal_index=self.index, signal=self._plan())
        return self.vars['signal']

    def should_long(self):
        return self._signal() == 1

    def should_short(self):
        return self._signal() == -1

    def go_long(self):
        self.buy = self.vars['plan']['qty'], self.price

    def go_short(self):
        self.sell = self.vars['plan']['qty'], self.price

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        p = self.vars['plan']
        entry = float(self.position.entry_price)
        self.stop_loss = abs(self.position.qty), entry-p['side']*p['distance']
        if p['target'] is not None:
            self.take_profit = abs(self.position.qty), p['target']
        self.vars.update(opened_at=int(self.position.opened_at), hold_ms=p['hours']*3600000,
                         entry_d_seq=self.vars['d_seq'], next_daily=p['next_daily'], exit_debt=False)

    def update_position(self):
        next_day = (self.vars.get('next_daily') and self.vars['daily_completed']
                    and self.vars['d_seq'] > self.vars['entry_d_seq'])
        due = next_day or self.vars.get('phase_exit') or self.time-self.vars['opened_at'] >= self.vars['hold_ms']
        if due:
            self.vars['exit_debt'] = True
        # Debt survives leaving the signal's calendar; stops never switch off.
        if self.vars.get('exit_debt') and self._fix() is not None:
            self.liquidate()

    def _cross_state(self, key, state):
        old = self.vars.get(key, 0)
        self.vars[key] = state
        return state != 0 and state != old

    def _block_signal(self, blocks, h, a):
        if len(blocks) < 11:
            return None
        b = blocks[-1]
        seq = self.vars['b_seq']
        episode = self.vars.get('pressure_episode')
        if episode and seq-episode['seq'] > 12:
            self.vars['pressure_episode'] = None
            episode = None
        if episode is None:
            upper = max(float(v[3]) for v in blocks[-11:-1])
            lower = min(float(v[4]) for v in blocks[-11:-1])
            if not lower <= self.price <= upper:
                return None
            up, down = upper-self.price, self.price-lower
            if up == down or min(up, down) > 0.5*a:
                return None
            side, level = (1, upper) if up < down else (-1, lower)
            used = self.vars.setdefault('pressure_levels', set())
            key = (side, level)
            if key in used:
                return None
            used.add(key)  # Even an expired setup consumes this level/direction.
            self.vars['pressure_episode'] = {
                'seq': seq, 'side': side, 'level': level, 'a': a, 'tests': 0,
                'extreme': float(b[4] if side == 1 else b[3]), 'pressure': False}
            return None
        side, level, frozen = episode['side'], episode['level'], episode['a']
        beyond = side*(self.price-level) > 0
        # Two failed tests must precede the breakout. An earlier close through
        # the barrier invalidates this setup rather than becoming a hidden test.
        if beyond and episode['tests'] < 2:
            self.vars['pressure_episode'] = None
            return None
        extreme = float(b[4] if side == 1 else b[3])
        test = (b[3] >= level-0.1*frozen and self.price <= level if side == 1 else
                b[4] <= level+0.1*frozen and self.price >= level)
        if episode['tests'] == 0:
            episode['extreme'] = min(episode['extreme'], extreme) if side == 1 else max(episode['extreme'], extreme)
            if test:
                episode.update(tests=1, first_extreme=episode['extreme'], last_test=seq, extreme=None)
        elif episode['tests'] == 1:
            previous = episode['extreme']
            episode['extreme'] = (extreme if previous is None else
                                  (min(previous, extreme) if side == 1 else max(previous, extreme)))
            if test and seq-episode['last_test'] >= 2:
                pressure = side*(episode['extreme']-episode['first_extreme']) > 0
                episode.update(tests=2, pressure=pressure, second_test=seq)
        elif episode['pressure'] and seq > episode['second_test'] and beyond:
            self.vars['pressure_episode'] = None
            return self._event(side, frozen, 120)
        return None

```

## R40SpyRunDurationResponse
SHA256 4d3460d0924855009f3da18e4a871205921716a3e5e818e379c88c1bf8a04907

```python
import math
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

NY = ZoneInfo('America/New_York')
MINUTE = 60000
HALF = 30 * MINUTE
RISK = 0.01
GROSS = 4.4
RESERVE = 0.001  # Sizing reserve only; fills do not include this slippage.
HURDLE = 0.0019  # 9bps modeled roundtrip fee plus10bps reserve, fixed before results.


class R40SpyRunDurationResponse(Strategy):
    """R40 price experiment with daily sessions and closed2h RTH blocks.

    Absences are not imputed. Complete M1 timestamps do not certify the
    upstream provider's treatment of gaps. No volume or live parity is inferred.
    """

    def trading_hours(self):
        return {'timezone': 'America/New_York', 'hours': {'Mon-Fri': '09:30-16:00'}}

    @property
    @cached
    def session_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    @staticmethod
    def _local(stamp):
        return datetime.fromtimestamp(stamp/1000, timezone.utc).astimezone(NY)

    @staticmethod
    def _civil_previous(day):
        d = datetime.fromisoformat(day).date()
        return (d-timedelta(days=3 if d.weekday() == 0 else 1)).isoformat()

    def _fix(self):
        c = self.get_candles(self.exchange, self.symbol, '1m')
        if not len(c):
            return None
        i = int(np.searchsorted(c[:, 0], self.time-MINUTE, side='right'))-1
        if i < 0 or int(c[i, 0])+MINUTE != int(self.time):
            return None
        price = float(c[i, 2])
        if not math.isfinite(price) or price <= 0:
            return None
        assert math.isclose(price, self.price, rel_tol=1e-10, abs_tol=1e-8), 'R40_PRICE_NOT_FRESH'
        return price

    def _complete_bar(self):
        c = self.get_candles(self.exchange, self.symbol, '1m')
        lo = int(np.searchsorted(c[:, 0], self.closed_candle_open_time, side='left'))
        hi = int(np.searchsorted(c[:, 0], self.time, side='left'))
        b = c[lo:hi]
        return (len(b) == 30 and int(b[0, 0]) == self.closed_candle_open_time
                and int(b[-1, 0])+MINUTE == self.time
                and bool(np.all(np.diff(b[:, 0]) == MINUTE)) and self._fix() is not None)

    @staticmethod
    def _atr(h):
        if len(h) < 15:
            return None
        ranges = [max(v['high']-v['low'], abs(v['high']-p['close']),
                      abs(v['low']-p['close'])) for p, v in zip(h[:-1], h[1:])]
        a = float(np.mean(ranges[-14:]))
        return a if math.isfinite(a) and a > 0 else None

    @staticmethod
    def _entropy(closes):
        counts = {}
        for i in range(len(closes)-2):
            triple = closes[i:i+3]
            if len(set(triple)) != 3:
                return None
            key = tuple(int(v) for v in np.argsort(triple))
            counts[key] = counts.get(key, 0)+1
        total = sum(counts.values())
        entropy = -sum((n/total)*math.log(n/total) for n in counts.values())/math.log(6)
        return {'h': entropy, 'up': counts.get((0, 1, 2), 0), 'down': counts.get((2, 1, 0), 0)}

    def _record_event(self, event):
        if event is not None:
            self.vars['events'] = self.vars.get('events', 0)+1
            if self.is_open:
                self.vars['occupied_events'] = self.vars.get('occupied_events', 0)+1
        self.vars['event'] = event

    def before(self):
        self.vars.update(event=None, phase_exit=False, daily_completed=False)
        self.vars.setdefault('history', [])
        self.vars.setdefault('blocks', [])
        self.vars.setdefault('d_seq', 0)
        self.vars.setdefault('b_seq', 0)
        opened = self._local(self.closed_candle_open_time)
        day = opened.date().isoformat()
        minute = opened.hour*60+opened.minute
        if self.vars.get('session_day') != day:
            self.vars.update(session_day=day, day_bars=[], day_invalid=True,
                             block_key=None, block_rows=[], block_invalid=True)
        if not self.is_trading_hours:
            return
        c = self.session_candles
        if not len(c) or int(c[-1, 0]) != self.closed_candle_open_time:
            return
        # Each2h group has an independent completeness gate. A missing early
        # bar invalidates daily OHLC, not an unrelated complete afternoon block.
        if minute < 930:
            group = (minute-570)//120
            key = (day, group)
            if self.vars['block_key'] != key:
                self.vars.update(block_key=key, block_rows=[],
                                 block_invalid=(minute != 570+120*group))
        if minute == 570:
            self.vars.update(day_bars=[], day_invalid=False)
        if not self._complete_bar():
            self.vars['day_invalid'] = True
            self.vars['block_invalid'] = True
            self.vars['missing_bars'] = self.vars.get('missing_bars', 0)+1
            return
        bar = c[-1].copy()
        day_bars = self.vars['day_bars']
        if day_bars and int(bar[0]-day_bars[-1][0]) != HALF:
            self.vars['day_invalid'] = True
        day_bars.append(bar)
        h = self.vars['history']
        a = self._atr(h)
        if minute == 570 and a:
            self._record_event(self._opening_signal(h, bar, day, a))
        if minute < 930:
            rows = self.vars['block_rows']
            if rows and int(bar[0]-rows[-1][0]) != HALF:
                self.vars['block_invalid'] = True
            rows.append(bar)
            if len(rows) == 4 and not self.vars['block_invalid']:
                block = np.array([rows[0][0], rows[0][1], rows[-1][2],
                                  max(v[3] for v in rows), min(v[4] for v in rows), 0.])
                blocks = self.vars['blocks']
                blocks.append(block)
                self.vars['blocks'] = blocks[-300:]
                self.vars['b_seq'] += 1
                if a:
                    self._record_event(self._block_signal(self.vars['blocks'], h, a))
        decision = self._local(self.time)
        if (decision.hour, decision.minute) != (16, 0) or self.vars['day_invalid'] or len(day_bars) != 13:
            return
        closes = [float(v[2]) for v in day_bars]
        self.vars['d_seq'] += 1
        d = {'day': day, 'time': int(self.time), 'seq': self.vars['d_seq'],
             'open': float(day_bars[0][1]), 'close': closes[-1],
             'high': max(float(v[3]) for v in day_bars),
             'low': min(float(v[4]) for v in day_bars), 'closes30': closes,
             'a_prev': a, 'entropy': self._entropy(closes)}
        previous = h[-1] if h else None
        d['gap'] = (math.log(d['open']/previous['close'])
                    if previous and previous['day'] == self._civil_previous(day) else None)
        d['cash'] = math.log(d['close']/d['open'])
        # The partition telescopes to cash return, including interbar jumps.
        d['intraday_returns'] = np.log(np.array(closes)/np.array([d['open']]+closes[:-1])).tolist()
        change = d['close']-previous['close'] if previous else 0.
        sign = 1 if change > 0 else (-1 if change < 0 else 0)
        run = previous['run']+1 if previous and sign and previous['run_sign'] == sign else (1 if sign else 0)
        d.update(run_sign=sign, run=run)
        h.append(d)
        self.vars['history'] = h[-400:]  # Technical retention exceeds252/180D lookbacks.
        self.vars['daily_completed'] = True
        if a:
            self._record_event(self._daily_signal(self.vars['history'], a))

    def _opening_signal(self, h, bar, day, a):
        return None

    def _block_signal(self, blocks, h, a):
        return None

    def _daily_signal(self, h, a):
        return None

    def _event(self, side, a, hours, target=None, next_daily=False):
        if target is not None and side*(target-self.price) <= 0:
            return None
        distance = 2*a
        if not 0 < distance < self.price:
            return None
        return {'side': side, 'distance': distance, 'hours': hours,
                'target': target, 'next_daily': next_daily}

    def _plan(self):
        event = self.vars.get('event')
        if self.symbol != 'SPY-USDT' or len(self.routes) != 1 or not event or self._fix() is None:
            return 0
        entry = float(self.price)
        stop = entry-event['side']*event['distance']
        capital = max(0., min(float(self.balance), float(self.portfolio_value)))
        unit = event['distance']+self.fee_rate*(entry+stop)+RESERVE*entry
        qty = min(capital*RISK/unit, capital*GROSS/entry,
                  max(0., self.leveraged_available_margin*0.90)/entry)
        qty = math.floor(qty/0.001)*0.001  # Research precision, not venue-lot certification.
        if qty <= 0:
            return 0
        self.vars['plan'] = dict(event, qty=qty)
        return event['side']

    def _signal(self):
        if self.vars.get('signal_index') != self.index:
            self.vars.update(signal_index=self.index, signal=self._plan())
        return self.vars['signal']

    def should_long(self):
        return self._signal() == 1

    def should_short(self):
        return self._signal() == -1

    def go_long(self):
        self.buy = self.vars['plan']['qty'], self.price

    def go_short(self):
        self.sell = self.vars['plan']['qty'], self.price

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        p = self.vars['plan']
        entry = float(self.position.entry_price)
        self.stop_loss = abs(self.position.qty), entry-p['side']*p['distance']
        if p['target'] is not None:
            self.take_profit = abs(self.position.qty), p['target']
        self.vars.update(opened_at=int(self.position.opened_at), hold_ms=p['hours']*3600000,
                         entry_d_seq=self.vars['d_seq'], next_daily=p['next_daily'], exit_debt=False)

    def update_position(self):
        next_day = (self.vars.get('next_daily') and self.vars['daily_completed']
                    and self.vars['d_seq'] > self.vars['entry_d_seq'])
        due = next_day or self.vars.get('phase_exit') or self.time-self.vars['opened_at'] >= self.vars['hold_ms']
        if due:
            self.vars['exit_debt'] = True
        # Debt survives leaving the signal's calendar; stops never switch off.
        if self.vars.get('exit_debt') and self._fix() is not None:
            self.liquidate()

    def _cross_state(self, key, state):
        old = self.vars.get(key, 0)
        self.vars[key] = state
        return state != 0 and state != old

    def _daily_signal(self, h, a):
        current = h[-1]
        if not current['run_sign']:
            return None
        records = []
        for origin, target in zip(h[:-1], h[1:]):
            assert origin['time'] < target['time'] <= self.time
            if target['time']-origin['time'] > 120*3600000:
                continue
            state = (origin['run_sign'], min(origin['run'], 4))
            records.append((state, math.log(target['close']/origin['close'])))
        if len(records) < 252:
            return None
        records = records[-252:]
        state = (current['run_sign'], min(current['run'], 4))
        group = [label for key, label in records if key == state]
        if len(group) < 15:
            return None
        global_mean = float(np.mean([label for key, label in records]))
        forecast = (sum(group)+20*global_mean)/(len(group)+20)
        if not math.isfinite(forecast) or abs(forecast) <= HURDLE:
            return None
        return self._event(1 if forecast > 0 else -1, a, 120, next_daily=True)

```

## AngleBtcProbability4h
SHA256 d4add40c46e6c46210e77b976e93759da8ee368d182ec5343c453a7dc7ab47c1

```python
import math
from collections import deque
from datetime import datetime, timezone

import numpy as np
import jesse.indicators as ta
from jesse.strategies import Strategy

BAR_MS = 4 * 60 * 60 * 1000
MINUTE_MS = 60 * 1000
LEARNING_WINDOW = 1080  # 180 days of non-overlapping four-hour outcomes.
MIN_STATE_CASES = 80  # Avoid decisions supported by a handful of pattern matches.
PRIOR_CASES = 20.0  # Balanced zero-mean, unit-R-second-moment shrinkage prior.
BASE_FEE = 0.00045
FRICTION_BUFFER = 0.001  # Forecast haircut and sizing reserve, NOT simulated slippage.
TRADE_RISK = 0.01
NOTIONAL_CAP = 4.4
STOP_LEVERAGE_BUFFER = 0.75  # Keep25%inside ideal1/leverage; not exact liquidation math.


class AngleBtcProbability4h(Strategy):
    """Causal four-state monetary expectancy with explicit abstention.

    Two return signs define four states. No trend/reversal direction is assumed.
    Smoothed win probability is diagnostic; net payoff and uncertainty gate trades.
    This is a research hypothesis, not a claim of calibrated probabilities.
    """

    def _model(self):
        if 'probability_model' not in self.vars:
            self.vars['probability_model'] = {
                'observations': deque(),
                'count': np.zeros(4, dtype=np.int64),
                'sum': np.zeros((4, 2)),
                'sum_square': np.zeros((4, 2)),
                'wins': np.zeros((4, 2), dtype=np.int64),
                'pending': None,
                'last_processed': None,
                'labels_total': 0,
                'missing_labels': 0,
                'year': None,
                'skip_window': 0, 'skip_state_cases': 0, 'skip_edge': 0,
                'skip_stop_safety': 0, 'skip_qty': 0,
                'long_signals': 0, 'short_signals': 0,
            }
        return self.vars['probability_model']

    def _log_model_summary(self, label):
        m = self._model()
        self.log('ANGLE_PROBABILITY_SUMMARY ' + label + ' cumulative '
                 + str({k: (len(m['observations']) if k == 'window_length' else
                            m['count'].tolist() if k == 'state_counts' else m[k])
                        for k in ('labels_total', 'missing_labels', 'window_length',
                                  'state_counts', 'skip_window', 'skip_state_cases',
                                  'skip_edge', 'skip_stop_safety', 'skip_qty',
                                  'long_signals', 'short_signals')}))

    def _label(self, pending):
        # Only source minutes after the previous decision and already CLOSED now
        # can mature its label. No forward-fill or stale multi-hour substitute.
        if int(self.time) != pending['time'] + BAR_MS:
            return None
        minutes = self.get_candles(self.exchange, self.symbol, '1m')
        if len(minutes) < 240:
            return None
        minutes = minutes[-240:]
        expected = pending['time'] + np.arange(240, dtype=np.int64) * MINUTE_MS
        assert np.all(minutes[:, 0] < self.time), 'PROBABILITY_FUTURE_MINUTE'
        if not np.array_equal(minutes[:, 0].astype(np.int64), expected):
            return None
        if not np.isfinite(minutes[:, :5]).all() or np.any(minutes[:, 1:5] <= 0):
            return None
        entry = pending['entry']
        distance = pending['distance']
        outcomes = []
        for side in (1, -1):
            stop = entry - side * distance
            exit_price = float(minutes[-1, 2])
            for row in minutes:
                opening = float(row[1])
                # A protective STOP crossed by an opening gap fills at that
                # adverse minute opening; otherwise its first touched stop wins.
                if (side == 1 and opening <= stop) or (side == -1 and opening >= stop):
                    exit_price = opening
                    break
                if (side == 1 and row[4] <= stop) or (side == -1 and row[3] >= stop):
                    exit_price = stop
                    break
            # Signal costs remain fixed in later effective-fee stress. Every
            # virtual outcome bears both taker fees plus a conservative haircut.
            cash_per_unit = (side * (exit_price - entry)
                             - BASE_FEE * (entry + exit_price)
                             - FRICTION_BUFFER * entry)
            outcomes.append(cash_per_unit / distance)
        return np.asarray(outcomes)

    def _record(self, pending, outcomes):
        model = self._model()
        observations = model['observations']
        if len(observations) == LEARNING_WINDOW:
            state, old = observations.popleft()
            model['count'][state] -= 1
            model['sum'][state] -= old
            model['sum_square'][state] -= old * old
            model['wins'][state] -= (old > 0).astype(np.int64)
        state = pending['state']
        observations.append((state, outcomes.copy()))
        model['count'][state] += 1
        model['sum'][state] += outcomes
        model['sum_square'][state] += outcomes * outcomes
        model['wins'][state] += (outcomes > 0).astype(np.int64)
        model['labels_total'] += 1
        assert int(model['count'].sum()) == len(observations)
        assert np.all(model['count'] >= 0)

    def before(self):
        assert self.symbol == 'BTC-USDT' and self.timeframe == '4h'
        assert self.is_futures_trading
        model = self._model()
        if model['last_processed'] == int(self.time):
            return
        model['last_processed'] = int(self.time)
        year = datetime.fromtimestamp(self.time / 1000, timezone.utc).year
        if model['year'] is not None and year != model['year']:
            self._log_model_summary('through_year_' + str(model['year']))
        model['year'] = year
        pending = model['pending']
        if pending is not None:
            outcomes = self._label(pending)
            if outcomes is None:
                model['missing_labels'] += 1
                # Eight failed maturation attempts with zero valid labels is a
                # data/cadence failure, not evidence that the economic gate abstains.
                # Occasional gaps after valid observations remain permitted.
                if model['labels_total'] == 0 and model['missing_labels'] >= 8:
                    self._log_model_summary('invalid_m1_coverage')
                    raise AssertionError('ANGLE_NO_MATURED_LABELS: verify240closed_contiguous_M1_and_clock')
            else:
                self._record(pending, outcomes)
        c = self.candles
        model['pending'] = None
        if len(c) < 30:
            return
        # All three closes are known now. Equal closes join the non-positive
        # state; there is no extra flat-return threshold to fit.
        closes = c[-3:, 2]
        if not np.isfinite(closes).all() or np.any(closes <= 0):
            return
        state = 2 * int(closes[1] > closes[0]) + int(closes[2] > closes[1])
        atr = float(ta.atr(c))
        distance = 3 * atr  # Emergency stop, not an optimized entry filter.
        if not (math.isfinite(distance) and 0 < distance < float(self.price)):
            return
        # Ideal liquidation distance1/L ignores maintenance/fees. Staying25%
        # inside it avoids obviously unprotected labels, without promising an
        # exact exchange liquidation boundary. This is not an optimizable gate.
        if distance / float(self.price) > STOP_LEVERAGE_BUFFER / self.leverage:
            model['skip_stop_safety'] += 1
            return
        model['pending'] = {'state': state, 'entry': float(self.price),
                            'distance': distance, 'time': int(self.time)}

    def _decision(self):
        if self.vars.get('decision_time') == int(self.time):
            return self.vars['decision_side']
        self.vars['decision_time'] = int(self.time)
        self.vars['decision_side'] = 0
        model = self._model()
        current = model['pending']
        # Runtime startup is fully retained as cash in the backtest. Warm-up
        # candles supply ATR only; no future/pretrained outcome table is loaded.
        if current is None or len(model['observations']) < LEARNING_WINDOW:
            model['skip_window'] += 1
            return 0
        state = current['state']
        n = int(model['count'][state])
        if n < MIN_STATE_CASES:
            model['skip_state_cases'] += 1
            return 0
        total = n + PRIOR_CASES
        mean = model['sum'][state] / total
        variance = np.maximum((model['sum_square'][state] + PRIOR_CASES) / total
                              - mean * mean, 0.0)
        standard_error = np.sqrt(variance / total)
        # This one-SE lower score is a conservative decision heuristic, NOT a
        # confidence statement under independent observations or a p-value.
        lower = mean - standard_error
        direction = int(np.argmax(lower))
        if not np.isfinite(lower).all() or lower[direction] <= 0:
            model['skip_edge'] += 1
            return 0
        side = 1 if direction == 0 else -1
        entry = current['entry']
        distance = current['distance']
        if distance / entry > STOP_LEVERAGE_BUFFER / self.leverage:
            model['skip_stop_safety'] += 1
            return 0
        stop = entry - side * distance
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        # The single BTC route starts at1%, below the approved3%/8% ceilings.
        unit_risk = distance + self.fee_rate * (entry + stop) + FRICTION_BUFFER * entry
        qty = min(capital * TRADE_RISK / unit_risk,
                  capital * NOTIONAL_CAP / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        # Research precision only; native lot/min-notional must precede live use.
        qty = math.floor(qty / 0.001) * 0.001
        if qty <= 0:
            model['skip_qty'] += 1
            return 0
        assert qty * unit_risk <= capital * TRADE_RISK + 1e-8
        self.vars['plan'] = {
            'qty': qty, 'distance': distance, 'entry': entry, 'state': state,
            'state_cases': n, 'expected_net_r': float(mean[direction]),
            'one_se_lower_r': float(lower[direction]),
            'win_probability': float((model['wins'][state, direction] + PRIOR_CASES / 2) / total),
        }
        model['long_signals' if side == 1 else 'short_signals'] += 1
        self.vars['decision_side'] = side
        return side

    def should_long(self):
        return self._decision() == 1

    def should_short(self):
        return self._decision() == -1

    def go_long(self):
        p = self.vars['plan']
        self.buy = p['qty'], self.price

    def go_short(self):
        p = self.vars['plan']
        self.sell = p['qty'], self.price

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        p = self.vars['plan']
        self.vars['opened_time'] = int(self.time)
        entry = float(self.position.entry_price)
        distance = p['distance']
        assert distance / entry <= STOP_LEVERAGE_BUFFER / self.leverage + 1e-12, 'ANGLE_FILL_STOP_BEYOND_SAFETY'
        if self.is_long:
            self.stop_loss = abs(self.position.qty), entry - distance
        else:
            self.stop_loss = abs(self.position.qty), entry + distance

    def update_position(self):
        # If an emergency stop did not already close it intrabar, close at the
        # first next four-hour decision. Jesse does not reopen in that callback.
        if self.time - self.vars['opened_time'] >= BAR_MS:
            self.liquidate()

    def on_increased_position(self, order):
        raise AssertionError('PROBABILITY_PYRAMIDING_UNSUPPORTED')

    def on_reduced_position(self, order):
        raise AssertionError('PROBABILITY_PARTIAL_EXIT_UNSUPPORTED')

    def before_terminate(self):
        self._log_model_summary('final')
```

## AngleCombinedBtcEventClock1m
SHA256 038554637216a164f0e16b6f01d5063fc78cc70442cea34ee324979c7f92cb70

```python
import math
from datetime import datetime, timezone
import jesse.helpers as jh
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


class AngleCombinedBtcEventClock1m(Strategy):
    """BTC close-only directional-change clock replacing short RSI eligibility.

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
            # Keep the baseline long signal frequency on the 4h boundary.
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

    def _event_counts(self, year=None):
        year = self.vars['event_year'] if year is None else year
        return self.vars.setdefault('event_counts', {}).setdefault(year, {
            'minutes': 0, 'down': 0, 'up': 0, 'blocked_open': 0,
            'blocked_pending': 0, 'long_priority': 0, 'rejected': 0,
            'plans': 0, 'armed': 0, 'fills': 0,
        })

    def _event_log(self, label):
        # Bounded yearly aggregates only; never retain a per-minute/event list.
        timestamps = {key: self.vars.get(key) for key in (
            'event_first_minute', 'event_init_time', 'event_last_minute')}
        jh.debug('EVENT_CLOCK ' + label + ' timestamps=' + str(timestamps)
                 + ' counts=' + str(self.vars.get('event_counts', {})))

    def before(self) -> None:
        if self.symbol != 'BTC-USDT':
            return
        now = int(self.time)
        self.vars.setdefault('event_first_minute', now)
        minute = self.candles[-1]
        assert int(minute[0]) + 60000 == now, 'EVENT_M1_NOT_FRESH'
        price, low = float(minute[2]), float(minute[4])
        assert all(math.isfinite(v) and v > 0 for v in (price, low)), 'EVENT_M1_INVALID'
        assert low <= price, 'EVENT_M1_LOW_ABOVE_CLOSE'
        assert math.isclose(price, self.price, rel_tol=1e-10, abs_tol=1e-8), 'EVENT_PRICE_MISMATCH'
        previous = self.vars.get('event_last_minute')
        assert previous is None or previous < now, 'EVENT_MINUTE_REPLAY'
        self.vars['event_last_minute'] = now
        # This timestamp is a pulse, not a queue. Open/pending orders cannot
        # save it for a later flat callback or extend a pending deadline.
        self.vars['event_down_time'] = None
        year = datetime.fromtimestamp(now / 1000, timezone.utc).year
        old_year = self.vars.get('event_year')
        if old_year is not None and year != old_year:
            self._event_log('YEAR_END ' + str(old_year))
        self.vars['event_year'] = year
        counts = self._event_counts()
        counts['minutes'] += 1

        boundary = now % BAR_MS == 0
        if boundary:
            c = self.signal_candles
            assert len(c) >= 240, 'EVENT_AUX_4H_WARMUP'
            assert int(c[-1, 0]) + BAR_MS == now, 'EVENT_AUX_4H_NOT_FRESH'
            macro = ta.ema(c, period=120, sequential=True)
            cache = {
                'bar': int(c[-1, 0]), 'atr': float(ta.atr(c)),
                'fast': float(ta.ema(c, period=20)),
                'macro': float(macro[-1]), 'macro_old': float(macro[-10]),
            }
            assert all(math.isfinite(v) for v in cache.values()), 'EVENT_4H_INVALID'
            assert cache['atr'] > 0, 'EVENT_ATR_NONPOSITIVE'
            self.vars['event_4h'] = cache
            self.vars['clock_warmup_checked'] = True
        if 'event_phase' not in self.vars:
            if not boundary:
                return
            self.vars.update({
                'event_phase': 0, 'event_seed': price,
                'event_delta': self.vars['event_4h']['atr'],
                'event_phase_time': now, 'event_extreme': price,
                'event_init_time': now,
            })
            return

        cache = self.vars['event_4h']
        assert cache['bar'] + BAR_MS <= now < cache['bar'] + 2 * BAR_MS, 'EVENT_AUX_CACHE_STALE'
        phase = self.vars['event_phase']
        delta = float(self.vars['event_delta'])
        assert phase in (-1, 0, 1) and math.isfinite(delta) and delta > 0, 'EVENT_STATE_INVALID'
        assert self.vars['event_phase_time'] <= now, 'EVENT_PHASE_FUTURE'
        if phase == 0:
            seed = self.vars['event_seed']
            direction = 1 if price >= seed + delta else (-1 if price <= seed - delta else 0)
            if direction:
                # Seeding the initial direction is not a tradable reversal.
                self.vars.update({
                    'event_phase': direction, 'event_extreme': price,
                    'event_delta': cache['atr'], 'event_phase_time': now,
                })
            return
        extreme = float(self.vars['event_extreme'])
        assert math.isfinite(extreme) and extreme > 0, 'EVENT_EXTREME_INVALID'
        if phase == 1:
            extreme = max(extreme, price)
            self.vars['event_extreme'] = extreme
            crossed = extreme - price >= delta
        else:
            extreme = min(extreme, price)
            self.vars['event_extreme'] = extreme
            crossed = price - extreme >= delta
        if not crossed:
            return
        assert now > self.vars['event_phase_time'], 'EVENT_DOUBLE_PHASE_SAME_MINUTE'
        # The crossing used the OLD phase delta. Only the newly started
        # phase gets the latest strictly closed 4h ATR.
        self.vars.update({
            'event_phase': -phase, 'event_extreme': price,
            'event_delta': cache['atr'], 'event_phase_time': now,
        })
        if phase == 1:
            counts['down'] += 1
            self.vars['event_down_time'] = now
            self.vars['event_m1_low'] = low
            if self.is_open:
                counts['blocked_open'] += 1
        else:
            counts['up'] += 1

    def before_terminate(self) -> None:
        if self.symbol == 'BTC-USDT':
            self._event_log('FINAL')

    def _signal(self) -> int:
        # One plan per M1, with the unchanged 4h long policy taking priority.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            if self.symbol != 'BTC-USDT':
                self.vars['signal_value'] = 1 if self._plan() else (-1 if self._short_plan() else 0)
            else:
                down = self.vars.get('event_down_time') == int(self.time)
                if self.vars.get('event_cancel_time') == int(self.time):
                    self.vars['signal_value'] = 0
                elif self._plan():
                    self.vars['signal_value'] = 1
                    if down:
                        self._event_counts()['long_priority'] += 1
                elif down:
                    planned = self._short_plan()
                    self.vars['signal_value'] = -1 if planned else 0
                    self._event_counts()['plans' if planned else 'rejected'] += 1
                else:
                    self.vars['signal_value'] = 0
        return self.vars['signal_value']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        plan = self.vars['plan']
        if self.symbol == 'BTC-USDT':
            self.vars['entry_deadline'] = int(self.time) + BAR_MS
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], plan['entry']

    def _short_plan(self) -> bool:
        """An observed DOWN event replaces RSI; all risk gates stay frozen."""
        if self.symbol != 'BTC-USDT' or self.vars.get('event_down_time') != int(self.time):
            return False
        if self.vars.get('event_cancel_time') == int(self.time):
            return False
        cache = self.vars['event_4h']
        assert cache['bar'] + BAR_MS <= self.time < cache['bar'] + 2 * BAR_MS, 'EVENT_SIGNAL_CACHE_STALE'
        fast, atr = cache['fast'], cache['atr']
        if not (atr > 0 and cache['macro'] > cache['macro_old']
                and self.price > cache['macro'] - atr):
            return False
        # Adapt the known signal low to the event's M1, not a prior 4h bar.
        # It is an order level for FUTURE execution, never a backdated fill.
        entry = min(float(self.vars['event_m1_low']), self.price - 0.25 * atr)
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
        assert self.vars.get('event_down_time') == int(self.time), 'EVENT_ORDER_REPLAY'
        assert self.vars.get('event_order_time') != int(self.time), 'EVENT_DUPLICATE_ORDER'
        self.vars['event_order_time'] = int(self.time)
        self._event_counts()['armed'] += 1
        plan = self.vars['plan']
        if self.symbol == 'BTC-USDT':
            self.vars['entry_deadline'] = int(self.time) + BAR_MS
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        if self.symbol == 'BTC-USDT':
            if self.vars.get('event_down_time') == int(self.time):
                self._event_counts()['blocked_pending'] += 1
            # Pending entries keep their risk/notional reservation for the full
            # original 4h lifetime, despite 1m cancellation callbacks.
            if self.time < self.vars['entry_deadline']:
                return False
        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.
        # Jesse processes cancellation before evaluating the next route.
        if self.symbol == 'BTC-USDT':
            self.vars['event_cancel_time'] = int(self.time)
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        self.vars['initial_distance'] = distance
        # An intrabar fill must not inherit highs/closes from before its entry.
        self.vars['best_close'] = entry
        if self.is_short:
            if self.symbol == 'BTC-USDT':
                self._event_counts()['fills'] += 1
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

    def on_close_position(self, order, closed_trade) -> None:
        self._ledger().pop(self._key(), None)
```

# Prior protocols and closures, full text

## strategies/AngleBtcProbability4h/reports/ANGLE_BTC_PROBABILITY_PROTOCOL_20261018.md
SHA256 4a943aed4cc6cd6d107b22c7081078e9a825e049d22cbe0a8ac0f87e3a0629ab

# Protocolo previo: probabilidad secuencial y expectativa monetaria BTC4h

Estado: implementación para revisión, SIN backtest lanzado. Una sola receta, sin rejilla ni modelo preentrenado. Prefijo propioAngleBtcProbability; referencia original intacta y2026reservado.

## Hipótesis y diferencia limitada
Cuatro estados, definidos por el signo de los dos últimos retornos4h, podrían presentar expectativas de continuación/reversión cambiantes. La estrategia no fija de antemano el sentido rentable: aprende sólo de resultados pasados y puede abstenerse. No agrega información externa ni una teoría nueva; podría ser otra expresión estadística de momentum/reversión ya estudiados. Si no demuestra ventaja neta, no renombrarla como mecanismo independiente ni complicarla conHMM/redes.

Inventario leído porMCP: ORCH_GLOBAL_MECHANISM_INVENTORY_20261018.md, registro global y progreso canónico. Trend/medias/breakout/retest/rangos/compresión/dips/gestión/rotación y pares ya están intensamente explorados. Esta prueba cambia la regla de decisión hacia estimación secuencial parsimoniosa, no la fuente informativa.

## Observaciones, maduración y ausencia de fuga
Antes de cada decisión4h se madura exclusivamente la etiqueta de la decisión anterior. Se exigen240M1cerradas ycontiguas con timestamps exactos desde el anteriorcierre hasta el actual; ninguna vela futura, interpolación ni relleno de huecos. Etiqueta madura sólo a+4h; si falta cobertura, no se añade.

Para long y short hipotéticos se calcula retornoR de una entradaMARKET al cierre anterior,stopemergencia3ATR conocido entonces y salida al cierre siguiente si no se tocóstop. PrimercruceM1: apertura adversa que salta stop ejecuta aesaapertura; en otro caso, primerlow/high que toca ejecuta alstop. No depende del ordenhigh/low de toda4h. Es una reconstrucción de etiquetas conM1, NO una garantía general de paridad con el motor bajo todas sus convenciones. No se reportan etiquetas como trades reales.

Cada etiqueta resta ambasfeesBASE0.00045porlado yhaircut10bpsRT; todo dividido por distancia de stop. Costesde señal quedanfijos para posteriores controles de fee efectiva. Haircut ybuffer de sizing NO son slippage efectivamente simulado.

## Tamaño, shrinkage y decisión
Ventana rolling1080etiquetas aceptadas, aproximadamente180días; se acumula ENRUNTIME. Warmup240sólo apoyaATR; no se usa para cargar una tabla futura ni completar1080. Todo startupcash se conserva en métricas y meses/trimestres; no recortar la ventana de evaluación.

Para cada4estados y2direcciones se mantienen n,sumaR,sumaR²,wins. Exigir almenos80observaciones delestado y ventana1080llena. Prior20casos balanceados: mediaR0,momento2=1R²,winrate50%. Media=(sumR)/(n+20);var=(sumR²+20)/(n+20)−media²;SE=sqrt(var/(n+20)). Entrar sólo si media−1SE>0; escoger la dirección conmayor score o mantenercash. La probabilidad(wins+10)/(n+20) se conserva como diagnóstico,no gate51%.

SE es una heurística de prudencia, NO intervalo válido de confirmación: hay dependencia temporal, cambio de régimen y selección acumulada. El sistema no se presenta como probabilidad calibrada sin evaluación adicional. NoKelly ni riesgo ajustado por probabilidad.

## Órdenes y límites
Una rutaBTC-USDT4h,BinancePerpetual,normal,benchmark=True,2020-10-15→2025-12-31exclusivo;10000USDT,5xaislado,fee0.00045porlado,warmup240. EntradasMARKET;3ATRstopfijo;sinTP/trail/parciales/piramidado. Salida al siguiente cierre4h si sobrevive. El motor no vuelve a entrar en el mismo callback que liquida una posición; no se fuerzan reaperturas ni transacciones fuera del ciclo.

Riesgo1%de min(wallet,equity), incluyendo fees reales y10bpsreserve; por debajo de3%/trade y8%global. Gross<=4.4x y90%de margenleverageddisponible. Cantidad variable redondeada haciaabajo. Lot/minnotional nativo, funding eimpacto no están validados para live.

## Falsación y evaluación
Primera corrida única sin cambiar1080/80/20/1SE/3ATR después. Cero operaciones es resultado admisible: evidencia insuficiente, no razón para relajar gates. Neto<=0,DD>25%,expectativa eliminada porcostes o muestraescasa impiden promover. Si promete, ROOT decidirá un control sinestados y vecindario acotado; no está autorizado aún.

Se revisarán PnLneto/fees/númerooperaciones, long/short,concentración,años2020–2025 ycalendarioMTMcon startupcash íntegro. No llamar2024–2025OOSlimpio ni confundir entrenamiento causal de cada predicción con independencia de la investigación completa. Las metas65–70%mesesactivos/80%trimestres se mantienen; reportar también todoslosmeses/períodoscompletos.

Implementación sóloMCP/Strategy/NumPy/stdlib, sin scripts nuevos, red, archivos, randomness, framework, instalaciones, live/Pi o datos externos. Revisar fuente conROOT ANTES de corrida y coordinar máximo2simultáneas.


## Revisión técnica ex ante anterior al primer run

ROOT pidió añadir distancia/entry<=0.75/leverage tanto al armar pendinglabels como al plan de entrada; assert de coherencia también al fill. A5x equivale aproximadamente15%,25% de colchón respecto a distancia ideal1/L, NO cálculo exacto de liquidación con mantenimiento/fees. Es un guard de seguridad fijo, no parámetro de optimización ni ajuste visto el resultado.

Logs self.log al cambiar año y before_terminate resumen contadores ACUMULADOS: labels_total,missing_labels,windowlen,counts4estados,skipwindow/estado/edge/seguridad/cantidad yseñaleslong/short. Son diagnósticos, no resultados económicos inventados. Si hay ocho intentos de maduración fallidos SIN ninguna etiqueta válida, se aborta con error descriptivo de coberturaM1/clock. Una eventual corrida0trades sólo es interpretable con aprendizaje funcional; huecos aislados después de observaciones válidas no producen ese aborto.

Sin cambio a1080/80/20/1SE/3ATR, fees,señales probabilísticas ni riesgo. Gross4.4x es techo de admisión, no garantía continua después de moverse el precio. Esta primera corrida es standaloneBTC; integración con otras patas exige ledgercompartido explícito.


## strategies/AngleBtcProbability4h/reports/ANGLE_BTC_PROBABILITY_INITIAL_RESULT_20261018.md
SHA256 cfd7235548b7d23ddbc7384966b946077290c5c1d661294664d00155bee35fc9

# BTC probability: initial result and completed technical diagnosis — 2026-10-18

## Verdict

This particular four-state, shrinkage, one-SE monetary-expectancy recipe abstains economically throughout the development window. It is not a missing-data or immature-training-window result. Do not relax thresholds, remove the friction haircut, increase risk or add an unconditional comparison to manufacture trades.

This is evidence against usefulness of the tested recipe, not a proof that every causal probabilistic approach to BTC is impossible.

## Sessions and unchanged design

[Initial run](http://localhost:9200/#/backtest/8fb36f9a-ead7-41cd-9341-bc95de116f5a): finished20.11s, zero trades, metrics null, no error, empty stored equity curves. Debug=False prevented access to the diagnostic self.log summaries. Source was reviewed and unchanged.

[Same-policy diagnostic repeat](http://localhost:9200/#/backtest/ab8e72a8-f81f-41d8-8d95-8681d27e1b9c): finished100.51s, zero trades, metrics null, no error, empty stored equity curves; debug=True. No source, threshold, fee, risk or calendar change. This repeat is a technical diagnostic, not a second economic hypothesis or an optimization.

Both forms specify BTC-USDT4h, Binance Perpetual Futures,2020-10-15 through2025-12-31 exclusive, initialcash10000, fee0.00045,5xisolated, normal mode, warmup240 and benchmarkTrue.2026 was not evaluated.

## Directly verified final diagnostics

The bounded MCP logs page of the repeat shows at2025-12-31T00:00:
- labels_total11297, missing_labels0;
- window_length1080, state_counts[264,272,273,271];
- skip_window1200, skip_state_cases0;
- skip_edge10218, skip_stop_safety120, skip_qty0;
- long_signals0, short_signals0;
- final saved daily portfolio balance10000.0.

Thus the M1 maturation clock and exact contiguous240-minute coverage produced11297 valid causal labels, the rolling window filled, all states had adequate samples, and quantity constraints never suppressed a positive forecast. No eligible decision overcame the unchanged positive lower-score gate. The stop-safety count is an ex-ante protection, not a reason to loosen leverage or stops. Counters are cumulative and can overlap in diagnostic purpose: do not sum them as mutually exclusive trade cohorts.

There are no actual executed trades. Do not invent a CAGR, drawdown, winrate or positive-month rate from null metrics or absent curves. The logged cash balance supports cash retention; the dashboard does not supply a normal performance curve in this zero-trade storage path.

## Interpretation and next step

Short-horizon return-sign states did not support positive net expectancy under the tested stop/horizon, both taker fees,10bps forecast haircut and one-SE shrinkage score. This remains development evidence across2020–2025, not clean out-of-sample validation. No policy adjustment or additional run is justified on these results alone.

The independent combined intrabar-acceptance gate is separately predeclared under AngleCombinedBtcAcceptance4h; it does not modify or rescue this recipe. Reference MultiAssetRetestBtcShort4h remains unchanged.


## strategies/MultiAssetRetestBtcShort4h/reports/BTC_NEW_ANGLES_RESULTS_20261018.md
SHA256 2c51d2eb2debb30679c0c628db6e6e7eae1a07e84aaf576f9bd80d220039ba63

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


# Prepared W source texts before creation / economics

Implementation/checks later authorized; no drafts/economics. Current ATR0 distinction and all-trajectory mathematical-state equality clarified before these sources.

## BtcResearchR23PassageBase1m
SHA256 ef1cf7776c46ae6af17e8a8fcf041d2db9e7a18b9de3c80574c4942203dfda3c

```python
import math

import numpy as np
from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def passage_anchor(now, price, atr):
    """Guard absolute barriers physically; no buffer or outcome-based repair."""
    if atr is None or not all(math.isfinite(v) for v in (price, atr)):
        return None
    lower, upper = price - 2*atr, price + 2*atr
    if not (price > 0 and atr > 0 and math.isfinite(lower)
            and math.isfinite(upper) and lower > 0 and upper > 0):
        return None
    return dict(a=float(price), d=float(atr), t0=int(now), s=0, t1=None)


def passage_machine(anchor, now, price, atr):
    """One close, at most one passage; current ATR cannot erase old frozen d."""
    if anchor is None:
        new = passage_anchor(now, price, atr)
        return new, None, "seed" if new is not None else "anchor_invalid"
    assert now > anchor["t0"]
    a, d = anchor["a"], anchor["d"]
    if anchor["t1"] is None:
        sign = 1 if price >= a+d else -1 if price <= a-d else 0
        if not sign:
            return anchor, None, "wait_first"
        if sign*(price-a) >= 2*d:
            # No invented intermediate timestamp or same-close new first passage.
            return passage_anchor(now, price, atr), None, "degenerate"
        return dict(anchor, s=sign, t1=int(now)), None, "first"
    assert now > anchor["t1"]
    z = anchor["s"]*(price-a)
    if 0 < z < 2*d:
        return anchor, None, "wait_second"
    kind = "REV" if z <= 0 else "CONT"
    r = -anchor["s"] if kind == "REV" else anchor["s"]
    u, v = anchor["t1"]-anchor["t0"], now-anchor["t1"]
    assert u > 0 and v > 0
    event = dict(type=kind, fast=bool(v < u), r=int(r), t0=anchor["t0"],
                 t1=anchor["t1"], t2=int(now), a=a, d=d, u=int(u), v=int(v),
                 entry=float(price))
    return passage_anchor(now, price, atr), event, "event"


def passage_model():
    return dict(anchor=None, last=None, pending=[], bank=[])


def passage_advance(model, now, price, atr):
    """Mature before observing today's event. No orders/occupancy/model mode."""
    assert math.isfinite(price) and price > 0
    reset = model["last"] is not None and now != model["last"]+BAR
    if reset:
        model.clear()
        model.update(passage_model())
    matured = 0
    remaining = []
    for pending in model["pending"]:
        age = now-pending["t2"]
        assert age > 0 and age % BAR == 0 and age <= 6*BAR
        if age == 6*BAR:
            y = pending["r"]*(math.log(price)-math.log(pending["entry"]))
            assert math.isfinite(y)
            model["bank"].append(dict(type=pending["type"], fast=pending["fast"],
                                      y=float(y), t2=pending["t2"], matured=int(now)))
            if len(model["bank"]) > 240:
                model["bank"].pop(0)
            matured += 1
        else:
            remaining.append(pending)
    model["pending"] = remaining
    # This call is deliberately AFTER maturation and independent of atr validity.
    model["anchor"], event, action = passage_machine(model["anchor"], now, price, atr)
    if event is not None:
        model["pending"].append(dict(event))
    model["last"] = int(now)
    return event, dict(action=action, matured=matured, gap_reset=bool(reset),
                       reset_anchor_invalid=model["anchor"] is None)


def passage_bootstrap(rows):
    """Exactly1000 closed rows, row14 seed; replay once, never submit a trade."""
    assert len(rows) == 1000
    model, counts = passage_model(), {}
    for j in range(14, 1000):
        now = int(rows[j, 0])+BAR
        atr = atr14(rows[j-14:j+1])
        event, info = passage_advance(model, now, float(rows[j, 2]), atr)
        counts[info["action"]] = counts.get(info["action"], 0)+1
        counts["matured"] = counts.get("matured", 0)+info["matured"]
        counts["bars"] = counts.get("bars", 0)+1
    return model, counts


def passage_forecasts(bank, event):
    """The SAME complete240 bank/shared20-cell domain for both conditional means."""
    if len(bank) != 240:
        return None
    cell = [item["y"] for item in bank
            if item["type"] == event["type"] and item["fast"] == event["fast"]]
    group = [item["y"] for item in bank if item["type"] == event["type"]]
    if len(cell) < 20 or not all(math.isfinite(v) for v in group):
        return None
    state, by_type = float(np.mean(cell)), float(np.mean(group))
    if not all(math.isfinite(v) for v in (state, by_type)):
        return None
    return dict(state_mean=state, type_mean=by_type, cell_n=len(cell), type_n=len(group),
                bank_first=bank[0]["t2"], bank_last=bank[-1]["t2"])


class BtcResearchR23PassageBase1m(BtcResearchR12ArBase1m):
    MODE = "abstract"

    def _passage_count(self, name, amount=1):
        stats = self.vars.setdefault("passage_runtime_counts", {})
        stats[name] = stats.get(name, 0)+amount

    def _passage_reset(self, reason):
        # A market-data discontinuity discards all predictive history. This is
        # NOT a second bootstrap and cannot cancel broker stops/time exits.
        self.vars["passage_model"] = passage_model()
        self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
        self._passage_count("invalid:"+reason)

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("STATE", "TYPE_CONTROL")
            self.vars["checked"] = True
            self._log("R23_PASSAGE_CONFIG", dict(mode=self.MODE, bootstrap_rows=1000,
                      seed_row=14, bank=240, cell_min=20, horizon_hours=24,
                      stop_atr=2, target=None, risk=.02, aggregate=.06,
                      leverage=3, fee=.00045, feature="observed_type_fast_not_pure_speed"))
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR or now > self.FINISH:
            return
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        if not self.vars.get("passage_bootstrapped"):
            rows = closed_window(candles, now, 1000)
            if (rows is None or not np.all(rows[:, 0] % BAR == 0)
                    or not math.isclose(float(rows[-1, 2]), float(self.price),
                                        rel_tol=1e-10, abs_tol=1e-8)):
                self._passage_count("bootstrap_wait")
                return
            model, counts = passage_bootstrap(rows)
            self.vars["passage_model"] = model
            self.vars["passage_bootstrap_counts"] = counts
            self.vars["passage_bootstrapped"] = True
            self.vars["passage_initialized_at"] = now
            self._log("R23_PASSAGE_BOOTSTRAP", dict(time=now, counts=counts,
                      bank=len(model["bank"]), pending=len(model["pending"])))
            # The last replay event is mathematical, never a queued first trade.
            return
        rows = closed_window(candles, now, 15)
        if rows is None or not np.all(rows[:, 0] % BAR == 0):
            self._passage_reset("ohlc_or_clock")
            return
        if not math.isclose(float(rows[-1, 2]), float(self.price),
                            rel_tol=1e-10, abs_tol=1e-8):
            self._passage_reset("asof_price")
            return
        model = self.vars["passage_model"]
        atr = atr14(rows)
        # ATR0/None blocks ONLY new anchor/order; old pending and frozen-d phase
        # still advance on this valid close. Never return before this call.
        event, info = passage_advance(model, now, float(rows[-1, 2]), atr)
        self._passage_count("bars")
        self._passage_count(info["action"])
        self._passage_count("matured", info["matured"])
        self._passage_count("gap_reset", int(info["gap_reset"]))
        if event is None:
            return
        self._passage_count(event["type"]+("_FAST" if event["fast"] else "_SLOW"))
        forecasts = passage_forecasts(model["bank"], event)
        if forecasts is None:
            self._passage_count("insufficient_bank_or_cell")
            return
        mean = forecasts["state_mean"] if self.MODE == "STATE" else forecasts["type_mean"]
        score = event["r"]*mean
        if abs(score) <= .0019 or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        if atr is None:
            self._passage_count("entry_atr_invalid")
            return
        direction = 1 if score > 0 else -1
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = direction
        self.vars["passage_evidence"] = dict(event=event, score=score, **forecasts)

    def on_open_position(self, order):
        super().on_open_position(order)
        self._log("R23_PASSAGE_OPEN", dict(mode=self.MODE, time=int(self.time),
                  entry=float(self.position.entry_price),
                  evidence=self.vars["passage_evidence"]))

    def _emit(self, stage):
        super()._emit(stage)
        model = self.vars.get("passage_model", passage_model())
        cells = {kind+("_FAST" if fast else "_SLOW"): sum(
                    item["type"] == kind and item["fast"] == fast for item in model["bank"])
                 for kind in ("REV", "CONT") for fast in (False, True)}
        anchor = model["anchor"]
        self._log("R23_PASSAGE_STATS", dict(stage=stage, mode=self.MODE,
                  initialized=self.vars.get("passage_initialized_at"),
                  bootstrap=self.vars.get("passage_bootstrap_counts", {}),
                  runtime=self.vars.get("passage_runtime_counts", {}),
                  bank=len(model["bank"]), cells=cells, pending=len(model["pending"]),
                  last=model["last"], incomplete_episode=anchor is not None,
                  first_passage_seen=bool(anchor is not None and anchor["t1"] is not None)))
```

## BtcResearchR23PassageState1m
SHA256 e9081120f22dc4d2afac6fc26dbcbb2893b41131968148b7d0921792534cb157

```python
from strategies.BtcResearchR23PassageBase1m import BtcResearchR23PassageBase1m


class BtcResearchR23PassageState1m(BtcResearchR23PassageBase1m):
    MODE = "STATE"
```

## BtcResearchR23PassageType1m
SHA256 08b7695bfe1ca0f9d500a7c9fd7025228cf5de2c9031f5874ee2609de03294fb

```python
from strategies.BtcResearchR23PassageBase1m import BtcResearchR23PassageBase1m


class BtcResearchR23PassageType1m(BtcResearchR23PassageBase1m):
    MODE = "TYPE_CONTROL"
```

# Telemetry-only revision after first successful technical check

First job f1e8a4381ec2420cabd48a06cf435689 succeeded117 assertions on baseef1cf7776c46ae6af17e8a8fcf041d2db9e7a18b9de3c80574c4942203dfda3c. Root review requested explicit bootstrap cells/ties, runtime ties and actual stop/position deadline/label deadline in fill evidence. Add counters/log fields only; mathematical model/labels/forecast/sizing/management unchanged. Prior source and check remain preserved. CURRENT base follows; final check must use it.

## BtcResearchR23PassageBase1m CURRENT instrumented
SHA256 d8ac03f4b02fa3c471fdac510a6d9b2f36c2aa80cd3c0a65661a0cd887fafccc

```python
import math

import numpy as np
from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def passage_anchor(now, price, atr):
    """Guard absolute barriers physically; no buffer or outcome-based repair."""
    if atr is None or not all(math.isfinite(v) for v in (price, atr)):
        return None
    lower, upper = price - 2*atr, price + 2*atr
    if not (price > 0 and atr > 0 and math.isfinite(lower)
            and math.isfinite(upper) and lower > 0 and upper > 0):
        return None
    return dict(a=float(price), d=float(atr), t0=int(now), s=0, t1=None)


def passage_machine(anchor, now, price, atr):
    """One close, at most one passage; current ATR cannot erase old frozen d."""
    if anchor is None:
        new = passage_anchor(now, price, atr)
        return new, None, "seed" if new is not None else "anchor_invalid"
    assert now > anchor["t0"]
    a, d = anchor["a"], anchor["d"]
    if anchor["t1"] is None:
        sign = 1 if price >= a+d else -1 if price <= a-d else 0
        if not sign:
            return anchor, None, "wait_first"
        if sign*(price-a) >= 2*d:
            # No invented intermediate timestamp or same-close new first passage.
            return passage_anchor(now, price, atr), None, "degenerate"
        return dict(anchor, s=sign, t1=int(now)), None, "first"
    assert now > anchor["t1"]
    z = anchor["s"]*(price-a)
    if 0 < z < 2*d:
        return anchor, None, "wait_second"
    kind = "REV" if z <= 0 else "CONT"
    r = -anchor["s"] if kind == "REV" else anchor["s"]
    u, v = anchor["t1"]-anchor["t0"], now-anchor["t1"]
    assert u > 0 and v > 0
    event = dict(type=kind, fast=bool(v < u), r=int(r), t0=anchor["t0"],
                 t1=anchor["t1"], t2=int(now), a=a, d=d, u=int(u), v=int(v),
                 entry=float(price))
    return passage_anchor(now, price, atr), event, "event"


def passage_model():
    return dict(anchor=None, last=None, pending=[], bank=[])


def passage_advance(model, now, price, atr):
    """Mature before observing today's event. No orders/occupancy/model mode."""
    assert math.isfinite(price) and price > 0
    reset = model["last"] is not None and now != model["last"]+BAR
    if reset:
        model.clear()
        model.update(passage_model())
    matured = 0
    remaining = []
    for pending in model["pending"]:
        age = now-pending["t2"]
        assert age > 0 and age % BAR == 0 and age <= 6*BAR
        if age == 6*BAR:
            y = pending["r"]*(math.log(price)-math.log(pending["entry"]))
            assert math.isfinite(y)
            model["bank"].append(dict(type=pending["type"], fast=pending["fast"],
                                      y=float(y), t2=pending["t2"], matured=int(now)))
            if len(model["bank"]) > 240:
                model["bank"].pop(0)
            matured += 1
        else:
            remaining.append(pending)
    model["pending"] = remaining
    # This call is deliberately AFTER maturation and independent of atr validity.
    model["anchor"], event, action = passage_machine(model["anchor"], now, price, atr)
    if event is not None:
        model["pending"].append(dict(event))
    model["last"] = int(now)
    return event, dict(action=action, matured=matured, gap_reset=bool(reset),
                       reset_anchor_invalid=model["anchor"] is None)


def passage_bootstrap(rows):
    """Exactly1000 closed rows, row14 seed; replay once, never submit a trade."""
    assert len(rows) == 1000
    model, counts = passage_model(), {}
    for j in range(14, 1000):
        now = int(rows[j, 0])+BAR
        atr = atr14(rows[j-14:j+1])
        event, info = passage_advance(model, now, float(rows[j, 2]), atr)
        counts[info["action"]] = counts.get(info["action"], 0)+1
        counts["matured"] = counts.get("matured", 0)+info["matured"]
        counts["bars"] = counts.get("bars", 0)+1
        if event is not None:
            cell = event["type"]+("_FAST" if event["fast"] else "_SLOW")
            counts[cell] = counts.get(cell, 0)+1
            counts["ties"] = counts.get("ties", 0)+int(event["u"] == event["v"])
    return model, counts


def passage_forecasts(bank, event):
    """The SAME complete240 bank/shared20-cell domain for both conditional means."""
    if len(bank) != 240:
        return None
    cell = [item["y"] for item in bank
            if item["type"] == event["type"] and item["fast"] == event["fast"]]
    group = [item["y"] for item in bank if item["type"] == event["type"]]
    if len(cell) < 20 or not all(math.isfinite(v) for v in group):
        return None
    state, by_type = float(np.mean(cell)), float(np.mean(group))
    if not all(math.isfinite(v) for v in (state, by_type)):
        return None
    return dict(state_mean=state, type_mean=by_type, cell_n=len(cell), type_n=len(group),
                bank_first=bank[0]["t2"], bank_last=bank[-1]["t2"])


class BtcResearchR23PassageBase1m(BtcResearchR12ArBase1m):
    MODE = "abstract"

    def _passage_count(self, name, amount=1):
        stats = self.vars.setdefault("passage_runtime_counts", {})
        stats[name] = stats.get(name, 0)+amount

    def _passage_reset(self, reason):
        # A market-data discontinuity discards all predictive history. This is
        # NOT a second bootstrap and cannot cancel broker stops/time exits.
        self.vars["passage_model"] = passage_model()
        self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
        self._passage_count("invalid:"+reason)

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("STATE", "TYPE_CONTROL")
            self.vars["checked"] = True
            self._log("R23_PASSAGE_CONFIG", dict(mode=self.MODE, bootstrap_rows=1000,
                      seed_row=14, bank=240, cell_min=20, horizon_hours=24,
                      stop_atr=2, target=None, risk=.02, aggregate=.06,
                      leverage=3, fee=.00045, feature="observed_type_fast_not_pure_speed"))
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR or now > self.FINISH:
            return
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        if not self.vars.get("passage_bootstrapped"):
            rows = closed_window(candles, now, 1000)
            if (rows is None or not np.all(rows[:, 0] % BAR == 0)
                    or not math.isclose(float(rows[-1, 2]), float(self.price),
                                        rel_tol=1e-10, abs_tol=1e-8)):
                self._passage_count("bootstrap_wait")
                return
            model, counts = passage_bootstrap(rows)
            self.vars["passage_model"] = model
            self.vars["passage_bootstrap_counts"] = counts
            self.vars["passage_bootstrapped"] = True
            self.vars["passage_initialized_at"] = now
            self._log("R23_PASSAGE_BOOTSTRAP", dict(time=now, counts=counts,
                      bank=len(model["bank"]), pending=len(model["pending"])))
            # The last replay event is mathematical, never a queued first trade.
            return
        rows = closed_window(candles, now, 15)
        if rows is None or not np.all(rows[:, 0] % BAR == 0):
            self._passage_reset("ohlc_or_clock")
            return
        if not math.isclose(float(rows[-1, 2]), float(self.price),
                            rel_tol=1e-10, abs_tol=1e-8):
            self._passage_reset("asof_price")
            return
        model = self.vars["passage_model"]
        atr = atr14(rows)
        # ATR0/None blocks ONLY new anchor/order; old pending and frozen-d phase
        # still advance on this valid close. Never return before this call.
        event, info = passage_advance(model, now, float(rows[-1, 2]), atr)
        self._passage_count("bars")
        self._passage_count(info["action"])
        self._passage_count("matured", info["matured"])
        self._passage_count("gap_reset", int(info["gap_reset"]))
        if event is None:
            return
        self._passage_count(event["type"]+("_FAST" if event["fast"] else "_SLOW"))
        self._passage_count("ties", int(event["u"] == event["v"]))
        forecasts = passage_forecasts(model["bank"], event)
        if forecasts is None:
            self._passage_count("insufficient_bank_or_cell")
            return
        mean = forecasts["state_mean"] if self.MODE == "STATE" else forecasts["type_mean"]
        score = event["r"]*mean
        if abs(score) <= .0019 or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        if atr is None:
            self._passage_count("entry_atr_invalid")
            return
        direction = 1 if score > 0 else -1
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = direction
        self.vars["passage_evidence"] = dict(event=event, score=score, **forecasts)

    def on_open_position(self, order):
        super().on_open_position(order)
        entry = float(self.position.entry_price)
        direction = 1 if self.is_long else -1
        opened = int(self.position.opened_at)
        evidence = self.vars["passage_evidence"]
        self._log("R23_PASSAGE_OPEN", dict(mode=self.MODE, time=int(self.time),
                  entry=entry, actual_stop=entry-direction*self.vars["plan"]["distance"],
                  actual_opened=opened, position_deadline=opened+6*BAR,
                  label_deadline=evidence["event"]["t2"]+6*BAR,
                  evidence=evidence))

    def _emit(self, stage):
        super()._emit(stage)
        model = self.vars.get("passage_model", passage_model())
        cells = {kind+("_FAST" if fast else "_SLOW"): sum(
                    item["type"] == kind and item["fast"] == fast for item in model["bank"])
                 for kind in ("REV", "CONT") for fast in (False, True)}
        anchor = model["anchor"]
        self._log("R23_PASSAGE_STATS", dict(stage=stage, mode=self.MODE,
                  initialized=self.vars.get("passage_initialized_at"),
                  bootstrap=self.vars.get("passage_bootstrap_counts", {}),
                  runtime=self.vars.get("passage_runtime_counts", {}),
                  bank=len(model["bank"]), cells=cells, pending=len(model["pending"]),
                  last=model["last"],
                  terminal_censored_labels=len(model["pending"]) if int(self.time) >= self.FINISH else 0,
                  incomplete_episode=anchor is not None,
                  first_passage_seen=bool(anchor is not None and anchor["t1"] is not None)))
```
