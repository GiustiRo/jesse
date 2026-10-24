import math
import numpy as np
from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan

MINUTE = 60000
DAY = 6*BAR
LABEL_FEE = .00045


def utility_label(origin_rows, minutes, origin_time, now):
    """Two mathematical fee-only outcomes, not trades/orders or full net PnL."""
    deadline = origin_time+DAY
    if now < deadline:
        return dict(mature=False, valid=False, reason="immature", deadline=deadline)
    record = dict(mature=True, valid=False, deadline=deadline)
    if len(origin_rows) != 15:
        return dict(record, reason="atr_history")
    entry = float(origin_rows[-1, 2])
    atr = atr14(origin_rows)
    distance = 2*atr if atr is not None else float("nan")
    if not (math.isfinite(entry) and math.isfinite(distance) and 0 < distance < entry):
        return dict(record, reason="atr_or_stop")
    # Search views; never copy/filter/scan the growing full M1 buffer.
    times = minutes[:, 0]
    left = int(np.searchsorted(times, origin_time, side="left"))
    right = int(np.searchsorted(times, deadline, side="left"))
    path = minutes[left:right]
    if len(path) != 1440:
        return dict(record, reason="m1_count")
    expected = origin_time+np.arange(1440, dtype=np.int64)*MINUTE
    if not np.array_equal(path[:, 0], expected):
        return dict(record, reason="m1_clock")
    if int(path[-1, 0])+MINUTE > now:
        return dict(mature=False, valid=False, reason="immature", deadline=deadline)
    if (not np.all(np.isfinite(path[:, :5])) or np.any(path[:, 1:5] <= 0)
            or np.any(path[:, 3] < np.maximum(path[:, 1], path[:, 2]))
            or np.any(path[:, 4] > np.minimum(path[:, 1], path[:, 2]))):
        return dict(record, reason="m1_ohlc")
    outcomes, exits, touches = [], [], []
    for side in (1, -1):
        stop = entry-side*distance
        hit = path[:, 4] <= stop if side == 1 else path[:, 3] >= stop
        indices = np.flatnonzero(hit)
        if len(indices):
            index = int(indices[0])
            opening = float(path[index, 1])
            exit_price = min(opening, stop) if side == 1 else max(opening, stop)
            touch = index
        else:
            exit_price = float(path[-1, 2])
            touch = None
        payoff = side*(exit_price-entry)/entry-LABEL_FEE*(entry+exit_price)/entry
        if not math.isfinite(payoff):
            return dict(record, reason="nonfinite_payoff")
        outcomes.append(float(payoff))
        exits.append(float(exit_price))
        touches.append(touch)
    # Funding deliberately absent: real held-position ledger still pays funding.
    return dict(record, valid=True, reason=None, entry=entry, distance=distance,
                outcomes=outcomes, exits=exits, touches=touches)


def utility_sample(rows, minutes, now, cache, counters):
    """Fixed360 origins with8 padding bars; cache only immutable mature pairs."""
    assert len(rows) == 380
    origins = np.arange(14, 374, dtype=int)
    origin_times = [int(rows[i, 0])+BAR for i in origins]
    expected = set(origin_times)
    for key in tuple(cache):
        if key not in expected:
            del cache[key]
            counters["cache_purged"] = counters.get("cache_purged", 0)+1
    # A binary asof boundary avoids an O(total M1 history) mask/copy every4h.
    right = int(np.searchsorted(minutes[:, 0], now-MINUTE, side="right"))
    closed_minutes = minutes[:right]
    counters["m1_visible_rows"] = right
    counters["m1_oldest"] = int(closed_minutes[0, 0]) if right else None
    counters["fixed_origins"] = 360
    logs = np.log(rows[:, 2])
    returns = np.diff(logs)
    raw_vectors = returns[origins[:, None]-6+np.arange(6)]
    norms = np.linalg.norm(raw_vectors, axis=1)
    current = returns[-6:]
    current_norm = float(np.linalg.norm(current))
    eligible_origins, vectors, outcomes = [], [], []
    feature_invalid = 0
    for j, i in enumerate(origins):
        origin_time = origin_times[j]
        if origin_time in cache:
            record = cache[origin_time]
            counters["cache_hits"] = counters.get("cache_hits", 0)+1
        else:
            counters["cache_misses"] = counters.get("cache_misses", 0)+1
            record = utility_label(rows[i-14:i+1], closed_minutes, origin_time, now)
            if record["mature"]:
                cache[origin_time] = record
                key = "labels_valid" if record["valid"] else "labels_invalid"
                counters[key] = counters.get(key, 0)+1
                if not record["valid"]:
                    reasons = counters.setdefault("invalid_reasons", {})
                    reason = record["reason"]
                    reasons[reason] = reasons.get(reason, 0)+1
            else:
                counters["future_denied"] = counters.get("future_denied", 0)+1
        feature_valid = bool(np.all(np.isfinite(raw_vectors[j]))
                             and math.isfinite(float(norms[j])) and norms[j] > 0)
        feature_invalid += int(not feature_valid)
        if record["valid"] and feature_valid:
            eligible_origins.append(int(i))
            vectors.append(raw_vectors[j]/norms[j])
            outcomes.append(record["outcomes"])
    count = len(eligible_origins)
    counters["common_valid"] = count
    counters["common_valid_min"] = min(counters.get("common_valid_min", count), count)
    counters["common_valid_max"] = max(counters.get("common_valid_max", count), count)
    counters["feature_invalid"] = feature_invalid
    counters["cached"] = len(cache)
    counters["decisions"] = counters.get("decisions", 0)+1
    if (not np.all(np.isfinite(current)) or not math.isfinite(current_norm)
            or current_norm <= 0 or count < 20):
        return None
    return dict(origins=np.asarray(eligible_origins, dtype=int),
                vectors=np.asarray(vectors), outcomes=np.asarray(outcomes),
                current=current/current_norm)


def utility_choice(means):
    """LONG wins an exact positive tie; negative utilities never imply short."""
    long, short = float(means[0]), float(means[1])
    if not math.isfinite(long) or not math.isfinite(short) or max(long, short) <= .0019:
        return 0
    return 1 if long >= short else -1


def utility_forecast(rows, minutes, now, cache, counters, nearest):
    sample = utility_sample(rows, minutes, now, cache, counters)
    if sample is None:
        return 0, None
    cosine = sample["vectors"] @ sample["current"]
    if not np.all(np.isfinite(cosine)):
        return 0, None
    order = np.argsort(-cosine, kind="stable")
    chosen = order[:20] if nearest else np.arange(len(order))
    means = np.mean(sample["outcomes"][chosen], axis=0)
    direction = utility_choice(means)
    evidence = dict(long_utility=float(means[0]), short_utility=float(means[1]),
        valid_origins=len(order), selected=len(chosen),
        chosen_origins=[int(i) for i in sample["origins"][chosen]] if nearest else None,
        label_units="fee_only_per_initial_notional", label_funding=False)
    return direction, evidence


class BtcResearchR19UtilityBase1m(BtcResearchR12ArBase1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-LABEL_FEE) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("KNN", "GLOBAL")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 380)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        minutes = self.get_candles(self.exchange, self.symbol, "1m")
        counters = self.vars.setdefault("utility_counters", {})
        direction, evidence = utility_forecast(rows, minutes, now,
            self.vars.setdefault("utility_cache", {}), counters, self.MODE == "KNN")
        if not direction or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(rows)
        if atr is None:
            return
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            return
        self.vars["plan"] = dict(plan, utility=dict(evidence))
        self.vars["direction"] = direction

    def on_open_position(self, order):
        # Preserve actual-fill SL, noTP and24h/first4h-after-deadline semantics.
        # Label entry at origin-close and exact24h is a declared counterfactual.
        super().on_open_position(order)
        direction = 1 if self.is_long else -1
        key = "long_fills" if direction == 1 else "short_fills"
        self.vars[key] = self.vars.get(key, 0)+1
        self._log("R19_UTILITY_OPEN", dict(time=int(self.time), mode=self.MODE,
            opened_at=int(self.position.opened_at), direction=direction,
            evidence=self.vars["plan"]["utility"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R19_UTILITY_STATS", dict(stage=stage, mode=self.MODE,
            long_fills=self.vars.get("long_fills", 0),
            short_fills=self.vars.get("short_fills", 0),
            coverage=self.vars.get("utility_counters", {}),
            label_funding=False, actual_funding="historical_ledger_required"))
