# Tanda I: vacío de participación y reparación del impulso

## Pregunta y presupuesto previo
¿Un desplazamiento fuerte con poco volumen, seguido por recuperación cuando regresa la participación, identifica una reversión BTC mejor que el patrón de precios solo? Esta es la porción creativa: se combina secuencia de precio y participación normalizada por hora, sin afirmar flujo real o liquidez observada. Dos políticas y exactamente dos corridas económicas; hasta dos reemplazos por fallos técnicos documentados, nunca por PnL. Máximo dos motores y un análisis propio. Sin vecinos ni optimización posterior.

## Antecedentes exactos
V4Shock: desplazamiento horario grande y ALTO volumen, reversión inmediata. BtcExploreR101: alto volumen>=2mediana30, rechazo y confirmación por encima del máximo de S, macro/operativa basal. RangeFade5m: flush con alto volumen y macro/gestión parcial. CAbsorption: alto volumen con cuerpo pequeño y escape posterior. AngleCombinedBtcVolume4h usa mediana28 días del mismo bloqueUTC como admisión del BTC basal. Aquí se contrasta el ORDEN baja participación durante desplazamiento y normalización durante recuperación, sin macro/RSI/canal ni receta basal. Los antecedentes fueron leídos; no se encontró equivalente económico de esta secuencia en fuentes revisadas. No demostrar novedad universal ni independencia estadística.

## Reglas congeladas
S=penúltima4h, B=última4h, P=cierre anterior aS. A=ATR14simple conocido antes deS. Impulso D=C_S−P, exigir abs(D)>=A. B debe devolver al menos50% del impulso y permanecer estrictamente antes de su reparación completa: f=(C_B−C_S)/(P−C_S), .5<=f<1. Dirección contraria aD, MARKET tras cierreB. No se interpreta secuencia intrabar desde OHLC.

PRICE: sólo ese patrón, con validez común de datos. PHASE: además V_S<=.5*mediana28delbloqueUTCdeS y V_B>=mediana28delbloqueUTCdeB. Ambas medianas se calculan con28 días anteriores de su propio bloque4h y están enteramente disponibles ANTES deS. Unir ventanas exige170OHLC4h; S está en posición168 yB169; referenciasS índices0,6,...162 yB1,7,...163. No usar S o B en sus propios baselines. Esto evita llamar anomalía a diferencias normales entre horarios.

Precios/candles cerrados consecutivos yvolúmenes170 finitos estrictamente positivos en ambas políticas. Una ausencia o volumen0 no se imputa y no se selecciona como vacío. Cada parejaS/B es evento independiente de estado, consumido aunocupado; no cola, no reentrada al salir en mismo cierre. Ventanas se solapan y no son muestras independientes.

Protección común: stop2A congelado, TP2R, vencimiento48h en cierres4h. TP puede superar la reparación del impulso: se prueba la hipótesis de persistencia posterior a la recuperación inicial, no una orden al precio previo. Una posición sinpirámides. SizingR10feeaware2%, margen90%,floor8. Gaps/funding pueden exceder riesgo esperado.

## Contrato y puertas
BTC-USDT Binance Perpetual Futures, ruta1m observador ydatos4h,warmup2404h;[2020-10-15,2026-01-01)UTC desarrollo ampliamente reutilizado. Capital10k,2%/6%/3xaislado,fee.00045porlado, funding históricoON aplicado/verificado snapshot9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 con marcasproxy declaradas;slippage0. Sin estrés,variantesriesgo,nuevaeconomía2026,ML/HMM,live/paper/Pi/configglobal.

MediciónR11 wallet+PnLabierto porM1 yfill; fronteras00:00UTCpostfunding/predecisión, convenciónporfase; DD M1+eventos no todoslos extremosintraminuto. Mesescalendario inactivos incluidos en mediana. Gatesr9:CAGR>=30%,PF>=1.2,DD<=25%(objetivo20%),M65activos,Q80completos,medianacalendario>0,netoquitando2mejoresmeses>0,N>=100preliminar sinconfianzaporelconteo. Aspiraciones40–50%+/M70. Ganar alcontrol no basta;cada política porseparado. Si falla economía NO_CUMPLE; si economía favorable pero poca muestra INCONCLUSA. Si noparticipación, informar sin fingir rechazo de toda familia. Estrés sólo tras candidata y acuerdo.

## Verificación y cierre
ChecksAST, señales espejo, f=.5/f<1, exclusión deS/B de baselines porUTC,volumen0/NaN inválidos, ATRpreS sincontaminación,asof/gaps/futuro,sizing/protección y revisión independiente antes de economía. Fuentes/readback/hash/config enmanifiesto previo. Auditoría completa posterior: bruto−fees+funding=PNLsum=equityfinal−10k a1e−6,2.741.760marcasM1/63intervalos/62meses/20Q ytelescopíamensual. ReportesMCP yHubíndiceúltimo. Si falla, cerrar receta y vecinos locales; seguir con otra pregunta material dentro del objetivo autónomo, no bajar puertas ni ampliar presupuesto para aprobar.
