# Orquestación — asignación, protocolo previo a resultados
2026-10-18. Dos hipótesis estructurales; sin optimización ni barridos.
## Referencia inmutable
[MultiAssetRetestBtcShort4h](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).
Tres rutas 4h BTC/PAXG/SPY, longs todas y shorts BTC, cuenta10k, fee0.00045 por lado incluso LIMIT, 5xisolated, normal replay, warmup240, 2020-10-15→2025-12-31 exclusivo.
2026 no se lee ni se evalúa.
## A: OrchAllocCommonClock4h
Conserva todas las señales y gestión. Sustituye inversoATR en el techo nocional individual por inversa desviación estándar muestral de20 retornos logarítmicos de precios de cierre de buckets4h abiertos16UTC, cerrados20UTC. Se usan exactamente21 timestamps comunes observados en las tres rutas, estrictamente anteriores al bucket cerrado de decisión. Sin rellenar días/velas, sin rutas diarias que obliguen a warmup inexistentePAXG2019. Un mes bursátil aproximado20retornos se fija de antemano. Si falta historia, no admite esa señal. Normalizar pesos sum1. Riesgo3%/8%, global4.4x sin cambios.
Hipótesis: un mismo reloj elimina el sesgo de comparar ATR de sesiones discontinuas con cripto continuo y puede estabilizar aportaciones.
Limitación: días faltantes generan retornos de varios días y no corrigen price/feed/native parity; solo hace idénticas las fechas del estimador entre activos. Los stops siguen ATRoriginal y esa deliberada diferencia puede limitar el impacto.
## B: OrchAllocEqualRisk4h
Conserva todas las señales y gestión. Asigna8%/3=2.6666667% de riesgo máximo por activo y retira techo nocional individual inversoATR. Mantiene tope8%agregado,4.4xglobal y90% margen. Como solo una posición/pendiente por símbolo, no se transfieren presupuestos de riesgo inactivos.
Hipótesis: el presupuesto explícito de riesgo evita infraexposición cripto por repartir nocional en vez de riesgo.
Comparadores: referencia y variante histórica sin techoindividual3% (CAGR37.43/DD18.42/meses55.74%) para separar mecanismo de asignación de mayor utilización de capital.
Limitación: el capglobal de nocional y margen todavía puede hacer relevante la prioridad real interna. No se afirma neutralidad de orden.
## Criterios de falsación
Primario: mejora de meses activos y trimestres MTM, con DD<=25% y rentabilidad útil. Objetivo final65–70% mesesactivos/80%trimestres; ningún simple aumento de CAGR sirve como aprobación. Métricas0%/períodosfronteraparciales y mismo auditorV3. Si solo sube retorno sin regularidad, rama de asignación no resuelve el problema y se descarta como candidata de regularidad.
Reportar TODAS las variantes incluso negativas, contribución y concentración, costes y años si pasan primer control. Prohibido seleccionar20/anchor/presupuesto después de ver resultados. No se cambia referencia, no se abre2026.
