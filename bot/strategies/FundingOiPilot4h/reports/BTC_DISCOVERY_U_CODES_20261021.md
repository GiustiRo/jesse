# U — complete read sources and closures before implementation

Status: protocol/feasibility only. No new strategy classes, jobs, drafts, economics or observed candles. DOCS.md and bot/AGENTS.md were read from the authorized environment during T preparation; strategy/report reads exclusively MCP. This file preserves exact complete texts read, not fabricated runtime/indicator code. R16/R11/R10 remain unchanged.

## BTCExploreR805
SHA256 246150464d5636e3a107ba8ad69eb63d3ca98de4d1410d75e12044ef0d36e08a

```python
import math
import json
import jesse.helpers as jh
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

# User-approved research limits; risk is not an optimization parameter.
TRADE_RISK = 0.01
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.
SLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.


class BTCExploreR805(Strategy):
    """Frozen R8 X805 alternative supplement; original branches retained.

    Shared risk and margin reservations; exploratory research, not approved live.
    SPY uses a session-filtered SPX CFD proxy; holidays and native parity remain
    unverified. Parameter-neighbour variants are sensitivity controls, not winners.
    """

    def hyperparameters(self) -> list:
        return [
            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},
            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},
            {'name': 'ema_slow', 'type': int, 'min': 80, 'max': 140, 'default': 80},
            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},
            {'name': 'stop_atr', 'type': float, 'min': 1.6, 'max': 3.0, 'default': 2.0},
            {'name': 'trail_atr', 'type': float, 'min': 3.0, 'max': 5.0, 'default': 4.2},
            {'name': 'be_r', 'type': float, 'min': 1.75, 'max': 3.0, 'default': 2.25},
        ]

    def trading_hours(self):
        if self.symbol == 'SPY-USDT':
            # The fixed UTC whole-bar intersection excludes the US index daily
            # break in both DST regimes. This is an intentional common window,
            # not an assertion that the source's full session ends at 20:00 UTC.
            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}
        return None

    @property
    @cached
    def signal_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    def _entry_window(self) -> bool:
        if self.symbol != 'SPY-USDT':
            return True
        # A closed bar opening at 12:00 triggers at 16:00. Its order expires
        # at 20:00, before the excluded 20:00-24:00 bucket. A 16:00-open bar
        # must not arm a new order at 20:00. Pending orders still cancel then.
        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}
        return self.is_trading_hours and utils.is_in_trading_hours(
            self.closed_candle_open_time, window)

    def _ledger(self) -> dict:
        return self.shared_vars.setdefault('phase2_reservations', {})

    def _key(self) -> str:
        return self.exchange + ':' + self.symbol

    def _capital(self) -> float:
        # Floating gains do not enlarge the risk budget; floating losses reduce it.
        return max(0.0, min(float(self.balance), float(self.portfolio_value)))

    def _committed(self) -> tuple:
        risk, notional = 0.0, 0.0
        ledger = self._ledger()
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            strategy = route.strategy
            if strategy.is_open:
                qty = abs(float(strategy.position.qty))
                entry = float(strategy.position.entry_price)
                # Risk is measured from the current mark, so protected floating PnL
                # is not silently treated as free capacity for another trade.
                value = abs(float(strategy.position.value))
                mark = value / qty if qty else entry
                stop = float(strategy.average_stop_loss)
                distance = max(0.0, mark - stop) if strategy.is_long else max(0.0, stop - mark)
                risk += qty * (distance + mark * (self.fee_rate + SLIPPAGE_RESERVE))
                notional += value
            else:
                reservation = ledger.get(route.exchange + ':' + route.symbol)
                if reservation:
                    # Includes not-yet-filled STOP/LIMIT entries, not only open positions.
                    risk += reservation['risk']
                    notional += reservation['notional']
        return risk, notional

    def _volatility_share(self) -> float:
        """Reserve a common gross-exposure budget using inverse ATR fractions.

        All configured assets receive an ex-ante share, even while their signal
        is idle. This prevents the first route from consuming all shared margin.
        It is a capital-efficiency tradeoff to test, not an optimal allocation.
        """
        weights = {}
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            c = utils.filter_candles_by_hours(route.strategy.candles, route.strategy.trading_hours())
            if len(c) < int(self.hp['ema_slow']) + 20:
                return 0.0
            atr = float(ta.atr(c))
            price = float(c[-1, 2])
            if not math.isfinite(atr) or atr <= 0 or price <= 0:
                return 0.0
            # Stops use a common ATR multiple. Equal risk therefore needs
            # notional proportional to price/ATR before gross-leverage scaling.
            weights[route.symbol] = price / atr
        return weights.get(self.symbol, 0.0) / sum(weights.values()) if weights else 0.0

    def _plan(self) -> bool:
        if self.symbol not in ('BTC-USDT', 'PAXG-USDT', 'SPY-USDT') or not self._entry_window():
            return False
        c = self.signal_candles
        n = int(self.hp['donchian_len'])
        slow_n = int(self.hp['ema_slow'])
        if len(c) < max(slow_n + 20, n):
            return False
        fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))
        slow = ta.ema(c, period=slow_n, sequential=True)
        atr = float(ta.atr(c))
        adx = float(ta.adx(c))
        rsi = float(ta.rsi(c))
        # The closed bar has broken the PRIOR channel. A passive LIMIT at that
        # boundary can fill only on a future retest within one 4h order lifetime.
        entry = float(np.max(c[-n-1:-1, 3]))
        if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):
            return False
        if not (atr > 0 and entry < self.price <= entry + atr and self.price > slow[-1]
                and fast > slow[-1] > slow[-5] and adx >= self.hp['adx_min']
                and 52 <= rsi <= 76 and self.high - self.low <= 3 * atr):
            return False
        distance = float(self.hp['stop_atr']) * atr
        if not 0 < distance < entry:
            return False
        capital = self._capital()
        committed_risk, committed_notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - committed_risk))
        # Fees at both planned entry and stop, plus an explicit adverse-fill reserve.
        unit_risk = distance + self.fee_rate * (entry + entry - distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - committed_notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        # Historical research precision only. Native symbol lot/min-notional
        # constraints must be verified before any live use.
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        self._record_capacity('long', capital, budget, unit_risk, entry,
                              room, margin_room, qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {
            'qty': qty, 'entry': entry, 'distance': distance,
            'risk': qty * unit_risk, 'notional': qty * entry,
        }
        return True

    def _signal(self) -> int:
        # Compute exactly one plan per bar, with long priority. Checking
        # should_short after go_long must never overwrite a queued long plan.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            if self._plan():
                signal = 1
            elif self._short_plan():
                signal = -1
            else:
                event = self.vars.get('explore_event')
                signal = (-1 if event and self._explore_size(event) else 0)
            self.vars['signal_value'] = signal
        return self.vars['signal_value']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], plan['entry']

    def _short_plan(self) -> bool:
        """Test selloff continuation instead of buying an oversold dip.

        A rising slow regime can still suffer a fast liquidation leg. This
        exploratory hypothesis came from the failed long mean-reversion sleeve;
        it is development evidence, not an independent validation.
        """
        if self.symbol != 'BTC-USDT' or not self._entry_window():
            return False
        c = self.signal_candles
        if len(c) < 140:
            return False
        macro = ta.ema(c, period=120, sequential=True)
        fast = float(ta.ema(c, period=20))
        atr = float(ta.atr(c))
        quick_rsi = float(ta.rsi(c, period=3))
        if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, quick_rsi)):
            return False
        if not (atr > 0 and macro[-1] > macro[-10]
                and self.price > macro[-1] - atr and quick_rsi <= 20):
            return False
        entry = min(float(c[-1, 4]), self.price - 0.25 * atr)
        distance = fast - entry
        if not (atr <= distance <= 3 * atr and distance >= 6 * self.fee_rate * entry):
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry + distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        qty = min(budget / unit_risk, room / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        self._record_capacity('short', capital, budget, unit_risk, entry,
                              room, max(0.0, float(self.leveraged_available_margin) * 0.90), qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry,
                             'target_distance': 1.5 * atr}
        return True

    def go_short(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.
        # Jesse processes cancellation before evaluating the next route.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:

        plan = self.vars['plan']
        self.vars['explore_kind'] = plan.get('kind')
        if self.vars['explore_kind']:
            # Geometry is frozen at signal; protection is relative to actual fill.
            entry = float(self.position.entry_price)
            distance = plan['distance']
            self.vars['initial_distance'] = distance
            self.vars['opened_time'] = int(self.time)
            self.vars['explore_deadline'] = int(self.time) + plan['hold_hours'] * 3600000
            qty = abs(float(self.position.qty))
            if self.is_long:
                self.stop_loss = qty, entry - distance
                self.take_profit = qty, entry + plan['target_distance']
            else:
                self.stop_loss = qty, entry + distance
                self.take_profit = qty, entry - plan['target_distance']
            self._ledger().pop(self._key(), None)
            audit = self.vars.setdefault('explore_audit', {})
            audit['fills'] = audit.get('fills', 0) + 1
            jh.debug('BTC_EXPLORE_FILL ' + json.dumps({
                'recipe': self.vars['explore_kind'], 'time': int(self.time),
                'side': 'long' if self.is_long else 'short',
                'entry': entry, 'qty': qty, 'distance': distance,
                'target_distance': plan['target_distance'],
                'deadline': self.vars['explore_deadline']}, sort_keys=True))
            return
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        self.vars['initial_distance'] = distance
        # An intrabar fill must not inherit highs/closes from before its entry.
        self.vars['best_close'] = entry
        if self.is_short:
            self.vars['opened_time'] = int(self.time)
            self.stop_loss = abs(self.position.qty), entry + distance
            self.take_profit = abs(self.position.qty), entry - self.vars['plan']['target_distance']
        else:
            self.stop_loss = abs(self.position.qty), entry - distance
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:

        if self.vars.get('explore_kind'):
            # Only the first closed 4h decision at/after the fill-based deadline.
            if int(self.time) >= self.vars['explore_deadline']:
                self.liquidate()
            return
        if self.is_short:
            if self.time - self.vars['opened_time'] >= 72 * 60 * 60 * 1000:
                self.liquidate()
            return
        history = self.signal_candles
        atr = float(ta.atr(history))
        if not math.isfinite(atr) or atr <= 0:
            return
        entry = float(self.position.entry_price)
        distance = self.vars['initial_distance']
        self.vars['best_close'] = max(self.vars['best_close'], float(history[-1, 2]))
        best_r = (self.vars['best_close'] - entry) / distance
        mult = float(self.hp['trail_atr'])
        # Inherited late-trend tightening; retained as a controlled baseline choice.
        if best_r >= 8:
            mult *= 0.62
        elif best_r >= 5:
            mult *= 0.78
        stop = self.vars['best_close'] - mult * atr
        if best_r >= float(self.hp['be_r']):
            stop = max(stop, entry * (1 + 2.5 * self.fee_rate))
        if self.average_stop_loss < stop < self.price:
            self.stop_loss = abs(self.position.qty), stop

    def on_close_position(self, order, closed_trade) -> None:
        if self.vars.get('explore_kind'):
            audit = self.vars.setdefault('explore_audit', {})
            audit['closes'] = audit.get('closes', 0) + 1
        self.vars['explore_kind'] = None
        self._ledger().pop(self._key(), None)

    def _record_capacity(self, side, capital, budget, unit_risk, entry,
                         room, margin_room, raw_qty, step) -> None:
        """Observe existing sizing only; never gates signals or changes quantities.

        Counts plans reaching sizing while flat and without a pending entry.
        It does not infer trades that would have filled or signals while occupied.
        Quantity tolerances below classify numerical ties, not trading thresholds.
        """
        audit = self.vars.setdefault('portfolio_capacity_audit', {})
        row = audit.setdefault(side, {'eligible_sizing_attempts': 0,
                                     'risk_budget_limited': 0,
                                     'notional_or_weight_limited': 0,
                                     'margin_limited': 0,
                                     'sized_below_trade_target': 0,
                                     'capacity_zero': 0,
                                     'zero_after_lot_rounding': 0})
        row['eligible_sizing_attempts'] += 1
        target_qty = capital * TRADE_RISK / unit_risk
        tolerance = max(1e-8, abs(target_qty) * 1e-10)
        row['risk_budget_limited'] += int(budget / unit_risk + tolerance < target_qty)
        row['notional_or_weight_limited'] += int(room / entry + tolerance < target_qty)
        row['margin_limited'] += int(margin_room / entry + tolerance < target_qty)
        row['sized_below_trade_target'] += int(raw_qty + tolerance < target_qty)
        row['capacity_zero'] += int(raw_qty <= 0 < target_qty)
        row['zero_after_lot_rounding'] += int(math.floor(raw_qty / step) * step <= 0 < raw_qty)

    def terminate(self) -> None:
        jh.debug('BTC_R8_M1 ' + json.dumps(self.vars.get('research_m1_audit', {}), sort_keys=True))
        jh.debug('BTC_EXPLORE ' + json.dumps({'recipe': 'X805',
            'counts': self.vars.get('explore_audit', {})}, sort_keys=True))
        # One compact persisted record per route, after engine final liquidation.
        # The runner requires debug_mode=True to persist these diagnostic logs.
        jh.debug('PORT_CAPACITY ' + json.dumps({
            'symbol': self.symbol, 'strategy': self.__class__.__name__,
            'trade_risk': TRADE_RISK, 'portfolio_risk': PORTFOLIO_RISK,
            'notional_cap': NOTIONAL_CAP,
            'counts': self.vars.get('portfolio_capacity_audit', {})
        }, sort_keys=True))

    def _explore_window(self, n):
        """Require the exact closed 4h clock; invalid input cannot create an event."""
        c = self.signal_candles
        if len(c) < n:
            return None
        w = c[-n:]
        if (not np.all(np.isfinite(w))
                or int(w[-1, 0]) != int(self.closed_candle_open_time)
                or w[-1, 0] + 14400000 > self.time
                or not np.all(np.diff(w[:, 0]) == 14400000)
                or not np.all(w[:, 1:] > 0)
                or not np.all(w[:, 3] >= w[:, 4])):
            return None
        return c

    def _explore_size(self, event):
        """Use the original budget, reservations, fees and volatility quota."""
        side = event['side']
        entry, distance = float(self.price), float(event['distance'])
        if not (math.isfinite(entry) and math.isfinite(distance)
                and 0 < distance < entry):
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        stop = entry - distance if side == 'long' else entry + distance
        unit_risk = distance + self.fee_rate * (entry + stop) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        step = 0.001
        self._record_capacity(side, capital, budget, unit_risk, entry,
                              room, margin_room, qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = dict(event, qty=qty, entry=entry,
                                risk=qty * unit_risk, notional=qty * entry)
        return True

    def before(self) -> None:
        # Event state is price-only and advances even while occupied or pending.
        if self.vars.get('explore_clock') == int(self.closed_candle_open_time):
            return
        self.vars['explore_event'] = None
        self.vars['explore_clock'] = int(self.closed_candle_open_time)
        c = self._explore_window(14)
        if c is None:
            self.vars['explore_previous'] = False
            return
        s, t = c[-2], c[-1]
        setup = bool(self._research_setup(c))
        previous = self.vars.get('explore_previous', False)
        self.vars['explore_previous'] = setup
        if not setup or previous:
            return
        atr = float(ta.atr(c))
        if not (math.isfinite(atr) and atr > 0):
            return
        distance = float(max(s[3], t[3]) + 0.25 * atr - t[2])
        if not atr <= distance <= 3 * atr:
            return
        self.vars['explore_event'] = {'side': 'short', 'kind': 'X805',
            'distance': distance, 'target_distance': 2 * distance, 'hold_hours': 48}
        audit = self.vars.setdefault('explore_audit', {})
        audit['events'] = audit.get('events', 0) + 1
        audit['events_occupied'] = audit.get('events_occupied', 0) + int(self.is_open)

    def _research_setup(self, c):
        s, t = c[-2], c[-1]
        if not (s[2] > c[-14, 2] and t[2] < t[1]):
            return False
        minute = self.get_candles(self.exchange, self.symbol, '1m')
        valid, reason, fraction = self._volume_clock_setup(
            minute, int(t[0]), int(t[0]) + 14400000, float(t[2]))
        audit = self.vars.setdefault('research_m1_audit', {})
        audit[reason] = audit.get(reason, 0) + 1
        if fraction is not None:
            # Aggregate diagnostics only; never used to accept or reject a setup.
            audit['partition_count'] = audit.get('partition_count', 0) + 1
            audit['fraction_sum'] = audit.get('fraction_sum', 0.0) + fraction
            audit['fraction_min'] = min(audit.get('fraction_min', fraction), fraction)
            audit['fraction_max'] = max(audit.get('fraction_max', fraction), fraction)
        return valid

    @staticmethod
    def _volume_clock_setup(minute, start, end, close):
        # The boundary minute belongs wholly to group one. Its OHLC is not split.
        if minute.ndim != 2 or minute.shape[1] < 6:
            return False, 'missing_shape', None
        rows = minute[(minute[:, 0] >= start) & (minute[:, 0] < end)]
        if (len(rows) != 240 or int(rows[0, 0]) != start
                or int(rows[-1, 0]) + 60000 != end
                or not np.all(np.diff(rows[:, 0]) == 60000)):
            return False, 'missing_clock', None
        if (not np.all(np.isfinite(rows[:, :6]))
                or not np.all(rows[:, 1:5] > 0) or not np.all(rows[:, 5] >= 0)
                or not np.all(rows[:, 4] <= np.minimum(rows[:, 1], rows[:, 2]))
                or not np.all(np.maximum(rows[:, 1], rows[:, 2]) <= rows[:, 3])):
            return False, 'corrupt', None
        if float(rows[-1, 2]) != close:
            return False, 'close_mismatch', None
        volume = rows[:, 5]
        total = float(np.sum(volume))
        if total <= 0:
            return False, 'zero_volume', None
        boundary = int(np.searchsorted(np.cumsum(volume), 0.5 * total, side='left'))
        first, second = rows[:boundary + 1], rows[boundary + 1:]
        v1, v2 = float(np.sum(first[:, 5])), float(np.sum(second[:, 5]))
        if len(first) == 0 or len(second) == 0 or v1 <= 0 or v2 <= 0:
            return False, 'empty_partition', None
        a1 = float(np.sum(np.mean(first[:, [3, 4, 2]], axis=1) * first[:, 5]) / v1)
        a2 = float(np.sum(np.mean(second[:, [3, 4, 2]], axis=1) * second[:, 5]) / v2)
        return bool(a2 < a1 and close < np.min(first[:, 4])), 'valid', v1 / total
```

## BtcResearchR16LegacyBase1m
SHA256 56f5d56aa004f24db450797cee8b11febd84a5804a2a5d70bcd2cd4ed73e6542

```python
import math
import numpy as np
import jesse.indicators as ta

from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR

# Frozen legacy recipe values, not optimizer ranges. The 10bp reserve sizes
# conservatively; it is never charged as cash or simulated execution friction.
HP = dict(donchian_len=26, ema_fast=20, ema_slow=80, adx_min=26,
          stop_atr=2.0, trail_atr=4.2, be_r=2.25)
RESERVE = .001
LOT = .001


def legacy_history(candles, now):
    """Keep exposed closed history; cross-route seed parity needs framework audit."""
    rows = candles[candles[:, 0]+BAR <= now]
    if len(rows) < 14 or rows[-1, 0] != now-BAR:
        return None
    if (not np.all(np.diff(rows[:, 0]) == BAR)
            or not np.all(np.isfinite(rows[:, :5]))
            or not np.all(rows[:, 1:5] > 0)
            or np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2]))
            or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2]))):
        return None
    return rows


def legacy_long(c):
    if len(c) < 100:
        return None
    price = float(c[-1, 2])
    fast = float(ta.ema(c, period=20))
    slow = ta.ema(c, period=80, sequential=True)
    atr, adx, rsi = float(ta.atr(c)), float(ta.adx(c)), float(ta.rsi(c))
    entry = float(np.max(c[-27:-1, 3]))
    if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):
        return None
    if not (atr > 0 and entry < price <= entry+atr and price > slow[-1]
            and fast > slow[-1] > slow[-5] and adx >= 26
            and 52 <= rsi <= 76 and c[-1, 3]-c[-1, 4] <= 3*atr):
        return None
    distance = 2*atr
    if not 0 < distance < entry:
        return None
    return dict(origin="LONG_RUNNER", direction=1, entry=entry,
                distance=distance, target_distance=None, hold_hours=None,
                order_kind="LIMIT")


def legacy_short(c):
    if len(c) < 140:
        return None
    price = float(c[-1, 2])
    macro = ta.ema(c, period=120, sequential=True)
    fast, atr, rsi = float(ta.ema(c, period=20)), float(ta.atr(c)), float(ta.rsi(c, period=3))
    if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, rsi)):
        return None
    if not (atr > 0 and macro[-1] > macro[-10] and price > macro[-1]-atr and rsi <= 20):
        return None
    entry = min(float(c[-1, 4]), price-.25*atr)
    distance = fast-entry
    if not (atr <= distance <= 3*atr and distance >= 6*.00045*entry):
        return None
    return dict(origin="CORE_SHORT", direction=-1, entry=entry,
                distance=distance, target_distance=1.5*atr, hold_hours=72,
                order_kind="STOP")


def legacy_supplement(c, mode, previous):
    """Consume setup before ATR/geometry/account tests, as in each frozen parent."""
    assert mode in ("K1001", "N204")
    w = c[-14:]
    if (len(w) < 14 or not np.all(np.isfinite(w))
            or not np.all(w[:, 1:] > 0) or not np.all(w[:, 3] >= w[:, 4])):
        return None, False
    s, t, window = c[-2], c[-1], c[-13:-1]
    spans = window[:, 3]-window[:, 4]
    q = np.divide(window[:, 5]*(2*window[:, 2]-window[:, 3]-window[:, 4]),
                  spans, out=np.zeros(12), where=spans > 0)
    cohort = window[q > 0]
    vwap = (float(np.sum(cohort[:, 5]*np.mean(cohort[:, [3, 4, 2]], axis=1))
                  / np.sum(cohort[:, 5])) if len(cohort) else float("nan"))
    setup = bool(s[2] > c[-14, 2] and np.sum(q) < 0
                 and s[2] >= vwap and t[2] < t[1] and t[2] < vwap)
    if mode == "K1001" and setup:
        changes = c[-13:-1, 2]-c[-14:-2, 2]
        path = float(np.sum(np.abs(changes)))
        efficiency = float(s[2]-c[-14, 2])/path if path > 0 else float("nan")
        setup = bool(path > 0 and 0 < efficiency <= 1/3)
    if not setup or previous:
        return None, setup
    atr = float(ta.atr(c))
    if not math.isfinite(atr) or atr <= 0:
        return None, setup
    distance = float(max(s[3], t[3])+.25*atr-t[2])
    if not atr <= distance <= 3*atr:
        return None, setup
    entry = float(min(s[4], t[4])) if mode == "K1001" else float(t[2])
    if mode == "K1001" and not (math.isfinite(entry) and entry > 2*distance and entry < t[2]):
        return None, setup
    if not (math.isfinite(entry) and math.isfinite(distance) and 0 < distance < entry):
        return None, setup
    return dict(origin="SUPPLEMENT", direction=-1, entry=entry,
                distance=distance, target_distance=2*distance, hold_hours=48,
                order_kind="STOP" if mode == "K1001" else "MARKET",
                anchor=vwap), setup


def legacy_plan(event, capital, margin, leverage, fee):
    """BTC100%; preserve reserve/lot, with the common 90%-margin fee buffer."""
    entry, distance, direction = event["entry"], event["distance"], event["direction"]
    stop = entry-direction*distance
    if (direction not in (-1, 1)
            or not all(math.isfinite(v) and v > 0 for v in
                       (entry, distance, stop, capital, margin, leverage))
            or not math.isfinite(fee) or fee < 0):
        return None
    unit = distance+fee*(entry+stop)+RESERVE*entry
    budget = .02*capital
    risk_qty = budget/unit
    gross_qty = 4.4*capital/entry  # Legacy ceiling; 3x margin prevents 4.4x exposure.
    margin_qty = .90*margin*leverage/(entry*(1+fee*leverage))
    qty = math.floor(min(risk_qty, gross_qty, margin_qty)/LOT)*LOT
    if qty <= 0:
        return None
    assert qty*unit <= budget+1e-6
    return dict(event, qty=qty, risk_budget=budget, planned_loss=qty*unit,
                planned_stop_fees=qty*(distance+fee*(entry+stop)),
                margin_limited=margin_qty < risk_qty,
                gross_limited=gross_qty < risk_qty,
                reserve=RESERVE)


class BtcResearchR16LegacyBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def _ledger(self):
        return self.vars.setdefault("legacy_ledger", {
            name: dict(fills=0, closes=0, net=0.0)
            for name in ("LONG_RUNNER", "CORE_SHORT", "SUPPLEMENT")})

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("K1001", "N204")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        # Advance the price machine once, independently of occupancy. Actual
        # framework cancellation may re-enter should_* in this same4h cycle.
        self.vars["decision_at"] = now
        rows = legacy_history(self.get_candles(self.exchange, self.symbol, "4h"), now)
        self.vars["legacy_rows"] = rows
        if rows is None:
            self.vars["previous_setup"] = False
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        self.vars["history_min"] = min(self.vars.get("history_min", len(rows)), len(rows))
        self.vars["history_max"] = max(self.vars.get("history_max", len(rows)), len(rows))
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        event, setup = legacy_supplement(rows, self.MODE, self.vars.get("previous_setup", False))
        self.vars["previous_setup"] = setup
        self.vars["supplement_event"] = event
        self.vars["supplement_events"] = self.vars.get("supplement_events", 0)+int(event is not None)
        if self.is_open or self.entry_orders:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1

    def _prepare_entry(self):
        """Memoize after broker cancellation releases margin; preserve one plan."""
        now = int(self.time)
        if (now % BAR or self.vars.get("decision_at") != now
                or self.is_open or self.entry_orders
                or self.vars.get("last_exit_at") == now
                or not self.START < now < self.FINISH):
            return 0
        if self.vars.get("prepared_at") == now:
            return self.vars.get("direction", 0)
        self.vars["prepared_at"] = now
        rows = self.vars.get("legacy_rows")
        if rows is None:
            return 0
        # Priority includes account eligibility: if a higher recipe cannot size,
        # the next original recipe is considered, exactly as the frozen parents.
        for candidate in (legacy_long(rows), legacy_short(rows),
                          self.vars.get("supplement_event")):
            if candidate is None:
                continue
            plan = legacy_plan(candidate, max(0.0, float(self.balance)),
                               float(self.available_margin), float(self.leverage),
                               float(self.fee_rate))
            if plan is not None:
                self.vars["plan"] = dict(plan, signal_at=now, expiry=now+BAR)
                self.vars["direction"] = plan["direction"]
                self.vars["signals"] = self.vars.get("signals", 0)+1
                return plan["direction"]
        return 0

    def should_long(self):
        return self._prepare_entry() == 1

    def should_short(self):
        return self._prepare_entry() == -1

    def _submit(self, direction):
        plan = self.vars["plan"]
        assert self.vars.get("submitted_at") != int(self.time), "P_DUPLICATE_SUBMISSION"
        assert self.vars.get("direction") == direction
        assert int(self.time) == plan["signal_at"] and not self.is_open and not self.entry_orders
        self.vars["submitted_at"] = int(self.time)
        self.vars["pending_plan"] = dict(plan)
        if direction == 1:
            self.buy = plan["qty"], plan["entry"]
        else:
            self.sell = plan["qty"], plan["entry"]

    def go_long(self):
        self._submit(1)

    def go_short(self):
        self._submit(-1)

    def should_cancel_entry(self):
        plan = self.vars.get("pending_plan")
        assert plan is not None, "P_PENDING_WITHOUT_PLAN"
        due = int(self.time) % BAR == 0 and int(self.time) >= plan["expiry"]
        if due:
            self.vars["pending_plan"] = None
            self.vars["cancellations"] = self.vars.get("cancellations", 0)+1
        return due

    def on_open_position(self, order):
        plan = self.vars["pending_plan"]
        assert plan is not None and self.vars.get("position_plan") is None
        now = int(self.time)
        assert plan["signal_at"] <= now <= plan["expiry"], "P_FILL_OUTSIDE_ORDER_LIFE"
        assert plan["signal_at"] <= int(self.position.opened_at) <= plan["expiry"]
        direction = 1 if self.is_long else -1
        assert direction == plan["direction"]
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        stop = entry-direction*plan["distance"]
        target = (entry+direction*plan["target_distance"]
                  if plan["target_distance"] is not None else None)
        loss = qty*(plan["distance"]+self.fee_rate*(entry+stop)+RESERVE*entry)
        assert math.isfinite(loss) and stop > 0 and (target is None or target > 0)
        assert loss <= plan["risk_budget"]+1e-6, "P_ACTUAL_FILL_RISK"
        assert abs(qty-plan["qty"]) < 1e-8, "P_UNEXPECTED_FILL_QUANTITY"
        # Frozen geometry is placed relative to actual fill, never order price.
        self.stop_loss = qty, stop
        if target is not None:
            self.take_profit = qty, target
        self.vars["position_plan"] = dict(plan, actual_entry=entry, actual_loss=loss,
                                          filled_at=int(self.position.opened_at))
        self.vars["pending_plan"] = None
        self.vars["best_close"] = entry
        self._ledger()[plan["origin"]]["fills"] += 1
        self.vars["entries"] = self.vars.get("entries", 0)+1
        self._observe("open")
        self._log("R16_LEGACY_OPEN", dict(mode=self.MODE, origin=plan["origin"], time=now,
            opened_at=int(self.position.opened_at), signal_at=plan["signal_at"],
            expiry=plan["expiry"], order_kind=plan["order_kind"],
            requested_entry=plan["entry"], actual_entry=entry, qty=qty,
            distance=plan["distance"], stop=stop, target=target,
            risk_budget=plan["risk_budget"], actual_loss=loss,
            planned_loss=plan["planned_loss"], planned_stop_fees=plan["planned_stop_fees"],
            margin_limited=plan["margin_limited"], reserve=RESERVE))

    def update_position(self):
        now = int(self.time)
        if now % BAR:
            return
        plan = self.vars["position_plan"]
        opened = plan["filled_at"]
        if plan["hold_hours"] is not None:
            if now-opened >= plan["hold_hours"]*3600000:
                self.liquidate()
            return
        # A close completed before the fill cannot improve its trailing stop.
        if now <= opened:
            return
        rows = self.vars.get("legacy_rows")
        if rows is None or self.vars.get("decision_at") != now:
            return
        atr = float(ta.atr(rows))
        if not math.isfinite(atr) or atr <= 0:
            return
        entry = plan["actual_entry"]
        self.vars["best_close"] = max(self.vars["best_close"], float(rows[-1, 2]))
        best_r = (self.vars["best_close"]-entry)/plan["distance"]
        mult = 4.2
        if best_r >= 8:
            mult *= .62
        elif best_r >= 5:
            mult *= .78
        stop = self.vars["best_close"]-mult*atr
        if best_r >= 2.25:
            stop = max(stop, entry*(1+2.5*self.fee_rate))
        if self.average_stop_loss < stop < self.price:
            self.stop_loss = abs(float(self.position.qty)), stop

    def on_close_position(self, order, closed_trade):
        plan = self.vars["position_plan"]
        row = self._ledger()[plan["origin"]]
        pnl = float(closed_trade.pnl)
        assert math.isfinite(pnl)
        row["closes"] += 1
        row["net"] += pnl
        self.vars["position_plan"] = None
        self.vars["pending_plan"] = None
        self._log("R16_LEGACY_CLOSE", dict(time=int(self.time), origin=plan["origin"], net=pnl))
        # R11 can emit FINAL here; source totals must already include this close.
        super().on_close_position(order, closed_trade)

    def _emit(self, stage):
        super()._emit(stage)
        rows = self._ledger()
        self._log("R16_LEGACY_STATS", dict(stage=stage, mode=self.MODE, sources=rows,
            fills=sum(r["fills"] for r in rows.values()),
            closes=sum(r["closes"] for r in rows.values()),
            net=sum(r["net"] for r in rows.values()),
            supplement_events=self.vars.get("supplement_events", 0),
            cancellations=self.vars.get("cancellations", 0),
            history_min=self.vars.get("history_min"), history_max=self.vars.get("history_max")))
```

## BtcResearchR11Base1m
SHA256 be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87

```python
import json
import math
from datetime import datetime, timezone

import numpy as np
from jesse.strategies import Strategy
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def cusum_step(rows, accumulators):
    """Transfer the R40 design:60 past log returns, drift0.25, boundary4."""
    returns = np.diff(np.log(rows[-62:, 2]))
    sigma = float(np.std(returns[:-1], ddof=1))
    if not math.isfinite(sigma) or sigma <= 0:
        return 0, (0.0, 0.0)
    z = float((returns[-1] - np.mean(returns[:-1])) / sigma)
    if not math.isfinite(z):
        return 0, (0.0, 0.0)
    up = max(0.0, accumulators[0] + z - 0.25)
    down = max(0.0, accumulators[1] - z - 0.25)
    if up >= 4 or down >= 4:
        direction = 0 if up >= 4 and down >= 4 else 1 if up >= 4 else -1
        return direction, (0.0, 0.0)
    return 0, (up, down)


def absorption_signal(rows):
    """Large volume but small body, followed by escape of that closed bar."""
    window, setup, confirmation = rows[-26:-2], rows[-2], rows[-1]
    if not np.all(np.isfinite(rows[-26:, 5])) or np.any(rows[-26:, 5] < 0):
        return 0
    average_volume = float(np.mean(window[:, 5]))
    prior_atr = atr14(window)
    if not math.isfinite(average_volume) or average_volume <= 0 or prior_atr is None:
        return 0
    if setup[5] < 2 * average_volume or abs(setup[2] - setup[1]) > 0.25 * prior_atr:
        return 0
    if confirmation[2] > setup[3]:
        return 1
    if confirmation[2] < setup[4]:
        return -1
    return 0


def month_name(timestamp):
    return datetime.fromtimestamp(timestamp / 1000, timezone.utc).strftime("%Y-%m")


def monthly_summary(boundaries, active_months):
    """Declared post-settlement/pre-decision UTC cuts; no00:01 approximation."""
    points = sorted(boundaries.items())
    months = []
    for (start, before), (finish, after) in zip(points, points[1:]):
        stamp = datetime.fromtimestamp(start / 1000, timezone.utc)
        month = stamp.strftime("%Y-%m")
        complete = stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0
        if before <= 0:
            continue
        months.append(dict(month=month, start=start, finish=finish,
                           complete=complete, active=month in active_months,
                           pnl=after-before, return_fraction=after/before-1))
    complete = [m for m in months if m["complete"]]
    active = [m for m in complete if m["active"]]
    quarter_groups = {}
    for m in months:
        quarter = m["month"][:4] + "Q" + str((int(m["month"][5:])-1)//3+1)
        quarter_groups.setdefault(quarter, []).append(m)
    quarters = [q for q in quarter_groups.values()
                if len(q) == 3 and all(m["complete"] for m in q)]
    returns = [m["return_fraction"] for m in complete]
    contributions = sorted([m["pnl"] for m in months], reverse=True)
    return dict(months=months, complete_months=len(complete), active_months=len(active),
                positive_active=sum(m["pnl"] > 0 for m in active),
                positive_calendar=sum(m["pnl"] > 0 for m in complete),
                median_return=float(np.median(returns)) if returns else None,
                complete_quarters=len(quarters),
                positive_quarters=sum(sum(m["pnl"] for m in q) > 0 for q in quarters),
                pnl_without_best_two=sum(m["pnl"] for m in months)-sum(contributions[:2]))


class BtcResearchR11Base1m(Strategy):
    """M1 accounting observer; signal and management decisions remain4h."""
    MODE = "abstract"
    START = 1602720000000
    FINISH = 1767225600000

    def _log(self, label, payload):
        # Event logs stay small; monthly history is emitted as separate rows.
        self.log(label + " " + json.dumps(payload, separators=(",", ":"), allow_nan=False))

    def _observe(self, stage):
        now = int(self.time)
        # BTC-only futures equity. portfolio_value multiplies open PnL by
        # leverage in this checkout, so it is deliberately not used here.
        equity = float(self.balance) + (float(self.position.pnl) if self.is_open else 0.0)
        assert math.isfinite(equity)
        self.vars["peak"] = max(self.vars.get("peak", 10000.0), equity)
        drawdown = equity / self.vars["peak"] - 1
        self.vars["dd"] = min(self.vars.get("dd", 0.0), drawdown)
        self.vars["sequence"] = self.vars.get("sequence", 0) + 1
        self.vars["last_equity"] = equity
        active = self.vars.setdefault("active_months", set())
        if self.is_open:
            # Pre marks describe exposure during the minute that just closed;
            # an opening fill at T instead belongs to the new interval.
            active.add(month_name(now if stage == "open" else now-1))
        boundaries = self.vars.setdefault("boundaries", {self.START: 10000.0})
        if stage == "pre":
            self.vars["minute_marks"] = self.vars.get("minute_marks", 0) + 1
            stamp = datetime.fromtimestamp(now / 1000, timezone.utc)
            if stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0:
                boundaries[now] = equity
        if now >= self.FINISH:
            # A later terminal close callback replaces the mark with post-fee equity.
            boundaries[self.FINISH] = equity
        return equity

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate - 0.00045) < 1e-12
            assert abs(self.balance - 10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        # This is signal alignment, not a market-session/calendar filter.
        if now % BAR != 0:
            return
        count = 62 if self.MODE == "CUSUM" else 26
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        rows = closed_window(candles, now, count)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            self.vars["cusum"] = (0.0, 0.0)
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        if self.MODE == "CUSUM":
            direction, state = cusum_step(rows, self.vars.get("cusum", (0.0, 0.0)))
            self.vars["cusum"] = state
        else:
            assert self.MODE == "ABSORPTION"
            direction = absorption_signal(rows)
        if not direction or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0) + 1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0) + 1
            return
        atr = atr14(rows)
        if atr is None:
            return
        # Flat BTC account: wallet equals equity. Reuse the frozen2% fee-aware
        # plan, eight-decimal research precision and90% margin ceiling.
        capital = max(0.0, float(self.balance))
        plan = entry_plan(float(self.price), capital, float(self.available_margin),
                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)
        if plan is None or self.price + direction * 2 * plan["distance"] <= 0:
            return
        self.vars["direction"] = direction
        self.vars["plan"] = plan

    def should_long(self):
        return self.vars.get("direction") == 1

    def should_short(self):
        return self.vars.get("direction") == -1

    def go_long(self):
        self.buy = self.vars["plan"]["qty"], self.price

    def go_short(self):
        self.sell = self.vars["plan"]["qty"], self.price

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        stop = entry - direction * plan["distance"]
        target = entry + direction * 2 * plan["distance"]
        assert qty * (plan["distance"] + self.fee_rate * (entry + stop)) <= plan["risk_budget"] + 1e-6
        self.stop_loss = qty, stop
        self.take_profit = qty, target
        self.vars["entries"] = self.vars.get("entries", 0) + 1
        self._observe("open")

    def update_position(self):
        # Preserve the four-hour management clock despite the M1 observer.
        if int(self.time) % BAR == 0 and int(self.time) - int(self.position.opened_at) >= 12 * BAR:
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        now = int(self.time)
        active = self.vars.setdefault("active_months", set())
        active.add(month_name(now-1))
        # At a month boundary, retain both the held interval and any fee-only
        # execution month. Terminal liquidation belongs to the final interval.
        if now < self.FINISH:
            active.add(month_name(now))
        self.vars["last_exit_at"] = now
        self._observe("close")
        if now >= self.FINISH and self.vars.get("emitted"):
            self._emit("FINAL")

    def _emit(self, stage):
        summary = monthly_summary(self.vars["boundaries"], self.vars.get("active_months", set()))
        # Emit rows at the end, so one bounded log page can retrieve all months.
        for item in summary.pop("months"):
            self._log("R11_MONTH", dict(stage=stage, **item))
        summary.update(stage=stage, equity=self.vars["last_equity"],
                       dd_m1_events=self.vars.get("dd", 0),
                       minute_marks=self.vars.get("minute_marks", 0),
                       sequence=self.vars.get("sequence", 0),
                       signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
                       invalid_windows=self.vars.get("invalid_windows", 0))
        self._log("R11_SUMMARY", summary)

    def before_terminate(self):
        self._observe("terminal")
        self.vars["emitted"] = True
        self._emit("PRETERMINAL")
```

## BtcResearchR10Base4h
SHA256 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9

```python
import json
import math

import numpy as np
from jesse.strategies import Strategy

BAR = 14400000
DAY = 86400000


def closed_window(candles, now, count):
    """Use only consecutive, closed 4h bars; no synthetic gap repair."""
    rows = candles[candles[:, 0] + BAR <= now][-count:]
    if len(rows) != count or rows[-1, 0] != now - BAR:
        return None
    if not np.all(np.diff(rows[:, 0]) == BAR):
        return None
    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):
        return None
    if np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2])):
        return None
    if np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2])):
        return None
    return rows


def atr14(rows):
    previous = rows[-15:-1, 2]
    current = rows[-14:]
    tr = np.maximum(current[:, 3] - current[:, 4],
                    np.maximum(abs(current[:, 3] - previous), abs(current[:, 4] - previous)))
    value = float(np.mean(tr))
    return value if math.isfinite(value) and value > 0 else None


def breadth_state(closes):
    changes = np.diff(closes)
    positive = changes > 0
    negative = changes < 0
    if int(positive[-6:].sum()) >= 4 and int(positive[-24:].sum()) >= 16:
        return 1
    if int(negative[-6:].sum()) >= 4 and int(negative[-24:].sum()) >= 16:
        return -1
    return 0


def breadth_signal(rows):
    """Count sign persistence, not return magnitudes; consume only new states."""
    now_state = breadth_state(rows[-25:, 2])
    old_state = breadth_state(rows[-26:-1, 2])
    return now_state if now_state != old_state else 0


def funding_failure_signal(rows, now, events):
    """Observe a full post-payment bar; never know or collect the next payment."""
    event_start = now - BAR
    matching = []
    for event in events:
        raw = int(event["settled_at"])
        effective = raw // 60000 * 60000
        if effective == event_start and 0 <= raw - effective <= 1000:
            if int(event["available_at"]) <= now and int(event["available_at"]) > raw:
                matching.append(event)
    if len(matching) != 1:
        return 0, None
    event = matching[0]
    rate = float(event["rate_decimal"])
    if not math.isfinite(rate):
        return 0, None
    pre, post = rows[-2], rows[-1]
    if rate > 0 and pre[2] > pre[1] and post[2] < pre[1]:
        return -1, dict(settled_at=int(event["settled_at"]), available_at=int(event["available_at"]), rate=rate)
    if rate < 0 and pre[2] < pre[1] and post[2] > pre[1]:
        return 1, dict(settled_at=int(event["settled_at"]), available_at=int(event["available_at"]), rate=rate)
    return 0, None


def entry_plan(price, capital, margin, leverage, fee, direction, distance):
    stop = price - direction * distance
    values = (price, capital, margin, leverage, distance, stop)
    if direction not in (-1, 1) or not all(math.isfinite(v) and v > 0 for v in values):
        return None
    if not math.isfinite(fee) or fee < 0:
        return None
    unit_loss = distance + fee * (price + stop)
    # 2% includes both execution fees. The 90% margin ceiling retains the
    # historical reserve and does not increase the stop's monetary risk.
    risk_qty = 0.02 * capital / unit_loss
    margin_qty = 0.90 * margin * leverage / (price * (1 + fee * leverage))
    qty = math.floor(min(risk_qty, margin_qty) * 1e8) / 1e8
    if qty <= 0:
        return None
    assert qty * unit_loss <= 0.02 * capital + 1e-6
    return dict(qty=qty, price=price, capital=capital, distance=distance,
                stop=stop, risk_budget=0.02 * capital,
                planned_loss=qty * unit_loss, margin_capped=margin_qty < risk_qty)


class BtcResearchR10Base4h(Strategy):
    """R10 discovery harness: one BTC position, fixed risk and base costs only."""
    MODE = "abstract"
    START = 1602720000000
    FINISH = 1767225600000

    def _log(self, label, value):
        self.log(label + " " + json.dumps(value, separators=(",", ":"), allow_nan=False))

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT"
            assert self.leverage == 3
            assert abs(self.fee_rate - 0.00045) < 1e-12
            self.vars["checked"] = True
            self._log("R10_CONFIG", dict(mode=self.MODE, risk=0.02, aggregate=0.06,
                                        leverage=self.leverage, fee=self.fee_rate,
                                        margin_buffer=0.90, stop_atr=2, target_r=2, hold_hours=48))
        self.vars["direction"] = 0
        rows = closed_window(self.candles, now, 26)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            return
        if self.MODE == "BREADTH":
            direction = breadth_signal(rows)
            evidence = None
        else:
            assert self.MODE == "POST_FUNDING"
            events = self.get_funding_history(count=6)
            assert all(int(e["available_at"]) <= now for e in events)
            direction, evidence = funding_failure_signal(rows, now, events)
        if not direction or not self.START < now < self.FINISH:
            return
        # Signals are evaluated and consumed while occupied as well. No deferred
        # order or re-entry from a previously blocked funding/breadth event.
        self.vars["signals"] = self.vars.get("signals", 0) + 1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0) + 1
            return
        atr = atr14(rows)
        if atr is None:
            return
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        plan = entry_plan(float(self.price), capital, float(self.available_margin),
                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)
        if plan is None or float(self.price) + direction * 2 * plan["distance"] <= 0:
            return
        self.vars["direction"] = direction
        self.vars["plan"] = plan
        self.vars["evidence"] = evidence

    def should_long(self):
        return self.vars.get("direction") == 1

    def should_short(self):
        return self.vars.get("direction") == -1

    def go_long(self):
        plan = self.vars["plan"]
        self.buy = plan["qty"], self.price

    def go_short(self):
        plan = self.vars["plan"]
        self.sell = plan["qty"], self.price

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        distance = plan["distance"]
        stop = entry - direction * distance
        target = entry + direction * 2 * distance
        assert qty * (distance + self.fee_rate * (entry + stop)) <= plan["risk_budget"] + 1e-6
        self.stop_loss = qty, stop
        self.take_profit = qty, target
        self.vars["entries"] = self.vars.get("entries", 0) + 1
        self._log("R10_ENTRY", dict(time=int(self.time), direction=direction, entry=entry,
                                   qty=qty, stop=stop, target=target, plan=plan,
                                   evidence=self.vars.get("evidence")))

    def update_position(self):
        # No ratchet, discretionary exit or same-close reversal. Funding applies
        # continuously to actual held quantity, independently of signal inputs.
        if int(self.time) - int(self.position.opened_at) >= 12 * BAR:
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        self.vars["last_exit_at"] = int(self.time)

    def before_terminate(self):
        self._log("R10_COUNTERS", dict(signals=self.vars.get("signals", 0),
                                     occupied=self.vars.get("occupied", 0),
                                     entries=self.vars.get("entries", 0),
                                     invalid_windows=self.vars.get("invalid_windows", 0)))
```

## BtcResearchR13ExternalBase1m
SHA256 aea8fe53975ab2a75efdccc1f254cd15c07299faa3acdeab6466be985f91106a

```python
import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import atr14, entry_plan

HOUR = 3600000


def closed_hour_window(candles, now):
    rows = candles[candles[:, 0]+HOUR <= now][-26:]
    if len(rows) != 26 or rows[-1, 0] != now-HOUR:
        return None
    if not np.all(np.diff(rows[:, 0]) == HOUR):
        return None
    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):
        return None
    if np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2])) or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2])):
        return None
    return rows


def external_confirmation(btc, eth, require_eth):
    """Both baselines exclude current returns; BTC alone defines direction."""
    own, leader = np.diff(np.log(btc[:, 2])), np.diff(np.log(eth[:, 2]))
    own_sigma = float(np.std(own[:-1], ddof=1))
    leader_sigma = float(np.std(leader[:-1], ddof=1))
    if not all(math.isfinite(x) and x > 0 for x in (own_sigma, leader_sigma)):
        return 0
    if abs(float(own[-1])) > own_sigma:
        return 0
    momentum = float(own[-7:-1].sum())
    direction = 1 if momentum > 0 else -1 if momentum < 0 else 0
    if require_eth and not (abs(float(leader[-1])) >= 2*leader_sigma and direction*float(leader[-1]) > 0):
        return 0
    return direction


class BtcResearchR13ExternalBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % HOUR:
            return
        btc = closed_hour_window(self.get_candles(self.exchange, "BTC-USDT", "1h"), now)
        eth = closed_hour_window(self.get_candles(self.exchange, "ETH-USDT", "1h"), now)
        if btc is None or eth is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert np.array_equal(btc[:, 0], eth[:, 0])
        assert math.isclose(float(btc[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("ETH_CONFIRM", "BTC_CONTROL")
        direction = external_confirmation(btc, eth, self.MODE == "ETH_CONFIRM")
        if not direction or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(btc)
        if atr is None:
            return
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None or self.price+direction*2*plan["distance"] <= 0:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = direction

    def update_position(self):
        if int(self.time) % HOUR == 0 and int(self.time)-int(self.position.opened_at) >= 6*HOUR:
            self.liquidate()
```

## BtcResearchR17RelativeBase1m
SHA256 b40f428caaa728a117953fc97e4eee3372b895e622ba927c695fdef665dfefb8

```python
import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def relative_beta(btc, eth):
    """240 paired returns from241 prior closes; current closes never fit beta."""
    own = np.diff(np.log(btc[-242:-1, 2]))
    external = np.diff(np.log(eth[-242:-1, 2]))
    assert len(own) == len(external) == 240
    xc, yc = external-np.mean(external), own-np.mean(own)
    denominator = float(np.dot(xc, xc))
    variance = denominator/(len(external)-1)
    if not math.isfinite(variance) or variance <= 0:
        return None
    beta = float(np.dot(xc, yc)/denominator)
    return beta if math.isfinite(beta) else None


def relative_level_state(btc, eth, fitted_beta, residual):
    """Use one current refit for all60 reference levels and the current level."""
    model_beta = fitted_beta if residual else 0.0
    levels = np.log(btc[-61:, 2])-model_beta*np.log(eth[-61:, 2])
    reference = levels[:-1]
    assert len(reference) == 60
    mean = float(np.mean(reference))
    sigma = float(np.std(reference, ddof=1))
    evidence = dict(fitted_beta=fitted_beta, model_beta=model_beta,
                    mean=mean, sigma=sigma, z=None, beta_returns=240, reference_levels=60)
    if not math.isfinite(mean) or not math.isfinite(sigma) or sigma <= 0:
        # Degenerate levels are neutral, with no epsilon/winsorization rescue.
        evidence["mean"] = mean if math.isfinite(mean) else None
        evidence["sigma"] = sigma if math.isfinite(sigma) else None
        return 0, evidence
    z = float((levels[-1]-mean)/sigma)
    if not math.isfinite(z):
        return 0, evidence
    evidence["z"] = z
    state = 1 if z <= -2 else -1 if z >= 2 else 0
    return state, evidence


class BtcResearchR17RelativeBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("RESIDUAL", "PRICE")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        btc = closed_window(self.get_candles(self.exchange, "BTC-USDT", "4h"), now, 242)
        eth = closed_window(self.get_candles(self.exchange, "ETH-USDT", "4h"), now, 242)
        if btc is None or eth is None or not np.array_equal(btc[:, 0], eth[:, 0]):
            self.vars["relative_state"] = 0
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(btc[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        # ETH validity and finite positive variance are shared by the PRICE arm.
        beta = relative_beta(btc, eth)
        if beta is None:
            self.vars["relative_state"] = 0
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        state, evidence = relative_level_state(btc, eth, beta, self.MODE == "RESIDUAL")
        previous = self.vars.get("relative_state", 0)
        self.vars["relative_state"] = state
        # Refit-induced transitions are intentionally part of this definition.
        direction = state if state and state != previous else 0
        if not direction or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(btc)
        if atr is None:
            return
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None or self.price+direction*2*plan["distance"] <= 0:
            return
        self.vars["plan"] = dict(plan, relative=dict(evidence))
        self.vars["direction"] = direction

    def on_open_position(self, order):
        # Reuse the unchanged R11 fee-risk assertion, actual-fill SL/TP and count.
        super().on_open_position(order)
        side = 1 if self.is_long else -1
        key = "long_fills" if side == 1 else "short_fills"
        self.vars[key] = self.vars.get(key, 0)+1
        self._log("R17_RELATIVE_OPEN", dict(time=int(self.time), mode=self.MODE,
            direction=side, evidence=self.vars["plan"]["relative"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R17_RELATIVE_STATS", dict(stage=stage, mode=self.MODE,
            long_fills=self.vars.get("long_fills", 0),
            short_fills=self.vars.get("short_fills", 0),
            signals=self.vars.get("signals", 0), occupied=self.vars.get("occupied", 0)))
```

# Closures and prior protocols read completely

## strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_FROZEN_PROTOCOL_20261019.md
SHA256 2df6de45e4f438c5a9e3b111b9b66f9a3e68486753bd8873b127a9cb0df77d08

# BTC — protocolo congelado R8

## Objetivo y presupuesto

Investigar selección de entradas/contexto original tras R7, sin seguir afinando defensas de salida. Dos investigadores: rootfamiliaV801..805,subagenteexperimentalX801..805.20backtestsnominales=10recetasB/C;2simultáneosporinvestigador,max4global;2análisismaxglobal. Cada investigador empieza con suprimerpar y pide ticketparaelsiguiente. Protocoloantesfuentes/drafts/resultados. Ceroañadidosposthoc.

N204=X03ExploreR204referenciaultimate. N503=N204ExploreR503yP604=N503CapacityR604candidatasnopromovidas. R7defensasgeneralesdeganancia fallaronentreambas semillas;S701replicóP604yS704P603. O700instrumentaciónparidadexactaN503264/271trades,375R/82eventos/11ocupados/67fills,registrodisponible. Noevidencianuevaalrepetiridénticatrayectoria.

## Familia de contexto

### V801 — BtcContextR801

Consumir eventoN204 original; veto si ERnoOK, conERexactoN5030<ER<=1/3. Control del latch: ERse aplica postevento, noalsetup/latchcomoN503.

### V802 — BtcContextR802

Consumir eventoN204; veto si Gactual=True. Transferencia explícita P601desdeN503aN204, no nuevoindicador.

### V803 — BtcContextR803

Consumir eventoN204; veto si ERnoOK ANDGactual. Recortar trayectorias directas sólo encontexto original.

### V804 — BtcContextR804

Consumir eventoN204; veto si ERnoOK ORGactual. Unióncontrolada para compararcon ERsolo/Gsolo/intersección.

### V805 — BtcContextR805

Consumir eventoN204; veto si ERnoOK ANDalgunoR(cFull[:-1]),R(cFull[:-2]),R(cFull[:-3])True. ExcluyecurrentR; recomputaciónprefijosdelbufferactual,noestadohistóricobuffer. Transferencia condicionada del R6P602queeraidénticoN503; no afirmar mecanismo inédito.

N204setup/latchfalse→trueoriginalintacto,geometría1..3ATRoriginal,rawsourceevent+occupiedcontadosANTESveto. Veto consume evento yborra explore_event,sinretry/cola mientrasN204setupTrue. R/GpuroR6:>=140velas4hcontiguascerradas,EMA120[-1]>[-10],C>EMA120−ATR,RSI3<=20paraR,sinRSIparaG;entrye=min(L,C−.25ATR),distance=EMA20−e entre1..3ATR y>=6fee*e. No llamar métodosdeorden ni mutarplan/ledger/capacidad. Vcontexto usa cFull=_explore_window(143),invalid=>veto+contadorinvalid,noinferirpreparación. V801sóloERusa14original. ContadoresER/G/recienteR/veto/aceptado: observacionales,no órdeneshipotéticas. Prefijoshistóricosesbufferactual,notracehistóricodeindicadores.

## Familia experimental

### X801 — BTCExploreR801

Reemplazar setup suplemento: W12previasthroughs;k=maxV,empatemásreciente;kverde,A=HLC3k;Cs>Cprev12,Cs>=A,troja,Ct<A. Costeproxydeeventodominante,no q/VWAPcohorte niER.

### X802 — BTCExploreR802

W6previasthroughs;L*=maxL,H*=minH;L*<H*,CsentreL*yH*inclusive,troja,Ct<L*. Salidabajistadezonacomúnnegociadaentodaslas6velas; noinsidebarindividual.

### X803 — BTCExploreR803

W12previas;k=min(C-O),empatemásreciente;kroja,knoúltima;M=(Ok+Ck)/2;desde k+1hastas almenosunC>=M yningunoC>Ok,Cs>=M;troja,Ct<M. Impulso→recuperaciónincompleta→pérdidademitad. Cs>=M implica existencia,condiciónredundante explícita.

### X804 — BTCExploreR804

W12previas,ri=Ci-Cprevio;sumVi*ri primeras6>0 yúltimas6<0;Cs>Cprev12;troja,Ct<min(Cs,Os). Transiciónvolumen-retornoentre cierres,no qdelocalización niER.

### X805 — BTCExploreR805

Cs>Cprev12,troja;exact240M1cerradas/contiguasdet4h,OHLCVválido,V>=0,totalV>0,últimoC1m=Ct. Cortartrasprimerminuto cuyoVcum>=.5Vtotal,enterocompletamentealprimergrupo;segundo=resto;ambosnovacíos yV>0. VWAPHLC3×Vcadauno,A2<A1,Ct<minLprimergrupo. FraccióndeVrealprimergrupo sólo diagnóstico;sinfraccionarcompartirOHLC,inventar intraminutofillsni afirmar mitadesexactas.

Sólosetupdel suplemento se reemplaza; latchfalse→trueavanzaocupado/pending,señalcompletacomovariantesprevias,sincola. Riesgo/d/orden/SL1R/TP2R/48h/priorityoriginal. d=max(Hs,Ht)+.25ATRt−Ctcongate1..3ATRinmutable. Todos usanventana14parad/gate; W6oW12segúnreceta. Datosprecios/volumenrealesOHLCVcerrados; q/HLC3×Vsonproxies,no flujotakerobservado. X805coberturaM1exacta240desde t.open a t.open+4h−1m,cierres<=decisión,shape2D6cols,OHLCfinitepositivo,L<=min(O,C)<=max(O,C)<=H,V>=0;últimoC=Ct exacto. Missing/corrupt/clock/mismatchfalseconcontadoresdistintos. Sinfeedsnuevos,interpolación niinferirordenintraminuto.

## Contrato fijo

2020-10-15→2025-12-31EXCLUSIVA,últimoprecio2025-12-30.2026CERRADO inclusoinspección; muestra de desarrollo reusada,noOOSni pruebaantisobreajuste.10000USDTshared,1%trade/8%agregado,isolated5x,nopyramid,cap4.4,reserva.001sizing;fee.00045porlado;warmup240,debugtrue,fastfalse,charttrue. RutasBTC/PAXG/SPY4h+3feeds1m. PAXGMarketBEfeeoriginal. SPYBSecondsegundaexacta/precioestructural;SPYCMarketdesde2/preciomercado. B/C no son muestrasindependientes. No cambiarHP,ledger,sizing,STOPshortolargooriginal,jerarquía,feeglobal,dataseries,live/paper/Pi ni funding.

## Auditoría y gates antes de resultados

Fills/qty/fees/PNL/wallet/terminal/MTMUTCdiario4anclashistóricas. CohortessuplementoMARKET/STOP/largo/otrasrutas,desplazamientoycapitalendógenos,no causalidadaislada. Overlays+5/+10bpsRTadicionales sobre fills/cantidades/precios/tiemposfijos,no mayorfeeengine ni slippagepuro. Mesesfull61/all63,Q19/21,activosycalendariomostrados,positivos>0sinredondeo.

TODOSambasB/C paraelegir:ΔnetN204>1e-7;+5Mactivos>=65%yQ>=80%full/included;+10net>=N204−1e-7;DDmotor>=−25%. Diversidadprefijada adaptada a entradas:suplemento>=30fills y>=10entradasdel suplementoañadidas+retiradasrespectoN204porclavesymbol/side/entrytype/open. Umbralesoperativos,no confianzaestadística. EnV mideeventosfiltrados;Xpuedesustituirsetup. AdemásΔMTMN204>1e-7enalmenos3de5bloquesanuales2021..2025,2025PARCIAL;ΔnetN204trasdescontar mejormesincremental>1e-7. Omitir sóloaritmético,no reejecucióncapitalni OOS. Parámetrosnocambianporresultados. Ranking mayor mínmargenM/Q,mayorminΔ+10,menorpeorDD,IDlex.

Unaúnica elegible despuésde20 activa6fullsadicionales:2feeengine.00070/ladoB/C vsN204altofeeB9a6c7c24-8847-42d1-aadb-206f21723c1f/C541d2bf4-ffca-4f2d-969b-c25165e7b960;exigirΔnetpositivo,M65/Q80full/allambas,DD25.4vecinosnominalesTP1.8R/2.2RcadaB/Csinmoverd/SL/48hresto. No elegirsegundasi falla,ni vecino ganador. Ningunaelegible=>ceroextras;máximototal26.

## QA, archivos y mantenimiento

Antesdelprimerparporfamilia:fuentesexactas/protectedmethods/ramasoriginales,fixturesfronteras/empates/ventanas/contexto/clocks/missing/ER,latchvsfiltropostevento,comentariosconstantesyrenovaciónstate. RevisióncruzadadespuésdeQAantesdeusardatoscomoavance. Testssintéticosdehelpersno pruebanlifecycle/financiero. Todoslos20formularios/60snapshots yfuentesfinalesleídos;auditoríasJSON/reportes/URLs yselecciónarchivados. Protocoloesperadorevisiónantesdeejecución;nodejarfuentesenestado ambiguo.

Jesserespondenormalmente;0backtestsactivosalinicio. No limpieza sin señal de necesidad. Noretirarfuentes/sesiones/reportesanteriores; sihacefaltaarchivarconservarcódigoexacto,dependencias,hipótesis,resultados,URLs,motivodescarteymanifiestorecuperaciónantes. ErrorPNGartifact_changedprevionoseatiendeborrandoestrategias;no repetirlecturasdeimagenconocidamentefallidas ni usarworkarounds externos.


## strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_FINAL_RESEARCH_RESULTS_20261019.md
SHA256 4066e53cf744efc6166d59abdae26ebaf6dc7842f8c6d81b45a6e75e7b691f7f

# BTC R8 — resultado final y candidata Y902 retenida

## Decisión y alcance

Se completaron13recetas en26backtests nominales:5contextuales,5experimentales y3del agente creativo adicional solicitado. Se conserva N204 como referencia operativa y Y902 como candidata de investigación prometedora. Ninguna receta cumple simultáneamente todas las puertas congeladas en B y C; por eso no se activan las6verificaciones condicionales ni se elige un ganador alternativo. Esto no equivale a descartar Y902 ni demuestra sobreajuste.

2026 permaneció cerrado incluso a inspección. Misma muestra de desarrollo2020-10-15 inclusiva→2025-12-31 exclusiva, cuatro años calendario completos2021–24 y2025parcial; no validación fuera de muestra. B/C son configuraciones relacionadas de SPY, no dos muestras independientes. Neto de cartera BTC/PAXG/SPY con capital compartido10000USDT y riesgo1% por operación/8% agregado; aislado5x, capnocional4.4 yfee.00045porlado. Reserva.001es dimensionamiento, no slippage ejecutado. No se añadió funding. Se mantuvieron PAXG original y las variantes SPY BSecond/CMarket.

## Resultados nominales

N204 referencia: B13056.614915 y C13239.442380USDT. N503 semilla de la familia creativa: B13328.711713 y C13536.902513USDT. Cada enlace lleva al registro de backtest devuelto por Jesse.

|Receta|Neto B USDT|Neto C USDT|Δ N204 B/C|Conclusión|
|---|---:|---:|---|---|
|V801|[13328.71](http://localhost:9200/#/backtest/b0c5ce4f-ed64-4b07-bdca-f708aae2d445)|[13536.90](http://localhost:9200/#/backtest/5de86562-4ba7-4f2f-b9fb-f647ed2a8b70)|272.10 / 297.46|Identidad económica con N503; no nueva observación independiente. C falla calendario bajo +5.|
|V802|[12838.90](http://localhost:9200/#/backtest/876feccb-b93c-4fb0-a6ea-3a4b58c642c7)|[13013.55](http://localhost:9200/#/backtest/8e889155-eabc-4187-acc5-748f98dc5378)|-217.71 / -225.89|Menor neto; cambios demasiado escasos.|
|V803|[13056.61](http://localhost:9200/#/backtest/e7ef94a6-5249-44ea-b0bc-8c3cb7e3c531)|[13239.44](http://localhost:9200/#/backtest/1d818489-9707-43ab-8106-98cacdbf0a56)|0.00 / 0.00|Identidad económica con N204.|
|V804|[13123.60](http://localhost:9200/#/backtest/b481d1da-f0b2-4c9c-b663-b4a4a8c44896)|[13307.81](http://localhost:9200/#/backtest/b042558a-4ea4-41f1-a2de-7d51d8d53b56)|66.99 / 68.37|Pequeña mejora nominal; falla calendario, distribución y omisión del mejor mes.|
|V805|[13056.61](http://localhost:9200/#/backtest/0af9be29-c28a-490b-a7d7-6a481660a950)|[13239.44](http://localhost:9200/#/backtest/ec8d524e-d8c0-4b55-8dbe-da6ae8051918)|0.00 / 0.00|Identidad económica con N204.|
|X801|[4947.13](http://localhost:9200/#/backtest/f660ef63-d7c6-4792-9f21-06c1d7ebd85f)|[5129.70](http://localhost:9200/#/backtest/4e432aac-71c2-4023-a978-6d8a618aa660)|-8109.48 / -8109.74|Ancla en vela de máximo volumen; menor neto.|
|X802|[7971.10](http://localhost:9200/#/backtest/261696a9-33ee-4504-a310-b8a44c63dcd3)|[8181.46](http://localhost:9200/#/backtest/07a45656-81e2-4fd8-9851-3aa16a782c2e)|-5085.51 / -5057.98|Ruptura de compresión común de seis velas; menor neto.|
|X803|[8013.23](http://localhost:9200/#/backtest/5208fe79-c420-4328-b5dd-1a67177f1ccf)|[8180.37](http://localhost:9200/#/backtest/a86de192-2f0d-4b34-a4ae-ce4f686d4757)|-5043.39 / -5059.08|Readmisión y pérdida del punto medio de vela bajista; menor neto.|
|X804|[5040.50](http://localhost:9200/#/backtest/ed50a692-6ce7-4014-baea-eb7b6b5acad9)|[5213.66](http://localhost:9200/#/backtest/09421154-a313-480c-9ab0-6c28cdcf810d)|-8016.11 / -8025.78|Cambio de presión de volumen/retornos; menor neto.|
|X805|[3846.19](http://localhost:9200/#/backtest/22b632fe-7fa2-450a-9f34-47c6e13efec8)|[3967.02](http://localhost:9200/#/backtest/69c41479-2763-4150-ad60-68e1fd605b41)|-9210.43 / -9272.42|Reloj de volumen M1; sobreoperación y menor neto.|
|Y901|[11046.64](http://localhost:9200/#/backtest/ee4ecf79-a83d-4388-b4de-3f2e44d62fd2)|[11228.81](http://localhost:9200/#/backtest/fc3f7e80-a6a0-4d61-8bc1-11ef693aac9c)|-2009.97 / -2010.63|Retesteo LIMIT; menor neto.|
|Y902|[13446.23](http://localhost:9200/#/backtest/cb305a17-1312-463e-bbf1-c8173dfae22c)|[13680.35](http://localhost:9200/#/backtest/b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff)|389.62 / 440.91|Candidata prometedora retenida; B falla únicamente concentración nominal del mejor mes.|
|Y903|[10679.17](http://localhost:9200/#/backtest/99393647-2bca-405b-b3f3-6c2b1a0bed33)|[10898.84](http://localhost:9200/#/backtest/745952c3-9fef-4c4c-8450-9fe8b6d142ff)|-2377.44 / -2340.60|Invalidación adversa; menor neto pese a recortar algunas salidas.|

V801 reproduce económicamente N503; V803 y V805 reproducen N204 (tolerancia1e-7, tiempos/tipos exactos). Son comprobaciones de equivalencia en esta muestra, no tres mejoras independientes. Las fuentes originales no cambian; la ocupación sí puede cambiar ejecuciones: X805 retiene30de31largos originales, no31. Todos los experimentos deben evaluarse por cartera y coste de oportunidad, no sólo por rendimiento aislado de su suplemento.

## Y902: qué aporta y qué queda incierto

Usa el mismo evento N503 pero solicita un SELL STOP en el mínimo de la vela de señal, válido sólo durante la siguiente4h. Distancia técnica congelada desde la señal, SL1R/TP2R desde fill y48h desde fill real; misma fórmula de sizing evaluada en el precio candidato, prioridad original y cancelación existentes. No hay reintentos de la misma señal. Se ejecutaron46suplementos frente a67N503. Los logs completos identifican45STOP y1MARKET por cartera; tipo STOP no significa corto original. El motor puede seleccionar MARKET cuando su regla de proximidad lo determina.

Mejora frente a N204: +389.619610/+440.906791USDT; frente a N503: +117.522813/+143.446658. Bajo overlay de10bps adicionales por round trip, mejora frente a N204 +546.100683/+591.583164. Son costes estáticos sobre fills/cantidades fijados, no un backtest con comisión elevada ni una prueba de liquidez real.

Bajo +5bpsRT:
- B:41de63meses calendario positivos (41/62activos), igual número calendario que N204.
- C:42de63positivos (42/62activos), un mes más que N204.
- Trimestres17/21en ambas, igual a N204B y uno menos que N204C.
- Sólo meses completos: B41/61calendario y C42/61, sobre60activos en Y902.
- Mejora MTM en4de5bloques2021–25 frente a N204;2025no es año completo.

Hay un coste: DDmotor−9.6941%/−9.6301%, frente a−8.7768%/−9.0579%N204. No mejora todas las dimensiones.

Enero2022 aporta +409.380189/+400.581645USDT de ventaja incremental. Al descontarlo aritméticamente, el resto suma−19.760578/+40.325146 frente a N204. Es el único fallo de B bajo el contrato de selección; C cumple todas las condiciones. Los−19.76no son una pérdida de un escenario de2022. La cercanía al cero, el mejor neto bajo costes y4/5bloques favorables justifican retener la candidata. La concentración justifica prudencia antes de sustituir la referencia; no diagnostica por sí sola sobreajuste.

## Consulta posterior: regularidad quitando enero2022 de ambas

Se realizó un análisis descriptivo adicional a petición del usuario, sin nuevos backtests, sin ajustar fuentes ni puertas y sin abrir2026. Entre los62meses calendario restantes:
- Nominal: B41/62positivos en ambas; C42/62en ambas.
- +5bpsRT: B N20441/62 frente aY90240/62; C41/62en ambas.
- +10bpsRT: B38/62en ambas; C39/62en ambas.

Y902 tiene un mes plano/inactivo; sus porcentajes sobre meses activos usan61, frente a62N204. El denominador activo puede elevar su porcentaje sin agregar un mes ganador. Sólo meses completos (60calendario tras retirar enero) da la misma conclusión relativa. No es un replay de capital sin enero ni una validación fuera de muestra.

Bajo +5 estático, la ventaja monetaria restante es +54.33/+111.64USDT; bajo+10,+128.43/+182.95. La casi igualdad nominal restante no agota la comparación, pero tampoco prueba mejora uniforme de regularidad. Detalle y código: BTC_R8_Y902_WITHOUT_JAN2022_MONTHLY_REGULARITY_20261019.md, job3025c86117854b62ac3e9b8f5581e7d6.

## Validación y trazabilidad

26formularios y78snapshots finales coherentes;37fuentes exactas (bases y rondas preservadas);13auditorías financieras de pares con4anclas inmutables, conciliando fills/qty/fees/PNL/wallet/terminal/MTM. Todos los targets pasan. Metadatos de Y901/Y902/Y903 conciliados contra logs MCP paginados completos:33/46/70suplementos por cartera. Y903modifica29salidas del suplemento emparejadas contra N503; se conservó el diagnóstico de toda la cartera separado para evitar atribuir cambios ajenos al mecanismo.

QA:102contextual,184experimental,201creativa final; hay200checks creativos previos a añadir telemetría. Estas comprobaciones se solapan y no son observaciones estadísticas independientes. Revisión independiente final310comprobacionesPASS, incluyendo puertas de26filas y trazabilidad Y903. Fuentes económicas congeladas; cambios de fixtures QA anteriores a las corridas no se presentan como backtests. La telemetría creativa se refrescó en los mismos6drafts antes de sus corridas mediante snapshots nuevos.

Hubo una respuesta MCP noJSON en el tramo previo y se suspendieron herramientas; al recuperar, se comprobaron estados existentes y se continuó el draft sin duplicar corridas. Límites lógicos de capacidad de análisis se gestionaron esperando trabajos existentes. No hubo purgas, borrados, reinicios ni cambios en framework o live/paper. Figuras PNG no se descargaron por el fallo de integridad conocido; artefactos textuales y cálculos sí se verificaron.

## Continuidad propuesta

Retener N204 y Y902 con sus fuentes actuales. La próxima fase útil es validar causalmente el cambio de ejecución Y902: qué entradas pierde/gana, cuánto depende la mejora de selección frente a precio y cuánto cambia la disponibilidad del corto original y el capital compartido. Diseñar cualquier validación de fee endógeno/bloques antes de correrla, sin afinar la receta para rescatar el margen de−19.76 ni abrir2026. No se ejecutó esa fase en esta ronda.

## Índice de evidencia

- BTC_R8_FROZEN_PROTOCOL_20261019.md y BTC_R8_CREATIVE_Y_FROZEN_ADDENDUM_20261019.md: hipótesis/gates/budget previos.
- BTC_R8_RESULTS_MATRIX_20261019.md: matriz26filas completa, elegibilidad y URLs.
- BTC_R8_FINAL_MANIFEST_20261019.md:26sesiones/78snapshots/37fuentes/13jobs y conciliaciones.
- BTC_R8_AUDIT_<receta>_20261019.md:13auditorías financieras.
- BTC_R8_Y901/902/903_SLEEVE_IDENTIFICATION_20261019.md: conciliación completa.
- BTC_R8_Y903_EXIT_ATTRIBUTION_CLARIFICATION_20261019.md y BTC_R8_Y903_SUPPLEMENT_EXIT_TRACE_20261019.md: atribución conservadora antes de resultados y29pares después.
- BTC_R8_FINAL_SELECTION_AND_METADATA_SOURCE_20261019.md: helpers finales.
- ../BTCExploreR801/reports/BTC_R8_INDEPENDENT_FINAL_GATE_REVIEW_20261019.md: dictamen independiente.
- ../BTCNovelR901/reports/BTC_R8_Y_FAMILY_RESULTS_20261019.md: informe del agente creativo.


## strategies/BTCExploreR801/reports/BTC_R8_EXPERIMENTAL_FINAL_RESULTS_20261019.md
SHA256 16a92396dc08eb9da31b48e254573295bb040cf06496f417cb6eac2037658eb5

# R8 — familia experimental BTC: cinco hipótesis, diez backtests

## Decisión de esta familia

Ninguna de las cinco hipótesis supera el neto nominal de N204 en ninguna cartera. Por esa condición necesaria ya quedan descartadas para promoción; no corresponde elegir la menos mala como nueva referencia. La selección consolidada, conciliación financiera completa y comparación de cohortes pertenecen a la auditoría central de R8. N204 sigue siendo el control, N503/P604 candidatas no promovidas.

## Diseño y límites

Se reemplazó sólo el setup del suplemento MARKET SHORT desde el esqueleto N204. Cada setup completo avanza su latch false→true incluso ocupado o pendiente; sin cola ni intento diferido. Geometría original d=max(Hs,Ht)+0.25ATR−Ct, gate1..3ATR; SL1R, TP2R y48h desde fill real. Largo y corto STOP originales, prioridades, HP, ledger y sizing intactos.

2020-10-15→2025-12-31 exclusiva; última fecha de precios2025-12-30. 2026 cerrado incluso inspección. Desarrollo reutilizado, sin prueba OOS. Capital compartido10000USDT, riesgo1% por trade/8% agregado, isolated5x, cap4.4, reserva.001 sólo sizing, fee.00045/lado, warm240, debugtrue, fastfalse, charttrue. BTC/PAXG/SPY4h+feeds1m. B=SPYsegunda oportunidad exacta/precioestructural; C=desde segunda/preciomercado. PAXG mantiene BE original dependiente del fee. Ningún cambio de datos, fee global, live/paper/Pi o funding.

## Hipótesis y resultados nominales

|Receta|Lectura|Neto B/C USDT|Sharpe B/C|Operaciones totales B/C|DDmotor B/C%|Eventos/ocupados/fills suplemento|
|---|---|---:|---:|---:|---:|---|
|X801|Pérdida del coste de la vela de mayor volumen|4947.13 / 5129.70|0.736565 / 0.748464|392 / 399|-12.6172 / -12.4988|294/79/210|
|X802|Ruptura bajista de la intersección de seis rangos|7971.10 / 8181.46|1.071839 / 1.076872|325 / 332|-13.0368 / -13.7806|171/37/127|
|X803|Recuperación fallida del mayor cuerpo vendedor|8013.23 / 8180.37|1.077109 / 1.079897|323 / 330|-11.7726 / -11.4880|185/49/133|
|X804|Transición de presión volumen × innovación entre cierres|5040.50 / 5213.66|0.749344 / 0.758312|365 / 372|-14.8298 / -11.7468|268/67/178|
|X805|Reversión intrabar usando una partición por volumen|3846.19 / 3967.02|0.539656 / 0.548995|590 / 597|-16.0514 / -15.7965|665/229/421|

X801 sustituye el VWAP de una cohorte por HLC3 de la vela de volumen máximo W12, empate más reciente; exige esa vela verde y cruce bajista del coste tras avance. X802 usa intersección real de los rangos previos W6 y pérdida por cierre de su límite inferior. X803 usa el cuerpo vendedor más negativo W12, empate más reciente, recuperación posterior limitada por su apertura y pérdida de su mitad. X804 mide cambio de signo entre dos bloques de seis de V×(C−Cprevio), con avance neto anterior y trigger bajista. X805 usa los240M1 de t y corta después del primer minuto que alcance50% del volumen, minuto completo al primer grupo, con VWAP HLC3 del segundo menor al primero y cierre por debajo del mínimo del primero. No son filtros añadidos a N204/N503 ni defensas de salida. Definiciones exactas y fórmulas en protocolo congelado central, fuentes y snapshots.

La fuerte degradación en las cinco familias indica que esos reemplazos no preservan la selección del suplemento de referencia bajo este contrato. Tener más señales no compensó su calidad y su interacción con el STOP original/capital compartido. No permite afirmar que todo método basado en volumen o aceptación sea inválido; sí descarta estas reglas concretas sin ajustar umbrales después de observar resultados.

## Observación M1 de X805

Ambas carteras:3024 consultas con datos válidos y3024 particiones. Missing_shape=0, missing_clock=0, corrupt=0, close_mismatch=0, zero_volume=0, empty_partition=0 (contadores ausentes se interpretan0). Se consulta sólo cuando Cs>Cprev12 y t roja; la cobertura observada no describe todos los minutos del histórico ni otros símbolos.

Primer grupo: fracción mínima0.5000020315817414, máxima0.6461235991665403, suma1530.0156635170379, count3024, media0.5059575606868512. Es un corte de minutos completos cercano a mitad de volumen; no mitad exacta ni fracción de OHLC compartida. valid=3024 significa cobertura/OHLC/volumen y partición válidos, NO3024 setups aceptados. Eventos665, ocupados229, fills421. VWAP HLC3×V y volumen OHLCV son proxies, no flujo taker ni fills intraminuto observados.

## QA, ejecución y trazabilidad

QA184PASS,0FAIL, job02f73c58f2c3422cbd48344fcc4cb74e; fuente/harness y review cruzada en esta carpeta. Primer harness falló porque ATR sintético2 volvía inelegible una geometría12.5; corregido sólo el stubATR5 y expectativa13.25. No se cambió ninguna fuente económica. Helpers y fixtures no demuestran el ciclo real del motor ni sustituyen la conciliación financiera central.

Revisión final: cinco fuentes exactas sin cambios desde creación, diez formularios exactos, treinta snapshots exactos; diez sesiones finished sin excepción, cero corridas propias activas. No nuevas corridas sin ticket. Dos simultáneas por par; máximo global coordinado4. Hubo interrupción MCP después del primer par; se detuvieron llamadas, luego se comprobó estado finished antes de continuar con X802. Nunca se relanzó X801 ni se usó acceso alternativo.

Los contadores terminate se imprimen antes del cierre forzado final del motor en algunos casos. X803 fills133/closes132 y X805421/420 no se interpretan como pérdidas de registro: la auditoría central debe reconstruir fills y terminal completo. Las métricas motor total_open_trades/open_pl pueden reflejar ese instante previo. No se ajustaron salidas para borrar esa diferencia observacional.

Diario de métricas y contadores: strategies/BTCExploreR801/reports/BTC_R8_EXPERIMENTAL_TERMINAL_JOURNAL_20261019.md.
Registro y formularios: strategies/BTCExploreR801/reports/BTC_R8_EXPERIMENTAL_DRAFT_REGISTRY_20261019.md.
Protocolo: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_FROZEN_PROTOCOL_20261019.md.
Matriz/auditoría financiera final: responsabilidad root; este informe no presenta los overlays como mayor fee engine ni afirma validación independiente.

## Sesiones

### X801B

Dashboard: http://localhost:9200/#/backtest/f660ef63-d7c6-4792-9f21-06c1d7ebd85f

ID: f660ef63-d7c6-4792-9f21-06c1d7ebd85f

### X801C

Dashboard: http://localhost:9200/#/backtest/4e432aac-71c2-4023-a978-6d8a618aa660

ID: 4e432aac-71c2-4023-a978-6d8a618aa660

### X802B

Dashboard: http://localhost:9200/#/backtest/261696a9-33ee-4504-a310-b8a44c63dcd3

ID: 261696a9-33ee-4504-a310-b8a44c63dcd3

### X802C

Dashboard: http://localhost:9200/#/backtest/07a45656-81e2-4fd8-9851-3aa16a782c2e

ID: 07a45656-81e2-4fd8-9851-3aa16a782c2e

### X803B

Dashboard: http://localhost:9200/#/backtest/5208fe79-c420-4328-b5dd-1a67177f1ccf

ID: 5208fe79-c420-4328-b5dd-1a67177f1ccf

### X803C

Dashboard: http://localhost:9200/#/backtest/a86de192-2f0d-4b34-a4ae-ce4f686d4757

ID: a86de192-2f0d-4b34-a4ae-ce4f686d4757

### X804B

Dashboard: http://localhost:9200/#/backtest/ed50a692-6ce7-4014-baea-eb7b6b5acad9

ID: ed50a692-6ce7-4014-baea-eb7b6b5acad9

### X804C

Dashboard: http://localhost:9200/#/backtest/09421154-a313-480c-9ab0-6c28cdcf810d

ID: 09421154-a313-480c-9ab0-6c28cdcf810d

### X805B

Dashboard: http://localhost:9200/#/backtest/22b632fe-7fa2-450a-9f34-47c6e13efec8

ID: 22b632fe-7fa2-450a-9f34-47c6e13efec8

### X805C

Dashboard: http://localhost:9200/#/backtest/69c41479-2763-4150-ad60-68e1fd605b41

ID: 69c41479-2763-4150-ad60-68e1fd605b41


## Revisión de matriz central V/X tras auditorías

Las cinco X incumplen además calendario, Δ+10 y distribución; ninguna elegible. Revisión independiente de gates V/X190comprobacionesPASS, sin reconstruir MTMdesde cero. V801replicaN503yC40/63falla; V803/V805replicanN204, noavance. X805retiene30de31entradaslargasBTC y sus30salidas en ambascarteras: se preservó código/prioridad, no todas las ejecuciones; la ocupación y el capital compartido pueden desplazar operaciones. El resultado confirma que no se deben atribuir los netos sólo al suplemento. Revisión en BTC_R8_INDEPENDENT_VX_GATE_REVIEW_20261019.md.


## strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_CREATIVE_Y_FROZEN_ADDENDUM_20261019.md
SHA256 f9bec65aad4f3ffddf8fb249b87fd141a82e2ef200998a66c61ba09fe1d22e26

# BTC R8 — ampliación creativa Y solicitada por usuario

## Alcance y momento

El usuario pidió un subagente creativo adicional después de iniciada R8. Se fijan3hipótesisANTESdecrearfuentes/drafts/corridasY;elagentenoharecibidométricasnuevasV/X. Las20nominalesV/X siguenexactamentecongeladas. Ampliación6nominalesY=3recetasB/C;total26nominales,nomás. Elecciónúnicaglobaldespuésde26;puedeactivar6verificacionesprefijadas(feeengine2yTPvecinos4),max32total. Sinsegundaselecciónsi falla ni añadidosposthoc.

### Y901 — BTCNovelR901

Mismo eventoN503; SELL LIMIT candidatoA congelado conA>Ct, doriginaldelCtcongelado, sizingoriginalconentry=A yguardentry>2d. Pendienteúnicamentesiguientebarra4h, should_cancel_entryoriginal, sinreintento. SLfill+d/TPfill−2d,48hdesdeactualfill.

### Y902 — BTCNovelR902

MismoeventoN503; SELL STOP candidatoLt congelado sóloLt<Ct,igualdadrechaza,entry>2d. Sizingoriginalconentry=Lt,doriginalCt,pendientesólosiguientebarra4h,cancelaciónoriginal/sinretry;SL1RTP2R48hfill.

### Y903 — BTCNovelR903

EntradasN503idénticas; congelarAeventoenplan/varsfill. Deadline48hprioritario;sólo4hcompletaspostfillcontiguas,cuandocierre>A_frozen yqactual=V*(2C−H−L)/(H−L)>0(span0=>q0) yC>actualentry, cerrarMARKET. Invalidezadversa,no protecciónbeneficio;SLTPoriginales.

## Invariantes y ejecución real

N503seed,N204referenceultimate,P604contextocomparación. CódigooriginalBTC largo/STOPshort,HP,ledger,sizingfórmula/caps/prioridadsinmodificar. Y901/902sólopreciodeentradaen_explore_size para suplementos másmetadatosdeanchor/candidate. El presupuesto,feesunitrisk,reserve,volatilityquota ymargin se calculan alpreciocandidato;sin riesgoextra ni qtyfija. dsignalCt sigue1..3ATR,fijoalcrearorder; desplazarlafillmueveSL/TPalrededordelfillporlógicaexistente, nóvelaestructura originaldistinta. entry>2d esguardfísicodeTPpositivo,nodeunaoptimización.

Motor smartordereligeLIMIT/STOP/MARKET porrelaciónpreciocurrente;equal/nearpuedeaproximaraMARKET. No forzartipo ni afirmar100%LIMIT/STOP;registrarrequestedentryyprecios/tiposobservados. PendienteocupaBTCycapitalreservado duranteuna4h;esaocupaciónforma parte delexperimento. _signaloriginalmantieneprioridadantesdecrearorden. should_cancel_entryoriginalexpiraalsiguientecierre;no cola deeventosocupados, no reintento, no forzar aperturaoriginal en callback; motor normal gestiona su ciclo. Deadline desde fillreal,noarmado. FillsM1reales,noproyeccióncontrafactualniiordenintraminutoinventado.

Y903usaAevento congelado,semánticasetup/latchN503exacta,entryMARKETsin cambios. Excluirvelaentradaparcial;relojsfullclosed/idempotencia/resetporfill;span0q0;48hprioritario. Sólorecortapérdidasporreadmisióndehipótesiscompradora,nosefija objetivo de pérdida monetaria ni umbraloptimizado.

## Auditoría, identificación y gates

Mismosdatos/contrato/fechasR8;2026cerradoinclusoinspección,ventana2020-10-15→2025-12-31exclusiva.10000shared1%trade/8%total,isolated5x,cap4.4,reserva.001sizing,fee.00045lado;PAXGoriginalBEfee,SPYBSecond/CMarket,4h+1mfeeds,warm240debugtruefastfalsecharttrue. Riesgo de seleccióndevelopmentmuestrareutilizadanocambia.

Corefinanciero porrun_analysisdeinputscompletos: fills/qty/fees/PNL/wallet/terminal/MTMUTC4anclas,overlays5/10RTsobre fillsfijos. Snapshottradesincluyeórdenesejecutadas, no garantizabracketscancelados: NO etiquetarSTOPoriginalpormerotipoentrada ni porratioSL/TPausente. Y901/902 mezclansmarttypes;BTCshortSTOPenentry_type_groupsnoes necesariamenteoriginalSTOP.

ConciliaciónadicionaldemetadatosvíaMCP logscompletos: leerpáginaslogs hastafin(noestima),parseBTC_EXPLORE_FILL conreceta/actualtime/entry/qty/d/target yterminalBTC_EXPLOREcounts. Exigirnumlogsfill==terminalfills==matchesbijectivoscontrapathsdelanálisisporBTCshort/openclock/precio/qty(tol1e-7),target/d2.0,terminalcloses=fills. Cualquierunknown/faltante/ambiguo=>bloqueoelegibilidad, no imputar etiquetas. Lasetiquetassleeve se añaden a paths para selección porconciliacióndemetadatos,nosepasanarraysde resultados aPython ni seléeFS/DB. No presentarcohortesmonetariasdesupl/originalSTOP si elinputdelanálisis no soportaesas etiquetas; informar cartera/BTCglobalyconteosreconciliados. Esta conciliación no cambiaPNL/fees/MTM ni essegunda reconstrucciónfinanciera.

GateslegacyR8idénticosambasB/C:ΔnetN204>1e-7,+5Mactivos65/Q80full/included,+10net>=N204−1e-7,DDmotor>=−25%.>=30fillsdelsuplporlogsreconciliados. Diversidad adaptadaANTESresultados: Y901/902>=10entradasconcambiorealejecuciónvsN503(contartipo/tiempo/precio,altas/bajas;precios1e-7);Y903>=10salidasemparejadasmodificadasvsN503. Además>=3de5bloques2021..2025(2025parcial)ΔMTMN204positiva yΔnettrasdescontarmejormesincrementalpositivo. Filtrosoperativos,noconfianzaestadística niOOS. Rankingúnicoparalas13recetas,mismo mínimoM/Q,mínΔ+10,peorDD,IDlex;sinbononovedad. Si ningunaelegible,ceroextras.

## QA y trazabilidad

Fuentes23métodosprotegidos salvo los puntos declaradosdeejecución/metadata/ramasuple,posiciónriesgo/smartorder/cancelación/expiry/rearm/costos/qtyround/reset/clocks/deadlinevalidos;fixturesnogarantizanlifecycle. LeerfuentesporMCP,revisiónrootycrossreview,6formularios/18snapshots,datosfinancieros/metadatosreconciliadosantesselección. Sólo2runsYalavezcuandohaya2slotslibres,globalmáximo4; no interferirV/X, nopurgas ni modificacióndereferencias.

## Aclaración terminal anterior a las corridas Y

Los contadores de cierre de estrategia pueden preceder la liquidación forzada del motor al final. Se exige fillslogs=terminalfills=matches y cierresobservados+suplementoscerradosenboundaryreconciliada=fills; es admisiblecierres==fillsya deorigen. Si se usaajusteboundary, esexactamenteelnúmerodepathsdesuplementoclose==finishMs y MTMterminal_reconcilestrue, noestimaciónniimputación. Si loscontadoresincluyenlaclausurafinal,no se suma doble. Elcloseforzado nopruebaliquidez ejecutable fueradelmotor. No cambia hipótesis/precio/riesgo ni fechasY; corrigecriteriometadataalcomportamientoyaconocidodelmotorantesdeYresultados.


## strategies/BTCNovelR901/reports/BTC_R8_Y_FAMILY_RESULTS_20261019.md
SHA256 6f2d700f19e591c4e29e627db31443830eff36dbf371ae5f3990a96f7a1d152a

# BTC R8 creative Y — resultados finales de la familia

## Resultado

Se ejecutaron las tres hipótesis congeladas sobre N503, seis carteras completas B/C. Ninguna modificación económica después de resultados. **Y902 es un hallazgo positivo y queda retenida como candidata prometedora**: mejora neto, regularidad bajo costes y distribución por años. Aún no cumple todos los criterios del contrato congelado para reemplazar N204; un gate pendiente no prueba sobreajuste ni justifica descartarla. N204 sigue referencia; 2026 permaneció cerrado incluso a inspección.

| Receta | Cambio | Neto B USDT | Neto C USDT | Fills suplemento B/C |
|---|---|---:|---:|---:|
|Y901|Retesteo LIMIT al coste A congelado, una barra4h|11046.643830038218|11228.810189574662|33/33|
|Y902|Continuación STOP al mínimo de trigger, una barra4h|13446.23452557522|13680.349170886388|46/46|
|Y903|Salida adversa por readmisión sobre A con presión positiva|10679.172563829175|10898.840239454656|70/70|

- [Y901B](http://localhost:9200/#/backtest/ee4ecf79-a83d-4388-b4de-3f2e44d62fd2) — ee4ecf79-a83d-4388-b4de-3f2e44d62fd2
- [Y901C](http://localhost:9200/#/backtest/fc3f7e80-a6a0-4d61-8bc1-11ef693aac9c) — fc3f7e80-a6a0-4d61-8bc1-11ef693aac9c
- [Y902B](http://localhost:9200/#/backtest/cb305a17-1312-463e-bbf1-c8173dfae22c) — cb305a17-1312-463e-bbf1-c8173dfae22c
- [Y902C](http://localhost:9200/#/backtest/b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff) — b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff
- [Y903B](http://localhost:9200/#/backtest/99393647-2bca-405b-b3f3-6c2b1a0bed33) — 99393647-2bca-405b-b3f3-6c2b1a0bed33
- [Y903C](http://localhost:9200/#/backtest/745952c3-9fef-4c4c-8450-9fe8b6d142ff) — 745952c3-9fef-4c4c-8450-9fe8b6d142ff

## Aprendizajes y límites

Y901 pierde rentabilidad: esperar retesteo redujo fills67→33 frente a N503 y alteró ocupación/reservas. Root concilió33 LIMIT por cartera. No se infiere el valor de las oportunidades no llenadas como si se hubieran operado.

Y902 mejora frente a N204 +389.619610497556/+440.906791039596 USDT y frente a N503 +117.52281275929/+143.446657826983 USDT. Root auditó finanzas y metadatos PASS,46suplementos:45STOP+1MARKET en cada cartera. El motor puede aproximar smartorders a MARKET; se informan tipos reales. +10bpsRT estático neto11477.310426/11594.998628, costes/calendario/años4de5 pasan según root. **Falla B al descontar su mejor mes incremental (enero2022): −19.760578 USDT; C +40.325146.** Ese −19.760578 es la diferencia incremental MTM acumulada del resto del período al retirar el mejor mes, **no una pérdida del escenario2022**. C conserva +40.325146. Este único gate pendiente bloquea el reemplazo bajo el contrato vigente, pero **no descarta Y902 ni demuestra sobreajuste**. Se retiene para estudiar concentración, estabilidad de ejecución y continuidad del mecanismo. La muestra sigue reutilizada y no constituye validación independiente. No se añadieron filtros a enero2022 ni se reajustaron umbrales.

Y903 intervino29veces por cartera y empeoró el neto a pesar de menor DD B. events82,occupied7,fills70,closes70 ambas. Root confirmó **29 salidas emparejadas del suplemento modificadas frente a N503**, misma entrada, superando el gate de diversidad sin contar efectos indirectos de cartera. Finanzas y metadatos auditados PASS;70/70fills MARKET reconciliados por cartera, +10bpsRT estático neto8711.308825975375/8823.544272012321. Prueba central: BTC_R8_Y903_SUPPLEMENT_EXIT_TRACE. Su resultado nominal ya no supera referencia.

Las atribuciones monetarias se limitan a cartera auditada; no se llama original a todo STOP porque Y902 mezcla tipos. Root hace unión bijectiva de logs BTC_EXPLORE_FILL contra paths por tiempo/entry/qty, ratios y terminalcounts; no se copiaron arrays financieros a código.

## Validación y reproducibilidad

QA final745b2036ce3c456c933267f36026baaf: **201PASS**; fixtures fuente/fórmula/clock/expiry/reset/SLTPdeadline/telemetría. PrimerQA200PASS; dos fallos iniciales sólo del harness quedaron corregidos/documentados. No sustituyen validación engine. Fuentes finales3 readbacks exactos,6sesiones finished sin excepción,6formas completas exactas y18snapshots exactos. Contrato10000USDTshared,1%trade/8%agregado,5xisolated,cap4.4,reserva.001,fee.00045lado;PAXG original ySPYB/C conservados. Fechas2020-10-15→2025-12-31 exclusiva; últimos precios2025-12-30. Duraciones:83.37/83.67s Y901,101.29/101.56s Y902,82.08/82.42s Y903. Sin fallos engine, limpieza ni cambios live/globalconfig.

Las seis corridas terminaron y root confirmó sus auditorías financieras y reconciliaciones de metadatos PASS. Matriz global26/26 final: ninguna elegible para reemplazo según contrato congelado. **Y902 se conserva como candidata prometedora**, sin promoción y sin nuevos backtests en esta ronda.


## strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_P_FINAL_20261021.md
SHA256 8f804089b19a1a892498367f55f3c55ac6b4b4104e30a78aa026f0309f4702be

# Tanda P: K1001/N204, cuentas BTC individuales

Dos recetas legacy completas medidas en cuentas BTC individuales, sin candidata. Se resuelve la brecha entre contribuciones de cartera y retorno de una cuenta individual; no se atribuyen a BTC los CAGR de las carteras. K1001 yN204 fallanCAGR30%,M65activosyQ80, aun conPF/DD/mediana/concentración favorables. K37/58=63.7931% no65%; ambos15/20Q=75% no80%. No promoverporcercanía ni subirriesgo,retirarreserva,eliminarcomponentes o cambiarplazos para rescatar.

|Cuenta|N|CAGR neto|PF|DD M1+fills|M+activos|Q+|Mediana mensual|Neto sin2mejores meses|Sharpe diario|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[K1001](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4)|192|26.8148%|1.8489|16.5039%|37/58|15/20|1.1820%|15497.8805|1.4994|
|[N204](http://localhost:9200/#/backtest/ea5e1bd8-3ecd-4762-b03e-1f5d3e76ca61)|222|25.0358%|1.6530|17.8990%|36/60|15/20|1.1131%|13008.2229|1.3792|

## Receta y adaptaciones declaradas

LONG_RUNNER LIMITretsteoDonchian26/EMA20,80/ADX26/RSI52–76,SL2ATRta,BE2.25R/trail4.2ATRconajustesheredados,sinTP/plazo; CORE_SHORT STOPconmacroEMA120ascendente/RSI3<=20,TP1.5ATR,72h; suplementoN204MARKETcohorteVWAP yfallodeavance2R/48h,K1001añadeeficiencia<=1/3ySTOPestructural. Prioridadlong→shortoriginal→suplemento. Setupavanzaocupado; LIMIT/STOPpendientehasta4h,gestiónsólo4h, fill/proteccionesM1.

AislarBTCretira cuotaATRotrasrutas→100%BTC; cuenta/cantidades/funding/M1yúltimodía2025 incluido cambian frente a las anclas de cartera. No réplica idéntica ni ablationcausal de unasola diferencia. Capital10k,riesgo2%stop+fees+reserva.001desizing,6%capadmisiónnovinculanteconunaposición,aislado3x,margen90%confees,lot.001. Reserva.001REDUCEqty,no débito/PnL/slippage aplicado. No variar reserva/lote/capdespués. Feereal.00045porlado taker+fundinghistóricofrozenBTCaplicado/verificado,snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571,proxiesdeclarados,slippage0. Neto sólo después de costosefectivamentemodelados. BTC-USDTBinancePerpetualFutures,[2020-10-15,2026-01-01)UTCdesarrolloobservado;noeconomía2026nueva.

## Ledger y auditoría
[BtcResearchR16LegacyK1001m](http://localhost:9200/#/backtest/94ec00b5-7541-4e9a-b685-a98160e1abd4):brutoprecio28115.585676,fees3176.475399,funding-410.421286,neto24528.688991(245.2869%),capitalfinal34528.688991USDT. DDdiarioframework-15.5129% distintoM1. Ledgerrealpororigen:{"LONG_RUNNER":{"fills":31,"closes":31,"net":10650.419092195123},"CORE_SHORT":{"fills":116,"closes":116,"net":4686.29849188876},"SUPPLEMENT":{"fills":45,"closes":45,"net":9191.971406577974}}. Planes313,fills192,cancelaciones121,eventossuplemento82.

[BtcResearchR16LegacyN2041m](http://localhost:9200/#/backtest/ea5e1bd8-3ecd-4762-b03e-1f5d3e76ca61):brutoprecio25902.273489,fees3518.650568,funding-308.065527,neto22075.557394(220.7556%),capitalfinal32075.557394USDT. DDdiarioframework-16.7707% distintoM1. Ledgerrealpororigen:{"LONG_RUNNER":{"fills":31,"closes":31,"net":10594.666156313726},"CORE_SHORT":{"fills":113,"closes":113,"net":4342.279629642518},"SUPPLEMENT":{"fills":78,"closes":78,"net":7138.611607679111}}. Planes318,fills222,cancelaciones96,eventossuplemento96.

Auditoría0aceae731d224b0585f7fe7ff6ac3d47 succeeded:414registrosentrepolíticasalternativas,noindependientes. Bruto−fees+funding=PNLsum=equityfinal−10000 a<1e−6USDT; fundingconciliado; suma ledger3orígenesconciliadaN/closes/neto. Todoslosorígenespositivosdentrodeambascuentas,noderivartresestrategiasindependientesniquitarelorigenpormétricaretrospectiva. Posicionesfinales0,PRETERMINALno pendiente económicofinal.

Telemetríaexactasegúnconvención:2.741.760marcasM1,63intervalosmensuales/62completos,20Q,invalid0; equitywallet+PnLabierto,DDM1+fillsnoextremosintraminuto; fronterasmensualesUTCpostfunding/predecisiónporfase. Mediana incluyecalendarioinactivo,M65sólomesescompletosactivos. History4hmin241/max11664enambas,compatibleconretencióndecrecimiento. No prueba deigualdadnuméricaconcarteras quenotienenlasmismascondiciones.

## Verificación técnica e intentos

Fuentespadres/R11/R10inmutables;CODES/readbacks/hashesenrecibotécnico. PrimercheckfallóSyntaxErrorenexpresiónVWAPnuevaantesdepruebas,corregido/registado; segundo5962asercionespassconmétodospadreembebidos/featuresartificiales. Checksnoimportanestrategiasrealesnidataobservadanibrokerreal. Auditoríaframeworkreadonlydelcheckoutbindmontado,resguardadaMCP,detectóque docsresumidassimplificaban cancelación: _checkcancela ypuede reevaluarentradasenmismociclo. LazyplanmemoizadoahorapreservarearmadopostTTL/margenliberado,perono tras cierreposición. Replayprocesaminutoexpiryantescancel; verificadaspolíticasdehistoria/taATRscalarúltimas240/EMAseqhistoriacompleta. No editarframework/config ni leerestrategiasporfilesystem,ningúnDockerrestart. Revisiónindependientefinalconforme ymanifiestodeformulariosrealesantesmotores.

Doseconómicascompletadas,0fallos/reemplazos/backteststécnicos. Doschecksprogramáticos,1fallotécnicoy1pass,noeconomíainterna. Desde r9:30económicascompletadas, no30muestrasindependientes;bloqueV1–V6209conservadoseparado. Ppresupuestocerrado,sin nuevosvecinos/ablaciones decomponentes,risk,prioridad,gestiónoplazos. Sinestrés,nuevos2026,live/paper/Pi,instalaciones,reinicios,configglobal. La autorización de contingenciaDockerlocal sólo aplica sifallaMCPdenuevo.

Control de repetición adicional:CROSS_P yaBTCindividual2%/3x/fundingconcapnocional1x,cupo1entrada/día,screen2020-09a2024-01CAGR21.3292%. No estuvo sinfunding ni sinriesgoactual;no nueva economía CROSS ni retirarcappararescatar. No selecciónnuevadefinalistasV5cerradas.

Continuidad:otra pregunta material,protocolo ypresupuestoantesdenuevaprueba;actualmente se contrasta inventario para residualBTC/ETHcontrarian vscontrolprecioBTC, sin estrategias/jobsaprobadosaún. Ningunapromoción ni autorizaciónoperativa/estrés.

## Años y ventanas móviles, descripción

Calculados aritméticamente desde los63intervalos R11 completos delreciboMCP (62mesescompletos para este resumen), usando productos de retornos M1/frontera declarada. Se excluye2020 incompleto de añosanuales;51ventanas12meses solapadas no son independientes ni OOS. No cambian gates/veredictos ni se usan para nuevos filtros.

K1001: añoscompletos={"2021":37.754599469109664,"2022":30.137400778791168,"2023":46.386546735302446,"2024":11.405045108153988,"2025":13.967847464097982};rolling12={"N":51,"positive":46,"min":{"start":"2023-07","finish":"2024-06","return_pct":-7.806699187854072},"max":{"start":"2022-07","finish":"2023-06","return_pct":67.37900185704851}}.

N204: añoscompletos={"2021":37.72403744564716,"2022":27.511781442433957,"2023":42.26544154555545,"2024":10.88869735715441,"2025":11.047192591105404};rolling12={"N":51,"positive":46,"min":{"start":"2023-08","finish":"2024-07","return_pct":-9.240395861709516},"max":{"start":"2022-03","finish":"2023-02","return_pct":69.32315922926566}}.


## strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_J_PROTOCOL_20261021.md
SHA256 7e8e3a57fb5e05609b6d066779dbc02e22ad865c0d6f206f1eb2933718f8b12b

# Tanda J: información ETH para una operativa exclusivamente BTC

## Pregunta y antecedentes
¿Un movimiento excepcional de ETH confirma una entrada definida con BTC antes de que BTC tenga un movimiento igualmente excepcional? ETH se usa únicamente como dato: ninguna posición, asignación o funding ETH. Control BTC define su propia dirección; el tratamiento agrega información externa sin cambiar protección. Esto no es una cartera ni una demostración de causalidad ETH→BTC: shocks comunes y selección de oportunidades siguen siendo explicaciones posibles.

Antecedente OrchLateralRelativeShock1h: OLS96 retornos contemporáneos BTC~ETH, residual2h y confirmación1h, dos patas con beta. Cerrado negativo en ORCHESTRATION_ROUND5_RESULTS_20261018.md; no quitar una pata ni rescatar ese residual. R20PaxgSpyDelayed1h: fixingsNY,20retornosprevios,shockSPY2sigma/PAXGquiet.25sigma y entrada OPUESTA al líder; R20 excluyóBTC. La pregunta J cambia mecanismo a continuación cripto, datos1h continuos y control definido con BTC. No se declara una transferencia exacta o éxito del antecedente.

ETHM1 existente acreditado en ledgerORCH2020-08-15→2026-10-18. No inspeccionar velas antes: el motor valida el tramo2020–25. Ninguna lectura económica2026. No importar datos nuevos por este protocolo; si falta cobertura, registrar limitación y pasar a otra pregunta material sin fabricar datos ni sustituir feeds.

## Reglas previas a economía
Cada cierre1hUTC,26cierres1h completos/consecutivos de BTC yETH, sincronizados.25logretornos poractivo;24anteriores excluyendo actual para desviación muestral sigma(ddof1). Ambas sigma finitas>0 como validez común de datos.

Patrón BTC: abs(rBTC_actual)<=1*sigmaBTC_previa; no exige queBTCestéinmóvil, sólo que su paso sea ordinario frente al shockETH>=2sigma. Dirección=signo de suma de los seis retornos BTC ANTERIORES alactual (r[-7:-1]); suma0=>noentry. UmbralBTC1sigma se fija antes de resultadosJ como escala ordinaria, diferente del .25sigma del antecedentePAXG; no es vecino ensayado ni ajuste por señalesBTCobservadas.

BTC_CONTROL: operar ese patrón. ETH_CONFIRM: mismo patrón y además abs(rETH_actual)>=2*sigmaETH_previa y signoETHactual igual a direcciónBTC. Mismasventanas/historia, BTCdefine direcciónenambos; ninguna OLS/beta/residual ni posiciónopuestaETH. Cada cierre es evento nuevo, consumido siocupado, sincola ni reentradaalmismocierre de salida. No seleccionar lados después de veratribución. Las políticas son anidadas; capital y ocupación hacen que diferencia dePnL nosea un efecto causal aislado del filtro.

MARKETalcloseBTCcerrado; stop2ATR14simpleBTC1h actual congelado, TP2R, liquidación a6h desde opened_at en cierres1h. Horizonte6h expresa propagación próxima, fijado antes de resultado; no ampliar trasfracaso. ProtecciónintrabarM1; terminalmotorconfees. Una posiciónBTCsinpirámides. SizinghelperR10feeaware2%/margen90%/floor8;gaps/fundingpuedensuperarpérdidaprevista.

## Contrato y gates
BTC-USDT Binance Perpetual Futures ruta1m observador, datosBTC1h yETH1h;warmup2401h. [2020-10-15,2026-01-01)UTC, desarrolloampliamenteobservado,noOOS. 10k,2%portrade/6%agregado/3xaislado,fee.00045porlado,fundinghistóricoBTC ON/aplicado/verificado snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 conproxiesdeclarados;slippage0. Sinestres/variantesriesgo/2026nuevo/ML/live/paper/Pi/configglobal. Ningúnhorariobursátil: BTC yETHcontinuos24/7,noheredarfijaciónNY dePAXGSPY.

ObservadorR11 wallet+PnLabiertoM1yfills, fronteras00:00UTCpostfunding/predecisiónporfase, no agrupaciónestricta de eventos por mes; DDM1noextremotick. Gates:CAGR>=30%,PF>=1.2,DD<=25%(objetivo20%),M65activos,Q80completos,mediana mensual calendario>0incluyendoinactivos,netoquitando2mejoresmeses>0,N100preliminarsinconfianzaporelconteo. Aspiraciones40–50%+/M70. Ganaralcontrolno basta; cada política porseparado. NO_CUMPLEsi falla economía;INCONCLUSAsieconomíafavorable yfaltamuestra/medición. Estrés sólo tras candidata/acuerdo,base noautoriza operar.

## Presupuesto y cierre
Dos corridas económicas continuas, una porpolítica; hastadosreemplazos sólo técnicos documentados, no porPnL. Máximo2motoresglobales y1análisispropio. AST/checks sintéticos de26cierres/24sigmaanteriores/6BTCprevios/sinactualendirección,espejo/control/filtroETH/ceros,asof/gaps/horas/sizing antes de economía;revisiónseparada yreadback/hash/configenmanifiesto. Auditoría posterior completa bruto−fees+funding=PNLsum=equityfinal−10k a1e−6;M1yfronteras/mesesreconciliados. ReportesMCP yHubíndiceúltimo. No barrer .25/.5/1/2sigmas, horas olookbacks alfallar;cerrar ycontinuar autónomamente otra pregunta material.


## strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_J_FINAL_20261021.md
SHA256 904784346d1287cb21f5745303555ed3c7d16d265715203bb18d05dcd3c5ddcf

# Tanda J cerrada: confirmación ETH frente a control BTC

Las dos políticas pierden y no cumplen los objetivos. ETH se usó sólo como información: todas las posiciones, comisiones y funding fueron BTC. La reducción de actividad mejoró el resultado relativo del tratamiento, sin generar rentabilidad ni acreditar causalidad ETH→BTC.

## Reglas y contrato

La dirección se definió con seis retornos BTC previos. BTC actual debía moverse dentro de una desviación previa; ETH_CONFIRM agregaba un shock ETH de al menos dos desviaciones en esa dirección. El control mantenía el mismo patrón BTC. Entradas horarias; stop2ATR14simple1h, TP2R y vencimiento6h. El umbralBTC1sigma fue declarado antes de ejecutar, diferente del .25sigma del antecedentePAXG. No hubo OLS residual, hedge ni estrategia ETH.

Ventana [2020-10-15,2026-01-01), desarrollo reutilizado, BTC-USDT Binance Perpetual Futures. Capital10k, riesgo2%/6%/3x, fee.00045porlado, funding histórico aplicado con proxies declarados, slippage0. Sin estrés, nueva economía2026 ni importaciones. Motor validó cobertura BTC/ETH sin ventanas inválidas.

| Política | CAGR neto | DD M1 y ejecuciones | PF | Meses activos positivos | Trimestres positivos | N |
|---|---:|---:|---:|---:|---:|---:|
| [BtcResearchR13EthConfirm1m](http://localhost:9200/#/backtest/0e718943-cb4a-4fed-b6a5-55ca1a60192a) | -8.90% | 44.24% | 0.708 | 24/61 | 4/20 | 225 |
| [BtcResearchR13BtcControl1m](http://localhost:9200/#/backtest/3dd41c61-da74-463d-a551-2fa1e618e3d0) | -81.57% | 99.99% | 0.884 | 9/62 | 1/20 | 6808 |

Dashboard: http://localhost:9200/#/backtest/0e718943-cb4a-4fed-b6a5-55ca1a60192a

BtcResearchR13EthConfirm1m: neto-3849.06USDT; bruto de precio-1318.34, fees2375.58, funding-155.13; saldo final6150.94; Sharpe-0.8971. Mediana mensual calendario-0.9073%; neto sin dos mejores meses-4697.44USDT.

Dashboard: http://localhost:9200/#/backtest/3dd41c61-da74-463d-a551-2fa1e618e3d0

BtcResearchR13BtcControl1m: neto-9998.53USDT; bruto de precio2107.80, fees11874.14, funding-232.18; saldo final1.47; Sharpe-2.9721. Mediana mensual calendario-13.0230%; neto sin dos mejores meses-12816.69USDT.

## Qué aprendimos

El control realizó6808 operaciones y terminó con1,47USDT. Su resultado bruto de precio fue positivo, pero no cubrió comisiones y funding. Es un resultado simulado completo, no una cuenta operativa ni un experimento cancelado por pérdidas parciales. ETH_CONFIRM redujo a225 operaciones, pero también perdió antes de fees. No basta reducir rotación para encontrar la ventaja. La diferencia mezcla selección, ocupación y trayectorias de capital; no es efecto causal aislado del inputETH.

Ambas fallan CAGR30, PF1.2, DD25, M65 yQ80, mediana y concentración. Los conteos por sí mismos no aportan confianza estadística. Cerrar las dos recetas y sus vecinos; no elegir long-only, otras sigmas u horas tras observar resultados.

## Auditoría y cierre

Protocolo y manifiesto guardados antes de economía. Check7efe483fb2214f7f8418e49f191211b3 passed; fuenteSHA256aea8fe53975ab2a75efdccc1f254cd15c07299faa3acdeab6466be985f91106a. Revisión independiente sin errores materiales. Análisis a189e8474f5b4e7ea94da9879d22527c completo225/6808trades: bruto−fees+funding=sumaPNL=equityfinal−10k, error<1e−6USDT. Ambas telemetrías tienen2.741.760marcasM1,63intervalos/62meses/20Q; fronteras y contribuciones reconciliadas. DDM1noextremosintraminuto; cortes mensuales postfunding/predecisión según convención por fase R11. Sin posiciones terminales, errores económicos ni reemplazos.

Fuentes: BTC_DISCOVERY_J_PROTOCOL_20261021.md, BTC_DISCOVERY_J_MANIFEST_20261021.json, BTC_DISCOVERY_J_ACCOUNTING_20261021.json y telemetrías. Framework/configglobal intactos; sinpaper/live/Pi. Desde r9 van19corridas cerradas; no son muestras independientes. Objetivo pendiente; continúa investigación autónoma con otra pregunta material.


## strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_Q_PROTOCOL_20261021.md
SHA256 6f21ddc13c369c42cfe510f1dcf5fc53946b6dfc01b2ff94c269735dd9324122

# Tanda Q — desplazamiento BTC relativo a ETH frente a precio BTC

Prerregistro2026-10-21, antes de nuevas fuentes/drafts/economía. Pregunta: ¿normalizar el nivel logBTC por una beta histórica de retornos frenteETH produce una operativa BTC individual de reversión útil, comparada con la misma regla de precio BTC con beta0? Dos recetas cerradas, no quitar la pata de un par existente ni refinar el filtroETH de J.

## Antecedentes y selección

Leídos completos por MCP: OrchLateralRelativeShock1h (parBTC/ETH de dos patas, OLS96retornos1h,shock2h yconfirmación), R40PaxgBetaResidual1h (PAXG/SPY,OLSlogniveles de60fixings,z1.5 ysalida residual), BtcResearchR13ExternalBase1m de J (ETHconfirmación1h deimpulso, BTCdirection). Son antecedentes materiales conservados; no afirmar novedad universal. Q cambia pregunta/variables/horizonte y opera sóloBTC:β de retornos4h previos y desplazamiento de niveles conβcomún a toda referencia; salida fixed independiente del modelo. No deriva PnL BTC de las dos patas antiguas ni suma curvas, no usa desempeño2026para selección. Los datos2020–2025 ya fueron examinados por muchas tandas; Q es desarrollo adaptativo, no OOS ni prueba independiente. P se cerró sin candidata y no se rescata con vecinos.

HashesSHA256 de textos completos:
- BtcResearchR11Base1m: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87
- BtcResearchR10Base4h: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9
- OrchLateralRelativeShock1h: 4a0fb55580b5eda3b5bd954b829860eb15c40fb1b5f592d143d418f11956a610
- R40PaxgBetaResidual1h: f445b96c2b92686228a7976943bf8b4c1ab9ae53b1c77bc8792c6d58f3a8f4f8
- BtcResearchR13ExternalBase1m: aea8fe53975ab2a75efdccc1f254cd15c07299faa3acdeab6466be985f91106a

## Regla exacta causal en T4h

Datos BTC4h yETH4h:242 barras cerradas consecutivas porstream, últimaopen=T-4h, timestampsidénticos; incluir sóloopen+4h<=T. Validez común en AMBOS modelos:242exactas,sync,OHLCfinito/positivo ycoherente,ninguna vela parcial. BTCúltimoclosealineadoconprecioactual. Sin imputación, no preinspección de cobertura. Si faltan datos el motor informa; sin importaciones.

βT=cov(rBTC,rETH)/var(rETH) sobre241closesPREVIOS rows[-242:-1], dando240retornoslog4h. Excluyeamboscurrentclosesdelajuste. Usarcentrado/denominador deOLS equivalentea covarianza/varianza conmisma normalización. Si varETH<=0 o nofinita,βnofinita:commoninvalid,resetestado0/noentrada enAMBOS, incluidoβ0. Sin eps,clipping,regularización,winsorizing ni vetoβnegativa.

Tratamiento RESIDUAL:levels=logBTC−βTlogETH. Control PRICE:levels=logBTC conβmodelo0. En ambos reference=levels[-61:-1],60nivelesPREVIOS;mean/reference,std(ddof1),currentlevel=levels[-1],z=(current−mean)/std. EnRESIDUAL usar EL MISMOβT al recalcular toda referencia ycurrent; no mezclar residuosdebetashistóricas. Encontrol la validación/βTETHsigue común aunque no se resteETH. σ<=0/nofinita o z nofinito implicaestado0; no epsilon. Umbral fijo:estado+1(long) si z<=−2;estado−1(short) si z>=2;resto0. No flipdireccióntrasPnL.

Evento nuevo sólo estadoactual no nulo distinto delestadoalmacenado;actualizarestado cada4h,aunocupado/pendiente/sameexit. CambiarβT/μ/σpuedeoriginartransición aunqueBTCquieto: aceptadoahora, no esconderlocomomeanreversioncausalprobada. Gap/commoninvalid reiniciaestado0; recuperacióndatospuede crearun nuevoevento. Estado0porσplana tambiénconsume/reset. Ocupado descartar sincola; noentrada tras salida enmismotimestamp. MARKETBTC alcloseconocido, ceroórdenesETH. Una única posición2%total.

## Gestión, riesgo, costos y medición congelados

Tres fuentes nuevas: BtcResearchR17RelativeBase1m, BtcResearchR17RelativeResidual1m y BtcResearchR17RelativePrice1m. Base hereda observador/fill/gestión/cierre R11 sin cambiarlo. R10 closed_window/atr14/entry_plan sin cambios:ATR14SIMPLE4hBTCactual,stop2ATR/TP2R y48h,gestiónsólocierres4h,proteccionesM1; noTPdinámicoβ,ratio,recovery,refit otradeETH.

RutaBTC-USDT BinancePerpetualFutures1m,dataBTC4h+ETH4h,warmup3004h. Ventana[2020-10-15,2026-01-01)UTC,10k,2%poroperación/6%agregado/3xaislado,fee.00045porlado takerdescuento,fundingBTChistóricoON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 aplicado/verificado/proxydeclarado,slippageaplicado0. SizingR10 feeaware90%margen/floor8 sin reservaextra deP ni cambiosriesgo. Fecha final excluye2026. Sin estrés/riskvariants/nuevosdatos/import/live/paper/Pi/framework/global/install/restarts/scripts.

No claim de cointegración, estacionariedad, par neutral ni arbitraje:BTCsolo puede perder aunqueelratioseacerque, siETHse mueve. βdescriptiva de retornos no garantiza nivel estable ni beneficio después deSL/TP/costos.

R11congelado equity=wallet+PnLabierto M1/fills,cortesUTC00postfunding/predecisión porfase,DDM1+eventos sinextremosintraminuto. Logscompactos de fill incluyen beta ajustada/modelo,μ/σ/z/n ysentido; fillsrealizados separados deeventosdescartados. Resumen final acompañaR11 sin milloneslíneasM1.

## Presupuesto y puertas

Exact2económicas RESIDUAL/PRICE; hasta2reemplazos sólo técnicosdocumentados, nunca porPnL. No barrer242/240/60/2/βclip/plazo/direccióntrasresultado. Una misma validez/muestreoexógeno paraambas, pero sus estados/ocupación pueden diferir. Si PRICEfalla no prueba queETHmejora; comparar diferenciasdescriptivas con dependencia/selecciónreconocidas y exigir cada cuenta susgates.

Gatesr9: CAGRnetobase>=30%,PF>=1.2,DD<=25%(objetivo20%),M65activospositivos,Q80completos,medianaretornomensualcalendario>0 incluidosinactivos,netoaritmético quitandomejores2meses>0,N>=100preliminar no confianza/potencia porconteo. Aspiraciones40–50%+/M70 no sustituyengates. NO_CUMPLEalfallareconomía,INCONCLUSA si favorableconmediciónfaltante. No OOSreclamado.

Antes de economía:readback/hashfuentesnuevas/deps ychecks temporales supplied-sourceAST, sin importingestrategiasreales/framework ni datosobservados. Cubrir242/241/240/60índices,betaexcluyecurrentambos,oráculocov/var,βnegativapermitida,commonvalidETHenPRICE,normalizaciónmismaβenreference/current,σ0noeps,signos±2/transiciones/refit/gaps/sync/futuros,advanceocupado/noqueue,sameexit,ATR/risk/SLTP48hheredados. Guardarcódigo/resultados/errores yCODES completos. Sinbacktestdesdeanalysis. Root revisa fuentes y manifiesto genuino/drafts/preflight antes motor. Después auditoría completa gross−fees+funding=PNLsum=equityfinal−10k1e-6USDT,2.741.760marcasM1,63intervalos/62meses/20Q yterminalfee. Hubinmutable archivosprimero/índiceúltimo. Si falla,cerrar presupuesto y otra pregunta material sin retocarQ.

## Límite numérico preeconómico

La implementación usa directamente logBTC−βTlogETH y std(ddof1) declarados, sin epsilon económico. En relación proporcional perfecta, logaritmos/OLS y resta pueden producir sigma residual positiva casi0 por redondeo en lugar de0 matemático; se aplica literalmente el z/umbral resultante si sigma>0, yestado0 si sigma<=0/no finita. Esto puede producir eventos sensibles al redondeo en casos degenerados; no se interpreta como ventaja ni cointegración. El check incluye caso proporcional con diagnóstico explícito, además de invariancia de unidadesBTC/ETH en caso no degenerado. No se observó mercado para elegir estabilización o tolerancia. La alternativa de centrar algebraicamente no se añade después de resultados.


## strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_Q_FINAL_20261021.md
SHA256 50eea56a0a6eb1c9197a58dc7d5b1a27011bf22f422f321bb43a55688dbc707e

# Q: desplazamiento relativo BTC/ETH, cierre

Ambas políticas pierden yningunacumpleobjetivos. RESIDUALmejorarelativamente aPRICEenCAGR/PF,pero no seafirmaedge validada/superioridadindependiente. FallanCAGR30%,PF1.2,DD25%,M65,Q80,medianapositiva yconcentración aritmética. No retirarshorts,invertirregla,z,beta,ventanas,TPoplazopararescate. PresupuestoQcerrado.

|ModeloBTCsolo|N|CAGRneto|PF|DDM1+fills|M+activos|Q+|Mediana mensual|Neto sin2mejores|Sharpe diario|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[residual](http://localhost:9200/#/backtest/e73bf5e8-688e-4c5f-9ef9-d54f135b3329)|319|-8.3625%|0.8646|54.6898%|24/62|8/20|-1.4710%|-5843.2633|-0.4808|
|[price](http://localhost:9200/#/backtest/dd092c9a-f668-412f-aca7-b73ecf1cb76b)|312|-12.7061%|0.7761|54.5700%|22/62|6/20|-1.2504%|-6436.6213|-0.8049|

## Contraste y contrato

242barras4hBTC/ETHsincronizadas;βOLS240retornosPREVIOSexclactual,60lognivelespreviosyactualbajoMISMOβT. RESIDUALlogBTC−βlogETH,PRICEβ0. VarETHpositivafinita/sharedvalidityparaambos;βnegpermitido,sinclip/epsilon;σ<=0neutral. z<=−2long/z>=2short,freshstateavanzaaunocupado,refitpuedetransicionar. NoETHorders,nocointegraciónni neutralidaddecarteraacreditadas; una recuperación de ratio porETHno garantizagananciaBTC. No rescatarparlegacyquitandopataETHnifiltrarJdenuevo.

GestiónR11/R10frozen:unaposición2%feeaware,6%capnovinculante,3xaislado,margen90%floor8;SL2ATR14simple4h/TP2R/48hgestión4h,proteccionesM1.10k,BTC-USDTBinancePerpetualFutures,ruta1m/datosBTC4hETH4h,warmup300;[2020-10-15,2026-01-01)UTCdesarrolloobservado. Fee.00045porlado takerdescuento,fundingBTCdatasetfrozen9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571aplicado/verificado,marksproxydeclaradas,slippage0. Neto trasfees/fundingmodelados,no todoscostosreales. SinfundingETHporqueETHnooperó.

## Cuentas y calendario
[BtcResearchR17RelativeResidual1m](http://localhost:9200/#/backtest/e73bf5e8-688e-4c5f-9ef9-d54f135b3329):bruto-1824.640484,fee1803.336986,funding-31.039806,neto-3659.017276(-36.5902%),capitalfinal6340.982724USDT. DDdiarioframework-54.1618% distintoM1. Stats{"stage":"FINAL","mode":"RESIDUAL","long_fills":144,"short_fills":175,"signals":452,"occupied":133}. AñoscompletosdesdeM1mensual{"2021":9.77927073437872,"2022":27.990403894111427,"2023":-28.642193744798373,"2024":-23.34925698029996,"2025":-8.94588687871558};rolling12{"N":51,"positive":22,"min":{"start":"2023-11","finish":"2024-10","return_pct":-36.220949261646},"max":{"start":"2021-11","finish":"2022-10","return_pct":38.016726103780044}}.

[BtcResearchR17RelativePrice1m](http://localhost:9200/#/backtest/dd092c9a-f668-412f-aca7-b73ecf1cb76b):bruto-4001.107926,fee1365.602994,funding288.773547,neto-5077.937373(-50.7794%),capitalfinal4922.062627USDT. DDdiarioframework-53.5384% distintoM1. Stats{"stage":"PRETERMINAL","mode":"PRICE","long_fills":144,"short_fills":168,"signals":400,"occupied":88}. AñoscompletosdesdeM1mensual{"2021":-2.8059636410820876,"2022":-11.668302440882329,"2023":-1.113060755528894,"2024":-17.86436776885797,"2025":-21.402335504990212};rolling12{"N":51,"positive":10,"min":{"start":"2023-10","finish":"2024-09","return_pct":-28.278348351408933},"max":{"start":"2021-06","finish":"2022-05","return_pct":6.609939306708412}}.

Calendario descriptivo calculado aritméticamente deintervalosR11completosMCP;2020incompletono entra en añocompleto,51ventanas12mesessolapadasno independientes ni OOS. Resultadosporladoexplicanledger,noseusanpararetirarshorts.

## Verificación y límites

Auditoríaa55de9597b6e4e61a6f0b1a1f40ae29dsucceeded;631registrosdepolíticasalternativasnoindependientes. Fullsnapshotsgross−fees+funding=PnL=equityfinal−10000 error<1e−6USDT,fundingconciliado. Telemetríavalidada2.741.760marcasM1,63intervalos/62meses/20Q,invalid0entimestampsBTCyETH,fillcounts319y312igualesmetrics;monthlytelescopingcuadra. RESIDUALFINALpostliquidaciónterminalfeeincluida;rawopen1esmetadataPRE,no pendiente económico. PRICEPREsinposiciónterminal.

DDwallet+PnLabiertoM1/fillsno todosextremosintraminuto; cortesUTCpostfunding/predecisiónporfase,no agrupaciónestrictaeventosfecha. Mediana calendarioconinactivos,M65activoscompletos; N>=100preliminaroperativo,nopotencia/confianza.

Doschecksintéticosexitosos(99y108assertions),0errores,CODES8readbacksidénticos,root+indepreviewconformes,protocolo/manifiestoantes2motores. ExtensiónreescalaBTC/ETH ydiagnósticoproporciónperfectaδσ2.239e−16/z.9916neutral, sin cambiarfuenteeconómicaniañadirepsilon. Noclaimderobustezeconómicaporcheckmatemático. Dosbacktestseconómicoscompletados,0fallos/reemplazos/backteststécnicos. TotalA–Qdesde r9:32económicas,noindependientes;V1–V6209separadas.

No estrés/riskvariants,nuevos2026/live/paper/Pi/framework/global/install/restarts/scripts. ContinuidadR: pregunta distinta deformasmultibarra/kNNNumPymínimoconcontrolmediaglobal,protocolo/checkenpreparación,no economíaaún. R20PAXGanálogosnegativoyM/G/Angleestadospreservados, nonewfamilyclaim. No promociónoperativani estrésautomático.


# Prepared U implementation texts before creation / economics

## BtcResearchR21ExternalClockBase1m
SHA256 85d6827a13c24379349e22c0bf6654ccf9912efc0f6d4a8c3248ddc99f2ce3a2

```python
import math
import numpy as np
import jesse.indicators as ta

from strategies.BtcResearchR16LegacyBase1m import BtcResearchR16LegacyBase1m, legacy_history
from strategies.BtcResearchR10Base4h import BAR

MINUTE = 60000


def external_clock_context(btc_minutes, eth_minutes, now, btc_close):
    """Both past M1 windows/cutoffs share validity; ETH sets time only."""
    start = now - BAR
    windows = []
    for raw in (btc_minutes, eth_minutes):
        if raw.ndim != 2 or raw.shape[1] < 6:
            return None, "shape"
        rows = raw[(raw[:, 0] >= start) & (raw[:, 0] < now)]
        if (len(rows) != 240
                or not np.array_equal(rows[:, 0], start + np.arange(240) * MINUTE)):
            return None, "clock"
        if (not np.all(np.isfinite(rows[:, :6]))
                or not np.all(rows[:, 1:5] > 0) or np.any(rows[:, 5] < 0)
                or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2]))
                or np.any(np.maximum(rows[:, 1], rows[:, 2]) > rows[:, 3])):
            return None, "ohlcv"
        windows.append(rows)
    btc, eth = windows
    if float(btc[-1, 2]) != float(btc_close):
        return None, "btc_close"
    cutoffs, fractions = [], []
    for rows in windows:
        # Preserve X805 raw arithmetic, including side='left' at exact half.
        # Normalization is conceptual; near-half floating sums need not scale
        # identically and are never repaired with an economic epsilon.
        volume = rows[:, 5]
        with np.errstate(over="ignore", invalid="ignore"):
            total = float(np.sum(volume))
            cumulative = np.cumsum(volume)
        if not math.isfinite(total) or total <= 0 or not np.all(np.isfinite(cumulative)):
            return None, "total"
        cutoff = int(np.searchsorted(cumulative, .5 * total, side="left"))
        if not 0 <= cutoff < 239:
            return None, "empty_partition"
        cutoffs.append(cutoff)
        fractions.append(float(cumulative[cutoff] / total))
    contexts = []
    for cutoff in cutoffs:
        first, second = btc[:cutoff+1], btc[cutoff+1:]
        # ETH second-group volume is allowed to be zero. Only BTC weights price.
        costs = []
        for group in (first, second):
            with np.errstate(over="ignore", invalid="ignore"):
                weight = float(np.sum(group[:, 5]))
                typical = np.mean(group[:, [3, 4, 2]], axis=1)
                products = typical * group[:, 5]
                weighted = float(np.sum(products))
            if (not math.isfinite(weight) or weight <= 0
                    or not np.all(np.isfinite(typical))
                    or not np.all(np.isfinite(products)) or not math.isfinite(weighted)):
                return None, "btc_weight_or_cost"
            cost = weighted / weight
            if not math.isfinite(cost) or cost <= 0:
                return None, "btc_cost"
            costs.append(cost)
        contexts.append(dict(cutoff=cutoff, time=int(btc[cutoff, 0]),
                             first_cost=costs[0], second_cost=costs[1],
                             first_low=float(np.min(first[:, 4]))))
    return dict(start=int(start), finish=int(now), btc=contexts[0], eth=contexts[1],
                btc_first_fraction=fractions[0], eth_first_fraction=fractions[1]), None


def clock_setups(c, context):
    """The ORIGINAL short-only X805 setup, differing only at chosen boundary."""
    w = c[-14:]
    if (context is None or len(w) != 14 or not np.all(np.isfinite(w))
            or not np.all(w[:, 1:] > 0) or not np.all(w[:, 3] >= w[:, 4])):
        return None
    s, t = c[-2], c[-1]
    base = bool(s[2] > c[-14, 2] and t[2] < t[1])
    values = {}
    for key in ("btc", "eth"):
        part = context[key]
        values[key] = bool(base and part["second_cost"] < part["first_cost"]
                           and t[2] < part["first_low"])
    return dict(base=base, **values)


def clock_supplement_event(c, context):
    """Called only AFTER selected full setup has consumed its false->true latch."""
    atr = float(ta.atr(c))  # Real legacy Wilder14/default with exposed history.
    if not math.isfinite(atr) or atr <= 0:
        return None
    s, t = c[-2], c[-1]
    distance = float(max(s[3], t[3]) + .25 * atr - t[2])
    if not atr <= distance <= 3 * atr:
        return None
    entry = float(t[2])
    # Exact physical TP guard, common to both clocks, AFTER latch consumption.
    if not (math.isfinite(distance) and 0 < distance < entry and entry - 2*distance > 0):
        return None
    return dict(origin="SUPPLEMENT", direction=-1, entry=entry, distance=distance,
                target_distance=2*distance, hold_hours=48, order_kind="MARKET",
                clock_evidence=context)


class BtcResearchR21ExternalClockBase1m(BtcResearchR16LegacyBase1m):
    MODE = "abstract"

    def _clock_count(self, label, value=1):
        if self.START < int(self.time) < self.FINISH:
            counts = self.vars.setdefault("clock_counts", {})
            counts[label] = counts.get(label, 0) + value

    def _clock_invalid(self, reason):
        self.vars["previous_setup"] = False
        self.vars["supplement_event"] = None
        self._clock_count("invalid:" + reason)

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("BTC_CLOCK", "ETH_CLOCK")
            self.vars["checked"] = True
            self._log("R21_CLOCK_CONFIG", dict(mode=self.MODE, fraction=.5,
                      minutes=240, original_setup="X805", branches=3,
                      risk=.02, aggregate=.06, leverage=3, fee=.00045,
                      reserve=.001, lot=.001))
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        self.vars["decision_at"] = now
        self.vars["supplement_event"] = None
        rows = legacy_history(self.get_candles(self.exchange, self.symbol, "4h"), now)
        self.vars["legacy_rows"] = rows
        if rows is None:
            self.vars["previous_setup"] = False
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self._clock_count("btc4h_invalid")
            return
        self.vars["history_min"] = min(self.vars.get("history_min", len(rows)), len(rows))
        self.vars["history_max"] = max(self.vars.get("history_max", len(rows)), len(rows))
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        self._clock_count("btc4h_valid")
        if self.is_open or self.entry_orders:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
        context, reason = external_clock_context(
            self.get_candles(self.exchange, self.symbol, "1m"),
            self.get_candles(self.exchange, "ETH-USDT", "1m"), now, float(rows[-1, 2]))
        if context is None:
            # Missing external data suppresses ONLY supplement, never original
            # core/runner candidates or their valid BTC history/trailing.
            self._clock_invalid(reason)
            return
        self._clock_count("input_valid")
        self._clock_count("same_cut", int(context["btc"]["cutoff"] == context["eth"]["cutoff"]))
        self._clock_count("cut_distance_sum", abs(context["btc"]["cutoff"]-context["eth"]["cutoff"]))
        self._clock_count("btc_cut_sum", context["btc"]["cutoff"])
        self._clock_count("eth_cut_sum", context["eth"]["cutoff"])
        self._clock_count("btc_first_fraction_sum", context["btc_first_fraction"])
        self._clock_count("eth_first_fraction_sum", context["eth_first_fraction"])
        setups = clock_setups(rows, context)
        if setups is None:
            self._clock_invalid("supplement4h")
            return
        self._clock_count("base", int(setups["base"]))
        self._clock_count("btc_setup", int(setups["btc"]))
        self._clock_count("eth_setup", int(setups["eth"]))
        self._clock_count("disagreement", int(setups["btc"] != setups["eth"]))
        if self.is_open or self.entry_orders:
            self._clock_count("occupied_disagreement", int(setups["btc"] != setups["eth"]))
        chosen = "eth" if self.MODE == "ETH_CLOCK" else "btc"
        setup = setups[chosen]
        previous = self.vars.get("previous_setup", False)
        # Update full setup BEFORE taATR, geometry, monetary and occupation gates.
        self.vars["previous_setup"] = setup
        if not setup or previous:
            return
        self._clock_count("selected_transition")
        evidence = dict(context, chosen=chosen, setup_btc=setups["btc"], setup_eth=setups["eth"])
        event = clock_supplement_event(rows, evidence)
        if event is None:
            self._clock_count("geometry_or_physical_rejection")
            return
        self.vars["supplement_event"] = event
        self.vars["supplement_events"] = self.vars.get("supplement_events", 0)+1
        self._clock_count("event")

    def on_open_position(self, order):
        super().on_open_position(order)
        plan = self.vars["position_plan"]
        if plan["origin"] == "SUPPLEMENT":
            self._log("R21_CLOCK_OPEN", dict(mode=self.MODE, time=int(self.time),
                      evidence=plan["clock_evidence"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R21_CLOCK_STATS", dict(stage=stage, mode=self.MODE,
                  counts=self.vars.get("clock_counts", {})))
```

## BtcResearchR21BtcClock1m
SHA256 a46e3a9e286bcad0887e828bcdadd3cf5733617081c742b65358cda8566ea3a0

```python
from strategies.BtcResearchR21ExternalClockBase1m import BtcResearchR21ExternalClockBase1m


class BtcResearchR21BtcClock1m(BtcResearchR21ExternalClockBase1m):
    MODE = "BTC_CLOCK"
```

## BtcResearchR21EthClock1m
SHA256 2d548c234aaa72bea131718d2364e82eab1fe660b729b4accfacd4d249cd8846

```python
from strategies.BtcResearchR21ExternalClockBase1m import BtcResearchR21ExternalClockBase1m


class BtcResearchR21EthClock1m(BtcResearchR21ExternalClockBase1m):
    MODE = "ETH_CLOCK"
```

# Pre-check performance correction (no job launched yet)

Root reviewed three sources and requested binary range extraction over sorted runtime M1 timestamps, retaining exact240/clock validity. No alpha/parameter change. The preceding base is preserved as initial source; CURRENT base below supersedes it. Wrappers and all parents unchanged. Check must include mask-oracle parity and sorted prefixes/future rows.

## BtcResearchR21ExternalClockBase1m CURRENT
SHA256 2174f87c436d513dc71acd01f906f7f933df4fff7ab79bd1cb7a9527085d696f

```python
import math
import numpy as np
import jesse.indicators as ta

from strategies.BtcResearchR16LegacyBase1m import BtcResearchR16LegacyBase1m, legacy_history
from strategies.BtcResearchR10Base4h import BAR

MINUTE = 60000


def external_clock_context(btc_minutes, eth_minutes, now, btc_close):
    """Both past M1 windows/cutoffs share validity; ETH sets time only."""
    start = now - BAR
    windows = []
    for raw in (btc_minutes, eth_minutes):
        if raw.ndim != 2 or raw.shape[1] < 6:
            return None, "shape"
        # Runtime M1 timestamps are sorted (P framework audit). Binary bounds\n        # avoid scanning/copying a growing multi-year history for each decision.\n        times = raw[:, 0]\n        left = int(np.searchsorted(times, start, side="left"))\n        right = int(np.searchsorted(times, now, side="left"))\n        rows = raw[left:right]
        if (len(rows) != 240
                or not np.array_equal(rows[:, 0], start + np.arange(240) * MINUTE)):
            return None, "clock"
        if (not np.all(np.isfinite(rows[:, :6]))
                or not np.all(rows[:, 1:5] > 0) or np.any(rows[:, 5] < 0)
                or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2]))
                or np.any(np.maximum(rows[:, 1], rows[:, 2]) > rows[:, 3])):
            return None, "ohlcv"
        windows.append(rows)
    btc, eth = windows
    if float(btc[-1, 2]) != float(btc_close):
        return None, "btc_close"
    cutoffs, fractions = [], []
    for rows in windows:
        # Preserve X805 raw arithmetic, including side='left' at exact half.
        # Normalization is conceptual; near-half floating sums need not scale
        # identically and are never repaired with an economic epsilon.
        volume = rows[:, 5]
        with np.errstate(over="ignore", invalid="ignore"):
            total = float(np.sum(volume))
            cumulative = np.cumsum(volume)
        if not math.isfinite(total) or total <= 0 or not np.all(np.isfinite(cumulative)):
            return None, "total"
        cutoff = int(np.searchsorted(cumulative, .5 * total, side="left"))
        if not 0 <= cutoff < 239:
            return None, "empty_partition"
        cutoffs.append(cutoff)
        fractions.append(float(cumulative[cutoff] / total))
    contexts = []
    for cutoff in cutoffs:
        first, second = btc[:cutoff+1], btc[cutoff+1:]
        # ETH second-group volume is allowed to be zero. Only BTC weights price.
        costs = []
        for group in (first, second):
            with np.errstate(over="ignore", invalid="ignore"):
                weight = float(np.sum(group[:, 5]))
                typical = np.mean(group[:, [3, 4, 2]], axis=1)
                products = typical * group[:, 5]
                weighted = float(np.sum(products))
            if (not math.isfinite(weight) or weight <= 0
                    or not np.all(np.isfinite(typical))
                    or not np.all(np.isfinite(products)) or not math.isfinite(weighted)):
                return None, "btc_weight_or_cost"
            cost = weighted / weight
            if not math.isfinite(cost) or cost <= 0:
                return None, "btc_cost"
            costs.append(cost)
        contexts.append(dict(cutoff=cutoff, time=int(btc[cutoff, 0]),
                             first_cost=costs[0], second_cost=costs[1],
                             first_low=float(np.min(first[:, 4]))))
    return dict(start=int(start), finish=int(now), btc=contexts[0], eth=contexts[1],
                btc_first_fraction=fractions[0], eth_first_fraction=fractions[1]), None


def clock_setups(c, context):
    """The ORIGINAL short-only X805 setup, differing only at chosen boundary."""
    w = c[-14:]
    if (context is None or len(w) != 14 or not np.all(np.isfinite(w))
            or not np.all(w[:, 1:] > 0) or not np.all(w[:, 3] >= w[:, 4])):
        return None
    s, t = c[-2], c[-1]
    base = bool(s[2] > c[-14, 2] and t[2] < t[1])
    values = {}
    for key in ("btc", "eth"):
        part = context[key]
        values[key] = bool(base and part["second_cost"] < part["first_cost"]
                           and t[2] < part["first_low"])
    return dict(base=base, **values)


def clock_supplement_event(c, context):
    """Called only AFTER selected full setup has consumed its false->true latch."""
    atr = float(ta.atr(c))  # Real legacy Wilder14/default with exposed history.
    if not math.isfinite(atr) or atr <= 0:
        return None
    s, t = c[-2], c[-1]
    distance = float(max(s[3], t[3]) + .25 * atr - t[2])
    if not atr <= distance <= 3 * atr:
        return None
    entry = float(t[2])
    # Exact physical TP guard, common to both clocks, AFTER latch consumption.
    if not (math.isfinite(distance) and 0 < distance < entry and entry - 2*distance > 0):
        return None
    return dict(origin="SUPPLEMENT", direction=-1, entry=entry, distance=distance,
                target_distance=2*distance, hold_hours=48, order_kind="MARKET",
                clock_evidence=context)


class BtcResearchR21ExternalClockBase1m(BtcResearchR16LegacyBase1m):
    MODE = "abstract"

    def _clock_count(self, label, value=1):
        if self.START < int(self.time) < self.FINISH:
            counts = self.vars.setdefault("clock_counts", {})
            counts[label] = counts.get(label, 0) + value

    def _clock_invalid(self, reason):
        self.vars["previous_setup"] = False
        self.vars["supplement_event"] = None
        self._clock_count("invalid:" + reason)

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("BTC_CLOCK", "ETH_CLOCK")
            self.vars["checked"] = True
            self._log("R21_CLOCK_CONFIG", dict(mode=self.MODE, fraction=.5,
                      minutes=240, original_setup="X805", branches=3,
                      risk=.02, aggregate=.06, leverage=3, fee=.00045,
                      reserve=.001, lot=.001))
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        self.vars["decision_at"] = now
        self.vars["supplement_event"] = None
        rows = legacy_history(self.get_candles(self.exchange, self.symbol, "4h"), now)
        self.vars["legacy_rows"] = rows
        if rows is None:
            self.vars["previous_setup"] = False
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self._clock_count("btc4h_invalid")
            return
        self.vars["history_min"] = min(self.vars.get("history_min", len(rows)), len(rows))
        self.vars["history_max"] = max(self.vars.get("history_max", len(rows)), len(rows))
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        self._clock_count("btc4h_valid")
        if self.is_open or self.entry_orders:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
        context, reason = external_clock_context(
            self.get_candles(self.exchange, self.symbol, "1m"),
            self.get_candles(self.exchange, "ETH-USDT", "1m"), now, float(rows[-1, 2]))
        if context is None:
            # Missing external data suppresses ONLY supplement, never original
            # core/runner candidates or their valid BTC history/trailing.
            self._clock_invalid(reason)
            return
        self._clock_count("input_valid")
        self._clock_count("same_cut", int(context["btc"]["cutoff"] == context["eth"]["cutoff"]))
        self._clock_count("cut_distance_sum", abs(context["btc"]["cutoff"]-context["eth"]["cutoff"]))
        self._clock_count("btc_cut_sum", context["btc"]["cutoff"])
        self._clock_count("eth_cut_sum", context["eth"]["cutoff"])
        self._clock_count("btc_first_fraction_sum", context["btc_first_fraction"])
        self._clock_count("eth_first_fraction_sum", context["eth_first_fraction"])
        setups = clock_setups(rows, context)
        if setups is None:
            self._clock_invalid("supplement4h")
            return
        self._clock_count("base", int(setups["base"]))
        self._clock_count("btc_setup", int(setups["btc"]))
        self._clock_count("eth_setup", int(setups["eth"]))
        self._clock_count("disagreement", int(setups["btc"] != setups["eth"]))
        if self.is_open or self.entry_orders:
            self._clock_count("occupied_disagreement", int(setups["btc"] != setups["eth"]))
        chosen = "eth" if self.MODE == "ETH_CLOCK" else "btc"
        setup = setups[chosen]
        previous = self.vars.get("previous_setup", False)
        # Update full setup BEFORE taATR, geometry, monetary and occupation gates.
        self.vars["previous_setup"] = setup
        if not setup or previous:
            return
        self._clock_count("selected_transition")
        evidence = dict(context, chosen=chosen, setup_btc=setups["btc"], setup_eth=setups["eth"])
        event = clock_supplement_event(rows, evidence)
        if event is None:
            self._clock_count("geometry_or_physical_rejection")
            return
        self.vars["supplement_event"] = event
        self.vars["supplement_events"] = self.vars.get("supplement_events", 0)+1
        self._clock_count("event")

    def on_open_position(self, order):
        super().on_open_position(order)
        plan = self.vars["position_plan"]
        if plan["origin"] == "SUPPLEMENT":
            self._log("R21_CLOCK_OPEN", dict(mode=self.MODE, time=int(self.time),
                      evidence=plan["clock_evidence"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R21_CLOCK_STATS", dict(stage=stage, mode=self.MODE,
                  counts=self.vars.get("clock_counts", {})))
```

# Corrected pre-check literal-newline source error

Hash2174f87c436d513dc71acd01f906f7f933df4fff7ab79bd1cb7a9527085d696f is INVALID: the searchsorted replacement accidentally contained literal backslash-n inside the comment, commenting rows extraction. Root/independent review caught it before any check/draft. Replace those sequences with real newlines only; preserve invalid source above, no economic use. CURRENT corrected base follows; wrappers/parents unchanged.

## BtcResearchR21ExternalClockBase1m CURRENT corrected
SHA256 caa81c408d261e5d802203d8fdf4b9926a616ae1def52e174c481450faa75ebc

```python
import math
import numpy as np
import jesse.indicators as ta

from strategies.BtcResearchR16LegacyBase1m import BtcResearchR16LegacyBase1m, legacy_history
from strategies.BtcResearchR10Base4h import BAR

MINUTE = 60000


def external_clock_context(btc_minutes, eth_minutes, now, btc_close):
    """Both past M1 windows/cutoffs share validity; ETH sets time only."""
    start = now - BAR
    windows = []
    for raw in (btc_minutes, eth_minutes):
        if raw.ndim != 2 or raw.shape[1] < 6:
            return None, "shape"
        # Runtime M1 timestamps are sorted (P framework audit). Binary bounds
        # avoid scanning/copying a growing multi-year history for each decision.
        times = raw[:, 0]
        left = int(np.searchsorted(times, start, side="left"))
        right = int(np.searchsorted(times, now, side="left"))
        rows = raw[left:right]
        if (len(rows) != 240
                or not np.array_equal(rows[:, 0], start + np.arange(240) * MINUTE)):
            return None, "clock"
        if (not np.all(np.isfinite(rows[:, :6]))
                or not np.all(rows[:, 1:5] > 0) or np.any(rows[:, 5] < 0)
                or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2]))
                or np.any(np.maximum(rows[:, 1], rows[:, 2]) > rows[:, 3])):
            return None, "ohlcv"
        windows.append(rows)
    btc, eth = windows
    if float(btc[-1, 2]) != float(btc_close):
        return None, "btc_close"
    cutoffs, fractions = [], []
    for rows in windows:
        # Preserve X805 raw arithmetic, including side='left' at exact half.
        # Normalization is conceptual; near-half floating sums need not scale
        # identically and are never repaired with an economic epsilon.
        volume = rows[:, 5]
        with np.errstate(over="ignore", invalid="ignore"):
            total = float(np.sum(volume))
            cumulative = np.cumsum(volume)
        if not math.isfinite(total) or total <= 0 or not np.all(np.isfinite(cumulative)):
            return None, "total"
        cutoff = int(np.searchsorted(cumulative, .5 * total, side="left"))
        if not 0 <= cutoff < 239:
            return None, "empty_partition"
        cutoffs.append(cutoff)
        fractions.append(float(cumulative[cutoff] / total))
    contexts = []
    for cutoff in cutoffs:
        first, second = btc[:cutoff+1], btc[cutoff+1:]
        # ETH second-group volume is allowed to be zero. Only BTC weights price.
        costs = []
        for group in (first, second):
            with np.errstate(over="ignore", invalid="ignore"):
                weight = float(np.sum(group[:, 5]))
                typical = np.mean(group[:, [3, 4, 2]], axis=1)
                products = typical * group[:, 5]
                weighted = float(np.sum(products))
            if (not math.isfinite(weight) or weight <= 0
                    or not np.all(np.isfinite(typical))
                    or not np.all(np.isfinite(products)) or not math.isfinite(weighted)):
                return None, "btc_weight_or_cost"
            cost = weighted / weight
            if not math.isfinite(cost) or cost <= 0:
                return None, "btc_cost"
            costs.append(cost)
        contexts.append(dict(cutoff=cutoff, time=int(btc[cutoff, 0]),
                             first_cost=costs[0], second_cost=costs[1],
                             first_low=float(np.min(first[:, 4]))))
    return dict(start=int(start), finish=int(now), btc=contexts[0], eth=contexts[1],
                btc_first_fraction=fractions[0], eth_first_fraction=fractions[1]), None


def clock_setups(c, context):
    """The ORIGINAL short-only X805 setup, differing only at chosen boundary."""
    w = c[-14:]
    if (context is None or len(w) != 14 or not np.all(np.isfinite(w))
            or not np.all(w[:, 1:] > 0) or not np.all(w[:, 3] >= w[:, 4])):
        return None
    s, t = c[-2], c[-1]
    base = bool(s[2] > c[-14, 2] and t[2] < t[1])
    values = {}
    for key in ("btc", "eth"):
        part = context[key]
        values[key] = bool(base and part["second_cost"] < part["first_cost"]
                           and t[2] < part["first_low"])
    return dict(base=base, **values)


def clock_supplement_event(c, context):
    """Called only AFTER selected full setup has consumed its false->true latch."""
    atr = float(ta.atr(c))  # Real legacy Wilder14/default with exposed history.
    if not math.isfinite(atr) or atr <= 0:
        return None
    s, t = c[-2], c[-1]
    distance = float(max(s[3], t[3]) + .25 * atr - t[2])
    if not atr <= distance <= 3 * atr:
        return None
    entry = float(t[2])
    # Exact physical TP guard, common to both clocks, AFTER latch consumption.
    if not (math.isfinite(distance) and 0 < distance < entry and entry - 2*distance > 0):
        return None
    return dict(origin="SUPPLEMENT", direction=-1, entry=entry, distance=distance,
                target_distance=2*distance, hold_hours=48, order_kind="MARKET",
                clock_evidence=context)


class BtcResearchR21ExternalClockBase1m(BtcResearchR16LegacyBase1m):
    MODE = "abstract"

    def _clock_count(self, label, value=1):
        if self.START < int(self.time) < self.FINISH:
            counts = self.vars.setdefault("clock_counts", {})
            counts[label] = counts.get(label, 0) + value

    def _clock_invalid(self, reason):
        self.vars["previous_setup"] = False
        self.vars["supplement_event"] = None
        self._clock_count("invalid:" + reason)

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("BTC_CLOCK", "ETH_CLOCK")
            self.vars["checked"] = True
            self._log("R21_CLOCK_CONFIG", dict(mode=self.MODE, fraction=.5,
                      minutes=240, original_setup="X805", branches=3,
                      risk=.02, aggregate=.06, leverage=3, fee=.00045,
                      reserve=.001, lot=.001))
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        self.vars["decision_at"] = now
        self.vars["supplement_event"] = None
        rows = legacy_history(self.get_candles(self.exchange, self.symbol, "4h"), now)
        self.vars["legacy_rows"] = rows
        if rows is None:
            self.vars["previous_setup"] = False
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            self._clock_count("btc4h_invalid")
            return
        self.vars["history_min"] = min(self.vars.get("history_min", len(rows)), len(rows))
        self.vars["history_max"] = max(self.vars.get("history_max", len(rows)), len(rows))
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        self._clock_count("btc4h_valid")
        if self.is_open or self.entry_orders:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
        context, reason = external_clock_context(
            self.get_candles(self.exchange, self.symbol, "1m"),
            self.get_candles(self.exchange, "ETH-USDT", "1m"), now, float(rows[-1, 2]))
        if context is None:
            # Missing external data suppresses ONLY supplement, never original
            # core/runner candidates or their valid BTC history/trailing.
            self._clock_invalid(reason)
            return
        self._clock_count("input_valid")
        self._clock_count("same_cut", int(context["btc"]["cutoff"] == context["eth"]["cutoff"]))
        self._clock_count("cut_distance_sum", abs(context["btc"]["cutoff"]-context["eth"]["cutoff"]))
        self._clock_count("btc_cut_sum", context["btc"]["cutoff"])
        self._clock_count("eth_cut_sum", context["eth"]["cutoff"])
        self._clock_count("btc_first_fraction_sum", context["btc_first_fraction"])
        self._clock_count("eth_first_fraction_sum", context["eth_first_fraction"])
        setups = clock_setups(rows, context)
        if setups is None:
            self._clock_invalid("supplement4h")
            return
        self._clock_count("base", int(setups["base"]))
        self._clock_count("btc_setup", int(setups["btc"]))
        self._clock_count("eth_setup", int(setups["eth"]))
        self._clock_count("disagreement", int(setups["btc"] != setups["eth"]))
        if self.is_open or self.entry_orders:
            self._clock_count("occupied_disagreement", int(setups["btc"] != setups["eth"]))
        chosen = "eth" if self.MODE == "ETH_CLOCK" else "btc"
        setup = setups[chosen]
        previous = self.vars.get("previous_setup", False)
        # Update full setup BEFORE taATR, geometry, monetary and occupation gates.
        self.vars["previous_setup"] = setup
        if not setup or previous:
            return
        self._clock_count("selected_transition")
        evidence = dict(context, chosen=chosen, setup_btc=setups["btc"], setup_eth=setups["eth"])
        event = clock_supplement_event(rows, evidence)
        if event is None:
            self._clock_count("geometry_or_physical_rejection")
            return
        self.vars["supplement_event"] = event
        self.vars["supplement_events"] = self.vars.get("supplement_events", 0)+1
        self._clock_count("event")

    def on_open_position(self, order):
        super().on_open_position(order)
        plan = self.vars["position_plan"]
        if plan["origin"] == "SUPPLEMENT":
            self._log("R21_CLOCK_OPEN", dict(mode=self.MODE, time=int(self.time),
                      evidence=plan["clock_evidence"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R21_CLOCK_STATS", dict(stage=stage, mode=self.MODE,
                  counts=self.vars.get("clock_counts", {})))
```
