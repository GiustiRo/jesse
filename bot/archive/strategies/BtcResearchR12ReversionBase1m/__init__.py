import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def kalman_event(rows, state):
    """Predict before assimilating current close; original R40 coefficients."""
    x = np.log(rows[-62:, 2])
    variance = float(np.var(np.diff(x[:-1]), ddof=1))
    if not math.isfinite(variance) or variance <= 0:
        return None, {}
    q, r = .01 * variance, .25 * variance
    m, p = state.get("filter", (float(x[-2]), r))
    pp = p + q
    innovation, s = float(x[-1]) - m, pp + r
    z = innovation / math.sqrt(s)
    k = pp / s
    regime = 1 if z >= 1.5 else -1 if z <= -1.5 else 0
    new = {"filter": (m+k*innovation, (1-k)*pp), "regime": regime}
    if not regime or regime == state.get("regime", 0):
        return None, new
    direction, target = -regime, math.exp(m)
    atr = atr14(rows)
    if atr is None or direction * (target-float(rows[-1, 2])) <= 0:
        return None, new
    return dict(direction=direction, distance=2*atr, target=target, hours=48), new


def recovery_event(rows, state):
    """One mature excursion, frozen arm ATR, separate confirmation and expiry."""
    state = dict(state)
    state["used"] = dict(state.get("used", {1: -1, -1: -1}))
    used = state["used"]
    now, price = int(rows[-1, 0])+BAR, float(rows[-1, 2])
    episode = state.get("episode")
    if episode:
        episode = dict(episode)
        state["episode"] = episode
        direction = episode["direction"]
        if now-episode["armed"] >= 60*BAR:
            used[direction] = episode["origin"]
            state.pop("episode")
            return None, state
        episode["turn"] = (min if direction == 1 else max)(episode["turn"], price)
        depth = direction * (episode["anchor"]-episode["turn"])
        level = episode["turn"] + direction*.5*depth
        if direction*(price-level) >= 0 and depth >= 4*episode["atr"]:
            used[direction] = episode["origin"]
            state.pop("episode")
            return dict(direction=direction, distance=2*episode["atr"],
                        target=None, hours=72), state
        return None, state
    atr = atr14(rows)
    if atr is None:
        return None, state
    c = rows[-60:, 2]
    imax = len(c)-1-int(np.argmax(c[::-1]))
    imin = len(c)-1-int(np.argmin(c[::-1]))
    candidates = []
    for direction, index in ((1, imax), (-1, imin)):
        anchor, origin = float(c[index]), int(rows[-60+index, 0])
        displacement = direction*(anchor-price)
        if len(c)-1-index >= 12 and displacement >= 4*atr and origin > used[direction]:
            turn = float((np.min if direction == 1 else np.max)(c[index:]))
            candidates.append(dict(direction=direction, origin=origin, anchor=anchor,
                                   turn=turn, atr=atr, armed=now, score=displacement/atr))
    candidates.sort(key=lambda a: -a["score"])
    if candidates and (len(candidates) == 1 or candidates[0]["score"] > candidates[1]["score"]):
        state["episode"] = candidates[0]
    return None, state


class BtcResearchR12ReversionBase1m(BtcResearchR11Base1m):
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
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 62)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self.vars["model"] = {}
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("KALMAN", "RECOVERY")
        function = kalman_event if self.MODE == "KALMAN" else recovery_event
        event, state = function(rows, self.vars.get("model", {}))
        self.vars["model"] = state
        if not event or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        direction = event["direction"]
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, event["distance"])
        if plan is None or (event["target"] is None and self.price+direction*2*plan["distance"] <= 0):
            return
        self.vars["plan"] = dict(plan, target=event["target"], hours=event["hours"])
        self.vars["direction"] = direction

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        stop = entry-direction*plan["distance"]
        assert qty*(plan["distance"]+self.fee_rate*(entry+stop)) <= plan["risk_budget"]+1e-6
        self.stop_loss = qty, stop
        # Kalman target is the frozen predictive level, not shifted by the fill.
        target = plan["target"] if plan["target"] is not None else entry+direction*2*plan["distance"]
        assert direction*(target-entry) > 0
        self.take_profit = qty, target
        self.vars["holding_hours"] = plan["hours"]
        self.vars["entries"] = self.vars.get("entries", 0)+1
        self._observe("open")

    def update_position(self):
        if int(self.time) % BAR == 0 and int(self.time)-int(self.position.opened_at) >= self.vars["holding_hours"]*3600000:
            self.liquidate()
