# V6 — NR7: contracción relativa de rango y expansión al cierre, 4h

Autor: /root/v6_nr7, subagente dedicado al sector NR7. Fecha: 2026-10-21 UTC.
Estado: propuesta previa a implementación y resultados V6. Sólo diseño. No se crearon estrategias, helpers ejecutables, drafts, jobs ni backtests. Root consolidará protocolo, presupuesto y GO. La autorización del usuario para continuar V5 y V6 no abre 2026 ni trading.

## Hipótesis y parentesco con lo ya observado

Una barra de cuatro horas cuyo rango high–low es el menor estricto entre siete barras consecutivas puede representar contracción local. Si la siguiente barra termina fuera del rango de esa barra estrecha, se investiga continuación en el sentido del cierre, con protección y objetivo conocidos sólo desde la entrada. Es una hipótesis de expansión posterior a contracción, no una afirmación de ventaja demostrada ni de distribución futura de volatilidad.

Revisión documental por MCP: RESEARCH_PROTOCOL_V1.md, FINAL_DECISION_V2.md, RESEARCH_PROTOCOL_V3_20261020.md, V3_TREND_CHANNEL_PROPOSAL.md, V3_RANGE_REVERSION_PROPOSAL.md, V4_VOLUME_SHOCK_1H_PROPOSAL.md, RESEARCH_PROTOCOL_V4_20261020.md y las propuestas V5 CROSS, VWAP y FUNDING_TREND. Una búsqueda inicial de V3_CHANNEL_BREAKOUT_PROPOSAL.md no existía; se obtuvo el nombre correcto del protocolo V3 y se leyó la propuesta correcta. No se usó esa ausencia como evidencia de que no había una estrategia previa.

El diferencial es mecánico y queda fijado antes de resultados:

- V1 H1/V2 comparaban el cierre con extremos del día UTC anterior. Aquí no hay ancla diaria ni seis barras del día; se compara la barra previa con sus seis predecesoras y sólo su rango define el nivel de ruptura.
- V3 CHANNEL exigía cierre fuera de máximos/mínimos de veinte barras, nivel y pendiente de SMA120, luego trailing y máximo de siete días. NR7 requiere contracción relativa de una única barra previa, no extremo de canal de veinte barras ni régimen de media. Usa stop y TP fijos, sin trailing.
- V3 RANGE y V4 OSCILLATOR, SHOCK y FUNDING_RESET investigaban reversión o normalización. NR7 continúa en el sentido de la expansión cerrada; no entra contra un shock ni requiere un volumen extraordinario.
- V5 CROSS cambia de dirección por cruce de medias, VWAP busca reingreso hacia un centro ponderado y FUNDING_TREND exige carry persistente favorable. NR7 no usa medias, centro de valor o signo de funding para señalar.

Comparte la familia amplia de ruptura con CHANNEL y H1, y todos usan el mismo BTC y años ya vistos. El cambio de mecanismo no crea independencia estadística. No se presenta como efecto aislado de un único filtro sobre trades idénticos ni como auditoría exhaustiva de todas las estrategias legacy del workspace.

Los tres regímenes anuales 2021, 2022 y 2023 y la reserva interna 2024–2025 ya fueron observados en investigaciones anteriores. Prerregistrar reduce discreción posterior, pero no vuelve esos datos vírgenes. No se consultaron precios, tasas, OI ni resultados nuevos para elegir NR7 o sus múltiplos.

## Universo y reloj

BTC-USDT, Binance Perpetual Futures. Una ruta 4h UTC con ejecución histórica completa de 1 minuto; mercado 24/7, long/short simétricos, una posición neta por sesión. Sin pirámides, parciales, escalado, break-even o órdenes de entrada retenidas.

BAR = 14.400.000 ms; DAY = 86.400.000 ms. T es la decisión al cierre. B0 abre en T−BAR y termina en T. B−k es la barra k períodos anterior; O_k, C_k, H_k y L_k son sus OHLC.

Sólo filas con apertura+BAR<=T. Última apertura exactamente T−BAR, alineación UTC y consecutividad por BAR. OHLC finitos y positivos, H>=max(O,C), L<=min(O,C), H>=L. Cualquier hueco, duplicado, desalineación o dato inválido en la ventana requerida invalida esa función; no rellenar ni comprimir ventanas.

Warmup 240 barras 4h sin operar. Son 40 días y cubren las ventanas nominales y vecinas. OI no se reconstruye desde warmup.

## Contracción NR7 y entrada nominal exacta

R_k = H_k−L_k, rango high–low de B−k. Es rango de esa barra, no true range: un gap entre barras no entra en R_k. Las diferencias y comparaciones deben permanecer finitas.

La barra B−1 es NR7 sólo si:

R_1 < min(R_2, R_3, R_4, R_5, R_6, R_7).

Son siete barras previas, terminadas como máximo en T−BAR. B0 no participa en la elección de la barra estrecha. Empatar el mínimo no califica; no seleccionar discrecionalmente la más reciente entre empates.

No se añade un gate R_1/ATR, un porcentaje de rango mínimo o un filtro de color. Una barra con H_1=L_1 y OHLC coherente puede ser el mínimo estricto si las otras seis tienen rango positivo; se admite conforme a esta definición. Siete barras de rango cero empatadas no califican. ATR de entrada, separadamente, debe ser positivo. No excluir esos casos después de conocer sus resultados.

Si B−1 es NR7:

- Long si C_0>H_1.
- Short si C_0<L_1.
- En otro caso dirección cero.

Las comparaciones de ruptura son estrictas; C_0=H_1 o C_0=L_1 no entra. No se requiere un cruce adicional: C_1 está dentro del rango válido de B−1, y el cierre actual fuera ya implica el desplazamiento de cierre en esa dirección. No agregar confirmación de una barra futura, pendiente, media, ADX, volumen, tasa o día de semana.

La señal nominal exige ocho OHLC consecutivas B−7…B0. Vecino NR6 exige siete; NR8 exige nueve. ATR exige quince y domina la ventana total para habilitar una entrada.

La oportunidad pertenece únicamente a la barra que sigue inmediatamente a la contracción. Si se bloquea por posición, cuota, calidad, OI o calendario, se pierde; no conservar el nivel de B−1 para otra barra ni reintentar sin un nuevo setup. En la siguiente decisión se evaluará su propia barra previa y su propia ventana, sin latch.

### La barra actual alcanza ambos lados

B0 puede tener H_0>H_1 y L_0<L_1. Eso no produce dos órdenes ni ambigüedad de la señal: sólo su cierre decide dirección, y H_1>=L_1 impide que C_0 sea a la vez mayor que H_1 y menor que L_1.

Si el cierre vuelve dentro del rango previo, no hay entrada aunque ambos lados se hayan negociado intrabar. Si termina por encima, la señal es long; si termina por debajo, short. No inferir cuál extremo ocurrió primero ni atribuir una entrada histórica en el nivel previo. Toda la trayectoria de B0 ocurrió antes del fill de T.

## Ejecución, riesgo, stop y TP

Entrada MARKET al precio disponible en T, sólo estando plano, sin entrada pendiente y con cuota UTC libre. start<T<finish y a<T<b para cada intervalo activo, sin fusionar intervalos. No entrada en la misma decisión que cerró una posición previa.

ATR14 simple actual A_0:

TR_j=max(H_j−L_j, abs(H_j−C_(j+1)), abs(L_j−C_(j+1))), j=0…13;
A_0=media aritmética de esos catorce TR.

Son quince OHLC B−14…B0. Incluye B0 y sus gaps respecto al cierre previo. No ATR Wilder, semilla recursiva ni ATR previo que excluya la expansión. Exigir A_0>0 y finita; finitud tras aritmética, sin epsilon o clamps.

Distancia nominal d=2A_0, congelada al decidir entrada. Con C=available_margin previo, p=precio de decisión, s=+1 long/−1 short y f=fee del escenario:

stop_pre=p−s*d;
u=d+f*(p+stop_pre);
q=floor8(min(C/p, 0,02*C/u)).

C, p, d, stop_pre, u y q deben ser finitos/positivos; f finita>=0. Floor8 redondea cantidad hacia abajo a ocho decimales. Cap nocional 1x al precio del plan, isolated3x sin multiplicar tamaño por leverage. Si el cap limita el riesgo a menos del 2%, se acepta ese tamaño; no alterar el objetivo para gastar presupuesto.

Tras fill real e:

- Stop = e−s*d.
- TP = e+s*3d = e+s*6A_0.

Son protección STOP y objetivo LIMIT por la cantidad completa. RR nominal 3 antes de comisiones, funding, slippage y gaps; no denominarlo ratio neto garantizado. Niveles desde fill, no desde H_1/L_1 ni precio teórico de ruptura. No afirmar TP o stop ejecutados dentro de B0, que precedió a la entrada.

No trailing ni actualizaciones de stop/TP por rangos o ATR posteriores. Si protección u objetivo quedan inválidos después de un fill adverso, solicitar cierre MARKET de seguridad, registrar el trade y consumir cuota; no reparar silenciosamente el nivel ni borrar la operación.

Máximo 24 barras×4h=96 horas=4 días desde opened_at. Solicitar MARKET en el primer cierre con edad>=96h; el reloj es tiempo absoluto, no número de llamadas válidas. La falta de indicadores u OI no suspende protección, máximo holding o calendario.

Prioridades: protección intrabar ya instalada según motor; en decisión, frontera de calendario y luego máximo holding. No hay otra salida indicadora o invalidación adicional por volver al rango NR7. Al cierre final/fold se liquida con costes. Una sola solicitud de salida por decisión.

Una entrada ejecutada por día UTC, compartida entre long/short, incluidas entradas cerradas por seguridad. Rechazos no consumen cuota ni quedan pendientes. Un nuevo día puede permitir otra entrada sólo con una nueva contracción/ruptura válida, nunca por recordar un setup previo.

## Configuraciones nominales y ablación OI

Exactamente dos configuraciones nuevas:

- NR7_P: patrón de precio NR7, protección y salidas anteriores; sin gate económico OI o funding.
- NR7_POI: las mismas reglas, más gate OI creciente 24h.

POI exige OI actual observado causalmente en T>OI observado exactamente en la decisión T−24h; ambos valores positivos, disponibles y frescos. El gate es idéntico para long/short y mide participación, no el signo de posiciones.

En 4h son seis barras de referencia. Guardar un slot en cada decisión, incluidos ausentes, ceros y stale. Primeras seis decisiones inicializan; primera referencia posible en la séptima. Buffer nominal ocho registros con holgura. Sin backfill desde warmup, interpolación o usar otro timestamp para sustituir una referencia faltante.

Disponibilidad asumida label+6min y freshness diez minutos desde available_at. Archivo retrospectivo sin certificación point-in-time. NR7_P no exige calidad OI para entrar; no puede quedar bloqueada por una feature desactivada.

Retraso robusto adicional de cuatro horas de reloj = una barra 4h: en T entregar current originalmente observado en T−4h y referencia T−28h, conservando la calidad en sus relojes originales. Buffer nueve; primeras siete decisiones inicializan. No prolongar la frescura de una observación retrasada.

Replays mantienen historia en intervalos inactivos; los WF independientes la reinician por definición. No sumarlos como una cuenta continua.

## Costes, datos y presupuesto que consolidará root

Nominal: capital 10.000 USDT, fee 0,00045 por lado, slippage cero, funding histórico contable ON también en P, isolated3x/cap nocional 1x. Configuración de cada draft, sin tocar ajustes globales.

Funding dataset:
9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571

OI dataset:
6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf

Tasa final publicada, nunca tasa próxima estimada; cashflow=−signed_qty*mark*rate_decimal sin otro multiplicador de leverage. Una entrada T no paga retrospectivamente el evento procesado antes de esa decisión. Mantener effective_at normalizado y settled_at raw con jitter documentado. Marcas exactas/proxy/sin clasificar separadas.

Bruto−fees+funding=PNL y saldo final con tolerancia 1e−6 USDT. Funding, gaps y slippage pueden exceder el riesgo previsto del 2% stop+fees o el cap basado en decisión; medirlo sin restablecer cantidades nominales retrospectivamente.

El máximo de cuatro días limita duración, pero no predice cuatro días de tendencia ni financiación favorable. El stop basado en ATR actual puede ampliarse después de la expansión, reduciendo tamaño; es parte de esta regla, no un error para cambiar a ATR previo si la economía falla.

Root fija el presupuesto V6 antes de motores. Este sector aporta dos nominales, no grilla ni optimización. No abrir confirmación por obligación si no hay elegibles. V5 y V6 pueden tener protocolos propios, con todas las decisiones y fuentes congeladas antes de consultar su siguiente etapa.

## Vecinos prerregistrables, sin elegir ganador

Nominal: N=7, stop2A, TP3R, hold24 barras y ATR14.

| Vecino | Cambio exacto | Conserva |
|---|---|---|
| R09 | Stop1,8A; TP=3×1,8A=5,4A | N7, ATR14, hold24 y gates |
| R11 | Stop2,2A; TP=3×2,2A=6,6A | N7, ATR14, hold24 y gates |
| A09 | Contracción NR6 | Stop2A, TP6A, ATR14 y hold24 |
| A11 | Contracción NR8 | Stop2A, TP6A, ATR14 y hold24 |

El vecino discreto de señal redondea 7×0,9=6,3 a 6 y 7×1,1=7,7 a 8. No son variaciones exactas del 10%: representan −14,2857% y +14,2857% en el número entero de barras. Se declara ese límite antes de resultados; no se sustituye por N5/N9 ni se escoge el que apruebe.

Para N variable, B−1 debe tener rango menor estricto que B−2…B−N; sólo cambia esa ventana. La barra siguiente y ruptura por cierre quedan iguales. No mezclar cambios de riesgo y señal en una grilla. Los cuatro vecinos exigidos deben mantener neto>0 y DD<=25 si la nominal llega a esa fase; no reemplazan una nominal rechazada.

Fricción común V4 propuesta: S1 fee0,0009/slip0; S2 fee0,00045/slip5bps; S3 fee0,0009/slip10bps, motor real y calendario fijo. S1/S3 net>0 y DD<=25; S2 se reporta sin nuevo gate. Para P, lag OI es equivalente nominal y se reutiliza. Sensibilidades proxy/global funding×0,5/1,5 son contables con cantidades fijas, no replay ni candidata.

## Selección y criterios sin relajar

Screening propuesto común [2020-09-01,2024-01-01), continuo desde 10.000:

- N>=30 operaciones, neto>0, PF neto>=1,2 y |DD del motor|<=25%.
- Al menos dos de los tres años completos 2021, 2022 y 2023 positivos por equity. Separar 2020 parcial.
- Ranking común: menor |DD|, mayor PF, menor turnover, menos features OI y después ID estable.

Root fija shortlist antes de nueva economía V6 de 2024–2025. Cuatro semestres de confirmación con train expansivo, selección previa a evaluación y calendario individual de elegibilidad separado del selector global.

Replay propuesto [2024-01-01,2026-01-01), 731 días y capital continuo, con cuatro intervalos semestrales separados y cierre en cada frontera. No restablecer capital/OI para esconder un período adverso.

Promoción histórica: neto>0, PF>=1,2, DD<=25%, N>=100, al menos tres de cuatro semestres positivos y CAGR>=15%, además de fricción/vecinos/lag requeridos. CAGR=(saldo_final/10000)^(365/731)−1; no anualizar sólo exposición ni promediar PF. Meta orientativa 20–30% anual, sin promesa.

Rango estrecho puede no aportar suficientes trades. Un N insuficiente es un fallo del criterio, no permiso para ampliar la ventana histórica, aceptar empates o forzar nuevas entradas. Sin elegibles, cerrar la fase conforme al protocolo y conservar resultados negativos.

## Pruebas deterministas previstas antes de economía

No ejecutadas en esta propuesta:

1. Oráculo manual de siete rangos; B−1 estrictamente menor, empate con una o varias barras, mínimo en otro índice, rangos cero y OHLC coherentes. Verificar N6/N7/N8 y ventanas 7/8/9.
2. Rupturas long/short, igualdad en H_1/L_1, cierre dentro, barra actual que alcanza ambos lados y dirección exclusiva por cierre. Reflejar OHLC positivos invierte la señal.
3. Excluir B0 del ranking NR7 y rechazar usar B−8 nominal. Mutar cualquier prefijo anterior a la ventana o añadir/mutar futuro no cambia señal. Huecos/duplicados/no alineación/NaN/Inf y overflow rechazan sin contaminar JSON.
4. ATR simple de catorce TR sobre quince OHLC, incluye B0 y gaps. Mismo rango NR7 con ATR distinta cambia riesgo pero no la selección de contracción. ATR<=0 invalida la entrada, no el holding/calendario.
5. No latch: un bloqueo no conserva nivel; sólo barra inmediatamente siguiente. Cuota UTC, no reentrada en decisión de cierre y ausencia de órdenes pendientes retenidas.
6. Sizing fees/cap/floor8, stop2A y TP3R desde fill real para ambos lados; fill adverso no cambia d; invalid_after_fill cierra y conserva trade/cupo. Nada de TP alcanzado antes del fill.
7. Stop/TP fijo durante la posición; prioridad intrabar y calendario, holding96h exacto, deduplicación de salida. Tiempo absoluto aunque falten datos.
8. OI24h=seis barras, lag4h=una, calidad original, ceros/stale/missing y slots no comprimidos; P no exige OI.
9. Logs <=1900 caracteres, JSON finito y procedencia: N, siete rangos o sus ventanas con hash, B−1 high/low/rango, C0, narrow flag, dirección/causa, ATR/fill/stop/TP/qty/capital/fees, timestamps OI/funding y motivo de cierre real.
10. Particiones mensuales por all/long/short/none, barras, setup, cupo, calidad/OI, entradas/cierres y cierre forzado posterior al resumen. Contabilidad desde snapshots completos, PF de trades únicos, equity por calendario, gross/fees/funding, exposición/turnover, concentración y efecto descriptivo de retirar mejor semestre.

Un smoke técnico sin trades no demuestra fills, stop/TP o hold reales. Los checks puros sólo acreditan las ramas comprobadas. Registrar limitaciones y fallos técnicos; no retocar la regla económica a partir de PnL del smoke.

## Riesgos y límites

Contracción relativa no garantiza compresión absoluta: los siete rangos pueden ser grandes. NR7 puede marcar ruido y whipsaws, mientras un gap crea cierre fuera sin liquidez al nivel previo. El objetivo3R puede quedar demasiado lejos para cuatro días; no acercarlo después para mejorar win rate. ATR de expansión puede dar stop amplio y exposición baja; costes y carry pueden consumir la ventaja. El gate OI creciente puede confirmar una ruptura fallida, no su calidad.

Las reglas fijas y los datos compartidos limitan la inferencia. No usar un resultado favorable para afirmar que NR7 funciona en general o que seis configuraciones de V6 son seis pruebas independientes. La propuesta no autoriza 2026, ML, RST, live/paper, órdenes reales, Pi, cuentas, instalaciones, reinicios, commits o push.

La entrega termina en este documento. Esperar GO de root para cualquier implementación o ejecución.
