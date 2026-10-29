# K1001 LONG MARKET: supplied-source synthetic check (prepared, not executed)

Fecha documental: 2026-10-21. Root ejecutara este unico check coordinado; este autor NO ha ejecutado el codigo ni creado jobs, drafts o motores. El contenido incluye seis padres congelados y la unica clase nueva f3aeb9be8082cfb7f5cbd4a310da1b741a7bec9d675e25d657131754f5e8b32b. Solo AST de textos provistos, stubs e indicadores sinteticos. No imports reales de estrategias, datos observados ni motor anidado. Versiones Python/NumPy/Pandas y hashes se registran al ejecutarlo; no se declaran ahora resultados PASS.

Se comprueba exclusivamente el cambio, junto a hashes/herencia: validacion completa original antes del clone, bordes/falsos, inmutabilidad, replan .5/.5 y diferencia qty LIMIT, memo/cash/sin fallback, submission heredada y _emit super1/filas completas menores1900/sin recuento ni cambios de ledger o R11. No repite la bateria previa de68outcomes. Guardar resultado en output/K1001_LONG_MARKET_SYNTHETIC_CHECK_RESULT.json dentro del workspace temporal de analysis.

Precision broker comunicada por root: el control es una politica LIMIT nominal con conversion nativa near-price; root verifico27LIMIT+4MARKET reales en31trades. No es un control de31LIMIT estrictos. Las cuentas siguen validas. Este check solo verifica request actual self.price; la semantica/tipo MARKET y fill de las ordenes nuevas se auditan DESPUES del unico motor economico, sin preflight economico adicional. La revision estatica del framework existente y esta prueba no se presentan como ejecucion nativa nueva.

```python
SOURCES = {
  "BtcResearchR10Base4h": "import json\nimport math\n\nimport numpy as np\nfrom jesse.strategies import Strategy\n\nBAR = 14400000\nDAY = 86400000\n\n\ndef closed_window(candles, now, count):\n    \"\"\"Use only consecutive, closed 4h bars; no synthetic gap repair.\"\"\"\n    rows = candles[candles[:, 0] + BAR <= now][-count:]\n    if len(rows) != count or rows[-1, 0] != now - BAR:\n        return None\n    if not np.all(np.diff(rows[:, 0]) == BAR):\n        return None\n    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):\n        return None\n    if np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2])):\n        return None\n    if np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2])):\n        return None\n    return rows\n\n\ndef atr14(rows):\n    previous = rows[-15:-1, 2]\n    current = rows[-14:]\n    tr = np.maximum(current[:, 3] - current[:, 4],\n                    np.maximum(abs(current[:, 3] - previous), abs(current[:, 4] - previous)))\n    value = float(np.mean(tr))\n    return value if math.isfinite(value) and value > 0 else None\n\n\ndef breadth_state(closes):\n    changes = np.diff(closes)\n    positive = changes > 0\n    negative = changes < 0\n    if int(positive[-6:].sum()) >= 4 and int(positive[-24:].sum()) >= 16:\n        return 1\n    if int(negative[-6:].sum()) >= 4 and int(negative[-24:].sum()) >= 16:\n        return -1\n    return 0\n\n\ndef breadth_signal(rows):\n    \"\"\"Count sign persistence, not return magnitudes; consume only new states.\"\"\"\n    now_state = breadth_state(rows[-25:, 2])\n    old_state = breadth_state(rows[-26:-1, 2])\n    return now_state if now_state != old_state else 0\n\n\ndef funding_failure_signal(rows, now, events):\n    \"\"\"Observe a full post-payment bar; never know or collect the next payment.\"\"\"\n    event_start = now - BAR\n    matching = []\n    for event in events:\n        raw = int(event[\"settled_at\"])\n        effective = raw // 60000 * 60000\n        if effective == event_start and 0 <= raw - effective <= 1000:\n            if int(event[\"available_at\"]) <= now and int(event[\"available_at\"]) > raw:\n                matching.append(event)\n    if len(matching) != 1:\n        return 0, None\n    event = matching[0]\n    rate = float(event[\"rate_decimal\"])\n    if not math.isfinite(rate):\n        return 0, None\n    pre, post = rows[-2], rows[-1]\n    if rate > 0 and pre[2] > pre[1] and post[2] < pre[1]:\n        return -1, dict(settled_at=int(event[\"settled_at\"]), available_at=int(event[\"available_at\"]), rate=rate)\n    if rate < 0 and pre[2] < pre[1] and post[2] > pre[1]:\n        return 1, dict(settled_at=int(event[\"settled_at\"]), available_at=int(event[\"available_at\"]), rate=rate)\n    return 0, None\n\n\ndef entry_plan(price, capital, margin, leverage, fee, direction, distance):\n    stop = price - direction * distance\n    values = (price, capital, margin, leverage, distance, stop)\n    if direction not in (-1, 1) or not all(math.isfinite(v) and v > 0 for v in values):\n        return None\n    if not math.isfinite(fee) or fee < 0:\n        return None\n    unit_loss = distance + fee * (price + stop)\n    # 2% includes both execution fees. The 90% margin ceiling retains the\n    # historical reserve and does not increase the stop's monetary risk.\n    risk_qty = 0.02 * capital / unit_loss\n    margin_qty = 0.90 * margin * leverage / (price * (1 + fee * leverage))\n    qty = math.floor(min(risk_qty, margin_qty) * 1e8) / 1e8\n    if qty <= 0:\n        return None\n    assert qty * unit_loss <= 0.02 * capital + 1e-6\n    return dict(qty=qty, price=price, capital=capital, distance=distance,\n                stop=stop, risk_budget=0.02 * capital,\n                planned_loss=qty * unit_loss, margin_capped=margin_qty < risk_qty)\n\n\nclass BtcResearchR10Base4h(Strategy):\n    \"\"\"R10 discovery harness: one BTC position, fixed risk and base costs only.\"\"\"\n    MODE = \"abstract\"\n    START = 1602720000000\n    FINISH = 1767225600000\n\n    def _log(self, label, value):\n        self.log(label + \" \" + json.dumps(value, separators=(\",\", \":\"), allow_nan=False))\n\n    def before(self):\n        now = int(self.time)\n        if not self.vars.get(\"checked\"):\n            assert self.symbol == \"BTC-USDT\"\n            assert self.leverage == 3\n            assert abs(self.fee_rate - 0.00045) < 1e-12\n            self.vars[\"checked\"] = True\n            self._log(\"R10_CONFIG\", dict(mode=self.MODE, risk=0.02, aggregate=0.06,\n                                        leverage=self.leverage, fee=self.fee_rate,\n                                        margin_buffer=0.90, stop_atr=2, target_r=2, hold_hours=48))\n        self.vars[\"direction\"] = 0\n        rows = closed_window(self.candles, now, 26)\n        if rows is None:\n            self.vars[\"invalid_windows\"] = self.vars.get(\"invalid_windows\", 0) + 1\n            return\n        if self.MODE == \"BREADTH\":\n            direction = breadth_signal(rows)\n            evidence = None\n        else:\n            assert self.MODE == \"POST_FUNDING\"\n            events = self.get_funding_history(count=6)\n            assert all(int(e[\"available_at\"]) <= now for e in events)\n            direction, evidence = funding_failure_signal(rows, now, events)\n        if not direction or not self.START < now < self.FINISH:\n            return\n        # Signals are evaluated and consumed while occupied as well. No deferred\n        # order or re-entry from a previously blocked funding/breadth event.\n        self.vars[\"signals\"] = self.vars.get(\"signals\", 0) + 1\n        if self.is_open or self.entry_orders or self.vars.get(\"last_exit_at\") == now:\n            self.vars[\"occupied\"] = self.vars.get(\"occupied\", 0) + 1\n            return\n        atr = atr14(rows)\n        if atr is None:\n            return\n        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))\n        plan = entry_plan(float(self.price), capital, float(self.available_margin),\n                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)\n        if plan is None or float(self.price) + direction * 2 * plan[\"distance\"] <= 0:\n            return\n        self.vars[\"direction\"] = direction\n        self.vars[\"plan\"] = plan\n        self.vars[\"evidence\"] = evidence\n\n    def should_long(self):\n        return self.vars.get(\"direction\") == 1\n\n    def should_short(self):\n        return self.vars.get(\"direction\") == -1\n\n    def go_long(self):\n        plan = self.vars[\"plan\"]\n        self.buy = plan[\"qty\"], self.price\n\n    def go_short(self):\n        plan = self.vars[\"plan\"]\n        self.sell = plan[\"qty\"], self.price\n\n    def should_cancel_entry(self):\n        return True\n\n    def on_open_position(self, order):\n        plan = self.vars[\"plan\"]\n        direction = 1 if self.is_long else -1\n        entry = float(self.position.entry_price)\n        qty = abs(float(self.position.qty))\n        distance = plan[\"distance\"]\n        stop = entry - direction * distance\n        target = entry + direction * 2 * distance\n        assert qty * (distance + self.fee_rate * (entry + stop)) <= plan[\"risk_budget\"] + 1e-6\n        self.stop_loss = qty, stop\n        self.take_profit = qty, target\n        self.vars[\"entries\"] = self.vars.get(\"entries\", 0) + 1\n        self._log(\"R10_ENTRY\", dict(time=int(self.time), direction=direction, entry=entry,\n                                   qty=qty, stop=stop, target=target, plan=plan,\n                                   evidence=self.vars.get(\"evidence\")))\n\n    def update_position(self):\n        # No ratchet, discretionary exit or same-close reversal. Funding applies\n        # continuously to actual held quantity, independently of signal inputs.\n        if int(self.time) - int(self.position.opened_at) >= 12 * BAR:\n            self.liquidate()\n\n    def on_close_position(self, order, closed_trade):\n        self.vars[\"last_exit_at\"] = int(self.time)\n\n    def before_terminate(self):\n        self._log(\"R10_COUNTERS\", dict(signals=self.vars.get(\"signals\", 0),\n                                     occupied=self.vars.get(\"occupied\", 0),\n                                     entries=self.vars.get(\"entries\", 0),\n                                     invalid_windows=self.vars.get(\"invalid_windows\", 0)))\n",
  "BtcResearchR11Base1m": "import json\nimport math\nfrom datetime import datetime, timezone\n\nimport numpy as np\nfrom jesse.strategies import Strategy\nfrom strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan\n\n\ndef cusum_step(rows, accumulators):\n    \"\"\"Transfer the R40 design:60 past log returns, drift0.25, boundary4.\"\"\"\n    returns = np.diff(np.log(rows[-62:, 2]))\n    sigma = float(np.std(returns[:-1], ddof=1))\n    if not math.isfinite(sigma) or sigma <= 0:\n        return 0, (0.0, 0.0)\n    z = float((returns[-1] - np.mean(returns[:-1])) / sigma)\n    if not math.isfinite(z):\n        return 0, (0.0, 0.0)\n    up = max(0.0, accumulators[0] + z - 0.25)\n    down = max(0.0, accumulators[1] - z - 0.25)\n    if up >= 4 or down >= 4:\n        direction = 0 if up >= 4 and down >= 4 else 1 if up >= 4 else -1\n        return direction, (0.0, 0.0)\n    return 0, (up, down)\n\n\ndef absorption_signal(rows):\n    \"\"\"Large volume but small body, followed by escape of that closed bar.\"\"\"\n    window, setup, confirmation = rows[-26:-2], rows[-2], rows[-1]\n    if not np.all(np.isfinite(rows[-26:, 5])) or np.any(rows[-26:, 5] < 0):\n        return 0\n    average_volume = float(np.mean(window[:, 5]))\n    prior_atr = atr14(window)\n    if not math.isfinite(average_volume) or average_volume <= 0 or prior_atr is None:\n        return 0\n    if setup[5] < 2 * average_volume or abs(setup[2] - setup[1]) > 0.25 * prior_atr:\n        return 0\n    if confirmation[2] > setup[3]:\n        return 1\n    if confirmation[2] < setup[4]:\n        return -1\n    return 0\n\n\ndef month_name(timestamp):\n    return datetime.fromtimestamp(timestamp / 1000, timezone.utc).strftime(\"%Y-%m\")\n\n\ndef monthly_summary(boundaries, active_months):\n    \"\"\"Declared post-settlement/pre-decision UTC cuts; no00:01 approximation.\"\"\"\n    points = sorted(boundaries.items())\n    months = []\n    for (start, before), (finish, after) in zip(points, points[1:]):\n        stamp = datetime.fromtimestamp(start / 1000, timezone.utc)\n        month = stamp.strftime(\"%Y-%m\")\n        complete = stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0\n        if before <= 0:\n            continue\n        months.append(dict(month=month, start=start, finish=finish,\n                           complete=complete, active=month in active_months,\n                           pnl=after-before, return_fraction=after/before-1))\n    complete = [m for m in months if m[\"complete\"]]\n    active = [m for m in complete if m[\"active\"]]\n    quarter_groups = {}\n    for m in months:\n        quarter = m[\"month\"][:4] + \"Q\" + str((int(m[\"month\"][5:])-1)//3+1)\n        quarter_groups.setdefault(quarter, []).append(m)\n    quarters = [q for q in quarter_groups.values()\n                if len(q) == 3 and all(m[\"complete\"] for m in q)]\n    returns = [m[\"return_fraction\"] for m in complete]\n    contributions = sorted([m[\"pnl\"] for m in months], reverse=True)\n    return dict(months=months, complete_months=len(complete), active_months=len(active),\n                positive_active=sum(m[\"pnl\"] > 0 for m in active),\n                positive_calendar=sum(m[\"pnl\"] > 0 for m in complete),\n                median_return=float(np.median(returns)) if returns else None,\n                complete_quarters=len(quarters),\n                positive_quarters=sum(sum(m[\"pnl\"] for m in q) > 0 for q in quarters),\n                pnl_without_best_two=sum(m[\"pnl\"] for m in months)-sum(contributions[:2]))\n\n\nclass BtcResearchR11Base1m(Strategy):\n    \"\"\"M1 accounting observer; signal and management decisions remain4h.\"\"\"\n    MODE = \"abstract\"\n    START = 1602720000000\n    FINISH = 1767225600000\n\n    def _log(self, label, payload):\n        # Event logs stay small; monthly history is emitted as separate rows.\n        self.log(label + \" \" + json.dumps(payload, separators=(\",\", \":\"), allow_nan=False))\n\n    def _observe(self, stage):\n        now = int(self.time)\n        # BTC-only futures equity. portfolio_value multiplies open PnL by\n        # leverage in this checkout, so it is deliberately not used here.\n        equity = float(self.balance) + (float(self.position.pnl) if self.is_open else 0.0)\n        assert math.isfinite(equity)\n        self.vars[\"peak\"] = max(self.vars.get(\"peak\", 10000.0), equity)\n        drawdown = equity / self.vars[\"peak\"] - 1\n        self.vars[\"dd\"] = min(self.vars.get(\"dd\", 0.0), drawdown)\n        self.vars[\"sequence\"] = self.vars.get(\"sequence\", 0) + 1\n        self.vars[\"last_equity\"] = equity\n        active = self.vars.setdefault(\"active_months\", set())\n        if self.is_open:\n            # Pre marks describe exposure during the minute that just closed;\n            # an opening fill at T instead belongs to the new interval.\n            active.add(month_name(now if stage == \"open\" else now-1))\n        boundaries = self.vars.setdefault(\"boundaries\", {self.START: 10000.0})\n        if stage == \"pre\":\n            self.vars[\"minute_marks\"] = self.vars.get(\"minute_marks\", 0) + 1\n            stamp = datetime.fromtimestamp(now / 1000, timezone.utc)\n            if stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0:\n                boundaries[now] = equity\n        if now >= self.FINISH:\n            # A later terminal close callback replaces the mark with post-fee equity.\n            boundaries[self.FINISH] = equity\n        return equity\n\n    def before(self):\n        now = int(self.time)\n        if not self.vars.get(\"checked\"):\n            assert self.symbol == \"BTC-USDT\" and self.timeframe == \"1m\"\n            assert self.leverage == 3 and abs(self.fee_rate - 0.00045) < 1e-12\n            assert abs(self.balance - 10000) < 1e-6\n            self.vars[\"checked\"] = True\n        self._observe(\"pre\")\n        self.vars[\"direction\"] = 0\n        # This is signal alignment, not a market-session/calendar filter.\n        if now % BAR != 0:\n            return\n        count = 62 if self.MODE == \"CUSUM\" else 26\n        candles = self.get_candles(self.exchange, self.symbol, \"4h\")\n        rows = closed_window(candles, now, count)\n        if rows is None:\n            self.vars[\"invalid_windows\"] = self.vars.get(\"invalid_windows\", 0) + 1\n            self.vars[\"cusum\"] = (0.0, 0.0)\n            return\n        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)\n        if self.MODE == \"CUSUM\":\n            direction, state = cusum_step(rows, self.vars.get(\"cusum\", (0.0, 0.0)))\n            self.vars[\"cusum\"] = state\n        else:\n            assert self.MODE == \"ABSORPTION\"\n            direction = absorption_signal(rows)\n        if not direction or not self.START < now < self.FINISH:\n            return\n        self.vars[\"signals\"] = self.vars.get(\"signals\", 0) + 1\n        if self.is_open or self.entry_orders or self.vars.get(\"last_exit_at\") == now:\n            self.vars[\"occupied\"] = self.vars.get(\"occupied\", 0) + 1\n            return\n        atr = atr14(rows)\n        if atr is None:\n            return\n        # Flat BTC account: wallet equals equity. Reuse the frozen2% fee-aware\n        # plan, eight-decimal research precision and90% margin ceiling.\n        capital = max(0.0, float(self.balance))\n        plan = entry_plan(float(self.price), capital, float(self.available_margin),\n                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)\n        if plan is None or self.price + direction * 2 * plan[\"distance\"] <= 0:\n            return\n        self.vars[\"direction\"] = direction\n        self.vars[\"plan\"] = plan\n\n    def should_long(self):\n        return self.vars.get(\"direction\") == 1\n\n    def should_short(self):\n        return self.vars.get(\"direction\") == -1\n\n    def go_long(self):\n        self.buy = self.vars[\"plan\"][\"qty\"], self.price\n\n    def go_short(self):\n        self.sell = self.vars[\"plan\"][\"qty\"], self.price\n\n    def should_cancel_entry(self):\n        return True\n\n    def on_open_position(self, order):\n        plan = self.vars[\"plan\"]\n        direction = 1 if self.is_long else -1\n        entry = float(self.position.entry_price)\n        qty = abs(float(self.position.qty))\n        stop = entry - direction * plan[\"distance\"]\n        target = entry + direction * 2 * plan[\"distance\"]\n        assert qty * (plan[\"distance\"] + self.fee_rate * (entry + stop)) <= plan[\"risk_budget\"] + 1e-6\n        self.stop_loss = qty, stop\n        self.take_profit = qty, target\n        self.vars[\"entries\"] = self.vars.get(\"entries\", 0) + 1\n        self._observe(\"open\")\n\n    def update_position(self):\n        # Preserve the four-hour management clock despite the M1 observer.\n        if int(self.time) % BAR == 0 and int(self.time) - int(self.position.opened_at) >= 12 * BAR:\n            self.liquidate()\n\n    def on_close_position(self, order, closed_trade):\n        now = int(self.time)\n        active = self.vars.setdefault(\"active_months\", set())\n        active.add(month_name(now-1))\n        # At a month boundary, retain both the held interval and any fee-only\n        # execution month. Terminal liquidation belongs to the final interval.\n        if now < self.FINISH:\n            active.add(month_name(now))\n        self.vars[\"last_exit_at\"] = now\n        self._observe(\"close\")\n        if now >= self.FINISH and self.vars.get(\"emitted\"):\n            self._emit(\"FINAL\")\n\n    def _emit(self, stage):\n        summary = monthly_summary(self.vars[\"boundaries\"], self.vars.get(\"active_months\", set()))\n        # Emit rows at the end, so one bounded log page can retrieve all months.\n        for item in summary.pop(\"months\"):\n            self._log(\"R11_MONTH\", dict(stage=stage, **item))\n        summary.update(stage=stage, equity=self.vars[\"last_equity\"],\n                       dd_m1_events=self.vars.get(\"dd\", 0),\n                       minute_marks=self.vars.get(\"minute_marks\", 0),\n                       sequence=self.vars.get(\"sequence\", 0),\n                       signals=self.vars.get(\"signals\", 0), entries=self.vars.get(\"entries\", 0),\n                       invalid_windows=self.vars.get(\"invalid_windows\", 0))\n        self._log(\"R11_SUMMARY\", summary)\n\n    def before_terminate(self):\n        self._observe(\"terminal\")\n        self.vars[\"emitted\"] = True\n        self._emit(\"PRETERMINAL\")\n",
  "BtcResearchR16LegacyBase1m": "import math\nimport numpy as np\nimport jesse.indicators as ta\n\nfrom strategies.BtcResearchR11Base1m import BtcResearchR11Base1m\nfrom strategies.BtcResearchR10Base4h import BAR\n\n# Frozen legacy recipe values, not optimizer ranges. The 10bp reserve sizes\n# conservatively; it is never charged as cash or simulated execution friction.\nHP = dict(donchian_len=26, ema_fast=20, ema_slow=80, adx_min=26,\n          stop_atr=2.0, trail_atr=4.2, be_r=2.25)\nRESERVE = .001\nLOT = .001\n\n\ndef legacy_history(candles, now):\n    \"\"\"Keep exposed closed history; cross-route seed parity needs framework audit.\"\"\"\n    rows = candles[candles[:, 0]+BAR <= now]\n    if len(rows) < 14 or rows[-1, 0] != now-BAR:\n        return None\n    if (not np.all(np.diff(rows[:, 0]) == BAR)\n            or not np.all(np.isfinite(rows[:, :5]))\n            or not np.all(rows[:, 1:5] > 0)\n            or np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2]))\n            or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2]))):\n        return None\n    return rows\n\n\ndef legacy_long(c):\n    if len(c) < 100:\n        return None\n    price = float(c[-1, 2])\n    fast = float(ta.ema(c, period=20))\n    slow = ta.ema(c, period=80, sequential=True)\n    atr, adx, rsi = float(ta.atr(c)), float(ta.adx(c)), float(ta.rsi(c))\n    entry = float(np.max(c[-27:-1, 3]))\n    if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):\n        return None\n    if not (atr > 0 and entry < price <= entry+atr and price > slow[-1]\n            and fast > slow[-1] > slow[-5] and adx >= 26\n            and 52 <= rsi <= 76 and c[-1, 3]-c[-1, 4] <= 3*atr):\n        return None\n    distance = 2*atr\n    if not 0 < distance < entry:\n        return None\n    return dict(origin=\"LONG_RUNNER\", direction=1, entry=entry,\n                distance=distance, target_distance=None, hold_hours=None,\n                order_kind=\"LIMIT\")\n\n\ndef legacy_short(c):\n    if len(c) < 140:\n        return None\n    price = float(c[-1, 2])\n    macro = ta.ema(c, period=120, sequential=True)\n    fast, atr, rsi = float(ta.ema(c, period=20)), float(ta.atr(c)), float(ta.rsi(c, period=3))\n    if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, rsi)):\n        return None\n    if not (atr > 0 and macro[-1] > macro[-10] and price > macro[-1]-atr and rsi <= 20):\n        return None\n    entry = min(float(c[-1, 4]), price-.25*atr)\n    distance = fast-entry\n    if not (atr <= distance <= 3*atr and distance >= 6*.00045*entry):\n        return None\n    return dict(origin=\"CORE_SHORT\", direction=-1, entry=entry,\n                distance=distance, target_distance=1.5*atr, hold_hours=72,\n                order_kind=\"STOP\")\n\n\ndef legacy_supplement(c, mode, previous):\n    \"\"\"Consume setup before ATR/geometry/account tests, as in each frozen parent.\"\"\"\n    assert mode in (\"K1001\", \"N204\")\n    w = c[-14:]\n    if (len(w) < 14 or not np.all(np.isfinite(w))\n            or not np.all(w[:, 1:] > 0) or not np.all(w[:, 3] >= w[:, 4])):\n        return None, False\n    s, t, window = c[-2], c[-1], c[-13:-1]\n    spans = window[:, 3]-window[:, 4]\n    q = np.divide(window[:, 5]*(2*window[:, 2]-window[:, 3]-window[:, 4]),\n                  spans, out=np.zeros(12), where=spans > 0)\n    cohort = window[q > 0]\n    vwap = (float(np.sum(cohort[:, 5]*np.mean(cohort[:, [3, 4, 2]], axis=1))\n                  / np.sum(cohort[:, 5])) if len(cohort) else float(\"nan\"))\n    setup = bool(s[2] > c[-14, 2] and np.sum(q) < 0\n                 and s[2] >= vwap and t[2] < t[1] and t[2] < vwap)\n    if mode == \"K1001\" and setup:\n        changes = c[-13:-1, 2]-c[-14:-2, 2]\n        path = float(np.sum(np.abs(changes)))\n        efficiency = float(s[2]-c[-14, 2])/path if path > 0 else float(\"nan\")\n        setup = bool(path > 0 and 0 < efficiency <= 1/3)\n    if not setup or previous:\n        return None, setup\n    atr = float(ta.atr(c))\n    if not math.isfinite(atr) or atr <= 0:\n        return None, setup\n    distance = float(max(s[3], t[3])+.25*atr-t[2])\n    if not atr <= distance <= 3*atr:\n        return None, setup\n    entry = float(min(s[4], t[4])) if mode == \"K1001\" else float(t[2])\n    if mode == \"K1001\" and not (math.isfinite(entry) and entry > 2*distance and entry < t[2]):\n        return None, setup\n    if not (math.isfinite(entry) and math.isfinite(distance) and 0 < distance < entry):\n        return None, setup\n    return dict(origin=\"SUPPLEMENT\", direction=-1, entry=entry,\n                distance=distance, target_distance=2*distance, hold_hours=48,\n                order_kind=\"STOP\" if mode == \"K1001\" else \"MARKET\",\n                anchor=vwap), setup\n\n\ndef legacy_plan(event, capital, margin, leverage, fee):\n    \"\"\"BTC100%; preserve reserve/lot, with the common 90%-margin fee buffer.\"\"\"\n    entry, distance, direction = event[\"entry\"], event[\"distance\"], event[\"direction\"]\n    stop = entry-direction*distance\n    if (direction not in (-1, 1)\n            or not all(math.isfinite(v) and v > 0 for v in\n                       (entry, distance, stop, capital, margin, leverage))\n            or not math.isfinite(fee) or fee < 0):\n        return None\n    unit = distance+fee*(entry+stop)+RESERVE*entry\n    budget = .02*capital\n    risk_qty = budget/unit\n    gross_qty = 4.4*capital/entry  # Legacy ceiling; 3x margin prevents 4.4x exposure.\n    margin_qty = .90*margin*leverage/(entry*(1+fee*leverage))\n    qty = math.floor(min(risk_qty, gross_qty, margin_qty)/LOT)*LOT\n    if qty <= 0:\n        return None\n    assert qty*unit <= budget+1e-6\n    return dict(event, qty=qty, risk_budget=budget, planned_loss=qty*unit,\n                planned_stop_fees=qty*(distance+fee*(entry+stop)),\n                margin_limited=margin_qty < risk_qty,\n                gross_limited=gross_qty < risk_qty,\n                reserve=RESERVE)\n\n\nclass BtcResearchR16LegacyBase1m(BtcResearchR11Base1m):\n    MODE = \"abstract\"\n\n    def _ledger(self):\n        return self.vars.setdefault(\"legacy_ledger\", {\n            name: dict(fills=0, closes=0, net=0.0)\n            for name in (\"LONG_RUNNER\", \"CORE_SHORT\", \"SUPPLEMENT\")})\n\n    def before(self):\n        now = int(self.time)\n        if not self.vars.get(\"checked\"):\n            assert self.symbol == \"BTC-USDT\" and self.timeframe == \"1m\"\n            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12\n            assert abs(self.balance-10000) < 1e-6\n            assert self.MODE in (\"K1001\", \"N204\")\n            self.vars[\"checked\"] = True\n        self._observe(\"pre\")\n        self.vars[\"direction\"] = 0\n        if now % BAR:\n            return\n        # Advance the price machine once, independently of occupancy. Actual\n        # framework cancellation may re-enter should_* in this same4h cycle.\n        self.vars[\"decision_at\"] = now\n        rows = legacy_history(self.get_candles(self.exchange, self.symbol, \"4h\"), now)\n        self.vars[\"legacy_rows\"] = rows\n        if rows is None:\n            self.vars[\"previous_setup\"] = False\n            self.vars[\"invalid_windows\"] = self.vars.get(\"invalid_windows\", 0)+1\n            return\n        self.vars[\"history_min\"] = min(self.vars.get(\"history_min\", len(rows)), len(rows))\n        self.vars[\"history_max\"] = max(self.vars.get(\"history_max\", len(rows)), len(rows))\n        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)\n        event, setup = legacy_supplement(rows, self.MODE, self.vars.get(\"previous_setup\", False))\n        self.vars[\"previous_setup\"] = setup\n        self.vars[\"supplement_event\"] = event\n        self.vars[\"supplement_events\"] = self.vars.get(\"supplement_events\", 0)+int(event is not None)\n        if self.is_open or self.entry_orders:\n            self.vars[\"occupied\"] = self.vars.get(\"occupied\", 0)+1\n\n    def _prepare_entry(self):\n        \"\"\"Memoize after broker cancellation releases margin; preserve one plan.\"\"\"\n        now = int(self.time)\n        if (now % BAR or self.vars.get(\"decision_at\") != now\n                or self.is_open or self.entry_orders\n                or self.vars.get(\"last_exit_at\") == now\n                or not self.START < now < self.FINISH):\n            return 0\n        if self.vars.get(\"prepared_at\") == now:\n            return self.vars.get(\"direction\", 0)\n        self.vars[\"prepared_at\"] = now\n        rows = self.vars.get(\"legacy_rows\")\n        if rows is None:\n            return 0\n        # Priority includes account eligibility: if a higher recipe cannot size,\n        # the next original recipe is considered, exactly as the frozen parents.\n        for candidate in (legacy_long(rows), legacy_short(rows),\n                          self.vars.get(\"supplement_event\")):\n            if candidate is None:\n                continue\n            plan = legacy_plan(candidate, max(0.0, float(self.balance)),\n                               float(self.available_margin), float(self.leverage),\n                               float(self.fee_rate))\n            if plan is not None:\n                self.vars[\"plan\"] = dict(plan, signal_at=now, expiry=now+BAR)\n                self.vars[\"direction\"] = plan[\"direction\"]\n                self.vars[\"signals\"] = self.vars.get(\"signals\", 0)+1\n                return plan[\"direction\"]\n        return 0\n\n    def should_long(self):\n        return self._prepare_entry() == 1\n\n    def should_short(self):\n        return self._prepare_entry() == -1\n\n    def _submit(self, direction):\n        plan = self.vars[\"plan\"]\n        assert self.vars.get(\"submitted_at\") != int(self.time), \"P_DUPLICATE_SUBMISSION\"\n        assert self.vars.get(\"direction\") == direction\n        assert int(self.time) == plan[\"signal_at\"] and not self.is_open and not self.entry_orders\n        self.vars[\"submitted_at\"] = int(self.time)\n        self.vars[\"pending_plan\"] = dict(plan)\n        if direction == 1:\n            self.buy = plan[\"qty\"], plan[\"entry\"]\n        else:\n            self.sell = plan[\"qty\"], plan[\"entry\"]\n\n    def go_long(self):\n        self._submit(1)\n\n    def go_short(self):\n        self._submit(-1)\n\n    def should_cancel_entry(self):\n        plan = self.vars.get(\"pending_plan\")\n        assert plan is not None, \"P_PENDING_WITHOUT_PLAN\"\n        due = int(self.time) % BAR == 0 and int(self.time) >= plan[\"expiry\"]\n        if due:\n            self.vars[\"pending_plan\"] = None\n            self.vars[\"cancellations\"] = self.vars.get(\"cancellations\", 0)+1\n        return due\n\n    def on_open_position(self, order):\n        plan = self.vars[\"pending_plan\"]\n        assert plan is not None and self.vars.get(\"position_plan\") is None\n        now = int(self.time)\n        assert plan[\"signal_at\"] <= now <= plan[\"expiry\"], \"P_FILL_OUTSIDE_ORDER_LIFE\"\n        assert plan[\"signal_at\"] <= int(self.position.opened_at) <= plan[\"expiry\"]\n        direction = 1 if self.is_long else -1\n        assert direction == plan[\"direction\"]\n        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))\n        stop = entry-direction*plan[\"distance\"]\n        target = (entry+direction*plan[\"target_distance\"]\n                  if plan[\"target_distance\"] is not None else None)\n        loss = qty*(plan[\"distance\"]+self.fee_rate*(entry+stop)+RESERVE*entry)\n        assert math.isfinite(loss) and stop > 0 and (target is None or target > 0)\n        assert loss <= plan[\"risk_budget\"]+1e-6, \"P_ACTUAL_FILL_RISK\"\n        assert abs(qty-plan[\"qty\"]) < 1e-8, \"P_UNEXPECTED_FILL_QUANTITY\"\n        # Frozen geometry is placed relative to actual fill, never order price.\n        self.stop_loss = qty, stop\n        if target is not None:\n            self.take_profit = qty, target\n        self.vars[\"position_plan\"] = dict(plan, actual_entry=entry, actual_loss=loss,\n                                          filled_at=int(self.position.opened_at))\n        self.vars[\"pending_plan\"] = None\n        self.vars[\"best_close\"] = entry\n        self._ledger()[plan[\"origin\"]][\"fills\"] += 1\n        self.vars[\"entries\"] = self.vars.get(\"entries\", 0)+1\n        self._observe(\"open\")\n        self._log(\"R16_LEGACY_OPEN\", dict(mode=self.MODE, origin=plan[\"origin\"], time=now,\n            opened_at=int(self.position.opened_at), signal_at=plan[\"signal_at\"],\n            expiry=plan[\"expiry\"], order_kind=plan[\"order_kind\"],\n            requested_entry=plan[\"entry\"], actual_entry=entry, qty=qty,\n            distance=plan[\"distance\"], stop=stop, target=target,\n            risk_budget=plan[\"risk_budget\"], actual_loss=loss,\n            planned_loss=plan[\"planned_loss\"], planned_stop_fees=plan[\"planned_stop_fees\"],\n            margin_limited=plan[\"margin_limited\"], reserve=RESERVE))\n\n    def update_position(self):\n        now = int(self.time)\n        if now % BAR:\n            return\n        plan = self.vars[\"position_plan\"]\n        opened = plan[\"filled_at\"]\n        if plan[\"hold_hours\"] is not None:\n            if now-opened >= plan[\"hold_hours\"]*3600000:\n                self.liquidate()\n            return\n        # A close completed before the fill cannot improve its trailing stop.\n        if now <= opened:\n            return\n        rows = self.vars.get(\"legacy_rows\")\n        if rows is None or self.vars.get(\"decision_at\") != now:\n            return\n        atr = float(ta.atr(rows))\n        if not math.isfinite(atr) or atr <= 0:\n            return\n        entry = plan[\"actual_entry\"]\n        self.vars[\"best_close\"] = max(self.vars[\"best_close\"], float(rows[-1, 2]))\n        best_r = (self.vars[\"best_close\"]-entry)/plan[\"distance\"]\n        mult = 4.2\n        if best_r >= 8:\n            mult *= .62\n        elif best_r >= 5:\n            mult *= .78\n        stop = self.vars[\"best_close\"]-mult*atr\n        if best_r >= 2.25:\n            stop = max(stop, entry*(1+2.5*self.fee_rate))\n        if self.average_stop_loss < stop < self.price:\n            self.stop_loss = abs(float(self.position.qty)), stop\n\n    def on_close_position(self, order, closed_trade):\n        plan = self.vars[\"position_plan\"]\n        row = self._ledger()[plan[\"origin\"]]\n        pnl = float(closed_trade.pnl)\n        assert math.isfinite(pnl)\n        row[\"closes\"] += 1\n        row[\"net\"] += pnl\n        self.vars[\"position_plan\"] = None\n        self.vars[\"pending_plan\"] = None\n        self._log(\"R16_LEGACY_CLOSE\", dict(time=int(self.time), origin=plan[\"origin\"], net=pnl))\n        # R11 can emit FINAL here; source totals must already include this close.\n        super().on_close_position(order, closed_trade)\n\n    def _emit(self, stage):\n        super()._emit(stage)\n        rows = self._ledger()\n        self._log(\"R16_LEGACY_STATS\", dict(stage=stage, mode=self.MODE, sources=rows,\n            fills=sum(r[\"fills\"] for r in rows.values()),\n            closes=sum(r[\"closes\"] for r in rows.values()),\n            net=sum(r[\"net\"] for r in rows.values()),\n            supplement_events=self.vars.get(\"supplement_events\", 0),\n            cancellations=self.vars.get(\"cancellations\", 0),\n            history_min=self.vars.get(\"history_min\"), history_max=self.vars.get(\"history_max\")))\n",
  "BtcResearchR16LegacyK1001m": "from strategies.BtcResearchR16LegacyBase1m import BtcResearchR16LegacyBase1m\n\n\nclass BtcResearchR16LegacyK1001m(BtcResearchR16LegacyBase1m):\n    MODE = \"K1001\"\n",
  "BtcResearchR16K1001QuotaBase1m": "import math\nfrom datetime import datetime, timezone\n\nfrom strategies.BtcResearchR16LegacyK1001m import BtcResearchR16LegacyK1001m\nfrom strategies.BtcResearchR16LegacyBase1m import legacy_long, legacy_short, legacy_plan\nfrom strategies.BtcResearchR10Base4h import BAR\n\n# The account still starts at10000. Both halves are fixed allocations of its\n# current wallet/free margin, not a second account or a redistribution rule.\nQUOTA = .5\n\n\ndef quota_counts():\n    return dict(fills=0, closes=0, net=0.0, trace_completed=0, trace_missing=0)\n\n\ndef quota_year(timestamp):\n    return str(datetime.fromtimestamp(timestamp / 1000, timezone.utc).year)\n\n\nclass BtcResearchR16K1001QuotaBase1m(BtcResearchR16LegacyK1001m):\n    \"\"\"Original K1001 groups with1% total-account risk; observational trace only.\n\n    before, supplement latch, indicators, order lifetime and management remain\n    inherited. Only the permitted group and the .5/.5 sizing arguments change.\n    Observed R uses open0, later closed M1 marks and the actual exit fill; it is\n    neither intraminute MFE/MAE nor a counterfactual path after the real exit.\n    \"\"\"\n    GROUP = \"abstract\"\n\n    def _quota_state(self):\n        state = self.vars.get(\"k1001_quota\")\n        if state is None:\n            assert self.GROUP in (\"LONG_ONLY\", \"SHORT_BOOK\")\n            state = dict(active=None, trade_sequence=0, last_fill_identity=None, errors={},\n                         sources={name: quota_counts() for name in\n                                  (\"LONG_RUNNER\", \"CORE_SHORT\", \"SUPPLEMENT\")},\n                         open_years={}, close_years={})\n            self.vars[\"k1001_quota\"] = state\n            self._log(\"K1001_QUOTA_CONFIG\", dict(\n                group=self.GROUP, mode=self.MODE, account_start=10000,\n                capital_fraction=QUOTA, margin_fraction=QUOTA,\n                target_risk_total=.01, aggregate_limit=.06, leverage=3,\n                reserve=.001, lot=.001, redistribution=False,\n                price_trace=\"open0_pre_strictly_after_open_exit_fill\"))\n        return state\n\n    def _quota_error(self, reason):\n        state = self._quota_state()\n        count = state[\"errors\"].get(reason, 0) + 1\n        state[\"errors\"][reason] = count\n        # Record the first example; counters expose repeated failures without\n        # producing one error line per M1 callback.\n        if count == 1:\n            self._log(\"K1001_QUOTA_TRACE_ERROR\", dict(\n                reason=reason, time=int(self.time), group=self.GROUP))\n\n    def _prepare_entry(self):\n        now = int(self.time)\n        if (now % BAR or self.vars.get(\"decision_at\") != now\n                or self.is_open or self.entry_orders\n                or self.vars.get(\"last_exit_at\") == now\n                or not self.START < now < self.FINISH):\n            return 0\n        if self.vars.get(\"prepared_at\") == now:\n            return self.vars.get(\"direction\", 0)\n        self.vars[\"prepared_at\"] = now\n        rows = self.vars.get(\"legacy_rows\")\n        if rows is None:\n            return 0\n        # Use only the event generated by inherited before. In particular, no\n        # second supplement evaluation or previous_setup write is permitted.\n        if self.GROUP == \"LONG_ONLY\":\n            candidates = (legacy_long(rows),)\n        else:\n            assert self.GROUP == \"SHORT_BOOK\"\n            candidates = (legacy_short(rows), self.vars.get(\"supplement_event\"))\n        capital = max(0.0, float(self.balance))\n        margin = float(self.available_margin)\n        for candidate in candidates:\n            if candidate is None:\n                continue\n            # Keep the frozen .02 helper: .02*.5 ==.01 of this account's wallet.\n            # Its .90 buffer on half free margin leaves the other half unused.\n            plan = legacy_plan(candidate, QUOTA*capital, QUOTA*margin,\n                               float(self.leverage), float(self.fee_rate))\n            if plan is not None:\n                self.vars[\"plan\"] = dict(plan, signal_at=now, expiry=now+BAR)\n                self.vars[\"direction\"] = plan[\"direction\"]\n                self.vars[\"signals\"] = self.vars.get(\"signals\", 0)+1\n                self._log(\"K1001_QUOTA_PLAN\", dict(\n                    time=now, group=self.GROUP, origin=plan[\"origin\"],\n                    qty=plan[\"qty\"], risk_budget=plan[\"risk_budget\"],\n                    capital_total=capital, capital_scaled=QUOTA*capital,\n                    margin_total=margin, margin_scaled=QUOTA*margin,\n                    planned_loss=plan[\"planned_loss\"],\n                    planned_stop_fees=plan[\"planned_stop_fees\"],\n                    reserve=plan[\"reserve\"], gross_limited=plan[\"gross_limited\"],\n                    margin_limited=plan[\"margin_limited\"], expiry=now+BAR))\n                return plan[\"direction\"]\n        return 0\n\n    @staticmethod\n    def _quota_identity(plan):\n        return (plan[\"origin\"], int(plan[\"signal_at\"]), int(plan[\"filled_at\"]),\n                float(plan[\"actual_entry\"]), float(plan[\"qty\"]),\n                float(plan[\"distance\"]), int(plan[\"direction\"]))\n\n    def _quota_start_trace(self):\n        state = self._quota_state()\n        plan = self.vars.get(\"position_plan\")\n        if plan is None:\n            self._quota_error(\"open_without_position_plan\")\n            return\n        identity = self._quota_identity(plan)\n        if state[\"last_fill_identity\"] == identity:\n            return  # Same open hook, not a second executed fill.\n        state[\"last_fill_identity\"] = identity\n        state[\"trade_sequence\"] += 1\n        state[\"sources\"][plan[\"origin\"]][\"fills\"] += 1\n        year = quota_year(identity[2])\n        rows = state[\"open_years\"].setdefault(year, {})\n        rows.setdefault(plan[\"origin\"], quota_counts())[\"fills\"] += 1\n        # Execution counts are independent of whether its observational trace\n        # can be completed. A trace failure must not erase a real native fill.\n        active = state[\"active\"]\n        if active is not None:\n            active[\"broken\"] = True\n            self._quota_error(\"overlapping_trace_identity\")\n            return\n        entry, distance = identity[3], identity[5]\n        if not (math.isfinite(entry) and entry > 0\n                and math.isfinite(distance) and distance > 0):\n            self._quota_error(\"invalid_open_price_or_distance\")\n            return\n        opened = identity[2]\n        state[\"active\"] = dict(\n            identity=identity, trace_id=state[\"trade_sequence\"],\n            origin=plan[\"origin\"], signal_at=int(plan[\"signal_at\"]),\n            opened_at=opened, entry=entry, qty=float(plan[\"qty\"]),\n            distance=distance, direction=int(plan[\"direction\"]),\n            min_r=0.0, max_r=0.0, min_at=opened, max_at=opened,\n            min_stage=\"open\", max_stage=\"open\", first_at=opened,\n            last_at=opened, last_stage=\"open\", last_pre_at=None,\n            marks=1, m1_marks=0, broken=False)\n\n    def _quota_mark(self, trace, price, timestamp, stage):\n        if stage == \"pre\":\n            if timestamp <= trace[\"opened_at\"]:\n                return False  # A close at the fill timestamp is not post-fill.\n            previous = trace[\"last_pre_at\"]\n            if previous is not None and timestamp <= previous:\n                if timestamp < previous:\n                    trace[\"broken\"] = True\n                    self._quota_error(\"backward_pre_timestamp\")\n                return False\n        if not math.isfinite(price) or price <= 0:\n            trace[\"broken\"] = True\n            self._quota_error(\"nonfinite_or_nonpositive_mark\")\n            return False\n        if timestamp < trace[\"last_at\"]:\n            trace[\"broken\"] = True\n            self._quota_error(\"backward_mark_timestamp\")\n            return False\n        value = trace[\"direction\"]*(price-trace[\"entry\"])/trace[\"distance\"]\n        if not math.isfinite(value):\n            trace[\"broken\"] = True\n            self._quota_error(\"nonfinite_price_r\")\n            return False\n        # Strict changes retain the first phase/time on ties. Open and exit\n        # remain distinct even when a real trade has zero holding time.\n        if value < trace[\"min_r\"]:\n            trace.update(min_r=value, min_at=timestamp, min_stage=stage)\n        if value > trace[\"max_r\"]:\n            trace.update(max_r=value, max_at=timestamp, max_stage=stage)\n        trace.update(last_at=timestamp, last_stage=stage, marks=trace[\"marks\"]+1)\n        if stage == \"pre\":\n            trace[\"last_pre_at\"] = timestamp\n            trace[\"m1_marks\"] += 1\n        return True\n\n    def _observe(self, stage):\n        value = super()._observe(stage)\n        # Never call the parent observer twice or alter its returned equity.\n        state = self._quota_state()\n        if stage == \"open\":\n            self._quota_start_trace()\n        elif stage == \"pre\" and self.is_open:\n            trace = state[\"active\"]\n            plan = self.vars.get(\"position_plan\")\n            if trace is None or plan is None:\n                self._quota_error(\"pre_without_trace_or_plan\")\n            elif trace[\"identity\"] != self._quota_identity(plan):\n                trace[\"broken\"] = True\n                self._quota_error(\"pre_identity_mismatch\")\n            else:\n                # self.price here is the same already-closed M1 close supplied\n                # to R11's pre observer. Do not use high/low or later prices.\n                self._quota_mark(trace, float(self.price), int(self.time), \"pre\")\n        return value\n\n    def on_close_position(self, order, closed_trade):\n        # Complete our observer before R16 clears its plan and R11 can emit FINAL.\n        state = self._quota_state()\n        plan = self.vars[\"position_plan\"]\n        origin = plan[\"origin\"]\n        trace = state[\"active\"]\n        complete = False\n        if trace is not None and trace[\"identity\"] == self._quota_identity(plan):\n            marked = self._quota_mark(\n                trace, float(closed_trade.exit_price),\n                int(closed_trade.closed_at), \"exit\")\n            complete = marked and not trace[\"broken\"]\n        else:\n            self._quota_error(\"close_identity_missing_or_mismatch\")\n        net = float(closed_trade.pnl)\n        opened_year = quota_year(int(plan[\"filled_at\"]))\n        closed_year = quota_year(int(closed_trade.closed_at))\n        open_rows = state[\"open_years\"].setdefault(opened_year, {})\n        close_rows = state[\"close_years\"].setdefault(closed_year, {})\n        # All three ledgers refer to executed trades, never signal cohorts.\n        for row in (state[\"sources\"][origin],\n                    open_rows.setdefault(origin, quota_counts()),\n                    close_rows.setdefault(origin, dict(\n                        closes=0, net=0.0, trace_completed=0, trace_missing=0))):\n            row[\"closes\"] += 1\n            row[\"net\"] += net\n            row[\"trace_completed\" if complete else \"trace_missing\"] += 1\n        payload = dict(\n            group=self.GROUP, origin=origin, trade_id=str(closed_trade.id),\n            signal_at=int(plan[\"signal_at\"]), opened_at=int(plan[\"filled_at\"]),\n            closed_at=int(closed_trade.closed_at), entry=float(plan[\"actual_entry\"]),\n            exit=float(closed_trade.exit_price), qty=float(plan[\"qty\"]),\n            distance=float(plan[\"distance\"]), net=net, trace_complete=complete,\n            exit_order_id=str(order.id), exit_order_type=order.type,\n            exit_submitted_via=order.submitted_via)\n        if trace is not None and trace[\"identity\"] == self._quota_identity(plan):\n            payload.update({key: trace[key] for key in (\n                \"trace_id\", \"min_r\", \"max_r\", \"min_at\", \"max_at\", \"min_stage\",\n                \"max_stage\", \"first_at\", \"last_at\", \"last_stage\", \"marks\", \"m1_marks\")})\n        self._log(\"K1001_QUOTA_PRICE_TRACE\", payload)\n        state[\"active\"] = None\n        super().on_close_position(order, closed_trade)\n\n    def _emit(self, stage):\n        super()._emit(stage)\n        state = self._quota_state()\n        self._log(\"K1001_QUOTA_STATS\", dict(\n            stage=stage, group=self.GROUP, sources=state[\"sources\"],\n            open_years=state[\"open_years\"], close_years=state[\"close_years\"],\n            trace_errors=state[\"errors\"],\n            open_trace=state[\"active\"] is not None))\n",
  "BtcResearchR16K1001LongOnly1m": "from strategies.BtcResearchR16K1001QuotaBase1m import BtcResearchR16K1001QuotaBase1m\n\n\nclass BtcResearchR16K1001LongOnly1m(BtcResearchR16K1001QuotaBase1m):\n    GROUP = \"LONG_ONLY\"\n",
  "BtcResearchR16K1001LongMarket1m": "from strategies.BtcResearchR16K1001LongOnly1m import BtcResearchR16K1001LongOnly1m\nfrom strategies.BtcResearchR16LegacyBase1m import legacy_long, legacy_plan\nfrom strategies.BtcResearchR16K1001QuotaBase1m import QUOTA\nfrom strategies.BtcResearchR10Base4h import BAR\n\n\nclass BtcResearchR16K1001LongMarket1m(BtcResearchR16K1001LongOnly1m):\n    \"\"\"K long entry-policy ablation; original signal, quota and runner unchanged.\n\n    Validate the complete frozen LIMIT recipe first. Only its requested entry\n    changes to the exact decision price; native inherited submission handles\n    MARKET execution. Compact terminal rows expose the existing real ledger,\n    never hypothetical fills or a new economic decision.\n    \"\"\"\n    ENTRY_POLICY = \"MARKET_AT_DECISION_CLOSE\"\n\n    def _prepare_entry(self):\n        now = int(self.time)\n        if (now % BAR or self.vars.get(\"decision_at\") != now\n                or self.is_open or self.entry_orders\n                or self.vars.get(\"last_exit_at\") == now\n                or not self.START < now < self.FINISH):\n            return 0\n        if self.vars.get(\"prepared_at\") == now:\n            return self.vars.get(\"direction\", 0)\n        self.vars[\"prepared_at\"] = now\n        rows = self.vars.get(\"legacy_rows\")\n        if rows is None:\n            return 0\n        # Includes H < close <= H+ATR and distance < H: MARKET must not relax\n        # any original signal geometry, even when the new price is higher.\n        original = legacy_long(rows)\n        if original is None:\n            return 0\n        decision_price = float(self.price)\n        candidate = dict(original, entry=decision_price, order_kind=\"MARKET\")\n        capital = max(0.0, float(self.balance))\n        margin = float(self.available_margin)\n        # Reprice sizing, fees and reserve at MARKET, with the same inactive\n        # half-account allocation as LIMIT. Never recycle its quantity.\n        plan = legacy_plan(candidate, QUOTA*capital, QUOTA*margin,\n                           float(self.leverage), float(self.fee_rate))\n        if plan is None:\n            return 0\n        self.vars[\"plan\"] = dict(plan, signal_at=now, expiry=now+BAR)\n        self.vars[\"direction\"] = plan[\"direction\"]\n        self.vars[\"signals\"] = self.vars.get(\"signals\", 0)+1\n        self._log(\"K1001_QUOTA_PLAN\", dict(\n            time=now, group=self.GROUP, origin=plan[\"origin\"],\n            qty=plan[\"qty\"], risk_budget=plan[\"risk_budget\"],\n            capital_total=capital, capital_scaled=QUOTA*capital,\n            margin_total=margin, margin_scaled=QUOTA*margin,\n            planned_loss=plan[\"planned_loss\"],\n            planned_stop_fees=plan[\"planned_stop_fees\"],\n            reserve=plan[\"reserve\"], gross_limited=plan[\"gross_limited\"],\n            margin_limited=plan[\"margin_limited\"], expiry=now+BAR))\n        # One record per admitted plan; memo calls produce no extra record.\n        self._log(\"K1001_MARKET_PLAN\", dict(\n            time=now, entry_policy=self.ENTRY_POLICY, origin=plan[\"origin\"],\n            original_trigger_level=float(original[\"entry\"]),\n            decision_price=decision_price,\n            original_distance=float(original[\"distance\"]),\n            requested_entry=plan[\"entry\"], qty=plan[\"qty\"],\n            risk_budget=plan[\"risk_budget\"], expiry=now+BAR))\n        return plan[\"direction\"]\n\n    def _emit(self, stage):\n        super()._emit(stage)\n        state = self._quota_state()\n        # Split the fixed schemas by origin and year so each complete record\n        # stays below 1900 characters, beneath the MCP reader's 2000 cut.\n        # Stages are snapshots, not additional ledger observations.\n        self._log(\"K1001_MARKET_SUMMARY\", dict(\n            stage=stage, policy=self.ENTRY_POLICY,\n            trace_errors=state[\"errors\"], open_trace=state[\"active\"] is not None))\n        for origin, row in state[\"sources\"].items():\n            self._log(\"K1001_MARKET_SOURCE\", dict(stage=stage, origin=origin, **row))\n        for axis in (\"open_years\", \"close_years\"):\n            for year, origins in state[axis].items():\n                for origin, row in origins.items():\n                    self._log(\"K1001_MARKET_COHORT\", dict(\n                        stage=stage, axis=axis, year=year, origin=origin, **row))\n"
}
EXPECTED_HASHES = {
  "BtcResearchR16K1001LongOnly1m": "703a63b968d532e57527fd485c83493685ed77c39a486c9dff97674f6e6a3289",
  "BtcResearchR16K1001QuotaBase1m": "5f41d87af1eeb629a381d6bcc63de8595897646357864f9e28a913b3e631c884",
  "BtcResearchR16LegacyK1001m": "bf88cb663d8561e107446bfce32024ed87531d096362671f7aafce72a09f25ad",
  "BtcResearchR16LegacyBase1m": "56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542",
  "BtcResearchR11Base1m": "be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87",
  "BtcResearchR10Base4h": "2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9",
  "BtcResearchR16K1001LongMarket1m": "f3aeb9be8082cfb7f5cbd4a310da1b741a7bec9d675e25d657131754f5e8b32b"
}

import ast
import copy
import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace as NS

import numpy as np
import pandas as pd

outcomes = []
def check(ok, label):
    if not bool(ok):
        raise AssertionError(label)
    outcomes.append(label)

def parsed_class(text, name):
    return next(n for n in ast.parse(text).body
                if isinstance(n, ast.ClassDef) and n.name == name)

class StrategyStub:
    """Callback/attribute fixture only; no broker, candles engine or indicators."""
    def __init__(self):
        self.vars, self.logs = {}, []
        self.time = 1602720000000 + 14400000
        self.balance = self.available_margin = 10000.
        self.leverage, self.fee_rate = 3., .00045
        self.price = 101.
        self.symbol, self.timeframe, self.exchange = "BTC-USDT", "1m", "synthetic"
        self.entry_orders, self.is_open = [], False
        self.position = NS(qty=0., entry_price=0., opened_at=0, pnl=0.)
    def log(self, value):
        self.logs.append(str(value))

class Indicators:
    """Explicit synthetic scalars; frozen legacy_long itself stays real."""
    def reset(self):
        self.fast, self.slow, self.old_slow = 95., 90., 89.
        self.atr_value, self.adx_value, self.rsi_value = 2., 26., 60.
    def ema(self, rows, period=20, sequential=False):
        if sequential:
            a = np.full(len(rows), self.slow)
            a[-5] = self.old_slow
            return a
        return self.fast
    def atr(self, rows, *args, **kwargs):
        return self.atr_value
    def adx(self, rows, *args, **kwargs):
        return self.adx_value
    def rsi(self, rows, *args, **kwargs):
        return self.rsi_value

ta = Indicators()
ta.reset()
env = dict(__name__="supplied_market_change_check", Strategy=StrategyStub,
           math=math, np=np, json=json, datetime=datetime, timezone=timezone, ta=ta)
source_hashes = {name: hashlib.sha256(text.encode("utf-8")).hexdigest()
                 for name, text in SOURCES.items()}
check(source_hashes == EXPECTED_HASHES, "seven_supplied_source_hashes_frozen_exact")
for name, text in SOURCES.items():
    tree = ast.parse(text)
    tree.body = [n for n in tree.body if not isinstance(n, (ast.Import, ast.ImportFrom))]
    exec(compile(ast.fix_missing_locations(tree), name + ".supplied", "exec"), env)

Market = env["BtcResearchR16K1001LongMarket1m"]
Long = env["BtcResearchR16K1001LongOnly1m"]
Quota = env["BtcResearchR16K1001QuotaBase1m"]
R16 = env["BtcResearchR16LegacyBase1m"]
R11 = env["BtcResearchR11Base1m"]
BAR = env["BAR"]
real_long, real_plan = env["legacy_long"], env["legacy_plan"]
market_ast = parsed_class(SOURCES[Market.__name__], Market.__name__)
methods = {n.name for n in market_ast.body if isinstance(n, ast.FunctionDef)}
check(methods == {"_prepare_entry", "_emit"}, "only_two_authorized_overrides")
check(Market.__bases__ == (Long,) and Market.MODE == "K1001"
      and Market.GROUP == "LONG_ONLY", "lineage_and_group_unchanged")
check(Market.before is R16.before and Market.update_position is R16.update_position
      and Market.on_open_position is R16.on_open_position
      and Market._submit is R16._submit
      and Market._observe is Quota._observe
      and Market.on_close_position is Quota.on_close_position
      and Market._quota_mark is Quota._quota_mark,
      "before_runner_open_submit_trace_close_inherited_literal")
check(sum(isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
          and n.func.attr == "_emit" and isinstance(n.func.value, ast.Call)
          and isinstance(n.func.value.func, ast.Name)
          and n.func.value.func.id == "super"
          for n in ast.walk(next(n for n in market_ast.body
                                if isinstance(n, ast.FunctionDef) and n.name == "_emit"))) == 1,
      "emit_ast_super_exactly_once")

def candles(now, close=101., count=120):
    rows = np.array([[now-(count-i)*BAR, 99., 99., 100., 98., 1.]
                     for i in range(count)], dtype=float)
    rows[-1, 1:5] = [100., close, max(102., close), 99.]
    return rows

def setup(rows=None):
    s = Market()
    ta.reset()
    s.vars.update(decision_at=s.time, direction=0,
                  legacy_rows=candles(s.time) if rows is None else rows)
    return s

def decoded(s, prefix):
    return [json.loads(line[len(prefix)+1:]) for line in s.logs
            if line.startswith(prefix+" ")]

# Negative cases exercise the actual complete legacy_long helper. If admission
# erroneously reaches sizing, the sentinel raises rather than silently passing.
def forbidden_plan(*args):
    raise AssertionError("rejected_original_setup_reached_sizing")
invalid_cases = [
    ("close_equal_trigger", lambda s: s.vars["legacy_rows"].__setitem__((-1,2),100.)),
    ("extension_above_one_ATR", lambda s: s.vars["legacy_rows"].__setitem__((-1,2),np.nextafter(102.,np.inf))),
    ("short_history", lambda s: s.vars.__setitem__("legacy_rows",candles(s.time,count=99))),
    ("ATR_zero", lambda s: setattr(ta,"atr_value",0.)),
    ("ATR_nan", lambda s: setattr(ta,"atr_value",float("nan"))),
    ("EMA_fast_equal_slow", lambda s: setattr(ta,"fast",90.)),
    ("EMA_fast_nan", lambda s: setattr(ta,"fast",float("nan"))),
    ("price_below_slow", lambda s: (setattr(ta,"fast",110.),setattr(ta,"slow",105.),setattr(ta,"old_slow",104.))),
    ("EMA_slope_flat", lambda s: setattr(ta,"old_slow",90.)),
    ("ADX_below26", lambda s: setattr(ta,"adx_value",np.nextafter(26.,-np.inf))),
    ("RSI_below52", lambda s: setattr(ta,"rsi_value",np.nextafter(52.,-np.inf))),
    ("RSI_above76", lambda s: setattr(ta,"rsi_value",np.nextafter(76.,np.inf))),
    ("range_above3ATR", lambda s: s.vars["legacy_rows"].__setitem__((-1,3),np.nextafter(105.,np.inf))),
]
env["legacy_plan"] = forbidden_plan
for label, mutate in invalid_cases:
    s = setup()
    mutate(s)
    check(s._prepare_entry() == 0 and "plan" not in s.vars
          and not decoded(s,"K1001_MARKET_PLAN"), "original_reject_before_clone_"+label)
# Distance guard must still be against old H=4, even though MARKET=5 would allow
# a positive stop at 1. No high-price replan may rescue this original rejection.
s = setup()
s.vars["legacy_rows"][:,1:5] = [3.,3.,4.,2.]
s.vars["legacy_rows"][-1,1:5] = [4.,5.,5.,3.]
s.price = 5.
ta.fast, ta.slow, ta.old_slow = 3.,2.,1.
check(s._prepare_entry() == 0 and "plan" not in s.vars,
      "original_distance_equal_trigger_not_rescued_by_market")
env["legacy_plan"] = real_plan

# Inclusive boundary passes use actual signal helper rather than an event fake.
for label, mutate in [
    ("extension_exact_one_ATR", lambda s: (s.vars["legacy_rows"].__setitem__((-1,2),102.),setattr(s,"price",102.))),
    ("RSI_lower52", lambda s: setattr(ta,"rsi_value",52.)),
    ("RSI_upper76", lambda s: setattr(ta,"rsi_value",76.)),
    ("range_exact3ATR", lambda s: s.vars["legacy_rows"].__setitem__((-1,3),105.)),
]:
    s = setup()
    mutate(s)
    check(s._prepare_entry() == 1, "original_inclusive_boundary_"+label)

# Capture the REAL original helper result and REAL planner inputs/output. Neither
# wrapper replaces the math; the manual oracle below is independent scalar math.
events, plan_calls = [], []
def captured_long(rows):
    event = real_long(rows)
    if event is not None:
        events.append((event, copy.deepcopy(event)))
    return event
def captured_plan(event, capital, margin, leverage, fee):
    plan_calls.append((copy.deepcopy(event),capital,margin,leverage,fee))
    return real_plan(event,capital,margin,leverage,fee)
env["legacy_long"], env["legacy_plan"] = captured_long, captured_plan
s = setup()
check(s._prepare_entry() == 1, "valid_original_selects_market")
event, original_copy = events[-1]
plan = s.vars["plan"]
check(event == original_copy and event["entry"] == 100. and event["order_kind"] == "LIMIT",
      "real_original_event_dict_not_mutated")
args = plan_calls[-1]
check(args[0]["entry"] == float(s.price) == 101.
      and args[0]["order_kind"] == "MARKET"
      and args[0]["distance"] == event["distance"] == 4.
      and args[0]["origin"] == "LONG_RUNNER"
      and args[0]["target_distance"] is None and args[0]["hold_hours"] is None,
      "clone_changes_only_entry_and_documented_order_kind")
check(args[1:] == (5000.,5000.,3.,.00045), "helper_half_wallet_half_free_margin")
def qty_oracle(entry, distance, balance, margin):
    unit = distance+.00045*(entry+entry-distance)+.001*entry
    qty = math.floor(min(.01*balance/unit,4.4*.5*balance/entry,
                         .9*.5*margin*3/(entry*(1+.00045*3)))/.001)*.001
    return qty, unit
oracle_qty, unit = qty_oracle(101.,4.,10000.,10000.)
limit_plan = real_plan(event,5000.,5000.,3.,.00045)
check(plan["qty"] == oracle_qty and plan["risk_budget"] == 100.
      and math.isclose(plan["planned_loss"],oracle_qty*unit,abs_tol=1e-12)
      and plan["qty"] != limit_plan["qty"], "qty_repriced_not_limit_qty_reused")
check(plan["signal_at"] == s.time and plan["expiry"] == s.time+BAR
      and s.vars["signals"] == 1, "selected_plan_lifecycle_metadata")
calls_before = len(plan_calls), len(events), len(s.logs)
check(s._prepare_entry() == 1 and not s.should_short()
      and (len(plan_calls),len(events),len(s.logs)) == calls_before
      and s.vars["signals"] == 1, "memo_no_extra_helper_calls_or_plan_logs")
policy = decoded(s,"K1001_MARKET_PLAN")
check(len(policy) == 1 and policy[0]["original_trigger_level"] == 100.
      and policy[0]["requested_entry"] == s.price
      and policy[0]["original_distance"] == 4.
      and policy[0]["entry_policy"] == Market.ENTRY_POLICY,
      "one_policy_log_preserves_original_trigger")
s.go_long()
check(s.buy == (plan["qty"],s.price) and not s.is_open,
      "inherited_submit_requests_current_price_not_stub_fill")

# A margin-bound case checks the same scaling independently. Native fills are
# deliberately absent: submission tuple is not claimed as broker evidence.
s = setup()
s.available_margin = 10.
check(s._prepare_entry() == 1, "margin_bound_plan_allowed")
q,_ = qty_oracle(s.price,4.,s.balance,s.available_margin)
check(s.vars["plan"]["qty"] == q and s.vars["plan"]["margin_limited"],
      "market_replan_keeps_half_margin_lot_buffer")
s = setup()
s.available_margin = 0.
check(s._prepare_entry() == 0 and "plan" not in s.vars,
      "replan_rejection_cash_no_limit_fallback")

# Guard tests must not call even the signal helper.
def forbidden_signal(rows):
    raise AssertionError("entry_guard_reached_signal")
env["legacy_long"] = forbidden_signal
guard_mutations = [
    ("non4h", lambda s:setattr(s,"time",s.time+1)),
    ("wrong_decision_at", lambda s:s.vars.__setitem__("decision_at",s.time-BAR)),
    ("occupied", lambda s:setattr(s,"is_open",True)),
    ("pending", lambda s:setattr(s,"entry_orders",[object()])),
    ("same_exit", lambda s:s.vars.__setitem__("last_exit_at",s.time)),
    ("start_boundary", lambda s:(setattr(s,"time",s.START),s.vars.__setitem__("decision_at",s.START))),
    ("finish_boundary", lambda s:(setattr(s,"time",s.FINISH),s.vars.__setitem__("decision_at",s.FINISH))),
    ("history_none", lambda s:s.vars.__setitem__("legacy_rows",None)),
]
for label, mutate in guard_mutations:
    s = setup()
    mutate(s)
    check(s._prepare_entry() == 0 and "plan" not in s.vars, "cash_guard_"+label)
env["legacy_long"] = lambda rows: None
env["legacy_short"] = lambda *args: (_ for _ in ()).throw(AssertionError("short_fallback"))
s = setup()
s.vars["supplement_event"] = dict(origin="SUPPLEMENT",direction=-1)
check(s._prepare_entry() == 0 and "plan" not in s.vars,
      "long_absent_never_falls_through_short_or_supplement")
env["legacy_long"],env["legacy_plan"] = real_long,real_plan

# _emit is the only other new override. Execute the real parent chain with
# populated bounded schemas. Spy only counts calls; parent body still executes.
parent_emit = Long._emit
emit_calls = []
def counted_parent_emit(self, stage):
    emit_calls.append(stage)
    return parent_emit(self,stage)
Long._emit = counted_parent_emit
s = setup()
s.time = s.FINISH
s.balance = 12345.
s._observe("terminal")
state = s._quota_state()
for i,(origin,row) in enumerate(state["sources"].items()):
    row.update(fills=10+i,closes=10+i,net=10.25+i,
               trace_completed=10+i,trace_missing=0)
    s._ledger()[origin].update(fills=10+i,closes=10+i,net=10.25+i)
for axis in ("open_years","close_years"):
    for year in range(2020,2026):
        state[axis][str(year)] = {
            origin: dict(row) for origin,row in state["sources"].items()}
# Error schema is finite/fixed by source. Include a nonzero diagnostic error
# to ensure summary doesn't suppress it, without inventing an economic fill.
state["errors"] = {"bad_geometry":1,"missing_plan":2}
state["active"] = None
def canonical_vars(value):
    # Stable observational snapshot, including synthetic ndarray/set fields.
    return json.dumps(value,sort_keys=True,allow_nan=False,
        default=lambda x: x.tolist() if isinstance(x,np.ndarray) else
                          sorted(x) if isinstance(x,set) else x.item())
before = canonical_vars(s.vars)
for stage in ("PRETERMINAL","FINAL","FINAL"):
    at = len(s.logs)
    s._emit(stage)
    rows = s.logs[at:]
    check(emit_calls[-1] == stage and len(emit_calls) == len(
          decoded(s,"K1001_MARKET_SUMMARY")), "emit_parent_once_"+str(len(emit_calls)))
    check(canonical_vars(s.vars) == before, "emit_no_ledger_recount_or_R11_counter_change_"+str(len(emit_calls)))
    summaries = [x for x in rows if x.startswith("R11_SUMMARY ")]
    oldstats = [x for x in rows if x.startswith("K1001_QUOTA_STATS ")]
    check(len(summaries) == len(oldstats) == 1, "parent_evidence_once_"+str(len(emit_calls)))
    compact = [x for x in rows if x.startswith(("K1001_MARKET_SUMMARY ",
               "K1001_MARKET_SOURCE ","K1001_MARKET_COHORT "))]
    check(len(compact) == 1+3+2*6*3
          and all(len(line) < 1900 and len(line.encode("utf-8")) < 1900
                  for line in compact), "bounded_complete_compact_rows_"+str(len(emit_calls)))
    actual = {}
    for line in compact:
        label,raw = line.split(" ",1)
        payload = json.loads(raw)
        if payload["stage"] != stage:
            raise AssertionError("compact_wrong_stage")
        if label == "K1001_MARKET_SUMMARY":
            key = (label,)
            expect = dict(stage=stage,policy=Market.ENTRY_POLICY,
                          trace_errors=state["errors"],open_trace=False)
        elif label == "K1001_MARKET_SOURCE":
            key = (label,payload["origin"])
            expect = dict(stage=stage,origin=payload["origin"],
                          **state["sources"][payload["origin"]])
        else:
            key = (label,payload["axis"],payload["year"],payload["origin"])
            expect = dict(stage=stage,axis=payload["axis"],year=payload["year"],
                          origin=payload["origin"],
                          **state[payload["axis"]][payload["year"]][payload["origin"]])
        if key in actual or payload != expect:
            raise AssertionError("compact_missing_duplicate_or_changed_field")
        actual[key] = payload
    check(len(actual) == len(compact), "compact_field_coverage_unique_"+str(len(emit_calls)))
# Additional active-state summary is observational, not a terminal-close claim.
state["active"] = {"synthetic_active":True}
s._emit("PRETERMINAL")
check(decoded(s,"K1001_MARKET_SUMMARY")[-1]["open_trace"] is True
      and state["active"] == {"synthetic_active":True}, "active_trace_flag_no_close_mutation")
Long._emit = parent_emit

report = dict(status="passed",outcomes=outcomes,outcome_count=len(outcomes),
    source_hashes=source_hashes,
    runtime=dict(python=sys.version,numpy=np.__version__,pandas=pd.__version__),
    limitations=[
        "Supplied-source AST and explicit synthetic indicators/attributes only; no real strategy/framework import.",
        "Frozen parents checked by exact hashes/literal method identity, not a repeat of the prior68-outcome suite.",
        "No observed OHLCV, engine, backtest, optimization, broker fill, indicator kernel or nested job.",
        "Current-price submission is not proof of native MARKET; inspect real order type/fill AFTER the one economic run.",
        "Control is nominal LIMIT policy with native near-price MARKET conversion, not31strictLIMIT orders.",
        "Repeated _emit snapshots may produce repeated rows; stages must not be summed or ledger-recounted.",
        "Outcome count is not independent evidence or economic validation."
    ])
Path("output").mkdir(exist_ok=True)
Path("output/K1001_LONG_MARKET_SYNTHETIC_CHECK_RESULT.json").write_text(
    json.dumps(report,indent=2,allow_nan=False),encoding="utf-8")

```
