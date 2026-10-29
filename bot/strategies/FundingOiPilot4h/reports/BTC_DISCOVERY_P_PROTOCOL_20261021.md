# Tanda P — BTC individual: aislamiento de K1001 y N204 congeladas

Estado2026-10-21: diseño revisado por root, implementación técnica autorizada; aún sin drafts/economía. Este documento no afirma aprobación económica ni equivalencia histórica. Se autorizaron nuevas clases y check sintético posterior; ninguna corrida económica o draft desde este subagente.

## Pregunta material, selección e historia

¿Las recetas legacy completas K1001 y N204, operando cada una en una cuenta exclusivamente BTC con riesgo acordado, cumplen los gates individuales actuales? Dos recetas como pares originales; no seleccionar retrospectivamente sólo su componente más rentable ni sumar contribuciones de cartera. El foco es resolver una brecha de medición/aislamiento documentada, no declarar nueva familia de señales.

BTC_INDIVIDUAL_EVIDENCE_MATRIX_20261021.md distingue expresamente contribuciones K1001/N204 R12 de cuenta BTC aislada. Búsquedas readonly por título: K1001 40 sesiones, N204 84, R14 12; los casos hallados contienen tres rutas. Búsquedas standalone/individual/BTC only/BTC solo dieron cero. No se afirma censo global: el inventario general1000 agotó timeout10s, se detuvo sin bypass; MCP se recuperó y estos padres/deps se releyeron. Los resultados ya existentes2026 no se usan para elegir parámetros ni para nueva economía P.

Anclas consultadas:
- K1001: http://localhost:9200/#/backtest/3ec33cac-3ea6-43c7-9cfe-4d315930fee2
- N204: http://localhost:9200/#/backtest/436b001f-2868-44cc-890e-77d62e7a6397

Son carteras BTC/PAXG/SPY,10k,2%/6%,3x,fee.00045,ventana[2020-10-15,2025-12-31); sus CAGR publicados34.6595%/33.4551% pertenecen a esas cuentas combinadas, no al BTC individual. Formulario leído sin funding histórico configurado. Sus logs BTC registran intentos de sizing menores al objetivo: K long17/45,short182/268; N long17/45,short186/275. No son todos los eventos ni todos los fills. No deducir un CAGR BTC de estas cantidades.

Antecedentes conservados: N204 viene de X03 R2; K1001 de Y902/R9. Ambas incorporan long runner y short original, además de suplemento. R1401 deshabilitó sólo suplemento; R1402 filtró long por eficiencia>1/3; R1403 filtró long porEMA120/slope. Sus12 corridas mantuvieron tres rutas. P no reabre esos filtros, quitar short, plazos, vecinos, riesgo o gastos para rescatar un ganador. V1–V6 ya exploraron mecanismos emparentados y tienen sus rechazos completos; no se resetea historial de selección. A–O y Ncomposición A/F–B/F no equivalen a estas recetas legacy completas en una cuenta BTC. P es desarrollo adaptativo ampliamente observado, no OOS, WF prospectivo ni evidencia independiente. N y O se cierran según su evidencia, no cambian el diseño P después.

## Fuentes congeladas y dependencias

SHA256 de texto UTF8 completo leído vía read_strategy:
- CapitalR12K1001R2A6: 5ae10247b55da1af56bcd46c8a84d4df36ad7e923e3a499fa0902e6a3e9413a0
- CapitalR12N204R2A6: 5cf339d1a2f2096bc484a88c5790c677e41088db0067fe46ca333a4c5a7cfff4
- BtcResearchR11Base1m: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87
- BtcResearchR10Base4h: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9

Padres K/N son clases autocontenidas: imports math/json/numpy, jesse.helpers jh, Strategy/cached, jesse.utils e indicadores ta. No importan otra estrategia. La adaptación debe portar literalmente los bloques de señal/gestión, con cambios de acceso a la vela4h expresamente revisados, sin editar padres. El observador R11 se reutiliza sólo para medición/callback; no heredar accidentalmente sus entradas, ATR simple, TP2R o plazo48h para todos los componentes. R11 importa R10, cuyo hash se registra aunque sus helpers de señal/sizing/ATR no sustituyen los legacy.

Indicadores verificados por catálogo y get_indicator_details MCP: ta.ema(c,period,source_type='close',sequential=False), ta.atr(c,period=14,sequential=False), ta.adx(c,period=14,sequential=False), ta.rsi(c,period=14,source_type='close',sequential=False). Se conserva ta.atr existente (backend Rust), NO el helper atr14 simple de R10; EMA secuencial para pendientes preserva sus arrays. No se cambia implementación de indicadores ni se afirma hash del runtime Rust a partir de su firma. Antes de motor el recibo CODES debe congelar fuentes completas padres/adaptaciones/observador/R10 y metadatos de indicadores; hashes sólo de textos realmente leídos. Framework/broker/indicadores son runtime existente, sin modificación.

## Contrato común y cambios inevitables

Dos cuentas separadas, cada una BTC-USDT Binance Perpetual Futures; ruta de ejecución/observación1m y datos4h. Warmup2404h, suficiente para mínimo140 del short y medias80/120; No inspeccionar disponibilidad de velas antes del motor; si faltan datos, el motor lo reportará y se detendrá sin importar ni reconfigurar. Intervalo[2020-10-15,2026-01-01)UTC,10k,2%poroperación/6%agregado,3xaislado,una posición BTC, sin pirámides. Dos recetas separadas, no dos posiciones2% en una cuenta.

Fee.00045porlado taker con descuento, fundingBTC histórico ON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 aplicado/verificado en snapshot, marksproxy declaradas; slippage aplicado0. Reserva legacy.001 sólo en sizing conservada como se define abajo. Sin estrés, variantes de riesgo, nuevas pruebas económicas2026, importaciones, ML, scripts, instalaciones, reinicios, globalconfig, live/paper/Pi.

Diferencias inevitables frente a las anclas, todas declaradas: (1) sólo BTC y cuota100%, sin compartir cash/riesgo/margen/historia con otras rutas; (2) capital/qty futuros recalculados sobre esa cuenta, no mismos fills/tamaños; (3) funding aplicado modifica wallet y cantidades; (4) ejecución/observaciónM1 y reloj4h explícito pueden cambiar orden de callbacks, timestamps exactos de fill/protección/expiración y trayectoria respecto a ruta4h con replay internoM1; (5) finish2026-01-01 incluye el último día2025, mientras anclas finalizaban2025-12-31 exclusivo. No es reproducción idéntica ni comparación causal de una única ablation con esas carteras. Estas adaptaciones responden al contrato actual; ninguna se ajusta al PnL de P.

## Historia4h, acceso causal y relojes

En cada T múltiplo4h usar exclusivamente velas4h con open+4h<=T y última open=T-4h, estrictamente consecutivas/positivas/finitas y OHLC válido. Todos los self.high/self.low/self.closed_candle_open_time legacy se refieren a esa vela4h; no a la vela1m de ejecución. Precio de decisión debe coincidir con su close. Excluir cualquier vela4h parcial que get_candles exponga. Mantener la misma historia4h disponible/retención y llamadas ta que los padres; no recortar EMA/ATR a26 o14 por comodidad ni cambiar semilla/horizonte. Validar paridad con arrays de historia suministrados.

Actualizar la máquina del suplemento una sola vez por cierre4h aun ocupado/pendiente; setup es estado de precio, no depende de capital. Gap/invalidación reinicia explore_previous=False y elimina evento, sin puentearlo ni dejar reentrada en minutos posteriores. No emitir nuevas entradas en cierre inválido. Protecciones ya colocadas y deadlines temporales siguen activos; ATR inválido inhibe sólo actualización del runner, como el padre, no detiene stops ni vencimientos. No fabricar barras.

Resetear elegibilidad de entrada cadaM1; sólo en T4h, START<T<FINISH, plano/sinentrada pendiente/sin salida en mismo T, evaluar prioridad original. No cola/reversión/reentrada en mismo cierre de salida. Después del evento4h, no volver a ejecutar _signal por nuevos índicesM1. Consumir suplemento aun si perdió por prioridad/ocupación. Las señales long/short originales son condiciones reevaluadas en cada4h, no transiciones nuevas inventadas; pueden rearmarse en otro cierre4h conforme a reglas originales.

## Reglas exactas comunes (c es historia4h cerrada)

Hiperparámetros fijos de los padres, sin optimización: donchian_len26,ema_fast20,ema_slow80,adx_min26,stop_atr2,trail_atr4.2,be_r2.25. Los rangos que publican hyperparameters no autorizan búsqueda.

Prioridad cuando plano: _plan LONG_RUNNER primero; si falla _short_plan CORE_SHORT; si falla evento suplemento con _explore_size. Se conserva incluso que una candidata de prioridad superior que no puede formar plan/qty permita intentar la siguiente. Un solo plan por decisión, sin sobreescritura por should_short después de go_long.

### LONG_RUNNER

Requiere len(c)>=max(80+20,26). fast=EMA20(c); slow=EMA80(c,sequential=True); atr=ta.atr14(c); adx=ta.adx14(c); rsi=ta.rsi14(c); entry=max(c[-27:-1,high]), las26 barras previas sin actual. Valores finitos,atr>0,entry<close<=entry+atr,close>slow[-1],fast>slow[-1]>slow[-5],adx>=26,52<=rsi<=76 y high_actual-low_actual<=3atr. Distancia inicial=2atr y0<distance<entry.

Entrar BUY LIMIT al entry congelado, pendiente una4h; no convertir a MARKET. Fill real E: stop=E-distance, sinTP; best_close=E para excluir máximos/cierres anteriores al fill. En cada cierre4h POSTERIOR al fill: best_close=max(best_close,close4h); best_r=(best_close-E)/distance; mult4.2,×.62 si best_r>=8,si no×.78 si>=5. Stop candidato=best_close-mult×ATR14 actual. Si best_r>=2.25, elevar a mínimo E×(1+2.5fee). Reemplazar sólo si average_stop_loss<candidato<precio4h. Nunca aflojar stop ni aplicar retrospectivamente dentro de vela pasada. No TP ni máximo48h/72h/720h: runner sin plazo heredado. Al fill en un cierre4h no usar la barra que terminó antes de ese fill para trailing/BE; primera actualización usa un cierre4h estrictamente posterior al timestamp del fill.

### CORE_SHORT original

Requiere len(c)>=140; macro=EMA120(c,sequential=True),fast=EMA20(c),atr=ATR14(c),quick_rsi=RSI3(c), valores finitos. atr>0,macro[-1]>macro[-10],close>macro[-1]-atr,quick_rsi<=20. Entry=min(low_actual,close-.25atr);distance=fast-entry. Exigir atr<=distance<=3atr ydistance>=6fee×entry.

SELL STOP al entry congelado, pendiente una4h; sin conversión a MARKET. Fill E: stop=E+distance,TP=E-1.5atr_de_señal. Mantener ambos fijos; no trailing/BE. Salida MARKET en primer cierre4h T con T-fill_timestamp>=72h; no salida al minuto exacto si no es4h. Guardar target_distance1.5atr en plan, no recalcular por ATR de fill.

## Suplementos: comparación de los dos padres originales

Ventana mínima14 cerradas y consecutivas; s=c[-2],t=c[-1],window=c[-13:-1] (12barras anteriores a t). spans=high-low. q=volume×(2close-high-low)/span, con q0 si span0, como np.divide where del padre. Cohort=window[q>0]; VWAPcohorte=sum(volume×mean(high,low,close))/sum(volume), sólo cohorte, no todas las barras. Si cohorte vacía,VWAPNaN,setup falso. OHLCVpressure es proxy, no flujo taker observado. Se preserva validación positiva de c[:,1:] que padre _explore_window exige, incluyendo volumen>0 en sus14 últimas barras.

Setup N204: s.close>c[-14].close;sum(q)<0;s.close>=VWAP;t.close<t.open;t.close<VWAP. Setup K1001 añade efficiency=(s.close-c[-14].close)/sum(abs(c[-13:-1].close-c[-14:-2].close));path>0 y0<efficiency<=1/3. Esta diferencia está heredada, no elegida con resultadosP.

Guardar previous_setup y actualizarlo antes de elegibilidad de cuenta/ATR/distancia. Emitir evento sólo setupTrue ypreviousFalse. Después ATR14 válida;distance=max(s.high,t.high)+.25atr-t.close yatr<=distance<=3atr. Si filtro de distancia falla igualmente el setup se consumió; no retrasarlo hasta que distancia mejore.

N204: SELL MARKET al close4h conocido, con distance congelada. K1001: entry=min(s.low,t.low),SELL STOP bajo estructura de dos barras; exigir finito,entry>2distance yentry<close, además0<distance<entry, exactamente la guarda heredada. No sustituir por low de t ni por MARKET, no añadir RSI/EMA nuevos.

Fill real E de cada suplemento: stop=E+distance,TP=E-2distance,qty constante, sin trailing/BE. Deadline=fill_timestamp+48h; salida MARKET en primer cierre4h T>=deadline. Distancia/proyección de TP congeladas desde señal y centradas en E, no usar high/low anterior al fill ni recalcular estructura después.

## Pendientes, fills y protección

El nacimiento de LIMIT/STOP sucede después del cierre4h que arma la orden; no permitir fill retroactivo dentro de esa vela. Registrar signal_time,requested_entry,order_kind,expiry=signal_time+4h,distancia ytipo de componente en plan inmutable. Sólo una pendiente. En minutos intermedios should_cancel_entry=False; en primer cierre4h>=expiry cancelar/sacar reserva. La fuente real del framework (revisada por root) vuelve a consultar should_short/should_long después de cancelar si está plano y sinórdenes; se permite rearmado en el MISMO cierre4h, con planlazy memoizado y marginreleased, preservando la semántica real del padre. No rearmar en minutos intermedios ni después de cierre de posición en el mismo timestamp. No reutilizar should_cancel_entry=True de R11 cadaM1: alteraría la vida de la receta. Verificar en framework existente el orden de ejecución/cancelación exactamente en expiración y fijarlo en recibo antes de motor, sin cambiar framework. Una potencial ejecución en el minuto que termina en expiry debe seguir el orden real del motor, no un replay contrafactual nuevo.

On_open_position debe derivar stop/TP desde E=position.entry_price yqty real, nunca desde requested_entry. Conservar distances/targets heredados y el reloj de fill. Verificar con casos sintéticos LIMIT mejora/gap,STOPgap yMARKET que plannedbudget no se excede después de fees/reserva usando E real. Registrar requested/actual/risk reales y timestamps. No aceptar silenciosamente protección<=0 o riesgo planificado mayor2%; si un gap hipotético produce esa rama incompatible, tratar como bloqueo técnico previo a economía para resolver ejecución con root, no cambiar distancia,recortar pérdida ex post o seleccionar otra receta. Los gaps reales/funding posteriores no garantizan pérdida máxima2%.

M1 monitoriza equity y procesa protecciones existentes; señales/trailing/timeouts sólo4h. Sin modificar posición por señales de otro componente, sin pirámide ni scaleout. Callback de cierre limpia origen/política/reservas; si hay liquidación terminal, contabilizarla antes del FINAL del observador.

## Riesgo y margen: cambio de asignación declarado, no barrido

Capital plano=max(0,wallet); coincide con min(balance,portfolio_value) del padre cuando no hayposición. En BTC individual no usar portfolio_value para equity abierta del observador por su escala conocida. Una posición/pendiente,2% objetivo monetario total y6% límite agregado; no aumentar a4% por dos señales ni repartir2% entre trescomponentes.

CuotaATR compartida se retira: BTC100%, sin consultar PAXG/SPY, sus calendarios o historial. No retirar partes del PnL padre. Mantener techo nocional legacy4.4×capital como techo adicional, pero margen común90%con3x/fees es vinculante y nunca permite4.4x real. Planned_margin_qty=.90×available_margin×3/[requested_entry×(1+fee×3)], consistente con política común. Limitar por2%/unitrisk y techo nocional; floor(qty/.001)×.001, lotBTClegacy conservado, no floor8nuevo. Sin variantes de techo/margen/lot según resultados.

Para Eplan y stopplan, unitrisk=distance+fee×(Eplan+stopplan)+.001×Eplan. Budget=.02×capital; q_risk=budget/unitrisk. La reserva.001 legacy son10bps roundtrip de nocional que REDUCEN qty; no es comisión extra,debitcash,fillslippage o descuento de PnL. Los costes reales de backtest son fee.00045yfunding histórico; slippage aplicado0. Conservar esta reserva es paridad de tamaño y no autoriza agotar2%quitándola; puede producir riesgo stop+fees real<2%. Registrar planned_loss con ysinreserva, marginlimited,notionallimited,risklimited y qty despuéslot. No convertir la reserva a estrés ni variar. Fee actual en fill puede diferir por precio; verificar q×(distance+fee×(Eactual+stopactual)+.001×Eactual)<=budget+tolerancia numérica1e-6, sin usar tolerancia como aumento de riesgo.

## Medición, auditoría y gates

Observador R11 congelado: equity=wallet+PnLabierto, M1/fills, cortes mensuales00:00UTCpostfunding/predecisión porfase, no mes de cierre realizado ni DD4h. Preservar PRETERMINAL/FINAL con close terminal posterior. Ledger por LONG_RUNNER/CORE_SHORT/SUPPLEMENT con fills/closes/net de closed_trade.pnl; actualiza cierre ANTES callback R11. Emitir resumen compacto después del padre; no millones de logsM1. Distinguir eventos,planes,pending,cancelaciones,fills,ocupados ytransicionesconsumidas. Es medición, no selector.

Snapshots completos deben reconciliar gross−fees+funding=PNLsum=equityfinal−10k a1e-6USDT; suma ledger componentes concilia N yPNL, incluido cierre terminal. Verificar2.741.760marcasM1,63intervalos,62mesescompletos y20Qcompletos según convención; si existen huecos, no imputar cumplimiento. Reportar aportes por origen sin inferir tres estrategias independientes.

Gatesr9 por cuenta individual: CAGRnetobase>=30%,PF>=1.2,DDM1+eventos<=25%(objetivo20%),65%mesesactivospositivos,80%trimestrescompletospositivos,mediana retorno mensualcalendario>0 incluyendo inactivos,neto aritmético excluyendo los dos mejoresmeses>0. N>=100 preliminar operativo, sin convertir conteo en potencia/confianza; aspiraciones40–50%+/M70 no sustituyen gates. Fallo económico=NO_CUMPLE; favorableconmediciónfaltante=INCONCLUSA. Nopromociónporcartera histórica>30,por superar al otro padre o por componente elegido después.

## Presupuesto y gates técnicos previos

Exactamente dos económicas nuevas, K1001 individual y N204 individual. Hasta dos reemplazos sólo por fallos técnicos documentados; nunca porPnL. No nuevos vecinos, ablaciones, gestión,risk,priority,plazos o variantes de reserva después. Conservados todos intentos, sin borrar fallos. Máximo2motoresglobales/1análisispropio coordinado con root.

Antes de implementar: revisiónroot de este protocolo y diferencias4h→M1/funding/sizing. Después implementaciones nuevas sin tocarpadres; readbacks/hashes completos. Checks supplied-source AST/synthetic temporales sin importar/releerestrategias ni datosobservados: señales exactas/indicadoresinterfaces; self.high/low/candle4h; prioridad/consumo estadoocupado; invaliddata; vidaLIMIT/STOP4h sin cancelM1; fillsretroactivosprohibidos; timestamps intrabar y48h/72h alprimer4h; runner sólo postfill,sinTP/sinplazo,stopratchet; riesgo requested/actual/gap/lote/reserva/margen; unaposición; ningún sameexitempty; ledgerterminalantesFINAL. Ningún test económico oculto ni backtestdesdeanalysis. Indicadores reales deben conservarse sin sustituir por fakes en economía; tests con fakes sólo declaran qué prueban.

Con revisión ycheckpass, root creará dos drafts genuinos y manifiesto desdeformularios/preflight con fundingapplied/proxy yfuentes completas, antes de iniciar. No sesiones/manifiestosinventados. Luego auditoría/cierre yHub inmutable archivosprimero/índiceúltimo. Si ambas fallan, cerrar Psinrescates y continuar otra pregunta material bajo autorización autónoma vigente.

## CODES — snapshots completos de fuentes leídas antes de implementación

Estos bloques son texto exacto recibido por read_strategy y sus hashes figuran arriba. No son clases nuevas ni instrucciones para escribir en padres. Dependencias externas de framework/indicadores no se fingen como snapshots de código; sus firmas se registran al final.

### CapitalR12K1001R2A6

```python
import math
import json
import jesse.helpers as jh
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

# R12 R2A6: user-requested risk target 2% and aggregate admission cap 6%.
TRADE_RISK = 0.02
PORTFOLIO_RISK = 0.06
NOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.
SLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.


class CapitalR12K1001R2A6(Strategy):
    """K1001: frozen R9 single-mechanism experiment from Y902; original routes retained.

    Shared risk and margin reservations; exploratory research, not approved live.
    SPY uses a session-filtered SPX CFD proxy; holidays and native parity remain
    unverified. Parameter-neighbour variants are sensitivity controls, not winners.
    """

    def hyperparameters(self) -> list:
        return [
            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},
            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},
            {'name': 'ema_slow', 'type': int, 'min': 80, 'max': 140, 'default': 80},
            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},
            {'name': 'stop_atr', 'type': float, 'min': 1.6, 'max': 3.0, 'default': 2.0},
            {'name': 'trail_atr', 'type': float, 'min': 3.0, 'max': 5.0, 'default': 4.2},
            {'name': 'be_r', 'type': float, 'min': 1.75, 'max': 3.0, 'default': 2.25},
        ]

    def trading_hours(self):
        if self.symbol == 'SPY-USDT':
            # The fixed UTC whole-bar intersection excludes the US index daily
            # break in both DST regimes. This is an intentional common window,
            # not an assertion that the source's full session ends at 20:00 UTC.
            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}
        return None

    @property
    @cached
    def signal_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    def _entry_window(self) -> bool:
        if self.symbol != 'SPY-USDT':
            return True
        # A closed bar opening at 12:00 triggers at 16:00. Its order expires
        # at 20:00, before the excluded 20:00-24:00 bucket. A 16:00-open bar
        # must not arm a new order at 20:00. Pending orders still cancel then.
        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}
        return self.is_trading_hours and utils.is_in_trading_hours(
            self.closed_candle_open_time, window)

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

    def _volatility_share(self) -> float:
        """Reserve a common gross-exposure budget using inverse ATR fractions.

        All configured assets receive an ex-ante share, even while their signal
        is idle. This prevents the first route from consuming all shared margin.
        It is a capital-efficiency tradeoff to test, not an optimal allocation.
        """
        weights = {}
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            c = utils.filter_candles_by_hours(route.strategy.candles, route.strategy.trading_hours())
            if len(c) < int(self.hp['ema_slow']) + 20:
                return 0.0
            atr = float(ta.atr(c))
            price = float(c[-1, 2])
            if not math.isfinite(atr) or atr <= 0 or price <= 0:
                return 0.0
            # Stops use a common ATR multiple. Equal risk therefore needs
            # notional proportional to price/ATR before gross-leverage scaling.
            weights[route.symbol] = price / atr
        return weights.get(self.symbol, 0.0) / sum(weights.values()) if weights else 0.0

    def _plan(self) -> bool:
        if self.symbol not in ('BTC-USDT', 'PAXG-USDT', 'SPY-USDT') or not self._entry_window():
            return False
        c = self.signal_candles
        n = int(self.hp['donchian_len'])
        slow_n = int(self.hp['ema_slow'])
        if len(c) < max(slow_n + 20, n):
            return False
        fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))
        slow = ta.ema(c, period=slow_n, sequential=True)
        atr = float(ta.atr(c))
        adx = float(ta.adx(c))
        rsi = float(ta.rsi(c))
        # The closed bar has broken the PRIOR channel. A passive LIMIT at that
        # boundary can fill only on a future retest within one 4h order lifetime.
        entry = float(np.max(c[-n-1:-1, 3]))
        if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):
            return False
        if not (atr > 0 and entry < self.price <= entry + atr and self.price > slow[-1]
                and fast > slow[-1] > slow[-5] and adx >= self.hp['adx_min']
                and 52 <= rsi <= 76 and self.high - self.low <= 3 * atr):
            return False
        distance = float(self.hp['stop_atr']) * atr
        if not 0 < distance < entry:
            return False
        capital = self._capital()
        committed_risk, committed_notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - committed_risk))
        # Fees at both planned entry and stop, plus an explicit adverse-fill reserve.
        unit_risk = distance + self.fee_rate * (entry + entry - distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - committed_notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        # Historical research precision only. Native symbol lot/min-notional
        # constraints must be verified before any live use.
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        self._record_capacity('long', capital, budget, unit_risk, entry,
                              room, margin_room, qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {
            'qty': qty, 'entry': entry, 'distance': distance,
            'risk': qty * unit_risk, 'notional': qty * entry,
        }
        return True

    def _signal(self) -> int:
        # Compute exactly one plan per bar, with long priority. Checking
        # should_short after go_long must never overwrite a queued long plan.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            if self._plan():
                signal = 1
            elif self._short_plan():
                signal = -1
            else:
                event = self.vars.get('explore_event')
                signal = (-1 if event and self._explore_size(event) else 0)
            self.vars['signal_value'] = signal
        return self.vars['signal_value']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], plan['entry']

    def _short_plan(self) -> bool:
        """Test selloff continuation instead of buying an oversold dip.

        A rising slow regime can still suffer a fast liquidation leg. This
        exploratory hypothesis came from the failed long mean-reversion sleeve;
        it is development evidence, not an independent validation.
        """
        if self.symbol != 'BTC-USDT' or not self._entry_window():
            return False
        c = self.signal_candles
        if len(c) < 140:
            return False
        macro = ta.ema(c, period=120, sequential=True)
        fast = float(ta.ema(c, period=20))
        atr = float(ta.atr(c))
        quick_rsi = float(ta.rsi(c, period=3))
        if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, quick_rsi)):
            return False
        if not (atr > 0 and macro[-1] > macro[-10]
                and self.price > macro[-1] - atr and quick_rsi <= 20):
            return False
        entry = min(float(c[-1, 4]), self.price - 0.25 * atr)
        distance = fast - entry
        if not (atr <= distance <= 3 * atr and distance >= 6 * self.fee_rate * entry):
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry + distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        qty = min(budget / unit_risk, room / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        self._record_capacity('short', capital, budget, unit_risk, entry,
                              room, max(0.0, float(self.leveraged_available_margin) * 0.90), qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry,
                             'target_distance': 1.5 * atr}
        return True

    def go_short(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.
        # Jesse processes cancellation before evaluating the next route.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:

        plan = self.vars['plan']
        self.vars['explore_kind'] = plan.get('kind')
        if self.vars['explore_kind']:
            # Geometry is frozen at signal; protection is relative to actual fill.
            entry = float(self.position.entry_price)
            distance = plan['distance']
            self.vars['initial_distance'] = distance
            self.vars['opened_time'] = int(self.time)
            self.vars['explore_deadline'] = int(self.time) + plan['hold_hours'] * 3600000
            qty = abs(float(self.position.qty))
            if self.is_long:
                self.stop_loss = qty, entry - distance
                self.take_profit = qty, entry + plan['target_distance']
            else:
                self.stop_loss = qty, entry + distance
                self.take_profit = qty, entry - plan['target_distance']
            self._ledger().pop(self._key(), None)
            audit = self.vars.setdefault('explore_audit', {})
            audit['fills'] = audit.get('fills', 0) + 1
            jh.debug('BTC_EXPLORE_FILL ' + json.dumps({
                'recipe': self.vars['explore_kind'], 'time': int(self.time),
                'side': 'long' if self.is_long else 'short',
                'entry': entry, 'qty': qty, 'distance': distance,
                'requested_entry': float(plan['novel_requested_entry']),
                'signal_anchor': float(plan['novel_anchor']),
                'target_distance': plan['target_distance'],
                'deadline': self.vars['explore_deadline']}, sort_keys=True))
            return
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        self.vars['initial_distance'] = distance
        # An intrabar fill must not inherit highs/closes from before its entry.
        self.vars['best_close'] = entry
        if self.is_short:
            self.vars['opened_time'] = int(self.time)
            self.stop_loss = abs(self.position.qty), entry + distance
            self.take_profit = abs(self.position.qty), entry - self.vars['plan']['target_distance']
        else:
            self.stop_loss = abs(self.position.qty), entry - distance
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:

        if self.vars.get('explore_kind'):
            # Only the first closed 4h decision at/after the fill-based deadline.
            if int(self.time) >= self.vars['explore_deadline']:
                self.liquidate()
            return
        if self.is_short:
            if self.time - self.vars['opened_time'] >= 72 * 60 * 60 * 1000:
                self.liquidate()
            return
        history = self.signal_candles
        atr = float(ta.atr(history))
        if not math.isfinite(atr) or atr <= 0:
            return
        entry = float(self.position.entry_price)
        distance = self.vars['initial_distance']
        self.vars['best_close'] = max(self.vars['best_close'], float(history[-1, 2]))
        best_r = (self.vars['best_close'] - entry) / distance
        mult = float(self.hp['trail_atr'])
        # Inherited late-trend tightening; retained as a controlled baseline choice.
        if best_r >= 8:
            mult *= 0.62
        elif best_r >= 5:
            mult *= 0.78
        stop = self.vars['best_close'] - mult * atr
        if best_r >= float(self.hp['be_r']):
            stop = max(stop, entry * (1 + 2.5 * self.fee_rate))
        if self.average_stop_loss < stop < self.price:
            self.stop_loss = abs(self.position.qty), stop

    def on_close_position(self, order, closed_trade) -> None:
        if self.vars.get('explore_kind'):
            audit = self.vars.setdefault('explore_audit', {})
            audit['closes'] = audit.get('closes', 0) + 1
        self.vars['explore_kind'] = None
        self._ledger().pop(self._key(), None)

    def _record_capacity(self, side, capital, budget, unit_risk, entry,
                         room, margin_room, raw_qty, step) -> None:
        """Observe existing sizing only; never gates signals or changes quantities.

        Counts plans reaching sizing while flat and without a pending entry.
        It does not infer trades that would have filled or signals while occupied.
        Quantity tolerances below classify numerical ties, not trading thresholds.
        """
        audit = self.vars.setdefault('portfolio_capacity_audit', {})
        row = audit.setdefault(side, {'eligible_sizing_attempts': 0,
                                     'risk_budget_limited': 0,
                                     'notional_or_weight_limited': 0,
                                     'margin_limited': 0,
                                     'sized_below_trade_target': 0,
                                     'capacity_zero': 0,
                                     'zero_after_lot_rounding': 0})
        row['eligible_sizing_attempts'] += 1
        target_qty = capital * TRADE_RISK / unit_risk
        tolerance = max(1e-8, abs(target_qty) * 1e-10)
        row['risk_budget_limited'] += int(budget / unit_risk + tolerance < target_qty)
        row['notional_or_weight_limited'] += int(room / entry + tolerance < target_qty)
        row['margin_limited'] += int(margin_room / entry + tolerance < target_qty)
        row['sized_below_trade_target'] += int(raw_qty + tolerance < target_qty)
        row['capacity_zero'] += int(raw_qty <= 0 < target_qty)
        row['zero_after_lot_rounding'] += int(math.floor(raw_qty / step) * step <= 0 < raw_qty)

    def terminate(self) -> None:
        jh.debug('BTC_NOVEL ' + json.dumps({'recipe': 'K1001',
            'counts': self.vars.get('novel_audit', {})}, sort_keys=True))
        jh.debug('BTC_EXPLORE ' + json.dumps({'recipe': 'K1001',
            'counts': self.vars.get('explore_audit', {})}, sort_keys=True))
        # One compact persisted record per route, after engine final liquidation.
        # The runner requires debug_mode=True to persist these diagnostic logs.
        jh.debug('PORT_CAPACITY ' + json.dumps({
            'symbol': self.symbol, 'strategy': self.__class__.__name__,
            'trade_risk': TRADE_RISK, 'portfolio_risk': PORTFOLIO_RISK,
            'notional_cap': NOTIONAL_CAP,
            'counts': self.vars.get('portfolio_capacity_audit', {})
        }, sort_keys=True))

    def _explore_window(self, n):
        """Require the exact closed 4h clock; invalid input cannot create an event."""
        c = self.signal_candles
        if len(c) < n:
            return None
        w = c[-n:]
        if (not np.all(np.isfinite(w))
                or int(w[-1, 0]) != int(self.closed_candle_open_time)
                or w[-1, 0] + 14400000 > self.time
                or not np.all(np.diff(w[:, 0]) == 14400000)
                or not np.all(w[:, 1:] > 0)
                or not np.all(w[:, 3] >= w[:, 4])):
            return None
        return c

    def _explore_size(self, event):
        """Use the original budget, reservations, fees and volatility quota."""
        side = event['side']
        entry, distance = float(event['novel_requested_entry']), float(event['distance'])
        # Change only execution price; signal geometry remains frozen from trigger close.
        # Positive TP is a physical constraint, not a searched price-distance cut.
        if not (math.isfinite(entry) and entry > 2 * distance
                and entry < float(self.price)):
            audit = self.vars.setdefault('novel_audit', {})
            audit['invalid_candidate'] = audit.get('invalid_candidate', 0) + 1
            return False
        if not (math.isfinite(entry) and math.isfinite(distance)
                and 0 < distance < entry):
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        stop = entry - distance if side == 'long' else entry + distance
        unit_risk = distance + self.fee_rate * (entry + stop) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        step = 0.001
        self._record_capacity(side, capital, budget, unit_risk, entry,
                              room, margin_room, qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = dict(event, qty=qty, entry=entry,
                                risk=qty * unit_risk, notional=qty * entry)
        return True

    def before(self) -> None:
        # Event state is price-only and advances even while occupied or pending.
        if self.vars.get('explore_clock') == int(self.closed_candle_open_time):
            return
        self.vars['explore_event'] = None
        self.vars['explore_clock'] = int(self.closed_candle_open_time)
        c = self._explore_window(14)
        if c is None:
            self.vars['explore_previous'] = False
            return
        s, t = c[-2], c[-1]
        window = c[-13:-1]
        spans = window[:, 3] - window[:, 4]
        q = np.divide(window[:, 5] * (2 * window[:, 2] - window[:, 3] - window[:, 4]),
                      spans, out=np.zeros(12), where=spans > 0)
        cohort = window[q > 0]
        # No positive-pressure cohort means no reference cost and a false setup.
        vwap = (float(np.sum(cohort[:, 5] * np.mean(cohort[:, [3, 4, 2]], axis=1))
                      / np.sum(cohort[:, 5])) if len(cohort) else float('nan'))
        # The positive close-location cohort defines cost; an empty cohort is not a setup.
        # OHLCV pressure is a proxy, not observed taker flow.
        setup = bool(s[2] > c[-14, 2] and np.sum(q) < 0
                     and s[2] >= vwap and t[2] < t[1] and t[2] < vwap
                     and self._research_gate(c, window, q, vwap,
                         int(self.closed_candle_open_time) + 14400000))
        previous = self.vars.get('explore_previous', False)
        self.vars['explore_previous'] = setup
        if not setup or previous:
            return
        atr = float(ta.atr(c))
        if not (math.isfinite(atr) and atr > 0):
            return
        distance = float(max(s[3], t[3]) + 0.25 * atr - t[2])
        if not atr <= distance <= 3 * atr:
            return
        # Two-bar structural low asks for failure of both signal bars.
        self.vars['explore_event'] = {'side': 'short', 'kind': 'K1001',
            'distance': distance, 'target_distance': 2 * distance, 'hold_hours': 48,
            'novel_anchor': float(vwap), 'novel_requested_entry': float(min(s[4], t[4]))}
        audit = self.vars.setdefault('explore_audit', {})
        audit['events'] = audit.get('events', 0) + 1
        audit['events_occupied'] = audit.get('events_occupied', 0) + int(self.is_open)

    @staticmethod
    def _research_gate(c, window, q, vwap, decision_close):
        # One third separates a circuitous advance from a direct trend.
        # It is a single broad development cut, not a searched optimum.
        changes = c[-13:-1, 2] - c[-14:-2, 2]
        path = float(np.sum(np.abs(changes)))
        if path <= 0:
            return False
        efficiency = float(c[-2, 2] - c[-14, 2]) / path
        return bool(0 < efficiency <= 1 / 3)
```

### CapitalR12N204R2A6

```python
import math
import json
import jesse.helpers as jh
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

# R12 R2A6: user-requested risk target 2% and aggregate admission cap 6%.
TRADE_RISK = 0.02
PORTFOLIO_RISK = 0.06
NOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.
SLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.


class CapitalR12N204R2A6(Strategy):
    """Frozen X03 R2 N204; original long runners retained.

    Shared risk and margin reservations; exploratory research, not approved live.
    SPY uses a session-filtered SPX CFD proxy; holidays and native parity remain
    unverified. Parameter-neighbour variants are sensitivity controls, not winners.
    """

    def hyperparameters(self) -> list:
        return [
            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},
            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},
            {'name': 'ema_slow', 'type': int, 'min': 80, 'max': 140, 'default': 80},
            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},
            {'name': 'stop_atr', 'type': float, 'min': 1.6, 'max': 3.0, 'default': 2.0},
            {'name': 'trail_atr', 'type': float, 'min': 3.0, 'max': 5.0, 'default': 4.2},
            {'name': 'be_r', 'type': float, 'min': 1.75, 'max': 3.0, 'default': 2.25},
        ]

    def trading_hours(self):
        if self.symbol == 'SPY-USDT':
            # The fixed UTC whole-bar intersection excludes the US index daily
            # break in both DST regimes. This is an intentional common window,
            # not an assertion that the source's full session ends at 20:00 UTC.
            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}
        return None

    @property
    @cached
    def signal_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    def _entry_window(self) -> bool:
        if self.symbol != 'SPY-USDT':
            return True
        # A closed bar opening at 12:00 triggers at 16:00. Its order expires
        # at 20:00, before the excluded 20:00-24:00 bucket. A 16:00-open bar
        # must not arm a new order at 20:00. Pending orders still cancel then.
        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}
        return self.is_trading_hours and utils.is_in_trading_hours(
            self.closed_candle_open_time, window)

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

    def _volatility_share(self) -> float:
        """Reserve a common gross-exposure budget using inverse ATR fractions.

        All configured assets receive an ex-ante share, even while their signal
        is idle. This prevents the first route from consuming all shared margin.
        It is a capital-efficiency tradeoff to test, not an optimal allocation.
        """
        weights = {}
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            c = utils.filter_candles_by_hours(route.strategy.candles, route.strategy.trading_hours())
            if len(c) < int(self.hp['ema_slow']) + 20:
                return 0.0
            atr = float(ta.atr(c))
            price = float(c[-1, 2])
            if not math.isfinite(atr) or atr <= 0 or price <= 0:
                return 0.0
            # Stops use a common ATR multiple. Equal risk therefore needs
            # notional proportional to price/ATR before gross-leverage scaling.
            weights[route.symbol] = price / atr
        return weights.get(self.symbol, 0.0) / sum(weights.values()) if weights else 0.0

    def _plan(self) -> bool:
        if self.symbol not in ('BTC-USDT', 'PAXG-USDT', 'SPY-USDT') or not self._entry_window():
            return False
        c = self.signal_candles
        n = int(self.hp['donchian_len'])
        slow_n = int(self.hp['ema_slow'])
        if len(c) < max(slow_n + 20, n):
            return False
        fast = float(ta.ema(c, period=int(self.hp['ema_fast'])))
        slow = ta.ema(c, period=slow_n, sequential=True)
        atr = float(ta.atr(c))
        adx = float(ta.adx(c))
        rsi = float(ta.rsi(c))
        # The closed bar has broken the PRIOR channel. A passive LIMIT at that
        # boundary can fill only on a future retest within one 4h order lifetime.
        entry = float(np.max(c[-n-1:-1, 3]))
        if not all(math.isfinite(v) for v in (fast, slow[-1], slow[-5], atr, adx, rsi, entry)):
            return False
        if not (atr > 0 and entry < self.price <= entry + atr and self.price > slow[-1]
                and fast > slow[-1] > slow[-5] and adx >= self.hp['adx_min']
                and 52 <= rsi <= 76 and self.high - self.low <= 3 * atr):
            return False
        distance = float(self.hp['stop_atr']) * atr
        if not 0 < distance < entry:
            return False
        capital = self._capital()
        committed_risk, committed_notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - committed_risk))
        # Fees at both planned entry and stop, plus an explicit adverse-fill reserve.
        unit_risk = distance + self.fee_rate * (entry + entry - distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - committed_notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        # Historical research precision only. Native symbol lot/min-notional
        # constraints must be verified before any live use.
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        self._record_capacity('long', capital, budget, unit_risk, entry,
                              room, margin_room, qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {
            'qty': qty, 'entry': entry, 'distance': distance,
            'risk': qty * unit_risk, 'notional': qty * entry,
        }
        return True

    def _signal(self) -> int:
        # Compute exactly one plan per bar, with long priority. Checking
        # should_short after go_long must never overwrite a queued long plan.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            if self._plan():
                signal = 1
            elif self._short_plan():
                signal = -1
            else:
                event = self.vars.get('explore_event')
                signal = (-1 if event and self._explore_size(event) else 0)
            self.vars['signal_value'] = signal
        return self.vars['signal_value']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], plan['entry']

    def _short_plan(self) -> bool:
        """Test selloff continuation instead of buying an oversold dip.

        A rising slow regime can still suffer a fast liquidation leg. This
        exploratory hypothesis came from the failed long mean-reversion sleeve;
        it is development evidence, not an independent validation.
        """
        if self.symbol != 'BTC-USDT' or not self._entry_window():
            return False
        c = self.signal_candles
        if len(c) < 140:
            return False
        macro = ta.ema(c, period=120, sequential=True)
        fast = float(ta.ema(c, period=20))
        atr = float(ta.atr(c))
        quick_rsi = float(ta.rsi(c, period=3))
        if not all(math.isfinite(v) for v in (macro[-1], macro[-10], fast, atr, quick_rsi)):
            return False
        if not (atr > 0 and macro[-1] > macro[-10]
                and self.price > macro[-1] - atr and quick_rsi <= 20):
            return False
        entry = min(float(c[-1, 4]), self.price - 0.25 * atr)
        distance = fast - entry
        if not (atr <= distance <= 3 * atr and distance >= 6 * self.fee_rate * entry):
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry + distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        qty = min(budget / unit_risk, room / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        self._record_capacity('short', capital, budget, unit_risk, entry,
                              room, max(0.0, float(self.leveraged_available_margin) * 0.90), qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry,
                             'target_distance': 1.5 * atr}
        return True

    def go_short(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.
        # Jesse processes cancellation before evaluating the next route.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:

        plan = self.vars['plan']
        self.vars['explore_kind'] = plan.get('kind')
        if self.vars['explore_kind']:
            # Geometry is frozen at signal; protection is relative to actual fill.
            entry = float(self.position.entry_price)
            distance = plan['distance']
            self.vars['initial_distance'] = distance
            self.vars['opened_time'] = int(self.time)
            self.vars['explore_deadline'] = int(self.time) + plan['hold_hours'] * 3600000
            qty = abs(float(self.position.qty))
            if self.is_long:
                self.stop_loss = qty, entry - distance
                self.take_profit = qty, entry + plan['target_distance']
            else:
                self.stop_loss = qty, entry + distance
                self.take_profit = qty, entry - plan['target_distance']
            self._ledger().pop(self._key(), None)
            audit = self.vars.setdefault('explore_audit', {})
            audit['fills'] = audit.get('fills', 0) + 1
            jh.debug('BTC_EXPLORE_FILL ' + json.dumps({
                'recipe': self.vars['explore_kind'], 'time': int(self.time),
                'side': 'long' if self.is_long else 'short',
                'entry': entry, 'qty': qty, 'distance': distance,
                'target_distance': plan['target_distance'],
                'deadline': self.vars['explore_deadline']}, sort_keys=True))
            return
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        self.vars['initial_distance'] = distance
        # An intrabar fill must not inherit highs/closes from before its entry.
        self.vars['best_close'] = entry
        if self.is_short:
            self.vars['opened_time'] = int(self.time)
            self.stop_loss = abs(self.position.qty), entry + distance
            self.take_profit = abs(self.position.qty), entry - self.vars['plan']['target_distance']
        else:
            self.stop_loss = abs(self.position.qty), entry - distance
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:

        if self.vars.get('explore_kind'):
            # Only the first closed 4h decision at/after the fill-based deadline.
            if int(self.time) >= self.vars['explore_deadline']:
                self.liquidate()
            return
        if self.is_short:
            if self.time - self.vars['opened_time'] >= 72 * 60 * 60 * 1000:
                self.liquidate()
            return
        history = self.signal_candles
        atr = float(ta.atr(history))
        if not math.isfinite(atr) or atr <= 0:
            return
        entry = float(self.position.entry_price)
        distance = self.vars['initial_distance']
        self.vars['best_close'] = max(self.vars['best_close'], float(history[-1, 2]))
        best_r = (self.vars['best_close'] - entry) / distance
        mult = float(self.hp['trail_atr'])
        # Inherited late-trend tightening; retained as a controlled baseline choice.
        if best_r >= 8:
            mult *= 0.62
        elif best_r >= 5:
            mult *= 0.78
        stop = self.vars['best_close'] - mult * atr
        if best_r >= float(self.hp['be_r']):
            stop = max(stop, entry * (1 + 2.5 * self.fee_rate))
        if self.average_stop_loss < stop < self.price:
            self.stop_loss = abs(self.position.qty), stop

    def on_close_position(self, order, closed_trade) -> None:
        if self.vars.get('explore_kind'):
            audit = self.vars.setdefault('explore_audit', {})
            audit['closes'] = audit.get('closes', 0) + 1
        self.vars['explore_kind'] = None
        self._ledger().pop(self._key(), None)

    def _record_capacity(self, side, capital, budget, unit_risk, entry,
                         room, margin_room, raw_qty, step) -> None:
        """Observe existing sizing only; never gates signals or changes quantities.

        Counts plans reaching sizing while flat and without a pending entry.
        It does not infer trades that would have filled or signals while occupied.
        Quantity tolerances below classify numerical ties, not trading thresholds.
        """
        audit = self.vars.setdefault('portfolio_capacity_audit', {})
        row = audit.setdefault(side, {'eligible_sizing_attempts': 0,
                                     'risk_budget_limited': 0,
                                     'notional_or_weight_limited': 0,
                                     'margin_limited': 0,
                                     'sized_below_trade_target': 0,
                                     'capacity_zero': 0,
                                     'zero_after_lot_rounding': 0})
        row['eligible_sizing_attempts'] += 1
        target_qty = capital * TRADE_RISK / unit_risk
        tolerance = max(1e-8, abs(target_qty) * 1e-10)
        row['risk_budget_limited'] += int(budget / unit_risk + tolerance < target_qty)
        row['notional_or_weight_limited'] += int(room / entry + tolerance < target_qty)
        row['margin_limited'] += int(margin_room / entry + tolerance < target_qty)
        row['sized_below_trade_target'] += int(raw_qty + tolerance < target_qty)
        row['capacity_zero'] += int(raw_qty <= 0 < target_qty)
        row['zero_after_lot_rounding'] += int(math.floor(raw_qty / step) * step <= 0 < raw_qty)

    def terminate(self) -> None:
        jh.debug('BTC_EXPLORE ' + json.dumps({'recipe': 'N204',
            'counts': self.vars.get('explore_audit', {})}, sort_keys=True))
        # One compact persisted record per route, after engine final liquidation.
        # The runner requires debug_mode=True to persist these diagnostic logs.
        jh.debug('PORT_CAPACITY ' + json.dumps({
            'symbol': self.symbol, 'strategy': self.__class__.__name__,
            'trade_risk': TRADE_RISK, 'portfolio_risk': PORTFOLIO_RISK,
            'notional_cap': NOTIONAL_CAP,
            'counts': self.vars.get('portfolio_capacity_audit', {})
        }, sort_keys=True))

    def _explore_window(self, n):
        """Require the exact closed 4h clock; invalid input cannot create an event."""
        c = self.signal_candles
        if len(c) < n:
            return None
        w = c[-n:]
        if (not np.all(np.isfinite(w))
                or int(w[-1, 0]) != int(self.closed_candle_open_time)
                or w[-1, 0] + 14400000 > self.time
                or not np.all(np.diff(w[:, 0]) == 14400000)
                or not np.all(w[:, 1:] > 0)
                or not np.all(w[:, 3] >= w[:, 4])):
            return None
        return c

    def _explore_size(self, event):
        """Use the original budget, reservations, fees and volatility quota."""
        side = event['side']
        entry, distance = float(self.price), float(event['distance'])
        if not (math.isfinite(entry) and math.isfinite(distance)
                and 0 < distance < entry):
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        stop = entry - distance if side == 'long' else entry + distance
        unit_risk = distance + self.fee_rate * (entry + stop) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        step = 0.001
        self._record_capacity(side, capital, budget, unit_risk, entry,
                              room, margin_room, qty, step)
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = dict(event, qty=qty, entry=entry,
                                risk=qty * unit_risk, notional=qty * entry)
        return True

    def before(self) -> None:
        # Event state is price-only and advances even while occupied or pending.
        if self.vars.get('explore_clock') == int(self.closed_candle_open_time):
            return
        self.vars['explore_event'] = None
        self.vars['explore_clock'] = int(self.closed_candle_open_time)
        c = self._explore_window(14)
        if c is None:
            self.vars['explore_previous'] = False
            return
        s, t = c[-2], c[-1]
        window = c[-13:-1]
        spans = window[:, 3] - window[:, 4]
        q = np.divide(window[:, 5] * (2 * window[:, 2] - window[:, 3] - window[:, 4]),
                      spans, out=np.zeros(12), where=spans > 0)
        cohort = window[q > 0]
        # No positive-pressure cohort means no reference cost and a false setup.
        vwap = (float(np.sum(cohort[:, 5] * np.mean(cohort[:, [3, 4, 2]], axis=1))
                      / np.sum(cohort[:, 5])) if len(cohort) else float('nan'))
        # The positive close-location cohort defines cost; an empty cohort is not a setup.
        # OHLCV pressure is a proxy, not observed taker flow.
        setup = bool(s[2] > c[-14, 2] and np.sum(q) < 0
                     and s[2] >= vwap and t[2] < t[1] and t[2] < vwap)
        previous = self.vars.get('explore_previous', False)
        self.vars['explore_previous'] = setup
        if not setup or previous:
            return
        atr = float(ta.atr(c))
        if not (math.isfinite(atr) and atr > 0):
            return
        distance = float(max(s[3], t[3]) + 0.25 * atr - t[2])
        if not atr <= distance <= 3 * atr:
            return
        self.vars['explore_event'] = {'side': 'short', 'kind': 'N204',
            'distance': distance, 'target_distance': 2 * distance, 'hold_hours': 48}
        audit = self.vars.setdefault('explore_audit', {})
        audit['events'] = audit.get('events', 0) + 1
        audit['events_occupied'] = audit.get('events_occupied', 0) + int(self.is_open)
```

### BtcResearchR11Base1m

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

### BtcResearchR10Base4h

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

### Metadatos de indicadores, no código ni hash de runtime

```json
{
  "ema": {
    "status": "success",
    "indicator_name": "ema",
    "signature": "(candles: numpy.ndarray, period: int = 5, source_type: str = 'close', sequential: bool = False) -> Union[float, numpy.ndarray]",
    "parameters": {
      "candles": {
        "name": "candles",
        "default": null,
        "annotation": "<class 'numpy.ndarray'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      },
      "period": {
        "name": "period",
        "default": 5,
        "annotation": "<class 'int'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      },
      "source_type": {
        "name": "source_type",
        "default": "close",
        "annotation": "<class 'str'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      },
      "sequential": {
        "name": "sequential",
        "default": false,
        "annotation": "<class 'bool'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      }
    },
    "return_annotation": "typing.Union[float, numpy.ndarray]",
    "docstring": "EMA - Exponential Moving Average\n\n    :param candles: np.ndarray\n    :param period: int - default: 5\n    :param source_type: str - default: \"close\"\n    :param sequential: bool - default: False\n\n    :return: float | np.ndarray",
    "namedtuple_info": null,
    "usage_example": "import jesse.indicators as ta\n\n# Basic usage\nresult = ta.ema(self.candles, period=5)\n\n# Get full series (sequential=True)\nresult = ta.ema(self.candles, period=5, sequential=True)",
    "file_path": "/src/jesse/indicators/ema.py",
    "message": "Successfully retrieved details for indicator: ema"
  },
  "atr": {
    "status": "success",
    "indicator_name": "atr",
    "signature": "(candles: numpy.ndarray, period: int = 14, sequential: bool = False) -> Union[float, numpy.ndarray]",
    "parameters": {
      "candles": {
        "name": "candles",
        "default": null,
        "annotation": "<class 'numpy.ndarray'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      },
      "period": {
        "name": "period",
        "default": 14,
        "annotation": "<class 'int'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      },
      "sequential": {
        "name": "sequential",
        "default": false,
        "annotation": "<class 'bool'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      }
    },
    "return_annotation": "typing.Union[float, numpy.ndarray]",
    "docstring": "ATR - Average True Range using optimized Rust implementation\n\n    :param candles: np.ndarray\n    :param period: int - default: 14\n    :param sequential: bool - default: False\n\n    :return: float | np.ndarray",
    "namedtuple_info": null,
    "usage_example": "import jesse.indicators as ta\n\n# Basic usage\nresult = ta.atr(self.candles, period=14)\n\n# Get full series (sequential=True)\nresult = ta.atr(self.candles, period=14, sequential=True)",
    "file_path": "/src/jesse/indicators/atr.py",
    "message": "Successfully retrieved details for indicator: atr"
  },
  "adx": {
    "status": "success",
    "indicator_name": "adx",
    "signature": "(candles: numpy.ndarray, period: int = 14, sequential: bool = False) -> Union[float, numpy.ndarray]",
    "parameters": {
      "candles": {
        "name": "candles",
        "default": null,
        "annotation": "<class 'numpy.ndarray'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      },
      "period": {
        "name": "period",
        "default": 14,
        "annotation": "<class 'int'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      },
      "sequential": {
        "name": "sequential",
        "default": false,
        "annotation": "<class 'bool'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      }
    },
    "return_annotation": "typing.Union[float, numpy.ndarray]",
    "docstring": "ADX - Average Directional Movement Index\n\n    :param candles: np.ndarray, expected 2D array with OHLCV data where index 3 is high, index 4 is low, and index 2 is close\n    :param period: int - default: 14\n    :param sequential: bool - if True, return full series, else return last value\n    :return: float | np.ndarray",
    "namedtuple_info": null,
    "usage_example": "import jesse.indicators as ta\n\n# Basic usage\nresult = ta.adx(self.candles, period=14)\n\n# Get full series (sequential=True)\nresult = ta.adx(self.candles, period=14, sequential=True)",
    "file_path": "/src/jesse/indicators/adx.py",
    "message": "Successfully retrieved details for indicator: adx"
  },
  "rsi": {
    "status": "success",
    "indicator_name": "rsi",
    "signature": "(candles: numpy.ndarray, period: int = 14, source_type: str = 'close', sequential: bool = False) -> Union[float, numpy.ndarray]",
    "parameters": {
      "candles": {
        "name": "candles",
        "default": null,
        "annotation": "<class 'numpy.ndarray'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      },
      "period": {
        "name": "period",
        "default": 14,
        "annotation": "<class 'int'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      },
      "source_type": {
        "name": "source_type",
        "default": "close",
        "annotation": "<class 'str'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      },
      "sequential": {
        "name": "sequential",
        "default": false,
        "annotation": "<class 'bool'>",
        "kind": "POSITIONAL_OR_KEYWORD"
      }
    },
    "return_annotation": "typing.Union[float, numpy.ndarray]",
    "docstring": "RSI - Relative Strength Index\n\n    :param candles: np.ndarray\n    :param period: int - default: 14\n    :param source_type: str - default: \"close\"\n    :param sequential: bool - default: False\n\n    :return: float | np.ndarray",
    "namedtuple_info": null,
    "usage_example": "import jesse.indicators as ta\n\n# Basic usage\nresult = ta.rsi(self.candles, period=14)\n\n# Get full series (sequential=True)\nresult = ta.rsi(self.candles, period=14, sequential=True)",
    "file_path": "/src/jesse/indicators/rsi.py",
    "message": "Successfully retrieved details for indicator: rsi"
  }
}
```

## Addendum de revisión del reloj antes del motor

La documentación MCP jesse://strategy presenta un else simplificado que sugería que cancelar consumía el ciclo. Root comprobó fuente real Strategy.py:_check1106/1150 y _execute_cancel844: cancelar reseteaórdenes y después reevalúa entradas si estáplano/sinórdenes. Esa evidencia de código prevalece: P usa _prepare_entry lazy en should_short/long, memo porT, estado suplemento una vez en before, sizing después de liberarmargen y admite rearmado TTL mismo4h. No cancela cadaM1 ni admite reentrada en mismo timestamp de salida de posición. La documentación no especifica el orden intrabar del minuto que termina en expiry frente al callbackcancel: los checks sólo validan política, no inventan orden de broker. Root debe resolver esa precisión antes de motor mediante documentación/fuente framework permitida. Se registran history_min/max para exponer la retención realmente recibida; los checks no prueban semillas numéricas del runtime de indicadores con fakes.

## Check de implementación P

Segundo análisis temporal d51ec9023e254adf866ad6b9de27d089 succeeded,5962 aserciones; ASTprovidedsource/stubs, sin datosobservados/importsestrategiasreales/framework. Paridad con métodos padres exactos suministrados y features artificiales:75long/29short/6K/7Ncasospositivos. Primer análisis9b621b05a6384925bfd5ab3a8e91e8f4 falló SyntaxError en expresión VWAP nueva antes de pruebas; se corrigió paréntesis y se preserva error en recibo. No backtests técnicos/económicos. La paridad sintética no acredita semillas reales de indicadores, retención4h-vs-data4h ni orden brokerintrabar TTL, que root revisa antes del motor.
