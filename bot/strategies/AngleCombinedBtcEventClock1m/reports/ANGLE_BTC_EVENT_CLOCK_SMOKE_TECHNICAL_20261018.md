# EventClock — smoke técnico y diagnóstico de cobertura
[Smoke Q1-2021](http://localhost:9200/#/backtest/124865f1-ec3c-4c0a-a6d9-7dcb5ad3bda6). Finished en16,64s, sin error de invariantes;10trades,8shortsSTOP y2longs, contador abierto0. No se usa beneficio para elegir el full ni se cuenta como prueba económica.

Counters FINAL2021 entregados por root: minutes125340,down101,up102,blocked_open39,blocked_pending0,long_priority0,rejected52,plans10,armed10,fills8. Identidad101=39+52+10. Auditoría wallet/fills e2046b7b88bc4b2593603aa5d3bde62f pendiente al recibir esta tarea; no declarar reconciliación antes de resultado.

125340callbacks son menos que129600minutos del trimestre. La causa aún no está demostrada: no atribuirla a SPY/feriado ni recortar ventana. Root pidió diagnóstico adicional previo a full: event_first_minute=setdefault(now) y log anual/final con first/init/last, conservando absolutamente ventanas, inicialización y decisiones.

Se guardó fuente víaMCP y readback exacto. Reversión textual de sólo setdefault, formato de log y comentario devuelve exactamente fuente ejecutada en smoke; ningún otro código cambió. Comentario de _entry_window ahora describe frecuencia long4h, reconociendo la cadencia nueva short. No se repitió smoke, no se creó borrador ni se lanzó full. La ampliación de telemetría no justifica inferir fechas que todavía no se observaron.