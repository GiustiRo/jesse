# AA — fuentes y cierres completos antes de implementación

Fecha2026-10-21. Archivo documental; cero nuevas fuentes de estrategia, jobs, drafts o economía. Materialidad y protocolo en revisión. Nombres futuros reservados: BtcResearchR27VolumeInteractionBase1m / BtcResearchR27VolumeInteraction1m / BtcResearchR27MainEffects1m. No se han creado. Padres y antecedentes leídos por MCP; textos completos propios, no papers externos. Y sólo fuente y protocolo; no resultados consultados para AA.

jesse://strategy fue leído completo mediante servidor jesse-local, incluyendo Trading Hours y adaptación24/7. El primer nombre incorrecto de servidor jesse_local fue un error semántico corregido, no conectividad. Adaptación nativa BTC continua documentada en protocolo; no calendario/horario/datos de acciones. Referencia externa sólo mediante enlaces en propuestaAA; no cita ni resumen repetido aquí.

## Índice SHA256 de fuentes

- BtcResearchR10Base4h: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9
- BtcResearchR11Base1m: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87
- BtcResearchR12ArBase1m: 1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343
- BTCExploreR804: 86bcb4297fed564346c949b7f02886a062134b20a75db32d35c657b6184c6692
- N204ExploreR501: c66bc848789a06a0c70c8915e613b2034cc0ef6254eb25c741eb172614992830
- ResearchV4ShockPV1h: 5694fb437896416ff34513c38a3c9844f0c26663263f7e30504ae7fadaa6e7b0
- BtcResearchR12ParticipationBase1m: 3928d2b3fd4ba9ffab43b89e134e982fb65e941cccaba9ba38e3c845bf9acfba
- BtcResearchR25VolumeLagBase1m: 437833f8ab078a24843b0ce326a4cd556bae8cdcb755be420febe648165251b7
- ResearchV5FundingFP4h: ef0ea4ff2e9e5444a5ee0da2d0a35d0c8d92a6d939172d24244aff15646edefd
- ResearchV4FundingFP1h: 61b5db6848d086b629be0122b435da89cc76850284db74f5d03207a7c6270358
- FundingWfPilotBase4h: 3a1c52ae84c7e5673a51c30de8dd6158c21a345f95ac391c8302e2713aeef28c
- strategies/ResearchV4Base1h/shock_features.py: 0ebf34769d0ad821e19773dfe5f6494398a0727ec5d1a93fc42c84472650a43b
- strategies/ResearchV5Base4h/funding_features.py: a9e7d666706c41624deebfd19d905331296efd9839f6d28e68a615cec82f12ce

## Fuente completa: strategies/BtcResearchR10Base4h/__init__.py

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

## Fuente completa: strategies/BtcResearchR11Base1m/__init__.py

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

## Fuente completa: strategies/BtcResearchR12ArBase1m/__init__.py

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

## Fuente completa: strategies/BTCExploreR804/__init__.py

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

## Fuente completa: strategies/N204ExploreR501/__init__.py

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


class N204ExploreR501(Strategy):
    """Frozen X03 R2 N204; original long runners retained.

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
        jh.debug('BTC_EXPLORE ' + json.dumps({'recipe': 'N501',
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
        self.vars['explore_event'] = {'side': 'short', 'kind': 'N501',
            'distance': distance, 'target_distance': 2 * distance, 'hold_hours': 48}
        audit = self.vars.setdefault('explore_audit', {})
        audit['events'] = audit.get('events', 0) + 1
        audit['events_occupied'] = audit.get('events_occupied', 0) + int(self.is_open)

    @staticmethod
    def _research_gate(c, window, q, vwap, decision_close):
        # Compare the price locations of selling and buying proxy cohorts.
        # These are OHLCV cohorts, not observed aggressor trades or inventory.
        negative = window[q < 0]
        if not len(negative):
            return False
        weight = float(np.sum(negative[:, 5]))
        other = float(np.sum(negative[:, 5] * np.mean(negative[:, [3, 4, 2]], axis=1)) / weight)
        return bool(math.isfinite(other) and other < vwap)

```

## Fuente completa: strategies/ResearchV4ShockPV1h/__init__.py

```python
from strategies.ResearchV4Base1h import ResearchV4Base1h
from strategies.ResearchV4Base1h.shock_features import features as shock_features


class ResearchV4ShockPV1h(ResearchV4Base1h):
    LINE = "SHOCK"
    USE_OI = False
    ATR_OFFSET_BARS = 1
    STOP_MULTIPLIER = 1.
    REWARD_MULTIPLE = 1.
    TARGET_MODE = "r_multiple"
    MAX_HOLD_BARS = 6
    # Signal neighbors change only these two; risk neighbors change only STOP.
    SHOCK_MULTIPLIER = 2.
    VOLUME_MULTIPLIER = 2.

    def features(self, candles, now, atr):
        return shock_features(candles, now, atr, self.SHOCK_MULTIPLIER, self.VOLUME_MULTIPLIER)

```

## Fuente completa: strategies/BtcResearchR12ParticipationBase1m/__init__.py

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

## Fuente completa: strategies/BtcResearchR25VolumeLagBase1m/__init__.py

```python
"""Y: temporal orientation of BTC volume/amplitude association, not order flow."""
import math
import numpy as np

from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def cell_key(values):
    return "/".join(str(int(v)) for v in values)


def all_cells():
    return {cell_key((s, q, d)): 0
            for s in (-1, 1) for q in (-1, 1) for d in (-1, 1)}


def volume_lag_features(rows):
    """One feature per endpoint from index25; each owns its25 paired samples."""
    assert rows.ndim == 2 and rows.shape[1] >= 6 and len(rows) >= 26
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        returns = np.diff(np.log(rows[:, 2]))
        magnitude = np.lib.stride_tricks.sliding_window_view(np.abs(returns), 25)
        log_volume = np.lib.stride_tricks.sliding_window_view(np.log(rows[1:, 5]), 25)
        # Same25 centers/scales in BOTH lag directions, independently per row.
        amean, vmean = magnitude.mean(axis=1), log_volume.mean(axis=1)
        asd, vsd = magnitude.std(axis=1, ddof=0), log_volume.std(axis=1, ddof=0)
        a = (magnitude-amean[:, None])/asd[:, None]
        v = (log_volume-vmean[:, None])/vsd[:, None]
        forward = np.mean(v[:, :-1]*a[:, 1:], axis=1)
        reverse = np.mean(a[:, :-1]*v[:, 1:], axis=1)
        symmetric, orientation = forward+reverse, forward-reverse
    raw = np.column_stack((returns[24:], symmetric, orientation))
    signs = np.where(np.isfinite(raw), np.sign(raw), 0).astype(np.int8)
    valid = (np.all(np.isfinite(magnitude), axis=1)
             & np.all(np.isfinite(log_volume), axis=1)
             # An exactly constant array can acquire a tiny std from mean
             # rounding (e.g. log(2)); reject mathematical degeneracy exactly.
             & ~np.all(magnitude == magnitude[:, :1], axis=1)
             & ~np.all(log_volume == log_volume[:, :1], axis=1)
             & np.isfinite(asd) & (asd > 0)
             & np.isfinite(vsd) & (vsd > 0)
             & np.all(np.isfinite(raw), axis=1)
             & np.all(signs != 0, axis=1))
    # log of nonpositive volume is already nonfinite; no pseudocount/epsilon.
    return dict(valid=valid, signs=signs, forward=forward, reverse=reverse,
                symmetric=symmetric, orientation=orientation)


def current_volume_feature(rows):
    features = volume_lag_features(rows)
    assert len(rows) == 26 and len(features["valid"]) == 1
    if not features["valid"][0]:
        return None
    return dict(state=tuple(int(x) for x in features["signs"][0]),
                forward=float(features["forward"][0]), reverse=float(features["reverse"][0]),
                symmetric=float(features["symmetric"][0]),
                orientation=float(features["orientation"][0]))


def volume_lag_forecasts(rows):
    """Exactly360 slots, ages6..365; row0 padding is deliberately unused."""
    assert len(rows) == 392
    features = volume_lag_features(rows)
    # Feature index0 ends at row25; endpoints26..385 are indices1..360.
    states = features["signs"][1:361]
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        labels = np.log(rows[32:392, 2])-np.log(rows[26:386, 2])
    valid = features["valid"][1:361] & np.isfinite(labels)
    assert len(states) == len(labels) == len(valid) == 360
    support = all_cells()
    for values in support:
        key = tuple(int(x) for x in values.split("/"))
        support[values] = int(np.sum(valid & np.all(states == key, axis=1)))
    evidence = dict(reason="current_feature_invalid", slots=360,
                    valid_origins=int(np.sum(valid)), support=support,
                    n_state=0, n_control=0)
    if not features["valid"][-1]:
        return None, evidence
    current = features["signs"][-1]
    selected = valid & np.all(states == current, axis=1)
    # Both policies start with the SAME all-three-signs/nonzero mask.
    control = valid & np.all(states[:, :2] == current[:2], axis=1)
    n_state, n_control = int(np.sum(selected)), int(np.sum(control))
    evidence.update(n_state=n_state, n_control=n_control,
                    current_state=[int(x) for x in current])
    if n_state < 20:
        evidence["reason"] = "insufficient_cell"
        return None, evidence
    state_mean, control_mean = float(np.mean(labels[selected])), float(np.mean(labels[control]))
    if not math.isfinite(state_mean) or not math.isfinite(control_mean):
        evidence["reason"] = "mean_invalid"
        return None, evidence
    evidence.update(reason="valid", state_mean=state_mean, control_mean=control_mean,
                    bank_first=int(rows[26, 0])+BAR, bank_last=int(rows[385, 0])+BAR,
                    last_target=int(rows[391, 0])+BAR)
    return dict(STATE=state_mean, SYMMETRIC=control_mean), evidence


def empty_diagnostic():
    return dict(last=None, pending=[], registered=0, matured=0,
                censored_gap=0, censored_terminal=0, terminal=False,
                cells={key: dict(n=0, sum_y=0., sum_sy=0.) for key in all_cells()})


def diagnostic_step(state, now, bar, feature):
    """Math-only ledger: mature six actual OHLC bars before any training gate."""
    if state["last"] is not None and now <= state["last"]:
        return state
    assert not state["terminal"]
    result = dict(state, pending=[], cells={k: dict(v) for k, v in state["cells"].items()})
    pending = state["pending"]
    gap = state["last"] is not None and now != state["last"]+BAR
    if gap or bar is None:
        result["censored_gap"] += len(pending)
        pending = []
    if bar is not None:
        assert int(bar[0])+BAR == now
        for item in pending:
            observed = dict(item, steps=item["steps"]+1)
            assert observed["steps"] <= 6
            if observed["steps"] == 6:
                assert now == observed["deadline"]
                label = math.log(float(bar[2]))-math.log(observed["price"])
                assert math.isfinite(label)
                cell = result["cells"][cell_key(observed["state"])]
                cell["n"] += 1
                cell["sum_y"] += label
                cell["sum_sy"] += observed["state"][0]*label
                result["matured"] += 1
            else:
                assert now < observed["deadline"]
                result["pending"].append(observed)
        if feature is not None:
            result["pending"].append(dict(origin=now, price=float(bar[2]),
                state=feature["state"], deadline=now+6*BAR, steps=0))
            result["registered"] += 1
    else:
        assert feature is None
    result["last"] = now
    assert len(result["pending"]) <= 6
    return result


def diagnostic_finish(state):
    """PRETERMINAL/FINAL may repeat: censor each remaining origin only once."""
    if state["terminal"]:
        return state
    return dict(state, pending=[], terminal=True,
                censored_terminal=state["censored_terminal"]+len(state["pending"]))


class BtcResearchR25VolumeLagBase1m(BtcResearchR12ArBase1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("STATE", "SYMMETRIC")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        diagnostic = self.vars.get("volume_diagnostic", empty_diagnostic())
        # Do not rewind/censor/recount on duplicate or earlier callbacks.
        if diagnostic["last"] is not None and now <= diagnostic["last"]:
            return
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        counts = self.vars.setdefault("volume_lag_counts", {})
        current_bar = closed_window(candles, now, 1)
        mismatch = current_bar is not None and not math.isclose(
            float(current_bar[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        # Route/as-of parity is integrity for diagnostic labels too, even when
        # the longer training history is unavailable. Never record stale prices.
        if mismatch:
            current_bar = None
            counts["price_alignment_invalid"] = counts.get("price_alignment_invalid", 0)+1
        feature_rows = None if mismatch else closed_window(candles, now, 26)
        feature = current_volume_feature(feature_rows) if feature_rows is not None else None
        capture = feature if self.START < now < self.FINISH else None
        self.vars["volume_diagnostic"] = diagnostic_step(
            diagnostic, now, None if current_bar is None else current_bar[-1], capture)
        for reason in ("feature_valid" if feature is not None else "feature_invalid",):
            counts[reason] = counts.get(reason, 0)+1
        if mismatch:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        # Diagnostic above must not depend on this longer historical window.
        rows = closed_window(candles, now, 392)
        if rows is None:
            counts["train_window_invalid"] = counts.get("train_window_invalid", 0)+1
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        forecasts, evidence = volume_lag_forecasts(rows)
        self.vars["volume_train_last"] = evidence
        reason = evidence["reason"]
        counts[reason] = counts.get(reason, 0)+1
        if forecasts is None:
            return
        forecast = forecasts[self.MODE]
        if abs(forecast) <= .0019 or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(rows)
        if atr is None:
            counts["atr_invalid"] = counts.get("atr_invalid", 0)+1
            return
        direction = 1 if forecast > 0 else -1
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            counts["plan_invalid"] = counts.get("plan_invalid", 0)+1
            return
        assert feature is not None
        self.vars["plan"] = dict(plan, volume_evidence=evidence, volume_feature=feature,
                                forecast=forecast, forecast_origin=now)
        self.vars["direction"] = direction

    def on_open_position(self, order):
        super().on_open_position(order)
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        self._log("R25_VOLUME_OPEN", dict(time=int(self.time), mode=self.MODE,
            forecast=plan["forecast"], forecast_origin=plan["forecast_origin"],
            forecast_deadline=plan["forecast_origin"]+6*BAR,
            opened_at=int(self.position.opened_at),
            hold_deadline=int(self.position.opened_at)+6*BAR,
            stop=float(self.position.entry_price)-direction*plan["distance"],
            distance=plan["distance"], risk_budget=plan["risk_budget"],
            feature=plan["volume_feature"], evidence=plan["volume_evidence"]))

    def _emit(self, stage):
        diagnostic = self.vars.get("volume_diagnostic", empty_diagnostic())
        if stage in ("PRETERMINAL", "FINAL"):
            diagnostic = diagnostic_finish(diagnostic)
            self.vars["volume_diagnostic"] = diagnostic
        super()._emit(stage)
        self._log("R25_TRAIN_STATS", dict(stage=stage, mode=self.MODE,
            counts=self.vars.get("volume_lag_counts", {}),
            last=self.vars.get("volume_train_last", {}),
            signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
            occupied=self.vars.get("occupied", 0)))
        self._log("R25_DIAG_STATS", dict(stage=stage, last=diagnostic["last"],
            registered=diagnostic["registered"], matured=diagnostic["matured"],
            censored_gap=diagnostic["censored_gap"],
            censored_terminal=diagnostic["censored_terminal"],
            pending=len(diagnostic["pending"]), terminal=diagnostic["terminal"]))
        # Bounded one-cell rows avoid truncating one large journal line.
        for key, values in diagnostic["cells"].items():
            self._log("R25_DIAG_CELL", dict(stage=stage, cell=key, **values))

```

## Fuente completa: strategies/ResearchV5FundingFP4h/__init__.py

```python
from strategies.ResearchV5Base4h import ResearchV5Base4h
from strategies.ResearchV5Base4h.funding_features import features, exit_state


class ResearchV5FundingFP4h(ResearchV5Base4h):
    LINE = "FUNDING_TREND"
    USE_OI = False
    PRICE_SMA_PERIOD = 120
    RETURN_LAG = 30
    FUNDING_COUNT = 3
    STOP_MULTIPLIER = 3.
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 180
    TARGET_MODE = "none"

    def features(self, candles, now, atr):
        result = features(candles, now, atr, self.get_funding_history(count=self.FUNDING_COUNT),
                          self.settled_funding_rate, self.settled_funding_timestamp,
                          self.PRICE_SMA_PERIOD, self.RETURN_LAG, self.FUNDING_COUNT)
        evidence = result["evidence"]
        event = evidence["settled_at"]
        # Deduplicate publication evidence only. Repeated funding states remain eligible.
        if event is not None and event != self.vars.get("funding_logged_timestamp"):
            self.vars["funding_logged_timestamp"] = event
            self._log_json("V5_FUNDING_PUBLICATION", dict(time=now, **evidence))
        return {key: result[key] for key in ("valid", "direction", "reason", "details")}

    def manage_position(self, atr):
        # The core enforces post-fill timing. Funding and price invalidity are independent.
        state = exit_state(self.candles, int(self.time), 1 if self.is_long else -1,
                           self.get_funding_history(count=1), self.settled_funding_rate,
                           self.settled_funding_timestamp, self.PRICE_SMA_PERIOD, self.RETURN_LAG)
        if state["reason"]:
            self._log_json("V5_FUNDING_EXIT_STATE", dict(time=int(self.time),
                opened_at=int(self.position.opened_at), direction=1 if self.is_long else -1, **state))
            self.request_exit(state["reason"])

```

## Fuente completa: strategies/ResearchV4FundingFP1h/__init__.py

```python
from strategies.ResearchV4Base1h import ResearchV4Base1h
from strategies.ResearchV4Base1h.funding_features import features, ma24_state


class ResearchV4FundingFP1h(ResearchV4Base1h):
    LINE = "FUNDING_RESET"
    STOP_MULTIPLIER = 2.
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 72
    TARGET_MODE = "none"
    EXTREME_Z = 1.
    RESET_Z = .5

    def features(self, candles, now, atr):
        result = features(candles, now, atr, self.get_funding_history(count=32),
                          self.settled_funding_rate, self.settled_funding_timestamp,
                          self.vars.get("funding_last_seen"), self.EXTREME_Z, self.RESET_Z)
        self.vars["funding_last_seen"] = result["next_seen"]
        if result["event_new"]:
            event = result["event"]
            # New rejected events are logged too; canonical halves preserve evidence below1900chars.
            self._log_json("V4_FUNDING_EVENT", dict(time=now, settled_at=event["settled_at"],
                reason=result["reason"], valid=result["valid"], direction=result["direction"],
                sha256=event["sha256"], count=len(event["window"]), details=result["details"]))
            for index in (0, 1):
                self._log_json("V4_FUNDING_WINDOW", dict(time=now, settled_at=event["settled_at"],
                    sha256=event["sha256"], part=index, rows=event["window"][index*16:(index+1)*16]))
        return {key: result[key] for key in ("valid", "direction", "reason", "details")}

    def manage_position(self, atr):
        # Core enforces T>opened_at; the exit is an adverse state, not a crossing latch.
        state = ma24_state(self.candles, int(self.time))
        if state is not None and ((self.is_long and state["close"] < state["sma24"]) or
                                  (self.is_short and state["close"] > state["sma24"])):
            self._log_json("V4_FUNDING_EXIT_STATE", dict(time=int(self.time),
                opened_at=int(self.position.opened_at), direction=1 if self.is_long else -1, **state))
            self.request_exit("ma24_adverse")

```

## Fuente completa: strategies/FundingWfPilotBase4h/__init__.py

```python
import json

import numpy as np

from jesse import utils
from jesse.strategies import Strategy


class FundingWfPilotBase4h(Strategy):
    """Frozen mechanical price control; no claim of a demonstrated trading edge."""

    FUNDING_FILTER = False
    DAY_MS = 86_400_000
    STOP_FRACTION = 0.02
    TARGET_FRACTION = 0.04
    RISK_PERCENT = 2
    MAX_HOLD_MS = DAY_MS
    REFERENCE_EVENTS = 30
    EXTREME_Z = 2.0

    def before(self):
        day = int(self.time) // self.DAY_MS * self.DAY_MS
        candles = self.candles
        # Only the previous completed UTC day supplies the breakout boundaries.
        previous = candles[(candles[:, 0] >= day - self.DAY_MS) & (candles[:, 0] < day)]
        direction = 0
        if len(previous) == 6 and len(set(previous[:, 0])) == 6:
            assert max(previous[:, 0]) + 4 * 3_600_000 <= self.time
            upper = float(np.max(previous[:, 3]))
            lower = float(np.min(previous[:, 4]))
            direction = 1 if self.price > upper else -1 if self.price < lower else 0

        rows = self.get_funding_history(count=self.REFERENCE_EVENTS + 1)
        assert all(row["available_at"] <= self.time for row in rows)
        valid = False
        adverse = False
        zscore = None
        if len(rows) == self.REFERENCE_EVENTS + 1:
            latest = rows[-1]
            reference = np.array([row["rate_decimal"] for row in rows[:-1]], dtype=float)
            deviation = float(np.std(reference, ddof=0))
            # Equal historical rates do not define a standardized surprise.
            # This frozen pilot requires nonzero dispersion in filtered entries.
            if np.ptp(reference) > 0 and deviation > 0 and np.isfinite(deviation):
                zscore = (latest["rate_decimal"] - float(np.mean(reference))) / deviation
                valid = bool(np.isfinite(zscore))
                adverse = valid and (
                    (direction == 1 and latest["rate_decimal"] > 0 and zscore > self.EXTREME_Z)
                    or (direction == -1 and latest["rate_decimal"] < 0 and zscore < -self.EXTREME_Z)
                )

        opportunity = direction != 0 and self.vars.get("entry_day") != day and self.is_close
        allowed = opportunity and (not self.FUNDING_FILTER or (valid and not adverse))
        self.vars["context"] = {"day": day, "direction": direction, "allowed": allowed}
        audit = self.vars.setdefault("audit", {
            "bars": 0, "price_opportunities": 0, "adverse_blocks": 0,
            "unavailable_blocks": 0, "entries": 0,
        })
        audit["bars"] += 1
        if opportunity:
            audit["price_opportunities"] += 1
            if self.FUNDING_FILTER and not valid:
                audit["unavailable_blocks"] += 1
            elif self.FUNDING_FILTER and adverse:
                audit["adverse_blocks"] += 1

    def should_long(self):
        context = self.vars["context"]
        return context["allowed"] and context["direction"] == 1

    def should_short(self):
        context = self.vars["context"]
        return context["allowed"] and context["direction"] == -1

    def _enter(self, direction):
        stop = self.price * (1 - direction * self.STOP_FRACTION)
        # Budget price loss plus both execution fees at the stop; funding and
        # slippage remain additional costs. Cap notional at available capital.
        capital = self.available_margin
        unit_loss = abs(self.price - stop) + self.fee_rate * (self.price + stop)
        notional = min(capital, capital * self.RISK_PERCENT / 100 / unit_loss * self.price)
        qty = utils.size_to_qty(notional, self.price, precision=8)
        self.vars["entry_day"] = self.vars["context"]["day"]
        if direction == 1:
            self.buy = qty, self.price
        else:
            self.sell = qty, self.price

    def go_long(self):
        self._enter(1)

    def go_short(self):
        self._enter(-1)

    def on_open_position(self, order):
        direction = 1 if self.is_long else -1
        entry = self.position.entry_price
        self.stop_loss = abs(self.position.qty), entry * (1 - direction * self.STOP_FRACTION)
        self.take_profit = abs(self.position.qty), entry * (1 + direction * self.TARGET_FRACTION)
        self.vars["audit"]["entries"] += 1

    def update_position(self):
        if self.time - self.position.opened_at >= self.MAX_HOLD_MS:
            self.liquidate()

    def should_cancel_entry(self):
        return False

    def before_terminate(self):
        self.log("PILOT_AUDIT " + json.dumps(self.vars.get("audit", {}), sort_keys=True))

```

## Helper completo: strategies/ResearchV4Base1h/shock_features.py

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

## Helper completo: strategies/ResearchV5Base4h/funding_features.py

```python
"""Persistent carry state; no entry-event latch and no estimated future funding."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV5Base4h import BAR, closed_window

EIGHT_HOURS = 28800000
JITTER_MS = 1000


def _number(value):
    if isinstance(value, (bool, str)) or not isinstance(value, (int, float, np.integer, np.floating)):
        return None
    value = float(value)
    return value if math.isfinite(value) else None


def _timestamp(value):
    number = _number(value)
    return int(number) if number is not None and number >= 0 and number == int(number) else None


def funding_state(history, now, current_rate, current_timestamp, count=3):
    """Public final rows only. count1 is deliberately independent for protective exits."""
    valid_input = isinstance(history, (list, tuple))
    source = history[-count:] if valid_input else []
    rows = [[_timestamp(r.get("settled_at")), _timestamp(r.get("available_at")),
             _number(r.get("rate_decimal"))] if isinstance(r, dict) else [None, None, None]
            for r in source]
    digest = hashlib.sha256(json.dumps(rows, separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    result = dict(valid=False, reason="funding_history_count", rows=rows, sha256=digest,
                  settled_at=_timestamp(current_timestamp), direction=0)
    if not valid_input or len(history) != count or len(rows) != count:
        return result
    if any(t is None or a is None or rate is None for t, a, rate in rows):
        result["reason"] = "funding_history_invalid"
        return result
    if any(a <= t or a > now for t, a, rate in rows):
        result["reason"] = "funding_unpublished"
        return result
    if any(abs(right[0] - left[0] - EIGHT_HOURS) > JITTER_MS
           for left, right in zip(rows, rows[1:])):
        result["reason"] = "funding_history_gap"
        return result
    event, available, rate = rows[-1]
    if event != _timestamp(current_timestamp) or rate != _number(current_rate):
        result["reason"] = "funding_accessor_mismatch"
        return result
    # The prior event remains usable at the boundary before the new final rate is published.
    if not 0 < now - event <= EIGHT_HOURS + JITTER_MS:
        result["reason"] = "funding_event_age"
        return result
    direction = 1 if all(r[2] < 0 for r in rows) else -1 if all(r[2] > 0 for r in rows) else 0
    reason = "funding_state" if direction else "funding_zero" if any(r[2] == 0 for r in rows) else "funding_mixed"
    result.update(valid=True, reason=reason, direction=direction,
                  available_at=available, rate_decimal=rate)
    return result


def price_state(candles, now, sma_period=120, return_lag=30):
    """Twenty-day mean and five-day return require120 closes, not151."""
    if (isinstance(sma_period, bool) or isinstance(return_lag, bool) or
            not isinstance(sma_period, int) or not isinstance(return_lag, int) or
            sma_period < 1 or return_lag < 1):
        return dict(valid=False, reason="price_parameters_invalid")
    rows = closed_window(candles, now, max(sma_period, return_lag + 1))
    if rows is None:
        return dict(valid=False, reason="price_window_invalid")
    close, reference = float(rows[-1, 2]), float(rows[-return_lag-1, 2])
    with np.errstate(over="ignore", invalid="ignore"):
        average = float(np.mean(rows[-sma_period:, 2]))
    if not all(math.isfinite(v) for v in (close, reference, average)):
        return dict(valid=False, reason="price_arithmetic_invalid")
    direction = 1 if close > average and close > reference else -1 if close < average and close < reference else 0
    digest = hashlib.sha256(json.dumps(rows[:, :5].tolist(), separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    return dict(valid=True, reason="price_state" if direction else "no_setup_price",
                direction=direction, close=close, sma=average, reference=reference,
                sma_period=sma_period, return_lag=return_lag,
                first=int(rows[0, 0]), last=int(rows[-1, 0]), bars=len(rows), sha256=digest)


def features(candles, now, atr, history, current_rate, current_timestamp,
             sma_period=120, return_lag=30, funding_count=3):
    """Repeatable state: an unchanged published trio never consumes future decisions."""
    funding = funding_state(history, now, current_rate, current_timestamp, funding_count)
    result = dict(valid=False, direction=0, reason=funding["reason"], details={},
                  evidence=funding)
    if not funding["valid"]:
        return result
    price = price_state(candles, now, sma_period, return_lag)
    if not price["valid"]:
        result["reason"] = price["reason"]
        return result
    result["details"] = dict(price=price, funding_direction=funding["direction"],
        funding_settled_at=funding["settled_at"], funding_sha256=funding["sha256"])
    if not isinstance(atr, dict) or _number(atr.get("value")) is None or atr["value"] <= 0:
        result["reason"] = "atr_invalid"
        return result
    direction = price["direction"]
    reason = "setup"
    if not direction:
        reason = "no_setup_price"
    elif not funding["direction"]:
        reason = funding["reason"]
    elif direction != funding["direction"]:
        reason = "carry_sign_reject"
    result.update(valid=True, direction=direction if reason == "setup" else 0, reason=reason)
    return result


def exit_state(candles, now, direction, history, current_rate, current_timestamp,
               sma_period=120, return_lag=30):
    """Bad funding cannot disable a price exit; bad price cannot disable a funding exit."""
    funding = funding_state(history, now, current_rate, current_timestamp, 1)
    if funding["valid"] and direction * funding["rate_decimal"] > 0:
        return dict(reason="funding_adverse", funding=funding)
    price = price_state(candles, now, sma_period, return_lag)
    if price["valid"] and direction * (price["close"] - price["sma"]) <= 0:
        return dict(reason="trend_adverse", price=price, funding_quality=funding["reason"])
    return dict(reason=None, funding_quality=funding["reason"], price_quality=price["reason"])


def self_checks():
    """Synthetic prices/payments cover strict signs, state repetition and independent exits."""
    checks = 0

    def check(value):
        nonlocal checks
        assert bool(value)
        checks += 1

    now = 1000 * BAR
    event = now - BAR
    closes = 100. + np.arange(132)
    candles = np.array([[now - (132-i)*BAR, p, p, p+1, p-1, 1] for i, p in enumerate(closes)])
    history = [dict(settled_at=event-(2-i)*EIGHT_HOURS,
                    available_at=event-(2-i)*EIGHT_HOURS+60000,
                    rate_decimal=-.0001) for i in range(3)]
    atr = dict(value=2.)
    snapshot = json.dumps(history, sort_keys=True)
    untouched = candles.copy()

    def call(h=None, c=None, t=now, rate=-.0001, stamp=event, risk=atr, period=120, lag=30):
        return features(candles if c is None else c, t, risk,
                        history if h is None else h, rate, stamp, period, lag)

    result = call()
    check(result["valid"] and result["direction"] == 1)
    check(result == call())  # No hidden event-consumption state.
    check(result["details"]["price"]["bars"] == 120)
    check(result["details"]["price"]["reference"] == candles[-31, 2])
    check(result["details"]["price"]["sma"] == float(np.mean(candles[-120:, 2])))
    check(json.dumps(history, sort_keys=True) == snapshot)
    check(np.array_equal(candles, untouched))
    check(call(c=candles[-119:])["valid"] is False)
    check(call(c=candles[-120:])["direction"] == 1)
    for period, lag in ((108,27), (132,33)):
        r = call(period=period, lag=lag)
        check(r["direction"] == 1)
        check(r["details"]["price"]["reference"] == candles[-lag-1,2])
        check(r["details"]["price"]["bars"] == period)
    future = np.vstack([candles, [now,999,999,1000,998,1]])
    check(call(c=future) == result)
    changed = candles.copy()
    changed[:-120,1:5] *= .5
    check(call(c=changed) == result)
    changed = candles.copy()
    changed[-4,0] += 1
    check(call(c=changed)["reason"] == "price_window_invalid")
    check(call(t=now+1)["valid"] is False)
    for bad in (0., -1., float("nan"), float("inf")):
        check(call(risk=dict(value=bad))["reason"] == "atr_invalid")
    check(call(risk=None)["reason"] == "atr_invalid")
    # Sign reflection also swaps high/low, preserving valid positive OHLC.
    down = candles.copy()
    down[:,1] = 400-candles[:,1]
    down[:,2] = 400-candles[:,2]
    down[:,3] = 400-candles[:,4]
    down[:,4] = 400-candles[:,3]
    positive = [dict(r, rate_decimal=.0001) for r in history]
    check(call(h=positive,c=down,rate=.0001)["direction"] == -1)
    check(call(h=positive,rate=.0001)["reason"] == "carry_sign_reject")
    for rates, expected in (([0.,0.,0.],"funding_zero"),
                             ([-.0001,0.,-.0001],"funding_zero"),
                             ([-.0001,.0001,-.0001],"funding_mixed")):
        modified = [dict(r,rate_decimal=v) for r,v in zip(history,rates)]
        check(call(h=modified,rate=rates[-1])["reason"] == expected)
    check(call(h=history[:2])["reason"] == "funding_history_count")
    check(call(rate=.0001)["reason"] == "funding_accessor_mismatch")
    check(call(stamp=event+1)["reason"] == "funding_accessor_mismatch")
    for field,value,reason in (("rate_decimal",float("nan"),"funding_history_invalid"),
                               ("available_at",now+1,"funding_unpublished"),
                               ("available_at",event,"funding_unpublished"),
                               ("settled_at",history[-2]["settled_at"],"funding_history_gap")):
        modified=[dict(r) for r in history];modified[-1][field]=value
        check(call(h=modified)["reason"] == reason)
    modified=[dict(r) for r in history];modified[-1]["settled_at"]+=4
    check(call(h=modified,stamp=event+4)["direction"] == 1)
    check(funding_state(history,event+EIGHT_HOURS+1000,-.0001,event)["valid"])
    check(not funding_state(history,event+EIGHT_HOURS+1001,-.0001,event)["valid"])
    check(not funding_state(history,event,-.0001,event)["valid"])
    # Rate zero is neutral for open exposure; it is not a positive carry substitute.
    zero=[dict(history[-1],rate_decimal=0.)]
    check(exit_state(candles,now,1,zero,0.,event)["reason"] is None)
    check(exit_state(candles,now,1,positive[-1:],.0001,event)["reason"] == "funding_adverse")
    check(exit_state(down,now,-1,history[-1:],-.0001,event)["reason"] == "funding_adverse")
    check(exit_state(down,now,1,[],None,None)["reason"] == "trend_adverse")
    check(exit_state(candles,now,-1,[],None,None)["reason"] == "trend_adverse")
    check(exit_state(candles[-20:],now,1,positive[-1:],.0001,event)["reason"] == "funding_adverse")
    flat=candles.copy();flat[:,1:5]=[100.,100.,101.,99.]
    for direction in (-1,1):
        check(exit_state(flat,now,direction,[],None,None)["reason"] == "trend_adverse")
    # An adverse funding event takes priority when the price also wants to exit.
    check(exit_state(down,now,1,positive[-1:],.0001,event)["reason"] == "funding_adverse")
    huge=candles.copy();huge[:,1:5]=1e308
    invalid=call(c=huge)
    check(invalid["reason"] == "price_arithmetic_invalid")
    check(exit_state(huge,now,1,positive[-1:],.0001,event)["reason"] == "funding_adverse")
    check(json.loads(json.dumps(invalid,allow_nan=False))["valid"] is False)
    for prefix in ("V5_FEATURES ", "V5_FUNDING_PUBLICATION "):
        payload = {k:result[k] for k in ("valid","direction","reason","details")} if "FEATURES" in prefix else result["evidence"]
        check(len(prefix+json.dumps(dict(time=now,**payload),allow_nan=False,separators=(",",":"))) < 1800)
    return dict(status="passed", assertions=checks)

```

## Documento completo: strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_G_PROTOCOL_20261021.md
SHA256 27877aae6e18d406b89778dac42fec702190a64c484c2587237a0531303df5c6

```markdown
# Tanda G: respuesta autorregresiva frente a deriva media

Registrado antes de resultados G. Pregunta: ¿la dependencia de retornos previos añade valor sobre el simple promedio reciente al pronosticar24h BTC? Dos políticas prefijadas: AR1 y deriva sola, dos corridas económicas continuas. No usar resultadoFpara escoger umbrales. Hasta dos reemplazos sólo técnicos documentados, máximo dos motores y un análisis propio. No vecinos, grilla ni selecciónporlado/año.

## Antecedentes y diferencia
Transferencia explícita R20PaxgARResponse4h aBTC, con comparador de media para atribuir contribución AR; R20 excluyóBTC y recetaPAXG fue negativa. BtcAdaptiveTrend2h y BtcRegimeBreakout1h usan filtros de tendencia, no pronósticoAR. V6EFFICIENCY net/path no es autocovarianza. KalmanE es nivel latente y reversión de innovación, no ajuste de dependencia entre retornos. Ni un nombre estadístico ni transferir activo acreditan ventaja; se prueba contra control y puertas absolutas. No machinelearning/HMM ni librerías nuevas.

## Reglas invariables
242 cierres4h consecutivos=>241logretornos r; entrenamiento240pares x=r[:-1],y=r[1:] ya observados al cerrarT. AR OLS: beta=mean((x−meanx)*(y−meany))/varx; intercept=meany−beta*meanx. Forecastdesde último retorno, seis iteraciones v=intercept+beta*v y suma(v), sin clipping de beta. La última y ya fue observada en T y no es etiqueta futura. Control DRIFT: beta0,intercept=mean(y),forecast6*mean(y). Mismaventana/mismas241observaciones/mismos240y; sólo difiere la contribución de dependencia.

EntradaMARKETdirecciónforecast siabs(forecast)>.0019, umbralheredadoR20fijo antesde resultados. Es un umbral de admisión de señal, no un costo extra aplicado ni estrés/slippage simulado. Varx<=0/no finito=>noentryenambaspolíticas. Sin filtro macro/volumen/funding/OI, sin selección de dirección por atribución. En cada cierre4h reevalúa; ocupado descarta sincola, alclose de salida no reentra. Stop2ATR14simple congelado, sinTP para conservar el horizonte del modelo; liquidar24hdesdefill en cierres4h. StopintrabarM1, terminalmotorconfees. Tamaño2%feeawaredeR10, margen90%,floor8, no pirámide.

## Contrato
BTC-USDT Binance Perpetual Futures, ruta1mM1observer y datos4h, [2020-10-15,2026-01-01)UTC desarrollo reutilizado. Warmup3004h porque requiere242cierres; cambio técnico de suficiencia no selección de resultados ni riesgo. 10k,2%/6%/3xaislado, fee.00045porlado, funding históricoON aplicado/verificado snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 (proxiesmarcasdeclarados), slippage0. No estrés ni nuevas pruebas2026. Una posición; futurosgaps/fundingpuedensuperarriesgoprevisto.

ObservaciónR11wallet+PnLabierto porM1yfill;fronterasUTCpostfunding/predecisión, convenciónporfase, no agrupación estricta deeventospormes; DD M1+eventos no extremosintraminuto.62mesescompletos/20Qincluyendoinactivosenmediana.

## Gates y cierre
CAGR>=30%,PF>=1.2,DD<=25%(objetivo20%),M65activos,Q80completos,medianacalendario>0,netoaritméticoquitando2mejoresmeses>0,N>=100preliminar sinconfianzaporelconteo. Aspiraciones40–50%+yM70. Cada política debe cumplirpor sí misma; ganaralcontrolno basta. Sinpromociónoperativa niestresautomático.

AST, OLSsyntético AR exacto,controlmedia, pronósticorecursivo/seisiteraciones, varcero/causalidad/ventanas y source/readback/hash/config antesde economía. Auditoría posterior completa bruto−fees+funding=PNLsum=equityfinal−10k a1e−6, equityM1/cobertura/meses. Guardar fallos/reportesysubirHubíndiceúltimo. Si falla, cerrar estasrecetas ybuscarotra pregunta, no barrerbetas/ventanas/hurdles. Autonomía vigente hasta objetivo con límitesr9.

```

## Documento completo: strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_G_FINAL_20261021.md
SHA256 f23d675c8e1aee9fadfde9c3efc9fc0133848f60a760afa41d91840ef2405e82

```markdown
# Tanda G cerrada: dependencia AR no mejora la deriva media

Dos políticas predeclaradas con242cierres/240paresobservados ypronóstico6pasos. AR1 vscontrol6mean(y), mismohurdle.0019 heredado(señal,nocostoextra),stop2ATRsinTP/24h. Transferencia explícita deR20PAXG,norecetaBTCyaevaluada niinvención. BTC-USDTperpetuoBinance,[2020-10-15,2026-01-01),warmup3004hporlookback,desarrolloreutilizado.10k,2%/6%/3x,fee.00045+fundingconproxies,slippage0;sinestres/nuevaeconomía2026.

## BtcResearchR12Ar1m
Dashboard: http://localhost:9200/#/backtest/c72b53d8-c986-4131-814b-788cdc0f49e2

CAGR -7.4440%; neto -3320.40USDT; PF 0.9688; Sharpe -0.1392; DD M1+eventos 62.0354%; 1481 trades; meses activos positivos 27/62; trimestres 8/20. Mediana calendario -2.3918%; neto sin mejores2meses -8850.38USDT. NO_CUMPLE.

## BtcResearchR12Drift1m
Dashboard: http://localhost:9200/#/backtest/cbfafdb4-ea81-48f7-bd40-5ade91a3bfa4

CAGR -3.6236%; neto -1751.34USDT; PF 0.9830; Sharpe -0.0075; DD M1+eventos 56.1243%; 1355 trades; meses activos positivos 26/62; trimestres 8/20. Mediana calendario -1.7159%; neto sin mejores2meses -7507.85USDT. NO_CUMPLE.

Ambas pierden y excedenDD25%, no cumplenCAGR/PF/regularidad. La contribuciónARdeestaformulación no justifica conservarla. No cambiarventana,hurdle,beta,horas o seleccionarregímenes/ladosposteriorespararescate. Dos corridascerradas,ceroreemplazos. Mantenerobjetivoglobalautónomo,buscarotrapreguntamaterial.

Checkspreviostransformación/OLS240pares/forecast6/controlesvarcero ypasado:job9fdcbf0a81e94c4db9b50a909f34b509 passed,sourcehash1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343. Revisiónindependientesinerror. Auditoríajobf54b317db242406da4d9f5c6e544cb67 sobre1481/1355tradescompletos,bruto−fees+funding=PNLsum=finishing−10k a1e−6;fundingaplicado. TelemetríaM1completa,63intervalos/62meses/20Q,sumaPnL/equityfinalreconciliadas. DD M1+eventosnoextremosintraminuto;fronteraspostfunding/predecisiónsegúncontratoR11. ContadoropenpreterminalnosustituyetradesFINAL. MissingData: sinβportradeenlogs,porloquenoatribuimosresultadosarégimenβpositivo/negativo;noesnecesariopararechazarlascurvasnegativas.

Fuentes/config/manifiestoGguardadosantesdeejecutar. Sinframework/configglobal/live/paper/Pi. Evidencias BTC_DISCOVERY_G_PROTOCOL_20261021.md, BTC_DISCOVERY_G_MANIFEST_20261021.json, BTC_DISCOVERY_G_ACCOUNTING_20261021.json ytelemetrías. Ningunacandidata;Hyaestápredeclarada.

```

## Documento completo: strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_I_PROTOCOL_20261021.md
SHA256 8496d263ed520b25a6aabbe4608f557caebbd756c1c56408c16321d41b93d91e

```markdown
# Tanda I: vacío de participación y reparación del impulso

## Pregunta y presupuesto previo
¿Un desplazamiento fuerte con poco volumen, seguido por recuperación cuando regresa la participación, identifica una reversión BTC mejor que el patrón de precios solo? Esta es la porción creativa: se combina secuencia de precio y participación normalizada por hora, sin afirmar flujo real o liquidez observada. Dos políticas y exactamente dos corridas económicas; hasta dos reemplazos por fallos técnicos documentados, nunca por PnL. Máximo dos motores y un análisis propio. Sin vecinos ni optimización posterior.

## Antecedentes exactos
V4Shock: desplazamiento horario grande y ALTO volumen, reversión inmediata. BtcExploreR101: alto volumen>=2mediana30, rechazo y confirmación por encima del máximo de S, macro/operativa basal. RangeFade5m: flush con alto volumen y macro/gestión parcial. CAbsorption: alto volumen con cuerpo pequeño y escape posterior. AngleCombinedBtcVolume4h usa mediana28 días del mismo bloqueUTC como admisión del BTC basal. Aquí se contrasta el ORDEN baja participación durante desplazamiento y normalización durante recuperación, sin macro/RSI/canal ni receta basal. Los antecedentes fueron leídos; no se encontró equivalente económico de esta secuencia en fuentes revisadas. No demostrar novedad universal ni independencia estadística.

## Reglas congeladas
S=penúltima4h, B=última4h, P=cierre anterior aS. A=ATR14simple conocido antes deS. Impulso D=C_S−P, exigir abs(D)>=A. B debe devolver al menos50% del impulso y permanecer estrictamente antes de su reparación completa: f=(C_B−C_S)/(P−C_S), .5<=f<1. Dirección contraria aD, MARKET tras cierreB. No se interpreta secuencia intrabar desde OHLC.

PRICE: sólo ese patrón, con validez común de datos. PHASE: además V_S<=.5*mediana28delbloqueUTCdeS y V_B>=mediana28delbloqueUTCdeB. Ambas medianas se calculan con28 días anteriores de su propio bloque4h y están enteramente disponibles ANTES deS. Unir ventanas exige170OHLC4h; S está en posición168 yB169; referenciasS índices0,6,...162 yB1,7,...163. No usar S o B en sus propios baselines. Esto evita llamar anomalía a diferencias normales entre horarios.

Precios/candles cerrados consecutivos yvolúmenes170 finitos estrictamente positivos en ambas políticas. Una ausencia o volumen0 no se imputa y no se selecciona como vacío. Cada parejaS/B es evento independiente de estado, consumido aunocupado; no cola, no reentrada al salir en mismo cierre. Ventanas se solapan y no son muestras independientes.

Protección común: stop2A congelado, TP2R, vencimiento48h en cierres4h. TP puede superar la reparación del impulso: se prueba la hipótesis de persistencia posterior a la recuperación inicial, no una orden al precio previo. Una posición sinpirámides. SizingR10feeaware2%, margen90%,floor8. Gaps/funding pueden exceder riesgo esperado.

## Contrato y puertas
BTC-USDT Binance Perpetual Futures, ruta1m observador ydatos4h,warmup2404h;[2020-10-15,2026-01-01)UTC desarrollo ampliamente reutilizado. Capital10k,2%/6%/3xaislado,fee.00045porlado, funding históricoON aplicado/verificado snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 con marcasproxy declaradas;slippage0. Sin estrés,variantesriesgo,nuevaeconomía2026,ML/HMM,live/paper/Pi/configglobal.

MediciónR11 wallet+PnLabierto porM1 yfill; fronteras00:00UTCpostfunding/predecisión, convenciónporfase; DD M1+eventos no todoslos extremosintraminuto. Mesescalendario inactivos incluidos en mediana. Gatesr9:CAGR>=30%,PF>=1.2,DD<=25%(objetivo20%),M65activos,Q80completos,medianacalendario>0,netoquitando2mejoresmeses>0,N>=100preliminar sinconfianzaporelconteo. Aspiraciones40–50%+/M70. Ganar alcontrol no basta;cada política porseparado. Si falla economía NO_CUMPLE; si economía favorable pero poca muestra INCONCLUSA. Si noparticipación, informar sin fingir rechazo de toda familia. Estrés sólo tras candidata y acuerdo.

## Verificación y cierre
ChecksAST, señales espejo, f=.5/f<1, exclusión deS/B de baselines porUTC,volumen0/NaN inválidos, ATRpreS sincontaminación,asof/gaps/futuro,sizing/protección y revisión independiente antes de economía. Fuentes/readback/hash/config enmanifiesto previo. Auditoría completa posterior: bruto−fees+funding=PNLsum=equityfinal−10k a1e−6,2.741.760marcasM1/63intervalos/62meses/20Q ytelescopíamensual. ReportesMCP yHubíndiceúltimo. Si falla, cerrar receta y vecinos locales; seguir con otra pregunta material dentro del objetivo autónomo, no bajar puertas ni ampliar presupuesto para aprobar.

```

## Documento completo: strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_I_FINAL_20261021.md
SHA256 3f4335eebf72ddfdc9e783567fb6fac05385de027609e3a5f825c869d19a14c0

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

## Documento completo: strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_Y_PROTOCOL_20261021.md
SHA256 f4efdd64b3b85da4a85a8d3a989a5a36498967b914a71bdec0f8fc7107cb4e3b

```markdown
# BTC Discovery Y — protocolo documental de asociación temporal volumen/amplitud

Fecha: 2026-10-21. Estado: fuentes R25 implementadas y FULLcheck sintético PASSED tras revisión y autorización root/independiente. Todavía NO drafts/economía. Protocolo y precisiones T<=last/terminal/asof/constantes fueron guardados/releídos antes de cada fuente correspondiente. Revisión final de recibos antes de motores. Nombres reservados propuestos: BtcResearchR25VolumeLagBase1m, BtcResearchR25VolumeLagState1m, BtcResearchR25VolumeLagSymmetric1m. R24/X queda reservado al HOLD del proxy; no se renombra o sobrescribe.

Y se diseñó y documentó sin consultar resultados económicos de W. Se leyó Hub r22 y se reconocen sus campos stale de roadmap/blockers; no se deducen tareas pendientes de esos campos. Root conserva la publicación del Hub. Este documento no crea un permiso económico.

## 1. Hipótesis económica y falsación

Pregunta: ¿la orientación temporal de la asociación entre volumen BTC y magnitud de retorno modifica la continuación/reversión de la dirección actual y mejora un pronóstico de retorno BTC24h, frente a conservar la dirección actual y la asociación simétrica?

Hipótesis exploratoria: participación que antecede al reajuste de amplitud podría acompañar persistencia; actividad que aparece después del reajuste podría reflejar respuesta tardía y menor persistencia. No se observan atención, agentes, órdenes agresoras, información privada o liquidaciones. D no mide impacto causal ni identifica el origen de un episodio económico.

Debilidad principal: ambas variables son no direccionales y suelen describir o anticipar volatilidad antes que media de retorno. Sólo habría una justificación de señal si su relación temporal cambia la persistencia de la dirección actual. Otra transformación distinta no basta para autorizar una corrida. La relación propuesta puede ser nula, inestable o confundida por autocorrelación, tendencia intraventana, fase UTC, heterocedasticidad o ruido finito.

Falsación de la receta: si STATE no cumple gates r9, rechazar aunque haya una celda o año atractivo; no seleccionar subgrupos. Una utilidad incremental requiere además mayor retorno de libro que SYMMETRIC bajo ventana/capital/costos comunes, sin vender ese delta como significancia o causalidad. Que SYMMETRIC falle no vuelve bueno STATE. Si reproducen economía, registrar equivalencia y no contar evidencia independiente.

Diagnóstico narrativo predeclarado: persistencia s*y mayor con D positivo que negativo dentro de comparaciones de s/q con soporte sería compatible con la explicación anticipatoria. Si es opuesta, ausente o sin soporte, no sostener esa explicación ni cambiar su signo para encajar el resultado. El diagnóstico no orienta órdenes, no selecciona celdas, no modifica forecast/admisión y no constituye un nuevo motor o gate de p-values.

## 2. Contrato fijo y datos permitidos

Sólo BTC-USDT, Binance Perpetual Futures; trading route1m y data routeBTC4h. No ETH/SPY/PAXG u otros inputs. Datos existentes: sin inspección de velas, get_existing_candles, precheck de cobertura, importaciones, descargas o datasets nuevos. El motor informaría faltantes si se autorizara posteriormente. No scripts ni framework/global config.

UTC [2020-10-15,2026-01-01), capital10000USDT;2% objetivo por trade,6% agregado,3x aislado, una posición sin pirámides. Fee0,00045 por lado,taker con descuento para todos tipos. Funding BTC histórico ON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 aplicado/verificado con marcas proxy declaradas; slippage aplicado0. Neto tras fees/funding modelados, no todos costos reales.

Warmup4004h, fijado por lookback392 y ocho filas de margen; no por frecuencias observadas. No replay1000 ni preload de un banco de eventos. Cash inicial se conserva. START<decisión<FINISH para entradas; no consultar2026 para completar labels.

## 3. Característica causal de CADA origen

Cierre4h del origen i. Usar26cierres C_(i−25)..C_i y25volúmenes V_(i−24)..V_i. Por j=i−24..i:
r_j=log(C_j)−log(C_(j−1)).
a_j=abs(r_j).
v_j=log(V_j).

Exigir volúmenes finitos y estrictamente positivos en esas25barras; sin log1p, pseudocuentas, epsilon, winsorizar o imputar. OHLC finitos/positivos/consistentes y timestamps4h exactos. Las25observaciones forman cada serie emparejada. Calcular media25(a), media25(v), std25(a,ddof=0), std25(v,ddof=0). Desviaciones finitas>0 y toda aritmética finita. Rechazar además si las25magnitudes o25logV son exactamente iguales entre sí: np.all(serie==serie[:, :1],axis=1). Es integridad de varianza matemáticamente nula, sin epsilon/cutoff; evita que el redondeo de la media fabrique std>0 para una constante.

A_j=(a_j−media25(a))/std25(a).
Z_j=(v_j−media25(v))/std25(v).
F_i=mean24(Z_j*A_(j+1)).
R_i=mean24(A_j*Z_(j+1)).
S_i=F_i+R_i.
D_i=F_i−R_i.

Ambas direcciones usan los mismos centros y escalas de25, NO centros diferentes sobre cada par de24. Cada origen de entrenamiento recalcula su característica exclusivamente con SU PROPIA ventana26/25 terminada en i. Prohibido normalizar con todo el banco, con el origen actual o con información posterior a i. La característica actual usa su propia ventana; su normalización puede incluir su barra actual porque ya cerró.

Convención de diseño previamente fija:24observaciones anteriores equivalen a cuatro días de barras4h y se agrega la actual para obtener24pares de un lag4h. Las26filas de cierres abarcan100horas de precio; no se afirma que cuatro días sean un ciclo económico demostrado. No buscar otros lags/ventanas.

Estados: s_i=sign(r_i), q_i=sign(S_i), d_i=sign(D_i). Cero EXACTO de r/S/D, desviación<=0/no finita o aritmética no finita => característica inválida. Sin tercer estado, redondeo de signos, umbral a abs(S/D), banda de ruido ni fallback. La fragilidad flotante de signos cercanos a cero se declara, sin elegir tolerancia económica después.

Inversión temporal: invertir conjuntamente el orden de las25PAREJAS(a,v) conserva sus marginales/centros/escalas y asociación contemporánea; intercambia F y R, mantiene S e invierte D salvo error flotante. No es afirmación sobre ventanas rolling sucesivas con extremos distintos, sobre invertir sólo una variable o sobre invertir OHLC crudos. El diagnóstico algebraico no prueba información direccional.

## 4. Ventana de aprendizaje y validez común

Cada T4h usar392OHLCV cerradas consecutivas, current index391, última apertura=T−4h. Row0 es padding DELIBERADO SIN USAR en features/labels seleccionados:391filas bastarían si se reindexara, pero se conserva392 ya fijado. La integridad OHLC/timestamp de row0 SÍ se valida por closed_window392; una row0 inválida no conserva admisión. No mover entrenamiento para aprovechar esa fila.

Orígenes exactos i=26..385 inclusive,360slots con edades6..365barras respecto al current391. Para cada i, feature propia en cierres i−25..i (primer origen usa filas1..26) y25volúmenes i−24..i. Label:
y_i=log(C_(i+6))−log(C_i).
Targets32..391, todos conocidos a T. No entrenar con label del current391 ni adelantar madurez. El label describe precio bruto, no payoff con SL/costos/funding; no importar targetS.

Se conserva360 de antecedentes M/R/S para no escoger historia por frecuencia de ocho celdas:60días de orígenes4h, no60días independientes. Conservar exactamente360slots; excluir sólo orígenes con feature inválida o y no finito, sin buscar olderfill ni completar360válidos. Misma máscara válida para STATE y SYMMETRIC, incluyendo s/q/dtodosnozero aunque SYMMETRIC ignore d.

STATE: media simple de y_i con (s_i,q_i,d_i)==estadoactual.
SYMMETRIC: media simple de y_i con (s_i,q_i)==(s_actual,q_actual), usando TODOS los orígenes de esa misma máscara común, no reincorporar D0/invalid para el control.

Exigir n_celdaactual(s,q,d)>=20 en AMBAS políticas y ambas medias finitas; si falla, ambas cash. No exigir20en las otras siete celdas o completar casos viejos. El control conserva sólo sign(S), no su magnitud, las escalas originales ni todo régimen: no afirmar que es un control perfecto de la asociación simétrica. Ocho celdas y mínimo20 no acreditan potencia ni confianza.

Sin shrinkage, standard errors, SEgates, OLS, kNN, prior, weighting o selección de modelo. Reutilizar una tabla de celdas no es innovación ni motivo suficiente para más intentos. La pregunta versa sólo sobre la interacción económica propuesta.

Forecast>0,0019 LONG; forecast<−0,0019 SHORT; igualdades y banda central cash. Hurdle heredado es regla de señal, no costo extra debitado. No multiplicar la media raw y por s al generar órdenes: ya pronostica retorno BTC. s*y se usa sólo para diagnóstico narrativo. Cada4h es una oportunidad nueva, sin transición de estado adicional.

## 5. Reloj y diagnóstico narrativo separado

Procesar cada nueva frontera4h una sola vez. Para matemática/diagnóstico, T<=last es no-op antes de procesar datos: no retroceder reloj ni crear, madurar o censurar otra vez. El observer R11 conserva su llamada heredada por callback, sin modificarlo por esta deduplicación. T>last+BAR sí censura pendientes afectados por el salto; no se reordena ni rellena historia. Observación/feature/modelo avanzan aunque abierto, con pendingentry o sameexit. Señal ocupada se descarta sin cola, replay, pirámides o reversión; no entry en mismo timestamp de salida real.

El entrenamiento es stateless desde392filas en cadaT: no es un replay1000, banco online de eventos ni walk-forward posthoc. El siguiente registro diagnóstico sí es incremental y no cambia la estrategia:

1. Primero, en cadaT4h, validar el OHLC actual cerrado/asof y procesar pendientes anteriores ANTES de early-returns por feature, volumen, ATR o TRAIN392. Cada pendiente conserva T_origen,C_origen,s/q/d,deadline=T_origen+6BAR,últimoT y número de siguientes barras observadas.
2. Exigir exactamente seis cierres futuros4h consecutivos con OHLC íntegro/asof. Gap, timestamp desalineado o OHLC inválido censura los pendientes afectados; no esperar sólo el precio final, rellenar, madurar tarde o reetiquetar. La invalidez de volumen, de otra feature, std o ATR NO invalida un label cuyo camino de OHLC sea íntegro.
3. Al sexto cierre, agregar una vez y=log(C_T)−log(C_origen) y s*y en bounded counts/sum_y/sum_sy por(s,q,d). El origen sale de pending. No recorrer repetidamente los360orígenes de TRAIN para sumar estas estadísticas. Identidad única por T_origen/deadline mediante reloj monotónico, sin un seen-set infinito.
4. Después de madurar, si la característica de origen ACTUAL es válida en sus26filas y START<T<FINISH, registrar una sola pendiente actual ANTES de insuficiencia TRAIN/celda20/hurdle/ocupación/órdenes. Puede existir origen diagnóstico cuando la ventana TRAIN392 antigua es inválida pero su propia feature26 es válida; declarar esa diferencia de universo en el reporte. No condicionar a fills ni cobertura de las ocho celdas.
5. Hasta seis pendientes simultáneas después de madurar/agregar, ocho acumuladores de celda y contadores de validez/censura; sin guardar toda la historia de mercado. Universo diagnóstico runtime, sin bootstrap retrospectivo de warmup ni eventos anteriores a START. Terminal: pendientes sin seis barras válidas observadas hasta FINISH quedan censuradas; no engineextra, consultas2026 o callback inventado para completarlas. Separar censura de terminal frente a gap/OHLC. Censura terminal idempotente: PRETERMINAL/FINAL repetidos contabilizan cada pendiente una sola vez y dejan la cola vacía o marcada, sin madurar artificialmente a FINISH con un precio final no observado en callback4h.

El diagnóstico resulta igual en ambas políticas si reciben los mismos datos: nunca depende de wallet, posiciones o selección de señal. No es un tercer brazo económico ni un nuevo análisis de mercado autorizado ahora. Las medias agregadas por celdas y sus contrastes son descriptivas: observaciones temporalmente dependientes y seleccionadas en desarrollo, no ensayos independientes. Reportar soporte, no esconder celdas vacías ni fabricar diferencia cuando falte una direcciónD. No orientar estrategia con estas sumas.

## 6. Gestión heredada sin cambios

R10 entry_plan: capitalmax(0,balance)flat,available_margin,3x,fee-aware2%,margen90%,floor8decimales research; riesgo6% agregado no vinculante con una posición. Fee de entrada y stop incluidas en budget; sin reserva legacy0,001/lot0,001 de P/U.

MARKET al precio BTC actual en T4h, corroborado con cierre4h fresco. SL2ATR14SIMPLE BTC actual, media14TR de15OHLC; plan congela distance y fill real hereda stop relativo a entry_price. R12ArBase on_open_position intacto: assertion risk_budget con fees, sin TP, entrycount real y observeropen. Override heredado update_position: primerT4h con T−opened_at>=6BAR liquida; no cambiar por origen del forecast, nuevo estado, horario o volumen. Broker/proteccionesM1 siempre activos. No heredar accidentalmente TP2R/48h del R11.

ATR actual0/None impide plan, pero no madurar label diagnóstico, agregar origen featureválido o calcular TRAIN. Feature/data invalid no extiende posiciones/deadlines reales. Observer R11 completo, PRETERMINAL/FINAL tras comisión terminal; DDwallet+PnLabierto M1/fills, no todos extremos intraminuto. Fronteras mensuales por fase postfunding/predecisión. Labels y pronóstico bruto no representan funding/fees; ledger real sí.

## 7. Telemetría, controles futuros y gates

Resumen acotado por4h/FINAL: ventanasTRAIN válidas/invalid, features actuales válidas/invalid y razones, slots360/validorigins, n_celda/n_control, insuficiencia20, medias/score en fill real, signal/occupied/sameexit/entrycount real; diagnóstico registered/matured/censored_gap/censored_terminal/pending y count/sum_y/sum_sy de ocho celdas. No millones de logsM1 ni usar plan como fill. Contadores descriptivos no son evidencia de potencia.

Checks futuros, si root autoriza implementación más tarde: supplied-source AST/stubs sin importar estrategias reales/framework ni precios observados; oráculo S/D por inversión conjunta con centros25; normalización pororigen,392/row0unused/360slots/targets<=391/no label actual; vol0/log/σ0/rSD0/NaN/sharedmask/n20/controlSgrosero; reflexión de dirección s y rawlabel, hurdle exacto; pending único/madurez6/gapcensura/volumeinvalid-ATRinvalid-TRAINinvalid no impiden camino válido; sin contar train repetido o influir órdenes; gestión/sizing/fill/FINAL. Sin contador de assertions como validación económica.

Gates r9 CADA cuenta: CAGRnetobase>=30%,PF>=1,2,DD<=25%(objetivo20),M65mesesactivoscompletos positivos,Q80trimestrescompletos,mediana mensual calendario>0 incl inactivos,neto sin mejores2meses>0,N>=100 sólo operativo preliminar. Aspiraciones preservadas40–50%+/M70. No relajar al superar control. Auditoría fullsnapshot gross−fees+funding=PNLsum=equityfinal−10000, funding aplicado, M1/calendario/terminalfee conciliados; rolling12m y labels solapados no OOS ni independientes.

## 8. Deduplicación y cierre de presupuesto

Se leyó la propuesta Y y fuentes/cierres completos más cercanos, preservados en BTC_DISCOVERY_Y_CODES_AND_ANTECEDENTS_20261021.md:
- X804/BTCExploreR804: cambio de sumas contemporáneas V*ΔC en dos mitades, no contraste V_j*abs(r_(j+1)) frente a abs(r_j)*V_(j+1).
- N204/K1001/R1/R4/R5/R6/R8/P: cohortesVWAP, localización del cierre, eficiencia, ocupación y convivencia. No se rescata esa operativa ni se suma su runner.
- C/I: volumen sin avance/escape y secuencia low-volume impulso/high-volume reparación. Antecedente económico cercano, no novedad universal; no mover umbrales para relajar sus cierres.
- AngleVolume/Acceptance: nivel de volumen por fase u ocupaciónM1 ya explorados. No repetición ni otro umbral.
- D/X805/U: reloj de volumen y frontera de cohortes; no F−R. U cerrado, sin quitar ramas u otros clocks.
- V4shock/V5VWAP: shock simultáneo, media/dispersion ponderada; no orientación de asociaciones cruzadas.
- F/H/M/O/R/S/T/V/W: partición de saltos, geometría, orden de extremos, vecinoskNN/targetfee-only, faseUTC, VARretornosBTC/ETH y pasajes. Y no cambia ninguno de sus parámetros/modelos/labels/clocks. W sólo protocolo leído para dedup, sin resultados económicos usados para diseño.
- Tabla de medias/gate20 también aparecen en antecedentes: no es una familia de aprendizaje nueva.

Lectura dirigida y listado de estrategias sin truncar; no equivalencia concreta hallada, tampoco ausencia universal acreditada. No hay obligación de implementar por haber encontrado un observable distinto. Revisiones root/independiente pueden retirar Y documentalmente sin simulaciones.

Presupuesto PROPUESTO para aprobación posterior: exactamente dos economías STATE/SYMMETRIC, hasta dos reemplazos exclusivamente técnicos, nunca por PnL. Antes: fuentes nuevas/autorización, readback/hash/checks/revisión y manifiesto con campos reales. Máximo global2backtests y1análisis técnico simultáneos, coordinados con root; ningún slot usado por este documento. No motores/drafts autorizados ahora.

Tras dos resultados, cerrar sin vecinos25/360/20,lag,transformación/log,bandas,ceros/signos,S/D,magnitudes,labels/horizonte/costos/modelo/shrink,lados,fasesUTC/gestión/riesgo. No rescatar la hipótesis cambiando target a volatilidad si falló media. Conservar insuficiencia y fallo económico como hechos distintos, sin seleccionar celdas ganadoras.

X HOLD permanece en BTC_DISCOVERY_X_PROPOSAL_HOLD_20261021.md. Y propuesta previa permanece en BTC_DISCOVERY_Y_PROPOSAL_20261021.md como historial; este protocolo normativo posterior precisa row0unused, máscara, diagnóstico y causalidad. Fuentes nuevas R25 guardadas/readback exacto y2jobs técnicos succeeded (1probe y1fullcheck),0jobsfallidos. Cero drafts/economía o velas inspeccionadas; sin imports/datos nuevos/research_scripts/install/restart/global/framework/live/paper/Pi/nuevos2026.

## Precisión técnica antes del check final
Revisión root/independiente detectó paridad de precio sólo validada después de TRAIN392: corregida ANTES de madurar/capturar diagnóstico. Mismatch entre current4h y self.price (rel1e−10,abs1e−8 heredadas) es asof inválido: censura pending como integridad, no captura origen y bloquea nuevas entradas sin afectar protecciones.

Probe sintético bdc2d3c5c0294a7cbc97ca925e8c4894, NumPy1.26.4, encontró con V=2 constante exacta std(logV)=1.1102230246251565e−16 y feature espuria válida; por eso root aprobó guard de igualdad EXACTA en25logV y25magnitudes antes de fuente final. No se añadió tolerancia económica ni se eliminan signos pequeños no constantes. Versiones33d07… y8113… se preservan con motivo, código exacto de probe y artefacto, sin economía.

## Estado técnico completado, sin economía
FULLcheck7a53cb54457e4d478247cfae6dd4155b PASSED13grupos materiales al primer intento, NumPy1.26.4. Probe previo bdc2d3c5c0294a7cbc97ca925e8c4894 SUCCEEDED, evidencia degeneracyV2constante. Dosjobs técnicos totales,0jobsfallidos/0erroresharness, dos defectosfuente corregidos antesFULLcheck. Fuente final base437833f8ab078a24843b0ce326a4cd556bae8cdcb755be420febe648165251b7; wrappers State01c7aba73af2f10b5af06f46be016e0e90b34e9cb15aad494f97f64cb103b041 y Symmetric2913fee1da3cd5e219fcee4c6691d802716bdace2bccf07011c41537394261d1. PadresR10/R11/R12AR releídos intactos tras check.

Recibos permanentes: BTC_DISCOVERY_Y_TECHNICAL_RECEIPT_20261021.json (JSONestricto, códigos/jobs/artifacts exactos, RawNaNprobe como STRING, tresversionesfuente y motivos), BTC_DISCOVERY_Y_IMPLEMENTED_CODES_20261021.md (CODES final ysupersedidos), BTC_DISCOVERY_Y_TECHNICAL_PREPARATION_20261021.md. Antecedentes completos permanecen separados yreadback paginado exacto313513caracteres. Ningún resultado económico inferido de sintéticos; cobertura/funding/broker deben verificarse si root autoriza motores después de revisar recibos.

```

## Documento completo: strategies/FundingOiPilot4h/reports/RESEARCH_PROTOCOL_V1.md
SHA256 8262d7f10435ae44a4ca2faea7bc61bed501a7ed2b24b8cf04a0f4cb4b77c717

```markdown
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

## Documento completo: strategies/FundingOiPilot4h/reports/FINAL_DECISION_V1.md
SHA256 169d7eb87a1b473dc3a203b7c407d9c62588b83f2fe932d3a4a6137053adb3f8

```markdown
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

## Documento completo: strategies/FundingOiPilot4h/reports/FINAL_DECISION_V4.md
SHA256 d04a1a6790b5084cc9f94c779081a359372225cbc5091f731f851f43a00b007e

```markdown
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

## Documento completo: strategies/FundingOiPilot4h/reports/RESEARCH_PROTOCOL_V5_20261020.md
SHA256 cbb2139196f85009a98b70ac190143af36d869af8750e0c75b601c18e00252d1

```markdown
# V5 — prerregistro de cruces, VWAP móvil y carry persistente

Emitido 2026-10-21 00:47:53 UTC, antes de implementación y economía V5. El usuario pidió continuar explícitamente con V5 y V6 después del cierre V4. Esta autorización extiende el alcance anterior; no modifica V1–V4 ni abre 2026.

## Antecedentes y alcance

Hasta V4 se completaron 151 backtests económicos nuevos, 170 slots nominales con 19 reutilizaciones y 17 intentos técnicos. Ninguna candidata aprobó. CHANNEL_P de V3 dejó CAGR17,54%, PF1,35, DD18,41% y95 operaciones; no se baja el mínimo100 ni se reemplaza retrospectivamente el selector que eligió OI.

Todo2020–2025 está observado en investigaciones previas.2024–25 sólo será confirmación interna reutilizada, nunca OOS independiente.2026 permanece cerrado; la excepción K1001 no aplica. Sólo BTC-USDT Binance Perpetual Futures. Sin ML, RST no solicitado, live/paper, órdenes reales, Pi, cuentas, instalaciones, reinicios, CLI de investigación, cambios de configuración global, commits o push. Toda investigación, fuentes, sesiones y reportes por Jesse MCP local.

Tres sectores y dueños: CROSS /root/audit, VWAP /root/atr_oi, FUNDING_TREND /root/atr_p. Root mantiene núcleos, registro, auditoría financiera y selección. Máximo dos motores globales, dos por agente y dos jobs analíticos. No se inicia economía hasta compilación/checks y smoke de las tres líneas.

## Fuentes normativas y reglas únicas

V5_CROSS_PROPOSAL.md, V5_VWAP_PROPOSAL.md y V5_FUNDING_TREND_PROPOSAL.md se incorporan íntegros. Este documento ratifica las decisiones siguientes. No hay grilla ni alternativas ocultas.

CROSS: 4h. F0/F1=SMA20 actual/previa; S0/S1=SMA80 actual/previa. Long F1<=S1 yF0>S0; short F1>=S1 yF0<S0. Exactos81 cierres. Sin SMA200. Salida por cruce opuesto después del fill. No reversión ni latch: el cruce que cierra no se usa para entrar contrario en esa decisión o una posterior sin cruce nuevo. Stop fijo3ATR14 simple, sinTP/trailing, hold180barras4h=30d. Vecinos señal18/72 y22/88 cambian tanto entrada como salida; riesgo2.7/3.3ATR.

VWAP: 1h. Proxy HLC3 ponderado por volumen base en ventanas móviles24h actuales/previas propias. No es VWAP de ticks ni indicador anchoredD de Jesse. Pesos normalizados por máximo volumen, luego suma; dos pasadas media/varianza poblacional, sin epsilon/clamp. Ceros individuales permitidos, ventana toda cero inválida. S=max(desvío ponderado,ATR14simple), banda M±2S. Long C1<M1−2S1, M0−2S0<=C0<M0 yC0>C1; short espejo. Exactos25 cierres para entrada. Salida estado C0>=M0long/<=M0short, sóloT>fill, con24cierres válidos ysin exigirATR. Stop2ATRactual fijo, sinTP/trailing, hold24h. Vecinos señalK1.8/2.2; riesgo1.8/2.2ATR.

FUNDING_TREND: 4h. Estado de tendencia C0>SMA120 yC0>C30long, espejo short. Últimos tres pagos publicados estrictamente negativos long o positivos short. Tres pagos abarcan16h entre extremos; no baseline/zscore/reset. Ventana120cierres. Cada timestamp raw y tasa coinciden con accesores, separados8h±1000ms, available<=T y>settled_at; último0<edad<=8h+1000ms. Entrada por estado repetible; mismo trío puede habilitar otra decisión si plano/cupo libre. Deduplicar eventos sólo en evidencia, no consumir señal. Cero no abre ni obliga a cerrar. Salida por última tasa válida/fresca adversa (long>0,short<0), o precio<=SMA120long/>=SMA120short. Funding tiene prioridad sobre salida por precio; si funding inválido sigue activa salida de precio/stop/hold. Sólo después del fill. Stop3ATRfijo, sinTP/trailing, hold180barras30d. Vecinos señalSMA108/C27 ySMA132/C33, manteniendo tres pagos; riesgo2.7/3.3ATR.

Seis nombres/IDs/atributos nominales exactos en REGISTRY_V5.json. P es precio; PV incluye volumen; FP incluye funding. Cada pareja añade exclusivamente filtro OI creciente24h. No confundir FP/PV con controles de precio puro.

## Núcleos, datos, reloj y ejecución

Nuevos ResearchV5Base1h yResearchV5Base4h se derivan de la fuente congelada V4 para mantener no reentrada en misma decisión, prioridad calendario/hold/indicador, JSON acotado y auditoría de causas. Sólo se heredan hooks neutrales al reloj de ResearchV2Core4h, que permanece congelado. V1–V4 no se editan.

BAR1h=3600000 yBAR4h=14400000, DAY=86400000. Cada helper verifica velas cerradas, alineadas y consecutivas, última aperturaT−BAR; OHLC finitos positivos/coherentes. Aritmética finita tras medias/productos. Prefijos viejos y futuras filas no influyen. ATR se mantiene como media14TR sobre15OHLC, offset0. VWAP también calcula ATRprevio con ventana propia excluyendo última barra. Warmup240 velas de cada ruta (10d1h/40d4h), sin operar; suficiente para todas las ventanas y vecinos. No preinspeccionar velas: motor primero, importación MCP sólo ante error de datos.

Dataset funding 9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571; OI 6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf. Funding históricoON en todas las variantes, también sin filtro. Tasas finales publicadas asof, nunca tasa siguiente. Marcas exactas/proxy separadas.

OI por cada decisión incluyendo slots ausentes/cero/stale, sin warmup artificial. Referencia EXACTA T−24h:24 barras1h o6barras4h. Primeras24/6decisiones inicializan, primera referencia posible25ª/7ª; buffers26/8. Valores positivos, disponibilidad asumida etiqueta+6min y freshness10min desde disponibilidad; archivo retrospectivo noPIT. Precio sinOI no exige calidadOI. Retardo robusto adicional4h de reloj:4barras1h/1barra4h; currentT−4h/refT−28h con calidad de relojes originales ybuffers30/9.

Plan MARKET actual con capitalC=available_margin, preciop, distanciad ydireccións:
q=floor8(min(C/p,.02*C/[d+fee*(p+stop_pre)])), stop_pre=p−s*d>0.
Capital inicial10000 por sesión, isolated3x, capnocional1x; sin multiplicar q por leverage. Instalar stop desde fill real con d congelada. Riesgo previsto2%stop+ambosfees; funding/gaps/slippage pueden excederlo. Entrada de seguridad se conserva con costes yconsume cuota. Sin piramidar/parciales.

Una entrada ejecutada por díaUTC compartida longshort; no reentrada cuando v5_last_exit_at==T. start<T<finish yventanas activas a<T<b estrictas. Señal bloqueada no se difiere. Salidas intrabar protectoras según motor; decisión calendario, luego hold absoluto desde opened_at, luego indicador únicamenteT>opened_at. Final/folds cierran con costes. Fundingefectivo>=finish yvelas con apertura>=finish excluidos; cierreTfinish basado enúltima vela2025 no abre datos2026.

Fee nominal.00045, slippage0; debug/fast solicitadostrue yfast efectivo false por funding; exports/benchmarkfalse. Config completa congelada por sesión.

## A — screening

Seis sesiones continuas [2020-09-01,2024-01-01),cada una con10000. Gates sin cambios: N>=30,neto>0,PF dePNLneto>=1.2,DD absoluto del motor<=25%,almenos2/3años completos2021–23 positivos por equity.2020parcial se informa. CAGR de desarrollo descriptivo, sin gate nuevo.

Hasta dos finalistas por ranking menorDD absoluto,mayorPF,menorturnover,menosfeaturesOI,IDlex. Guardar shortlist/fuentes/config/hashes antes de economía2024–25V5. Sin elegibles se omiten fases futurasV5 yse conserva cierre negativo. El usuario autorizó V6 de forma separada: se completa según su prerregistro, sin reasignar slots V5 a nuevas variantes.

## B — walk-forward

Cuatro semestres2024H1/H2,2025H1/H2; trains expansivos desde2020Sep hasta comienzoeval. C1train reutilizaSCREEN si exacto. Para cada fold guardar gatestrain N30/net/PF/DD yselección global por ranking ANTESdeeval. Evaluar finalistas individuales permitido para diagnóstico; selección global no cambia por retorno futuro.

Hasta16slots (2finalistas×4×train/eval),incluye hasta2reutilizaciones. Wrapper sóloSTART/FINISH. Calendarios individuales de replay contienen semestres elegibles en train, distintos del selector global; sin seleccionar retrospectivamente según PNL de evaluación.

## C — replay y robustez

Hasta dos replays [2024-01-01,2026-01-01),731días,capital10000 continuo. Cuatro intervalos semestrales separados ycierres en todos bordes. OI/capital siguen continuos durante inactividad. Nominal candidato histórico requiere net>0,PF>=1.2,DD<=25,N>=100,>=3/4semestres positivos por equity yCAGR>=15% (convención365días). Meta orientativa20–30%anual, no garantía.

S1fee.0009/slip0;S2fee.00045/slip5;S3fee.0009/slip10bps. Motor completo con calendario nominal fijo, fee entra en sizing. S1/S3 net>0/DD<=25 obligatorios;S2 informativo. Cuatro vecinos por finalista, definidos arriba, todos net>0/DD<=25 requeridos. Señal y riesgo separados, sin elegir vecino ganador. RetardoOI4h también net>0/DD<=25;sinOI reutiliza nominal para ese slot. No modificar calendarios por costes o vecinos.

Sensibilidades proxy-only/globalfunding×.5/1.5 con cantidades fijas son descriptivas,no replays; fuentes desconocidas separadas. WF reescalado y replay comparados por operaciones/capital, sin vender sumas de sesiones reseteadas como cuenta continua.

## Presupuesto y auditoría

Máximo40slots económicos =6SCREEN+16WF+2REPLAY+6COST+8VECINOS+2LAG. Reutilizaciones cuentan slots, no motores nuevos. Hasta6técnicos: smoke7d2020Sep1→Sep8 por sector ycomo máximo un reemplazo por sector sólo por fallo técnico documentado. No usar PNL del smoke para cambiar reglas. Si no hay trade, no afirmar cobertura real de fills.

Antes de economía: compilar/AST/hashes, checks causales de cada señal/entrada/salida/overflow,bar1h/4h,OI24h/lag4h/slots,cuotaUTC/no reentrada,protecciónfill/riesgo+fees/cap,prioridadhold/calendario yJSON<=1900chars. Smoke engine con asserts en hooks según skill local. Fuentes/helpers nuevos porMCP; reportes.md save_strategy_report; JSON write_project_file.

Snapshotrun_analysis completo summary/metrics/trades/equity, sóloinputs/ youtput/. Nada de lectura proyecto/DB/env desde análisis, ni scripts persistentes. Validación estática con fuentes literales capturadas yAST, no importación de proyecto. Contabilidad tolerancia1e−6USDT, bruto−fees+funding=PNL/saldo, ledgerqty/mark/rate/effectiveclock yfeesfills/slippage. Reloj raw conserva jitter<=1000ms.

Logs completos, contadores por mes/dirección/features/causas, planes/cierres yprovenance. Equity diaria completa, años/semestres por calendario, PF sin duplicar trades, DDmotor ymuestreado terminal separados, Sharpe si disponible, gross/fees/funding,turnover/exposición/longshort/concentración. Zero-trades puede carecer de métricas/curvas: etiquetar ausencia, no fabricar meses/retornos.

Timeout de start: guardarraw, consultar mismoID tras recuperar lectura, jamás duplicar. Si MCPunavailable, suspender dependientes hasta lectura exitosa, sin workaround. No resets/restarts.

Estados SIN_CANDIDATA/RECHAZADA/FRÁGIL/INCONCLUSA/CANDIDATA_HISTÓRICA; criterios no se redondean ni se reducen para aprobar. Fuentes deV5secongelan después de checks yantes de economía. V6seprerregistra aparte antes de sus datos; se definirán sus mecanismos antes de los resultadosV5 para reducir selección adaptativa. El nuevo permiso amplía investigación, no convierte las reservas reutilizadas en evidencia independiente.

```

## Documento completo: strategies/FundingOiPilot4h/reports/FINAL_DECISION_V5.md
SHA256 5c870d2475bc57dde0fa982f03acfae842217fd99d25cf4aed989e2817f03520

```markdown
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

## Documento completo: strategies/FundingOiPilot4h/reports/BTC_NEXT_QUESTION_DEDUP_FUNDING_20261021.md
SHA256 ed1377b401218f1dae92a8831d574c142d92848b8ec1032bcc64472bf0cede13

```markdown
# Descarte previo de posible pregunta: carry funding BTC

No constituye U ni corrida nueva. Revisión sólo lectura de fuentes y decisiones por btc_next_material;0jobs/0datosobservados/0estrategias. Se conserva para evitar repetir trabajo.

ResearchV5Base4h/funding_features.py YA define Persistent carry state:3pagos publicados negativos→long,positivos→short,available_at<=now,secuencia8h,freshness8h+1s,precioSMA120/retorno30alineado,salida funding_adverse porúltimopago. ResearchV5FundingFPReplay4h sinOI:[replay](http://localhost:9200/#/backtest/ff2f12bf-1faf-4bec-808f-800a778421a4),107trades,CAGR−1.043844%,PF.960575,net−207.96,fundingfavorable+167.58. FINAL_DECISION_V5 cierra nominal,costos,vecinos y40slots.

FundingWfPilotFiltered4h comparó breakoutprecio con/sinveto fundingadversoextremo(últimopagovs30previos),OI_PILOT_RESULTS_20261020 cierrarescatesporumbral. ResearchV4FundingFP1h/funding_features.py fundingextremonormalizado+confirmaciónprecio:[sesión](http://localhost:9200/#/backtest/fa6ee4dd-4ea8-434d-84a1-dbe0249c9068),26trades,−6.93%,PF.590;FINAL_DECISION_V4shortlistvacía. A_EVENTpostpagofallo454trades,CAGR−7.57%con fundingfavorable ya cerradoBTC_DISCOVERY_AB_FINAL_20261021.

Decisiónroot: no nuevo experimento de carrydireccional,filtroveto oclockpostpago;quitarfiltroprecio,cambiarcantidadpagos/signo sería vecino de líneas cerradas. No tocarlabelsSfunding nirescatarsulínea. Conteoseconómicossincambios.

```

## Documento completo: strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_Z_DOCUMENTAL_DEDUP_NO_EXPERIMENT_20261021.md
SHA256 2ff7e92afd450f03d20cb58d422b969d5bf8797fdd229d25c0ab16b4a8a4dfe0

```markdown
# Próxima pregunta BTC: revisión documental Z sin experimento seleccionado

Fecha: 2026-10-21. Estado: DESCARTE DOCUMENTAL; Z no tiene receta ejecutable, protocolo ni presupuesto económico aprobado. Este archivo registra trabajo de deduplicación y no cuenta como hipótesis nueva probada. Se elaboró sin consultar resultados Y. Cero fuentes nuevas de estrategia, jobs, drafts, importaciones o velas observadas.

## Decisión

No recomendar una nueva economía sobre funding acumulado. La hipótesis tentativa era que el coste de financiación ya pagado por un lado, combinado con resistencia del precio, informase sobre posterior reversión o continuación frente a un control de precio. La motivación económica sería presión de mantenimiento de posiciones apalancadas. Sin embargo, el dato no identifica quién mantuvo posiciones, su coste de entrada, patrimonio o liquidación: sumar tasas no mide el coste acumulado de una cohorte real.

La traducción concreta disponible sería otra persistencia/signo/magnitud o ventana de pagos publicados condicionada por precio. Eso permanece dentro de los mecanismos de carry, veto o normalización ya cerrados. No se encuentra aquí una diferencia estructural suficiente; cambiar una suma por tres signos, una ventana, normalización o tabla de medias no basta. No se autoriza un intento para averiguar si un vecino sale mejor.

Esta decisión no demuestra que todo funding carezca de información, ni que sea imposible otra pregunta material con datos existentes. Es una conclusión acotada sobre esta propuesta y los antecedentes consultados. Tampoco afirma un inventario exhaustivo de todas las fuentes del servidor.

## Comparación concreta

| Idea considerada | Antecedente exacto leído | Qué se conserva / diferencia tentativa | Decisión |
|---|---|---|---|
| Coste acumulado de financiación y resistencia del precio | ResearchV5FundingFP4h; ResearchV5Base4h/funding_features.py; RESEARCH_PROTOCOL_V5_20261020.md; FINAL_DECISION_V5.md | Misma fuente de tasas finales publicadas y condición de precio; sustituir persistencia de tres signos por acumulación/tamaño sería reformulación o vecino. V5 ya usa carry favorable alineado con SMA120/ROC30, salida por tasa o tendencia adversa. | Retirar; no control ni motor nuevo. |
| Veto de crowding a señal de precio | FundingWfPilotBase4h; RESEARCH_PROTOCOL_V1.md; BTC_NEXT_QUESTION_DEDUP_FUNDING_20261021.md | H1 ya bloquea precio con funding extremo adverso; H2/H3 combinan extremos o normalización y confirmación de precio. | Reutilizar evidencia; no cambiar umbral/suma para rescatar. |
| Descarga o reversión después de pago conocido | BtcResearchR10FundingEvent4h; BtcResearchR10Base4h previamente leído y congelado; BTC_DISCOVERY_AB_FINAL_20261021.md | A_EVENT ya espera una barra completa tras pago publicado e invalida el movimiento del lado pagador. Otro reloj de pago o selección posterior de sentido sería vecino. | Cerrado sin candidata; no repetir. |
| Normalización de extremos de funding | ResearchV4FundingFP1h; FINAL_DECISION_V4.md | Receta V4 usa extremos normalizados, confirmación de precio y salida por SMA24. No convertir nueva agregación en supuesto input virgen. | Cerrado; no rescate. |
| Nueva tabla de OHLCV o lag volumen/amplitud | BTC_DISCOVERY_Y_PROTOCOL_20261021.md | Y ya pregunta si orientación temporal D añade a asociación simétrica S y dirección actual. Cambiar sólo ecuación, celda o ventana no acredita otro mecanismo económico. | No proponer por obligación. |
| Reapertura de proxy o aceptación/ocupación M1 | Hub r23 HANDOFF.md y BTC_DISCOVERY_W_FINAL_20261021.md | X está HOLD por producto/calendario; ocupación ya descartada por AngleCombinedBtcAcceptance4h según cierre root. No se reevalúa aquí esa fuente como novedad. | Preservar HOLD/descarte; no sustituir validación faltante por otro motor. |

El descarte previo de carry fue leído antes de decidir. Su decisión root explícita ya retiraba un nuevo experimento de carry direccional, veto o reloj postpago; quitar filtro de precio, cambiar número de pagos o signo tampoco queda pendiente.

## Evidencia económica que se reutiliza

V5 Funding sin OI ya tiene [replay continuo](http://localhost:9200/#/backtest/ff2f12bf-1faf-4bec-808f-800a778421a4): 107 trades, CAGR −1,043844%, PF 0,960575, neto −207,960651 USDT y funding favorable +167,581792 USDT. V5 completa nominal, costes, vecinos y selección bajo su contrato original; no cambiar el ranking cerrado ni atribuirle riesgo actual idéntico: usa cap nocional 1x y cuota diaria.

V4 funding sin OI [screening](http://localhost:9200/#/backtest/fa6ee4dd-4ea8-434d-84a1-dbe0249c9068): 26 trades, neto del período −6,93%, PF 0,590. Es resultado de screening 2020–2023, no CAGR ni confirmación 2024–2025. A_EVENT ya fue evaluada bajo riesgo de investigación actual y cerró negativa; ninguna se reejecuta para este documento.

Hub r23 registra W cerrada y 44 ejecuciones económicas por ID desde r9, no muestras independientes. Esto no incorpora Y: no se inspeccionaron sus resultados, sesiones ni datos para seleccionar esta decisión.

## Fuentes consultadas y límites

Ruta base de los documentos: strategies/FundingOiPilot4h/reports/.

- RESEARCH_HUB/index.json: revisión actual 20261021-r23.
- RESEARCH_HUB/revisions/20261021-r23/revision.json, HANDOFF.md y DISCOVERY_RESULTS.md.
- RESEARCH_HUB/revisions/20261021-r4/EXPLORATION_HISTORY.md.
- BTC_INDIVIDUAL_EVIDENCE_MATRIX_20261021.md.
- BTC_NEXT_QUESTION_DEDUP_FUNDING_20261021.md.
- BTC_DISCOVERY_AB_FINAL_20261021.md y BTC_DISCOVERY_CD_FINAL_20261021.md.
- BTC_DISCOVERY_K_FINAL_20261021.md, BTC_DISCOVERY_L_FINAL_20261021.md, BTC_DISCOVERY_V_FINAL_20261021.md y BTC_DISCOVERY_W_FINAL_20261021.md.
- BTC_DISCOVERY_Y_PROTOCOL_20261021.md, sólo especificación, sin resultados.
- RESEARCH_PROTOCOL_V1.md, RESEARCH_PROTOCOL_V5_20261020.md.
- FINAL_DECISION_V1.md, FINAL_DECISION_V4.md, FINAL_DECISION_V5.md.
- RESEARCH_DATA_AND_EXECUTION_FREEZE.md: leído únicamente como documento histórico de disponibilidad/unidades, sin consultas de series.

Fuentes completas obtenidas por read_strategy: FundingWfPilotBase4h, FundingOiPilot4h, ResearchV4FundingFP1h, ResearchV5FundingFP4h y BtcResearchR10FundingEvent4h. Helper completo leído por read_project_file: strategies/ResearchV5Base4h/funding_features.py. La fuente R10 base ya estaba leída y congelada durante W; no se editó ni se infirió un comportamiento nuevo de un nombre de wrapper.

Dos búsquedas de nombres tentativos (ResearchV5FundingBase4h y ResearchV4FundingBase1h) devolvieron strategy_not_found. Se corrigieron consultando las fuentes exactas anteriores; son ausencias semánticas, no outage MCP ni experimentos técnicos. Los listados alfabéticos acotados truncados no se trataron como censo ni evidencia de ausencia.

No se reauditan todos los fills o todas las estrategias antiguas. La evidencia suficiente para este descarte es la equivalencia conceptual concreta y los cierres existentes, no una pretendida refutación universal.

## Contrato que no cambia

Cualquier futura pregunta realmente distinta conserva BTC individual, capital 10.000 USDT, riesgo 2% por trade / 6% agregado / 3x aislado, fee taker con descuento 0,00045 por lado, funding BTC histórico aplicado con proxies declarados y slippage modelado cero. Ventana UTC [2020-10-15,2026-01-01), sin nueva economía 2026. R10 sizing y observador R11; gestión usual R12AR: stop 2 ATR14 simple, sin TP, 24 horas. No se cambian exposición, lados, gestión, riesgo o costes para recuperar resultados.

No se consume presupuesto económico por este descarte. Root puede continuar buscando otra pregunta independiente; este archivo no obliga a abrir Z y no altera el Hub, sus veredictos ni el protocolo Y.

```

## Documento completo: strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261021-r23/HANDOFF.md
SHA256 e82c7ac9c198b0eb7d326041ea9ec259614d5f962b4901fd4625a525a9d93039

```markdown
# Continuidad BTC — r23

W cerrada y auditada sin candidata; ver DISCOVERY_RESULTS y RESULTS. A–W suman44 ejecuciones por ID desde r9, no muestras independientes. V AR/G réplica sigue identificada. Ambos motores W y auditoría b2bfc1cd5bc24e7bb02e55e045049be7 terminales. No repetir sesiones.

W STATE290trades/CAGR1,254%/DD22,811%; control252/−0,977%/18,415%. M21/49 y21/43, Q10/20 y9/20, mediana calendario0 en ambas, neto sin dos mejores meses negativo. Ninguna alcanza gates. Bootstrap común57 eventos y runtime753; bank240,183 eventos insuficientes, sin resets/ventanas inválidas. PRETERMINALflat en ambas contiene equityfinal; funding y ledger conciliados a1e−6.

Presupuesto W cerrado sin vecinos de feature, banco, celda, barreras, bootstrap, horizonte, gestión, riesgo o selección de lados. Dos versiones técnicas117/129 comprobaciones solapadas por instrumentación, recibos y fuentes completos; no sumar. Contadores terminales iguales no son auditoría de cada estado de la trayectoria completa.

X reapertura bursátil queda HOLD documental: proxy SPX CFD BID/10 no ETF, calendario holidays/early closes no acreditado. No adquirir datos ni gastar motores para forzar. Ocupación M1 descartada como repetición de AngleCombinedBtcAcceptance4h. Propuesta Y documental en preparación independiente, aún no protocolo ni fuentes/jobs/drafts. Root revisará materialidad/hipótesis económica/dedup antes de permitir implementación.

Autonomía vigente hasta objetivo, sin parada por cierre de pregunta. BTC individual,10k/2%/6%/3x,fee.00045 por lado y fundingBTC9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 aplicado, slippage0. Ventana[2020-10-15,2026-01-01), sin nueva economía2026/imports/datasets/live/paper/Pi/install/framework/globalconfig. Estrés diferido a candidata y acuerdo. Máximo2 backtests +1analysis. Reportes y estrategias sóloMCP. MCP sigue sano; no reinicioDocker realizado. Usuario autoriza restart local únicamente si vuelvefallar, identificar instancia y sesiones antes.

Publicar archivos/readback completos antes de índice. Corregidos roadmap/etapa/blockers heredados; preservar toda evidencia previa. Goaltool sigue blocked por outage anterior y API no permite resume; humano reanudó explícitamente, no duplicar ni marcar completo. Continuar manualmente.

```

## Documento completo: strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_AB_FINAL_20261021.md
SHA256 10da77ca7fe2464f732c52b6bed4cda1869389da0ff54c01ed59384dac87a60b

```markdown
# Primer ciclo autónomo BTC: cierre de las tandas A y B
Fecha: 2026-10-21. Estado: cerrado sin candidata.

## Qué se ejecutó
Se contrastó la evidencia BTC existente y se ejecutaron dos hipótesis nuevas más una iteración de gestión. Tres backtests económicos terminados, sin errores ni reemplazos técnicos. Se mantuvo el perfil 2% por operación / 6% agregado / 3x aislado, con 10.000 USDT virtuales por cuenta, comisión 0,00045 por lado y funding activado. No se hicieron pruebas de estrés, variantes de riesgo o nuevas corridas de 2026.

Ventana común: [2020-10-15, 2026-01-01) UTC. Es desarrollo histórico ya observado; 2020 es parcial y 2021–2025 son años completos. Neto significa después de comisiones y funding modelados, con slippage cero modelado. No significa neto de todos los costos reales.

| Receta | CAGR | DD diario reportado | PF neto | Trades | Retorno total | Decisión |
|---|---:|---:|---:|---:|---:|---|
| [A: persistencia de signos](http://localhost:9200/#/backtest/438b717c-7b5e-4589-a84a-687fa63f8645) | 11,59% | −14,52% | 1,473 | 193 | +77,20% | No cumple CAGR ≥30%. |
| [A: fallo posterior al funding](http://localhost:9200/#/backtest/b3fa7fff-0b6b-44de-ac23-230c118a94b0) | −7,57% | −35,24% | 0,896 | 454 | −33,66% | No cumple retorno, PF ni DD. |
| [B: signos con salida por estado](http://localhost:9200/#/backtest/62c90517-9034-4b34-91af-f77457895157) | 23,39% | −33,10% | 1,576 | 102 | +199,28% | No cumple CAGR ni DD. |

No confundir retorno total de unos cinco años con rentabilidad anual. Ninguna receta alcanza los objetivos decisivos; ninguna se promueve.

## Preguntas y diferencias frente a los antecedentes
La matriz inicial confirmó que V1–V6 sí contiene BTC individual con funding. CHANNEL_P quedó en 17,54% de CAGR en su replay y CROSS_P sólo tiene screening, sin confirmación posterior. Ninguna acredita el objetivo actual. No era necesario repetir sus backtests ni atribuir a BTC el CAGR de K1001/N204 de cartera.

La tanda A se registró antes de sus resultados:
- **Persistencia de signos:** contar cambios positivos o negativos en las últimas 6 y 24 barras de cuatro horas, con una mayoría de dos tercios. Entrar sólo al aparecer el estado. Difiere del cociente de eficiencia de V6 y del cruce de medias de V5: cuenta signos, no magnitudes ni posición respecto de una media.
- **Fallo posterior al funding:** esperar una barra completa después de un pago ya publicado y operar cuando se invalida el movimiento previo del lado pagador. Fue la parte creativa: una de las dos hipótesis iniciales. No usa el próximo pago ni acredita liquidaciones reales; la hora UTC y el evento siguen confundidos.

Ambas tenían stop fijo de 2 ATR, objetivo de 2R y salida máxima a las 48 horas. Los eventos bloqueados por una posición se consumían, sin cola.

Después de observar A se registró una sola iteración B: misma entrada, sizing y stop, pero sin objetivo de beneficio, con salida por estado contrario y límite de 30 días. Es una transferencia explícita de gestión conocida en V5 a otra señal. Cambia una política completa; no identifica por separado el efecto del TP, del plazo o de la salida. El control A se reutilizó.

La revisión de fuentes y los chequeos sintéticos precedieron a la economía. Un segundo agente contrastó las reglas y el reloj de funding. No se quitaron shorts según su resultado ni se probaron vecinos para rescatar una curva.

## Qué aprendimos
La señal de signos produjo utilidad positiva bajo costos base, pero insuficiente para el objetivo. Dejar correr posiciones elevó el retorno y también el drawdown. No demuestra que la gestión inicial fuera la causa del fallo.

La receta posterior al funding perdió pese a recibir funding neto favorable. No se justifica invertir su dirección después de ver el resultado.

Funding neto: −574,54 USDT en A_SIGN, +894,62 en A_EVENT y −4.281,41 en B. Mayor duración cambia exposición y pagos; no es un estrés de comisiones. La concentración de B también aumentó: sus dos mejores meses aproximados aportan 16.695,50 USDT frente a 19.927,68 de neto total. Seguir positivo sin ellos no basta para aprobar regularidad.

## Verificación y límites de medición
La auditoría completa recibió 193, 454 y 102 trades, y 1.905 puntos de equity por cuenta. Reconcilió bruto de precios − comisiones + funding = suma de PnL = saldo final − 10.000, y recalculó PF y CAGR. Error máximo absoluto: 5,10×10⁻¹¹ USDT, inferior a la tolerancia contable de 10⁻⁶. No se calcularon totales desde páginas parciales.

Se verificó funding.applied=true, el dataset congelado y el replay completo M1. El snapshot contiene 6.576 eventos y 4.198 marcas proxy en toda su cobertura; las posiciones de las tres recetas usaron respectivamente 513, 1.207 y 1.772 pagos con marca aproximada. No son precios exactos de ejecución de una cuenta real.

En B, el summary conserva total_open_trades=1 y open_pl preterminal. Los logs finales muestran la orden MARKET reduce-only ejecutada, cierre del trade, cancelación del stop y saldo final 29.927,68. Los 102 trades cerrados reconcilian con ese saldo; el contador previo no se presenta como posición real abierta.

Dos límites importantes:
- El max_drawdown del framework se calcula con daily_balance. Los DD de la tabla son muestreados diariamente y pueden omitir extremos intradiarios. Se aclara la frase imprecisa del protocolo A que sugería otra resolución.
- La curva diaria usa cortes a las 00:01 UTC, más valores inicial y terminal. Los CSV mensuales y anuales derivados se etiquetan como aproximados. No acreditan cortes exactos a las 00:00 ni las puertas M65/Q80, mediana y concentración. Como las tres recetas ya fallan retorno o DD obligatorio, el rechazo no depende de inventar esas mediciones. Una futura candidata requerirá medición suficiente antes de promoverse.

Respecto de V1–V6, la política común de esta tanda no impone su cap nocional 1x ni cuota diaria: aplica el riesgo objetivo hasta donde permite el margen 3x reservado. Es una diferencia explícita de exposición, no evidencia de mejor señal comparando programas. No hubo rejilla de caps o riesgos.

## Cierre y continuidad
Las tandas A (dos corridas) y B (una) agotaron su presupuesto y se cierran sin candidata. No seguir con pequeñas variantes de ventanas, TP o plazo, ni eliminar shorts por su PnL observado. La siguiente tanda deberá justificar otra pregunta material, contrastarla con estos resultados y los antecedentes, y registrar su presupuesto antes de ejecutar. El permiso autónomo del usuario sigue vigente.

Los 209 backtests económicos históricos V1–V6 se conservan aparte de estos tres; no son un censo de todo el proyecto ni muestras independientes. La participación creativa continuará con hipótesis comprobables. PAXG/SPY y cartera siguen diferidos; estrés sólo después de candidatas y acuerdo conjunto. No se operó paper/live, no se accedió a la Pi ni se alteró configuración global.

## Trazabilidad
En strategies/FundingOiPilot4h/reports/:
- BTC_INDIVIDUAL_EVIDENCE_MATRIX_20261021.md.
- BTC_DISCOVERY_A_PROTOCOL_20261021.md y BTC_DISCOVERY_A_MANIFEST_20261021.json.
- BTC_DISCOVERY_A_RESULTS_20261021.md/.json.
- BTC_DISCOVERY_B_PROTOCOL_20261021.md y BTC_DISCOVERY_B_MANIFEST_20261021.json.
- BTC_DISCOVERY_AB_RESULTS_20261021.json y CSV *_monthly_approx.

Auditoría final: job 0fef85256f9e453abcd5e35c2c3ee42c, con snapshots completos. Los resultados y CSV se recuperaron y guardaron mediante MCP. Los manifiestos conservan código, hashes y configuración anterior a cada ejecución.

```

## Documento completo: strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_CD_FINAL_20261021.md
SHA256 26fe4f3940e85e7561d64d0a12309b2da5979ed0316abf537ec8146f6ebf2643

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

## Documento completo: strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_W_FINAL_20261021.md
SHA256 fa31022b6a35bcfc09494926c130be95f9b4210940c085787be3b33566830f48

```markdown
# BTC Discovery W — cierre

La pregunta es si el estado observado (tipo de episodio, duración relativa FAST/SLOW) añade utilidad predictiva frente al tipo REV/CONT solamente. Los episodios usan dos pasajes de cierre: un primer avance de una ATR desde ancla congelada, seguido de retorno al ancla o continuación a dos ATR. Un primer cruce que ya alcanza dos ATR se descarta como degenerado. Los overshoots y la discretización hacen que FAST/SLOW no mida velocidad pura ni un efecto causal aislado.

Ambas políticas comparten los eventos y las etiquetas maduras de retorno bruto posterior a 24 horas, orientadas por el segundo pasaje. STATE aprende la media por (tipo, FAST/SLOW); TYPE_CONTROL por tipo. Banco rolling completo de 240 etiquetas y mínimo común de 20 casos por celda, sin extender ventanas para completarlas. Bootstrap matemático causal de exactamente 1000 cierres, una sola vez; sin órdenes durante el replay ni en la inicialización. Las reglas se fijaron antes de los resultados V.

Contrato UTC [2020-10-15, 2026-01-01), capital virtual 10.000 USDT, riesgo 2% por operación / 6% agregado / 3x aislado. Fee .00045 por lado y funding BTC histórico aplicado, con marcas proxy declaradas; slippage modelado cero. Entrada al precio actual, stop 2 ATR14 simple actual, sin take profit y timeout de 24 horas desde el fill en la primera frontera de 4 horas elegible. Padres R10/R11/R12AR intactos. Historia de desarrollo ampliamente explorada, sin nueva economía 2026.

Verificación previa: revisión de fuentes por root e independiente conforme; 129 comprobaciones sintéticas finales aprobadas. La versión inicial aprobó 117 comprobaciones que se solapan con las finales: no se suman. La revisión posterior sólo añadió instrumentación; ambas versiones, harnesses y recibos quedan preservados. Estas comprobaciones no acreditan ventaja predictiva ni cobertura de datos real.

| Política | N | CAGR % | PF | DD M1 + fills % | Meses activos positivos | Trimestres positivos | Mediana mensual % | Neto sin dos mejores meses |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [STATE](http://localhost:9200/#/backtest/bfbcc16b-5acb-4659-a087-66bbf3b31371) | 290 | 1.254048 | 1.032271 | 22.810641 | 21/49 | 10/20 | 0.000000 | -2285.432344 |
| [TYPE_CONTROL](http://localhost:9200/#/backtest/c5f3e262-5e40-4127-8e3e-d60234e5f880) | 252 | -0.977381 | 0.967142 | 18.415074 | 21/43 | 9/20 | 0.000000 | -2020.296144 |

STATE: bruto de precio 2789.253281, comisiones 2043.099491, funding -74.458376, neto 671.695414 y capital final 10671.695414 USDT. Años completos (%): {"2021":2.815764912877272,"2022":7.55827602454362,"2023":10.299282821929602,"2024":-6.713970666436753,"2025":-6.213445479251767}. Peor/mejor ventana de 12 meses: -18.789702/32.109763%. Ventanas solapadas, descriptivas.

TYPE_CONTROL: bruto de precio 1065.583159, comisiones 1505.665231, funding -59.366633, neto -499.448706 y capital final 9500.551294 USDT. Años completos (%): {"2021":0,"2022":-11.826983283465943,"2023":12.501680702521822,"2024":3.1847479068843887,"2025":-7.180635805646485}. Peor/mejor ventana de 12 meses: -11.826983/13.775750%. Ventanas solapadas, descriptivas.

**Veredicto: NO_CUMPLE en ambas; ninguna candidata.** STATE mejora al control, pero CAGR, PF, M65, Q80, mediana y neto sin los dos mejores meses fallan. Ambas cumplen el techo de drawdown y N operativo preliminar; eso no compensa las demás puertas ni aporta potencia estadística por conteo. STATE tiene 13 meses completos inactivos y TYPE_CONTROL 19, todos incluidos con cero en la mediana calendario. No se elegirá sólo shorts o una celda tras atribución.

El motor tuvo cobertura suficiente para inicializar el bootstrap en 2020-10-15 04:00 UTC. Produjo 57 eventos maduros en el replay y 753 eventos completos de runtime; el replay no operó. Hubo 183 eventos con banco o celda insuficiente, sin relajar umbrales. Las dos políticas tienen los mismos contadores de bootstrap/runtime, banco terminal y celdas: 11.423 barras de runtime, 159 degenerados, 80 empates y cero resets/gaps/ventanas inválidas. Al cierre queda un episodio incompleto, con primer pasaje observado; cero etiquetas pendientes terminales. Incompleto no se convierte en SLOW. La igualdad de resúmenes corrobora la entrada común; no constituye una comparación observada de cada estado interno de toda la trayectoria. El código determinista separa matemática y cuenta.

Ambas cuentas cierran flat y usan PRETERMINAL, que ya contiene el capital final sin necesitar callback de liquidación final. La auditoría del snapshot completo reconcilia bruto − comisiones + funding = suma PNL = capital final − 10.000, y funding contra su métrica, a menos de 1e−6 USDT. Marcas proxy aplicadas: 341/332. R11 registra 2.741.760 marcas M1, 63 intervalos/62 meses y 20 trimestres completos; equity wallet + PnL abierto, fronteras UTC post-funding/predecisión por fase. DD M1 y fills no representa todos los extremos intraminuto. Mensuales suman el neto de cuenta y sus cortes son contiguos.

Presupuesto cerrado: dos ejecuciones económicas, cero errores o reemplazos económicos. W eleva a 44 los IDs económicos ejecutados desde r9; son ejecuciones, no 44 hipótesis o muestras independientes. Se conserva identificada la réplica AR/G de V. No vecinos de banco, celda, bootstrap, barreras, duración, horizonte, hurdle, filtros, lados, riesgo o gestión; no rescatar la línea ni adaptar etiquetas después de resultados. Sin estrés, nueva economía 2026, importaciones o cambios operativos.

Auditoría: b2bfc1cd5bc24e7bb02e55e045049be7 succeeded. Código exacto, recibo y resultados completos en BTC_DISCOVERY_W_ACCOUNTING_20261021.json; fuentes/versiones en CODES y checks en TECHNICAL_CHECK_RECEIPT. Protocolo y manifiesto se guardaron y releían antes de motores. X sobre reapertura de un proxy estadounidense queda HOLD por integridad/calendario; no se ejecutó. La autonomía continúa buscando otra pregunta material desde antecedentes.

```

## Documento completo: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_FINAL_RESEARCH_RESULTS_20261019.md
SHA256 4066e53cf744efc6166d59abdae26ebaf6dc7842f8c6d81b45a6e75e7b691f7f

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

## Documento completo: strategies/MultiAssetRetestBtcShort4h/reports/N204_T403_R5_FROZEN_PROTOCOL_20261019.md
SHA256 f816c62471ab615f514c7b0730f610cc1c0224db0300b6ba42407e1acea24dd8

```markdown
# N204 / T403 — protocolo R5 congelado antes de resultados

Usuario autorizó una nueva ronda con dos agentes nuevos. Semillas: N204 ganadora vigente; T403 candidata no promovida, no ganadora alternativa. Todas las hipótesis siguientes se fijan juntas antes de crear fuentes o sesiones. R4 se conserva íntegra. 2026 CERRADO incluso a inspección. Ventana2020-10-15→2025-12-31EXCLUSIVA(últimodía2025-12-30). Muestra intensamente reutilizada de desarrollo, no OOS ni prueba anti-sobreajuste.

## Presupuesto y controles
10recetas×B/C=20backtestsnominales. Cada uno de dos nuevos agentes dispara2simultáneos por ticketroot;máximo4global y2análisis. Ninguna receta nueva tras mirar resultados, sin combinaciones de ganadores ni umbrales de rescate. Conservartodosincluidosceros/sinoperaciones/bajamuestra. Un máximo de6fulls de verificación paraUNcandidatoelegible tras terminar20:2fees+.00025/lado y4vecinos de target .9/1.1. Si ninguno elegible, detener20. Reparaciones exclusivamente técnicas se documentan y repiten porpareja; rawpreservadoapartado, no son ideasnuevas. Sinrestarts/imports preventivos/configglobal/live/paper/Pi/instalaciones/research_scripts/funding.

Contrato vigente:10000USDTshared,1%trade/8%agregado,isolated5x,nopyramid,cap4.4,reserva.001sólosizing. Fee nominal.00045/lado,todosordertypes. BTC/PAXG/SPY4h+3feeds1m enBinancePerpetualFutures,warmup240,debugtruefastfalsecharttrue. PAXGPortComparePaxgMarket4horiginalfeeBE(noadoptarBEfijoR3),SPYBPortCompareSpySecond4h,CPortCompareSpyMarket4h. OriginalesBTC long/STOP short,HP,prioridad,sizing,ledger/volatility/budget intactos. Noafirmarejecucionesoriginalesidénticas:ocupación/capitalcompartidopuededesplazar.

NuevasfuentesautocontenidasN204ExploreR501..505 yT403ExploreR501..505. N501..505añadenunsetupcompletoalN204; latchfalse→true delsetupMODIFICADO seactualizainclusoocupado/pending,sincolas. C501..505mantienenN204entry/latch deT403con excepciónlabelyAextraenC504sinmodificarcriterios. Sóloactúansobre suplementoMARKET, originalesintactos. E=fillreal,d=distanciaplaninicial,SL=E+d,TP=E-2d,deadline48hdesdefill. No parciales. Sólo4hcompletaspostfill,contiguas,clockcandleopen>=fill,close<=decision yprimerfull=ceil(fill/4h)*4h; idempotencia,resetporfill ydeadlineprimero. Antesdeladverso seprocesaprogresoC505; misma-baradverso no puede recuperar porcondicionescontrarias, comprobartiemposestrictos. N504UTCclockcalendario,ningunbarpartial/futura. OHLCVpresiónproxy,noobservedflow.

## Hipótesis exactas
```json
{
  "n204": [
    {
      "id": "N501",
      "strategy": "N204ExploreR501",
      "seed": "N204",
      "rule": "N204 fullsetup AND Bneg<Apos: W12 originalq; HLC3 VWAP B with volume ofq<0cohort; Aoriginalpositivecohort; emptynegfalse. Noqweight/Achange."
    },
    {
      "id": "N502",
      "strategy": "N204ExploreR502",
      "seed": "N204",
      "rule": "N204fullsetup AND median(TRlast6W)<median(TRfirst6W) AND TR_t>median(TRW). TR_i=max(H-L,abs(H-Cprev),abs(L-Cprev)),includesgap,priorcloseavailable14bars. Strict inequalities."
    },
    {
      "id": "N503",
      "strategy": "N204ExploreR503",
      "seed": "N204",
      "rule": "N204fullsetup AND0<ER<=1/3,ER=(C_s-C_s12)/sum12abs(closechanges throughs);denominator0false. NoERthresholdsweep."
    },
    {
      "id": "N504",
      "strategy": "N204ExploreR504",
      "seed": "N204",
      "rule": "N204fullsetup AND latest2completeUTC12h bars each3exactcontiguous4h, end=floor(decisionclose/12h)*12h: previousgreen Cp>Op,latestred Cl<Ol,Ol>=Cp,Cl<=Op. Currentpartial12hexcluded,daymidnightjustclosedincluded. Missing/duplicate/reorderfalse."
    },
    {
      "id": "N505",
      "strategy": "N204ExploreR505",
      "seed": "N204",
      "rule": "N204fullsetup AND atleast8of12Wcloses>=originalA. Acalculatedonceoriginalcohort. Fixed8/12nostepsweep."
    }
  ],
  "t403": [
    {
      "id": "C501",
      "strategy": "T403ExploreR501",
      "seed": "T403",
      "rule": "RetainN204entry/T403adverseactivationfirstcomplete4hclose>=E+.5d. Require2consecutivecomplete4hcloses<=E strictlyAFTERadversebeforeMARKETexit atsecond. Anyclose>Ereset0. SL1RTP2R48hunchanged,deadlinefirst."
    },
    {
      "id": "C502",
      "strategy": "T403ExploreR502",
      "seed": "T403",
      "rule": "Afterfirstadverse>=E+.5d, firststrictlylaterfull4hclose<=E freezes thatbarhigh recovery_high,doesnotexit. Onlystrictlylaterfull4hclose>recovery_highexitsMARKET; barrierfixeduntilclose,noSLmove. SL1RTP2R48hdeadlinefirst."
    },
    {
      "id": "C503",
      "strategy": "T403ExploreR503",
      "seed": "T403",
      "rule": "AfterT403adverseactivation,strictlylaterfull4hclose<=E exitsMARKETonlyifH>LandC>=(H+L)/2 ofthatbar. Recoveryclosedinlowerhalfmaintain/re-evaluatelaterbars. Noentryfilter/SLmove,deadlinefirst."
    },
    {
      "id": "C504",
      "strategy": "T403ExploreR504",
      "seed": "T403",
      "rule": "CaptureoriginaleventApositivecohortHLC3VWAPinplan/fill,fixedfortrade. AfterT403adverseactivation,strictlylaterfull4hclose<A exitsMARKET,replacesclose<=E(notAND). NoArecursion/recalculation/noentrysetupchange. SL1RTP2R48hdeadlinefirst."
    },
    {
      "id": "C505",
      "strategy": "T403ExploreR505",
      "seed": "T403",
      "rule": "Ifanycompletepostfill4hclose<=E-d BEFOREfirstadverseclose>=E+.5d,permanentlydisableT403rescueforthattrade. OtherwiseT403exact. ProgressobservedCnotintrabarL,adverse/progresscannotbothoccur,sweepnone. SL1RTP2R48hdeadlinefirst."
    }
  ]
}
```

## Evaluación congelada
AuditorreutilizafillsyMTMUTCcon4anclascongeladasR4; cantidades/fees/PNL/wallet/terminal/partialsexactos ypreciosanchorcheck.61meses/19Qcompletos,63/21incluidos,mesesactivosycalendarioexplícitos,positivos>0sinredondeo. Overlays+5/+10bpsRT sobrecadarealfillañaden.00025/.00050porlado,qty/precios/timestampsfijos; no reruns/slippagepuro. DDMotor ydayclose separados,cohortesnoMTMporaperturaseparadas. SupplementMARKETvsoriginalSTOP/long,ex1/ex3+10,exposición,notional×time,cohortesaño,capital/desplazamientoscomo diagnósticos.

Comparaciones: todascontraN204B/C nominal para elegibilidad;líneaCademáscontraT403B/C paraatribuircambio. ReferenciasN204Bbc5aaba6-2746-4e90-b0de-7b7955b66142,C6dead093-4663-4da9-ac62-c2ad9f9bb794;T403B9014f7d9-fa7e-4af7-94b7-dc98940f21b8,Cbd5f78dd-b730-48ad-ab01-e4c3f4726d29. TodasyaresumidasMCPfinished/errornull antescongelar.

ElegibilidadTODOSenB/C:nominalnet>N204;+5Mpositivos/activos>=.65 yQpositivos>=.80,encompletoseincluidos;+10net>=N204mismocoste;DDmotor>=-25%. BatirT403noalcanza. Rankingfijo:mayormínmargenM65/Q80sobreambosbins/B/C;mayormínΔnet+10;menorpeorDD;IDlex. Noelegible=>ceroverificaciones. Unaúnicarecetaelegible(tras20auditados) seconfirmafee.00070/ladoB/C mismasfuentescontraN204feealtoB9a6c7c24-8847-42d1-aadb-206f21723c1f/C541d2bf4-ffca-4f2d-969b-c25165e7b960. Exigirdelta>0M65Q80ambosbinsambascarteras,DD>=-25. Si falla,noseescogealternativa. Dosvecinosdevalidaciónnoelegiblesparaescoger:TPsuplementario1.8R/2.2R(.9/1.1×2R),SL/restointactos,cadaB/Cnominal4fulls. Reportarmatrizsin elegirmejorvecino.

QA antesfulls:fuentesmétodosprotegidos/dedupR4,rangos/finito/igualdad/clock full,latch/occupied/pending/reset,idempotencia,indicadoresnuevossólodocumentados(nohanpropuestonuevos),casosnoobservablesfalse. NopegararraysderesultadosenPython,nofuturosniM1preconstruidosparapostfill. Inventarios/objetivohipótesisno justificanpromoción. Root revisa las10fuentes y lasbases antes de lanzar,cadafuente3snapshots/formsexactos. Criteriosnoadaptadosdespués. ReportesMCPobligatoriosporfamilia,matriz20,registro,diagnósticos yrevisiónindependienteantesfinal.


Precisión numérica previa a resultados: los porcentajes de meses/Q siguen >0 sin redondear; no se fuerza cero. Para incremento de neto, diferencias absolutas <=1e-7USDT se etiquetan identidad numérica y no mejora, tanto nominal como en confirmación fee. Conservar delta bruto; nominal elegible requiere delta>1e-7. Comparación no-inferior de +10 admite tolerancia contable1e-7. Es una tolerancia de conciliación de floats, no un umbral elegido por resultados. Fuente/riesgo no cambian.

```

## Documento completo: strategies/MultiAssetRetestBtcShort4h/reports/N204_T403_R5_FINAL_RESULTS_20261019.md
SHA256 ed7c9bfa10a65eab0cfce04be4ebb7a34da5f5430da135423d3f16caa8f04af4

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

## Documento completo: strategies/MultiAssetRetestBtcShort4h/reports/N204_R4_FINAL_RESULTS_20261019.md
SHA256 b073ee832160a3f5c3d3379b9da24ec9a65e87dd1115a5f2fb90a8c333a88800

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

## Documento completo: strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_FINAL_RESULTS_20261019.md
SHA256 07b1a7e356cf69975c881d5ea4b0826d6363d8ea7b7e128bf25c616a64ca78f5

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

# Nuevas fuentes autorizadas, primera versión previa al check

Estado implementación/checks autorizados, cero economía/drafts. La instrumentación de fits, gammaRAW, fills y deadlines se incluyó desde esta primera versión. Padres previos intactos.

## BtcResearchR27VolumeInteractionBase1m — SHA256 ba61a93ecfb9891d2d80c0e43b224814ab8f2efe9d5e6cea45e49c80b9a8f475

```python
"""AA: conditional price response to participation, not identified order flow."""
import math
import numpy as np

from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def interaction_inputs(rows):
    """Origins42..401/current407; every surprise owns42 strictly prior volumes."""
    if rows.ndim != 2 or rows.shape[0] != 408 or rows.shape[1] < 6:
        return None
    if (not np.all(np.isfinite(rows[:, :6])) or np.any(rows[:, 1:6] <= 0)
            or not np.all(np.diff(rows[:, 0]) == BAR)
            or np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2]))
            or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2]))):
        return None
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        close = np.log(rows[:, 2])
        volume = np.log(rows[:, 5])
        # Last sliding window includes V407 and has no following current volume:
        # discard it. Remaining366 windows end one bar BEFORE each origin42..407.
        prior = np.lib.stride_tricks.sliding_window_view(volume, 42)[:-1]
        r = np.diff(close)[41:]
        v = volume[42:]-np.mean(prior, axis=1)
        # RAW product is prescribed for interpretable coefficient conversion.
        # Products after affine centering can span the same model with main effects.
        raw = np.column_stack((r, v, r*v))
        labels = close[48:408]-close[42:402]
    if not np.all(np.isfinite(raw)) or not np.all(np.isfinite(labels)):
        return None
    return raw[:360], labels, raw[-1]


def interaction_fit(raw, labels, current):
    """Two nested OLS models share all360 rows, scalers and numerical admission."""
    if raw.shape != (360, 3) or labels.shape != (360,) or current.shape != (3,):
        return None, dict(reason="shape_invalid")
    if not all(np.all(np.isfinite(x)) for x in (raw, labels, current)):
        return None, dict(reason="arithmetic_invalid")
    # Exact constants can yield a tiny positive std after a rounded mean. Detect
    # equality first; no near-zero threshold or dropping a column for MAIN.
    if np.any(np.all(raw == raw[:1], axis=0)):
        return None, dict(reason="constant_column")
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        center = raw.mean(axis=0)
        scale = raw.std(axis=0, ddof=0)
        scaled = (raw-center)/scale
        point = (current-center)/scale
    if (not np.all(np.isfinite(center)) or not np.all(np.isfinite(scale))
            or np.any(scale <= 0) or not np.all(np.isfinite(scaled))
            or not np.all(np.isfinite(point))):
        return None, dict(reason="scale_invalid")
    full = np.column_stack((np.ones(360), scaled))
    main = full[:, :3]
    try:
        # None is NumPy's dtype/shape-dependent default numerical-rank cutoff,
        # frozen ex ante. Deficient rank rejects BOTH; no ridge or fallback.
        bf, _, rankf, sf = np.linalg.lstsq(full, labels, rcond=None)
        bm, _, rankm, sm = np.linalg.lstsq(main, labels, rcond=None)
    except np.linalg.LinAlgError:
        return None, dict(reason="solver_error")
    if rankf != 4 or rankm != 3:
        return None, dict(reason="rank_invalid", ranks=[int(rankf), int(rankm)])
    if not all(np.all(np.isfinite(x)) for x in (bf, bm, sf, sm)):
        return None, dict(reason="coefficient_invalid")
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        x = np.r_[1., point]
        ff = float(x @ bf)
        fm = float(x[:3] @ bm)
        g = float(bf[3]/scale[2])
    if not all(math.isfinite(x) for x in (ff, fm, g)):
        return None, dict(reason="forecast_or_g_invalid")
    evidence = dict(reason="valid", n=360, origins=[42, 401], current_index=407,
        target_indices=[48, 407], current_raw=current.tolist(),
        center=center.tolist(), scale=scale.tolist(),
        coefficients_full=bf.tolist(), coefficients_main=bm.tolist(),
        ranks=[int(rankf), int(rankm)], singular_full=sf.tolist(),
        singular_main=sm.tolist(), g_raw=g,
        forecast_full=ff, forecast_main=fm)
    return (ff, fm), evidence


def interaction_forecasts(rows):
    values = interaction_inputs(rows)
    if values is None:
        return None, dict(reason="data_invalid")
    return interaction_fit(*values)


def empty_interaction_diagnostic():
    return dict(last=None, n=0, g_negative=0, g_zero=0, g_positive=0,
        means={key: dict(available=True, value=None)
               for key in ("g_raw", "forecast_full", "forecast_main")},
        aggregation_errors=0, latest=None)


def interaction_diagnostic(state, now, evidence):
    """O(1), once per valid fit, independent of mode, hurdle, ATR and occupation."""
    if state["last"] is not None and now <= state["last"]:
        return state
    result = dict(state)
    result["last"], result["n"] = int(now), state["n"]+1
    g = evidence["g_raw"]
    key = "g_negative" if g < 0 else "g_positive" if g > 0 else "g_zero"
    result[key] += 1
    result["latest"] = {key: evidence[key]
                        for key in ("g_raw", "forecast_full", "forecast_main")}
    result["means"] = {}
    for key, old in state["means"].items():
        item = dict(old)
        if old["available"]:
            value = evidence[key]
            mean = value if state["n"] == 0 else old["value"]+(value-old["value"])/result["n"]
            if math.isfinite(mean):
                item["value"] = mean
            else:
                # An unavailable descriptive aggregate cannot affect any forecast
                # or the accepted fit. Do not serialize Infinity or invent a mean.
                item.update(available=False, value=None)
                result["aggregation_errors"] += 1
        result["means"][key] = item
    return result


class BtcResearchR27VolumeInteractionBase1m(BtcResearchR12ArBase1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("INTERACTION", "MAIN_EFFECTS")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        last = self.vars.get("interaction_last")
        if last is not None and now <= last:
            return
        self.vars["interaction_last"] = now
        if not self.START < now < self.FINISH:
            return
        counts = self.vars.setdefault("interaction_counts", {})
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 408)
        if rows is None:
            counts["window_invalid"] = counts.get("window_invalid", 0)+1
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        forecasts, evidence = interaction_forecasts(rows)
        reason = evidence["reason"]
        counts[reason] = counts.get(reason, 0)+1
        self.vars["interaction_latest_fit"] = evidence
        if forecasts is None:
            return
        evidence.update(origin=now, window_first=int(rows[0, 0]), window_last=int(rows[-1, 0]))
        # Record BOTH forecasts and raw gamma before all trading gates. MODE and
        # wallet/order state never enter any mathematical/diagnostic helper.
        diagnostic = self.vars.get("interaction_diagnostic", empty_interaction_diagnostic())
        self.vars["interaction_diagnostic"] = interaction_diagnostic(diagnostic, now, evidence)
        forecast = forecasts[0 if self.MODE == "INTERACTION" else 1]
        if abs(forecast) <= .0019:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(rows)
        if atr is None:
            counts["atr_invalid"] = counts.get("atr_invalid", 0)+1
            return
        direction = 1 if forecast > 0 else -1
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            counts["plan_invalid"] = counts.get("plan_invalid", 0)+1
            return
        self.vars["plan"] = dict(plan, interaction_evidence=evidence,
                                forecast=forecast, forecast_origin=now)
        self.vars["direction"] = direction

    def on_open_position(self, order):
        super().on_open_position(order)
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        self._log("R27_OPEN", dict(time=int(self.time), mode=self.MODE,
            forecast=plan["forecast"], forecast_origin=plan["forecast_origin"],
            forecast_deadline=plan["forecast_origin"]+6*BAR,
            opened_at=int(self.position.opened_at),
            hold_deadline=int(self.position.opened_at)+6*BAR,
            entry=float(self.position.entry_price), qty=abs(float(self.position.qty)),
            stop=float(self.position.entry_price)-direction*plan["distance"],
            distance=plan["distance"], risk_budget=plan["risk_budget"]))
        self._log("R27_OPEN_FIT", plan["interaction_evidence"])

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R27_COUNTS", dict(stage=stage, mode=self.MODE,
            counts=self.vars.get("interaction_counts", {}),
            signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
            occupied=self.vars.get("occupied", 0)))
        self._log("R27_DIAGNOSTIC", dict(stage=stage,
            **self.vars.get("interaction_diagnostic", empty_interaction_diagnostic())))
        self._log("R27_LAST_FIT", dict(stage=stage,
            **self.vars.get("interaction_latest_fit", {})))

```

## BtcResearchR27VolumeInteraction1m — SHA256 0d36dd073a021dab6c1932d6c8f90c3c30c5d95c098d08bb3f9e85415e3264f4

```python
from strategies.BtcResearchR27VolumeInteractionBase1m import BtcResearchR27VolumeInteractionBase1m


class BtcResearchR27VolumeInteraction1m(BtcResearchR27VolumeInteractionBase1m):
    MODE = "INTERACTION"

```

## BtcResearchR27MainEffects1m — SHA256 cff9b19badf7750d8e9e8ecf2b05f8bcad84fbf2ed32f7487288873c0d1a656e

```python
from strategies.BtcResearchR27VolumeInteractionBase1m import BtcResearchR27VolumeInteractionBase1m


class BtcResearchR27MainEffects1m(BtcResearchR27VolumeInteractionBase1m):
    MODE = "MAIN_EFFECTS"

```

## Revisión técnica de fuente previa al primer check

Root pidió sustituir assert de paridad de precio por invalidez de datos compartida CASH antes de modelo/diagnóstico, coherente con protocolo. Primera versión conservada íntegra arriba, SHA256 ba61a93ecfb9891d2d80c0e43b224814ab8f2efe9d5e6cea45e49c80b9a8f475. Sin job sobre esa versión, sin cambio de modelo/riesgo/gestión. La siguiente es versión vigente:

SHA256 aae9138ae04a4b14bec1970f6c598e03cfee62ae9d0e392816cc48e2e8e94cfa

```python
"""AA: conditional price response to participation, not identified order flow."""
import math
import numpy as np

from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def interaction_inputs(rows):
    """Origins42..401/current407; every surprise owns42 strictly prior volumes."""
    if rows.ndim != 2 or rows.shape[0] != 408 or rows.shape[1] < 6:
        return None
    if (not np.all(np.isfinite(rows[:, :6])) or np.any(rows[:, 1:6] <= 0)
            or not np.all(np.diff(rows[:, 0]) == BAR)
            or np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2]))
            or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2]))):
        return None
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        close = np.log(rows[:, 2])
        volume = np.log(rows[:, 5])
        # Last sliding window includes V407 and has no following current volume:
        # discard it. Remaining366 windows end one bar BEFORE each origin42..407.
        prior = np.lib.stride_tricks.sliding_window_view(volume, 42)[:-1]
        r = np.diff(close)[41:]
        v = volume[42:]-np.mean(prior, axis=1)
        # RAW product is prescribed for interpretable coefficient conversion.
        # Products after affine centering can span the same model with main effects.
        raw = np.column_stack((r, v, r*v))
        labels = close[48:408]-close[42:402]
    if not np.all(np.isfinite(raw)) or not np.all(np.isfinite(labels)):
        return None
    return raw[:360], labels, raw[-1]


def interaction_fit(raw, labels, current):
    """Two nested OLS models share all360 rows, scalers and numerical admission."""
    if raw.shape != (360, 3) or labels.shape != (360,) or current.shape != (3,):
        return None, dict(reason="shape_invalid")
    if not all(np.all(np.isfinite(x)) for x in (raw, labels, current)):
        return None, dict(reason="arithmetic_invalid")
    # Exact constants can yield a tiny positive std after a rounded mean. Detect
    # equality first; no near-zero threshold or dropping a column for MAIN.
    if np.any(np.all(raw == raw[:1], axis=0)):
        return None, dict(reason="constant_column")
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        center = raw.mean(axis=0)
        scale = raw.std(axis=0, ddof=0)
        scaled = (raw-center)/scale
        point = (current-center)/scale
    if (not np.all(np.isfinite(center)) or not np.all(np.isfinite(scale))
            or np.any(scale <= 0) or not np.all(np.isfinite(scaled))
            or not np.all(np.isfinite(point))):
        return None, dict(reason="scale_invalid")
    full = np.column_stack((np.ones(360), scaled))
    main = full[:, :3]
    try:
        # None is NumPy's dtype/shape-dependent default numerical-rank cutoff,
        # frozen ex ante. Deficient rank rejects BOTH; no ridge or fallback.
        bf, _, rankf, sf = np.linalg.lstsq(full, labels, rcond=None)
        bm, _, rankm, sm = np.linalg.lstsq(main, labels, rcond=None)
    except np.linalg.LinAlgError:
        return None, dict(reason="solver_error")
    if rankf != 4 or rankm != 3:
        return None, dict(reason="rank_invalid", ranks=[int(rankf), int(rankm)])
    if not all(np.all(np.isfinite(x)) for x in (bf, bm, sf, sm)):
        return None, dict(reason="coefficient_invalid")
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        x = np.r_[1., point]
        ff = float(x @ bf)
        fm = float(x[:3] @ bm)
        g = float(bf[3]/scale[2])
    if not all(math.isfinite(x) for x in (ff, fm, g)):
        return None, dict(reason="forecast_or_g_invalid")
    evidence = dict(reason="valid", n=360, origins=[42, 401], current_index=407,
        target_indices=[48, 407], current_raw=current.tolist(),
        center=center.tolist(), scale=scale.tolist(),
        coefficients_full=bf.tolist(), coefficients_main=bm.tolist(),
        ranks=[int(rankf), int(rankm)], singular_full=sf.tolist(),
        singular_main=sm.tolist(), g_raw=g,
        forecast_full=ff, forecast_main=fm)
    return (ff, fm), evidence


def interaction_forecasts(rows):
    values = interaction_inputs(rows)
    if values is None:
        return None, dict(reason="data_invalid")
    return interaction_fit(*values)


def empty_interaction_diagnostic():
    return dict(last=None, n=0, g_negative=0, g_zero=0, g_positive=0,
        means={key: dict(available=True, value=None)
               for key in ("g_raw", "forecast_full", "forecast_main")},
        aggregation_errors=0, latest=None)


def interaction_diagnostic(state, now, evidence):
    """O(1), once per valid fit, independent of mode, hurdle, ATR and occupation."""
    if state["last"] is not None and now <= state["last"]:
        return state
    result = dict(state)
    result["last"], result["n"] = int(now), state["n"]+1
    g = evidence["g_raw"]
    key = "g_negative" if g < 0 else "g_positive" if g > 0 else "g_zero"
    result[key] += 1
    result["latest"] = {key: evidence[key]
                        for key in ("g_raw", "forecast_full", "forecast_main")}
    result["means"] = {}
    for key, old in state["means"].items():
        item = dict(old)
        if old["available"]:
            value = evidence[key]
            mean = value if state["n"] == 0 else old["value"]+(value-old["value"])/result["n"]
            if math.isfinite(mean):
                item["value"] = mean
            else:
                # An unavailable descriptive aggregate cannot affect any forecast
                # or the accepted fit. Do not serialize Infinity or invent a mean.
                item.update(available=False, value=None)
                result["aggregation_errors"] += 1
        result["means"][key] = item
    return result


class BtcResearchR27VolumeInteractionBase1m(BtcResearchR12ArBase1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("INTERACTION", "MAIN_EFFECTS")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        last = self.vars.get("interaction_last")
        if last is not None and now <= last:
            return
        self.vars["interaction_last"] = now
        if not self.START < now < self.FINISH:
            return
        counts = self.vars.setdefault("interaction_counts", {})
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 408)
        if rows is None:
            counts["window_invalid"] = counts.get("window_invalid", 0)+1
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        if not math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8):
            # As-of route mismatch is shared invalid data, before either model or
            # diagnostic. It is cash, not a framework invariant that halts a run.
            counts["price_alignment_invalid"] = counts.get("price_alignment_invalid", 0)+1
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        forecasts, evidence = interaction_forecasts(rows)
        reason = evidence["reason"]
        counts[reason] = counts.get(reason, 0)+1
        self.vars["interaction_latest_fit"] = evidence
        if forecasts is None:
            return
        evidence.update(origin=now, window_first=int(rows[0, 0]), window_last=int(rows[-1, 0]))
        # Record BOTH forecasts and raw gamma before all trading gates. MODE and
        # wallet/order state never enter any mathematical/diagnostic helper.
        diagnostic = self.vars.get("interaction_diagnostic", empty_interaction_diagnostic())
        self.vars["interaction_diagnostic"] = interaction_diagnostic(diagnostic, now, evidence)
        forecast = forecasts[0 if self.MODE == "INTERACTION" else 1]
        if abs(forecast) <= .0019:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(rows)
        if atr is None:
            counts["atr_invalid"] = counts.get("atr_invalid", 0)+1
            return
        direction = 1 if forecast > 0 else -1
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            counts["plan_invalid"] = counts.get("plan_invalid", 0)+1
            return
        self.vars["plan"] = dict(plan, interaction_evidence=evidence,
                                forecast=forecast, forecast_origin=now)
        self.vars["direction"] = direction

    def on_open_position(self, order):
        super().on_open_position(order)
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        self._log("R27_OPEN", dict(time=int(self.time), mode=self.MODE,
            forecast=plan["forecast"], forecast_origin=plan["forecast_origin"],
            forecast_deadline=plan["forecast_origin"]+6*BAR,
            opened_at=int(self.position.opened_at),
            hold_deadline=int(self.position.opened_at)+6*BAR,
            entry=float(self.position.entry_price), qty=abs(float(self.position.qty)),
            stop=float(self.position.entry_price)-direction*plan["distance"],
            distance=plan["distance"], risk_budget=plan["risk_budget"]))
        self._log("R27_OPEN_FIT", plan["interaction_evidence"])

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R27_COUNTS", dict(stage=stage, mode=self.MODE,
            counts=self.vars.get("interaction_counts", {}),
            signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
            occupied=self.vars.get("occupied", 0)))
        self._log("R27_DIAGNOSTIC", dict(stage=stage,
            **self.vars.get("interaction_diagnostic", empty_interaction_diagnostic())))
        self._log("R27_LAST_FIT", dict(stage=stage,
            **self.vars.get("interaction_latest_fit", {})))

```
