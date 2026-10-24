# BTC Discovery AA — protocolo de interacción volumen × retorno

Fecha2026-10-21. Estado: implementación y checks sintéticos completados; fuentes finales y recibos revisados por root e independiente. Root creó dos borradores para preflight; motores aún no iniciados antes del manifiesto. Se conserva la propuesta AA previa, sus objeciones y deduplicación; este protocolo fija las precisiones técnicas antes de código. No se consultaron resultados Y para formularlo.

Nombres reservados exactos, corregidos por root antes de código: BtcResearchR27VolumeInteractionBase1m, BtcResearchR27VolumeInteraction1m, BtcResearchR27MainEffects1m. Z/R26 es descarte de carry; AB/R28 permanece HOLD documental por datos. Las tres clases AA están implementadas; los estados documentales anteriores se conservan en CODES y recibos.

## 1. Pregunta, controles y motivación

Pregunta: ¿el volumen relativo de la barra BTC actual modifica la respuesta predictiva a SU retorno4h con signo y mejora la operativa24h, más allá de efectos principales de retorno y volumen? INTERACTION añade sólo el producto r·v al diseño MAIN_EFFECTS. Ambas políticas comparten target, universo, filas, normalización, máscara, admisión numérica, hurdle, ejecución, gestión, riesgo, costes y ventana.

La motivación de provisión de liquidez es una hipótesis: actividad extraordinaria podría reducir persistencia direccional. El signo negativo del coeficiente del producto sería compatible con menor pendiente condicional; no mide presión exógena, órdenes agresoras, inventarios, inversores informados, causalidad o sinergia probada. El volumen podría capturar noticias/volatilidad/horario y la interacción podría no aportar nada. El término y un estimador distinto sólo se justifican por esta pregunta y su control anidado; no por fallos previos.

Literatura y límites ya documentados una sola vez en BTC_DISCOVERY_AA_VOLUME_INTERACTION_PROPOSAL_20261021.md. Enlaces: [paper primario publicado1993](https://web.mit.edu/wangj/www/pap/CampbellGrossmanWang93.pdf), [ficha del autor](https://campbell.scholars.harvard.edu/publications/trading-volume-and-serial-correlation-stock-returns), [working paper NBER4193,1992](https://www.nber.org/papers/w4193), DOI10.3386/w4193 y publicaciónDOI10.2307/2118454. No se reproduce aquí cita/resumen ni paper completo. La referencia de promedio del estudio es hacia ATRÁS, no una tendencia estimada con datos futuros. AA es diseño propio, no réplica.

## 2. Adaptación deliberada a BTC24/7 y documentación leída

Se leyó por recurso MCP jesse://strategy completo, server jesse-local, incluyendo Trading Hours y Adapting traditional-market research to24/7execution, ANTES de implementar. Primer intento con nombre de server jesse_local devolvió unknownserver; se descubrió el nombre registrado y se leyó correctamente. Fue error semántico del identificador, no timeout ni permiso de workaround o reinicio.

BTC-USDT es el perpetuo nativo Binance, no token de acciones ni proxy bursátil. Mantener historia nativa continua y trading_hours=None; no imponer horario, weekday, festivos, cierres tempranos o coeficientes de acciones. Ruta1m y input4h UTC continuo. Los cierres4h se procesan sólo una vez y todas las gestiones reales siguen activas24/7. No existe calendario externo por acreditar para este instrumento.

El targetBTC24h y retorno explicativo4h son diferentes del estimando diario de la fuente. No convertir seis barras BTC en una supuesta réplica de serial correlation diaria de índice. Volumen de un venue no es turnover ni inventario de inversores. ATR/stop se calculan sobre BTC4h nativo. No se sobrescribe self.candles, reconstruyen sesiones o rellenan huecos.

Fuentes originales y cierres completos leídos se archivan en BTC_DISCOVERY_AA_CODES_20261021.md; padres R10/R11/R12AR se releen completos antes del protocolo y no se modifican. No se usa el resumen genérico de lifecycle para corregir el código auditado del framework; heredar la gestión congelada.

## 3. Datos, índices y característica propia de cada origen

Sólo OHLCV BTC4h existentes. No mirar series reales, get_existing_candles, prechecks, imports, descargas o datasets nuevos. Motor será autoridad sobre disponibilidad si se autoriza economía. Warmup4204h, fijo por408filas necesarias más12de margen; no es selección basada en soporte observado. Cobertura suficiente aún NO acreditada.

En cada nueva fronteraT4h, tomar exactamente408filas cerradas consecutivas y alineadas, índices0..407. Última aperturaT−BAR, BAR=14400000ms. Futuros y prefijos fuera de ventana no entran. OHLC finitos/positivos/coherentes, timestamps estrictamente a4h y asof; las408V finitas y estrictamente positivas. No excepciones por padding; todas las filas se validan.

C_i=cierre,V_i=volumen en columna5. Para cada origen i:
r_i=log(C_i)−log(C_(i−1)).
v_i=log(V_i)−mean(log(V_(i−42)),...,log(V_(i−1))).
z_i=r_i·v_i.

42volúmenes previos corresponden a una semana completa24/7 y contienen todos sus bloques horarios. Se fijó para comparar actividad actual con nivel reciente, no como evidencia de ciclo óptimo ni garantía de desestacionalización. El actual V_i queda FUERA de su propia media; cada origen reconstruye SU baseline con información anterior a él. No usar media/std del currentT para rehacer sorpresas históricas ni permitir futuros relativos al origen.

No log1p, epsilon, imputar, winsorizar, rankear por cuantiles, clip, ponderar, dividir por OI o interpretar v como turnover. Volumen cero/negativo/NaN no es actividad escasa: invalida común. r,v,z pueden valer exactamente0; eso es admisible en observaciones individuales. El producto z RAW se crea ANTES de cualquier centrado o escaladoOLS. Su aritmética no finita invalida común. Con intercepto y efectos principales r/v, usar un producto de r/v centrados y escalados puede generar el MISMO espacio de columnas por transformación afín, por lo que no se afirmará que necesariamente cambie las predicciones. Aquí se prescribe el producto RAW para una representación y conversión de g_RAW inequívocas; el check debe verificar features/conversión, no inventar diferencias predictivas entre parametrizaciones equivalentes.

Current=407. Exactamente360orígenes entrenados i=42..401 inclusive; target:
y_i=log(C_(i+6))−log(C_i).
Targets48..407, íntegramente conocidos enT. Etiqueta del current407 no se usa. No origen402..407 porque sus24h no maduraron. No descartar orígenes y llenar con casos más viejos ni ampliar408/360 después.

La continuidad OHLC completa valida todas las seis barras futuras ya observadas de cada target; no basta endpoints si hay un gap intermedio. Targetprecio BRUTO, no payoff con stop ni neto de fees/funding. Funding se aplica en ledger real, no en y. Labels se solapan, no360muestras independientes ni360trades.

## 4. Escalado compartido y OLS anidado

Sobre los MISMOS360casos, construir matriz RAW F con columnas ordenadas(r,v,z). Antes de std, para CADA una de estas tres columnas nointercept comprobar igualdad exacta de TODAS sus observaciones a la primera. Si es constante exacta, AMBAS cash: evita std positiva artificial por redondeo de la media. Sin tolerancia nearzero ni retirar z para que opere MAIN.

Calcular medias m_j y desviaciones poblacionales s_j(ddof0) de cada columnaRAW sobre360casos. Todos centros y escalas finitos; exigir cada s_j>0. Estandarizar X_j=(F_j−m_j)/s_j. No usar std/centros de otra ventana, sólo submuestras o punto407. Es parametrización numérica del ajuste hecho enT con datos entrenados, no parte de la sorpresa v_i conocida en su origen.

FULL=[1,X_r,X_v,X_z], MAIN=[1,X_r,X_v]. R y V usan EXACTAMENTE los mismos centros/escalas/columnas normalizadas en ambos diseños, derivados una sola vez; MAIN es literalmente la primera terna de FULL. No estandarizar de nuevo MAIN.

Ajustar separadamente np.linalg.lstsq(FULL,y,rcond=None) y np.linalg.lstsq(MAIN,y,rcond=None). rcond=None conserva umbral numérico por defecto de NumPy según dtype/tamaño; NO rcond elegido, regularización económica, penalización, hiperparámetro o alternativa tras resultados. Registrar versiónNumPy/runtime con recibo técnico/fuente.

Admisión compartida:
- Ambos diseños/labels/puntoactual transformado y resultados aritméticos finitos.
- RankFULL==4 y rankMAIN==3 devueltos por esos mismos ajustes; coeficientes y valores singulares finitos.
- Ambos forecast407 finitos.
- g_RAW=coefFULL_interaction_ESCALADO/s_z finito, por salud numérica de la evidencia común. No se usa magnitud/signo para admitir; un desborde numérico se declara inválido en ambos. No cambiar a coeficiente clippeado para emitirJSON.

El único error capturado como fallo numérico cash de solver será np.linalg.LinAlgError. No catchgeneral de excepciones de programación, buffers, tipos u órdenes. La invalidez comprobada explícitamente se registra y devuelve cash común; no falla silenciosamente hacia modelo menor. No pseudo-inversa de rango insuficiente, ridge/shrinkage, boundbeta, selección de variables, SEgate, threshold de condición, optimización o grid. Condición numérica/singular values pueden informarse, sin nuevos filtros.

CurrentRAW=(r407,v407,z407) se transforma con los mismos m/s y se evalúa en ambos modelos. ForecastFULL y forecastMAIN son predicciones DIRECTAS de retorno24h: no seis recursionesAR, sumas de forecasts4h ni media corregida por signo.

Los parámetros a,b,c son reestimados en ambos modelos anidados, no fijados a coeficientes del otro brazo. El contraste de cuentas no es una estimación causal aislada de g. No reutilizar G como controlidéntico: G usa240pares de retorno siguiente4h y seis recursiones sin volumen; estas reglas son diferentes.

## 5. Reloj, diagnóstico descriptivo y separación de órdenes

En cada callback1m mantener _observeR11 heredado. Para el modeloAA usar reloj monotónico4h: T<=last no-op matemático antes de validar ventana o contar nuevamente. Un gap de callbacks no genera oportunidades retroactivas ni etiquetas nuevas: el siguiente T sólo evalúa su ventana408cerrada y, si íntegra, ambosfits. Modelo stateless porventana, sinbootstrap/replay, banco de eventos o órdenes ficticias.

El MODE únicamente elige forecastDESPUÉS de computar y validar ambos fits. Todo ajuste/diagnóstico es idéntico por diseño en ambas políticas aunque sus posiciones, capital o fills diverjan. No afirmar igualdad observada de toda trayectoria sólo por contadores terminales concordantes.

Para CADA fit conjunto válido en START<T<FINISH, una vez porT, ANTES del hurdle, ocupación, ATR y sizing, mantener diagnóstico O(1):
- n_valid_fits.
- g_negative/g_zero/g_positive según g_RAW<0/==0/>0 exactos.
- medias online de g_RAW, forecastFULL y forecastMAIN.
- últimoT, g_RAW y ambosforecast.
- contador de errores numéricos de agregación diagnóstica y bandera de media no disponible si ocurre overflow.

Los tres signos suman n_valid_fits. El g de diagnóstico es RAW, no su coeficiente de columna estandarizada. Las medias se actualizan sin guardar arrays de toda historia. Si la agregación de una media desborda, marcar ESA media no disponible/contar incidente y seguir counts/órdenes de fits válidos; diagnóstico nunca filtra, recorta, selecciona o altera forecast. No inventar sumas finitas ni inflar soporte. NoSE, t-test, p-value, períodos favorables, relación con trades ganadores o filtro gnegativo.

gRAW negativo expresa menor pendiente condicional en ESTE modelo y universo de fits válidos. No identifica causa, no prueba mecanismo de liquidez, no asegura mayorretorno neto. gpositivo/noevidencia no permite cambiar narrativa, invertir dirección o correr otro brazo. Los contadores de fits son observaciones dependientes de desarrollo; no intervalos de confianza.

Evidencia por fill: T/forecastorigen,MODE, ambosforecasts, centros/escalas o huella+datos acotados,rank4/3,gRAW y coeficientes, entrada real/qty/distance/stop/deadline/riskbudget. Terminal: contadores invaliddata/constant/scales/rank/solver/arithmetic, fits y gsign/means; no historial ilimitado. JSON sólo finito o null explícito por diagnóstico no disponible, líneas acotadas para lecturaMCP. No añadir telemetría que cambie modelo.

## 6. Señal, gestión y cuenta intactas

Admisión señal común: forecast elegida>.0019 LONG; <−.0019 SHORT; igualdades/banda cash. Hurdle es de señal heredado, no coste debitado, stress o estimación de spread. Cero de r/v/z individual no genera descarte por sí solo.

Procesar matemática y diagnóstico aunque abierto, con entrypending o en timestamp de salida. Señal bloqueada se consume, noqueue/replay/reversa/pirámides. No entrada sameexit; START<T<FINISH estricto.

Herencia futura literal BtcResearchR12ArBase1m→R11→R10. Override de before paraAA; on_open_position puede llamar super y añadir evidencia; _emit puede llamar super y añadir diagnósticos. No cambiar padres, update_position/onclose/risk. Stop2ATR14SIMPLE ACTUALBTC4h, calculado con15OHLC/14TR causales; valor0/None impide plan DESPUÉS del fit/diagnóstico, no borra ambos. Fijar distance2ATR antes de orden; stop relativo al fill real mediante R12AR. SinTP,24hdesde opened_at, primera frontera4h edad>=6BAR; brokerproteccionesM1 activo24/7. No usar un target de esta etiqueta como precio de salida.

R10entry_plan literal: capitalmax(0,balance)flat, available_margin,3x,2%fee-aware con feesentry/stop,margen90%,floor8research. NoLOT/reserva legacy, minimumcapital inventado o límite1x. Una posiciónBTC, riesgoagregado6% no vinculante conuna. Gaps/funding/pérdidasreales pueden exceder budgetprevisto.

UTC[2020-10-15,2026-01-01), BTC-USDT BinancePerpetualFutures route1m y dataBTC4h,10k,isolated3x. Fee.00045porlado todos tipos/taker descuento, fundingBTC histórico ON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571, marcasproxydeclaradas, slippage0. Neto de estos costesmodelados, no todos los costes reales.

MediciónR11 wallet+PnLabierto cadaM1/fill, sin multiplicar nuevamente porleverage; fronterasUTCpostfunding/predecisiónporfase,63intervalos/62mesescompletos/20Q. Inactivos incluidos en mediana calendario. DD M1+eventos no todos los extremosintraminuto. Auditoría completa posterior, si autorizada, bruto−fees+funding=PNLsum=equityfinal−10000 a1e−6 y cortes/terminal/sumas reconciliados.

## 7. Antecedentes y cierres conservados

Matriz y detalles están en propuestaAA; CODES archiva fuentes/cierres completos, sin paper completo:
- V4ShockPV: reversión horaria predeterminada de shock>=2ATRprev yV>=2media24, stop1ATR/TP1R/6h, cerrada negativa. AA no cambia sus umbrales, stop o ventana para rescatar.
- X804/BTCExploreR804: presiónV×innovación monetaria en12velas, cambio entre mitades, confirmación y suplemento short heredado. AA no reabre ese setup; pregunta pendiente continua con control anidado.
- N501/N204ExploreR501: cohortes OHLCV presión positiva/negativa yprecioVWAP, filtro delsetup. No inventario observado ni control equivalentedeAA.
- I: impulso escasa participación y reparación confirmada con retorno deV porfase; soporteescaso yclosure conservados, no aflojarconfirmación.
- G: respuestaARconstante vsderiva, negativa yvecinoscerrados. AA no busca otra beta, regularización, horizonte, lado o régimen de aquelmotor; interacción de participación es cuestión adicional fijada antes de sus propios datos.
- Y: lags de asociación magnitud/volumen con S/D ytabla, no producto direccional contemporáneo/controladitivo. Sólo protocolo/fuenteleídos, no resultados paraAA.
- V1/V4/V5funding/OI ydescartecarryZ permanecen cerrados. Sin añadir esos inputs como filtrosAA.
- N/P/Angle/CROSS/F/W yotros cierres no se reabren por combinarse conAA.

No se encontró equivalenteeconómico en fuentesconsultadas; no afirma censoexhaustivo o novedaduniversal. Cambios cosméticos no bastan; root puede rechazar implementación si la comparación sigueambigua.

## 8. Gates, presupuesto futuro y abandono

Gatesvigentes por política:CAGR>=30%(aspiración40–50%+),PF>=1.2,DD<=25%(objetivo20),M65activos(aspiración70),Q80completos,medianacalendario>0incluyendoinactivos,netoaritméticosin2mejoresmeses>0,N>=100preliminar sinconfianzaporconteo. Ganar acontrol negativo no basta.

Para sostener aporte económico incremental INTERACTION además debe tener neto de libro mayor al MAIN_EFFECTS bajo contrato común y cumplir todas las puertas propias; comparación descriptiva, no significancia ni causalidad. El control se juzga también individualmente, sin que su fallo salve alFULL. Ni signo g ni una celda/año/lado reemplaza estaspuertas.

Presupuestofuturo: exactamente2económicas y hasta2reemplazostécnicos con lógica/datosidénticos por fallo técnico documentado, sólo tras autorizaciónroot independiente de este documento. Ningúnmotor autorizadoahora. Máximo2backtests/1analysisglobal coordinados porroot. Checks no son motores con datosobservados.

Si falla cerrar ambasrecetas; no vecinos de42/408/360/warmup,horizonte,hurdle,grado,normalización,rank/rcond,regularización,coeficientes,signos,lados,calendario,filtros,risk/gestión/costes. No seleccionar sólo gnegativa o discrepancias. No convertir la línea en búsqueda de polinomios. Sinestres hasta candidata/acuerdo; sin nuevaeconomía2026,imports,datasets,installs,framework/globalconfig,portfolio,live/paper/Pi.

## 9. Verificaciones futuras antes de economía

Revisión de protocolo porroot+independiente ANTES de nuevas fuentes. Sólo si luego autorizan implementación: leer fuente completa de padres/codes, crear3fuentes nuevas completas víaMCP, readbacks/hashes; no modificar padres.

Checks suministrados AST/stubs, sin imports de framework/estrategiasreales, velasobservadas o nestedbacktest. Oráculos matemáticos independientes de coeficientes/diseños:
- i42..401/targets48..407/current407 y baseline previo42, excluiractual/datosfuturos/prefijos, gaps/OHLCVinvalid.
- Cambiar futuro de un origen no cambia SU feature, pero puede cambiar labels que maduren posteriormente; no confundir causalidad de x con target.
- Fixture coeficientes conocidos, inclusión deintercept yprediccióndirecta24h, controlMAIN=primeras3columnasFULL, mismoscentros.
- RAWproductoantesescala y conversión gRAW exacta; controlar que usar producto de r/v estandarizados NO pase como misma representación prescrita.
- Constantesexactas antesstd,rank4/3común, volumen0, overflowaritmético y sóloLinAlgErrorcapturado; sin fallback.
- Límitehurdle, ceros individuales, espejo deprecio sintético cuando sea algebraicamente válido, unidadesvolumen sinprometer igualdadflotante universal.
- RelojT<=last/idempotencia, diagnósticoúnicoanteshurdle/ocupación/ATR/sizing, modo no afecta cálculo, gsignsum, mediaoverflow no cambia señales.
- Gestión24hreal, stop2ATR desde fill, sizingfee-aware2%, observer/terminal/noqueue/nosameexit ypadres byteidénticos.

Recibo completo/versiones/intentos decheck antes dedrafts; revisiónroot+independiente de fuentes/checks precede economía. Timeout/errorMCP=>halt yreportar, consultar mismoID alrecuperar sin duplicar niCLIworkaround. No afirmar pruebas o cobertura de mercado que todavía no existen.

## Autorización de implementación antes de fuentes

Root e independiente conformes con precisiones algebraicas/numeraciónR27. Se autoriza crear las tres fuentes y un check suministrado sin datosobservados, guardando versiones/harness/recibo antes de economía. No se autoriza todavía drafts o motores. Esta actualización de estado se guarda/relee antes de crear la primera clase.

## Cierre técnico previo a revisión económica

Tres fuentes creadas y readbacks exactos, padres intactos. Primercheck1d4b814efa56487299eec6c3ba1b4a98falló por predicadoAST delharness sobre substringResearch; repeatceec1738eb4748e5aa2f2eeae039d5a0succeeded129comprobaciones. Ambos fullcodes/jobs/resultados preservados enTECHNICAL_CHECK_RECEIPT; no sumar conteo incompleto ni equipararloamuestras. Cambio productivo previo a amboschecks sólo guardparidadprecio→cash común, con primera fuente preservada. No economía/drafts autorizados por este cierre.

NumPybaseline1.26.4 corroborada en artefacto técnico previo job7a53cb54457e4d478247cfae6dd4155b/y_technical_check.json. Root confirma entorno/container sinrestart/install/cambios desde esa medición; continuidad inferida explícita. AAchecknoemitióversiónindependiente, peroverificórcondNone/rangos. Sin tercerjobmetadata ni lectura de resultados económicosY.
