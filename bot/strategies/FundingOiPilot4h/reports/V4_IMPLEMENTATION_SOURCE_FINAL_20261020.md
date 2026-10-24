# V4 final implementation before economic runs

## strategies/ResearchV4Base1h/__init__.py
SHA256: 8f543abebd045e374f16a51b64a8b5223645ebf92a705d256c21cd87b86155e9

```python
import hashlib
import json
import math
from datetime import datetime, timezone

import numpy as np

from strategies.ResearchV2Core4h import (
    ResearchV2Core4h, ACCOUNTING_TOLERANCE,
)

# V4 decisions are hourly; no imported 4h indicator or clock is reused.
BAR = 3600000
DAY = 86400000
OI_REFERENCE_BARS = 24


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


def v4_entry_plan(price, capital, fee, direction, distance):
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


class ResearchV4Base1h(ResearchV2Core4h):
    """Hourly context and execution; frozen V2 contributes only clock-neutral hooks."""
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

    def on_v4_open(self):
        pass

    def manage_position(self, atr):
        pass

    def _log_json(self, label, payload):
        # Preserve inherited accounting labels while identifying this new hourly cycle.
        if label.startswith("V2_"):
            label = "V4_" + label[3:]
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
        # Twenty-four actual hourly decisions, delayed scenario and one spare; no backfill.
        history[:] = history[-(26 + self.OI_LAG_BARS):]
        oi = oi_context(history, now, self.OI_LAG_BARS)
        funding_rows = self.get_funding_history(count=1)
        assert all(r["available_at"] <= now for r in funding_rows)
        funding = funding_rows[-1] if funding_rows else None
        day = now // DAY * DAY
        opportunity = bool(direction and self.is_close and not self.entry_orders and
                           self.vars.get("entry_day") != day and self.vars.get("v4_last_exit_at") != now and
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
        elif self.vars.get("v4_last_exit_at") == now:
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
            plan = v4_entry_plan(self.price, self.available_margin, self.fee_rate, direction, distance)
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
        # Updating a trailing stop and a holding boundary must not double-submit exits.
        if not self.is_open or self.vars.get("v4_exit_requested_at") == int(self.time):
            return
        self.vars["v4_exit_requested_at"] = int(self.time)
        self.vars["exit_reason"] = reason
        self._log_json("V4_EXIT_REQUEST", dict(time=int(self.time), reason=reason))
        self.liquidate()

    def on_open_position(self, order):
        intent = self.vars["intent"]
        context, plan = intent["context"], intent["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = self.position.entry_price, abs(self.position.qty)
        distance = plan["distance"]
        stop = entry - direction * distance
        target = self._target(entry, direction, distance, context["features"])
        self.vars.pop("v4_exit_requested_at", None)
        self.vars["entry_day"] = context["day"]
        for side in ("all", "long" if direction == 1 else "short"):
            self._bucket(context["month"], side)["entries"] += 1
        atr = context["atr"]
        digest = hashlib.sha256(json.dumps(atr["bars"], separators=(",", ":"), allow_nan=False).encode()).hexdigest()
        self._log_json("V4_FEATURES", dict(time=int(self.time), line=self.LINE,
                                        **context["features"]))
        self._log_json("V4_ENTRY", dict(time=int(self.time), direction=direction, decision=plan["price"],
            fill=entry, capital=plan["capital"], qty=qty, distance_pre=distance, distance_fill=distance,
            planned_stop_loss=plan["planned_stop_loss"], risk_budget=plan["risk_budget"],
            stop=stop, target=target, atr=dict(value=atr["value"], first=atr["first"], last=atr["last"],
                                             bars=15, offset_bars=self.ATR_OFFSET_BARS, sha256=digest), oi=context["oi"], funding=context["funding"]))
        self.vars["v4_trade"] = dict(entry_at=int(self.position.opened_at), entry_atr=atr["value"],
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
        self.on_v4_open()

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
        self.vars["v4_last_exit_at"] = int(closed_trade.closed_at)
        super().on_close_position(order, closed_trade)

    def before_terminate(self):
        if self.is_open:
            self.vars["exit_reason"] = "fold_end"
            self._log_json("V4_EXIT_REQUEST", dict(time=int(self.time), reason="fold_end"))
        for key, value in sorted(self.vars.get("audit", {}).items()):
            assert value["bars"] == sum(value["primary"].values())
            assert value["entries"] == value["primary"].get("allowed", 0)
            assert value["bars"] == sum(value.get("feature_reasons", {}).values())
            self._log_json("V4_AUDIT", dict(key=key, **value))
        self._log_json("V4_PROVENANCE", dict(line=self.LINE, use_oi=self.USE_OI,
            oi_lag_bars=self.OI_LAG_BARS, stop_multiplier=self.STOP_MULTIPLIER,
            bar_ms=BAR, oi_reference_bars=OI_REFERENCE_BARS,
            atr_offset_bars=self.ATR_OFFSET_BARS, target_mode=self.TARGET_MODE,
            reward_multiple=self.REWARD_MULTIPLE, max_hold_bars=self.MAX_HOLD_BARS,
            start=self.START, finish=self.FINISH, active_windows=self.ACTIVE_WINDOWS,
            force_boundaries=self.FORCE_BOUNDARIES, final_exit_may_follow=True,
            self_checks=self.vars.get("self_checks")))

```

## strategies/ResearchV4Base1h/common_checks.py
SHA256: e78f335738e8f92e3bea84805af2705bc2d6e325d7700d41e4fd9ae92d18be6e

```python
import json
import math
from types import SimpleNamespace
import numpy as np
from strategies.ResearchV4Base1h import (
    ResearchV4Base1h, BAR, DAY, closed_window, atr_window, oi_context, v4_entry_plan,
)

def self_checks():
    """Artificial scalar state checks scheduling/risk; it does not simulate broker fills."""
    checks = 0
    def check(value):
        nonlocal checks
        assert value
        checks += 1
    now = 400 * BAR
    candles = np.array([[t,100.,100.,101.,99.,1.] for t in range(now-240*BAR,now,BAR)])
    check(closed_window(candles,now,224).shape == (224,6))
    future = np.vstack([candles,[now,100,100,1000,1,1]])
    check(np.array_equal(closed_window(future,now,224),closed_window(candles,now,224)))
    check(closed_window(candles,now+1,15) is None)
    for column,value in ((0,now-2*BAR),(2,float("nan")),(3,98.)):
        bad=candles.copy(); bad[-1,column]=value
        check(closed_window(bad,now,15) is None)
    check(closed_window(candles[:-1],now,15) is None)
    check(atr_window(candles,now)["value"] == 2.)
    shock=candles.copy();shock[-1,3]=129.
    check(atr_window(shock,now)["value"] > 2.)
    check(atr_window(shock,now,1)["value"] == 2.)
    check(atr_window(candles[-15:],now,1) is None)
    check(atr_window(candles,now,2) is None)
    history=[dict(time=now+i*BAR,value=100.+i,label=now+i*BAR-600000,
                  available_at=now+i*BAR-240000,status="valid") for i in range(31)]
    check(oi_context(history[:24],now+23*BAR)["quality"] == "initialization")
    check(oi_context(history[:25],now+24*BAR)["passed"])
    check(oi_context(history[:28],now+27*BAR,4)["quality"] == "initialization")
    check(oi_context(history[:29],now+28*BAR,4)["passed"])
    bad=[dict(r) for r in history];bad[0]["value"]=0
    check(oi_context(bad,now+24*BAR)["quality"] == "reference_invalid")
    bad=[dict(r) for r in history];bad[24]["value"]=100.
    check(not oi_context(bad,now+24*BAR)["passed"])
    bad=[dict(r) for r in history];bad[24]["available_at"]=bad[24]["time"]+1
    check(oi_context(bad,now+24*BAR)["quality"] == "invalid")
    for direction in (-1,1):
        plan=v4_entry_plan(100.,10000.,.00045,direction,4.)
        check(plan["reason"] == "allowed")
        check(plan["qty"]*plan["unit_loss"] <= 200.+1e-8)
        check(plan["qty"]*100 <= 10000.)
        check(plan["qty"] == math.floor(plan["qty"]*1e8+.01)/1e8)
    check(v4_entry_plan(100.,10000.,-.1,1,4.)["reason"] == "distance_invalid")
    check(v4_entry_plan(100.,10000.,.00045,1,101.)["reason"] == "distance_invalid")
    class Surface:
        _entry_window=ResearchV4Base1h._entry_window
        _target=ResearchV4Base1h._target
        _target_valid=staticmethod(ResearchV4Base1h._target_valid)
        request_exit=ResearchV4Base1h.request_exit
        def __init__(self):
            self.vars={};self.time=now;self.START=now-50*BAR;self.FINISH=now+100*BAR
            self.ACTIVE_WINDOWS=None;self.FORCE_BOUNDARIES=()
            self.TARGET_MODE="none";self.REWARD_MULTIPLE=1.;self.MAX_HOLD_BARS=24
            self.STOP_MULTIPLIER=2.;self.ATR_OFFSET_BARS=0;self.OI_LAG_BARS=0
            self.USE_OI=False;self.LINE="test";self.candles=candles
            self.open_interest=100.;self.open_interest_timestamp=now-600000
            self.price=100.;self.available_margin=10000.;self.fee_rate=.00045
            self.is_open=False;self.is_close=True;self.is_long=True;self.entry_orders=[]
            self.position=SimpleNamespace(opened_at=now,entry_price=100.,qty=1.)
            self.exits=0;self.managed=0;self.opened=0;self.logs=[]
        def features(self,*args):return dict(valid=True,direction=1,reason="setup")
        def get_funding_history(self,**kwargs):return []
        def _bucket(self,month,direction):
            return self.vars.setdefault("audit",{}).setdefault(month+direction,
                dict(bars=0,entries=0,opportunities=0,primary={},flags={}))
        def _log_json(self,label,payload):
            check(len(label+" "+json.dumps(payload,allow_nan=False,separators=(",",":"))) <= 1900)
            self.logs.append((label,payload))
        def liquidate(self):self.exits+=1
        def manage_position(self,atr):self.managed+=1
        def on_v4_open(self):self.opened+=1
    surface=Surface()
    check(surface._entry_window(now))
    check(not surface._entry_window(surface.START))
    surface.ACTIVE_WINDOWS=()
    check(not surface._entry_window(now))
    surface=Surface();ResearchV4Base1h.before(surface)
    check(surface.vars["context"]["allowed"])
    surface=Surface();surface.vars["v4_last_exit_at"]=now
    ResearchV4Base1h.before(surface)
    check(not surface.vars["context"]["allowed"])
    check(any(b["primary"].get("same_decision_exit") for b in surface.vars["audit"].values()))
    surface=Surface();surface.vars["entry_day"]=now//DAY*DAY
    ResearchV4Base1h.before(surface)
    check(not surface.vars["context"]["allowed"])
    check(any(b["primary"].get("daily_limit") for b in surface.vars["audit"].values()))
    surface=Surface();surface.vars["entry_day"]=(now//DAY-1)*DAY
    ResearchV4Base1h.before(surface)
    check(surface.vars["context"]["allowed"])
    surface=Surface();surface.USE_OI=True
    ResearchV4Base1h.before(surface)
    check(not surface.vars["context"]["allowed"])
    surface=Surface();surface.is_open=True
    surface.request_exit("first");surface.request_exit("second")
    check(surface.exits == 1 and surface.vars["exit_reason"] == "first")
    surface.time+=BAR;surface.request_exit("next")
    check(surface.exits == 2)
    surface=Surface();surface.vars["context"]={"atr":None}
    ResearchV4Base1h.update_position(surface)
    check(surface.managed == 0)
    surface.time+=BAR;ResearchV4Base1h.update_position(surface)
    check(surface.managed == 1)
    surface.time=now+24*BAR;surface.is_open=True
    ResearchV4Base1h.update_position(surface)
    check(surface.vars["exit_reason"] == "maximum_hold")
    surface=Surface();surface.is_open=True;surface.time=now+24*BAR
    surface.FORCE_BOUNDARIES=(surface.time,)
    ResearchV4Base1h.update_position(surface)
    check(surface.vars["exit_reason"] == "calendar_boundary")
    for direction in (-1,1):
        surface=Surface()
        ResearchV4Base1h.before(surface)
        context=surface.vars["context"];plan=context["plan"]
        surface.vars["intent"]=dict(context=context,plan=plan)
        surface.is_long=direction==1;surface.is_open=True
        surface.position.entry_price=100.+direction*.05
        surface.position.qty=direction*plan["qty"]
        surface.TARGET_MODE="r_multiple"
        surface.vars["v4_exit_requested_at"]=now
        ResearchV4Base1h.on_open_position(surface,None)
        check(surface.stop_loss[1] == surface.position.entry_price-direction*4.)
        check(surface.take_profit[1] == surface.position.entry_price+direction*4.)
        check(surface.opened == 1 and surface.vars["entry_day"] == context["day"])
        check("v4_exit_requested_at" not in surface.vars)
    return dict(status="passed",assertions=checks)

```

## strategies/ResearchV4Base1h/oscillator_features.py
SHA256: 20aa757e423d6105c3276b92ad16ac154f51edae040243551de5662249521c72

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

## strategies/ResearchV4OscillatorP1h/__init__.py
SHA256: d7a7e7436a51ea0b308c168967fafbad13e9d304166d4954ab620a5aec4fb957

```python
from strategies.ResearchV4Base1h import ResearchV4Base1h
from strategies.ResearchV4Base1h.oscillator_features import features, rsi32


class ResearchV4OscillatorP1h(ResearchV4Base1h):
    LINE = "OSCILLATOR"
    USE_OI = False
    RSI_ENTRY_LEVEL = 10.
    STOP_MULTIPLIER = 2.
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 24
    TARGET_MODE = "none"

    def features(self, candles, now, atr):
        return features(candles, now, atr, self.RSI_ENTRY_LEVEL)

    def manage_position(self, atr):
        # Core already prioritizes calendar/hold and requires a post-fill close.
        # Exit needs only 32 valid bars, never the entry trend's 224-bar history.
        oscillator = rsi32(self.candles, int(self.time))
        if oscillator["valid"] and ((self.is_long and oscillator["value"] >= 50.) or
                                   (self.is_short and oscillator["value"] <= 50.)):
            self.request_exit("rsi_normalized")

```

## strategies/ResearchV4OscillatorOi1h/__init__.py
SHA256: 4e6c86d9386a2ecf655b61dfd3b1d37b7278c9bb7dac3e2a92108ea316e8535f

```python
from strategies.ResearchV4OscillatorP1h import ResearchV4OscillatorP1h


class ResearchV4OscillatorOi1h(ResearchV4OscillatorP1h):
    USE_OI = True

```

## strategies/ResearchV4OscillatorSmoke1h/__init__.py
SHA256: faa80b03c4e9f6a14c625e33329026d13749f80446940fb81454a9e87c32bba8

```python
from strategies.ResearchV4OscillatorP1h import ResearchV4OscillatorP1h
from strategies.ResearchV4Base1h.oscillator_features import self_checks
from strategies.ResearchV4Base1h.common_checks import self_checks as base_checks


class ResearchV4OscillatorSmoke1h(ResearchV4OscillatorP1h):
    FINISH = 1599523200000  # Seven-day technical window ending 2020-09-08 UTC.

    def before(self):
        if not self.vars.get("v4_smoke_checks_done"):
            sector = self_checks()
            common = base_checks()
            assert sector["status"] == common["status"] == "passed"
            self.vars["self_checks"] = sector
            self.vars["v4_base_checks"] = common
            self._log_json("V4_SELF_CHECKS", sector)
            self._log_json("V4_BASE_CHECKS", common)
            self.vars["v4_smoke_checks_done"] = True
        super().before()

```

## strategies/ResearchV4Base1h/shock_features.py
SHA256: 0ebf34769d0ad821e19773dfe5f6494398a0727ec5d1a93fc42c84472650a43b

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

## strategies/ResearchV4ShockPV1h/__init__.py
SHA256: 5694fb437896416ff34513c38a3c9844f0c26663263f7e30504ae7fadaa6e7b0

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

## strategies/ResearchV4ShockPVOi1h/__init__.py
SHA256: 5a3dec1ee3040ba1243018bc801c294c81115d3546a54d8e848254bed71f9e40

```python
from strategies.ResearchV4ShockPV1h import ResearchV4ShockPV1h


class ResearchV4ShockPVOi1h(ResearchV4ShockPV1h):
    USE_OI = True

```

## strategies/ResearchV4ShockSmoke1h/__init__.py
SHA256: b4109c1bc37fd67369e4d258e6dd6d2eec7140f74726325f796d5ae0c3cbea49

```python
from strategies.ResearchV4ShockPV1h import ResearchV4ShockPV1h
from strategies.ResearchV4Base1h.shock_features import self_checks
from strategies.ResearchV4Base1h.common_checks import self_checks as common_checks


class ResearchV4ShockSmoke1h(ResearchV4ShockPV1h):
    FINISH = 1599523200000

    def before(self):
        if "self_checks" not in self.vars:
            # Pure source checks precede motor context; this smoke adds no signal rule.
            self.vars["self_checks"] = self_checks()
            self.vars["base_checks"] = common_checks()
            self._log_json("V4_SELF_CHECKS", self.vars["self_checks"])
            self._log_json("V4_BASE_CHECKS", self.vars["base_checks"])
        super().before()

```

## strategies/ResearchV4Base1h/funding_features.py
SHA256: 894fa8b7d9b53d66b60f7fc48bbd34308bd740af1d41c56f518e267dda87b701

```python
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV4Base1h import BAR, closed_window


def _number(value):
    # Reject bool/string coercions and sanitize nonfinite data before JSON evidence.
    if isinstance(value, (bool, str)) or not isinstance(value, (int, float, np.integer, np.floating)):
        return None
    value = float(value)
    return value if math.isfinite(value) else None


def _timestamp(value):
    number = _number(value)
    return int(number) if number is not None and number >= 0 and number == int(number) else None


def canonical_window(history):
    """Bounded evidence contains only identity, publication and decimal rate."""
    rows = history if isinstance(history, (list, tuple)) else []
    result = []
    for row in rows[-32:]:
        row = row if isinstance(row, dict) else {}
        result.append([_timestamp(row.get("settled_at")),
                       _timestamp(row.get("available_at")), _number(row.get("rate_decimal"))])
    return result


def window_hash(window):
    return hashlib.sha256(json.dumps(window, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def reset_signal(previous, current, baseline, extreme_z=1., reset_z=.5):
    """Both events share the strictly preceding baseline; constant history has sigma zero."""
    if len(baseline) != 30 or not all(math.isfinite(x) for x in baseline):
        return dict(direction=0, reason="funding_baseline_invalid")
    try:
        mean = math.fsum(x / 30 for x in baseline)
        # Constant positive rates may have a tiny floating residual: detect equality directly.
        sigma = 0. if max(baseline) == min(baseline) else math.sqrt(math.fsum((x - mean) ** 2 / 30 for x in baseline))
    except (OverflowError, ValueError):
        return dict(direction=0, reason="funding_baseline_invalid")
    if not math.isfinite(sigma) or sigma <= 0:
        return dict(direction=0, reason="funding_sigma_zero", baseline=mean, sigma=sigma if math.isfinite(sigma) else None)
    zprev, znow = (previous - mean) / sigma, (current - mean) / sigma
    if not all(math.isfinite(x) for x in (zprev, znow)):
        return dict(direction=0, reason="funding_z_invalid", baseline=mean, sigma=sigma)
    direction = 1 if zprev >= extreme_z and 0 <= znow <= reset_z else -1 if zprev <= -extreme_z and -reset_z <= znow <= 0 else 0
    return dict(direction=direction, reason="funding_reset" if direction else "funding_no_reset",
                baseline=mean, sigma=sigma, zprev=zprev, znow=znow)


def ma24_state(candles, now):
    """A state exit needs only 24 closed prices, independent of entry warmup."""
    rows = closed_window(candles, now, 24)
    if rows is None:
        return None
    # Finite individual OHLC can still overflow an aggregate; never emit Infinity.
    with np.errstate(over="ignore", invalid="ignore"):
        close, average = float(rows[-1, 2]), float(np.mean(rows[:, 2]))
    if not all(math.isfinite(value) for value in (close, average)):
        return None
    return dict(close=close, sma24=average)


def features(candles, now, atr, history32, current_rate, current_timestamp,
             last_seen, extreme_z=1., reset_z=.5):
    """Pure event evaluation. next_seen consumes new events even when a gate rejects."""
    window = canonical_window(history32)
    event = _timestamp(current_timestamp)
    result = dict(valid=True, direction=0, reason="funding_repeated", details={},
                  next_seen=last_seen, event_new=False,
                  event=dict(settled_at=event, window=window, sha256=window_hash(window)))

    def reject(reason, valid=False):
        result.update(valid=valid, reason=reason)
        return result

    if event is None:
        return reject("funding_missing")
    if last_seen is None:
        result.update(next_seen=event, event_new=True)
        return reject("funding_initialization", True)
    if event < last_seen:
        return reject("funding_clock_regression")
    if event == last_seen:
        return result
    result.update(next_seen=event, event_new=True)
    params = [_number(extreme_z), _number(reset_z)]
    if None in params or not 0 < params[1] < params[0]:
        return reject("funding_params_invalid")
    if not 0 < now - event <= 2 * BAR:
        return reject("funding_event_age")
    if not isinstance(history32, (list, tuple)) or len(history32) != 32:
        return reject("funding_history_count")
    if any(t is None or a is None or rate is None for t, a, rate in window):
        return reject("funding_history_invalid")
    if any(a > now or a <= t for t, a, rate in window):
        return reject("funding_unpublished")
    if any(not 8 * BAR - 1000 <= right[0] - left[0] <= 8 * BAR + 1000
           for left, right in zip(window, window[1:])):
        return reject("funding_history_gap")
    if window[-1][0] != event or _number(current_rate) != window[-1][2]:
        return reject("funding_accessor_mismatch")
    # Thirty prior payments span about ten days; the final pair never enters the baseline.
    signal = reset_signal(window[-2][2], window[-1][2],
                          [row[2] for row in window[:30]], extreme_z, reset_z)
    direction = signal.pop("direction")
    reason = signal.pop("reason")
    result["details"] = signal
    result["event"].update(available_at=window[-1][1], rate_decimal=window[-1][2])
    if direction == 0:
        return reject(reason, reason == "funding_no_reset")
    # 72 current closes and the 72-window shifted24h require exactly96, not84.
    rows = closed_window(candles, now, 96)
    if rows is None:
        return reject("funding_price_window")
    if not isinstance(atr, dict) or _number(atr.get("value")) is None or atr["value"] <= 0:
        return reject("funding_atr_invalid")
    close = rows[:, 2]
    current = float(close[-1])
    # Aggregate overflow is invalid data, even when every original OHLC is finite.
    with np.errstate(over="ignore", invalid="ignore"):
        sma72, old72 = float(np.mean(close[-72:])), float(np.mean(close[-96:-24]))
        sma24 = float(np.mean(close[-24:]))
    old6 = float(close[-7])
    if not all(math.isfinite(value) for value in (current, sma72, old72, sma24, old6)):
        return reject("funding_price_arithmetic")
    result["details"].update(close=current, sma72=sma72, sma72_previous24=old72,
                             sma24=sma24, close_previous6=old6, funding_direction=direction)
    passed = (current > sma72 > old72 and current > sma24 and current > old6) if direction == 1 else (current < sma72 < old72 and current < sma24 and current < old6)
    result.update(direction=direction if passed else 0, reason="funding_reset" if passed else "funding_regime_reject")
    return result


def self_checks():
    """Deterministic synthetic cases exercise event time, symmetry and immutable inputs."""
    assertions = 0

    def check(condition):
        nonlocal assertions
        assert condition
        assertions += 1

    now = 2000 * BAR
    event = now - BAR
    history = [dict(settled_at=event - (31 - i) * 8 * BAR,
                    available_at=event - (31 - i) * 8 * BAR + 60000,
                    rate_decimal=(-.0001 if i % 2 == 0 else .0001)) for i in range(32)]
    history[-2]["rate_decimal"] = .0002
    history[-1]["rate_decimal"] = .000025
    prices = np.arange(100., 196.)
    candles = np.array([[now - (96 - i) * BAR, p, p, p + 1, p - 1, 1] for i, p in enumerate(prices)])
    atr = dict(value=2.)
    original = json.dumps(history, sort_keys=True)
    candle_copy = candles.copy()

    def call(h=None, c=None, t=now, rate=None, stamp=event, seen=event-8*BAR, risk=atr):
        h = history if h is None else h
        return features(candles if c is None else c, t, risk, h,
                        h[-1]["rate_decimal"] if rate is None else rate, stamp, seen)

    result = call()
    check(result["direction"] == 1 and result["valid"])
    check(result["next_seen"] == event and result["event_new"])
    check(result["details"]["baseline"] == 0.)
    check(abs(result["details"]["sigma"] - .0001) < 1e-15)
    check(json.dumps(history, sort_keys=True) == original)
    check(np.array_equal(candles, candle_copy))
    check(call(seen=None)["reason"] == "funding_initialization")
    check(call(seen=event)["event_new"] is False)
    check(call(seen=event+1)["reason"] == "funding_clock_regression")
    check(call(stamp=None)["reason"] == "funding_missing")
    check(call(t=event)["reason"] == "funding_event_age")
    check(call(t=event+2*BAR+1)["reason"] == "funding_event_age")
    check(call(h=history[:-1])["next_seen"] == event)
    check(call(h=history[:-1])["reason"] == "funding_history_count")
    check(call(rate=.0123)["reason"] == "funding_accessor_mismatch")
    for key, value, reason in [("available_at", now+1, "funding_unpublished"),
                               ("available_at", event, "funding_unpublished"),
                               ("rate_decimal", float("nan"), "funding_history_invalid"),
                               ("settled_at", history[-2]["settled_at"], "funding_history_gap")]:
        changed = [dict(r) for r in history]
        changed[-1][key] = value
        check(call(h=changed)["reason"] == reason)
    changed = [dict(r) for r in history]
    changed[1]["settled_at"] += 1001
    check(call(h=changed)["reason"] == "funding_history_gap")
    changed = [dict(r) for r in history]
    changed[-1]["settled_at"] += 4
    changed[-1]["available_at"] = event+60000
    check(call(h=changed, stamp=event+4)["direction"] == 1)
    flat = [dict(r, rate_decimal=.0001) for r in history]
    check(call(h=flat)["reason"] == "funding_sigma_zero")
    flat = [dict(r, rate_decimal=0.) for r in history]
    check(call(h=flat)["reason"] == "funding_sigma_zero")
    check(call(c=candles[-95:])["reason"] == "funding_price_window")
    check(call(risk=None)["reason"] == "funding_atr_invalid")
    future = np.vstack([candles, [now, 500, 500, 501, 499, 1]])
    check(call(c=future)["direction"] == 1)
    broken = candles.copy()
    broken[4, 0] += 1
    check(call(c=broken)["reason"] == "funding_price_window")
    broken = candles.copy()
    broken[-1, 2] = 80
    broken[-1, 4] = 79
    check(call(c=broken)["reason"] == "funding_regime_reject")
    for scale in (1., -1.):
        baseline = [scale*x for x in [-1., 1.]*15]
        signal = reset_signal(scale, scale*.5, baseline)
        check(signal["direction"] == int(scale))
        check(reset_signal(scale, 0., baseline)["direction"] == int(scale))
        check(reset_signal(scale, -scale*.01, baseline)["direction"] == 0)
        check(reset_signal(scale*.999, scale*.1, baseline)["direction"] == 0)
        check(reset_signal(scale, scale*.50001, baseline)["direction"] == 0)
        shifted = reset_signal(2.+scale, 2.+scale*.5, [x+2. for x in baseline])
        check(shifted["direction"] == int(scale))
    short_history = [dict(r, rate_decimal=-r["rate_decimal"]) for r in history]
    descending = candles.copy()
    descending[:, 1:5] = np.column_stack([400-prices, 400-prices, 401-prices, 399-prices])
    check(call(h=short_history, c=descending)["direction"] == -1)
    state = ma24_state(candles, now)
    check(state["close"] > state["sma24"])
    check(ma24_state(candles[-23:], now) is None)
    # Huge yet coherent finite OHLC must reject overflowing means without JSON NaN/Infinity.
    huge = candles.copy()
    huge[:, 1:5] = 1e308
    invalid = call(c=huge)
    check(invalid["valid"] is False and invalid["reason"] == "funding_price_arithmetic")
    check(invalid["next_seen"] == event)
    check(ma24_state(huge, now) is None)
    check(json.loads(json.dumps(invalid, allow_nan=False))["direction"] == 0)
    check(len(result["event"]["window"]) == 32)
    check(result["event"]["sha256"] == window_hash(canonical_window(history)))
    bad = canonical_window([dict(settled_at=event, available_at=now, rate_decimal=float("nan"))])
    check(bad[0][2] is None)
    for block in (result["event"]["window"][:16], result["event"]["window"][16:]):
        check(len(json.dumps(dict(time=now, sha256=result["event"]["sha256"], rows=block), allow_nan=False)) < 1800)
    return dict(status="passed", assertions=assertions)

```

## strategies/ResearchV4FundingFP1h/__init__.py
SHA256: 61b5db6848d086b629be0122b435da89cc76850284db74f5d03207a7c6270358

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

## strategies/ResearchV4FundingFPOi1h/__init__.py
SHA256: 25bf4805ceb6b1eddc6d7676fec704ea491b6d66b8ab48db53b0f7ee5409b027

```python
from strategies.ResearchV4FundingFP1h import ResearchV4FundingFP1h


class ResearchV4FundingFPOi1h(ResearchV4FundingFP1h):
    USE_OI = True

```

## strategies/ResearchV4FundingSmoke1h/__init__.py
SHA256: cdf8240af1ce8a94cb753221b9a041baf65aeebe97407cec9810f22a6b2f4f90

```python
from strategies.ResearchV4FundingFP1h import ResearchV4FundingFP1h
from strategies.ResearchV4Base1h.funding_features import self_checks
from strategies.ResearchV4Base1h.common_checks import self_checks as common_checks


class ResearchV4FundingSmoke1h(ResearchV4FundingFP1h):
    FINISH = 1599523200000

    def before(self):
        if not self.vars.get("funding_smoke_checks_done"):
            self.vars["funding_smoke_checks_done"] = True
            result = self_checks()
            common = common_checks()
            self.vars["self_checks"] = dict(funding=result, common=common)
            self._log_json("V4_SELF_CHECKS", result)
            self._log_json("V4_COMMON_CHECKS", common)
        super().before()

```
