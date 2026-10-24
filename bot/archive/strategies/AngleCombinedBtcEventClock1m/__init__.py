import math
from datetime import datetime, timezone
import jesse.helpers as jh
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


class AngleCombinedBtcEventClock1m(Strategy):
    """BTC close-only directional-change clock replacing short RSI eligibility.

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
            # Keep the baseline long signal frequency on the 4h boundary.
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

    def _event_counts(self, year=None):
        year = self.vars['event_year'] if year is None else year
        return self.vars.setdefault('event_counts', {}).setdefault(year, {
            'minutes': 0, 'down': 0, 'up': 0, 'blocked_open': 0,
            'blocked_pending': 0, 'long_priority': 0, 'rejected': 0,
            'plans': 0, 'armed': 0, 'fills': 0,
        })

    def _event_log(self, label):
        # Bounded yearly aggregates only; never retain a per-minute/event list.
        timestamps = {key: self.vars.get(key) for key in (
            'event_first_minute', 'event_init_time', 'event_last_minute')}
        jh.debug('EVENT_CLOCK ' + label + ' timestamps=' + str(timestamps)
                 + ' counts=' + str(self.vars.get('event_counts', {})))

    def before(self) -> None:
        if self.symbol != 'BTC-USDT':
            return
        now = int(self.time)
        self.vars.setdefault('event_first_minute', now)
        minute = self.candles[-1]
        assert int(minute[0]) + 60000 == now, 'EVENT_M1_NOT_FRESH'
        price, low = float(minute[2]), float(minute[4])
        assert all(math.isfinite(v) and v > 0 for v in (price, low)), 'EVENT_M1_INVALID'
        assert low <= price, 'EVENT_M1_LOW_ABOVE_CLOSE'
        assert math.isclose(price, self.price, rel_tol=1e-10, abs_tol=1e-8), 'EVENT_PRICE_MISMATCH'
        previous = self.vars.get('event_last_minute')
        assert previous is None or previous < now, 'EVENT_MINUTE_REPLAY'
        self.vars['event_last_minute'] = now
        # This timestamp is a pulse, not a queue. Open/pending orders cannot
        # save it for a later flat callback or extend a pending deadline.
        self.vars['event_down_time'] = None
        year = datetime.fromtimestamp(now / 1000, timezone.utc).year
        old_year = self.vars.get('event_year')
        if old_year is not None and year != old_year:
            self._event_log('YEAR_END ' + str(old_year))
        self.vars['event_year'] = year
        counts = self._event_counts()
        counts['minutes'] += 1

        boundary = now % BAR_MS == 0
        if boundary:
            c = self.signal_candles
            assert len(c) >= 240, 'EVENT_AUX_4H_WARMUP'
            assert int(c[-1, 0]) + BAR_MS == now, 'EVENT_AUX_4H_NOT_FRESH'
            macro = ta.ema(c, period=120, sequential=True)
            cache = {
                'bar': int(c[-1, 0]), 'atr': float(ta.atr(c)),
                'fast': float(ta.ema(c, period=20)),
                'macro': float(macro[-1]), 'macro_old': float(macro[-10]),
            }
            assert all(math.isfinite(v) for v in cache.values()), 'EVENT_4H_INVALID'
            assert cache['atr'] > 0, 'EVENT_ATR_NONPOSITIVE'
            self.vars['event_4h'] = cache
            self.vars['clock_warmup_checked'] = True
        if 'event_phase' not in self.vars:
            if not boundary:
                return
            self.vars.update({
                'event_phase': 0, 'event_seed': price,
                'event_delta': self.vars['event_4h']['atr'],
                'event_phase_time': now, 'event_extreme': price,
                'event_init_time': now,
            })
            return

        cache = self.vars['event_4h']
        assert cache['bar'] + BAR_MS <= now < cache['bar'] + 2 * BAR_MS, 'EVENT_AUX_CACHE_STALE'
        phase = self.vars['event_phase']
        delta = float(self.vars['event_delta'])
        assert phase in (-1, 0, 1) and math.isfinite(delta) and delta > 0, 'EVENT_STATE_INVALID'
        assert self.vars['event_phase_time'] <= now, 'EVENT_PHASE_FUTURE'
        if phase == 0:
            seed = self.vars['event_seed']
            direction = 1 if price >= seed + delta else (-1 if price <= seed - delta else 0)
            if direction:
                # Seeding the initial direction is not a tradable reversal.
                self.vars.update({
                    'event_phase': direction, 'event_extreme': price,
                    'event_delta': cache['atr'], 'event_phase_time': now,
                })
            return
        extreme = float(self.vars['event_extreme'])
        assert math.isfinite(extreme) and extreme > 0, 'EVENT_EXTREME_INVALID'
        if phase == 1:
            extreme = max(extreme, price)
            self.vars['event_extreme'] = extreme
            crossed = extreme - price >= delta
        else:
            extreme = min(extreme, price)
            self.vars['event_extreme'] = extreme
            crossed = price - extreme >= delta
        if not crossed:
            return
        assert now > self.vars['event_phase_time'], 'EVENT_DOUBLE_PHASE_SAME_MINUTE'
        # The crossing used the OLD phase delta. Only the newly started
        # phase gets the latest strictly closed 4h ATR.
        self.vars.update({
            'event_phase': -phase, 'event_extreme': price,
            'event_delta': cache['atr'], 'event_phase_time': now,
        })
        if phase == 1:
            counts['down'] += 1
            self.vars['event_down_time'] = now
            self.vars['event_m1_low'] = low
            if self.is_open:
                counts['blocked_open'] += 1
        else:
            counts['up'] += 1

    def before_terminate(self) -> None:
        if self.symbol == 'BTC-USDT':
            self._event_log('FINAL')

    def _signal(self) -> int:
        # One plan per M1, with the unchanged 4h long policy taking priority.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            if self.symbol != 'BTC-USDT':
                self.vars['signal_value'] = 1 if self._plan() else (-1 if self._short_plan() else 0)
            else:
                down = self.vars.get('event_down_time') == int(self.time)
                if self.vars.get('event_cancel_time') == int(self.time):
                    self.vars['signal_value'] = 0
                elif self._plan():
                    self.vars['signal_value'] = 1
                    if down:
                        self._event_counts()['long_priority'] += 1
                elif down:
                    planned = self._short_plan()
                    self.vars['signal_value'] = -1 if planned else 0
                    self._event_counts()['plans' if planned else 'rejected'] += 1
                else:
                    self.vars['signal_value'] = 0
        return self.vars['signal_value']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        plan = self.vars['plan']
        if self.symbol == 'BTC-USDT':
            self.vars['entry_deadline'] = int(self.time) + BAR_MS
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], plan['entry']

    def _short_plan(self) -> bool:
        """An observed DOWN event replaces RSI; all risk gates stay frozen."""
        if self.symbol != 'BTC-USDT' or self.vars.get('event_down_time') != int(self.time):
            return False
        if self.vars.get('event_cancel_time') == int(self.time):
            return False
        cache = self.vars['event_4h']
        assert cache['bar'] + BAR_MS <= self.time < cache['bar'] + 2 * BAR_MS, 'EVENT_SIGNAL_CACHE_STALE'
        fast, atr = cache['fast'], cache['atr']
        if not (atr > 0 and cache['macro'] > cache['macro_old']
                and self.price > cache['macro'] - atr):
            return False
        # Adapt the known signal low to the event's M1, not a prior 4h bar.
        # It is an order level for FUTURE execution, never a backdated fill.
        entry = min(float(self.vars['event_m1_low']), self.price - 0.25 * atr)
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
        assert self.vars.get('event_down_time') == int(self.time), 'EVENT_ORDER_REPLAY'
        assert self.vars.get('event_order_time') != int(self.time), 'EVENT_DUPLICATE_ORDER'
        self.vars['event_order_time'] = int(self.time)
        self._event_counts()['armed'] += 1
        plan = self.vars['plan']
        if self.symbol == 'BTC-USDT':
            self.vars['entry_deadline'] = int(self.time) + BAR_MS
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        if self.symbol == 'BTC-USDT':
            if self.vars.get('event_down_time') == int(self.time):
                self._event_counts()['blocked_pending'] += 1
            # Pending entries keep their risk/notional reservation for the full
            # original 4h lifetime, despite 1m cancellation callbacks.
            if self.time < self.vars['entry_deadline']:
                return False
        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.
        # Jesse processes cancellation before evaluating the next route.
        if self.symbol == 'BTC-USDT':
            self.vars['event_cancel_time'] = int(self.time)
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        self.vars['initial_distance'] = distance
        # An intrabar fill must not inherit highs/closes from before its entry.
        self.vars['best_close'] = entry
        if self.is_short:
            if self.symbol == 'BTC-USDT':
                self._event_counts()['fills'] += 1
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

    def on_close_position(self, order, closed_trade) -> None:
        self._ledger().pop(self._key(), None)
