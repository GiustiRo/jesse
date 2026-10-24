import math
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils

NY = ZoneInfo('America/New_York')
MINUTE = 60000
# Fixed research risk; the 10bps reserve changes sizing, not simulated fills.
RISK = 0.01
GROSS_CAP = 4.4
RESERVE = 0.001


class ResearchSpyOpeningRange60(Strategy):
    """First-hour cash-auction range, first subsequent 30m close breakout.
    
    CFD price proxy, volume unused. Weekday schedule is not a holiday calendar.
    Isolated research only; integration requires a shared account-risk design.
    """

    def trading_hours(self):
        return {'timezone': 'America/New_York', 'hours': {'Mon-Fri': '09:30-16:00'}}

    @property
    @cached
    def session_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    @staticmethod
    def _local(timestamp):
        return datetime.fromtimestamp(timestamp / 1000, timezone.utc).astimezone(NY)

    def _fresh(self):
        minute = self.get_candles(self.exchange, self.symbol, '1m')
        if not len(minute):
            return False
        i = int(np.searchsorted(minute[:, 0], self.time - MINUTE, side='right')) - 1
        if i < 0 or int(minute[i, 0]) + MINUTE != int(self.time):
            return False
        assert math.isclose(self.price, float(minute[i, 2]), rel_tol=1e-10, abs_tol=1e-8), 'SPY_PRICE_NOT_FRESH'
        return True

    def before(self):
        opened = self._local(self.closed_candle_open_time)
        day = opened.date().isoformat()
        if self.vars.get('day') != day:
            self.vars.update(day=day, opening_bars=[], opening_range=None, used=False)
        if not self.is_trading_hours:
            return
        c = self.session_candles
        if not len(c) or int(c[-1, 0]) != self.closed_candle_open_time:
            return
        # Both constituent bars must actually be present and consecutive.
        if (opened.hour, opened.minute) == (9, 30):
            self.vars['opening_bars'] = [c[-1].copy()]
        elif (opened.hour, opened.minute) == (10, 0):
            bars = self.vars['opening_bars']
            if len(bars) == 1 and int(c[-1, 0] - bars[0][0]) == 30 * MINUTE:
                # Reject a partial or gap-filled opening hour: every M1 open must exist.
                minutes = self.get_candles(self.exchange, self.symbol, '1m')
                hour = minutes[(minutes[:, 0] >= bars[0][0]) & (minutes[:, 0] < self.time)]
                if len(hour) != 60 or not np.all(np.diff(hour[:, 0]) == MINUTE):
                    return
                if int(hour[0, 0]) != int(bars[0][0]) or int(hour[-1, 0]) + MINUTE != self.time:
                    return
                first, last = bars[0], c[-1]
                self.vars['opening_range'] = {
                    'high': max(float(first[3]), float(last[3])),
                    'low': min(float(first[4]), float(last[4])),
                    'open': float(first[1]), 'close': float(last[2]),
                }

    def _raw_signal(self):
        decision = self._local(self.time)
        minute = decision.hour * 60 + decision.minute
        opening = self.vars.get('opening_range')
        # 11:00 is the earliest CLOSED post-range 30m observation.
        if not opening or not 660 <= minute <= 720:
            return 0
        if self.price > opening['high']:
            return 1
        if self.price < opening['low']:
            return -1
        return 0

    def _signal(self):
        if self.vars.get('signal_index') == self.index:
            return self.vars['signal']
        self.vars['signal_index'] = self.index
        signal = 0
        if (self.symbol == 'SPY-USDT' and len(self.routes) == 1
                and self.is_trading_hours and not self.vars.get('used') and self._fresh()):
            side = self._raw_signal()
            if side:
                opening = self.vars['opening_range']
                stop = opening['low'] if side == 1 else opening['high']
                entry = float(self.price)
                distance = side * (entry - stop)
                capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
                # Stop fees include both sides, with the adverse-fill reserve.
                unit_risk = distance + self.fee_rate * (entry + stop) + RESERVE * entry
                if all(math.isfinite(v) for v in (entry, stop, distance, capital, unit_risk)) and distance > 0 and stop > 0:
                    qty = min(capital * RISK / unit_risk, capital * GROSS_CAP / entry,
                              max(0.0, self.leveraged_available_margin * 0.90) / entry)
                    # Research precision inherited from the SPY baseline.
                    qty = math.floor(qty / 0.001) * 0.001
                    if qty > 0:
                        self.vars['plan'] = {'qty': qty, 'stop': stop, 'side': side}
                        signal = side
        self.vars['signal'] = signal
        return signal

    def should_long(self):
        return self._signal() == 1

    def should_short(self):
        return self._signal() == -1

    def go_long(self):
        self.vars['used'] = True
        self.buy = self.vars['plan']['qty'], self.price

    def go_short(self):
        self.vars['used'] = True
        self.sell = self.vars['plan']['qty'], self.price

    def should_cancel_entry(self):
        # Market entries normally fill immediately; no resting orders survive.
        return True

    def on_open_position(self, order):
        self.vars['entry_day'] = self._local(self.time).date().isoformat()
        self.stop_loss = abs(self.position.qty), self.vars['plan']['stop']

    def update_position(self):
        now = self._local(self.time)
        # Exit debt survives missing quotes and date/session changes. The protective
        # stop is never disabled, including outside the cash-entry window.
        due = now.date().isoformat() != self.vars['entry_day'] or now.hour * 60 + now.minute >= 930
        if due and self._fresh():
            self.liquidate()
