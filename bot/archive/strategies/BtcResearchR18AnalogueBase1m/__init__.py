import math
import numpy as np
from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def analogue_sample(rows):
    """360 mature origins in a fixed372-bar window; no future labels or padding."""
    logs = np.log(rows[-372:, 2])
    assert len(logs) == 372
    returns = np.diff(logs)
    origins = np.arange(6, 366, dtype=int)
    # Return index j links close j to close j+1. Origin i therefore uses i-6:i.
    vectors = returns[origins[:, None]-6+np.arange(6)]
    labels = logs[origins+6]-logs[origins]
    norms = np.linalg.norm(vectors, axis=1)
    current = returns[-6:]
    current_norm = float(np.linalg.norm(current))
    if not np.all(np.isfinite(current)) or not math.isfinite(current_norm) or current_norm <= 0:
        return None
    valid = (np.all(np.isfinite(vectors), axis=1) & np.isfinite(norms)
             & (norms > 0) & np.isfinite(labels))
    origins, vectors, norms, labels = origins[valid], vectors[valid], norms[valid], labels[valid]
    if len(origins) < 20:
        return None
    return dict(origins=origins, vectors=vectors/norms[:, None],
                labels=labels, current=current/current_norm)


def analogue_forecast(rows, nearest):
    """Fixed top20 cosine mean versus all valid labels; exact ties prefer older."""
    sample = analogue_sample(rows)
    if sample is None:
        return None, None
    origins, labels = sample["origins"], sample["labels"]
    cosine = sample["vectors"] @ sample["current"]
    if not np.all(np.isfinite(cosine)):
        return None, None
    # Origins arrive oldest first; stable sorting preserves that order on ties.
    order = np.argsort(-cosine, kind="stable")
    chosen = order[:20] if nearest else np.arange(len(origins))
    forecast = float(np.mean(labels[chosen]))
    if not math.isfinite(forecast):
        return None, None
    evidence = dict(valid_origins=len(origins), selected=len(chosen),
                    first_origin=int(origins[0]), last_origin=int(origins[-1]),
                    chosen_origins=[int(x) for x in origins[chosen]] if nearest else None,
                    best_cosine=float(cosine[order[0]]),
                    twentieth_cosine=float(cosine[order[19]]),
                    forecast=forecast)
    return forecast, evidence


class BtcResearchR18AnalogueBase1m(BtcResearchR12ArBase1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("KNN", "GLOBAL")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 372)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        forecast, evidence = analogue_forecast(rows, self.MODE == "KNN")
        # The inherited .0019 hurdle is a signal rule, never an extra PnL debit.
        if forecast is None or abs(forecast) <= .0019 or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        direction = 1 if forecast > 0 else -1
        atr = atr14(rows)
        if atr is None:
            return
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            return
        self.vars["plan"] = dict(plan, analogue=dict(evidence))
        self.vars["direction"] = direction

    def on_open_position(self, order):
        # Parent supplies actual-fill stop, no TP, risk check and24h clock.
        super().on_open_position(order)
        direction = 1 if self.is_long else -1
        key = "long_fills" if direction == 1 else "short_fills"
        self.vars[key] = self.vars.get(key, 0)+1
        self._log("R18_ANALOGUE_OPEN", dict(time=int(self.time), mode=self.MODE,
            direction=direction, evidence=self.vars["plan"]["analogue"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R18_ANALOGUE_STATS", dict(stage=stage, mode=self.MODE,
            long_fills=self.vars.get("long_fills", 0),
            short_fills=self.vars.get("short_fills", 0),
            signals=self.vars.get("signals", 0), occupied=self.vars.get("occupied", 0)))
