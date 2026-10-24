# SPY apertura cash — ronda 0 cerrada
Desarrollo adaptativo 2020-10-15 → 2025-12-31 exclusivo. Referencia de cartera y 2026 intactos. Protocolo previo SPY_OPENING_AUCTION_PROTOCOL_20261018.md y notas de implementación en esta carpeta. Tres fulls nuevos terminados, una hipótesis de apertura con contraste de política fijo y control contextual. No optimización.

| Política | Trades | Neto USDT | Fees USDT | Precio antes de fees | CAGR motor | DD motor | PF |
|---|---:|---:|---:|---:|---:|---:|---:|
|[Referencia SPY aislada 1%](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2)|31|751.35|286.48|1037.82|1.399%|−5.213%|1.493|
|[Ruptura rango primera hora](http://localhost:9200/#/backtest/a68dbfa8-3efe-410a-9c8b-861bf3609f38)|890|−6273.02|7559.20|1286.19|−17.247%|−63.748%|0.661|
|[Impulso primera hora](http://localhost:9200/#/backtest/98918ea4-78a2-4548-8f23-8c7459d07a30)|1162|−8700.06|9569.47|869.41|−32.384%|−87.217%|0.613|

Riesgo planificado 1% por operación, 10k inicial, 5x isolated, techo bruto 4.4x, comisión .00045 por lado, reserva .001 sólo sizing. El proxy de precio SPX CFD BID/10 es el aceptado por el usuario. Funding fuera de esta etapa.

## Decisión y mecanismo
Archivar AMBAS políticas de apertura probadas. No seleccionar sólo longs, mover horarios, reducir stop o aumentar riesgo para rescatar. Antes de fees el beneficio equivale aproximadamente a 1.53 bps por nocional inicial en ORB y 0.82 bps en Drive; no sostiene los aproximadamente 9 bps modelados por vuelta. Esto no rechaza toda continuación intradía ni demuestra ausencia de prima bruta; sí rechaza estas recetas netas al coste vigente.

Longs y shorts pierden: ORB −3462.12 / −2810.90 USDT; Drive −3911.51 / −4788.55. Neto por nocional agregado de entrada: referencia 23.643 bps, ORB −7.469 bps, Drive −8.183 bps. Son cocientes de fills, no retornos de cartera.

Recargo estático +5 / +10 bps roundtrip, medio recargo en cada lado sobre nocionales realmente ejecutados: referencia +592.19 / +433.04; ORB −10472.57 / −14672.13; Drive −14016.43 / −19332.81 USDT. No son nuevos backtests dinámicos ni CAGR/DD bajo slippage; tamaños y decisiones quedan fijos.

Referencia depende de runners: top5 suman1508.88, neto excluyéndolos−757.54. Descriptivo de concentración, no criterio automático para quitar ganancias de una tendencia.

## Auditoría efectuada
Todos los snapshots completos concilian PNL = precio×cantidad menos fees, suma de fees con métrica y fee .00045 por entrada/salida. Todas las entradas H1 en NY11:00(563),11:30(221),12:00(106); C1 NY10:30(1162). Cero fechas de entrada duplicadas y sólo días hábiles NY. ZoneInfo y schedule mantienen DST; primera hora requiere60M1 contiguas y dos30m presentes. Esto verifica datos disponibles a la estrategia, no ausencia de relleno upstream.

Ocho trades de CADA política cruzan medianoche UTC: cierres tempranos y huecos activaron deuda de salida. No se inventa salida15:30 cuando falta quote. Hay otros cierres tardíos sin cruzar medianoche. La estrategia no tiene calendario festivo NYSE completo. No llamar a estas políticas siempre flat overnight.

Curva motor muestreada alrededor00:01; no usarla como cierres diarios UTC. Primer intento de auditoría04562648d83a4f3c82d584e84e9f88a8 falló justamente aserción de flat diario, sin producir regularidad válida. Análisis reparado0c056e6b2f6a4fe3a86cf6253e117550 succeeded, dejó explícitos8cruces y omitió MTM cash inválido. El archivo temporal spy_equity.png de ese job sólo dibujó referencia: NO usar como comparación ni evidencia de MTM. Root ejecuta reconstrucción V4 unificada y reportará años/meses con anclas correctas.

## Persistencia
Fuente en ResearchSpyReference4h, ResearchSpyOpeningRange60 y ResearchSpyOpeningDrive60; snapshots completos de código en notas de cada sesión. Análisis inicial de estructura749cd97e74864c059540f568b061a140 succeeded; auditoría completa reparada0c056e6b2f6a4fe3a86cf6253e117550 succeeded. JSON temporal spy_summary.json incluye estadísticas, horarios y cruces; sus números principales están persistidos aquí. No scripts nuevos, framework, instalaciones, live/paper, descargas ni 2026.

La ronda siguiente autorizada por root estudia exposición SPY lenta frente a un control beta protegido. Es otra pregunta económica y tiene protocolo previo separado; no rescate de horarios de apertura.