# Propuesta V3 — tendencia por ruptura de canal con protección ATR
Fecha: 2026-10-20. Estado: DISEÑO DEL SECTOR APROBADO POR ROOT; pendiente de congelación en el protocolo global V3. No autorizado aún implementar ni ejecutar.
Sector dedicado: tendencia de canal. No se creó código ni se ejecutaron backtests V3 al redactar. Antecedente observado: FINAL_DECISION_V2.md, leído por MCP.

## 1. Hipótesis y diferencia con V2
Una ruptura de un canal de varios días, alineada con un régimen de varias semanas y gestionada mediante stop de tendencia sin objetivo fijo, puede conservar movimientos persistentes durante más de un día. La participación creciente observada mediante OI24h podría filtrar algunas rupturas débiles; debe medirse por ablación P/POI.
Es una hipótesis nueva que cambia conjuntamente mecanismo de entrada y salida. No se presenta como estimación independiente ni como efecto aislado del trailing.
V2 cerró SIN_CANDIDATA: sus controles y nuevas variantes no superaron los gates de entrenamiento, aun cuando ATR+OI obtuvo cuatro semestres exploratorios positivos. Esa información motiva investigar otro mecanismo, pero no justifica relajar sus criterios ni copiar los semestres ganadores como evidencia nueva.

## 2. Universo, reloj y datos
BTC-USDT, Binance Perpetual Futures. Una ruta, long/short simétricos, sin ML, piramidar ni parciales. Ejecución completa1m, decisión4h UTC con datos cerrados. Contabilidad funding ON en ambas variantes; sin gate económico de funding.
Conservar datasets ya versionados:
- funding: 9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571;
- OI: 6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf.
Funding liquidado publicado +1m, marcas proxy explícitas. OI archivo retrospectivo label+6m, stale máximo10m desde disponibilidad, valores>0; sin rellenar huecos ni ceros. Estos supuestos siguen sin certificar point-in-time.
Sólo se propone explorar datos hasta fin exclusivo2024-01-01 al inicio. No consultar2024–2025 antes de shortlist/protocolo global, ni2026. Las ventanas2020–2023 ya fueron observadas en V1/V2.
Capital10.000USDT por sesión, isolated3x, cap notional C, fee nominal0,00045 por lado y slippage nominal a fijar por root en el protocolo global. Si se mantiene0bps para comparabilidad, declarar ese límite y estrés real posterior. No calibrar costos para rescatar la candidata.

## 3. Notación y ventanas causales exactas
T es la decisión. B_t es la última barra4h con open_time+4h=T; usar sólo barras terminadas<=T. Requerir timestamps consecutivos y OHLC finito, positivo y coherente en cada ventana exigida.
c_t es su cierre.
Canal de entrada:
H20_t=max(high_(t-20),...,high_(t-1));
L20_t=min(low_(t-20),...,low_(t-1)).
La barra de señal B_t queda excluida del canal. Se requieren21 barras completas para canal+señal.
Régimen lento aprobado:
M120_t=(c_(t-119)+...+c_t)/120.
Es SMA120, incluye el cierre conocido de señal y no tiene semilla recursiva. Se usa además M120_(t−6), media de los120 cierres c_(t−125)...c_(t−6). Pendiente24h positiva si M120_t>M120_(t−6), negativa si M120_t<M120_(t−6); igualdad no habilita entrada. Ambas ventanas exigen126 barras4h cerradas consecutivas en total. Root eligió esta convención antes de cualquier resultado V3; no intercambiar por EMA o añadir un mínimo de pendiente después.
Volatilidad:
A_t es SMA14 de true ranges de las últimas14 barras completas:
TR_i=max(high_i−low_i,abs(high_i−c_(i-1)),abs(low_i−c_(i-1))).
Requiere15 barras, mismo cálculo inequívoco de V2. No Wilder, no extrapolación, no clamps porcentuales.
Warmup240 barras4h sin operar, suficiente para126 cierres exigidos por régimen y pendiente, además de canal/ATR; no ofrece observaciones OI previas ficticias. La validez se determina por timestamps, no sólo por cantidad de filas.

## 4. Entradas
P_LONG: c_t>H20_t, c_t>M120_t y M120_t>M120_(t−6).
P_SHORT: c_t<L20_t, c_t<M120_t y M120_t<M120_(t−6).
Igualdad en cualquier umbral no habilita ese lado. La pendiente aprobada es sólo comparación24h de la misma media; no agregar umbral porcentual de pendiente, ADX, volumen, banda ni otro filtro posterior.
Convención aprobada: condición por estado, sin exigir cruce adicional del canal anterior; el canal ya excluye B_t y comprueba un cierre fuera de extremos anteriores. No introducir un cruce distinto tras observar resultados.
Sólo plano/sin entrada pendiente; máximo una entrada efectiva por día UTC; start<T<finish. No reentrar en la misma decisión en que se cerró una posición: contexto de entrada calculado antes de gestión permanece deshabilitado si estaba abierta.
Entrada MARKET al precio de decisión con slippage real del motor cuando se configure. Registrar decisión y fill.

## 5. Ablación OI
IDs propuestos: V3_TREND_CHANNEL_P y V3_TREND_CHANNEL_POI.
POI exige OI disponible en T mayor que el valor efectivamente observado en la decisión T−24h; ambos válidos y >0. P no exige disponibilidad OI. Regla idéntica para long/short.
OI es confirmación de participación, no predicción del signo. Primeras seis decisiones4h inicializan referencia dentro de cada sesión; no backfill desde warmup.
Separar ausencia, stale, cero actual, inicialización, referencia inválida y gate no creciente. No afirmar que diferencia operativa P/POI sea exclusivamente señal económica si no se igualaron máscaras.

## 6. Sizing y protección inicial
s=+1 long/−1 short; p=precio decisión; C=available_margin previo a entrada; f=fee configurada; d_pre=2A_t.
stop_pre=p−s*d_pre. Rechazar entrada si p,C,A_t,d_pre o stop_pre no son finitos/positivos. Sin objetivo fijo.
u=d_pre+f*(p+stop_pre).
qty=floor8(min(C/p,0,02C/u)).
El riesgo presupuestado2% incluye pérdida al stop y fees de entrada/salida, no funding, gaps o slippage adicionales. No multiplicar tamaño por leverage. El cap de notional puede dejar riesgo menor2%; reportarlo.
Con fill e, stop_inicial=e−s*2A_entry, con A_entry congelada en decisión. Validar de nuevo positividad; si falla, solicitar MARKET inmediato, registrar invalid_after_fill y conservar el trade.
No take-profit. El STOP inicial queda activo intraminuto mientras se actualiza el trailing en decisiones4h.

## 7. Trailing de tendencia con orden temporal explícito
Al entrar, HWM=e y LWM=e. No incorporar high/low de la barra de señal: ocurrieron antes del fill y contaminarían la trayectoria posterior.
En cada cierre4h posterior a la entrada, incorporar solamente barras completas cuyo open_time>=timestamp de entrada:
HWM_T=max(e, highs de esas barras completas);
LWM_T=min(e, lows de esas barras completas).
El primer trailing se actualiza tras la primera barra completa posterior a la entrada. Nunca se calcula con un high/low parcial ni con una barra anterior al fill.
A_T es la volatilidad causal de la decisión actual; esta elección permite adaptación reciente, pero el stop no puede aflojar:
- Long: candidato=HWM_T−3A_T; stop_nuevo=max(stop_anterior,candidato).
- Short: candidato=LWM_T+3A_T; stop_nuevo=min(stop_anterior,candidato).
Si faltan datos válidos para el nuevo A_T/high-water mark, conservar el STOP vigente y registrar trailing_data_invalid; nunca suspender gestión ni resetear extremos.
El STOP anterior estuvo activo durante la barra que acaba de terminar y pudo ejecutarse allí. Si la posición sigue abierta, el nuevo stop sólo tiene vigencia hacia adelante desde T: no simular un fill retrospectivo en el extremo de esa barra.
Si el nuevo umbral ya está atravesado al precio actual (long stop_nuevo>=precio_T; short stop_nuevo<=precio_T), solicitar salida MARKET ahora, causa trailing_cross_on_update. No colocar un STOP incorrecto al otro lado del mercado ni cobrar artificialmente el precio del umbral.
Si el umbral todavía es protector, reemplazar STOP por qty completa. Cancelación/sustitución debe seguir el motor Jesse, sin añadir un segundo stop que duplique reduce_only.
La salida de tendencia aprobada es este trailing. No añadir salida por SMA o canal de reversión.

## 8. Duración y bordes
Máximo7d=168h=42 barras4h desde el timestamp real de apertura. Salir MARKET en la primera decisión con edad>=168h aunque ATR/OI/régimen falten.
En una decisión con límite de duración cumplido, holding_7d tiene prioridad sobre actualización de trailing. Si el STOP previo ya ejecutó antes de T, esa salida protectora sigue siendo la real.
Cierre forzado al borde final del fold, plano al iniciar cada sesión, costos incluidos; no mantener posiciones cuyos resultados atraviesen train/evaluación. Máximo holding mayor no autoriza consultar el futuro para cerrar la última posición de train.
No salida adicional por invertir el régimen ni reversión inmediata long↔short. No TP fijo ni take-profit de emergencia.
Registrar motivos: initial_stop/trailing_stop (con versión de stop ejecutada), holding_7d, trailing_cross_on_update, fold_end e invalid_after_fill. Distinguir orden ejecutada de solicitud de gestión.

## 9. Razón de las escalas, sin selección por métricas
- Canal20×4h=80h: ruptura de extremos de aproximadamente3,3 días; distinto del día UTC previo de H1 y no requiere calendario de sesiones bursátiles.
- Media120×4h=480h=20 días: contexto de varias semanas, unas6 veces la longitud del canal. La comparación de la media contra seis barras antes mide orientación24h dentro de ese contexto, sin umbral de pendiente calibrado.
- ATR14×4h=56h: escala local de rango de unos2,3 días; mide ruido reciente antes de la ruptura.
- Stop2ATR: protección inicial en unidades de volatilidad ya conocida; trailing3ATR es más ancho que esa protección al inicio y deja margen a continuidad. La regla max/min evita aflojar el riesgo aun cuando crezca ATR.
- Hold7d: límite semanal de exposición y financiación para que el mecanismo no quede indefinidamente abierto; se mantiene tiempo para persistencia multidiaria.
Estas razones mecánicas no acreditan edge ni óptimos. No estimar ventanas o múltiplos usando semestres V2; vecindad pequeña posterior deberá congelarse globalmente antes de resultados V3.

## 10. Pruebas de implementación que deberán preceder economía
- Ejemplo manual donde B_t marca nuevo extremo y sólo hay señal si el canal excluye esa barra; comprobar ambos lados y empates.
- SMA120 actual y desplazada6barras exactas, con126barras requeridas en conjunto, sin dependencia de filas más antiguas; probar ambos signos y empate de pendiente, sin media119/121 ni semilla implícita.
- ATR14 exacta con gap y rechazo de OHLC inválido/huecos, prefijos y mutación futura para todas las transformaciones.
- No incluir high de barra de señal al inicializar HWM; actualización sólo tras una barra completa postentrada.
- Ratchet long/short nunca se afloja ante aumento de ATR; high-water mark no se reinicia ni usa máximo global prefold.
- Nuevo stop atravesado provoca MARKET al precio actual con fricción; jamás fill histórico en candidato.
- STOP antiguo conserva prioridad intrabar; update a cierre no puede rescatar o empeorar retroactivamente una salida ya ejecutada.
- Mantener STOP y salida168h si faltan ATR/OI; contador de trailing_data_invalid separado.
- Sizing2%+fees y capC para ambos lados, fill adverso y precio protector inválido, salidas reduce_only completas.
- Conciliar ledger funding, fees, PNL y wallet por trade. Hold7d eleva número de pagos y riesgo de pérdidas adicionales por financiación.
- Cierre forzado real al borde, separando contadores before_terminate y cierre posterior como en V2.
Probar ramas técnicas deterministas, no escoger una ventana económica que gane. Congelar fuentes completas/hashes/config y timestamps antes de nuevos resultados.

## 11. Presupuesto y coordinación del protocolo global pendiente
Root prevé screening continuo [2020-09-01,2024-01-01) de seis configuraciones globales. Este sector aporta exactamente dos: CHANNEL_P y CHANNEL_POI. No reutiliza sesiones V2 porque entradas, filtro y salidas son distintas.
No se implementa aquí una selección E1–E4 heredada automáticamente de V2. Root fijará antes del primer resultado nuevo los gates de screening, ranking entre sectores, máximo de finalistas, presupuesto total y matriz de robustez. Sólo elegibles habilitarán confirmación walk-forward2024–2025; los datos de screening serán desarrollo observado.
La screening continua empieza plana con10.000 y termina con cierre forzado; puede transportar capital/posición dentro de2020–2023 según reglas. Eso no implica transportar capital entre posteriores folds de confirmación si root elige reinicios.
Como gestor exclusivo del sector, ejecutaré hasta dos runs simultáneos sólo si protocolo global y servicio lo permiten. Tras timeouts V2 es preferible uno por sector inicialmente y máximo dos globales. Cada evaluación de confirmación exige selección previa guardada por root.
No escribir REGISTRY global desde la rama; progreso exclusivo y auditorías propias, root integra, auditor independiente concilia snapshots.
Sin elegibles no abrir confirmación por obligación. No2026, sin cuentas/Pi/live/paper/instalaciones/reinicios ni otros chats.

## 12. Decisiones de root incorporadas antes de resultados
- SMA120 actual y comparación contra SMA120 seis barras antes; no EMA.
- Canal20 excluyendo barra de señal; entrada por estado, filtro de nivel más pendiente24h simétrico y máximo1entrada/día UTC.
- Stop inicial2ATR14, trailing3ATR14 como única salida de tendencia, sin TP o salida SMA adicional; hold máximo7d.
- HWM/LWM sólo con highs/lows de barras completas posteriores al fill; ratchet nunca afloja y umbral recién atravesado provoca MARKET ahora, sin retrofill.
Estas decisiones preceden código y nuevos resultados. La propuesta queda FINALIZADA PARA CONGELACIÓN GLOBAL. Aún no crear estrategias ni ejecutar sesiones hasta GO del protocolo global.
