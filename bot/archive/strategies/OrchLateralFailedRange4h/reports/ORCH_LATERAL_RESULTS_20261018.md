# Resultado: fallo de rango4h descartado como pata candidata

[Corrida terminada](http://localhost:9200/#/backtest/acae5bd3-7f00-439d-991b-7eabbf86b903). Protocolo previo ORCH_LATERAL_PROTOCOL_20261018.md. 2020-10-15→2025-12-31exclusivo,normal,warmup240,10000compartidos,5xaislado,1%riesgo/operación,8%agregado,fee0.00045porlado. 2026 no consultado.

144operaciones83long/61short,0abiertas;saldo10174.5491USDT;neto174.5491;fees1160.5373;CAGR0.33245%;DDmotor−13.5253%;Sharpe0.09278;winrate48.6111%. Top2ganadoras368.8796,mayor que neto total. La ventaja es marginal antes de estrés, no justifica elevar riesgo.

## Componentes: PnL neto, no rentabilidades de cuentas aisladas
|Activosentido|Trades|NetoUSDT|Fees|WR|
|---|---:|---:|---:|---:|
|BTClong|41|754.57|196.32|56.10%|
|BTCshort|30|−53.08|154.13|43.33%|
|PAXGlong|24|−728.98|239.50|37.50%|
|PAXGshort|19|−123.92|221.16|47.37%|
|SPYlong|18|120.88|200.99|55.56%|
|SPYshort|12|205.07|148.44|50.00%|

BTCsumado+701.50,PAXG−852.90,SPY+325.95. Muestras de cada dirección PAXG/SPY son pequeñas; no seleccionar BTClong retrospectivamente como nueva ventaja confirmada. BTCagregado positivo2020parcial/2021/2022/2023/2024,negativo2025;PAXGsolopositivo2022,SPYpositivo2022–24,negativo2021/2025. Todos los activos pierden2025. No construir filtros de esos años.

## Estrés diagnóstico sobre mismos fills y cantidades
Análisis MCP 30d5e6d5cd6d4606b9c67bb9481e2122,succeeded. Notional operado=fee/0.00045. Restar0.0005porlado(+0.10%operacióncompleta) deja neto−1114.9368;restar0.00125porlado(+0.25%operacióncompleta) deja−3049.1656. Es sensibilidad aritmética con cantidades/fillsfijos, no nuevo backtest niCAGR/DDestresados. BTClong conserva209.25bajoestréssevero,pero selección ex post y41operaciones no valida rama. Otras5componentes negativas severo.

## Lectura y decisión
El rejected breakout oscilante tiene ganancias típicas demasiado próximas a sus pérdidas para absorber costes en PAXG/SPY. Targetmidpoint evita exposición tendencial grande, pero también limita premio; no hay evidencia para perseguir umbralesER/stop en cuadrícula. Aún falta diagnóstico MTMexacto deROOT; no presentar meses de cierres de trades como mesesMTM. Incluso si correlaciónconreferencia baja, complementar unedge casinulo/costefrágil no mejora robustez. No promover ni combinar aún. Conservar negativos y datos para atribución.

No segunda variante ni nuevo backtest iniciado. Una alternativa estructural distinta sería estudiar shock relativoBTC/ETHen1hconbeta estimada exclusivamente de retornospasados y reentrada tras recuperación parcial, doslegs opuestos sin asumir cointegración. RequiereETHhistórico,control de ejecuciónconjunta/exposiciónyfeesdoslegs;solo planteamiento,aún noimplementado ni autorizadointernamente. Simplemente cambiar esta pata a1h probablemente agravefricción; no es siguienteprueba justificada porahora.

No cambiosframework/configglobal/live/Pi. Referenciaintacta. SPY/PAXGsiguenproxies; sinvalidaciónfunding/spread/colas. Estado línea: DESCARTAR forma actual y esperar análisis conjunto antesde siguienteestructura.