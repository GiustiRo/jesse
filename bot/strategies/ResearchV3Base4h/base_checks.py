import math
from types import SimpleNamespace

import numpy as np

from strategies.ResearchV3Base4h import ResearchV3Base4h, closed_window, v3_entry_plan, BAR


class StopSurface:
    """Public strategy surface only; this fake never simulates fills or broker PnL."""
    def __init__(self, direction):
        self.is_long = direction == 1
        self.price = 100.
        self.time = 1000000
        self.position = SimpleNamespace(qty=direction * 2.)
        self.vars = {"v3_trade": {"stop_price": 95. if direction == 1 else 105.}}
        self.stop_loss = None
        self.events = []

    def request_exit(self, reason):
        self.events.append(reason)

    def _log_json(self, label, payload):
        self.events.append(label)


class ExitSurface:
    def __init__(self):
        self.is_open = True
        self.time = 1000000
        self.vars = {}
        self.exits = 0

    def _log_json(self, label, payload):
        pass

    def liquidate(self):
        self.exits += 1


def self_checks():
    count = 0
    def check(value):
        nonlocal count
        assert value
        count += 1

    rows = np.array([[i * BAR, 100., 100., 101., 99., 1.] for i in range(150)])
    now = 144 * BAR
    check(len(closed_window(rows, now, 144)) == 144)
    changed = rows.copy()
    changed[changed[:, 0] + BAR > now, 1:5] = np.nan
    check(np.array_equal(closed_window(changed, now, 144), closed_window(rows[:144], now, 144)))
    gap = np.delete(rows, 30, axis=0)
    check(closed_window(gap, now, 144) is None)
    check(closed_window(rows[:143], now, 144) is None)
    for direction in (-1, 1):
        plan = v3_entry_plan(100., 10000., .00045, direction, 2.)
        unit = 2 + .00045 * (200 - direction * 2)
        check(plan["qty"] == math.floor(200 / unit * 1e8) / 1e8)
        check(plan["qty"] * unit <= 200.)
        check(v3_entry_plan(100., 10000., .00045, direction, .01)["qty"] == 100.)
        check(v3_entry_plan(100., 1e-12, .00045, direction, 2.)["reason"] == "qty_invalid")
        fake = StopSurface(direction)
        old = fake.vars["v3_trade"]["stop_price"]
        ResearchV3Base4h.replace_stop(fake, old - direction)
        check(fake.stop_loss is None and not fake.events)
        ResearchV3Base4h.replace_stop(fake, old + direction)
        check(fake.stop_loss == (2., old + direction))
        ResearchV3Base4h.replace_stop(fake, 100 + direction)
        check(fake.events[-1] == "trailing_crossed_at_decision")
        check(fake.vars["v3_trade"]["stop_price"] == old + direction)
        check(ResearchV3Base4h._target_valid(110 if direction == 1 else 90, 100, direction))
        check(not ResearchV3Base4h._target_valid(90 if direction == 1 else 110, 100, direction))
    fake = ExitSurface()
    ResearchV3Base4h.request_exit(fake, "one")
    ResearchV3Base4h.request_exit(fake, "two")
    check(fake.exits == 1 and fake.vars["exit_reason"] == "one")
    fake.time += BAR
    ResearchV3Base4h.request_exit(fake, "next")
    check(fake.exits == 2 and fake.vars["exit_reason"] == "next")
    check(v3_entry_plan(100., 10000., .00045, 1, 100.)["reason"] == "distance_invalid")
    check(ResearchV3Base4h._target_valid(None, 100., 1))
    return dict(status="passed", assertions=count)
