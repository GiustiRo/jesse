# V4 — propuesta oscilador RSI2 de pullback en tendencia, 1h
Fecha:2026-10-20. Estado: DISEÑO EXACTO PREVIO A IMPLEMENTACIÓN Y RESULTADOS V4. Único entregable de este sector; no hay fuentes ejecutables, drafts, motores o jobs V4. Root prerregistrará reglas comunes, presupuesto y fuentes del ciclo completo antes de cualquier resultado económico.

## Restricciones y procedencia
Releído completo mediante MCP RESEARCH_WALK_FORWARD_HANDOFF_20261020.md y RESEARCH_PROTOCOL_V3_20261020.md; consultados jesse://strategy, jesse://funding y plan previo de contabilidad/replay. La lectura documental vigente DOCS.md fue comunicada por root, quien la releyó del checkout: «Timeframes: A explorar/definir.»; «Prioridad: rentabilidad, no frecuencia.»; «Riesgo elegido: 2% por trade. Meta aceptada: 20–30% anual (Negociable).». No afirmo haber releído directamente DOCS por MCP: el lector de proyecto sólo expone strategies/ y research_scripts/.
El handoff dice «señales iniciales4h», «Mantener4h al inicio» y que cambios de timeframe consumen presupuesto de configuración; no establece prohibición permanente1h. El recurso funding documenta ejecución1m independiente del horizonte1h/4h. V3 estaba fijado4h: V4 declara explícitamente cambio de horizonte, hipótesis nueva y dos configuraciones nominales contadas; no modifica ni rescata V3.
BTC-USDT, Binance Perpetual Futures, continuo24/7 sin filtro horario/semanal; isolated3x de investigación, capnotional1x al dimensionar. El live5x de DOCS no aplica. Sólo MCP para investigación; no CLI/DB/env/research_scripts, instalaciones, reinicios, cuentas, Pi, live/paper ni commits.2026 sigue cerrado; excepción anteriorK1001 no se extiende aquí. Fecha final máxima2026-01-01 exclusiva.

## Hipótesis y diferencia económica
Una tendencia persistente puede sufrir una secuencia corta adversa que empuje un oscilador rápido a extremo. Se compra esa desaceleración transitoria dentro de un régimen alcista lento, y se vende su espejo bajista; la salida busca normalización del impulso, no una ruptura posterior.
No requiere toque SMA20, una vela que contenga una media, recuperar esa media ni romper el extremo de la vela previa. No usa canal, bandas ni umbral de funding. V3 PULLBACK esperaba reanudación de precio tras tocar SMA20 en4h; esta hipótesis toma el extremo de dos cambios suavizados en1h y sale cuando el oscilador vuelve al centro. Elegir1h cambia mecanismo temporal, no sólo el número de períodos de V3.
Motivación sin superioridad asumida: capturar reversión de impulso rápido condicionada por tendencia lenta; puede sufrir continuación adversa, whipsaws y costes altos. Mayor número de decisiones no garantiza más trades elegibles ni mejora de rentabilidad. N100 permanece filtro de evidencia, no objetivo que debamos fabricar. Los resultados V3 ya vistos motivan un ciclo nuevo, no estiman estos parámetros.

## Convención temporal y validación de datos
B0 es última vela1h cerrada al instante de decisiónT, con aperturaT−1h; B−k termina k horas antes. Sólo usar filas con apertura+3600000<=T, última exactamenteT−1h y aperturas consecutivas de1h. Ck/Hk/Lk/O k denotan cierre/máximo/mínimo/apertura deB−k.
Para habilitar entradas exigir224 velas1h cerradas consecutivas válidas: todo OHLC finito y positivo, low<=min(open,close)<=max(open,close)<=high. No reparar faltantes ni usar vela en formación. Warmup propuesto240velas1h sin operar, distinto en duración a240velas4h; suficiente para lookback224. OI no se rellena desde warmup.
Si falta dato de una señal se bloquea nueva exposición; stop previo y salida por holding/borde continúan. Un dato inválido no se convierte en neutral para habilitar entrada.

## RSI2 exacto: Wilder finito con semilla declarada
Definir R(k) independientemente sobre los32 cierres consecutivos terminados enB−k, del más viejo al más nuevo x0,…,x31. Para j=1,…,31:
g_j=max(x_j−x_(j−1),0), l_j=max(x_(j−1)−x_j,0).
Semilla G2=(g1+g2)/2; L2=(l1+l2)/2. Para j=3,…,31, en ese orden:
G_j=(G_(j−1)+g_j)/2; L_j=(L_(j−1)+l_j)/2.
Son29 recurrencias posteriores a la semilla. Si G31+L31>0: R(k)=100*G31/(G31+L31). Si ambos son exactamente0: R(k)=50. Si sólo pérdidas0 y ganancias>0:100; si sólo ganancias0 y pérdidas>0:0, ya contenidos por la fórmula. No epsilon, relleno, NaN->50, ni redondeo antes de comparar; valores intermedios deben ser finitos y no negativos.
Este es RSI de período2 con suavizado Wilder sobre historia FINITA32, no un RSI global de historia ilimitada ni una llamada de biblioteca con semilla implícita. Cada R(0) y R(1) usa su propia ventana32 y semilla propia; R(1) es exactamente el RSI que corresponde a la decisión anterior sobre su ventana, no el penúltimo estado de la ventana recién desplazada R(0). Para ambos bastan33cierres, contenidos en224.
La ventana32 acota procedencia y hace exacta la independencia de todo prefijo anterior a ella; peso de la semilla tras29actualizaciones es2^−29 por componente. Esto no autoriza a sustituirlo por RSI recursivo persistente: diferencias pequeñas cerca del umbral pueden cambiar un cruce.32 es una decisión técnica previa, no un parámetro que se probará por rentabilidad. No probar 16/64 u otras semillas para rescatar resultados.

## Régimen lento y ATR
M(k)=media aritmética de200 cierres desdeB−(k+199) hastaB−k, inclusive. Longtrend: C0>M(0) y M(0)>M(24). Shorttrend: C0<M(0) y M(0)<M(24). Igualdad no habilita dirección. M(24) requiere224cierres;24barras aquí son24horas. No filtro adicional de intensidad, ADX, color, volumen o distancia a media.
SMA200 representa nivel lento de unas8,33jornadas criptográficas; comparar con24h atrás exige deriva alineada durante un ciclo diario sin cambiar de timeframe ni introducir EMA/semilla. No se elige por un backtest.
A=media aritmética de14 true ranges de las últimas14velas, usando15OHLC cerradas: TR_j=max(H_j−L_j,abs(H_j−C_(j+1)),abs(L_j−C_(j+1))) para j=0,…,13. A finito>0. No ATR Wilder. Se conserva el cálculo explícito de riesgo previo;2A es distancia inicial, no otro filtro de alfa.

## Entradas exactas y dos ablaciones
Precio P:
- Long si longtrend y R(1)>10 y R(0)<=10.
- Short si shorttrend y R(1)<90 y R(0)>=90.
Son cruces frescos hacia extremo; no entrada repetida por permanecer extremo ni espera de rebote.10/90 son umbrales simétricos de agotamiento fuerte fijados antes de cualquier resultado, sin grilla. No fuerza50/50 en trades.
Además estar plano, sin orden pendiente, C disponible finito>0, cuota UTC libre y start<T<finish dentro del intervalo activo. Regímenes opuestos no pueden cumplir simultáneamente. Una señal bloqueada no se guarda para entrar horas más tarde sin cruce nuevo.
Dos únicas configuraciones de este sector:
1. OSCILLATOR_1H_P: precio anterior; no requiere validez de OI para entrar.
2. OSCILLATOR_1H_POI: mismas reglas +OI observado disponible enT mayor al observado en decisiónT−24h, ambos positivos y con calidad válida.
No añade gate funding, períodos alternativos, sólolong o variantes por salida. POI no infiere dirección de OI; valida aumento de participación.

OI histórico: dataset6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf; label+6min asumido, available_at pasado y edad<=10min desde disponibilidad. Guardar valor, label, available_at y reloj de observación. No cero, interpolación ni backfill. Referencia es observación causal guardada exactamente24decisiones1h antes, no el último valor encontrado para una fecha retrospectiva.
Con decisiones inicialesTstart+1h y sin warmupOI, primeras24decisiones tienen inicialización explícita; primera referencia posible en decisión25, Tstart+25h. Replays continuos conservan historia por todos los semestres, incluso inactivos; sesiones WF reinician explícitamente. En datos reales no certificadoPIT; huecos/ceros actuales o referencia inválida bloquean sólo variante dependiente y nunca desactivan gestión.

## Riesgo, ejecución y salidas
Una entrada MARKET en el precio de decisiónp (fill reale con slippage del escenario); no órdenes limit de entrada, pirámides, aumentos ni reversión instantánea. Una entrada ejecutada por díaUTC compartida long/short; consumir cuota por opened_at aunque cierre de inmediato. Sin entrada nueva en la misma decisión que liquidó una posición. Nunca reiniciar cuota o capital para elevar N.
s=+1long/−1short, d=2A, stop_pre=p−s*d; positivo. C=available_margin inmediatamente antes de entrar;f=fee del escenario.
q=floor8(min(C/p,0.02*C/[d+f*(p+stop_pre)])); floor8 redondea hacia abajo a8decimales. q>0, cantidades válidas; C/p es capnotional1x al precio de dimensionamiento, sin multiplicar por3leverage. Fee estresada participa en sizing. Registrar notional real al fill y exceso de presupuesto por ejecución sin ocultarlo.
Stop inicial fijo=e−s*d, A congelada en decisión; validar finito y positivo. Si una anomalía invalida la protección trasfill, liquidarMARKET inmediato con motivo y costos, sin borrartrade. Sin trailing, takeprofit en precio ni target3R.
En cada cierre1h posterior a entrada:
- long solicita cierreMARKET si R(0)>=50;
- short solicita cierreMARKET si R(0)<=50.
Es condición de estado de normalización, no exigir un cruce50 que pudiera perderse por dato inválido. Sólo se evalúa con32cierres válidos; la vela que produjo entrada no se reutiliza para salida posterior. No cierre adicional por perdertrend, SMA, color ni funding.
Holding máximo24horas desdeopened_at: cerrarMARKET en primer cierre1h con T−opened_at>=86400000, aunque RSI esté inválido. Cierre forzado de fold/calendario prioritario; después holding, después RSI. Protecciones antiguas ejecutadas intrabar por motor preceden decisiones de cierre1h; no fabricar fill retrospectivo.
Funding/slippage/gaps son adicionales a presupuesto stop+fees2%; pueden superar pérdida2% y deben reportarse. Stop2A limita riesgo estructural, salidaRSI50 busca normalización rápida y hold24h limita exposición si el extremo persiste; ningún múltiplo fue calibrado por resultados V4.

## Contabilidad, ventanas y criterios sin relajaciones
Funding contableON también enP, dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571. Fee nominal0.00045, slip0; config/datasets locales por sesión, balance10000 y full replay1m, funding efectivo impide fast real. Funding decimal: cashflow=−signedqty*mark*rate, sin multiplicar otra vez leverage. Contabilidad bruto−fees+funding=PNL y saldo terminal conciliados; sourceproxy identificado.
Fills[T−1min,T)→funding efectivoT→decisiónMARKETT. EntryT no paga ese evento, salidaMARKETT puede pagarlo. Usar effective_at y preservar settled_at con jitter documentado. No aplicar funding>=finish ni usar una vela con apertura2026; decisión/cierreTfinish puede apoyarse en última vela histórica terminada allí.
Root fijará desarrollo, confirmación, calendario y presupuesto V4 antes de implementaciones económicas. Propuesta hereda gates fijos de referencia y NO los disminuye: train>=30trades/net>0/PF>=1.2/|DD|<=25%, más gate anual de screening si protocoloV4lo mantiene; confirmación replay>=100trades únicos, net>0/PF>=1.2/|DD|<=25%,>=3/4semestres positivos y CAGR>=15% sobre731d si misma ventana2024–25. Selección train guardada antes deeval, replay con capital transportado y calendarios individuales separados delselector. Años previamente vistos nunca recuperan virginidad.
V3 P95/OI84 fallaronN100: no combinar trades de ambos ni añadirlos aV4. La nueva1h no garantizaN100; si falla se rechaza o declara insuficiencia sin bajar gate. No tocar umbral/cap/cuota/salida para aumentar muestra tras verlo.
S1fee0.0009/slip0;S2fee0.00045/slip5bps;S3fee0.0009/slip10bps, calendario fijo si root los prerregistra paraV4. Vecinos/lag/budget corresponden alprotocolo central, no ramas alternativas que este sector pueda elegir. Un lag adicional1barra de este horizonte sería1h, no4h; nunca modificar esa definición silenciosamente. Sensibilidades fundingproxy/global0.5/1.5 son cashflows con cantidades/fills fijos, no replays ni resultados para elegir parámetro.

## Pruebas técnicas y evidencia exigibles antes de economía
No ejecutadas en esta propuesta. A implementar sólo conGO posterior:
- Oráculo algebraico RSI2: ventanas32/33, exactamente2deltas de semilla y29actualizaciones, seriesflat/monótonas/alternadas, casosganancia0/pérdida0, límites10/90/50 e igualdad, overflow/NaN. Comparar R(1) con cálculo sobre prefijo que termina una hora antes.
- Invariancia exacta ante agregar o mutar prefijos anteriores a los32cierres de cada R(k); no confundir con independencia de los224cierres deltrend. Mutar cualquier barra más vieja que224 no cambia ninguna señal. Mutar dentro de224 pero fuera de33puede cambiartrend y se espera.
- Prefijos/mutaciónfutura no cambian señales; timestamps1h y OHLCinválido/consecutividad/lookbacks224/15 correctos; el agregado1h debe terminar antes o enT.
- Long/short espejos, frescura del cruce y no reentrada en estado extremo; datoRSIinválido no desactiva stop/hold; salidaRSI50 posterior alfill, holding24h, cuotaUTC y ausencia de dobleentrada en mismoT.
- POI24h=24barras1h; primera24decisiones inicialización, nada desdewarmup, missing/stale/zero/reference por separado. Mantenerhistoria en calendarioinactivo.
- Sizingstop+fees,cap1x,rounddown8 y stressfee; protecciónancladafill y cobrosfunding/bordes. Detallar eventos sin atribucióncausalcuando faltalogs.
- Procedencia acotada: parámetros/versión, hashes de ventanas, R0/R1, semillasG/L y rango de timestamps, SMA200actual/24hatrás, ATR, OI,capital/qty/fees/stop/razónsalida. Logs JSON acotados por línea y contadores por mes/dirección separando no_setup/trend_reject/RSIinválido/cuota/pendiente/calendario/OIcausas/entradas/salidas.
Reportar después meses/años/semestres por equity,PFtradesúnicos,long/short,gross/fees/funding,turnover,exposición,holding,concentración y causas. No sumartrainenagregados ni PNLcerrados para retorno semestral.

Riesgos principales: tendencia estimada puede retrasarse y RSIextremo ser inicio de aceleración adversa; stopintrabar puede cortar antes de normalización; turnover y fundingpueden eliminar edge; cuota1/día puede censurar señales útiles; finite-seed/umbral tiene discontinuidades definidas y no se ajustará por beneficio; archivoOIretrospectivo puede revisar historia. Esta propuesta define una hipótesis falsable, no evidencia de ventaja o autorización operativa.
