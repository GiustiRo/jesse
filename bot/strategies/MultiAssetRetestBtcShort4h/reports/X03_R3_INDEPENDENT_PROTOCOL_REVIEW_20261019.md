# X03 R3 — revisión independiente del protocolo

Revisor de robustez. Sólo lectura y metodología: no se crearon fuentes, drafts, backtests ni jobs de análisis. Se leyeron DOCS.md, bot/AGENTS.md, backtest-expert, la fuente original PortComparePaxgMarket4h, el protocolo R3 completo y los resultados/handoff/revisiones R2.

El diseño congelado es adecuado como contraste de implementación condicionado a este simulador y muestra. No constituye una nueva validación OOS ni una prueba de ausencia de sobreajuste. No se propone ninguna receta, métrica de selección o umbral adicional.

## Contraste e identificación

El contraste principal debe comparar fixedBE menos actualBE al mismo fee motor, mismo BTC y misma cartera. En .00045 ambas políticas son equivalentes: las cuatro comparaciones nominales deben tener paridad económica. El protocolo exige comprobar trades, precios, timestamps, cantidades y fees, con tolerancia de PNL 1e-7 USDT. Si falla, se debe resolver la implementación antes de interpretar resultados; no cambiar la hipótesis por el beneficio observado.

En .00070, la diferencia identifica el efecto total de cambiar únicamente el piso BE de PAXG dentro de las condiciones del simulador. Los cambios posteriores de capital, sizing, ocupación y otras patas son mediadores de esa intervención. No equivalen a alpha causal BTC ni a un efecto universal de la política.

Las demás funciones que usan fee deben seguir usando la comisión real: sizing, reservas/riesgo agregado, márgenes y cualquier condición de entrada o gestión de BTC/SPY. En el contraste al mismo fee tienen la misma especificación. La comparación nominal→fee alto dentro de una política mezcla coste cobrado, sizing, gestión de otras patas y sus interacciones; no se interpreta como coste directo puro.

La diferencia de diferencias N204−X03 entre políticas BE mide si la ventaja de N204 depende de esa intervención. Es una interacción descriptiva en los mismos datos; B/C y las ocho runs no son observaciones independientes.

## Invariantes de fuente y paridad

La copia debe ser autocontenida, conservar el original y cambiar sólo nombre de clase, constante documentada y el fee usado en el piso BE. El trigger correcto es best_r=(best_close−entry)/initial_distance >= 2.25. Se conservan ATR, trailing, latches, guardas de actualización y cadencia. Trailing o guardas pueden hacer que el cambio del piso no altere una orden.

El piso anclado a .00045 representa +11.25 bps brutos sobre entrada, frente a 14 bps RT de comisión real en .00070. Puede cerrar con pérdida neta; no debe denominarse break-even neto garantizado. El ancla nominal es una intervención diagnóstica y no una recomendación operativa.

Tras paridad, la revisión debe distinguir primer cambio de stop/ejecución PAXG de las consecuencias posteriores. Conviene conservar todas las divergencias, pérdidas, runners y reentradas, no sólo el episodio de enero de 2025 que motivó el diseño. Las coincidencias de timestamps no implican coincidencia de cantidades ni PNL.

## Diagnóstico mensual sin seleccionar umbrales

El calendario común 61 meses/19 Q completos y 63/21 con fronteras, los denominadores activos/todos y el criterio >0 sin redondear son apropiados. Las contribuciones deben ser MTM por ruta al mismo calendario, no PNL de trades imputado por fecha de cierre.

La clasificación económica debe ser exhaustiva y disjunta:

- Base >0 y overlay >0.
- Base >0 y overlay <=0.
- Base <0, pérdida ya presente antes del overlay.
- Base =0.

Root corrigió antes de nuevos outputs la redacción a base<0 y base=0 disjuntos, y explicitó el trigger en R. No se altera el umbral económico ni el 65%/80%. La clasificación adicional 0<ganancia<=coste5, coste5<ganancia<=coste10 y ganancia>coste10 usa los dos presupuestos ya congelados.

“Beneficio pequeño” queda definido por el coste adicional ya congelado: base mensual >0 pero <=su coste extra. Es preferible a escoger un corte de USDT o porcentaje después de ver los meses. Publicar cada mes, turnover, fee real, coste extra, neto tras +5/+10 y signo permite verificarlo. Para extra s bps RT, el coste estático es s*turnover/20000, sumando entrada y salida ejecutadas en ese mes. Turnover cero no admite un umbral finito de fricción por fills del mes.

El overlay es un presupuesto de fricción aplicado a fills fijos, no slippage observado, latencia ni simulación de nuevos precios de ejecución. +5 sobre .00070 debe etiquetarse distinto de +5 sobre .00045. Los meses ya negativos muestran pérdida económica dentro del modelo antes del overlay; no son evidencia de pérdida en operativa real.

Media/mediana, ganancias/pérdidas, peor mes, concentración y co-loss son diagnósticos predeclarados. No cambiar frecuencia, denominadores ni umbral de aprobación para rescatar una política.

## Claims R2 y cierre R3

Los resultados R2 distinguen correctamente overlay y motor, reconocen BE PAXG sensible a fees, concentración temporal, fronteras del bootstrap y selección acumulada. Mantener X03 como referencia y N204 como investigación, sin promoción tras fallar regularidad real, es coherente.

La preselección R3 de N204 usa la regla ya congelada: incremento positivo frente a X03 en ambas B/C y ambas políticas BE al fee alto, DD dentro de 25% y QA/paridad correctas. No permite seleccionar BE por beneficio. No equivale a cumplir M65%/Q80%, ni a autorizar apertura de 2026; cualquier fallo debe quedar explícito.

Pendiente: lectura independiente del clon y QA cuando estén disponibles, y revisión de resultados/atribución/calendario una vez terminales. Ningún nuevo análisis o run autorizado al revisor.
