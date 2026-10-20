# PAXG 0,75 ATR: resultado de los dos controles adicionales

Fecha local: 18 de octubre de 2026. Ambos controles terminaron. El hallazgo exploratorio de 0,75 ATR conserva rentabilidad frente a un control hábil al mismo umbral y al retirar el target LIMIT. Estos controles fueron elegidos después de observar la variante de 0,75: siguen siendo desarrollo adaptativo y no validación independiente. La primaria de 1 ATR permanece sin cambios y no se reemplaza automáticamente.

## Cambios y resultados

El protocolo PAXG_EVENT075_FALSIFICATION_PROTOCOL_20261018.md se guardó antes de ejecutar. El control hábil cambia únicamente clase y EVENT_ATR respecto del control hábil de 1 ATR. El estrés cambia únicamente clase y EVENT_ATR respecto del estrés de ejecución de 1 ATR de root.

Se conservan 10.000 USDT, riesgo del 1%, fee 0,00045 por lado, 5x aislado, techo bruto 4,4x y reserva de 10 bps sólo para sizing. Ventana 2020-10-15 a 2025-12-31 exclusiva; PAXG-USDT 1h y auxiliares 1m/4h. Sin datos nuevos, funding, framework, scripts ni 2026.

| Variante y dashboard | Trades | Neto USD | Antes de fees USD | Fees USD | PF neto | CAGR motor | DD motor |
|---|---:|---:|---:|---:|---:|---:|---:|
| [Fin de semana 0,75, target pasivo ya observado](http://localhost:9200/#/backtest/ff199ebe-dab0-4c09-9078-fff98188e97c) | 60 | 764,04 | 1.178,35 | 414,32 | 1,7318 | 1,422% | −2,991% |
| [Control hábil 0,75](http://localhost:9200/#/backtest/62e11d8f-f098-44df-8b6f-2861a0503811) | 188 | −1.171,40 | 135,16 | 1.306,56 | 0,7569 | −2,361% | −12,709% |
| [Fin de semana 0,75, target mediante MARKET](http://localhost:9200/#/backtest/d75e1a23-0429-4b61-800e-a1cb24835459) | 60 | 768,17 | 1.181,89 | 413,72 | 1,7359 | 1,430% | −2,991% |

El neto por suma de nocional de entrada es 16,578 bps para el pasivo, −8,070 bps para el control hábil y 16,696 bps para el estrés. El control hábil tiene una ganancia pequeña antes de fees que no compensa su turnover. Los días y las distribuciones de movimientos difieren: el contraste no prueba causalidad de mint/redeem.

El estrés elimina el target LIMIT. Tras observar el primer toque en una vela 1h ya cerrada, sale MARKET a su cierre si hay cotización M1 fresca y consistente; conserva stop y máximo de 24 horas. No es una cota pesimista de ejecución: el cierre posterior puede resultar mejor o peor que el precio del target. El resultado indica que esta perturbación concreta no elimina el beneficio.

## Fricción y temporalidad

| Sensibilidad sobre mismos fills | Pasivo 0,75 USD | Hábil 0,75 USD | Estrés 0,75 USD |
|---|---:|---:|---:|
| Neto con 5 bps RT extra | 533,60 | −1.897,22 | 538,13 |
| Neto con 10 bps RT extra | 303,17 | −2.623,03 | 308,09 |
| Neto de cohortes de cierre 2023–2025 | 310,76 | −537,01 | 366,39 |
| Cohortes 2023–2025 con 5 bps extra | 146,43 | −1.007,15 | 202,29 |
| Cohortes 2023–2025 con 10 bps extra | −17,91 | −1.477,30 | 38,19 |

Son sensibilidades estáticas sobre fills observados, no una nueva simulación de cuenta o ejecución nativa. Las cohortes de cierre no son retornos anuales MTM ni una muestra fuera de selección.

| Año de cierre | Pasivo 0,75 USD | Hábil 0,75 USD | Estrés 0,75 USD |
|---|---:|---:|---:|
| 2020 parcial | 133,50 | −70,49 | 134,49 |
| 2021 | 78,27 | −367,62 | 55,72 |
| 2022 | 241,50 | −196,28 | 211,58 |
| 2023 | 123,20 | 86,49 | 236,07 |
| 2024 | 177,67 | −6,10 | 133,21 |
| 2025 | 9,89 | −617,40 | −2,89 |

El estrés no mantiene todos los signos anuales del pasivo: 2025 queda ligeramente negativo con diez trades. El agregado 2023–2025 sigue positivo, incluso con 10 bps extra, pero con margen pequeño. No se eliminan 2025 ni trades desfavorables. Tampoco se exige retrospectivamente que cada año sea positivo como criterio inventado después de observarlo.

Los tres mayores ganadores representan el 39,57% del neto pasivo y el 53,74% del estrés. Al quitarlos descriptivamente quedan +461,72 y +355,36 USD. El estrés distribuye −o mejora− los resultados de manera distinta por dirección: longs +58,54 USD en 18 trades, shorts +709,63 USD en 42; el pasivo tiene longs −57,22 y shorts +821,26. Se conservan ambos sentidos; no se seleccionan shorts retrospectivamente.

Exposición temporal: 1,445% pasivo, 7,856% hábil y 1,488% estrés. La escasez de la señal sigue limitando su capacidad potencial de aportar regularidad a una cartera.

## Auditoría completa

El job fd4426de9efd4a01b1bf74b37f8a27f9 terminó succeeded / exit 0, con todos los snapshots de las tres sesiones. Resultados numéricos persistidos en PAXG_EVENT075_FALSIFICATION_AUDIT_20261018.md.

Las 60 entradas del pasivo y del estrés coinciden en timestamp y sentido; máxima diferencia de precio 4,55e−13. Los tamaños pueden cambiar al cambiar los resultados previos de la cuenta. Las entradas del calendario son domingo 16:00 de Nueva York y las del control, miércoles 16:00.

Todos los fills, fees, cantidades y wallet concilian. Error máximo de fee inferior a 1,8e−15 USD, PnL inferior a 1,6e−12 y wallet inferior a 1,7e−11. No hay posiciones superpuestas, salidas terminales sintéticas ni holdings superiores a 24 horas.

El pasivo tiene 37 targets LIMIT, 8 stops y 15 salidas de tiempo a 24 horas. El control hábil tiene 46 targets, 45 stops y 97 salidas de tiempo. El estrés tiene 52 salidas MARKET y 8 stops, sin salidas LIMIT.

Esta auditoría no reproduce todas las oportunidades ni certifica la fuente de velas: los snapshots sólo incluyen resultados. La fuente conserva anclas causales, ATR 4h completo, timestamps M1 frescos, paridad 1h/M1 y calendario ZoneInfo. Tampoco se certifica cotización native perpetual durante las dislocaciones.

Root informó para el pasivo 0,75: 28/40 meses activos positivos, pero 28/63 de calendario y 16/21 trimestres. Períodos completos: 27/39 activos, 27/61 de calendario y 14/19 trimestres. No equivale a cumplir la meta de cartera. El calendario MTM exacto de los nuevos controles corresponde al análisis unificado de root; no se usa la curva del motor a las 00:01 como cierre UTC.

## Decisión y conteo final

El 0,75 supera estos dos intentos concretos de falsación: la reversión genérica hábil al mismo umbral no ofrece rentabilidad neta y retirar el target pasivo no elimina el resultado del fin de semana. Es evidencia suficiente para conservar una candidata exploratoria de desarrollo, con selección explícita, sin llamarla robusta fuera de muestra ni reemplazar la primaria.

Siguen pendientes demostrar utilidad incremental en una cuenta compartida y la transferencia del comportamiento específico del spot al perpetual. No se ejecutó integración, optimización, nuevos umbrales ni apertura de 2026. La concentración temporal de la primaria de 1 ATR y el fallo de fricción del vecino 1,25 permanecen en el registro.

Este agente completó NUEVE full PAXG nuevos; con el estrés de 1 ATR de root son DIEZ de la línea PAXG global. Los resultados anteriores no se borran. No quedan backtests ni análisis propios activos.
