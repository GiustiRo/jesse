# R4 — reparación de transporte de diagnóstico

La API corta cada línea de log alrededor de2000caracteres, aun con página más grande. Los4JSON de20filas del diagnóstico inicial no son íntegros: no se interpretan sus fragmentos.

Root leyó la fuente final víaMCP y comparó todo el texto: sólo cambia `_path_report`,20filas/JSON→1fila/JSON, con comentario de motivo. Ningún cambio de clock, captura, entry, exit, sizing o riesgo. QA reparación45PASS,job b2c45a03f9d74012b12f244a2efe8e77,79partes de1fila<1800chars. Dos reruns diagnósticos adicionales por fallo de instrumentación, explícitamente separados del presupuesto26–32económico; no agregan variantes ni pruebas elegibles.

Paridad inicial exacta de273/280trades, cantidades, precios, fechas,fees yPNL conN204. Auditorjob cca567267156411e8aff6ec08c981fcd;máxΔPNL0. Repetir misma paridad sobre retry y unir las79observaciones al trade real antes de describir excursiones. Los umbrales de salidas ya estaban congelados; no se reajustan al verlos.

Retry preparados, sin ejecutar al guardar este informe: [B](http://localhost:9200/#/backtest/c26a2bbc-d960-4a13-873b-07e52f57b05b),[C](http://localhost:9200/#/backtest/cacecd6c-6f04-46d4-b456-5b667010bee8). 2026 cerrado.