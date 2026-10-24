# V5 replay — fuentes congeladas y verificación

Autor: /root/audit. Estado PASS técnico, sin autorización de motores o drafts por este documento.

Calendario exclusivo: V5_REPLAY_CALENDAR.json. Ambas variantes elegibles individualmente en C1–C4; cuatro semestres separados, selector OI en todos. START1704067200000 y FINISH1767225600000. SHA256 canónico del calendario: fd82a1bdba7be9d1ae8769e3eb246e903164fe7debfe20309cb109e3a136e536. SHA256 config nominal: 8f9e73c52ecf50f01b6f1f3efdfa98e06081151b15820d46588b5874da5f35cb.

Once clases: dos nominales, ocho vecinos separados de riesgo/señal y un lagOI4h=una barra. Costes S1/S2/S3 modifican configuración, no requieren clases. Core/helper/padres V5 intactos y SHA iguales al snapshot/registro; V2 se captura como dependencia, sin cambiarlo.

Readback MCP exacto 11/11. Compile+AST literal/herencia sin hooks/calls y captured-class checks: **1002 comprobaciones PASS**, job final 7de5d23d0f0e4e1c824e514d2892b887. Fixtures de ventanas estrictas, bordes sin unión, calendar antes de holding/salida indicadora, deduplicación, hold180, salida posterior al fill, OI continuo en inactividad con buffers8/9 y referencias24h/lag4h, calidad original, tamaño stop+fees/riesgo2%/cap1x, protección desde fill/distancia congelada, SMA108/132 y lagprecio27/33, funding adverso independiente y logs<=1900.

El harness no demuestra fills del broker ni orden de cashflows del motor. El contrato contable previo es cashflow funding motor ANTES de decisión calendar en borde interno. Tampoco demuestra el cierre final real: before_terminate permite cierre posterior al AUDIT. Ledger/logs futuros deberán auditarse desde sesiones efectivas.

Incidente únicamente de artefacto temporal: job inicial f8bdd3748eab4bd58bd28073979f98a3 también terminó passed1002, pero escribió JSON al cwd temporal, fuera de output/. No se leyó ese cwd. Segundo job secuencial cambió sólo destino a output/ e import os; artefacto recuperado por get_analysis_artifact. No hubo cambios de señales ni repetición económica. Ambos códigos y raws se conservan en V5_REPLAY_TEST_CODE.json y V5_REPLAY_SOURCE_VERIFICATION.json.

Manifiesto: V5_REPLAY_WRAPPERS.json. Pruebas completas: V5_REPLAY_TEST_RESULTS.json. Fuente de verificación y raws: V5_REPLAY_SOURCE_VERIFICATION.json.

## strategies/ResearchV5FundingFPReplay4h/__init__.py

SHA256 4f46c444582008453d969108ff2a5156170e0f934d20c7c8a4c6f28f1886884d

```python
from strategies.ResearchV5FundingFP4h import ResearchV5FundingFP4h


class ResearchV5FundingFPReplay4h(ResearchV5FundingFP4h):
    # Frozen individual TRAIN calendar; adjacent semesters deliberately stay separate.
    START = 1704067200000
    FINISH = 1767225600000
    USE_OI = False
    OI_LAG_BARS = 0
    PRICE_SMA_PERIOD = 120
    RETURN_LAG = 30
    FUNDING_COUNT = 3
    STOP_MULTIPLIER = 3
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 180
    TARGET_MODE = "none"
    ACTIVE_WINDOWS = ((1704067200000, 1719792000000), (1719792000000, 1735689600000), (1735689600000, 1751328000000), (1751328000000, 1767225600000),)
    FORCE_BOUNDARIES = (1719792000000, 1735689600000, 1751328000000, 1767225600000,)
```

## strategies/ResearchV5FundingFPReplayR09_4h/__init__.py

SHA256 e09c16890e434f621b292390efd62911e926fc88cec4f9231c3e8b868c971428

```python
from strategies.ResearchV5FundingFPReplay4h import ResearchV5FundingFPReplay4h


class ResearchV5FundingFPReplayR09_4h(ResearchV5FundingFPReplay4h):
    # One frozen scenario only; inheritance preserves the nominal TRAIN calendar.
    STOP_MULTIPLIER = 2.7
```

## strategies/ResearchV5FundingFPReplayR11_4h/__init__.py

SHA256 2f80aaddf9e316f5fb3d0a7eb79d840e67ff4d85a39d19ea7721bbc38dcf1de1

```python
from strategies.ResearchV5FundingFPReplay4h import ResearchV5FundingFPReplay4h


class ResearchV5FundingFPReplayR11_4h(ResearchV5FundingFPReplay4h):
    # One frozen scenario only; inheritance preserves the nominal TRAIN calendar.
    STOP_MULTIPLIER = 3.3
```

## strategies/ResearchV5FundingFPReplayA09_4h/__init__.py

SHA256 ad62845e26ae95b25a2d52869b8d2efad37cfc3de4de4da4945794ddfeb92758

```python
from strategies.ResearchV5FundingFPReplay4h import ResearchV5FundingFPReplay4h


class ResearchV5FundingFPReplayA09_4h(ResearchV5FundingFPReplay4h):
    # One frozen scenario only; inheritance preserves the nominal TRAIN calendar.
    PRICE_SMA_PERIOD = 108
    RETURN_LAG = 27
```

## strategies/ResearchV5FundingFPReplayA11_4h/__init__.py

SHA256 94550781cee8a2fb6fa11d7a196a0b1a475f7f417b7688a7e78f5c273e5ed7d0

```python
from strategies.ResearchV5FundingFPReplay4h import ResearchV5FundingFPReplay4h


class ResearchV5FundingFPReplayA11_4h(ResearchV5FundingFPReplay4h):
    # One frozen scenario only; inheritance preserves the nominal TRAIN calendar.
    PRICE_SMA_PERIOD = 132
    RETURN_LAG = 33
```

## strategies/ResearchV5FundingFPOiReplay4h/__init__.py

SHA256 6bdb969805f06ac39eed1e0dfd4721d197499bd068ec10a86b42f51258187517

```python
from strategies.ResearchV5FundingFPOi4h import ResearchV5FundingFPOi4h


class ResearchV5FundingFPOiReplay4h(ResearchV5FundingFPOi4h):
    # Frozen individual TRAIN calendar; adjacent semesters deliberately stay separate.
    START = 1704067200000
    FINISH = 1767225600000
    USE_OI = True
    OI_LAG_BARS = 0
    PRICE_SMA_PERIOD = 120
    RETURN_LAG = 30
    FUNDING_COUNT = 3
    STOP_MULTIPLIER = 3
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 180
    TARGET_MODE = "none"
    ACTIVE_WINDOWS = ((1704067200000, 1719792000000), (1719792000000, 1735689600000), (1735689600000, 1751328000000), (1751328000000, 1767225600000),)
    FORCE_BOUNDARIES = (1719792000000, 1735689600000, 1751328000000, 1767225600000,)
```

## strategies/ResearchV5FundingFPOiReplayR09_4h/__init__.py

SHA256 197b38b4a4890d3f6cec4d12dc73a9d74333a4dfbb91008a0de6b7403bc08c8c

```python
from strategies.ResearchV5FundingFPOiReplay4h import ResearchV5FundingFPOiReplay4h


class ResearchV5FundingFPOiReplayR09_4h(ResearchV5FundingFPOiReplay4h):
    # One frozen scenario only; inheritance preserves the nominal TRAIN calendar.
    STOP_MULTIPLIER = 2.7
```

## strategies/ResearchV5FundingFPOiReplayR11_4h/__init__.py

SHA256 0152e51cb5342f2acb0918b50026bc66810ecdf8a1408aee054dd8a707acf7a4

```python
from strategies.ResearchV5FundingFPOiReplay4h import ResearchV5FundingFPOiReplay4h


class ResearchV5FundingFPOiReplayR11_4h(ResearchV5FundingFPOiReplay4h):
    # One frozen scenario only; inheritance preserves the nominal TRAIN calendar.
    STOP_MULTIPLIER = 3.3
```

## strategies/ResearchV5FundingFPOiReplayA09_4h/__init__.py

SHA256 5b048fcda8f4ee239662d54ca38519069a4af42fcdbdb57dda3b33629e88605d

```python
from strategies.ResearchV5FundingFPOiReplay4h import ResearchV5FundingFPOiReplay4h


class ResearchV5FundingFPOiReplayA09_4h(ResearchV5FundingFPOiReplay4h):
    # One frozen scenario only; inheritance preserves the nominal TRAIN calendar.
    PRICE_SMA_PERIOD = 108
    RETURN_LAG = 27
```

## strategies/ResearchV5FundingFPOiReplayA11_4h/__init__.py

SHA256 b1546b2bef88867140562eba5f92d87019371e2a5b74b10bd7c0d2ce3894b791

```python
from strategies.ResearchV5FundingFPOiReplay4h import ResearchV5FundingFPOiReplay4h


class ResearchV5FundingFPOiReplayA11_4h(ResearchV5FundingFPOiReplay4h):
    # One frozen scenario only; inheritance preserves the nominal TRAIN calendar.
    PRICE_SMA_PERIOD = 132
    RETURN_LAG = 33
```

## strategies/ResearchV5FundingFPOiReplayLag4h/__init__.py

SHA256 8c45d72df968c06cc47af595b88940a5fc28107cd46c80d1e2bb2929c426f6b8

```python
from strategies.ResearchV5FundingFPOiReplay4h import ResearchV5FundingFPOiReplay4h


class ResearchV5FundingFPOiReplayLag4h(ResearchV5FundingFPOiReplay4h):
    # One 4h decision of additional OI lag; price and funding keep their own clocks.
    OI_LAG_BARS = 1
```

# Dependencias capturadas sólo para la verificación

## Captured dependency ResearchV2Core4h

SHA256 577b84ebd15f27f5f598af5a4d1a3d3ed98313797656206c7691d29ad877564b

```python
import hashlib
import json
import math
from datetime import datetime, timezone

import numpy as np
from jesse.strategies import Strategy

BAR = 14400000
DAY = 86400000
ATR_PERIOD = 14
QTY_SCALE = 100000000
ACCOUNTING_TOLERANCE = 1e-6


def atr_window(candles, now):
    """Fourteen arithmetic TRs require fifteen complete, consecutive OHLC bars."""
    rows = candles[candles[:, 0] + BAR <= now][-15:]
    if len(rows) != 15 or rows[-1, 0] != now - BAR:
        return None
    if not np.all(np.diff(rows[:, 0]) == BAR):
        return None
    o, c, h, low = (rows[:, i] for i in (1, 2, 3, 4))
    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):
        return None
    if np.any(h < np.maximum(o, c)) or np.any(low > np.minimum(o, c)) or np.any(h < low):
        return None
    tr = np.maximum(h[1:] - low[1:], np.maximum(abs(h[1:] - c[:-1]), abs(low[1:] - c[:-1])))
    value = float(np.mean(tr))
    if not math.isfinite(value) or value <= 0:
        return None
    return dict(value=value, first=int(rows[0, 0]), last=int(rows[-1, 0]),
                bars=rows[:, :5].tolist())


def h1_direction(candles, now):
    rows = candles[candles[:, 0] + BAR <= now]
    if len(rows) < 2 or rows[-1, 0] != now - BAR or rows[-2, 0] != now - 2 * BAR:
        return 0
    day = now // DAY * DAY
    previous = rows[(rows[:, 0] >= day - DAY) & (rows[:, 0] < day)]
    if len(previous) != 6 or len(set(previous[:, 0])) != 6:
        return 0
    high, low = float(np.max(previous[:, 3])), float(np.min(previous[:, 4]))
    close = float(rows[-1, 2])
    return 1 if close > high else -1 if close < low else 0


def oi_context(history, now, lag_bars=0):
    # Freshness belongs to the original observation, including the lagged scenario.
    target = now - lag_bars * BAR
    current = next((r for r in reversed(history) if r["time"] == target), None)
    reference = next((r for r in reversed(history) if r["time"] == target - DAY), None)
    result = dict(quality="initialization", passed=False, current=current, reference=reference)
    if current is None:
        return result
    if current["status"] != "valid":
        result["quality"] = current["status"]
    elif reference is None:
        result["quality"] = "initialization"
    elif reference["status"] != "valid":
        result["quality"] = "reference_invalid"
    else:
        result["quality"] = "valid"
        result["passed"] = current["value"] > reference["value"]
    return result


def protective_prices(entry, direction, distance):
    """The distance is frozen at decision for ATR, and based on fill for FIXED."""
    stop, target = entry - direction * distance, entry + direction * 2 * distance
    if direction not in (-1, 1) or not all(math.isfinite(x) and x > 0 for x in (entry, distance, stop, target)):
        return None
    return stop, target


def entry_plan(price, capital, fee, direction, distance):
    if not all(math.isfinite(x) and x > 0 for x in (price, capital)):
        return dict(reason="distance_invalid")
    prices = protective_prices(price, direction, distance)
    if prices is None or not math.isfinite(fee) or fee < 0:
        return dict(reason="distance_invalid")
    stop, target = prices
    # Protocol budgets 2% for stop plus round-trip fees; leverage never scales quantity.
    unit = distance + fee * (price + stop)
    raw = min(capital / price, .02 * capital / unit)
    qty = math.floor(raw * QTY_SCALE) / QTY_SCALE
    if qty <= 0:
        return dict(reason="qty_invalid")
    assert qty * unit <= .02 * capital + ACCOUNTING_TOLERANCE
    assert qty * price <= capital + ACCOUNTING_TOLERANCE
    return dict(reason="allowed", price=price, capital=capital, fee=fee, qty=qty,
                distance=distance, stop=stop, target=target, unit_loss=unit,
                risk_budget=.02 * capital, planned_stop_loss=qty * unit)


class ResearchV2Core4h(Strategy):
    """Independent V2 implementation; V1 source is never modified or inherited."""
    USE_ATR = True
    USE_OI = False
    ATR_MULTIPLIER = 2.
    FIXED_STOP = .02
    OI_LAG_BARS = 0
    START = 1598918400000
    FINISH = 1640995200000

    def _bucket(self, month, direction):
        return self.vars.setdefault("audit", {}).setdefault(month + ":" + direction, dict(
            bars=0, opportunities=0, entries=0, exits=0, primary={}, flags={}))

    def _log_json(self, label, payload):
        line = label + " " + json.dumps(payload, separators=(",", ":"), allow_nan=False)
        # Framework truncates long log lines; fail instead of silently losing provenance.
        assert len(line) <= 1900
        self.log(line)

    def before(self):
        now = int(self.time)
        direction = h1_direction(self.candles, now)
        atr = atr_window(self.candles, now)
        value, label = self.open_interest, self.open_interest_timestamp
        if value is not None:
            # Frozen archive policy: label +6m availability, then at most 10m of freshness.
            assert value >= 0 and label is not None and label + 360000 <= now <= label + 960000
            self.vars["last_oi_label"] = label
            status = "zero" if value == 0 else "valid"
        else:
            assert label is None
            status = "stale" if "last_oi_label" in self.vars else "absent"
        history = self.vars.setdefault("oi_history", [])
        history.append(dict(time=now, value=value, label=label,
                            available_at=label + 360000 if label is not None else None, status=status))
        # Six 4h steps form 24h; keep current, lag and one spare without backfilling.
        history[:] = history[-(8 + self.OI_LAG_BARS):]
        oi = oi_context(history, now, self.OI_LAG_BARS)
        funding_rows = self.get_funding_history(count=1)
        assert all(r["available_at"] <= now for r in funding_rows)
        funding = funding_rows[-1] if funding_rows else None
        day = now // DAY * DAY
        opportunity = bool(direction and self.is_close and not self.entry_orders and
                           self.vars.get("entry_day") != day and self.START < now < self.FINISH)
        flags = []
        current, reference = oi["current"], oi["reference"]
        if current is None:
            flags.append("oi_initialization")
        elif current["status"] != "valid":
            flags.append("oi_" + current["status"])
        if reference is None:
            if "oi_initialization" not in flags:
                flags.append("oi_initialization")
        elif reference["status"] != "valid":
            flags.append("oi_reference_invalid")
        if oi["quality"] == "valid" and not oi["passed"]:
            flags.append("oi_nonrising")
        if atr is None:
            flags.append("atr_invalid")
        plan = None
        reason = "allowed"
        # Preserve V1 gate precedence; the new distance checks follow the OI gates.
        if not self.START < now < self.FINISH:
            reason = "boundary"
        elif direction == 0:
            reason = "no_price"
        elif not self.is_close or self.entry_orders:
            reason = "in_position_or_pending"
        elif self.vars.get("entry_day") == day:
            reason = "daily_limit"
        elif self.USE_OI and oi["quality"] != "valid":
            reason = "oi_" + oi["quality"]
        elif self.USE_OI and not oi["passed"]:
            reason = "oi_nonrising"
        elif self.USE_ATR and atr is None:
            reason = "atr_invalid"
        else:
            distance = self.ATR_MULTIPLIER * atr["value"] if self.USE_ATR else self.FIXED_STOP * self.price
            plan = entry_plan(self.price, self.available_margin, self.fee_rate, direction, distance)
            reason = plan["reason"]
        if reason in ("distance_invalid", "qty_invalid"):
            flags.append(reason)
        month = datetime.fromtimestamp((now - 1) / 1000, timezone.utc).strftime("%Y-%m")
        key = "long" if direction == 1 else "short" if direction == -1 else "none"
        for bucket_direction in ("all", key):
            bucket = self._bucket(month, bucket_direction)
            bucket["bars"] += 1
            bucket["opportunities"] += int(opportunity)
            bucket["primary"][reason] = bucket["primary"].get(reason, 0) + 1
            if opportunity:
                for flag in flags:
                    bucket["flags"][flag] = bucket["flags"].get(flag, 0) + 1
        self.vars["context"] = dict(time=now, day=day, month=month, direction=direction,
                                   allowed=reason == "allowed", oi=oi, atr=atr, plan=plan, funding=funding)

    def should_long(self):
        return self.vars["context"]["allowed"] and self.vars["context"]["direction"] == 1

    def should_short(self):
        return self.vars["context"]["allowed"] and self.vars["context"]["direction"] == -1

    def _enter(self, direction):
        context = self.vars["context"]
        plan = context["plan"]
        assert plan and plan["reason"] == "allowed" and context["direction"] == direction
        self.vars.pop("exit_reason", None)
        self.vars["intent"] = dict(plan=plan, context=context)
        if direction == 1:
            self.buy = plan["qty"], plan["price"]
        else:
            self.sell = plan["qty"], plan["price"]

    def go_long(self):
        self._enter(1)

    def go_short(self):
        self._enter(-1)

    def on_open_position(self, order):
        intent = self.vars["intent"]
        context, plan = intent["context"], intent["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = self.position.entry_price, abs(self.position.qty)
        distance = plan["distance"] if self.USE_ATR else self.FIXED_STOP * entry
        prices = protective_prices(entry, direction, distance)
        self.vars["entry_day"] = context["day"]
        for side in ("all", "long" if direction == 1 else "short"):
            self._bucket(context["month"], side)["entries"] += 1
        atr = context["atr"]
        provenance = None
        if atr is not None:
            # Hash canonical UTF-8 OHLC payload, not a platform-dependent ndarray buffer.
            digest = hashlib.sha256(json.dumps(atr["bars"], separators=(",", ":"), allow_nan=False).encode()).hexdigest()
            provenance = dict(value=atr["value"], first=atr["first"], last=atr["last"], bars=15, sha256=digest)
        self._log_json("V2_ENTRY", dict(time=int(self.time), direction=direction, decision=plan["price"],
            fill=entry, capital=plan["capital"], qty=qty, distance_pre=plan["distance"], distance_fill=distance,
            planned_stop_loss=plan["planned_stop_loss"], risk_budget=plan["risk_budget"],
            stop=prices[0] if prices else None, target=prices[1] if prices else None,
            atr=provenance, oi=context["oi"], funding=context["funding"]))
        if prices is None:
            # No invalid protective order is submitted. Entry remains in the audit and PnL.
            self.vars["exit_reason"] = "invalid_after_fill"
            for side in ("all", "long" if direction == 1 else "short"):
                bucket = self._bucket(context["month"], side)
                bucket["flags"]["invalid_after_fill"] = bucket["flags"].get("invalid_after_fill", 0) + 1
            self._log_json("V2_EXIT_REQUEST", dict(time=int(self.time), reason="invalid_after_fill"))
            self.liquidate()
            return
        self.stop_loss = qty, prices[0]
        self.take_profit = qty, prices[1]

    def update_position(self):
        if self.time - self.position.opened_at >= DAY:
            self.vars["exit_reason"] = "holding_24h"
            self._log_json("V2_EXIT_REQUEST", dict(time=int(self.time), reason="holding_24h"))
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        intent = self.vars["intent"]
        assert abs(self.balance - intent["plan"]["capital"] - closed_trade.pnl) < ACCOUNTING_TOLERANCE
        direction = 1 if closed_trade.type == "long" else -1
        gross = direction * (closed_trade.exit_price - closed_trade.entry_price) * closed_trade.qty
        reason = self.vars.get("exit_reason") or order.submitted_via or "unclassified"
        assert reason != "unclassified"
        month = datetime.fromtimestamp((int(self.time) - 1) / 1000, timezone.utc).strftime("%Y-%m")
        for side in ("all", closed_trade.type):
            self._bucket(month, side)["exits"] += 1
        self._log_json("V2_CLOSE", dict(time=int(self.time), trade_id=str(closed_trade.id),
            reason=reason, pnl=closed_trade.pnl, balance=self.balance, gross=gross,
            risk_budget=intent["plan"]["risk_budget"],
            realized_loss=max(0., -closed_trade.pnl),
            loss_over_budget=max(0., -closed_trade.pnl - intent["plan"]["risk_budget"])))

    def should_cancel_entry(self):
        return False

    def before_terminate(self):
        # Framework closes positions after this hook; preserve the explicit border motive.
        if self.is_open:
            self.vars["exit_reason"] = "fold_end"
            self._log_json("V2_EXIT_REQUEST", dict(time=int(self.time), reason="fold_end"))
        for key, value in sorted(self.vars.get("audit", {}).items()):
            assert value["bars"] == sum(value["primary"].values())
            assert value["entries"] == value["primary"].get("allowed", 0)
            self._log_json("V2_AUDIT", dict(key=key, **value))
        self._log_json("V2_PROVENANCE", dict(atr=self.USE_ATR, period=ATR_PERIOD,
            multiplier=self.ATR_MULTIPLIER, fixed_stop=self.FIXED_STOP, oi=self.USE_OI,
            oi_lag_bars=self.OI_LAG_BARS, hold_ms=DAY, start=self.START, finish=self.FINISH,
            final_exit_may_follow=True, self_checks=self.vars.get("self_checks")))
```

## Captured dependency ResearchV5Base4h

SHA256 5e0124dbc86305cccfdbbd857ba158a2e7dc10c9fdf2a905f31cfc1dd59890aa

```python
import hashlib
import json
import math
from datetime import datetime, timezone

import numpy as np

from strategies.ResearchV2Core4h import (
    ResearchV2Core4h, ACCOUNTING_TOLERANCE,
)

# V5 4h decisions use explicit local clocks; only neutral V2 hooks are inherited.
BAR = 14400000
DAY = 86400000
OI_REFERENCE_BARS = 6


def closed_window(candles, now, count):
    """Finite OHLC with exactly the causal, consecutive window requested."""
    if (not isinstance(candles, np.ndarray) or candles.ndim != 2 or
            candles.shape[1] < 5 or count < 1 or now % BAR):
        return None
    rows = candles[candles[:, 0] + BAR <= now][-count:]
    if len(rows) != count or rows[-1, 0] != now - BAR or not np.all(np.diff(rows[:, 0]) == BAR):
        return None
    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):
        return None
    o, c, h, low = (rows[:, i] for i in (1, 2, 3, 4))
    if np.any(h < np.maximum(o, c)) or np.any(low > np.minimum(o, c)) or np.any(h < low):
        return None
    return rows


def atr_window(candles, now, offset_bars=0):
    """Arithmetic TR, with shock risk frozen before the event when offset is one."""
    if offset_bars not in (0, 1):
        return None
    rows = closed_window(candles, now, 15 + offset_bars)
    if rows is None:
        return None
    if offset_bars:
        rows = rows[:-offset_bars]
    close, high, low = (rows[:, i] for i in (2, 3, 4))
    tr = np.maximum(high[1:] - low[1:],
                    np.maximum(abs(high[1:] - close[:-1]), abs(low[1:] - close[:-1])))
    value = float(np.mean(tr))
    if not math.isfinite(value) or value <= 0:
        return None
    return dict(value=value, first=int(rows[0, 0]), last=int(rows[-1, 0]),
                bars=rows[:, :5].tolist(), offset_bars=offset_bars)


def _oi_record_valid(record):
    """Freshness remains attached to its original decision, including delayed tests."""
    try:
        value, label, available, observed = (record[k] for k in
                                             ("value", "label", "available_at", "time"))
        return (record["status"] == "valid" and value is not None and
                math.isfinite(value) and value > 0 and label is not None and
                available == label + 360000 and available <= observed <= available + 600000)
    except (KeyError, TypeError, ValueError):
        # Missing/malformed provenance is invalid data, never an as-of replacement.
        return False


def oi_context(history, now, lag_bars=0):
    target = now - lag_bars * BAR
    current = next((r for r in reversed(history) if r["time"] == target), None)
    reference = next((r for r in reversed(history) if r["time"] == target - DAY), None)
    result = dict(quality="initialization", passed=False, current=current, reference=reference)
    if current is None:
        return result
    if current["status"] != "valid":
        result["quality"] = current["status"]
    elif not _oi_record_valid(current):
        result["quality"] = "invalid"
    elif reference is None:
        result["quality"] = "initialization"
    elif not _oi_record_valid(reference):
        result["quality"] = "reference_invalid"
    else:
        result["quality"] = "valid"
        result["passed"] = bool(current["value"] > reference["value"])
    return result


def v5_entry_plan(price, capital, fee, direction, distance):
    """Risk includes both taker fees; absence of TP does not create a fake target."""
    stop = price - direction * distance
    if direction not in (-1, 1) or not all(math.isfinite(v) and v > 0 for v in (price, capital, distance, stop)):
        return dict(reason="distance_invalid")
    if not math.isfinite(fee) or fee < 0:
        return dict(reason="distance_invalid")
    unit = distance + fee * (price + stop)
    # Eight decimals and 2% plus the notional cap are frozen research conventions.
    qty = math.floor(min(capital / price, .02 * capital / unit) * 1e8) / 1e8
    if qty <= 0:
        return dict(reason="qty_invalid")
    assert qty * unit <= .02 * capital + ACCOUNTING_TOLERANCE
    assert qty * price <= capital + ACCOUNTING_TOLERANCE
    return dict(reason="allowed", price=price, capital=capital, fee=fee, qty=qty,
                distance=distance, stop=stop, unit_loss=unit,
                risk_budget=.02 * capital, planned_stop_loss=qty * unit)


class ResearchV5Base4h(ResearchV2Core4h):
    """4h context and execution; frozen V2 contributes only clock-neutral hooks."""
    LINE = "abstract"
    TARGET_MODE = "none"
    REWARD_MULTIPLE = 1.
    MAX_HOLD_BARS = 24
    STOP_MULTIPLIER = 2.
    ATR_OFFSET_BARS = 0
    START = 1598918400000
    FINISH = 1704067200000
    USE_OI = False
    OI_LAG_BARS = 0
    ACTIVE_WINDOWS = None
    FORCE_BOUNDARIES = ()

    def features(self, candles, now, atr):
        raise NotImplementedError

    def on_v5_open(self):
        pass

    def manage_position(self, atr):
        pass

    def _log_json(self, label, payload):
        # Preserve inherited accounting labels while identifying this new hourly cycle.
        if label.startswith("V2_"):
            label = "V5_" + label[3:]
        super()._log_json(label, payload)

    def _entry_window(self, now):
        return (self.START < now < self.FINISH and
                (self.ACTIVE_WINDOWS is None or any(a < now < b for a, b in self.ACTIVE_WINDOWS)))

    def _target(self, price, direction, distance, features):
        if self.TARGET_MODE == "none":
            return None
        assert self.TARGET_MODE == "r_multiple"
        return price + direction * self.REWARD_MULTIPLE * distance

    @staticmethod
    def _target_valid(target, price, direction):
        return target is None or (math.isfinite(target) and target > 0 and direction * (target - price) > 0)

    def before(self):
        now = int(self.time)
        atr = atr_window(self.candles, now, self.ATR_OFFSET_BARS)
        features = self.features(self.candles, now, atr)
        assert isinstance(features, dict) and features["direction"] in (-1, 0, 1)
        assert isinstance(features["valid"], bool) and isinstance(features.get("reason", "no_setup"), str)
        direction = int(features["direction"])
        value, label = self.open_interest, self.open_interest_timestamp
        if value is not None:
            # Frozen retrospective policy: availability label+6m, freshness another10m.
            assert math.isfinite(value) and value >= 0 and label is not None and label + 360000 <= now <= label + 960000
            self.vars["last_oi_label"] = label
            status = "zero" if value == 0 else "valid"
        else:
            assert label is None
            status = "stale" if "last_oi_label" in self.vars else "absent"
        history = self.vars.setdefault("oi_history", [])
        history.append(dict(time=now, value=value, label=label,
                            available_at=label + 360000 if label is not None else None, status=status))
        # Exact 24h reference in this clock, delayed scenario and one spare; no backfill.
        history[:] = history[-(OI_REFERENCE_BARS + 2 + self.OI_LAG_BARS):]
        oi = oi_context(history, now, self.OI_LAG_BARS)
        funding_rows = self.get_funding_history(count=1)
        assert all(r["available_at"] <= now for r in funding_rows)
        funding = funding_rows[-1] if funding_rows else None
        day = now // DAY * DAY
        opportunity = bool(direction and self.is_close and not self.entry_orders and
                           self.vars.get("entry_day") != day and self.vars.get("v5_last_exit_at") != now and
                           self._entry_window(now))
        flags = []
        current, reference = oi["current"], oi["reference"]
        if current is None:
            flags.append("oi_initialization")
        elif current["status"] != "valid":
            flags.append("oi_" + current["status"])
        if reference is None:
            if "oi_initialization" not in flags:
                flags.append("oi_initialization")
        elif reference["status"] != "valid":
            flags.append("oi_reference_invalid")
        if oi["quality"] == "valid" and not oi["passed"]:
            flags.append("oi_nonrising")
        if atr is None:
            flags.append("atr_invalid")
        if not features["valid"]:
            flags.append("features_invalid")
        plan = None
        reason = "allowed"
        if not self._entry_window(now):
            reason = "boundary_or_inactive"
        elif atr is None:
            reason = "atr_invalid"
        elif not features["valid"]:
            reason = "features_invalid"
        elif direction == 0:
            reason = features.get("reason", "no_setup")
        elif self.vars.get("v5_last_exit_at") == now:
            reason = "same_decision_exit"
        elif not self.is_close or self.entry_orders:
            reason = "in_position_or_pending"
        elif self.vars.get("entry_day") == day:
            reason = "daily_limit"
        elif self.USE_OI and oi["quality"] != "valid":
            reason = "oi_" + oi["quality"]
        elif self.USE_OI and not oi["passed"]:
            reason = "oi_nonrising"
        else:
            distance = self.STOP_MULTIPLIER * atr["value"]
            plan = v5_entry_plan(self.price, self.available_margin, self.fee_rate, direction, distance)
            reason = plan["reason"]
            if reason == "allowed":
                target = self._target(plan["price"], direction, distance, features)
                if not self._target_valid(target, plan["price"], direction):
                    reason = "target_invalid"
        if reason in ("distance_invalid", "qty_invalid", "target_invalid"):
            flags.append(reason)
        month = datetime.fromtimestamp((now - 1) / 1000, timezone.utc).strftime("%Y-%m")
        key = "long" if direction == 1 else "short" if direction == -1 else "none"
        for bucket_direction in ("all", key):
            bucket = self._bucket(month, bucket_direction)
            feature_reason = features.get("reason", "no_setup")
            reasons = bucket.setdefault("feature_reasons", {})
            reasons[feature_reason] = reasons.get(feature_reason, 0) + 1
            bucket["bars"] += 1
            bucket["opportunities"] += int(opportunity)
            bucket["primary"][reason] = bucket["primary"].get(reason, 0) + 1
            if opportunity:
                for flag in flags:
                    bucket["flags"][flag] = bucket["flags"].get(flag, 0) + 1
        self.vars["context"] = dict(time=now, day=day, month=month, direction=direction,
            allowed=reason == "allowed", oi=oi, atr=atr, plan=plan, funding=funding, features=features)

    def request_exit(self, reason):
        # Multiple close conditions at the same decision must not double-submit exits.
        if not self.is_open or self.vars.get("v5_exit_requested_at") == int(self.time):
            return
        self.vars["v5_exit_requested_at"] = int(self.time)
        self.vars["exit_reason"] = reason
        self._log_json("V5_EXIT_REQUEST", dict(time=int(self.time), reason=reason))
        self.liquidate()

    def on_open_position(self, order):
        intent = self.vars["intent"]
        context, plan = intent["context"], intent["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = self.position.entry_price, abs(self.position.qty)
        distance = plan["distance"]
        stop = entry - direction * distance
        target = self._target(entry, direction, distance, context["features"])
        self.vars.pop("v5_exit_requested_at", None)
        self.vars["entry_day"] = context["day"]
        for side in ("all", "long" if direction == 1 else "short"):
            self._bucket(context["month"], side)["entries"] += 1
        atr = context["atr"]
        digest = hashlib.sha256(json.dumps(atr["bars"], separators=(",", ":"), allow_nan=False).encode()).hexdigest()
        self._log_json("V5_FEATURES", dict(time=int(self.time), line=self.LINE,
                                        **context["features"]))
        self._log_json("V5_ENTRY", dict(time=int(self.time), direction=direction, decision=plan["price"],
            fill=entry, capital=plan["capital"], qty=qty, distance_pre=distance, distance_fill=distance,
            planned_stop_loss=plan["planned_stop_loss"], risk_budget=plan["risk_budget"],
            stop=stop, target=target, atr=dict(value=atr["value"], first=atr["first"], last=atr["last"],
                                             bars=15, offset_bars=self.ATR_OFFSET_BARS, sha256=digest), oi=context["oi"], funding=context["funding"]))
        self.vars["v5_trade"] = dict(entry_at=int(self.position.opened_at), entry_atr=atr["value"],
                                    entry_fill=entry, distance=distance, stop_price=stop, target_price=target)
        if not math.isfinite(stop) or stop <= 0 or not self._target_valid(target, entry, direction):
            for side in ("all", "long" if direction == 1 else "short"):
                bucket = self._bucket(context["month"], side)
                bucket["flags"]["invalid_after_fill"] = bucket["flags"].get("invalid_after_fill", 0) + 1
            self.request_exit("invalid_after_fill")
            return
        self.stop_loss = qty, stop
        if target is not None:
            self.take_profit = qty, target
        self.on_v5_open()

    def update_position(self):
        # Calendar and elapsed holding exits take priority over indicator normalization.
        if any(self.time - BAR < boundary <= self.time for boundary in self.FORCE_BOUNDARIES):
            self.request_exit("calendar_boundary")
            return
        if self.time - self.position.opened_at >= self.MAX_HOLD_BARS * BAR:
            self.request_exit("maximum_hold")
            return
        # Indicator exits may only use a close after the fill, never its entry decision.
        if self.time > self.position.opened_at:
            self.manage_position(self.vars["context"]["atr"])

    def on_close_position(self, order, closed_trade):
        self.vars["v5_last_exit_at"] = int(closed_trade.closed_at)
        super().on_close_position(order, closed_trade)

    def before_terminate(self):
        if self.is_open:
            self.vars["exit_reason"] = "fold_end"
            self._log_json("V5_EXIT_REQUEST", dict(time=int(self.time), reason="fold_end"))
        for key, value in sorted(self.vars.get("audit", {}).items()):
            assert value["bars"] == sum(value["primary"].values())
            assert value["entries"] == value["primary"].get("allowed", 0)
            assert value["bars"] == sum(value.get("feature_reasons", {}).values())
            self._log_json("V5_AUDIT", dict(key=key, **value))
        self._log_json("V5_PROVENANCE", dict(line=self.LINE, use_oi=self.USE_OI,
            oi_lag_bars=self.OI_LAG_BARS, stop_multiplier=self.STOP_MULTIPLIER,
            bar_ms=BAR, oi_reference_bars=OI_REFERENCE_BARS,
            atr_offset_bars=self.ATR_OFFSET_BARS, target_mode=self.TARGET_MODE,
            reward_multiple=self.REWARD_MULTIPLE, max_hold_bars=self.MAX_HOLD_BARS,
            start=self.START, finish=self.FINISH, active_windows=self.ACTIVE_WINDOWS,
            force_boundaries=self.FORCE_BOUNDARIES, final_exit_may_follow=True,
            self_checks=self.vars.get("self_checks")))
```

## Captured dependency funding_features

SHA256 a9e7d666706c41624deebfd19d905331296efd9839f6d28e68a615cec82f12ce

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

## Captured dependency ResearchV5FundingFP4h

SHA256 ef0ea4ff2e9e5444a5ee0da2d0a35d0c8d92a6d939172d24244aff15646edefd

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

## Captured dependency ResearchV5FundingFPOi4h

SHA256 c702e26a6ebd33e76af2861914e4ce9732c98375a12a3df86d3c41d91ac74dee

```python
from strategies.ResearchV5FundingFP4h import ResearchV5FundingFP4h


class ResearchV5FundingFPOi4h(ResearchV5FundingFP4h):
    USE_OI = True
```
