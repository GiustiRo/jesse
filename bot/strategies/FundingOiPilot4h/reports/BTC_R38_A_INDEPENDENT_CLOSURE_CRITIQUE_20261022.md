# R38 A — revisión interpretativa independiente de cierre

Fecha: 2026-10-22. Se leyeron completos BTC_R38_A_RESULTS_20261022.json (dos páginas, 2.369 líneas) y BTC_R38_UNIVERSE_CHECK_20261022.json. Esta revisión interpreta la auditoría guardada; no repite la auditoría de 484 trades/4.365 pagos de funding ni acredita una segunda conciliación por fill.

**Dictamen: ninguna candidata; SECOND no demuestra una mejor capacidad predictiva ni gana el contraste completo.**

| Política | CAGR neto | PF neto USD | DD M1+fills | Meses positivos calendario | Q positivos | Mediana mensual calendario |
|---|---:|---:|---:|---:|---:|---:|
| [FIRST](http://localhost:9200/#/backtest/7d2a7a2f-77e0-4926-ab15-b6772beac17b) | 6,77785% | 1,21335 | 15,95913% | 30/62 | 8/20 | −0,14265% |
| [SECOND](http://localhost:9200/#/backtest/ff157a56-362d-4a0a-9fd3-c8d90c813577) | 6,88483% | 1,34098 | 17,41512% | 27/62 | 12/20 | −0,33039% |

Ambas incumplen CAGR, regularidad mensual/trimestral y mediana positiva. SECOND también empeora DD y número de meses positivos respecto de FIRST. Su 27/61 entre meses activos no sustituye el 27/62 calendario; ninguno de esos denominadores se aproxima al objetivo. El PF mayor y los cuatro trimestres positivos adicionales no compensan estas fallas.

SECOND gana sólo 73,738207 USDT de neto adicional en toda la ventana. La descomposición guardada es −400,482944 de bruto de precio, +423,889057 de ahorro de comisiones y +50,332094 de menor débito de funding. Por tanto, la mejora neta procede de costos realizados más bajos, mientras el bruto empeora. Es una descripción de dos trayectorias económicas con tamaños y calendarios propios, no una prueba aislada de que ordinal 2 prediga mejor. Tampoco el PF es tasa de acierto ni debe promediarse entre políticas para crear un tercer resultado.

El replay común confirma 832 cierres extremos (492 up/340 down), 298 resets y cero invalidaciones. Los eventos seleccionados —296 y 184— se ejecutaron todos, sin bloqueo por ocupación ni rechazo de geometría. Aquí la diferencia de actividad deriva de la selección ordinal, no de una cola de señales bloqueadas. Los 832 raw no son 832 trades omitidos ni oportunidades rentables acreditadas. SECOND puede seleccionar un segundo cierre extremo consecutivo; no exige un primer fallo ni un retest independiente.

La gestión estructural sí quedó ejercida: FIRST tuvo 122 stops y 174 salidas por reset; SECOND 71 y 113, con holds máximos 332h/324h y sin TP ni cierre terminal. Esto acredita qué mecanismo cerró las operaciones, pero no su ventaja frente a un plazo o target alternativo, que no fueron comparados. No autoriza añadir ahora esas variantes.

La historia muestra concentración temporal: 2023 aporta +30,16%/+34,66%, mientras 2025 pierde −4,10%/−11,14%. Las ventanas móviles finales también se deterioran. El neto sin los dos mejores meses sigue positivo (+242,737/+404,545 USDT), por lo que esa puerta formal se cumple; el remanente reducido no transforma la regularidad negativa en robustez. Long/short son atribuciones descriptivas, sin autorización para retirar un lado.

Se leyó además BTC_R38_NATIVE_WALLET_SIZING_CHECK_20261022.json: la auditoría nativa de root verifica las 484 entradas, presupuesto 1% de wallet total y cantidad exacta legacyhalf, sin límite de margen vinculante. Esta revisión cita ese PASS sin recalcular el sizing. No hay evidencia de una falla de cuota que explique el bajo retorno; el denominador no es 5.000.

Se mantiene el denominador wallet total 10.000 con cuota 1%, resto ocioso y funding histórico aplicado/proxies declarados. Son cuentas alternativas, sin suma de curvas, sin OOS y sin potencia estadística acreditada por N. DD M1+fills no es DD intraminuto.

**Cierre recomendado:** conservar ambos resultados y el PASS técnico; no promover FIRST ni SECOND. Sin ordinal 3, otro canal, filtros, cambio de gestión, exposición o selección de años/lados para rescatar esta pregunta. Cero nuevos jobs, fuentes o motores en esta revisión.
