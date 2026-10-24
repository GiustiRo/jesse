import math

import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan

DAY = 86400000


def clock_signal(rows, state, volume_clock):
    """Whole4h bars form activity buckets; no split or invented intra-bar fill."""
    row = rows[-1]
    if not np.all(np.isfinite(rows[:, 5])) or np.any(rows[:, 5] < 0):
        return 0, {}
    previous = list(state.get("closed", []))
    active = dict(state["active"]) if state.get("active") else None
    if active is None:
        # Calendar comparator uses whole UTC days even after an invalid-data reset.
        if not volume_clock and int(row[0]) % DAY != 0:
            return 0, dict(active=None, closed=previous)
        threshold = 6 * float(np.mean(rows[-25:-1, 5]))
        if volume_clock and (not math.isfinite(threshold) or threshold <= 0):
            return 0, {}
        active = dict(volume=0.0, bars=0, high=float(row[3]), low=float(row[4]),
                      threshold=threshold, start=int(row[0]))
    active["volume"] += float(row[5])
    active["bars"] += 1
    active["high"] = max(active["high"], float(row[3]))
    active["low"] = min(active["low"], float(row[4]))
    completed = active["volume"] >= active["threshold"] if volume_clock else active["bars"] == 6
    if not completed:
        return 0, dict(active=active, closed=previous)
    direction = 0
    if len(previous) == 3:
        if row[2] > max(p["high"] for p in previous):
            direction = 1
        elif row[2] < min(p["low"] for p in previous):
            direction = -1
    # Consume the full overshoot and the event, including when a trade is occupied.
    previous.append(dict(high=active["high"], low=active["low"],
                         start=active["start"], finish=int(row[0]) + BAR))
    return direction, dict(active=None, closed=previous[-3:])


class BtcResearchR11ClockBase1m(BtcResearchR11Base1m):
    """Compare activity sampling against a fixed-calendar channel."""
    MODE = "abstract"

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
        count = 25
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        rows = closed_window(candles, now, count)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            self.vars["bucket_state"] = {}
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("VOLUME_CLOCK", "FIXED_CLOCK")
        direction, state = clock_signal(rows, self.vars.get("bucket_state", {}),
                                        self.MODE == "VOLUME_CLOCK")
        self.vars["bucket_state"] = state
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

