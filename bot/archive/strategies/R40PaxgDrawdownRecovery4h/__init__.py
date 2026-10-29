import math
from datetime import datetime
from zoneinfo import ZoneInfo
import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta

TRADE_RISK = 0.01
NOTIONAL_CAP = 4.4
SLIPPAGE_RESERVE = 0.001  # Sizing only; fills do not simulate these extra costs.
NEW_YORK = ZoneInfo('America/New_York')
HOUR_MS = 3600000


class R40PaxgDrawdownRecovery4h(Strategy):
    """PAXG40-08: predeclared price-only development, not independent validation."""

    def _fresh_quote(self, symbol=None):
        symbol = self.symbol if symbol is None else symbol
        c = self.get_candles(self.exchange, symbol, '1m')
        if not len(c) or int(c[-1, 0]) != int(self.time)-60000:
            return None
        price = float(c[-1, 2])
        if not (math.isfinite(price) and price > 0):
            return None
        if symbol == self.symbol and not math.isclose(
                price, float(self.price), rel_tol=1e-10, abs_tol=1e-8):
            return None
        return price

    def _atr(self, c=None):
        c = self.candles if c is None else c
        if len(c) < 30:
            return None
        value = float(ta.atr(c))
        return value if math.isfinite(value) and value > 0 else None

    def _fourhour_atr(self):
        c = self.get_candles(self.exchange, self.symbol, '4h')
        c = c[c[:, 0]+4*HOUR_MS <= int(self.time)]
        return self._atr(c)

    def _local_time(self):
        return datetime.fromtimestamp(int(self.time)/1000, tz=NEW_YORK)

    def _paired_fix(self):
        local = self._local_time()
        if local.weekday() > 4 or local.hour != 16 or local.minute != 0:
            return None
        own, spy = self._fresh_quote(), self._fresh_quote('SPY-USDT')
        if own is None or spy is None:
            return None
        fixes = self.vars.setdefault('paired_fixes', [])
        day = local.date().isoformat()
        if fixes and fixes[-1]['date'] == day:
            return None
        fixes.append({'date': day, 'time': int(self.time), 'own': own, 'spy': spy})
        # Keep paired observations; models exclude the newly appended fixing in training.
        self.vars['paired_fixes'] = fixes[-200:]
        return self.vars['paired_fixes']

    def before(self) -> None:
        if self.vars.get('processed_index') == self.index:
            return
        self.vars['processed_index'] = self.index
        # State and episode consumption run even when a position is open.
        # An occupied event is discarded on the next bar, never queued.
        self.vars['r40_custom_exit'] = False
        self.vars['r40_event'] = self._model_event()

    def _signal(self) -> int:
        if self.vars.get('signal_index') == self.index:
            return self.vars['signal_value']
        self.vars['signal_index'] = self.index
        self.vars['signal_value'] = 0
        event = self.vars.get('r40_event')
        if (self.symbol != 'PAXG-USDT' or not event or self.vars.get('r40_custom_exit')
                or self._fresh_quote() is None):
            return 0
        entry = float(self.price)
        distance = float(event['distance'])
        direction = int(event['direction'])
        if not (math.isfinite(distance) and 0 < distance < entry and direction in (-1, 1)):
            return 0
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        stop = entry-direction*distance
        unit_risk = distance+self.fee_rate*(entry+stop)+SLIPPAGE_RESERVE*entry
        room = min(capital*NOTIONAL_CAP,
                   max(0.0, float(self.leveraged_available_margin)*0.90))
        qty = min(capital*TRADE_RISK/unit_risk, room/entry)
        # Existing PAXG research precision, not proof of native contract lot rules.
        qty = math.floor(qty/0.0001)*0.0001
        if qty <= 0:
            return 0
        self.vars['r40_plan'] = dict(event, qty=qty, entry=entry)
        self.vars['signal_value'] = direction
        return direction

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        self.buy = self.vars['r40_plan']['qty'], self.price

    def go_short(self) -> None:
        self.sell = self.vars['r40_plan']['qty'], self.price

    def should_cancel_entry(self) -> bool:
        # Entries are MARKET; unexpected pending entries cannot persist.
        return True

    def on_open_position(self, order) -> None:
        plan = self.vars['r40_plan']
        self.vars['r40_opened'] = int(self.position.opened_at)
        self.vars['r40_hours'] = float(plan['hours'])
        self.vars['r40_exit_debt'] = False
        # Frozen exit coefficients belong to the actual fill, not later event models.
        self.vars['r40_open_plan'] = dict(plan)
        entry = float(self.position.entry_price)
        direction = 1 if self.is_long else -1
        self.stop_loss = abs(self.position.qty), entry-direction*plan['distance']
        if plan.get('fixed_target') is not None:
            # Kalman price target is a frozen predictive level, never shifted by fill.
            self.take_profit = abs(self.position.qty), plan['fixed_target']
        elif plan.get('tp') is not None:
            self.take_profit = abs(self.position.qty), entry+direction*plan['tp']

    def update_position(self) -> None:
        elapsed = int(self.time)-self.vars['r40_opened']
        due = elapsed >= self.vars['r40_hours']*HOUR_MS
        due = due or self.vars.get('r40_custom_exit', False) or self.vars.get('r40_exit_debt', False)
        # A stale quote cannot erase an already-triggered model or time exit.
        self.vars['r40_exit_debt'] = bool(due)
        if due and self._fresh_quote() is not None:
            self.liquidate()

    def _regime_event(self, key, state):
        prior = self.vars.get(key, 0)
        self.vars[key] = state
        return bool(state and state != prior)

    def _event(self, direction, atr, hours, stop=2.0, target=None, **extra):
        if atr is None or not math.isfinite(atr) or atr <= 0:
            return None
        event = dict(direction=int(direction), distance=stop*atr, hours=hours)
        if target is not None:
            event['tp'] = target*atr
        event.update(extra)
        return event

    def _aggregate(self, c, span, offset=0):
        # Only exact, contiguous complete OHLC blocks enter higher-timeframe features.
        groups = {}
        for row in c:
            ts = int(row[0])
            bucket = ((ts-offset)//span)*span+offset
            if bucket+span <= int(self.time):
                groups.setdefault(bucket, []).append(row)
        out = []
        expected = span//(4*HOUR_MS)
        for ts, rows in sorted(groups.items()):
            if len(rows) != expected:
                continue
            a = np.asarray(rows)
            if not np.array_equal(a[:, 0], ts+np.arange(expected)*4*HOUR_MS):
                continue
            out.append([ts, a[0, 1], a[-1, 2], np.max(a[:, 3]),
                        np.min(a[:, 4]), np.sum(a[:, 5])])
        return np.asarray(out, dtype=float).reshape((-1, 6))

    def _model_event(self):
        """Sixty bars and minimum age twelve distinguish a mature excursion. Four-ATR depth and half recovery define one consumed episode."""
        c = self.candles
        if len(c) < 61:
            return None
        price = float(self.price)
        episode = self.vars.get('recovery_episode')
        used = self.vars.setdefault('recovery_consumed', {1: -1, -1: -1})
        if episode:
            direction = episode['direction']
            if self.index-episode['armed'] >= 60:
                used[direction] = episode['origin']
                self.vars.pop('recovery_episode', None)
                return None
            if direction == 1:
                episode['turn'] = min(episode['turn'], price)
                depth = episode['anchor']-episode['turn']
                level = episode['turn']+0.5*depth
                trigger = price >= level
            else:
                episode['turn'] = max(episode['turn'], price)
                depth = episode['turn']-episode['anchor']
                level = episode['turn']-0.5*depth
                trigger = price <= level
            if trigger and depth >= 4*episode['atr']:
                used[direction] = episode['origin']
                self.vars.pop('recovery_episode', None)
                return self._event(direction, episode['atr'], 72)
            return None
        atr = self._atr()
        if atr is None:
            return None
        closes = c[-60:, 2]
        # Most recent equal extreme, not an arbitrary first occurrence.
        imax = len(closes)-1-int(np.argmax(closes[::-1]))
        imin = len(closes)-1-int(np.argmin(closes[::-1]))
        candidates = []
        for direction, origin_index in ((1, imax), (-1, imin)):
            age = len(closes)-1-origin_index
            anchor = float(closes[origin_index])
            displacement = direction*(anchor-price)
            origin = int(c[-60+origin_index, 0])
            if age >= 12 and displacement >= 4*atr and origin > used[direction]:
                turn = float(np.min(closes[origin_index:]) if direction == 1
                             else np.max(closes[origin_index:]))
                candidates.append(dict(direction=direction, origin=origin, anchor=anchor,
                                       turn=turn, atr=atr, armed=self.index,
                                       score=displacement/atr))
        if candidates:
            candidates.sort(key=lambda q: -q['score'])
            if len(candidates) == 1 or candidates[0]['score'] > candidates[1]['score']:
                self.vars['recovery_episode'] = candidates[0]
        # Arming and triggering on the same bar is prohibited.
        return None

