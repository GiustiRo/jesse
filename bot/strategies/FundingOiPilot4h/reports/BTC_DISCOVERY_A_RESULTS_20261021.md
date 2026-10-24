# Cierre tanda A — BTC individual
Dos recetas nuevas ejecutadas bajo protocolo previo BTC_DISCOVERY_A_PROTOCOL_20261021.md. Ventana2020-10-15→2026-01-01exclusiva,desarrollo yaobservado. Cuenta10kporreceta,2%/6%/3x,fijo fee0.00045+fundingON,slippage0modelado,sin estrés.

| Receta | CAGR | DD reportado diario | PF neto | Trades | Neto período | Decisión |
|---|---:|---:|---:|---:|---:|---|
| [Amplitud de signos](http://localhost:9200/#/backtest/438b717c-7b5e-4589-a84a-687fa63f8645) |11.5920%|−14.5163%|1.47268|193|+77.2049%|NO_CUMPLE: CAGR<30%.|
| [Fallo post-funding](http://localhost:9200/#/backtest/b3fa7fff-0b6b-44de-ac23-230c118a94b0) |−7.5665%|−35.2419%|0.89566|454|−33.6639%|NO_CUMPLE: CAGR/PF/DD.|

Neto de comisiones yfunding modelados,no de todosloscostosreales. Fundingsignos−574.5431USDT,postevento+894.6158;confirmadoappliedtrue ydatasetcorrecto,efectivofastfalse. Fee1556.0649/2251.3714. Pagosconmarcaproxy513/1207: no confundir con4198proxies delsnapshotcompleto. Efectovíaqty/saldomodelado,noobservaciónvenue.

## Contabilidad completa
run_analysis d5e3e557906a4af5917de4122d74399c recibió193y454tradescompletos y1905puntos equityporlibro. Comprobó bruto deprecios−fees+funding=sumPNL=finishing−10000,PF yCAGRrecalculados. Máximoerrorcontable3.19e−11USDT<tolerancia1e−6. Totalopen0segúnmotor. No se sumaron páginas parciales. Primera inspección8ef4e9ad195c4dc98aae8071d6e49b2a no produjoartefactospersistentes;laauditoríacompleta posterior sí.

## Límites del muestreo identificados
Auditoría del framework: max_drawdown se calcula sobre daily_balance, porloqueestosDD sonmuestreadosdiarios;no certifican elmáximointradiario. La frase deprotocoloA que sugeríaDDmotor distinto deldiario se aclara conesta evidenciayprotocoloB;no cambiarechazoA.
Equityguardada00:01UTCmásinicial/terminal. Monthly_approx_only yannual_approxdelJSON usanese muestreo;no se venden comocortes00:00exactos paraacreditarM65/Q80/medianayconcentración. Descriptivamente,signos33/59mesesactivoscompletospositivos,evento28/62;no sonpuertasexactas aprobadas. No gastarotromotorpara fabricarcomparabilidad;ambosya fallanretornoobligatorio.

## Aprendizaje y decisión
Elconteodesignos produjoexpectativapositivacondesplieguecomún,pero no la rentabilidadexigida. No subirriesgo,quitarshortssegúnatribuciónni variarumbrales.
Lareceta creativa postfundingfallóinclusoconfundingnetofavorable. No invertirdirecciónocambiarventana despuéspararescatar.
Una iteraciónBseprerregistródespuésdeA:transferirgestiónsinTP/salidaestadoopuesto/30d a entradasBreadth, controlAreutilizado. Contrasta unapolíticacompleta,nopruebaqueTP/48hcausaraelfalloA. VerBTC_DISCOVERY_B_PROTOCOL_20261021.md;noalterarestecierre.

## Trazabilidad
BTC_DISCOVERY_A_MANIFEST_20261021.json preservacódigoSHA256/configdraftprevia/fundingID/checkjob. AST/purefunctions pasaron;unarevisiónseparadacontrastóreglas. Elcampo checks23 deldiagnósticosintético esunconteodeclarado,nouncensodinámicodeasserts ni muestrasde mercado;no se usa comoconfianza.
Resultados completos: BTC_DISCOVERY_A_RESULTS_20261021.json. Auditorías/curve/CSVaproximados deljob fueronrecuperadosporMCP;sin research_scripts,imports,estrés,globalconfig,live/paperoPi.
