# R40 PAXG: diez escenarios primarios nuevos para revisión

Fecha local: 18 de octubre de 2026. Estado: propuesta completa, anterior a código y resultados R40. Requiere revisión de root antes de crear estrategias o lanzar. Tanda humana nueva de veinte exploraciones; este documento cubre diez PAXG, IDs PAXG40-01 a PAXG40-10.

## Alcance y contrato congelable

Se han consultado handoff, consolidado de diecisiete corridas, ledger histórico y cierre R20. R20 terminó diez de diez netos negativos; cinco muestras menores de treinta y cuatro DD superiores al 25%. No se cambia ninguna receta previa ni se seleccionan después lados, horas o años favorables. La referencia y la candidata weekend 0,75 permanecen intactas.

Estas son diez formulaciones operativas nuevas, no diez causas económicas independientes. Comparten grandes familias de tendencia y reversión. La información nueva puede consistir en un estimador, reloj, memoria del episodio, agregación OHLC o payoff medible; un nombre de indicador no constituye por sí solo evidencia. Ninguna narrativa observa inventario, noticias, liquidez, valor justo o flujo de órdenes.

Cada fila autoriza exactamente un full primario, sin barridos ni reruns económicos para rescatarla. Ventana 2020-10-15 a 2025-12-31 exclusiva. Capital 10.000 USDT, PAXG-USDT aislado sobre spot proxy aceptado, fee 0,00045 por lado en TODAS las órdenes, riesgo planificado 1%, 5x isolated, techo nocional 4,4x. Reserva de 10 bps sólo para sizing, no slippage ejecutado. Sin piramidado. Hasta dos backtests y un análisis propios, cuatro/dos globales coordinados. Sólo Jesse MCP; sin nuevos scripts, framework, instalaciones, fuentes, funding, live/paper, BTC ni 2026.

Motor común autocontenido en cada clase: cierre completo, decisión MARKET, quote propia M1 exacta T−60 segundos y paridad con cierre de ruta; stop activo permanente; máximo nocional y sizing conservador con costes/reserva iguales a R20. ATR14, conocido al decidir, salvo fijación distinta explícita. Evento consumido aunque ya exista posición, estados actualizados siempre, sin cola ni reutilización de transición. Las salidas de tiempo y señal requieren quote fresca; se conserva deuda hasta disponer de ella. Todo plazo se cuenta desde fill real. Se redondea cantidad hacia abajo a 0,0001. No contar frecuencias de oportunidades a partir sólo de trades.

Rutas 4h para 01–09, data M1; 10 ruta 1h con data M1 PAXG/SPY y 4h PAXG completas para ATR. Bloques diarios UTC sólo con seis 4h contiguas y semanales lunes UTC sólo con siete días completos; un bloque incompleto no se rellena. No se añade una ruta diaria que exija historia importada anterior. Inicio cash mientras no madure historia requerida, incluido en resultados.

Comparadores existentes para TODAS las filas: cash; retest PAXG aislado 1% (93a16137-e819-41a3-b325-0631a6627a6c, neto 546,11, 35 trades); weekend 0,75 aislado (ff199ebe-dab0-4c09-9078-fff98188e97c, neto 764,04, 60 trades, seleccionado adaptativamente). Cada fila añade el contraste histórico operacional más cercano. Comparar exposición y horizonte, no interpretar diferencias como ensayos aleatorizados. Un superviviente requiere contrastes posteriores coordinados, no promoción automática.

Gates descriptivos: neto positivo, PF >=1,2, N >=30, DD motor no peor que −25%; N menor es inconcluso y se conserva también su signo. A continuación costes extra 5/10 bps RT estáticos sobre todos los fills, cohortes 2023–2025, lados, concentración, auditoría de fills y MTM si sobrevive. Regularidad es meta de cartera; no exigir que cada señal opere todos los meses. 2020–2025 ya ha sido extensamente seleccionado. Predeclarar esta tanda no produce validación independiente ni OOS.

## Resumen de frecuencias previstas, sin conteos observados

| ID | Clase | Información/representación | Frecuencia prevista cualitativa |
|---|---|---|---|
| 01 | R40PaxgKalmanInnovation4h | Innovación normalizada de nivel latente causal | Media: desviaciones recurrentes de un filtro lento |
| 02 | R40PaxgLearnedSeason4h | Estacionalidad móvil estimada en los seis buckets UTC | Alta: dos oportunidades diarias después de maduración |
| 03 | R40PaxgSpectralProjection4h | Proyección de oscilación dominante sólo pasada | Media: cambios de fase en ventanas de semanas |
| 04 | R40PaxgWickBalance4h | Balance agregado de mechas sin volumen | Media: episodios de rechazo acumulado |
| 05 | R40PaxgKamaHysteresis4h | Tendencia adaptativa con banda y salida lenta | Baja/media: varios episodios por trimestre posibles |
| 06 | R40PaxgRangeCenterLead4h | Migración de centros high/low que precede cierres | Media: divergencias de agregados de dos días |
| 07 | R40PaxgWeeklyDailyPullback4h | Pullback diario alineado con tendencia semanal completa | Baja/media: varios eventos por trimestre posibles |
| 08 | R40PaxgDrawdownRecovery4h | Recuperación de mitad de excursión madura | Media: episodios de varios días, no extremos anuales |
| 09 | R40PaxgCusumDrift4h | Acumulación secuencial estandarizada de drift | Media/alta: suma de movimientos menores, no shock único |
| 10 | R40PaxgBetaResidual1h | Residual de lognivel condicionado por SPY | Media: observación diaria hábil, desviación de 1,5 sigma |

Son expectativas de diseño, no promesas de N ni estimaciones obtenidas de velas. No se exige conjunción de cinco filtros raros. Si una receta produce pocos trades se conserva como tal y no se relaja retrospectivamente.

## PAXG40-01 — corrección de innovación Kalman

Mecanismo funcional: separar un nivel suavizado de una desviación transitoria mediante un filtro recursivo causal. No se afirma que ese nivel sea valor justo ni que PAXG esté cointegrado con oro.

Sobre logcierres 4h, después de 61 precios, estimar v como varianza muestral de los 60 logretornos inmediatamente anteriores a la vela actual. Modelo local de nivel: Q=0,01v; R=0,25v. Inicializar m con logcierre anterior al primer update y P=R. Para cada nueva vela: Ppred=P+Q; innovación e=x−m; S=Ppred+R; z=e/sqrt(S); K=Ppred/S; actualizar m=m+K*e y P=(1−K)*Ppred. La señal usa e y S ANTES del update. Varianza cero/no finita => no señal y reinitialización en la siguiente muestra válida, sin inventar escala. No usar filtro suavizado hacia atrás.

Primer cruce desde |z|<1,5 hacia z>=1,5 vende; hacia z<=−1,5 compra. No repetir señal mientras siga del mismo lado. Stop 2 ATR4h; target fijo precio equivalente al m predictivo anterior al update si queda favorable a la entrada; si no queda favorable, descartar. Máximo 48h. Congelar target al evento; no convertirlo luego en media móvil.

Diferencia medible: estimador recursivo y escala de incertidumbre frente a shock de una vela o RSI. Contraste cercano: espejos de shock 4h y R20-01 AR. No se cuenta como una causa independiente de MR. Descartar con gates comunes o si target tan estrecho no soporta costes.

## PAXG40-02 — estacionalidad aprendida sin escoger horas posteriormente

Hipótesis funcional: la distribución del retorno condicionado por franja puede cambiar lentamente, aun sin poder identificar noticias o flujo. Todos los buckets compiten bajo la misma regla causal; no se fija una hora ganadora observada.

Seis buckets por hora de inicio UTC de la próxima 4h: 00,04,08,12,16,20. Para cada uno, media de sus últimos 90 logretornos de cuatro horas completamente maduros antes de la decisión. Necesita 90 por bucket; máximo unas 540 barras anteriores. Cada comienzo de día UTC congelar ranking de seis medias con información hasta ese momento: elegir sólo la mayor y la menor, desempate por hora UTC ascendente. En el cierre inmediatamente anterior al bucket elegido, comprar la mayor si su media es positiva y vender la menor si es negativa. Si ambas condiciones no se cumplen, el lado correspondiente no se opera. No restar media global ni inventar signo. Si los seis valores empatan, no operar. Entrada al precio de cierre que es el comienzo de ese bucket; retorno pasado de cada muestra pertenece al mismo intervalo de apertura a cierre 4h. Sin datos futuros del bucket actual.

Stop 2 ATR4h; sin TP; salida a las cuatro horas, máximo una oportunidad por bucket/día, incluida si estaba ocupado. Horas seleccionadas cambian sólo por entrenamiento pasado bajo receta fija. No hay filtro de significación ni de fees que se ajuste después.

Aporta una función de calendario estimada y móvil frente al calendario fijo/SPY hábil y fin de semana PAXG. No se llama patrón de oro físico ni efecto independiente del proveedor. La frecuencia es alta deliberadamente; el test puede mostrar que la dependencia estimada es ruido y los 9 bps la destruyen. Benchmark adicional: cash y R20-01/02 como modelos aprendidos de precio, no comparación causal limpia.

## PAXG40-03 — proyección espectral de ventana pasada

Hipótesis funcional: una oscilación dominante observada puede persistir una fracción de ciclo. Es una hipótesis predictiva, no evidencia de ciclo estable.

Usar exactamente últimos 192 logcierres 4h. Ajustar tendencia lineal OLS sobre t=0..191 y restarla, sólo dentro de esa ventana conocida. Calcular DFT real del residual; entre k=1..8 elegir máxima energía (desempate k menor). Esos periodos son 192/k barras. Ajustar residual por OLS a seno/coseno de la frecuencia elegida, intercepto incluido. Proyectar ese componente armónico en t=197 frente a t=191, equivalente a seis barras. NO extrapolar el drift lineal; únicamente la diferencia armónica. Si abs(diferencia log) >=0,5 ATR4h/cierre, operar su signo al primer cruce de esa condición o cambio de signo; condición persistente del mismo lado no repite. Todo ajuste recalculado con ventana terminada en la vela de decisión.

Stop 2 ATR4h, sin TP, máximo 24h. No centrar con futuro, FFT de historia completa ni elección posterior de frecuencia/ventana. Diferencia frente a AR/análogos: fase global de baja frecuencia, no dependencia de retorno adyacente ni vecinos de un patrón de ocho barras. Benchmark cercano R20-01/02. Riesgo específico: fuga de extremos de ventana y frecuencia espuria; se conserva incluso si falla.

## PAXG40-04 — balance de mechas agregado

Hipótesis funcional: rechazos repetidos de precios extremos pueden preceder desplazamiento cuando los cierres aún no muestran avance. Las mechas son OHLC observado, no absorción ni flujo agresor.

Ocho velas 4h completas: lower=min(open,close)−low; upper=high−max(open,close). B=(sum(lower)−sum(upper))/sum(high−low), sólo si denominador positivo. Requerir abs(cierre_actual−cierre_hace8)<=ATR14 conocido ANTES de la ventana (ATR en vela anterior a esas ocho). Señal long si B cruza >=0,20 con esa condición; short si cruza <=−0,20. Rearme al volver |B|<0,20 o cambiar lado; actualizar incluso ocupado. No requiere soporte, ruptura o nivel redondo.

Stop 2 ATR previo a ventana; TP 3 del mismo ATR; máximo 48h. Diferencia frente a barrera redonda R20-05: agrega forma de ocho velas sin precio nominal de barrera, y frente a semivarianza R20-08 utiliza excursiones intrabar en vez de signos de logretorno. No independencia de familias de rechazo/MR. Frecuencia media prevista.

## PAXG40-05 — tendencia KAMA con histéresis

Hipótesis funcional: un estimador de tendencia que se adapta a eficiencia del camino reduce cambios de posición en ruido. El contraste es un filtro y salida distintos, no una nueva causa de tendencia.

KAMA20 con fast_length=2 y slow_length=30 de Jesse, secuencial causal. Banda ±0,5 ATR14 actual alrededor de KAMA. Long en primer cruce del cierre por encima de banda superior; short en primer cruce por debajo de inferior. No requiere máximos Donchian, retest ni ADX. Señal consumida siempre; si se estaba ocupado no se reserva para después.

Stop inicial fijo 3 ATR al entrar; sin TP. Cerrar long cuando cierre<=KAMA−0,5 ATR contemporáneo o short cuando cierre>=KAMA+0,5 ATR, más máximo 20 días. La señal opuesta en esa misma vela sólo cierra; no reversa en una vela. Próxima entrada necesita cruce nuevo posterior. Sin trailing adicional, BE ni piramidado.

Diferencia respecto Turtle/retest y exposición lenta: estimador endógeno a eficiencia, banda simétrica y salida de histéresis; horizonte más largo que modelos R20. Indicador documentado por get_indicator_details(kama), no defaults supuestos. Benchmark cercano retest, Turtle histórico y exposición lenta como contexto; no recortar runners post hoc.

## PAXG40-06 — migración del centro del rango con cierres rezagados

Hipótesis funcional: la ubicación de excursiones high/low puede desplazarse antes que el cierre neto, incorporando información de trayectoria distinta del cierre.

Centro por vela m=(high+low)/2. A=media de seis m más recientes menos media de seis m anteriores. ATR congelado al comienzo de las doce velas. Requerir |A|>=0,75 ATR y |cierre_actual−cierre_hace12|<=0,5 ATR. Operar signo(A) en primer evento calificado; no repetir mientras persista mismo signo/calificación. Rearme cuando deja de calificar o cambia signo. No se exige contracción de volatilidad ni ruptura de máximos/mínimos.

Stop 2 ATR congelado; TP 3 ATR congelado; máximo 48h. Contraste cercano R20-09 (agotamiento de pendientes de cierres): aquí el cierre está rezagado y la dirección la aportan rangos, no se apuesta contra una tendencia lineal que se agota. Parentesco con 04 reconocido; uno usa ubicación del rango, el otro asimetría de mechas, sin afirmar causas independientes.

## PAXG40-07 — pullback diario alineado con tendencia semanal

Hipótesis funcional: un retroceso de días puede revertir dentro de dirección de varias semanas. No se afirma que RSI sea una nueva causa frente a sleeves anteriores.

Construir diarios UTC completos desde 4h y semanas lunes UTC completas. Tendencia semanal: media de últimos cuatro cierres semanales versus media de últimos ocho; long si SMA4>SMA8, short si menor. No usar la semana en curso. RSI2 Jesse sobre diarios completos, calculado en cierre UTC de cada día. En tendencia long, episodio cuando RSI<20; señal al primer día posterior que cruza >=20 mientras tendencia siga long. Espejo short: armar RSI>80 y disparar <=80 con tendencia short. Un cambio de tendencia desarma episodio; actualización diaria aunque ocupado. No señal intradiaria a partir del RSI diario incompleto.

Stop 2 ATR14 diario completo al evento; sin TP; máximo cinco días. Entrada tras fijación diaria conocida con quote M1 fresca. Diferencia operacional frente a RSI3 de sleeve 4h y retest Donchian: horizonte diario/semanal completo, salida temporal fija sin target de media ni retest de nivel. Evitar llamar a esta receta una causa económica independiente. Espera cualitativa varios episodios por trimestre; N bajo se informa, sin cambiar niveles.

## PAXG40-08 — recuperación parcial de excursión madura

Hipótesis funcional: una recuperación de mitad de una excursión de varios días puede tener continuación hacia reparación adicional. No observa cuentas bajo agua ni órdenes de breakeven.

Cuando no exista episodio, identificar dentro de 60 cierres 4h el máximo y mínimo más recientes (desempate extremo más reciente). Si precio está al menos 4 ATR por debajo del máximo con edad >=12 barras, armar episodio long con peak máximo y ATR del armado. Espejo short desde mínimo. Si ambos candidatos simultáneos, elegir mayor excursión en ATR, empate =>ninguno. Un episodio activo dura como máximo 60 barras desde armado. Para long, actualizar trough mínimo observado desde peak hasta armado y posteriormente; señal al primer cierre que recupera >=50% de peak−trough, siempre que excursión peak−trough>=4 ATR congelado y edad del peak>=12. Short simétrico con techo observado y nivel de mitad. Actualizar extremos aunque ocupado. Evento/expiry consume episodio y memoriza timestamp del extremo de origen para no reutilizarlo; nuevo episodio requiere origen posterior, no armar y disparar en la misma vela.

Stop 2 ATR congelado al armado; sin TP; máximo 72h. Diferencia frente a R20-06 revisita breakeven: entrada en mitad de recuperación y continuación, sin retorno/rechazo de nivel de origen congelado. Frente R20-04 directional change: memoria de 60 velas, madurez mínima y profundidad>=4 ATR antes de armar, no cada reversión local. Es parentesco de reloj de evento, no causa independiente; estudiar su coste y muestra.

## PAXG40-09 — cambio secuencial de drift CUSUM

Hipótesis funcional: muchos movimientos menores coherentes pueden indicar cambio de drift sin que una sola vela sea un shock. Un detector secuencial reemplaza el calendario de evaluación del movimiento.

En cada 4h, z=(r_actual−media(r_previos60))/std(r_previos60), logretornos y desviación muestral; excluir r_actual del baseline. Splus=max(0,Splus+z−0,25), Sminus=max(0,Sminus−z−0,25). Si Splus>=4 o Sminus>=4, evento en el signo correspondiente y resetear AMBOS a cero, aun si ocupado. Empate simultáneo =>no trade y reset; varianza cero/no finita =>reset y no trade. Valores de referencia no calibrados después.

Stop 2 ATR4h, TP 4 ATR4h, máximo 48h. Aporta acumulación normalizada y reset de estado frente shock1,5ATR de una vela, staircase de seis signos iguales o AR estimada. No barrer h/k tras resultado. Frecuencia media/alta prevista; dependencia entre eventos no se niega.

## PAXG40-10 — residual de lognivel condicionado por beta SPY

Hipótesis funcional: una relación estimada entre precios puede producir desviaciones reversibles de PAXG. No afirma cointegración estable, hedge ejecutado, valor justo del oro ni cobertura de riesgo neutral a SPY.

Fijaciones de lunes a viernes 16:00 Nueva York con ambas M1 exactas T−60 segundos; manejar DST por zona horaria. Antes de fijación actual, últimas 60 fijaciones válidas conjuntas de logPAXG y logSPY: OLS y=a+b*x. Usar media y std muestral de residuos de esas 60 observaciones; si var(x)=0, stdresidual=0 o coeficientes no finitos, no señal. Residuo actual e=yactual−a−b*xactual; z=(e−meanresidual)/stdresidual. Primera transición z>=1,5 =>short PAXG; z<=−1,5 =>long PAXG; no reentrar por desviación persistente mismo lado. No clipping oculto de beta, ni ajuste con fijación actual.

Congelar a,b y meanresidual de la señal para la salida: cerrar en una fijación posterior cuando el residual bajo ESE modelo haya cruzado meanresidual hacia la dirección objetivo, o máximo cinco días naturales con salida por quote propia fresca. Stop 2 ATR14 de 4h completas al evento, sin TP pasivo; mantener stop aunque SPY esté cerrado. Sin SPY fresco no hay nuevo evento/residual; la salida por tiempo propia no depende de SPY. Una salida de residual con quote conjunta válida no se guarda como nuevo entry. Eventos se actualizan aunque ocupado.

Diferencia frente a divergencia7d y R20-10 mes-fin: relación de niveles con beta e intercepto estimados en 60 observaciones, sin fin de mes, sin cociente nominal de precios y con salida bajo parámetros congelados. No es dos patas ni carry. Riesgo material de regresión espuria entre niveles: esto se prueba como señal funcional y no se presenta como evidencia econométrica de cointegración. Si sobrevive, el control con beta fija y ablation causal se coordina antes de promover, sin rellenar diez ideas con esos controles.

## Trazabilidad y criterio de cierre

Tras aprobación: diez archivos autocontenidos generados desde un template; readback completo, comparación de prefijo normalizado y diez bloques de señal. Presentar motor común una vez y diferencias antes de los dos primeros runs. La fuente completa queda en strategy_codes de cada sesión. No usar módulo externo mutable. Solicitar detalles de indicadores antes de emplearlos: KAMA, RSI y ATR ya documentados por MCP en diseño.

Reportar diez sesiones, todos fallos técnicos/económicos, N, neto bruto/fees, PF/DD, exposición, cohortes, lados, concentración y recargos estáticos. Pocos trades no justifican bajar requisitos; un resultado negativo se archiva con alcance preciso. Una superviviente exige auditoría de ejecución, robustez coordinada y después cuenta compartida real; no sumar curvas aisladas. Nada de ello abre 2026.

Toda modificación de ecuación antes del primer run se guardará como adenda explícita revisada; una vez observados resultados de una fila no se modifica para rescatarla.
## Adenda definitiva tras revisión de root, anterior a código/resultados

Root aprobó las diez formulaciones para implementar con estas precisiones, que prevalecen sobre el texto de propuesta:

- 01 exige 62 precios incluyendo actual, para 60 retornos anteriores al actual. Clasificar z en −1/0/+1 con umbral ±1,5. Dispara 0→±1 o cambio directo de lado; persistencia del mismo lado no repite. Actualizar filtro y clasificación aun ocupado.
- 02 reemplaza log(close/open) por log(C_i/C_{i−1}) asociado a hora de apertura de barra i, sólo si esos cierres están separados exactamente cuatro horas. Alinea etiqueta con entrada al cierre anterior y evita asumir open futuro o ausencia de gap. Necesita 90 retornos maduros por bucket y el cierre previo (al menos 541 cierres). Ranking sólo a 00 UTC con la barra 20→00 ya madura; arranque intradiario espera medianoche. Esta versión reemplaza la mención body del diseño inicial, sin resultado observado.
- 03 conserva t197 frente t191 y ajuste exclusivo pasado.
- 07 usa semanas lunes UTC y días completos; sin velas superiores en formación.
- 08 conserva origen consumido y prohibición de armar/disparar en misma barra.
- 10 congela parámetros de salida del trade, separados de los modelos que siguen actualizándose aunque ocupado.

Todas las fórmulas de filtros y episodios se ejecutarán en before incluso ocupado; no se difieren eventos. Las clases se generarán autocontenidas y se presentará motor común más diez señales con readback antes de ejecutar.

## Adenda de conformidad de implementación, anterior al primer run

Tras revisión de root del motor y diez bloques:

- 01 guarda fixed_target=exp(m_predictivo) como precio absoluto congelado. on_open_position prioriza ese precio sobre TP expresado como distancia; no se desplaza con el fill. Los targets ATR de otras recetas siguen relativos al fill real.
- 02 recorre la historia disponible en orden inverso, sólo pares close/close contiguos, hasta obtener las 90 etiquetas maduras más recientes de cada bucket. Se elimina el límite técnico arbitrario de 650 barras. El almacenamiento disponible del motor es el límite de historia; no se afirma importar datos adicionales.

Root aprobó el resto del motor y diez señales y autorizó iniciar 01/02 y seguir la cola fija una vez persistidos cambios y readback. No había resultados ni corridas R40 PAXG al aplicar esta adenda.
