import math
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils

NY = ZoneInfo('America/New_York')
MINUTE = 60000
HALF_HOUR = 30 * MINUTE
RISK = 0.01
GROSS = 4.4
RESERVE = 0.001  # Sizing only; no adverse fill is simulated by this reserve.


class R20SpyCashInventoryRecovery(Strategy):
    """R20 predeclared price experiment; session OHLC uses complete observed M1.

    Full common engine is copied, avoiding imports between project strategies.
    Weekdays are not a complete NYSE holiday calendar; absent sessions stay absent.
    """
    USE_PAXG = False

    def trading_hours(self):
        return {'timezone': 'America/New_York', 'hours': {'Mon-Fri': '09:30-16:00'}}

    @property
    @cached
    def session_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    @staticmethod
    def _local(stamp):
        return datetime.fromtimestamp(stamp / 1000, timezone.utc).astimezone(NY)

    def _fix(self, symbol=None):
        symbol = symbol or self.symbol
        c = self.get_candles(self.exchange, symbol, '1m')
        if not len(c):
            return None
        i = int(np.searchsorted(c[:, 0], self.time - MINUTE, side='right')) - 1
        if i < 0 or int(c[i, 0]) + MINUTE != int(self.time):
            return None
        price = float(c[i, 2])
        if not math.isfinite(price) or price <= 0:
            return None
        if symbol == self.symbol:
            assert math.isclose(price, self.price, rel_tol=1e-10, abs_tol=1e-8), 'R20_FRESH_PRICE_MISMATCH'
        return price

    def _complete_bar(self):
        c = self.get_candles(self.exchange, self.symbol, '1m')
        start = self.closed_candle_open_time
        lo = int(np.searchsorted(c[:, 0], start, side='left'))
        hi = int(np.searchsorted(c[:, 0], self.time, side='left'))
        block = c[lo:hi]
        return (len(block) == 30 and int(block[0, 0]) == start
                and int(block[-1, 0]) + MINUTE == self.time
                and bool(np.all(np.diff(block[:, 0]) == MINUTE))
                and self._fix() is not None)

    @staticmethod
    def _civil_previous(day):
        d = datetime.fromisoformat(day).date()
        return (d - timedelta(days=3 if d.weekday() == 0 else 1)).isoformat()

    @staticmethod
    def _atr(history):
        # Simple mean of14 observed-session true ranges, not Wilder/4h ATR.
        if len(history) < 15:
            return None
        tr = [max(v['high']-v['low'], abs(v['high']-p['close']),
                  abs(v['low']-p['close'])) for p, v in zip(history[:-1], history[1:])]
        a = float(np.mean(tr[-14:]))
        return a if math.isfinite(a) and a > 0 else None

    def before(self):
        self.vars['event'] = None
        self.vars.setdefault('history', [])
        self.vars.setdefault('sequence', 0)
        opened = self._local(self.closed_candle_open_time)
        day = opened.date().isoformat()
        if self.vars.get('session_day') != day:
            self.vars.update(session_day=day, bars=[])
        if not self.is_trading_hours:
            return
        c = self.session_candles
        if not len(c) or int(c[-1, 0]) != self.closed_candle_open_time:
            return
        bars = self.vars['bars']
        if (opened.hour, opened.minute) == (9, 30):
            bars.clear()
        # An incomplete bar invalidates the entire session; later bars cannot
        # repair the missing prefix or create a synthetic overnight observation.
        if not self._complete_bar():
            bars.clear()
            return
        if not bars:
            if (opened.hour, opened.minute) != (9, 30):
                return
        elif int(c[-1, 0]) - int(bars[-1][0]) != HALF_HOUR:
            bars.clear()
            return
        bars.append(c[-1].copy())
        decision = self._local(self.time)
        h = self.vars['history']
        if (decision.hour, decision.minute) == (10, 0) and len(bars) == 1:
            a = self._atr(h)
            if a:
                self.vars['event'] = self._opening_signal(h, bars[0], day, a)
        if (decision.hour, decision.minute) != (16, 0) or len(bars) != 13:
            return
        self.vars['sequence'] += 1
        previous = h[-1] if h else None
        record = {'day': day, 'seq': self.vars['sequence'],
                  'open': float(bars[0][1]), 'close': float(bars[-1][2]),
                  'high': max(float(v[3]) for v in bars),
                  'low': min(float(v[4]) for v in bars), 'paxg': None}
        record['gap'] = (record['open']-previous['close']
                         if previous and previous['day'] == self._civil_previous(day) else None)
        if self.USE_PAXG:
            record['paxg'] = self._fix('PAXG-USDT')
        h.append(record)
        self.vars['history'] = h[-150:]  # Technical retention exceeds every64-observation feature.
        a = self._atr(h[:-1])  # The event session cannot enlarge its own denominator.
        if a:
            self.vars['event'] = self._daily_signal(h, a)

    def _opening_signal(self, h, bar, day, a):
        return None

    def _daily_signal(self, h, a):
        return None

    def _event(self, side, a, hours, target=None, structural=None):
        if target is not None and side * (target-self.price) <= 0:
            return None
        distance = max(2*a, side*(self.price-structural)) if structural is not None else 2*a
        if not 0 < distance < self.price:
            return None
        return {'side': side, 'a': a, 'hours': hours, 'target': target,
                'structural': structural, 'distance': distance}

    def _plan(self):
        event = self.vars.get('event')
        if self.symbol != 'SPY-USDT' or len(self.routes) != 1 or not event or self._fix() is None:
            return 0
        price = float(self.price)
        side = event['side']
        stop = price-side*event['distance']
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        unit = event['distance']+self.fee_rate*(price+stop)+RESERVE*price
        qty = min(capital*RISK/unit, capital*GROSS/price,
                  max(0.0, self.leveraged_available_margin*0.90)/price)
        qty = math.floor(qty/0.001)*0.001
        if qty <= 0:
            return 0
        self.vars['plan'] = dict(event, qty=qty, capital=capital)
        return side

    def _signal(self):
        if self.vars.get('signal_index') != self.index:
            self.vars.update(signal_index=self.index, signal=self._plan())
        return self.vars['signal']

    def should_long(self):
        return self._signal() == 1

    def should_short(self):
        return self._signal() == -1

    def go_long(self):
        self.buy = self.vars['plan']['qty'], self.price

    def go_short(self):
        self.sell = self.vars['plan']['qty'], self.price

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        p = self.vars['plan']
        entry = float(self.position.entry_price)
        distance = (max(2*p['a'], p['side']*(entry-p['structural']))
                    if p['structural'] is not None else p['distance'])
        stop = entry-p['side']*distance
        self.vars.update(opened_at=int(self.position.opened_at), hold_ms=p['hours']*3600000)
        self.stop_loss = abs(self.position.qty), stop
        if p['target'] is not None:
            self.take_profit = abs(self.position.qty), p['target']

    def update_position(self):
        # Risk exits remain active outside the entry calendar. Missing quotes
        # defer the time exit; they never fabricate liquidity at the deadline.
        if self.time-self.vars['opened_at'] >= self.vars['hold_ms'] and self._fix() is not None:
            self.liquidate()

    def _cross(self, key, state):
        old = self.vars.get(key, False)
        self.vars[key] = bool(state)
        return bool(state) and not old

    @staticmethod
    def _paxg_event(h):
        # Denominator is frozen before the three intervals defining the event.
        if len(h) < 64:
            return None
        px = [v['paxg'] for v in h[-64:]]
        if any(v is None for v in px):
            return None
        std = float(np.std(np.diff(px[:-3]), ddof=0))
        return (px[-1]-px[-4], std) if std > 0 and math.isfinite(std) else None

    def _crash(self, h):
        if len(h) < 21:
            return None
        row = h[-1]
        price = row['close']
        episode = self.vars.get('crash')
        if episode and price >= episode['peak']:
            self.vars['crash'] = None
            episode = None
        prior = h[-21:-1]
        peak = max(v['close'] for v in prior)
        peak_row = next(v for v in reversed(prior) if v['close'] == peak)
        state = price <= peak*0.90 and row['seq']-peak_row['seq'] <= 5
        crossed = self._cross('crash_state', state)
        if episode is None and crossed:
            episode = {'peak': peak, 'low': price, 'recovered': False,
                       'long_done': False, 'short_done': False}
            self.vars['crash'] = episode
        if episode is None:
            return None
        episode['new_recovery'] = False
        episode['new_failure'] = False
        if not episode['recovered']:
            episode['low'] = min(episode['low'], price)
            if price >= episode['low']*1.03:
                episode.update(recovered=True, floor=episode['low'], bounce_peak=price,
                               new_recovery=True)
        else:
            episode['bounce_peak'] = max(episode['bounce_peak'], price)
            if price < episode['floor'] and not episode['short_done']:
                episode['new_failure'] = True
                episode['short_done'] = True
        return episode

    def _daily_signal(self, h, a):
        d = h[-1]
        if d['gap'] is None or d['gap'] < 0:
            return None
        if d['close']-d['open'] > -a or d['close'] > d['low']+0.25*(d['high']-d['low']):
            return None
        return self._event(1, a, 48, target=d['open'])

