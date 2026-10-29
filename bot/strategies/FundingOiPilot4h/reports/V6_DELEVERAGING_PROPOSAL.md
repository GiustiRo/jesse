# V6 — recuperación después de reducción de OI en 4h

Estado: propuesta previa a implementación y economía. Dueño dedicado: /root/v6_deleverage. Entregable de diseño, sin estrategias, drafts, jobs ni backtests. Root consolidará el protocolo, el presupuesto y el GO. Sólo MCP Jesse local; BTC-USDT Binance Perpetual Futures. No se abre 2026, ML, live/paper, cuentas, Pi, CLI o reinicios.

## Hipótesis y parentesco

Después de un desplazamiento de precio de 24 horas grande frente a la volatilidad actual, una reducción simultánea de OI podría indicar que parte de la exposición se está cerrando. La primera corrección de precio puede ofrecer recuperación parcial durante las siguientes 48 horas. Es una hipótesis de reversión con un proxy de reducción de posiciones, no una identificación de liquidaciones forzadas: OI también cae por cierres voluntarios y no identifica por sí mismo qué lado cerró.

Documentos revisados por MCP: RESEARCH_PROTOCOL_V1.md, V3_RANGE_REVERSION_PROPOSAL.md y V4_VOLUME_SHOCK_1H_PROPOSAL.md, además del contexto de cierres V1–V4. H1 V1 continuaba rupturas del día UTC anterior; H2 revertía el reingreso a ese rango; H3 seguía precio24h y precio de última barra en la misma dirección, con normalización de funding en sus variantes F. Su gate OI era creciente para ambos lados. V3 RANGE pedía excursión nueva contra una media20 bajo baja deriva; su propuesta prohibía invertir OI dentro de ese ciclo. V4 SHOCK revertía una vela1h de desplazamiento y volumen anormales, sin esperar corrección. Esta V6 combina desplazamiento24h de signo contrario a la última corrección4h y caída de OI24h; no usa rango UTC, media/zscore, volumen de shock ni funding predictivo.

Cambiar risingOI por caídaOI habría sido un cambio económico prohibido dentro de las versiones anteriores. Aquí se registra explícitamente como hipótesis nueva solicitada por el usuario en V6, con nueva ablación P/POI y sin reutilizar una sesión anterior como si implementase la nueva regla. No se ha consultado economía nueva para elegir umbrales. No se afirma revisión exhaustiva de toda estrategia legacy del workspace ni independencia respecto a datos o familias de reversión ya observadas.

## Reloj y calidad

BAR=14.400.000 ms, DAY=86.400.000 ms. T es una decisión4h UTC. B0 es la vela cerrada que abrió en T−BAR; B−k es k barras anterior. Sólo se aceptan filas cuya apertura+BAR<=T, con última apertura exactamente T−BAR, timestamps alineados y consecutivos. No se usa una vela abierta en T.

C0, C1 y C6 son cierres de B0, B−1 y B−6. C6 terminó exactamente24h antes que C0; no son seis horas. Para precio hacen falta siete cierres; la entrada completa requiere quince OHLC por el ATR. Las quince barras deben ser finitas, positivas y coherentes: L<=min(O,C)<=max(O,C)<=H. Duplicados, gaps, NaN/Inf o incoherencia invalidan sin sustituir filas por otras más antiguas. Filas futuras no intervienen aunque sean inválidas.

A es ATR14 simple actual: media aritmética de catorce true ranges sobre las quince OHLC cerradas terminadas en B0. TR=max(H−L,abs(H−Cprev),abs(L−Cprev)). No es Wilder/EMA; incluye la barra de corrección B0 y no tiene semilla recursiva. Exigir A>0 y finito. Toda resta, producto, cociente y resultado de señal debe ser finito. El warmup común de240 velas4h es suficiente; no se opera durante warmup.

## Única señal nominal de precio

Definir D=C0−C6, M=2,0 y corrección Q=C0−C1.

- Long si D<=−M*A y Q>0.
- Short si D>=+M*A y Q<0.
- En otro caso, ninguna dirección.

La igualdad del desplazamiento cuenta; la corrección exige movimiento estricto. Con A>0 y M>0, las dos ramas son excluyentes. Si C0=C1 no se entra. La corrección no necesita recuperar un porcentaje del desplazamiento, tocar una media ni cruzar el cierre anterior de24h. No se añaden esas condiciones después de conocer resultados.

No se exige cruce fresco del umbral M entre dos decisiones. Es un estado evaluado en cada cierre4h: puede seguir habilitado después de una salida si vuelve a haber corrección y cumple la cuota temporal. No hay latch de un evento bloqueado ni ejecución diferida de una señal antigua; cada decisión recalcula C0/C1/C6/A con su ventana actual.

La dirección contraria al desplazamiento24h diferencia esta regla del régimen H3 de continuidad. La corrección cerrada distingue la entrada de una venta/compra inmediata al superar el umbral. Ambas diferencias son reglas económicas prerregistradas, no evidencia de una ventaja.

## OI decreciente, sólo en POI

Se utiliza cantidad base de OI del accessor público, con su procedencia confirmada antes de implementar. No usar value_quote: una caída del precio podría reducir notional sin reducir posiciones. Nunca interpretar OI como flujo direccional observado.

OI0 es la lectura disponible en la decisión T y OI24 la lectura efectivamente guardada en T−DAY. Ambas deben ser finitas y estrictamente positivas, con status válido y timestamps de procedencia. El archivo retrospectivo conserva el supuesto de disponibilidad label+360.000 ms; exigir available_at=label+360.000, available_at<=tiempo de su decisión y edad desde available_at<=600.000 ms. No renovar stale ni reconsultar retrospectivamente una referencia con publicaciones posteriores.

Para POI definir delta=0,02 y R=OI0/OI24. Exigir R finito y R<=1−delta=0,98. La igualdad habilita. Subida, igualdad de OI o descenso menor de2% rechaza. Un cero no representa una caída válida del100%: invalida por calidad. El control P no exige OI para entrar aunque el núcleo lo observe para auditoría.

Es una referencia exacta de seis pasos4h. Se preservan slots ausentes, stale y cero; no se comprime el tiempo, no se interpola ni se llena desde warmup. Primeras seis decisiones sin referencia24h, primer contexto posible en la séptima. El buffer nominal requiere ocho registros como convención común con uno de reserva.

El filtro OI es el mismo para long y short: exige reducción de exposición agregada, no predice el lado de la corrección. Esta POI NO debe pasar además un gate OI creciente. Root deberá implementar un modo explícito declining con delta configurable y logs/causas propios, o un adaptador equivalente auditado. No invertir silenciosamente el booleano rising ni etiquetar una aprobación como oi_nonrising sin distinguir el rechazo económico de calidad.

P significa patrón de precio. POI añade exclusivamente esta caída de OI. Funding contable sigue ON en ambas; no hay requisito económico de tasa, signo, extremos o calendario de pago.

## Entradas y economía

Entrada MARKET en T, únicamente plano, sin orden pendiente, start<T<finish y dentro de las ventanas activas estrictas del protocolo. Una entrada ejecutada como máximo por día UTC compartida entre long y short. No piramidar, parciales, órdenes retenidas ni reapertura en la misma decisión que un cierre. Un rechazo no consume cuota y no guarda oportunidad pendiente. Un fill cerrado por seguridad sí consume la entrada del día.

Capital inicial10.000 USDT por sesión, isolated3x contable y cap nocional1x del capital disponible; no multiplicar cantidad por leverage. Riesgo previsto2% por stop más ambos fees. Con p precio de decisión, C margen disponible, s=+1 long/−1 short, d=2A y stop_pre=p−s*d:

u=d+f*(p+stop_pre)
q=floor8(min(C/p,0,02*C/u)).

Exigir todos los precios, capital, distancia, stop_pre, u y q finitos y positivos, fee f>=0. El stop/target se ancla después al fill real usando distancia congelada; no redimensionar retrospectivamente. Funding, gaps y slippage pueden superar el riesgo previsto o el cap calculado antes del fill; reportar el hecho, sin garantía artificial.

Nominal fee0,00045 por lado y slippage0bps; funding histórico activo, debug/fast solicitados true, fast efectivo según contrato del motor y funding; exports/benchmark false. Datasets comunes congelados:
- Funding: 9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571.
- OI: 6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf.
No modificar configuración global.

## Stop, objetivo y holding

Congelar A al decidir. Desde fill real e:
- Stop=e−s*2A.
- Objetivo=e+s*4A, equivalente a2R.
- Holding máximo12 barras4h=48h absolutas desde opened_at.

Stop STOP y objetivo LIMIT por toda la posición según API smart orders existente. No trailing, breakeven, media móvil, parcial ni salida por cambio de OI posterior. El OI sólo gobierna nuevas entradas: su recuperación no se convierte en salida no declarada. No gestionar protección usando retrospectivamente el extremo o cierre previo del desplazamiento.

Validar stop/target positivos y finitos antes de ordenar y después del fill. Si el fill vuelve inválido el plan, el núcleo solicita cierre MARKET de seguridad; no elimina la operación ni inventa un fill al objetivo. Ratio2R permite una recuperación de hasta dos veces la distancia de stop, pero la corrección no está obligada a alcanzar ese nivel: puede revertir de nuevo y perder.

Prioridades: protección intrabar del motor; cierre de calendario; máximo48h; cierre final de sesión. No hay salida indicadora discrecional. Hold se mide por tiempo real transcurrido, no número de invocaciones. Stop y objetivo siguen activos aunque OI/precio de señal sea inválido. En los bordes semestrales se fuerza flat y se bloquea entrada en la decisión del borde; las reglas comunes preservan la separación de fases y costes.

## Vecinos previamente fijados

No grilla ni sustitución del nominal por el mejor vecino.

- Riesgo R09: stop1,8A, target3,6A, RR2 fijo; señal M2/delta0,02/periodo6 y hold12 iguales.
- Riesgo R11: stop2,2A, target4,4A; resto igual.
- Señal A09: M1,8 y delta0,018, de modo que el umbral OI es ratio<=0,982; stop2A/target4A/hold12 iguales.
- Señal A11: M2,2 y delta0,022, ratio<=0,978; resto igual.

En P los vecinos de señal sólo cambian M; no se introduce OI. En POI se mueven coherentemente intensidad de precio y caída OI ±10%, con períodos24h/última corrección4h intactos. No cambiar período6, corrección estricta, dirección, tamaño, hold o RR en estos vecinos.

Retraso OI adicional común: cuatro horas de reloj, una barra4h. En T se entrega observación obtenida en T−4h y referencia obtenida en T−28h; su calidad se evalúa en cada reloj original, sin volverlas frescas por entrega posterior. Primera referencia posible después de siete decisiones de inicialización; buffer nominal más una barra de lag. El precio sigue evaluándose con el cierre actual T: el escenario mide entrega tardía de la feature OI, no un desplazamiento de toda la estrategia. P reutiliza nominal para ese slot si el protocolo lo establece.

## Gates, presupuesto y datos ya observados

Root fija fechas y presupuesto comunes antes de economía. Se mantienen sin relajar los gates de SCREEN: N>=30, neto>0, PF>=1,2, DD absoluto<=25% y al menos dos años positivos entre2021–2023 completos. Confirmación/replay: N>=100, neto>0, PF>=1,2, DD<=25%, al menos tres de cuatro semestres positivos y CAGR>=15%, además de fricción/vecinos/lag exigidos. La meta orientativa sigue20–30% anual. Menos operaciones no equivale a menor riesgo económico ni permite bajar la muestra mínima.

2020–2025 ya son datos observados en ciclos previos;2024–2025 sólo puede ser confirmación interna reutilizada, no OOS virgen. No consultar2026. Dos ablaciones nuevas, ninguna reutilización económica de P de otras familias. Si no pasan las condiciones, cerrar el intento según el protocolo, sin invertir de nuevo la relación OI ni buscar umbrales que lo salven.

## Checks y trazabilidad antes del GO económico

Plan de pruebas, todavía no ejecutado:
1. Exactitud de C0/C1/C6 y ATR14 actual/15OHLC; simetría de desplazamiento/corrección; igualdad M*A cuenta, corrección0 no; ventanas finitas, prefijos, anexos futuros, gaps/duplicados/NaN/overflow.
2. Ambos extremos OI, ratio exactamente0,98, apenas mayor/menor, igualdad/rising, cero, negativos, ausencia, referencia24h exacta, slots intermedios inválidos conservados. No exigir rising como segundo gate.
3. Disponibilidad label+6m/fresh10m en ambos relojes, primer contexto séptima decisión, lag4h exacto y sin re-aging. Proveniencia cantidad base.
4. Cuota UTC en medianoche, estado repetido y señal bloqueada sin latch, una posición, no reentrada en la decisión de cierre.
5. Cantidad floor8/riesgo+fees/cap, stop/TP congelados desde fill, target2R, fill inválido y protección, máximo48h/frontera/dedup de salidas.
6. Logs JSON finitos con línea<=1900 caracteres; meses/direcciones con partición de motivos y conteos conservados; precios/fill/plan/stop/TP/ATR, OI0/OI24/timestamps/ratio/delta/regla, hashes de ventanas y parámetros.
7. Conciliación de órdenes, trades, bruto−fees+funding=PNL y saldo final con tolerancia común. No afirmar cobertura de un fill/ramo que el smoke no ejerció.

## Riesgos que pueden falsar la tesis

Una reducción de OI puede ser cierre ordenado antes de más tendencia, reducción normal de contratos o cambio de base de posiciones; no prueba capitulación. El precio podría continuar el desplazamiento aunque la última barra corrija. Usar ATR actual incluye la corrección: cambia simultáneamente escala, distancia de stop y tamaño y no identifica un efecto aislado. La ratio OI puede seleccionar regímenes extremos poco frecuentes y dejar muestra insuficiente. La regla de estado puede reentrar en una reversión fallida en días sucesivos; se mide sin añadir un cooldown posterior. OI retrospectivo no certificado point-in-time y funding con marcas proxy mantienen sus limitaciones.

Se entrega sólo esta propuesta. No se implementó ni se ejecutó nada. Cualquier clarificación de interfaz o fuente debe registrarse antes de la primera economía V6.
