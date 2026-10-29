# Monte Carlo conjunto: alcance disponible y propuesta
Estado: diagnóstico y diseño, NO implementado, ningún MC conjunto ejecutado. No abrir2026.

## Evidencia del motor
_prepare_routes en jesse/modes/backtest_mode.py crea instancias de pipeline separadas por ruta, incluidas data_routes. MovingBlockBootstrapCandlesPipeline usa RNG y buffers locales por instancia y remuestrea bloques de deltas OHLC absolutos sobre sus propias filas; mantiene timestamps/volúmenes.
Con seed=None las elecciones son independientes. Reutilizar una semilla tampoco alinea UTC cuando SPY no tiene las mismas filas que BTC/PAXG. Que el simulador soporte huecos no implica que el remuestreo conserve dependencia entre activos.
El pipeline gaussian añade ruido absoluto en USD; compartir sigma entre BTC y SPY no iguala severidad relativa ni constituye estrés conjunto calibrado.
No se modifica código ni se presenta MC univariado como certificación de cartera.

## Diseño concreto para una futura extensión separada
1. Plan de remuestreo de calendario compartido por todas las rutas y data_routes, generado una sola vez por escenario/semilla.
2. Bloques de semanas UTC completas, con elección común del bloque fuente por escenario para conservar shocks simultáneos y estructura semanal.
3. Rendimientos relativos/log y geometría OHLC relativa al cierre previo, reconstruidos sobre el nivel destino; evitar deltas absolutos que distorsionen severidad al variar niveles de precio.
4. Máscaras de disponibilidad de origen/destino explícitas, sin velas sintéticas de SPY en cierres. Rechazar o definir de forma documentada bloques incompatibles, feriados y cambios de sesión antes de medir resultados. No rellenar silenciosamente precios negociables.
5. Warm-up y rutas auxiliares coherentes con el mismo plan; aislamiento de semillas entre escenarios y reproducibilidad de escenarios reanudados.
6. Revalidar contabilidad, STOP/LIMIT con gaps y equivalencia de ejecuciones normal/rápido donde aplique. La diferencia de muestreo de equity debe seguir identificada.
7. Pruebas con series perfectamente correlacionadas, inversamente correlacionadas, escalas de precio distintas y SPY cerrado; ausencia de fuga entre escenarios y conservación de OHLC válido.
8. Comparar datos originales, escenarios y correlaciones contemporáneas por régimen; después200escenarios candles-only con original/mediana/colas para retorno/DD/Sharpe. El remuestreo seguiría siendo un modelo condicionado a2020–25, no prueba definitiva de ausencia de sobreajuste.

Esta extensión toca framework y Monte Carlo compartido. La autorización actual cubre únicamente persistencia de equity y corrección de reserva por submitted_price, no esta funcionalidad. Requiere excepción adicional expresa a bot/AGENTS.md antes de implementarla. No es razonable ampliar el framework para certificar una candidata que todavía falla criterios de consistencia/shorts; primero resolver esa decisión de investigación.
