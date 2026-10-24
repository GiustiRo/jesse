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
