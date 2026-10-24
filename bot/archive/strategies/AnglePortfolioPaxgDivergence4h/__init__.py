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


PAXG_CONTEXT_SYMBOLS = ('BTC-USDT', 'PAXG-USDT', 'SPY-USDT')
PAXG_BAR_MS = 4 * 60 * 60 * 1000
PAXG_DAY_MS = 24 * 60 * 60 * 1000


class AnglePortfolioPaxgDivergence4h(Strategy):
    """Baseline BTC/SPY with PAXG long/cash on synchronized seven-day divergence.

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
        if self.symbol == 'PAXG-USDT':
            return self._paxg_plan()
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
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {
            'qty': qty, 'entry': entry, 'distance': distance,
            'risk': qty * unit_risk, 'notional': qty * entry,
        }
        return True

    def _paxg_state(self):
        if 'paxg_divergence' not in self.vars:
            self.vars['paxg_divergence'] = {
                'snapshots': {}, 'context': None, 'event_time': None,
                'exit_pending': False, 'event_entry_allowed': False,
                'first_callback': int(self.time),
                'last_callback': int(self.time), 'first_context': None,
                'last_context': None, 'year': None, 'samples': [],
                'counts': {key: 0 for key in (
                    'callbacks', 'capture_attempts', 'captures', 'missing_capture',
                    'update_attempts', 'missing_current', 'missing_prior',
                    'missing_decision_quote', 'missing_4h', 'valid_updates',
                    'active_updates', 'events', 'events_open', 'events_pending',
                    'entry_risk_rejected', 'plans', 'fills', 'context_exit_requests',
                    'context_exits', 'deferred_exit_quotes', 'closed')},
            }
        return self.vars['paxg_divergence']

    def _paxg_quote(self, symbol, stamp):
        # Read only the minute that has just closed. Historical endpoint quotes
        # live in our own bounded memory, never in assumed 7-day M1 retention.
        minutes = self.get_candles(self.exchange, symbol, '1m')
        if len(minutes) == 0:
            return None
        idx = int(np.searchsorted(minutes[:, 0], stamp - 60000, side='right')) - 1
        if idx < 0 or int(minutes[idx, 0]) + 60000 != stamp:
            return None
        price = float(minutes[idx, 2])
        assert math.isfinite(price) and price > 0, 'PAXG_M1_INVALID'
        return price

    def _paxg_log(self, label):
        state = self._paxg_state()
        metadata = {key: state[key] for key in (
            'first_callback', 'last_callback', 'first_context', 'last_context')}
        jh.debug('PAXG_DIVERGENCE ' + label + ' metadata=' + str(metadata)
                 + ' counts_preterminal=' + str(state['counts']))
        if label == 'FINAL':
            jh.debug('PAXG_DIVERGENCE bounded_context_samples=' + str(state['samples']))

    def _paxg_endpoint(self, stamp):
        state = self._paxg_state()
        quote = state['snapshots'].get(stamp)
        if quote is None:
            return None
        assert stamp < int(self.time), 'PAXG_ENDPOINT_NOT_PRIOR'
        prices = {}
        for route in self.routes:
            if route.exchange != self.exchange or route.symbol not in PAXG_CONTEXT_SYMBOLS:
                continue
            # At the 16:00 decision, every route has already finished 12:00.
            # Do not ask another route's potentially stale cached property.
            c = route.strategy.candles
            opening = stamp - PAXG_BAR_MS
            idx = int(np.searchsorted(c[:, 0], opening, side='right')) - 1
            if idx < 0 or int(c[idx, 0]) != opening:
                return None
            assert int(c[idx, 0]) + PAXG_BAR_MS == stamp, 'PAXG_ENDPOINT_CLOCK'
            price = float(c[idx, 2])
            assert math.isfinite(price) and price > 0, 'PAXG_4H_INVALID'
            assert math.isclose(price, quote[route.symbol], rel_tol=1e-10, abs_tol=1e-8), 'PAXG_ENDPOINT_PARITY'
            prices[route.symbol] = price
        assert set(prices) == set(PAXG_CONTEXT_SYMBOLS), 'PAXG_CONTEXT_ROUTES'
        return prices

    def before(self) -> None:
        if self.symbol != 'PAXG-USDT':
            return
        state = self._paxg_state()
        now = int(self.time)
        assert now % PAXG_BAR_MS == 0, 'PAXG_EXPECTS_4H_CLOCK'
        state['event_time'] = None
        state['event_entry_allowed'] = False
        state['last_callback'] = now
        counts = state['counts']
        counts['callbacks'] += 1
        clock = datetime.fromtimestamp(now / 1000, timezone.utc)
        if state['year'] is not None and state['year'] != clock.year:
            self._paxg_log('CUMULATIVE_THROUGH_YEAR_END ' + str(state['year']))
        state['year'] = clock.year
        # Keep at least eight calendar days, including the exact T-7d key.
        cutoff = now - 8 * PAXG_DAY_MS
        for stamp in list(state['snapshots']):
            if stamp < cutoff:
                del state['snapshots'][stamp]
        if clock.weekday() >= 5:
            return
        if clock.hour == 12:
            counts['capture_attempts'] += 1
            quote = {symbol: self._paxg_quote(symbol, now) for symbol in PAXG_CONTEXT_SYMBOLS}
            if any(value is None for value in quote.values()):
                counts['missing_capture'] += 1
                return
            assert now not in state['snapshots'], 'PAXG_CAPTURE_REPLAY'
            assert math.isclose(self.price, quote[self.symbol], rel_tol=1e-10, abs_tol=1e-8), 'PAXG_CAPTURE_OWN_PRICE'
            # Capture M1 proof now without depending on SPY's 4h callback order.
            state['snapshots'][now] = quote
            counts['captures'] += 1
            return
        if clock.hour != 16:
            return
        counts['update_attempts'] += 1
        end = now - PAXG_BAR_MS
        start = end - 7 * PAXG_DAY_MS
        if end not in state['snapshots']:
            counts['missing_current'] += 1
            return
        if start not in state['snapshots']:
            counts['missing_prior'] += 1
            return
        spy_quote = self._paxg_quote('SPY-USDT', now)
        own_quote = self._paxg_quote(self.symbol, now)
        if spy_quote is None or own_quote is None:
            counts['missing_decision_quote'] += 1
            return
        assert math.isclose(self.price, own_quote, rel_tol=1e-10, abs_tol=1e-8), 'PAXG_DECISION_PRICE'
        current, prior = self._paxg_endpoint(end), self._paxg_endpoint(start)
        if current is None or prior is None:
            counts['missing_4h'] += 1
            return
        returns = {symbol: current[symbol] / prior[symbol] - 1.0 for symbol in PAXG_CONTEXT_SYMBOLS}
        assert all(math.isfinite(value) for value in returns.values()), 'PAXG_RETURNS_INVALID'
        active = (returns['BTC-USDT'] < 0 and returns['SPY-USDT'] < 0
                  and returns['PAXG-USDT'] > 0)
        old = state['context']
        state['context'] = active
        state['last_context'] = now
        if state['first_context'] is None:
            state['first_context'] = now
        counts['valid_updates'] += 1
        counts['active_updates'] += int(active)
        if len(state['samples']) < 8:
            state['samples'].append({
                'decision': now, 'T': end, 'T_minus_7d': start,
                'current': current, 'prior': prior, 'returns': returns,
                'active': active,
            })
        if not active:
            # Missing data never produces this debt. A genuinely observed false
            # state survives until an existing/pending position can close safely.
            if self.is_open or self._ledger().get(self._key()):
                if not state['exit_pending']:
                    counts['context_exit_requests'] += 1
                    jh.debug('PAXG_DIVERGENCE FALSE_TO_EXIT_DEBT ' + str({
                        'decision': now, 'T': end, 'T_minus_7d': start,
                        'returns': returns, 'allowed': False,
                        'open': bool(self.is_open),
                        'pending': bool(self._ledger().get(self._key())),
                    }))
                state['exit_pending'] = True
            return
        if not self.is_open and not self._ledger().get(self._key()):
            state['exit_pending'] = False
        if old is not True:
            # This is a one-callback pulse even if open, pending, or out of risk.
            state['event_time'] = now
            counts['events'] += 1
            if self.is_open:
                counts['events_open'] += 1
            elif self._ledger().get(self._key()):
                counts['events_pending'] += 1
            else:
                state['event_entry_allowed'] = not state['exit_pending']
            jh.debug('PAXG_DIVERGENCE EVENT ' + str({
                'decision': now, 'T': end, 'T_minus_7d': start,
                'returns': returns, 'allowed': state['event_entry_allowed'],
                'open': bool(self.is_open),
                'pending': bool(self._ledger().get(self._key())),
            }))

    def _paxg_plan(self) -> bool:
        state = self._paxg_state()
        if (state['event_time'] != int(self.time) or state['exit_pending']
                or not state['event_entry_allowed']):
            return False
        if self.is_open or self._ledger().get(self._key()):
            return False
        c = self.signal_candles
        assert len(c) >= 100, 'PAXG_PLAN_WARMUP'
        atr = float(ta.atr(c))
        entry = float(self.price)
        distance = 2.0 * atr
        if not (math.isfinite(distance) and 0 < distance < entry):
            state['counts']['entry_risk_rejected'] += 1
            return False
        capital = self._capital()
        committed_risk, committed_notional = self._committed()
        # Same 3%/8%, fee reserve, gross share and margin caps as the baseline.
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - committed_risk))
        unit_risk = distance + self.fee_rate * (entry + entry - distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - committed_notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        qty = math.floor(qty / 0.0001) * 0.0001
        if qty <= 0:
            state['counts']['entry_risk_rejected'] += 1
            return False
        assert qty * unit_risk <= budget + 1e-8, 'PAXG_PLAN_RISK'
        self.vars['plan'] = {
            'qty': qty, 'entry': entry, 'distance': distance,
            'risk': qty * unit_risk, 'notional': qty * entry,
            'paxg_event_time': int(self.time),
        }
        state['counts']['plans'] += 1
        return True

    def _paxg_open(self) -> None:
        state = self._paxg_state()
        assert self.is_long and self.position.entry_price > 0, 'PAXG_LONG_ONLY'
        assert self.time >= self.vars['plan']['paxg_event_time'], 'PAXG_FILL_BEFORE_EVENT'
        state['counts']['fills'] += 1
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        assert 0 < distance < entry, 'PAXG_FILL_STOP_DISTANCE'
        self.vars['initial_distance'] = distance
        self.vars['best_close'] = entry
        self.stop_loss = abs(self.position.qty), entry - distance
        if state['context'] is False:
            state['exit_pending'] = True
        self._ledger().pop(self._key(), None)

    def _paxg_update(self) -> None:
        state = self._paxg_state()
        if not state['exit_pending']:
            return
        own_quote = self._paxg_quote(self.symbol, int(self.time))
        if own_quote is None:
            state['counts']['deferred_exit_quotes'] += 1
            return
        assert math.isclose(self.price, own_quote, rel_tol=1e-10, abs_tol=1e-8), 'PAXG_EXIT_PRICE'
        state['counts']['context_exits'] += 1
        self.liquidate()

    def before_terminate(self) -> None:
        if self.symbol == 'PAXG-USDT':
            self._paxg_log('FINAL')

    def _signal(self) -> int:
        # Compute exactly one plan per bar, with long priority. Checking
        # should_short after go_long must never overwrite a queued long plan.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            self.vars['signal_value'] = 1 if self._plan() else (-1 if self._short_plan() else 0)
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
        if self.symbol == 'PAXG-USDT':
            self._paxg_open()
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
        if self.symbol == 'PAXG-USDT':
            self._paxg_update()
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
        if self.symbol == 'PAXG-USDT':
            state = self._paxg_state()
            state['counts']['closed'] += 1
            state['exit_pending'] = False
