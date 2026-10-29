# X03 R3 — atribución de N204 frente a X03

La mejora observada combina sustitución de operaciones de peor resultado y diferencias de cantidades en las operaciones compartidas. **Las operaciones añadidas pierden neto en los cuatro contrastes.** No aparece una mejora del PNL por unidad en las operaciones retenidas: sus precios/recorridos de salida coinciden, y el cambio monetario procede de cantidades. Esta identidad contable no identifica un efecto causal puro de la referencia VWAP ni un alpha nuevo.

Job b7aee9a90c834d05ba7c5015ff39755d succeeded,2026-10-19T16:45:43Z→16:45:47Z,exit0. Ocho inputs de sesiones finished, tarifas verificadas .00045 nominal y.00070 por lado en reejecuciones de motor. Ventana2020-10-15→2025-12-31exclusivo;2026 cerrado. Sin datos nuevos, nuevos backtests, filtros o refit. Riesgo1%/8%,10000USDT,isolated5x. Fuente congelada del análisis: X03_R3_ATTRIBUTION_SOURCE_20261019.md, enesta carpeta.

## Las ocho referencias

- [nom_X_B](http://localhost:9200/#/backtest/53937852-34a3-48c7-ab35-fac586341127): 273trades, neto11964.238131USDT.
- [nom_X_C](http://localhost:9200/#/backtest/3935efb3-2b27-4ada-86ce-94123d7a6e2c): 280trades, neto12135.876834USDT.
- [nom_N_B](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142): 273trades, neto13056.614915USDT.
- [nom_N_C](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794): 280trades, neto13239.442380USDT.
- [fee_X_B](http://localhost:9200/#/backtest/1277ad3f-21b3-41d7-9c04-9485dec1f907): 274trades, neto9344.147577USDT.
- [fee_X_C](http://localhost:9200/#/backtest/24e0fc97-92d3-4b55-8c19-afc149e9f993): 281trades, neto9420.867003USDT.
- [fee_N_B](http://localhost:9200/#/backtest/9a6c7c24-8847-42d1-aadb-206f21723c1f): 274trades, neto10267.311379USDT.
- [fee_N_C](http://localhost:9200/#/backtest/541d2bf4-ffca-4f2d-969b-c25165e7b960): 281trades, neto10408.935274USDT.

## Identidad monetaria exacta

Emparejamiento único por símbolo/dirección/opened_at; identificación BTCshort MARKET=suplemento ySTOP=original mediante orden ejecutada. Cada fila retenida usa u=PNLneto/qty y la identidad simétrica Δ(q*u)=Δq*(uN+uX)/2+Δu*(qN+qX)/2. Las eliminadas aportan menos su PNLX real; las añadidas su PNLN real. Se conciliaron fills, cantidades, fees, PNL, wallet y cierres terminales de las8sesiones, sin precios diarios ni auditoríaMTM duplicada.

|Contraste N204−X03|Retenidas|Eliminadas/añadidas|−PNL eliminadas|PNL añadidas|Cantidad retenidas|Unidad neta retenidas|Δneto|
|---|---:|---:|---:|---:|---:|---:|---:|
|nom_B|256|17/17|724.399036|-24.514635|392.492383|≈0 (1.28e-11)|1092.376784|
|nom_C|263|17/17|719.400308|-19.637654|403.802892|≈0 (5.21e-12)|1103.565546|
|fee_B|257|17/17|733.849844|-54.416659|243.730617|≈0 (9.41e-12)|923.163802|
|fee_C|264|17/17|731.149062|-46.043996|302.963205|≈0 (-7.20e-12)|988.068271|

En cada contraste se sustituyen15 suplementosMARKET y2shorts originalesSTOP; se retienen64 suplementos,111STOPoriginales,31longBTC ytodosloslongPAXG/SPY (38PAXG nominal,39confeealto;12SPYB/19SPYC). Los17añadidos y17eliminados son eventos ejecutados observados, no todaslas señales potenciales. No inferir señales bloqueadas no registradas.

## Pérdidas incluidas

|Contraste|Añadidas ganadoras/perdedoras|Neto añadidas|Bruto añadidas|Fees añadidas|Eliminadas ganadoras/perdedoras|Neto eliminadas|
|---|---:|---:|---:|---:|---:|---:|
|nom_B|8/9|-24.514635|53.545928|78.060564|6/11|-724.399036|
|nom_C|8/9|-19.637654|57.692278|77.329932|6/11|-719.400308|
|fee_B|8/9|-54.416659|60.577552|114.994211|6/11|-733.849844|
|fee_C|8/9|-46.043996|67.953273|113.997270|6/11|-731.149062|

Las añadidas tienen bruto positivo antes de fees, pero pérdida neta después. Las retiradas contienen6ganadoras y11perdedoras y pierden también antes de fees. No describir la intervención como añadir17buenas operaciones ni eliminar17malas. Aumentar cantidades en compartidas amplifica tanto ganancias como pérdidas; sus sumas perdedoras se conservan en elJSONporgrupo.

## Distribución por familia de operaciones

|Contraste|Familia|Retenidas|Eliminadas/añadidas|Efecto cantidad retenida|Sustitución neta|Δtotal|
|---|---|---:|---:|---:|---:|---:|
|nom_B|BTC original long|31|0/0|91.981969|0.000000|91.981969|
|nom_B|BTC original STOP|111|2/2|73.207166|25.855707|99.062873|
|nom_B|BTC supplemental MARKET|64|15/15|74.724251|674.028694|748.752945|
|nom_B|PAXG-USDT original long|38|0/0|101.173343|0.000000|101.173343|
|nom_B|SPY-USDT original long|12|0/0|51.405653|0.000000|51.405653|
|nom_C|BTC original long|31|0/0|90.103600|0.000000|90.103600|
|nom_C|BTC original STOP|111|2/2|71.688205|32.481689|104.169894|
|nom_C|BTC supplemental MARKET|64|15/15|82.182241|667.280965|749.463206|
|nom_C|PAXG-USDT original long|38|0/0|102.909802|0.000000|102.909802|
|nom_C|SPY-USDT original long|19|0/0|56.919045|0.000000|56.919045|
|fee_B|BTC original long|31|0/0|45.463490|0.000000|45.463490|
|fee_B|BTC original STOP|111|2/2|41.966674|19.303684|61.270358|
|fee_B|BTC supplemental MARKET|64|15/15|75.780140|660.129501|735.909641|
|fee_B|PAXG-USDT original long|39|0/0|41.171420|0.000000|41.171420|
|fee_B|SPY-USDT original long|12|0/0|39.348893|0.000000|39.348893|
|fee_C|BTC original long|31|0/0|81.459500|0.000000|81.459500|
|fee_C|BTC original STOP|111|2/2|52.845306|23.162177|76.007483|
|fee_C|BTC supplemental MARKET|64|15/15|77.987299|661.942889|739.930188|
|fee_C|PAXG-USDT original long|39|0/0|44.090756|0.000000|44.090756|
|fee_C|SPY-USDT original long|19|0/0|46.580345|0.000000|46.580345|

El subtotalMARKETnominal gana748.752945B/749.463206C; confeealto735.909641B/739.930188C. El subtotalSTOPoriginal gana99.062873/104.169894 nominal y61.270358/76.007483 confeealto. LoslongoriginalesBTC/PAXG/SPY ganan en conjunto244.560965B/249.932446C nominal; esas diferencias proceden de cantidades observadas, no de nuevas reglas ni nuevos retornos unitarios en esas patas.

## Ocupación, costes y tamaño endógeno

|Sesión|Alguna posición%|Notional×time/equityinicial|FeesUSDT|Trades|
|---|---:|---:|---:|---:|
|nom_X_B|38.522253|0.422385624|1877.503730|273|
|nom_X_C|40.854024|0.476342165|1974.478329|280|
|nom_N_B|38.616475|0.437018817|1912.864654|273|
|nom_N_C|40.957005|0.492654155|2012.424224|280|
|fee_X_B|38.306877|0.379707655|2694.702460|274|
|fee_X_C|40.638648|0.427204448|2822.955059|281|
|fee_N_B|38.401099|0.391959292|2740.006654|274|
|fee_N_C|40.741629|0.441734276|2877.907745|281|

Notional×time integra cada slice ejecutado al precio de entrada sobrelas horasreales, dividido por10000USDT ytiempo total; no mark-to-market nocional actual ni exposición contrafactual. Alguna posición esunión de intervalos de toda la cartera; los solapamientos se cuentan una vez. Las8cuentas son compartidas: capital, ocupación, límitesnocionales, cuotaATR yredondeo participan enel sizing. El término cantidad no separa sus causas individuales y no prueba que todo sea compounding. No se reconstruyeron presupuestos de riesgo disponibles en cada decisión.

Lasfee.00070 son corridas nuevas delmotor sobre reglasoriginales, no overlays. Cada unadeellas conserva todoslos horariosdeentrada nominal y añadeuna entradaPAXG; también pueden cambiar salidas y cantidades porla dependencia de gestiónrespecto fees. La rondaR3fixedBE deotroagente investiga ese mecanismo; este informe no adelanta resultados niatribuye la caída a coste directo solamente.

## Evidencia y límites

X03_R3_ATTRIBUTION_EXACT_20261019.md conservaJSONcompleto49.9kB, manifest8inputs, grupos, pérdidas ydiagnósticos. El primer volcadoALL_TRADES se etiquetó erróneamente completo pese truncated=true cerca64KiB; se corrigió de inmediato. Root autorizó jobcorrectivo de presentación b2d5bd2e153a4d4389a465360fbef55a, succeeded16:48:08Z→16:48:11Z, con mismos8inputs ymatemática. SuJSONeconómico esexactamenteidéntico aloriginal. Se recuperaron12partesCSV<=40kB,truncated=false,tamaños/conteosverificados yhashfull=hashconcat enmanifest. X03_R3_ATTRIBUTION_ALL_TRADES_20261019.md fue reemplazado porlas1176filas completas(290/297/291/298),incluidos perdedores, másmanifestSHA256. Sin nuevascorridaseconómicas. ElPNGwaterfall se generó, pero dosintentos depreview devolvieron artifact_changed pesejobterminal; no seafirma previewverificada ni seutilizó otroacceso.

Todoslosretainedunit≈0 son residuos numéricos1e−11USDT, no edge detectable. Igualdaddehorarios/paths noimplicaigualriesgomonetario. Mejora neta de cuenta no demuestra mejorabilidad futura, regularidad bajo costes, diversificaciónnueva ni validación independiente. B/C compartenmuestra yBTC;2020–2025sigue desarrollo reutilizado. No se suman curvas independientes ni se construye un counterfactual deqtyfija. Los calendariosMTM yla prueba de fixedBEquedan a cargo deroot.
