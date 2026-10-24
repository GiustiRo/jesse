import math
import numpy as np

from strategies.BtcResearchR32SpecialistBase1m import BtcResearchR32SpecialistBase1m
from strategies.BtcResearchR10Base4h import BAR, DAY

MINUTE = 60000


def _closed_tail(candles, now, width, count):
    """Small closed slice only; sorted engine timestamps are a supplied contract."""
    rows = np.asarray(candles)
    if rows.ndim != 2 or rows.shape[1] < 5 or len(rows) < count:
        return None
    # No conversion/full scan of the growing auxiliary M1 buffer.
    end = int(np.searchsorted(rows[:, 0], now - width, side="right"))
    selected = rows[max(0, end - count):end]
    if len(selected) != count or selected[-1, 0] != now - width:
        return None
    if not np.all(np.isfinite(selected[:, :5])):
        return None
    if not np.all(np.diff(selected[:, 0]) == width):
        return None
    if np.any(selected[:, 1:5] <= 0):
        return None
    if np.any(selected[:, 3] < np.maximum(selected[:, 1], selected[:, 2])):
        return None
    if np.any(selected[:, 4] > np.minimum(selected[:, 1], selected[:, 2])):
        return None
    return selected


def daily_context(btc4h, paxg4h, paxg1m, now):
    """Return (dailyrow, reason), using exactly [now-DAY,now) at UTC midnight.

    dailyrow keys: time (close timestamp), btc_open/close/high/low, paxg_close.
    Reasons identify integrity failures; none of these imply provider provenance.
    """
    if now % DAY:
        return None, "not_utc_midnight"
    btc = _closed_tail(btc4h, now, BAR, 6)
    if btc is None:
        return None, "btc_4h_day_invalid"
    paxg = _closed_tail(paxg4h, now, BAR, 6)
    if paxg is None:
        return None, "paxg_4h_day_invalid"
    minute = _closed_tail(paxg1m, now, MINUTE, 1)
    if minute is None:
        return None, "paxg_last_m1_invalid"
    if not math.isclose(float(paxg[-1, 2]), float(minute[-1, 2]),
                        rel_tol=1e-10, abs_tol=1e-8):
        return None, "paxg_m1_4h_close_mismatch"
    return dict(time=int(now), btc_open=float(btc[0, 1]),
                btc_close=float(btc[-1, 2]), btc_high=float(np.max(btc[:, 3])),
                btc_low=float(np.min(btc[:, 4])),
                paxg_close=float(paxg[-1, 2])), None


def timing_setup(history):
    """64 valid online daily rows -> setup; never reconstruct old fixings.

    Returned context includes current/prior PAXG prices even during seed.
    ready=True means 64 rows; invalid derived statistics mean ineligible, not
    broken OHLC history. A uses 14 daily TRs excluding the latest daily row.
    """
    size = len(history)
    context = dict(ready=False, eligible=False, reason="seed",
                   days=size, G=None, B=None, sigma=None, A=None,
                   paxg_close=None, paxg_previous=None)
    if not size:
        return context
    context["paxg_close"] = float(history[-1]["paxg_close"])
    if size >= 2:
        context["paxg_previous"] = float(history[-2]["paxg_close"])
    if size < 64:
        return context
    rows = history[-64:]
    p = np.array([row["paxg_close"] for row in rows], dtype=float)
    closes = np.array([row["btc_close"] for row in rows], dtype=float)
    # 63 daily changes minus the last three event changes = exactly 60.
    with np.errstate(over="ignore", invalid="ignore"):
        sigma = float(np.std(np.diff(p)[:-3], ddof=0))
        G = float(p[-1] - p[-4])
        B = float(closes[-1] - closes[-4])
        previous = closes[-16:-2]
        current = rows[-15:-1]
        highs = np.array([row["btc_high"] for row in current], dtype=float)
        lows = np.array([row["btc_low"] for row in current], dtype=float)
        tr = np.maximum(highs - lows,
                        np.maximum(abs(highs - previous), abs(lows - previous)))
        A = float(np.mean(tr))
    context["ready"] = True
    for key, value in (("sigma", sigma), ("G", G), ("B", B), ("A", A)):
        context[key] = value if math.isfinite(value) else None
    if not all(math.isfinite(value) for value in (sigma, G, B, A)):
        context["reason"] = "derived_nonfinite"
    elif sigma <= 0 or A <= 0:
        context["reason"] = "derived_nonpositive"
    else:
        context["reason"] = "eligible" if G >= 2 * sigma and abs(B) <= .5 * A else "ineligible"
        context["eligible"] = context["reason"] == "eligible"
    return context


def advance_episode(state, context, now):
    """Pure common episode clock; returns (newstate, actions), independent of MODE.

    state: eligible_previous, episode (or None), last_time. Episode keeps both
    firing flags even in the other policy. actions has unwind/clock opportunities,
    armed metadata, dropped_transition, expired, and expired_without_unwind.
    Caller clears state/history on OHLC or daily-clock failure before invoking.
    """
    updated = dict(eligible_previous=bool(state.get("eligible_previous", False)),
                   episode=None if state.get("episode") is None else dict(state["episode"]),
                   last_time=int(state.get("last_time", -1)))
    actions = dict(unwind=None, clock=None, armed=None,
                   dropped_transition=False, expired=False,
                   expired_without_unwind=False)
    if now <= updated["last_time"]:
        return updated, actions
    updated["last_time"] = int(now)
    eligible = bool(context["eligible"])
    transition = eligible and not updated["eligible_previous"]
    had_episode = updated["episode"] is not None
    # Snapshot occupancy at midnight: expiry today cannot permit rearm today.
    if had_episode:
        episode = updated["episode"]
        age = (now - int(episode["armed_at"])) // DAY
        assert now - int(episode["armed_at"]) == age * DAY and 1 <= age <= 3
        evidence = dict(armed_at=episode["armed_at"], age_days=int(age),
                        paxg_at_arm=episode["paxg_at_arm"],
                        paxg_current=context["paxg_close"],
                        paxg_previous=context["paxg_previous"],
                        arm_G=episode["G"], arm_B=episode["B"],
                        arm_sigma=episode["sigma"], arm_A=episode["A"])
        if age == 1 and not episode["clock_fired"]:
            episode["clock_fired"] = True
            actions["clock"] = dict(evidence)
        # A currently degenerate setup cannot invalidate an already armed event.
        if (not episode["unwind_fired"]
                and context["paxg_close"] < context["paxg_previous"]):
            episode["unwind_fired"] = True
            actions["unwind"] = dict(evidence)
        if age == 3:
            actions["expired"] = True
            actions["expired_without_unwind"] = not episode["unwind_fired"]
            updated["episode"] = None
        if transition:
            actions["dropped_transition"] = True
    elif transition:
        episode = dict(armed_at=int(now), paxg_at_arm=context["paxg_close"],
                       G=context["G"], B=context["B"],
                       sigma=context["sigma"], A=context["A"],
                       unwind_fired=False, clock_fired=False)
        updated["episode"] = episode
        actions["armed"] = dict(episode)
    updated["eligible_previous"] = eligible
    return updated, actions


class BtcResearchR40PaxgTimingBase1m(BtcResearchR32SpecialistBase1m):
    """UTC daily context only; BTC execution and the real ledger stay inherited."""
    MODE = "abstract"
    HOLD_HOURS = 48
    TP_R = None

    def _timing_counts(self):
        return self.vars.setdefault("r40_counts", dict(
            days=0, valid_days=0, seed_days=0, eligible_days=0,
            invalid_days=0, gap_resets=0, setup_degenerate=0,
            transitions=0, arms=0, transitions_lost=0,
            clock_events=0, unwind_events=0, selected_events=0,
            expired=0, expired_without_unwind=0, invalid_reasons={}))

    def _clear_timing(self):
        self.vars["r40_history"] = []
        self.vars["r40_state"] = dict(eligible_previous=False, episode=None,
                                      last_time=-1)

    def _begin_day(self, now):
        if now % DAY or not self.START <= now < self.FINISH:
            return False, False
        previous = self.vars.get("r40_last_day")
        if previous is not None and now <= previous:
            return False, False
        counts = self._timing_counts()
        gap = previous is not None and now != previous + DAY
        if gap:
            self._clear_timing()
            counts["gap_resets"] += 1
        self.vars["r40_last_day"] = int(now)
        counts["days"] += 1
        return True, gap

    def _invalid_day(self, now, reason, gap=False):
        counts = self._timing_counts()
        counts["invalid_days"] += 1
        reasons = counts["invalid_reasons"]
        reasons[reason] = reasons.get(reason, 0) + 1
        self._clear_timing()
        self._log("R40_DAY", dict(label=self.LABEL, time=now,
            status="invalid", reason=reason, gap_reset=gap, history_days=0,
            daily=None, setup=None, state=self.vars["r40_state"]))

    def _invalid_event(self, now):
        accepted, gap = self._begin_day(now)
        if accepted:
            self._invalid_day(now, "btc_parent_64_invalid", gap)

    def _event(self, rows, now):
        assert self.MODE in ("UNWIND", "CLOCK")
        accepted, gap = self._begin_day(now)
        if not accepted:
            return None
        daily, reason = daily_context(rows,
            self.get_candles(self.exchange, "PAXG-USDT", "4h"),
            self.get_candles(self.exchange, "PAXG-USDT", "1m"), now)
        if daily is None:
            self._invalid_day(now, reason, gap)
            return None
        counts = self._timing_counts()
        counts["valid_days"] += 1
        history = list(self.vars.get("r40_history", []))
        history.append(daily)
        history = history[-64:]
        self.vars["r40_history"] = history
        context = timing_setup(history)
        state = self.vars.get("r40_state",
                              dict(eligible_previous=False, episode=None, last_time=-1))
        had_episode = state["episode"] is not None
        if not context["ready"]:
            counts["seed_days"] += 1
        elif context["reason"] in ("derived_nonfinite", "derived_nonpositive"):
            counts["setup_degenerate"] += 1
        if context["eligible"]:
            counts["eligible_days"] += 1
        if context["eligible"] and not state["eligible_previous"]:
            counts["transitions"] += 1
        state, actions = advance_episode(state, context, now)
        self.vars["r40_state"] = state
        if actions["armed"] is not None:
            counts["arms"] += 1
            self._log("R40_ARM", dict(label=self.LABEL, time=now, **actions["armed"]))
        if actions["dropped_transition"]:
            counts["transitions_lost"] += 1
        for kind in ("clock", "unwind"):
            if actions[kind] is not None:
                counts[kind + "_events"] += 1
                self._log("R40_EVENT", dict(label=self.LABEL, time=now,
                    kind=kind.upper(), selected=self.MODE == kind.upper(),
                    **actions[kind]))
        if actions["expired"]:
            counts["expired"] += 1
            counts["expired_without_unwind"] += int(actions["expired_without_unwind"])
        # Bounded complete fixings allow an audit replay without external candles.
        self._log("R40_DAY", dict(label=self.LABEL, time=now,
            status=context["reason"], gap_reset=gap, history_days=len(history),
            daily=daily, setup=context, state=state,
            episode_at_start=had_episode,
            armed=actions["armed"] is not None, expired=actions["expired"],
            expired_without_unwind=actions["expired_without_unwind"],
            dropped_transition=actions["dropped_transition"],
            clock_event=actions["clock"] is not None,
            unwind_event=actions["unwind"] is not None))
        selected = actions[self.MODE.lower()]
        if selected is None:
            return None
        counts["selected_events"] += 1
        return dict(direction=1, meta=dict(mode=self.MODE, **selected))

    def update_position(self):
        # Native termination has priority over an otherwise simultaneous 48h exit.
        if int(self.time) >= self.FINISH:
            return
        super().update_position()

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R40_STATS", dict(stage=stage, label=self.LABEL,
            mode=self.MODE, history_days=len(self.vars.get("r40_history", [])),
            **self._timing_counts()))
