# V3 — propuesta sector rango y reversión a media 4h
Fecha: 2026-10-20.
Estado: DISEÑO SOLAMENTE; sin código, drafts ni backtests de este sector. Pendiente integración en protocolo V3 de root y GO explícito para implementar.
Antecedentes leídos: DOCS.md, skill backtest-expert y FINAL_DECISION_V2.md por MCP. V2 cerró SIN_CANDIDATA; no se cambian sus reglas ni se retoman sus slots.

## Hipótesis
En un régimen de desplazamiento lento pequeño, una excursión nueva de cierre fuera de dos desviaciones del precio medio reciente tiende a revertir hacia esa media antes del stop protector o48h. La información OI creciente24h se mide por ablación y puede perjudicar esta hipótesis; no se presupone que tenga valor.
Éste es un sector de reversión contraria al desplazamiento extremo en4h, diferente de continuación por canal o pullback de tendencia. No se seleccionarán umbrales a partir de su primer resultado.

## Dos variantes, sin grilla
- RANGE_P: señal de precio y filtro lateral descritos abajo.
- RANGE_POI: lo mismo más OI actual>OI observado24h antes.
Los nombres definitivos de clases quedan a root. Funding contable ON en ambas; sin gate económico funding.
Se proponen únicamente estas dos configuraciones. Cambiar dirección, reingreso a banda, umbral, ventanas, objetivo u horizonte después de resultados sería otra versión, no una variante gratuita.

## Datos y reloj
Sólo BTC-USDT perpetual Binance, decisión4h UTC con ejecución histórica1m completa. En T se usan únicamente barras open_time+4h<=T, y la última debe terminar exactamente en T. Los últimos144 cierres deben ser consecutivos, finitos, positivos y acompañados de OHLC coherente. La gestión de posiciones sigue activa aunque se invalide una feature.
Warmup240barras4h, sin operar durante warmup. El requisito144 proviene de dos medias120 separadas24barras: su unión abarca144cierres. OI24h son seis barras, una escala distinta.
Usar datasets exactos congelados que indique protocolo V3; no reemplazarlos silenciosamente. Mantener distinción de ausente, stale, cero e inicialización. No consultar métricas ni datos nuevos2024–2025/2026 para esta propuesta.

## Fórmulas causales, calculadas al cierre T
C_k es el cierre k barras antes del último cierre terminado en T, k=0...143. Cada barra dura4h.
1. M20(T)=media(C_0...C_19).
2. σ20(T)=std(C_0...C_19,ddof=0); exigir σ>0 finita.
3. z(T)=(C_0−M20(T))/σ20(T).
4. M20(T−1barra)=media(C_1...C_20); σ anterior análoga, positiva y finita, con z_pre=(C_1−M20_pre)/σ_pre.
5. M120(T)=media(C_0...C_119).
6. M120(T−24barras)=media(C_24...C_143). Veinticuatro barras son96h, no24h.
7. A(T)=media aritmética de los14 true ranges de las últimas14 barras4h cerradas, usando15OHLC cerradas para sus cierres previos:
TR_i=max(high_i−low_i,abs(high_i−close_(i−1)),abs(low_i−close_(i−1))).
No es ATR Wilder ni un promedio sembrado implícitamente.
8. Régimen lateral: R(T)=abs(M120(T)−M120(T−24barras))/A(T)<=0,5, con A>0 finita.
El cociente permite un desplazamiento de la media lenta de hasta media ATR actual durante cuatro días. Umbral0,5, ventana120 y separación24 son elecciones conservadoras iniciales de diseño, no estimaciones óptimas ni evidencia de lateralidad real.

## Entradas, simétricas
Exigir régimen lateral en T.
- Long: z(T)<−2 y z_pre>=−2.
- Short: z(T)>+2 y z_pre<=+2.
Es una excursión nueva fuera de la banda, no un reingreso posterior ni una confirmación de giro. La barra que cruza está cerrada y participa legítimamente en su propia media/desviación. El criterio anterior usa su propia banda anterior; no comparar el cierre previo con una banda posterior.
Orden MARKET en la decisión T. Ambas direcciones disponibles, sólo plano/sin entrada pendiente, máximo una entrada efectiva por día UTC, sin piramidar ni parciales. Gate temporal start<T<finish.
La excursión puede continuar: ese riesgo es parte de la hipótesis y no se añade un filtro de aceleración/RSI/volumen tras observar pérdidas.

## OI de RANGE_POI
Aplicar exactamente el gate común24h: observación causal disponible en T y observación efectivamente obtenida en T−24h, ambas válidas y >0, actual>referencia.
Archivo retrospectivo label+6m y máximo10m desde disponibilidad según freeze, sin llenar huecos ni prolongar stale. Primeras seis decisiones de la sesión inicializan la referencia; no tomarla del warmup. RANGE_P no exige OI.
Registrar flags simultáneos y causa exclusiva. El rising OI puede confirmar una ruptura tendencial y empeorar un fade; la ablación sirve para falsarlo. No invertir a OI decreciente dentro de este ciclo si POI pierde.

## Salidas completamente especificadas
A0=A(T) y objetivo Q=M20(T) se congelan al decidir entrada. No recalcular Q con precios de barras posteriores.
Tras fill real e:
- Long: stop=e−2A0; objetivo LIMIT=Q.
- Short: stop=e+2A0; objetivo LIMIT=Q.
Stop STOP y objetivo LIMIT por toda la cantidad. No trailing, break-even, escalado ni salida por un cambio de régimen posterior.
La media congelada da un nivel alcanzable definido en la decisión; una media móvil dinámica sería otro mecanismo.
Salida MARKET en primera decisión4h con edad>=48h, o cierre forzado al borde exclusivo del fold, con costos.
Validar antes de ordenar stop_pre=p−s*2A0>0, Q>0 y s*(Q−p)>0, s=+1long/−1short. Si inválido, no entrar y registrar causa.
Tras fill exigir stop y Q finitos/positivos y s*(Q−e)>0. Si un fill adverso cruza Q o vuelve inválida la protección, cerrar MARKET inmediatamente con motivo invalid_after_fill o target_crossed_after_fill; no fingir un fill favorable en el objetivo ni cambiarlo después.
No imponer ratio mínimo de beneficio/riesgo adicional: Q puede estar cerca en relación a2A0 y fees. Registrar ese ratio y sus costos como diagnóstico, no como un gate no declarado.
Conflictos intraminuto y gaps conservan la política documentada del motor, sin elegir trayectorias favorables.

## Sizing y costos
C=available_margin antes de entrada, p=precio de decisión, s=+1long/−1short, d=2A0, f=fee de la sesión.
stop_pre=p−s*d.
u=d+f*(p+stop_pre).
qty=floor8(min(C/p,0,02*C/u)).
Exigir valores positivos finitos y cantidad>0. Notional capC, sin multiplicar por isolated3x. Presupuesto2% cubre stop y fees redondos presupuestados; slippage, funding y gaps son adicionales, no pérdida máxima garantizada.
Nominal propuesto:10000USDT,isolated3x,fee0,00045 por lado,slippage0 para continuidad comparativa. Root fija nominal/estrés global antes de resultados. Funding contable siempre activo con el dataset freeze y su límite de marcas proxy. Bajo fee estresada se redimensiona con esa fee; no reconstruir fills con haircut posterior.

## Por qué no es reabrir RangeFade5m
DOCS.md registra RangeFade5m descartada. Este diseño no copia ni modifica su código ni presume sus parámetros; no afirma conocer detalles no leídos.
La pregunta aquí está fijada a4h, media de20cierres (~80h), media lenta120cierres (~20días), filtro cuantitativo de deriva96h/ATR, stop2ATR4h y holding48h. Es otra escala temporal y una hipótesis explícita de régimen antes del fade, no un nuevo nombre para validar retrospectivamente la estrategia5m descartada.
La diferencia de horizonte no garantiza independencia estadística: usa el mismo activo y años de desarrollo ya observados. Se debe registrar parentesco como familia de reversión; no contar como prueba independiente que nunca fue explorada.

## Riesgos que el resultado debe poder mostrar
- Un filtro de media lenta rezagada puede llamar lateral al inicio de una tendencia nueva.
- Un pico ATR eleva el denominador de R y puede volver admisible una ruptura violenta; no limitar ATR después de resultados.
- Cruzar hacia afuera puede entrar contra un movimiento persistente; no equivale a observar agotamiento.
- La media objetivo puede dar premio/riesgo insuficiente y los costos consumir el rebote.
- Dos días aumentan ocupación, cobros funding y restricciones de nuevas entradas; comparar turnos/exposición, no sólo N.
- Rising OI puede reforzar la continuación en vez de la reversión. Su utilidad queda abierta.
- Dataset OI retrospectivo sin certificación point-in-time, funding con marcas proxy y nominal sin slippage no validan ejecución real.
- El filtro puede reducir la muestra. Falta de trades es evidencia insuficiente, no estabilidad ni permiso para ampliar el umbral.

## Instrumentación, pruebas y límites para el GO
Antes de economía: fuente completa/hashes, pruebas de prefijos/mutación futura para M20/σ/z y sus versiones previas, M120 actual/retrasada y A; ventana144 consecutiva, horarioUTC, ceros/NaN/gaps, simetría long/short y target congelado con fill adverso.
Guardar por entrada M20,σ,z,z_pre,M120 actual/retrasada,R,A, extremos/hash de144OHLC, p/fill/qty/stop/Q, OI timestamps, margen y riesgo presupuestado. Loggear explícitamente salida por stop, objetivo,48h,fold_end yfillinválido. Conciliar bruto−fees+funding=PNL/saldo y contadores.
No se proponen cambios de gates de selección de V2 dentro de este sector. Root define el protocolo V3 completo, cronología, presupuesto, selección y eventual confirmación antes de probar; no asignar slots nuevos automáticamente ni abrir reserva2024–2025/2026.
Si se conserva cuatrofolds train/eval, este sector usa2×4×2=16slots nominales de exploración; el presupuesto global y fases posteriores pertenecen al protocolo coordinado.
Máximo2backtests simultáneos por subagente sólo si backend estable y root lo habilita; la reducción previa auno porsector sigue siendo prudente ante timeouts. Esto es capacidad operativa, no selección económica.
No implementar ni ejecutar hasta GO. Sin CLI,DB,env,research_scripts,instalaciones,live/paper,Pi,commit/push o reinicio.
