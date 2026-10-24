import math
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

# User-approved research limits; risk is not an optimization parameter.
BR_MODE = 2  # Predeclared structural contrast; not an optimization parameter.
TRADE_RISK = 0.01
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.
SLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.


class SpyLastMechanism03(Strategy):
    """Long LIMIT retests plus BTC-only pullback-continuation STOP shorts.

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
        event = self.vars.get('struct_event')
        if self.symbol != 'SPY-USDT' or not event or not self._entry_window() or not self._fresh_quote():
            return False
        entry, distance = event['entry'], event['distance']
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

    def _fresh_quote(self) -> bool:
        """Exact latest M1 quote; absent/stale data makes this tick ineligible."""
        c = self.get_candles(self.exchange, self.symbol, '1m')
        if not len(c):
            return False
        i = int(np.searchsorted(c[:, 0], self.time - 60000, side='right')) - 1
        if i < 0 or int(c[i, 0]) + 60000 != int(self.time):
            return False
        price = float(c[i, 2])
        return (math.isfinite(price) and price > 0
                and math.isclose(price, self.price, rel_tol=1e-10, abs_tol=1e-8))

    def _context(self):
        """Closed filtered-bar features; no position, cash or margin conditioning."""
        c = self.signal_candles
        n, slow_n = int(self.hp['donchian_len']), int(self.hp['ema_slow'])
        if len(c) < max(slow_n + 20, n + 1):
            return None
        fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))
        slow = ta.ema(c, period=slow_n, sequential=True)
        atr, adx, rsi = float(ta.atr(c)), float(ta.adx(c)), float(ta.rsi(c))
        level = float(np.max(c[-n-1:-1, 3]))
        if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, level)):
            return None
        regime = (atr > 0 and self.price > slow[-1]
                  and fast > slow[-1] > slow[-5] and adx >= self.hp['adx_min']
                  and 52 <= rsi <= 76 and self.high - self.low <= 3 * atr)
        return {'atr': atr, 'level': level, 'regime': regime}

    def _origin(self, context):
        """Cq price/data eligibility BEFORE account state or sizing."""
        if context is None or not context['regime'] or not self._entry_window() or not self._fresh_quote():
            return False
        level, atr = context['level'], context['atr']
        return level < self.price <= level + atr and 0 < 2 * atr < level

    def _set_struct_event(self, entry, context):
        # The event is consumed by the caller even if this data/regime gate fails.
        if (context is None or not context['regime'] or not self._entry_window()
                or not self._fresh_quote()):
            return
        distance = float(self.hp['stop_atr']) * context['atr']
        if 0 < distance < entry:
            self.vars['struct_event'] = {'entry': float(entry), 'distance': distance}

    def before(self) -> None:
        self.vars['struct_event'] = None
        if self.symbol != 'SPY-USDT' or not self.is_trading_hours:
            return
        c = self.signal_candles
        if not len(c) or int(c[-1, 0]) != int(self.closed_candle_open_time):
            return
        context = self._context()
        if BR_MODE <= 2:
            # Left-censored epoch remains ineligible until a reset is observed.
            n = int(self.hp['donchian_len'])
            if len(c) >= n + 1:
                upper = float(np.max(c[-n-1:-1, 3]))
                lower = float(np.min(c[-n-1:-1, 4]))
                if math.isfinite(upper) and math.isfinite(lower) and self.price <= (upper + lower) / 2:
                    self.vars.update(epoch_seen=True, epoch_count=0)
            if not self.vars.get('epoch_seen') or not self._origin(context):
                return
            ordinal = self.vars.get('epoch_count', 0) + 1
            self.vars['epoch_count'] = ordinal
            # Frozen ordinal contrast: count opportunities before occupancy or sizing.
            if ordinal == 3:
                self._set_struct_event(context['level'], context)
            return

        episode = self.vars.get('episode')
        if episode is None:
            if self._origin(context):
                self.vars['episode'] = {'level': context['level'], 'high': float(self.high),
                                        'age': 0, 'interaction': None, 'consumed': False}
            return  # The arming bar is never its own retest.

        episode['age'] += 1  # Only closed bars in the original filtered session count.
        age, level = episode['age'], episode['level']
        if episode['interaction'] is None and self.low <= level:
            if self.high < level:
                # Entire bar below the level: no observable crossing through it.
                episode.update(interaction='gap_below', consumed=True)
            elif self.price > level:
                episode.update(interaction='held', consumed=True)
                if BR_MODE == 3:
                    self._set_struct_event(float(self.price), context)
                elif BR_MODE == 5:
                    self._set_struct_event(max(float(self.high), float(self.price)), context)
                elif BR_MODE == 6:
                    self._set_struct_event(max(episode['high'], float(self.price)), context)
            else:
                episode.update(interaction='failed', touch_age=age, consumed=(BR_MODE != 4))
        elif (BR_MODE == 4 and episode['interaction'] == 'failed'
              and not episode['consumed'] and age > episode['touch_age'] and self.price > level):
            episode['consumed'] = True
            self._set_struct_event(float(self.price), context)

        # Shared expiry survives consumption, absent quotes, regime failure and occupancy.
        # Clearing occurs AFTER this fourth observation, so it cannot rearm on this bar.
        if age >= 4:
            self.vars['episode'] = None
