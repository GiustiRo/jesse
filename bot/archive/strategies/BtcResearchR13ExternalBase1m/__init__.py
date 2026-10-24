import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import atr14, entry_plan

HOUR = 3600000


def closed_hour_window(candles, now):
    rows = candles[candles[:, 0]+HOUR <= now][-26:]
    if len(rows) != 26 or rows[-1, 0] != now-HOUR:
        return None
    if not np.all(np.diff(rows[:, 0]) == HOUR):
        return None
    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):
        return None
    if np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2])) or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2])):
        return None
    return rows


def external_confirmation(btc, eth, require_eth):
    """Both baselines exclude current returns; BTC alone defines direction."""
    own, leader = np.diff(np.log(btc[:, 2])), np.diff(np.log(eth[:, 2]))
    own_sigma = float(np.std(own[:-1], ddof=1))
    leader_sigma = float(np.std(leader[:-1], ddof=1))
    if not all(math.isfinite(x) and x > 0 for x in (own_sigma, leader_sigma)):
        return 0
    if abs(float(own[-1])) > own_sigma:
        return 0
    momentum = float(own[-7:-1].sum())
    direction = 1 if momentum > 0 else -1 if momentum < 0 else 0
    if require_eth and not (abs(float(leader[-1])) >= 2*leader_sigma and direction*float(leader[-1]) > 0):
        return 0
    return direction


class BtcResearchR13ExternalBase1m(BtcResearchR11Base1m):
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
        if now % HOUR:
            return
        btc = closed_hour_window(self.get_candles(self.exchange, "BTC-USDT", "1h"), now)
        eth = closed_hour_window(self.get_candles(self.exchange, "ETH-USDT", "1h"), now)
        if btc is None or eth is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert np.array_equal(btc[:, 0], eth[:, 0])
        assert math.isclose(float(btc[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("ETH_CONFIRM", "BTC_CONTROL")
        direction = external_confirmation(btc, eth, self.MODE == "ETH_CONFIRM")
        if not direction or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(btc)
        if atr is None:
            return
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None or self.price+direction*2*plan["distance"] <= 0:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = direction

    def update_position(self):
        if int(self.time) % HOUR == 0 and int(self.time)-int(self.position.opened_at) >= 6*HOUR:
            self.liquidate()
