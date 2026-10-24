# Fase 2 — retest LIMIT (no seleccionado en BTC)

Dashboard: http://localhost:9200/#/backtest/5fc3dd4f-2eed-4cbf-b8d5-9e5bc9e7eb8a

BTC-USDT 4h, 2020-02-15 a 2025-12-31. 10000 USDT iniciales, 5x isolated, fee fijo 0.00045, fast_mode=False, warmup 240, curva MTM persistida (2147 puntos). Desarrollo solamente, 2026 sin usar.

Hipótesis predeclarada: tras cierre por encima del Donchian de las 26 barras previas, colocar LIMIT en el borde y permitir únicamente fills posteriores a la decisión; cancelar/reevaluar al siguiente cierre. No se usan touches anteriores para ejecutar. Gestión y sizing del prototipo STOP con reserva por volatilidad (una sola ruta en esta prueba); riesgo máximo planeado 3%, presupuesto agregado 8% y nocional 4.4x.

34 trades (15 ganadores, 19 perdedores), CAGR 18.361230532154703%, beneficio neto 169.42108348172164%, saldo 26942.108348172158, DD diario -17.26003487714296%, Sharpe 0.9955480457732372, Calmar 1.0638003145909067. Menor frecuencia y rentabilidad que el control BTC al 3% (45 trades, CAGR 35.10%). No se escoge por ser LIMIT ni se atribuye ganancia extra maker: el fee simulado se mantiene taker.

Pendiente comprobar utilidad en cartera y cualquier combinación STOP/LIMIT sin seleccionar retrospectivamente fills favorables. Sin Monte Carlo ni validación lockbox. No se inició live/paper.