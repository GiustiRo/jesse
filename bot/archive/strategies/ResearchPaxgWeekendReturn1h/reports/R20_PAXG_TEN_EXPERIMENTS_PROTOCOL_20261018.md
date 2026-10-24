# R20 PAXG: matriz de diez experimentos primarios para revisión

Fecha local: 18 de octubre de 2026. Estado: MATRIZ DEFINITIVA APROBADA CON ADENDA; no se ha creado código de trading ni ejecutado ningún backtest de esta tanda. Leer junto con R20_SPY_PAXG_STAGE_PROTOCOL_20261018.md y el consolidado SPY_PAXG_RESEARCH_RESULTS_20261018.md.

Se han leído completos el handoff original, su actualización SPY/PAXG y el consolidado de diecisiete runs. La referencia, BTC, las estrategias de fin de semana ya investigadas y 2026 quedan intactos. Root aprobó los diez diseños con las precisiones de la adenda final; no quedan retiradas de diseño ni sustituciones en esta matriz.

## Contrato común y alcance de evidencia

Cada ID tendrá un full primario nuevo. Controles o sensibilidad posteriores no rellenan el cupo. No hay rejillas ni cambio de recetas tras observar resultados. Las familias amplias se solapan; no se afirma independencia económica o estadística entre diez tests ni frente al historial global.

Son hipótesis exploratorias de precio, no hechos empíricos ya probados. Algunas son modelos funcionales de predictibilidad; sus narrativas de inventario, memoria o información no implican observar flujos, noticias o valor justo. No se descarga nueva información.

Todos: PAXG-USDT aislado, Binance Perpetual Futures simulado sobre spot existente aceptado, capital 10.000 USDT, riesgo planificado fijo del 1%, fee 0,00045 por lado incluidas LIMIT, 5x aislado, máximo nocional 4,4x, sin piramidado. Reserva de 10 bps sólo en sizing, no fricción aplicada. Ventana 2020-10-15 a 2025-12-31 exclusiva. Modo normal, warmup 240 actual. Hasta dos backtests y un análisis propios; cuatro y dos globales. No configuración global, framework, instalaciones, scripts nuevos, fuentes nuevas, live/paper, Pi ni funding.

Entradas MARKET después de vela cerrada, salvo que una fila especifique otra cosa. Cada entrada requiere última M1 propia exacta T−60 segundos, precio positivo finito y paridad con cierre de la ruta. Una señal es una oportunidad por evento; si está ocupado, se descarta, sin cola. Stops permanecen activos siempre. Salidas de tiempo requieren quote propia fresca; deuda se conserva hasta una quote válida. Cantidad = mínimo de presupuesto del 1% incluyendo fees y reserva, techo 4,4x y 90% de margen apalancado, redondeada hacia abajo a 0,0001. Un único activo/posición; no se usa la simultaneidad para evadir riesgo.

ATR es Jesse ATR14 por defecto; se identifica cuándo se fija. Si una entrada necesita 4h auxiliares, se retienen sólo timestamps+4h<=T. Historial insuficiente produce cash de inicio incluido, no velas inventadas. No añadir 1D que exija nueva historia de 2019: cuando se necesiten días, usar fijaciones observadas o agrupaciones completas de historia existente; especificarlo en código antes del run.

Comparadores existentes, sin repetirlos:
- [Retest PAXG aislado 1%](http://localhost:9200/#/backtest/93a16137-e819-41a3-b325-0631a6627a6c), 35 trades, neto 546,11 USD.
- [Fin de semana 0,75 aislado 1%](http://localhost:9200/#/backtest/ff199ebe-dab0-4c09-9078-fff98188e97c), 60 trades, neto 764,04 USD.
- Cash, expectativa cero antes de inflación, como contraste mínimo.
Las diferencias de exposición y horizonte impiden interpretar esos comparadores como ensayos aleatorizados.

Gates descriptivos de todos los IDs: neto positivo, PF>=1,2, al menos 30 trades, DD no peor que −25%. Menos de 30 es inconcluso, no refutación de toda la idea. Luego costes extra 5/10 bps RT sobre mismos fills, concentración, cohortes 2023–2025 y auditoría MTM coordinada. Regularidad 65–70% meses / 80% trimestres es meta de CARTERA, no gate de cada señal. 2020–2025 sigue ampliamente seleccionado.

## Matriz de hipótesis y recetas

### PAXG20-01 — respuesta autorregresiva estimada

Estrategia propuesta: R20PaxgARResponse4h. Ruta 4h; data M1.

Hipótesis funcional: el signo de la respuesta de corto plazo cambia entre persistencia y corrección; estimar esa dependencia con datos maduros puede superar imponer siempre continuación o reversión después de un shock. No se presupone que el estimador detecte liquidez o causas económicas.

Trigger: sobre los últimos 241 retornos log 4h disponibles, estimar OLS r[t]=a+b*r[t−1]. Todos los pares de entrenamiento ya están cerrados. Proyectar recursivamente seis pasos desde el último retorno y sumar su retorno esperado. Entrar en su signo únicamente si magnitud de retorno esperado supera 2*fee+0,001 (19 bps). Matriz singular o valores no finitos: no operar. Mínimo 242 cierres.

Salida: stop fijo 2 ATR 4h desde fill; sin TP ni trailing; máximo 24 horas.

Aporte frente al historial: dependencia estimada y signo variable, no shock fijo 1,5 ATR, Donchian o un RSI distinto. Es un nuevo modelo funcional, no evidencia independiente de momentum/MR. Comparar con cash/retest y, descriptivamente, los shocks archivados. Descartar por gates comunes y si beneficio depende de un período o pocos coeficientes extremos.

### PAXG20-02 — analogía de trayectorias maduras

Estrategia: R20PaxgPathAnalogue4h. Ruta 4h; data M1.

Hipótesis funcional: una secuencia multibar puede contener información sobre la continuación/corrección que no está resumida en el último retorno ni en pivots discretos. La semejanza de formas se contrasta, no se atribuye automáticamente a ciclos de inventario.

Trigger: vector de los últimos ocho retornos 4h, cada uno dividido por ATR/close conocido al comenzar su ventana. Buscar dentro de las 720 observaciones previas ventanas de ocho retornos cuya etiqueta a seis barras esté COMPLETAMENTE madura al decidir. Elegir los 20 vecinos de menor distancia euclídea con finales separados al menos ocho barras, excluyendo la ventana actual y cualquier futuro. Forecast = media de sus retornos log de las seis barras siguientes. Operar su signo si forecast absoluto supera 19 bps. Requiere veinte vecinos válidos y 740 cierres; sin reajuste de k, distancia o ventana.

Salida: stop 2 ATR 4h actual desde fill, sin TP ni trailing, máximo 24h.

Aporte: pronóstico no lineal de forma con etiquetas maduras, distinto del observador BTC de pivots/first-touch y del AR lineal del ID01. Se reconoce selección de representación y riesgo de sobreajuste; no claims ML fuera de muestra. Comparadores existentes cash/retest; ID01 sólo contraste interno adicional, sin reemplazar la primaria. Gate común y concentración temporal.

### PAXG20-03 — retraso tras shock de SPY con PAXG inicialmente quieto

Estrategia: R20PaxgSpyDelayed1h. Ruta PAXG 1h; data M1 PAXG/SPY y PAXG4h.

Hipótesis: si existe ajuste tardío defensivo, una gran variación de SPY sin movimiento contemporáneo apreciable en PAXG podría preceder una respuesta contraria de PAXG. Un desplazamiento contemporáneo no basta: se exige quietud PAXG y se evalúa sólo PnL posterior. No se afirma que investigaciones de oro demuestren el efecto en este token.

Trigger: fijaciones emparejadas propias de ambos precios a las 16:00 America/New_York. Sólo cambios de fijaciones separados 23–25 horas, excluyendo lag de fin de semana por alineación del horizonte. Calcular sigma de los veinte cambios diarios emparejados previos, sin incluir el actual. Evento: abs(retSPY)>=2*sigmaSPY y abs(retPAXG)<=0,25*sigmaPAXG. Entrada PAXG opuesta al signo SPY. Fresh M1 exacta en ambos extremos, sin imputar ausencias. No cambiar signos ni retirar shorts después del resultado.

Salida: stop 2 ATR PAXG4h ya completas al evento; sin TP; máximo 24h.

Aporte: ventana y quietud identifican retraso posterior, no la divergencia contemporánea 7d BTC/SPY/PAXG ya fallida. Solapa ampliamente la familia risk-off y debe revisarse especialmente por duplicación. Comparar con cash/retest y con la divergencia archivada sólo como antecedente. Gates comunes; pocos eventos es inconcluso.

### PAXG20-04 — overshoot en reloj de cambio direccional

Estrategia: R20PaxgDirectionalOvershoot1h. Ruta 1h; data M1.

Hipótesis: tras una reversión de magnitud material respecto del extremo móvil, el desplazamiento puede continuar un tramo adicional; el reloj intrínseco representa estructura distinta de un canal temporal o un único shock.

Trigger: inicializar el primer extremo con el primer cierre válido. Fijar H=2 ATR1h conocido al iniciar cada tramo. Actualizar extremo de cierre a favor de la dirección; confirmar cambio cuando cierre retrocede H desde el extremo. En cada cambio confirmado, invertir dirección del estado y fijar el H del siguiente tramo con ATR actual. Entrar en la NUEVA dirección en ese cierre, sólo una vez por cambio. El estado continúa actualizándose mientras hay posición y los eventos ocupados se pierden, sin cola. Primer estado se confirma tras desplazamiento H desde inicialización.

Salida: stop a H de entrada y TP a 2H desde fill, H igual al umbral que confirmó el evento; máximo 24h.

Aporte: muestreo por distancia y extremo móvil, no Donchian/quiet-channel ni BTC event-clock con buckets temporales. Familia de continuación compartida, sin afirmar independencia. Comparadores cash/retest; gates comunes y fricción por posible turnover.

### PAXG20-05 — rechazo de barrera nominal predeterminada

Estrategia: R20PaxgRoundBarrier1h. Ruta 1h; data M1.

Hipótesis: la concentración psicológica en precios nominales redondos podría generar respuesta distinta al rechazo de un extremo endógeno. No se observan órdenes ni stops reales.

Trigger: rejilla ex ante de múltiplos de 50 USD. Si una vela cruza una barrera desde abajo, su high queda al menos 0,25 ATR previo por encima y su cierre vuelve debajo, vender; caso simétrico desde arriba para comprar. El cierre anterior debe estar del lado de aproximación. Si cruza más de una barrera, no operar para evitar una elección retrospectiva de nivel. Cada barrera sólo se rearma tras cierre a más de un ATR de distancia; se consume la oportunidad al primer rechazo. No seleccionar múltiplos o cambiar el tamaño de rejilla.

Salida: stop 1 ATR previo desde fill, target 2 ATR previo; máximo 12h.

Aporte: nivel nominal fijado antes de observar la trayectoria, distinto de fallo de rango20 con ER y del retest de ruptura. Sigue familia amplia de rechazo y requiere revisión crítica de duplicación. Gates comunes; el valor nominal y sus cambios históricos son una limitación explícita de esta hipótesis.

### PAXG20-06 — revisita al precio de equilibrio tras pérdida profunda

Estrategia: R20PaxgBreakevenRevisit4h. Ruta 4h; data M1.

Hipótesis: tras una excursión profunda, la primera recuperación hacia un extremo previo puede encontrar venta de salida al equilibrio, o compra simétrica tras un rally. Es memoria de un episodio de pérdidas, sin afirmar inventario observado.

Trigger: con al menos 180 barras, al estar flat identificar un máximo de las 120 barras anteriores, ocurrido al menos seis barras atrás. Armar ese máximo si cierre está al menos 4 ATR actuales debajo; congelar nivel y ATR. Mantener hasta 120 barras. Primer toque posterior del high a nivel−0,25 ATR congelado, con cierre por debajo del nivel, genera short; el nivel se consume aunque el evento ocurra ocupado. Regla espejo con mínimo/rally/revisita genera long. Si hay dos candidatos simultáneos, no armar; un único episodio activo. Si vence, esperar una nueva excursión, sin reciclar el mismo extremo.

Salida: stop 2 ATR congelados y target 2 ATR, máximo 48h.

Aporte: procedencia explícita del nivel y excursión profunda/recuperación, no rango lateral oscilante ni pivots usados para pronóstico binario. Solapa rechazo/MR pero contrasta memoria del episodio. Gate común; una muestra pequeña se registra como inconclusa.

### PAXG20-07 — continuación de escalera de cierres sin impulso aislado

Estrategia: R20PaxgStaircase4h. Ruta 4h; data M1.

Hipótesis: un ajuste gradual de precio puede persistir aunque no aparezca una vela de noticia o liquidación grande. Se distingue camino distribuido de salto, sin observar noticias.

Trigger: seis retornos de cierre consecutivos estrictamente del mismo signo. ATR fijado antes de esas seis barras; cada cambio absoluto debe ser <=0,75 ATR y la suma direccional >=1,5 ATR. Entrar en el signo de la secuencia al completarse; una secuencia se consume al primer evento y sólo se rearma tras un retorno de signo opuesto. Sin requisito de nuevo máximo, Donchian, EMA o ADX.

Salida: stop 2 ATR del inicio de secuencia, target 3 ATR; máximo 24h.

Aporte: difusión distribuida y exclusión de salto aislado; no variación del shock1,5ATR ni de su horizonte48h. Familia momentum compartida, test de forma de acumulación. Gate común y auditoría de episodios.

### PAXG20-08 — asimetría de riesgo con desplazamiento neto neutro

Estrategia: R20PaxgSemivariance4h. Ruta 4h; data M1.

Hipótesis: la geometría de variaciones alcistas y bajistas puede anticipar dirección aun cuando el cambio neto sea pequeño; no equivale a momentum de cierre ni afirma opciones o skew implícito.

Trigger: últimos sesenta retornos log. Sumar cuadrados positivos y negativos por separado. Exigir desplazamiento neto absoluto de las sesenta barras <=un ATR actual/close. Si semivarianza positiva/negativa>=3, operar long; si la inversa>=3, short. Ambas partes estrictamente positivas, sin divisiones por cero. Sólo la transición desde estado no elegible arma evento; salidas no rearman el mismo estado.

Salida: stop 2 ATR actuales, target 3 ATR, máximo 48h.

Aporte: anticipación de riesgo asimétrico en precio casi neutro, no shock puntual ni compresión de varianza total. Es un funcional distributivo nuevo, no un indicador con umbral elegido de una receta fallida. Gate común y extrema concentración se reportan.

### PAXG20-09 — agotamiento por pérdida de pendiente de un desplazamiento suave

Estrategia: R20PaxgTrendExhaustion4h. Ruta 4h; data M1.

Hipótesis: una tendencia suave que pierde pendiente antes de revertir podría expresar agotamiento de la demanda/oferta; la curvatura es un proxy de precio, no flujo observado.

Trigger: con treinta cierres, estimar OLS lineal en las primeras quince y últimas quince barras. Para short: avance total de treinta barras >=3 ATR actuales, pendiente anterior>0 y pendiente reciente>=0 pero <=0,25 de la anterior; R2 de la primera mitad>=0,7. Long simétrico tras caída. Entrar sólo cuando el estado pasa de falso a verdadero; no elegir pivots con confirmación futura ni variar ventanas/R2 después. Si las pendientes están indefinidas, no operar.

Salida: stop 2 ATR actuales; sin target ni trailing; máximo 48h.

Aporte: anticipa agotamiento por desaceleración, distinto de comprar sobreventa en tendencia macro, ruptura o rechazo de nivel. Riesgo de ser una representación técnica superficial se somete expresamente a revisión root. Gate común; no se rescata el diseño cambiando ventanas o R2.

### PAXG20-10 — rebalanceo contrarian relativo al final de mes

Estrategia: R20PaxgMonthEndRebalance1h. Ruta PAXG1h; data M1 PAXG/SPY y PAXG4h.

Hipótesis: la necesidad de rebalancear exposición tras rendimiento relativo fuerte puede generar reversión alrededor del cierre mensual, distinta de mantener al ganador por momentum. No se observan flujos institucionales ni se afirma estacionalidad probada del token.

Trigger: fijaciones emparejadas a las16NY, precios propios frescos. Último día lunes–viernes del mes según calendario nominal (si es festivo y faltan quotes, se pierde ese mes). Con veinte fijaciones previas, calcular retorno20obsPAXG−retorno20obsSPY; normalizar por sqrt(20)*std de los veinte cambios diarios relativos previos. Si magnitud>=1sigma de horizonte20, operar PAXG en sentido contrario al rendimiento relativo: ganadorPAXG→short, rezagado→long. Una entrada máxima por mes. No se elige retrospectivamente un mes del año o un signo.

Salida: stop2ATR4h completas al evento, sin TP. Salir tras tercera fijación emparejada válida del mes siguiente. Failsafe máximo diez días naturales con deuda de salida hasta quote propia fresca, para no mantener indefinidamente por ausencias. Stops siempre activos.

Aporte: contrarian relativo y ventana de rebalanceo, no rotación mensual long del mejor activo ni calendario SPY turn-of-month fijo sin señal relativa. Comparte familia calendario/momentum relativo y no se presenta como independencia. Gate común; analizar concentración por año y baja muestra.

## Novedad, revisión y congelación

Los IDs01/02 son hipótesis funcionales predictivas, no nuevas causas económicas observadas. Los IDs03/05/06/09/10 tienen riesgo de solapar familias previas; esta matriz los identifica antes de gastar runs. Root debe aceptar una diferencia medible o retirar/sustituir el diseño antes de la matriz definitiva. No se avanzará un duplicado sólo para completar diez nombres.

Las fuentes primarias sobre oro sugeridas por root sirven como motivación y crítica, no como validación PAXG. No se han atribuido sus conclusiones a precios posteriores que no observan. No se requiere acceso externo adicional para ejecutar las recetas de velas aceptadas.

Tras revisión, guardar una matriz definitiva que sustituya íntegramente este estado de diseño, registrar toda retirada previa y ejecutar los diez primarios congelados. Después, análisis de TODOS los resultados terminales y comunicación temprana de hallazgos. Cualquier control o integración será protocolo separado coordinado por root.


## Adenda definitiva aprobada por root — anterior a código y resultados

Root leyó las diez recetas completas y aprobó su ejecución como exploraciones funcionales diferenciadas, NO como diez causas económicas nuevas. Esta adenda resuelve las ambigüedades del diseño previo y prevalece sobre ellas; el resto de reglas queda congelado.

1. IDs03/10: todos los retornos PAXG/SPY y sus diferencias son LOG y adimensionales. No se restan cambios nominales en USD. ID03 exige al menos 22 fijaciones emparejadas y sigma de veinte retornos ANTERIORES, excluyendo el actual; cada intervalo aceptado debe ser de 23–25h, sin puentear fines de semana. ID10 exige 22 fijaciones; retorno relativo de veinte observaciones y sigma de veinte retornos relativos previos, sin incluir el último. sqrt(20) es normalizador heurístico, no supuesto IID, error estándar ni confianza estadística.
2. ID02: cada etiqueta se calcula exactamente a seis barras cerradas después de su origen y debe madurar antes o en el instante de decisión. La normalización ATR se fija al comienzo de cada ventana. Se vectorizará la extracción de ventanas y se calculará una serie ATR una vez por decisión, evitando cientos de llamadas a ta.atr. No se inventará un registro de predicciones: los snapshots de sesión no incluyen vars.
3. ID01: no se recortan coeficientes extremos ni se introducen regularizadores ocultos. Varianza cero o valores no finitos producen ausencia de señal. Coeficientes extremos son un riesgo del modelo, no permiso para filtrarlos tras resultados.
4. ID06 y todos los modelos stateful04/05/07/08/09: actualizar estados, vencimientos y consumo de eventos en before SIEMPRE, incluso ocupado. Sólo se permite la entrada si flat. No hay deuda de entrada ni reutilización de un extremo vencido. En ID06 la frase anterior «al estar flat identificar» queda sustituida por esta actualización continua. Los extremos ya usados o vencidos no se reciclan como episodios nuevos.
5. ID05: si la vela cruza varias barreras nominales de 50 USD, no hay señal; la regla se mantiene aunque ATR sea mayor que el paso. Ambos sentidos y rearme por alejamiento de un ATR se aplican simétricamente. No escoger una barrera favorable dentro de la vela.
6. Los parentescos amplios y riesgos de duplicación de IDs03/05/06/09/10 permanecen explícitos. La aprobación se basa en diferencias operacionales medibles, no en independencia estadística.
7. Diez clases AUTOCONTENIDAS generadas desde un template, cada snapshot conserva todo el motor y su señal. No módulo mixin externo: una posterior alteración externa no debe cambiar silenciosamente lo que representa strategy_codes de una sesión. Root revisará una sola copia del motor y diez bloques de señal, y se verificará readback de cada fuente completa antes de los primeros dos runs. No código ni resultados anteriores a esta adenda.


## Dependencia del ID02 y cola iniciada

Revisión final de root completada antes de lanzar IDs01/02. Se confirma: normalización ATR conocida al inicio, inputs terminan en k y labels exactamente en k+6<=j−2. La separación de ocho barras se impone a patrones de entrada; las etiquetas y ventanas de otros patrones conservan dependencia temporal. No se infieren veinte muestras independientes ni un tamaño efectivo de veinte por pronóstico. No se guardan predicciones fuera del contrato de snapshots.

Primeras sesiones iniciadas tras la revisión: [PAXG20-01](http://localhost:9200/#/backtest/51a0c817-4c43-4940-ab0e-4bfec6b3a52c) y [PAXG20-02](http://localhost:9200/#/backtest/a758809e-9d05-4e7e-a5b9-333751a19395). No se han cambiado recetas tras resultados.
