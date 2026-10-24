import math

import numpy as np
from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def passage_anchor(now, price, atr):
    """Guard absolute barriers physically; no buffer or outcome-based repair."""
    if atr is None or not all(math.isfinite(v) for v in (price, atr)):
        return None
    lower, upper = price - 2*atr, price + 2*atr
    if not (price > 0 and atr > 0 and math.isfinite(lower)
            and math.isfinite(upper) and lower > 0 and upper > 0):
        return None
    return dict(a=float(price), d=float(atr), t0=int(now), s=0, t1=None)


def passage_machine(anchor, now, price, atr):
    """One close, at most one passage; current ATR cannot erase old frozen d."""
    if anchor is None:
        new = passage_anchor(now, price, atr)
        return new, None, "seed" if new is not None else "anchor_invalid"
    assert now > anchor["t0"]
    a, d = anchor["a"], anchor["d"]
    if anchor["t1"] is None:
        sign = 1 if price >= a+d else -1 if price <= a-d else 0
        if not sign:
            return anchor, None, "wait_first"
        if sign*(price-a) >= 2*d:
            # No invented intermediate timestamp or same-close new first passage.
            return passage_anchor(now, price, atr), None, "degenerate"
        return dict(anchor, s=sign, t1=int(now)), None, "first"
    assert now > anchor["t1"]
    z = anchor["s"]*(price-a)
    if 0 < z < 2*d:
        return anchor, None, "wait_second"
    kind = "REV" if z <= 0 else "CONT"
    r = -anchor["s"] if kind == "REV" else anchor["s"]
    u, v = anchor["t1"]-anchor["t0"], now-anchor["t1"]
    assert u > 0 and v > 0
    event = dict(type=kind, fast=bool(v < u), r=int(r), t0=anchor["t0"],
                 t1=anchor["t1"], t2=int(now), a=a, d=d, u=int(u), v=int(v),
                 entry=float(price))
    return passage_anchor(now, price, atr), event, "event"


def passage_model():
    return dict(anchor=None, last=None, pending=[], bank=[])


def passage_advance(model, now, price, atr):
    """Mature before observing today's event. No orders/occupancy/model mode."""
    assert math.isfinite(price) and price > 0
    reset = model["last"] is not None and now != model["last"]+BAR
    if reset:
        model.clear()
        model.update(passage_model())
    matured = 0
    remaining = []
    for pending in model["pending"]:
        age = now-pending["t2"]
        assert age > 0 and age % BAR == 0 and age <= 6*BAR
        if age == 6*BAR:
            y = pending["r"]*(math.log(price)-math.log(pending["entry"]))
            assert math.isfinite(y)
            model["bank"].append(dict(type=pending["type"], fast=pending["fast"],
                                      y=float(y), t2=pending["t2"], matured=int(now)))
            if len(model["bank"]) > 240:
                model["bank"].pop(0)
            matured += 1
        else:
            remaining.append(pending)
    model["pending"] = remaining
    # This call is deliberately AFTER maturation and independent of atr validity.
    model["anchor"], event, action = passage_machine(model["anchor"], now, price, atr)
    if event is not None:
        model["pending"].append(dict(event))
    model["last"] = int(now)
    return event, dict(action=action, matured=matured, gap_reset=bool(reset),
                       reset_anchor_invalid=model["anchor"] is None)


def passage_bootstrap(rows):
    """Exactly1000 closed rows, row14 seed; replay once, never submit a trade."""
    assert len(rows) == 1000
    model, counts = passage_model(), {}
    for j in range(14, 1000):
        now = int(rows[j, 0])+BAR
        atr = atr14(rows[j-14:j+1])
        event, info = passage_advance(model, now, float(rows[j, 2]), atr)
        counts[info["action"]] = counts.get(info["action"], 0)+1
        counts["matured"] = counts.get("matured", 0)+info["matured"]
        counts["bars"] = counts.get("bars", 0)+1
        if event is not None:
            cell = event["type"]+("_FAST" if event["fast"] else "_SLOW")
            counts[cell] = counts.get(cell, 0)+1
            counts["ties"] = counts.get("ties", 0)+int(event["u"] == event["v"])
    return model, counts


def passage_forecasts(bank, event):
    """The SAME complete240 bank/shared20-cell domain for both conditional means."""
    if len(bank) != 240:
        return None
    cell = [item["y"] for item in bank
            if item["type"] == event["type"] and item["fast"] == event["fast"]]
    group = [item["y"] for item in bank if item["type"] == event["type"]]
    if len(cell) < 20 or not all(math.isfinite(v) for v in group):
        return None
    state, by_type = float(np.mean(cell)), float(np.mean(group))
    if not all(math.isfinite(v) for v in (state, by_type)):
        return None
    return dict(state_mean=state, type_mean=by_type, cell_n=len(cell), type_n=len(group),
                bank_first=bank[0]["t2"], bank_last=bank[-1]["t2"])


class BtcResearchR23PassageBase1m(BtcResearchR12ArBase1m):
    MODE = "abstract"

    def _passage_count(self, name, amount=1):
        stats = self.vars.setdefault("passage_runtime_counts", {})
        stats[name] = stats.get(name, 0)+amount

    def _passage_reset(self, reason):
        # A market-data discontinuity discards all predictive history. This is
        # NOT a second bootstrap and cannot cancel broker stops/time exits.
        self.vars["passage_model"] = passage_model()
        self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
        self._passage_count("invalid:"+reason)

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("STATE", "TYPE_CONTROL")
            self.vars["checked"] = True
            self._log("R23_PASSAGE_CONFIG", dict(mode=self.MODE, bootstrap_rows=1000,
                      seed_row=14, bank=240, cell_min=20, horizon_hours=24,
                      stop_atr=2, target=None, risk=.02, aggregate=.06,
                      leverage=3, fee=.00045, feature="observed_type_fast_not_pure_speed"))
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR or now > self.FINISH:
            return
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        if not self.vars.get("passage_bootstrapped"):
            rows = closed_window(candles, now, 1000)
            if (rows is None or not np.all(rows[:, 0] % BAR == 0)
                    or not math.isclose(float(rows[-1, 2]), float(self.price),
                                        rel_tol=1e-10, abs_tol=1e-8)):
                self._passage_count("bootstrap_wait")
                return
            model, counts = passage_bootstrap(rows)
            self.vars["passage_model"] = model
            self.vars["passage_bootstrap_counts"] = counts
            self.vars["passage_bootstrapped"] = True
            self.vars["passage_initialized_at"] = now
            self._log("R23_PASSAGE_BOOTSTRAP", dict(time=now, counts=counts,
                      bank=len(model["bank"]), pending=len(model["pending"])))
            # The last replay event is mathematical, never a queued first trade.
            return
        rows = closed_window(candles, now, 15)
        if rows is None or not np.all(rows[:, 0] % BAR == 0):
            self._passage_reset("ohlc_or_clock")
            return
        if not math.isclose(float(rows[-1, 2]), float(self.price),
                            rel_tol=1e-10, abs_tol=1e-8):
            self._passage_reset("asof_price")
            return
        model = self.vars["passage_model"]
        atr = atr14(rows)
        # ATR0/None blocks ONLY new anchor/order; old pending and frozen-d phase
        # still advance on this valid close. Never return before this call.
        event, info = passage_advance(model, now, float(rows[-1, 2]), atr)
        self._passage_count("bars")
        self._passage_count(info["action"])
        self._passage_count("matured", info["matured"])
        self._passage_count("gap_reset", int(info["gap_reset"]))
        if event is None:
            return
        self._passage_count(event["type"]+("_FAST" if event["fast"] else "_SLOW"))
        self._passage_count("ties", int(event["u"] == event["v"]))
        forecasts = passage_forecasts(model["bank"], event)
        if forecasts is None:
            self._passage_count("insufficient_bank_or_cell")
            return
        mean = forecasts["state_mean"] if self.MODE == "STATE" else forecasts["type_mean"]
        score = event["r"]*mean
        if abs(score) <= .0019 or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        if atr is None:
            self._passage_count("entry_atr_invalid")
            return
        direction = 1 if score > 0 else -1
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = direction
        self.vars["passage_evidence"] = dict(event=event, score=score, **forecasts)

    def on_open_position(self, order):
        super().on_open_position(order)
        entry = float(self.position.entry_price)
        direction = 1 if self.is_long else -1
        opened = int(self.position.opened_at)
        evidence = self.vars["passage_evidence"]
        self._log("R23_PASSAGE_OPEN", dict(mode=self.MODE, time=int(self.time),
                  entry=entry, actual_stop=entry-direction*self.vars["plan"]["distance"],
                  actual_opened=opened, position_deadline=opened+6*BAR,
                  label_deadline=evidence["event"]["t2"]+6*BAR,
                  evidence=evidence))

    def _emit(self, stage):
        super()._emit(stage)
        model = self.vars.get("passage_model", passage_model())
        cells = {kind+("_FAST" if fast else "_SLOW"): sum(
                    item["type"] == kind and item["fast"] == fast for item in model["bank"])
                 for kind in ("REV", "CONT") for fast in (False, True)}
        anchor = model["anchor"]
        self._log("R23_PASSAGE_STATS", dict(stage=stage, mode=self.MODE,
                  initialized=self.vars.get("passage_initialized_at"),
                  bootstrap=self.vars.get("passage_bootstrap_counts", {}),
                  runtime=self.vars.get("passage_runtime_counts", {}),
                  bank=len(model["bank"]), cells=cells, pending=len(model["pending"]),
                  last=model["last"],
                  terminal_censored_labels=len(model["pending"]) if int(self.time) >= self.FINISH else 0,
                  incomplete_episode=anchor is not None,
                  first_passage_seen=bool(anchor is not None and anchor["t1"] is not None)))
