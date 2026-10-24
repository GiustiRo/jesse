# Presupuestos iguales de riesgo — resultado inicial
Dashboard: http://localhost:9200/#/backtest/72996434-7c02-4589-9400-42a23229ae02
Referencia: http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb
Comparador sin techoindividual3%: http://localhost:9200/#/backtest/9f7ac256-699a-4e4d-9d4d-a639c0158a85
## Hipótesis y método
Protocolo ORCH_ALLOC_PROTOCOL_20261018.md guardado antes del run. Presupuestos de riesgo3activos:8%/3=2.6666667% por posición; única posición/pending por símbolo ysinpiramidado. Techoindividualnocional retirado; global8%riesgo/4.4xnocional/90%margen sin cambios. Señales/gestión idénticas. BTC/PAXG/SPY4h;long3shortBTC;10k/5xisolated/fee0.00045todasórdenes;normalreplay,warmup240,2020-10-15→2025-12-31exclusivo.2026reservado.
## Resultado
219trades97long/122short,neto+32114.454825USDT(+321.144548%),saldo42114.454825,CAGR31.755093%,DDmotor−17.683970%,Sharpe1.206608,fee7371.262090,0open.
Referencia:CAGR28.829387%,DD−14.890506%,Sharpe1.316428,net27461.463375,220trades.
Sin techoindividual3%:CAGR37.43%,DD−18.42%; nuevo presupuesto reduce retorno yDD respecto a esecomparador.
## Verificación y limitaciones
Fuente releída idéntica al código preparado; constanteTRADE_RISK8%/3 y_volatility_share1.0 son únicos cambios económicos. _committed/ledger/calculoriesgo desde marca/reservapendiente/fee/slippage de sizingconservados. _signalcache y gestión1entrada1salida sin cambios. Límite de admisión NO implica capcontinuo trasmoverprecio/gaps.
Asignación8%/3 presupuesta en admisión por activo; riesgo desde marca puede variar en posiciones abiertas. No se presta el presupuesto de riesgo inactivo porencimade2.667, pero el nocionalglobal sí secomparte. La prioridad de escasez de margen/grossglobal no desaparece.
## Datos pendientes y decisión
MTMv3mensual/trimestral, aportación/activo/dirección,costes yperíodos se obtendrán en análisis conjunto del orquestador. No afirmar regularidadporCAGR oSharpe. Estrategia no aprobada, referencia intacta. No frameworks/live/config.
