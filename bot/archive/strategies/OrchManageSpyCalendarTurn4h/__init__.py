import calendar
import math
from datetime import datetime, timezone
import numpy as np
from jesse.strategies import Strategy

TRADE_RISK = 0.03
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 1.0
TAIL_STOP = 0.03
SLIPPAGE_RESERVE = 0.001  # Sizing reserve only, not simulated fill friction.


class OrchManageSpyCalendarTurn4h(Strategy):
    """Single SPY calendar-turn adaptation: last four dates to first four.

    This is NOT the paper's last-trading-day/first-three-trading-days rule:
    no NYSE holiday calendar is invented. The fixed16UTC clock also differs
    from the US cash close. Fresh own M1 quotes govern discretionary actions.
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
        # A closed4h bar opening at12UTC makes its decision at16UTC.
        # This calendar condition limits decisions, never exchange stop execution.
        return {'timezone': 'UTC', 'hours': {'Mon-Fri': '12:00-16:00'}}

    @staticmethod
    def _entry_turn(date):
        last = calendar.monthrange(date.year, date.month)[1]
        if date.day < last - 3:
            return None
        # The turn is named by the FOLLOWING month, including December rollover.
        return (date.year + 1, 1) if date.month == 12 else (date.year, date.month + 1)

    @staticmethod
    def _exit_after(turn):
        # First discretionary exit is at16UTC on/after date5, if a fresh quote
        # exists. Date arithmetic uses no future prices or inferred holidays.
        return int(datetime(turn[0], turn[1], 5, tzinfo=timezone.utc).timestamp() * 1000)

    def _fresh_quote(self):
        minute = self.get_candles(self.exchange, self.symbol, '1m')
        if not len(minute):
            return False
        index = int(np.searchsorted(minute[:, 0], self.time - 60000, side='right')) - 1
        if index < 0 or int(minute[index, 0]) + 60000 != int(self.time):
            return False
        assert math.isclose(float(self.price), float(minute[index, 2]),
                            rel_tol=1e-10, abs_tol=1e-8), 'TOM_DECISION_PRICE_NOT_FRESH'
        return True

    def before(self):
        if self.vars.get('calendar_checked'):
            return
        # Deterministic civil-calendar checks, not performance tests or tuning.
        date = lambda y,m,d: datetime(y,m,d,16,tzinfo=timezone.utc)
        assert self._entry_turn(date(2020,12,27)) is None
        assert self._entry_turn(date(2020,12,28)) == (2021,1)
        assert self._entry_turn(date(2020,2,25)) is None
        assert self._entry_turn(date(2020,2,26)) == (2020,3)
        assert self._entry_turn(date(2021,2,24)) is None
        assert self._entry_turn(date(2021,2,25)) == (2021,3)
        assert self._entry_turn(date(2020,4,26)) is None
        assert self._entry_turn(date(2020,4,27)) == (2020,5)
        assert self._exit_after((2021,1)) == int(datetime(2021,1,5,tzinfo=timezone.utc).timestamp()*1000)
        self.vars['calendar_checked'] = True

    def should_long(self):
        # One component only. Portfolio integration needs a separately reviewed
        # account-state design, not an accidental additional route.
        if self.symbol != 'SPY-USDT' or len(self.routes) != 1 or not self.is_trading_hours:
            return False
        turn = self._entry_turn(datetime.fromtimestamp(self.time / 1000, timezone.utc))
        if turn is None or self.vars.get('entry_used_turn') == turn or not self._fresh_quote():
            return False
        entry = float(self.price)
        if not math.isfinite(entry) or entry <= 0:
            return False
        distance = TAIL_STOP * entry
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry - distance) + SLIPPAGE_RESERVE * entry
        room = max(0.0, capital * NOTIONAL_CAP - notional)
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        if budget <= 0 or room <= 0 or margin_room <= 0:
            return False
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        # Same SPY research precision as prior controls; not native lot parity.
        qty = math.floor(qty / 0.001) * 0.001
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'turn': turn, 'risk': qty * unit_risk,
                             'notional': qty * entry}
        return True

    def should_short(self):
        return False

    def go_long(self):
        plan = self.vars['plan']
        assert self._fresh_quote(), 'TOM_ENTRY_WITHOUT_FRESH_QUOTE'
        assert self.vars.get('entry_used_turn') != plan['turn'], 'TOM_SECOND_ENTRY_SAME_TURN'
        self.vars['entry_used_turn'] = plan['turn']
        self.vars['exit_after'] = self._exit_after(plan['turn'])
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], self.price

    def go_short(self):
        pass

    def should_cancel_entry(self):
        # A cancelled entry still consumes that turn. No stop/cancellation churn.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order):
        assert self.is_long, 'TOM_UNEXPECTED_SHORT'
        self.stop_loss = abs(self.position.qty), float(self.position.entry_price) * (1 - TAIL_STOP)
        self._ledger().pop(self._key(), None)

    def update_position(self):
        # Discretionary exits defer to a fresh own16UTC quote. The initial
        # protective STOP remains active intrabar whenever actual quotes exist.
        # No special handling anticipates the research window's final timestamp.
        if (self.time >= self.vars['exit_after'] and self.is_trading_hours
                and self._fresh_quote()):
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        self._ledger().pop(self._key(), None)
