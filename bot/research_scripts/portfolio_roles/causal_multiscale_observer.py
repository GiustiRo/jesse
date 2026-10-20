"""Provisional causal multiscale BTC observer; no trading or external data.

Only --describe-api and --self-test are ready for host review. The DB adapter
is deliberately absent until Jesse's public get_candles contract is confirmed.
The pure core accepts chronological OHLCV arrays and never reads ahead of asof.
"""
import argparse
import csv
import importlib
import inspect
import json
import math
import sys
from collections import Counter, deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

MINUTE = 60_000
BAR = 4 * 60 * MINUTE
DAY = 24 * 60 * MINUTE
HORIZON = DAY
WINDOW = 180 * DAY
SHRINK = 20.0
ATR_PERIOD = 14
CLASSES = ("up", "down", "none")
STATES = ("U", "D", "M")
START = int(datetime(2020, 10, 15, tzinfo=timezone.utc).timestamp() * 1000)
FINISH = int(datetime(2025, 12, 31, tzinfo=timezone.utc).timestamp() * 1000)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def utc_year(stamp):
    return datetime.fromtimestamp(stamp / 1000, timezone.utc).year


def valid_ohlc(row):
    p = np.asarray(row[1:5], dtype=float)
    return bool(np.isfinite(p).all() and np.all(p > 0)
                and row[3] >= max(row[1], row[2])
                and row[4] <= min(row[1], row[2]) and row[3] >= row[4])


def validate_clock(rows, step):
    require(rows.ndim == 2 and rows.shape[1] == 6, "OHLCV requires six columns")
    require(np.isfinite(rows[:, 0]).all(), "Invalid timestamps")
    stamps = rows[:, 0].astype(np.int64)
    require(np.array_equal(stamps, rows[:, 0]), "Fractional timestamps")
    require(np.all(stamps % step == 0), "Clock misalignment")
    require(np.all(np.diff(stamps) > 0), "Duplicate or unordered candles")


def aggregate_complete(rows, source_step, target_step):
    """Missing/invalid constituent bars never become a synthetic full candle."""
    validate_clock(rows, source_step)
    require(target_step % source_step == 0, "Nonintegral aggregation")
    expected_count = target_step // source_step
    if not len(rows):
        return np.empty((0, 6))
    keys = rows[:, 0].astype(np.int64) // target_step * target_step
    starts = np.r_[0, np.flatnonzero(np.diff(keys)) + 1]
    ends = np.r_[starts[1:], len(rows)]
    output = []
    for a, b in zip(starts, ends):
        block = rows[a:b]
        opening = int(keys[a])
        if len(block) != expected_count:
            continue
        expected = opening + np.arange(expected_count) * source_step
        if not np.array_equal(block[:, 0], expected):
            continue
        if not all(valid_ohlc(row) for row in block):
            continue
        output.append([opening, block[0, 1], block[-1, 2],
                       np.max(block[:, 3]), np.min(block[:, 4]),
                       np.sum(block[:, 5])])
    return np.asarray(output, dtype=float).reshape((-1, 6))


@dataclass
class PivotState:
    step: int
    scale: str
    bars: deque = field(default_factory=lambda: deque(maxlen=5))
    highs: deque = field(default_factory=lambda: deque(maxlen=2))
    lows: deque = field(default_factory=lambda: deque(maxlen=2))
    events: list = field(default_factory=list)
    last_close: int | None = None

    def feed(self, row):
        closing = int(row[0]) + self.step
        require(self.last_close is None or closing > self.last_close, "Pivot replay")
        self.last_close = closing
        self.bars.append(np.asarray(row).copy())
        if len(self.bars) < 5:
            return
        block = np.asarray(self.bars)
        if not np.all(np.diff(block[:, 0]) == self.step):
            return
        high = bool(block[2, 3] > np.max(block[[0, 1, 3, 4], 3]))
        low = bool(block[2, 4] < np.min(block[[0, 1, 3, 4], 4]))
        if high and low:
            return  # An outside bar does not establish an ordered pair of swings.
        for detected, kind, column, storage in (
                (high, "high", 3, self.highs), (low, "low", 4, self.lows)):
            if detected:
                event = {"scale": self.scale, "kind": kind,
                         "extreme_open": int(block[2, 0]), "confirmed_at": closing,
                         "price": float(block[2, column])}
                require(event["confirmed_at"] == event["extreme_open"] + 3 * self.step,
                        "Two right bars must close before a pivot is known")
                storage.append(event)
                self.events.append(event)

    def snapshot(self):
        direction = "unknown"
        if len(self.highs) == 2 and len(self.lows) == 2:
            h = self.highs[1]["price"] - self.highs[0]["price"]
            l = self.lows[1]["price"] - self.lows[0]["price"]
            direction = "up" if h > 0 and l > 0 else (
                "down" if h < 0 and l < 0 else "range")
        return {"direction": direction, "asof_close": self.last_close,
                "highs": list(self.highs), "lows": list(self.lows)}


def joint_state(daily, intraday):
    if "unknown" in (daily["direction"], intraday["direction"]):
        return "unknown"
    if daily["direction"] == intraday["direction"] == "up":
        return "U"
    if daily["direction"] == intraday["direction"] == "down":
        return "D"
    return "M"


def causal_features(four_hours):
    """Precompute prefix-causal features; no forecast ever uses a later row.

    ATR is Wilder14 seeded by the mean of the first14 true ranges; the first
    true range is high-low. This initialization is explicit and never tuned.
    """
    validate_clock(four_hours, BAR)
    days = aggregate_complete(four_hours, BAR, DAY)
    daily, intra = PivotState(DAY, "1D"), PivotState(BAR, "4h")
    features, day_index, previous, atr = {}, 0, None, None
    seed = []
    previous_open = None
    for row in four_hours:
        now = int(row[0]) + BAR
        # A gap restarts ATR history rather than asserting an unobserved path.
        if previous_open is not None and int(row[0]) != previous_open + BAR:
            previous, atr, seed = None, None, []
        tr = float(row[3] - row[4]) if previous is None else max(
            float(row[3] - row[4]), abs(float(row[3] - previous)),
            abs(float(row[4] - previous)))
        if atr is None:
            seed.append(tr)
            if len(seed) == ATR_PERIOD:
                atr = float(np.mean(seed))
        else:
            atr = ((ATR_PERIOD - 1) * atr + tr) / ATR_PERIOD
        previous, previous_open = float(row[2]), int(row[0])
        intra.feed(row)
        while day_index < len(days) and int(days[day_index, 0]) + DAY <= now:
            daily.feed(days[day_index])
            day_index += 1
        ds, fs = daily.snapshot(), intra.snapshot()
        for snapshot in (ds, fs):
            for event in snapshot["highs"] + snapshot["lows"]:
                require(event["confirmed_at"] <= now, "Future pivot in feature")
        features[now] = {"state": joint_state(ds, fs), "daily": ds, "four_h": fs,
                         "atr": atr, "reference": float(row[2])}
    return features, intra.events + daily.events


@dataclass
class Episode:
    origin: int
    state: str
    reference: float
    atr: float
    baseline: list
    conditional: list
    evidence_n: int
    state_n: int
    structure: dict
    event: str | None = None
    first_event_close: int | None = None
    expected: int = field(init=False)
    seen: int = 0
    complete: bool = True

    def __post_init__(self):
        self.expected = self.origin

    @property
    def deadline(self):
        return self.origin + HORIZON

    def consume(self, row):
        opening = int(row[0])
        if opening < self.origin or opening >= self.deadline:
            return
        if opening != self.expected or not valid_ohlc(row):
            self.complete = False
        self.expected = opening + MINUTE
        self.seen += 1
        if self.event is not None or not valid_ohlc(row):
            return
        upper, lower = self.reference + self.atr, self.reference - self.atr
        if row[1] >= upper:
            event = "up"
        elif row[1] <= lower:
            event = "down"
        elif row[3] >= upper and row[4] <= lower:
            event = "ambiguous"
        elif row[3] >= upper:
            event = "up"
        elif row[4] <= lower:
            event = "down"
        else:
            return
        self.event, self.first_event_close = event, opening + MINUTE

    def status(self, asof, terminal=False):
        if asof < self.deadline:
            require(terminal, "Immature episode cannot enter training")
            return "right_censored", None
        if not self.complete or self.seen != HORIZON // MINUTE or self.expected != self.deadline:
            return "missing_or_invalid", None
        if self.event == "ambiguous":
            return "ambiguous", None
        return "valid", self.event or "none"

    def record(self, status, label):
        return {"origin": self.origin, "deadline": self.deadline, "state": self.state,
                "reference": self.reference, "atr": self.atr,
                "upper": self.reference + self.atr, "lower": self.reference - self.atr,
                "baseline": self.baseline, "conditional": self.conditional,
                "evidence_n": self.evidence_n, "state_n": self.state_n,
                "structure": self.structure, "status": status, "label": label,
                "first_event": self.event, "first_event_close": self.first_event_close,
                "minutes_seen": self.seen, "coverage_complete": self.complete}


class RollingModel:
    def __init__(self):
        self.observations = deque()
        self.global_counts = np.zeros(3, dtype=np.int64)
        self.state_counts = np.zeros((3, 3), dtype=np.int64)

    def expire(self, now):
        while self.observations and self.observations[0][0] < now - WINDOW:
            _, state, label = self.observations.popleft()
            self.global_counts[label] -= 1
            if state in STATES:
                self.state_counts[STATES.index(state), label] -= 1
        require(np.all(self.global_counts >= 0) and np.all(self.state_counts >= 0),
                "Negative rolling counts")

    def predict(self, state, now):
        self.expire(now)
        n = int(self.global_counts.sum())
        p0 = (self.global_counts + 1.0) / (n + 3.0)
        state_n = 0
        ps = p0.copy()
        if state in STATES:
            counts = self.state_counts[STATES.index(state)]
            state_n = int(counts.sum())
            ps = (counts + SHRINK * p0) / (state_n + SHRINK)
        require(np.all(p0 > 0) and np.all(ps > 0), "Probabilities must be positive")
        return p0.tolist(), ps.tolist(), n, state_n

    def learn(self, episode, label, now):
        require(now >= episode.deadline, "Early maturity")
        require(episode.status(now)[0] == "valid", "Only fully observed labels enter training")
        self.expire(now)
        if episode.origin < now - WINDOW:
            return
        k = CLASSES.index(label)
        self.observations.append((episode.origin, episode.state, k))
        self.global_counts[k] += 1
        if episode.state in STATES:
            self.state_counts[STATES.index(episode.state), k] += 1


def losses(probability, label):
    k = CLASSES.index(label)
    p = np.asarray(probability)
    y = np.eye(3)[k]
    return float(np.sum((p - y) ** 2)), -math.log(float(p[k]))


def score_record(record):
    base = {"origin": record["origin"], "state": record["state"],
            "year": utc_year(record["origin"]),
            "midnight_cohort": record["origin"] % DAY == 0, "status": record["status"]}
    if record["status"] == "valid":
        b, l = losses(record["baseline"], record["label"])
        s, t = losses(record["conditional"], record["label"])
        base.update(brier_baseline=b, brier_conditional=s, brier_delta=s - b,
                    logloss_baseline=l, logloss_conditional=t, logloss_delta=t - l)
    elif record["status"] == "ambiguous":
        delta = []
        for label in ("up", "down"):
            b, l = losses(record["baseline"], label)
            s, t = losses(record["conditional"], label)
            delta.append((s - b, t - l))
        base.update(brier_bound_low=min(x[0] for x in delta),
                    brier_bound_high=max(x[0] for x in delta),
                    logloss_bound_low=min(x[1] for x in delta),
                    logloss_bound_high=max(x[1] for x in delta))
    return base


def summarize(records):
    scores = [score_record(r) for r in records]
    groups = {}
    for row in scores:
        keys = ["global", "year:" + str(row["year"]), "state:" + row["state"]]
        if row["midnight_cohort"]:
            keys.append("midnight")
        for key in keys:
            groups.setdefault(key, []).append(row)
    summaries = {}
    for key, rows in groups.items():
        valid = [x for x in rows if x["status"] == "valid"]
        ambiguous = [x for x in rows if x["status"] == "ambiguous"]
        summary = {"count": len(rows), "statuses": dict(Counter(x["status"] for x in rows)),
                   "known_state_count": sum(x["state"] != "unknown" for x in rows)}
        for metric in ("brier", "logloss"):
            for kind in ("baseline", "conditional", "delta"):
                summary[metric + "_" + kind] = (float(np.mean([
                    x[metric + "_" + kind] for x in valid])) if valid else None)
            denominator = len(valid) + len(ambiguous)
            known_delta = sum(x[metric + "_delta"] for x in valid)
            summary[metric + "_ambiguous_inclusive_delta_bounds"] = (
                [(known_delta + sum(x[metric + "_bound_" + side] for x in ambiguous))
                 / denominator for side in ("low", "high")] if denominator else None)
        summaries[key] = summary
    calibration = []
    for model in ("baseline", "conditional"):
        for k, label in enumerate(CLASSES):
            buckets = [[] for _ in range(5)]
            for record in records:
                if record["status"] == "valid":
                    probability = record[model][k]
                    buckets[min(4, int(probability * 5))].append(
                        (probability, int(record["label"] == label)))
            for index, bucket in enumerate(buckets):
                calibration.append({"model": model, "class": label, "bin": index,
                                    "count": len(bucket),
                                    "mean_probability": float(np.mean([x[0] for x in bucket])) if bucket else None,
                                    "observed_frequency": float(np.mean([x[1] for x in bucket])) if bucket else None})
    return {"groups": summaries, "calibration": calibration,
            "iid_inference": False, "trading": False}, scores


def observe(minutes, start, finish):
    """Pure chronological simulation; loading and artifact writing are separate."""
    validate_clock(minutes, MINUTE)
    require(start < finish <= FINISH, "2026 reserved")
    require(start % BAR == finish % BAR == 0, "Evaluation requires4h UTC boundaries")
    require(len(minutes) and int(minutes[-1, 0]) < finish, "Input reaches beyond exclusive cutoff")
    four_hours = aggregate_complete(minutes, MINUTE, BAR)
    features, pivots = causal_features(four_hours)
    model, pending, records = RollingModel(), [], []
    emitted, invalid_atr, observed_slots, missing_four_h = 0, 0, 0, 0
    for minute in minutes:
        now = int(minute[0]) + MINUTE
        if now < start:
            continue
        for episode in pending:
            episode.consume(minute)
        matured = [e for e in pending if e.deadline <= now]
        pending = [e for e in pending if e.deadline > now]
        for episode in matured:
            status, label = episode.status(now)
            records.append(episode.record(status, label))
            if status == "valid":
                model.learn(episode, label, now)
        if now >= finish or now % BAR != 0:
            continue
        observed_slots += 1
        if now not in features:
            missing_four_h += 1
            continue
        f = features[now]
        atr = f["atr"]
        if atr is None or not math.isfinite(atr) or not 0 < atr < f["reference"]:
            invalid_atr += 1
            continue
        require(math.isclose(f["reference"], float(minute[2]), rel_tol=1e-10, abs_tol=1e-8),
                "M1/4h decision quote mismatch")
        p0, ps, n, state_n = model.predict(f["state"], now)
        pending.append(Episode(now, f["state"], f["reference"], atr, p0, ps, n,
                               state_n, {"daily": f["daily"], "four_h": f["four_h"]}))
        emitted += 1
    for episode in pending:
        status, label = episode.status(finish, terminal=True)
        records.append(episode.record(status, label))
    records.sort(key=lambda r: r["origin"])
    require(len(records) == emitted, "Episode accounting mismatch")
    summary, scores = summarize(records)
    summary["decision_clock"] = {"emitted": emitted, "invalid_atr": invalid_atr,
                                  "start": start, "finish_exclusive": finish,
                                  "retained_training_labels": len(model.observations),
                                  "expected_decision_slots": (finish - start) // BAR,
                                  "observed_boundary_minutes": observed_slots,
                                  "missing_boundary_minutes": (finish - start) // BAR - observed_slots,
                                  "missing_complete_4h": missing_four_h}
    return records, pivots, scores, summary


def write_artifacts(directory, records, pivots, scores, summary, manifest):
    """Only called with a fresh directory below this script's output folder."""
    root = Path(__file__).resolve().parent / "output"
    target = root / directory
    require(target.parent == root and directory not in ("", ".", ".."), "Unsafe output name")
    target.mkdir(parents=True, exist_ok=False)
    def table(name, rows):
        keys = sorted({key for row in rows for key in row})
        with (target / name).open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=keys)
            writer.writeheader()
            for row in rows:
                writer.writerow({key: json.dumps(value, sort_keys=True, allow_nan=False)
                                 if isinstance(value, (dict, list)) else value
                                 for key, value in row.items()})
    table("forecasts_labels.csv", records)
    table("pivots.csv", pivots)
    table("scores.csv", scores)
    for name, value in (("summary.json", summary), ("manifest.json", manifest)):
        (target / name).write_text(json.dumps(value, indent=2, sort_keys=True,
                                             allow_nan=False), encoding="utf-8")
    return str(target)


def candle(stamp, opening=100.0, close=100.0, high=100.5, low=99.5):
    return np.asarray([stamp, opening, close, high, low, 1.0])


def self_test():
    checks = []
    pivot = PivotState(BAR, "4h")
    highs = [2, 3, 5, 4, 3]
    for j in range(4):
        pivot.feed(candle(j * BAR, 1, 1, highs[j], 0.5))
    require(not pivot.events, "Pivot visible before two right bars")
    pivot.feed(candle(4 * BAR, 1, 1, highs[4], 0.5))
    require(pivot.highs[0]["confirmed_at"] == 5 * BAR, "Wrong pivot confirmation")
    checks.append("two_right_bars_no_early_pivot")
    tied = PivotState(BAR, "4h")
    for j, high in enumerate([2, 3, 5, 5, 3]):
        tied.feed(candle(j * BAR, 1, 1, high, 0.5))
    require(not tied.events, "Tied extrema must not become pivots")
    checks.append("ties_are_not_pivots")
    outside = PivotState(BAR, "4h")
    for j, high in enumerate([2, 3, 5, 4, 3]):
        outside.feed(candle(j * BAR, 1, 1, high, 0.1 if j == 2 else 0.5))
    require(not outside.events, "Outside high/low pair must stay ambiguous")
    checks.append("outside_pivot_pair_not_ordered")
    require(joint_state({"direction": "up"}, {"direction": "up"}) == "U", "Up agreement")
    require(joint_state({"direction": "down"}, {"direction": "down"}) == "D", "Down agreement")
    require(joint_state({"direction": "up"}, {"direction": "down"}) == "M", "Mixed state")
    require(joint_state({"direction": "unknown"}, {"direction": "up"}) == "unknown", "Unknown coverage")
    checks.append("three_known_states_and_explicit_unknown")
    p0 = [1 / 3] * 3
    make = lambda: Episode(0, "unknown", 100, 1, p0, p0, 0, 0, {})
    amb = make()
    amb.consume(candle(0, 100, 100, 101, 99))
    require(amb.event == "ambiguous", "Invented intraminute barrier ordering")
    gap = make()
    gap.consume(candle(0, 102, 100, 102, 98))
    require(gap.event == "up", "Opening outside barrier must resolve first")
    checks.append("ambiguous_touch_and_known_opening_order")
    model = RollingModel()
    try:
        model.learn(gap, "up", HORIZON - 1)
        raise AssertionError("Accepted immature label")
    except AssertionError as exc:
        require(str(exc) == "Early maturity", "Unexpected maturation assertion")
    require(model.global_counts.sum() == 0, "Early outcome leaked into training")
    for j in range(1, 1440):
        gap.consume(candle(j * MINUTE))
    model.learn(gap, "up", HORIZON)
    b, s, n, _ = model.predict("unknown", HORIZON)
    require(b == s and n == 1, "Unknown must emit unconditional and remain scored")
    model.expire(WINDOW + 1)
    require(model.global_counts.sum() == 0, "Window expiry counts mismatch")
    checks.extend(["deadline_maturity_only", "unknown_equals_baseline", "calendar_window_expiry"])
    complete = make()
    for j in range(1440):
        complete.consume(candle(j * MINUTE))
    require(complete.status(DAY) == ("valid", "none"), "Wrong no-barrier outcome")
    require(complete.status(DAY - 1, terminal=True)[0] == "right_censored", "Censor leak")
    missing = make()
    for j in range(1440):
        if j != 600:
            missing.consume(candle(j * MINUTE))
    require(missing.status(DAY)[0] == "missing_or_invalid", "Gap must invalidate horizon")
    checks.extend(["complete_none_and_terminal_censor", "missing_minute_invalidates"])
    rows = np.asarray([candle(j * MINUTE) for j in range(240)])
    require(len(aggregate_complete(rows, MINUTE, BAR)) == 1, "Complete4h missing")
    require(len(aggregate_complete(np.delete(rows, 20, axis=0), MINUTE, BAR)) == 0,
            "Incomplete4h fabricated")
    four = np.asarray([candle(j * BAR, 100, 100, 101, 99) for j in range(60)])
    prefix, _ = causal_features(four[:40])
    full, _ = causal_features(four)
    require(all(prefix[t] == full[t] for t in prefix), "Future bars revised old features")
    require(math.isclose(full[60 * BAR]["atr"], 2.0), "Wilder ATR fixture")
    checks.extend(["aggregation_requires_contiguity", "prefix_causal_features"])
    scored = complete.record("valid", "none")
    row = score_record(scored)
    require(row["brier_delta"] == row["logloss_delta"] == 0.0, "Paired score equality")
    checks.append("paired_scoring_identity")
    return {"self_tests_passed": checks, "database_read": False,
            "network": False, "trading": False, "provisional_adapter": True}


def describe_api():
    # Lazy import keeps synthetic tests free of DB API imports and side effects.
    research = importlib.import_module("jesse.research")
    function = research.get_candles
    return {"public_api": "jesse.research.get_candles",
            "signature": str(inspect.signature(function)), "doc": inspect.getdoc(function),
            "database_query_performed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--self-test", action="store_true")
    mode.add_argument("--describe-api", action="store_true")
    args = parser.parse_args()
    result = describe_api() if args.describe_api else self_test()
    sys.stdout.write(json.dumps(result, sort_keys=True, allow_nan=False) + "\n")


if __name__ == "__main__":
    main()
