# V3 CHANNEL — cribado de sector completado
Fecha:2026-10-20. Estado: SCREENING_SECTOR_COMPLETE_AWAIT_ROOT_GATE.
Se completaron dos sesiones continuas de desarrollo [2020-09-01,2024-01-01), sin modificar fuentes, reglas, datasets o configuración entre P y POI. Cada sesión inició plana con10.000USDT y transportó su capital dentro de esos40meses. No son folds reseteados ni muestra de confirmación.
Un motor de este sector por vez, compartiendo presupuesto global con otro sector. Token liberado; no nuevas ejecuciones CHANNEL hasta siguiente GO root.

## Resultados nominales
| Variante/sesión | N | Neto % | PF | DD motor % | Duración motor s |
|---|---:|---:|---:|---:|---:|
| [CHANNEL_P](http://localhost:9200/#/backtest/05828944-d350-4852-b13d-af24c2815bc5) | 150 | 36.78 | 1.222410 | -23.62 | 30.61 |
| [CHANNEL_POI](http://localhost:9200/#/backtest/eb4ea7d5-dc0c-4f08-9450-1584f49cdfe0) | 127 | 50.78 | 1.337217 | -22.72 | 29.52 |

Fee0,00045/lado,slippage0,isolated3x,capnotionalC,riesgo2%stop+fees,contabilidadfundingON. OI histórico configurado en ambas, pero gate sóloPOI. Stop2ATR14, trailing3ATR14 sinTP, máximo7d; entradas por canal20/SMA120/pediente24h. Son mecanismos idénticos con ablación OI24h.
Ambas superan los cuatro umbrales simples de screening (N>=30,neto>0,PF>=1,2,DDmotor<=25). La elegibilidad completa además requiere al menos dos años completos2021/2022/2023 positivos por equity; esa comprobación y la conciliación central pertenecen a root. Este informe no anticipa shortlist ni ranking global antes de las seis configuraciones.
Un resultado nominal positivo no acredita robustez de fricción ni la meta anual. No anualizar el mejor año ni usar el neto40meses como anual.

## Auditoría de ejecución y contadores
Cada sesión contiene7.302decisiones4h en40meses. Hay142buckets observados, frente al máximo160posibles: ciertas direcciones no generaron eventos en algunosmeses. No se fabrican18buckets vacíos.
Para cada bucket se verificó partición exclusiva sum(primary)=bars yallowed=entries; para cada mes, sumas deall concilian conlong/short/none.
P:150entradas=150cierres antes de auditoría, sin cierre forzado posterior.
POI:127entradas=127cierres antes de auditoría, sin cierre forzado posterior.
POI rechazos exclusivos: inicialización2 yOI no creciente48. Sus oportunidades no son el mismo conjunto queP porque cambian ocupación y entradas posteriores; no atribuir diferencias a filtro puro entre trades idénticos.
No aparecen flags atr_invalid/features_invalid/trailing_data_invalid ni rechazo de distancia/qty en las oportunidades registradas. Los costos y trayectoria completa se concilian vía snapshots por root; no desde páginas parciales ni desde esta cola de logs.
Archivos: AUDIT_ResearchV3ChannelP4h_SCREEN.json y AUDIT_ResearchV3ChannelOi4h_SCREEN.json. Incluyen todos los buckets y procedencia desde cola MCP suficiente, no todos los logs históricos de gestión.
El smoke previo validó47checks de sector+28base, diezratchets y cierre forzado. Este lote no cambió implementación según resultados.

## Procedencia, límites y próximos pasos
Fuentes/hashes congelados en V3_IMPLEMENTATION_SOURCE_20261020.md yREGISTRY_V3.json. Fuentes locales de sector/progreso exclusivo enV3_CHANNEL_PROGRESS.json; base y dependenciasV2/V1 no modificadas.
Los dos run_backtest devolvieronstatusstarted; respuestas rawcompletas conservadas. No timeout en estos dos arranques, no retry ni duplicados. Ambos resultados finished sinerror.
OI sigue retrospectivo sinPITcertificado y funding con marcasproxy; nominal sin slippage ni liquidez/latencia real. Las ventanas2020–2023 ya se observaron en investigación previa. No usar este screening como prueba independiente.
Root comparará las seis configuraciones con gates anuales, conciliación completa, DDmuestreado terminal diagnóstico y criterios globales, sin cambiarDDmotor prerregistrado. Sólo tras shortlist congelada se abre confirmación2024–2025;2026 permanece cerrado.
No run_analysis propio, screening extra, tuning, ML, RST, cuentas, Pi, live/paper, instalación, reinicio, commit o push.
