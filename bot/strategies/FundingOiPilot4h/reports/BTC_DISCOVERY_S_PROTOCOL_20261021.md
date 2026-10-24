# Tanda S — protocolo de viabilidad: target de payoff fee-only con stop24h

Estado2026-10-21: protocolo revisado por root; IMPLEMENTACIÓN Y CHECKS SINTÉTICOS AUTORIZADOS. Todavía sin drafts/economía. Se crearán sólo fuentes nuevas y análisis temporales supplied-source/stubs, sin precios observados/importsframework ni mutación de padres. No importación ni inspección de cobertura.

## Pregunta material y relación con historia

¿El mismo estimador de formasBTC24h de R cambia materialmente su operativa al aprender utilidad long/short realizable bajo stop2ATR/noTP24h, en lugar de retorno final bruto de precio? La necesidad representacional está en el TARGET: SL y fees transforman de forma no lineal y asimétrica el precio terminal en payoff. La justificación no es que otras recetas hayan fallado, ni supone que cambiar target vaya a generar rentabilidad.

R se conserva cerrado sin vecinos: KNN/GLOBAL fueron negativos y no se vuelve a calibrar suK,d6,ventana360,h6,cosine,L2,empates,umbral. S es hipótesis posterior adaptativa, no ablation pura sin confusores ni OOS. Los precios/datos2020–2025 ya fueron ampliamente explorados. Comparaciones conR serán descriptivas; S añade validez path/ATR pororigen que puede excluir candidatos queRretuvo, sin ampliar ventana ni llenar cupos.

Antecedente IMPORTANTE: AngleBtcProbability4h YA calcula dos labels long/short con minutos futuros maduros, stopfirst/gapopen y fees. Fuente leída completa. Su receta usa3ATR4h,unidadesR,240minutos/4h,cuatrobins,ventana1080,min80porestado,shrink20 yunaSEmás haircut10bp; sus cero señales no autorizan quitarle puertas para promoverla. S no importa su estimador ni relaja un gate deAngle: aplica payoff matemático al kNN/GLOBAL deR ya definido, horizonte24h y unidadretorno sobre nocional. Se mantiene toda su historia como antecedente; no afirmar novedad universal ni independencia.

Fuentes completas releídasMCP ySHA256:
- AngleBtcProbability4h: d4add40c46e6c46210e77b976e93759da8ee368d182ec5343c453a7dc7ab47c1
- BtcResearchR18AnalogueBase1m: e8fc9ba9710cef644a41e32608b3132d38d6aca55f5027f259b1c147404e9e2e
- BtcResearchR10Base4h: 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9
- BtcResearchR12ArBase1m: 1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343
- BtcResearchR11Base1m: be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87

## Estimador y features: R congelado, padding sólo para ATR

En cada T4h usar380velasBTC4h cerradas consecutivas OHLCfinitas/positivas/coherentes,últimaopen=T-4h;currentindex379. La ventana de FEATURES es EXACTAMENTE rows[8:380],372velas igualqueR; las8anteriores sólo sirven para construirATRdel primerorigen. No cambiar años/horizonte, no mover origen para conseguir labels fáciles.

Mapping:
- Rlocalindex0..371 correspondeSpaddedindex8..379.
- OrígenesR6..365 sonSpadded14..373 inclusive:360candidatos exactos, ages365..6barras4h desdecurrent.
- Featureorigen i=seislogreturns de closes[i−6:i+1].
- Currentfeature closes373..379, seisretornos.
- ATRprimerorigen i14 usa15OHLC rows0..14;TRde14barrasj1..14 conprevclosej0..13. Por eso se requieren8OHLCprevias, no14extra ni recortar orígenes a352.
- Deadline label_i = close_time_i+6BAR;últimoorigen373 madura precisamente enTcurrent379.

FeatureL2 unitaria, pastnorma0/nofinita excluido, currentnorma0/nofinita neutralCOMÚN. Misma ventana360, no últimos360válidos. Sin eps/clipping/recenter/vol-normalization nueva.

KNNtop20porcosine descendente; exacttiesolderoriginfirst con sortestable; mediauniforme. Sinminseparaciónembargoextra ni distancethreshold. GLOBALmedia de amboslabels entreTODOSlosorígenesválidos del mismo set. Amboscomparten validezM1/ATR/labels, no seleccionarvecinos diferentes para long yshort. >=20orígenesválidos compartidos. No enseñar tamaño/fees/funding futuros ni trayectoria de capital del backtest.

Los labels se solapan entre sí y con partes del featureactual conocidas enT. Esa reutilización es causal pero no crea20regímenesindependientes, potencia o significancia. Entrenamientoonline causal dentrodeuna trayectoria, no WFposthoc.

## Entry/ATR/stop conocidos al origen

Origen i tiene timestamp T_i = OHLCopen_i+4h. Entryhipotético E_i=C_i. ATR_i=R10atr14(rows[i−14:i+1]) SIMPLE: promedio14TR concloseprevio, incluyeorigen; distanciaD_i=2ATR_i. No usarATRactualT, ATRdeexit, ta.atr diferente o barrahorizontefutura. Ambosstops fijos y sinTP:
longstop=E_i−D_i;shortstop=E_i+D_i.

Requerir E_i,D_i finitos/positivos y longstop>0 (shortstoptambiénfinito/positivo), para que amboscontrafactuales tengan protección física válida. Si falla, origen inválido paraambos. No adaptar distancia a cada side ni clip a1/leverage. Este filtro físico compartido se declara antes de economía; no aumenta riesgo delmotor. Los retornoslabels son pornosional, no inferencia de liquidación/margen del exchange.

## M1: madurez y validez compartida

Fuentepermitida sólo candlesM1BTC disponibles en el runtime asofT. El label de cadaorigen necesita EXACTAMENTE1440M1 con OPENtimestamps:
T_i + k×60000 para k=0..1439.
Últimoopen=T_i+24h−1m ysuclose=T_i+24h. TODOSdebenestar cerradosenT:open+1m<=T. Se excluye el minuto que termina enT_i yse incluye el que termina enT_i+24h. Timestamp exacto, sin duplicados/huecos/forwardfill;OHLCfinitos/positivos/coherentes. Volumen no entra al label y no agrega filtro. Madurez exige T>=T_i+24h aunque ambasramas ya tocaronstop alprimer minuto. No completar labeltemprano, censurar supervivientes o etiquetar conpathparcial.

Gate fijado por root antes de implementar: origen conpathincompleto/ATRinválido/normainválida se excluye DEAMBOSmodelos yamboslabels; cash siquedan<20válidos, sin ampliar360. Currentfeatureinválido tambiénimplicacashcomún. No se exigen360válidos artificialmente, ni se aprueba label que sólo tenga minutos hasta primerstop. Se conservapolítica>=20válidos delestimadorR y se exige1440completos para cada origen queentra; registrarconteos/mínimoválidos/faltantes.

Un streamM1sin historia suficiente no se imputa ni consulta datos externos: produce missinglabels/cash hasta alcanzarelgate predeclarado, con contadores visibles. El motor es autoridad de datos faltantes; NOget_existing_candles ni precheck/importaciones. La revisión estática de root indica loadermax4h400≈96000M1 yDynamicNumpyArraynodrop; esto hace viable acceder~61d a laspaths más antiguas, pero NO demuestra completitud deM1 enunrun. Historiavisible yconteo de labels se deben medir cuando haya implementación/motor autorizado; este protocolo no afirma validación de datos.

## Dos labels fee-only, stopfirst y gapadverso

Para CADA lado side∈{+1,−1}, recorrer1440minutos cronológicos delmismopath COMPLETO; salidaE independiente de la delotrocontrafactual. NoTP.
- Long: primerrow cuyo low<=stoplong sale a min(row.open,stoplong).
- Short: primerrow cuyo high>=stopshort sale a max(row.open,stopshort).
- Son toques inclusivos. OHLCcoherente asegura que openinggapadverso tambiéncumplelow/high;min/max aplica filldeaperturaadverso envezdeinventarprecio destopmejor.
- Si no hubo touch enTODOelhorizonte, saliralclose deúltimaM1, T_i+24h.
- Enúltimominuto checkstop ANTES de asignarcierretemporal; stop gana si tocaenminuto1439 aunqueelclosefueraotro.
- Una vezprimerstop tocado, ignorarsubsecuentesprices PARAEXITdeeselado; elpathrestante sigue obligatorioPARAVALIDEZ/MADUREZcompartida.
- No peak/recovery, trailing,BE,salidasaprendidas oescenariosintrabarconTP; no hayambigüedadSL/TP porqueTPno existe.

Etiqueta:
utility_side = side×(exit_side−E_i)/E_i − .00045×(E_i+exit_side)/E_i.

Unidad: retornoARITMÉTICO fee-only sobre1unidad de nocional inicial. No Rmultiple, no logreturn, no retorno apalancado deequity,no haircutAngle. Los dos fees usanentryyexitrespectivos, con denominadorE_i; long/short nose obtienen negandounmismoretorno porque pueden tener stopsdistintos y distintos exits. Feeconstante.00045 conocidoenorigen según contrato, nofeerateestimadodespués.

**Funding NO entra en labels. No llamarlos neto completo ni retornofinalrealizado.** Los cargosfunding históricos sí se aplicarán alledgerREAL de lasoperacionesdeS,igualalrestodeinvestigación. Entrenamiento no pronostica funding ni usa pagosfuturos, yunautilidadfee-onlypositiva puede quedarnegativa despuésfunding. Slippageaplicado0,no reserve/costextra enlabel. No backtestanidado, rutasvirtuales,broker oculto ni paper/live: es una función matemática contrafactual sobreOHLCM1yaobservado.

No se afirma igualdad exacta con fills delbroker real:el label usaentradaC_origen yprimerstop congapregladeclarada; una ejecuciónreal podría diferir porsemánticadeengine,fees/funding,previoestadoocupado o timestampdeentrada. Las operacionesreales usan mecanismosJesse y su auditoría. Root revisará timing ycasosgap antes de motor; no se modifica framework para acomodar labels.

## Forecaster y decisión

Para el setcomún válido:
- KNNelige20vecinosUNAvezporfeatures,calcula mean(utility_long) ymean(utility_short) delmismo20.
- GLOBALcalcula ambasmediasdetodoslosválidos; noelige20globalesniun lado conotrosvecinos.
- Mejor forecast Emax=max(meanlong,meanshort).
- Si Emax>.0019,comprar si meanlong>=meanshort (LONG enempate exacto) o vender si meanshort>meanlong. Si Emax<=.0019,cash. No short porque ambospayoffsseannegativos;no flippingsegúnPnL.
- Dosmediasno son probabilidadescalibradas; sinSE/shrink/optimización nueva. Per-nocional no equivale a maximizar utilidad de equity2%: cantidades fee-aware pueden diferir porlado y funding/ocupación/capital endógeno quedan fuera deltarget. Esa limitación se conserva, no se corrige despuésdePnL.

Hurdlenumérico.0019 fijo deR se mantiene sobreunidadfee-only: ahora exige19bps de payoffestimado DESPUÉSde feesbase modelados, no mero logpriceforecast19bps. Es decisiónmásrestrictiva porunidad/costos yse declara comopartedelargetnuevo; no es estrés aplicado. EnPNLreal fee se cobrauna vez. Labelrestarfee yledgerrealfee no es doblecargo sobrecapital: unoentrenamodelo yotroescontabilidadejecución. No deducir.0019delPNL.

Cada4huna oportunidadnueva,inclusoconmisma dirección;calcularyactualizarmuestras/cachéaunocupado. Descartareventosocupadossincola/samecloseexitentry/reverse. SinTP24h/stop2ATRsimple actual/entry_planR10feeaware2%unchanged/R12ARonopen+gestión6BAR/R11observer.

## Caché y costo computacional, sin madurez anticipada

Diseño propuesto:
1. EnT4h obtener380OHLCcerradas yM1runtime;buscar límites por timestamps sorted, nunca índicesrelativosguardados que cambienalcrecerbuffer.
2. Determinar EXACTOS360timestampsdeorigenesperados a partirde14..373.
3. Cachepor T_i. Almacenar sólo resultado maduro:validpairlabels+metadata(entry,distance,deadline,firsttouch/exit,reason) o inválidomaduro+reason. No cachear «maduro» antesde deadline, incluso contouch temprano.
4. Enprimercierre de ensayo puedeharse360×1440 comprobacionescausales yaobservadas, equivalentes~518400filas×2lados (sin crear trades). Implementar min/max/touchconNumPy yprimeríndiceTrue paraevitar overheadPython innecesario; no optimizar investigación ni escoger resultados.
5. Luego cada4h aparecehabitualmenteunorigenreciénmaduro ycaducauno:reuse359pares ycomputar1path de1440M1. Un avance congap/reinicio procesa sóloorígenesesperados no cacheados yya maduros. No saltearobservaciónporocupación.
6. Purgecache a timestampsactualesdelos360orígenes; no ampliartrainingwindow ni manteneri excluidospararescatarválidos. Cache no son360trades ni resultados deestrategia.
7. Inválidomaduro corresponde datos pasadosinmutables deesecache:si faltaM1no sehace backfill/importdetrás. Store reason y disponibilidad. Si seanticipacorreccióndedatosrun,tarea se detiene/es técnica nueva; no reutilizar cachépreviamenteinválida con datasource cambiado.
8. Sólo leeasof:bloqueextras futurosenbufferNOentra ni para declararvalidoprocesosporadelantado. Hasta deadline exacto, ningún labelvisible alestimador.

Memoria de cacheO360conmetadata compacta, no360copiasdelpath. M1bufferdelmotorpermanecepropiedaddelruntime; no modificarvariablesglobales,retención ni framework. Si no hayforma de recuperarelpath exactoylímiteasof conAPIexistente, SquedaBLOQUEADOTÉCNICO antesdeeconomía; no usarresearch_script/exportcandle/importfueraalcance.

Medición requerida:cachehits/misses/valid/invalidreason/futuredenied/maduras,totalfixedorigins360,commonvalidn,min/M1oldest,newlabelsper4h yretenciónvisible;emitirresúmenescompactos, no logporM1. Lasfronterasmensuales/DD siguenR11 sin alteración. Primer4h de startup no borra cashhistórico ni presupone labelsprospectivos.

## Contrato, gates y presupuesto

BTC-USDT BinancePerpetualFutures ruta1m,dataBTC4h,warmup4004h igualR,[2020-10-15,2026-01-01)UTC,10k,2%portrade/6%agregado/3xaislado,unaposición. R10sizingfee-aware90%margen/floor8,no reservaP ni haircutAngle,stop2ATR14SIMPLEactual,noTP,max24hprimer4hposterioralplazo de fill. MARKETBTC conocidas. Fee.00045/side,slip0,fundingBTChistóricoON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 aplicado/verificado/proxymarksdeclaradas. SóloBTCoperativo.

Gatesr9sinrelajar: CAGRnetobase>=30%,PF>=1.2,DD<=25%(obj20%),M65activospositivos,Q80completos,medianamensualcalendario>0 incluidosinactivos,netoaritmético quitandomejores2meses>0,N>=100preliminar sinconfianza/potencia porconteo. Aspiraciones40–50%+/M70no reemplazan puertas. NoETH/PAXG/SPYoperativa,no2026nuevo,noestrés,riskvariants,vecinos,direcciónflip,HMM/neural,installs/restarts/global,framework,imports,live/paper/Pi/scripts.

Presupuesto S:exactamente2económicas KNNutility/GLOBALutility, hasta2reemplazos sólo técnicosdocumentados,no porPnL. No rerunR exacto,no otrosneighbors/horizontes/deltas/costlabels/fundinglabels/cutstop/shrinkdespuésdeverPnL. Si S falla,cerrar presupuesto sinretocar y seguirotra pregunta material. No promover uncomponente aislado retrospectivamente ni la varianteque«menos pierde».

## Gates de revisión antes de implementar

Root fijó gate deorígenesfaltantes y revisa todavía viabilidad/caché/paridad brokerlabel. Después,y sólo si autorizado,clases nuevas sin editar R/Angle/padres;protocoloactualizadoyreadbackhash antescódigo. Checks temporalesprovidedsourceAST,sin velasobservadas/importrealstrategy/framework/backtestanidado: mapping380→372/360,ATRi14padding,first/lastM1/closedasof,1440contiguasobligatoriasaunambosstopstempranos,madurezdeadline,stopfirst/últimominuto/gapambossides,fees/pernocional/0fundinglabels,cachekeys/parityuncached/maturación/purge/duplicados,top20ties/valididadcomún/mediaslongshort/argmaxempatelong/hurdle,ocupación/nuevas4h/nosameexit,riskSLnoTP24h/FINAL. Los datos reales sólo a travésdelmotor autorizado;no inspecciónparaajustaresta receta.

Tras checks root revisaráfullsource/hash+recibos antesdedrafts/manifiestogenuino/economía;ninguna sesiónficticia. Auditoríasnapshotcompleto gross−fees+funding=PNLsum=equityfinal−10k1e-6USDT,2.741.760M1marks,63intervalos/62meses/20Q/terminalfee;diagnósticoslabelcoverage/cachéno reemplazanaccounting. Archivosprimero/Hubíndiceúltimo. Root autorizó implementar y checks supplied-source, sin economía/drafts. Los intentos de análisis sintéticos se cuentan aparte de los hasta2reemplazos técnicos de backtests económicos; fallos puramente de harness se documentan y corrigen sin confundir ambos presupuestos.

## CODES — fuentes completas leídas por MCP antes de implementación

Los siguientes textos exactos y sus hashes de arriba documentan antecedentes y dependencias. No crean clases nuevas ni modifican padres. No afirman completitud M1 ni ejecutan sus funciones en esta fase.

### AngleBtcProbability4h

```python
import math
from collections import deque
from datetime import datetime, timezone

import numpy as np
import jesse.indicators as ta
from jesse.strategies import Strategy

BAR_MS = 4 * 60 * 60 * 1000
MINUTE_MS = 60 * 1000
LEARNING_WINDOW = 1080  # 180 days of non-overlapping four-hour outcomes.
MIN_STATE_CASES = 80  # Avoid decisions supported by a handful of pattern matches.
PRIOR_CASES = 20.0  # Balanced zero-mean, unit-R-second-moment shrinkage prior.
BASE_FEE = 0.00045
FRICTION_BUFFER = 0.001  # Forecast haircut and sizing reserve, NOT simulated slippage.
TRADE_RISK = 0.01
NOTIONAL_CAP = 4.4
STOP_LEVERAGE_BUFFER = 0.75  # Keep25%inside ideal1/leverage; not exact liquidation math.


class AngleBtcProbability4h(Strategy):
    """Causal four-state monetary expectancy with explicit abstention.

    Two return signs define four states. No trend/reversal direction is assumed.
    Smoothed win probability is diagnostic; net payoff and uncertainty gate trades.
    This is a research hypothesis, not a claim of calibrated probabilities.
    """

    def _model(self):
        if 'probability_model' not in self.vars:
            self.vars['probability_model'] = {
                'observations': deque(),
                'count': np.zeros(4, dtype=np.int64),
                'sum': np.zeros((4, 2)),
                'sum_square': np.zeros((4, 2)),
                'wins': np.zeros((4, 2), dtype=np.int64),
                'pending': None,
                'last_processed': None,
                'labels_total': 0,
                'missing_labels': 0,
                'year': None,
                'skip_window': 0, 'skip_state_cases': 0, 'skip_edge': 0,
                'skip_stop_safety': 0, 'skip_qty': 0,
                'long_signals': 0, 'short_signals': 0,
            }
        return self.vars['probability_model']

    def _log_model_summary(self, label):
        m = self._model()
        self.log('ANGLE_PROBABILITY_SUMMARY ' + label + ' cumulative '
                 + str({k: (len(m['observations']) if k == 'window_length' else
                            m['count'].tolist() if k == 'state_counts' else m[k])
                        for k in ('labels_total', 'missing_labels', 'window_length',
                                  'state_counts', 'skip_window', 'skip_state_cases',
                                  'skip_edge', 'skip_stop_safety', 'skip_qty',
                                  'long_signals', 'short_signals')}))

    def _label(self, pending):
        # Only source minutes after the previous decision and already CLOSED now
        # can mature its label. No forward-fill or stale multi-hour substitute.
        if int(self.time) != pending['time'] + BAR_MS:
            return None
        minutes = self.get_candles(self.exchange, self.symbol, '1m')
        if len(minutes) < 240:
            return None
        minutes = minutes[-240:]
        expected = pending['time'] + np.arange(240, dtype=np.int64) * MINUTE_MS
        assert np.all(minutes[:, 0] < self.time), 'PROBABILITY_FUTURE_MINUTE'
        if not np.array_equal(minutes[:, 0].astype(np.int64), expected):
            return None
        if not np.isfinite(minutes[:, :5]).all() or np.any(minutes[:, 1:5] <= 0):
            return None
        entry = pending['entry']
        distance = pending['distance']
        outcomes = []
        for side in (1, -1):
            stop = entry - side * distance
            exit_price = float(minutes[-1, 2])
            for row in minutes:
                opening = float(row[1])
                # A protective STOP crossed by an opening gap fills at that
                # adverse minute opening; otherwise its first touched stop wins.
                if (side == 1 and opening <= stop) or (side == -1 and opening >= stop):
                    exit_price = opening
                    break
                if (side == 1 and row[4] <= stop) or (side == -1 and row[3] >= stop):
                    exit_price = stop
                    break
            # Signal costs remain fixed in later effective-fee stress. Every
            # virtual outcome bears both taker fees plus a conservative haircut.
            cash_per_unit = (side * (exit_price - entry)
                             - BASE_FEE * (entry + exit_price)
                             - FRICTION_BUFFER * entry)
            outcomes.append(cash_per_unit / distance)
        return np.asarray(outcomes)

    def _record(self, pending, outcomes):
        model = self._model()
        observations = model['observations']
        if len(observations) == LEARNING_WINDOW:
            state, old = observations.popleft()
            model['count'][state] -= 1
            model['sum'][state] -= old
            model['sum_square'][state] -= old * old
            model['wins'][state] -= (old > 0).astype(np.int64)
        state = pending['state']
        observations.append((state, outcomes.copy()))
        model['count'][state] += 1
        model['sum'][state] += outcomes
        model['sum_square'][state] += outcomes * outcomes
        model['wins'][state] += (outcomes > 0).astype(np.int64)
        model['labels_total'] += 1
        assert int(model['count'].sum()) == len(observations)
        assert np.all(model['count'] >= 0)

    def before(self):
        assert self.symbol == 'BTC-USDT' and self.timeframe == '4h'
        assert self.is_futures_trading
        model = self._model()
        if model['last_processed'] == int(self.time):
            return
        model['last_processed'] = int(self.time)
        year = datetime.fromtimestamp(self.time / 1000, timezone.utc).year
        if model['year'] is not None and year != model['year']:
            self._log_model_summary('through_year_' + str(model['year']))
        model['year'] = year
        pending = model['pending']
        if pending is not None:
            outcomes = self._label(pending)
            if outcomes is None:
                model['missing_labels'] += 1
                # Eight failed maturation attempts with zero valid labels is a
                # data/cadence failure, not evidence that the economic gate abstains.
                # Occasional gaps after valid observations remain permitted.
                if model['labels_total'] == 0 and model['missing_labels'] >= 8:
                    self._log_model_summary('invalid_m1_coverage')
                    raise AssertionError('ANGLE_NO_MATURED_LABELS: verify240closed_contiguous_M1_and_clock')
            else:
                self._record(pending, outcomes)
        c = self.candles
        model['pending'] = None
        if len(c) < 30:
            return
        # All three closes are known now. Equal closes join the non-positive
        # state; there is no extra flat-return threshold to fit.
        closes = c[-3:, 2]
        if not np.isfinite(closes).all() or np.any(closes <= 0):
            return
        state = 2 * int(closes[1] > closes[0]) + int(closes[2] > closes[1])
        atr = float(ta.atr(c))
        distance = 3 * atr  # Emergency stop, not an optimized entry filter.
        if not (math.isfinite(distance) and 0 < distance < float(self.price)):
            return
        # Ideal liquidation distance1/L ignores maintenance/fees. Staying25%
        # inside it avoids obviously unprotected labels, without promising an
        # exact exchange liquidation boundary. This is not an optimizable gate.
        if distance / float(self.price) > STOP_LEVERAGE_BUFFER / self.leverage:
            model['skip_stop_safety'] += 1
            return
        model['pending'] = {'state': state, 'entry': float(self.price),
                            'distance': distance, 'time': int(self.time)}

    def _decision(self):
        if self.vars.get('decision_time') == int(self.time):
            return self.vars['decision_side']
        self.vars['decision_time'] = int(self.time)
        self.vars['decision_side'] = 0
        model = self._model()
        current = model['pending']
        # Runtime startup is fully retained as cash in the backtest. Warm-up
        # candles supply ATR only; no future/pretrained outcome table is loaded.
        if current is None or len(model['observations']) < LEARNING_WINDOW:
            model['skip_window'] += 1
            return 0
        state = current['state']
        n = int(model['count'][state])
        if n < MIN_STATE_CASES:
            model['skip_state_cases'] += 1
            return 0
        total = n + PRIOR_CASES
        mean = model['sum'][state] / total
        variance = np.maximum((model['sum_square'][state] + PRIOR_CASES) / total
                              - mean * mean, 0.0)
        standard_error = np.sqrt(variance / total)
        # This one-SE lower score is a conservative decision heuristic, NOT a
        # confidence statement under independent observations or a p-value.
        lower = mean - standard_error
        direction = int(np.argmax(lower))
        if not np.isfinite(lower).all() or lower[direction] <= 0:
            model['skip_edge'] += 1
            return 0
        side = 1 if direction == 0 else -1
        entry = current['entry']
        distance = current['distance']
        if distance / entry > STOP_LEVERAGE_BUFFER / self.leverage:
            model['skip_stop_safety'] += 1
            return 0
        stop = entry - side * distance
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        # The single BTC route starts at1%, below the approved3%/8% ceilings.
        unit_risk = distance + self.fee_rate * (entry + stop) + FRICTION_BUFFER * entry
        qty = min(capital * TRADE_RISK / unit_risk,
                  capital * NOTIONAL_CAP / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        # Research precision only; native lot/min-notional must precede live use.
        qty = math.floor(qty / 0.001) * 0.001
        if qty <= 0:
            model['skip_qty'] += 1
            return 0
        assert qty * unit_risk <= capital * TRADE_RISK + 1e-8
        self.vars['plan'] = {
            'qty': qty, 'distance': distance, 'entry': entry, 'state': state,
            'state_cases': n, 'expected_net_r': float(mean[direction]),
            'one_se_lower_r': float(lower[direction]),
            'win_probability': float((model['wins'][state, direction] + PRIOR_CASES / 2) / total),
        }
        model['long_signals' if side == 1 else 'short_signals'] += 1
        self.vars['decision_side'] = side
        return side

    def should_long(self):
        return self._decision() == 1

    def should_short(self):
        return self._decision() == -1

    def go_long(self):
        p = self.vars['plan']
        self.buy = p['qty'], self.price

    def go_short(self):
        p = self.vars['plan']
        self.sell = p['qty'], self.price

    def should_cancel_entry(self):
        return True

    def on_open_position(self, order):
        p = self.vars['plan']
        self.vars['opened_time'] = int(self.time)
        entry = float(self.position.entry_price)
        distance = p['distance']
        assert distance / entry <= STOP_LEVERAGE_BUFFER / self.leverage + 1e-12, 'ANGLE_FILL_STOP_BEYOND_SAFETY'
        if self.is_long:
            self.stop_loss = abs(self.position.qty), entry - distance
        else:
            self.stop_loss = abs(self.position.qty), entry + distance

    def update_position(self):
        # If an emergency stop did not already close it intrabar, close at the
        # first next four-hour decision. Jesse does not reopen in that callback.
        if self.time - self.vars['opened_time'] >= BAR_MS:
            self.liquidate()

    def on_increased_position(self, order):
        raise AssertionError('PROBABILITY_PYRAMIDING_UNSUPPORTED')

    def on_reduced_position(self, order):
        raise AssertionError('PROBABILITY_PARTIAL_EXIT_UNSUPPORTED')

    def before_terminate(self):
        self._log_model_summary('final')
```

### BtcResearchR18AnalogueBase1m

```python
import math
import numpy as np
from strategies.BtcResearchR12ArBase1m import BtcResearchR12ArBase1m
from strategies.BtcResearchR10Base4h import BAR, closed_window, atr14, entry_plan


def analogue_sample(rows):
    """360 mature origins in a fixed372-bar window; no future labels or padding."""
    logs = np.log(rows[-372:, 2])
    assert len(logs) == 372
    returns = np.diff(logs)
    origins = np.arange(6, 366, dtype=int)
    # Return index j links close j to close j+1. Origin i therefore uses i-6:i.
    vectors = returns[origins[:, None]-6+np.arange(6)]
    labels = logs[origins+6]-logs[origins]
    norms = np.linalg.norm(vectors, axis=1)
    current = returns[-6:]
    current_norm = float(np.linalg.norm(current))
    if not np.all(np.isfinite(current)) or not math.isfinite(current_norm) or current_norm <= 0:
        return None
    valid = (np.all(np.isfinite(vectors), axis=1) & np.isfinite(norms)
             & (norms > 0) & np.isfinite(labels))
    origins, vectors, norms, labels = origins[valid], vectors[valid], norms[valid], labels[valid]
    if len(origins) < 20:
        return None
    return dict(origins=origins, vectors=vectors/norms[:, None],
                labels=labels, current=current/current_norm)


def analogue_forecast(rows, nearest):
    """Fixed top20 cosine mean versus all valid labels; exact ties prefer older."""
    sample = analogue_sample(rows)
    if sample is None:
        return None, None
    origins, labels = sample["origins"], sample["labels"]
    cosine = sample["vectors"] @ sample["current"]
    if not np.all(np.isfinite(cosine)):
        return None, None
    # Origins arrive oldest first; stable sorting preserves that order on ties.
    order = np.argsort(-cosine, kind="stable")
    chosen = order[:20] if nearest else np.arange(len(origins))
    forecast = float(np.mean(labels[chosen]))
    if not math.isfinite(forecast):
        return None, None
    evidence = dict(valid_origins=len(origins), selected=len(chosen),
                    first_origin=int(origins[0]), last_origin=int(origins[-1]),
                    chosen_origins=[int(x) for x in origins[chosen]] if nearest else None,
                    best_cosine=float(cosine[order[0]]),
                    twentieth_cosine=float(cosine[order[19]]),
                    forecast=forecast)
    return forecast, evidence


class BtcResearchR18AnalogueBase1m(BtcResearchR12ArBase1m):
    MODE = "abstract"

    def before(self):
        now = int(self.time)
        if not self.vars.get("checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            assert self.MODE in ("KNN", "GLOBAL")
            self.vars["checked"] = True
        self._observe("pre")
        self.vars["direction"] = 0
        if now % BAR:
            return
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 372)
        if rows is None:
            self.vars["invalid_windows"] = self.vars.get("invalid_windows", 0)+1
            return
        assert math.isclose(float(rows[-1, 2]), float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        forecast, evidence = analogue_forecast(rows, self.MODE == "KNN")
        # The inherited .0019 hurdle is a signal rule, never an extra PnL debit.
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
        self.vars["plan"] = dict(plan, analogue=dict(evidence))
        self.vars["direction"] = direction

    def on_open_position(self, order):
        # Parent supplies actual-fill stop, no TP, risk check and24h clock.
        super().on_open_position(order)
        direction = 1 if self.is_long else -1
        key = "long_fills" if direction == 1 else "short_fills"
        self.vars[key] = self.vars.get(key, 0)+1
        self._log("R18_ANALOGUE_OPEN", dict(time=int(self.time), mode=self.MODE,
            direction=direction, evidence=self.vars["plan"]["analogue"]))

    def _emit(self, stage):
        super()._emit(stage)
        self._log("R18_ANALOGUE_STATS", dict(stage=stage, mode=self.MODE,
            long_fills=self.vars.get("long_fills", 0),
            short_fills=self.vars.get("short_fills", 0),
            signals=self.vars.get("signals", 0), occupied=self.vars.get("occupied", 0)))
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

### BtcResearchR12ArBase1m

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

## Recibo técnico preeconómico

Fuenteeconómica guardada después de autorizaciónroot, revisiónroot/independienteconforme. Check1a13343c98ea41adbf0ee4bb6d97ab74 succeeded alprimerintento:1900aserciones,incluidooráculopara360orígenes que explica granpartedelconteo; no es confianzaestadística ni evidenciaeconómica. Ceroerrores/análisisrepetidos/backtests técnicos/económicos/drafts desdeeste subagente. Ochofuentes readbackcompletoidénticas, padres intactos. Labelmath/caché/asof/360orígenes/1440M1completos/gaps/fees-only/argmax/gestiónheredada probados conarrayssintéticos suministrados, no datosobservados. Completitud/retenciónM1real y diferenciasbroker/label siguenlimitaciones;expirylabel24hexacto desdeoriginT versus primer4h tras>=24hdesdeopened_atreal no se igualaron artificialmente.
