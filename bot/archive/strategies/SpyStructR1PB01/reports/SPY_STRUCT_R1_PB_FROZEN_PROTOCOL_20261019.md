# Propuesta SPY: corrección y continuación, especialista B

Fecha local 2026-10-19. Estado: planificación para revisión root; ningún código ni backtest nuevo creado o ejecutado.

## Alcance y antecedentes

Leídos DOCS.md, instrucciones del proyecto, backtest-expert, jesse://strategy, referencia AttrSpyCqFreshLimit, protocolos SPY20/SPY40 y resultados/handoff R60. Coordinación con especialista A: él estudia rupturas Donchian26 y retests de su techo congelado. Esta línea estudia recuperación de una corrección sin exigir ruptura de Donchian. Las ideas siguen siendo familiares de continuación y precio; no afirmar seis fuentes independientes.

No repetir gaps RTH, shock/crash, mean reversion hacia perfil de cierres, entropía, regresión, bandpass, barreras repetidas o compresión genérica. La inside bar aquí se exige DESPUÉS de corrección concreta bajo régimen original, sin buscar expansión desde baja volatilidad total; aun así existe parentesco con patrones de compresión. Un pullback genérico ya tiene antecedentes, por lo que la novedad defendible es la comparación de confirmación estructural conservando las mismas salidas/riesgo, no el nombre de un patrón.

## Propuesta de seis fulls: tres parejas en 4h

Sea t la vela 4h recién cerrada y O/C/H/L sus campos. Historia y decisiones conservan calendario UTC Mon-Fri00–20 e intervalo de entradas por apertura00–16. Mercado al cierre conocido, quote M1 exactamente decision_time−60s y misma close; si falta, omitir evento y no diferirlo.

Todas las filas reemplazan SOLO la exigencia Donchian26 y el desplazamiento desde esa frontera por su patrón. Conservar filtros actuales: C(t)>EMA80, EMA20>EMA80>EMA80[-5], ADX14>=26, RSI14 entre52y76, rango de vela4h<=3ATR14, al menos100 velas retenidas. ATR, EMA y demás se calculan en historia4h filtrada. Distancia de stop2ATR y validación0<distancia<entrada MARKET. Gestión original BE2,25R/trailing4,2ATR con tightening heredado, sizing1%,10k,fee0,00045lado,isolated5x,cap4,4,reserva0,001sólosizing. Sin nuevo filtro horario en gestión.

| ID | Disparador completo | Mecanismo y contraste |
|---|---|---|
| B01 Giro tras dos velas | C(t−2)<O(t−2), C(t−1)<O(t−1), C(t−1)<C(t−2); C(t)>O(t) y C(t)>C(t−1) | Recuperación básica tras corrección corta. No se exige nuevo máximo. |
| B02 Giro confirmado | B01 y C(t)>H(t−1) | ¿Superar la última oferta observada aporta más que sólo cerrar en verde? |
| B03 Inside tras corrección | Mother t−2 roja; t−1 inside estricta H(t−1)<H(t−2), L(t−1)>L(t−2); C(t−1)<C(t−3); C(t)>H(t−1) | Pausa posterior a pérdida neta y recuperación del rango corto. Sólo primera vela siguiente; no se conserva setup pendiente. |
| B04 Recuperación de mother | B03 y C(t)>H(t−2) | ¿Recuperar todo el rango de venta aporta más que superar su pausa interna? |
| B05 Barrido y recuperación | q=min(L(t−3),L(t−2),L(t−1)); L(t)<q y C(t)>q | Intento fallido de extender corrección; no atribuir absorción ni stops reales observados. |
| B06 Barrido confirmado | B05 y C(t)>H(t−1) | ¿El cambio de estructura mejora respecto a recuperar sólo el mínimo barrido? |

Igualdades no cuentan en comparaciones estrictas. Cada patrón sólo usa velas cerradas y se evalúa sobre t una vez; no retrospectivamente escoger el mínimo futuro. Las oportunidades se consumen si hay posición o no hay quote; no se encolan ni recuperan tras salir de otra operación. Eventos de velas diferentes son oportunidades distintas; una vela actual se registra una sola vez por receta. Estado actualizado incluso ocupado mediante before. La gestión alterará ocupación posterior; comparaciones de políticas no son causalidad sobre entradas idénticas.

## Presupuesto y decisión

Recomiendo techo de tres rondas, seis fulls por especialista en ronda1 (12 globales), no compromiso de gastar todo. Esta ronda contiene tres mecanismos y sus confirmaciones emparejadas. Ronda2 sólo hasta una línea defendible por especialista: atribución de componentes y estabilidad, seis contrastes como techo. Ronda3 bloques temporales emparejando candidata y referencia; si hay dos candidatas y misma base, tres bloques requieren nueve corridas únicas, no doce, techo global33 en lugar36. Los bloques reutilizan desarrollo; no llamarlos OOS.

Dos backtests simultáneos por especialista/cuatro globales cuando hay cola; un análisis propio/dos globales. Fallos o pendientes se informan; no completar recuentos con estimaciones.

No exigir que toda curva de tendencias permanezca positiva sin sus tres mejores trades: usar concentración como diagnóstico y comparar contra base. Exigir evidencia conjunta de mejora material, coste +5/+10bps, DD, capital-tiempo, contribución temporal y trayectoria distinta; N pequeño es inconcluso. Si ninguna línea ofrece evidencia suficiente tras ronda1, detener o reformular mecanismo antes de gastar ronda2. No escoger un máximo de +0,36USDT como progreso.2026 sigue cerrado; no se garantiza obtener ganadora.

## 1h queda reservado

No propongo1h en la ronda1: cambiaría simultáneamente driver, oportunidades y reloj de gestión. Si se aprueba posteriormente, necesita pareja4h/1h explícita. En1h, sólo consumir auxiliares4h con open+4h<=decisiontime, régimen/ATR4h de última vela completa y filtros de rango explícitos4h; nunca valores4h en formación. Cotización M1 exacta. Gestión original sólo en ticks correspondientes a cierre4h, también fuera del horario de entrada, con stops permanentes; deduplicar timestamp4h. Revisar warmup retenido y el origen del primer dato válido sin inventar velas. No imponer RTH ni usar1D filtrado por ventana intradía.

Ventana fija2020-10-15→2025-12-31exclusiva. Sin PAXG/BTC, datos nuevos, funding, instalaciones, research_scripts, framework, reinicios o live/paper/Pi. Todo por MCP. Esta propuesta no es autorización de ejecución y puede afinarse antes de congelar fuentes.

## Ronda1 autorizada: protocolo congelado de ejecución

El usuario autorizó ejecutar seis B01..B06. Las otras rondas siguen sin autorización; ningún resultado observado al congelar este protocolo.
Nombres: SpyStructR1PB01, SpyStructR1PB02, SpyStructR1PB03, SpyStructR1PB04, SpyStructR1PB05, SpyStructR1PB06.
Se mantienen EXACTOS los seis patrones propuestos arriba. Base de ejecución actual AttrSpyMarket. Referencia económica [Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) y comparador de mismo tipo de entrada [MARKET](http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07), existentes; no nuevas réplicas.
No atribuir diferencia frente Cq sólo al patrón, pues además cambia orden. MARKET sirve de comparación controlada del tipo de orden, aunque señales/ocupación/gestión anclada a entry siguen distintas.

Diferencias concretas con antecedentes:
- R20 gap/inventory dependía de sesionesRTH, gaps o retorno de día cash; B01/02 sólo usan dos velas4h rojas y recuperación inmediata dentro de régimen original, sin diarioRTH, gap, target/horizonte nuevo.
- R40RepeatedBarrierPressure pedía dos tests de barrera10B, retiro decreciente, episodio12B y ruptura POSTERIOR de techo/suelo, ambos sentidos y gestión fija120h. B03/04 exigen insideestricta tras motherroja, pérdida neta desde antes de mother y cierre inmediato sobre su máximo; una señal local, sólo long, originaltrailing. Parentesco compresión admitido; no réplica del protocolo anterior.
- R40OccupationFlip usaba conteos de13closes30m respecto de aperturaRTH y rechazo al final; B05/06 usan mínimo de3velas4h y lowactual que lo barre y recupera en misma vela. No cuentan ocupación intradía, no operan short ni representan absorción observada.
- R20CashGapFade y R40CloseDensity eran reversión hacia referencia/target fijo; sweepB05/06 es recuperación local dentro de tendencia con gestión runner original.
Ninguna es una fuente independiente garantizada. Es investigación adicional sobre desarrollo seleccionado.

Invariantes de motor: todas autocontenidas; señales estateless por vela t y cache _signal por index, sin before necesario al no existir setup que sobreviva. Evento ocupado/noquote no se almacena. Más adelante puede aparecer otro evento propio, nunca reproducción del anterior. Semántica de velas consecutivas es consecutivas RETENIDAS del calendario; pueden estar separadas por noche o fin de semana, como historia original; no inventar continuidad temporal.
Gestión, riesgo, horarios y helperfresh son copias exactas de base. Se conserva rama BTC inactiva heredada, sin ruta/datos/operación BTC. donchian_len sigue en hyperparameters y guard100 por copia, pero NO interviene en nuevo evento ni entry; no optimizarlo. Restricción símbolo se conserva por mínima diferencia; ruta únicaSPY.
La validez histórica de OHLC se comprueba finita en patrón, sin tratarla como quote ni fabricar data. Mercado= self.price exacto. Distancia sólo contra entrada actual: la fronteraDonchian eliminada no participa.

Cola PB01/PB02,PB03/PB04,PB05/PB06; hasta2simultáneas,4globales, llenar slots listos. Leer formularios antes de run y snapshotsdespués. Ningún run hasta revisión root.
Análisis8inputs con seis nuevas y dosreferencias; métricas exactas y conciliación completa, +5/+10bpsRTestáticos conservandoqty/fills, exposición horaria, nocionaldeentrada-tiempo etiquetado sin afirmarMTM, concentración y cohortes por cierre. Root hará MTM; no duplicarlo.
