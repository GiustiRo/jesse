# Handoff Fase2 — carteras de candidatas completadas — 19/10/2026

Leer PORT_CANDIDATES_RESULTS_20261019.md y EXACT_AUDIT en esta carpeta. Cuatro variantes económicas y cuatro réplicas debug de captura, todas finished; análisis terminados, sin más runs autorizados/pendientes de esta tarea.

Cuenta10k compartidos/1%trade/8%agregado/5xisolated/cap4.4/fees.00045side/reserva.001sólosizing. Ventana2020-10-15→2025-12-31exclusiva.2026cerrado. Se normalizó BTC3%→1%sin tocar señales/gestión. CONTROL no replica la cartera antigua3%/28.83%CAGR, sino referencias frescas a1%. No aumentar riesgo o comparar directamente retornos del control antiguo.

| Cartera | PAXG/SPY | Neto | CAGR | DDmotor | Meses+ completos/activos | Q+ completos |
|---|---|---:|---:|---:|---|---|
| CONTROL |Cq/Cq|7815.59|11.71%|−8.54%|33/59=55.93%|13/19|
| A |M/Cq|8527.17|12.56%|−7.43%|35/59=59.32%|14/19|
| B |M/MECH01|9234.19|13.37%|−7.50%|37/57=64.9123%|16/19|
| C |M/MECH05|9407.83|13.56%|−8.17%|38/57=66.67%|16/19|

C supera65%activos y80%Q sólo en completos; incluyendo fronterasparciales queda38/59=64.41%mesesactivos y17/21Q=80.95%. B con parciales37/59=62.71%. No redondear B64.91a65 ni aceptarCignorando parciales. CAGR inferior a20–30%aspiracional. Objetivo global no alcanzado; sin promoción.

C candidata por neto/regularidad; B alternativa por eficiencia/menorDD/Sharpe. Diferencia C−B173.63USDT en toda ventana, pero mayorfee91.85 yconcosteextra10bps diferencia sólo71.58. Todas carteras conservan neto con costes, ex3 y castigo conjunto estático. Ninguna validación OOS limpia.

BTC156trades en cada cartera,31long125short; timestamps/dirección exactos yprecios equivalentes conmáx2.91e-11USDT, cantidades/PNL endógenos. Recortes observadosBTCshort18–19 por nocional/peso, ningún plan flat que llegara a sizing con capacidad nula/margen/riesgoagregado8% insuficiente. No inferir oportunidades mientras ocupado. Cuentos capturados por12JSONde4réplicasdebugtrue; originalesdebugfalse no persistieronlogs.

Réplicas tienen hashesexactostrades4/4;curvasB/Cexactas,CONTROL/A máxima diferencia3.64e-12USDT; mismo1904timestamps. Auditoría concilia fills/fees/PNL/wallet/MTM;C tiene forcedboundaryconciliado, no prueba liquidez.48checksAST de ledger/diagnóstico pasaron. No se tocaronframework/configglobal/datos/instalaciones/live/Pi/research_scripts.

Próximo foco sugerido: BTCshort selectividad/fricción dentro de carterasB/C, preservando runnerslong. Cshortnet1251.49/fees661.42; +10bpsRT516.58. Aporta en2022, no eliminarlo sin contraste. En peores meses2021short ylong coinciden en pérdidas:agostoB−4.3935%,short−2.6912,long−1.7023puntos;abrilC−4.6955%,short−1.9877,long−.9515. Años son diagnóstico, no filtros. Definir nueva hipótesis antes de ejecutar, no rescatar SPY/PAXG con tuning.

Sesiones primarias:
[CONTROL](http://localhost:9200/#/backtest/5cead429-3356-437b-b03d-9e861f10974e)

Dashboard: http://localhost:9200/#/backtest/5cead429-3356-437b-b03d-9e861f10974e

[A](http://localhost:9200/#/backtest/5fb1aa55-6ed3-4ac4-bb84-08e82dad3d49)

Dashboard: http://localhost:9200/#/backtest/5fb1aa55-6ed3-4ac4-bb84-08e82dad3d49

[B](http://localhost:9200/#/backtest/29387384-c48c-4ac9-94bd-632a2ec3bb7f)

Dashboard: http://localhost:9200/#/backtest/29387384-c48c-4ac9-94bd-632a2ec3bb7f

[C](http://localhost:9200/#/backtest/30ab3788-51bb-4435-8c21-9b12c45f8835)

Dashboard: http://localhost:9200/#/backtest/30ab3788-51bb-4435-8c21-9b12c45f8835


Fuentes nuevas congeladas: PortCompareBtc4h, PortComparePaxgRetest4h, PortComparePaxgMarket4h, PortCompareSpyRetest4h, PortCompareSpySecond4h, PortCompareSpyMarket4h; originales intactas. Cada sesión guarda sus tres snapshots. Informes fuentes/QA/análisis/capacidad porMCP en esta carpeta. ImagenPNG no se pudo inspeccionar por artifact_changed; no afecta auditoría numérica. No hay nuevos experimentosBTC corriendo ni2026consultado.
