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


class BtcY902ExploreR1004(Strategy):
    """K1004: frozen R9 single-mechanism experiment from Y902; original routes retained.

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
            # Reset every fill: a prior trade cannot consume or arm the next one.
            self.vars['r9_management_clock'] = None
            self.vars['r9_first_complete_seen'] = False
            self.vars['r9_trail_armed'] = False
            self.vars['r9_signal_anchor'] = float(plan['novel_anchor'])
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
                'requested_entry': float(plan['novel_requested_entry']),
                'signal_anchor': float(plan['novel_anchor']),
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
            self._r9_manage()
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
        jh.debug('BTC_NOVEL ' + json.dumps({'recipe': 'K1004',
            'counts': self.vars.get('novel_audit', {})}, sort_keys=True))
        jh.debug('BTC_EXPLORE ' + json.dumps({'recipe': 'K1004',
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
        entry, distance = float(event['novel_requested_entry']), float(event['distance'])
        # Change only execution price; signal geometry remains frozen from trigger close.
        # Positive TP is a physical constraint, not a searched price-distance cut.
        if not (math.isfinite(entry) and entry > 2 * distance
                and entry < float(self.price)):
            audit = self.vars.setdefault('novel_audit', {})
            audit['invalid_candidate'] = audit.get('invalid_candidate', 0) + 1
            return False
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
        window = c[-13:-1]
        spans = window[:, 3] - window[:, 4]
        q = np.divide(window[:, 5] * (2 * window[:, 2] - window[:, 3] - window[:, 4]),
                      spans, out=np.zeros(12), where=spans > 0)
        cohort = window[q > 0]
        # No positive-pressure cohort means no reference cost and a false setup.
        vwap = (float(np.sum(cohort[:, 5] * np.mean(cohort[:, [3, 4, 2]], axis=1))
                      / np.sum(cohort[:, 5])) if len(cohort) else float('nan'))
        # The positive close-location cohort defines cost; an empty cohort is not a setup.
        # OHLCV pressure is a proxy, not observed taker flow.
        setup = bool(s[2] > c[-14, 2] and np.sum(q) < 0
                     and s[2] >= vwap and t[2] < t[1] and t[2] < vwap
                     and self._research_gate(c, window, q, vwap,
                         int(self.closed_candle_open_time) + 14400000))
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
        self.vars['explore_event'] = {'side': 'short', 'kind': 'K1004',
            'distance': distance, 'target_distance': 2 * distance, 'hold_hours': 48,
            'novel_anchor': float(vwap), 'novel_requested_entry': float(t[4])}
        audit = self.vars.setdefault('explore_audit', {})
        audit['events'] = audit.get('events', 0) + 1
        audit['events_occupied'] = audit.get('events_occupied', 0) + int(self.is_open)

    @staticmethod
    def _research_gate(c, window, q, vwap, decision_close):
        # One third separates a circuitous advance from a direct trend.
        # It is a single broad development cut, not a searched optimum.
        changes = c[-13:-1, 2] - c[-14:-2, 2]
        path = float(np.sum(np.abs(changes)))
        if path <= 0:
            return False
        efficiency = float(c[-2, 2] - c[-14, 2]) / path
        return bool(0 < efficiency <= 1 / 3)

    def _r9_manage(self):
        """Evaluate only complete post-fill bars once; pending orders never call this."""
        c = self._explore_window(2)
        if c is None:
            return
        t = c[-1]
        clock = int(t[0])
        if clock < self.vars['opened_time'] or self.vars.get('r9_management_clock') == clock:
            return
        self.vars['r9_management_clock'] = clock
        audit = self.vars.setdefault('novel_audit', {})
        audit['complete_checks'] = audit.get('complete_checks', 0) + 1
        entry = float(self.position.entry_price)
        span = float(t[3] - t[4])
        pressure = float(t[5] * (2 * t[2] - t[3] - t[4]) / span) if span > 0 else 0.0
        # Transport of Y903: test interaction with continuation entry, not a new signal.
        if (float(t[2]) > self.vars['r9_signal_anchor']
                and pressure > 0 and float(t[2]) > entry):
            audit['management_exits'] = audit.get('management_exits', 0) + 1
            self.liquidate()
