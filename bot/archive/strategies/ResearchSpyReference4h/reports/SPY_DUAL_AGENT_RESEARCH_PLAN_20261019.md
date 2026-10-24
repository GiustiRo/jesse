# Plan SPY con dos especialistas: hasta 33 backtests

Fecha local: 19 de octubre de 2026. Estado: propuesta de investigación preparada; sin nuevas estrategias ni backtests ejecutados en esta etapa de planificación.

El usuario pide continuar con el especialista SPY existente y crear otro para SPY. Se mantiene /root/spy_research y se creó /root/spy_pullback. El trabajo se concentra en SPY. Cada especialista mantendrá dos backtests simultáneos mientras tenga cola, cuatro globales; máximo un análisis por especialista y dos globales.

## Presupuesto y avance condicionado

| Ronda | Propósito | Backtests nuevos máximos |
|---|---|---:|
| 1 | Tres pares estructurales por especialista, seis configuraciones cada uno | 12 |
| 2 | Atribución y estabilidad de hasta una línea defendible por especialista | 12 |
| 3 | Tres bloques temporales, una referencia común y hasta dos candidatas por bloque | 9 |
| Total | Techo de corridas únicas, sin duplicar referencias compartidas | 33 |

No es obligación consumir las 33. Una máxima marginal, un único runner o una muestra pequeña no justifican desarrollar una idea por completar una cuota. Si no hay una línea defendible en ronda 1, se revisa el mecanismo antes de gastar ronda 2. Una variante prometedora se analiza junto con todos sus descartes.

## Especialista A: ruptura, episodio y retest

Continuar con el agente existente. Estructuras propuestas para seis fulls en tres pares:

1. Primera ruptura calificante de un episodio frente a rupturas posteriores del mismo tramo. La propuesta define nuevo episodio tras cierre en la mitad inferior del canal26; el estado debe evolucionar aun estando ocupado.
2. Primer retest del techo congelado que cierra encima frente a primer retest que cierra debajo y recuperación posterior. Ambos ejecutan MARKET tras confirmación.
3. Sobre el mismo evento de retest confirmado del punto anterior, STOP en máximo de vela de retest frente a STOP en máximo de ruptura original. Si el umbral ya está superado al decidir, el contrato debe especificar ejecución al precio actual y evitar convertirlo accidentalmente en LIMIT.

La propuesta de trabajo contempla hasta cuatro barras4h filtradas para esperar el retest, nivel de ruptura congelado y vigencia posterior de órdenes de una barra como en la referencia. Antes de código se fijarán exactamente inicialización de estado, resets, definición de toque observable, vencimiento y prioridad de eventos. No se retrofecha un fill ni se cuentan señales ocupadas como entradas hipotéticas.

Se conserva gestión/riesgo original. Las referencias Cq y M existentes dan contexto. Las secuencias de señal y la ocupación difieren, por lo que sus pares no representan una intervención causal sobre entradas idénticas.

## Especialista B: corrección y recuperación sin exigir Donchian

Nuevo agente /root/spy_pullback. Seis fulls en tres pares, con ejecución MARKET constante:

1. Dos velas bajistas con cierres descendentes seguidas de recuperación alcista del cierre previo; su pareja exige además superar el máximo previo.
2. Inside bar posterior a corrección, recuperación de su máximo; su pareja exige recuperar también el máximo de la vela madre.
3. Barrido del mínimo de las tres velas anteriores y cierre de vuelta por encima; su pareja exige además superar el máximo previo.

Se conserva régimen EMA20/80, pendiente EMA80, ADX26, RSI52–76 y filtro de rango, ATR4h y gestión originales. Se sustituye la condición Donchian/desplazamiento por el patrón. Se usan únicamente velas cerradas y quote M1 exacta.

El contraste incluye AttrSpyMarket como referencia de ejecución y Cq como referencia económica principal. No atribuir diferencias de MARKET frente a LIMIT exclusivamente al patrón. Dentro de cada par sí se mantiene constante la modalidad de ejecución.

Estas familias tienen antecedentes en investigación de precio. La novedad defendible es el contraste específico de confirmación estructural bajo reglas comunes. Antes de ejecutar, contrastar las reglas completas con R20/R40 y sustituir duplicados exactos; no presentar una receta renombrada como descubrimiento nuevo.

Propuesta técnica preservada en strategies/ResearchSpyReference4h/reports/SPY_PULLBACK_PLAN_PROPOSAL_20261019.md.

## Ronda 2: desarrollar sin mezclar todos los ganadores

Hasta seis contrastes por especialista y una línea seleccionada por una razón explicable. Retirar componentes, comprobar perturbaciones cercanas y atribuir si aporta la señal, la confirmación o el precio de entrada. No combinar automáticamente el mejor parámetro de cada prueba.

La temporización1h con régimen4h puede entrar aquí si existe una hipótesis defendible. Requiere control explícito del driver, sólo barras auxiliares4h completamente cerradas (open+4h<=decisiontime), ATR4h, filtros de rango declarados y gestión original al cierre4h. No introducir simultáneamente otra lógica de salida.

Costes adicionales, concentración y análisis temporal acompañan cada comparación. Los recargos estáticos no se cuentan como nuevos backtests ni como ejecución dinámica con spread/impacto.

## Ronda 3: contraste temporal de reglas congeladas

Hasta dos candidatas fijas y tres bloques cronológicos fijados antes de ejecutar. Una referencia y dos candidatas por bloque son nueve corridas únicas. No duplicar la misma referencia por agente para llegar a doce.

Comparar costes, DD, exposición, muestra, concentración y contribución por calendario. Si sólo queda una candidata se reduce el presupuesto. No reoptimizar en cada bloque ni llamarlos validación independiente: 2020–2025 ya fue utilizado como desarrollo.

Las fechas exactas de bloques y los contratos de ejecución de cada ronda quedarán fijados antes de sus resultados. 2026 permanece cerrado en todo este plan.

## Condiciones comunes y criterios

Capital aislado10.000USDT, riesgo planificado1%, fee0,00045 por lado, isolated5x, cap4,4, reserva0,001 sólo sizing; gestión original stop2ATR/BE2,25R/trailing4,2 con tightening. Se empieza en4h con datosM1 existentes y calendario SPY original UTC Mon–Fri00–20 para historia y barras abiertas00–16 para entradas. Sin imponer RTH.

Preservar proxies aceptados, datos, riesgo y costes. Sin funding, nuevo histórico, PAXG/BTC, instalaciones, scripts de investigación, framework, reinicios o live/paper/Pi. Todo el proyecto mediante MCP y fuentes autocontenidas con revisión y snapshots.

La mejora se juzga por retorno después de costes, DD, exposición, muestra y repetibilidad temporal en conjunto. La frecuencia por sí misma no es objetivo. Concentración en pocos runners es diagnóstico; no un descarte automático. Una modificación de pocos centavos no justifica sustituir la referencia.

Este documento responde al presupuesto y direcciones solicitados. La ronda 1 necesita su matriz técnica final y fuentes revisadas antes de lanzar; no hay corridas nuevas en segundo plano.
