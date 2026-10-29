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


SUPPLEMENT_WEEKDAY = 1  # UTC: fixed before results, no day/hour search.
SUPPLEMENT_RISK = 0.01
SUPPLEMENT_DURATION = 48 * 60 * 60 * 1000


class AngleCombinedBtcWeekdayControl4h(Strategy):
    """Tuesday BTC beta control; never select this control as an alternative winner.

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
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {
            'qty': qty, 'entry': entry, 'distance': distance,
            'risk': qty * unit_risk, 'notional': qty * entry,
        }
        return True

    def _calendar_counts(self):
        return self.vars.setdefault('calendar_counts', {
            'slots': 0, 'occupied': 0, 'pending': 0, 'baseline_priority': 0,
            'evaluated': 0, 'regime_rejected': 0, 'risk_rejected': 0,
            'plans': 0, 'fills': 0, 'closed': 0, 'time_exits': 0,
            'delayed_fills': 0, 'delayed_time_exits': 0,
            'stale_entry_quotes': 0, 'deferred_exit_quotes': 0,
        })

    def _calendar_slot(self) -> bool:
        if self.symbol != 'BTC-USDT':
            return False
        now = datetime.fromtimestamp(self.time / 1000, timezone.utc)
        # Clock is the decision/close timestamp, not the 4h bar's opening day.
        return now.weekday() == SUPPLEMENT_WEEKDAY and now.hour == 0 and now.minute == 0

    def before(self) -> None:
        if not self._calendar_slot():
            return
        now = int(self.time)
        assert self.vars.get('calendar_last_slot') != now, 'CALENDAR_SLOT_REPLAY'
        self.vars['calendar_last_slot'] = now
        counts = self._calendar_counts()
        counts['slots'] += 1
        if self.is_open:
            counts['occupied'] += 1
        elif self._ledger().get(self._key()):
            counts['pending'] += 1

    def _calendar_quote_fresh(self) -> bool:
        # The draft must include the existing BTC M1 series as a data route.
        # No copying/forward filling: orders use a minute that just closed.
        minutes = self.get_candles(self.exchange, self.symbol, '1m')
        if len(minutes) == 0:
            return False
        idx = int(np.searchsorted(minutes[:, 0], self.time - 60000, side='right')) - 1
        if idx < 0 or int(minutes[idx, 0]) + 60000 != int(self.time):
            return False
        close = float(minutes[idx, 2])
        assert math.isfinite(close) and close > 0, 'CALENDAR_M1_INVALID'
        assert math.isclose(close, self.price, rel_tol=1e-10, abs_tol=1e-8), 'CALENDAR_M1_PRICE_MISMATCH'
        return True

    def _calendar_plan(self) -> bool:
        """A single scheduled long supplement after both baseline plans fail."""
        if not self._calendar_slot():
            return False
        counts = self._calendar_counts()
        counts['evaluated'] += 1
        if not self._calendar_quote_fresh():
            counts['stale_entry_quotes'] += 1
            return False
        c = self.signal_candles
        assert int(c[-1, 0]) + 4 * 60 * 60 * 1000 == int(self.time), 'CALENDAR_4H_NOT_CLOSED'
        assert math.isclose(float(c[-1, 2]), self.price, rel_tol=1e-10, abs_tol=1e-8), 'CALENDAR_PRICE_MISMATCH'
        assert not self.is_open and not self._ledger().get(self._key()), 'CALENDAR_NOT_FLAT'
        slow_n = int(self.hp['ema_slow'])
        if len(c) < max(100, slow_n + 20):
            raise AssertionError('CALENDAR_AUX_WARMUP')
        fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))
        slow = ta.ema(c, period=slow_n, sequential=True)
        atr = float(ta.atr(c))
        if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr)):
            raise AssertionError('CALENDAR_REGIME_INVALID')
        if not (atr > 0 and fast > slow[-1] > slow[-5] and self.price > slow[-1]):
            counts['regime_rejected'] += 1
            return False
        entry = float(self.price)
        distance = 2.0 * atr
        if not 0 < distance < entry:
            counts['risk_rejected'] += 1
            return False
        capital = self._capital()
        committed_risk, committed_notional = self._committed()
        # Exact baseline sizing with only the leg's trade-risk ceiling reduced
        # from 3% to 1%; portfolio, gross, inverse-ATR share and margin caps stay.
        budget = min(capital * SUPPLEMENT_RISK, max(0.0, capital * PORTFOLIO_RISK - committed_risk))
        unit_risk = distance + self.fee_rate * (entry + entry - distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - committed_notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        qty = math.floor(qty / 0.001) * 0.001
        if qty <= 0:
            counts['risk_rejected'] += 1
            return False
        assert qty * unit_risk <= budget + 1e-8, 'CALENDAR_RISK_BUDGET'
        self.vars['plan'] = {
            'qty': qty, 'entry': entry, 'distance': distance,
            'risk': qty * unit_risk, 'notional': qty * entry,
            'calendar_leg': True, 'calendar_signal_time': int(self.time),
            'calendar_deadline': int(self.time) + SUPPLEMENT_DURATION,
        }
        counts['plans'] += 1
        return True

    def _calendar_open(self) -> None:
        plan = self.vars['plan']
        assert self.symbol == 'BTC-USDT' and self.is_long, 'CALENDAR_WRONG_LEG'
        assert self.time >= plan['calendar_signal_time'], 'CALENDAR_FILL_BEFORE_SIGNAL'
        self.vars['calendar_position'] = True
        self.vars['calendar_deadline'] = plan['calendar_deadline']
        self.vars['calendar_fill_time'] = int(self.time)
        counts = self._calendar_counts()
        counts['fills'] += 1
        if int(self.time) != plan['calendar_signal_time']:
            counts['delayed_fills'] += 1
        entry = float(self.position.entry_price)
        distance = plan['distance']
        # Protective STOP uses the real fill, never a hypothetical weekend quote.
        self.vars['initial_distance'] = distance
        self.vars['best_close'] = entry
        self.stop_loss = abs(self.position.qty), entry - distance
        self._ledger().pop(self._key(), None)

    def before_terminate(self) -> None:
        if self.symbol == 'BTC-USDT':
            jh.debug('CALENDAR_SUPPLEMENT weekday=' + str(SUPPLEMENT_WEEKDAY)
                     + ' counts_preterminal=' + str(self._calendar_counts()))

    def _signal(self) -> int:
        # Freeze original long-then-short priority at every decision. A calendar
        # position can still block FUTURE baseline signals; this is measured.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            if self._plan():
                self.vars['signal_value'] = 1
                if self._calendar_slot():
                    self._calendar_counts()['baseline_priority'] += 1
            elif self._short_plan():
                self.vars['signal_value'] = -1
                if self._calendar_slot():
                    self._calendar_counts()['baseline_priority'] += 1
            else:
                self.vars['signal_value'] = 1 if self._calendar_plan() else 0
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
        if self.vars['plan'].get('calendar_leg', False):
            self._calendar_open()
            return
        self.vars['calendar_position'] = False
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
        if self.vars.get('calendar_position', False):
            assert self.symbol == 'BTC-USDT' and self.is_long, 'CALENDAR_ACTIVE_LEG_INVALID'
            if self.time >= self.vars['calendar_deadline']:
                counts = self._calendar_counts()
                if not self._calendar_quote_fresh():
                    counts['deferred_exit_quotes'] += 1
                    return
                counts['time_exits'] += 1
                if self.time > self.vars['calendar_deadline']:
                    counts['delayed_time_exits'] += 1
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
        self._ledger().pop(self._key(), None)
        if self.vars.get('calendar_position', False):
            self._calendar_counts()['closed'] += 1
            self.vars['calendar_position'] = False
