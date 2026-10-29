# R32 B — check supplied-source listo

Estado: código preparado antes de ejecutar. Sólo fuente suministrada, AST/stubs y arrays fabricados. Sin proyecto/frameworkimports, precios reales ni motores. Output previsto output/b_failure_check.json, menor48k. La prueba no reemplaza auditoría nativa ni el recibo común R32.

```python
import ast
import hashlib
import json
import math
from pathlib import Path
import numpy as np

# Only literal supplied strategy source is parsed. No project/framework imports,
# files, observed candles, engine instance or second simulated book are used.
SOURCES = json.loads("{\"BtcResearchR32FailureBase1m\":\"import numpy as np\\n\\nfrom strategies.BtcResearchR32SpecialistBase1m import BtcResearchR32SpecialistBase1m\\n\\n\\ndef failure_pattern(rows):\\n    \\\"\\\"\\\"Classify 26 prior ranges, then breakout/failure/resolution closes.\\n\\n    R32 validates the full 64-row clock/OHLC contract before calling the leaf.\\n    Only the last 29 rows define this pattern; no signal-bar extreme moves\\n    the frozen boundary. Equality is never an interior or exterior crossing.\\n    \\\"\\\"\\\"\\n    context = rows[-29:-3]\\n    lower = float(np.min(context[:, 4]))\\n    upper = float(np.max(context[:, 3]))\\n    if lower >= upper:\\n        return None\\n    breakout, failure, resolution = rows[-3], rows[-2], rows[-1]\\n    c_b, c_f, c_r = (float(row[2]) for row in (breakout, failure, resolution))\\n    side = 1 if c_b > upper else -1 if c_b < lower else 0\\n    if side == 0 or not lower < c_f < upper:\\n        return None\\n    if lower < c_r < upper:\\n        category = \\\"interior\\\"\\n    elif c_r == lower or c_r == upper:\\n        category = \\\"boundary\\\"\\n    elif (side == 1 and c_r > upper) or (side == -1 and c_r < lower):\\n        category = \\\"recovered_original\\\"\\n    else:\\n        category = \\\"crossed_opposite\\\"\\n    return dict(\\n        breakout_at=int(breakout[0]), failure_at=int(failure[0]),\\n        resolution_at=int(resolution[0]), lower=lower, upper=upper,\\n        breakout_close=c_b, failure_close=c_f, resolution_close=c_r,\\n        breakout_side=side, category=category)\\n\\n\\nclass BtcResearchR32FailureBase1m(BtcResearchR32SpecialistBase1m):\\n    \\\"\\\"\\\"Observe the same raw failures before policy, occupancy and sizing.\\\"\\\"\\\"\\n    PERSIST_ONLY = None\\n    HOLD_HOURS = 48\\n    TP_R = 2.0\\n\\n    def _event(self, rows, now):\\n        assert isinstance(self.PERSIST_ONLY, bool)\\n        previous = self.vars.get(\\\"r32_b_last_event\\\")\\n        if previous is not None and now <= previous:\\n            return None\\n        self.vars[\\\"r32_b_last_event\\\"] = now\\n        pattern = failure_pattern(rows)\\n        if pattern is None:\\n            return None\\n        selected = not self.PERSIST_ONLY or pattern[\\\"category\\\"] == \\\"interior\\\"\\n        # One compact row per raw pattern, including rejected and occupied\\n        # events. These denominators describe opportunities, not native fills.\\n        self._log(\\\"R32_B_PATTERN\\\", dict(\\n            policy=self.LABEL, time=int(now), selected=selected, **pattern))\\n        if not selected:\\n            return None\\n        return dict(direction=-pattern[\\\"breakout_side\\\"], meta=pattern)\\n\",\"BtcResearchR32FailureAll1m\":\"from strategies.BtcResearchR32FailureBase1m import BtcResearchR32FailureBase1m\\n\\n\\nclass BtcResearchR32FailureAll1m(BtcResearchR32FailureBase1m):\\n    LABEL = \\\"B_FAILURE_ALL\\\"\\n    PERSIST_ONLY = False\\n\",\"BtcResearchR32FailurePersist1m\":\"from strategies.BtcResearchR32FailureBase1m import BtcResearchR32FailureBase1m\\n\\n\\nclass BtcResearchR32FailurePersist1m(BtcResearchR32FailureBase1m):\\n    LABEL = \\\"B_FAILURE_PERSIST\\\"\\n    PERSIST_ONLY = True\\n\",\"BtcResearchR32SpecialistBase1m\":\"import math\\n\\nfrom strategies.BtcResearchR11Base1m import BtcResearchR11Base1m\\nfrom strategies.BtcResearchR10Base4h import BAR, closed_window, atr14\\nfrom strategies.BtcResearchR16LegacyBase1m import legacy_plan\\n\\n\\nclass BtcResearchR32SpecialistBase1m(BtcResearchR11Base1m):\\n    \\\"\\\"\\\"Frozen one-percent specialist execution; leaves define causal events only.\\\"\\\"\\\"\\n    LABEL = \\\"abstract\\\"\\n    HOLD_HOURS = 48\\n    TP_R = 2.0\\n\\n    def _event(self, rows, now):\\n        raise NotImplementedError\\n\\n    def _invalid_event(self, now):\\n        # Stateful leaves may invalidate an episode; rolling leaves need no state.\\n        pass\\n\\n    def _r32_counts(self):\\n        return self.vars.setdefault(\\\"r32_counts\\\", dict(events=0, plans=0,\\n            occupied=0, rejected_geometry=0, opens=0, closes=0,\\n            long_opens=0, short_opens=0, net=0.0))\\n\\n    def before(self):\\n        now = int(self.time)\\n        if not self.vars.get(\\\"checked\\\"):\\n            assert self.LABEL != \\\"abstract\\\"\\n            assert self.symbol == \\\"BTC-USDT\\\" and self.timeframe == \\\"1m\\\"\\n            assert self.leverage == 3 and abs(self.fee_rate - .00045) < 1e-12\\n            assert abs(self.balance - 10000) < 1e-6\\n            assert self.HOLD_HOURS in (24, 48)\\n            assert self.TP_R in (None, 2.0)\\n            self.vars[\\\"checked\\\"] = True\\n        self._observe(\\\"pre\\\")\\n        self.vars[\\\"direction\\\"] = 0\\n        if now % BAR:\\n            return\\n        rows = closed_window(self.get_candles(self.exchange, self.symbol, \\\"4h\\\"),\\n                             now, 64)\\n        if rows is None:\\n            self.vars[\\\"invalid_windows\\\"] = self.vars.get(\\\"invalid_windows\\\", 0) + 1\\n            self._invalid_event(now)\\n            return\\n        assert math.isclose(float(rows[-1, 2]), float(self.price),\\n                            rel_tol=1e-10, abs_tol=1e-8)\\n        # Evaluate/consume before occupancy and account guards, identically in\\n        # both leaves of a comparison. Never defer an occupied event to later.\\n        event = self._event(rows, now)\\n        if event is None:\\n            return\\n        direction = event[\\\"direction\\\"]\\n        assert direction in (-1, 1)\\n        counts = self._r32_counts()\\n        counts[\\\"events\\\"] += 1\\n        self.vars[\\\"signals\\\"] = self.vars.get(\\\"signals\\\", 0) + 1\\n        if not self.START < now < self.FINISH:\\n            return\\n        if self.is_open or self.entry_orders or self.vars.get(\\\"last_exit_at\\\") == now:\\n            counts[\\\"occupied\\\"] += 1\\n            return\\n        atr = atr14(rows)\\n        if atr is None:\\n            counts[\\\"rejected_geometry\\\"] += 1\\n            return\\n        entry = float(self.price)\\n        distance = 2 * atr\\n        target_distance = None if self.TP_R is None else self.TP_R * distance\\n        if target_distance is not None and entry + direction * target_distance <= 0:\\n            counts[\\\"rejected_geometry\\\"] += 1\\n            return\\n        candidate = dict(origin=self.LABEL, direction=direction, entry=entry,\\n            distance=distance, target_distance=target_distance,\\n            hold_hours=self.HOLD_HOURS, order_kind=\\\"MARKET\\\")\\n        plan = legacy_plan(candidate, .5 * max(0.0, float(self.balance)),\\n                           .5 * float(self.available_margin),\\n                           float(self.leverage), float(self.fee_rate))\\n        if plan is None:\\n            counts[\\\"rejected_geometry\\\"] += 1\\n            return\\n        plan.update(signal_at=now, meta=event.get(\\\"meta\\\", {}))\\n        self.vars[\\\"plan\\\"] = plan\\n        self.vars[\\\"direction\\\"] = direction\\n        counts[\\\"plans\\\"] += 1\\n        self._log(\\\"R32_PLAN\\\", dict(label=self.LABEL, time=now,\\n            direction=direction, entry=entry, distance=distance,\\n            qty=plan[\\\"qty\\\"], risk_budget=plan[\\\"risk_budget\\\"],\\n            planned_loss=plan[\\\"planned_loss\\\"], meta=plan[\\\"meta\\\"]))\\n\\n    def on_open_position(self, order):\\n        plan = self.vars[\\\"plan\\\"]\\n        direction = 1 if self.is_long else -1\\n        entry = float(self.position.entry_price)\\n        qty = abs(float(self.position.qty))\\n        assert direction == plan[\\\"direction\\\"]\\n        assert math.isclose(entry, plan[\\\"entry\\\"], rel_tol=1e-10, abs_tol=1e-8)\\n        stop = entry - direction * plan[\\\"distance\\\"]\\n        unit = plan[\\\"distance\\\"] + self.fee_rate * (entry + stop) + .001 * entry\\n        assert stop > 0 and qty * unit <= plan[\\\"risk_budget\\\"] + 1e-6\\n        self.stop_loss = qty, stop\\n        if plan[\\\"target_distance\\\"] is not None:\\n            target = entry + direction * plan[\\\"target_distance\\\"]\\n            assert target > 0\\n            self.take_profit = qty, target\\n        self.vars[\\\"entries\\\"] = self.vars.get(\\\"entries\\\", 0) + 1\\n        counts = self._r32_counts()\\n        counts[\\\"opens\\\"] += 1\\n        counts[\\\"long_opens\\\" if direction == 1 else \\\"short_opens\\\"] += 1\\n        self._log(\\\"R32_OPEN\\\", dict(label=self.LABEL, time=int(self.time),\\n            signal_at=plan[\\\"signal_at\\\"], opened_at=int(self.position.opened_at),\\n            direction=direction, entry=entry, qty=qty,\\n            distance=plan[\\\"distance\\\"], risk_budget=plan[\\\"risk_budget\\\"],\\n            stop=stop, target_distance=plan[\\\"target_distance\\\"],\\n            hold_hours=plan[\\\"hold_hours\\\"]))\\n        self._observe(\\\"open\\\")\\n\\n    def update_position(self):\\n        # Management remains on closed four-hour clocks; MARKET entry at that\\n        # same clock cannot trigger its own time exit.\\n        now = int(self.time)\\n        if now % BAR == 0 and now - int(self.position.opened_at) >= self.HOLD_HOURS * 3600000:\\n            self.liquidate()\\n\\n    def on_close_position(self, order, closed_trade):\\n        counts = self._r32_counts()\\n        pnl = float(closed_trade.pnl)\\n        assert math.isfinite(pnl)\\n        counts[\\\"closes\\\"] += 1\\n        counts[\\\"net\\\"] += pnl\\n        self.vars[\\\"direction\\\"] = 0\\n        self._log(\\\"R32_CLOSE\\\", dict(label=self.LABEL, time=int(self.time), net=pnl))\\n        # Source totals must precede any terminal observer emission.\\n        super().on_close_position(order, closed_trade)\\n\\n    def _emit(self, stage):\\n        super()._emit(stage)\\n        self._log(\\\"R32_SUMMARY\\\", dict(stage=stage, label=self.LABEL,\\n            hold_hours=self.HOLD_HOURS, tp_r=self.TP_R,\\n            risk_total=.01, capital_denominator=\\\"total BTC wallet\\\",\\n            redistribution=False, **self._r32_counts()))\\n\",\"BtcResearchR10Base4h\":\"import json\\nimport math\\n\\nimport numpy as np\\nfrom jesse.strategies import Strategy\\n\\nBAR = 14400000\\nDAY = 86400000\\n\\n\\ndef closed_window(candles, now, count):\\n    \\\"\\\"\\\"Use only consecutive, closed 4h bars; no synthetic gap repair.\\\"\\\"\\\"\\n    rows = candles[candles[:, 0] + BAR <= now][-count:]\\n    if len(rows) != count or rows[-1, 0] != now - BAR:\\n        return None\\n    if not np.all(np.diff(rows[:, 0]) == BAR):\\n        return None\\n    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):\\n        return None\\n    if np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2])):\\n        return None\\n    if np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2])):\\n        return None\\n    return rows\\n\\n\\ndef atr14(rows):\\n    previous = rows[-15:-1, 2]\\n    current = rows[-14:]\\n    tr = np.maximum(current[:, 3] - current[:, 4],\\n                    np.maximum(abs(current[:, 3] - previous), abs(current[:, 4] - previous)))\\n    value = float(np.mean(tr))\\n    return value if math.isfinite(value) and value > 0 else None\\n\\n\\ndef breadth_state(closes):\\n    changes = np.diff(closes)\\n    positive = changes > 0\\n    negative = changes < 0\\n    if int(positive[-6:].sum()) >= 4 and int(positive[-24:].sum()) >= 16:\\n        return 1\\n    if int(negative[-6:].sum()) >= 4 and int(negative[-24:].sum()) >= 16:\\n        return -1\\n    return 0\\n\\n\\ndef breadth_signal(rows):\\n    \\\"\\\"\\\"Count sign persistence, not return magnitudes; consume only new states.\\\"\\\"\\\"\\n    now_state = breadth_state(rows[-25:, 2])\\n    old_state = breadth_state(rows[-26:-1, 2])\\n    return now_state if now_state != old_state else 0\\n\\n\\ndef funding_failure_signal(rows, now, events):\\n    \\\"\\\"\\\"Observe a full post-payment bar; never know or collect the next payment.\\\"\\\"\\\"\\n    event_start = now - BAR\\n    matching = []\\n    for event in events:\\n        raw = int(event[\\\"settled_at\\\"])\\n        effective = raw // 60000 * 60000\\n        if effective == event_start and 0 <= raw - effective <= 1000:\\n            if int(event[\\\"available_at\\\"]) <= now and int(event[\\\"available_at\\\"]) > raw:\\n                matching.append(event)\\n    if len(matching) != 1:\\n        return 0, None\\n    event = matching[0]\\n    rate = float(event[\\\"rate_decimal\\\"])\\n    if not math.isfinite(rate):\\n        return 0, None\\n    pre, post = rows[-2], rows[-1]\\n    if rate > 0 and pre[2] > pre[1] and post[2] < pre[1]:\\n        return -1, dict(settled_at=int(event[\\\"settled_at\\\"]), available_at=int(event[\\\"available_at\\\"]), rate=rate)\\n    if rate < 0 and pre[2] < pre[1] and post[2] > pre[1]:\\n        return 1, dict(settled_at=int(event[\\\"settled_at\\\"]), available_at=int(event[\\\"available_at\\\"]), rate=rate)\\n    return 0, None\\n\\n\\ndef entry_plan(price, capital, margin, leverage, fee, direction, distance):\\n    stop = price - direction * distance\\n    values = (price, capital, margin, leverage, distance, stop)\\n    if direction not in (-1, 1) or not all(math.isfinite(v) and v > 0 for v in values):\\n        return None\\n    if not math.isfinite(fee) or fee < 0:\\n        return None\\n    unit_loss = distance + fee * (price + stop)\\n    # 2% includes both execution fees. The 90% margin ceiling retains the\\n    # historical reserve and does not increase the stop's monetary risk.\\n    risk_qty = 0.02 * capital / unit_loss\\n    margin_qty = 0.90 * margin * leverage / (price * (1 + fee * leverage))\\n    qty = math.floor(min(risk_qty, margin_qty) * 1e8) / 1e8\\n    if qty <= 0:\\n        return None\\n    assert qty * unit_loss <= 0.02 * capital + 1e-6\\n    return dict(qty=qty, price=price, capital=capital, distance=distance,\\n                stop=stop, risk_budget=0.02 * capital,\\n                planned_loss=qty * unit_loss, margin_capped=margin_qty < risk_qty)\\n\\n\\nclass BtcResearchR10Base4h(Strategy):\\n    \\\"\\\"\\\"R10 discovery harness: one BTC position, fixed risk and base costs only.\\\"\\\"\\\"\\n    MODE = \\\"abstract\\\"\\n    START = 1602720000000\\n    FINISH = 1767225600000\\n\\n    def _log(self, label, value):\\n        self.log(label + \\\" \\\" + json.dumps(value, separators=(\\\",\\\", \\\":\\\"), allow_nan=False))\\n\\n    def before(self):\\n        now = int(self.time)\\n        if not self.vars.get(\\\"checked\\\"):\\n            assert self.symbol == \\\"BTC-USDT\\\"\\n            assert self.leverage == 3\\n            assert abs(self.fee_rate - 0.00045) < 1e-12\\n            self.vars[\\\"checked\\\"] = True\\n            self._log(\\\"R10_CONFIG\\\", dict(mode=self.MODE, risk=0.02, aggregate=0.06,\\n                                        leverage=self.leverage, fee=self.fee_rate,\\n                                        margin_buffer=0.90, stop_atr=2, target_r=2, hold_hours=48))\\n        self.vars[\\\"direction\\\"] = 0\\n        rows = closed_window(self.candles, now, 26)\\n        if rows is None:\\n            self.vars[\\\"invalid_windows\\\"] = self.vars.get(\\\"invalid_windows\\\", 0) + 1\\n            return\\n        if self.MODE == \\\"BREADTH\\\":\\n            direction = breadth_signal(rows)\\n            evidence = None\\n        else:\\n            assert self.MODE == \\\"POST_FUNDING\\\"\\n            events = self.get_funding_history(count=6)\\n            assert all(int(e[\\\"available_at\\\"]) <= now for e in events)\\n            direction, evidence = funding_failure_signal(rows, now, events)\\n        if not direction or not self.START < now < self.FINISH:\\n            return\\n        # Signals are evaluated and consumed while occupied as well. No deferred\\n        # order or re-entry from a previously blocked funding/breadth event.\\n        self.vars[\\\"signals\\\"] = self.vars.get(\\\"signals\\\", 0) + 1\\n        if self.is_open or self.entry_orders or self.vars.get(\\\"last_exit_at\\\") == now:\\n            self.vars[\\\"occupied\\\"] = self.vars.get(\\\"occupied\\\", 0) + 1\\n            return\\n        atr = atr14(rows)\\n        if atr is None:\\n            return\\n        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))\\n        plan = entry_plan(float(self.price), capital, float(self.available_margin),\\n                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)\\n        if plan is None or float(self.price) + direction * 2 * plan[\\\"distance\\\"] <= 0:\\n            return\\n        self.vars[\\\"direction\\\"] = direction\\n        self.vars[\\\"plan\\\"] = plan\\n        self.vars[\\\"evidence\\\"] = evidence\\n\\n    def should_long(self):\\n        return self.vars.get(\\\"direction\\\") == 1\\n\\n    def should_short(self):\\n        return self.vars.get(\\\"direction\\\") == -1\\n\\n    def go_long(self):\\n        plan = self.vars[\\\"plan\\\"]\\n        self.buy = plan[\\\"qty\\\"], self.price\\n\\n    def go_short(self):\\n        plan = self.vars[\\\"plan\\\"]\\n        self.sell = plan[\\\"qty\\\"], self.price\\n\\n    def should_cancel_entry(self):\\n        return True\\n\\n    def on_open_position(self, order):\\n        plan = self.vars[\\\"plan\\\"]\\n        direction = 1 if self.is_long else -1\\n        entry = float(self.position.entry_price)\\n        qty = abs(float(self.position.qty))\\n        distance = plan[\\\"distance\\\"]\\n        stop = entry - direction * distance\\n        target = entry + direction * 2 * distance\\n        assert qty * (distance + self.fee_rate * (entry + stop)) <= plan[\\\"risk_budget\\\"] + 1e-6\\n        self.stop_loss = qty, stop\\n        self.take_profit = qty, target\\n        self.vars[\\\"entries\\\"] = self.vars.get(\\\"entries\\\", 0) + 1\\n        self._log(\\\"R10_ENTRY\\\", dict(time=int(self.time), direction=direction, entry=entry,\\n                                   qty=qty, stop=stop, target=target, plan=plan,\\n                                   evidence=self.vars.get(\\\"evidence\\\")))\\n\\n    def update_position(self):\\n        # No ratchet, discretionary exit or same-close reversal. Funding applies\\n        # continuously to actual held quantity, independently of signal inputs.\\n        if int(self.time) - int(self.position.opened_at) >= 12 * BAR:\\n            self.liquidate()\\n\\n    def on_close_position(self, order, closed_trade):\\n        self.vars[\\\"last_exit_at\\\"] = int(self.time)\\n\\n    def before_terminate(self):\\n        self._log(\\\"R10_COUNTERS\\\", dict(signals=self.vars.get(\\\"signals\\\", 0),\\n                                     occupied=self.vars.get(\\\"occupied\\\", 0),\\n                                     entries=self.vars.get(\\\"entries\\\", 0),\\n                                     invalid_windows=self.vars.get(\\\"invalid_windows\\\", 0)))\\n\",\"BtcResearchR16LegacyBase1m\":\"import math\\nimport numpy as np\\nimport jesse.indicators as ta\\n\\nfrom strategies.BtcResearchR11Base1m import BtcResearchR11Base1m\\nfrom strategies.BtcResearchR10Base4h import BAR\\n\\n# Frozen legacy recipe values, not optimizer ranges. The 10bp reserve sizes\\n# conservatively; it is never charged as cash or simulated execution friction.\\nHP = dict(donchian_len=26, ema_fast=20, ema_slow=80, adx_min=26,\\n          stop_atr=2.0, trail_atr=4.2, be_r=2.25)\\nRESERVE = .001\\nLOT = .001\\n\\n\\ndef legacy_history(candles, now):\\n    \\\"\\\"\\\"Keep exposed closed history; cross-route seed parity needs framework audit.\\\"\\\"\\\"\\n    rows = candles[candles[:, 0]+BAR <= now]\\n    if len(rows) < 14 or rows[-1, 0] != now-BAR:\\n        return None\\n    if (not np.all(np.diff(rows[:, 0]) == BAR)\\n            or not np.all(np.isfinite(rows[:, :5]))\\n            or not np.all(rows[:, 1:5] > 0)\\n            or np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2]))\\n            or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2]))):\\n        return None\\n    return rows\\n\\n\\ndef legacy_long(c):\\n    if len(c) < 100:\\n        return None\\n    price = float(c[-1, 2])\\n    fast = float(ta.ema(c, period=20))\\n    slow = ta.ema(c, period=80, sequential=True)\\n    atr, adx, rsi = float(ta.atr(c)), float(ta.adx(c)), float(ta.rsi(c))\\n    entry = float(np.max(c[-27:-1, 3]))\\n    if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):\\n        return None\\n    if not (atr > 0 and entry < price <= entry+atr and price > slow[-1]\\n            and fast > slow[-1] > slow[-5] and adx >= 26\\n            and 52 <= rsi <= 76 and c[-1, 3]-c[-1, 4] <= 3*atr):\\n        return None\\n    distance = 2*atr\\n    if not 0 < distance < entry:\\n        return None\\n    return dict(origin=\\\"LONG_RUNNER\\\", direction=1, entry=entry,\\n                distance=distance, target_distance=None, hold_hours=None,\\n                order_kind=\\\"LIMIT\\\")\\n\\n\\ndef legacy_short(c):\\n    if len(c) < 140:\\n        return None\\n    price = float(c[-1, 2])\\n    macro = ta.ema(c, period=120, sequential=True)\\n    fast, atr, rsi = float(ta.ema(c, period=20)), float(ta.atr(c)), float(ta.rsi(c, period=3))\\n    if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, rsi)):\\n        return None\\n    if not (atr > 0 and macro[-1] > macro[-10] and price > macro[-1]-atr and rsi <= 20):\\n        return None\\n    entry = min(float(c[-1, 4]), price-.25*atr)\\n    distance = fast-entry\\n    if not (atr <= distance <= 3*atr and distance >= 6*.00045*entry):\\n        return None\\n    return dict(origin=\\\"CORE_SHORT\\\", direction=-1, entry=entry,\\n                distance=distance, target_distance=1.5*atr, hold_hours=72,\\n                order_kind=\\\"STOP\\\")\\n\\n\\ndef legacy_supplement(c, mode, previous):\\n    \\\"\\\"\\\"Consume setup before ATR/geometry/account tests, as in each frozen parent.\\\"\\\"\\\"\\n    assert mode in (\\\"K1001\\\", \\\"N204\\\")\\n    w = c[-14:]\\n    if (len(w) < 14 or not np.all(np.isfinite(w))\\n            or not np.all(w[:, 1:] > 0) or not np.all(w[:, 3] >= w[:, 4])):\\n        return None, False\\n    s, t, window = c[-2], c[-1], c[-13:-1]\\n    spans = window[:, 3]-window[:, 4]\\n    q = np.divide(window[:, 5]*(2*window[:, 2]-window[:, 3]-window[:, 4]),\\n                  spans, out=np.zeros(12), where=spans > 0)\\n    cohort = window[q > 0]\\n    vwap = (float(np.sum(cohort[:, 5]*np.mean(cohort[:, [3, 4, 2]], axis=1))\\n                  / np.sum(cohort[:, 5])) if len(cohort) else float(\\\"nan\\\"))\\n    setup = bool(s[2] > c[-14, 2] and np.sum(q) < 0\\n                 and s[2] >= vwap and t[2] < t[1] and t[2] < vwap)\\n    if mode == \\\"K1001\\\" and setup:\\n        changes = c[-13:-1, 2]-c[-14:-2, 2]\\n        path = float(np.sum(np.abs(changes)))\\n        efficiency = float(s[2]-c[-14, 2])/path if path > 0 else float(\\\"nan\\\")\\n        setup = bool(path > 0 and 0 < efficiency <= 1/3)\\n    if not setup or previous:\\n        return None, setup\\n    atr = float(ta.atr(c))\\n    if not math.isfinite(atr) or atr <= 0:\\n        return None, setup\\n    distance = float(max(s[3], t[3])+.25*atr-t[2])\\n    if not atr <= distance <= 3*atr:\\n        return None, setup\\n    entry = float(min(s[4], t[4])) if mode == \\\"K1001\\\" else float(t[2])\\n    if mode == \\\"K1001\\\" and not (math.isfinite(entry) and entry > 2*distance and entry < t[2]):\\n        return None, setup\\n    if not (math.isfinite(entry) and math.isfinite(distance) and 0 < distance < entry):\\n        return None, setup\\n    return dict(origin=\\\"SUPPLEMENT\\\", direction=-1, entry=entry,\\n                distance=distance, target_distance=2*distance, hold_hours=48,\\n                order_kind=\\\"STOP\\\" if mode == \\\"K1001\\\" else \\\"MARKET\\\",\\n                anchor=vwap), setup\\n\\n\\ndef legacy_plan(event, capital, margin, leverage, fee):\\n    \\\"\\\"\\\"BTC100%; preserve reserve/lot, with the common 90%-margin fee buffer.\\\"\\\"\\\"\\n    entry, distance, direction = event[\\\"entry\\\"], event[\\\"distance\\\"], event[\\\"direction\\\"]\\n    stop = entry-direction*distance\\n    if (direction not in (-1, 1)\\n            or not all(math.isfinite(v) and v > 0 for v in\\n                       (entry, distance, stop, capital, margin, leverage))\\n            or not math.isfinite(fee) or fee < 0):\\n        return None\\n    unit = distance+fee*(entry+stop)+RESERVE*entry\\n    budget = .02*capital\\n    risk_qty = budget/unit\\n    gross_qty = 4.4*capital/entry  # Legacy ceiling; 3x margin prevents 4.4x exposure.\\n    margin_qty = .90*margin*leverage/(entry*(1+fee*leverage))\\n    qty = math.floor(min(risk_qty, gross_qty, margin_qty)/LOT)*LOT\\n    if qty <= 0:\\n        return None\\n    assert qty*unit <= budget+1e-6\\n    return dict(event, qty=qty, risk_budget=budget, planned_loss=qty*unit,\\n                planned_stop_fees=qty*(distance+fee*(entry+stop)),\\n                margin_limited=margin_qty < risk_qty,\\n                gross_limited=gross_qty < risk_qty,\\n                reserve=RESERVE)\\n\\n\\nclass BtcResearchR16LegacyBase1m(BtcResearchR11Base1m):\\n    MODE = \\\"abstract\\\"\\n\\n    def _ledger(self):\\n        return self.vars.setdefault(\\\"legacy_ledger\\\", {\\n            name: dict(fills=0, closes=0, net=0.0)\\n            for name in (\\\"LONG_RUNNER\\\", \\\"CORE_SHORT\\\", \\\"SUPPLEMENT\\\")})\\n\\n    def before(self):\\n        now = int(self.time)\\n        if not self.vars.get(\\\"checked\\\"):\\n            assert self.symbol == \\\"BTC-USDT\\\" and self.timeframe == \\\"1m\\\"\\n            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12\\n            assert abs(self.balance-10000) < 1e-6\\n            assert self.MODE in (\\\"K1001\\\", \\\"N204\\\")\\n            self.vars[\\\"checked\\\"] = True\\n        self._observe(\\\"pre\\\")\\n        self.vars[\\\"direction\\\"] = 0\\n        if now % BAR:\\n            return\\n        # Advance the price machine once, independently of occupancy. Actual\\n        # framework cancellation may re-enter should_* in this same4h cycle.\\n        self.vars[\\\"decision_at\\\"] = now\\n        rows = legacy_history(self.get_candles(self.exchange, self.symbol, \\\"4h\\\"), now)\\n        self.vars[\\\"legacy_rows\\\"] = rows\\n        if rows is None:\\n            self.vars[\\\"previous_setup\\\"] = False\\n            self.vars[\\\"invalid_windows\\\"] = self.vars.get(\\\"invalid_windows\\\", 0)+1\\n            return\\n        self.vars[\\\"history_min\\\"] = min(self.vars.get(\\\"history_min\\\", len(rows)), len(rows))\\n        self.vars[\\\"history_max\\\"] = max(self.vars.get(\\\"history_max\\\", len(rows)), len(rows))\\n        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)\\n        event, setup = legacy_supplement(rows, self.MODE, self.vars.get(\\\"previous_setup\\\", False))\\n        self.vars[\\\"previous_setup\\\"] = setup\\n        self.vars[\\\"supplement_event\\\"] = event\\n        self.vars[\\\"supplement_events\\\"] = self.vars.get(\\\"supplement_events\\\", 0)+int(event is not None)\\n        if self.is_open or self.entry_orders:\\n            self.vars[\\\"occupied\\\"] = self.vars.get(\\\"occupied\\\", 0)+1\\n\\n    def _prepare_entry(self):\\n        \\\"\\\"\\\"Memoize after broker cancellation releases margin; preserve one plan.\\\"\\\"\\\"\\n        now = int(self.time)\\n        if (now % BAR or self.vars.get(\\\"decision_at\\\") != now\\n                or self.is_open or self.entry_orders\\n                or self.vars.get(\\\"last_exit_at\\\") == now\\n                or not self.START < now < self.FINISH):\\n            return 0\\n        if self.vars.get(\\\"prepared_at\\\") == now:\\n            return self.vars.get(\\\"direction\\\", 0)\\n        self.vars[\\\"prepared_at\\\"] = now\\n        rows = self.vars.get(\\\"legacy_rows\\\")\\n        if rows is None:\\n            return 0\\n        # Priority includes account eligibility: if a higher recipe cannot size,\\n        # the next original recipe is considered, exactly as the frozen parents.\\n        for candidate in (legacy_long(rows), legacy_short(rows),\\n                          self.vars.get(\\\"supplement_event\\\")):\\n            if candidate is None:\\n                continue\\n            plan = legacy_plan(candidate, max(0.0, float(self.balance)),\\n                               float(self.available_margin), float(self.leverage),\\n                               float(self.fee_rate))\\n            if plan is not None:\\n                self.vars[\\\"plan\\\"] = dict(plan, signal_at=now, expiry=now+BAR)\\n                self.vars[\\\"direction\\\"] = plan[\\\"direction\\\"]\\n                self.vars[\\\"signals\\\"] = self.vars.get(\\\"signals\\\", 0)+1\\n                return plan[\\\"direction\\\"]\\n        return 0\\n\\n    def should_long(self):\\n        return self._prepare_entry() == 1\\n\\n    def should_short(self):\\n        return self._prepare_entry() == -1\\n\\n    def _submit(self, direction):\\n        plan = self.vars[\\\"plan\\\"]\\n        assert self.vars.get(\\\"submitted_at\\\") != int(self.time), \\\"P_DUPLICATE_SUBMISSION\\\"\\n        assert self.vars.get(\\\"direction\\\") == direction\\n        assert int(self.time) == plan[\\\"signal_at\\\"] and not self.is_open and not self.entry_orders\\n        self.vars[\\\"submitted_at\\\"] = int(self.time)\\n        self.vars[\\\"pending_plan\\\"] = dict(plan)\\n        if direction == 1:\\n            self.buy = plan[\\\"qty\\\"], plan[\\\"entry\\\"]\\n        else:\\n            self.sell = plan[\\\"qty\\\"], plan[\\\"entry\\\"]\\n\\n    def go_long(self):\\n        self._submit(1)\\n\\n    def go_short(self):\\n        self._submit(-1)\\n\\n    def should_cancel_entry(self):\\n        plan = self.vars.get(\\\"pending_plan\\\")\\n        assert plan is not None, \\\"P_PENDING_WITHOUT_PLAN\\\"\\n        due = int(self.time) % BAR == 0 and int(self.time) >= plan[\\\"expiry\\\"]\\n        if due:\\n            self.vars[\\\"pending_plan\\\"] = None\\n            self.vars[\\\"cancellations\\\"] = self.vars.get(\\\"cancellations\\\", 0)+1\\n        return due\\n\\n    def on_open_position(self, order):\\n        plan = self.vars[\\\"pending_plan\\\"]\\n        assert plan is not None and self.vars.get(\\\"position_plan\\\") is None\\n        now = int(self.time)\\n        assert plan[\\\"signal_at\\\"] <= now <= plan[\\\"expiry\\\"], \\\"P_FILL_OUTSIDE_ORDER_LIFE\\\"\\n        assert plan[\\\"signal_at\\\"] <= int(self.position.opened_at) <= plan[\\\"expiry\\\"]\\n        direction = 1 if self.is_long else -1\\n        assert direction == plan[\\\"direction\\\"]\\n        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))\\n        stop = entry-direction*plan[\\\"distance\\\"]\\n        target = (entry+direction*plan[\\\"target_distance\\\"]\\n                  if plan[\\\"target_distance\\\"] is not None else None)\\n        loss = qty*(plan[\\\"distance\\\"]+self.fee_rate*(entry+stop)+RESERVE*entry)\\n        assert math.isfinite(loss) and stop > 0 and (target is None or target > 0)\\n        assert loss <= plan[\\\"risk_budget\\\"]+1e-6, \\\"P_ACTUAL_FILL_RISK\\\"\\n        assert abs(qty-plan[\\\"qty\\\"]) < 1e-8, \\\"P_UNEXPECTED_FILL_QUANTITY\\\"\\n        # Frozen geometry is placed relative to actual fill, never order price.\\n        self.stop_loss = qty, stop\\n        if target is not None:\\n            self.take_profit = qty, target\\n        self.vars[\\\"position_plan\\\"] = dict(plan, actual_entry=entry, actual_loss=loss,\\n                                          filled_at=int(self.position.opened_at))\\n        self.vars[\\\"pending_plan\\\"] = None\\n        self.vars[\\\"best_close\\\"] = entry\\n        self._ledger()[plan[\\\"origin\\\"]][\\\"fills\\\"] += 1\\n        self.vars[\\\"entries\\\"] = self.vars.get(\\\"entries\\\", 0)+1\\n        self._observe(\\\"open\\\")\\n        self._log(\\\"R16_LEGACY_OPEN\\\", dict(mode=self.MODE, origin=plan[\\\"origin\\\"], time=now,\\n            opened_at=int(self.position.opened_at), signal_at=plan[\\\"signal_at\\\"],\\n            expiry=plan[\\\"expiry\\\"], order_kind=plan[\\\"order_kind\\\"],\\n            requested_entry=plan[\\\"entry\\\"], actual_entry=entry, qty=qty,\\n            distance=plan[\\\"distance\\\"], stop=stop, target=target,\\n            risk_budget=plan[\\\"risk_budget\\\"], actual_loss=loss,\\n            planned_loss=plan[\\\"planned_loss\\\"], planned_stop_fees=plan[\\\"planned_stop_fees\\\"],\\n            margin_limited=plan[\\\"margin_limited\\\"], reserve=RESERVE))\\n\\n    def update_position(self):\\n        now = int(self.time)\\n        if now % BAR:\\n            return\\n        plan = self.vars[\\\"position_plan\\\"]\\n        opened = plan[\\\"filled_at\\\"]\\n        if plan[\\\"hold_hours\\\"] is not None:\\n            if now-opened >= plan[\\\"hold_hours\\\"]*3600000:\\n                self.liquidate()\\n            return\\n        # A close completed before the fill cannot improve its trailing stop.\\n        if now <= opened:\\n            return\\n        rows = self.vars.get(\\\"legacy_rows\\\")\\n        if rows is None or self.vars.get(\\\"decision_at\\\") != now:\\n            return\\n        atr = float(ta.atr(rows))\\n        if not math.isfinite(atr) or atr <= 0:\\n            return\\n        entry = plan[\\\"actual_entry\\\"]\\n        self.vars[\\\"best_close\\\"] = max(self.vars[\\\"best_close\\\"], float(rows[-1, 2]))\\n        best_r = (self.vars[\\\"best_close\\\"]-entry)/plan[\\\"distance\\\"]\\n        mult = 4.2\\n        if best_r >= 8:\\n            mult *= .62\\n        elif best_r >= 5:\\n            mult *= .78\\n        stop = self.vars[\\\"best_close\\\"]-mult*atr\\n        if best_r >= 2.25:\\n            stop = max(stop, entry*(1+2.5*self.fee_rate))\\n        if self.average_stop_loss < stop < self.price:\\n            self.stop_loss = abs(float(self.position.qty)), stop\\n\\n    def on_close_position(self, order, closed_trade):\\n        plan = self.vars[\\\"position_plan\\\"]\\n        row = self._ledger()[plan[\\\"origin\\\"]]\\n        pnl = float(closed_trade.pnl)\\n        assert math.isfinite(pnl)\\n        row[\\\"closes\\\"] += 1\\n        row[\\\"net\\\"] += pnl\\n        self.vars[\\\"position_plan\\\"] = None\\n        self.vars[\\\"pending_plan\\\"] = None\\n        self._log(\\\"R16_LEGACY_CLOSE\\\", dict(time=int(self.time), origin=plan[\\\"origin\\\"], net=pnl))\\n        # R11 can emit FINAL here; source totals must already include this close.\\n        super().on_close_position(order, closed_trade)\\n\\n    def _emit(self, stage):\\n        super()._emit(stage)\\n        rows = self._ledger()\\n        self._log(\\\"R16_LEGACY_STATS\\\", dict(stage=stage, mode=self.MODE, sources=rows,\\n            fills=sum(r[\\\"fills\\\"] for r in rows.values()),\\n            closes=sum(r[\\\"closes\\\"] for r in rows.values()),\\n            net=sum(r[\\\"net\\\"] for r in rows.values()),\\n            supplement_events=self.vars.get(\\\"supplement_events\\\", 0),\\n            cancellations=self.vars.get(\\\"cancellations\\\", 0),\\n            history_min=self.vars.get(\\\"history_min\\\"), history_max=self.vars.get(\\\"history_max\\\")))\\n\"}")
BAR = 14400000
RESERVE = .001
LOT = .001
checks = []
fixtures = 0

def check(name, condition):
    assert bool(condition), name
    checks.append(name)

def supplied(name, wanted):
    tree = ast.parse(SOURCES[name], filename="<supplied:"+name+">")
    body = [node for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.ClassDef))
            and node.name in wanted]
    assert len(body) == len(wanted)
    exec(compile(ast.Module(body=body, type_ignores=[]),
                 "<supplied:"+name+">", "exec"), globals())

class BtcResearchR11Base1m:
    START = 0
    FINISH = 10**15

    def _observe(self, stage):
        self.observed.append(stage)
        return self.balance

    def _log(self, label, payload):
        # Serialize exactly like R11, without writing observed market data.
        line = label+" "+json.dumps(payload, separators=(",", ":"), allow_nan=False)
        assert len(line) < 1900
        self.logs.append((label, dict(payload)))

supplied("BtcResearchR10Base4h", {"closed_window", "atr14"})
supplied("BtcResearchR16LegacyBase1m", {"legacy_plan"})
supplied("BtcResearchR32SpecialistBase1m", {"BtcResearchR32SpecialistBase1m"})
supplied("BtcResearchR32FailureBase1m", {"failure_pattern", "BtcResearchR32FailureBase1m"})
supplied("BtcResearchR32FailureAll1m", {"BtcResearchR32FailureAll1m"})
supplied("BtcResearchR32FailurePersist1m", {"BtcResearchR32FailurePersist1m"})

def fixture(side=1, resolution=100.):
    rows = np.array([[i*BAR,100.,100.,101.,99.,1.] for i in range(64)])
    for idx, close in ((61,102. if side == 1 else 98.), (62,100.), (63,resolution)):
        rows[idx,1:5] = (100.,close,max(101.,close+.1),min(99.,close-.1))
    return rows

def mirror(rows):
    result = rows.copy()
    result[:,1] = 200.-rows[:,1]
    result[:,2] = 200.-rows[:,2]
    result[:,3] = 200.-rows[:,4]
    result[:,4] = 200.-rows[:,3]
    return result

def oracle(rows):
    # Ordinary Python loop, not NumPy reductions or production category branches.
    context = list(rows)[-29:-3]
    lo = min(float(row[4]) for row in context)
    hi = max(float(row[3]) for row in context)
    cb,cf,cr = [float(row[2]) for row in list(rows)[-3:]]
    if not hi > lo or lo <= cb <= hi or not lo < cf < hi:
        return None
    side = 1 if cb > hi else -1
    location = -1 if cr < lo else 1 if cr > hi else 0
    category = ("boundary" if cr in (lo,hi) else
                "interior" if location == 0 else
                "recovered_original" if location == side else "crossed_opposite")
    return side, category, lo, hi

def leaf(cls, rows, now=None):
    obj = cls()
    obj.vars = {}
    obj.logs, obj.observed = [], []
    obj.time = int(rows[-1,0])+BAR if now is None else now
    obj.price = float(rows[-1,2])
    obj.symbol, obj.timeframe, obj.exchange = "BTC-USDT", "1m", "synthetic"
    obj.leverage, obj.fee_rate = 3, .00045
    obj.balance = obj.available_margin = 10000.
    obj.is_open, obj.entry_orders = False, []
    obj.get_candles = lambda exchange,symbol,timeframe: rows
    return obj

# AST surface prevents a leaf from replacing execution, hooks, sizing or exits.
for name in ("BtcResearchR32FailureBase1m", "BtcResearchR32FailureAll1m", "BtcResearchR32FailurePersist1m"):
    tree = ast.parse(SOURCES[name])
    methods = [node.name for cls in tree.body if isinstance(cls,ast.ClassDef)
               for node in cls.body if isinstance(node,ast.FunctionDef)]
    check("economic_surface_"+name,
          methods == (["_event"] if name.endswith("Base1m") else []))
check("shared_contract", BtcResearchR32FailureAll1m.HOLD_HOURS == 48
      and BtcResearchR32FailurePersist1m.HOLD_HOURS == 48
      and BtcResearchR32FailureAll1m.TP_R == BtcResearchR32FailurePersist1m.TP_R == 2.)
check("distinct_policy_labels", BtcResearchR32FailureAll1m.LABEL != BtcResearchR32FailurePersist1m.LABEL)

expected_by_resolution = {98.:"crossed_opposite",99.:"boundary",100.:"interior",
                          101.:"boundary",102.:"recovered_original"}
for close, expected in expected_by_resolution.items():
    original = fixture(resolution=close)
    for data in (original,mirror(original)):
        fixtures += 1
        independent = oracle(data)
        pattern = failure_pattern(data)
        assert independent is not None
        assert pattern["category"] == expected == independent[1]
        assert pattern["breakout_side"] == independent[0]
        assert (pattern["lower"],pattern["upper"]) == independent[2:]
        assert (pattern["breakout_at"],pattern["failure_at"],pattern["resolution_at"]) == (61*BAR,62*BAR,63*BAR)
        all_leaf = leaf(BtcResearchR32FailureAll1m,data)
        persist_leaf = leaf(BtcResearchR32FailurePersist1m,data)
        ea = all_leaf._event(data,64*BAR)
        ep = persist_leaf._event(data,64*BAR)
        assert ea["direction"] == -independent[0]
        assert (ep is not None) == (expected == "interior")
        if ep is not None:
            assert ep == ea
        pa, pp = all_leaf.logs[0][1],persist_leaf.logs[0][1]
        assert {k:v for k,v in pa.items() if k not in ("policy","selected")} == {k:v for k,v in pp.items() if k not in ("policy","selected")}
        assert pa["selected"] and pp["selected"] == (expected == "interior")
check("four_categories_reflection_and_common_raw_mask",fixtures == 10)

# Full control versus filtered policy on a fabricated finite grid: no prices observed.
grid_fixtures = 0
for cb in (98.,99.,100.,101.,102.):
    for cf in (98.,99.,100.,101.,102.):
        for cr in (98.,99.,100.,101.,102.):
            data = fixture(resolution=cr)
            for idx,close in ((61,cb),(62,cf)):
                data[idx,1:5] = (100.,close,max(101.,close+.1),min(99.,close-.1))
            expected = oracle(data)
            actual = failure_pattern(data)
            assert (actual is None) == (expected is None)
            if actual is not None:
                assert (actual["breakout_side"],actual["category"],actual["lower"],actual["upper"]) == expected
            grid_fixtures += 1
check("independent_125_grid_oracle",grid_fixtures == 125)

data = fixture()
base_pattern = failure_pattern(data)
check("known_26_plus_3_boundaries",base_pattern["lower"] == 99. and base_pattern["upper"] == 101.)
for index in (35,60):
    changed = data.copy()
    changed[index,3] = 104.
    check("context_endpoint_"+str(index),failure_pattern(changed) is None)
for index in (34,0):
    changed = data.copy()
    changed[index,1:5] = (10000.,10000.,10001.,9999.)
    check("valid_old_row_formula_invariant_"+str(index),failure_pattern(changed) == base_pattern)
for index in (61,62,63):
    changed = data.copy()
    changed[index,3], changed[index,4] = 150.,50.
    check("signal_extrema_not_boundary_"+str(index),failure_pattern(changed) == base_pattern)
flat = data.copy()
flat[:,1:5] = (100.,100.,100.,100.)
check("zero_context_range_cash",failure_pattern(flat) is None)
for index in (61,62):
    for close in (99.,101.):
        changed = data.copy()
        changed[index,2] = close
        check("strict_break_or_return_"+str(index)+"_"+str(close),failure_pattern(changed) is None)

# Future bars are excluded by the real closed_window, with asof parity separate.
future = np.array([[64*BAR,1e5,1e5,1e5,1e5,1.],
                   [65*BAR,1e6,1e6,1e6,1e6,1.]])
appended = np.vstack((data,future))
check("prefix_future_mutation",np.array_equal(closed_window(appended,64*BAR,64),data))
check("input_not_mutated",np.array_equal(data,fixture()))
obj = leaf(BtcResearchR32FailureAll1m,appended,64*BAR)
obj.price = 100.
obj.before()
check("asof_full_source_before",obj.vars["direction"] == -1 and obj.vars["plan"]["signal_at"] == 64*BAR)
check("quota_and_market_plan",obj.vars["plan"]["risk_budget"] == 100.
      and obj.vars["plan"]["entry"] == 100.
      and obj.vars["plan"]["order_kind"] == "MARKET"
      and obj.vars["plan"]["origin"] == obj.LABEL)
check("distance_and_management",obj.vars["plan"]["distance"] == 2*atr14(data)
      and obj.vars["plan"]["target_distance"] == 2*obj.vars["plan"]["distance"]
      and obj.vars["plan"]["hold_hours"] == 48)
check("reserve_lot_margin",obj.vars["plan"]["reserve"] == .001
      and abs(obj.vars["plan"]["qty"]/.001-round(obj.vars["plan"]["qty"]/.001)) < 1e-8
      and obj.vars["plan"]["planned_loss"] <= 100.+1e-6)
check("observer_once_per_before",obj.observed == ["pre"])

for occupied in ("position","pending","same_exit"):
    obj = leaf(BtcResearchR32FailureAll1m,data)
    if occupied == "position":
        obj.is_open = True
    elif occupied == "pending":
        obj.entry_orders = [object()]
    else:
        obj.vars["last_exit_at"] = obj.time
    obj.before()
    check("consumed_"+occupied,obj.vars["direction"] == 0
          and obj._r32_counts()["occupied"] == 1 and len(obj.logs) == 1)
    obj.is_open, obj.entry_orders = False,[]
    obj.vars.pop("last_exit_at",None)
    obj.before()
    check("no_queue_same_timestamp_"+occupied,obj.vars["direction"] == 0
          and len(obj.logs) == 1)
    count = len(obj.logs)
    check("backward_noop_"+occupied,obj._event(data,obj.time-BAR) is None
          and len(obj.logs) == count and obj.vars["r32_b_last_event"] == obj.time)

# Next close cannot recycle the identical old breakout; a different triplet may rearm.
extra = np.vstack((data,[[64*BAR,100.,100.,101.,99.,1.]]))
obj = leaf(BtcResearchR32FailureAll1m,data)
check("initial_pattern",obj._event(data,64*BAR) is not None)
check("old_breakout_expired",obj._event(extra,65*BAR) is None and len(obj.logs) == 1)
new_rows = data.copy()
new_rows[:,0] += 4*BAR
check("new_timestamp_pattern_can_rearm",obj._event(new_rows,68*BAR) is not None and len(obj.logs) == 2)

for kind in ("gap","old_invalid","future_clock"):
    bad = data.copy()
    if kind == "gap":
        bad[10,0] += BAR
    elif kind == "old_invalid":
        bad[0,2] = float("nan")
    else:
        bad[-1,0] += BAR
    obj = leaf(BtcResearchR32FailureAll1m,bad,64*BAR)
    obj.price = 100.
    obj.before()
    check("shared_64_integrity_"+kind,obj.vars["direction"] == 0
          and obj.vars["invalid_windows"] == 1 and not obj.logs)
obj = leaf(BtcResearchR32FailureAll1m,data)
obj.price = 100.1
try:
    obj.before()
except AssertionError:
    mismatch = True
else:
    mismatch = False
check("asof_mismatch_before_pattern_log",mismatch and not obj.logs)

obj = leaf(BtcResearchR32FailurePersist1m,fixture(resolution=102.))
obj.before()
check("filter_before_occupancy_and_sizing",obj.vars["direction"] == 0
      and obj.logs[0][0] == "R32_B_PATTERN"
      and not obj.logs[0][1]["selected"] and "plan" not in obj.vars)
max_pattern_line = max(len(label+" "+json.dumps(payload,separators=(",",":"),allow_nan=False))
                       for label,payload in obj.logs)
check("compact_pattern_record",max_pattern_line < 1900)

result = dict(status="PASS",checks=len(checks),check_names=checks,
              fabricated_grid=grid_fixtures,reflected_fixtures=fixtures,
              max_checked_pattern_chars=max_pattern_line,
              versions=dict(python=__import__("sys").version,numpy=np.__version__),
              source_hashes={name:hashlib.sha256(source.encode()).hexdigest()
                             for name,source in SOURCES.items()},
              limitations=["Supplied source and fabricated arrays only.",
                           "R11 observer is a stub; common execution has its separate receipt.",
                           "No native orders, observed prices, funding ledger or economic backtest certified."])
Path("output").mkdir(exist_ok=True)
Path("output/b_failure_check.json").write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False),encoding="utf-8")
print(json.dumps(result,ensure_ascii=False,allow_nan=False))
```
