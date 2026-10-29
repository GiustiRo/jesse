# O: código completo del check sintético previo

Sin inputs económicos reales; AST de fuentes suministradas y stubs de hooks. No valida fills del motor. Código enviado exactamente a run_analysis:

```python
import ast
import hashlib
import json
import math
from datetime import datetime, timezone
from types import SimpleNamespace
from pathlib import Path

import numpy as np

SOURCES = {"BtcResearchR15PathBase1m":"import math\nimport numpy as np\n\nfrom strategies.BtcResearchR11Base1m import BtcResearchR11Base1m\nfrom strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan\n\nDAY = 86400000\n\n\ndef day_path(rows):\n    \"\"\"Pure daily path label; reject extrema whose order is unidentified.\"\"\"\n    if rows.ndim != 2 or rows.shape[1] < 5 or len(rows) < 6:\n        return None\n    block = rows[-6:]\n    # Volume is deliberately unused in both policies. A forming or displaced\n    # day is never relabelled by shifting the six-bar window.\n    if not np.all(np.isfinite(block[:, :5])):\n        return None\n    times = block[:, 0]\n    start = float(times[0])\n    if start % DAY != 0 or not np.array_equal(times, start + np.arange(6) * BAR):\n        return None\n    if np.any(block[:, 1:5] <= 0):\n        return None\n    if (np.any(block[:, 3] < np.maximum(block[:, 1], block[:, 2]))\n            or np.any(block[:, 4] > np.minimum(block[:, 1], block[:, 2]))):\n        return None\n    opening, close = float(block[0, 1]), float(block[-1, 2])\n    if close == opening:\n        return None\n    highs = np.flatnonzero(block[:, 3] == np.max(block[:, 3]))\n    lows = np.flatnonzero(block[:, 4] == np.min(block[:, 4]))\n    # Do not resolve ties by a favorable first/last occurrence, or infer the\n    # high/low order inside the same four-hour bar.\n    if len(highs) != 1 or len(lows) != 1 or highs[0] == lows[0]:\n        return None\n    high_index, low_index = int(highs[0]), int(lows[0])\n    direction = 1 if close > opening else -1\n    repair = ((direction == 1 and high_index < low_index)\n              or (direction == -1 and low_index < high_index))\n    return dict(direction=direction, repair=bool(repair),\n                label=\"repair\" if repair else \"body_only\",\n                high_index=high_index, low_index=low_index)\n\n\nclass BtcResearchR15PathBase1m(BtcResearchR11Base1m):\n    MODE = \"abstract\"\n\n    def before(self):\n        now = int(self.time)\n        if not self.vars.get(\"checked\"):\n            assert self.symbol == \"BTC-USDT\" and self.timeframe == \"1m\"\n            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12\n            assert abs(self.balance-10000) < 1e-6\n            self.vars[\"checked\"] = True\n        self._observe(\"pre\")\n        self.vars[\"direction\"] = 0\n        # A UTC data-aggregation clock on continuous BTC, not market hours.\n        if now % DAY:\n            return\n        rows = closed_window(self.get_candles(self.exchange, self.symbol, \"4h\"), now, 15)\n        if rows is None:\n            self.vars[\"invalid_windows\"] = self.vars.get(\"invalid_windows\", 0)+1\n            return\n        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)\n        assert self.MODE in (\"REPAIR\", \"BODY\")\n        event = day_path(rows)\n        if event is None:\n            return\n        if not self.START < now < self.FINISH:\n            return\n        counts = self.vars.setdefault(\"day_path_counts\", {\"repair\": 0, \"body_only\": 0})\n        counts[event[\"label\"]] += 1\n        if self.MODE == \"REPAIR\" and not event[\"repair\"]:\n            return\n        self.vars[\"signals\"] = self.vars.get(\"signals\", 0)+1\n        if self.is_open or self.entry_orders or self.vars.get(\"last_exit_at\") == now:\n            self.vars[\"occupied\"] = self.vars.get(\"occupied\", 0)+1\n            return\n        # Daily entries retain the common four-hour ATR protection. The current\n        # day's closed bars are known; this is not a daily-ATR substitution.\n        atr = atr14(rows)\n        if atr is None:\n            return\n        direction = event[\"direction\"]\n        plan = entry_plan(float(self.price), max(0., float(self.balance)),\n                          float(self.available_margin), float(self.leverage),\n                          float(self.fee_rate), direction, 2*atr)\n        if plan is None or self.price+direction*2*plan[\"distance\"] <= 0:\n            return\n        self.vars[\"plan\"] = dict(plan, path_label=event[\"label\"],\n                                 high_index=event[\"high_index\"], low_index=event[\"low_index\"])\n        self.vars[\"direction\"] = direction\n\n    def on_open_position(self, order):\n        super().on_open_position(order)\n        plan = self.vars[\"plan\"]\n        # Persist the observed label only after an actual simulated opening fill.\n        self._log(\"R15_PATH_OPEN\", dict(\n            time=int(self.time), path_label=plan[\"path_label\"],\n            high_index=plan[\"high_index\"], low_index=plan[\"low_index\"]))\n\n    def _emit(self, stage):\n        super()._emit(stage)\n        self._log(\"R15_PATH_STATS\", dict(\n            stage=stage, counts=self.vars.get(\"day_path_counts\", {}),\n            signals=self.vars.get(\"signals\", 0), entries=self.vars.get(\"entries\", 0),\n            occupied=self.vars.get(\"occupied\", 0)))\n","BtcResearchR15Repair1m":"from strategies.BtcResearchR15PathBase1m import BtcResearchR15PathBase1m\n\n\nclass BtcResearchR15Repair1m(BtcResearchR15PathBase1m):\n    MODE = \"REPAIR\"\n","BtcResearchR15Body1m":"from strategies.BtcResearchR15PathBase1m import BtcResearchR15PathBase1m\n\n\nclass BtcResearchR15Body1m(BtcResearchR15PathBase1m):\n    MODE = \"BODY\"\n","BtcResearchR10Base4h":"import json\nimport math\n\nimport numpy as np\nfrom jesse.strategies import Strategy\n\nBAR = 14400000\nDAY = 86400000\n\n\ndef closed_window(candles, now, count):\n    \"\"\"Use only consecutive, closed 4h bars; no synthetic gap repair.\"\"\"\n    rows = candles[candles[:, 0] + BAR <= now][-count:]\n    if len(rows) != count or rows[-1, 0] != now - BAR:\n        return None\n    if not np.all(np.diff(rows[:, 0]) == BAR):\n        return None\n    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):\n        return None\n    if np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2])):\n        return None\n    if np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2])):\n        return None\n    return rows\n\n\ndef atr14(rows):\n    previous = rows[-15:-1, 2]\n    current = rows[-14:]\n    tr = np.maximum(current[:, 3] - current[:, 4],\n                    np.maximum(abs(current[:, 3] - previous), abs(current[:, 4] - previous)))\n    value = float(np.mean(tr))\n    return value if math.isfinite(value) and value > 0 else None\n\n\ndef breadth_state(closes):\n    changes = np.diff(closes)\n    positive = changes > 0\n    negative = changes < 0\n    if int(positive[-6:].sum()) >= 4 and int(positive[-24:].sum()) >= 16:\n        return 1\n    if int(negative[-6:].sum()) >= 4 and int(negative[-24:].sum()) >= 16:\n        return -1\n    return 0\n\n\ndef breadth_signal(rows):\n    \"\"\"Count sign persistence, not return magnitudes; consume only new states.\"\"\"\n    now_state = breadth_state(rows[-25:, 2])\n    old_state = breadth_state(rows[-26:-1, 2])\n    return now_state if now_state != old_state else 0\n\n\ndef funding_failure_signal(rows, now, events):\n    \"\"\"Observe a full post-payment bar; never know or collect the next payment.\"\"\"\n    event_start = now - BAR\n    matching = []\n    for event in events:\n        raw = int(event[\"settled_at\"])\n        effective = raw // 60000 * 60000\n        if effective == event_start and 0 <= raw - effective <= 1000:\n            if int(event[\"available_at\"]) <= now and int(event[\"available_at\"]) > raw:\n                matching.append(event)\n    if len(matching) != 1:\n        return 0, None\n    event = matching[0]\n    rate = float(event[\"rate_decimal\"])\n    if not math.isfinite(rate):\n        return 0, None\n    pre, post = rows[-2], rows[-1]\n    if rate > 0 and pre[2] > pre[1] and post[2] < pre[1]:\n        return -1, dict(settled_at=int(event[\"settled_at\"]), available_at=int(event[\"available_at\"]), rate=rate)\n    if rate < 0 and pre[2] < pre[1] and post[2] > pre[1]:\n        return 1, dict(settled_at=int(event[\"settled_at\"]), available_at=int(event[\"available_at\"]), rate=rate)\n    return 0, None\n\n\ndef entry_plan(price, capital, margin, leverage, fee, direction, distance):\n    stop = price - direction * distance\n    values = (price, capital, margin, leverage, distance, stop)\n    if direction not in (-1, 1) or not all(math.isfinite(v) and v > 0 for v in values):\n        return None\n    if not math.isfinite(fee) or fee < 0:\n        return None\n    unit_loss = distance + fee * (price + stop)\n    # 2% includes both execution fees. The 90% margin ceiling retains the\n    # historical reserve and does not increase the stop's monetary risk.\n    risk_qty = 0.02 * capital / unit_loss\n    margin_qty = 0.90 * margin * leverage / (price * (1 + fee * leverage))\n    qty = math.floor(min(risk_qty, margin_qty) * 1e8) / 1e8\n    if qty <= 0:\n        return None\n    assert qty * unit_loss <= 0.02 * capital + 1e-6\n    return dict(qty=qty, price=price, capital=capital, distance=distance,\n                stop=stop, risk_budget=0.02 * capital,\n                planned_loss=qty * unit_loss, margin_capped=margin_qty < risk_qty)\n\n\nclass BtcResearchR10Base4h(Strategy):\n    \"\"\"R10 discovery harness: one BTC position, fixed risk and base costs only.\"\"\"\n    MODE = \"abstract\"\n    START = 1602720000000\n    FINISH = 1767225600000\n\n    def _log(self, label, value):\n        self.log(label + \" \" + json.dumps(value, separators=(\",\", \":\"), allow_nan=False))\n\n    def before(self):\n        now = int(self.time)\n        if not self.vars.get(\"checked\"):\n            assert self.symbol == \"BTC-USDT\"\n            assert self.leverage == 3\n            assert abs(self.fee_rate - 0.00045) < 1e-12\n            self.vars[\"checked\"] = True\n            self._log(\"R10_CONFIG\", dict(mode=self.MODE, risk=0.02, aggregate=0.06,\n                                        leverage=self.leverage, fee=self.fee_rate,\n                                        margin_buffer=0.90, stop_atr=2, target_r=2, hold_hours=48))\n        self.vars[\"direction\"] = 0\n        rows = closed_window(self.candles, now, 26)\n        if rows is None:\n            self.vars[\"invalid_windows\"] = self.vars.get(\"invalid_windows\", 0) + 1\n            return\n        if self.MODE == \"BREADTH\":\n            direction = breadth_signal(rows)\n            evidence = None\n        else:\n            assert self.MODE == \"POST_FUNDING\"\n            events = self.get_funding_history(count=6)\n            assert all(int(e[\"available_at\"]) <= now for e in events)\n            direction, evidence = funding_failure_signal(rows, now, events)\n        if not direction or not self.START < now < self.FINISH:\n            return\n        # Signals are evaluated and consumed while occupied as well. No deferred\n        # order or re-entry from a previously blocked funding/breadth event.\n        self.vars[\"signals\"] = self.vars.get(\"signals\", 0) + 1\n        if self.is_open or self.entry_orders or self.vars.get(\"last_exit_at\") == now:\n            self.vars[\"occupied\"] = self.vars.get(\"occupied\", 0) + 1\n            return\n        atr = atr14(rows)\n        if atr is None:\n            return\n        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))\n        plan = entry_plan(float(self.price), capital, float(self.available_margin),\n                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)\n        if plan is None or float(self.price) + direction * 2 * plan[\"distance\"] <= 0:\n            return\n        self.vars[\"direction\"] = direction\n        self.vars[\"plan\"] = plan\n        self.vars[\"evidence\"] = evidence\n\n    def should_long(self):\n        return self.vars.get(\"direction\") == 1\n\n    def should_short(self):\n        return self.vars.get(\"direction\") == -1\n\n    def go_long(self):\n        plan = self.vars[\"plan\"]\n        self.buy = plan[\"qty\"], self.price\n\n    def go_short(self):\n        plan = self.vars[\"plan\"]\n        self.sell = plan[\"qty\"], self.price\n\n    def should_cancel_entry(self):\n        return True\n\n    def on_open_position(self, order):\n        plan = self.vars[\"plan\"]\n        direction = 1 if self.is_long else -1\n        entry = float(self.position.entry_price)\n        qty = abs(float(self.position.qty))\n        distance = plan[\"distance\"]\n        stop = entry - direction * distance\n        target = entry + direction * 2 * distance\n        assert qty * (distance + self.fee_rate * (entry + stop)) <= plan[\"risk_budget\"] + 1e-6\n        self.stop_loss = qty, stop\n        self.take_profit = qty, target\n        self.vars[\"entries\"] = self.vars.get(\"entries\", 0) + 1\n        self._log(\"R10_ENTRY\", dict(time=int(self.time), direction=direction, entry=entry,\n                                   qty=qty, stop=stop, target=target, plan=plan,\n                                   evidence=self.vars.get(\"evidence\")))\n\n    def update_position(self):\n        # No ratchet, discretionary exit or same-close reversal. Funding applies\n        # continuously to actual held quantity, independently of signal inputs.\n        if int(self.time) - int(self.position.opened_at) >= 12 * BAR:\n            self.liquidate()\n\n    def on_close_position(self, order, closed_trade):\n        self.vars[\"last_exit_at\"] = int(self.time)\n\n    def before_terminate(self):\n        self._log(\"R10_COUNTERS\", dict(signals=self.vars.get(\"signals\", 0),\n                                     occupied=self.vars.get(\"occupied\", 0),\n                                     entries=self.vars.get(\"entries\", 0),\n                                     invalid_windows=self.vars.get(\"invalid_windows\", 0)))\n","BtcResearchR11Base1m":"import json\nimport math\nfrom datetime import datetime, timezone\n\nimport numpy as np\nfrom jesse.strategies import Strategy\nfrom strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan\n\n\ndef cusum_step(rows, accumulators):\n    \"\"\"Transfer the R40 design:60 past log returns, drift0.25, boundary4.\"\"\"\n    returns = np.diff(np.log(rows[-62:, 2]))\n    sigma = float(np.std(returns[:-1], ddof=1))\n    if not math.isfinite(sigma) or sigma <= 0:\n        return 0, (0.0, 0.0)\n    z = float((returns[-1] - np.mean(returns[:-1])) / sigma)\n    if not math.isfinite(z):\n        return 0, (0.0, 0.0)\n    up = max(0.0, accumulators[0] + z - 0.25)\n    down = max(0.0, accumulators[1] - z - 0.25)\n    if up >= 4 or down >= 4:\n        direction = 0 if up >= 4 and down >= 4 else 1 if up >= 4 else -1\n        return direction, (0.0, 0.0)\n    return 0, (up, down)\n\n\ndef absorption_signal(rows):\n    \"\"\"Large volume but small body, followed by escape of that closed bar.\"\"\"\n    window, setup, confirmation = rows[-26:-2], rows[-2], rows[-1]\n    if not np.all(np.isfinite(rows[-26:, 5])) or np.any(rows[-26:, 5] < 0):\n        return 0\n    average_volume = float(np.mean(window[:, 5]))\n    prior_atr = atr14(window)\n    if not math.isfinite(average_volume) or average_volume <= 0 or prior_atr is None:\n        return 0\n    if setup[5] < 2 * average_volume or abs(setup[2] - setup[1]) > 0.25 * prior_atr:\n        return 0\n    if confirmation[2] > setup[3]:\n        return 1\n    if confirmation[2] < setup[4]:\n        return -1\n    return 0\n\n\ndef month_name(timestamp):\n    return datetime.fromtimestamp(timestamp / 1000, timezone.utc).strftime(\"%Y-%m\")\n\n\ndef monthly_summary(boundaries, active_months):\n    \"\"\"Declared post-settlement/pre-decision UTC cuts; no00:01 approximation.\"\"\"\n    points = sorted(boundaries.items())\n    months = []\n    for (start, before), (finish, after) in zip(points, points[1:]):\n        stamp = datetime.fromtimestamp(start / 1000, timezone.utc)\n        month = stamp.strftime(\"%Y-%m\")\n        complete = stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0\n        if before <= 0:\n            continue\n        months.append(dict(month=month, start=start, finish=finish,\n                           complete=complete, active=month in active_months,\n                           pnl=after-before, return_fraction=after/before-1))\n    complete = [m for m in months if m[\"complete\"]]\n    active = [m for m in complete if m[\"active\"]]\n    quarter_groups = {}\n    for m in months:\n        quarter = m[\"month\"][:4] + \"Q\" + str((int(m[\"month\"][5:])-1)//3+1)\n        quarter_groups.setdefault(quarter, []).append(m)\n    quarters = [q for q in quarter_groups.values()\n                if len(q) == 3 and all(m[\"complete\"] for m in q)]\n    returns = [m[\"return_fraction\"] for m in complete]\n    contributions = sorted([m[\"pnl\"] for m in months], reverse=True)\n    return dict(months=months, complete_months=len(complete), active_months=len(active),\n                positive_active=sum(m[\"pnl\"] > 0 for m in active),\n                positive_calendar=sum(m[\"pnl\"] > 0 for m in complete),\n                median_return=float(np.median(returns)) if returns else None,\n                complete_quarters=len(quarters),\n                positive_quarters=sum(sum(m[\"pnl\"] for m in q) > 0 for q in quarters),\n                pnl_without_best_two=sum(m[\"pnl\"] for m in months)-sum(contributions[:2]))\n\n\nclass BtcResearchR11Base1m(Strategy):\n    \"\"\"M1 accounting observer; signal and management decisions remain4h.\"\"\"\n    MODE = \"abstract\"\n    START = 1602720000000\n    FINISH = 1767225600000\n\n    def _log(self, label, payload):\n        # Event logs stay small; monthly history is emitted as separate rows.\n        self.log(label + \" \" + json.dumps(payload, separators=(\",\", \":\"), allow_nan=False))\n\n    def _observe(self, stage):\n        now = int(self.time)\n        # BTC-only futures equity. portfolio_value multiplies open PnL by\n        # leverage in this checkout, so it is deliberately not used here.\n        equity = float(self.balance) + (float(self.position.pnl) if self.is_open else 0.0)\n        assert math.isfinite(equity)\n        self.vars[\"peak\"] = max(self.vars.get(\"peak\", 10000.0), equity)\n        drawdown = equity / self.vars[\"peak\"] - 1\n        self.vars[\"dd\"] = min(self.vars.get(\"dd\", 0.0), drawdown)\n        self.vars[\"sequence\"] = self.vars.get(\"sequence\", 0) + 1\n        self.vars[\"last_equity\"] = equity\n        active = self.vars.setdefault(\"active_months\", set())\n        if self.is_open:\n            # Pre marks describe exposure during the minute that just closed;\n            # an opening fill at T instead belongs to the new interval.\n            active.add(month_name(now if stage == \"open\" else now-1))\n        boundaries = self.vars.setdefault(\"boundaries\", {self.START: 10000.0})\n        if stage == \"pre\":\n            self.vars[\"minute_marks\"] = self.vars.get(\"minute_marks\", 0) + 1\n            stamp = datetime.fromtimestamp(now / 1000, timezone.utc)\n            if stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0:\n                boundaries[now] = equity\n        if now >= self.FINISH:\n            # A later terminal close callback replaces the mark with post-fee equity.\n            boundaries[self.FINISH] = equity\n        return equity\n\n    def before(self):\n        now = int(self.time)\n        if not self.vars.get(\"checked\"):\n            assert self.symbol == \"BTC-USDT\" and self.timeframe == \"1m\"\n            assert self.leverage == 3 and abs(self.fee_rate - 0.00045) < 1e-12\n            assert abs(self.balance - 10000) < 1e-6\n            self.vars[\"checked\"] = True\n        self._observe(\"pre\")\n        self.vars[\"direction\"] = 0\n        # This is signal alignment, not a market-session/calendar filter.\n        if now % BAR != 0:\n            return\n        count = 62 if self.MODE == \"CUSUM\" else 26\n        candles = self.get_candles(self.exchange, self.symbol, \"4h\")\n        rows = closed_window(candles, now, count)\n        if rows is None:\n            self.vars[\"invalid_windows\"] = self.vars.get(\"invalid_windows\", 0) + 1\n            self.vars[\"cusum\"] = (0.0, 0.0)\n            return\n        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)\n        if self.MODE == \"CUSUM\":\n            direction, state = cusum_step(rows, self.vars.get(\"cusum\", (0.0, 0.0)))\n            self.vars[\"cusum\"] = state\n        else:\n            assert self.MODE == \"ABSORPTION\"\n            direction = absorption_signal(rows)\n        if not direction or not self.START < now < self.FINISH:\n            return\n        self.vars[\"signals\"] = self.vars.get(\"signals\", 0) + 1\n        if self.is_open or self.entry_orders or self.vars.get(\"last_exit_at\") == now:\n            self.vars[\"occupied\"] = self.vars.get(\"occupied\", 0) + 1\n            return\n        atr = atr14(rows)\n        if atr is None:\n            return\n        # Flat BTC account: wallet equals equity. Reuse the frozen2% fee-aware\n        # plan, eight-decimal research precision and90% margin ceiling.\n        capital = max(0.0, float(self.balance))\n        plan = entry_plan(float(self.price), capital, float(self.available_margin),\n                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)\n        if plan is None or self.price + direction * 2 * plan[\"distance\"] <= 0:\n            return\n        self.vars[\"direction\"] = direction\n        self.vars[\"plan\"] = plan\n\n    def should_long(self):\n        return self.vars.get(\"direction\") == 1\n\n    def should_short(self):\n        return self.vars.get(\"direction\") == -1\n\n    def go_long(self):\n        self.buy = self.vars[\"plan\"][\"qty\"], self.price\n\n    def go_short(self):\n        self.sell = self.vars[\"plan\"][\"qty\"], self.price\n\n    def should_cancel_entry(self):\n        return True\n\n    def on_open_position(self, order):\n        plan = self.vars[\"plan\"]\n        direction = 1 if self.is_long else -1\n        entry = float(self.position.entry_price)\n        qty = abs(float(self.position.qty))\n        stop = entry - direction * plan[\"distance\"]\n        target = entry + direction * 2 * plan[\"distance\"]\n        assert qty * (plan[\"distance\"] + self.fee_rate * (entry + stop)) <= plan[\"risk_budget\"] + 1e-6\n        self.stop_loss = qty, stop\n        self.take_profit = qty, target\n        self.vars[\"entries\"] = self.vars.get(\"entries\", 0) + 1\n        self._observe(\"open\")\n\n    def update_position(self):\n        # Preserve the four-hour management clock despite the M1 observer.\n        if int(self.time) % BAR == 0 and int(self.time) - int(self.position.opened_at) >= 12 * BAR:\n            self.liquidate()\n\n    def on_close_position(self, order, closed_trade):\n        now = int(self.time)\n        active = self.vars.setdefault(\"active_months\", set())\n        active.add(month_name(now-1))\n        # At a month boundary, retain both the held interval and any fee-only\n        # execution month. Terminal liquidation belongs to the final interval.\n        if now < self.FINISH:\n            active.add(month_name(now))\n        self.vars[\"last_exit_at\"] = now\n        self._observe(\"close\")\n        if now >= self.FINISH and self.vars.get(\"emitted\"):\n            self._emit(\"FINAL\")\n\n    def _emit(self, stage):\n        summary = monthly_summary(self.vars[\"boundaries\"], self.vars.get(\"active_months\", set()))\n        # Emit rows at the end, so one bounded log page can retrieve all months.\n        for item in summary.pop(\"months\"):\n            self._log(\"R11_MONTH\", dict(stage=stage, **item))\n        summary.update(stage=stage, equity=self.vars[\"last_equity\"],\n                       dd_m1_events=self.vars.get(\"dd\", 0),\n                       minute_marks=self.vars.get(\"minute_marks\", 0),\n                       sequence=self.vars.get(\"sequence\", 0),\n                       signals=self.vars.get(\"signals\", 0), entries=self.vars.get(\"entries\", 0),\n                       invalid_windows=self.vars.get(\"invalid_windows\", 0))\n        self._log(\"R11_SUMMARY\", summary)\n\n    def before_terminate(self):\n        self._observe(\"terminal\")\n        self.vars[\"emitted\"] = True\n        self._emit(\"PRETERMINAL\")\n"}
BAR = 14400000
DAY = 86400000
T = 1609459200000
CHECKS = []

def check(value, name):
    assert bool(value), name
    CHECKS.append(name)

class Strategy:
    pass

ns = dict(np=np, math=math, json=json, datetime=datetime, timezone=timezone,
          Strategy=Strategy, BAR=BAR, DAY=DAY)

def supplied_nodes(name, selected):
    tree = ast.parse(SOURCES[name])
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in selected:
            exec(compile(ast.Module(body=[node], type_ignores=[]), name, "exec"), ns)
    check(selected.issubset(ns.keys()), "supplied_nodes_"+name)

for name, source in SOURCES.items():
    compile(source, name, "exec")
    check(True, "ast_compile_"+name)
hashes = {name: hashlib.sha256(source.encode()).hexdigest() for name, source in SOURCES.items()}
check(hashes["BtcResearchR10Base4h"] == "2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9", "frozen_R10_hash")
check(hashes["BtcResearchR11Base1m"] == "be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87", "frozen_R11_hash")
supplied_nodes("BtcResearchR10Base4h", {"closed_window", "atr14", "entry_plan"})
supplied_nodes("BtcResearchR11Base1m", {"month_name", "monthly_summary", "BtcResearchR11Base1m"})
supplied_nodes("BtcResearchR15PathBase1m", {"day_path", "BtcResearchR15PathBase1m"})
supplied_nodes("BtcResearchR15Repair1m", {"BtcResearchR15Repair1m"})
supplied_nodes("BtcResearchR15Body1m", {"BtcResearchR15Body1m"})
day_path, closed_window, atr14, entry_plan = (ns[k] for k in ("day_path", "closed_window", "atr14", "entry_plan"))

def fixture(now=T):
    rows = np.array([[now-15*BAR+i*BAR, 100., 100., 101., 99., 1.] for i in range(15)])
    block = np.array([[100., 101., 106., 99., 1.],
                      [102., 103., 115., 98., 1.],
                      [102., 103., 108., 98., 1.],
                      [102., 103., 108., 98., 1.],
                      [102., 103., 108., 90., 1.],
                      [103., 105., 107., 100., 1.]])
    rows[-6:, 1:] = block
    return rows

def mirror(rows):
    result = rows.copy()
    result[:, 1] = 300-rows[:, 1]
    result[:, 2] = 300-rows[:, 2]
    result[:, 3] = 300-rows[:, 4]
    result[:, 4] = 300-rows[:, 3]
    return result

rows = fixture()
event = day_path(rows)
check(event == dict(direction=1, repair=True, label="repair", high_index=1, low_index=4), "repair_exact_oracle")
reflected = day_path(mirror(rows))
check(reflected == dict(direction=-1, repair=True, label="repair", high_index=4, low_index=1), "mirror_exact_oracle")
reordered = rows.copy()
reordered[-5, 1:], reordered[-2, 1:] = rows[-2, 1:].copy(), rows[-5, 1:].copy()
ordinary = day_path(reordered)
check(ordinary["direction"] == 1 and not ordinary["repair"], "same_daily_body_different_order")
check(ordinary["high_index"] == 4 and ordinary["low_index"] == 1, "order_indices_changed")
for column, reduction in ((3, np.max), (4, np.min)):
    check(float(reduction(rows[-6:, column])) == float(reduction(reordered[-6:, column])), "same_daily_extreme_"+str(column))
check(rows[-6, 1] == reordered[-6, 1] and rows[-1, 2] == reordered[-1, 2], "same_daily_open_close")
check(day_path(mirror(reordered))["direction"] == -1 and not day_path(mirror(reordered))["repair"], "ordinary_mirror")
check(day_path(rows[-6:]) == event, "helper_uses_six_closed_bars")
original = rows.copy()
day_path(rows)
check(np.array_equal(original, rows), "helper_no_mutation")
older = rows.copy()
older[:9, 1:] = np.nan
check(day_path(older) == event, "path_ignores_older_prefix")
for value in (0., np.nan):
    volume = rows.copy()
    volume[:, 5] = value
    check(day_path(volume) == event, "volume_irrelevant_"+str(value))
for reason in ("doji", "high_tie", "low_tie", "same_bar", "gap", "shifted", "nan_price", "invalid_high", "zero_price"):
    bad = rows.copy()
    if reason == "doji":
        bad[-1, 2] = bad[-6, 1]
    elif reason == "high_tie":
        bad[-4, 3] = 115.
    elif reason == "low_tie":
        bad[-3, 4] = 90.
    elif reason == "same_bar":
        bad[-5, 3], bad[-5, 4] = 120., 80.
    elif reason == "gap":
        bad[-3, 0] += 60000
    elif reason == "shifted":
        bad[:, 0] += BAR
    elif reason == "nan_price":
        bad[-1, 2] = np.nan
    elif reason == "invalid_high":
        bad[-1, 3] = 100.
    else:
        bad[-1, 2] = 0.
    check(day_path(bad) is None, "invalid_path_"+reason)
check(day_path(rows[-5:]) is None, "short_day_reject")
check(day_path(rows[-6:, :4]) is None, "short_columns_reject")

future = np.array([[T, np.nan, np.nan, np.nan, np.nan, np.nan]])
selected = closed_window(np.vstack((rows, future)), T, 15)
check(np.array_equal(selected, rows), "future_excluded_by_closed_window")
check(day_path(selected) == event, "future_cannot_change_day_label")
check(closed_window(rows, T+60000, 15) is None, "asof_exact")
gap = rows.copy()
gap[3, 0] += 60000
check(closed_window(gap, T, 15) is None, "whole_atr_window_gap_reject")
old = rows.copy()
old[:, 0] -= 15*BAR
old[:, 1:] = np.nan
check(np.array_equal(closed_window(np.vstack((old, rows)), T, 15), rows), "old_prefix_excluded_by_closed_window")
check(day_path(closed_window(np.vstack((old, rows)), T, 15)) == event, "old_prefix_cannot_change_day")

# Independent true-range loop, not the vectorized implementation.
oracle_tr = [max(float(rows[i, 3]-rows[i, 4]),
                 abs(float(rows[i, 3]-rows[i-1, 2])),
                 abs(float(rows[i, 4]-rows[i-1, 2]))) for i in range(1, 15)]
oracle_atr = sum(oracle_tr)/14
check(math.isclose(atr14(rows), oracle_atr, abs_tol=1e-12), "atr14_independent_oracle")
check(math.isclose(atr14(mirror(rows)), oracle_atr, abs_tol=1e-12), "atr14_mirror")
check(np.array_equal(closed_window(rows, T, 15)[-6:, 0], T-DAY+np.arange(6)*BAR), "exact_utc_day_partition")

def instance(mode="REPAIR", candles=None, now=T):
    cls = ns["BtcResearchR15Repair1m" if mode == "REPAIR" else "BtcResearchR15Body1m"]
    obj = cls()
    obj.vars = {}
    obj.symbol, obj.timeframe, obj.exchange = "BTC-USDT", "1m", "Binance Perpetual Futures"
    obj.time = now
    obj.balance, obj.available_margin, obj.leverage, obj.fee_rate = 10000., 10000., 3, .00045
    obj.is_open, obj.is_long, obj.is_short = False, False, False
    obj.entry_orders = []
    obj.position = SimpleNamespace(pnl=0., qty=0., entry_price=0., opened_at=now)
    obj._candles = fixture(now) if candles is None else candles.copy()
    obj.price = float(obj._candles[-1, 2])
    obj.get_candles = lambda exchange, symbol, timeframe: obj._candles
    obj.logs = []
    obj.log = obj.logs.append
    obj.liquidations = []
    obj.liquidate = lambda: obj.liquidations.append(int(obj.time))
    return obj

for mode in ("REPAIR", "BODY"):
    obj = instance(mode)
    obj.before()
    check(obj.should_long() and not obj.should_short(), mode+"_repair_admitted")
    check(obj.vars["plan"]["path_label"] == "repair", mode+"_plan_label")
    check(obj.vars["plan"]["high_index"] == 1 and obj.vars["plan"]["low_index"] == 4, mode+"_plan_indices")
    check(math.isclose(obj.vars["plan"]["distance"], 2*oracle_atr), mode+"_two_atr_distance")
    plan = obj.vars["plan"]
    stop = obj.price-plan["distance"]
    loss = plan["qty"]*(plan["distance"]+obj.fee_rate*(obj.price+stop))
    check(loss <= .02*obj.balance+1e-6 and plan["risk_budget"] == 200., mode+"_fee_aware_risk")
    margin_qty = .90*obj.available_margin*3/(obj.price*(1+obj.fee_rate*3))
    check(plan["qty"] <= margin_qty, mode+"_margin_ceiling")
    qty_oracle = math.floor(min(200/(plan["distance"]+obj.fee_rate*(obj.price+stop)), margin_qty)*1e8)/1e8
    check(plan["qty"] == qty_oracle, mode+"_quantity_oracle")
    obj.go_long()
    check(obj.buy == (plan["qty"], obj.price), mode+"_market_intent")
    obj.is_open, obj.is_long = True, True
    obj.position = SimpleNamespace(pnl=0., qty=plan["qty"], entry_price=obj.price, opened_at=T)
    obj.on_open_position(None)
    check(obj.stop_loss == (plan["qty"], obj.price-plan["distance"]), mode+"_actual_fill_stop")
    check(obj.take_profit == (plan["qty"], obj.price+2*plan["distance"]), mode+"_actual_fill_target")
    path_log = [line for line in obj.logs if line.startswith("R15_PATH_OPEN ")]
    check(len(path_log) == 1, mode+"_fill_label_persisted")
    payload = json.loads(path_log[0].split(" ", 1)[1])
    check(payload == dict(time=T, path_label="repair", high_index=1, low_index=4), mode+"_fill_label_payload")
    check(obj.vars["entries"] == 1, mode+"_single_entry_counter")
    obj.time = T+11*BAR
    obj.update_position()
    check(not obj.liquidations, mode+"_no_exit_44h")
    obj.time = T+12*BAR-60000
    obj.update_position()
    check(not obj.liquidations, mode+"_no_exit_non4h_before48h")
    obj.time = T+12*BAR
    obj.update_position()
    check(obj.liquidations == [T+12*BAR], mode+"_exit_48h")
    check(obj.should_cancel_entry() is True, mode+"_no_persistent_entry")

for mode in ("REPAIR", "BODY"):
    for candles, valid in ((reordered, mode == "BODY"), (mirror(reordered), mode == "BODY")):
        obj = instance(mode, candles)
        obj.before()
        direction = 1 if candles[-1, 2] > candles[-6, 1] else -1
        check(obj.vars.get("direction", 0) == (direction if valid else 0), mode+"_ordinary_admission_"+str(direction))
    invalid_cases = [rows.copy() for _ in range(4)]
    invalid_cases[0][-1, 2] = invalid_cases[0][-6, 1]
    invalid_cases[1][-4, 3] = 115.
    invalid_cases[2][-3, 4] = 90.
    invalid_cases[3][-5, 3], invalid_cases[3][-5, 4] = 120., 80.
    for i, candles in enumerate(invalid_cases):
        obj = instance(mode, candles)
        obj.before()
        check(not obj.should_long() and not obj.should_short(), mode+"_shared_invalid_"+str(i))
    for value in (0., np.nan):
        candles = rows.copy()
        candles[:, 5] = value
        obj = instance(mode, candles)
        obj.before()
        check(obj.should_long(), mode+"_shared_volume_irrelevance_"+str(value))

for occupied in ("position", "pending", "same_exit"):
    obj = instance()
    if occupied == "position":
        obj.is_open = True
    elif occupied == "pending":
        obj.entry_orders = [object()]
    else:
        obj.vars["last_exit_at"] = T
    obj.before()
    check(obj.vars.get("direction", 0) == 0 and obj.vars.get("occupied") == 1, "occupied_consumed_"+occupied)
    obj.is_open, obj.entry_orders = False, []
    obj.time = T+60000
    obj.before()
    check(not obj.should_long() and not obj.should_short(), "no_queue_"+occupied)
    check(obj.vars.get("signals") == 1, "daily_signal_not_replayed_"+occupied)

obj = instance()
obj.time = T+60000
obj.before()
check("day_path_counts" not in obj.vars and obj.vars.get("direction") == 0, "no_nondaily_entry")
obj = instance(now=1767225600000)
obj.before()
check("day_path_counts" not in obj.vars and obj.vars.get("signals", 0) == 0, "exclusive_finish_has_no_counts_or_entries")
obj = instance(now=1602720000000)
obj.before()
check("day_path_counts" not in obj.vars and obj.vars.get("signals", 0) == 0, "exclusive_start_entry_guard")
obj = instance(candles=gap)
obj.before()
check(obj.vars.get("invalid_windows") == 1 and obj.vars["direction"] == 0, "invalid_signal_window_observed")
obj = instance()
obj.before()
obj.time += DAY
obj._candles[:, 0] += DAY
obj.before()
check(obj.vars.get("signals") == 2, "same_direction_new_day_is_new_event")
check(obj.vars["day_path_counts"] == dict(repair=2, body_only=0), "daily_counts_not_state_crossings")

# Hook stubs demonstrate terminal ordering, not broker fills or real economic runs.
obj = instance()
obj.vars["checked"] = True
start, finish = obj.START, obj.FINISH
boundaries = {start: 10000.}
stamp = datetime(2020, 11, 1, tzinfo=timezone.utc)
while int(stamp.timestamp()*1000) < finish:
    boundaries[int(stamp.timestamp()*1000)] = 10000.
    stamp = datetime(stamp.year+(stamp.month == 12), 1 if stamp.month == 12 else stamp.month+1, 1, tzinfo=timezone.utc)
boundaries[finish] = 10000.
obj.vars["boundaries"] = boundaries
obj.vars["active_months"] = {ns["month_name"](ts) for ts in boundaries if ts < finish}
obj.vars["day_path_counts"] = dict(repair=3, body_only=2)
obj.vars["signals"], obj.vars["entries"] = 3, 1
obj.time = finish
obj.is_open, obj.is_long = True, True
obj.position = SimpleNamespace(pnl=5., qty=1., entry_price=100., opened_at=finish-DAY)
obj.before_terminate()
pre = json.loads([line for line in obj.logs if line.startswith("R11_SUMMARY ")][-1].split(" ", 1)[1])
check(pre["stage"] == "PRETERMINAL" and pre["equity"] == 10005., "preterminal_open_equity")
obj.balance, obj.is_open = 9997., False
obj.position.pnl = 0.
obj.on_close_position(None, SimpleNamespace(pnl=-3.))
final = json.loads([line for line in obj.logs if line.startswith("R11_SUMMARY ")][-1].split(" ", 1)[1])
stats = json.loads([line for line in obj.logs if line.startswith("R15_PATH_STATS ")][-1].split(" ", 1)[1])
check(final["stage"] == "FINAL" and final["equity"] == 9997., "final_postclose_equity_overrides")
check(stats["stage"] == "FINAL" and stats["counts"] == dict(repair=3, body_only=2), "final_path_stats_persisted")
check(final["complete_months"] == 62 and final["complete_quarters"] == 20, "calendar_contract_62months20quarters")
final_months = [json.loads(line.split(" ", 1)[1]) for line in obj.logs if line.startswith("R11_MONTH ") and json.loads(line.split(" ", 1)[1])["stage"] == "FINAL"]
check(len(final_months) == 63, "calendar_contract_63intervals")
check(abs(sum(row["pnl"] for row in final_months)+3.) < 1e-6, "synthetic_monthly_telescope")
check(obj.vars["boundaries"][finish] == 9997., "terminal_boundary_updated")
check("2026-01" not in obj.vars["active_months"], "terminal_close_does_not_activate_next_month")

receipt = dict(status="passed", assertions=len(CHECKS), checks=CHECKS, source_sha256=hashes,
               real_inputs=[], engine_backtests_started=0,
               scope="AST supplied source functions and strategy hook stubs; not engine fill validation or economic evidence",
               parent_sources_unchanged=True)
Path("output").mkdir(exist_ok=True)
Path("output/O_CHECK_RECEIPT.json").write_text(json.dumps(receipt, indent=2)+"\n")
print(json.dumps(dict(status=receipt["status"], assertions=receipt["assertions"], source_sha256=hashes)))

```
