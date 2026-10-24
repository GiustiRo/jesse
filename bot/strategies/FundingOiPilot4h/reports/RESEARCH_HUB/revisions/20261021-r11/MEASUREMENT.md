# Medición de equity y regularidad desde la tanda C
Fecha:2026-10-21. Implementación local en nuevas estrategias, sin cambios del framework.

## Resolución y reloj
La ruta operativa es1m y la ruta de datos para señales es4h. El helper sólo consume velas4h cerradas y consecutivas; las decisiones de entrada y gestión siguen en cierres4h. El observador no agrega nuevas decisiones de trading.

En cada minuto se mide equity BTC como wallet+position.pnl. En este checkout portfolio_value multiplica el PnL abierto por leverage, por lo que no se usa para la observación. En R10 se usaba para sizing estando plano: esa diferencia no invalida sus entradas.

Se incorporan muestras en apertura/cierre para capturar comisiones que ocurren después de before/after. El DD es el de muestras M1 más eventos de ejecución; no se presenta como máximo de todos los ticks o extremos intraminuto.

## Fronteras mensuales
Se guarda equity a las00:00UTC después del funding efectivo de esa frontera y antes de las decisiones nuevas. Es una convención por fase: el funding a00:00 queda en el intervalo que acaba. No se afirma que sea la suma de eventos agrupados por fecha en meses estrictamente[inicio,fin).

Al finalizar la ventana, no se paga funding del finish exclusivo. El cierre final del motor incluye comisión de liquidación; si ocurre después del primer resumen, on_close actualiza equity terminal y emite FINAL, que prevalece sobre PRETERMINAL.

Se conserva actividad por exposición y ejecución. En una frontera de mes, un cierre marca de forma conservadora tanto el mes previo de exposición como el mes de ejecución/posible fee; el cierre terminal no activa un mes fuera de ventana. No deducir actividad de PnL distinto de cero.

## Integridad y evaluación
Por cada prueba2020-10-15→2026-01-01 se esperan2.741.760marcas M1,63intervalos mensuales,62mesescompletos y20trimestrescompletos. Los intervalos parciales se informan aparte. Se verifican continuidad de fronteras, unicidad de meses, equity final y telescopía de contribuciones mensuales contra saldo final.

Las filas mensuales se emiten juntas al finalizar, junto a un resumen. Se recupera todo ese bloque y se conserva el recibo, aunque no se soliciten los logs de trading anteriores. No calcular totales de trades desde esa página: la auditoría financiera usa snapshots completos mediante run_analysis.

La tanda C obtuvo exactamente esa cobertura en ambas pruebas, sin ventanas de señal inválidas. DD M1:19,27% CUSUM y13,53% absorción, frente a DD diarios18,85% y12,03%. La mayor resolución no se usa para relajar objetivos; ambas recetas ya incumplen puertas económicas.

## Versiones y límites
Fuente final BtcResearchR11Base1m SHA256 be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87; helpers R10 congelados, sin modificar sus resultados. Checks sintéticos y revisión separada precedieron a ejecuciones. No es validación de ticks, mercado real, slippage, impacto, liquidación de margen de venue ni derechos de datos.

Funding histórico incluye marcas proxy previamente declaradas y aplica sus pagos a la cantidad real simulada. No se modifica silenciosamente el dataset. Estas limitaciones acompañarán a cualquier candidata preliminar; el estrés sigue diferido hasta un acuerdo específico.
