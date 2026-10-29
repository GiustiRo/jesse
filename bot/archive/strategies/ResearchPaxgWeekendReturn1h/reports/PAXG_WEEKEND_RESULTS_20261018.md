# PAXG: reversión de fin de semana frente a control hábil

Fecha local: 18 de octubre de 2026. Ambos backtests terminaron. La receta de fin de semana supera los filtros iniciales, pero su concentración temporal impide presentarla como una estrategia validada. No se cambiaron reglas después de los resultados.

## Resultado y contraste

El protocolo PAXG_WEEKEND_PROTOCOL_20261018.md fue guardado antes de ejecutar. Usa el cierre semanal del mercado primario descrito por Paxos como motivación; las anclas son precios propios de PAXG, no valor justo observado del oro. El calendario de Nueva York se implementa con ZoneInfo.

Ambas recetas compran una caída o venden una subida de al menos un ATR 4h respecto de un ancla de dos fechas locales antes. El ATR se fija al capturar el ancla y sólo usa velas 4h completas. Entran MARKET, fijan target en el ancla, stop a dos ATR y salida máxima de 24 horas desde el fill. El fin de semana compara viernes 16:00 con domingo 16:00; el control compara lunes 16:00 con miércoles 16:00.

Las dos cuentas aisladas tienen 10.000 USDT, riesgo fijo del 1%, 5x aislado y fee de 0,00045 por lado, incluido el target LIMIT. La ventana es 2020-10-15 a 2025-12-31 exclusiva. No se utilizó 2026, funding ni datos nuevos.

| Diseño | Trades | Neto USD | Antes de fees USD | Fees USD | PF neto | CAGR motor | DD motor |
|---|---:|---:|---:|---:|---:|---:|---:|
| [Fin de semana](http://localhost:9200/#/backtest/2da06c02-d246-43a0-b265-8837aa9c4be5) | 37 | 400,22 | 659,35 | 259,13 | 1,5073 | 0,7555% | −2,0622% |
| [Control hábil](http://localhost:9200/#/backtest/3855e023-3d66-4aff-8a13-fbb3110a3255) | 162 | −1.245,28 | −119,12 | 1.126,16 | 0,7135 | −2,5186% | −13,0393% |

Neto sobre suma de nocional de entrada: 13,885 bps frente a −9,952 bps. La diferencia es descriptiva: los días y las muestras son distintos, sin asignación aleatoria. El control negativo reduce la explicación de reversión genérica bajo esta receta, pero no identifica causalmente el mecanismo de creación o redención.

## Costes, actividad y concentración

Con 5 bps extra por ida y vuelta sobre los mismos fills, el fin de semana conserva 256,10 USD; con 10 bps conserva 111,97 USD. Su margen estático agotador es 13,885 bps adicionales agregados sobre nocional de entrada. Estos cálculos no simulan cambios de órdenes, sizing, spreads o fills.

La exposición temporal es 1,006% frente al 7,137% del control. El holding medio es 12,42 horas frente a 20,12. La señal es demasiado escasa para asumir que arreglará por sí misma la regularidad de la cartera.

Los tres mayores ganadores suman 297,30 USD, el 74,28% del neto. Al quitarlos queda +102,92 USD, una descripción de concentración y no un criterio de selección de trades.

La debilidad principal es temporal. Las cohortes de trades por año de cierre arrojan:

| Año de cierre | Fin de semana, trades | Neto USD |
|---|---:|---:|
| 2020 parcial | 1 | 84,74 |
| 2021 | 7 | 12,89 |
| 2022 | 8 | 337,42 |
| 2023 | 10 | −43,73 |
| 2024 | 7 | 6,89 |
| 2025 | 4 | 2,01 |

Son cohortes de cierre, no rentabilidades anuales MTM. 2022 representa el 84,3% del beneficio total. El agregado 2023–2025 es −34,82 USD. Una pequeña ganancia en 2024 y 2025 no demuestra estabilidad reciente.

El fin de semana obtiene −87,02 USD en 11 longs y +487,25 USD en 26 shorts. Se conserva la receta simétrica: no se retiran longs después de ver resultados. El control pierde en ambos lados: 65 longs, −476,17 USD; 97 shorts, −769,10 USD.

## Verificación y límites

El análisis f6e032d499ae4fa1a354d3f9471d6fb7 terminó succeeded / exit 0 con snapshots completos de las dos sesiones. Resultados numéricos persistidos en PAXG_WEEKEND_AUDIT_20261018.md.

Todas las entradas del fin de semana ocurrieron el domingo a las 16:00 de Nueva York; las del control, el miércoles a las 16:00. Las salidas MARKET por tiempo ocurrieron exactamente a las 24 horas: 12 y 93 respectivamente. Ninguna posición duró más de 24 horas. El fin de semana tuvo 19 targets LIMIT y 6 stops; el control, 28 targets y 41 stops. No hubo posiciones superpuestas ni cierres terminales sintéticos.

Las cantidades, fees y PnL de todos los fills concilian con los trades; las diferencias máximas de PnL son inferiores a 1,4e−12 USD. La wallet final concilia con error inferior a 1,7e−11 USD. El máximo nocional inicial sobre wallet previa fue 1,194x y 1,518x, bajo el techo de 4,4x. Esto verifica el tamaño inicial, no la exposición marcada en cada instante.

La fuente comprueba M1 fresca y paridad de cierre 1h/M1, guarda el ancla con su ATR y respeta el reloj causal. Los snapshots de resultados no contienen las velas ni el estado de anclas: el análisis de fills no constituye una reproducción independiente de todas las señales. Tampoco certifica que el proveedor nunca haya rellenado velas.

La curva del motor contiene 1.902 muestras a las 00:01 UTC y dos fronteras a las 00:00. No se usa como cierre diario para porcentajes mensuales. Root coordina el auditor MTM V4 con precios y anclas de snapshots. El DD de cierre diario puede diferir del DD mostrado en la tabla.

El cierre del mercado primario documentado actualmente por Paxos motivó el diseño. No se auditó en esta ronda la estabilidad histórica de esa política durante 2020–2025. Tampoco se observaron operaciones de mint/redeem. Si la ventaja proviene de una prima específica del token spot, su traslado al perpetual requiere corroboración: una similitud visual general del precio no prueba igualdad precisamente durante esas dislocaciones.

## Decisión

El fin de semana supera los gates iniciales predeclarados: neto positivo, PF mayor de 1,2, al menos 30 trades, DD inferior al 25%, mejor neto por nocional que el control y supervivencia al coste extra estático de 5 bps. Es un hallazgo de desarrollo que merece contraste, no una candidata robusta aceptada.

La concentración en 2022, la escasez de trades y el posible carácter específico del spot exigen cautela antes de integrar. No se ejecutaron variantes, selección de lado, optimización, MC, cambios del framework ni apertura de 2026. Cualquier continuación necesita protocolo previo y conservará estos resultados completos. La referencia permanece intacta.

Conteo de la línea PAXG: cinco backtests económicos nuevos terminados, incluyendo el control de retest; tres recetas de hipótesis y un control de calendario, además del control existente. El historial global anterior sigue contando y la muestra no se convierte en OOS.
