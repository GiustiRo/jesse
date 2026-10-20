# R60: veinte contrastes SPY/PAXG fijados antes de resultados

Fecha local: 19 de octubre de 2026. Usuario autoriza diez configuraciones por activo en paralelo. Exactamente 20 nuevos fulls; las referencias existentes no se vuelven a contar como nuevas exploraciones.

## PAXG: cinco pares de políticas, diez fulls

Bases: AttrPaxgCqFreshRetest4h y AttrPaxgMMarketSignal4h. Cada contexto se ejecuta con ambas políticas. Se cambia una sola pieza frente a cada base:

| Contexto | Parámetro alterado | Retest | MARKET |
|---|---|---|---|
| P1 | Donchian 24 en vez de 26 | 1 full | 1 full |
| P2 | Donchian 28 en vez de 26 | 1 full | 1 full |
| P3 | ADX mínimo 24 en vez de 26 | 1 full | 1 full |
| P4 | ADX mínimo 28 en vez de 26 | 1 full | 1 full |
| P5 | EMA rápida 24 en vez de 20 | 1 full | 1 full |

Los cuatro primeros contextos amplían el plan de estabilidad local anterior. P5 completa la petición de diez configuraciones con una perturbación de +20% de la media rápida, fijada antes de resultados y aplicada por igual a las dos políticas. No se escoge a partir de un vecino ganador. Cada pareja conserva filtros, quote guard, stop 2 ATR, BE 2,25R, trailing 4,2 y tightening originales. M valida distancia contra frontera original antes de sustituir el precio por el cierre y recalcular sizing.

Referencias: [Cq](http://localhost:9200/#/backtest/0fc6e1f7-66ea-4587-884a-ef616ecbfbc1) y [M](http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae). No se usan cinco pares como observaciones IID ni como OOS limpio. Se evalúa la estabilidad del signo y magnitud de MARKET−retest a lo largo del conjunto, con DD/exposición/costes y concentración. No seleccionar el mejor vecino como confirmación.

## SPY: diez perturbaciones individuales

Base: AttrSpyCqFreshLimit. Definir g=(close−máxima Donchian previa)/ATR. La base exige 0<g<=1. Sólo cambia la pieza indicada por fila:

| Control | Cambio único |
|---|---|
| S01 | 0,10<g<=1 |
| S02 | 0,25<g<=1 |
| S03 | 0<g<=0,50 |
| S04 | 0<g<=0,75 |
| S05 | Donchian 24 en vez de 26 |
| S06 | Donchian 28 en vez de 26 |
| S07 | ADX mínimo 24 en vez de 26 |
| S08 | ADX mínimo 28 en vez de 26 |
| S09 | EMA rápida 16 en vez de 20 |
| S10 | EMA rápida 24 en vez de 20 |

Las primeras seis estaban propuestas en el handoff anterior. Las cuatro añadidas completan diez con perturbaciones simétricas de umbral ADX y velocidad de la media rápida. No se combina el mejor intervalo con el mejor parámetro. Las fracciones de ATR son partes redondas del intervalo original, no se estiman de operaciones favorables.

Referencia: [SPY Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639). Se conservan precio a frontera, vigencia de orden de una barra, sizing, gestión y calendario. Smart-order del motor puede convertir a MARKET precios dentro de 1,5 bps del actual; no se modifica esa semántica ni se promete LIMIT pura.

## Invariantes, ejecución y revisión

Ventana 2020-10-15 a 2025-12-31 exclusiva, último día de datos 2025-12-30. 2026 cerrado. Capital 10.000 USDT aislado por full; riesgo planificado 1%, fee 0,00045 por lado en todos los tipos, isolated 5x, cap nocional 4,4, sin piramidado. Reserva 0,001 sólo sizing, no fricción simulada. Una ruta 4h y data route M1 del mismo activo, warmup240, fast/debug false. SPY conserva exactamente UTC Mon–Fri00–20 para historia y barras abiertas00–16 para entradas. PAXG sin ventana.

Los proxies existentes SPX CFD BID/10 y spot PAXG están aceptados para investigación de precio; no se añade funding ni histórico. Sin instalaciones, cambios de framework/config global, BTC, scripts de investigación, reinicios o sesiones live/paper/Pi.

Dos especialistas autorizados, dos backtests y un análisis simultáneo por especialista; cuatro backtests y dos análisis globales. Uso de MCP para toda operación del proyecto. Fuentes autocontenidas, nombres nuevos, snapshots completos en las sesiones. Root revisa fuentes/readback/diffs antes de liberar las colas. No se alteran tras resultados.

Se reutilizan las referencias recién reproducidas: no hay otro full de paridad dentro de los veinte. Si se detecta cambio del motor, datos o referencia que invalide comparabilidad, se investiga antes de continuar y se declara cualquier prueba adicional.

## Evaluación sin escoger el máximo

Informar todas las filas, incluidos negativos y sin operaciones. N, neto y antes de fees, fees, PF, Sharpe, CAGR/DD motor, duración, tiempo abierto, nocional-tiempo a precio de entrada, rotación y neto por nocional. Recargos estáticos de 5/10 bps RT (mitad cada lado) mantienen fills/tamaños: no representan nuevos backtests con impacto. Excluir mejor operación/tres mayores PnL como concentración descriptiva, no veto universal a seguidores de tendencia.

Cohortes por año de cierre se etiquetan como tales, sin presentarlas como retornos MTM. Root reconstruirá dayclose UTC con auditor validado y cuatro snapshots de anclaje; 61 meses y 19 trimestres completos más fronteras parciales aparte. Cierres terminales concilian con wallet/open_pl; no prueban liquidez nativa. Snapshots ejecutados se cotejan contra fuentes revisadas.

Comparaciones de entrada/salida cambian ocupación y tamaño posteriores. Pares de fills o created_at exactos, cuando se muestren, son intersecciones seleccionadas y no un efecto causal puro. No ajustar exposición retrospectivamente para favorecer una variante.

Toda la historia 2020–2025 ya es desarrollo reutilizado. Vecinos estables mejoran el diagnóstico de fragilidad, no borran selección previa ni prueban ausencia de sobreajuste. No abrir2026, integrar cartera o promover por el mayor neto de esta tabla. Conservar cronología R20/R40/atribución y esta ronda.
