import math
from collections import Counter
import numpy as np
from jesse.strategies import Strategy

MINUTE = 60000
BAR = 14400000
DAY = 86400000
BASE_COLUMNS = ["intercept"] + ["age"+str(age) for age in range(2, 12)] + ["side", "progress"]


def stop_event(side, stop, m1):
    """Independent unit shadow: last closed M1 touch, adverse open gap, no TP."""
    assert side in (-1, 1)
    touched = float(m1[4]) <= stop if side == 1 else float(m1[3]) >= stop
    if not touched:
        return None
    price = min(float(m1[1]), stop) if side == 1 else max(float(m1[1]), stop)
    return dict(exit_time=int(m1[0])+MINUTE, exit_price=price, reason="STOP")


def review_features(side, entry, D, previous_mark, bestR, mark, age):
    """Only already observed 4h closing marks update bestR; no high/low extrema."""
    assert side in (-1, 1) and 1 <= age <= 11 and D > 0
    progress = side*(mark-entry)/D
    best = max(0., bestR, progress)
    result = dict(side=int(side), age=int(age), progress=float(progress),
                  recent=float(side*(mark-previous_mark)/D),
                  giveback=float(best-progress), bestR=float(best))
    assert all(math.isfinite(float(value)) for value in result.values())
    return result


def merge_registry(registry, incoming, now, exchange, symbol):
    """Pure public-history ingestion; registry is insertion-ordered effective->row.

    Incoming rows expose settled_at, not effective_at; boundary jitter is retained.
    Every later causal window must overlap the previous most recent event.
    """
    assert isinstance(incoming, list) and 0 < len(incoming) <= 16, "R46_FUND_WINDOW_EMPTY"
    normalized = []
    previous = None
    for source in incoming:
        assert source["exchange"] == exchange and source["symbol"] == symbol
        settled = int(source["settled_at"])
        effective = settled-settled % MINUTE
        available = int(source["available_at"])
        assert 0 <= settled-effective <= 1000
        assert available == effective+MINUTE and available <= now
        assert previous is None or effective > previous, "R46_FUND_WINDOW_ORDER"
        previous = effective
        rate, mark = float(source["rate_decimal"]), float(source["mark_price"])
        assert math.isfinite(rate) and math.isfinite(mark) and mark > 0
        normalized.append(dict(exchange=exchange, symbol=symbol, settled_at=settled,
            effective_at=effective, available_at=available, rate_decimal=rate,
            mark_price=mark, mark_price_source=source["mark_price_source"]))
    if registry:
        last = next(reversed(registry))
        assert any(row["effective_at"] == last for row in normalized), "R46_FUND_OVERLAP_LOST"
    updated, fresh = dict(registry), []
    for row in normalized:
        key = row["effective_at"]
        if key in updated:
            assert updated[key] == row, "R46_FUND_CONFLICT"
        else:
            assert not updated or key > next(reversed(updated)), "R46_FUND_REGRESSION"
            updated[key] = row
            fresh.append(row)
    return updated, fresh


def label_value(side, mark, exit_price, D, fee, events,
                node_time, exit_time, exit_kind, finish):
    """Incremental cashflow per D: entry fees and funding through node_time are sunk.

    events may be a causal registry slice; the caller separately proves its
    relative completeness via overlap and the target+1m ingestion.
    """
    assert side in (-1, 1) and D > 0 and exit_time > node_time
    assert exit_kind in ("STOP", "horizon", "deadline")
    included = [row for row in events
        if node_time < row["effective_at"] < finish
        and (row["effective_at"] < exit_time if exit_kind == "STOP"
             else row["effective_at"] <= exit_time)]
    funding = -side*sum(row["mark_price"]*row["rate_decimal"] for row in included)
    price_component = side*(exit_price-mark)
    fee_component = fee*(mark-exit_price)
    delta = (price_component+fee_component+funding)/D
    assert all(math.isfinite(x) for x in (funding, price_component, fee_component, delta))
    return dict(price_component=float(price_component), fee_component=float(fee_component),
                funding=float(funding), delta=float(delta),
                funding_effectives=[row["effective_at"] for row in included])


def design_vector(row, context=False):
    """13-column shared control; context appends only recent and giveback."""
    age = int(row["age"])
    assert 1 <= age <= 11 and row["side"] in (-1, 1)
    values = [1.] + [float(age == value) for value in range(2, 12)]
    values += [float(row["side"]), float(row["progress"])]
    if context:
        values += [float(row["recent"]), float(row["giveback"])]
    return np.asarray(values, dtype=float)


def weighted_ridge(rows, context=False):
    """Origin-day mass1, weights rescaled to mean1; lambda1, no target scaling."""
    N = len(rows)
    assert N > 0
    day_counts = Counter(int(row["origin"]) for row in rows)
    days = len(day_counts)
    weights = np.array([N/(days*day_counts[int(row["origin"])]) for row in rows])
    X = np.array([design_vector(row, context) for row in rows])
    y = np.array([float(row["delta"]) for row in rows])
    assert np.all(np.isfinite(X)) and np.all(np.isfinite(y))
    means, scales = np.zeros(X.shape[1]), np.ones(X.shape[1])
    constant = np.zeros(X.shape[1], dtype=bool)
    transformed = X.copy()
    for j in range(1, X.shape[1]):
        if np.ptp(X[:, j]) == 0:
            means[j], scales[j], constant[j] = X[0, j], 1., True
            transformed[:, j] = 0.
        else:
            means[j] = np.sum(weights*X[:, j])/np.sum(weights)
            scales[j] = math.sqrt(float(np.sum(weights*(X[:, j]-means[j])**2)/np.sum(weights)))
            assert math.isfinite(scales[j]) and scales[j] > 0
            transformed[:, j] = (X[:, j]-means[j])/scales[j]
    penalty = np.eye(X.shape[1])
    penalty[0, 0] = 0.
    beta = np.linalg.solve(transformed.T@(weights[:, None]*transformed)+penalty,
                           transformed.T@(weights*y))
    assert np.all(np.isfinite(beta)) and np.all(np.isfinite(means)) and np.all(np.isfinite(scales))
    return dict(context=bool(context), columns=BASE_COLUMNS+(["recent", "giveback"] if context else []),
                means=means, scales=scales, constant=constant, beta=beta, N=N,
                days=days, weights_sum=float(weights.sum()),
                day_counts=sorted(day_counts.items()))


def fit_window(bank, fit_time):
    """Last180 origin DAYS mature at48h+1m, no filling older valid observations.

    bank[origin]={origin,valid,released,release_at,nodes}; each node is a mature
    row with origin/side/age/progress/recent/giveback/delta/ready.
    """
    latest = ((fit_time-2*DAY-MINUTE)//DAY)*DAY
    wanted = [latest-i*DAY for i in range(179, -1, -1)]
    episodes = [bank.get(day) for day in wanted]
    if any(episode is None for episode in episodes):
        return None, "missing_180_origin_days"
    if any(not e["released"] or e["release_at"] > fit_time for e in episodes):
        return None, "origin_days_not_mature"
    if any(not e["valid"] for e in episodes):
        return None, "invalid_origin_day_in_window"
    rows = [node for episode in episodes for node in episode["nodes"]]
    assert all(node["mature"] and node["ready"] <= fit_time for node in rows)
    if len(rows) < 360:
        return None, "fewer_than_360_nodes"
    counts = Counter(int(node["age"]) for node in rows)
    if any(counts[age] < 20 for age in range(1, 12)):
        return None, "age_support_below_20"
    return dict(control=weighted_ridge(rows, False), context=weighted_ridge(rows, True),
                day_ids=wanted, age_counts={age:counts[age] for age in range(1, 12)},
                origin_episodes=360), None


def predict(model, row):
    vector = design_vector(row, model["context"])
    transformed = (vector-model["means"])/model["scales"]
    transformed[0] = 1.
    transformed[model["constant"]] = 0.
    value = float(transformed@model["beta"])
    assert math.isfinite(value)
    return value


class BtcResearchR46ContinuationMath(Strategy):
    """Importable pure helper container, never an economic strategy."""
    def should_long(self):
        return False

    def should_short(self):
        return False

    def go_long(self):
        raise AssertionError("R46 math has no orders")

    def go_short(self):
        raise AssertionError("R46 math has no orders")
