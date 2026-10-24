import math
import numpy as np
import jesse.indicators as ta

from strategies.BtcResearchR16LegacyBase1m import BtcResearchR16LegacyBase1m, legacy_history
from strategies.BtcResearchR10Base4h import BAR

MINUTE = 60000


def external_clock_context(btc_minutes, eth_minutes, now, btc_close):
    """Both past M1 windows/cutoffs share validity; ETH sets time only."""
    start = now - BAR
    windows = []
    for raw in (btc_minutes, eth_minutes):
        if raw.ndim != 2 or raw.shape[1] < 6:
            return None, "shape"
        # Runtime M1 timestamps are sorted (P framework audit). Binary bounds
        # avoid scanning/copying a growing multi-year history for each decision.
        times = raw[:, 0]
        left = int(np.searchsorted(times, start, side="left"))
        right = int(np.searchsorted(times, now, side="left"))
        rows = raw[left:right]
        if (len(rows) != 240
                or not np.array_equal(rows[:, 0], start + np.arange(240) * MINUTE)):
            return None, "clock"
        if (not np.all(np.isfinite(rows[:, :6]))
                or not np.all(rows[:, 1:5] > 0) or np.any(rows[:, 5] < 0)
                or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2]))
                or np.any(np.maximum(rows[:, 1], rows[:, 2]) > rows[:, 3])):
            return None, "ohlcv"
        windows.append(rows)
    btc, eth = windows
    if float(btc[-1, 2]) != float(btc_close):
        return None, "btc_close"
    cutoffs, fractions = [], []
    for rows in windows:
        # Preserve X805 raw arithmetic, including side='left' at exact half.
        # Normalization is conceptual; near-half floating sums need not scale
        # identically and are never repaired with an economic epsilon.
        volume = rows[:, 5]
        with np.errstate(over="ignore", invalid="ignore"):
            total = float(np.sum(volume))
            cumulative = np.cumsum(volume)
        if not math.isfinite(total) or total <= 0 or not np.all(np.isfinite(cumulative)):
            return None, "total"
        cutoff = int(np.searchsorted(cumulative, .5 * total, side="left"))
        if not 0 <= cutoff < 239:
            return None, "empty_partition"
        cutoffs.append(cutoff)
        fractions.append(float(cumulative[cutoff] / total))
    contexts = []
    for cutoff in cutoffs:
        first, second = btc[:cutoff+1], btc[cutoff+1:]
        # ETH second-group volume is allowed to be zero. Only BTC weights price.
        costs = []
        for group in (first, second):
            with np.errstate(over="ignore", invalid="ignore"):
                weight = float(np.sum(group[:, 5]))
                typical = np.mean(group[:, [3, 4, 2]], axis=1)
                products = typical * group[:, 5]
                weighted = float(np.sum(products))
            if (not math.isfinite(weight) or weight <= 0
                    or not np.all(np.isfinite(typical))
                    or not np.all(np.isfinite(products)) or not math.isfinite(weighted)):
                return None, "btc_weight_or_cost"
            cost = weighted / weight
            if not math.isfinite(cost) or cost <= 0:
                return None, "btc_cost"
            costs.append(cost)
        contexts.append(dict(cutoff=cutoff, time=int(btc[cutoff, 0]),
                             first_cost=costs[0], second_cost=costs[1],
                             first_low=float(np.min(first[:, 4]))))
    return dict(start=int(start), finish=int(now), btc=contexts[0], eth=contexts[1],
                btc_first_fraction=fractions[0], eth_first_fraction=fractions[1]), None


def clock_setups(c, context):
    """The ORIGINAL short-only X805 setup, differing only at chosen boundary."""
    w = c[-14:]
    if (context is None or len(w) != 14 or not np.all(np.isfinite(w))
            or not np.all(w[:, 1:] > 0) or not np.all(w[:, 3] >= w[:, 4])):
        return None
    s, t = c[-2], c[-1]
    base = bool(s[2] > c[-14, 2] and t[2] < t[1])
    values = {}
    for key in ("btc", "eth"):
        part = context[key]
        values[key] = bool(base and part["second_cost"] < part["first_cost"]
                           and t[2] < part["first_low"])
    return dict(base=base, **values)


def clock_supplement_event(c, context):
    """Called only AFTER selected full setup has consumed its false->true latch."""
    atr = float(ta.atr(c))  # Real legacy Wilder14/default with exposed history.
    if not math.isfinite(atr) or atr <= 0:
        return None
    s, t = c[-2], c[-1]
    distance = float(max(s[3], t[3]) + .25 * atr - t[2])
    if not atr <= distance <= 3 * atr:
        return None
    entry = float(t[2])
    # Exact physical TP guard, common to both clocks, AFTER latch consumption.
    if not (math.isfinite(distance) and 0 < distance < entry and entry - 2*distance > 0):
        return None
    return dict(origin="SUPPLEMENT", direction=-1, entry=entry, distance=distance,
                target_distance=2*distance, hold_hours=48, order_kind="MARKET",
                clock_evidence=context)


class BtcResearchR21ExternalClockBase1m(BtcResearchR16LegacyBase1m):
    MODE = "abstract"

    def _clock_count(self, label, value=1):
        if self.START < int(self.time) < self.FINISH:
            counts = self.vars.setdefault("clock_counts", {})
            counts[label] = counts.get(label, 0) + value

    def _clock_invalid(self, reason):
        self.vars["previous_setup"] = False
        self.vars["supplement_event"] = None
        self._clock_count("invalid:" + reason)

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("BTC_CLOCK", "ETH_CLOCK")
            self.vars["checked"] = True
            self._log("R21_CLOCK_CONFIG", dict(mode=self.MODE, fraction=.5,
                      minutes=240, original_setup="X805", branches=3,
                      risk=.02, aggregate=.06, leverage=3, fee=.00045,
                      reserve=.001, lot=.001))
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        self.vars["decision_at"] = now
        self.vars["supplement_event"] = None
        rows = legacy_history(self.get_candles(self.exchange, self.symbol, "4h"), now)
        self.vars["legacy_rows"] = rows
        if rows is None:
            self.vars["previous_setup"] = False
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self._clock_count("btc4h_invalid")
            return
        self.vars["history_min"] = min(self.vars.get("history_min", len(rows)), len(rows))
        self.vars["history_max"] = max(self.vars.get("history_max", len(rows)), len(rows))
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        self._clock_count("btc4h_valid")
        if self.is_open or self.entry_orders:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
        context, reason = external_clock_context(
            self.get_candles(self.exchange, self.symbol, "1m"),
            self.get_candles(self.exchange, "ETH-USDT", "1m"), now, float(rows[-1, 2]))
        if context is None:
            # Missing external data suppresses ONLY supplement, never original
            # core/runner candidates or their valid BTC history/trailing.
            self._clock_invalid(reason)
            return
        self._clock_count("input_valid")
        self._clock_count("same_cut", int(context["btc"]["cutoff"] == context["eth"]["cutoff"]))
        self._clock_count("cut_distance_sum", abs(context["btc"]["cutoff"]-context["eth"]["cutoff"]))
        self._clock_count("btc_cut_sum", context["btc"]["cutoff"])
        self._clock_count("eth_cut_sum", context["eth"]["cutoff"])
        self._clock_count("btc_first_fraction_sum", context["btc_first_fraction"])
        self._clock_count("eth_first_fraction_sum", context["eth_first_fraction"])
        setups = clock_setups(rows, context)
        if setups is None:
            self._clock_invalid("supplement4h")
            return
        self._clock_count("base", int(setups["base"]))
        self._clock_count("btc_setup", int(setups["btc"]))
        self._clock_count("eth_setup", int(setups["eth"]))
        self._clock_count("disagreement", int(setups["btc"] != setups["eth"]))
        if self.is_open or self.entry_orders:
            self._clock_count("occupied_disagreement", int(setups["btc"] != setups["eth"]))
        chosen = "eth" if self.MODE == "ETH_CLOCK" else "btc"
        setup = setups[chosen]
        previous = self.vars.get("previous_setup", False)
        # Update full setup BEFORE taATR, geometry, monetary and occupation gates.
        self.vars["previous_setup"] = setup
        if not setup or previous:
            return
        self._clock_count("selected_transition")
        evidence = dict(context, chosen=chosen, setup_btc=setups["btc"], setup_eth=setups["eth"])
        event = clock_supplement_event(rows, evidence)
        if event is None:
            self._clock_count("geometry_or_physical_rejection")
            return
        self.vars["supplement_event"] = event
        self.vars["supplement_events"] = self.vars.get("supplement_events", 0)+1
        self._clock_count("event")

    def on_open_position(self, order):
        super().on_open_position(order)
        plan = self.vars["position_plan"]
        if plan["origin"] == "SUPPLEMENT":
            self._log("R21_CLOCK_OPEN", dict(mode=self.MODE, time=int(self.time),
                      evidence=plan["clock_evidence"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R21_CLOCK_STATS", dict(stage=stage, mode=self.MODE,
                  counts=self.vars.get("clock_counts", {})))
