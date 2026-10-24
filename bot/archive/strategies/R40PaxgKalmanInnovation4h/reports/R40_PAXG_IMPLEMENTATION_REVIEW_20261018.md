# R40 PAXG: revisión de implementación antes de backtests

Estado: diez clases autocontenidas creadas y validadas por write_strategy; readback completo exacto 10/10. No hay ningún backtest R40 PAXG lanzado. Root revisó y aprobó motor y diez señales con dos ajustes ya aplicados; autorizado iniciar tras confirmación.

Protocolo con adenda definitiva: strategies/R20PaxgARResponse4h/reports/R40_PAXG_TEN_EXPERIMENTS_PROTOCOL_20261018.md.

Se generaron desde un template. El prefijo de cada readback normalizando nombre/docstring es exactamente el motor de abajo. Cada sufijo es el bloque señalado; no existe módulo común externo mutable. Nuevos archivos exclusivamente R40Paxg*, referencia, R20 y candidata anterior intactos.

Durante revisión propia anterior a runs se añadió latch persistente r40_exit_debt: una salida por modelo o tiempo disparada sin quote fresca no desaparece al resetear flags de la siguiente vela. Reinicia al fill nuevo. Esto implementa el contrato previo, sin cambiar señal ni horizonte. No hubo ejecución económica ni error runtime para descubrirlo.

Kalman 62 precios; estacionalidad con close/close y continuidad exacta, 90 muestras/bucket más cierre anterior; FFT en ventana pasada; días/semanas completos; fijaciones beta excluyen actual y exit congela parámetros. Los helpers de calendario sólo se invocan donde corresponde. before actualiza todos los estados aunque ocupado, motor no mantiene cola de señales. target de Kalman se calcula a partir del nivel predictivo anterior al update y permanece absoluto mediante fixed_target. Los demás TP ATR expresados como distancia en evento se instalan respecto a fill real; MARKET en motor actual usa el cierre validado.

No se ejecuta shell ni compilador externo: create/write_strategy validaron sintaxis/estructura mediante API; el primer full verifica ejecución real. No son tests unitarios de framework. KAMA/RSI/ATR documentados por get_indicator_details. ATR mantiene default 14; otros parámetros están explícitos en protocolo humano revisado.

## Prueba de readback

| ID | Clase | Caracteres | Igual al contenido enviado |
|---|---|---:|---|
| 1 | R40PaxgKalmanInnovation4h | 8405 | true |
| 2 | R40PaxgLearnedSeason4h | 9005 | true |
| 3 | R40PaxgSpectralProjection4h | 8295 | true |
| 4 | R40PaxgWickBalance4h | 7986 | true |
| 5 | R40PaxgKamaHysteresis4h | 8099 | true |
| 6 | R40PaxgRangeCenterLead4h | 7849 | true |
| 7 | R40PaxgWeeklyDailyPullback4h | 8679 | true |
| 8 | R40PaxgDrawdownRecovery4h | 9853 | true |
| 9 | R40PaxgCusumDrift4h | 8014 | true |
| 10 | R40PaxgBetaResidual1h | 9028 | true |

## Motor común (CLASSNAME/docstring normalizados)

```python
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



```

## PAXG40-01 — R40PaxgKalmanInnovation4h

```python
    def _model_event(self):
        """Local-level innovation reversal. Fixed Q/R ratios keep the state slower than noise; 1.5 is an ex-ante event boundary, not fitted."""
        c = self.candles
        if len(c) < 62:
            return None
        x = np.log(c[-62:, 2])
        variance = float(np.var(np.diff(x[:-1]), ddof=1))
        if not math.isfinite(variance) or variance <= 0:
            self.vars.pop('kalman', None)
            self._regime_event('kalman_regime', 0)
            return None
        q, r = 0.01*variance, 0.25*variance
        m, p = self.vars.get('kalman', (float(x[-2]), r))
        pp = p+q
        innovation, s = float(x[-1])-m, pp+r
        z = innovation/math.sqrt(s)
        k = pp/s
        # Signal uses the predictive level and covariance BEFORE this update.
        self.vars['kalman'] = (m+k*innovation, (1-k)*pp)
        state = 1 if z >= 1.5 else -1 if z <= -1.5 else 0
        if not self._regime_event('kalman_regime', state):
            return None
        direction = -state
        target_distance = direction*(math.exp(m)-float(self.price))
        atr = self._atr()
        if target_distance <= 0 or atr is None:
            return None
        return self._event(direction, atr, 48, fixed_target=math.exp(m))

```

## PAXG40-02 — R40PaxgLearnedSeason4h

```python
    def _model_event(self):
        """Ninety mature labels per UTC bucket estimate a rolling season. Top/bottom ranking uses all buckets and freezes at midnight."""
        c = self.candles
        now = datetime.fromtimestamp(int(self.time)/1000, tz=ZoneInfo('UTC'))
        if now.hour == 0 and len(c) >= 541:
            # Mature close-to-close labels align with the previous close entry.
            values = {h: [] for h in (0, 4, 8, 12, 16, 20)}
            # Collect the latest 90 VALID observations per bucket, without an arbitrary bar cap.
            for i in range(len(c)-1, 0, -1):
                if int(c[i, 0]-c[i-1, 0]) != 4*HOUR_MS:
                    continue
                h = datetime.fromtimestamp(int(c[i, 0])/1000,
                                           tz=ZoneInfo('UTC')).hour
                if h in values and len(values[h]) < 90 and c[i, 2] > 0 and c[i-1, 2] > 0:
                    values[h].append(math.log(c[i, 2]/c[i-1, 2]))
                if all(len(v) >= 90 for v in values.values()):
                    break
            if all(len(v) >= 90 for v in values.values()):
                means = {h: float(np.mean(v[-90:])) for h, v in values.items()}
                if max(means.values()) > min(means.values()):
                    best = sorted(means, key=lambda h: (-means[h], h))[0]
                    worst = sorted(means, key=lambda h: (means[h], h))[0]
                    self.vars['season_rank'] = (now.date().isoformat(), best, worst, means)
        rank = self.vars.get('season_rank')
        if not rank or rank[0] != now.date().isoformat():
            return None
        _, best, worst, means = rank
        direction = 1 if now.hour == best and means[best] > 0 else (
            -1 if now.hour == worst and means[worst] < 0 else 0)
        return self._event(direction, self._atr(), 4) if direction else None

```

## PAXG40-03 — R40PaxgSpectralProjection4h

```python
    def _model_event(self):
        """192 bars span about a month; frequencies 1..8 restrict the fit to slow components. Half-ATR forecast threshold and 24h exit are fixed."""
        if len(self.candles) < 192:
            return None
        x = np.log(self.candles[-192:, 2])
        t = np.arange(192, dtype=float)
        design = np.column_stack((np.ones(192), t))
        residual = x-design@np.linalg.lstsq(design, x, rcond=None)[0]
        energy = np.abs(np.fft.rfft(residual))[1:9]**2
        freq = int(np.argmax(energy))+1
        omega = 2*math.pi*freq/192
        harmonic = np.column_stack((np.ones(192), np.sin(omega*t), np.cos(omega*t)))
        coef = np.linalg.lstsq(harmonic, residual, rcond=None)[0]
        projected = (coef[1]*(math.sin(omega*197)-math.sin(omega*191))+
                     coef[2]*(math.cos(omega*197)-math.cos(omega*191)))
        atr = self._atr()
        state = (1 if projected > 0 else -1) if (
            atr is not None and abs(projected) >= 0.5*atr/float(self.price)) else 0
        if not self._regime_event('spectral_regime', state):
            return None
        return self._event(state, atr, 24)

```

## PAXG40-04 — R40PaxgWickBalance4h

```python
    def _model_event(self):
        """Eight-bar wick balance measures repeated rejection, not volume. The 0.20 balance and one-ATR displacement limits are ex-ante."""
        c = self.candles
        if len(c) < 40:
            return None
        a = c[-8:]
        total = float(np.sum(a[:, 3]-a[:, 4]))
        if total <= 0:
            self._regime_event('wick_regime', 0)
            return None
        lower = np.minimum(a[:, 1], a[:, 2])-a[:, 4]
        upper = a[:, 3]-np.maximum(a[:, 1], a[:, 2])
        b = float(np.sum(lower-upper)/total)
        state = 1 if b >= 0.20 else -1 if b <= -0.20 else 0
        crossed = self._regime_event('wick_regime', state)
        atr = self._atr(c[:-8])
        if not crossed or atr is None or abs(c[-1, 2]-c[-9, 2]) > atr:
            return None
        return self._event(state, atr, 48, target=3)

```

## PAXG40-05 — R40PaxgKamaHysteresis4h

```python
    def _model_event(self):
        """KAMA20 adapts to path efficiency; half-ATR hysteresis separates entry and exit bands. Three-ATR stop and 20-day expiry are fixed."""
        c = self.candles
        if len(c) < 60:
            return None
        atr = self._atr()
        if atr is None:
            return None
        value = float(ta.kama(c, period=20, fast_length=2, slow_length=30))
        if not math.isfinite(value):
            return None
        price = float(self.price)
        state = 1 if price > value+0.5*atr else -1 if price < value-0.5*atr else 0
        crossed = self._regime_event('kama_regime', state)
        # The opposite band closes; no same-bar reversal or queued crossing.
        self.vars['r40_custom_exit'] = bool(
            (self.is_long and price <= value-0.5*atr) or
            (self.is_short and price >= value+0.5*atr))
        if crossed:
            return self._event(state, atr, 480, stop=3)
        return None

```

## PAXG40-06 — R40PaxgRangeCenterLead4h

```python
    def _model_event(self):
        """Two six-bar centers detect a range-location lead. The 0.75/0.5 ATR boundaries separate midpoint movement from lagging closes."""
        c = self.candles
        if len(c) < 44:
            return None
        atr = self._atr(c[:-12])
        if atr is None:
            return None
        centers = (c[-12:, 3]+c[-12:, 4])/2
        lead = float(np.mean(centers[-6:])-np.mean(centers[:6]))
        qualifies = abs(lead) >= 0.75*atr and abs(c[-1, 2]-c[-13, 2]) <= 0.5*atr
        state = (1 if lead > 0 else -1) if qualifies else 0
        if not self._regime_event('range_lead_regime', state):
            return None
        return self._event(state, atr, 48, target=3)

```

## PAXG40-07 — R40PaxgWeeklyDailyPullback4h

```python
    def _model_event(self):
        """Four/eight completed weeks define context; RSI2 daily 20/80 captures a short pullback. No forming daily or weekly bar is used."""
        if int(self.time) % (24*HOUR_MS) != 0:
            return None
        c = self.candles
        daily = self._aggregate(c, 24*HOUR_MS)
        # Epoch is Thursday; +4 days anchors complete weeks to Monday UTC.
        weekly = self._aggregate(c, 7*24*HOUR_MS, 4*24*HOUR_MS)
        if len(daily) < 30 or len(weekly) < 8:
            return None
        if int(daily[-1, 0])+24*HOUR_MS != int(self.time):
            return None
        short_mean, long_mean = np.mean(weekly[-4:, 2]), np.mean(weekly[-8:, 2])
        trend = 1 if short_mean > long_mean else -1 if short_mean < long_mean else 0
        rsi = float(ta.rsi(daily, period=2))
        if not math.isfinite(rsi):
            return None
        previous_trend = self.vars.get('pullback_trend')
        armed = self.vars.get('pullback_armed', 0)
        if trend != previous_trend:
            armed = 0
        self.vars['pullback_trend'] = trend
        event = None
        if armed == 1 and trend == 1 and rsi >= 20:
            event, armed = self._event(1, self._atr(daily), 120), 0
        elif armed == -1 and trend == -1 and rsi <= 80:
            event, armed = self._event(-1, self._atr(daily), 120), 0
        elif trend == 1 and rsi < 20:
            armed = 1
        elif trend == -1 and rsi > 80:
            armed = -1
        self.vars['pullback_armed'] = armed
        return event

```

## PAXG40-08 — R40PaxgDrawdownRecovery4h

```python
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

```

## PAXG40-09 — R40PaxgCusumDrift4h

```python
    def _model_event(self):
        """Reference drift 0.25 sigma and boundary 4 are fixed CUSUM design choices; normalization excludes the current return."""
        if len(self.candles) < 62:
            return None
        r = np.diff(np.log(self.candles[-62:, 2]))
        sigma = float(np.std(r[:-1], ddof=1))
        if not math.isfinite(sigma) or sigma <= 0:
            self.vars['cusum'] = (0.0, 0.0)
            return None
        z = float((r[-1]-np.mean(r[:-1]))/sigma)
        up, down = self.vars.get('cusum', (0.0, 0.0))
        up, down = max(0.0, up+z-0.25), max(0.0, down-z-0.25)
        if up >= 4 or down >= 4:
            self.vars['cusum'] = (0.0, 0.0)
            if up >= 4 and down >= 4:
                return None
            return self._event(1 if up >= 4 else -1, self._atr(), 48, target=4)
        self.vars['cusum'] = (up, down)
        return None

```

## PAXG40-10 — R40PaxgBetaResidual1h

```python
    def _model_event(self):
        """Sixty prior paired loglevels estimate a descriptive beta, not cointegration. The 1.5-sigma event and five-day expiry are fixed."""
        fixes = self._paired_fix()
        if not fixes:
            return None
        current = fixes[-1]
        x_now, y_now = math.log(current['spy']), math.log(current['own'])
        # Exit uses coefficients frozen at fill, independent of today's refit.
        plan = self.vars.get('r40_open_plan', {})
        if (self.is_long or self.is_short) and 'beta' in plan:
            residual = y_now-plan['alpha']-plan['beta']*x_now
            self.vars['r40_custom_exit'] = bool(
                (self.is_long and residual >= plan['residual_mean']) or
                (self.is_short and residual <= plan['residual_mean']))
        if len(fixes) < 61:
            return None
        train = fixes[-61:-1]
        x = np.log([q['spy'] for q in train])
        y = np.log([q['own'] for q in train])
        xc = x-np.mean(x)
        denominator = float(np.dot(xc, xc))
        if denominator <= 0 or not math.isfinite(denominator):
            self._regime_event('beta_regime', 0)
            return None
        beta = float(np.dot(xc, y-np.mean(y))/denominator)
        alpha = float(np.mean(y)-beta*np.mean(x))
        residuals = y-alpha-beta*x
        mean = float(np.mean(residuals))
        sigma = float(np.std(residuals, ddof=1))
        if not all(math.isfinite(q) for q in (alpha, beta, mean, sigma)) or sigma <= 0:
            self._regime_event('beta_regime', 0)
            return None
        z = (y_now-alpha-beta*x_now-mean)/sigma
        state = 1 if z >= 1.5 else -1 if z <= -1.5 else 0
        if not self._regime_event('beta_regime', state):
            return None
        return self._event(-state, self._fourhour_atr(), 120,
                           beta=beta, alpha=alpha, residual_mean=mean)

```

## Formulario previsto

Diez fulls en cola fija 01..10, máximo dos propios simultáneos. Todos 2020-10-15→2025-12-31 exclusiva, modo normal, misma configuración actual 10k/.00045/5x isolated/warmup240. 01–09: PAXG-USDT 4h + data PAXG1m. 10: PAXG1h + data PAXG1m, PAXG4h y SPY1m. No rutas SPY de trading. Historia de entrenamiento crece en la ventana conocida; no consultar velas por preflight ni modificar gates tras resultados. Guardar sesiones y enlaces reales retornados. Esperar aprobación de esta revisión antes de lanzar 01/02.

## Readback final tras revisión de root

[{"id":1,"name":"R40PaxgKalmanInnovation4h","exact":true,"characters":8405},{"id":2,"name":"R40PaxgLearnedSeason4h","exact":true,"characters":9005},{"id":3,"name":"R40PaxgSpectralProjection4h","exact":true,"characters":8295},{"id":4,"name":"R40PaxgWickBalance4h","exact":true,"characters":7986},{"id":5,"name":"R40PaxgKamaHysteresis4h","exact":true,"characters":8099},{"id":6,"name":"R40PaxgRangeCenterLead4h","exact":true,"characters":7849},{"id":7,"name":"R40PaxgWeeklyDailyPullback4h","exact":true,"characters":8679},{"id":8,"name":"R40PaxgDrawdownRecovery4h","exact":true,"characters":9853},{"id":9,"name":"R40PaxgCusumDrift4h","exact":true,"characters":8014},{"id":10,"name":"R40PaxgBetaResidual1h","exact":true,"characters":9028}]

Se aplicaron antes de runs los dos ajustes de conformidad aprobados: fixed_target absoluto en 01, y búsqueda inversa de últimos 90 labels válidos/bucket sin límite arbitrario en 02. Prefijo común actualizado en diez clases. create/write y readbacks finales succeeded y exactos; no se alteraron 03–10. Root autorizó iniciar tras esta confirmación, sin nueva hipótesis ni resultado observado.
