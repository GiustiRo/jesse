# Protocolo previo — salida long completa a R fijo
Fecha2026-10-18. Protocolo previo a ejecución; código y drafts autorizados internamente para preparación, sin autorización de lanzamiento todavía. Guardada aquí como registro de línea orquestador; no modifica OrchAllocCommonClock4h.
## Hipótesis económica
La referencia conserva la cola de tendencias largas mediante trailing. Cerrar swings completos a un múltiplo fijo del riesgo inicial podría evitar la devolución de ganancias y liberar rutas para nuevas rupturas, a costa de truncar ganadores grandes y aumentar reinicios perdedores. Realizar un beneficio NO mejora por sí solo un mes MTM; la hipótesis es cambiar la trayectoria posterior por menor giveback y distintas reentradas.
Concentración alta en pocos trades PAXG/SPY motiva el contraste, no invalida automáticamente seguimiento tendencial.
## Dos vecinos predeclarados
OrchManageFixedR3: objetivo completo3R.
OrchManageFixedR5: objetivo completo5R.
No barrer otros valores ni seleccionar únicamente ganador después de mirar.
R=distancia inicial original de stop2ATR; desde entryfillreal en on_open_position. Longstoporiginalentry−distance,TPentry+R*distance,qtycompleta. Se retira gestión trailing/BE para representar salida swing fija coherente; precios de ejecución intrabar motor normal, gapsemánticavigente.
Sin modificación de señales, LIMITretest,shortsBTC STOP conTP1.5ATR/stopEMA20/72h; todos los activos y asignación referencia inversoATR original conservados. Riesgo3%/8%,gross4.4x,90%margen,fee0.00045todasórdenes,10k/5xisolated,warmup240,normal replay.
Ventana2020-10-15→2025-12-31exclusivo,2026reservado. Sin parciales/piramidado para compatibilidadauditorV3.
## Falsación y selección
Exigir mejora de mesesactivos Ytrimestres frente54.10%/71.43%,DD<=25%,rentabilidad económica útil antes de otra prueba de esta familia. 20% CAGR es orientación económica previa, no descarte automático: una variante19% que cumpla65/80/DD se analizaría para comparar economía. Final65–70%/80%no se rebaja.
Ambos vecinos deben ser viables y no divergir fuertemente; un pico aislado no cuenta como meseta. Si pierden la regularidad/retorno al truncar tendencias, descartar familia completa y conservar referencia. Winrate51%NOesobjetivo.
Medir cantidad nueva de señales/trades,holdingperiod,fee,aporte/dirección/activo,concentración,capitalexpuesto y MTMcalendarno00:01. Toda simulación queda registrada incluso si negativa.
## Limitaciones
Cierre porTPno garantiza continuidaddealpha niindependencia de señales; períodos2020–25vistos, hipótesis escogida por diagnósticoexpost. NoOOSni certificaciónejecuciónLIMIT/proxies.
