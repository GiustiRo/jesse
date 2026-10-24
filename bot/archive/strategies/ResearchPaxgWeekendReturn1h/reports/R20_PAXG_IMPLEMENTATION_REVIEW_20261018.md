# R20 PAXG: fuente común y diez señales para revisión previa

Diez clases autocontenidas, sin import de mixin externo. Se creó cada fuente por MCP y su readback completo es idéntico al template renderizado. No hay runs PAXG R20 iniciados. Configuración de datos/TF en la matriz definitiva. Este archivo sirve para revisar una copia común; cada strategy_codes conservará su clase completa.

Aclaración técnica del ID02, anterior a resultados: las ventanas históricas elegidas se separan ocho barras entre sí Y de la ventana actual. Cada etiqueta usa exactamente el retorno de seis barras siguientes al origen pasado; con esa separación madura al menos dos barras antes del origen actual. Esto evita solapamiento de inputs actuales/entrenamiento, sin información futura. No se ajustó tras resultados.

## Motor común

Sustituir CLASSNAME y EXPERIMENT por los valores de cada fila y SIGNAL_BLOCK por su bloque siguiente.

```python
import math
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta

TRADE_RISK = 0.01
NOTIONAL_CAP = 4.4
SLIPPAGE_RESERVE = 0.001  # Sizing only; fills do not simulate these extra costs.
FEE_FORECAST_HURDLE = 0.0019  # Fixed 9 bps modeled round trip plus 10 bps reserve.
NEW_YORK = ZoneInfo('America/New_York')
HOUR_MS = 3600000


class CLASSNAME(Strategy):
    """EXPERIMENT: predeclared price-only development, not independent validation."""

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
        # These models need at most 22 observations; retain a wider history for gaps.
        self.vars['paired_fixes'] = fixes[-200:]
        return self.vars['paired_fixes']

    def before(self) -> None:
        if self.vars.get('processed_index') == self.index:
            return
        self.vars['processed_index'] = self.index
        # State and episode consumption run even when a position is open.
        # An occupied event is discarded on the next bar, never queued.
        self.vars['r20_event'] = self._model_event()

    def _signal(self) -> int:
        if self.vars.get('signal_index') == self.index:
            return self.vars['signal_value']
        self.vars['signal_index'] = self.index
        self.vars['signal_value'] = 0
        event = self.vars.get('r20_event')
        if self.symbol != 'PAXG-USDT' or not event or self._fresh_quote() is None:
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
        self.vars['r20_plan'] = dict(event, qty=qty, entry=entry)
        self.vars['signal_value'] = direction
        return direction

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        self.buy = self.vars['r20_plan']['qty'], self.price

    def go_short(self) -> None:
        self.sell = self.vars['r20_plan']['qty'], self.price

    def should_cancel_entry(self) -> bool:
        # Entries are MARKET; unexpected pending entries cannot persist.
        return True

    def on_open_position(self, order) -> None:
        plan = self.vars['r20_plan']
        self.vars['r20_opened'] = int(self.position.opened_at)
        self.vars['r20_hours'] = float(plan['hours'])
        self.vars['r20_month_exit'] = bool(plan.get('month_exit', False))
        self.vars['r20_open_month'] = self._local_time().strftime('%Y-%m')
        self.vars['r20_exit_fixings'] = 0
        entry = float(self.position.entry_price)
        direction = 1 if self.is_long else -1
        self.stop_loss = abs(self.position.qty), entry-direction*plan['distance']
        if plan.get('tp') is not None:
            self.take_profit = abs(self.position.qty), entry+direction*plan['tp']

    def update_position(self) -> None:
        elapsed = int(self.time)-self.vars['r20_opened']
        due = elapsed >= self.vars['r20_hours']*HOUR_MS
        if self.vars.get('r20_month_exit'):
            due = due or self.vars.get('r20_exit_fixings', 0) >= 3
        if due and self._fresh_quote() is not None:
            self.liquidate()

SIGNAL_BLOCK

```

## Bloques de señal exactos

### PAXG20-01 — R20PaxgARResponse4h

```python
    def _model_event(self):
        if self.is_open:
            return None
        c = self.candles
        if len(c) < 242:
            return None
        close = c[-242:, 2].astype(float)
        if not np.all(np.isfinite(close)) or np.any(close <= 0):
            return None
        r = np.diff(np.log(close))
        x, y = r[:-1], r[1:]
        variance = float(np.mean((x-x.mean())**2))
        if variance <= 0 or not math.isfinite(variance):
            return None
        beta = float(np.mean((x-x.mean())*(y-y.mean()))/variance)
        intercept = float(y.mean()-beta*x.mean())
        # No hidden clipping: an explosive fit is a model risk, not a new filter.
        forecast, value = 0.0, float(r[-1])
        for _ in range(6):
            value = intercept+beta*value
            forecast += value
        atr = self._atr()
        if atr is None or not math.isfinite(forecast) or abs(forecast) <= FEE_FORECAST_HURDLE:
            return None
        return {'direction': 1 if forecast > 0 else -1,
                'distance': 2*atr, 'tp': None, 'hours': 24}

```

### PAXG20-02 — R20PaxgPathAnalogue4h

```python
    def _model_event(self):
        if self.is_open:
            return None
        c = self.candles
        n = len(c)
        if n < 740:
            return None
        close = c[:, 2].astype(float)
        if not np.all(np.isfinite(close)) or np.any(close <= 0):
            return None
        r = np.diff(np.log(close))
        atrs = ta.atr(c, sequential=True)
        j = n-1
        # Origin k's label ends at k+6. Leave eight bars to the current
        # pattern as well, avoiding overlapping training/current input windows.
        origins = np.arange(max(8, j-720), j-8+1, dtype=int)
        scales = atrs[origins-8]/close[origins-8]
        valid = np.isfinite(scales) & (scales > 0)
        origins, scales = origins[valid], scales[valid]
        current_scale = float(atrs[j-8]/close[j-8])
        if len(origins) < 20 or not math.isfinite(current_scale) or current_scale <= 0:
            return None
        # One ATR series and a vectorized view, not 720 repeated indicator calls.
        windows = np.lib.stride_tricks.sliding_window_view(r, 8)
        current = windows[j-8]/current_scale
        vectors = windows[origins-8]/scales[:, None]
        distances = np.sum((vectors-current)**2, axis=1)
        chosen = []
        for ix in np.argsort(distances):
            origin = int(origins[ix])
            if all(abs(origin-other) >= 8 for other in chosen):
                chosen.append(origin)
                if len(chosen) == 20:
                    break
        if len(chosen) < 20:
            return None
        chosen = np.array(chosen, dtype=int)
        forecast = float(np.mean(np.log(close[chosen+6]/close[chosen])))
        atr = self._atr()
        if atr is None or not math.isfinite(forecast) or abs(forecast) <= FEE_FORECAST_HURDLE:
            return None
        return {'direction': 1 if forecast > 0 else -1,
                'distance': 2*atr, 'tp': None, 'hours': 24}

```

### PAXG20-03 — R20PaxgSpyDelayed1h

```python
    def _model_event(self):
        fixes = self._paired_fix()
        if fixes is None or len(fixes) < 22:
            return None
        # Both assets use dimensionless log returns over the same 23-25h interval.
        returns = []
        for old, new in zip(fixes[:-1], fixes[1:]):
            lag = (new['time']-old['time'])/HOUR_MS
            if 23 <= lag <= 25:
                returns.append((new['time'], math.log(new['own']/old['own']),
                                math.log(new['spy']/old['spy'])))
        if len(returns) < 21 or returns[-1][0] != fixes[-1]['time']:
            return None
        previous = np.array([row[1:] for row in returns[-21:-1]], dtype=float)
        sig_own, sig_spy = np.std(previous, axis=0, ddof=1)
        own, spy = returns[-1][1:]
        if not (sig_own > 0 and sig_spy > 0 and math.isfinite(sig_own) and math.isfinite(sig_spy)):
            return None
        if not (abs(spy) >= 2*sig_spy and abs(own) <= 0.25*sig_own):
            return None
        atr = self._fourhour_atr()
        if atr is None:
            return None
        return {'direction': -1 if spy > 0 else 1,
                'distance': 2*atr, 'tp': None, 'hours': 24}

```

### PAXG20-04 — R20PaxgDirectionalOvershoot1h

```python
    def _model_event(self):
        atr = self._atr()
        if atr is None:
            return None
        price = float(self.price)
        state = self.vars.get('dc_state')
        if state is None:
            self.vars['dc_state'] = {'direction': 0, 'extreme': price, 'h': 2*atr}
            return None
        direction, extreme, h = state['direction'], state['extreme'], state['h']
        new_direction = None
        if direction == 0:
            if price >= extreme+h:
                new_direction = 1
            elif price <= extreme-h:
                new_direction = -1
        elif direction == 1:
            extreme = max(extreme, price)
            if price <= extreme-h:
                new_direction = -1
        else:
            extreme = min(extreme, price)
            if price >= extreme+h:
                new_direction = 1
        if new_direction is None:
            state['extreme'] = extreme
            return None
        # The event uses the old, precommitted threshold; the next leg gets a new H.
        self.vars['dc_state'] = {'direction': new_direction, 'extreme': price, 'h': 2*atr}
        return {'direction': new_direction, 'distance': h, 'tp': 2*h, 'hours': 24}

```

### PAXG20-05 — R20PaxgRoundBarrier1h

```python
    def _model_event(self):
        c = self.candles
        atr = self._atr(c[:-1]) if len(c) else None
        if atr is None or len(c) < 2:
            return None
        consumed = self.vars.setdefault('round_consumed', {})
        rearmed_now = set()
        for level in list(consumed):
            if abs(float(self.price)-level) > atr:
                consumed.pop(level)
                rearmed_now.add(level)
        first = math.ceil(float(self.low)/50)
        last = math.floor(float(self.high)/50)
        # Multiple crossed barriers are ambiguous; never select a favorable one.
        if last-first+1 != 1:
            return None
        level = float(first*50)
        if level in consumed or level in rearmed_now:
            return None
        previous, close = float(c[-2, 2]), float(self.price)
        direction = None
        if previous < level and float(self.high) >= level+0.25*atr and close < level:
            direction = -1
        elif previous > level and float(self.low) <= level-0.25*atr and close > level:
            direction = 1
        if direction is None:
            return None
        # Consume while occupied as well; a new event needs a later away-close rearmer.
        consumed[level] = int(self.time)
        return {'direction': direction, 'distance': atr, 'tp': 2*atr, 'hours': 12}

```

### PAXG20-06 — R20PaxgBreakevenRevisit4h

```python
    def _model_event(self):
        c = self.candles
        atr = self._atr()
        if atr is None or len(c) < 180:
            return None
        episode = self.vars.get('breakeven_episode')
        if episode is not None:
            if self.index-episode['index'] > 120:
                # Its extreme was consumed on arming, so expiry cannot recycle it.
                self.vars['breakeven_episode'] = None
                return None
            level, scale, side = episode['level'], episode['atr'], episode['side']
            touched = float(self.high) >= level-0.25*scale if side == -1 else float(self.low) <= level+0.25*scale
            if not touched:
                return None
            self.vars['breakeven_episode'] = None
            rejected = float(self.price) < level if side == -1 else float(self.price) > level
            if not rejected:
                return None
            return {'direction': side, 'distance': 2*scale, 'tp': 2*scale, 'hours': 48}
        prior = c[-121:-1]
        hi, lo = int(np.argmax(prior[:, 3])), int(np.argmin(prior[:, 4]))
        used = self.vars.setdefault('breakeven_used', {})
        candidates = []
        for side, ix, column in ((-1, hi, 3), (1, lo, 4)):
            level = float(prior[ix, column])
            stamp = int(prior[ix, 0])
            key = f'{side}:{stamp}'
            age = 120-ix
            depth = level-float(self.price) if side == -1 else float(self.price)-level
            if age >= 6 and depth >= 4*atr and key not in used:
                candidates.append((side, level, key))
        if len(candidates) != 1:
            return None
        side, level, key = candidates[0]
        used[key] = True
        self.vars['breakeven_episode'] = {'side': side, 'level': level,
                                         'atr': atr, 'index': self.index}
        return None

```

### PAXG20-07 — R20PaxgStaircase4h

```python
    def _model_event(self):
        c = self.candles
        if len(c) < 37:
            return None
        changes = np.diff(c[-7:, 2].astype(float))
        latest = 1 if changes[-1] > 0 else (-1 if changes[-1] < 0 else 0)
        consumed = self.vars.get('stair_consumed_sign', 0)
        if consumed and latest and latest != consumed:
            consumed = 0
            self.vars['stair_consumed_sign'] = 0
        atr = self._atr(c[:-6])
        if atr is None:
            return None
        sign = 1 if np.all(changes > 0) else (-1 if np.all(changes < 0) else 0)
        if not sign or consumed == sign:
            return None
        if np.any(np.abs(changes) > 0.75*atr) or abs(float(changes.sum())) < 1.5*atr:
            return None
        self.vars['stair_consumed_sign'] = sign
        return {'direction': sign, 'distance': 2*atr, 'tp': 3*atr, 'hours': 24}

```

### PAXG20-08 — R20PaxgSemivariance4h

```python
    def _model_event(self):
        c = self.candles
        atr = self._atr()
        if atr is None or len(c) < 61:
            return None
        close = c[-61:, 2].astype(float)
        direction = 0
        if np.all(np.isfinite(close)) and np.all(close > 0):
            r = np.diff(np.log(close))
            up = float(np.sum(r[r > 0]**2))
            down = float(np.sum(r[r < 0]**2))
            if up > 0 and down > 0 and abs(float(r.sum())) <= atr/float(close[-1]):
                if up/down >= 3:
                    direction = 1
                elif down/up >= 3:
                    direction = -1
        old = self.vars.get('semivar_direction', 0)
        self.vars['semivar_direction'] = direction
        if not direction or direction == old:
            return None
        return {'direction': direction, 'distance': 2*atr, 'tp': 3*atr, 'hours': 48}

```

### PAXG20-09 — R20PaxgTrendExhaustion4h

```python
    def _model_event(self):
        c = self.candles
        atr = self._atr()
        if atr is None or len(c) < 30:
            return None
        close = c[-30:, 2].astype(float)
        direction = 0
        if np.all(np.isfinite(close)):
            x = np.arange(15, dtype=float)
            x -= x.mean()
            a, b = close[:15], close[15:]
            old_slope = float(np.dot(x, a-a.mean())/np.dot(x, x))
            new_slope = float(np.dot(x, b-b.mean())/np.dot(x, x))
            variance = float(np.sum((a-a.mean())**2))
            if variance > 0:
                residual = a-(a.mean()+old_slope*x)
                r2 = 1-float(np.sum(residual**2))/variance
                change = float(close[-1]-close[0])
                if r2 >= 0.7:
                    if change >= 3*atr and old_slope > 0 and 0 <= new_slope <= 0.25*old_slope:
                        direction = -1
                    elif change <= -3*atr and old_slope < 0 and 0 >= new_slope >= 0.25*old_slope:
                        direction = 1
        old = self.vars.get('exhaustion_direction', 0)
        self.vars['exhaustion_direction'] = direction
        if not direction or direction == old:
            return None
        return {'direction': direction, 'distance': 2*atr, 'tp': None, 'hours': 48}

```

### PAXG20-10 — R20PaxgMonthEndRebalance1h

```python
    def _model_event(self):
        fixes = self._paired_fix()
        if fixes is None:
            return None
        local = self._local_time()
        # Count observed paired fixings, not fabricated business-day candles.
        if self.is_open and local.strftime('%Y-%m') != self.vars.get('r20_open_month'):
            self.vars['r20_exit_fixings'] = self.vars.get('r20_exit_fixings', 0)+1
        if len(fixes) < 22:
            return None
        next_day = local.date()+timedelta(days=1)
        while next_day.weekday() > 4:
            next_day += timedelta(days=1)
        if next_day.month == local.month:
            return None
        month = local.strftime('%Y-%m')
        if self.vars.get('month_consumed') == month:
            return None
        own = np.array([f['own'] for f in fixes[-22:]], dtype=float)
        spy = np.array([f['spy'] for f in fixes[-22:]], dtype=float)
        relative = np.diff(np.log(own))-np.diff(np.log(spy))
        sigma = float(np.std(relative[:-1], ddof=1))
        # sqrt(20) is a fixed scale heuristic, not an IID confidence claim.
        scale = math.sqrt(20)*sigma
        movement = math.log(own[-1]/own[-21])-math.log(spy[-1]/spy[-21])
        if not (math.isfinite(scale) and scale > 0 and math.isfinite(movement)):
            return None
        if abs(movement) < scale:
            return None
        self.vars['month_consumed'] = month
        atr = self._fourhour_atr()
        if atr is None:
            return None
        return {'direction': -1 if movement > 0 else 1,
                'distance': 2*atr, 'tp': None, 'hours': 240, 'month_exit': True}

```

## Readback completo

```json
[
  {
    "id": "PAXG20-01",
    "name": "R20PaxgARResponse4h",
    "same": true,
    "chars": 6524
  },
  {
    "id": "PAXG20-02",
    "name": "R20PaxgPathAnalogue4h",
    "same": true,
    "chars": 7365
  },
  {
    "id": "PAXG20-03",
    "name": "R20PaxgSpyDelayed1h",
    "same": true,
    "chars": 6639
  },
  {
    "id": "PAXG20-04",
    "name": "R20PaxgDirectionalOvershoot1h",
    "same": true,
    "chars": 6666
  },
  {
    "id": "PAXG20-05",
    "name": "R20PaxgRoundBarrier1h",
    "same": true,
    "chars": 6783
  },
  {
    "id": "PAXG20-06",
    "name": "R20PaxgBreakevenRevisit4h",
    "same": true,
    "chars": 7316
  },
  {
    "id": "PAXG20-07",
    "name": "R20PaxgStaircase4h",
    "same": true,
    "chars": 6321
  },
  {
    "id": "PAXG20-08",
    "name": "R20PaxgSemivariance4h",
    "same": true,
    "chars": 6321
  },
  {
    "id": "PAXG20-09",
    "name": "R20PaxgTrendExhaustion4h",
    "same": true,
    "chars": 6745
  },
  {
    "id": "PAXG20-10",
    "name": "R20PaxgMonthEndRebalance1h",
    "same": true,
    "chars": 7078
  }
]
```
