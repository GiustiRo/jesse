# K1001 cuota — supplied-source check técnico, NO ejecutado

Base congelada: 5f41d87af1eeb629a381d6bcc63de8595897646357864f9e28a913b3e631c884. Preparado para revisión root y eventual ejecución en un único slot de análisis. No ejecutar desde Markdown como una estrategia; es comprobación sintética con textos suministrados, sin imports de estrategias/framework ni precios observados. El reporte incluirá Python/NumPy/Pandas y hashes de los siete textos. El código escribe sólo un resultado JSON en output/ dentro del workspace temporal de análisis.

Estado: código preparado, cero jobs lanzados por este agente. No se afirma que pase ni que valide un broker real. La revisión independiente encontró el fallo de ledger dependiente de traza y el implementador lo corrigió antes de este congelado; el caso de regresión está incluido. Raíz revisará antes de ejecutar. Toda limitación de stubs figura también en el resultado previsto.

```python
SOURCES = {"BtcResearchR16LegacyBase1m":"import math\nimport numpy as np\nimport jesse.indicators as ta\n\nfrom strategies.BtcResearchR11Base1m import BtcResearchR11Base1m\nfrom strategies.BtcResearchR10Base4h import BAR\n\n# Frozen legacy recipe values, not optimizer ranges. The 10bp reserve sizes\n# conservatively; it is never charged as cash or simulated execution friction.\nHP = dict(donchian_len=26, ema_fast=20, ema_slow=80, adx_min=26,\n          stop_atr=2.0, trail_atr=4.2, be_r=2.25)\nRESERVE = .001\nLOT = .001\n\n\ndef legacy_history(candles, now):\n    \"\"\"Keep exposed closed history; cross-route seed parity needs framework audit.\"\"\"\n    rows = candles[candles[:, 0]+BAR <= now]\n    if len(rows) < 14 or rows[-1, 0] != now-BAR:\n        return None\n    if (not np.all(np.diff(rows[:, 0]) == BAR)\n            or not np.all(np.isfinite(rows[:, :5]))\n            or not np.all(rows[:, 1:5] > 0)\n            or np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2]))\n            or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2]))):\n        return None\n    return rows\n\n\ndef legacy_long(c):\n    if len(c) < 100:\n        return None\n    price = float(c[-1, 2])\n    fast = float(ta.ema(c, period=20))\n    slow = ta.ema(c, period=80, sequential=True)\n    atr, adx, rsi = float(ta.atr(c)), float(ta.adx(c)), float(ta.rsi(c))\n    entry = float(np.max(c[-27:-1, 3]))\n    if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):\n        return None\n    if not (atr > 0 and entry < price <= entry+atr and price > slow[-1]\n            and fast > slow[-1] > slow[-5] and adx >= 26\n            and 52 <= rsi <= 76 and c[-1, 3]-c[-1, 4] <= 3*atr):\n        return None\n    distance = 2*atr\n    if not 0 < distance < entry:\n        return None\n    return dict(origin=\"LONG_RUNNER\", direction=1, entry=entry,\n                distance=distance, target_distance=None, hold_hours=None,\n                order_kind=\"LIMIT\")\n\n\ndef legacy_short(c):\n    if len(c) < 140:\n        return None\n    price = float(c[-1, 2])\n    macro = ta.ema(c, period=120, sequential=True)\n    fast, atr, rsi = float(ta.ema(c, period=20)), float(ta.atr(c)), float(ta.rsi(c, period=3))\n    if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, rsi)):\n        return None\n    if not (atr > 0 and macro[-1] > macro[-10] and price > macro[-1]-atr and rsi <= 20):\n        return None\n    entry = min(float(c[-1, 4]), price-.25*atr)\n    distance = fast-entry\n    if not (atr <= distance <= 3*atr and distance >= 6*.00045*entry):\n        return None\n    return dict(origin=\"CORE_SHORT\", direction=-1, entry=entry,\n                distance=distance, target_distance=1.5*atr, hold_hours=72,\n                order_kind=\"STOP\")\n\n\ndef legacy_supplement(c, mode, previous):\n    \"\"\"Consume setup before ATR/geometry/account tests, as in each frozen parent.\"\"\"\n    assert mode in (\"K1001\", \"N204\")\n    w = c[-14:]\n    if (len(w) < 14 or not np.all(np.isfinite(w))\n            or not np.all(w[:, 1:] > 0) or not np.all(w[:, 3] >= w[:, 4])):\n        return None, False\n    s, t, window = c[-2], c[-1], c[-13:-1]\n    spans = window[:, 3]-window[:, 4]\n    q = np.divide(window[:, 5]*(2*window[:, 2]-window[:, 3]-window[:, 4]),\n                  spans, out=np.zeros(12), where=spans > 0)\n    cohort = window[q > 0]\n    vwap = (float(np.sum(cohort[:, 5]*np.mean(cohort[:, [3, 4, 2]], axis=1))\n                  / np.sum(cohort[:, 5])) if len(cohort) else float(\"nan\"))\n    setup = bool(s[2] > c[-14, 2] and np.sum(q) < 0\n                 and s[2] >= vwap and t[2] < t[1] and t[2] < vwap)\n    if mode == \"K1001\" and setup:\n        changes = c[-13:-1, 2]-c[-14:-2, 2]\n        path = float(np.sum(np.abs(changes)))\n        efficiency = float(s[2]-c[-14, 2])/path if path > 0 else float(\"nan\")\n        setup = bool(path > 0 and 0 < efficiency <= 1/3)\n    if not setup or previous:\n        return None, setup\n    atr = float(ta.atr(c))\n    if not math.isfinite(atr) or atr <= 0:\n        return None, setup\n    distance = float(max(s[3], t[3])+.25*atr-t[2])\n    if not atr <= distance <= 3*atr:\n        return None, setup\n    entry = float(min(s[4], t[4])) if mode == \"K1001\" else float(t[2])\n    if mode == \"K1001\" and not (math.isfinite(entry) and entry > 2*distance and entry < t[2]):\n        return None, setup\n    if not (math.isfinite(entry) and math.isfinite(distance) and 0 < distance < entry):\n        return None, setup\n    return dict(origin=\"SUPPLEMENT\", direction=-1, entry=entry,\n                distance=distance, target_distance=2*distance, hold_hours=48,\n                order_kind=\"STOP\" if mode == \"K1001\" else \"MARKET\",\n                anchor=vwap), setup\n\n\ndef legacy_plan(event, capital, margin, leverage, fee):\n    \"\"\"BTC100%; preserve reserve/lot, with the common 90%-margin fee buffer.\"\"\"\n    entry, distance, direction = event[\"entry\"], event[\"distance\"], event[\"direction\"]\n    stop = entry-direction*distance\n    if (direction not in (-1, 1)\n            or not all(math.isfinite(v) and v > 0 for v in\n                       (entry, distance, stop, capital, margin, leverage))\n            or not math.isfinite(fee) or fee < 0):\n        return None\n    unit = distance+fee*(entry+stop)+RESERVE*entry\n    budget = .02*capital\n    risk_qty = budget/unit\n    gross_qty = 4.4*capital/entry  # Legacy ceiling; 3x margin prevents 4.4x exposure.\n    margin_qty = .90*margin*leverage/(entry*(1+fee*leverage))\n    qty = math.floor(min(risk_qty, gross_qty, margin_qty)/LOT)*LOT\n    if qty <= 0:\n        return None\n    assert qty*unit <= budget+1e-6\n    return dict(event, qty=qty, risk_budget=budget, planned_loss=qty*unit,\n                planned_stop_fees=qty*(distance+fee*(entry+stop)),\n                margin_limited=margin_qty < risk_qty,\n                gross_limited=gross_qty < risk_qty,\n                reserve=RESERVE)\n\n\nclass BtcResearchR16LegacyBase1m(BtcResearchR11Base1m):\n    MODE = \"abstract\"\n\n    def _ledger(self):\n        return self.vars.setdefault(\"legacy_ledger\", {\n            name: dict(fills=0, closes=0, net=0.0)\n            for name in (\"LONG_RUNNER\", \"CORE_SHORT\", \"SUPPLEMENT\")})\n\n    def before(self):\n        now = int(self.time)\n        if not self.vars.get(\"checked\"):\n            assert self.symbol == \"BTC-USDT\" and self.timeframe == \"1m\"\n            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12\n            assert abs(self.balance-10000) < 1e-6\n            assert self.MODE in (\"K1001\", \"N204\")\n            self.vars[\"checked\"] = True\n        self._observe(\"pre\")\n        self.vars[\"direction\"] = 0\n        if now % BAR:\n            return\n        # Advance the price machine once, independently of occupancy. Actual\n        # framework cancellation may re-enter should_* in this same4h cycle.\n        self.vars[\"decision_at\"] = now\n        rows = legacy_history(self.get_candles(self.exchange, self.symbol, \"4h\"), now)\n        self.vars[\"legacy_rows\"] = rows\n        if rows is None:\n            self.vars[\"previous_setup\"] = False\n            self.vars[\"invalid_windows\"] = self.vars.get(\"invalid_windows\", 0)+1\n            return\n        self.vars[\"history_min\"] = min(self.vars.get(\"history_min\", len(rows)), len(rows))\n        self.vars[\"history_max\"] = max(self.vars.get(\"history_max\", len(rows)), len(rows))\n        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)\n        event, setup = legacy_supplement(rows, self.MODE, self.vars.get(\"previous_setup\", False))\n        self.vars[\"previous_setup\"] = setup\n        self.vars[\"supplement_event\"] = event\n        self.vars[\"supplement_events\"] = self.vars.get(\"supplement_events\", 0)+int(event is not None)\n        if self.is_open or self.entry_orders:\n            self.vars[\"occupied\"] = self.vars.get(\"occupied\", 0)+1\n\n    def _prepare_entry(self):\n        \"\"\"Memoize after broker cancellation releases margin; preserve one plan.\"\"\"\n        now = int(self.time)\n        if (now % BAR or self.vars.get(\"decision_at\") != now\n                or self.is_open or self.entry_orders\n                or self.vars.get(\"last_exit_at\") == now\n                or not self.START < now < self.FINISH):\n            return 0\n        if self.vars.get(\"prepared_at\") == now:\n            return self.vars.get(\"direction\", 0)\n        self.vars[\"prepared_at\"] = now\n        rows = self.vars.get(\"legacy_rows\")\n        if rows is None:\n            return 0\n        # Priority includes account eligibility: if a higher recipe cannot size,\n        # the next original recipe is considered, exactly as the frozen parents.\n        for candidate in (legacy_long(rows), legacy_short(rows),\n                          self.vars.get(\"supplement_event\")):\n            if candidate is None:\n                continue\n            plan = legacy_plan(candidate, max(0.0, float(self.balance)),\n                               float(self.available_margin), float(self.leverage),\n                               float(self.fee_rate))\n            if plan is not None:\n                self.vars[\"plan\"] = dict(plan, signal_at=now, expiry=now+BAR)\n                self.vars[\"direction\"] = plan[\"direction\"]\n                self.vars[\"signals\"] = self.vars.get(\"signals\", 0)+1\n                return plan[\"direction\"]\n        return 0\n\n    def should_long(self):\n        return self._prepare_entry() == 1\n\n    def should_short(self):\n        return self._prepare_entry() == -1\n\n    def _submit(self, direction):\n        plan = self.vars[\"plan\"]\n        assert self.vars.get(\"submitted_at\") != int(self.time), \"P_DUPLICATE_SUBMISSION\"\n        assert self.vars.get(\"direction\") == direction\n        assert int(self.time) == plan[\"signal_at\"] and not self.is_open and not self.entry_orders\n        self.vars[\"submitted_at\"] = int(self.time)\n        self.vars[\"pending_plan\"] = dict(plan)\n        if direction == 1:\n            self.buy = plan[\"qty\"], plan[\"entry\"]\n        else:\n            self.sell = plan[\"qty\"], plan[\"entry\"]\n\n    def go_long(self):\n        self._submit(1)\n\n    def go_short(self):\n        self._submit(-1)\n\n    def should_cancel_entry(self):\n        plan = self.vars.get(\"pending_plan\")\n        assert plan is not None, \"P_PENDING_WITHOUT_PLAN\"\n        due = int(self.time) % BAR == 0 and int(self.time) >= plan[\"expiry\"]\n        if due:\n            self.vars[\"pending_plan\"] = None\n            self.vars[\"cancellations\"] = self.vars.get(\"cancellations\", 0)+1\n        return due\n\n    def on_open_position(self, order):\n        plan = self.vars[\"pending_plan\"]\n        assert plan is not None and self.vars.get(\"position_plan\") is None\n        now = int(self.time)\n        assert plan[\"signal_at\"] <= now <= plan[\"expiry\"], \"P_FILL_OUTSIDE_ORDER_LIFE\"\n        assert plan[\"signal_at\"] <= int(self.position.opened_at) <= plan[\"expiry\"]\n        direction = 1 if self.is_long else -1\n        assert direction == plan[\"direction\"]\n        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))\n        stop = entry-direction*plan[\"distance\"]\n        target = (entry+direction*plan[\"target_distance\"]\n                  if plan[\"target_distance\"] is not None else None)\n        loss = qty*(plan[\"distance\"]+self.fee_rate*(entry+stop)+RESERVE*entry)\n        assert math.isfinite(loss) and stop > 0 and (target is None or target > 0)\n        assert loss <= plan[\"risk_budget\"]+1e-6, \"P_ACTUAL_FILL_RISK\"\n        assert abs(qty-plan[\"qty\"]) < 1e-8, \"P_UNEXPECTED_FILL_QUANTITY\"\n        # Frozen geometry is placed relative to actual fill, never order price.\n        self.stop_loss = qty, stop\n        if target is not None:\n            self.take_profit = qty, target\n        self.vars[\"position_plan\"] = dict(plan, actual_entry=entry, actual_loss=loss,\n                                          filled_at=int(self.position.opened_at))\n        self.vars[\"pending_plan\"] = None\n        self.vars[\"best_close\"] = entry\n        self._ledger()[plan[\"origin\"]][\"fills\"] += 1\n        self.vars[\"entries\"] = self.vars.get(\"entries\", 0)+1\n        self._observe(\"open\")\n        self._log(\"R16_LEGACY_OPEN\", dict(mode=self.MODE, origin=plan[\"origin\"], time=now,\n            opened_at=int(self.position.opened_at), signal_at=plan[\"signal_at\"],\n            expiry=plan[\"expiry\"], order_kind=plan[\"order_kind\"],\n            requested_entry=plan[\"entry\"], actual_entry=entry, qty=qty,\n            distance=plan[\"distance\"], stop=stop, target=target,\n            risk_budget=plan[\"risk_budget\"], actual_loss=loss,\n            planned_loss=plan[\"planned_loss\"], planned_stop_fees=plan[\"planned_stop_fees\"],\n            margin_limited=plan[\"margin_limited\"], reserve=RESERVE))\n\n    def update_position(self):\n        now = int(self.time)\n        if now % BAR:\n            return\n        plan = self.vars[\"position_plan\"]\n        opened = plan[\"filled_at\"]\n        if plan[\"hold_hours\"] is not None:\n            if now-opened >= plan[\"hold_hours\"]*3600000:\n                self.liquidate()\n            return\n        # A close completed before the fill cannot improve its trailing stop.\n        if now <= opened:\n            return\n        rows = self.vars.get(\"legacy_rows\")\n        if rows is None or self.vars.get(\"decision_at\") != now:\n            return\n        atr = float(ta.atr(rows))\n        if not math.isfinite(atr) or atr <= 0:\n            return\n        entry = plan[\"actual_entry\"]\n        self.vars[\"best_close\"] = max(self.vars[\"best_close\"], float(rows[-1, 2]))\n        best_r = (self.vars[\"best_close\"]-entry)/plan[\"distance\"]\n        mult = 4.2\n        if best_r >= 8:\n            mult *= .62\n        elif best_r >= 5:\n            mult *= .78\n        stop = self.vars[\"best_close\"]-mult*atr\n        if best_r >= 2.25:\n            stop = max(stop, entry*(1+2.5*self.fee_rate))\n        if self.average_stop_loss < stop < self.price:\n            self.stop_loss = abs(float(self.position.qty)), stop\n\n    def on_close_position(self, order, closed_trade):\n        plan = self.vars[\"position_plan\"]\n        row = self._ledger()[plan[\"origin\"]]\n        pnl = float(closed_trade.pnl)\n        assert math.isfinite(pnl)\n        row[\"closes\"] += 1\n        row[\"net\"] += pnl\n        self.vars[\"position_plan\"] = None\n        self.vars[\"pending_plan\"] = None\n        self._log(\"R16_LEGACY_CLOSE\", dict(time=int(self.time), origin=plan[\"origin\"], net=pnl))\n        # R11 can emit FINAL here; source totals must already include this close.\n        super().on_close_position(order, closed_trade)\n\n    def _emit(self, stage):\n        super()._emit(stage)\n        rows = self._ledger()\n        self._log(\"R16_LEGACY_STATS\", dict(stage=stage, mode=self.MODE, sources=rows,\n            fills=sum(r[\"fills\"] for r in rows.values()),\n            closes=sum(r[\"closes\"] for r in rows.values()),\n            net=sum(r[\"net\"] for r in rows.values()),\n            supplement_events=self.vars.get(\"supplement_events\", 0),\n            cancellations=self.vars.get(\"cancellations\", 0),\n            history_min=self.vars.get(\"history_min\"), history_max=self.vars.get(\"history_max\")))\n","BtcResearchR16LegacyK1001m":"from strategies.BtcResearchR16LegacyBase1m import BtcResearchR16LegacyBase1m\n\n\nclass BtcResearchR16LegacyK1001m(BtcResearchR16LegacyBase1m):\n    MODE = \"K1001\"\n","BtcResearchR11Base1m":"import json\nimport math\nfrom datetime import datetime, timezone\n\nimport numpy as np\nfrom jesse.strategies import Strategy\nfrom strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan\n\n\ndef cusum_step(rows, accumulators):\n    \"\"\"Transfer the R40 design:60 past log returns, drift0.25, boundary4.\"\"\"\n    returns = np.diff(np.log(rows[-62:, 2]))\n    sigma = float(np.std(returns[:-1], ddof=1))\n    if not math.isfinite(sigma) or sigma <= 0:\n        return 0, (0.0, 0.0)\n    z = float((returns[-1] - np.mean(returns[:-1])) / sigma)\n    if not math.isfinite(z):\n        return 0, (0.0, 0.0)\n    up = max(0.0, accumulators[0] + z - 0.25)\n    down = max(0.0, accumulators[1] - z - 0.25)\n    if up >= 4 or down >= 4:\n        direction = 0 if up >= 4 and down >= 4 else 1 if up >= 4 else -1\n        return direction, (0.0, 0.0)\n    return 0, (up, down)\n\n\ndef absorption_signal(rows):\n    \"\"\"Large volume but small body, followed by escape of that closed bar.\"\"\"\n    window, setup, confirmation = rows[-26:-2], rows[-2], rows[-1]\n    if not np.all(np.isfinite(rows[-26:, 5])) or np.any(rows[-26:, 5] < 0):\n        return 0\n    average_volume = float(np.mean(window[:, 5]))\n    prior_atr = atr14(window)\n    if not math.isfinite(average_volume) or average_volume <= 0 or prior_atr is None:\n        return 0\n    if setup[5] < 2 * average_volume or abs(setup[2] - setup[1]) > 0.25 * prior_atr:\n        return 0\n    if confirmation[2] > setup[3]:\n        return 1\n    if confirmation[2] < setup[4]:\n        return -1\n    return 0\n\n\ndef month_name(timestamp):\n    return datetime.fromtimestamp(timestamp / 1000, timezone.utc).strftime(\"%Y-%m\")\n\n\ndef monthly_summary(boundaries, active_months):\n    \"\"\"Declared post-settlement/pre-decision UTC cuts; no00:01 approximation.\"\"\"\n    points = sorted(boundaries.items())\n    months = []\n    for (start, before), (finish, after) in zip(points, points[1:]):\n        stamp = datetime.fromtimestamp(start / 1000, timezone.utc)\n        month = stamp.strftime(\"%Y-%m\")\n        complete = stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0\n        if before <= 0:\n            continue\n        months.append(dict(month=month, start=start, finish=finish,\n                           complete=complete, active=month in active_months,\n                           pnl=after-before, return_fraction=after/before-1))\n    complete = [m for m in months if m[\"complete\"]]\n    active = [m for m in complete if m[\"active\"]]\n    quarter_groups = {}\n    for m in months:\n        quarter = m[\"month\"][:4] + \"Q\" + str((int(m[\"month\"][5:])-1)//3+1)\n        quarter_groups.setdefault(quarter, []).append(m)\n    quarters = [q for q in quarter_groups.values()\n                if len(q) == 3 and all(m[\"complete\"] for m in q)]\n    returns = [m[\"return_fraction\"] for m in complete]\n    contributions = sorted([m[\"pnl\"] for m in months], reverse=True)\n    return dict(months=months, complete_months=len(complete), active_months=len(active),\n                positive_active=sum(m[\"pnl\"] > 0 for m in active),\n                positive_calendar=sum(m[\"pnl\"] > 0 for m in complete),\n                median_return=float(np.median(returns)) if returns else None,\n                complete_quarters=len(quarters),\n                positive_quarters=sum(sum(m[\"pnl\"] for m in q) > 0 for q in quarters),\n                pnl_without_best_two=sum(m[\"pnl\"] for m in months)-sum(contributions[:2]))\n\n\nclass BtcResearchR11Base1m(Strategy):\n    \"\"\"M1 accounting observer; signal and management decisions remain4h.\"\"\"\n    MODE = \"abstract\"\n    START = 1602720000000\n    FINISH = 1767225600000\n\n    def _log(self, label, payload):\n        # Event logs stay small; monthly history is emitted as separate rows.\n        self.log(label + \" \" + json.dumps(payload, separators=(\",\", \":\"), allow_nan=False))\n\n    def _observe(self, stage):\n        now = int(self.time)\n        # BTC-only futures equity. portfolio_value multiplies open PnL by\n        # leverage in this checkout, so it is deliberately not used here.\n        equity = float(self.balance) + (float(self.position.pnl) if self.is_open else 0.0)\n        assert math.isfinite(equity)\n        self.vars[\"peak\"] = max(self.vars.get(\"peak\", 10000.0), equity)\n        drawdown = equity / self.vars[\"peak\"] - 1\n        self.vars[\"dd\"] = min(self.vars.get(\"dd\", 0.0), drawdown)\n        self.vars[\"sequence\"] = self.vars.get(\"sequence\", 0) + 1\n        self.vars[\"last_equity\"] = equity\n        active = self.vars.setdefault(\"active_months\", set())\n        if self.is_open:\n            # Pre marks describe exposure during the minute that just closed;\n            # an opening fill at T instead belongs to the new interval.\n            active.add(month_name(now if stage == \"open\" else now-1))\n        boundaries = self.vars.setdefault(\"boundaries\", {self.START: 10000.0})\n        if stage == \"pre\":\n            self.vars[\"minute_marks\"] = self.vars.get(\"minute_marks\", 0) + 1\n            stamp = datetime.fromtimestamp(now / 1000, timezone.utc)\n            if stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0:\n                boundaries[now] = equity\n        if now >= self.FINISH:\n            # A later terminal close callback replaces the mark with post-fee equity.\n            boundaries[self.FINISH] = equity\n        return equity\n\n    def before(self):\n        now = int(self.time)\n        if not self.vars.get(\"checked\"):\n            assert self.symbol == \"BTC-USDT\" and self.timeframe == \"1m\"\n            assert self.leverage == 3 and abs(self.fee_rate - 0.00045) < 1e-12\n            assert abs(self.balance - 10000) < 1e-6\n            self.vars[\"checked\"] = True\n        self._observe(\"pre\")\n        self.vars[\"direction\"] = 0\n        # This is signal alignment, not a market-session/calendar filter.\n        if now % BAR != 0:\n            return\n        count = 62 if self.MODE == \"CUSUM\" else 26\n        candles = self.get_candles(self.exchange, self.symbol, \"4h\")\n        rows = closed_window(candles, now, count)\n        if rows is None:\n            self.vars[\"invalid_windows\"] = self.vars.get(\"invalid_windows\", 0) + 1\n            self.vars[\"cusum\"] = (0.0, 0.0)\n            return\n        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)\n        if self.MODE == \"CUSUM\":\n            direction, state = cusum_step(rows, self.vars.get(\"cusum\", (0.0, 0.0)))\n            self.vars[\"cusum\"] = state\n        else:\n            assert self.MODE == \"ABSORPTION\"\n            direction = absorption_signal(rows)\n        if not direction or not self.START < now < self.FINISH:\n            return\n        self.vars[\"signals\"] = self.vars.get(\"signals\", 0) + 1\n        if self.is_open or self.entry_orders or self.vars.get(\"last_exit_at\") == now:\n            self.vars[\"occupied\"] = self.vars.get(\"occupied\", 0) + 1\n            return\n        atr = atr14(rows)\n        if atr is None:\n            return\n        # Flat BTC account: wallet equals equity. Reuse the frozen2% fee-aware\n        # plan, eight-decimal research precision and90% margin ceiling.\n        capital = max(0.0, float(self.balance))\n        plan = entry_plan(float(self.price), capital, float(self.available_margin),\n                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)\n        if plan is None or self.price + direction * 2 * plan[\"distance\"] <= 0:\n            return\n        self.vars[\"direction\"] = direction\n        self.vars[\"plan\"] = plan\n\n    def should_long(self):\n        return self.vars.get(\"direction\") == 1\n\n    def should_short(self):\n        return self.vars.get(\"direction\") == -1\n\n    def go_long(self):\n        self.buy = self.vars[\"plan\"][\"qty\"], self.price\n\n    def go_short(self):\n        self.sell = self.vars[\"plan\"][\"qty\"], self.price\n\n    def should_cancel_entry(self):\n        return True\n\n    def on_open_position(self, order):\n        plan = self.vars[\"plan\"]\n        direction = 1 if self.is_long else -1\n        entry = float(self.position.entry_price)\n        qty = abs(float(self.position.qty))\n        stop = entry - direction * plan[\"distance\"]\n        target = entry + direction * 2 * plan[\"distance\"]\n        assert qty * (plan[\"distance\"] + self.fee_rate * (entry + stop)) <= plan[\"risk_budget\"] + 1e-6\n        self.stop_loss = qty, stop\n        self.take_profit = qty, target\n        self.vars[\"entries\"] = self.vars.get(\"entries\", 0) + 1\n        self._observe(\"open\")\n\n    def update_position(self):\n        # Preserve the four-hour management clock despite the M1 observer.\n        if int(self.time) % BAR == 0 and int(self.time) - int(self.position.opened_at) >= 12 * BAR:\n            self.liquidate()\n\n    def on_close_position(self, order, closed_trade):\n        now = int(self.time)\n        active = self.vars.setdefault(\"active_months\", set())\n        active.add(month_name(now-1))\n        # At a month boundary, retain both the held interval and any fee-only\n        # execution month. Terminal liquidation belongs to the final interval.\n        if now < self.FINISH:\n            active.add(month_name(now))\n        self.vars[\"last_exit_at\"] = now\n        self._observe(\"close\")\n        if now >= self.FINISH and self.vars.get(\"emitted\"):\n            self._emit(\"FINAL\")\n\n    def _emit(self, stage):\n        summary = monthly_summary(self.vars[\"boundaries\"], self.vars.get(\"active_months\", set()))\n        # Emit rows at the end, so one bounded log page can retrieve all months.\n        for item in summary.pop(\"months\"):\n            self._log(\"R11_MONTH\", dict(stage=stage, **item))\n        summary.update(stage=stage, equity=self.vars[\"last_equity\"],\n                       dd_m1_events=self.vars.get(\"dd\", 0),\n                       minute_marks=self.vars.get(\"minute_marks\", 0),\n                       sequence=self.vars.get(\"sequence\", 0),\n                       signals=self.vars.get(\"signals\", 0), entries=self.vars.get(\"entries\", 0),\n                       invalid_windows=self.vars.get(\"invalid_windows\", 0))\n        self._log(\"R11_SUMMARY\", summary)\n\n    def before_terminate(self):\n        self._observe(\"terminal\")\n        self.vars[\"emitted\"] = True\n        self._emit(\"PRETERMINAL\")\n","BtcResearchR10Base4h":"import json\nimport math\n\nimport numpy as np\nfrom jesse.strategies import Strategy\n\nBAR = 14400000\nDAY = 86400000\n\n\ndef closed_window(candles, now, count):\n    \"\"\"Use only consecutive, closed 4h bars; no synthetic gap repair.\"\"\"\n    rows = candles[candles[:, 0] + BAR <= now][-count:]\n    if len(rows) != count or rows[-1, 0] != now - BAR:\n        return None\n    if not np.all(np.diff(rows[:, 0]) == BAR):\n        return None\n    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):\n        return None\n    if np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2])):\n        return None\n    if np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2])):\n        return None\n    return rows\n\n\ndef atr14(rows):\n    previous = rows[-15:-1, 2]\n    current = rows[-14:]\n    tr = np.maximum(current[:, 3] - current[:, 4],\n                    np.maximum(abs(current[:, 3] - previous), abs(current[:, 4] - previous)))\n    value = float(np.mean(tr))\n    return value if math.isfinite(value) and value > 0 else None\n\n\ndef breadth_state(closes):\n    changes = np.diff(closes)\n    positive = changes > 0\n    negative = changes < 0\n    if int(positive[-6:].sum()) >= 4 and int(positive[-24:].sum()) >= 16:\n        return 1\n    if int(negative[-6:].sum()) >= 4 and int(negative[-24:].sum()) >= 16:\n        return -1\n    return 0\n\n\ndef breadth_signal(rows):\n    \"\"\"Count sign persistence, not return magnitudes; consume only new states.\"\"\"\n    now_state = breadth_state(rows[-25:, 2])\n    old_state = breadth_state(rows[-26:-1, 2])\n    return now_state if now_state != old_state else 0\n\n\ndef funding_failure_signal(rows, now, events):\n    \"\"\"Observe a full post-payment bar; never know or collect the next payment.\"\"\"\n    event_start = now - BAR\n    matching = []\n    for event in events:\n        raw = int(event[\"settled_at\"])\n        effective = raw // 60000 * 60000\n        if effective == event_start and 0 <= raw - effective <= 1000:\n            if int(event[\"available_at\"]) <= now and int(event[\"available_at\"]) > raw:\n                matching.append(event)\n    if len(matching) != 1:\n        return 0, None\n    event = matching[0]\n    rate = float(event[\"rate_decimal\"])\n    if not math.isfinite(rate):\n        return 0, None\n    pre, post = rows[-2], rows[-1]\n    if rate > 0 and pre[2] > pre[1] and post[2] < pre[1]:\n        return -1, dict(settled_at=int(event[\"settled_at\"]), available_at=int(event[\"available_at\"]), rate=rate)\n    if rate < 0 and pre[2] < pre[1] and post[2] > pre[1]:\n        return 1, dict(settled_at=int(event[\"settled_at\"]), available_at=int(event[\"available_at\"]), rate=rate)\n    return 0, None\n\n\ndef entry_plan(price, capital, margin, leverage, fee, direction, distance):\n    stop = price - direction * distance\n    values = (price, capital, margin, leverage, distance, stop)\n    if direction not in (-1, 1) or not all(math.isfinite(v) and v > 0 for v in values):\n        return None\n    if not math.isfinite(fee) or fee < 0:\n        return None\n    unit_loss = distance + fee * (price + stop)\n    # 2% includes both execution fees. The 90% margin ceiling retains the\n    # historical reserve and does not increase the stop's monetary risk.\n    risk_qty = 0.02 * capital / unit_loss\n    margin_qty = 0.90 * margin * leverage / (price * (1 + fee * leverage))\n    qty = math.floor(min(risk_qty, margin_qty) * 1e8) / 1e8\n    if qty <= 0:\n        return None\n    assert qty * unit_loss <= 0.02 * capital + 1e-6\n    return dict(qty=qty, price=price, capital=capital, distance=distance,\n                stop=stop, risk_budget=0.02 * capital,\n                planned_loss=qty * unit_loss, margin_capped=margin_qty < risk_qty)\n\n\nclass BtcResearchR10Base4h(Strategy):\n    \"\"\"R10 discovery harness: one BTC position, fixed risk and base costs only.\"\"\"\n    MODE = \"abstract\"\n    START = 1602720000000\n    FINISH = 1767225600000\n\n    def _log(self, label, value):\n        self.log(label + \" \" + json.dumps(value, separators=(\",\", \":\"), allow_nan=False))\n\n    def before(self):\n        now = int(self.time)\n        if not self.vars.get(\"checked\"):\n            assert self.symbol == \"BTC-USDT\"\n            assert self.leverage == 3\n            assert abs(self.fee_rate - 0.00045) < 1e-12\n            self.vars[\"checked\"] = True\n            self._log(\"R10_CONFIG\", dict(mode=self.MODE, risk=0.02, aggregate=0.06,\n                                        leverage=self.leverage, fee=self.fee_rate,\n                                        margin_buffer=0.90, stop_atr=2, target_r=2, hold_hours=48))\n        self.vars[\"direction\"] = 0\n        rows = closed_window(self.candles, now, 26)\n        if rows is None:\n            self.vars[\"invalid_windows\"] = self.vars.get(\"invalid_windows\", 0) + 1\n            return\n        if self.MODE == \"BREADTH\":\n            direction = breadth_signal(rows)\n            evidence = None\n        else:\n            assert self.MODE == \"POST_FUNDING\"\n            events = self.get_funding_history(count=6)\n            assert all(int(e[\"available_at\"]) <= now for e in events)\n            direction, evidence = funding_failure_signal(rows, now, events)\n        if not direction or not self.START < now < self.FINISH:\n            return\n        # Signals are evaluated and consumed while occupied as well. No deferred\n        # order or re-entry from a previously blocked funding/breadth event.\n        self.vars[\"signals\"] = self.vars.get(\"signals\", 0) + 1\n        if self.is_open or self.entry_orders or self.vars.get(\"last_exit_at\") == now:\n            self.vars[\"occupied\"] = self.vars.get(\"occupied\", 0) + 1\n            return\n        atr = atr14(rows)\n        if atr is None:\n            return\n        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))\n        plan = entry_plan(float(self.price), capital, float(self.available_margin),\n                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)\n        if plan is None or float(self.price) + direction * 2 * plan[\"distance\"] <= 0:\n            return\n        self.vars[\"direction\"] = direction\n        self.vars[\"plan\"] = plan\n        self.vars[\"evidence\"] = evidence\n\n    def should_long(self):\n        return self.vars.get(\"direction\") == 1\n\n    def should_short(self):\n        return self.vars.get(\"direction\") == -1\n\n    def go_long(self):\n        plan = self.vars[\"plan\"]\n        self.buy = plan[\"qty\"], self.price\n\n    def go_short(self):\n        plan = self.vars[\"plan\"]\n        self.sell = plan[\"qty\"], self.price\n\n    def should_cancel_entry(self):\n        return True\n\n    def on_open_position(self, order):\n        plan = self.vars[\"plan\"]\n        direction = 1 if self.is_long else -1\n        entry = float(self.position.entry_price)\n        qty = abs(float(self.position.qty))\n        distance = plan[\"distance\"]\n        stop = entry - direction * distance\n        target = entry + direction * 2 * distance\n        assert qty * (distance + self.fee_rate * (entry + stop)) <= plan[\"risk_budget\"] + 1e-6\n        self.stop_loss = qty, stop\n        self.take_profit = qty, target\n        self.vars[\"entries\"] = self.vars.get(\"entries\", 0) + 1\n        self._log(\"R10_ENTRY\", dict(time=int(self.time), direction=direction, entry=entry,\n                                   qty=qty, stop=stop, target=target, plan=plan,\n                                   evidence=self.vars.get(\"evidence\")))\n\n    def update_position(self):\n        # No ratchet, discretionary exit or same-close reversal. Funding applies\n        # continuously to actual held quantity, independently of signal inputs.\n        if int(self.time) - int(self.position.opened_at) >= 12 * BAR:\n            self.liquidate()\n\n    def on_close_position(self, order, closed_trade):\n        self.vars[\"last_exit_at\"] = int(self.time)\n\n    def before_terminate(self):\n        self._log(\"R10_COUNTERS\", dict(signals=self.vars.get(\"signals\", 0),\n                                     occupied=self.vars.get(\"occupied\", 0),\n                                     entries=self.vars.get(\"entries\", 0),\n                                     invalid_windows=self.vars.get(\"invalid_windows\", 0)))\n","BtcResearchR16K1001QuotaBase1m":"import math\nfrom datetime import datetime, timezone\n\nfrom strategies.BtcResearchR16LegacyK1001m import BtcResearchR16LegacyK1001m\nfrom strategies.BtcResearchR16LegacyBase1m import legacy_long, legacy_short, legacy_plan\nfrom strategies.BtcResearchR10Base4h import BAR\n\n# The account still starts at10000. Both halves are fixed allocations of its\n# current wallet/free margin, not a second account or a redistribution rule.\nQUOTA = .5\n\n\ndef quota_counts():\n    return dict(fills=0, closes=0, net=0.0, trace_completed=0, trace_missing=0)\n\n\ndef quota_year(timestamp):\n    return str(datetime.fromtimestamp(timestamp / 1000, timezone.utc).year)\n\n\nclass BtcResearchR16K1001QuotaBase1m(BtcResearchR16LegacyK1001m):\n    \"\"\"Original K1001 groups with1% total-account risk; observational trace only.\n\n    before, supplement latch, indicators, order lifetime and management remain\n    inherited. Only the permitted group and the .5/.5 sizing arguments change.\n    Observed R uses open0, later closed M1 marks and the actual exit fill; it is\n    neither intraminute MFE/MAE nor a counterfactual path after the real exit.\n    \"\"\"\n    GROUP = \"abstract\"\n\n    def _quota_state(self):\n        state = self.vars.get(\"k1001_quota\")\n        if state is None:\n            assert self.GROUP in (\"LONG_ONLY\", \"SHORT_BOOK\")\n            state = dict(active=None, trade_sequence=0, last_fill_identity=None, errors={},\n                         sources={name: quota_counts() for name in\n                                  (\"LONG_RUNNER\", \"CORE_SHORT\", \"SUPPLEMENT\")},\n                         open_years={}, close_years={})\n            self.vars[\"k1001_quota\"] = state\n            self._log(\"K1001_QUOTA_CONFIG\", dict(\n                group=self.GROUP, mode=self.MODE, account_start=10000,\n                capital_fraction=QUOTA, margin_fraction=QUOTA,\n                target_risk_total=.01, aggregate_limit=.06, leverage=3,\n                reserve=.001, lot=.001, redistribution=False,\n                price_trace=\"open0_pre_strictly_after_open_exit_fill\"))\n        return state\n\n    def _quota_error(self, reason):\n        state = self._quota_state()\n        count = state[\"errors\"].get(reason, 0) + 1\n        state[\"errors\"][reason] = count\n        # Record the first example; counters expose repeated failures without\n        # producing one error line per M1 callback.\n        if count == 1:\n            self._log(\"K1001_QUOTA_TRACE_ERROR\", dict(\n                reason=reason, time=int(self.time), group=self.GROUP))\n\n    def _prepare_entry(self):\n        now = int(self.time)\n        if (now % BAR or self.vars.get(\"decision_at\") != now\n                or self.is_open or self.entry_orders\n                or self.vars.get(\"last_exit_at\") == now\n                or not self.START < now < self.FINISH):\n            return 0\n        if self.vars.get(\"prepared_at\") == now:\n            return self.vars.get(\"direction\", 0)\n        self.vars[\"prepared_at\"] = now\n        rows = self.vars.get(\"legacy_rows\")\n        if rows is None:\n            return 0\n        # Use only the event generated by inherited before. In particular, no\n        # second supplement evaluation or previous_setup write is permitted.\n        if self.GROUP == \"LONG_ONLY\":\n            candidates = (legacy_long(rows),)\n        else:\n            assert self.GROUP == \"SHORT_BOOK\"\n            candidates = (legacy_short(rows), self.vars.get(\"supplement_event\"))\n        capital = max(0.0, float(self.balance))\n        margin = float(self.available_margin)\n        for candidate in candidates:\n            if candidate is None:\n                continue\n            # Keep the frozen .02 helper: .02*.5 ==.01 of this account's wallet.\n            # Its .90 buffer on half free margin leaves the other half unused.\n            plan = legacy_plan(candidate, QUOTA*capital, QUOTA*margin,\n                               float(self.leverage), float(self.fee_rate))\n            if plan is not None:\n                self.vars[\"plan\"] = dict(plan, signal_at=now, expiry=now+BAR)\n                self.vars[\"direction\"] = plan[\"direction\"]\n                self.vars[\"signals\"] = self.vars.get(\"signals\", 0)+1\n                self._log(\"K1001_QUOTA_PLAN\", dict(\n                    time=now, group=self.GROUP, origin=plan[\"origin\"],\n                    qty=plan[\"qty\"], risk_budget=plan[\"risk_budget\"],\n                    capital_total=capital, capital_scaled=QUOTA*capital,\n                    margin_total=margin, margin_scaled=QUOTA*margin,\n                    planned_loss=plan[\"planned_loss\"],\n                    planned_stop_fees=plan[\"planned_stop_fees\"],\n                    reserve=plan[\"reserve\"], gross_limited=plan[\"gross_limited\"],\n                    margin_limited=plan[\"margin_limited\"], expiry=now+BAR))\n                return plan[\"direction\"]\n        return 0\n\n    @staticmethod\n    def _quota_identity(plan):\n        return (plan[\"origin\"], int(plan[\"signal_at\"]), int(plan[\"filled_at\"]),\n                float(plan[\"actual_entry\"]), float(plan[\"qty\"]),\n                float(plan[\"distance\"]), int(plan[\"direction\"]))\n\n    def _quota_start_trace(self):\n        state = self._quota_state()\n        plan = self.vars.get(\"position_plan\")\n        if plan is None:\n            self._quota_error(\"open_without_position_plan\")\n            return\n        identity = self._quota_identity(plan)\n        if state[\"last_fill_identity\"] == identity:\n            return  # Same open hook, not a second executed fill.\n        state[\"last_fill_identity\"] = identity\n        state[\"trade_sequence\"] += 1\n        state[\"sources\"][plan[\"origin\"]][\"fills\"] += 1\n        year = quota_year(identity[2])\n        rows = state[\"open_years\"].setdefault(year, {})\n        rows.setdefault(plan[\"origin\"], quota_counts())[\"fills\"] += 1\n        # Execution counts are independent of whether its observational trace\n        # can be completed. A trace failure must not erase a real native fill.\n        active = state[\"active\"]\n        if active is not None:\n            active[\"broken\"] = True\n            self._quota_error(\"overlapping_trace_identity\")\n            return\n        entry, distance = identity[3], identity[5]\n        if not (math.isfinite(entry) and entry > 0\n                and math.isfinite(distance) and distance > 0):\n            self._quota_error(\"invalid_open_price_or_distance\")\n            return\n        opened = identity[2]\n        state[\"active\"] = dict(\n            identity=identity, trace_id=state[\"trade_sequence\"],\n            origin=plan[\"origin\"], signal_at=int(plan[\"signal_at\"]),\n            opened_at=opened, entry=entry, qty=float(plan[\"qty\"]),\n            distance=distance, direction=int(plan[\"direction\"]),\n            min_r=0.0, max_r=0.0, min_at=opened, max_at=opened,\n            min_stage=\"open\", max_stage=\"open\", first_at=opened,\n            last_at=opened, last_stage=\"open\", last_pre_at=None,\n            marks=1, m1_marks=0, broken=False)\n\n    def _quota_mark(self, trace, price, timestamp, stage):\n        if stage == \"pre\":\n            if timestamp <= trace[\"opened_at\"]:\n                return False  # A close at the fill timestamp is not post-fill.\n            previous = trace[\"last_pre_at\"]\n            if previous is not None and timestamp <= previous:\n                if timestamp < previous:\n                    trace[\"broken\"] = True\n                    self._quota_error(\"backward_pre_timestamp\")\n                return False\n        if not math.isfinite(price) or price <= 0:\n            trace[\"broken\"] = True\n            self._quota_error(\"nonfinite_or_nonpositive_mark\")\n            return False\n        if timestamp < trace[\"last_at\"]:\n            trace[\"broken\"] = True\n            self._quota_error(\"backward_mark_timestamp\")\n            return False\n        value = trace[\"direction\"]*(price-trace[\"entry\"])/trace[\"distance\"]\n        if not math.isfinite(value):\n            trace[\"broken\"] = True\n            self._quota_error(\"nonfinite_price_r\")\n            return False\n        # Strict changes retain the first phase/time on ties. Open and exit\n        # remain distinct even when a real trade has zero holding time.\n        if value < trace[\"min_r\"]:\n            trace.update(min_r=value, min_at=timestamp, min_stage=stage)\n        if value > trace[\"max_r\"]:\n            trace.update(max_r=value, max_at=timestamp, max_stage=stage)\n        trace.update(last_at=timestamp, last_stage=stage, marks=trace[\"marks\"]+1)\n        if stage == \"pre\":\n            trace[\"last_pre_at\"] = timestamp\n            trace[\"m1_marks\"] += 1\n        return True\n\n    def _observe(self, stage):\n        value = super()._observe(stage)\n        # Never call the parent observer twice or alter its returned equity.\n        state = self._quota_state()\n        if stage == \"open\":\n            self._quota_start_trace()\n        elif stage == \"pre\" and self.is_open:\n            trace = state[\"active\"]\n            plan = self.vars.get(\"position_plan\")\n            if trace is None or plan is None:\n                self._quota_error(\"pre_without_trace_or_plan\")\n            elif trace[\"identity\"] != self._quota_identity(plan):\n                trace[\"broken\"] = True\n                self._quota_error(\"pre_identity_mismatch\")\n            else:\n                # self.price here is the same already-closed M1 close supplied\n                # to R11's pre observer. Do not use high/low or later prices.\n                self._quota_mark(trace, float(self.price), int(self.time), \"pre\")\n        return value\n\n    def on_close_position(self, order, closed_trade):\n        # Complete our observer before R16 clears its plan and R11 can emit FINAL.\n        state = self._quota_state()\n        plan = self.vars[\"position_plan\"]\n        origin = plan[\"origin\"]\n        trace = state[\"active\"]\n        complete = False\n        if trace is not None and trace[\"identity\"] == self._quota_identity(plan):\n            marked = self._quota_mark(\n                trace, float(closed_trade.exit_price),\n                int(closed_trade.closed_at), \"exit\")\n            complete = marked and not trace[\"broken\"]\n        else:\n            self._quota_error(\"close_identity_missing_or_mismatch\")\n        net = float(closed_trade.pnl)\n        opened_year = quota_year(int(plan[\"filled_at\"]))\n        closed_year = quota_year(int(closed_trade.closed_at))\n        open_rows = state[\"open_years\"].setdefault(opened_year, {})\n        close_rows = state[\"close_years\"].setdefault(closed_year, {})\n        # All three ledgers refer to executed trades, never signal cohorts.\n        for row in (state[\"sources\"][origin],\n                    open_rows.setdefault(origin, quota_counts()),\n                    close_rows.setdefault(origin, dict(\n                        closes=0, net=0.0, trace_completed=0, trace_missing=0))):\n            row[\"closes\"] += 1\n            row[\"net\"] += net\n            row[\"trace_completed\" if complete else \"trace_missing\"] += 1\n        payload = dict(\n            group=self.GROUP, origin=origin, trade_id=str(closed_trade.id),\n            signal_at=int(plan[\"signal_at\"]), opened_at=int(plan[\"filled_at\"]),\n            closed_at=int(closed_trade.closed_at), entry=float(plan[\"actual_entry\"]),\n            exit=float(closed_trade.exit_price), qty=float(plan[\"qty\"]),\n            distance=float(plan[\"distance\"]), net=net, trace_complete=complete,\n            exit_order_id=str(order.id), exit_order_type=order.type,\n            exit_submitted_via=order.submitted_via)\n        if trace is not None and trace[\"identity\"] == self._quota_identity(plan):\n            payload.update({key: trace[key] for key in (\n                \"trace_id\", \"min_r\", \"max_r\", \"min_at\", \"max_at\", \"min_stage\",\n                \"max_stage\", \"first_at\", \"last_at\", \"last_stage\", \"marks\", \"m1_marks\")})\n        self._log(\"K1001_QUOTA_PRICE_TRACE\", payload)\n        state[\"active\"] = None\n        super().on_close_position(order, closed_trade)\n\n    def _emit(self, stage):\n        super()._emit(stage)\n        state = self._quota_state()\n        self._log(\"K1001_QUOTA_STATS\", dict(\n            stage=stage, group=self.GROUP, sources=state[\"sources\"],\n            open_years=state[\"open_years\"], close_years=state[\"close_years\"],\n            trace_errors=state[\"errors\"],\n            open_trace=state[\"active\"] is not None))\n","BtcResearchR16K1001LongOnly1m":"from strategies.BtcResearchR16K1001QuotaBase1m import BtcResearchR16K1001QuotaBase1m\n\n\nclass BtcResearchR16K1001LongOnly1m(BtcResearchR16K1001QuotaBase1m):\n    GROUP = \"LONG_ONLY\"\n","BtcResearchR16K1001ShortBook1m":"from strategies.BtcResearchR16K1001QuotaBase1m import BtcResearchR16K1001QuotaBase1m\n\n\nclass BtcResearchR16K1001ShortBook1m(BtcResearchR16K1001QuotaBase1m):\n    GROUP = \"SHORT_BOOK\"\n"}

import ast
import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace as NS

import numpy as np
import pandas as pd

EXPECTED_QUOTA_SHA = "5f41d87af1eeb629a381d6bcc63de8595897646357864f9e28a913b3e631c884"
checks = []
def check(condition, name):
    if not bool(condition):
        raise AssertionError(name)
    checks.append(name)

def class_node(source, name):
    return next(node for node in ast.parse(source).body
                if isinstance(node, ast.ClassDef) and node.name == name)

def stubless_tree(source):
    # Imports alone are removed. No import of strategies/framework is executed.
    tree = ast.parse(source)
    tree.body = [node for node in tree.body if not isinstance(node, (ast.Import, ast.ImportFrom))]
    return ast.fix_missing_locations(tree)

class StrategyStub:
    """State/callback stub only: no candle engine, exchange or broker emulation."""
    def __init__(self):
        self.vars, self.logs = {}, []
        self.time = 1602720000000 + 14400000
        self.balance = self.available_margin = 10000.
        self.leverage, self.fee_rate = 3., .00045
        self.price, self.symbol, self.timeframe = 100., "BTC-USDT", "1m"
        self.exchange, self.index = "synthetic", 0
        self.entry_orders, self.is_open = [], False
        self.position = NS(qty=0., entry_price=0., opened_at=0, pnl=0.)
        self.stop_loss = self.take_profit = self.buy = self.sell = None
        self.data, self.liquidations = None, 0
    @property
    def is_long(self):
        return self.is_open and self.position.qty > 0
    @property
    def is_short(self):
        return self.is_open and self.position.qty < 0
    @property
    def average_stop_loss(self):
        return float(self.stop_loss[1]) if self.stop_loss else 0.
    def get_candles(self, exchange, symbol, timeframe):
        assert symbol == self.symbol and timeframe == "4h"
        return self.data
    def liquidate(self):
        self.liquidations += 1
    def log(self, value):
        self.logs.append(str(value))

# Real indicator functions are deliberately not imported or tested here.
ta_stub = NS(
    atr=lambda candles: 2.,
    ema=lambda candles, period=20, sequential=False:
        np.full(len(candles), 100.) if sequential else 100.,
    adx=lambda candles: 0.,
    rsi=lambda candles, period=14: 50.,
)
env = dict(__name__="supplied_quota_check", math=math, np=np, json=json,
           datetime=datetime, timezone=timezone, Strategy=StrategyStub, ta=ta_stub)
order = (
    "BtcResearchR10Base4h", "BtcResearchR11Base1m",
    "BtcResearchR16LegacyBase1m", "BtcResearchR16LegacyK1001m",
    "BtcResearchR16K1001QuotaBase1m", "BtcResearchR16K1001LongOnly1m",
    "BtcResearchR16K1001ShortBook1m",
)
hashes = {name: hashlib.sha256(text.encode("utf-8")).hexdigest()
          for name, text in SOURCES.items()}
check(hashes["BtcResearchR16K1001QuotaBase1m"] == EXPECTED_QUOTA_SHA,
      "frozen_final_quota_hash")
for name in order:
    exec(compile(stubless_tree(SOURCES[name]), name + ".provided", "exec"), env)

R11 = env["BtcResearchR11Base1m"]
R16 = env["BtcResearchR16LegacyBase1m"]
Quota = env["BtcResearchR16K1001QuotaBase1m"]
Long = env["BtcResearchR16K1001LongOnly1m"]
Short = env["BtcResearchR16K1001ShortBook1m"]
BAR = env["BAR"]
quota_methods = {n.name for n in class_node(
    SOURCES["BtcResearchR16K1001QuotaBase1m"], Quota.__name__).body
    if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
check("before" not in quota_methods and "update_position" not in quota_methods
      and "on_open_position" not in quota_methods, "inherit_before_management_open_literal")
check(Quota.before is R16.before and Quota.update_position is R16.update_position
      and Quota.on_open_position is R16.on_open_position, "resolved_parent_methods_identical")
check(Long.MODE == Short.MODE == "K1001", "mode_k1001_unchanged")
check(Long.GROUP == "LONG_ONLY" and Short.GROUP == "SHORT_BOOK", "wrapper_allowlists")
prepare_ast = next(n for n in class_node(
    SOURCES["BtcResearchR16K1001QuotaBase1m"], Quota.__name__).body
    if isinstance(n, ast.FunctionDef) and n.name == "_prepare_entry")
check(not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
              and n.func.id == "legacy_supplement" for n in ast.walk(prepare_ast)),
      "no_supplement_recomputation_in_prepare")

def candles(end, count=240):
    times = end - np.arange(count, 0, -1, dtype=np.int64)*BAR
    return np.column_stack((times, np.full(count, 100.), np.full(count, 100.),
                            np.full(count, 101.), np.full(count, 99.), np.ones(count)))

def event(origin="LONG_RUNNER", entry=100., distance=2.):
    side = 1 if origin == "LONG_RUNNER" else -1
    return dict(origin=origin, direction=side, entry=entry, distance=distance,
                target_distance=None if side == 1 else (3. if origin == "CORE_SHORT" else 4.),
                hold_hours=None if side == 1 else (72 if origin == "CORE_SHORT" else 48),
                order_kind="LIMIT" if side == 1 else "STOP")

real_plan, real_long, real_short = env["legacy_plan"], env["legacy_long"], env["legacy_short"]
real_history, real_supplement = env["legacy_history"], env["legacy_supplement"]

def setup(cls, margin=10000.):
    obj = cls()
    obj.available_margin = float(margin)
    obj.data = candles(obj.time)
    obj.vars.update(decision_at=obj.time, direction=0, legacy_rows=obj.data,
                    supplement_event=event("SUPPLEMENT"))
    return obj

def with_candidates(long_candidate, short_candidate):
    env["legacy_long"] = lambda rows: long_candidate
    env["legacy_short"] = lambda rows: short_candidate

def records(obj, label):
    prefix = label + " "
    return [json.loads(row[len(prefix):]) for row in obj.logs if row.startswith(prefix)]

def expect_assert(callback, name):
    try:
        callback()
    except AssertionError:
        checks.append(name)
    else:
        raise AssertionError(name + ": expected AssertionError")

with_candidates(event(), event("CORE_SHORT"))
s = setup(Long)
check(s._prepare_entry() == 1 and s.vars["plan"]["origin"] == "LONG_RUNNER",
      "long_only_selects_long")
lp = dict(s.vars["plan"])
check(lp["risk_budget"] == .01*s.balance, "risk_budget_one_percent_total_wallet")
check(lp["qty"] == real_plan(event(), 5000., 5000., 3., .00045)["qty"],
      "uses_exact_half_balance_and_margin_arguments")
check(lp["planned_loss"] <= 100.+1e-6 and lp["reserve"] == .001,
      "fee_reserve_in_budget_no_removal")
check(math.isclose(lp["qty"]/.001, round(lp["qty"]/.001), abs_tol=1e-8),
      "legacy_lot_floor")
signals = s.vars["signals"]
env["legacy_long"] = lambda rows: (_ for _ in ()).throw(AssertionError("recomputed memo"))
check(s._prepare_entry() == 1 and s.vars["signals"] == signals, "same_t_plan_memo")
with_candidates(event(), event("CORE_SHORT"))
s = setup(Short)
check(s._prepare_entry() == -1 and s.vars["plan"]["origin"] == "CORE_SHORT",
      "short_book_core_priority_no_long")
# A controlled sizing failure tests priority FALLTHROUGH; actual lot failure is
# separately verified below. This candidate stub does not certify indicator geometry.
def core_cannot_size(candidate, capital, margin, leverage, fee):
    return None if candidate["origin"] == "CORE_SHORT" else real_plan(
        candidate, capital, margin, leverage, fee)
env["legacy_plan"] = core_cannot_size
s = setup(Short)
check(s._prepare_entry() == -1 and s.vars["plan"]["origin"] == "SUPPLEMENT",
      "short_core_size_failure_falls_to_original_supplement")
env["legacy_plan"] = real_plan
with_candidates(None, event("CORE_SHORT"))
s = setup(Long)
check(s._prepare_entry() == 0 and "plan" not in s.vars, "long_does_not_fall_to_short")
with_candidates(event(), event("CORE_SHORT"))

s = setup(Long, margin=10.)
check(s._prepare_entry() == 1, "margin_limited_plan_exists")
p = s.vars["plan"]
expected_qty = math.floor((.9*5.*3./(100.*(1+.00045*3)))/.001)*.001
check(p["qty"] == expected_qty and p["margin_limited"], "half_margin_buffer_and_fee_cap")
check(p["planned_loss"] < p["risk_budget"], "margin_cap_does_not_redistribute_idle_risk")
s = setup(Long, margin=.001)
check(s._prepare_entry() == 0, "zero_after_lot_no_upward_rounding")
s = setup(Short)
s.vars["legacy_rows"] = None
s.vars["supplement_event"] = event("SUPPLEMENT")
check(s._prepare_entry() == 0 and "plan" not in s.vars, "invalid_history_no_stale_event")
s = setup(Short)
s.vars["last_exit_at"] = s.time
check(s._prepare_entry() == 0, "same_exit_guard")
s = setup(Short)
s.entry_orders = [object()]
check(s._prepare_entry() == 0 and "prepared_at" not in s.vars, "pending_guard_before_memo")

# Exercise actual inherited before using a deterministic signal helper spy.
# This verifies callback/state consumption, not the helper's already-frozen economics.
seen_previous = []
def supplement_spy(rows, mode, previous):
    seen_previous.append((mode, previous))
    return (event("SUPPLEMENT") if not previous else None), True
env["legacy_supplement"] = supplement_spy
s = setup(Long)
s.vars.pop("decision_at", None)
s.entry_orders = [object()]
s.before()
check(seen_previous == [("K1001", False)] and s.vars["previous_setup"] is True,
      "parent_before_consumes_latch_even_long_only_pending")
s.time += BAR
s.data = candles(s.time)
s.before()
check(seen_previous[-1] == ("K1001", True) and s.vars["supplement_event"] is None,
      "no_retry_of_consumed_supplement")
env["legacy_history"] = lambda data, now: None
s.time += BAR
s.before()
check(s.vars["previous_setup"] is False and s.vars["legacy_rows"] is None,
      "parent_invalid_history_resets_latch")
env["legacy_history"], env["legacy_supplement"] = real_history, real_supplement

# Broker cancellation is simulated as a callback ordering fixture, not executed.
s = setup(Short)
check(s._prepare_entry() == -1, "ttl_plan_prepared")
s.go_short()
s.entry_orders = [object()]
signal_time = s.time
s.time += 60000
check(s.should_cancel_entry() is False, "pending_not_cancelled_every_m1")
s.time = signal_time + BAR
s.vars.update(decision_at=s.time, direction=0, legacy_rows=candles(s.time))
check(s._prepare_entry() == 0, "cannot_prepare_before_broker_releases_pending")
check(s.should_cancel_entry() is True and s.vars["pending_plan"] is None, "ttl_expiry_cancels")
s.entry_orders = []
s.available_margin = 8000.
check(s._prepare_entry() == -1, "rearm_same_close_after_cancel")
check(records(s, "K1001_QUOTA_PLAN")[-1]["margin_scaled"] == 4000.,
      "sizing_uses_released_margin_not_old_reservation")
s.go_short()
expect_assert(s.go_short, "duplicate_order_submission_same_t_rejected")
s = setup(Long)
s.time += 60000
check(s._prepare_entry() == 0, "no_entry_on_intermediate_m1")
s = setup(Long)
s.time = s.FINISH
s.vars["decision_at"] = s.time
check(s._prepare_entry() == 0, "no_entry_at_finish_boundary")

def open_position(obj, origin="LONG_RUNNER", fill=99., fill_offset=0):
    with_candidates(event(), event("CORE_SHORT"))
    if origin == "SUPPLEMENT":
        env["legacy_short"] = lambda rows: None
    obj.vars.update(direction=0, decision_at=obj.time, legacy_rows=candles(obj.time),
                    supplement_event=event("SUPPLEMENT"))
    obj._prepare_entry()
    plan = obj.vars["plan"]
    (obj.go_long if plan["direction"] == 1 else obj.go_short)()
    obj.time += fill_offset
    obj.price = fill
    obj.position = NS(qty=plan["direction"]*plan["qty"], entry_price=fill,
                      opened_at=obj.time, pnl=0.)
    obj.is_open = True
    obj.on_open_position(NS(id="entry"))
    return dict(obj.vars["position_plan"])

def close_position(obj, exit_price, pnl=12.5, at=None, ident="trade"):
    if at is not None:
        obj.time = int(at)
    trade = NS(id=ident, exit_price=exit_price, closed_at=obj.time, pnl=pnl)
    order = NS(id="exit-"+ident, type="MARKET", submitted_via="synthetic_close")
    obj.balance = 10000.+pnl
    obj.is_open = False
    obj.position = NS(qty=0., entry_price=0., opened_at=0, pnl=0.)
    obj.on_close_position(order, trade)

# Real fill-relative protection and risk assertion, on the supplied parent method.
for cls, origin in ((Long, "LONG_RUNNER"), (Short, "CORE_SHORT"), (Short, "SUPPLEMENT")):
    s = setup(cls)
    p = open_position(s, origin)
    check(s.stop_loss[1] == 99.-p["direction"]*p["distance"],
          origin+"_stop_relative_to_actual_fill")
    target = None if p["target_distance"] is None else 99.+p["direction"]*p["target_distance"]
    check((s.take_profit is None if target is None else s.take_profit[1] == target),
          origin+"_target_policy_preserved")
    check(p["actual_loss"] <= p["risk_budget"]+1e-6 and p["qty"] == s.vars["plan"]["qty"],
          origin+"_actual_fill_fee_reserve_risk")
    if origin != "LONG_RUNNER":
        opened = p["filled_at"]
        due = p["hold_hours"]*3600000
        s.time = opened+due-BAR
        s.update_position()
        check(s.liquidations == 0, origin+"_not_closed_before_deadline")
        s.time = opened+due
        s.update_position()
        check(s.liquidations == 1, origin+"_deadline_preserved")
# An impossible adverse long LIMIT fill is injected solely to prove the parent
# assertion does not silently resize or accept a budget breach.
s = setup(Long)
expect_assert(lambda: open_position(s, fill=1000.), "actual_fill_budget_breach_is_not_silently_repaired")

s = setup(Long)
p = open_position(s)
state = s.vars["k1001_quota"]
trace = state["active"]
check(trace["marks"] == 1 and trace["min_r"] == trace["max_r"] == 0.,
      "open_hook_before_first_before_initializes_zero_trace")
seq, equity = s.vars["sequence"], s.vars["last_equity"]
s._quota_start_trace()
check(state["sources"]["LONG_RUNNER"]["fills"] == 1 and trace["marks"] == 1,
      "duplicate_trace_open_own_ledger_idempotent")
check(s.vars["sequence"] == seq and s.vars["last_equity"] == equity,
      "trace_start_does_not_call_parent_observer")
s.price = 1000.
before_marks = trace["marks"]
returned = s._observe("pre")
check(trace["marks"] == before_marks, "same_timestamp_pre_is_not_post_fill")
check(s.vars["sequence"] == seq+1 and returned == s.balance,
      "parent_observer_once_and_return_preserved")
s.time += 60000
s.price = p["actual_entry"]+2*p["distance"]
s._observe("pre")
first_max_time = trace["max_at"]
s._observe("pre")
check(trace["m1_marks"] == 1 and trace["max_r"] == 2.,
      "duplicate_pre_dedup_own_trace_only")
s.time += 60000
s._observe("pre")
check(trace["max_at"] == first_max_time and trace["m1_marks"] == 2,
      "strict_extreme_keeps_first_tie")
exit_time = s.time
close_position(s, p["actual_entry"]-p["distance"], at=exit_time)
payload = records(s, "K1001_QUOTA_PRICE_TRACE")[-1]
check(payload["trace_complete"] and payload["min_r"] == -1. and payload["max_r"] == 2.,
      "exit_fill_is_in_trace_even_same_t_as_last_pre")
check(payload["m1_marks"] == 2 and payload["marks"] == 4,
      "open_pre_pre_exit_phases_counted")
check(state["sources"]["LONG_RUNNER"] == dict(
    fills=1, closes=1, net=12.5, trace_completed=1, trace_missing=0),
      "own_ledger_matches_real_close_once")

s = setup(Short)
p = open_position(s)
close_position(s, p["actual_entry"]-p["distance"], at=p["filled_at"], ident="zero")
payload = records(s, "K1001_QUOTA_PRICE_TRACE")[-1]
check(payload["trace_complete"] and payload["marks"] == 2 and payload["m1_marks"] == 0,
      "zero_holding_open_zero_and_exit_same_t_both_retained")
check(payload["max_r"] == 1. and payload["max_stage"] == "exit",
      "zero_holding_exit_direction_correct")

# Force a broken diagnostic record before a valid native fill. Execution counts
# MUST remain complete even though the trace is missing.
s = setup(Long)
qstate = s._quota_state()
qstate["active"] = dict(identity=("corrupt-old-trace",), broken=False)
p = open_position(s)
check(qstate["sources"]["LONG_RUNNER"]["fills"] == 1,
      "regression_fill_not_erased_when_trace_start_fails")
close_position(s, p["actual_entry"], ident="broken")
check(qstate["sources"]["LONG_RUNNER"]["closes"] == 1
      and qstate["sources"]["LONG_RUNNER"]["trace_missing"] == 1,
      "broken_trace_close_keeps_ledger_and_missing_evidence")
check(qstate["errors"].get("overlapping_trace_identity") == 1
      and qstate["errors"].get("close_identity_missing_or_mismatch") == 1,
      "broken_trace_is_not_silently_repaired")

# Terminal parent callback can emit FINAL. Own close/trace must already be final.
s = setup(Long)
p = open_position(s)
s.time, s.price = s.FINISH, p["actual_entry"]+p["distance"]
s.before_terminate()
check(records(s, "K1001_QUOTA_STATS")[-1]["open_trace"] is True,
      "preterminal_may_show_real_open_trace")
close_position(s, s.price, at=s.FINISH, ident="terminal")
final = [r for r in records(s, "K1001_QUOTA_STATS") if r["stage"] == "FINAL"][-1]
check(final["sources"]["LONG_RUNNER"]["closes"] == 1 and not final["open_trace"],
      "own_close_finalized_before_parent_final")
final_before = json.dumps(s.vars["k1001_quota"], sort_keys=True)
s._emit("FINAL")
check(json.dumps(s.vars["k1001_quota"], sort_keys=True) == final_before,
      "repeat_final_emit_does_not_recount_own_ledger")

# A trace-free observational subclass retains the SAME quota selector and native
# lifecycle. Compare economics under identical synthetic callback outcomes only.
class TraceMutedQuota(Quota):
    _observe = R11._observe
    on_close_position = R16.on_close_position
    _emit = R16._emit

def economics_fixture(cls, group):
    s = setup(cls)
    s.GROUP = group
    p = open_position(s, "LONG_RUNNER" if group == "LONG_ONLY" else "CORE_SHORT")
    s.time += BAR
    s.vars.update(legacy_rows=candles(s.time), decision_at=s.time)
    s.price = 115. if group == "LONG_ONLY" else 97.
    s._observe("pre")
    s.update_position()
    out = dict(qty=p["qty"], risk=p["risk_budget"], stop=s.stop_loss,
               target=s.take_profit, liquidations=s.liquidations,
               entries=s.vars["entries"])
    close_position(s, s.price, at=s.time, ident="invariance")
    out.update(balance=s.balance, native_ledger=s.vars["legacy_ledger"],
               boundaries=s.vars["boundaries"], active=sorted(s.vars["active_months"]),
               minute_marks=s.vars.get("minute_marks"), sequence=s.vars["sequence"])
    return out
for cls, group in ((Long, "LONG_ONLY"), (Short, "SHORT_BOOK")):
    check(economics_fixture(cls, group) == economics_fixture(TraceMutedQuota, group),
          group+"_observational_trace_does_not_change_synthetic_economics")

env["legacy_long"], env["legacy_short"], env["legacy_plan"] = real_long, real_short, real_plan
env["legacy_history"], env["legacy_supplement"] = real_history, real_supplement
report = dict(
    status="passed", checks=checks, check_count=len(checks),
    runtime=dict(python=sys.version, numpy=np.__version__, pandas=pd.__version__),
    source_hashes=hashes,
    limitations=[
        "No strategy/framework imports; AST executes only supplied text with explicit state/indicator stubs.",
        "No observed candles, backtest, optimization, broker/indicator kernel or account replay.",
        "Timing tests are callback-order fixtures; actual runtime expiry order relies on the frozen framework audit.",
        "Synthetic economy invariance compares identical supplied fill/close outcomes, not market profitability.",
        "No assertion count is independent evidence or proof of implementation beyond the named outcomes."
    ])
Path("output").mkdir(exist_ok=True)
Path("output/K1001_QUOTA_SYNTHETIC_CHECK_RESULT.json").write_text(
    json.dumps(report, indent=2, allow_nan=False), encoding="utf-8")

```
