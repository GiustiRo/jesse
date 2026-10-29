# V3 — Verificación técnica previa a screening

164 comprobaciones deterministas aprobadas; 15 fuentes compiladas y congeladas en V3_IMPLEMENTATION_SOURCE_20261020.md. Tres smokes únicos 2020-09-01 a 2020-09-08 finished sin error de motor. No se usó su rentabilidad para seleccionar ni ajustar reglas.

- CHANNEL: http://localhost:9200/#/backtest/cad4e9cd-a835-4a0b-afc6-5fb95749c1e4 — 2 entradas/cierres, stop y cierre final; 10 actualizaciones de trailing favorables.
- PULLBACK: http://localhost:9200/#/backtest/fb493cec-e17d-42f0-87d8-c74e953611ae — 2 entradas/cierres, stop y cierre final.
- RANGE: http://localhost:9200/#/backtest/7fcfb052-a9b8-4a9b-bc7f-2add6e3dd278 — 3 entradas/cierres, 2 stops y 1 objetivo SMA20 congelado.

Conciliación independiente sobre tres snapshots completos, job a4b9e46f500b4384b8431709fb5ae121: PNL bruto menos comisiones más funding igual PNL neto, comisiones por fills y saldo final; máximo error 3,64e-12 USDT. Capital 10000 y leverage 3/config nominal verificados, fast_mode efectivo false. Dos timeouts de respuesta de inicio se resolvieron leyendo los mismos IDs; sin duplicaciones.

Las métricas total_open_trades/open_pl en los dos primeros smokes describen el instante anterior al cierre final automático. No son posiciones todavía abiertas: snapshots de trades y saldo final ya incorporan los cierres. DDmotor es el gate prerregistrado; informar también límites de muestreo/equity terminal sin sustituir silenciosamente la definición.

Cobertura real incompleta: máximos de tenencia, trailing cruzado y gate OI habilitado no ocurrieron en todos los smokes; corresponden pruebas deterministas y auditoría posterior. Funding puede superar el presupuesto stop+fees del 2%; no se modificó sizing ni reglas tras observarlo. RANGE sí ejercitó takeprofit. Auditorías sectoriales conservan evidencia y raws.

Habilitada fase SCREEN de seis variantes con reglas/config/hashes ya fijados, hasta dos motores globales, sin abrir 2024–25 para selección ni 2026.