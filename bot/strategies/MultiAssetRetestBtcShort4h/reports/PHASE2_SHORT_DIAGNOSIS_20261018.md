# Diagnóstico de shorts y explicación de métricas
[Referencia congelada](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb). LongsBTC/PAXG/SPY,shortsBTC. Reglas,objetivos65–70%mesesactivos/80%trimestres y2026reservado se mantienen.

## Winrate y tiempo
Winning Avg Holding Time: duración cronológica media desde entrada a salida de las operaciones con PnLneto>0. Losing: misma medida con PnLneto<0. No son tiempo hasta entrada ni tiempo de recuperación de drawdown. Incluyen fines de semana/horas sin mercado si la posición sigue abierta.
Global ganadoras489736.76segundos=5.66825días,perdedoras190652.48segundos=2.20663días. La mezcla de estilos importa: shorts ganadores16.5353h/perdedores25.2512h; longs ganadores duran mucho más.
Un mínimo51% de winrate no es requisito matemático de rentabilidad: depende de magnitud de beneficios,pérdidas,costes y cola. No añadir ese umbral a posteriori.

| Dirección | Trades | Winrate % | Ganancia media USDT | Pérdida media USDT | PF neto | PnL neto USDT |
|---|---:|---:|---:|---:|---:|---:|
|Long|97|44.3299|1031.99|411.13|1.99879|22174.44|
|Short|123|55.2846|293.58|266.85|1.36024|5287.02|

Ganancia/pérdida media longs2.5101,shorts1.1002. Umbral de equilibrio descriptivo loss/(win+loss):28.4891%long y47.6147%short. No son estimaciones estables futuras ni justificación para aumentar riesgo; tamaños y capital variaron.
PF=beneficios netos de trades ganadores /abs(pérdidas netas de perdedores), comisiones incluidas por trade.

## Componentes
BTC long31trades,win48.3871%,PF3.4604,net13881.76.
PAXG long35,win40%,PF1.4996,net4632.27;su mejortrade representa90.0378% de ese neto.
SPY long31,win45.1613%,PF1.5023,net3660.42;su mejortrade representa93.6826%.
La concentración por activo exige revisión. Un sistema tendencial puede depender de pocas tendencias grandes, pero no debe venderse como evidencia abundante de tres ventajas independientes.

## Shorts por año de cierre
2020parcial7trades,-303.87;2021 30,-542.64;2022 16,+2262.65;2023 24,+1294.81;2024 28,+974.55;2025 18,+1601.52. PnL de cierres no equivale a retornos anualesMTM ni capital aislado.
La muestra no apoya asumir que solo ganen durante mercado bajista: entradas se habilitan en régimenEMA120ascendente, buscando continuación corta de liquidaciones/pullbacks.

## Tipos de salida
67targetsLIMIT:net+19800.78,tiempo medio15.654h.
49STOP:net-13774.46,tiempo medio19.180h.
7MARKET por caducidad:net-739.29,tiempo medio74.940h;1ganadora6perdedoras.
Las ejecuciones de salida almacenadas permiten clasificar estos tipos. No se dispone aquí de series intratrade MFE/MAE ni de stops cancelados completos en todas las operaciones: NO inventar excursiones ni calcular Rpara todos con estos snapshots. El ratioR reconstruible solo para49STOP (-1.0453Rmedio) no es ratioRglobal.

Trades de duración final<=12h aportan6776.62;>12h -1489.60. Esto usa una variable conocida solo al terminar: **no es un filtro negociable ni prueba causal**. Nuevas pruebas24/48h vs72h de salida temporal se predeclaran en informe separado y reejecutan cartera completa.

## Próximos caminos
1. Caducidad de la señal: controles24/48h, sin tocar longs/entradas; leer ambos aunque sean malos.
2. Si mejora, controles de costes y períodos congelados, sin abrir2026.
3. Si falla, investigar si el stop ligado aEMA20 y el objetivo fijoATR desalinean recompensa/riesgo entre entornos; una sola modificación justificable por prueba, no barrido RSI para escoger un pico.
4. Auditar concentración/regularidadlong y aportaciónincremental de cada activo. No atribuir todo déficit de regularidad a shorts.
5. MonteCarlo conjunto/paridad de ejecución solo tras candidata suficientemente estable. No hay autorización de nueva extensiónframework.

## Higiene y trazabilidad
Título/descripción de referencia actualizados en español con tabla explícita de3activos/direcciones; source snapshots originales preservados y métricas sin cambiar.
.gitignore ampliado por pedido del usuario: JSON de ejecuciones/researchjobs,exportacionesCSV,rawM1/ZIP/bi5/parciales. Se conservan scripts,estrategias,informes,manifest y auditorías pequeñas. Ningún archivo borrado ni cambios previos revertidos. Tras exclusiones y antes de los nuevos controleshabía90archivos modificados/no rastreados; los restantes contienen trabajo real y no se ocultan para maquillar el contador.

Análisis MCP succeeded: feb81963abd4403c867fae6472ec7015 yfafc6a6832a34b30b2ffef5db29cb796. Datos2020–25 únicamente.
