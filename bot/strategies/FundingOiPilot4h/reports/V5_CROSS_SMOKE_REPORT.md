# V5 CROSS — auditoría técnica de smoke

[Sesión terminada](http://localhost:9200/#/backtest/73f4d93a-8302-4ccb-b204-2a57dd61c1cb),2020-09-01→2020-09-08 exclusiva,4h,2,57s motor. Root creó y arrancó la única sesión; timeoutHTTP resuelto en la mismaID, sin retry. Esta auditoría no inició motor, draft ni job.

Resumen primero y luego38líneas de logs,2trades y15filas de funding completos víaMCP, sin páginas pendientes. Configuración nominal coincide exactamente con REGISTRY_V5; debug/fast solicitados true, fast efectivo false, exports/benchmark false. Provenance confirma BAR4h,OIref6,stop3ATR,hold180,targetnone,offset0 yPsinOI. CROSS180checks+comunes61 passed una vez.

42barras:40sin señal,1long y1short; particiones y causas concilian.2entradas=2trades=2callbacks de cierre:1STOP antes de AUDIT y1fold_end después. Planes comprobados contra cruce exacto20/80,81cierres,ATR15,stopdesde fill,qtyfloor8,2%stop+fees ycap1x. Primera entradaP conOIinicialización ysegunda conOInonrising: calidad/gateOI no restringen P. Máxima línea estructurada1022<=1900.

Funding procesó21eventos y15cargos/créditos sobre posiciones, todos conmarca proxy. La pérdida alstoplong excedió presupuesto200 en9,850051USDT, confundingadicional documentado; no es garantía de pérdida máxima2%. Root concilia contabilidad financiera sobre snapshots completos.

Indicador total_open_trades1/open_pl es captura previa al cierre final. Los dos trades/callbacks y saldo terminal incluyen fold_end; no posición residual activa. Sin salida opuesto_cross,hold30d ocalendario ejercida por motor en esta semana; no atribuirles cobertura de fills. Pruebas deterministas yAST son evidencia separada.

Evidencia durable en AUDIT_ResearchV5CrossSmoke4h.json y V5_CROSS_PROGRESS.json. Ninguna conclusión económica o cambio de parámetros proviene de la rentabilidad de siete días.