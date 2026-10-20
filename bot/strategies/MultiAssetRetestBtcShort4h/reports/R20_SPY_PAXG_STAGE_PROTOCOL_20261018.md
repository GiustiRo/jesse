# Nueva tanda: veinte exploraciones SPY/PAXG

Fecha local: 18 de octubre de 2026. Autorización humana: diez exploraciones nuevas para SPY y diez para PAXG, manteniendo el foco en esos activos hasta mejorar su operativa. Se reutilizan los dos agentes especialistas y se conserva la coordinación de root.

## Qué cuenta como exploración
Veinte experimentos primarios, con IDs SPY20-01 a SPY20-10 y PAXG20-01 a PAXG20-10. Cada uno debe fijar mecanismo, regla de entrada y salida, reloj causal, sizing, contraste y diferencia respecto del historial. Una variación de umbral, horario o indicador que sólo intenta rescatar un resultado anterior no cuenta como idea nueva. Las familias generales pueden compartir rasgos; no se afirma independencia económica ni estadística entre los veinte tests.

Cada agente guardará su matriz de diez recetas antes de observar los resultados de la tanda. Root revisará novedad, factibilidad y causalidad antes de lanzar. Se registrarán descartes de diseño; si un duplicado se retira antes de correr, se sustituye antes de fijar la matriz definitiva. No cambiar recetas tras sus resultados. Un arreglo técnico se registra por separado y no autoriza modificar alpha.

Los controles adicionales, sensibilidades e integraciones de una candidata prometedora se registrarán como tales; no rellenan artificialmente el cupo de veinte ideas. Root decidirá su utilidad después del cribado y fijará el protocolo antes de observar esos resultados.

## Contrato común
- Históricos existentes aceptados por el usuario: SPX CFD BID/10 como proxy SPY y spot PAXG como proxy perpetual. Investigación de precio; sin volumen ficticio, funding o datos externos nuevos.
- Desarrollo 2020-10-15 a 2025-12-31 exclusiva. 2026 reservado y sin consultar. Todo el historial de desarrollo tiene selección acumulada; no se reinicia el contador ni se lo presenta como OOS limpio.
- Capital aislado 10.000 USDT, riesgo planificado fijo del 1% por trade, fee 0,00045 por lado para todas las órdenes, 5x aislado, techo nocional bruto 4,4x y sin piramidado. Reserva de sizing no es slippage aplicado.
- Hasta dos backtests por agente y cuatro globales; hasta un análisis por agente y dos globales. No fuentes nuevas, scripts de investigación, instalaciones, framework, reinicios, live/paper, Pi, fondos o cambios de configuración global.
- Toda estrategia y reporte mediante Jesse MCP. Análisis de sesiones con run_analysis y snapshots completos. No fallbacks por shell, FS, SQL o red ante fallos del MCP.

## Comparación y evidencia
Controles existentes: SPY retest aislado1% (23c4974f-7503-4afe-8ffa-f69eb78c5ef2), PAXG retest aislado1% (93a16137-e819-41a3-b325-0631a6627a6c) y PAXG fin de semana0,75 aislado1% (ff199ebe-dab0-4c09-9078-fff98188e97c). Son comparadores de políticas con distinta exposición, no controles aleatorizados. No es necesario repetirlos sin causa.

Cribado descriptivo inicial: neto positivo, PF al menos1,2, muestra de unas30 operaciones y DD no peor que25%. Una muestra menor es evidencia insuficiente, no demostración de ausencia de efecto. Los criterios no certifican por sí solos robustez. Documentar cohortes y MTM por períodos, concentración, exposición y sensibilidad de5/10bps RT sobre mismos fills. No ocultar estrategias que sólo ganan en un año ni seleccionar retrospectivamente direcciones.

Una mejora defendible requiere valorar conjuntamente retorno, drawdown, costes, capital-tiempo y regularidad: no basta el mejor neto de veinte pruebas ni una métrica aislada. Los objetivos mensuales/trimestrales pertenecen a la cartera. Root revisará el frente de alternativas y el mecanismo antes de seleccionar candidatas para sensibilidad o cuenta compartida, dejando explícita esa selección adaptativa.

BTC y referencia original permanecen congelados. La referencia de cartera actual conserva CAGR28,83%, DD14,89%,33/61 meses activos positivos y15/21 trimestres. La cartera experimental PAXG0,75 anterior tiene27,55%,DD12,36%,35/61 y14/21: se mantiene como comparación, no reemplazo aceptado. No sumar curvas aisladas para representar cuenta compartida.

## Entregables y finalización
Matriz predeclarada por activo; veinte recetas y resultados terminales; diagnósticos de todas las pruebas, incluidas pérdidas; auditorías de fills/fees/wallet y MTM cuando se informe regularidad; informes finales por activo y consolidado con selección acumulada. Si aparece una candidata, contrastar mejoras de ejecución y cuenta compartida antes de aceptarla como mejora operativa. Si no aparece, informar esa evidencia sin garantizar que más intentos producirán una estrategia. No se rebajan metas para declarar éxito y no se abre2026 durante esta tanda.
