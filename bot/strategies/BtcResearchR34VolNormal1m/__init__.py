import math
import numpy as np
from strategies.BtcResearchR32SpecialistBase1m import BtcResearchR32SpecialistBase1m
from strategies.BtcResearchR10Base4h import BAR


def reset_vol_state(now):
    return dict(last=now, previous_shock=None, episode=None)


def vol_step(rows, now, previous, use_normalization):
    """Same market episode in both arms; account state never enters this step."""
    state = dict(previous or {})
    last = state.get("last")
    if last is not None and now <= last:
        return None, state, []
    closes = rows[-61:, 2]
    returns = closes[1:] / closes[:-1] - 1.0
    def sigma(values):
        # Mathematical constants must not acquire volatility from mean rounding.
        return 0.0 if np.all(values == values[0]) else float(np.std(values, ddof=0))
    if not np.all(np.isfinite(returns)):
        return None, reset_vol_state(now), [dict(kind="INVALID_FEATURE", time=now,
            episode=(state.get("episode") or {}).get("t0"))]
    v60, v10, v5 = sigma(returns), sigma(returns[-10:]), sigma(returns[-5:])
    if not all(math.isfinite(v) for v in (v60, v10, v5, 2*v60)):
        return None, reset_vol_state(now), [dict(kind="INVALID_FEATURE", time=now,
            episode=(state.get("episode") or {}).get("t0"))]
    shock = bool(v60 > 0 and v10 > 2*v60)
    if (last is None or state.get("previous_shock") is None
            or now != last + BAR):
        # First valid state, including after gaps: no manufactured transition.
        audit = []
        if state.get("episode") is not None:
            audit.append(dict(kind="CENSORED", reason="CLOCK", time=now,
                              episode=state["episode"]["t0"]))
        return None, dict(last=now, previous_shock=shock, episode=None), audit
    crossed = shock and not state["previous_shock"]
    state.update(last=now, previous_shock=shock)
    episode = state.get("episode")
    episode = dict(episode) if episode is not None else None
    audit = []
    if episode is None and crossed:
        episode = dict(t0=now, peak=v5, normal_done=False, day_done=False)
        audit.append(dict(kind="ARM", time=now, episode=now,
                          v60=v60, v10=v10, v5=v5))
    event = None
    if episode is not None:
        age = (now - episode["t0"]) // BAR
        episode["peak"] = max(episode["peak"], v5)
        normal = bool(1 <= age <= 20 and not episode["normal_done"]
                      and v5 < .5*episode["peak"])
        fixed = bool(age == 6 and not episode["day_done"])
        delta = float(closes[-1] - closes[-6])
        direction = 1 if delta > 0 else -1 if delta < 0 else 0
        if normal:
            episode["normal_done"] = True
            audit.append(dict(kind="NORMAL", time=now, episode=episode["t0"],
                              age=age, direction=direction, v5=v5, peak=episode["peak"]))
        if fixed:
            episode["day_done"] = True
            audit.append(dict(kind="DAY", time=now, episode=episode["t0"],
                              age=age, direction=direction, v5=v5, peak=episode["peak"]))
        if (normal if use_normalization else fixed) and direction:
            event = dict(direction=direction, meta=dict(episode=episode["t0"],
                age=age, v60=v60, v10=v10, v5=v5, peak=episode["peak"],
                direction_delta=delta))
        if age >= 20:
            audit.append(dict(kind="EXPIRE", time=now, episode=episode["t0"],
                normal_done=episode["normal_done"], day_done=episode["day_done"]))
            episode = None
    state["episode"] = episode
    return event, state, audit


def leaf_event(strategy, rows, now, use_normalization):
    event, state, audit = vol_step(rows, now, strategy.vars.get("vol_state"),
                                   use_normalization)
    strategy.vars["vol_state"] = state
    for row in audit:
        strategy._log("R34_VOL_EPISODE", dict(label=strategy.LABEL, **row))
    return event


def invalidate_leaf(strategy, now):
    episode = strategy.vars.get("vol_state", {}).get("episode")
    if episode is not None:
        strategy._log("R34_VOL_EPISODE", dict(label=strategy.LABEL,
            kind="CENSORED", time=now, episode=episode["t0"]))
    strategy.vars["vol_state"] = reset_vol_state(now)


class BtcResearchR34VolNormal1m(BtcResearchR32SpecialistBase1m):
    LABEL = "VOL_NORMAL"
    HOLD_HOURS = 48
    TP_R = None

    def _event(self, rows, now):
        return leaf_event(self, rows, now, True)

    def _invalid_event(self, now):
        invalidate_leaf(self, now)
