# T404 — revisión independiente de reparación de residuo numérico

Releí N204ExitR404 por MCP después de la reparación y comparé sus métodos con la fuente raw que había leído antes. **Sólo cambia on_reduced_position.** No ejecuté jobs, backtests ni stubs adicionales; no modifiqué fuentes.

El guard está limitado al suplemento (explore_kind) y usa estrictamente 0 < abs(position.qty) < .001. .001 es el lote BTC de investigación ya existente en sizing y división de targets; no es un umbral seleccionado por resultados. El guard registra el residuo, solicita self.liquidate() y retorna antes de recrear el stop. Cantidad cero no dispara liquidación; .001 exacto y cantidades mayores mantienen el camino anterior, con la cantidad restante y el mismo average_stop_loss.

Los TP1/TP2, sus precios y cantidades planificadas, geometría, entradas originales, riesgo, ledger, plazo y demás métodos son idénticos a raw. El remanente económico TP1 debe ser al menos un lote por construcción y no se pretende liquidarlo con este guard. La revisión de texto no demuestra todos los casos numéricos del motor; esa frontera requiere la QA y los fills reales.

Leí el caso documentado en N204_R4_T404_RAW_QUARANTINE_20261019.md: el raw C deja ~7e−18 después de TP2 y lo cierra recién a las 48h, alterando ocupación posterior. Por ello raw B/C quedan conservados como intentos con defecto de implementación, sin usarlos como comparación aceptada. No se añade retrospectivamente el PNL de la operación original desplazada: los tamaños y estados posteriores son endógenos.

**Pendiente antes de aceptar el retry:** demostrar en órdenes ejecutadas que TP2 y el cierre del residuo tienen el mismo executed_at y que la ruta no permanece ocupada hasta el deadline por ese residuo. Un stub puede verificar que el hook llama a liquidate, pero no prueba cuándo el motor procesa esa orden ni la liberación real del estado. Tampoco se trata de una garantía de ejecución live de un sublote: es una reparación acotada del simulador de investigación.

No encontré cambios de hipótesis ni ajustes económicos en la fuente reparada. La corrección mantiene la receta de salida parcial congelada; cualquier diferencia de PNL del retry debe atribuirse descriptivamente a su recorrido ejecutado y capital compartido. 2026 permanece cerrado.
