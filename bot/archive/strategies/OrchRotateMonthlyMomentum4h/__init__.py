import calendar
import math
from datetime import datetime, timezone
import numpy as np
from jesse.strategies import Strategy
from jesse import utils

TRADE_RISK = 0.03
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 1.0  # Admission ceiling; 10% stop and risk sizing deploy about 0.2945x.
TAIL_STOP = 0.10
SLIPPAGE_RESERVE = 0.001  # Sizing reserve only, not applied slippage.
DAY_MS = 86400000
COMMON_WINDOW = {'timezone': 'UTC', 'hours': {'Mon-Fri': '12:00-16:00'}}


class OrchRotateMonthlyMomentum4h(Strategy):
    """Monthly positive three-calendar-month momentum or cash.

    Long-only component. Common snapshots accumulate only from observed,
    fresh own M1 quotes at the 16:00 UTC callback. Startup cash stays visible.
    """

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


    def trading_hours(self):
        if self.symbol == 'SPY-USDT':
            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}
        return None

    def _state(self):
        return self.shared_vars.setdefault('orch_rotation', {
            'observations': {}, 'ranked_month': None, 'rank_time': None,
            'target': None, 'entry_used': True, 'exit_pending': {},
            'rank_records': [], 'first_eligible_rank': None,
        })

    @staticmethod
    def _pending(strategy):
        return any(order.status in ('ACTIVE', 'QUEUED') for order in strategy.entry_orders)

    def _fresh_quote(self):
        minute = self.get_candles(self.exchange, self.symbol, '1m')
        if not len(minute):
            return False
        # Binary search avoids copying the entire retained M1 history at every
        # callback. Ignore any forming minute; only its completed predecessor
        # can prove a tradable quote at this decision timestamp.
        index = int(np.searchsorted(minute[:, 0], self.time - 60000, side='right')) - 1
        if index < 0 or int(minute[index, 0]) + 60000 != int(self.time):
            return False
        # Numeric parity tolerance, not a trading threshold: the 4h decision
        # must use the same close as the verified last fully observed minute.
        assert math.isclose(float(self.price), float(minute[index, 2]),
                            rel_tol=1e-10, abs_tol=1e-8), 'Decision price is not the fresh own M1 quote'
        return True

    def _review_tick(self):
        # The 4h bar opening at noon decides at 16:00, via the public hours API.
        return utils.is_in_trading_hours(self.closed_candle_open_time, COMMON_WINDOW)

    @staticmethod
    def _three_months_before(stamp):
        date = datetime.fromtimestamp(stamp / 1000, timezone.utc)
        index = date.year * 12 + date.month - 1 - 3
        year, month0 = divmod(index, 12)
        month = month0 + 1
        day = min(date.day, calendar.monthrange(year, month)[1])
        return int(date.replace(year=year, month=month, day=day).timestamp() * 1000)

    def before(self):
        state = self._state()
        expected = {'BTC-USDT', 'PAXG-USDT', 'SPY-USDT'}
        if {route.symbol for route in self.routes if route.exchange == self.exchange} != expected:
            raise ValueError('Rotation needs exactly BTC, PAXG and SPY trading routes')
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            strategy = route.strategy
            if not strategy.is_open and not self._pending(strategy):
                state['exit_pending'].pop(route.exchange + ':' + route.symbol, None)
        if not self._review_tick():
            return
        if self._fresh_quote() and math.isfinite(self.price) and self.price > 0:
            # A route records ONLY its own actual observation. All five years
            # fit easily in this small dictionary; retain well over 120 days.
            state['observations'].setdefault(int(self.time), {})[self.symbol] = float(self.price)
        month = datetime.fromtimestamp(self.time / 1000, timezone.utc).strftime('%Y-%m')
        if state['ranked_month'] == month:
            return
        cutoff = int(self.closed_candle_open_time)
        common = [stamp for stamp, row in state['observations'].items()
                  if stamp < cutoff and set(row) == expected]
        # Strictly older CLOSE timestamps make selection independent of which
        # route has already processed the current timestamp. No bootstrap bars
        # are assumed fresh merely because their nominal 4h end is 16:00.
        if not common:
            return
        latest = max(common)
        if datetime.fromtimestamp(latest / 1000, timezone.utc).strftime('%Y-%m') != month:
            return
        assert latest < cutoff < int(self.time), 'Ranking used a nonhistorical common observation'
        anchor_target = self._three_months_before(latest)
        anchors = [stamp for stamp in common if stamp <= anchor_target]
        anchor = max(anchors) if anchors else None
        eligible = anchor is not None and anchor_target - anchor <= 7 * DAY_MS
        scores, target = {}, None
        if eligible:
            scores = {symbol: price / state['observations'][anchor][symbol] - 1
                      for symbol, price in state['observations'][latest].items()}
            # Explicit alphabetical tie handling, never callback-order priority.
            winner = sorted(scores, key=lambda symbol: (-scores[symbol], symbol))[0]
            if scores[winner] > 0:
                target = winner
            if state['first_eligible_rank'] is None:
                state['first_eligible_rank'] = int(self.time)
        state.update(ranked_month=month, rank_time=int(self.time), target=target)
        # A held unchanged winner uses this month's permission: a later stop
        # means cash until the NEXT monthly ranking, not immediate reentry.
        state['entry_used'] = any(
            route.exchange == self.exchange and route.symbol == target
            and (route.strategy.is_open or self._pending(route.strategy))
            for route in self.routes)
        for route in self.routes:
            if route.exchange == self.exchange and route.symbol != target:
                if route.strategy.is_open or self._pending(route.strategy):
                    state['exit_pending'][route.exchange + ':' + route.symbol] = True
        state['rank_records'].append({
            'month': month, 'rank_time': int(self.time), 'observation': latest,
            'anchor': anchor, 'eligible': eligible, 'scores': scores, 'target': target,
        })

    def should_long(self):
        state = self._state()
        if (state['target'] != self.symbol or state['entry_used']
                or state['exit_pending'] or state['rank_time'] is None
                or self.time <= state['rank_time'] or not self._review_tick()
                or not self._fresh_quote()):
            return False
        if any(route.strategy.is_open or self._pending(route.strategy)
               for route in self.routes if route.exchange == self.exchange):
            return False
        entry = float(self.price)
        distance = TAIL_STOP * entry
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry - distance) + SLIPPAGE_RESERVE * entry
        qty = min(budget / unit_risk,
                  max(0.0, capital * NOTIONAL_CAP - notional) / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        # Research precision only; native target lot/min-notional remain unverified.
        step = 0.0001 if self.symbol == 'PAXG-USDT' else 0.001
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry}
        return True

    def should_short(self):
        return False

    def go_long(self):
        plan = self.vars['plan']
        assert self.time > self._state()['rank_time'], 'Entry must follow ranking'
        assert not self._state()['exit_pending'], 'Uncompleted old exit request'
        assert not any(route.strategy.is_open or self._pending(route.strategy)
                       for route in self.routes if route.exchange == self.exchange), 'Old exposure not flat'
        plan['rank_time'] = self._state()['rank_time']
        self._state()['entry_used'] = True
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], self.price

    def should_cancel_entry(self):
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order):
        assert int(order.executed_at) > self.vars['plan']['rank_time'], 'Actual fill precedes ranking'
        assert not any(route.strategy.is_open
                       for route in self.routes if route.exchange == self.exchange
                       and route.symbol != self.symbol), 'Overlapping rotation positions'
        if self.is_long:
            self.stop_loss = abs(self.position.qty), float(self.position.entry_price) * (1 - TAIL_STOP)
            self.vars['stop_review_month'] = self._state()['ranked_month']
        self._ledger().pop(self._key(), None)
        if self._state()['target'] != self.symbol:
            self._state()['exit_pending'][self._key()] = True

    def update_position(self):
        state = self._state()
        if not self._fresh_quote():
            # Actual protective-stop execution remains active whenever M1 quotes
            # exist. Only this discretionary action waits for a fresh callback.
            return
        if self._key() in state['exit_pending'] or state['target'] != self.symbol:
            self.liquidate()
            return
        if (self._review_tick()
                and self.vars.get('stop_review_month') != state['ranked_month']):
            stop = self.price * (1 - TAIL_STOP)
            if self.average_stop_loss < stop < self.price:
                self.stop_loss = abs(self.position.qty), stop
            self.vars['stop_review_month'] = state['ranked_month']

    def on_close_position(self, order, closed_trade):
        self._ledger().pop(self._key(), None)
