# V6 source freeze before technical smoke and economics

## strategies/ResearchV6Base4h/__init__.py

SHA256: fdcd1eaffbcc7845dc5701bb04d8f2bda6317dbd2e780bfa737c8b6e770776e6

```python
import hashlib
import json
import math
from datetime import datetime, timezone

import numpy as np

from strategies.ResearchV2Core4h import (
    ResearchV2Core4h, ACCOUNTING_TOLERANCE,
)

# V6 4h decisions use explicit local clocks; only neutral V2 hooks are inherited.
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


def oi_context(history, now, lag_bars=0, rule="rising", decline_fraction=.02):
    assert rule in ("rising", "declining")
    assert math.isfinite(decline_fraction) and 0 < decline_fraction < 1
    target = now - lag_bars * BAR
    current = next((r for r in reversed(history) if r["time"] == target), None)
    reference = next((r for r in reversed(history) if r["time"] == target - DAY), None)
    result = dict(quality="initialization", passed=False, current=current, reference=reference,
                  rule=rule, decline_fraction=decline_fraction if rule == "declining" else None, ratio=None)
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
        ratio = current["value"] / reference["value"]
        result["ratio"] = float(ratio) if math.isfinite(ratio) else None
        if rule == "declining":
            # A zero/invalid observation never masquerades as a complete position reduction.
            if not math.isfinite(ratio):
                result["quality"] = "arithmetic_invalid"
            else:
                result["passed"] = bool(ratio <= 1. - decline_fraction)
        else:
            result["passed"] = bool(current["value"] > reference["value"])
    return result


def v6_entry_plan(price, capital, fee, direction, distance):
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


class ResearchV6Base4h(ResearchV2Core4h):
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
    OI_RULE = "rising"
    OI_DECLINE_FRACTION = .02
    ACTIVE_WINDOWS = None
    FORCE_BOUNDARIES = ()

    def features(self, candles, now, atr):
        raise NotImplementedError

    def on_v6_open(self):
        pass

    def manage_position(self, atr):
        pass

    def _log_json(self, label, payload):
        # Preserve inherited accounting labels while identifying this new hourly cycle.
        if label.startswith("V2_"):
            label = "V6_" + label[3:]
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
        oi = oi_context(history, now, self.OI_LAG_BARS, self.OI_RULE, self.OI_DECLINE_FRACTION)
        funding_rows = self.get_funding_history(count=1)
        assert all(r["available_at"] <= now for r in funding_rows)
        funding = funding_rows[-1] if funding_rows else None
        day = now // DAY * DAY
        opportunity = bool(direction and self.is_close and not self.entry_orders and
                           self.vars.get("entry_day") != day and self.vars.get("v6_last_exit_at") != now and
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
            flags.append("oi_nonrising" if self.OI_RULE == "rising" else "oi_decline_below_threshold")
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
        elif self.vars.get("v6_last_exit_at") == now:
            reason = "same_decision_exit"
        elif not self.is_close or self.entry_orders:
            reason = "in_position_or_pending"
        elif self.vars.get("entry_day") == day:
            reason = "daily_limit"
        elif self.USE_OI and oi["quality"] != "valid":
            reason = "oi_" + oi["quality"]
        elif self.USE_OI and not oi["passed"]:
            reason = "oi_nonrising" if self.OI_RULE == "rising" else "oi_decline_below_threshold"
        else:
            distance = self.STOP_MULTIPLIER * atr["value"]
            plan = v6_entry_plan(self.price, self.available_margin, self.fee_rate, direction, distance)
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
        if not self.is_open or self.vars.get("v6_exit_requested_at") == int(self.time):
            return
        self.vars["v6_exit_requested_at"] = int(self.time)
        self.vars["exit_reason"] = reason
        self._log_json("V6_EXIT_REQUEST", dict(time=int(self.time), reason=reason))
        self.liquidate()

    def on_open_position(self, order):
        intent = self.vars["intent"]
        context, plan = intent["context"], intent["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = self.position.entry_price, abs(self.position.qty)
        distance = plan["distance"]
        stop = entry - direction * distance
        target = self._target(entry, direction, distance, context["features"])
        self.vars.pop("v6_exit_requested_at", None)
        self.vars["entry_day"] = context["day"]
        for side in ("all", "long" if direction == 1 else "short"):
            self._bucket(context["month"], side)["entries"] += 1
        atr = context["atr"]
        digest = hashlib.sha256(json.dumps(atr["bars"], separators=(",", ":"), allow_nan=False).encode()).hexdigest()
        self._log_json("V6_FEATURES", dict(time=int(self.time), line=self.LINE,
                                        **context["features"]))
        self._log_json("V6_ENTRY", dict(time=int(self.time), direction=direction, decision=plan["price"],
            fill=entry, capital=plan["capital"], qty=qty, distance_pre=distance, distance_fill=distance,
            planned_stop_loss=plan["planned_stop_loss"], risk_budget=plan["risk_budget"],
            stop=stop, target=target, atr=dict(value=atr["value"], first=atr["first"], last=atr["last"],
                                             bars=15, offset_bars=self.ATR_OFFSET_BARS, sha256=digest), oi=context["oi"], funding=context["funding"]))
        self.vars["v6_trade"] = dict(entry_at=int(self.position.opened_at), entry_atr=atr["value"],
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
        self.on_v6_open()

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
        self.vars["v6_last_exit_at"] = int(closed_trade.closed_at)
        super().on_close_position(order, closed_trade)

    def before_terminate(self):
        if self.is_open:
            self.vars["exit_reason"] = "fold_end"
            self._log_json("V6_EXIT_REQUEST", dict(time=int(self.time), reason="fold_end"))
        for key, value in sorted(self.vars.get("audit", {}).items()):
            assert value["bars"] == sum(value["primary"].values())
            assert value["entries"] == value["primary"].get("allowed", 0)
            assert value["bars"] == sum(value.get("feature_reasons", {}).values())
            self._log_json("V6_AUDIT", dict(key=key, **value))
        self._log_json("V6_PROVENANCE", dict(line=self.LINE, use_oi=self.USE_OI,
            oi_lag_bars=self.OI_LAG_BARS, oi_rule=self.OI_RULE,
            oi_decline_fraction=self.OI_DECLINE_FRACTION, stop_multiplier=self.STOP_MULTIPLIER,
            bar_ms=BAR, oi_reference_bars=OI_REFERENCE_BARS,
            atr_offset_bars=self.ATR_OFFSET_BARS, target_mode=self.TARGET_MODE,
            reward_multiple=self.REWARD_MULTIPLE, max_hold_bars=self.MAX_HOLD_BARS,
            start=self.START, finish=self.FINISH, active_windows=self.ACTIVE_WINDOWS,
            force_boundaries=self.FORCE_BOUNDARIES, final_exit_may_follow=True,
            self_checks=self.vars.get("self_checks")))

```

## strategies/ResearchV6Base4h/common_checks.py

SHA256: eef5e609c1fad91fd995a51cf26bfe67d5f9f143f0eac87e7740055b697c8ff6

```python
import json
import math
from types import SimpleNamespace
import numpy as np
from strategies.ResearchV6Base4h import (
    ResearchV6Base4h, BAR, DAY, closed_window, atr_window, oi_context, v6_entry_plan,
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
    reference_bars=DAY//BAR
    lag_bars=14400000//BAR
    history=[dict(time=now+i*BAR,value=100.+i,label=now+i*BAR-600000,
                  available_at=now+i*BAR-240000,status="valid")
             for i in range(reference_bars+lag_bars+3)]
    check(oi_context(history[:reference_bars],now+(reference_bars-1)*BAR)["quality"] == "initialization")
    check(oi_context(history[:reference_bars+1],now+reference_bars*BAR)["passed"])
    check(oi_context(history[:reference_bars+lag_bars],now+(reference_bars+lag_bars-1)*BAR,lag_bars)["quality"] == "initialization")
    check(oi_context(history[:reference_bars+lag_bars+1],now+(reference_bars+lag_bars)*BAR,lag_bars)["passed"])
    bad=[dict(r) for r in history];bad[0]["value"]=0
    check(oi_context(bad,now+reference_bars*BAR)["quality"] == "reference_invalid")
    bad=[dict(r) for r in history];bad[reference_bars]["value"]=100.
    check(not oi_context(bad,now+reference_bars*BAR)["passed"])
    bad=[dict(r) for r in history];bad[reference_bars]["available_at"]=bad[reference_bars]["time"]+1
    check(oi_context(bad,now+reference_bars*BAR)["quality"] == "invalid")
    decline=[dict(r) for r in history]
    decline[reference_bars]["value"]=98.
    check(oi_context(decline,now+reference_bars*BAR,rule="declining")["passed"])
    check(not oi_context(decline,now+reference_bars*BAR)["passed"])
    decline[reference_bars]["value"]=98.+1e-8
    check(not oi_context(decline,now+reference_bars*BAR,rule="declining")["passed"])
    for fraction in (.018,.022):
        decline[reference_bars]["value"]=100*(1-fraction)-1e-8
        check(oi_context(decline,now+reference_bars*BAR,rule="declining",decline_fraction=fraction)["passed"])
    decline[reference_bars]["value"]=0.
    check(oi_context(decline,now+reference_bars*BAR,rule="declining")["quality"] == "invalid")
    for direction in (-1,1):
        plan=v6_entry_plan(100.,10000.,.00045,direction,4.)
        check(plan["reason"] == "allowed")
        check(plan["qty"]*plan["unit_loss"] <= 200.+1e-8)
        check(plan["qty"]*100 <= 10000.)
        check(plan["qty"] == math.floor(plan["qty"]*1e8+.01)/1e8)
    check(v6_entry_plan(100.,10000.,-.1,1,4.)["reason"] == "distance_invalid")
    check(v6_entry_plan(100.,10000.,.00045,1,101.)["reason"] == "distance_invalid")
    class Surface:
        _entry_window=ResearchV6Base4h._entry_window
        _target=ResearchV6Base4h._target
        _target_valid=staticmethod(ResearchV6Base4h._target_valid)
        request_exit=ResearchV6Base4h.request_exit
        def __init__(self):
            self.vars={};self.time=now;self.START=now-50*BAR;self.FINISH=now+100*BAR
            self.ACTIVE_WINDOWS=None;self.FORCE_BOUNDARIES=()
            self.TARGET_MODE="none";self.REWARD_MULTIPLE=1.;self.MAX_HOLD_BARS=24
            self.STOP_MULTIPLIER=2.;self.ATR_OFFSET_BARS=0;self.OI_LAG_BARS=0
            self.USE_OI=False;self.LINE="test";self.candles=candles
            self.OI_RULE="rising";self.OI_DECLINE_FRACTION=.02
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
        def on_v6_open(self):self.opened+=1
    surface=Surface()
    check(surface._entry_window(now))
    check(not surface._entry_window(surface.START))
    surface.ACTIVE_WINDOWS=()
    check(not surface._entry_window(now))
    surface=Surface();ResearchV6Base4h.before(surface)
    check(surface.vars["context"]["allowed"])
    surface=Surface();surface.vars["v6_last_exit_at"]=now
    ResearchV6Base4h.before(surface)
    check(not surface.vars["context"]["allowed"])
    check(any(b["primary"].get("same_decision_exit") for b in surface.vars["audit"].values()))
    surface=Surface();surface.vars["entry_day"]=now//DAY*DAY
    ResearchV6Base4h.before(surface)
    check(not surface.vars["context"]["allowed"])
    check(any(b["primary"].get("daily_limit") for b in surface.vars["audit"].values()))
    surface=Surface();surface.vars["entry_day"]=(now//DAY-1)*DAY
    ResearchV6Base4h.before(surface)
    check(surface.vars["context"]["allowed"])
    surface=Surface();surface.USE_OI=True
    ResearchV6Base4h.before(surface)
    check(not surface.vars["context"]["allowed"])
    surface=Surface();surface.is_open=True
    surface.request_exit("first");surface.request_exit("second")
    check(surface.exits == 1 and surface.vars["exit_reason"] == "first")
    surface.time+=BAR;surface.request_exit("next")
    check(surface.exits == 2)
    surface=Surface();surface.vars["context"]={"atr":None}
    ResearchV6Base4h.update_position(surface)
    check(surface.managed == 0)
    surface.time+=BAR;ResearchV6Base4h.update_position(surface)
    check(surface.managed == 1)
    surface.time=now+24*BAR;surface.is_open=True
    ResearchV6Base4h.update_position(surface)
    check(surface.vars["exit_reason"] == "maximum_hold")
    surface=Surface();surface.is_open=True;surface.time=now+24*BAR
    surface.FORCE_BOUNDARIES=(surface.time,)
    ResearchV6Base4h.update_position(surface)
    check(surface.vars["exit_reason"] == "calendar_boundary")
    for direction in (-1,1):
        surface=Surface()
        ResearchV6Base4h.before(surface)
        context=surface.vars["context"];plan=context["plan"]
        surface.vars["intent"]=dict(context=context,plan=plan)
        surface.is_long=direction==1;surface.is_open=True
        surface.position.entry_price=100.+direction*.05
        surface.position.qty=direction*plan["qty"]
        surface.TARGET_MODE="r_multiple"
        surface.vars["v6_exit_requested_at"]=now
        ResearchV6Base4h.on_open_position(surface,None)
        check(surface.stop_loss[1] == surface.position.entry_price-direction*4.)
        check(surface.take_profit[1] == surface.position.entry_price+direction*4.)
        check(surface.opened == 1 and surface.vars["entry_day"] == context["day"])
        check("v6_exit_requested_at" not in surface.vars)
    return dict(status="passed",assertions=checks)

```

## strategies/ResearchV6Base4h/efficiency_features.py

SHA256: ecfcc5fe4b77a2faee9edcdaea1bd391e33ec7fe73112e48718a2a8b90790bcf

```python
"""Finite directional path efficiency; pure algebra, with no engine state or IO."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV6Base4h import BAR, closed_window


def _digest(rows):
    return hashlib.sha256(json.dumps(rows[:, :5].tolist(),
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def efficiency24(candles, now):
    """Twenty-four deltas use exactly25closed prices; a flat path is neutral."""
    rows = closed_window(candles, now, 25)
    if rows is None:
        return dict(valid=False, value=None, reason="efficiency_window_invalid")
    closes = [float(value) for value in rows[:, 2]]
    deltas = [right - left for left, right in zip(closes, closes[1:])]
    displacement = closes[-1] - closes[0]
    if not math.isfinite(displacement) or not all(math.isfinite(x) for x in deltas):
        return dict(valid=False, value=None, reason="efficiency_arithmetic_invalid")
    scale = max(abs(x) for x in deltas)
    # Common normalization preserves the ratio while avoiding an overflowing raw sum.
    if scale == 0:
        normalized_path = normalized_displacement = value = 0.
    else:
        normalized_path = math.fsum(abs(x) / scale for x in deltas)
        normalized_displacement = displacement / scale
        if (not math.isfinite(normalized_path) or normalized_path <= 0 or
                not math.isfinite(normalized_displacement)):
            return dict(valid=False, value=None, reason="efficiency_arithmetic_invalid")
        value = normalized_displacement / normalized_path
    if not math.isfinite(value):
        return dict(valid=False, value=None, reason="efficiency_arithmetic_invalid")
    return dict(valid=True, value=float(value),
        reason="efficiency_flat" if scale == 0 else "efficiency_valid",
        displacement=float(displacement), step_scale=float(scale),
        normalized_displacement=float(normalized_displacement),
        normalized_path=float(normalized_path), first=int(rows[0, 0]),
        last=int(rows[-1, 0]), bars=25, sha256=_digest(rows))


def _cross_direction(current, previous, threshold):
    if previous <= threshold and current > threshold:
        return 1
    if previous >= -threshold and current < -threshold:
        return -1
    return 0


def features(candles, now, atr, threshold=.35):
    if (isinstance(threshold, (bool, str)) or
            not isinstance(threshold, (int, float, np.integer, np.floating)) or
            not math.isfinite(threshold) or not 0 < threshold < 1):
        return dict(valid=False, direction=0, reason="efficiency_threshold_invalid", details={})
    # A fresh crossing needs two independent25-close windows: their union is26.
    rows = closed_window(candles, now, 26)
    if rows is None:
        return dict(valid=False, direction=0, reason="efficiency_window_invalid", details={})
    try:
        atr_valid = (isinstance(atr, dict) and math.isfinite(atr["value"]) and atr["value"] > 0)
    except (KeyError, TypeError, ValueError):
        atr_valid = False
    if not atr_valid:
        return dict(valid=False, direction=0, reason="efficiency_atr_invalid", details={})
    current = efficiency24(candles, now)
    previous = efficiency24(candles, now - BAR)
    if not current["valid"] or not previous["valid"]:
        return dict(valid=False, direction=0, reason="efficiency_arithmetic_invalid", details={})
    direction = _cross_direction(current["value"], previous["value"], float(threshold))
    reason = "efficiency_setup" if direction else "efficiency_no_cross"
    details = dict(threshold=float(threshold), current=current, previous=previous,
        first=int(rows[0, 0]), last=int(rows[-1, 0]), bars=26, sha256=_digest(rows))
    return dict(valid=True, direction=int(direction), reason=reason, details=details)


def self_checks():
    """Independent finite-path oracles, boundaries and causal mutation checks."""
    count = 0

    def check(condition):
        nonlocal count
        assert bool(condition)
        count += 1

    def candles(closes, first=0):
        closes = np.asarray(closes, dtype=float)
        return np.column_stack((np.arange(len(closes))*BAR + first,
            closes, closes, closes*1.001, closes*.999, np.ones(len(closes))))

    def oracle(values):
        # Raw unnormalized arithmetic is independent of the scaled implementation.
        changes = [float(right - left) for left, right in zip(values, values[1:])]
        total = math.fsum(abs(x) for x in changes)
        return 0. if total == 0 else (float(values[-1]) - float(values[0])) / total

    closes = 100. + np.cumsum([0.] + [1., -1.]*12 + [14.])
    long = candles(closes)
    now = 26*BAR
    atr = dict(value=2.)
    short = long.copy()
    short[:, 1] = 400. - long[:, 1]
    short[:, 2] = 400. - long[:, 2]
    short[:, 3] = 400. - long[:, 4]
    short[:, 4] = 400. - long[:, 3]
    for case, expected in ((long, 1), (short, -1)):
        result = features(case, now, atr)
        check(result["valid"] and result["direction"] == expected)
        check(result["reason"] == "efficiency_setup")
        check(result["details"]["bars"] == 26)
        check(result["details"]["current"]["bars"] == 25)
        check(result["details"]["previous"]["bars"] == 25)
        check(len("V6_FEATURES " + json.dumps(dict(time=now, line="EFFICIENCY", **result),
              separators=(",", ":"), allow_nan=False)) <= 1900)
        for offset in (0, 1):
            state = efficiency24(case, now-offset*BAR)
            values = case[-25-offset:len(case)-offset if offset else None, 2]
            check(abs(state["value"] - oracle(values)) < 1e-12)
            check(state["last"]+BAR == now-offset*BAR)
            check(state["first"] == now-(25+offset)*BAR)
            mutated = case.copy()
            mutated[:len(case)-25-offset, 1:5] *= 1.1
            check(efficiency24(mutated, now-offset*BAR) == state)
        check(efficiency24(case[:-1], now-BAR) == efficiency24(case, now-BAR))
        check(features(case, now, atr, .315)["direction"] == expected)
        check(features(case, now, atr, .385)["direction"] == 0)
        check(features(case[-25:], now, atr)["valid"] is False)
        check(efficiency24(case[-25:], now)["valid"])
        future = candles([500., 600.], first=now)
        appended = np.vstack((case, future))
        check(features(appended, now, atr) == result)
        appended[-2:, 1:5] = float("nan")
        check(features(appended, now, atr) == result)
        older = candles(np.arange(40)+30., first=-40*BAR)
        extended = np.vstack((older, case))
        check(features(extended, now, atr) == result)
        extended[:40, 1:5] *= 2.
        check(features(extended, now, atr) == result)
        scaled = case.copy()
        scaled[:, 1:5] *= 2.
        check(abs(efficiency24(scaled, now)["value"] - result["details"]["current"]["value"]) < 1e-12)
        translated = case.copy()
        translated[:, 1:5] += 50.
        check(abs(efficiency24(translated, now)["value"] - result["details"]["current"]["value"]) < 1e-12)
        check(features(translated, now, atr)["direction"] == expected)
    check(abs(efficiency24(long, now)["value"] - 13./37.) < 1e-12)
    flat = candles([100.]*26)
    check(efficiency24(flat, now)["value"] == 0.)
    check(efficiency24(flat, now)["reason"] == "efficiency_flat")
    check(features(flat, now, atr)["valid"])
    check(features(flat, now, atr)["direction"] == 0)
    for values, expected in ((np.arange(26)+100., 1.), (200.-np.arange(26), -1.)):
        case = candles(values)
        check(efficiency24(case, now)["value"] == expected)
        check(features(case, now, atr)["direction"] == 0)
    zigzag = candles([100.] + [110., 100.]*11 + [110., 124.])
    straight = candles(np.arange(25)+100.)
    check(zigzag.shape[0] == 25)
    check(efficiency24(zigzag, 25*BAR)["displacement"] == efficiency24(straight, 25*BAR)["displacement"])
    check(efficiency24(zigzag, 25*BAR)["value"] < efficiency24(straight, 25*BAR)["value"])
    for h in (.315, .35, .385):
        check(_cross_direction(h+.01, h, h) == 1)
        check(_cross_direction(h, h-.01, h) == 0)
        check(_cross_direction(h+.01, h+.01, h) == 0)
        check(_cross_direction(-h-.01, -h, h) == -1)
        check(_cross_direction(-h, -h+.01, h) == 0)
        check(_cross_direction(-h-.01, -h-.01, h) == 0)
    for threshold in (0., 1., -.35, float("nan"), float("inf"), None, True, "0.35"):
        check(features(long, now, atr, threshold)["valid"] is False)
    for risk in (None, {}, dict(value=0.), dict(value=float("nan")), dict(value=float("inf"))):
        check(features(long, now, risk)["valid"] is False)
    for column, value in ((2, float("nan")), (1, 0.), (3, 1.), (4, 1000.), (0, now-2*BAR)):
        broken = long.copy()
        broken[-1, column] = value
        check(features(broken, now, atr)["valid"] is False)
        check(efficiency24(broken, now)["valid"] is False)
    check(features(long[:-1], now, atr)["valid"] is False)
    check(features(long, now+1, atr)["valid"] is False)
    check(efficiency24(long[-24:], now)["valid"] is False)
    # The raw path sum would overflow; scaling preserves a finite neutral result.
    large = candles([1e307 if i%2 == 0 else 9e307 for i in range(25)])
    large_state = efficiency24(large, 25*BAR)
    check(large_state["valid"] and large_state["value"] == 0.)
    check(large_state["normalized_path"] == 24.)
    check(len(json.dumps(large_state, allow_nan=False)) < 1000)
    original = long.copy()
    features(long, now, atr)
    check(np.array_equal(original, long))
    return dict(status="passed", assertions=count)

```

## strategies/ResearchV6EfficiencyP4h/__init__.py

SHA256: 315e3a0d3edf8f6e0f7ef3665556000e98159c7286706695c3d6892c8720a3a3

```python
from strategies.ResearchV6Base4h import ResearchV6Base4h
from strategies.ResearchV6Base4h.efficiency_features import features, efficiency24


class ResearchV6EfficiencyP4h(ResearchV6Base4h):
    LINE = "EFFICIENCY"
    USE_OI = False
    EFFICIENCY_THRESHOLD = .35
    STOP_MULTIPLIER = 2.5
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 60
    TARGET_MODE = "none"

    def features(self, candles, now, atr):
        return features(candles, now, atr, self.EFFICIENCY_THRESHOLD)

    def manage_position(self, atr):
        # Entry uses26prices; neutral-state exit needs only its own25valid closes.
        state = efficiency24(self.candles, int(self.time))
        if state["valid"] and ((self.is_long and state["value"] <= 0.) or
                               (self.is_short and state["value"] >= 0.)):
            self._log_json("V6_EFFICIENCY_EXIT_STATE", dict(time=int(self.time),
                opened_at=int(self.position.opened_at),
                direction=1 if self.is_long else -1, **state))
            self.request_exit("efficiency_neutral")

```

## strategies/ResearchV6EfficiencyOi4h/__init__.py

SHA256: e7ac140fe486446cc07bdf7029f1bae3404ae8030304542f48e17980eb4e012f

```python
from strategies.ResearchV6EfficiencyP4h import ResearchV6EfficiencyP4h


class ResearchV6EfficiencyOi4h(ResearchV6EfficiencyP4h):
    USE_OI = True

```

## strategies/ResearchV6EfficiencySmoke4h/__init__.py

SHA256: 7b2c28b0de8d3f1e5a81550f3dcec45e9a58bdfee7407f77cf159294f4e1347a

```python
from strategies.ResearchV6EfficiencyP4h import ResearchV6EfficiencyP4h
from strategies.ResearchV6Base4h.efficiency_features import self_checks
from strategies.ResearchV6Base4h.common_checks import self_checks as common_checks


class ResearchV6EfficiencySmoke4h(ResearchV6EfficiencyP4h):
    FINISH = 1599523200000  # Seven-day technical window ending2020-09-08UTC.

    def before(self):
        if not self.vars.get("efficiency_smoke_checks_done"):
            sector = self_checks()
            common = common_checks()
            assert sector["status"] == common["status"] == "passed"
            self.vars["self_checks"] = dict(efficiency=sector, common=common)
            self._log_json("V6_SELF_CHECKS", sector)
            self._log_json("V6_COMMON_CHECKS", common)
            self.vars["efficiency_smoke_checks_done"] = True
        super().before()

```

## strategies/ResearchV6Base4h/deleverage_features.py

SHA256: c26a24ae275ad2c314f0177ae00cf25e6d95695294f0e5960cb5ac30d8fe011c

```python
"""Causal 24h price displacement and a closed-bar correction; OI belongs to the core."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV6Base4h import BAR, atr_window, closed_window


def _direction(displacement, correction, threshold):
    # Inclusive displacement, strict correction: a flat last bar is never a turn.
    if displacement <= -threshold and correction > 0:
        return 1
    if displacement >= threshold and correction < 0:
        return -1
    return 0


def features(candles, now, atr, displacement_multiplier=2.):
    """Finite fifteen-OHLC context; no state, OI access, fill assumptions or IO."""
    invalid = dict(valid=False, direction=0, reason="deleverage_data_invalid", details={})
    rows = closed_window(candles, now, 15)
    if rows is None:
        return invalid
    if (isinstance(displacement_multiplier, bool) or
            not isinstance(displacement_multiplier, (int, float)) or
            not math.isfinite(displacement_multiplier) or displacement_multiplier <= 0):
        return dict(valid=False, direction=0, reason="deleverage_multiplier_invalid", details={})
    try:
        # Guard the common-core interface against a prior-bar ATR or another clock.
        if (atr is None or atr["offset_bars"] != 0 or
                atr["first"] != now - 15 * BAR or atr["last"] != now - BAR or
                not math.isfinite(atr["value"]) or atr["value"] <= 0):
            return dict(valid=False, direction=0, reason="deleverage_atr_invalid", details={})
        average_range = float(atr["value"])
    except (KeyError, TypeError, ValueError):
        return dict(valid=False, direction=0, reason="deleverage_atr_invalid", details={})
    close, prior, day_ago = (float(rows[index, 2]) for index in (-1, -2, -7))
    displacement, correction = close - day_ago, close - prior
    threshold = float(displacement_multiplier * average_range)
    if not all(math.isfinite(value) for value in (displacement, correction, threshold)) or threshold <= 0:
        return dict(valid=False, direction=0, reason="deleverage_arithmetic_invalid", details={})
    direction = _direction(displacement, correction, threshold)
    reason = ("deleverage_setup" if direction else
              "deleverage_displacement_below" if abs(displacement) < threshold else
              "deleverage_correction_reject")
    digest = hashlib.sha256(json.dumps(rows[:, :5].tolist(),
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    details = dict(close=close, previous_close=prior, close_24h_ago=day_ago,
        displacement_24h=displacement, correction_4h=correction,
        atr=average_range, displacement_multiplier=float(displacement_multiplier),
        displacement_threshold=threshold, first=int(rows[0, 0]),
        last=int(rows[-1, 0]), bars=15, reference_bars=6, sha256=digest)
    return dict(valid=True, direction=direction, reason=reason, details=details)


def self_checks():
    """Synthetic finite-window and boundary checks; no broker/provider emulation."""
    assertions = 0

    def check(condition):
        nonlocal assertions
        assert bool(condition)
        assertions += 1

    def candles(values, first=0):
        values = np.asarray(values, dtype=float)
        return np.column_stack((first + np.arange(len(values)) * BAR,
            values, values, values + .5, values - .5, np.ones(len(values))))

    now = 15 * BAR
    long = candles([104.] * 8 + [104., 102., 100., 98., 96., 95., 96.])
    short = long.copy()
    short[:, 1] = 200. - long[:, 1]
    short[:, 2] = 200. - long[:, 2]
    short[:, 3] = 200. - long[:, 4]
    short[:, 4] = 200. - long[:, 3]
    for source, expected in ((long, 1), (short, -1)):
        original = source.copy()
        atr = atr_window(source, now)
        result = features(source, now, atr)
        check(result["valid"] and result["direction"] == expected)
        check(result["reason"] == "deleverage_setup")
        check(result["details"]["reference_bars"] == 6)
        check(result["details"]["close_24h_ago"] == source[-7, 2])
        check(result["details"]["previous_close"] == source[-2, 2])
        check(result["details"]["first"] == 0 and result["details"]["last"] == 14 * BAR)
        check(len(json.dumps(result, allow_nan=False)) < 1000)
        for multiplier in (1.8, 2., 2.2):
            check(features(source, now, atr, multiplier)["direction"] == expected)
        # A different older prefix cannot alter either the feature or ATR context.
        prefix = candles([80., 81., 82.], first=-3 * BAR)
        extended = np.vstack([prefix, source])
        check(features(extended, now, atr_window(extended, now)) == result)
        extended[:3, 1:5] *= 1.1
        check(features(extended, now, atr_window(extended, now)) == result)
        future = candles([120., 121.], first=now)
        appended = np.vstack([source, future])
        check(features(appended, now, atr_window(appended, now)) == result)
        appended[-2:, 1:5] *= 2.
        check(features(appended, now, atr_window(appended, now)) == result)
        check(np.array_equal(original, source))
        check(not features(source[-14:], now, atr)["valid"])
        check(not features(source, now + 1, atr)["valid"])
        check(not features(source[:-1], now, atr)["valid"])
    # Exact scalar boundaries isolate inequalities from fixture-dependent ATR values.
    check(_direction(-4., 1., 4.) == 1)
    check(_direction(4., -1., 4.) == -1)
    check(_direction(-4. + 1e-8, 1., 4.) == 0)
    check(_direction(4. - 1e-8, -1., 4.) == 0)
    for correction in (0., -1.):
        check(_direction(-4., correction, 4.) == 0)
    for correction in (0., 1.):
        check(_direction(4., correction, 4.) == 0)
    check(_direction(0., 1., 4.) == 0)
    flat = candles([100.] * 15)
    flat_result = features(flat, now, atr_window(flat, now))
    check(flat_result["valid"] and flat_result["direction"] == 0)
    check(flat_result["reason"] == "deleverage_displacement_below")
    no_correction = long.copy()
    no_correction[-1, 1:5] = (94., 94., 94.5, 93.5)
    check(features(no_correction, now, atr_window(no_correction, now))["reason"] == "deleverage_correction_reject")
    good_atr = atr_window(long, now)
    for multiplier in (0., -1., float("nan"), float("inf"), None, True):
        check(not features(long, now, good_atr, multiplier)["valid"])
    for bad_atr in (None, {}, dict(good_atr, value=0.),
                    dict(good_atr, value=float("nan")), dict(good_atr, offset_bars=1),
                    dict(good_atr, first=-BAR), dict(good_atr, last=now)):
        check(features(long, now, bad_atr)["reason"] == "deleverage_atr_invalid")
    for column, value in ((2, float("nan")), (1, 0.), (3, 1.), (4, 1000.),
                          (0, now - 2 * BAR)):
        broken = long.copy()
        broken[-1, column] = value
        check(not features(broken, now, good_atr)["valid"])
    broken = long.copy()
    broken[-8, 0] -= BAR
    check(not features(broken, now, good_atr)["valid"])
    # A finite multiplier times a finite ATR can overflow: reject JSON-incompatible evidence.
    huge_atr = dict(good_atr, value=1e308)
    overflow = features(long, now, huge_atr, 2.)
    check(not overflow["valid"] and overflow["reason"] == "deleverage_arithmetic_invalid")
    check(len(json.dumps(overflow, allow_nan=False)) < 1000)
    # No OI appears in this pure price helper; the core separately checks declining ratios.
    check("oi" not in features(long, now, good_atr)["details"])
    return dict(status="passed", assertions=assertions)

```

## strategies/ResearchV6DeleverageP4h/__init__.py

SHA256: f6073c531e4ad42488d0c7335a3b02af9a91aa8e1f4bb983222d0a70eaeae8d1

```python
from strategies.ResearchV6Base4h import ResearchV6Base4h
from strategies.ResearchV6Base4h.deleverage_features import features as deleverage_features


class ResearchV6DeleverageP4h(ResearchV6Base4h):
    LINE = "DELEVERAGING"
    USE_OI = False
    OI_RULE = "declining"
    OI_DECLINE_FRACTION = .02
    DISPLACEMENT_MULTIPLIER = 2.
    STOP_MULTIPLIER = 2.
    REWARD_MULTIPLE = 2.
    TARGET_MODE = "r_multiple"
    MAX_HOLD_BARS = 12
    ATR_OFFSET_BARS = 0

    def features(self, candles, now, atr):
        return deleverage_features(candles, now, atr, self.DISPLACEMENT_MULTIPLIER)

```

## strategies/ResearchV6DeleverageOi4h/__init__.py

SHA256: bac06e94c6ebfe500d2c990cb41e582fd1792e330bf89964fb72062d903e7d26

```python
from strategies.ResearchV6DeleverageP4h import ResearchV6DeleverageP4h


class ResearchV6DeleverageOi4h(ResearchV6DeleverageP4h):
    USE_OI = True

```

## strategies/ResearchV6DeleverageSmoke4h/__init__.py

SHA256: 9a77ecb9fce9687fc3d2b8cda179ba192d54805750af8b703f3b30d84f613d2e

```python
from strategies.ResearchV6DeleverageP4h import ResearchV6DeleverageP4h
from strategies.ResearchV6Base4h.deleverage_features import self_checks
from strategies.ResearchV6Base4h.common_checks import self_checks as common_checks


class ResearchV6DeleverageSmoke4h(ResearchV6DeleverageP4h):
    FINISH = 1599523200000  # Seven-day technical window ending 2020-09-08 UTC.

    def before(self):
        if not self.vars.get("deleverage_smoke_checks_done"):
            sector = self_checks()
            common = common_checks()
            assert sector["status"] == common["status"] == "passed"
            self.vars["self_checks"] = dict(sector=sector, common=common)
            self._log_json("V6_SELF_CHECKS", sector)
            self._log_json("V6_COMMON_CHECKS", common)
            self.vars["deleverage_smoke_checks_done"] = True
        super().before()

```

## strategies/ResearchV6Base4h/nr7_features.py

SHA256: 7eb379f9934be3d544736c68a1ae4c73864f907212c0b9ad9efcffe91afea512

```python
"""Causal NR7 contraction and next-close expansion; no engine state or IO."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV6Base4h import BAR, atr_window, closed_window


def features(candles, now, atr, narrow_window=7):
    """Rank only prior bars; current close determines the exclusive direction."""
    invalid = dict(valid=False, direction=0, reason="nr7_data_invalid", details={})
    if (isinstance(narrow_window, bool) or not isinstance(narrow_window, int) or
            narrow_window < 2):
        return dict(valid=False, direction=0, reason="nr7_parameter_invalid", details={})
    rows = closed_window(candles, now, narrow_window + 1)
    if rows is None:
        return invalid
    try:
        # Risk must use current arithmetic14TR, not the pre-expansion offset.
        if (atr is None or atr["offset_bars"] != 0 or
                atr["first"] != now - 15 * BAR or atr["last"] != now - BAR or
                not math.isfinite(atr["value"]) or atr["value"] <= 0):
            return dict(valid=False, direction=0, reason="nr7_atr_invalid", details={})
    except (KeyError, TypeError, ValueError):
        return dict(valid=False, direction=0, reason="nr7_atr_invalid", details={})
    prior = rows[:-1]
    ranges = prior[:, 3] - prior[:, 4]
    if not np.all(np.isfinite(ranges)) or np.any(ranges < 0):
        return invalid
    setup_range = float(ranges[-1])
    comparison_min = float(np.min(ranges[:-1]))
    narrow = bool(setup_range < comparison_min)
    close, upper, lower = (float(rows[-1, 2]), float(prior[-1, 3]), float(prior[-1, 4]))
    direction = (1 if close > upper else -1 if close < lower else 0) if narrow else 0
    # Zero range may qualify strictly; equal minima do not. No epsilon changes ranking.
    reason = "nr7_breakout" if direction else "nr7_no_breakout" if narrow else "nr7_not_narrow"
    digest = hashlib.sha256(json.dumps(rows[:, :5].tolist(),
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    details = dict(narrow_window=narrow_window, first=int(rows[0, 0]),
        last=int(rows[-1, 0]), bars=narrow_window + 1, sha256=digest,
        setup_time=int(prior[-1, 0]), setup_high=upper, setup_low=lower,
        setup_range=setup_range, comparison_min=comparison_min,
        prior_ranges=[float(x) for x in ranges], narrow=narrow, close=close)
    return dict(valid=True, direction=direction, reason=reason, details=details)


def self_checks():
    """Synthetic algebra and clock checks; no claim about simulated broker fills."""
    count = 0

    def check(condition):
        nonlocal count
        assert condition
        count += 1

    def fixture():
        rows = np.array([[i*BAR, 100., 100., 102., 98., 1.] for i in range(15)])
        rows[-2, 3:5] = (100.5, 99.5)
        rows[-1, 2:5] = (103., 104., 99.)
        return rows

    now = 15 * BAR
    long = fixture()
    short = long.copy()
    short[:, 1] = 400. - long[:, 1]
    short[:, 2] = 400. - long[:, 2]
    short[:, 3] = 400. - long[:, 4]
    short[:, 4] = 400. - long[:, 3]
    for rows, expected in ((long, 1), (short, -1)):
        original = rows.copy()
        atr = atr_window(rows, now)
        result = features(rows, now, atr)
        check(result["valid"] and result["direction"] == expected)
        check(result["reason"] == "nr7_breakout")
        check(result["details"]["narrow"])
        check(result["details"]["setup_range"] == 1.)
        check(result["details"]["comparison_min"] == 4.)
        check(result["details"]["prior_ranges"] == [4.]*6 + [1.])
        check(result["details"]["first"] == now - 8*BAR)
        check(result["details"]["last"] == now - BAR)
        check(result["details"]["setup_time"] == now - 2*BAR)
        check(np.array_equal(rows, original))
        check(len("V6_FEATURES " + json.dumps(dict(time=now, line="NR7", **result),
              separators=(",", ":"), allow_nan=False)) <= 1900)
        for n in (6, 7, 8):
            item = features(rows, now, atr, n)
            check(item["direction"] == expected)
            check(item["details"]["bars"] == n + 1)
        prefix = rows[:4].copy()
        prefix[:, 0] -= 19 * BAR
        extended = np.vstack((prefix, rows))
        check(features(extended, now, atr) == result)
        extended[:4, 1:5] *= 1.5
        check(features(extended, now, atr) == result)
        future = np.array([[now, 1., float("nan"), float("inf"), -1., 0.]])
        extended = np.vstack((rows, future))
        check(features(extended, now, atr) == result)
        # Pattern depends on eight bars; ATR's independently frozen15-bar provenance stays supplied.
        check(features(rows[-8:], now, atr) == result)
        check(features(rows[-7:], now, atr)["valid"] is False)
        check(features(rows, now + 1, atr)["valid"] is False)
        check(features(rows[:-1], now, atr)["valid"] is False)
        changed = rows.copy()
        changed[-3, 3:5] = (100.5 if expected == 1 else 300.5,
                                  99.5 if expected == 1 else 299.5)
        check(features(changed, now, atr)["reason"] == "nr7_not_narrow")
    atr = atr_window(long, now)
    for value in (100.5, 99.5, 100.):
        changed = long.copy()
        changed[-1, 2] = value
        check(features(changed, now, atr)["direction"] == 0)
        check(features(changed, now, atr)["reason"] == "nr7_no_breakout")
    # B0 can traverse both previous extrema; only its final close decides, without retrofill.
    check(long[-1, 3] > long[-2, 3] and long[-1, 4] < long[-2, 4])
    check(features(long, now, atr)["direction"] == 1)
    changed = long.copy()
    changed[-1, 2] = 99.
    check(features(changed, now, atr)["direction"] == -1)
    changed[-1, 2] = 100.
    check(features(changed, now, atr)["direction"] == 0)
    # The expansion bar is never allowed to disqualify the prior NR7 contraction.
    changed = long.copy()
    changed[-1, 1:5] = (103., 103., 103.1, 102.9)
    check(features(changed, now, atr)["direction"] == 1)
    changed = long.copy()
    changed[-8, 3:5] = (100.25, 99.75)
    check(features(changed, now, atr, 6)["direction"] == 1)
    check(features(changed, now, atr, 7)["reason"] == "nr7_not_narrow")
    changed = long.copy()
    changed[-9, 3:5] = (100.25, 99.75)
    check(features(changed, now, atr, 7)["direction"] == 1)
    check(features(changed, now, atr, 8)["reason"] == "nr7_not_narrow")
    changed = long.copy()
    changed[-2, 1:5] = (100., 100., 100., 100.)
    check(features(changed, now, atr)["direction"] == 1)
    flat = np.array([[i*BAR, 100., 100., 100., 100., 1.] for i in range(15)])
    check(features(flat, now, atr)["reason"] == "nr7_not_narrow")
    check(atr_window(flat, now) is None)
    for column, value in ((0, now-3*BAR), (2, float("nan")), (3, 99.),
                          (4, 101.), (1, 0.)):
        changed = long.copy()
        changed[-2, column] = value
        check(features(changed, now, atr)["valid"] is False)
    for value in (0., -1., float("nan"), float("inf")):
        bad_atr = dict(atr, value=value)
        check(features(long, now, bad_atr)["reason"] == "nr7_atr_invalid")
    for key, value in (("offset_bars", 1), ("first", atr["first"]+BAR),
                       ("last", atr["last"]+BAR)):
        check(features(long, now, dict(atr, **{key:value}))["valid"] is False)
    check(features(long, now, None)["valid"] is False)
    for n in (0, 1, 7., True, None):
        check(features(long, now, atr, n)["reason"] == "nr7_parameter_invalid")
    # ATR supplied to entries is causal and includes the expansion's true range.
    previous_atr = atr_window(long, now, 1)
    check(previous_atr is None)
    sixteen = np.vstack((long[:1], long))
    sixteen[0, 0] -= BAR
    previous_atr = atr_window(sixteen, now, 1)
    check(previous_atr["value"] != atr["value"])
    check(features(sixteen, now, previous_atr)["reason"] == "nr7_atr_invalid")
    return dict(status="passed", assertions=count)

```

## strategies/ResearchV6Nr7P4h/__init__.py

SHA256: bf4a9993c706a34218249b7e90608108734ed2392686060fc76ee7703605fbb5

```python
from strategies.ResearchV6Base4h import ResearchV6Base4h
from strategies.ResearchV6Base4h.nr7_features import features


class ResearchV6Nr7P4h(ResearchV6Base4h):
    LINE = "NR7"
    USE_OI = False
    OI_RULE = "rising"
    NARROW_WINDOW = 7
    STOP_MULTIPLIER = 2.
    ATR_OFFSET_BARS = 0
    TARGET_MODE = "r_multiple"
    REWARD_MULTIPLE = 3.
    MAX_HOLD_BARS = 24

    def features(self, candles, now, atr):
        return features(candles, now, atr, self.NARROW_WINDOW)

```

## strategies/ResearchV6Nr7Oi4h/__init__.py

SHA256: 75dfd4b2faf89eb1a87c02d85a7d636c93ad6bbb0143df6d6e0f74937c77c4bf

```python
from strategies.ResearchV6Nr7P4h import ResearchV6Nr7P4h


class ResearchV6Nr7Oi4h(ResearchV6Nr7P4h):
    USE_OI = True

```

## strategies/ResearchV6Nr7Smoke4h/__init__.py

SHA256: e8a32b2075d052e866f082197e01f8abafa6fcc1633b05b7639d22d07a25f56d

```python
from strategies.ResearchV6Nr7P4h import ResearchV6Nr7P4h
from strategies.ResearchV6Base4h.nr7_features import self_checks as sector_checks
from strategies.ResearchV6Base4h.common_checks import self_checks as common_checks


class ResearchV6Nr7Smoke4h(ResearchV6Nr7P4h):
    FINISH = 1599523200000  # Seven-day technical window; source economic rules stay unchanged.

    def before(self):
        if not self.vars.get("nr7_smoke_checks_done"):
            sector = sector_checks()
            common = common_checks()
            assert sector["status"] == common["status"] == "passed"
            self.vars["self_checks"] = dict(sector=sector, common=common)
            self._log_json("V6_SELF_CHECKS", sector)
            self._log_json("V6_COMMON_CHECKS", common)
            self.vars["nr7_smoke_checks_done"] = True
        super().before()

```
