# Asignación con reloj común — resultado inicial
Dashboard: http://localhost:9200/#/backtest/9bbd9545-2154-4842-8902-8c926c7a4a56
Referencia: http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb
## Hipótesis y método
Ver ORCH_ALLOC_PROTOCOL_20261018.md guardado antes del run. Único cambio económico: techo nocional por inversa volatilidad20 retornos en21 timestamps comunes (buckets4h16UTC,cierre20UTC). Riesgo3%/8%,global4.4x y margen90%,señales/gestión sin cambios. Rutas BTC/PAXG/SPY4h;longs tres,shortBTC;10k/5xisolated/fee0.00045todasórdenes,warmup240,normal replay,2020-10-15→2025-12-31exclusivo.2026reservado.
## Resultado
222 operaciones (97long/125short); neto+19,595.973990USDT (+195.959740%); saldo29,595.973990; CAGR23.135580%; DDmotor−14.171011%; Sharpe1.198382;fees3,375.794438USDT;0posicionesabiertas.
Referencia:220operaciones,neto+27,461.463375,CAGR28.829387%,DD−14.890506%,Sharpe1.316428.
Cambia exposición y posiblemente admisión de señales por presupuestos, no señales brutas. Mantiene97longs pero suma2shorts por contexto de capacidad.
## Verificación de fuente/invariantes
Fuente guardada releída idéntica. Todos los timestamps deben existir en las3series; celdas observadas, ningún fill de días/velas; estrictamente t<closed_candle_open_time para eliminar dependencia de actualización de la barra actual. Requiere21cierrescomunes o rechaza. No datosdiarios/warmup2019 inexistente. Sin librerías/red/RNG. Conserva mismo ledger pendiente/open ycomisiones/reserva.
El calendario usa muestras20UTC,no empareja cierres económicos exactos por zona local ni garantiza días consecutivos: los huecos se mantienen y esos retornos multiday se comparten entre símbolos. Horarios SPY/fuentesproxy todavía son limitaciones.
## Datos pendientes y decisión
Calendario MTMv3, aportación por dirección/activo, riesgo realizado, costes yperiodos quedan para el análisis conjunto del orquestador. NO estimar esos resultados a partir de muestras00:01. No aprobada; el menorDDconmenorretornonodemuestra mejor regularidad. Mantener referencia congelada. Sin cambios framework/live/config.
