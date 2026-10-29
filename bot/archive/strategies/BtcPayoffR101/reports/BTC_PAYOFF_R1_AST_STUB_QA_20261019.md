# Payoff R1 causal source QA

Job1a560d1ce7e840f39c8fa5aa73fdef1b succeeded (2026-10-19T14:37:58Z), exit0. 101/101 checks PASS. PQA1 analysis slot released. Actual frozen MCP readbacks compiled and AST compared; three self-contained source texts and base embedded inline. No data snapshots, prices/results arrays, host source reads, network or MTM.

Checks cover original methods and long branch identity, corrected debug=true runner comment, rejection of partial entry bars and mismatched closed history, acceptance of full bars whose open equals fill, timeout72h outside full-bar gate, EMA never widening/crossing current price/nonfinite handling, half-target BE latch/formula/retention, unchanged qty/TP, RSI3 neutral50 boundary/nonfinite handling and JSON logging. Stubs exercise only exact extracted source methods with deterministic public state and indicator outputs. These are execution boundary unit checks, not engine fill simulation or economic validation.

P01 forms and snapshots separately verified via API readback before start. Both fulls still running at latest status; no economic conclusion. No P02 ticket or further draft.

## Exact results

```json
{
  "scope": "Actual frozen source AST/compile and isolated method stubs; no trading simulation or MTM",
  "checks": [
    {
      "name": "BtcPayoffR101_compile",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged_hyperparameters",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged_trading_hours",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged_signal_candles",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged__entry_window",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged__ledger",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged__key",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged__capital",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged__committed",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged__volatility_share",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged__plan",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged__signal",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged_should_long",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged_should_short",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged_go_long",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged__short_plan",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged_go_short",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged_should_cancel_entry",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_unchanged__record_capacity",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_long_branch",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_debug_comment",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_partial_no_new_rule",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_timeout_outside_gate",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_mismatched_closed_history",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_exact_fill_open_full_bar",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_ema_130",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_ema_qty_tp_130",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_ema_110",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_ema_qty_tp_110",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_ema_90",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_ema_qty_tp_90",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_ema_nan",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_ema_qty_tp_nan",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_never_widen_existing_tighter",
      "pass": true
    },
    {
      "name": "BtcPayoffR101_log_json",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_compile",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged_hyperparameters",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged_trading_hours",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged_signal_candles",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged__entry_window",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged__ledger",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged__key",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged__capital",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged__committed",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged__volatility_share",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged__plan",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged__signal",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged_should_long",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged_should_short",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged_go_long",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged__short_plan",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged_go_short",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged_should_cancel_entry",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_unchanged__record_capacity",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_long_branch",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_debug_comment",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_partial_no_new_rule",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_timeout_outside_gate",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_mismatched_closed_history",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_exact_fill_open_full_bar",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_half_target_latch",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_nominal_be_formula",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_be_qty_tp",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_be_latch_retained_no_widen",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_never_widen_tighter_stop",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_before_half_no_latch",
      "pass": true
    },
    {
      "name": "BtcPayoffR102_log_json",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_compile",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged_hyperparameters",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged_trading_hours",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged_signal_candles",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged__entry_window",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged__ledger",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged__key",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged__capital",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged__committed",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged__volatility_share",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged__plan",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged__signal",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged_should_long",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged_should_short",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged_go_long",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged__short_plan",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged_go_short",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged_should_cancel_entry",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_unchanged__record_capacity",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_long_branch",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_debug_comment",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_partial_no_new_rule",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_timeout_outside_gate",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_mismatched_closed_history",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_exact_fill_open_full_bar",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_rsi_49.999",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_rsi_qty_tp_49.999",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_rsi_50.0",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_rsi_qty_tp_50.0",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_rsi_80.0",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_rsi_qty_tp_80.0",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_rsi_nan",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_rsi_qty_tp_nan",
      "pass": true
    },
    {
      "name": "BtcPayoffR103_log_json",
      "pass": true
    }
  ],
  "total_checks": 101,
  "passed": 101
}
```

## Reproducible code

```python

import ast, copy, json, math
from pathlib import Path
from types import SimpleNamespace
import numpy as np

# Exact MCP readbacks embedded as source text, not external price/result datasets.
sources = json.loads("{\"PortCompareBtc4h\":\"import math\\nimport json\\nimport jesse.helpers as jh\\nimport numpy as np\\nfrom jesse.strategies import Strategy, cached\\nfrom jesse import utils\\nimport jesse.indicators as ta\\n\\n# User-approved research limits; risk is not an optimization parameter.\\nTRADE_RISK = 0.01\\nPORTFOLIO_RISK = 0.08\\nNOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.\\nSLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.\\n\\n\\nclass PortCompareBtc4h(Strategy):\\n    \\\"\\\"\\\"Long LIMIT retests plus BTC-only pullback-continuation STOP shorts.\\n\\n    Shared risk and margin reservations; exploratory research, not approved live.\\n    SPY uses a session-filtered SPX CFD proxy; holidays and native parity remain\\n    unverified. Parameter-neighbour variants are sensitivity controls, not winners.\\n    \\\"\\\"\\\"\\n\\n    def hyperparameters(self) -> list:\\n        return [\\n            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},\\n            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},\\n            {'name': 'ema_slow', 'type': int, 'min': 80, 'max': 140, 'default': 80},\\n            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},\\n            {'name': 'stop_atr', 'type': float, 'min': 1.6, 'max': 3.0, 'default': 2.0},\\n            {'name': 'trail_atr', 'type': float, 'min': 3.0, 'max': 5.0, 'default': 4.2},\\n            {'name': 'be_r', 'type': float, 'min': 1.75, 'max': 3.0, 'default': 2.25},\\n        ]\\n\\n    def trading_hours(self):\\n        if self.symbol == 'SPY-USDT':\\n            # The fixed UTC whole-bar intersection excludes the US index daily\\n            # break in both DST regimes. This is an intentional common window,\\n            # not an assertion that the source's full session ends at 20:00 UTC.\\n            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}\\n        return None\\n\\n    @property\\n    @cached\\n    def signal_candles(self):\\n        return utils.filter_candles_by_hours(self.candles, self.trading_hours())\\n\\n    def _entry_window(self) -> bool:\\n        if self.symbol != 'SPY-USDT':\\n            return True\\n        # A closed bar opening at 12:00 triggers at 16:00. Its order expires\\n        # at 20:00, before the excluded 20:00-24:00 bucket. A 16:00-open bar\\n        # must not arm a new order at 20:00. Pending orders still cancel then.\\n        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}\\n        return self.is_trading_hours and utils.is_in_trading_hours(\\n            self.closed_candle_open_time, window)\\n\\n    def _ledger(self) -> dict:\\n        return self.shared_vars.setdefault('phase2_reservations', {})\\n\\n    def _key(self) -> str:\\n        return self.exchange + ':' + self.symbol\\n\\n    def _capital(self) -> float:\\n        # Floating gains do not enlarge the risk budget; floating losses reduce it.\\n        return max(0.0, min(float(self.balance), float(self.portfolio_value)))\\n\\n    def _committed(self) -> tuple:\\n        risk, notional = 0.0, 0.0\\n        ledger = self._ledger()\\n        for route in self.routes:\\n            if route.exchange != self.exchange:\\n                continue\\n            strategy = route.strategy\\n            if strategy.is_open:\\n                qty = abs(float(strategy.position.qty))\\n                entry = float(strategy.position.entry_price)\\n                # Risk is measured from the current mark, so protected floating PnL\\n                # is not silently treated as free capacity for another trade.\\n                value = abs(float(strategy.position.value))\\n                mark = value / qty if qty else entry\\n                stop = float(strategy.average_stop_loss)\\n                distance = max(0.0, mark - stop) if strategy.is_long else max(0.0, stop - mark)\\n                risk += qty * (distance + mark * (self.fee_rate + SLIPPAGE_RESERVE))\\n                notional += value\\n            else:\\n                reservation = ledger.get(route.exchange + ':' + route.symbol)\\n                if reservation:\\n                    # Includes not-yet-filled STOP/LIMIT entries, not only open positions.\\n                    risk += reservation['risk']\\n                    notional += reservation['notional']\\n        return risk, notional\\n\\n    def _volatility_share(self) -> float:\\n        \\\"\\\"\\\"Reserve a common gross-exposure budget using inverse ATR fractions.\\n\\n        All configured assets receive an ex-ante share, even while their signal\\n        is idle. This prevents the first route from consuming all shared margin.\\n        It is a capital-efficiency tradeoff to test, not an optimal allocation.\\n        \\\"\\\"\\\"\\n        weights = {}\\n        for route in self.routes:\\n            if route.exchange != self.exchange:\\n                continue\\n            c = utils.filter_candles_by_hours(route.strategy.candles, route.strategy.trading_hours())\\n            if len(c) < int(self.hp['ema_slow']) + 20:\\n                return 0.0\\n            atr = float(ta.atr(c))\\n            price = float(c[-1, 2])\\n            if not math.isfinite(atr) or atr <= 0 or price <= 0:\\n                return 0.0\\n            # Stops use a common ATR multiple. Equal risk therefore needs\\n            # notional proportional to price/ATR before gross-leverage scaling.\\n            weights[route.symbol] = price / atr\\n        return weights.get(self.symbol, 0.0) / sum(weights.values()) if weights else 0.0\\n\\n    def _plan(self) -> bool:\\n        if self.symbol not in ('BTC-USDT', 'PAXG-USDT', 'SPY-USDT') or not self._entry_window():\\n            return False\\n        c = self.signal_candles\\n        n = int(self.hp['donchian_len'])\\n        slow_n = int(self.hp['ema_slow'])\\n        if len(c) < max(slow_n + 20, n):\\n            return False\\n        fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))\\n        slow = ta.ema(c, period=slow_n, sequential=True)\\n        atr = float(ta.atr(c))\\n        adx = float(ta.adx(c))\\n        rsi = float(ta.rsi(c))\\n        # The closed bar has broken the PRIOR channel. A passive LIMIT at that\\n        # boundary can fill only on a future retest within one 4h order lifetime.\\n        entry = float(np.max(c[-n-1:-1, 3]))\\n        if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):\\n            return False\\n        if not (atr > 0 and entry < self.price <= entry + atr and self.price > slow[-1]\\n                and fast > slow[-1] > slow[-5] and adx >= self.hp['adx_min']\\n                and 52 <= rsi <= 76 and self.high - self.low <= 3 * atr):\\n            return False\\n        distance = float(self.hp['stop_atr']) * atr\\n        if not 0 < distance < entry:\\n            return False\\n        capital = self._capital()\\n        committed_risk, committed_notional = self._committed()\\n        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - committed_risk))\\n        # Fees at both planned entry and stop, plus an explicit adverse-fill reserve.\\n        unit_risk = distance + self.fee_rate * (entry + entry - distance) + SLIPPAGE_RESERVE * entry\\n        room = min(max(0.0, capital * NOTIONAL_CAP - committed_notional),\\n                   capital * NOTIONAL_CAP * self._volatility_share())\\n        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)\\n        qty = min(budget / unit_risk, room / entry, margin_room / entry)\\n        # Historical research precision only. Native symbol lot/min-notional\\n        # constraints must be verified before any live use.\\n        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001\\n        self._record_capacity('long', capital, budget, unit_risk, entry,\\n                              room, margin_room, qty, step)\\n        qty = math.floor(qty / step) * step\\n        if qty <= 0:\\n            return False\\n        self.vars['plan'] = {\\n            'qty': qty, 'entry': entry, 'distance': distance,\\n            'risk': qty * unit_risk, 'notional': qty * entry,\\n        }\\n        return True\\n\\n    def _signal(self) -> int:\\n        # Compute exactly one plan per bar, with long priority. Checking\\n        # should_short after go_long must never overwrite a queued long plan.\\n        if self.vars.get('signal_index') != self.index:\\n            self.vars['signal_index'] = self.index\\n            self.vars['signal_value'] = 1 if self._plan() else (-1 if self._short_plan() else 0)\\n        return self.vars['signal_value']\\n\\n    def should_long(self) -> bool:\\n        return self._signal() == 1\\n\\n    def should_short(self) -> bool:\\n        return self._signal() == -1\\n\\n    def go_long(self) -> None:\\n        plan = self.vars['plan']\\n        self._ledger()[self._key()] = dict(plan)\\n        self.buy = plan['qty'], plan['entry']\\n\\n    def _short_plan(self) -> bool:\\n        \\\"\\\"\\\"Test selloff continuation instead of buying an oversold dip.\\n\\n        A rising slow regime can still suffer a fast liquidation leg. This\\n        exploratory hypothesis came from the failed long mean-reversion sleeve;\\n        it is development evidence, not an independent validation.\\n        \\\"\\\"\\\"\\n        if self.symbol != 'BTC-USDT' or not self._entry_window():\\n            return False\\n        c = self.signal_candles\\n        if len(c) < 140:\\n            return False\\n        macro = ta.ema(c, period=120, sequential=True)\\n        fast = float(ta.ema(c, period=20))\\n        atr = float(ta.atr(c))\\n        quick_rsi = float(ta.rsi(c, period=3))\\n        if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, quick_rsi)):\\n            return False\\n        if not (atr > 0 and macro[-1] > macro[-10]\\n                and self.price > macro[-1] - atr and quick_rsi <= 20):\\n            return False\\n        entry = min(float(c[-1, 4]), self.price - 0.25 * atr)\\n        distance = fast - entry\\n        if not (atr <= distance <= 3 * atr and distance >= 6 * self.fee_rate * entry):\\n            return False\\n        capital = self._capital()\\n        risk, notional = self._committed()\\n        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))\\n        unit_risk = distance + self.fee_rate * (2 * entry + distance) + SLIPPAGE_RESERVE * entry\\n        room = min(max(0.0, capital * NOTIONAL_CAP - notional),\\n                   capital * NOTIONAL_CAP * self._volatility_share())\\n        qty = min(budget / unit_risk, room / entry,\\n                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)\\n        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001\\n        self._record_capacity('short', capital, budget, unit_risk, entry,\\n                              room, max(0.0, float(self.leveraged_available_margin) * 0.90), qty, step)\\n        qty = math.floor(qty / step) * step\\n        if qty <= 0:\\n            return False\\n        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,\\n                             'risk': qty * unit_risk, 'notional': qty * entry,\\n                             'target_distance': 1.5 * atr}\\n        return True\\n\\n    def go_short(self) -> None:\\n        plan = self.vars['plan']\\n        self._ledger()[self._key()] = dict(plan)\\n        self.sell = plan['qty'], plan['entry']\\n\\n    def should_cancel_entry(self) -> bool:\\n        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.\\n        # Jesse processes cancellation before evaluating the next route.\\n        self._ledger().pop(self._key(), None)\\n        return True\\n\\n    def on_open_position(self, order) -> None:\\n        entry = float(self.position.entry_price)\\n        distance = self.vars['plan']['distance']\\n        self.vars['initial_distance'] = distance\\n        # An intrabar fill must not inherit highs/closes from before its entry.\\n        self.vars['best_close'] = entry\\n        if self.is_short:\\n            self.vars['opened_time'] = int(self.time)\\n            self.stop_loss = abs(self.position.qty), entry + distance\\n            self.take_profit = abs(self.position.qty), entry - self.vars['plan']['target_distance']\\n        else:\\n            self.stop_loss = abs(self.position.qty), entry - distance\\n        self._ledger().pop(self._key(), None)\\n\\n    def update_position(self) -> None:\\n        if self.is_short:\\n            if self.time - self.vars['opened_time'] >= 72 * 60 * 60 * 1000:\\n                self.liquidate()\\n            return\\n        history = self.signal_candles\\n        atr = float(ta.atr(history))\\n        if not math.isfinite(atr) or atr <= 0:\\n            return\\n        entry = float(self.position.entry_price)\\n        distance = self.vars['initial_distance']\\n        self.vars['best_close'] = max(self.vars['best_close'], float(history[-1, 2]))\\n        best_r = (self.vars['best_close'] - entry) / distance\\n        mult = float(self.hp['trail_atr'])\\n        # Inherited late-trend tightening; retained as a controlled baseline choice.\\n        if best_r >= 8:\\n            mult *= 0.62\\n        elif best_r >= 5:\\n            mult *= 0.78\\n        stop = self.vars['best_close'] - mult * atr\\n        if best_r >= float(self.hp['be_r']):\\n            stop = max(stop, entry * (1 + 2.5 * self.fee_rate))\\n        if self.average_stop_loss < stop < self.price:\\n            self.stop_loss = abs(self.position.qty), stop\\n\\n    def on_close_position(self, order, closed_trade) -> None:\\n        self._ledger().pop(self._key(), None)\\n\\n    def _record_capacity(self, side, capital, budget, unit_risk, entry,\\n                         room, margin_room, raw_qty, step) -> None:\\n        \\\"\\\"\\\"Observe existing sizing only; never gates signals or changes quantities.\\n\\n        Counts plans reaching sizing while flat and without a pending entry.\\n        It does not infer trades that would have filled or signals while occupied.\\n        Quantity tolerances below classify numerical ties, not trading thresholds.\\n        \\\"\\\"\\\"\\n        audit = self.vars.setdefault('portfolio_capacity_audit', {})\\n        row = audit.setdefault(side, {'eligible_sizing_attempts': 0,\\n                                     'risk_budget_limited': 0,\\n                                     'notional_or_weight_limited': 0,\\n                                     'margin_limited': 0,\\n                                     'sized_below_trade_target': 0,\\n                                     'capacity_zero': 0,\\n                                     'zero_after_lot_rounding': 0})\\n        row['eligible_sizing_attempts'] += 1\\n        target_qty = capital * TRADE_RISK / unit_risk\\n        tolerance = max(1e-8, abs(target_qty) * 1e-10)\\n        row['risk_budget_limited'] += int(budget / unit_risk + tolerance < target_qty)\\n        row['notional_or_weight_limited'] += int(room / entry + tolerance < target_qty)\\n        row['margin_limited'] += int(margin_room / entry + tolerance < target_qty)\\n        row['sized_below_trade_target'] += int(raw_qty + tolerance < target_qty)\\n        row['capacity_zero'] += int(raw_qty <= 0 < target_qty)\\n        row['zero_after_lot_rounding'] += int(math.floor(raw_qty / step) * step <= 0 < raw_qty)\\n\\n    def terminate(self) -> None:\\n        # One compact persisted record per route, after engine final liquidation.\\n        # jh.debug logs even with strategy debug_mode disabled; no decision is changed.\\n        jh.debug('PORT_CAPACITY ' + json.dumps({\\n            'symbol': self.symbol, 'strategy': self.__class__.__name__,\\n            'trade_risk': TRADE_RISK, 'portfolio_risk': PORTFOLIO_RISK,\\n            'notional_cap': NOTIONAL_CAP,\\n            'counts': self.vars.get('portfolio_capacity_audit', {})\\n        }, sort_keys=True))\\n\",\"BtcPayoffR101\":\"import math\\nimport json\\nimport jesse.helpers as jh\\nimport numpy as np\\nfrom jesse.strategies import Strategy, cached\\nfrom jesse import utils\\nimport jesse.indicators as ta\\n\\n# User-approved research limits; risk is not an optimization parameter.\\nTRADE_RISK = 0.01\\nPORTFOLIO_RISK = 0.08\\nNOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.\\nSLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.\\n\\n\\nclass BtcPayoffR101(Strategy):\\n    \\\"\\\"\\\"Frozen BtcPayoffR101 short-management experiment; long runner unchanged.\\n\\n    Shared risk and margin reservations; exploratory research, not approved live.\\n    SPY uses a session-filtered SPX CFD proxy; holidays and native parity remain\\n    unverified. Parameter-neighbour variants are sensitivity controls, not winners.\\n    \\\"\\\"\\\"\\n\\n    def hyperparameters(self) -> list:\\n        return [\\n            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},\\n            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},\\n            {'name': 'ema_slow', 'type': int, 'min': 80, 'max': 140, 'default': 80},\\n            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},\\n            {'name': 'stop_atr', 'type': float, 'min': 1.6, 'max': 3.0, 'default': 2.0},\\n            {'name': 'trail_atr', 'type': float, 'min': 3.0, 'max': 5.0, 'default': 4.2},\\n            {'name': 'be_r', 'type': float, 'min': 1.75, 'max': 3.0, 'default': 2.25},\\n        ]\\n\\n    def trading_hours(self):\\n        if self.symbol == 'SPY-USDT':\\n            # The fixed UTC whole-bar intersection excludes the US index daily\\n            # break in both DST regimes. This is an intentional common window,\\n            # not an assertion that the source's full session ends at 20:00 UTC.\\n            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}\\n        return None\\n\\n    @property\\n    @cached\\n    def signal_candles(self):\\n        return utils.filter_candles_by_hours(self.candles, self.trading_hours())\\n\\n    def _entry_window(self) -> bool:\\n        if self.symbol != 'SPY-USDT':\\n            return True\\n        # A closed bar opening at 12:00 triggers at 16:00. Its order expires\\n        # at 20:00, before the excluded 20:00-24:00 bucket. A 16:00-open bar\\n        # must not arm a new order at 20:00. Pending orders still cancel then.\\n        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}\\n        return self.is_trading_hours and utils.is_in_trading_hours(\\n            self.closed_candle_open_time, window)\\n\\n    def _ledger(self) -> dict:\\n        return self.shared_vars.setdefault('phase2_reservations', {})\\n\\n    def _key(self) -> str:\\n        return self.exchange + ':' + self.symbol\\n\\n    def _capital(self) -> float:\\n        # Floating gains do not enlarge the risk budget; floating losses reduce it.\\n        return max(0.0, min(float(self.balance), float(self.portfolio_value)))\\n\\n    def _committed(self) -> tuple:\\n        risk, notional = 0.0, 0.0\\n        ledger = self._ledger()\\n        for route in self.routes:\\n            if route.exchange != self.exchange:\\n                continue\\n            strategy = route.strategy\\n            if strategy.is_open:\\n                qty = abs(float(strategy.position.qty))\\n                entry = float(strategy.position.entry_price)\\n                # Risk is measured from the current mark, so protected floating PnL\\n                # is not silently treated as free capacity for another trade.\\n                value = abs(float(strategy.position.value))\\n                mark = value / qty if qty else entry\\n                stop = float(strategy.average_stop_loss)\\n                distance = max(0.0, mark - stop) if strategy.is_long else max(0.0, stop - mark)\\n                risk += qty * (distance + mark * (self.fee_rate + SLIPPAGE_RESERVE))\\n                notional += value\\n            else:\\n                reservation = ledger.get(route.exchange + ':' + route.symbol)\\n                if reservation:\\n                    # Includes not-yet-filled STOP/LIMIT entries, not only open positions.\\n                    risk += reservation['risk']\\n                    notional += reservation['notional']\\n        return risk, notional\\n\\n    def _volatility_share(self) -> float:\\n        \\\"\\\"\\\"Reserve a common gross-exposure budget using inverse ATR fractions.\\n\\n        All configured assets receive an ex-ante share, even while their signal\\n        is idle. This prevents the first route from consuming all shared margin.\\n        It is a capital-efficiency tradeoff to test, not an optimal allocation.\\n        \\\"\\\"\\\"\\n        weights = {}\\n        for route in self.routes:\\n            if route.exchange != self.exchange:\\n                continue\\n            c = utils.filter_candles_by_hours(route.strategy.candles, route.strategy.trading_hours())\\n            if len(c) < int(self.hp['ema_slow']) + 20:\\n                return 0.0\\n            atr = float(ta.atr(c))\\n            price = float(c[-1, 2])\\n            if not math.isfinite(atr) or atr <= 0 or price <= 0:\\n                return 0.0\\n            # Stops use a common ATR multiple. Equal risk therefore needs\\n            # notional proportional to price/ATR before gross-leverage scaling.\\n            weights[route.symbol] = price / atr\\n        return weights.get(self.symbol, 0.0) / sum(weights.values()) if weights else 0.0\\n\\n    def _plan(self) -> bool:\\n        if self.symbol not in ('BTC-USDT', 'PAXG-USDT', 'SPY-USDT') or not self._entry_window():\\n            return False\\n        c = self.signal_candles\\n        n = int(self.hp['donchian_len'])\\n        slow_n = int(self.hp['ema_slow'])\\n        if len(c) < max(slow_n + 20, n):\\n            return False\\n        fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))\\n        slow = ta.ema(c, period=slow_n, sequential=True)\\n        atr = float(ta.atr(c))\\n        adx = float(ta.adx(c))\\n        rsi = float(ta.rsi(c))\\n        # The closed bar has broken the PRIOR channel. A passive LIMIT at that\\n        # boundary can fill only on a future retest within one 4h order lifetime.\\n        entry = float(np.max(c[-n-1:-1, 3]))\\n        if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):\\n            return False\\n        if not (atr > 0 and entry < self.price <= entry + atr and self.price > slow[-1]\\n                and fast > slow[-1] > slow[-5] and adx >= self.hp['adx_min']\\n                and 52 <= rsi <= 76 and self.high - self.low <= 3 * atr):\\n            return False\\n        distance = float(self.hp['stop_atr']) * atr\\n        if not 0 < distance < entry:\\n            return False\\n        capital = self._capital()\\n        committed_risk, committed_notional = self._committed()\\n        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - committed_risk))\\n        # Fees at both planned entry and stop, plus an explicit adverse-fill reserve.\\n        unit_risk = distance + self.fee_rate * (entry + entry - distance) + SLIPPAGE_RESERVE * entry\\n        room = min(max(0.0, capital * NOTIONAL_CAP - committed_notional),\\n                   capital * NOTIONAL_CAP * self._volatility_share())\\n        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)\\n        qty = min(budget / unit_risk, room / entry, margin_room / entry)\\n        # Historical research precision only. Native symbol lot/min-notional\\n        # constraints must be verified before any live use.\\n        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001\\n        self._record_capacity('long', capital, budget, unit_risk, entry,\\n                              room, margin_room, qty, step)\\n        qty = math.floor(qty / step) * step\\n        if qty <= 0:\\n            return False\\n        self.vars['plan'] = {\\n            'qty': qty, 'entry': entry, 'distance': distance,\\n            'risk': qty * unit_risk, 'notional': qty * entry,\\n        }\\n        return True\\n\\n    def _signal(self) -> int:\\n        # Compute exactly one plan per bar, with long priority. Checking\\n        # should_short after go_long must never overwrite a queued long plan.\\n        if self.vars.get('signal_index') != self.index:\\n            self.vars['signal_index'] = self.index\\n            self.vars['signal_value'] = 1 if self._plan() else (-1 if self._short_plan() else 0)\\n        return self.vars['signal_value']\\n\\n    def should_long(self) -> bool:\\n        return self._signal() == 1\\n\\n    def should_short(self) -> bool:\\n        return self._signal() == -1\\n\\n    def go_long(self) -> None:\\n        plan = self.vars['plan']\\n        self._ledger()[self._key()] = dict(plan)\\n        self.buy = plan['qty'], plan['entry']\\n\\n    def _short_plan(self) -> bool:\\n        \\\"\\\"\\\"Test selloff continuation instead of buying an oversold dip.\\n\\n        A rising slow regime can still suffer a fast liquidation leg. This\\n        exploratory hypothesis came from the failed long mean-reversion sleeve;\\n        it is development evidence, not an independent validation.\\n        \\\"\\\"\\\"\\n        if self.symbol != 'BTC-USDT' or not self._entry_window():\\n            return False\\n        c = self.signal_candles\\n        if len(c) < 140:\\n            return False\\n        macro = ta.ema(c, period=120, sequential=True)\\n        fast = float(ta.ema(c, period=20))\\n        atr = float(ta.atr(c))\\n        quick_rsi = float(ta.rsi(c, period=3))\\n        if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, quick_rsi)):\\n            return False\\n        if not (atr > 0 and macro[-1] > macro[-10]\\n                and self.price > macro[-1] - atr and quick_rsi <= 20):\\n            return False\\n        entry = min(float(c[-1, 4]), self.price - 0.25 * atr)\\n        distance = fast - entry\\n        if not (atr <= distance <= 3 * atr and distance >= 6 * self.fee_rate * entry):\\n            return False\\n        capital = self._capital()\\n        risk, notional = self._committed()\\n        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))\\n        unit_risk = distance + self.fee_rate * (2 * entry + distance) + SLIPPAGE_RESERVE * entry\\n        room = min(max(0.0, capital * NOTIONAL_CAP - notional),\\n                   capital * NOTIONAL_CAP * self._volatility_share())\\n        qty = min(budget / unit_risk, room / entry,\\n                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)\\n        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001\\n        self._record_capacity('short', capital, budget, unit_risk, entry,\\n                              room, max(0.0, float(self.leveraged_available_margin) * 0.90), qty, step)\\n        qty = math.floor(qty / step) * step\\n        if qty <= 0:\\n            return False\\n        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,\\n                             'risk': qty * unit_risk, 'notional': qty * entry,\\n                             'target_distance': 1.5 * atr}\\n        return True\\n\\n    def go_short(self) -> None:\\n        plan = self.vars['plan']\\n        self._ledger()[self._key()] = dict(plan)\\n        self.sell = plan['qty'], plan['entry']\\n\\n    def should_cancel_entry(self) -> bool:\\n        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.\\n        # Jesse processes cancellation before evaluating the next route.\\n        self._ledger().pop(self._key(), None)\\n        return True\\n\\n    def on_open_position(self, order) -> None:\\n        entry = float(self.position.entry_price)\\n        distance = self.vars['plan']['distance']\\n        self.vars['initial_distance'] = distance\\n        # An intrabar fill must not inherit highs/closes from before its entry.\\n        self.vars['best_close'] = entry\\n        if self.is_short:\\n            self.vars['opened_time'] = int(self.time)\\n            self._payoff_log('short_open', initial_stop=entry + distance,\\n                             initial_target=entry - self.vars['plan']['target_distance'])\\n            self.stop_loss = abs(self.position.qty), entry + distance\\n            self.take_profit = abs(self.position.qty), entry - self.vars['plan']['target_distance']\\n        else:\\n            self.stop_loss = abs(self.position.qty), entry - distance\\n        self._ledger().pop(self._key(), None)\\n\\n    def update_position(self) -> None:\\n        if self.is_short:\\n            if self.time - self.vars['opened_time'] >= 72 * 60 * 60 * 1000:\\n                self._payoff_log('timeout')\\n                self.liquidate()\\n                return\\n            if not self._payoff_postfill_bar():\\n                return\\n            # The original EMA20 anchor may only ratchet toward price. A level\\n            # below the current mark would route as a limit, not a protective stop.\\n            ema = float(ta.ema(self.signal_candles, period=20))\\n            old = float(self.average_stop_loss)\\n            if math.isfinite(ema):\\n                new = min(old, ema)\\n                if self.price < new < old:\\n                    self._payoff_log('ema_stop', old_stop=old, new_stop=new, ema=ema)\\n                    self.stop_loss = abs(self.position.qty), new\\n            return\\n        history = self.signal_candles\\n        atr = float(ta.atr(history))\\n        if not math.isfinite(atr) or atr <= 0:\\n            return\\n        entry = float(self.position.entry_price)\\n        distance = self.vars['initial_distance']\\n        self.vars['best_close'] = max(self.vars['best_close'], float(history[-1, 2]))\\n        best_r = (self.vars['best_close'] - entry) / distance\\n        mult = float(self.hp['trail_atr'])\\n        # Inherited late-trend tightening; retained as a controlled baseline choice.\\n        if best_r >= 8:\\n            mult *= 0.62\\n        elif best_r >= 5:\\n            mult *= 0.78\\n        stop = self.vars['best_close'] - mult * atr\\n        if best_r >= float(self.hp['be_r']):\\n            stop = max(stop, entry * (1 + 2.5 * self.fee_rate))\\n        if self.average_stop_loss < stop < self.price:\\n            self.stop_loss = abs(self.position.qty), stop\\n\\n    def on_close_position(self, order, closed_trade) -> None:\\n        if closed_trade.type == 'short':\\n            self._payoff_log('short_close', exit_price=float(order.price))\\n        self._ledger().pop(self._key(), None)\\n\\n    def _record_capacity(self, side, capital, budget, unit_risk, entry,\\n                         room, margin_room, raw_qty, step) -> None:\\n        \\\"\\\"\\\"Observe existing sizing only; never gates signals or changes quantities.\\n\\n        Counts plans reaching sizing while flat and without a pending entry.\\n        It does not infer trades that would have filled or signals while occupied.\\n        Quantity tolerances below classify numerical ties, not trading thresholds.\\n        \\\"\\\"\\\"\\n        audit = self.vars.setdefault('portfolio_capacity_audit', {})\\n        row = audit.setdefault(side, {'eligible_sizing_attempts': 0,\\n                                     'risk_budget_limited': 0,\\n                                     'notional_or_weight_limited': 0,\\n                                     'margin_limited': 0,\\n                                     'sized_below_trade_target': 0,\\n                                     'capacity_zero': 0,\\n                                     'zero_after_lot_rounding': 0})\\n        row['eligible_sizing_attempts'] += 1\\n        target_qty = capital * TRADE_RISK / unit_risk\\n        tolerance = max(1e-8, abs(target_qty) * 1e-10)\\n        row['risk_budget_limited'] += int(budget / unit_risk + tolerance < target_qty)\\n        row['notional_or_weight_limited'] += int(room / entry + tolerance < target_qty)\\n        row['margin_limited'] += int(margin_room / entry + tolerance < target_qty)\\n        row['sized_below_trade_target'] += int(raw_qty + tolerance < target_qty)\\n        row['capacity_zero'] += int(raw_qty <= 0 < target_qty)\\n        row['zero_after_lot_rounding'] += int(math.floor(raw_qty / step) * step <= 0 < raw_qty)\\n\\n    def terminate(self) -> None:\\n        # One compact persisted record per route, after engine final liquidation.\\n        # The runner must use debug=true to persist these logs; decisions are unchanged.\\n        jh.debug('BTC_PAYOFF_SUMMARY ' + json.dumps({\\n            'strategy': self.__class__.__name__,\\n            'counts': self.vars.get('payoff_counts', {})\\n        }, sort_keys=True))\\n        jh.debug('PORT_CAPACITY ' + json.dumps({\\n            'symbol': self.symbol, 'strategy': self.__class__.__name__,\\n            'trade_risk': TRADE_RISK, 'portfolio_risk': PORTFOLIO_RISK,\\n            'notional_cap': NOTIONAL_CAP,\\n            'counts': self.vars.get('portfolio_capacity_audit', {})\\n        }, sort_keys=True))\\n\\n    def _payoff_postfill_bar(self) -> bool:\\n        \\\"\\\"\\\"Require a whole closed bar after entry; exclude the partial fill bar.\\\"\\\"\\\"\\n        c = self.signal_candles\\n        opened = int(self.vars['opened_time'])\\n        if not len(c) or int(c[-1, 0]) != int(self.closed_candle_open_time):\\n            self._payoff_log('invalid_closed_bar')\\n            return False\\n        # Comparing only close time with fill time would wrongly admit the\\n        # partly pre-entry 4h candle. An equal open is safe: no prefill interval.\\n        if int(c[-1, 0]) < opened or int(self.time) <= opened:\\n            self._payoff_log('partial_bar_skipped', bar_open=int(c[-1, 0]))\\n            return False\\n        return True\\n\\n    def _payoff_log(self, event: str, **fields) -> None:\\n        \\\"\\\"\\\"Persist causal review points; counters never alter decisions or sizing.\\\"\\\"\\\"\\n        counts = self.vars.setdefault('payoff_counts', {})\\n        counts[event] = counts.get(event, 0) + 1\\n        jh.debug('BTC_PAYOFF ' + json.dumps({\\n            'strategy': self.__class__.__name__, 'event': event,\\n            'time': int(self.time), 'bar_open': int(self.closed_candle_open_time),\\n            'opened': self.vars.get('opened_time'),\\n            'entry': float(self.position.entry_price) if self.is_open else None,\\n            'price': float(self.price), **fields\\n        }, sort_keys=True))\\n\",\"BtcPayoffR102\":\"import math\\nimport json\\nimport jesse.helpers as jh\\nimport numpy as np\\nfrom jesse.strategies import Strategy, cached\\nfrom jesse import utils\\nimport jesse.indicators as ta\\n\\n# User-approved research limits; risk is not an optimization parameter.\\nTRADE_RISK = 0.01\\nPORTFOLIO_RISK = 0.08\\nNOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.\\nSLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.\\n\\n\\nclass BtcPayoffR102(Strategy):\\n    \\\"\\\"\\\"Frozen BtcPayoffR102 short-management experiment; long runner unchanged.\\n\\n    Shared risk and margin reservations; exploratory research, not approved live.\\n    SPY uses a session-filtered SPX CFD proxy; holidays and native parity remain\\n    unverified. Parameter-neighbour variants are sensitivity controls, not winners.\\n    \\\"\\\"\\\"\\n\\n    def hyperparameters(self) -> list:\\n        return [\\n            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},\\n            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},\\n            {'name': 'ema_slow', 'type': int, 'min': 80, 'max': 140, 'default': 80},\\n            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},\\n            {'name': 'stop_atr', 'type': float, 'min': 1.6, 'max': 3.0, 'default': 2.0},\\n            {'name': 'trail_atr', 'type': float, 'min': 3.0, 'max': 5.0, 'default': 4.2},\\n            {'name': 'be_r', 'type': float, 'min': 1.75, 'max': 3.0, 'default': 2.25},\\n        ]\\n\\n    def trading_hours(self):\\n        if self.symbol == 'SPY-USDT':\\n            # The fixed UTC whole-bar intersection excludes the US index daily\\n            # break in both DST regimes. This is an intentional common window,\\n            # not an assertion that the source's full session ends at 20:00 UTC.\\n            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}\\n        return None\\n\\n    @property\\n    @cached\\n    def signal_candles(self):\\n        return utils.filter_candles_by_hours(self.candles, self.trading_hours())\\n\\n    def _entry_window(self) -> bool:\\n        if self.symbol != 'SPY-USDT':\\n            return True\\n        # A closed bar opening at 12:00 triggers at 16:00. Its order expires\\n        # at 20:00, before the excluded 20:00-24:00 bucket. A 16:00-open bar\\n        # must not arm a new order at 20:00. Pending orders still cancel then.\\n        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}\\n        return self.is_trading_hours and utils.is_in_trading_hours(\\n            self.closed_candle_open_time, window)\\n\\n    def _ledger(self) -> dict:\\n        return self.shared_vars.setdefault('phase2_reservations', {})\\n\\n    def _key(self) -> str:\\n        return self.exchange + ':' + self.symbol\\n\\n    def _capital(self) -> float:\\n        # Floating gains do not enlarge the risk budget; floating losses reduce it.\\n        return max(0.0, min(float(self.balance), float(self.portfolio_value)))\\n\\n    def _committed(self) -> tuple:\\n        risk, notional = 0.0, 0.0\\n        ledger = self._ledger()\\n        for route in self.routes:\\n            if route.exchange != self.exchange:\\n                continue\\n            strategy = route.strategy\\n            if strategy.is_open:\\n                qty = abs(float(strategy.position.qty))\\n                entry = float(strategy.position.entry_price)\\n                # Risk is measured from the current mark, so protected floating PnL\\n                # is not silently treated as free capacity for another trade.\\n                value = abs(float(strategy.position.value))\\n                mark = value / qty if qty else entry\\n                stop = float(strategy.average_stop_loss)\\n                distance = max(0.0, mark - stop) if strategy.is_long else max(0.0, stop - mark)\\n                risk += qty * (distance + mark * (self.fee_rate + SLIPPAGE_RESERVE))\\n                notional += value\\n            else:\\n                reservation = ledger.get(route.exchange + ':' + route.symbol)\\n                if reservation:\\n                    # Includes not-yet-filled STOP/LIMIT entries, not only open positions.\\n                    risk += reservation['risk']\\n                    notional += reservation['notional']\\n        return risk, notional\\n\\n    def _volatility_share(self) -> float:\\n        \\\"\\\"\\\"Reserve a common gross-exposure budget using inverse ATR fractions.\\n\\n        All configured assets receive an ex-ante share, even while their signal\\n        is idle. This prevents the first route from consuming all shared margin.\\n        It is a capital-efficiency tradeoff to test, not an optimal allocation.\\n        \\\"\\\"\\\"\\n        weights = {}\\n        for route in self.routes:\\n            if route.exchange != self.exchange:\\n                continue\\n            c = utils.filter_candles_by_hours(route.strategy.candles, route.strategy.trading_hours())\\n            if len(c) < int(self.hp['ema_slow']) + 20:\\n                return 0.0\\n            atr = float(ta.atr(c))\\n            price = float(c[-1, 2])\\n            if not math.isfinite(atr) or atr <= 0 or price <= 0:\\n                return 0.0\\n            # Stops use a common ATR multiple. Equal risk therefore needs\\n            # notional proportional to price/ATR before gross-leverage scaling.\\n            weights[route.symbol] = price / atr\\n        return weights.get(self.symbol, 0.0) / sum(weights.values()) if weights else 0.0\\n\\n    def _plan(self) -> bool:\\n        if self.symbol not in ('BTC-USDT', 'PAXG-USDT', 'SPY-USDT') or not self._entry_window():\\n            return False\\n        c = self.signal_candles\\n        n = int(self.hp['donchian_len'])\\n        slow_n = int(self.hp['ema_slow'])\\n        if len(c) < max(slow_n + 20, n):\\n            return False\\n        fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))\\n        slow = ta.ema(c, period=slow_n, sequential=True)\\n        atr = float(ta.atr(c))\\n        adx = float(ta.adx(c))\\n        rsi = float(ta.rsi(c))\\n        # The closed bar has broken the PRIOR channel. A passive LIMIT at that\\n        # boundary can fill only on a future retest within one 4h order lifetime.\\n        entry = float(np.max(c[-n-1:-1, 3]))\\n        if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):\\n            return False\\n        if not (atr > 0 and entry < self.price <= entry + atr and self.price > slow[-1]\\n                and fast > slow[-1] > slow[-5] and adx >= self.hp['adx_min']\\n                and 52 <= rsi <= 76 and self.high - self.low <= 3 * atr):\\n            return False\\n        distance = float(self.hp['stop_atr']) * atr\\n        if not 0 < distance < entry:\\n            return False\\n        capital = self._capital()\\n        committed_risk, committed_notional = self._committed()\\n        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - committed_risk))\\n        # Fees at both planned entry and stop, plus an explicit adverse-fill reserve.\\n        unit_risk = distance + self.fee_rate * (entry + entry - distance) + SLIPPAGE_RESERVE * entry\\n        room = min(max(0.0, capital * NOTIONAL_CAP - committed_notional),\\n                   capital * NOTIONAL_CAP * self._volatility_share())\\n        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)\\n        qty = min(budget / unit_risk, room / entry, margin_room / entry)\\n        # Historical research precision only. Native symbol lot/min-notional\\n        # constraints must be verified before any live use.\\n        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001\\n        self._record_capacity('long', capital, budget, unit_risk, entry,\\n                              room, margin_room, qty, step)\\n        qty = math.floor(qty / step) * step\\n        if qty <= 0:\\n            return False\\n        self.vars['plan'] = {\\n            'qty': qty, 'entry': entry, 'distance': distance,\\n            'risk': qty * unit_risk, 'notional': qty * entry,\\n        }\\n        return True\\n\\n    def _signal(self) -> int:\\n        # Compute exactly one plan per bar, with long priority. Checking\\n        # should_short after go_long must never overwrite a queued long plan.\\n        if self.vars.get('signal_index') != self.index:\\n            self.vars['signal_index'] = self.index\\n            self.vars['signal_value'] = 1 if self._plan() else (-1 if self._short_plan() else 0)\\n        return self.vars['signal_value']\\n\\n    def should_long(self) -> bool:\\n        return self._signal() == 1\\n\\n    def should_short(self) -> bool:\\n        return self._signal() == -1\\n\\n    def go_long(self) -> None:\\n        plan = self.vars['plan']\\n        self._ledger()[self._key()] = dict(plan)\\n        self.buy = plan['qty'], plan['entry']\\n\\n    def _short_plan(self) -> bool:\\n        \\\"\\\"\\\"Test selloff continuation instead of buying an oversold dip.\\n\\n        A rising slow regime can still suffer a fast liquidation leg. This\\n        exploratory hypothesis came from the failed long mean-reversion sleeve;\\n        it is development evidence, not an independent validation.\\n        \\\"\\\"\\\"\\n        if self.symbol != 'BTC-USDT' or not self._entry_window():\\n            return False\\n        c = self.signal_candles\\n        if len(c) < 140:\\n            return False\\n        macro = ta.ema(c, period=120, sequential=True)\\n        fast = float(ta.ema(c, period=20))\\n        atr = float(ta.atr(c))\\n        quick_rsi = float(ta.rsi(c, period=3))\\n        if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, quick_rsi)):\\n            return False\\n        if not (atr > 0 and macro[-1] > macro[-10]\\n                and self.price > macro[-1] - atr and quick_rsi <= 20):\\n            return False\\n        entry = min(float(c[-1, 4]), self.price - 0.25 * atr)\\n        distance = fast - entry\\n        if not (atr <= distance <= 3 * atr and distance >= 6 * self.fee_rate * entry):\\n            return False\\n        capital = self._capital()\\n        risk, notional = self._committed()\\n        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))\\n        unit_risk = distance + self.fee_rate * (2 * entry + distance) + SLIPPAGE_RESERVE * entry\\n        room = min(max(0.0, capital * NOTIONAL_CAP - notional),\\n                   capital * NOTIONAL_CAP * self._volatility_share())\\n        qty = min(budget / unit_risk, room / entry,\\n                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)\\n        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001\\n        self._record_capacity('short', capital, budget, unit_risk, entry,\\n                              room, max(0.0, float(self.leveraged_available_margin) * 0.90), qty, step)\\n        qty = math.floor(qty / step) * step\\n        if qty <= 0:\\n            return False\\n        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,\\n                             'risk': qty * unit_risk, 'notional': qty * entry,\\n                             'target_distance': 1.5 * atr}\\n        return True\\n\\n    def go_short(self) -> None:\\n        plan = self.vars['plan']\\n        self._ledger()[self._key()] = dict(plan)\\n        self.sell = plan['qty'], plan['entry']\\n\\n    def should_cancel_entry(self) -> bool:\\n        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.\\n        # Jesse processes cancellation before evaluating the next route.\\n        self._ledger().pop(self._key(), None)\\n        return True\\n\\n    def on_open_position(self, order) -> None:\\n        entry = float(self.position.entry_price)\\n        distance = self.vars['plan']['distance']\\n        self.vars['initial_distance'] = distance\\n        # An intrabar fill must not inherit highs/closes from before its entry.\\n        self.vars['best_close'] = entry\\n        if self.is_short:\\n            self.vars['opened_time'] = int(self.time)\\n            self.vars['payoff_be_latched'] = False\\n            self._payoff_log('short_open', initial_stop=entry + distance,\\n                             initial_target=entry - self.vars['plan']['target_distance'])\\n            self.stop_loss = abs(self.position.qty), entry + distance\\n            self.take_profit = abs(self.position.qty), entry - self.vars['plan']['target_distance']\\n        else:\\n            self.stop_loss = abs(self.position.qty), entry - distance\\n        self._ledger().pop(self._key(), None)\\n\\n    def update_position(self) -> None:\\n        if self.is_short:\\n            if self.time - self.vars['opened_time'] >= 72 * 60 * 60 * 1000:\\n                self._payoff_log('timeout')\\n                self.liquidate()\\n                return\\n            if not self._payoff_postfill_bar():\\n                return\\n            entry = float(self.position.entry_price)\\n            # Half of the original target is an ex-ante milestone, not a fitted\\n            # elapsed-time threshold. Only a complete postfill bar can latch it.\\n            milestone = entry - 0.5 * self.vars['plan']['target_distance']\\n            if not self.vars['payoff_be_latched'] and self.price <= milestone:\\n                self.vars['payoff_be_latched'] = True\\n                self._payoff_log('be_latch', milestone=milestone)\\n            if self.vars['payoff_be_latched']:\\n                # Exact nominal short breakeven for equal fees on both fills:\\n                # entry - exit - f*(entry + exit) = 0. No gap/spread guarantee.\\n                fee = 0.00045\\n                new = entry * (1 - fee) / (1 + fee)\\n                old = float(self.average_stop_loss)\\n                if self.price < new < old:\\n                    self._payoff_log('be_stop', old_stop=old, new_stop=new)\\n                    self.stop_loss = abs(self.position.qty), new\\n            return\\n        history = self.signal_candles\\n        atr = float(ta.atr(history))\\n        if not math.isfinite(atr) or atr <= 0:\\n            return\\n        entry = float(self.position.entry_price)\\n        distance = self.vars['initial_distance']\\n        self.vars['best_close'] = max(self.vars['best_close'], float(history[-1, 2]))\\n        best_r = (self.vars['best_close'] - entry) / distance\\n        mult = float(self.hp['trail_atr'])\\n        # Inherited late-trend tightening; retained as a controlled baseline choice.\\n        if best_r >= 8:\\n            mult *= 0.62\\n        elif best_r >= 5:\\n            mult *= 0.78\\n        stop = self.vars['best_close'] - mult * atr\\n        if best_r >= float(self.hp['be_r']):\\n            stop = max(stop, entry * (1 + 2.5 * self.fee_rate))\\n        if self.average_stop_loss < stop < self.price:\\n            self.stop_loss = abs(self.position.qty), stop\\n\\n    def on_close_position(self, order, closed_trade) -> None:\\n        if closed_trade.type == 'short':\\n            self._payoff_log('short_close', exit_price=float(order.price))\\n        self._ledger().pop(self._key(), None)\\n\\n    def _record_capacity(self, side, capital, budget, unit_risk, entry,\\n                         room, margin_room, raw_qty, step) -> None:\\n        \\\"\\\"\\\"Observe existing sizing only; never gates signals or changes quantities.\\n\\n        Counts plans reaching sizing while flat and without a pending entry.\\n        It does not infer trades that would have filled or signals while occupied.\\n        Quantity tolerances below classify numerical ties, not trading thresholds.\\n        \\\"\\\"\\\"\\n        audit = self.vars.setdefault('portfolio_capacity_audit', {})\\n        row = audit.setdefault(side, {'eligible_sizing_attempts': 0,\\n                                     'risk_budget_limited': 0,\\n                                     'notional_or_weight_limited': 0,\\n                                     'margin_limited': 0,\\n                                     'sized_below_trade_target': 0,\\n                                     'capacity_zero': 0,\\n                                     'zero_after_lot_rounding': 0})\\n        row['eligible_sizing_attempts'] += 1\\n        target_qty = capital * TRADE_RISK / unit_risk\\n        tolerance = max(1e-8, abs(target_qty) * 1e-10)\\n        row['risk_budget_limited'] += int(budget / unit_risk + tolerance < target_qty)\\n        row['notional_or_weight_limited'] += int(room / entry + tolerance < target_qty)\\n        row['margin_limited'] += int(margin_room / entry + tolerance < target_qty)\\n        row['sized_below_trade_target'] += int(raw_qty + tolerance < target_qty)\\n        row['capacity_zero'] += int(raw_qty <= 0 < target_qty)\\n        row['zero_after_lot_rounding'] += int(math.floor(raw_qty / step) * step <= 0 < raw_qty)\\n\\n    def terminate(self) -> None:\\n        # One compact persisted record per route, after engine final liquidation.\\n        # The runner must use debug=true to persist these logs; decisions are unchanged.\\n        jh.debug('BTC_PAYOFF_SUMMARY ' + json.dumps({\\n            'strategy': self.__class__.__name__,\\n            'counts': self.vars.get('payoff_counts', {})\\n        }, sort_keys=True))\\n        jh.debug('PORT_CAPACITY ' + json.dumps({\\n            'symbol': self.symbol, 'strategy': self.__class__.__name__,\\n            'trade_risk': TRADE_RISK, 'portfolio_risk': PORTFOLIO_RISK,\\n            'notional_cap': NOTIONAL_CAP,\\n            'counts': self.vars.get('portfolio_capacity_audit', {})\\n        }, sort_keys=True))\\n\\n    def _payoff_postfill_bar(self) -> bool:\\n        \\\"\\\"\\\"Require a whole closed bar after entry; exclude the partial fill bar.\\\"\\\"\\\"\\n        c = self.signal_candles\\n        opened = int(self.vars['opened_time'])\\n        if not len(c) or int(c[-1, 0]) != int(self.closed_candle_open_time):\\n            self._payoff_log('invalid_closed_bar')\\n            return False\\n        # Comparing only close time with fill time would wrongly admit the\\n        # partly pre-entry 4h candle. An equal open is safe: no prefill interval.\\n        if int(c[-1, 0]) < opened or int(self.time) <= opened:\\n            self._payoff_log('partial_bar_skipped', bar_open=int(c[-1, 0]))\\n            return False\\n        return True\\n\\n    def _payoff_log(self, event: str, **fields) -> None:\\n        \\\"\\\"\\\"Persist causal review points; counters never alter decisions or sizing.\\\"\\\"\\\"\\n        counts = self.vars.setdefault('payoff_counts', {})\\n        counts[event] = counts.get(event, 0) + 1\\n        jh.debug('BTC_PAYOFF ' + json.dumps({\\n            'strategy': self.__class__.__name__, 'event': event,\\n            'time': int(self.time), 'bar_open': int(self.closed_candle_open_time),\\n            'opened': self.vars.get('opened_time'),\\n            'entry': float(self.position.entry_price) if self.is_open else None,\\n            'price': float(self.price), **fields\\n        }, sort_keys=True))\\n\",\"BtcPayoffR103\":\"import math\\nimport json\\nimport jesse.helpers as jh\\nimport numpy as np\\nfrom jesse.strategies import Strategy, cached\\nfrom jesse import utils\\nimport jesse.indicators as ta\\n\\n# User-approved research limits; risk is not an optimization parameter.\\nTRADE_RISK = 0.01\\nPORTFOLIO_RISK = 0.08\\nNOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.\\nSLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.\\n\\n\\nclass BtcPayoffR103(Strategy):\\n    \\\"\\\"\\\"Frozen BtcPayoffR103 short-management experiment; long runner unchanged.\\n\\n    Shared risk and margin reservations; exploratory research, not approved live.\\n    SPY uses a session-filtered SPX CFD proxy; holidays and native parity remain\\n    unverified. Parameter-neighbour variants are sensitivity controls, not winners.\\n    \\\"\\\"\\\"\\n\\n    def hyperparameters(self) -> list:\\n        return [\\n            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},\\n            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},\\n            {'name': 'ema_slow', 'type': int, 'min': 80, 'max': 140, 'default': 80},\\n            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},\\n            {'name': 'stop_atr', 'type': float, 'min': 1.6, 'max': 3.0, 'default': 2.0},\\n            {'name': 'trail_atr', 'type': float, 'min': 3.0, 'max': 5.0, 'default': 4.2},\\n            {'name': 'be_r', 'type': float, 'min': 1.75, 'max': 3.0, 'default': 2.25},\\n        ]\\n\\n    def trading_hours(self):\\n        if self.symbol == 'SPY-USDT':\\n            # The fixed UTC whole-bar intersection excludes the US index daily\\n            # break in both DST regimes. This is an intentional common window,\\n            # not an assertion that the source's full session ends at 20:00 UTC.\\n            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}\\n        return None\\n\\n    @property\\n    @cached\\n    def signal_candles(self):\\n        return utils.filter_candles_by_hours(self.candles, self.trading_hours())\\n\\n    def _entry_window(self) -> bool:\\n        if self.symbol != 'SPY-USDT':\\n            return True\\n        # A closed bar opening at 12:00 triggers at 16:00. Its order expires\\n        # at 20:00, before the excluded 20:00-24:00 bucket. A 16:00-open bar\\n        # must not arm a new order at 20:00. Pending orders still cancel then.\\n        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}\\n        return self.is_trading_hours and utils.is_in_trading_hours(\\n            self.closed_candle_open_time, window)\\n\\n    def _ledger(self) -> dict:\\n        return self.shared_vars.setdefault('phase2_reservations', {})\\n\\n    def _key(self) -> str:\\n        return self.exchange + ':' + self.symbol\\n\\n    def _capital(self) -> float:\\n        # Floating gains do not enlarge the risk budget; floating losses reduce it.\\n        return max(0.0, min(float(self.balance), float(self.portfolio_value)))\\n\\n    def _committed(self) -> tuple:\\n        risk, notional = 0.0, 0.0\\n        ledger = self._ledger()\\n        for route in self.routes:\\n            if route.exchange != self.exchange:\\n                continue\\n            strategy = route.strategy\\n            if strategy.is_open:\\n                qty = abs(float(strategy.position.qty))\\n                entry = float(strategy.position.entry_price)\\n                # Risk is measured from the current mark, so protected floating PnL\\n                # is not silently treated as free capacity for another trade.\\n                value = abs(float(strategy.position.value))\\n                mark = value / qty if qty else entry\\n                stop = float(strategy.average_stop_loss)\\n                distance = max(0.0, mark - stop) if strategy.is_long else max(0.0, stop - mark)\\n                risk += qty * (distance + mark * (self.fee_rate + SLIPPAGE_RESERVE))\\n                notional += value\\n            else:\\n                reservation = ledger.get(route.exchange + ':' + route.symbol)\\n                if reservation:\\n                    # Includes not-yet-filled STOP/LIMIT entries, not only open positions.\\n                    risk += reservation['risk']\\n                    notional += reservation['notional']\\n        return risk, notional\\n\\n    def _volatility_share(self) -> float:\\n        \\\"\\\"\\\"Reserve a common gross-exposure budget using inverse ATR fractions.\\n\\n        All configured assets receive an ex-ante share, even while their signal\\n        is idle. This prevents the first route from consuming all shared margin.\\n        It is a capital-efficiency tradeoff to test, not an optimal allocation.\\n        \\\"\\\"\\\"\\n        weights = {}\\n        for route in self.routes:\\n            if route.exchange != self.exchange:\\n                continue\\n            c = utils.filter_candles_by_hours(route.strategy.candles, route.strategy.trading_hours())\\n            if len(c) < int(self.hp['ema_slow']) + 20:\\n                return 0.0\\n            atr = float(ta.atr(c))\\n            price = float(c[-1, 2])\\n            if not math.isfinite(atr) or atr <= 0 or price <= 0:\\n                return 0.0\\n            # Stops use a common ATR multiple. Equal risk therefore needs\\n            # notional proportional to price/ATR before gross-leverage scaling.\\n            weights[route.symbol] = price / atr\\n        return weights.get(self.symbol, 0.0) / sum(weights.values()) if weights else 0.0\\n\\n    def _plan(self) -> bool:\\n        if self.symbol not in ('BTC-USDT', 'PAXG-USDT', 'SPY-USDT') or not self._entry_window():\\n            return False\\n        c = self.signal_candles\\n        n = int(self.hp['donchian_len'])\\n        slow_n = int(self.hp['ema_slow'])\\n        if len(c) < max(slow_n + 20, n):\\n            return False\\n        fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))\\n        slow = ta.ema(c, period=slow_n, sequential=True)\\n        atr = float(ta.atr(c))\\n        adx = float(ta.adx(c))\\n        rsi = float(ta.rsi(c))\\n        # The closed bar has broken the PRIOR channel. A passive LIMIT at that\\n        # boundary can fill only on a future retest within one 4h order lifetime.\\n        entry = float(np.max(c[-n-1:-1, 3]))\\n        if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):\\n            return False\\n        if not (atr > 0 and entry < self.price <= entry + atr and self.price > slow[-1]\\n                and fast > slow[-1] > slow[-5] and adx >= self.hp['adx_min']\\n                and 52 <= rsi <= 76 and self.high - self.low <= 3 * atr):\\n            return False\\n        distance = float(self.hp['stop_atr']) * atr\\n        if not 0 < distance < entry:\\n            return False\\n        capital = self._capital()\\n        committed_risk, committed_notional = self._committed()\\n        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - committed_risk))\\n        # Fees at both planned entry and stop, plus an explicit adverse-fill reserve.\\n        unit_risk = distance + self.fee_rate * (entry + entry - distance) + SLIPPAGE_RESERVE * entry\\n        room = min(max(0.0, capital * NOTIONAL_CAP - committed_notional),\\n                   capital * NOTIONAL_CAP * self._volatility_share())\\n        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)\\n        qty = min(budget / unit_risk, room / entry, margin_room / entry)\\n        # Historical research precision only. Native symbol lot/min-notional\\n        # constraints must be verified before any live use.\\n        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001\\n        self._record_capacity('long', capital, budget, unit_risk, entry,\\n                              room, margin_room, qty, step)\\n        qty = math.floor(qty / step) * step\\n        if qty <= 0:\\n            return False\\n        self.vars['plan'] = {\\n            'qty': qty, 'entry': entry, 'distance': distance,\\n            'risk': qty * unit_risk, 'notional': qty * entry,\\n        }\\n        return True\\n\\n    def _signal(self) -> int:\\n        # Compute exactly one plan per bar, with long priority. Checking\\n        # should_short after go_long must never overwrite a queued long plan.\\n        if self.vars.get('signal_index') != self.index:\\n            self.vars['signal_index'] = self.index\\n            self.vars['signal_value'] = 1 if self._plan() else (-1 if self._short_plan() else 0)\\n        return self.vars['signal_value']\\n\\n    def should_long(self) -> bool:\\n        return self._signal() == 1\\n\\n    def should_short(self) -> bool:\\n        return self._signal() == -1\\n\\n    def go_long(self) -> None:\\n        plan = self.vars['plan']\\n        self._ledger()[self._key()] = dict(plan)\\n        self.buy = plan['qty'], plan['entry']\\n\\n    def _short_plan(self) -> bool:\\n        \\\"\\\"\\\"Test selloff continuation instead of buying an oversold dip.\\n\\n        A rising slow regime can still suffer a fast liquidation leg. This\\n        exploratory hypothesis came from the failed long mean-reversion sleeve;\\n        it is development evidence, not an independent validation.\\n        \\\"\\\"\\\"\\n        if self.symbol != 'BTC-USDT' or not self._entry_window():\\n            return False\\n        c = self.signal_candles\\n        if len(c) < 140:\\n            return False\\n        macro = ta.ema(c, period=120, sequential=True)\\n        fast = float(ta.ema(c, period=20))\\n        atr = float(ta.atr(c))\\n        quick_rsi = float(ta.rsi(c, period=3))\\n        if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, quick_rsi)):\\n            return False\\n        if not (atr > 0 and macro[-1] > macro[-10]\\n                and self.price > macro[-1] - atr and quick_rsi <= 20):\\n            return False\\n        entry = min(float(c[-1, 4]), self.price - 0.25 * atr)\\n        distance = fast - entry\\n        if not (atr <= distance <= 3 * atr and distance >= 6 * self.fee_rate * entry):\\n            return False\\n        capital = self._capital()\\n        risk, notional = self._committed()\\n        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))\\n        unit_risk = distance + self.fee_rate * (2 * entry + distance) + SLIPPAGE_RESERVE * entry\\n        room = min(max(0.0, capital * NOTIONAL_CAP - notional),\\n                   capital * NOTIONAL_CAP * self._volatility_share())\\n        qty = min(budget / unit_risk, room / entry,\\n                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)\\n        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001\\n        self._record_capacity('short', capital, budget, unit_risk, entry,\\n                              room, max(0.0, float(self.leveraged_available_margin) * 0.90), qty, step)\\n        qty = math.floor(qty / step) * step\\n        if qty <= 0:\\n            return False\\n        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,\\n                             'risk': qty * unit_risk, 'notional': qty * entry,\\n                             'target_distance': 1.5 * atr}\\n        return True\\n\\n    def go_short(self) -> None:\\n        plan = self.vars['plan']\\n        self._ledger()[self._key()] = dict(plan)\\n        self.sell = plan['qty'], plan['entry']\\n\\n    def should_cancel_entry(self) -> bool:\\n        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.\\n        # Jesse processes cancellation before evaluating the next route.\\n        self._ledger().pop(self._key(), None)\\n        return True\\n\\n    def on_open_position(self, order) -> None:\\n        entry = float(self.position.entry_price)\\n        distance = self.vars['plan']['distance']\\n        self.vars['initial_distance'] = distance\\n        # An intrabar fill must not inherit highs/closes from before its entry.\\n        self.vars['best_close'] = entry\\n        if self.is_short:\\n            self.vars['opened_time'] = int(self.time)\\n            self._payoff_log('short_open', initial_stop=entry + distance,\\n                             initial_target=entry - self.vars['plan']['target_distance'])\\n            self.stop_loss = abs(self.position.qty), entry + distance\\n            self.take_profit = abs(self.position.qty), entry - self.vars['plan']['target_distance']\\n        else:\\n            self.stop_loss = abs(self.position.qty), entry - distance\\n        self._ledger().pop(self._key(), None)\\n\\n    def update_position(self) -> None:\\n        if self.is_short:\\n            if self.time - self.vars['opened_time'] >= 72 * 60 * 60 * 1000:\\n                self._payoff_log('timeout')\\n                self.liquidate()\\n                return\\n            if not self._payoff_postfill_bar():\\n                return\\n            # RSI3 is the original entry momentum measure. Its neutral midpoint\\n            # is fixed before testing, not chosen from observed exit outcomes.\\n            rsi = float(ta.rsi(self.signal_candles, period=3))\\n            if math.isfinite(rsi) and rsi >= 50:\\n                self._payoff_log('rsi_neutral', rsi=rsi)\\n                self.liquidate()\\n            return\\n        history = self.signal_candles\\n        atr = float(ta.atr(history))\\n        if not math.isfinite(atr) or atr <= 0:\\n            return\\n        entry = float(self.position.entry_price)\\n        distance = self.vars['initial_distance']\\n        self.vars['best_close'] = max(self.vars['best_close'], float(history[-1, 2]))\\n        best_r = (self.vars['best_close'] - entry) / distance\\n        mult = float(self.hp['trail_atr'])\\n        # Inherited late-trend tightening; retained as a controlled baseline choice.\\n        if best_r >= 8:\\n            mult *= 0.62\\n        elif best_r >= 5:\\n            mult *= 0.78\\n        stop = self.vars['best_close'] - mult * atr\\n        if best_r >= float(self.hp['be_r']):\\n            stop = max(stop, entry * (1 + 2.5 * self.fee_rate))\\n        if self.average_stop_loss < stop < self.price:\\n            self.stop_loss = abs(self.position.qty), stop\\n\\n    def on_close_position(self, order, closed_trade) -> None:\\n        if closed_trade.type == 'short':\\n            self._payoff_log('short_close', exit_price=float(order.price))\\n        self._ledger().pop(self._key(), None)\\n\\n    def _record_capacity(self, side, capital, budget, unit_risk, entry,\\n                         room, margin_room, raw_qty, step) -> None:\\n        \\\"\\\"\\\"Observe existing sizing only; never gates signals or changes quantities.\\n\\n        Counts plans reaching sizing while flat and without a pending entry.\\n        It does not infer trades that would have filled or signals while occupied.\\n        Quantity tolerances below classify numerical ties, not trading thresholds.\\n        \\\"\\\"\\\"\\n        audit = self.vars.setdefault('portfolio_capacity_audit', {})\\n        row = audit.setdefault(side, {'eligible_sizing_attempts': 0,\\n                                     'risk_budget_limited': 0,\\n                                     'notional_or_weight_limited': 0,\\n                                     'margin_limited': 0,\\n                                     'sized_below_trade_target': 0,\\n                                     'capacity_zero': 0,\\n                                     'zero_after_lot_rounding': 0})\\n        row['eligible_sizing_attempts'] += 1\\n        target_qty = capital * TRADE_RISK / unit_risk\\n        tolerance = max(1e-8, abs(target_qty) * 1e-10)\\n        row['risk_budget_limited'] += int(budget / unit_risk + tolerance < target_qty)\\n        row['notional_or_weight_limited'] += int(room / entry + tolerance < target_qty)\\n        row['margin_limited'] += int(margin_room / entry + tolerance < target_qty)\\n        row['sized_below_trade_target'] += int(raw_qty + tolerance < target_qty)\\n        row['capacity_zero'] += int(raw_qty <= 0 < target_qty)\\n        row['zero_after_lot_rounding'] += int(math.floor(raw_qty / step) * step <= 0 < raw_qty)\\n\\n    def terminate(self) -> None:\\n        # One compact persisted record per route, after engine final liquidation.\\n        # The runner must use debug=true to persist these logs; decisions are unchanged.\\n        jh.debug('BTC_PAYOFF_SUMMARY ' + json.dumps({\\n            'strategy': self.__class__.__name__,\\n            'counts': self.vars.get('payoff_counts', {})\\n        }, sort_keys=True))\\n        jh.debug('PORT_CAPACITY ' + json.dumps({\\n            'symbol': self.symbol, 'strategy': self.__class__.__name__,\\n            'trade_risk': TRADE_RISK, 'portfolio_risk': PORTFOLIO_RISK,\\n            'notional_cap': NOTIONAL_CAP,\\n            'counts': self.vars.get('portfolio_capacity_audit', {})\\n        }, sort_keys=True))\\n\\n    def _payoff_postfill_bar(self) -> bool:\\n        \\\"\\\"\\\"Require a whole closed bar after entry; exclude the partial fill bar.\\\"\\\"\\\"\\n        c = self.signal_candles\\n        opened = int(self.vars['opened_time'])\\n        if not len(c) or int(c[-1, 0]) != int(self.closed_candle_open_time):\\n            self._payoff_log('invalid_closed_bar')\\n            return False\\n        # Comparing only close time with fill time would wrongly admit the\\n        # partly pre-entry 4h candle. An equal open is safe: no prefill interval.\\n        if int(c[-1, 0]) < opened or int(self.time) <= opened:\\n            self._payoff_log('partial_bar_skipped', bar_open=int(c[-1, 0]))\\n            return False\\n        return True\\n\\n    def _payoff_log(self, event: str, **fields) -> None:\\n        \\\"\\\"\\\"Persist causal review points; counters never alter decisions or sizing.\\\"\\\"\\\"\\n        counts = self.vars.setdefault('payoff_counts', {})\\n        counts[event] = counts.get(event, 0) + 1\\n        jh.debug('BTC_PAYOFF ' + json.dumps({\\n            'strategy': self.__class__.__name__, 'event': event,\\n            'time': int(self.time), 'bar_open': int(self.closed_candle_open_time),\\n            'opened': self.vars.get('opened_time'),\\n            'entry': float(self.position.entry_price) if self.is_open else None,\\n            'price': float(self.price), **fields\\n        }, sort_keys=True))\\n\"}")
report = {'scope': 'Actual frozen source AST/compile and isolated method stubs; no trading simulation or MTM', 'checks': []}
def check(name, condition):
    report['checks'].append({'name': name, 'pass': bool(condition)})
    assert condition, name
def methods(source):
    tree = ast.parse(source)
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef))
    return cls, {m.name:m for m in cls.body if isinstance(m, ast.FunctionDef)}
base_cls, base_methods = methods(sources['PortCompareBtc4h'])
changed = {'on_open_position', 'update_position', 'on_close_position', 'terminate'}
for name, source in sources.items():
    compile(source, name, 'exec')
    if name == 'PortCompareBtc4h':
        continue
    cls, mm = methods(source)
    check(name+'_compile', True)
    for method, node in base_methods.items():
        if method not in changed:
            check(name+'_unchanged_'+method, ast.dump(node) == ast.dump(mm[method]))
    check(name+'_long_branch', ast.dump(ast.Module(body=base_methods['update_position'].body[1:], type_ignores=[])) == ast.dump(ast.Module(body=mm['update_position'].body[1:], type_ignores=[])))
    check(name+'_debug_comment', 'runner must use debug=true' in source and 'jh.debug logs even with strategy debug_mode disabled' not in source)
    # Execute only actual management/helper methods, with deterministic public-state
    # stubs. These test boundary semantics, not fill realism or economic outcomes.
    selected = [copy.deepcopy(mm[m]) for m in ('update_position','_payoff_postfill_bar','_payoff_log')]
    stub_cls = ast.ClassDef(name='Stub', bases=[], keywords=[], body=selected, decorator_list=[])
    mod = ast.fix_missing_locations(ast.Module(body=[stub_cls],type_ignores=[]))
    logs=[]
    ta = SimpleNamespace(ema=lambda *a, **k: 110.0, rsi=lambda *a, **k: 50.0)
    env={'math':math,'json':json,'np':np,'ta':ta,'jh':SimpleNamespace(debug=logs.append)}
    exec(compile(mod,name+'_methods','exec'),env)
    Stub=env['Stub']
    def make(price=100, bar_open=14400000, opened=1000000, time=28800000, old=120):
        s=Stub()
        s.is_short=True; s.is_open=True; s.price=float(price); s.time=time
        s.closed_candle_open_time=bar_open
        s.vars={'opened_time':opened,'plan':{'target_distance':10.0},'payoff_be_latched':False}
        s.position=SimpleNamespace(entry_price=100.0,qty=-2.0)
        s.average_stop_loss=float(old)
        s.stop_loss=('unchanged',old); s.take_profit=(2.0,90.0)
        s.signal_candles=np.array([[float(bar_open),100,price,120,80,10]],dtype=float)
        s.liquidations=0
        def liquidate():s.liquidations+=1
        s.liquidate=liquidate
        return s
    def stable(s):
        return s.position.qty == -2 and s.take_profit == (2.0,90.0)
    s=make(price=90,bar_open=0)
    s.update_position()
    check(name+'_partial_no_new_rule',s.stop_loss[0]=='unchanged' and not s.vars['payoff_be_latched'] and s.liquidations==0)
    s=make(price=90,bar_open=0,time=72*3600000+1000000)
    s.update_position()
    check(name+'_timeout_outside_gate',s.liquidations==1)
    s=make();s.signal_candles=np.array([[0,100,100,120,80,10]],float);s.update_position()
    check(name+'_mismatched_closed_history',s.stop_loss[0]=='unchanged' and s.liquidations==0)
    s=make(opened=14400000)
    check(name+'_exact_fill_open_full_bar',s._payoff_postfill_bar())
    if name.endswith('101'):
        for ema, expected in [(130,False),(110,True),(90,False),(float('nan'),False)]:
            ta.ema=lambda *a, _ema=ema, **k:_ema
            s=make();s.update_position()
            check(name+'_ema_'+str(ema), (s.stop_loss==(2,110.0)) if expected else s.stop_loss[0]=='unchanged')
            check(name+'_ema_qty_tp_'+str(ema),stable(s))
        ta.ema=lambda *a,**k:110.0
        s=make(old=105);s.update_position()
        check(name+'_never_widen_existing_tighter',s.stop_loss==('unchanged',105))
    elif name.endswith('102'):
        s=make(price=95);s.update_position()
        be=100*(1-.00045)/(1+.00045)
        check(name+'_half_target_latch',s.vars['payoff_be_latched'] and s.stop_loss==(2,be))
        check(name+'_nominal_be_formula',abs(100-be-.00045*(100+be))<1e-12)
        check(name+'_be_qty_tp',stable(s))
        s.average_stop_loss=be;s.price=98;s.update_position()
        check(name+'_be_latch_retained_no_widen',s.vars['payoff_be_latched'] and s.stop_loss==(2,be))
        s=make(price=95,old=98);s.update_position()
        check(name+'_never_widen_tighter_stop',s.vars['payoff_be_latched'] and s.stop_loss==('unchanged',98))
        s=make(price=95.001);s.update_position()
        check(name+'_before_half_no_latch',not s.vars['payoff_be_latched'] and s.stop_loss[0]=='unchanged')
    else:
        for rsi, expected in [(49.999,0),(50.0,1),(80.0,1),(float('nan'),0)]:
            ta.rsi=lambda *a,_rsi=rsi,**k:_rsi
            s=make();s.update_position()
            check(name+'_rsi_'+str(rsi),s.liquidations==expected)
            check(name+'_rsi_qty_tp_'+str(rsi),stable(s))
    check(name+'_log_json',all(json.loads(t.split('BTC_PAYOFF ',1)[1]) for t in logs))
report['total_checks']=len(report['checks'])
report['passed']=sum(c['pass'] for c in report['checks'])
Path('output/source_stub_qa.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'}))

```
