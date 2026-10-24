# Capacidad compartida sin techo nocional individual: resultados

Hipótesis predeclarada: liberar la capacidad reservada a activos inactivos, conservando 3% de riesgo por trade, 8% agregado planificado, techo bruto global de 4,4x, buffer de margen y 5x aislado. No cambian señales ni gestión de posiciones. Comisión base 0,045% por lado; capital inicial 10.000 USDT, 4h, período de desarrollo 2020-10-15 a 2025-12-31 exclusivo. 2026 permanece reservado.

| Configuración | CAGR | DD del motor | Meses activos positivos | Todos los meses positivos | Trimestres positivos |
|---|---:|---:|---:|---:|---:|
| BTC ambos, con reserva individual | 21,71% | −13,01% | 34/56 = 60,71% | 34/63 | 14/21 = 66,67% |
| BTC ambos, capacidad compartida | 26,48% | −20,46% | 35/56 = 62,50% | 35/63 | 14/21 = 66,67% |
| Tres activos, referencia con reserva | 28,83% | −14,89% | 33/61 = 54,10% | 33/63 | 15/21 = 71,43% |
| Tres activos, capacidad compartida | 37,43% | −18,42% | 34/61 = 55,74% | 34/63 | 15/21 = 71,43% |

[BTC con reserva](http://localhost:9200/#/backtest/4623d369-05e7-4714-8f3b-5c10b1726663)
[BTC compartida](http://localhost:9200/#/backtest/bc516f87-1ebc-4fd9-b7eb-68b31d024304)
[Referencia tres activos](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb)
[Tres activos compartida](http://localhost:9200/#/backtest/9f7ac256-699a-4e4d-9d4d-a639c0158a85)

## Exposición y concentración del riesgo
Nocional bruto/equity medio al cierre diario:
- BTC con reserva: 0,11257x; sin reserva: 0,17197x.
- Tres activos con reserva: 0,60855x; sin reserva: 0,80680x.

La exposición máxima observada al cierre pasa a 4,42616x en tres activos compartidos. El techo de 4,4x se evalúa al admitir entradas; el movimiento posterior de precios/equity puede superarlo. No es una garantía continua ni una pérdida máxima contractual.

El peor mes de tres activos empeora de −7,02% a −13,40%; en BTC compartido es −12,59%. Elevar utilización del capital no resuelve automáticamente la regularidad. En BTC solo gana un mes adicional, con un aumento de drawdown de unos 7,45 puntos. En tres activos gana un mes, con unos 3,53 puntos más de drawdown.

Tres activos compartidos: 216 trades (96 long, 120 short), saldo final 52.475,03 USDT. PnL neto BTC long 20.724,14; BTC short 9.193,05; PAXG long 6.633,61; SPY long 5.924,23. Cambian trades elegibles por capacidad: no es escalar linealmente la curva original.
BTC compartido: 156 trades, saldo final 34.026,92; longs 18.113,58 y shorts 5.913,33 netos.

## Control de formulario: límite de la interpretación
[Repetición con rutas invertidas en el formulario](http://localhost:9200/#/backtest/f2397065-5b7f-47d8-b3c8-05ca159736ef) da los mismos 216 eventos y resultados, pero el motor ordena internamente las rutas por exchange/símbolo en el replay de timestamps. **No se cambió la prioridad real**, por lo que esa igualdad no certifica independencia de prioridad ni equidad de asignación.
El control interno de prioridad sigue pendiente; no se modificó el framework para hacerlo.

## Verificación y decisión
Análisis MCP 952f460501534c16b970c977512b12ef completado correctamente. Auditor MTM v3, autocontroles y reconciliación terminal pasaron. Las medias de exposición son muestras al cierre diario; no reconstruyen el máximo intradiario. Incluye períodos parciales de borde.

No sustituir la referencia por esta rama. Ningún caso cumple simultáneamente 65–70% de meses activos positivos y 80% de trimestres; el mayor retorno viene con mayor riesgo/exposición. Retener la rama como comparador de utilización de capital, sin declararla validada.
Antes de añadir filtros para forzar meses positivos, definir un reparto que pueda justificarse antes de conocer los resultados y validar prioridad/ejecución. No escoger el peso ni el orden que maximicen esta muestra. Datos proxy, ejecución LIMIT, financiación y validación conjunta siguen pendientes.
