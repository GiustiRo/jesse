import math
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

NY = ZoneInfo('America/New_York')
MINUTE = 60000
HALF = 30 * MINUTE
RISK = 0.01
GROSS = 4.4
RESERVE = 0.001  # Sizing reserve only; fills do not include this slippage.
HURDLE = 0.0019  # 9bps modeled roundtrip fee plus10bps reserve, fixed before results.


class R40SpyJumpComponentFade(Strategy):
    """R40 price experiment with daily sessions and closed2h RTH blocks.

    Absences are not imputed. Complete M1 timestamps do not certify the
    upstream provider's treatment of gaps. No volume or live parity is inferred.
    """

    def trading_hours(self):
        return {'timezone': 'America/New_York', 'hours': {'Mon-Fri': '09:30-16:00'}}

    @property
    @cached
    def session_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    @staticmethod
    def _local(stamp):
        return datetime.fromtimestamp(stamp/1000, timezone.utc).astimezone(NY)

    @staticmethod
    def _civil_previous(day):
        d = datetime.fromisoformat(day).date()
        return (d-timedelta(days=3 if d.weekday() == 0 else 1)).isoformat()

    def _fix(self):
        c = self.get_candles(self.exchange, self.symbol, '1m')
        if not len(c):
            return None
        i = int(np.searchsorted(c[:, 0], self.time-MINUTE, side='right'))-1
        if i < 0 or int(c[i, 0])+MINUTE != int(self.time):
            return None
        price = float(c[i, 2])
        if not math.isfinite(price) or price <= 0:
            return None
        assert math.isclose(price, self.price, rel_tol=1e-10, abs_tol=1e-8), 'R40_PRICE_NOT_FRESH'
        return price

    def _complete_bar(self):
        c = self.get_candles(self.exchange, self.symbol, '1m')
        lo = int(np.searchsorted(c[:, 0], self.closed_candle_open_time, side='left'))
        hi = int(np.searchsorted(c[:, 0], self.time, side='left'))
        b = c[lo:hi]
        return (len(b) == 30 and int(b[0, 0]) == self.closed_candle_open_time
                and int(b[-1, 0])+MINUTE == self.time
                and bool(np.all(np.diff(b[:, 0]) == MINUTE)) and self._fix() is not None)

    @staticmethod
    def _atr(h):
        if len(h) < 15:
            return None
        ranges = [max(v['high']-v['low'], abs(v['high']-p['close']),
                      abs(v['low']-p['close'])) for p, v in zip(h[:-1], h[1:])]
        a = float(np.mean(ranges[-14:]))
        return a if math.isfinite(a) and a > 0 else None

    @staticmethod
    def _entropy(closes):
        counts = {}
        for i in range(len(closes)-2):
            triple = closes[i:i+3]
            if len(set(triple)) != 3:
                return None
            key = tuple(int(v) for v in np.argsort(triple))
            counts[key] = counts.get(key, 0)+1
        total = sum(counts.values())
        entropy = -sum((n/total)*math.log(n/total) for n in counts.values())/math.log(6)
        return {'h': entropy, 'up': counts.get((0, 1, 2), 0), 'down': counts.get((2, 1, 0), 0)}

    def _record_event(self, event):
        if event is not None:
            self.vars['events'] = self.vars.get('events', 0)+1
            if self.is_open:
                self.vars['occupied_events'] = self.vars.get('occupied_events', 0)+1
        self.vars['event'] = event

    def before(self):
        self.vars.update(event=None, phase_exit=False, daily_completed=False)
        self.vars.setdefault('history', [])
        self.vars.setdefault('blocks', [])
        self.vars.setdefault('d_seq', 0)
        self.vars.setdefault('b_seq', 0)
        opened = self._local(self.closed_candle_open_time)
        day = opened.date().isoformat()
        minute = opened.hour*60+opened.minute
        if self.vars.get('session_day') != day:
            self.vars.update(session_day=day, day_bars=[], day_invalid=True,
                             block_key=None, block_rows=[], block_invalid=True)
        if not self.is_trading_hours:
            return
        c = self.session_candles
        if not len(c) or int(c[-1, 0]) != self.closed_candle_open_time:
            return
        # Each2h group has an independent completeness gate. A missing early
        # bar invalidates daily OHLC, not an unrelated complete afternoon block.
        if minute < 930:
            group = (minute-570)//120
            key = (day, group)
            if self.vars['block_key'] != key:
                self.vars.update(block_key=key, block_rows=[],
                                 block_invalid=(minute != 570+120*group))
        if minute == 570:
            self.vars.update(day_bars=[], day_invalid=False)
        if not self._complete_bar():
            self.vars['day_invalid'] = True
            self.vars['block_invalid'] = True
            self.vars['missing_bars'] = self.vars.get('missing_bars', 0)+1
            return
        bar = c[-1].copy()
        day_bars = self.vars['day_bars']
        if day_bars and int(bar[0]-day_bars[-1][0]) != HALF:
            self.vars['day_invalid'] = True
        day_bars.append(bar)
        h = self.vars['history']
        a = self._atr(h)
        if minute == 570 and a:
            self._record_event(self._opening_signal(h, bar, day, a))
        if minute < 930:
            rows = self.vars['block_rows']
            if rows and int(bar[0]-rows[-1][0]) != HALF:
                self.vars['block_invalid'] = True
            rows.append(bar)
            if len(rows) == 4 and not self.vars['block_invalid']:
                block = np.array([rows[0][0], rows[0][1], rows[-1][2],
                                  max(v[3] for v in rows), min(v[4] for v in rows), 0.])
                blocks = self.vars['blocks']
                blocks.append(block)
                self.vars['blocks'] = blocks[-300:]
                self.vars['b_seq'] += 1
                if a:
                    self._record_event(self._block_signal(self.vars['blocks'], h, a))
        decision = self._local(self.time)
        if (decision.hour, decision.minute) != (16, 0) or self.vars['day_invalid'] or len(day_bars) != 13:
            return
        closes = [float(v[2]) for v in day_bars]
        self.vars['d_seq'] += 1
        d = {'day': day, 'time': int(self.time), 'seq': self.vars['d_seq'],
             'open': float(day_bars[0][1]), 'close': closes[-1],
             'high': max(float(v[3]) for v in day_bars),
             'low': min(float(v[4]) for v in day_bars), 'closes30': closes,
             'a_prev': a, 'entropy': self._entropy(closes)}
        previous = h[-1] if h else None
        d['gap'] = (math.log(d['open']/previous['close'])
                    if previous and previous['day'] == self._civil_previous(day) else None)
        d['cash'] = math.log(d['close']/d['open'])
        # The partition telescopes to cash return, including interbar jumps.
        d['intraday_returns'] = np.log(np.array(closes)/np.array([d['open']]+closes[:-1])).tolist()
        change = d['close']-previous['close'] if previous else 0.
        sign = 1 if change > 0 else (-1 if change < 0 else 0)
        run = previous['run']+1 if previous and sign and previous['run_sign'] == sign else (1 if sign else 0)
        d.update(run_sign=sign, run=run)
        h.append(d)
        self.vars['history'] = h[-400:]  # Technical retention exceeds252/180D lookbacks.
        self.vars['daily_completed'] = True
        if a:
            self._record_event(self._daily_signal(self.vars['history'], a))

    def _opening_signal(self, h, bar, day, a):
        return None

    def _block_signal(self, blocks, h, a):
        return None

    def _daily_signal(self, h, a):
        return None

    def _event(self, side, a, hours, target=None, next_daily=False):
        if target is not None and side*(target-self.price) <= 0:
            return None
        distance = 2*a
        if not 0 < distance < self.price:
            return None
        return {'side': side, 'distance': distance, 'hours': hours,
                'target': target, 'next_daily': next_daily}

    def _plan(self):
        event = self.vars.get('event')
        if self.symbol != 'SPY-USDT' or len(self.routes) != 1 or not event or self._fix() is None:
            return 0
        entry = float(self.price)
        stop = entry-event['side']*event['distance']
        capital = max(0., min(float(self.balance), float(self.portfolio_value)))
        unit = event['distance']+self.fee_rate*(entry+stop)+RESERVE*entry
        qty = min(capital*RISK/unit, capital*GROSS/entry,
                  max(0., self.leveraged_available_margin*0.90)/entry)
        qty = math.floor(qty/0.001)*0.001  # Research precision, not venue-lot certification.
        if qty <= 0:
            return 0
        self.vars['plan'] = dict(event, qty=qty)
        return event['side']

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
        self.stop_loss = abs(self.position.qty), entry-p['side']*p['distance']
        if p['target'] is not None:
            self.take_profit = abs(self.position.qty), p['target']
        self.vars.update(opened_at=int(self.position.opened_at), hold_ms=p['hours']*3600000,
                         entry_d_seq=self.vars['d_seq'], next_daily=p['next_daily'], exit_debt=False)

    def update_position(self):
        next_day = (self.vars.get('next_daily') and self.vars['daily_completed']
                    and self.vars['d_seq'] > self.vars['entry_d_seq'])
        due = next_day or self.vars.get('phase_exit') or self.time-self.vars['opened_at'] >= self.vars['hold_ms']
        if due:
            self.vars['exit_debt'] = True
        # Debt survives leaving the signal's calendar; stops never switch off.
        if self.vars.get('exit_debt') and self._fix() is not None:
            self.liquidate()

    def _cross_state(self, key, state):
        old = self.vars.get(key, 0)
        self.vars[key] = state
        return state != 0 and state != old

    def _daily_signal(self, h, a):
        d = h[-1]
        r = np.array(d['intraday_returns'])
        rv = float(np.square(r).sum())
        if rv <= 0:
            return None
        # Thirteen intervals: a heuristic decomposition, not an asymptotic jump test.
        bv = (math.pi/2)*(13/12)*float(np.abs(r[1:]*r[:-1]).sum())
        fraction = max(rv-bv, 0.)/rv
        total = float(r.sum())
        if fraction < 1/3 or abs(total) < 0.5*a/h[-2]['close']:
            return None
        return self._event(-1 if total > 0 else 1, a, 72)

