import math
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

# User-approved research limits; risk is not an optimization parameter.
TRADE_RISK = 0.03
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.
SLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.
BAR_MS = 4 * 60 * 60 * 1000  # Preserve the baseline decision and order-lifetime clock.


class AngleCombinedBtcReclaim1m(Strategy):
    """Combined baseline with causal BTC long touch-and-reclaim MARKET execution.

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

    def _closed_btc_4h(self, strategy):
        # Auxiliary snapshots may contain a forming 4h row. Retain every closed
        # historical row, as the original store does; never truncate to warmup.
        raw = strategy.get_candles(strategy.exchange, strategy.symbol, '4h')
        return raw[raw[:, 0] + BAR_MS <= self.time]

    @property
    @cached
    def signal_candles(self):
        if self.symbol == 'BTC-USDT':
            return self._closed_btc_4h(self)
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    def _entry_window(self) -> bool:
        if self.symbol == 'BTC-USDT':
            # The 1m route is an execution clock, not a new signal frequency.
            return self.time % BAR_MS == 0
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
            if route.symbol == 'BTC-USDT':
                # Read raw auxiliary data at the caller's current clock. Another
                # route's @cached property can still belong to its previous step.
                c = self._closed_btc_4h(route.strategy)
            else:
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
        # self.high/low refer to M1 on BTC; the baseline range test remains 4h.
        signal_range = (float(c[-1, 3]) - float(c[-1, 4])
                        if self.symbol == 'BTC-USDT' else self.high - self.low)
        if not (atr > 0 and entry < self.price <= entry + atr and self.price > slow[-1]
                and fast > slow[-1] > slow[-5] and adx >= self.hp['adx_min']
                and 52 <= rsi <= 76 and signal_range <= 3 * atr):
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
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {
            'qty': qty, 'entry': entry, 'distance': distance,
            'risk': qty * unit_risk, 'notional': qty * entry,
        }
        return True

    def before(self) -> None:
        if self.symbol != 'BTC-USDT':
            return
        if self.timeframe != '1m':
            raise AssertionError('BTC reclaim execution requires its reviewed 1m trading route')
        armed = self.vars.get('reclaim_setup')
        if armed is None:
            return
        if self.is_open:
            raise AssertionError('A filled BTC long must release its reclaim setup')
        armed['ready'] = False
        if self.time >= armed['expiry']:
            self.vars.pop('reclaim_setup')
            self._ledger().pop(self._key(), None)
            # Original cancellation consumes this callback; do not arm another
            # 4h signal at exactly the old order's expiration boundary.
            self.vars['reclaim_expired_index'] = self.index
            return
        # This completed minute must belong to the period AFTER setup creation;
        # the setup's own 4h bar cannot retrospectively supply a touch.
        if (self.closed_candle_open_time < armed['setup_time']
                or self.time <= armed['setup_time']):
            return
        boundary = armed['plan']['entry']
        if armed['touch_close'] is None:
            if self.low <= boundary:
                armed['touch_close'] = int(self.time)
            return
        # A later M1 adds the preregistered persistence confirmation and latency;
        # same-minute low/close ordering alone would not require this delay.
        if self.time > armed['touch_close'] and self.price > boundary:
            armed['ready'] = True

    def _reclaim_quantity(self, armed) -> tuple:
        frozen = armed['plan']
        price = float(self.price)
        distance = frozen['distance']
        ledger = self._ledger()
        own = ledger.pop(self._key(), None)
        if own is None:
            raise AssertionError('An armed BTC setup must keep its reservation')
        try:
            # Callbacks are sequential. Excluding only this internal reservation
            # prevents double counting without freeing another route's capital.
            risk, notional = self._committed()
            capital = self._capital()
            budget = min(frozen['risk'], capital * TRADE_RISK,
                         max(0.0, capital * PORTFOLIO_RISK - risk))
            room = min(frozen['notional'],
                       max(0.0, capital * NOTIONAL_CAP - notional))
            margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
            if not math.isfinite(price) or not 0 < distance < price:
                return 0.0, 0.0
            unit_risk = distance + self.fee_rate * (2 * price - distance) + SLIPPAGE_RESERVE * price
            qty = min(frozen['qty'], budget / unit_risk, room / price, margin_room / price)
            # The original BTC research precision is retained. A smaller budget
            # can only reduce quantity; zero leaves the setup alive until expiry.
            qty = math.floor(qty / 0.001) * 0.001
            return qty, unit_risk
        finally:
            ledger[self._key()] = own

    def _signal(self) -> int:
        # Preserve the proven control verbatim on PAXG/SPY and on BTC shorts.
        # An armed BTC long owns priority until its fill or original 4h expiry.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            if self.symbol == 'BTC-USDT':
                self.vars.pop('reclaim_execution', None)
                armed = self.vars.get('reclaim_setup')
                if self.vars.get('reclaim_expired_index') == self.index:
                    self.vars['signal_value'] = 0
                elif armed is not None:
                    self.vars['signal_value'] = 0
                    if armed['ready']:
                        qty, unit_risk = self._reclaim_quantity(armed)
                        # Jesse requires should_long=True to result in an order.
                        # Zero size keeps the reservation and long priority, but
                        # never declares a signal whose go_long would be empty.
                        if qty > 0:
                            self.vars['reclaim_execution'] = {
                                'qty': qty, 'unit_risk': unit_risk,
                                'price': float(self.price), 'timestamp': int(self.time),
                                'index': self.index,
                            }
                            self.vars['signal_value'] = 1
                elif self.time % BAR_MS != 0:
                    self.vars['signal_value'] = 0
                else:
                    if not self.vars.get('clock_warmup_checked'):
                        if len(self.signal_candles) < 240:
                            raise AssertionError('BTC reclaim requires the proven 240 closed 4h warmup rows')
                        self.vars['clock_warmup_checked'] = True
                    if self._plan():
                        frozen = dict(self.vars['plan'])
                        self.vars['reclaim_setup'] = {
                            'plan': frozen, 'setup_time': int(self.time),
                            'expiry': int(self.time) + BAR_MS,
                            'touch_close': None, 'ready': False,
                        }
                        # No broker order exists yet, but other routes must see
                        # the same capital reservation as the original LIMIT.
                        self._ledger()[self._key()] = dict(frozen)
                        self.vars['signal_value'] = 0
                    else:
                        self.vars['signal_value'] = -1 if self._short_plan() else 0
            else:
                self.vars['signal_value'] = 1 if self._plan() else (-1 if self._short_plan() else 0)
        return self.vars['signal_value']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        if self.symbol == 'BTC-USDT':
            armed = self.vars['reclaim_setup']
            if not (armed['ready'] and self.time < armed['expiry']
                    and self.time > armed['touch_close']):
                raise AssertionError('BTC MARKET entry must follow a later reclaim before expiry')
            execution = self.vars.pop('reclaim_execution')
            if not (execution['qty'] > 0 and execution['unit_risk'] > 0
                    and execution['timestamp'] == int(self.time)
                    and execution['index'] == self.index
                    and execution['price'] == float(self.price)):
                raise AssertionError('BTC MARKET execution must consume a positive same-callback quote plan')
            qty, unit_risk = execution['qty'], execution['unit_risk']
            price = execution['price']
            frozen = armed['plan']
            self.vars['plan'] = {
                'qty': qty, 'entry': price, 'distance': frozen['distance'],
                'risk': qty * unit_risk, 'notional': qty * price,
            }
            self._ledger()[self._key()] = dict(self.vars['plan'])
            # Jesse treats an order at the current price as MARKET. The higher
            # reclaim close is paid explicitly, never the old channel boundary.
            self.buy = qty, price
            return
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
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry,
                             'target_distance': 1.5 * atr}
        return True

    def go_short(self) -> None:
        plan = self.vars['plan']
        if self.symbol == 'BTC-USDT':
            self.vars['entry_deadline'] = int(self.time) + BAR_MS
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        if self.symbol == 'BTC-USDT':
            # Pending entries keep their risk/notional reservation for the full
            # original 4h lifetime, despite 1m cancellation callbacks.
            if self.time < self.vars['entry_deadline']:
                return False
        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.
        # Jesse processes cancellation before evaluating the next route.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:
        if self.symbol == 'BTC-USDT' and self.is_long:
            armed = self.vars.get('reclaim_setup')
            if armed is None:
                raise AssertionError('BTC long fill must originate from the reserved reclaim setup')
            frozen = armed['plan']
            fill = float(self.position.entry_price)
            qty = abs(float(self.position.qty))
            actual_risk = qty * (frozen['distance'] + self.fee_rate * (2 * fill - frozen['distance'])
                                 + SLIPPAGE_RESERVE * fill)
            # This is floating arithmetic tolerance, not an economic oversizing allowance.
            if (qty > frozen['qty'] + 1e-8 or qty * fill > frozen['notional'] + 1e-8
                    or actual_risk > frozen['risk'] + 1e-8):
                raise AssertionError('BTC reclaim fill exceeds a frozen setup ceiling')
            self.vars.pop('reclaim_setup')
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
        if self.symbol == 'BTC-USDT' and self.time % BAR_MS != 0:
            # Protective broker orders remain active at M1; trailing and the
            # inherited 72h short time exit are evaluated only on the 4h clock.
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

    def before_terminate(self) -> None:
        # Mirror cancellation of an unfilled broker order at simulation end:
        # release only the internal pending reservation, without a synthetic fill.
        if self.symbol == 'BTC-USDT' and self.vars.pop('reclaim_setup', None) is not None:
            self._ledger().pop(self._key(), None)

    def on_close_position(self, order, closed_trade) -> None:
        self._ledger().pop(self._key(), None)
