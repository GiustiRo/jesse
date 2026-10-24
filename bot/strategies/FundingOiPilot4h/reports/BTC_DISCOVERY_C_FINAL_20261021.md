# Cierre C: acumulación de sorpresas y volumen sin progreso
2026-10-21. Dos backtests terminados, sin candidata ni fallos técnicos.

| Receta | CAGR neto | PF | DD M1 + eventos | Meses activos positivos | Trimestres positivos | Trades |
|---|---:|---:|---:|---:|---:|---:|
| [CUSUM BTC](http://localhost:9200/#/backtest/2664ba2b-b192-47ae-95aa-18fd2e6a4d9e) |8,98%|1,153|−19,27%|33/62 (53,23%)|12/20 (60%)|310|
| [Volumen sin progreso y escape](http://localhost:9200/#/backtest/e8af10d8-200f-4d21-b5dd-b59daa7b116b) |−1,12%|0,838|−13,53%|13/29 (44,83%)|4/20 (20%)|40|

Ventana[2020-10-15,2026-01-01)UTC,desarrollo observado. Perfil2%/6%/3x,10kporcuenta,fee0.00045porlado yfunding aplicado;slippage0modelado,sin estrés ni nuevaeconomía2026. Neto no incluye todosloscostosreales.
CUSUM fue transferencia explícita de un mecanismo R40 PAXG negativo a BTC, no método inédito. Absorción fue la hipótesis creativa, sin atribuir flujo real a OHLCV. Protocolos C y addendum de actividad se guardaron antes de ejecutar; no se cambiaron umbrales por resultados.

## Decisión
CUSUM no alcanza CAGR30,PF1.2,M65 oQ80. Absorción falla retorno/PF/regularidad y mediana;ademásN40<100operativo. No descartar sólo por muestra pequeña: hay fallos económicos decisivos. No rescatar quitando shorts ni variando drift/umbral/volumen. Presupuesto C cerrado.

## Medición y contabilidad
Cada ruta observó2.741.760minutos y eventos de ejecución. Se obtuvieron63intervalos mensuales (octubre2020parcial) y62mesescompletos,20trimestrescompletos. Equity=wallet+position.pnl,sinvolveramultiplicarporapalancamiento; las nuevas estrategias no usan portfolio_value abierto.
Cortes00:00UTC después del funding y antes de decisiones. Es una convención exacta por fase: fundingde00:00se asignaalintervaloqueacaba,noPnL porfecha[a,b)estricta. Actividadincluyeexposición ymesdeejecuciónconcriterioconservador;ceroscalendarionoseocultan. DDdeM1+eventosno sonextremosintraminuto.
Mediansmensualesde62meses: CUSUM+0,1714%,absorción0%. Netoaritmético sin2mejoresmeses:+2179,50/−1465,11USDT. Cumplir una puerta no rescata fallos en otras.
Contabilidad mediante run_analysis d4409ec183fe4e2cb54a3b10696f2dd3 con310/40tradescompletos. Bruto−fees+funding=sumPNL=saldo−10000,tolerancia1e−6;error máximo1,37e−11USDT. Funding−199,90/−14,72USDT,fees2543,02/236,92USDT;appliedtrue ydatasetcorrecto. Pagosconmarcaproxy777/81,provenanceconservada. Ambosrawopencounter0 ytelemetríafinalreconciliada.
Los summaries de telemetría son resultados emitidos por la estrategia y las63filas por cuenta se recuperaron completas delbloquefinal, aunque haya logs anteriores no incluidos en esa página;no son totales de trades calculados desde página parcial. Se conservanlosreciboscompletos ycontabilidadindependiente de snapshots.

## Continuidad
Se registró D,otra pregunta concontrol: canal en bloques de volumen frente a bloques calendario. No se usan CUSUM/absorción como finalistas. DnoesunavecindaddeCniunasegundapruebaciega;permisoautónomo vigente,riesgo/costos fijos.
Fuentes: BTC_DISCOVERY_C_PROTOCOL_20261021.md, ACTIVITY_ADDENDUM, MANIFEST, ACCOUNTING y archivos TELEMETRY por estrategia, todos bajo reports/. Clases nuevas y helpers anteriores congelados. No tocarframework,globalconfig,Pi,paper/live.
