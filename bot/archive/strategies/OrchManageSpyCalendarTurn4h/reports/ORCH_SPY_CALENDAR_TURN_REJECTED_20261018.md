# SPY: adaptación de cambio de mes — receta descartada
Dashboard: http://localhost:9200/#/backtest/2f510e3e-6563-4002-b96a-ef2bbd38e52d

## Protocolo y alcance
ORCH_SPY_CALENDAR_TURN_PROTOCOL_20261018.md se guardó antes del run. Una receta: long durante los últimos cuatro días de calendario y los cuatro primeros del mes siguiente, con decisiones16UTC y cotizaciónM1propia fresca. No es una réplica de la regla académica basada en días bursátiles/cierresNYSE, ni demuestra causalidad de aportes.
SPY-USDT4h + ruta de datos1m; proxy SPXCFDBID/10. Capital10k,5xaislado,risk3%/8%,cap1x,sizingrealaprox0.94x,stop3%desdeactualfill,fee0.00045porlado. SinTP/trailing/indicadores/filtros de tendencia. Una entrada por turno ysinreentrada tras stop.
Ventana2020-10-15→2025-12-31exclusivo,normal,warmup240.2026reservado. Sin nuevos datos, paquetes, framework ni configuración global.

## Resultado
62longs,29ganadores/33perdedores,neto−536.820945USDT, saldo9463.179055, CAGR−1.052722%, DDmotor−16.829365%, Sharpe−0.123227. Fees517.561727USDT y PnLantesdefees−19.259218USDT. No existe ventaja bruta que las comisiones estén ocultando en esta receta.
Holding mediano8d.11salidasSTOP y51MARKET; fuente conservada exactamente.

## Auditoría de ejecución y calendario
Análisis MCP36de31bf0af74cf3830ffab962984839 validó:
- Entradas en16UTC,hábilesMon–Fri,dentro de los últimos4d de calendario.
- Turnos únicos, sin reentrada.
- SalidasMARKET discrecionales posteriores al día4 del mes siguiente, a16UTC.
- Comisiones, PnL de trades y saldo final.
Un turno etiquetado2023-03 carece de entrada observada. No se atribuye su causa exacta a un hueco específico sin registros adicionales de cotización/estado; no se inventa una entrada pasada.

El V4 independiente del orquestador pasó fills/fees/wallet y la condición del contador previo a terminación:
-30/63mesesactivospositivos=47.6190%.
-30/63mesescalendario=47.6190%.
-9/21trimestrespositivos=42.8571%.
-Períodoscompletos:29/61meses=47.5410%;7/19trimestres=36.8421%.
-Peormes−4.22085%;drawdowncierrediarioUTC−16.79164%.
La pérdida mensual puede superar el riesgo por operación porque un mes puede contener salidas/entradas de turnos distintos. No confundir stop3%portrade con capmensual3%.

## Terminación sintética y liquidez
La última operaciónSPY abre2025-12-29a16UTC y cierra sintéticamente2025-12-31a00UTC. Su PnLbruto−7.1026737 explica exactamente open_pl previo a terminación y el contador total_open_trades=1. La salida completaMARKET registrada tiene fees8.02242866 y neto−15.12510236; todos los trades y wallet reconcilian.
Esto es convención de valoración de fin de muestra, NO evidencia de una cotización fresca ejecutable a00UTC. No se adelantó la salida mirando el final del backtest, no se modificó el framework ni se consultó2026.

## Años y costes
PnL por fecha de cierre (NO retornosMTM):
2020+749.56;2021−718.42;2022−869.50;2023+1022.36;2024−538.00;2025−182.83USDT.
Retornos anualesMTM V4:
2020parcial+7.9535%;2021−7.5707%;2022−7.4186%;2023+9.7216%;2024−4.9883%;2025parcial−1.7353%.
Fixedfills/cantidades con+10bpsRT adicionales dejan neto−1111.889530USDT. Diagnóstico aritmético, NO nuevoCAGR/DD ni modelo completo de spread/funding.

## Decisión
DESCARTAR esta adaptación4/4calendario/16UTC. No cumple rentabilidad neta ni objetivos65–70%mesesactivos/80%trimestres, y no se combina con referencia.
No ajustar ventanas, weekdays, meses ni stop después del resultado. No afirmar que el paper clásico sea falso: instrumento, horario, calendario y costes son distintos.
Referencias primarias e hipótesis figuran en el protocolo. Su evidencia histórica no garantizaba que esta implementación concreta tuviera una ventaja. Fuente y resultado negativo quedan registrados; referencia y2026intactos.
