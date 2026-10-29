# V5 source freeze before technical smoke and economics

## strategies/ResearchV5Base1h/__init__.py

SHA256: e3c79b915fe881d50f902456844217977f6885e28fb4191e080e89458e5b929b

```python
import hashlib
import json
import math
from datetime import datetime, timezone

import numpy as np

from strategies.ResearchV2Core4h import (
    ResearchV2Core4h, ACCOUNTING_TOLERANCE,
)

# V5 1h decisions use explicit local clocks; only neutral V2 hooks are inherited.
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


class ResearchV5Base1h(ResearchV2Core4h):
    """1h context and execution; frozen V2 contributes only clock-neutral hooks."""
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

## strategies/ResearchV5Base1h/common_checks.py

SHA256: c8a7ae4f1c373bdc78892bcb210ac2d534f4fc58b63ef3b3a1c52a6a74a4d2a7

```python
import json
import math
from types import SimpleNamespace
import numpy as np
from strategies.ResearchV5Base1h import (
    ResearchV5Base1h, BAR, DAY, closed_window, atr_window, oi_context, v5_entry_plan,
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
    for direction in (-1,1):
        plan=v5_entry_plan(100.,10000.,.00045,direction,4.)
        check(plan["reason"] == "allowed")
        check(plan["qty"]*plan["unit_loss"] <= 200.+1e-8)
        check(plan["qty"]*100 <= 10000.)
        check(plan["qty"] == math.floor(plan["qty"]*1e8+.01)/1e8)
    check(v5_entry_plan(100.,10000.,-.1,1,4.)["reason"] == "distance_invalid")
    check(v5_entry_plan(100.,10000.,.00045,1,101.)["reason"] == "distance_invalid")
    class Surface:
        _entry_window=ResearchV5Base1h._entry_window
        _target=ResearchV5Base1h._target
        _target_valid=staticmethod(ResearchV5Base1h._target_valid)
        request_exit=ResearchV5Base1h.request_exit
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
        def on_v5_open(self):self.opened+=1
    surface=Surface()
    check(surface._entry_window(now))
    check(not surface._entry_window(surface.START))
    surface.ACTIVE_WINDOWS=()
    check(not surface._entry_window(now))
    surface=Surface();ResearchV5Base1h.before(surface)
    check(surface.vars["context"]["allowed"])
    surface=Surface();surface.vars["v5_last_exit_at"]=now
    ResearchV5Base1h.before(surface)
    check(not surface.vars["context"]["allowed"])
    check(any(b["primary"].get("same_decision_exit") for b in surface.vars["audit"].values()))
    surface=Surface();surface.vars["entry_day"]=now//DAY*DAY
    ResearchV5Base1h.before(surface)
    check(not surface.vars["context"]["allowed"])
    check(any(b["primary"].get("daily_limit") for b in surface.vars["audit"].values()))
    surface=Surface();surface.vars["entry_day"]=(now//DAY-1)*DAY
    ResearchV5Base1h.before(surface)
    check(surface.vars["context"]["allowed"])
    surface=Surface();surface.USE_OI=True
    ResearchV5Base1h.before(surface)
    check(not surface.vars["context"]["allowed"])
    surface=Surface();surface.is_open=True
    surface.request_exit("first");surface.request_exit("second")
    check(surface.exits == 1 and surface.vars["exit_reason"] == "first")
    surface.time+=BAR;surface.request_exit("next")
    check(surface.exits == 2)
    surface=Surface();surface.vars["context"]={"atr":None}
    ResearchV5Base1h.update_position(surface)
    check(surface.managed == 0)
    surface.time+=BAR;ResearchV5Base1h.update_position(surface)
    check(surface.managed == 1)
    surface.time=now+24*BAR;surface.is_open=True
    ResearchV5Base1h.update_position(surface)
    check(surface.vars["exit_reason"] == "maximum_hold")
    surface=Surface();surface.is_open=True;surface.time=now+24*BAR
    surface.FORCE_BOUNDARIES=(surface.time,)
    ResearchV5Base1h.update_position(surface)
    check(surface.vars["exit_reason"] == "calendar_boundary")
    for direction in (-1,1):
        surface=Surface()
        ResearchV5Base1h.before(surface)
        context=surface.vars["context"];plan=context["plan"]
        surface.vars["intent"]=dict(context=context,plan=plan)
        surface.is_long=direction==1;surface.is_open=True
        surface.position.entry_price=100.+direction*.05
        surface.position.qty=direction*plan["qty"]
        surface.TARGET_MODE="r_multiple"
        surface.vars["v5_exit_requested_at"]=now
        ResearchV5Base1h.on_open_position(surface,None)
        check(surface.stop_loss[1] == surface.position.entry_price-direction*4.)
        check(surface.take_profit[1] == surface.position.entry_price+direction*4.)
        check(surface.opened == 1 and surface.vars["entry_day"] == context["day"])
        check("v5_exit_requested_at" not in surface.vars)
    return dict(status="passed",assertions=checks)

```

## strategies/ResearchV5Base4h/__init__.py

SHA256: 5e0124dbc86305cccfdbbd857ba158a2e7dc10c9fdf2a905f31cfc1dd59890aa

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

## strategies/ResearchV5Base4h/common_checks.py

SHA256: f8293f146665d1c28acef67ec4a44734a6f111b4334b17cbaa15e7808a1ebdcc

```python
import json
import math
from types import SimpleNamespace
import numpy as np
from strategies.ResearchV5Base4h import (
    ResearchV5Base4h, BAR, DAY, closed_window, atr_window, oi_context, v5_entry_plan,
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
    for direction in (-1,1):
        plan=v5_entry_plan(100.,10000.,.00045,direction,4.)
        check(plan["reason"] == "allowed")
        check(plan["qty"]*plan["unit_loss"] <= 200.+1e-8)
        check(plan["qty"]*100 <= 10000.)
        check(plan["qty"] == math.floor(plan["qty"]*1e8+.01)/1e8)
    check(v5_entry_plan(100.,10000.,-.1,1,4.)["reason"] == "distance_invalid")
    check(v5_entry_plan(100.,10000.,.00045,1,101.)["reason"] == "distance_invalid")
    class Surface:
        _entry_window=ResearchV5Base4h._entry_window
        _target=ResearchV5Base4h._target
        _target_valid=staticmethod(ResearchV5Base4h._target_valid)
        request_exit=ResearchV5Base4h.request_exit
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
        def on_v5_open(self):self.opened+=1
    surface=Surface()
    check(surface._entry_window(now))
    check(not surface._entry_window(surface.START))
    surface.ACTIVE_WINDOWS=()
    check(not surface._entry_window(now))
    surface=Surface();ResearchV5Base4h.before(surface)
    check(surface.vars["context"]["allowed"])
    surface=Surface();surface.vars["v5_last_exit_at"]=now
    ResearchV5Base4h.before(surface)
    check(not surface.vars["context"]["allowed"])
    check(any(b["primary"].get("same_decision_exit") for b in surface.vars["audit"].values()))
    surface=Surface();surface.vars["entry_day"]=now//DAY*DAY
    ResearchV5Base4h.before(surface)
    check(not surface.vars["context"]["allowed"])
    check(any(b["primary"].get("daily_limit") for b in surface.vars["audit"].values()))
    surface=Surface();surface.vars["entry_day"]=(now//DAY-1)*DAY
    ResearchV5Base4h.before(surface)
    check(surface.vars["context"]["allowed"])
    surface=Surface();surface.USE_OI=True
    ResearchV5Base4h.before(surface)
    check(not surface.vars["context"]["allowed"])
    surface=Surface();surface.is_open=True
    surface.request_exit("first");surface.request_exit("second")
    check(surface.exits == 1 and surface.vars["exit_reason"] == "first")
    surface.time+=BAR;surface.request_exit("next")
    check(surface.exits == 2)
    surface=Surface();surface.vars["context"]={"atr":None}
    ResearchV5Base4h.update_position(surface)
    check(surface.managed == 0)
    surface.time+=BAR;ResearchV5Base4h.update_position(surface)
    check(surface.managed == 1)
    surface.time=now+24*BAR;surface.is_open=True
    ResearchV5Base4h.update_position(surface)
    check(surface.vars["exit_reason"] == "maximum_hold")
    surface=Surface();surface.is_open=True;surface.time=now+24*BAR
    surface.FORCE_BOUNDARIES=(surface.time,)
    ResearchV5Base4h.update_position(surface)
    check(surface.vars["exit_reason"] == "calendar_boundary")
    for direction in (-1,1):
        surface=Surface()
        ResearchV5Base4h.before(surface)
        context=surface.vars["context"];plan=context["plan"]
        surface.vars["intent"]=dict(context=context,plan=plan)
        surface.is_long=direction==1;surface.is_open=True
        surface.position.entry_price=100.+direction*.05
        surface.position.qty=direction*plan["qty"]
        surface.TARGET_MODE="r_multiple"
        surface.vars["v5_exit_requested_at"]=now
        ResearchV5Base4h.on_open_position(surface,None)
        check(surface.stop_loss[1] == surface.position.entry_price-direction*4.)
        check(surface.take_profit[1] == surface.position.entry_price+direction*4.)
        check(surface.opened == 1 and surface.vars["entry_day"] == context["day"])
        check("v5_exit_requested_at" not in surface.vars)
    return dict(status="passed",assertions=checks)

```

## strategies/ResearchV5Base4h/cross_features.py

SHA256: 5df66fdb107fe3f16484ee5cd1ca91c121c4c8bea0095e3fd95799a354f5e1e0

```python
"""Finite four-hour SMA crosses; no state, engine IO, ATR or OI in exit signals."""
import hashlib
import json
import math

import numpy as np

from strategies.ResearchV5Base4h import BAR, closed_window


def _periods_valid(fast_period, slow_period):
    return (isinstance(fast_period, int) and not isinstance(fast_period, bool) and
            isinstance(slow_period, int) and not isinstance(slow_period, bool) and
            0 < fast_period < slow_period)


def _mean(values):
    # Scale before summation: a finite mean need not have a representable raw sum.
    value = math.fsum(float(x) / len(values) for x in values)
    return value if math.isfinite(value) else None


def _direction(fast_now, fast_previous, slow_now, slow_previous):
    """Equality is allowed on the prior bar, never on the current bar."""
    if fast_previous <= slow_previous and fast_now > slow_now:
        return 1
    if fast_previous >= slow_previous and fast_now < slow_now:
        return -1
    return 0


def cross_state(candles, now, fast_period=20, slow_period=80):
    """ATR-independent entry/exit cross; each average has its own finite window."""
    if not _periods_valid(fast_period, slow_period):
        return dict(valid=False, direction=0, reason="periods_invalid",
                    details=dict(reason="periods_invalid"))
    rows = closed_window(candles, now, slow_period + 1)
    if rows is None:
        return dict(valid=False, direction=0, reason="window_invalid",
                    details=dict(reason="window_invalid"))
    closes = rows[:, 2]
    try:
        fast_now = _mean(closes[-fast_period:])
        fast_previous = _mean(closes[-fast_period-1:-1])
        slow_now = _mean(closes[-slow_period:])
        slow_previous = _mean(closes[:-1])
    except (OverflowError, ValueError):
        # Invalid arithmetic blocks a signal; it is never converted to a trend.
        fast_now = fast_previous = slow_now = slow_previous = None
    if any(x is None for x in (fast_now, fast_previous, slow_now, slow_previous)):
        return dict(valid=False, direction=0, reason="mean_invalid",
                    details=dict(reason="mean_invalid"))
    direction = _direction(fast_now, fast_previous, slow_now, slow_previous)
    reason = "setup" if direction else "no_setup"
    digest = hashlib.sha256(json.dumps(rows[:, :5].tolist(),
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    details = dict(reason=reason, fast_period=fast_period, slow_period=slow_period,
        fast_now=fast_now, fast_previous=fast_previous,
        slow_now=slow_now, slow_previous=slow_previous,
        first=int(rows[0, 0]), last=int(rows[-1, 0]), bars=slow_period + 1,
        bar_ms=BAR, sha256=digest)
    return dict(valid=True, direction=int(direction), reason=reason, details=details)


def features(candles, now, atr, fast_period=20, slow_period=80):
    result = cross_state(candles, now, fast_period, slow_period)
    if not result["valid"]:
        return result
    value = atr.get("value") if isinstance(atr, dict) else None
    if (isinstance(value, bool) or not isinstance(value, (int, float, np.integer, np.floating)) or
            not math.isfinite(value) or value <= 0):
        # This check belongs only to new exposure. Exit crosses remain usable.
        return dict(valid=False, direction=0, reason="atr_invalid",
                    details=dict(reason="atr_invalid"))
    return result


def self_checks():
    """Deterministic algebra, sign symmetry and window/future independence; no IO."""
    count = 0

    def check(value):
        nonlocal count
        assert bool(value)
        count += 1

    def candles(closes, first=0):
        closes = np.asarray(closes, dtype=float)
        return np.column_stack((np.arange(len(closes)) * BAR + first,
            closes, closes, closes + .01, closes - .01, np.ones(len(closes))))

    def reflection(rows):
        result = rows.copy()
        result[:, 1] = 400. - rows[:, 1]
        result[:, 2] = 400. - rows[:, 2]
        result[:, 3] = 400. - rows[:, 4]
        result[:, 4] = 400. - rows[:, 3]
        return result

    atr = dict(value=2.)
    for fast_period, slow_period in ((20, 80), (18, 72), (22, 88)):
        # Flat long history, twenty (or neighboring count) weak closes, then a
        # positive close: the current fast/slow cross is fresh, not a state entry.
        prices = [100.] * (slow_period - fast_period) + [99.] * fast_period + [130.]
        rows = candles(prices)
        now = len(rows) * BAR
        original = rows.copy()
        for data, side in ((rows, 1), (reflection(rows), -1)):
            state = cross_state(data, now, fast_period, slow_period)
            result = features(data, now, atr, fast_period, slow_period)
            check(state["valid"])
            check(state["direction"] == side)
            check(result == state)
            detail = state["details"]
            check(detail["bars"] == slow_period + 1)
            check(detail["last"] + BAR == now)
            check(detail["last"] - detail["first"] == slow_period * BAR)
            for key, values in (("fast_now", data[-fast_period:, 2]),
                                ("fast_previous", data[-fast_period-1:-1, 2]),
                                ("slow_now", data[-slow_period:, 2]),
                                ("slow_previous", data[:-1, 2])):
                check(abs(detail[key] - sum(float(x) for x in values) / len(values)) < 1e-12)
            check(len(json.dumps(result, allow_nan=False)) < 1700)
            future = np.vstack((data, candles([150., 151.], first=now)))
            check(cross_state(future, now, fast_period, slow_period) == state)
            future[-2:, 1:5] *= 10.
            check(cross_state(future, now, fast_period, slow_period) == state)
            prefix = candles([90.] * 10, first=-10 * BAR)
            extended = np.vstack((prefix, data))
            check(cross_state(extended, now, fast_period, slow_period) == state)
            extended[:10, 1:5] *= 2.
            check(cross_state(extended, now, fast_period, slow_period) == state)
            prior = cross_state(extended[:-1], now - BAR, fast_period, slow_period)
            check(prior["valid"])
            check(abs(prior["details"]["fast_now"] - detail["fast_previous"]) < 1e-12)
            check(abs(prior["details"]["slow_now"] - detail["slow_previous"]) < 1e-12)
            check(cross_state(data[:-1], now, fast_period, slow_period)["valid"] is False)
            check(cross_state(data, now + 1, fast_period, slow_period)["valid"] is False)
            # ATR can prevent an entry, never the independently evaluated exit.
            check(features(data, now, None, fast_period, slow_period)["valid"] is False)
            check(cross_state(data, now, fast_period, slow_period) == state)
        check(np.array_equal(rows, original))
        flat = candles([100.] * (slow_period + 1))
        flat_state = cross_state(flat, now, fast_period, slow_period)
        check(flat_state["valid"] and flat_state["direction"] == 0)
        rising = candles(100. + np.arange(slow_period + 1))
        falling = reflection(rising)
        check(cross_state(rising, now, fast_period, slow_period)["direction"] == 0)
        check(cross_state(falling, now, fast_period, slow_period)["direction"] == 0)
    check(_direction(2., 1., 1., 1.) == 1)
    check(_direction(1., 2., 2., 2.) == -1)
    check(_direction(1., 0., 1., 1.) == 0)
    check(_direction(1., 2., 1., 1.) == 0)
    check(_direction(2., 2., 1., 1.) == 0)
    check(_direction(1., 1., 2., 2.) == 0)
    nominal = candles([100.] * 60 + [99.] * 20 + [130.])
    now = 81 * BAR
    detail = cross_state(nominal, now)["details"]
    check(abs(detail["fast_previous"] - 99.) < 1e-12)
    check(abs(detail["slow_previous"] - 99.75) < 1e-12)
    check(abs(detail["fast_now"] - 100.55) < 1e-12)
    check(abs(detail["slow_now"] - 100.125) < 1e-12)
    for value in (None, 0., -1., True, float("nan"), float("inf")):
        check(features(nominal, now, dict(value=value))["valid"] is False)
    for fast_period, slow_period in ((0, 80), (20, 20), (80, 20), (20., 80), (True, 80)):
        check(cross_state(nominal, now, fast_period, slow_period)["valid"] is False)
    for column, value in ((2, float("nan")), (2, float("inf")), (3, 1.), (4, 1000.), (1, 0.)):
        broken = nominal.copy()
        broken[-1, column] = value
        check(cross_state(broken, now)["valid"] is False)
        check(features(broken, now, atr)["valid"] is False)
    broken = nominal.copy()
    broken[-10, 0] -= BAR
    check(cross_state(broken, now)["valid"] is False)
    check(cross_state(nominal[-80:], now)["valid"] is False)
    # The raw sum would overflow; scaled finite arithmetic must remain JSON-safe.
    huge = np.tile([0., 1e308, 1e308, 1e308, 1e308, 1.], (81, 1))
    huge[:, 0] = np.arange(81) * BAR
    large_state = cross_state(huge, now)
    check(large_state["valid"])
    check(large_state["direction"] == 0)
    check(len(json.dumps(large_state, allow_nan=False)) < 1700)
    return dict(status="passed", assertions=count)

```

## strategies/ResearchV5CrossP4h/__init__.py

SHA256: 6e102adcf255761c49599d9aa7c37c39db5396d9eeb18f063927c88e174d6574

```python
from strategies.ResearchV5Base4h import ResearchV5Base4h
from strategies.ResearchV5Base4h.cross_features import cross_state, features


class ResearchV5CrossP4h(ResearchV5Base4h):
    LINE = "CROSS"
    USE_OI = False
    FAST_PERIOD = 20
    SLOW_PERIOD = 80
    STOP_MULTIPLIER = 3.
    MAX_HOLD_BARS = 180
    TARGET_MODE = "none"
    ATR_OFFSET_BARS = 0

    def features(self, candles, now, atr):
        return features(candles, now, atr, self.FAST_PERIOD, self.SLOW_PERIOD)

    def manage_position(self, atr):
        # The core already prioritizes calendar/holding and post-fill timing.
        # This exit cross has no ATR/OI requirement and never schedules reversal.
        state = cross_state(self.candles, int(self.time), self.FAST_PERIOD, self.SLOW_PERIOD)
        if state["valid"] and ((self.is_long and state["direction"] == -1) or
                               (self.is_short and state["direction"] == 1)):
            self._log_json("V5_CROSS_EXIT_STATE", dict(time=int(self.time),
                opened_at=int(self.position.opened_at),
                direction=1 if self.is_long else -1, **state["details"]))
            self.request_exit("opposite_cross")

```

## strategies/ResearchV5CrossOi4h/__init__.py

SHA256: d998f560279cefcc705abd7d14b013f5edc51758b2f7c07ce8d6d6af041326be

```python
from strategies.ResearchV5CrossP4h import ResearchV5CrossP4h


class ResearchV5CrossOi4h(ResearchV5CrossP4h):
    USE_OI = True

```

## strategies/ResearchV5CrossSmoke4h/__init__.py

SHA256: 32d50a92cdb834fb35d2021fb4950d46e0cd9884177a9a21973ab6c86d996c77

```python
from strategies.ResearchV5CrossP4h import ResearchV5CrossP4h
from strategies.ResearchV5Base4h.cross_features import self_checks
from strategies.ResearchV5Base4h.common_checks import self_checks as base_checks


class ResearchV5CrossSmoke4h(ResearchV5CrossP4h):
    FINISH = 1599523200000  # Fixed seven-day technical window, 2020-09-08 UTC.

    def before(self):
        if not self.vars.get("v5_cross_checks_done"):
            sector = self_checks()
            common = base_checks()
            assert sector["status"] == common["status"] == "passed"
            self.vars["self_checks"] = sector
            self.vars["v5_base_checks"] = common
            self._log_json("V5_SELF_CHECKS", sector)
            self._log_json("V5_BASE_CHECKS", common)
            self.vars["v5_cross_checks_done"] = True
        super().before()

```

## strategies/ResearchV5Base1h/vwap_features.py

SHA256: d6652607f3a667bcadaf10d2d64eed2af42864784f05c00123f1f429d5345bde

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

## strategies/ResearchV5VwapPV1h/__init__.py

SHA256: 8e887d48edda62c227a949705710e4d5ea7eb7a2ea128dd6fa97d3886288fe4d

```python
from strategies.ResearchV5Base1h import ResearchV5Base1h
from strategies.ResearchV5Base1h.vwap_features import features as vwap_features, exit_state


class ResearchV5VwapPV1h(ResearchV5Base1h):
    LINE = "VWAP"
    USE_OI = False
    ATR_OFFSET_BARS = 0
    STOP_MULTIPLIER = 2.
    TARGET_MODE = "none"
    MAX_HOLD_BARS = 24
    BAND_MULTIPLIER = 2.

    def features(self, candles, now, atr):
        return vwap_features(candles, now, atr, self.BAND_MULTIPLIER)

    def manage_position(self, atr):
        # Exit normalization needs24 valid volume bars, not entry25 or a valid ATR.
        if int(self.time) <= int(self.position.opened_at):
            return
        result = exit_state(self.candles, int(self.time), 1 if self.is_long else -1)
        if not result["valid"]:
            self._log_json("V5_VWAP_EXIT_SKIPPED", dict(time=int(self.time), reason="vwap_invalid"))
        elif result["exit"]:
            self._log_json("V5_VWAP_EXIT_CONTEXT", dict(time=int(self.time), **result["details"]))
            self.request_exit("vwap_normalization")

```

## strategies/ResearchV5VwapPVOi1h/__init__.py

SHA256: b298c52ac035df8290601d9902fb86373babb30a5d3b97f944e3104510499ee3

```python
from strategies.ResearchV5VwapPV1h import ResearchV5VwapPV1h


class ResearchV5VwapPVOi1h(ResearchV5VwapPV1h):
    USE_OI = True

```

## strategies/ResearchV5VwapSmoke1h/__init__.py

SHA256: b656e7f2dee140f4e4e9ab1a88522bda6be64c7688ae5b9cf032a6b2a1ecdf02

```python
from strategies.ResearchV5VwapPV1h import ResearchV5VwapPV1h
from strategies.ResearchV5Base1h.vwap_features import self_checks
from strategies.ResearchV5Base1h.common_checks import self_checks as common_checks


class ResearchV5VwapSmoke1h(ResearchV5VwapPV1h):
    FINISH = 1599523200000

    def before(self):
        if "self_checks" not in self.vars:
            self.vars["self_checks"] = self_checks()
            self.vars["base_checks"] = common_checks()
            self._log_json("V5_SELF_CHECKS", self.vars["self_checks"])
            self._log_json("V5_BASE_CHECKS", self.vars["base_checks"])
        super().before()

```

## strategies/ResearchV5Base4h/funding_features.py

SHA256: a9e7d666706c41624deebfd19d905331296efd9839f6d28e68a615cec82f12ce

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

## strategies/ResearchV5FundingFP4h/__init__.py

SHA256: ef0ea4ff2e9e5444a5ee0da2d0a35d0c8d92a6d939172d24244aff15646edefd

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

## strategies/ResearchV5FundingFPOi4h/__init__.py

SHA256: c702e26a6ebd33e76af2861914e4ce9732c98375a12a3df86d3c41d91ac74dee

```python
from strategies.ResearchV5FundingFP4h import ResearchV5FundingFP4h


class ResearchV5FundingFPOi4h(ResearchV5FundingFP4h):
    USE_OI = True

```

## strategies/ResearchV5FundingSmoke4h/__init__.py

SHA256: 7ba60e6fe0e61c9af52a313f2d92a08cff2f35d5d2ac61e1cacedb396acf1847

```python
from strategies.ResearchV5FundingFP4h import ResearchV5FundingFP4h
from strategies.ResearchV5Base4h.funding_features import self_checks
from strategies.ResearchV5Base4h.common_checks import self_checks as common_checks


class ResearchV5FundingSmoke4h(ResearchV5FundingFP4h):
    FINISH = 1599523200000

    def before(self):
        if not self.vars.get("funding_smoke_checks_done"):
            sector = self_checks()
            common = common_checks()
            assert sector["status"] == common["status"] == "passed"
            self.vars["funding_smoke_checks_done"] = True
            self.vars["self_checks"] = dict(sector=sector, common=common)
            self._log_json("V5_SELF_CHECKS", sector)
            self._log_json("V5_COMMON_CHECKS", common)
        super().before()

```
