import json
from datetime import datetime, timezone
import numpy as np
from jesse import utils
from jesse.strategies import Strategy

BAR = 14400000
DAY = 86400000


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


def funding_context(rows, now, family, direction):
    need = 32 if family == 3 else 31
    visible = [r for r in rows if r["available_at"] <= now][-need:]
    result = dict(quality="funding_absent", passed=False, rate=None, z=None, prior_z=None)
    if len(visible) != need:
        return result
    result.update(settled_at=visible[-1].get("settled_at"), available_at=visible[-1]["available_at"])
    rates = np.array([r["rate_decimal"] for r in visible], dtype=float)
    def z_at(values):
        ref = values[:-1]
        std = float(np.std(ref, ddof=0))
        if np.ptp(ref) <= 0 or std <= 0 or not np.isfinite(std):
            return None
        z = (values[-1] - float(np.mean(ref))) / std
        return float(z) if np.isfinite(z) else None
    z = z_at(rates[-31:])
    prior_z = z_at(rates[:-1]) if family == 3 else None
    result.update(rate=float(rates[-1]), z=z, prior_z=prior_z)
    if z is None or (family == 3 and prior_z is None):
        result["quality"] = "funding_variance"
        return result
    result["quality"] = "valid"
    rate = float(rates[-1])
    if family == 1:
        passed = not ((direction == 1 and rate > 0 and z > 2) or
                      (direction == -1 and rate < 0 and z < -2))
    elif family == 2:
        passed = (direction == 1 and rate < 0 and z < -2) or (direction == -1 and rate > 0 and z > 2)
    else:
        old = float(rates[-2])
        passed = ((direction == 1 and old < 0 and prior_z < -2 and old < rate <= 0 and abs(z) <= 2) or
                  (direction == -1 and old > 0 and prior_z > 2 and 0 <= rate < old and abs(z) <= 2))
    result["passed"] = bool(passed)
    return result


def oi_context(history, now, lag_bars=0):
    # Delaying a recorded observation never changes its original freshness test.
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


def feature_self_checks():
    now = 8 * BAR
    candles = np.array([[i * BAR, 100., 100., 110., 90., 1.] for i in range(20)])
    candles[6, 2], candles[7, 2] = 80, 100
    assert price_direction(candles, now, 2) == 1
    candles[6, 2] = 120
    assert price_direction(candles, now, 2) == -1
    candles[6, 2], candles[7, 2] = 119, 120
    assert price_direction(candles, now, 1) == price_direction(candles, now, 3) == 1
    candles[6, 2], candles[7, 2] = 81, 80
    assert price_direction(candles, now, 1) == price_direction(candles, now, 3) == -1
    for family in (1, 2, 3):
        for cutoff in (8 * BAR, 9 * BAR, 12 * BAR):
            prefix = candles[candles[:, 0] + BAR <= cutoff]
            changed = candles.copy()
            changed[changed[:, 0] + BAR > cutoff, 1:5] = 1e9
            assert price_direction(prefix, cutoff, family) == price_direction(candles, cutoff, family)
            assert price_direction(changed, cutoff, family) == price_direction(prefix, cutoff, family)
    rows = [dict(available_at=i * 60000, rate_decimal=(-1 if i % 2 else 1) * .0001) for i in range(36)]
    cutoff = 31 * 60000
    for family in (1, 2, 3):
        for direction in (-1, 1):
            changed = [dict(r) for r in rows]
            for row in changed[32:]:
                row["rate_decimal"] = 1e9
            assert funding_context(rows, cutoff, family, direction) == funding_context(rows[:32], cutoff, family, direction)
            assert funding_context(changed, cutoff, family, direction) == funding_context(rows[:32], cutoff, family, direction)
    for direction in (-1, 1):
        r = [dict(v) for v in rows[:32]]
        r[-2]["rate_decimal"] = -.01 * direction
        r[-1]["rate_decimal"] = -.00001 * direction
        assert funding_context(r, cutoff, 3, direction)["passed"]
        r[-1]["rate_decimal"] = -.01 * direction
        assert funding_context(r, cutoff, 2, direction)["passed"]
        r[-1]["rate_decimal"] = .01 * direction
        assert not funding_context(r, cutoff, 1, direction)["passed"]
    equal = [dict(available_at=i, rate_decimal=.0001) for i in range(32)]
    assert funding_context(equal, 32, 3, 1)["quality"] == "funding_variance"
    history = [dict(time=i * BAR, value=float(i + 1), status="valid", label=i * BAR - 600000) for i in range(10)]
    assert oi_context(history[:6], 5 * BAR)["quality"] == "initialization"
    assert oi_context(history, 6 * BAR)["passed"]
    changed = [dict(v) for v in history]
    for r in changed[7:]:
        r["value"] = 1e9
    assert oi_context(changed, 6 * BAR) == oi_context(history[:7], 6 * BAR)
    changed[6]["status"] = "zero"
    assert oi_context(changed, 6 * BAR)["quality"] == "zero"
    changed[6]["status"] = "stale"
    assert oi_context(changed, 6 * BAR)["quality"] == "stale"
    changed[6]["status"] = "valid"
    changed[0]["status"] = "zero"
    assert oi_context(changed, 6 * BAR)["quality"] == "reference_invalid"
    assert oi_context(history, 7 * BAR, 1) == oi_context(history, 6 * BAR)
    return "passed"


class ResearchWfCore4h(Strategy):
    """Frozen V1 rules; per-fold subclasses set only identity and UTC bounds."""
    FAMILY = 1
    USE_FUNDING = False
    USE_OI = False
    START = 1598918400000
    FINISH = 1640995200000
    STOP = .02
    TARGET = .04
    OI_LAG_BARS = 0
    MASK_FUNDING = False
    MASK_OI = False

    def _bucket(self, month, direction):
        return self.vars.setdefault("audit", {}).setdefault(month + ":" + direction, dict(
            bars=0, opportunities=0, entries=0, exits=0, primary={}, flags={}))

    def before(self):
        now = int(self.time)
        if "self_checks" not in self.vars:
            self.vars["self_checks"] = feature_self_checks()
        direction = price_direction(self.candles, now, self.FAMILY)
        rows = self.get_funding_history(count=32 if self.FAMILY == 3 else 31)
        assert all(r["available_at"] <= now for r in rows)
        funding = funding_context(rows, now, self.FAMILY, direction)
        value, label = self.open_interest, self.open_interest_timestamp
        if value is not None:
            assert value >= 0 and label is not None and label + 360000 <= now <= label + 960000
            self.vars["last_oi_label"] = label
            status = "zero" if value == 0 else "valid"
        else:
            assert label is None
            status = "stale" if "last_oi_label" in self.vars else "absent"
        history = self.vars.setdefault("oi_history", [])
        history.append(dict(time=now, value=value, label=label,
            available_at=label + 360000 if label is not None else None, status=status))
        history[:] = history[-(8 + self.OI_LAG_BARS):]
        oi = oi_context(history, now, self.OI_LAG_BARS)
        day = now // DAY * DAY
        opportunity = (direction != 0 and self.is_close and not self.entry_orders and
                       self.vars.get("entry_day") != day and self.START < now < self.FINISH)
        flags = []
        if funding["quality"] != "valid":
            flags.append(funding["quality"])
        elif not funding["passed"]:
            flags.append("funding_economic")
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
        reason = "allowed"
        if not self.START < now < self.FINISH:
            reason = "boundary"
        elif direction == 0:
            reason = "no_price"
        elif not self.is_close or self.entry_orders:
            reason = "in_position_or_pending"
        elif self.vars.get("entry_day") == day:
            reason = "daily_limit"
        elif (self.USE_FUNDING or self.MASK_FUNDING) and funding["quality"] != "valid":
            reason = funding["quality"]
        elif self.USE_FUNDING and not funding["passed"]:
            reason = "funding_economic"
        elif (self.USE_OI or self.MASK_OI) and oi["quality"] != "valid":
            reason = "oi_" + oi["quality"]
        elif self.USE_OI and not oi["passed"]:
            reason = "oi_nonrising"
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
            allowed=reason == "allowed", funding=funding, oi=oi)

    def should_long(self):
        return self.vars["context"]["allowed"] and self.vars["context"]["direction"] == 1

    def should_short(self):
        return self.vars["context"]["allowed"] and self.vars["context"]["direction"] == -1

    def _enter(self, direction):
        context = self.vars["context"]
        capital, price = self.available_margin, self.price
        stop = price * (1 - direction * self.STOP)
        unit = abs(price - stop) + self.fee_rate * (price + stop)
        qty = utils.size_to_qty(min(capital, .02 * capital / unit * price), price, precision=8)
        assert qty * unit <= .02 * capital + 1e-6
        self.vars["intent"] = dict(capital=capital, decision_price=price, qty=qty, context=context)
        if direction == 1:
            self.buy = qty, price
        else:
            self.sell = qty, price

    def go_long(self):
        self._enter(1)

    def go_short(self):
        self._enter(-1)

    def on_open_position(self, order):
        context = self.vars["intent"]["context"]
        direction = 1 if self.is_long else -1
        entry, qty = self.position.entry_price, abs(self.position.qty)
        self.stop_loss = qty, entry * (1 - direction * self.STOP)
        self.take_profit = qty, entry * (1 + direction * self.TARGET)
        self.vars["entry_day"] = context["day"]
        for d in ("all", "long" if direction == 1 else "short"):
            self._bucket(context["month"], d)["entries"] += 1
        # Bounded, durable intent/fill provenance; full source and parameters in registry.
        self.log("WF_ENTRY " + json.dumps(dict(time=int(self.time), direction=direction,
            capital=self.vars["intent"]["capital"], decision=self.vars["intent"]["decision_price"],
            fill=entry, qty=qty, stop=entry * (1 - direction * self.STOP),
            target=entry * (1 + direction * self.TARGET), funding=context["funding"], oi=context["oi"])))

    def on_close_position(self, order, closed_trade):
        assert abs(self.balance - self.vars["intent"]["capital"] - closed_trade.pnl) < 1e-6
        month = datetime.fromtimestamp((int(self.time) - 1) / 1000, timezone.utc).strftime("%Y-%m")
        for d in ("all", closed_trade.type):
            self._bucket(month, d)["exits"] += 1
        self.log("WF_CLOSE " + json.dumps(dict(time=int(self.time), pnl=closed_trade.pnl,
            balance=self.balance, trade_id=str(closed_trade.id))))

    def update_position(self):
        if self.time - self.position.opened_at >= DAY:
            self.liquidate()

    def should_cancel_entry(self):
        return False

    def before_terminate(self):
        # Framework may force-close a remaining trade after this hook. Its final
        # WF_CLOSE record is authoritative for exits; do not hide that ordering.
        for key, value in sorted(self.vars.get("audit", {}).items()):
            assert value["bars"] == sum(value["primary"].values())
            assert value["entries"] == value["primary"].get("allowed", 0)
            self.log("WF_AUDIT " + json.dumps(dict(key=key, **value), sort_keys=True))
        self.log("WF_PROVENANCE " + json.dumps(dict(self_checks=self.vars.get("self_checks"),
            family=self.FAMILY, funding=self.USE_FUNDING, oi=self.USE_OI, stop=self.STOP,
            target=self.TARGET, hold_ms=DAY, oi_lag_bars=self.OI_LAG_BARS,
            start=self.START, finish=self.FINISH, final_exit_may_follow=True)))
