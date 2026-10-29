# BTC Discovery V — protocolo previo: dinámica conjunta BTC/ETH vs AR1 BTC
Fecha UTC2026-10-21. Estado: FUENTES IMPLEMENTADAS y CHECK SINTÉTICO PASSED tras autorización root; pendiente revisión final root/independiente antes de drafts/economía. Estado fue actualizado y releído antes de crear fuentes. Root exige catch sólo np.linalg.LinAlgError numérico tras inputs finitos; errores de contrato/programación no se absorben. V se fija mientras U está en preparación; resultado económico U desconocido al redactar. Este archivo no autoriza economía ni modifica padres. Lecturas/escrituras de fuentes y recibos vía MCP; un análisis técnico temporal supplied-source. No velas observadas, precheck de históricos/importaciones, scripts, framework ni configuración global.

## 1. Pregunta material y límites
¿La representación dinámica conjunta de retornos BTC/ETH aporta un pronóstico BTC24h más útil económicamente que AR1 BTC, manteniendo240pares, horizonte6pasos, hurdle y gestión? Necesidad representacional: G sólo condiciona en retornoBTC previo; VAR1 puede condicionar la transición en ambos retornos y pronosticar recursivamente ambos. No se propone porque otros modelos perdieron, ni para rescatar una dirección/ventana favorable.

No se atribuye una diferencia de PnL exclusivamente al coeficiente ETH→BTC: seis pasos también incorporan la ecuación ETH, su persistencia y feedback BTC→ETH→BTC. No es causalidad económica, neutralidad de mercado, cointegración ni prueba de Granger. ETH es dato, nunca posición, fuente de funding ni ejecución. El estimador es entrenamiento online causal dentro de una trayectoria continua, no walk-forward posthoc ni OOS.

Desarrollo2020–2025 ampliamente observado y seleccionado, incluidos G/J/Q/R/S y ORCH. V es selección adaptativa adicional; el control reaparece y no es muestra independiente. No se declara novedad universal: inventario de nombres, búsquedas dirigidas de sesiones VAR/lead/lag/ETH y lectura de fuentes/antecedentes concretos, no censo exhaustivo de todo código legacy.

## 2. Datos y reloj congelados
BTC-USDT, Binance Perpetual Futures, route trading1m. Data routes BTC-USDT4h y ETH-USDT4h, mismo exchange. No route tradingETH ni M1ETH requerida por V. Se usan datos existentes sin inspección de velas antes del motor, importar ni descargar. El motor informará faltantes; no get_existing_candles ni acceso preliminar al histórico.

Cada cierre UTC4h T, obtener EXACTAS242OHLC cerradas consecutivas por activo mediante closed_window congelado R10. Exigir última apertura T−4h, timestamps idénticos BTC/ETH, todas OHLC finitas/positivas y consistentes, cero imputación, ninguna barra parcial. BTC cierre actual debe coincidir con precio ejecutable observado por la route1m con tolerancia heredada. Fuera de esas fronteras sólo observación M1/gestión protectora heredada.

242cierres producen241retornos log4h por activo. Orden de columnas SIEMPRE BTC,ETH. r_j=(log(CBTC_j/CBTC_{j−1}), log(CETH_j/CETH_{j−1})), j=1..241. X=r_1..r_240; Y=r_2..r_241: EXACTOS240pares. El último Y es retorno cerrado y conocido en T; es lícito entrenar con él. Estado de forecast actual r_241. No añadir fila futura ni desplazar entrenamiento para copiar Q: Q excluía el actual por su definición distinta de referencia contemporánea.

Warmup3004h fijado: headroom superior al lookback242, mismo valor documentado en G, no decisión por PnL. No ampliar window ni rellenar con observaciones válidas más viejas si hay gaps. No supuesto de cobertura hasta ejecución y auditoría. Fechas [2020-10-15,2026-01-01) UTC, START<decision<FINISH según harness congelado; sin nuevas evaluaciones2026.

## 3. VAR1 centrado: orientación y seis pasos
X,Y shape(240,2). xmean=mean(X,axis=0), ymean=mean(Y,axis=0).
B,residuals,rank,singular_values=np.linalg.lstsq(X−xmean,Y−ymean,rcond=None).
B shape(2,2); intercept=ymean−xmean@B shape(2,).
Filas de B son predictor, columnas son respuesta:
- B[0,0]: BTC previo→BTC siguiente;
- B[1,0]: ETH previo→BTC siguiente;
- B[0,1]: BTC previo→ETH siguiente;
- B[1,1]: ETH previo→ETH siguiente.
La notación de columna v_{t+1}=c+A v_t equivale a A=B.T; el código usa filas state@B, no B@state.

state=r_241; forecast_BTC=0. Seis iteraciones exactas: state=intercept+state@B; forecast_BTC+=state[0]. Comprobar ambos componentes de cada state finitos y suma finita. Cada ETH intermedio es PREDICHO por el mismo modelo; jamás ETH futuro realizado, ni refit entre pasos. Ningún clip de coeficientes, eigenvalues, beta o forecasts. No filtro de estabilidad, condition-number cutoff, ridge, shrinkage, epsilons, winsorización, fallback pseudoinverso seleccionado ni retry con otra ventana/rcond. No búsqueda de lagorder/horizonte/coupling ablations.

np.linalg.lstsq rcond=None determina rango numérico según default NumPy/máquina; exigir rank==2 del X centrado. No umbral económico inventado adicional. NumPy runtime del check técnico:1.26.4, registrado en recibo; futuras economías deben conservar documentación de entorno. El cálculo no garantiza estabilidad o buena estimación económica. Rango reportado por solver no convierte muestra correlacionada en independiente.

## 4. Control AR1 exacto G y admisibilidad común
El control llama/snapshot reutiliza return_forecast(rows,True) de BtcResearchR12ArBase1m, sin alterar su aritmética ni añadir ETH a su ecuación: returns=diff(log242BTCcloses), x=returns[:-1], y=returns[1:], beta=cov_population(x,y)/var_population(x), a=mean(y)−beta*mean(x); seis iteraciones escalares y suma. Nada de usar mediaDRIFT, vectorOLS para sustituir la fórmula o variar periodo.

Admisibilidad COMÚN antes de elegir brazo: ventanas BTC/ETH válidas y sincronizadas; ARvariance finita>0; X/Y/logreturns finitos; VARrank2; B/intercept finitos; ambos forecasts válidos, incluidos seis estados intermedios BTC/ETH VAR y seis valores/suma AR. Si cualquiera falla, AMBOS cash en T. En excepción numérica de lstsq no reintentar con otro solver/parámetro: clasificar invalid/cash común y registrar; sin ocultar errores de contrato/programación como falta de datos. No threshold de volatilidad extra.

El forecast AR sigue siendo la fórmula exacta de G, pero su dominio de admisión ahora incluye ETH/rango/forecastVAR. Por ello esta política control no es automáticamente la política económica G. Debe ejecutarse nuevamente con su contrato común si root aprueba economía; no reutilizar ni sumar la curva G. Aun si la paridad runtime de admisión fuese completa, reconocer reutilización/no independencia. Registrar causas de invalidación y contadores comunes, no declarar igualdad antes de medir.

## 5. Señal, consumo, gestión y riesgo sin cambios
Cada4h elegible es oportunidad nueva; no exigir transición de estado, smoothing ni filtro por régimen/lado. ForecastBTC>.0019 LONG; forecastBTC<−.0019 SHORT; igualdad/intervalo central cash. Hurdle .0019 heredado de G/R20 es umbral de señal, NO costo debitado extra. Ambos brazos forman el mismo diagnóstico y consumen oportunidad aun ocupados. Una posiciónBTC total, sin piramidado, parciales, reversión, cola/replay ni reentrada mismo timestamp de cierre real.

Entradas MARKET al precio actual heredado. Usar R10 entry_plan congelado con stopdistance=2*ATR14 SIMPLE4h actual, calculado de14TR/15cierres; no ta.atr recursivo ni otra protección. Capital max(0,balance), available_margin,3x,feesbase. Unit risk=distance+fee*(entry+stop); riesgo2% de capital, margen90% con denominador price*(1+fee*leverage), floor8decimales research; cap6% agregado no vinculante para una sola posición, no aumentar exposición para llegar a CAGR. Rechazar plan inválido. Protecciones en fill real según on_open_position de R12ArBase: mismo distance, stop relativo a entry_price, assertion fee-aware contra risk_budget, contar apertura real y _observe('open'). No TP ni guarda de TP ficticio añadida.

Gestión EXACTA R12ArBase: timeout cuando T4h−opened_at>=6*BAR; SL activo intrabar en motor1m. No cambiar timeout por forecast/eventtimestamp ni prometer salida exacta24h si fill fuese entre fronteras4h: primer callback4h elegible tras24h. Etiqueta/pronóstico son retornos de PRECIO log24h bruto, no payoff con SL, fees o funding. Sin stop contrafactual ni target S. Modelo de forecast y gestión pueden divergir; se declara, no se corrige tras resultados.

Observer R11 intacto: M1 wallet+PnLabierto y eventos, fronteras mensuales por fase postfunding/predecisión, active months incl cuotas por fills/cierres, before_terminate PRETERMINAL y FINAL si cierre terminal posterior. No heredar por accidente TP2R/48h del R11: overrides ARnoTP24h obligatorios. No cambios al framework/engine.

## 6. Contrato de costos, auditoría y gates r9
Capital10000USDT;2%portrade/6%agregado/3xaislado;fee .00045 por lado,taker con descuento para todos tipos;slippage aplicado0. FundingBTC histórico ON,dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571,marksproxy declaradas. Forecast bruto no incorpora funding; ledger real sí. Neto tras fees/funding modelados no equivale a todos costos reales/spread/impacto. Sin fundingETH porque no se opera. No estrés de costos ni variantes de riesgo.

Gates sin relajar: CAGR>=30%,PF>=1.2,DD<=25%(objetivo20),>=65%mesesactivoscompletos positivos,>=80%trimestrescompletos positivos,mediana mensual calendario>0 incl inactivos,neto aritmético quitando mejores2meses>0,N>=100 sólo suficiencia operativa preliminar. No confianza por conteo. Reportar calendario completo/parciales y rolling12m solapados sin llamarlos independientes/OOS. Financial fullsnapshot gross−fees+funding=PNLsum=final−10000;funding aplicado y observado, M1 y FINAL reconciliados. DD M1+fills no todos extremos intraminuto.

## 7. Presupuesto y secuencia
Root revisó normativa y autorizó implementar/checks, sin drafts/economía. Nuevas fuentes creadas: BtcResearchR22JointBase1m, BtcResearchR22JointVar1m y BtcResearchR22JointAr1m. Padres congelados. Readback/hash de fuentes/deps, check sintético supplied-source/stubs sólo MCP sin importar estrategias/framework ni precios observados. Cubrir orientaciónB,240pares/242closes, seis pasos, ETH predicho,no futuro,ARexacto,rank común/varcero/nonfinite/gaps,signo/hurdle,sizing,noTP/24h,observer terminal.

Máximo1análisis técnico simultáneo coordinado con root. Antes economía: revisiónroot e independiente, recibos/manifiesto/preflight con campos reales, motor informa faltantes. Presupuesto FUTURO2backtests económicos (VAR/AR) + máximo2reemplazos exclusivamente técnicos; no draft/economía autorizados por guardar este protocolo. Intentos de análisis técnico no son reemplazos económicos; documentar errores/soluciones sin inflar conteos como calidad.

Cerrar V tras esos dos resultados sin vecinos de horizonte,ventana,lag,regularización,rcond,clipping,hurdle,lado,estabilidad,gestión o coupling; no explotar segmentos/crosscoefs ganadores posteriores. Ninguna obligación de promover o de gastar motores si revisión detecta duplicación/defecto. No2026nuevo,import/live/paper/Pi/install/restart/framework/global/research_scripts/Hubindex.

## 8. Antecedentes y cierres que se conservan
G: AR1BTC240pares/6pasos frente DRIFT, SL2ATRsinTP24h; no rescatar sus ventanas/betas/hurdles/regímenes. J: shockETH contemporáneo confirmando BTC,1h/6h/TP; no otra sigma/hora/lado. Q: β contemporánea y residual de logniveles,z/freshstate, no VAR; no quitar pataETH al par viejo ni variar z/β/ventanas/TP/plazos. ORCH: OLS96retornos contemporáneos→shockrelativo+confirmación con dos patas; no retocar horas/umbrales/riesgo tras descarte. R/S: kNN6retornosL2/20coseno y targetprecio/payofffee-only; no cambio deK/feature/horizonte/target/stop para rescate.
R20PaxgSpyDelayed1h es shock contemporáneo externo con precio propio quieto. R40PaxgRangeCenterLead4h es midpoint propio; R40PaxgBetaResidual1h es lognivelOLS. V no elimina ninguna pata legada ni reutiliza contribuciones de cartera como rendimientos standalone.

A continuación fuentes COMPLETAS leídas por MCP, hashes SHA256 calculados sobre texto exacto y cierres completos. Son snapshot documental, nunca código ejecutado desde Markdown ni permiso para importar estrategias reales en análisis.

## CODES — fuentes completas congeladas

### strategies/BtcResearchR10Base4h/__init__.py
SHA256 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9; 8100 caracteres.

```python
import json
import math

import numpy as np
from jesse.strategies import Strategy

BAR = 14400000
DAY = 86400000


def closed_window(candles, now, count):
    """Use only consecutive, closed 4h bars; no synthetic gap repair."""
    rows = candles[candles[:, 0] + BAR <= now][-count:]
    if len(rows) != count or rows[-1, 0] != now - BAR:
        return None
    if not np.all(np.diff(rows[:, 0]) == BAR):
        return None
    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):
        return None
    if np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2])):
        return None
    if np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2])):
        return None
    return rows


def atr14(rows):
    previous = rows[-15:-1, 2]
    current = rows[-14:]
    tr = np.maximum(current[:, 3] - current[:, 4],
                    np.maximum(abs(current[:, 3] - previous), abs(current[:, 4] - previous)))
    value = float(np.mean(tr))
    return value if math.isfinite(value) and value > 0 else None


def breadth_state(closes):
    changes = np.diff(closes)
    positive = changes > 0
    negative = changes < 0
    if int(positive[-6:].sum()) >= 4 and int(positive[-24:].sum()) >= 16:
        return 1
    if int(negative[-6:].sum()) >= 4 and int(negative[-24:].sum()) >= 16:
        return -1
    return 0


def breadth_signal(rows):
    """Count sign persistence, not return magnitudes; consume only new states."""
    now_state = breadth_state(rows[-25:, 2])
    old_state = breadth_state(rows[-26:-1, 2])
    return now_state if now_state != old_state else 0


def funding_failure_signal(rows, now, events):
    """Observe a full post-payment bar; never know or collect the next payment."""
    event_start = now - BAR
    matching = []
    for event in events:
        raw = int(event["settled_at"])
        effective = raw // 60000 * 60000
        if effective == event_start and 0 <= raw - effective <= 1000:
            if int(event["available_at"]) <= now and int(event["available_at"]) > raw:
                matching.append(event)
    if len(matching) != 1:
        return 0, None
    event = matching[0]
    rate = float(event["rate_decimal"])
    if not math.isfinite(rate):
        return 0, None
    pre, post = rows[-2], rows[-1]
    if rate > 0 and pre[2] > pre[1] and post[2] < pre[1]:
        return -1, dict(settled_at=int(event["settled_at"]), available_at=int(event["available_at"]), rate=rate)
    if rate < 0 and pre[2] < pre[1] and post[2] > pre[1]:
        return 1, dict(settled_at=int(event["settled_at"]), available_at=int(event["available_at"]), rate=rate)
    return 0, None


def entry_plan(price, capital, margin, leverage, fee, direction, distance):
    stop = price - direction * distance
    values = (price, capital, margin, leverage, distance, stop)
    if direction not in (-1, 1) or not all(math.isfinite(v) and v > 0 for v in values):
        return None
    if not math.isfinite(fee) or fee < 0:
        return None
    unit_loss = distance + fee * (price + stop)
    # 2% includes both execution fees. The 90% margin ceiling retains the
    # historical reserve and does not increase the stop's monetary risk.
    risk_qty = 0.02 * capital / unit_loss
    margin_qty = 0.90 * margin * leverage / (price * (1 + fee * leverage))
    qty = math.floor(min(risk_qty, margin_qty) * 1e8) / 1e8
    if qty <= 0:
        return None
    assert qty * unit_loss <= 0.02 * capital + 1e-6
    return dict(qty=qty, price=price, capital=capital, distance=distance,
                stop=stop, risk_budget=0.02 * capital,
                planned_loss=qty * unit_loss, margin_capped=margin_qty < risk_qty)


class BtcResearchR10Base4h(Strategy):
    """R10 discovery harness: one BTC position, fixed risk and base costs only."""
    MODE = "abstract"
    START = 1602720000000
    FINISH = 1767225600000

    def _log(self, label, value):
        self.log(label + " " + json.dumps(value, separators=(",", ":"), allow_nan=False))

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT"
            assert self.leverage == 3
            assert abs(self.fee_rate - 0.00045) < 1e-12
            self.vars["checked"] = True
            self._log("R10_CONFIG", dict(mode=self.MODE, risk=0.02, aggregate=0.06,
                                        leverage=self.leverage, fee=self.fee_rate,
                                        margin_buffer=0.90, stop_atr=2, target_r=2, hold_hours=48))
        self.vars["direction"] = 0
        rows = closed_window(self.candles, now, 26)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            return
        if self.MODE == "BREADTH":
            direction = breadth_signal(rows)
            evidence = None
        else:
            assert self.MODE == "POST_FUNDING"
            events = self.get_funding_history(count=6)
            assert all(int(e["available_at"]) <= now for e in events)
            direction, evidence = funding_failure_signal(rows, now, events)
        if not direction or not self.START < now < self.FINISH:
            return
        # Signals are evaluated and consumed while occupied as well. No deferred
        # order or re-entry from a previously blocked funding/breadth event.
        self.vars["signals"] = self.vars.get("signals", 0) + 1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0) + 1
            return
        atr = atr14(rows)
        if atr is None:
            return
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        plan = entry_plan(float(self.price), capital, float(self.available_margin),
                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)
        if plan is None or float(self.price) + direction * 2 * plan["distance"] <= 0:
            return
        self.vars["direction"] = direction
        self.vars["plan"] = plan
        self.vars["evidence"] = evidence

    def should_long(self):
        return self.vars.get("direction") == 1

    def should_short(self):
        return self.vars.get("direction") == -1

    def go_long(self):
        plan = self.vars["plan"]
        self.buy = plan["qty"], self.price

    def go_short(self):
        plan = self.vars["plan"]
        self.sell = plan["qty"], self.price

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        distance = plan["distance"]
        stop = entry - direction * distance
        target = entry + direction * 2 * distance
        assert qty * (distance + self.fee_rate * (entry + stop)) <= plan["risk_budget"] + 1e-6
        self.stop_loss = qty, stop
        self.take_profit = qty, target
        self.vars["entries"] = self.vars.get("entries", 0) + 1
        self._log("R10_ENTRY", dict(time=int(self.time), direction=direction, entry=entry,
                                   qty=qty, stop=stop, target=target, plan=plan,
                                   evidence=self.vars.get("evidence")))

    def update_position(self):
        # No ratchet, discretionary exit or same-close reversal. Funding applies
        # continuously to actual held quantity, independently of signal inputs.
        if int(self.time) - int(self.position.opened_at) >= 12 * BAR:
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        self.vars["last_exit_at"] = int(self.time)

    def before_terminate(self):
        self._log("R10_COUNTERS", dict(signals=self.vars.get("signals", 0),
                                     occupied=self.vars.get("occupied", 0),
                                     entries=self.vars.get("entries", 0),
                                     invalid_windows=self.vars.get("invalid_windows", 0)))

```

### strategies/BtcResearchR11Base1m/__init__.py
SHA256 be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87; 10150 caracteres.

```python
import json
import math
from datetime import datetime, timezone

import numpy as np
from jesse.strategies import Strategy
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def cusum_step(rows, accumulators):
    """Transfer the R40 design:60 past log returns, drift0.25, boundary4."""
    returns = np.diff(np.log(rows[-62:, 2]))
    sigma = float(np.std(returns[:-1], ddof=1))
    if not math.isfinite(sigma) or sigma <= 0:
        return 0, (0.0, 0.0)
    z = float((returns[-1] - np.mean(returns[:-1])) / sigma)
    if not math.isfinite(z):
        return 0, (0.0, 0.0)
    up = max(0.0, accumulators[0] + z - 0.25)
    down = max(0.0, accumulators[1] - z - 0.25)
    if up >= 4 or down >= 4:
        direction = 0 if up >= 4 and down >= 4 else 1 if up >= 4 else -1
        return direction, (0.0, 0.0)
    return 0, (up, down)


def absorption_signal(rows):
    """Large volume but small body, followed by escape of that closed bar."""
    window, setup, confirmation = rows[-26:-2], rows[-2], rows[-1]
    if not np.all(np.isfinite(rows[-26:, 5])) or np.any(rows[-26:, 5] < 0):
        return 0
    average_volume = float(np.mean(window[:, 5]))
    prior_atr = atr14(window)
    if not math.isfinite(average_volume) or average_volume <= 0 or prior_atr is None:
        return 0
    if setup[5] < 2 * average_volume or abs(setup[2] - setup[1]) > 0.25 * prior_atr:
        return 0
    if confirmation[2] > setup[3]:
        return 1
    if confirmation[2] < setup[4]:
        return -1
    return 0


def month_name(timestamp):
    return datetime.fromtimestamp(timestamp / 1000, timezone.utc).strftime("%Y-%m")


def monthly_summary(boundaries, active_months):
    """Declared post-settlement/pre-decision UTC cuts; no00:01 approximation."""
    points = sorted(boundaries.items())
    months = []
    for (start, before), (finish, after) in zip(points, points[1:]):
        stamp = datetime.fromtimestamp(start / 1000, timezone.utc)
        month = stamp.strftime("%Y-%m")
        complete = stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0
        if before <= 0:
            continue
        months.append(dict(month=month, start=start, finish=finish,
                           complete=complete, active=month in active_months,
                           pnl=after-before, return_fraction=after/before-1))
    complete = [m for m in months if m["complete"]]
    active = [m for m in complete if m["active"]]
    quarter_groups = {}
    for m in months:
        quarter = m["month"][:4] + "Q" + str((int(m["month"][5:])-1)//3+1)
        quarter_groups.setdefault(quarter, []).append(m)
    quarters = [q for q in quarter_groups.values()
                if len(q) == 3 and all(m["complete"] for m in q)]
    returns = [m["return_fraction"] for m in complete]
    contributions = sorted([m["pnl"] for m in months], reverse=True)
    return dict(months=months, complete_months=len(complete), active_months=len(active),
                positive_active=sum(m["pnl"] > 0 for m in active),
                positive_calendar=sum(m["pnl"] > 0 for m in complete),
                median_return=float(np.median(returns)) if returns else None,
                complete_quarters=len(quarters),
                positive_quarters=sum(sum(m["pnl"] for m in q) > 0 for q in quarters),
                pnl_without_best_two=sum(m["pnl"] for m in months)-sum(contributions[:2]))


class BtcResearchR11Base1m(Strategy):
    """M1 accounting observer; signal and management decisions remain4h."""
    MODE = "abstract"
    START = 1602720000000
    FINISH = 1767225600000

    def _log(self, label, payload):
        # Event logs stay small; monthly history is emitted as separate rows.
        self.log(label + " " + json.dumps(payload, separators=(",", ":"), allow_nan=False))

    def _observe(self, stage):
        now = int(self.time)
        # BTC-only futures equity. portfolio_value multiplies open PnL by
        # leverage in this checkout, so it is deliberately not used here.
        equity = float(self.balance) + (float(self.position.pnl) if self.is_open else 0.0)
        assert math.isfinite(equity)
        self.vars["peak"] = max(self.vars.get("peak", 10000.0), equity)
        drawdown = equity / self.vars["peak"] - 1
        self.vars["dd"] = min(self.vars.get("dd", 0.0), drawdown)
        self.vars["sequence"] = self.vars.get("sequence", 0) + 1
        self.vars["last_equity"] = equity
        active = self.vars.setdefault("active_months", set())
        if self.is_open:
            # Pre marks describe exposure during the minute that just closed;
            # an opening fill at T instead belongs to the new interval.
            active.add(month_name(now if stage == "open" else now-1))
        boundaries = self.vars.setdefault("boundaries", {self.START: 10000.0})
        if stage == "pre":
            self.vars["minute_marks"] = self.vars.get("minute_marks", 0) + 1
            stamp = datetime.fromtimestamp(now / 1000, timezone.utc)
            if stamp.day == 1 and stamp.hour == 0 and stamp.minute == 0:
                boundaries[now] = equity
        if now >= self.FINISH:
            # A later terminal close callback replaces the mark with post-fee equity.
            boundaries[self.FINISH] = equity
        return equity

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate - 0.00045) < 1e-12
            assert abs(self.balance - 10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        # This is signal alignment, not a market-session/calendar filter.
        if now % BAR != 0:
            return
        count = 62 if self.MODE == "CUSUM" else 26
        candles = self.get_candles(self.exchange, self.symbol, "4h")
        rows = closed_window(candles, now, count)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0) + 1
            self.vars["cusum"] = (0.0, 0.0)
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        if self.MODE == "CUSUM":
            direction, state = cusum_step(rows, self.vars.get("cusum", (0.0, 0.0)))
            self.vars["cusum"] = state
        else:
            assert self.MODE == "ABSORPTION"
            direction = absorption_signal(rows)
        if not direction or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0) + 1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0) + 1
            return
        atr = atr14(rows)
        if atr is None:
            return
        # Flat BTC account: wallet equals equity. Reuse the frozen2% fee-aware
        # plan, eight-decimal research precision and90% margin ceiling.
        capital = max(0.0, float(self.balance))
        plan = entry_plan(float(self.price), capital, float(self.available_margin),
                          float(self.leverage), float(self.fee_rate), direction, 2 * atr)
        if plan is None or self.price + direction * 2 * plan["distance"] <= 0:
            return
        self.vars["direction"] = direction
        self.vars["plan"] = plan

    def should_long(self):
        return self.vars.get("direction") == 1

    def should_short(self):
        return self.vars.get("direction") == -1

    def go_long(self):
        self.buy = self.vars["plan"]["qty"], self.price

    def go_short(self):
        self.sell = self.vars["plan"]["qty"], self.price

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        stop = entry - direction * plan["distance"]
        target = entry + direction * 2 * plan["distance"]
        assert qty * (plan["distance"] + self.fee_rate * (entry + stop)) <= plan["risk_budget"] + 1e-6
        self.stop_loss = qty, stop
        self.take_profit = qty, target
        self.vars["entries"] = self.vars.get("entries", 0) + 1
        self._observe("open")

    def update_position(self):
        # Preserve the four-hour management clock despite the M1 observer.
        if int(self.time) % BAR == 0 and int(self.time) - int(self.position.opened_at) >= 12 * BAR:
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        now = int(self.time)
        active = self.vars.setdefault("active_months", set())
        active.add(month_name(now-1))
        # At a month boundary, retain both the held interval and any fee-only
        # execution month. Terminal liquidation belongs to the final interval.
        if now < self.FINISH:
            active.add(month_name(now))
        self.vars["last_exit_at"] = now
        self._observe("close")
        if now >= self.FINISH and self.vars.get("emitted"):
            self._emit("FINAL")

    def _emit(self, stage):
        summary = monthly_summary(self.vars["boundaries"], self.vars.get("active_months", set()))
        # Emit rows at the end, so one bounded log page can retrieve all months.
        for item in summary.pop("months"):
            self._log("R11_MONTH", dict(stage=stage, **item))
        summary.update(stage=stage, equity=self.vars["last_equity"],
                       dd_m1_events=self.vars.get("dd", 0),
                       minute_marks=self.vars.get("minute_marks", 0),
                       sequence=self.vars.get("sequence", 0),
                       signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
                       invalid_windows=self.vars.get("invalid_windows", 0))
        self._log("R11_SUMMARY", summary)

    def before_terminate(self):
        self._observe("terminal")
        self.vars["emitted"] = True
        self._emit("PRETERMINAL")

```

### strategies/BtcResearchR12ArBase1m/__init__.py
SHA256 1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343; 3347 caracteres.

```python
import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def return_forecast(rows, autoregressive):
    """240 observed (x,y) pairs, then six genuinely future recursive forecasts."""
    returns = np.diff(np.log(rows[-242:, 2]))
    x, y = returns[:-1], returns[1:]
    variance = float(np.mean((x-x.mean())**2))
    if not math.isfinite(variance) or variance <= 0:
        return None
    beta = float(np.mean((x-x.mean())*(y-y.mean()))/variance) if autoregressive else 0.
    intercept = float(y.mean()-beta*x.mean())
    value, forecast = float(returns[-1]), 0.
    for _ in range(6):
        value = intercept+beta*value
        forecast += value
    return forecast if math.isfinite(forecast) else None


class BtcResearchR12ArBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 242)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("AR1", "DRIFT")
        forecast = return_forecast(rows, self.MODE == "AR1")
        # Fixed signal hurdle inherited from R20, not simulated execution friction.
        if forecast is None or abs(forecast) <= .0019 or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        direction = 1 if forecast > 0 else -1
        atr = atr14(rows)
        if atr is None:
            return
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = direction

    def on_open_position(self, order):
        plan = self.vars["plan"]
        direction = 1 if self.is_long else -1
        entry, qty = float(self.position.entry_price), abs(float(self.position.qty))
        stop = entry-direction*plan["distance"]
        assert qty*(plan["distance"]+self.fee_rate*(entry+stop)) <= plan["risk_budget"]+1e-6
        self.stop_loss = qty, stop
        # Forecast horizon is24h; no fixed target clips the model's payoff.
        self.vars["entries"] = self.vars.get("entries", 0)+1
        self._observe("open")

    def update_position(self):
        if int(self.time) % BAR == 0 and int(self.time)-int(self.position.opened_at) >= 6*BAR:
            self.liquidate()

```

### strategies/BtcResearchR12Ar1m/__init__.py
SHA256 5abf0cb22dee8d8559eabe27be5ad6a9b9f5dd452c3b36a4d8fc83a2b7f73847; 138 caracteres.

```python
from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m


class BtcResearchR12Ar1m(BtcResearchR12ArBase1m):
    MODE = "AR1"

```

### strategies/BtcResearchR12Drift1m/__init__.py
SHA256 0b81355bf376486b26a32f2a14589b264fa770295c87e2bce42c6d236e9c7cd6; 143 caracteres.

```python
from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m


class BtcResearchR12Drift1m(BtcResearchR12ArBase1m):
    MODE = "DRIFT"

```

### strategies/BtcResearchR13ExternalBase1m/__init__.py
SHA256 aea8fe53975ab2a75efdccc1f254cd15c07299faa3acdeab6466be985f91106a; 3417 caracteres.

```python
import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import atr14, entry_plan

HOUR = 3600000


def closed_hour_window(candles, now):
    rows = candles[candles[:, 0]+HOUR <= now][-26:]
    if len(rows) != 26 or rows[-1, 0] != now-HOUR:
        return None
    if not np.all(np.diff(rows[:, 0]) == HOUR):
        return None
    if not np.all(np.isfinite(rows[:, :5])) or np.any(rows[:, 1:5] <= 0):
        return None
    if np.any(rows[:, 3] < np.maximum(rows[:, 1], rows[:, 2])) or np.any(rows[:, 4] > np.minimum(rows[:, 1], rows[:, 2])):
        return None
    return rows


def external_confirmation(btc, eth, require_eth):
    """Both baselines exclude current returns; BTC alone defines direction."""
    own, leader = np.diff(np.log(btc[:, 2])), np.diff(np.log(eth[:, 2]))
    own_sigma = float(np.std(own[:-1], ddof=1))
    leader_sigma = float(np.std(leader[:-1], ddof=1))
    if not all(math.isfinite(x) and x > 0 for x in (own_sigma, leader_sigma)):
        return 0
    if abs(float(own[-1])) > own_sigma:
        return 0
    momentum = float(own[-7:-1].sum())
    direction = 1 if momentum > 0 else -1 if momentum < 0 else 0
    if require_eth and not (abs(float(leader[-1])) >= 2*leader_sigma and direction*float(leader[-1]) > 0):
        return 0
    return direction


class BtcResearchR13ExternalBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % HOUR:
            return
        btc = closed_hour_window(self.get_candles(self.exchange, "BTC-USDT", "1h"), now)
        eth = closed_hour_window(self.get_candles(self.exchange, "ETH-USDT", "1h"), now)
        if btc is None or eth is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert np.array_equal(btc[:, 0], eth[:, 0])
        assert math.isclose(float(btc[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        assert self.MODE in ("ETH_CONFIRM", "BTC_CONTROL")
        direction = external_confirmation(btc, eth, self.MODE == "ETH_CONFIRM")
        if not direction or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(btc)
        if atr is None:
            return
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None or self.price+direction*2*plan["distance"] <= 0:
            return
        self.vars["plan"] = plan
        self.vars["direction"] = direction

    def update_position(self):
        if int(self.time) % HOUR == 0 and int(self.time)-int(self.position.opened_at) >= 6*HOUR:
            self.liquidate()

```

### strategies/BtcResearchR13EthConfirm1m/__init__.py
SHA256 8e9160cedc7fd067a7b065311f5d41cd3ce0abd96c776472f5e0bf57cce82461; 172 caracteres.

```python
from strategies.BtcResearchR13ExternalBase1m import BtcResearchR13ExternalBase1m


class BtcResearchR13EthConfirm1m(BtcResearchR13ExternalBase1m):
    MODE = "ETH_CONFIRM"

```

### strategies/BtcResearchR13BtcControl1m/__init__.py
SHA256 20d263f3cf3bf0e058c6d9eb75422d8867208a758350886a58cb5d5378f8e67f; 172 caracteres.

```python
from strategies.BtcResearchR13ExternalBase1m import BtcResearchR13ExternalBase1m


class BtcResearchR13BtcControl1m(BtcResearchR13ExternalBase1m):
    MODE = "BTC_CONTROL"

```

### strategies/BtcResearchR17RelativeBase1m/__init__.py
SHA256 b40f428caaa728a117953fc97e4eee3372b895e622ba927c695fdef665dfefb8; 5090 caracteres.

```python
import math
import numpy as np
from strategies.BtcResearchR11Base1m import BtcResearchR11Base1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def relative_beta(btc, eth):
    """240 paired returns from241 prior closes; current closes never fit beta."""
    own = np.diff(np.log(btc[-242:-1, 2]))
    external = np.diff(np.log(eth[-242:-1, 2]))
    assert len(own) == len(external) == 240
    xc, yc = external-np.mean(external), own-np.mean(own)
    denominator = float(np.dot(xc, xc))
    variance = denominator/(len(external)-1)
    if not math.isfinite(variance) or variance <= 0:
        return None
    beta = float(np.dot(xc, yc)/denominator)
    return beta if math.isfinite(beta) else None


def relative_level_state(btc, eth, fitted_beta, residual):
    """Use one current refit for all60 reference levels and the current level."""
    model_beta = fitted_beta if residual else 0.0
    levels = np.log(btc[-61:, 2])-model_beta*np.log(eth[-61:, 2])
    reference = levels[:-1]
    assert len(reference) == 60
    mean = float(np.mean(reference))
    sigma = float(np.std(reference, ddof=1))
    evidence = dict(fitted_beta=fitted_beta, model_beta=model_beta,
                    mean=mean, sigma=sigma, z=None, beta_returns=240, reference_levels=60)
    if not math.isfinite(mean) or not math.isfinite(sigma) or sigma <= 0:
        # Degenerate levels are neutral, with no epsilon/winsorization rescue.
        evidence["mean"] = mean if math.isfinite(mean) else None
        evidence["sigma"] = sigma if math.isfinite(sigma) else None
        return 0, evidence
    z = float((levels[-1]-mean)/sigma)
    if not math.isfinite(z):
        return 0, evidence
    evidence["z"] = z
    state = 1 if z <= -2 else -1 if z >= 2 else 0
    return state, evidence


class BtcResearchR17RelativeBase1m(BtcResearchR11Base1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("RESIDUAL", "PRICE")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        btc = closed_window(self.get_candles(self.exchange, "BTC-USDT", "4h"), now, 242)
        eth = closed_window(self.get_candles(self.exchange, "ETH-USDT", "4h"), now, 242)
        if btc is None or eth is None or not np.array_equal(btc[:, 0], eth[:, 0]):
            self.vars["relative_state"] = 0
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(btc[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        # ETH validity and finite positive variance are shared by the PRICE arm.
        beta = relative_beta(btc, eth)
        if beta is None:
            self.vars["relative_state"] = 0
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        state, evidence = relative_level_state(btc, eth, beta, self.MODE == "RESIDUAL")
        previous = self.vars.get("relative_state", 0)
        self.vars["relative_state"] = state
        # Refit-induced transitions are intentionally part of this definition.
        direction = state if state and state != previous else 0
        if not direction or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(btc)
        if atr is None:
            return
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None or self.price+direction*2*plan["distance"] <= 0:
            return
        self.vars["plan"] = dict(plan, relative=dict(evidence))
        self.vars["direction"] = direction

    def on_open_position(self, order):
        # Reuse the unchanged R11 fee-risk assertion, actual-fill SL/TP and count.
        super().on_open_position(order)
        side = 1 if self.is_long else -1
        key = "long_fills" if side == 1 else "short_fills"
        self.vars[key] = self.vars.get(key, 0)+1
        self._log("R17_RELATIVE_OPEN", dict(time=int(self.time), mode=self.MODE,
            direction=side, evidence=self.vars["plan"]["relative"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R17_RELATIVE_STATS", dict(stage=stage, mode=self.MODE,
            long_fills=self.vars.get("long_fills", 0),
            short_fills=self.vars.get("short_fills", 0),
            signals=self.vars.get("signals", 0), occupied=self.vars.get("occupied", 0)))

```

### strategies/BtcResearchR17RelativeResidual1m/__init__.py
SHA256 2f78bac618aabf929d5f39c7da77ac20e2dff07bd5507db65aae498b0973a37b; 175 caracteres.

```python
from strategies.BtcResearchR17RelativeBase1m import BtcResearchR17RelativeBase1m


class BtcResearchR17RelativeResidual1m(BtcResearchR17RelativeBase1m):
    MODE = "RESIDUAL"

```

### strategies/BtcResearchR17RelativePrice1m/__init__.py
SHA256 3a0ef1d9b18ca9d6fd2f5b306a2498fd93f469c79eec819f9973b40244af21e6; 169 caracteres.

```python
from strategies.BtcResearchR17RelativeBase1m import BtcResearchR17RelativeBase1m


class BtcResearchR17RelativePrice1m(BtcResearchR17RelativeBase1m):
    MODE = "PRICE"

```

### strategies/OrchLateralRelativeShock1h/__init__.py
SHA256 4a0fb55580b5eda3b5bd954b829860eb15c40fb1b5f592d143d418f11956a610; 13282 caracteres.

```python
import math
import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta

HOUR = 60 * 60 * 1000
SYMBOLS = ('BTC-USDT', 'ETH-USDT')
BASE_FEE = 0.00045
SLIPPAGE_RESERVE = 0.001  # Sizing buffer, never a claimed fill-cost model.
BASKET_RISK = 0.01
LEG_RISK = 0.005
GROSS_CAP = 4.4


class OrchLateralRelativeShock1h(Strategy):
    """Two sequential MARKET legs fading a confirmed relative-return shock.

    Shared state is a coordination protocol, not atomic exchange execution.
    Emergency stops can leave one leg until its next strategy execution.
    This is an isolated research basket, not an integration with the reference.
    """

    def _book(self):
        return self.shared_vars.setdefault('orch_relative_shock', {
            'phase': 'flat', 'plan': None, 'last_exit': -1,
            'baskets': 0, 'aborts': 0, 'orphan_hours': 0})

    def _strategies(self):
        selected = {r.symbol: r.strategy for r in self.routes
                    if r.exchange == self.exchange}
        # A new deployment with additional routes needs its own coordinated
        # allocator; silently mixing this prototype into a portfolio is forbidden.
        assert set(selected) == set(SYMBOLS), 'PAIR_REQUIRES_EXACTLY_BTC_ETH'
        assert all(s.timeframe == '1h' for s in selected.values())
        return selected

    def _histories(self):
        result = {}
        for symbol in SYMBOLS:
            c = self.get_candles(self.exchange, symbol, '1h')
            if len(c) < 100:
                return None
            # Skip rather than invent synchronized history or use a stale quote.
            c = c[-100:]
            if int(c[-1, 0]) != int(self.closed_candle_open_time):
                return None
            assert np.all(c[:, 0] <= self.closed_candle_open_time), 'PAIR_FUTURE_BAR'
            if not np.all(np.diff(c[:, 0]) == HOUR):
                return None
            result[symbol] = c
        assert np.array_equal(result[SYMBOLS[0]][:, 0], result[SYMBOLS[1]][:, 0])
        return result

    def _new_plan(self, history):
        b, e = (history[s] for s in SYMBOLS)
        rb, re = np.diff(np.log(b[:, 2])), np.diff(np.log(e[:, 2]))
        # Fit uses 96 hourly returns strictly before the two shock hours plus
        # the latest confirmation hour. No signal bar enters its own baseline.
        x, y = re[:-3], rb[:-3]
        assert len(x) == 96 and len(y) == 96
        variance = float(np.mean((x - x.mean()) ** 2))
        if not math.isfinite(variance) or variance <= 0:
            return None
        beta = float(np.mean((x - x.mean()) * (y - y.mean())) / variance)
        alpha = float(y.mean() - beta * x.mean())
        sigma = float(np.std(y - alpha - beta * x, ddof=1))
        # Reject unstable/sign-inverted hedge estimates instead of clipping them.
        if not (0.25 <= beta <= 4 and math.isfinite(sigma) and sigma > 1e-8):
            return None
        residual = rb[-3:] - alpha - beta * re[-3:]
        shock, confirmation = float(residual[:2].sum()), float(residual[-1])
        remaining = shock + confirmation
        shock_scale = sigma * math.sqrt(2)
        if not (abs(shock) >= 2 * shock_scale
                and shock * confirmation < 0 and shock * remaining > 0):
            return None
        sign = 1 if shock > 0 else -1
        sides = {SYMBOLS[0]: -sign, SYMBOLS[1]: sign}
        prices = {s: float(history[s][-1, 2]) for s in SYMBOLS}
        # Emergency stops use ATR known before any of the three signal hours.
        distances = {s: 3 * float(ta.atr(history[s][:-3])) for s in SYMBOLS}
        if not all(math.isfinite(distances[s]) and 0 < distances[s] < prices[s]
                   for s in SYMBOLS):
            return None
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        if capital <= 0:
            return None
        # Expected log-spread recovery is only an eligibility approximation.
        # Demand two complete two-leg round trips at BASE fees, kept fixed in
        # cost stress. Realized cash PnL can differ from this approximation.
        if abs(remaining) < 4 * BASE_FEE * (1 + beta):
            return None
        risk_fraction = {
            s: distances[s] / prices[s]
            + self.fee_rate * (2 + distances[s] / prices[s])
            + SLIPPAGE_RESERVE for s in SYMBOLS}
        rb_frac, re_frac = (risk_fraction[s] for s in SYMBOLS)
        free_margin = max(0.0, float(self.available_margin))
        # Compute both legs before arming either: beta links their notionals,
        # while per-leg and basket risk caps independently constrain scale.
        btc_notional = min(
            capital * LEG_RISK / rb_frac,
            capital * LEG_RISK / (beta * re_frac),
            capital * BASKET_RISK / (rb_frac + beta * re_frac),
            capital * GROSS_CAP / (1 + beta),
            free_margin * 0.90 / ((1 + beta) * (1 / self.leverage + self.fee_rate)))
        notionals = {SYMBOLS[0]: btc_notional, SYMBOLS[1]: beta * btc_notional}
        # Historical research precision; native venue minimums are unverified.
        qty = {s: math.floor(notionals[s] / prices[s] / 0.001) * 0.001 for s in SYMBOLS}
        if min(qty.values()) <= 0:
            return None
        notionals = {s: qty[s] * prices[s] for s in SYMBOLS}
        risks = {s: notionals[s] * risk_fraction[s] for s in SYMBOLS}
        gross = sum(notionals.values())
        margin = gross * (1 / self.leverage + self.fee_rate)
        assert max(risks.values()) <= capital * LEG_RISK + 1e-8
        assert sum(risks.values()) <= capital * BASKET_RISK + 1e-8
        assert sum(risks.values()) <= capital * 0.08 + 1e-8
        assert gross <= capital * GROSS_CAP + 1e-8
        assert margin <= free_margin * 0.90 + 1e-8
        # Rounding only reduces each leg. Bound deviation by their maximum lot
        # losses, not an arbitrary percentage that fails with small quantities.
        hedge_error = abs(notionals[SYMBOLS[1]] - beta * notionals[SYMBOLS[0]])
        assert hedge_error <= 0.001 * (prices[SYMBOLS[1]] + beta * prices[SYMBOLS[0]]) + 1e-8
        return dict(time=int(self.time), prices=prices, qty=qty, distances=distances,
                    sides=sides, risks=risks, margin=margin, gross=gross,
                    beta=beta, alpha=alpha, sigma=sigma, shock_scale=shock_scale,
                    sign=sign, remaining=remaining,
                    refs={s: float(history[s][-4, 2]) for s in SYMBOLS},
                    ref_time=int(b[-4, 0]) + HOUR,
                    queued=set(), filled={}, closed=set(), exit_reason=None)

    def _request_exit(self, reason):
        book = self._book()
        plan = book['plan']
        if plan is not None and plan['exit_reason'] is None:
            if reason in ('missing_or_closed_leg', 'leader_not_queued',
                          'entry_clock_or_price_mismatch', 'fill_mismatch',
                          'unexpected_pending_market_order'):
                book['aborts'] += 1
            plan['exit_reason'] = reason
            book['phase'] = 'exiting'
            self.log('ORCH_PAIR_EXIT reason=' + reason + ' basket=' + str(plan['time']))

    def before(self):
        assert self.is_futures_trading and self.leverage == 5
        strategies = self._strategies()
        book = self._book()
        plan = book['plan']
        if plan is not None and book['phase'] != 'flat':
            if self.time > plan['time']:
                opened = {s for s in SYMBOLS if strategies[s].is_open}
                if len(plan['filled']) != 2 or len(opened) != 2:
                    if opened:
                        if self.symbol == SYMBOLS[0]:
                            book['orphan_hours'] += 1
                        self._request_exit('missing_or_closed_leg')
                    else:
                        book['phase'] = 'flat'
                        book['last_exit'] = int(self.time)
                        book['plan'] = None
            return
        # BTC is the lead route under Jesse's symbol ordering. If synchronized
        # histories are not available at this callback, skip the opportunity.
        if self.symbol != SYMBOLS[0] or self.time <= book['last_exit']:
            return
        if any(s.is_open or s.entry_orders for s in strategies.values()):
            return
        history = self._histories()
        if history is None:
            return
        plan = self._new_plan(history)
        if plan is not None:
            book['plan'] = plan
            book['phase'] = 'armed'
            self.log('ORCH_PAIR_ARM basket=' + str(plan['time'])
                     + ' beta=' + str(plan['beta']) + ' risks=' + str(plan['risks']))

    def _side(self):
        book = self._book()
        plan = book['plan']
        if plan is None or book['phase'] not in ('armed', 'entering'):
            return 0
        if plan['time'] != int(self.time) or plan['exit_reason'] is not None:
            return 0
        if self.symbol in plan['queued']:
            return 0
        # Both callbacks enqueue before simulated MARKET orders execute.
        # Never require BTC.is_open here: doing so would block the ETH leg.
        if self.symbol == SYMBOLS[1] and SYMBOLS[0] not in plan['queued']:
            self._request_exit('leader_not_queued')
            return 0
        if not math.isclose(float(self.price), plan['prices'][self.symbol],
                            rel_tol=1e-10, abs_tol=1e-8):
            self._request_exit('entry_clock_or_price_mismatch')
            return 0
        return plan['sides'][self.symbol]

    def should_long(self):
        return self._side() == 1

    def should_short(self):
        return self._side() == -1

    def _enqueue(self):
        book = self._book()
        plan = book['plan']
        assert self.symbol not in plan['queued']
        plan['queued'].add(self.symbol)
        book['phase'] = 'entering'
        return plan['qty'][self.symbol]

    def go_long(self):
        self.buy = self._enqueue(), self.price

    def go_short(self):
        self.sell = self._enqueue(), self.price

    def should_cancel_entry(self):
        self._request_exit('unexpected_pending_market_order')
        return True

    def on_open_position(self, order):
        book = self._book()
        plan = book['plan']
        assert plan is not None and self.symbol in plan['queued']
        assert self.symbol not in plan['filled'], 'PAIR_DUPLICATE_ENTRY'
        actual = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        distance = plan['distances'][self.symbol]
        # A protective order is attached to each fill even if its counterpart
        # fails. No assumption of atomic entry or stop execution is made.
        stop = actual - distance if self.is_long else actual + distance
        self.stop_loss = qty, stop
        plan['filled'][self.symbol] = dict(price=actual, qty=qty, time=int(self.time))
        if not (math.isclose(actual, plan['prices'][self.symbol], rel_tol=1e-10, abs_tol=1e-8)
                and math.isclose(qty, plan['qty'][self.symbol], rel_tol=1e-10, abs_tol=1e-8)):
            self._request_exit('fill_mismatch')
        if len(plan['filled']) == 2 and plan['exit_reason'] is None:
            assert plan['queued'] == set(SYMBOLS)
            assert len({v['time'] for v in plan['filled'].values()}) == 1
            book['phase'] = 'active'
            book['baskets'] += 1

    def update_position(self):
        book = self._book()
        plan = book['plan']
        assert plan is not None
        if plan['exit_reason'] is None and book['phase'] == 'active':
            history = self._histories()
            if history is not None:
                hours = (self.time - plan['ref_time']) / HOUR
                residual = (math.log(float(history[SYMBOLS[0]][-1, 2]) / plan['refs'][SYMBOLS[0]])
                            - plan['beta'] * math.log(float(history[SYMBOLS[1]][-1, 2])
                                                      / plan['refs'][SYMBOLS[1]])
                            - plan['alpha'] * hours)
                if plan['sign'] * residual <= 0:
                    self._request_exit('relative_recovery')
                elif plan['sign'] * (residual - plan['remaining']) >= plan['shock_scale']:
                    self._request_exit('relative_adverse_stop')
            if self.time - plan['time'] >= 12 * HOUR:
                self._request_exit('twelve_hour_expiry')
        if plan['exit_reason'] is not None:
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        book = self._book()
        plan = book['plan']
        assert plan is not None
        assert self.symbol not in plan['closed'], 'PAIR_DUPLICATE_CLOSE'
        plan['closed'].add(self.symbol)
        if plan['exit_reason'] is None:
            self._request_exit('individual_emergency_or_terminal')
        if plan['closed'] == set(SYMBOLS):
            book['phase'] = 'flat'
            book['last_exit'] = int(self.time)
            book['plan'] = None

    def on_increased_position(self, order):
        raise AssertionError('PAIR_PYRAMIDING_UNSUPPORTED')

    def on_reduced_position(self, order):
        raise AssertionError('PAIR_PARTIAL_EXIT_UNSUPPORTED')

```

## CLOSURES — documentos completos leídos

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_G_FINAL_20261021.md
SHA256 f23d675c8e1aee9fadfde9c3efc9fc0133848f60a760afa41d91840ef2405e82

```markdown
# Tanda G cerrada: dependencia AR no mejora la deriva media

Dos políticas predeclaradas con242cierres/240paresobservados ypronóstico6pasos. AR1 vscontrol6mean(y), mismohurdle.0019 heredado(señal,nocostoextra),stop2ATRsinTP/24h. Transferencia explícita deR20PAXG,norecetaBTCyaevaluada niinvención. BTC-USDTperpetuoBinance,[2020-10-15,2026-01-01),warmup3004hporlookback,desarrolloreutilizado.10k,2%/6%/3x,fee.00045+fundingconproxies,slippage0;sinestres/nuevaeconomía2026.

## BtcResearchR12Ar1m
Dashboard: http://localhost:9200/#/backtest/c72b53d8-c986-4131-814b-788cdc0f49e2

CAGR -7.4440%; neto -3320.40USDT; PF 0.9688; Sharpe -0.1392; DD M1+eventos 62.0354%; 1481 trades; meses activos positivos 27/62; trimestres 8/20. Mediana calendario -2.3918%; neto sin mejores2meses -8850.38USDT. NO_CUMPLE.

## BtcResearchR12Drift1m
Dashboard: http://localhost:9200/#/backtest/cbfafdb4-ea81-48f7-bd40-5ade91a3bfa4

CAGR -3.6236%; neto -1751.34USDT; PF 0.9830; Sharpe -0.0075; DD M1+eventos 56.1243%; 1355 trades; meses activos positivos 26/62; trimestres 8/20. Mediana calendario -1.7159%; neto sin mejores2meses -7507.85USDT. NO_CUMPLE.

Ambas pierden y excedenDD25%, no cumplenCAGR/PF/regularidad. La contribuciónARdeestaformulación no justifica conservarla. No cambiarventana,hurdle,beta,horas o seleccionarregímenes/ladosposteriorespararescate. Dos corridascerradas,ceroreemplazos. Mantenerobjetivoglobalautónomo,buscarotrapreguntamaterial.

Checkspreviostransformación/OLS240pares/forecast6/controlesvarcero ypasado:job9fdcbf0a81e94c4db9b50a909f34b509 passed,sourcehash1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343. Revisiónindependientesinerror. Auditoríajobf54b317db242406da4d9f5c6e544cb67 sobre1481/1355tradescompletos,bruto−fees+funding=PNLsum=finishing−10k a1e−6;fundingaplicado. TelemetríaM1completa,63intervalos/62meses/20Q,sumaPnL/equityfinalreconciliadas. DD M1+eventosnoextremosintraminuto;fronteraspostfunding/predecisiónsegúncontratoR11. ContadoropenpreterminalnosustituyetradesFINAL. MissingData: sinβportradeenlogs,porloquenoatribuimosresultadosarégimenβpositivo/negativo;noesnecesariopararechazarlascurvasnegativas.

Fuentes/config/manifiestoGguardadosantesdeejecutar. Sinframework/configglobal/live/paper/Pi. Evidencias BTC_DISCOVERY_G_PROTOCOL_20261021.md, BTC_DISCOVERY_G_MANIFEST_20261021.json, BTC_DISCOVERY_G_ACCOUNTING_20261021.json ytelemetrías. Ningunacandidata;Hyaestápredeclarada.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_J_FINAL_20261021.md
SHA256 904784346d1287cb21f5745303555ed3c7d16d265715203bb18d05dcd3c5ddcf

```markdown
# Tanda J cerrada: confirmación ETH frente a control BTC

Las dos políticas pierden y no cumplen los objetivos. ETH se usó sólo como información: todas las posiciones, comisiones y funding fueron BTC. La reducción de actividad mejoró el resultado relativo del tratamiento, sin generar rentabilidad ni acreditar causalidad ETH→BTC.

## Reglas y contrato

La dirección se definió con seis retornos BTC previos. BTC actual debía moverse dentro de una desviación previa; ETH_CONFIRM agregaba un shock ETH de al menos dos desviaciones en esa dirección. El control mantenía el mismo patrón BTC. Entradas horarias; stop2ATR14simple1h, TP2R y vencimiento6h. El umbralBTC1sigma fue declarado antes de ejecutar, diferente del .25sigma del antecedentePAXG. No hubo OLS residual, hedge ni estrategia ETH.

Ventana [2020-10-15,2026-01-01), desarrollo reutilizado, BTC-USDT Binance Perpetual Futures. Capital10k, riesgo2%/6%/3x, fee.00045porlado, funding histórico aplicado con proxies declarados, slippage0. Sin estrés, nueva economía2026 ni importaciones. Motor validó cobertura BTC/ETH sin ventanas inválidas.

| Política | CAGR neto | DD M1 y ejecuciones | PF | Meses activos positivos | Trimestres positivos | N |
|---|---:|---:|---:|---:|---:|---:|
| [BtcResearchR13EthConfirm1m](http://localhost:9200/#/backtest/0e718943-cb4a-4fed-b6a5-55ca1a60192a) | -8.90% | 44.24% | 0.708 | 24/61 | 4/20 | 225 |
| [BtcResearchR13BtcControl1m](http://localhost:9200/#/backtest/3dd41c61-da74-463d-a551-2fa1e618e3d0) | -81.57% | 99.99% | 0.884 | 9/62 | 1/20 | 6808 |

Dashboard: http://localhost:9200/#/backtest/0e718943-cb4a-4fed-b6a5-55ca1a60192a

BtcResearchR13EthConfirm1m: neto-3849.06USDT; bruto de precio-1318.34, fees2375.58, funding-155.13; saldo final6150.94; Sharpe-0.8971. Mediana mensual calendario-0.9073%; neto sin dos mejores meses-4697.44USDT.

Dashboard: http://localhost:9200/#/backtest/3dd41c61-da74-463d-a551-2fa1e618e3d0

BtcResearchR13BtcControl1m: neto-9998.53USDT; bruto de precio2107.80, fees11874.14, funding-232.18; saldo final1.47; Sharpe-2.9721. Mediana mensual calendario-13.0230%; neto sin dos mejores meses-12816.69USDT.

## Qué aprendimos

El control realizó6808 operaciones y terminó con1,47USDT. Su resultado bruto de precio fue positivo, pero no cubrió comisiones y funding. Es un resultado simulado completo, no una cuenta operativa ni un experimento cancelado por pérdidas parciales. ETH_CONFIRM redujo a225 operaciones, pero también perdió antes de fees. No basta reducir rotación para encontrar la ventaja. La diferencia mezcla selección, ocupación y trayectorias de capital; no es efecto causal aislado del inputETH.

Ambas fallan CAGR30, PF1.2, DD25, M65 yQ80, mediana y concentración. Los conteos por sí mismos no aportan confianza estadística. Cerrar las dos recetas y sus vecinos; no elegir long-only, otras sigmas u horas tras observar resultados.

## Auditoría y cierre

Protocolo y manifiesto guardados antes de economía. Check7efe483fb2214f7f8418e49f191211b3 passed; fuenteSHA256aea8fe53975ab2a75efdccc1f254cd15c07299faa3acdeab6466be985f91106a. Revisión independiente sin errores materiales. Análisis a189e8474f5b4e7ea94da9879d22527c completo225/6808trades: bruto−fees+funding=sumaPNL=equityfinal−10k, error<1e−6USDT. Ambas telemetrías tienen2.741.760marcasM1,63intervalos/62meses/20Q; fronteras y contribuciones reconciliadas. DDM1noextremosintraminuto; cortes mensuales postfunding/predecisión según convención por fase R11. Sin posiciones terminales, errores económicos ni reemplazos.

Fuentes: BTC_DISCOVERY_J_PROTOCOL_20261021.md, BTC_DISCOVERY_J_MANIFEST_20261021.json, BTC_DISCOVERY_J_ACCOUNTING_20261021.json y telemetrías. Framework/configglobal intactos; sinpaper/live/Pi. Desde r9 van19corridas cerradas; no son muestras independientes. Objetivo pendiente; continúa investigación autónoma con otra pregunta material.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_Q_FINAL_20261021.md
SHA256 50eea56a0a6eb1c9197a58dc7d5b1a27011bf22f422f321bb43a55688dbc707e

```markdown
# Q: desplazamiento relativo BTC/ETH, cierre

Ambas políticas pierden yningunacumpleobjetivos. RESIDUALmejorarelativamente aPRICEenCAGR/PF,pero no seafirmaedge validada/superioridadindependiente. FallanCAGR30%,PF1.2,DD25%,M65,Q80,medianapositiva yconcentración aritmética. No retirarshorts,invertirregla,z,beta,ventanas,TPoplazopararescate. PresupuestoQcerrado.

|ModeloBTCsolo|N|CAGRneto|PF|DDM1+fills|M+activos|Q+|Mediana mensual|Neto sin2mejores|Sharpe diario|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|[residual](http://localhost:9200/#/backtest/e73bf5e8-688e-4c5f-9ef9-d54f135b3329)|319|-8.3625%|0.8646|54.6898%|24/62|8/20|-1.4710%|-5843.2633|-0.4808|
|[price](http://localhost:9200/#/backtest/dd092c9a-f668-412f-aca7-b73ecf1cb76b)|312|-12.7061%|0.7761|54.5700%|22/62|6/20|-1.2504%|-6436.6213|-0.8049|

## Contraste y contrato

242barras4hBTC/ETHsincronizadas;βOLS240retornosPREVIOSexclactual,60lognivelespreviosyactualbajoMISMOβT. RESIDUALlogBTC−βlogETH,PRICEβ0. VarETHpositivafinita/sharedvalidityparaambos;βnegpermitido,sinclip/epsilon;σ<=0neutral. z<=−2long/z>=2short,freshstateavanzaaunocupado,refitpuedetransicionar. NoETHorders,nocointegraciónni neutralidaddecarteraacreditadas; una recuperación de ratio porETHno garantizagananciaBTC. No rescatarparlegacyquitandopataETHnifiltrarJdenuevo.

GestiónR11/R10frozen:unaposición2%feeaware,6%capnovinculante,3xaislado,margen90%floor8;SL2ATR14simple4h/TP2R/48hgestión4h,proteccionesM1.10k,BTC-USDTBinancePerpetualFutures,ruta1m/datosBTC4hETH4h,warmup300;[2020-10-15,2026-01-01)UTCdesarrolloobservado. Fee.00045porlado takerdescuento,fundingBTCdatasetfrozen9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571aplicado/verificado,marksproxydeclaradas,slippage0. Neto trasfees/fundingmodelados,no todoscostosreales. SinfundingETHporqueETHnooperó.

## Cuentas y calendario
[BtcResearchR17RelativeResidual1m](http://localhost:9200/#/backtest/e73bf5e8-688e-4c5f-9ef9-d54f135b3329):bruto-1824.640484,fee1803.336986,funding-31.039806,neto-3659.017276(-36.5902%),capitalfinal6340.982724USDT. DDdiarioframework-54.1618% distintoM1. Stats{"stage":"FINAL","mode":"RESIDUAL","long_fills":144,"short_fills":175,"signals":452,"occupied":133}. AñoscompletosdesdeM1mensual{"2021":9.77927073437872,"2022":27.990403894111427,"2023":-28.642193744798373,"2024":-23.34925698029996,"2025":-8.94588687871558};rolling12{"N":51,"positive":22,"min":{"start":"2023-11","finish":"2024-10","return_pct":-36.220949261646},"max":{"start":"2021-11","finish":"2022-10","return_pct":38.016726103780044}}.

[BtcResearchR17RelativePrice1m](http://localhost:9200/#/backtest/dd092c9a-f668-412f-aca7-b73ecf1cb76b):bruto-4001.107926,fee1365.602994,funding288.773547,neto-5077.937373(-50.7794%),capitalfinal4922.062627USDT. DDdiarioframework-53.5384% distintoM1. Stats{"stage":"PRETERMINAL","mode":"PRICE","long_fills":144,"short_fills":168,"signals":400,"occupied":88}. AñoscompletosdesdeM1mensual{"2021":-2.8059636410820876,"2022":-11.668302440882329,"2023":-1.113060755528894,"2024":-17.86436776885797,"2025":-21.402335504990212};rolling12{"N":51,"positive":10,"min":{"start":"2023-10","finish":"2024-09","return_pct":-28.278348351408933},"max":{"start":"2021-06","finish":"2022-05","return_pct":6.609939306708412}}.

Calendario descriptivo calculado aritméticamente deintervalosR11completosMCP;2020incompletono entra en añocompleto,51ventanas12mesessolapadasno independientes ni OOS. Resultadosporladoexplicanledger,noseusanpararetirarshorts.

## Verificación y límites

Auditoríaa55de9597b6e4e61a6f0b1a1f40ae29dsucceeded;631registrosdepolíticasalternativasnoindependientes. Fullsnapshotsgross−fees+funding=PnL=equityfinal−10000 error<1e−6USDT,fundingconciliado. Telemetríavalidada2.741.760marcasM1,63intervalos/62meses/20Q,invalid0entimestampsBTCyETH,fillcounts319y312igualesmetrics;monthlytelescopingcuadra. RESIDUALFINALpostliquidaciónterminalfeeincluida;rawopen1esmetadataPRE,no pendiente económico. PRICEPREsinposiciónterminal.

DDwallet+PnLabiertoM1/fillsno todosextremosintraminuto; cortesUTCpostfunding/predecisiónporfase,no agrupaciónestrictaeventosfecha. Mediana calendarioconinactivos,M65activoscompletos; N>=100preliminaroperativo,nopotencia/confianza.

Doschecksintéticosexitosos(99y108assertions),0errores,CODES8readbacksidénticos,root+indepreviewconformes,protocolo/manifiestoantes2motores. ExtensiónreescalaBTC/ETH ydiagnósticoproporciónperfectaδσ2.239e−16/z.9916neutral, sin cambiarfuenteeconómicaniañadirepsilon. Noclaimderobustezeconómicaporcheckmatemático. Dosbacktestseconómicoscompletados,0fallos/reemplazos/backteststécnicos. TotalA–Qdesde r9:32económicas,noindependientes;V1–V6209separadas.

No estrés/riskvariants,nuevos2026/live/paper/Pi/framework/global/install/restarts/scripts. ContinuidadR: pregunta distinta deformasmultibarra/kNNNumPymínimoconcontrolmediaglobal,protocolo/checkenpreparación,no economíaaún. R20PAXGanálogosnegativoyM/G/Angleestadospreservados, nonewfamilyclaim. No promociónoperativani estrésautomático.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_R_FINAL_20261021.md
SHA256 beffb2ddf1ca02385248217794623b8130b5eb90320f077998477a2a32f05e00

```markdown
# BTC Discovery R — cierre

Pregunta: similitud de seis retornos normalizados L2, KNN20 coseno frente a media global de los mismos 360 orígenes maduros, para pronosticar retorno de precio a24h. Protocolo previo, dos corridas completas, ninguna sustitución económica.

Ventana UTC [2020-10-15,2026-01-01), desarrollo reutilizado. Capital10000; riesgo2%/6%/aislado3x; comisión taker0.00045 por lado; funding histórico aplicado y reconciliado, con marcas proxy declaradas; slippage0. Neto=fees+funding modelados. Stop2ATR14simple, sinTP, timeout24h. No estrés ni variantes de riesgo.

|Modelo|N|CAGR%|PF|DD M1+fills%|Meses activos positivos|Trimestres positivos|Mediana mensual%|Neto sin2mejores meses|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[KNN](http://localhost:9200/#/backtest/e9f4b1d0-277a-4ef7-b10d-c72365d1809e)|1751|-18.963571|0.941229|83.138366|25/62|7/20|-0.707490|-10656.139018|
|[GLOBAL](http://localhost:9200/#/backtest/ca8c8f66-8fe0-460a-a3ac-142c565b4961)|1265|-6.824291|0.962141|57.175057|22/58|8/20|-1.773945|-7173.250998|

KNN: bruto precio 4701.021658605742; comisiones 9948.266673171467; funding -1413.6015183596885; neto -6660.846532925419; equity final 3339.1534670745136. Años completos: {"2021":16.63716600808669,"2022":-22.378583620187133,"2023":-28.484899927751172,"2024":-46.389541736351866,"2025":-25.94236968672027}. Peor ventana móvil12m -46.90821269679664%; mejor 64.84593144335804%.

GLOBAL: bruto precio 5849.171266847794; comisiones 7018.0481513692275; funding -1914.8927447151261; neto -3083.769629236552; equity final 6916.230370763464. Años completos: {"2021":-7.939920017396518,"2022":-18.40805561046753,"2023":-19.45835468464412,"2024":9.187526351732078,"2025":-19.14598573194839}. Peor ventana móvil12m -37.62939107167723%; mejor 40.855837110551164%.

Auditoría financiera de snapshots completos: job f16a68a6f6cd49108af72f2fc0fa458c succeeded; errores de reconciliación <1e-6. No totales inferidos de páginas parciales. Telemetría63filas mensuales/62meses completos/20trimestres,2741760marcas M1 por receta,0ventanas inválidas. GLOBAL usa FINAL tras liquidación terminal; contador rawopen1 es metadato previo, no exposición final. DD observa M1+fills, no todos extremos intraminuto. Frontera mensual por fase postfunding/predecisión. Ventanas móviles solapadas, no OOS ni muestras independientes.

Chequeo técnico final1169PASS, job98cb30b8d9ac40a292e01402524fef09; primer intento tuvo SyntaxError del fake harness, corregido antes de economía. N>=100 sólo suficiencia operativa preliminar, no potencia estadística.

Decisión: ninguna candidata. Se cierra R sin ajustar K, dimensión, lookback, horizonte, distancia, hurdle ni signo. El beneficio bruto no cubre costos base. Otra pregunta material puede estudiar utilidad realizable con stop, preservando modelo y parámetros; requiere protocolo y revisión de antecedentes antes de implementación. No es aprobación ni ejecución de S.

```

### strategies/FundingOiPilot4h/reports/BTC_DISCOVERY_S_FINAL_20261021.md
SHA256 de4443371df6c39fbe733a523741f1b24e7b74c8b846c0af030b3dcbf4ed3bab

```markdown
# BTC Discovery S — cierre

Pregunta material: KNN20/cosenoL2 sobre seis retornos frente a GLOBAL de los mismos360orígenes, aprendiendo dos payoffs fee-only con stop2ATR/noTP24h. Cambio de target respectoR, no ablación causal pura ni evidenciaOOS. Antecedente Angle de labels monetarios preservado sin relajar sus gates.

Ventana[2020-10-15,2026-01-01)UTC,10k,2%/6%/3xaislado,fee.00045/lado,slippage0,funding históricoBTC ON/aplicado/verificado con proxiesdeclarados. Neto real incluye fees y funding; labels sólo fees por nocional, no neto completo ni órdenes contrafactuales ejecutadas.

|Modelo|N|CAGR%|PF|DD M1+fills%|Meses activos positivos|Q positivos|Mediana mensual%|Neto sin2mejores meses|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|[KNN](http://localhost:9200/#/backtest/97da0472-42e2-4f1a-b5be-b63f02e44318)|1643|-7.729306|0.967591|61.601500|28/62|7/20|-0.693118|-6553.473222|
|[GLOBAL](http://localhost:9200/#/backtest/1709388d-cc36-411b-bac0-7102b3fceb7e)|902|-2.061120|0.984002|45.289492|22/51|8/20|0.000000|-5221.973347|

KNN: bruto precio 8033.446762119682; fees 9937.80305348834; funding -1522.7381478642626; neto -3427.094439232939; capital final 6572.905560767034. Años completos {"2021":13.76937060504475,"2022":-32.731322578714504,"2023":-24.641796751558466,"2024":10.815320884566093,"2025":-22.00274004431979}; peor/mejor12m -40.72059174553348/35.95913156432082%.

GLOBAL: bruto precio 6014.539956064877; fees 5097.655771779939; funding -1946.3559332292652; neto -1029.471748944319; capital final 8970.528251055617. Años completos {"2021":-16.528798692063063,"2022":11.31917374924667,"2023":-19.46630366742482,"2024":-3.062729372668871,"2025":-5.675761671102153}; peor/mejor12m -26.973113346761224/28.5827735700936%.

Verificación real: en ambas recetas11424decisiones4h,360orígenesválidosmínimo/máximo,11783paresmaduroscalculados,4100857cachehits,11423purges,0featureinvalid/0missinglabels. Cada path1440M1exactoscerrados/deadline24h; esto acredita cobertura de esta ejecución, no ventaja predictiva. Forecasterfee-only no representa funding/margen y puede diferir del fill real; gestiónrealheredada desdeopened_at sin modificar.

Medición63intervalos/62meses completos/20trimestres,2741760M1marks cada cuenta,0invalidwindows; PRETERMINAL=finalsinposiciónabierta. DD M1+fills, no todos extremosintraminuto; corte mensual por fase postfunding/predecisión; mediana incluye inactivos. Ventanas12m solapadas, no independientes.

Auditoría financiera dbe601b37bc44b4fb350504abba12147 succeeded de snapshots completos: gross−fees+funding=PNLsum=equityfinal−10000,error<1e-6. N>=100 es suficiencia operativa preliminar, no confianza. Checktécnico suppliedsource/sintéticos1a13343c98ea41adbf0ee4bb6d97ab74,1900PASS primerintento; padres sin cambios. Dos económicos completos,0fallos/reemplazos/backtests técnicos.

Decisión: NO_CUMPLE,ninguna candidata. Se cierra S sin vecinos deK/d/lookback/horizonte/distancia/hurdle/signo/costlabels/fundinglabels/stop/shrink ni selección retrospectiva long-only. Bruto positivo no cubre costos. Sin estrés/riesgo nuevo/2026/live/paper/imports.

Continuidad: T, faseUTC4h frente a driftGLOBAL, protocolo fijado antesdelresultadoS. Todavía requiere recibos técnicos, manifiesto y preflightantesmotores. Objetivoeconómiconoalcanzado; continuarautónomamente.

```

### strategies/OrchLateralRelativeShock1h/reports/ORCH_RELATIVE_FULL_RESULTS_20261018.md
SHA256 e37d3b891fdc866c5f774e2ef9f3a37830104e815635c8e4c27f33af5115c6ee

```markdown
# Resultado completo: descartar la hipótesis de overshoot relativo

[Backtest completo BTC/ETH](http://localhost:9200/#/backtest/62b9f852-8b48-4b4c-b59b-537e9e687a64). Estado finished sin excepciones ni cambios de parámetros tras el protocolo y smoke. Ventana2020-10-15→2025-12-31exclusivo, normal, benchmark=True, warmup240;10000USDT,5xaislado,fee0.00045porlado. Riesgo inicial máximo1%basket/0.5%porleg. Fuente verificada idéntica a la revisada antes del run. 2026 no evaluado.

## Resultado económico de la cesta, no de piernas aisladas
|Medida|Resultado|
|---|---:|
|Baskets completos|1247|
|Piernas cerradas|2494|
|Neto|−3403.1719USDT|
|Comisiones|2947.4336USDT|
|Saldo final|6596.8281USDT|
|CAGR motor|−7.6689%|
|Drawdown motor|−34.3718%|
|Winrate de basket neto|36.3272%|
|Winrate de piernas individuales|44.7875%|

El PnL de precio a cantidades y fills realizados, antes de restar comisiones pagadas, es−455.7382USDT. No es un backtestfee0: sólo indica que la pérdida no se explica exclusivamente por comisiones. Las dos direcciones de basket pierden: BTClong+ETHshort−1573.4464;BTCshort+ETHlong−1829.7255. No se exige signo positivo a una pierna de cobertura individual.

PnL de baskets por año de cierre (NO retornos anualesMTM):2020parcial−197.3331;2021−610.3368;2022−746.0941;2023−922.7507;2024−477.4752;2025−449.1820. Todos negativos. No usar estos años para crear filtros retrospectivos.

## Costes diagnósticos sobre iguales fills y cantidades
Neto con coste adicional0.0005porlado(+0.10%poroperacióncompleta de cada leg):−6678.0981USDT. Con0.00125porlado(+0.25%):−11590.4875. Es aritmética de fills fijos; no nueva simulación, no CAGR/DDestresados ni cambios de tamaños/capital posteriores.

## Auditoría de ejecución y temporalidad
Análisis MCP7dfd3225695c40f5a1012a0233005c79 succeeded, input snapshot íntegro3962420bytes. Cadaopened_at contiene exactamente dos registros BTC/ETH con lados opuestos. Cada leg tiene una entradaMARKET y una salidaEXECUTED completa; no parciales/piramidado ni duplicados de entrada. Identidad precioPnL−fee y suma de baskets/neto reconciliadas. Cantidad relativa de notionalsETH/BTC observada0.25823–1.19077; no es una verificación independiente de β ni certificado de neutralidad.

191baskets (15.317%) tienen separación entre cierres de sus piernas. Máximo3540s(59min), suma326400s(90.6667h). No sumar esa duración como exposición monetaria: aquí no se reconstruyeron marks de la pierna sobreviviente. Hold máximo12h. La ejecución es secuencial y el riesgo huérfano es real dentro del modelo, aunque ambas entradas compartan timestamp.

## Contador de posiciones terminales: precisión importante
metrics.total_open_trades informa2 yopen_pl0.83463. La inspección read-only de Strategy._terminate muestra que incrementa ese contador ANTES de forzar el cierre al terminar. Las últimas dos piernas sí tienen MARKETreduce_onlyEXECUTED,closed_at=finish_date yPNL/fees registrados. Hay1247baskets íntegros; dos piernas fueron LIQUIDADAS POR FIN DEL BACKTEST, no naturalmente cerradas por la señal. No se cambió el snapshot ni se puso el contador a cero.

Por ese contador preterminación, el guard conservador actual de auditorMTMv4 rechazaría esta sesión aunque los registros cerrados permitan reconciliarla. No se presentan porcentajes mensualesMTM improvisados; ROOT decidirá si ampliar ese contrato con evidencia de fills terminales. La conclusión de descarte ya es inequívoca por neto yDD, sin necesitar un ajuste de auditor para rescatar resultados.

## Conclusión y límites
Descartar esta formulación. OLS de retornos con α/β congeladas sólo define exposición y una referencia causal; no demuestra cointegración, estacionariedad del spread acumulado ni recuperación. Es una hipótesis de overshoot transitorio que no superó la primera falsación económica. Recuperar residualcero tampoco garantiza PnLcash positivo por derivaα, beta y aproximaciónlog→cash.

No proceder a buscar un ganador1hvs2h, aumentar riesgo, cambiar umbrales ni introducir ejecución1m para rescatar esta pérdida. La ejecución1m/data1h queda como posible control técnico de otra hipótesis que primero demuestre ventaja. Sin funding/spread/impacto/rechazos reales modelados; esos costes adicionales no aportarían validación al resultado actual.

StandaloneBTC/ETH: la referencia ya operaBTC en Binanceone-way; sumar curvas o duplicar rutaBTC no sería integración ejecutable. La referencia y2026 siguen intactos. No cambios de framework, reinicios, instalaciones ni live/Pi. La importación ETH continúa almacenando datos posteriores mientras se completa; no se usa su rendimiento2026.

## Adenda: auditoría MTM V4 de ROOT completada

Job fbb1facc83304c62857321ebe9a914c1 succeeded. Auditor con diagnóstico terminal: ambas piernas forzadas, precioPnLpreclose ywallet reconciliados sin alterar métricas del snapshot. Escalas de precios verificadas con104anclasBTC y102ETH, timestamps distintos, errores relativos~1e−15.

10/63meses activos/calendario positivos=15.873%;1/21trimestres=4.762%. Excluyendo períodos parciales de borde:9/61meses=14.754%,1/19trimestres=5.263%. Peor mes−2.66866%;peor trimestre−4.83889%;DDdailyclose−34.3730%. Retornos anualesMTM2020parcial−1.9733%,2021−6.2262%,2022−8.1165%,2023−10.9250%,2024−6.3465%,2025parcial−6.3750%.

Correlación de contribucionesMTM entre piernas−0.7603: refleja exposición opuesta, no demuestra una fuente rentable. Confirma descarte; ninguna búsqueda de parámetros ni validación2026 procede para esta formulación.

Importación ETH finalizada:03565c0b-635f-4d7d-8055-61237d918b5a,3248443velasobservadasM1,2020-08-15→2026-10-18;filasexistentes retenidas. La evaluación anterior sólo usó2020–2025.

```

## Implementación aprobada y check técnico posterior — sin economía
Job9f08bcad89ec485a8757da1d6650e9be SUCCEEDED, primer intento,0errores.12grupos materiales sintéticos, no cifra de assertions como calidad. Inputs:[], sólo código suministrado→AST/stubs y precios sintéticos, sin imports de framework/estrategias reales ni IO fueraoutput. NumPy1.26.4. Padres R10/R11/R12AR releídos y hashes intactos.

Recibos permanentes: BTC_DISCOVERY_V_TECHNICAL_CHECK_20261021.json (incluye código completo del harness y SHA) y BTC_DISCOVERY_V_TECHNICAL_PREPARATION_20261021.md. Sin backtests/drafts/manifiesto de ejecución; root revisa antes de esos pasos. No validación de cobertura/edge por sintéticos.


### CODES implementado: strategies/BtcResearchR22JointBase1m/__init__.py
SHA256 7386e9ae363ffcd6efe9696baab7d9abb6b07fef57fd542572926e1659e6f4fc; readback exacto 6421 caracteres.

```python
"""V: joint one-lag returns vs the frozen G scalar forecast; no ETH orders."""
import math
import numpy as np

from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m, return_forecast
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def joint_forecasts(btc, eth):
    """Return both forecasts or common cash; B rows=predictors, columns=responses."""
    assert btc.shape[0] == eth.shape[0] == 242
    assert np.array_equal(btc[:, 0], eth[:, 0])
    evidence = dict(reason="returns_invalid", rank=None)
    # Callers validate OHLC; finite checks also guard log/difference arithmetic.
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        returns = np.column_stack((np.diff(np.log(btc[:, 2])),
                                   np.diff(np.log(eth[:, 2]))))
    if not np.all(np.isfinite(returns)):
        return None, evidence
    x, y = returns[:-1], returns[1:]
    assert x.shape == y.shape == (240, 2)
    own = x[:, 0]
    variance = float(np.mean((own-own.mean())**2))
    if not math.isfinite(variance) or variance <= 0:
        evidence["reason"] = "ar_variance_invalid"
        return None, evidence
    xmean, ymean = np.mean(x, axis=0), np.mean(y, axis=0)
    centered_x, centered_y = x-xmean, y-ymean
    if not np.all(np.isfinite(centered_x)) or not np.all(np.isfinite(centered_y)):
        return None, evidence
    try:
        # NumPy default numerical rank is the sole rank rule; no condition cutoff.
        b, _, rank, _ = np.linalg.lstsq(centered_x, centered_y, rcond=None)
    except np.linalg.LinAlgError:
        evidence["reason"] = "lstsq_numerical_error"
        return None, evidence
    evidence["rank"] = int(rank)
    if rank != 2:
        evidence["reason"] = "var_rank_invalid"
        return None, evidence
    intercept = ymean-xmean@b
    if not np.all(np.isfinite(b)) or not np.all(np.isfinite(intercept)):
        evidence["reason"] = "coefficients_invalid"
        return None, evidence
    # Frozen scalar G helper remains authoritative; do not replace it by lstsq.
    ar_forecast = return_forecast(btc, True)
    if ar_forecast is None:
        evidence["reason"] = "ar_forecast_invalid"
        return None, evidence
    ar_beta = float(np.mean((own-own.mean())*(y[:, 0]-y[:, 0].mean()))/variance)
    ar_intercept = float(y[:, 0].mean()-ar_beta*own.mean())
    ar_state = float(returns[-1, 0])
    state, var_forecast = returns[-1].copy(), 0.
    with np.errstate(over="ignore", invalid="ignore"):
        for _ in range(6):
            # Row-vector convention: B[1,0] is ETH lag -> next BTC; A=B.T.
            state = intercept+state@b
            ar_state = ar_intercept+ar_beta*ar_state
            if not np.all(np.isfinite(state)) or not math.isfinite(ar_state):
                evidence["reason"] = "recursive_state_invalid"
                return None, evidence
            var_forecast += float(state[0])
            if not math.isfinite(var_forecast):
                evidence["reason"] = "var_forecast_invalid"
                return None, evidence
    if not math.isfinite(ar_forecast):
        evidence["reason"] = "ar_forecast_invalid"
        return None, evidence
    evidence.update(reason="valid", matrix_b=b.tolist(), intercept=intercept.tolist(),
                    ar_beta=ar_beta, ar_intercept=ar_intercept,
                    var_forecast=var_forecast, ar_forecast=float(ar_forecast))
    return dict(VAR=var_forecast, AR=float(ar_forecast)), evidence


class BtcResearchR22JointBase1m(BtcResearchR12ArBase1m):
    """Inherit G no-TP/24h fill management and the unchanged R11 M1 observer."""
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("VAR", "AR")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        btc = closed_window(self.get_candles(self.exchange, "BTC-USDT", "4h"), now, 242)
        eth = closed_window(self.get_candles(self.exchange, "ETH-USDT", "4h"), now, 242)
        if btc is None or eth is None or not np.array_equal(btc[:, 0], eth[:, 0]):
            forecasts, evidence = None, dict(reason="windows_invalid", rank=None)
        else:
            assert math.isclose(float(btc[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
            forecasts, evidence = joint_forecasts(btc, eth)
        counts = self.vars.setdefault("joint_counts", {})
        reason = evidence["reason"]
        counts[reason] = counts.get(reason, 0)+1
        if forecasts is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        forecast = forecasts[self.MODE]
        # Hurdle inherited from G is a signal rule, not an extra execution charge.
        if abs(forecast) <= .0019 or not self.START < now < self.FINISH:
            return
        self.vars["signals"] = self.vars.get("signals", 0)+1
        if self.is_open or self.entry_orders or self.vars.get("last_exit_at") == now:
            self.vars["occupied"] = self.vars.get("occupied", 0)+1
            return
        atr = atr14(btc)
        if atr is None:
            return
        direction = 1 if forecast > 0 else -1
        plan = entry_plan(float(self.price), max(0., float(self.balance)),
                          float(self.available_margin), float(self.leverage),
                          float(self.fee_rate), direction, 2*atr)
        if plan is None:
            return
        self.vars["plan"] = dict(plan, joint_evidence=evidence)
        self.vars["direction"] = direction

    def on_open_position(self, order):
        super().on_open_position(order)
        self._log("R22_JOINT_OPEN", dict(time=int(self.time), mode=self.MODE,
                  evidence=self.vars["plan"]["joint_evidence"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R22_JOINT_STATS", dict(stage=stage, mode=self.MODE,
                  counts=self.vars.get("joint_counts", {}),
                  signals=self.vars.get("signals", 0), entries=self.vars.get("entries", 0),
                  occupied=self.vars.get("occupied", 0)))

```

### CODES implementado: strategies/BtcResearchR22JointVar1m/__init__.py
SHA256 94722be2699f2c10a924182b2ab73811094e8516680d06b9e1247f9653795f02; readback exacto 153 caracteres.

```python
from strategies.BtcResearchR22JointBase1m import BtcResearchR22JointBase1m


class BtcResearchR22JointVar1m(BtcResearchR22JointBase1m):
    MODE = "VAR"

```

### CODES implementado: strategies/BtcResearchR22JointAr1m/__init__.py
SHA256 399f0f43ed1f43f68014c92f74c37534df40802f82756b9e7d8799a968f340de; readback exacto 151 caracteres.

```python
from strategies.BtcResearchR22JointBase1m import BtcResearchR22JointBase1m


class BtcResearchR22JointAr1m(BtcResearchR22JointBase1m):
    MODE = "AR"

```
