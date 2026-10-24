# SPY40 — revisión de implementación previa a resultados

Diez fuentes autocontenidas creadas por Jesse MCP y leídas íntegramente de vuelta. Igualdad exacta contra código congelado: true. Sin backtests iniciados. Matriz, adenda y precisificaciones permanecen en esta carpeta. debug_mode=false, sin modificaciones de configuración global ni instrumentación nueva. Los snapshots de resultados no conservan vars: los fills no certifican oportunidades ocupadas ni estados internos; se informa ese límite.

Motor común reutiliza políticas de R20 pero construye bloques2h completos independientes y sesionesD completas. Todos los estados/features evolucionan en before incluso con posición abierta; sin replay de eventos. A previoD; debt de salidas permanece hasta quote fresh. Retención300B/400D. En10 cada nivel/lado se consume al armar incluso si vence; cierre temprano más allá de barrera invalida, sin reinterpretarlo como test. En09 desempate bins por distancia centroalúltimocierre y luego índice. Revisar también SPY40_IMPLEMENTATION_CLARIFICATIONS_20261018.md antes de aprobar lanzamiento.

## Motor común

```python
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


class CLASSNAME(Strategy):
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

SIGNALCODE

```

## SPY40-01 — R40SpyCausalCycle2h

Readback exacto: true. Fuente completa en strategies/R40SpyCausalCycle2h/__init__.py.

```python
    def _block_signal(self, blocks, h, a):
        if len(blocks) < 100:
            return None
        result = ta.bandpass(np.array(blocks))
        bp, value = float(result.bp), float(result.bp_normalized)
        previous = self.vars.get('cycle_previous')
        snapshots = self.vars.setdefault('cycle_bp', [])
        if not all(math.isfinite(v) for v in (bp, value)):
            self.vars['cycle_previous'] = None
            return None
        # Only values actually observed at their origins form the phase/amplitude.
        amplitude = max(snapshots)-min(snapshots) if len(snapshots) == 20 else None
        self.vars['cycle_previous'] = value
        self.vars['cycle_bp'] = (snapshots+[bp])[-20:]
        if self.is_long and value >= 0.5 or self.is_short and value <= -0.5:
            self.vars['phase_exit'] = True
        if previous is None or amplitude is None or amplitude <= HURDLE*self.price:
            return None
        side = 1 if previous <= -0.5 < value else (-1 if previous >= 0.5 > value else 0)
        return self._event(side, a, 120) if side else None

```

## SPY40-02 — R40SpyJumpComponentFade

Readback exacto: true. Fuente completa en strategies/R40SpyJumpComponentFade/__init__.py.

```python
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

```

## SPY40-03 — R40SpyOccupationFlip

Readback exacto: true. Fuente completa en strategies/R40SpyOccupationFlip/__init__.py.

```python
    def _daily_signal(self, h, a):
        d = h[-1]
        above = sum(c > d['open'] for c in d['closes30'])
        below = sum(c < d['open'] for c in d['closes30'])
        side = (-1 if above >= 10 and d['close'] <= d['open']-0.25*a else
                (1 if below >= 10 and d['close'] >= d['open']+0.25*a else 0))
        return self._event(side, a, 72) if side else None

```

## SPY40-04 — R40SpyOrdinalEntropy

Readback exacto: true. Fuente completa en strategies/R40SpyOrdinalEntropy/__init__.py.

```python
    def _daily_signal(self, h, a):
        current = h[-1]['entropy']
        prior = [v['entropy']['h'] for v in h[:-1] if v['entropy'] is not None][-60:]
        state = 0
        if current is not None and len(prior) == 60:
            difference = current['up']-current['down']
            if current['h'] <= float(np.percentile(prior, 25)) and abs(difference) >= 2:
                state = 1 if difference > 0 else -1
        return self._event(state, a, 72) if self._cross_state('ordinal_state', state) else None

```

## SPY40-05 — R40SpySegmentedResponse

Readback exacto: true. Fuente completa en strategies/R40SpySegmentedResponse/__init__.py.

```python
    def _daily_signal(self, h, a):
        d = h[-1]
        if d['gap'] is None:
            return None
        window = h[-181:]
        x, y = [], []
        for origin, target in zip(window[:-1], window[1:]):
            assert origin['time'] < target['time'] <= self.time
            if origin['gap'] is None or target['time']-origin['time'] > 120*3600000:
                continue
            x.append([1., origin['gap'], origin['cash']])
            y.append(math.log(target['close']/origin['close']))
        if len(y) < 120:
            return None
        x, y = np.array(x[-120:]), np.array(y[-120:])
        beta, residuals, rank, singular = np.linalg.lstsq(x, y, rcond=None)
        if rank != 3 or not bool(np.isfinite(beta).all()):
            return None
        forecast = float(np.dot([1., d['gap'], d['cash']], beta))
        if not math.isfinite(forecast) or abs(forecast) <= HURDLE:
            return None
        return self._event(1 if forecast > 0 else -1, a, 120, next_daily=True)

```

## SPY40-06 — R40SpyRangeCloseInformation

Readback exacto: true. Fuente completa en strategies/R40SpyRangeCloseInformation/__init__.py.

```python
    def _block_signal(self, blocks, h, a):
        if len(blocks) < 22:
            return None
        c = np.array(blocks)
        close_returns = np.diff(np.log(c[-22:-1, 2]))
        ranges = np.log(c[-21:-1, 3]/c[-21:-1, 4])
        cc = float(np.var(close_returns, ddof=0))
        pk = float(np.mean(np.square(ranges)))/(4*math.log(2))
        if pk <= 0 or not all(math.isfinite(v) for v in (cc, pk)):
            self.vars['range_ratio'] = None
            return None
        ratio = cc/pk
        previous = self.vars.get('range_ratio')
        self.vars['range_ratio'] = ratio
        move = float(c[-1, 2]-c[-6, 2])
        if previous is None or not previous <= 1 < ratio or abs(move) < 0.5*a:
            return None
        return self._event(1 if move > 0 else -1, a, 72)

```

## SPY40-07 — R40SpyRunDurationResponse

Readback exacto: true. Fuente completa en strategies/R40SpyRunDurationResponse/__init__.py.

```python
    def _daily_signal(self, h, a):
        current = h[-1]
        if not current['run_sign']:
            return None
        records = []
        for origin, target in zip(h[:-1], h[1:]):
            assert origin['time'] < target['time'] <= self.time
            if target['time']-origin['time'] > 120*3600000:
                continue
            state = (origin['run_sign'], min(origin['run'], 4))
            records.append((state, math.log(target['close']/origin['close'])))
        if len(records) < 252:
            return None
        records = records[-252:]
        state = (current['run_sign'], min(current['run'], 4))
        group = [label for key, label in records if key == state]
        if len(group) < 15:
            return None
        global_mean = float(np.mean([label for key, label in records]))
        forecast = (sum(group)+20*global_mean)/(len(group)+20)
        if not math.isfinite(forecast) or abs(forecast) <= HURDLE:
            return None
        return self._event(1 if forecast > 0 else -1, a, 120, next_daily=True)

```

## SPY40-08 — R40SpyWeeklyAuctionRepair

Readback exacto: true. Fuente completa en strategies/R40SpyWeeklyAuctionRepair/__init__.py.

```python
    def _daily_signal(self, h, a):
        if len(h) < 5:
            return None
        week = h[-5:]
        dates = [datetime.fromisoformat(v['day']).date() for v in week]
        if [d.weekday() for d in dates] != [0, 1, 2, 3, 4] or (dates[-1]-dates[0]).days != 4:
            return None
        high = max(v['high'] for v in week)
        low = min(v['low'] for v in week)
        last_high = max(i for i, v in enumerate(week) if v['high'] == high)
        opening, close = week[0]['open'], week[-1]['close']
        if close <= opening or close >= (high+low)/2 or last_high > 2 or close-opening < a:
            return None
        return self._event(-1, a, 120, target=opening)

```

## SPY40-09 — R40SpyCloseDensityReversion

Readback exacto: true. Fuente completa en strategies/R40SpyCloseDensityReversion/__init__.py.

```python
    def _opening_signal(self, h, bar, day, a):
        if len(h) < 5 or h[-1]['day'] != self._civil_previous(day):
            return None
        window = h[-5:]
        frozen_atr = window[0]['a_prev']
        if frozen_atr is None:
            return None
        width = 0.25*frozen_atr
        groups = {}
        for d in window:
            for price in d['closes30']:
                groups.setdefault(math.floor(price/width), []).append(price)
        # Bins tied by count use distance of their center, then lower bin index.
        key = min(groups, key=lambda k: (-len(groups[k]), abs((k+0.5)*width-h[-1]['close']), k))
        reference = float(np.median(groups[key]))
        move = self.price-reference
        if abs(move) < a:
            return None
        return self._event(-1 if move > 0 else 1, a, 48, target=reference)

```

## SPY40-10 — R40SpyRepeatedBarrierPressure

Readback exacto: true. Fuente completa en strategies/R40SpyRepeatedBarrierPressure/__init__.py.

```python
    def _block_signal(self, blocks, h, a):
        if len(blocks) < 11:
            return None
        b = blocks[-1]
        seq = self.vars['b_seq']
        episode = self.vars.get('pressure_episode')
        if episode and seq-episode['seq'] > 12:
            self.vars['pressure_episode'] = None
            episode = None
        if episode is None:
            upper = max(float(v[3]) for v in blocks[-11:-1])
            lower = min(float(v[4]) for v in blocks[-11:-1])
            if not lower <= self.price <= upper:
                return None
            up, down = upper-self.price, self.price-lower
            if up == down or min(up, down) > 0.5*a:
                return None
            side, level = (1, upper) if up < down else (-1, lower)
            used = self.vars.setdefault('pressure_levels', set())
            key = (side, level)
            if key in used:
                return None
            used.add(key)  # Even an expired setup consumes this level/direction.
            self.vars['pressure_episode'] = {
                'seq': seq, 'side': side, 'level': level, 'a': a, 'tests': 0,
                'extreme': float(b[4] if side == 1 else b[3]), 'pressure': False}
            return None
        side, level, frozen = episode['side'], episode['level'], episode['a']
        beyond = side*(self.price-level) > 0
        # Two failed tests must precede the breakout. An earlier close through
        # the barrier invalidates this setup rather than becoming a hidden test.
        if beyond and episode['tests'] < 2:
            self.vars['pressure_episode'] = None
            return None
        extreme = float(b[4] if side == 1 else b[3])
        test = (b[3] >= level-0.1*frozen and self.price <= level if side == 1 else
                b[4] <= level+0.1*frozen and self.price >= level)
        if episode['tests'] == 0:
            episode['extreme'] = min(episode['extreme'], extreme) if side == 1 else max(episode['extreme'], extreme)
            if test:
                episode.update(tests=1, first_extreme=episode['extreme'], last_test=seq, extreme=None)
        elif episode['tests'] == 1:
            previous = episode['extreme']
            episode['extreme'] = (extreme if previous is None else
                                  (min(previous, extreme) if side == 1 else max(previous, extreme)))
            if test and seq-episode['last_test'] >= 2:
                pressure = side*(episode['extreme']-episode['first_extreme']) > 0
                episode.update(tests=2, pressure=pressure, second_test=seq)
        elif episode['pressure'] and seq > episode['second_test'] and beyond:
            self.vars['pressure_episode'] = None
            return self._event(side, frozen, 120)
        return None

```
