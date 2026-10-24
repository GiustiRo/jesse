# Diagnóstico independiente y propuesta acotada

Estado: diagnóstico terminado; ningún backtest nuevo ejecutado. Referencia intacta, 2026 cerrado. Desarrollo 2020-10-15→2025-12-31 exclusivo, ampliamente seleccionado. No se reinicia historial de hipótesis.

## Datos y método

Referencia [dashboard](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb); contraste [roles combinada11](http://localhost:9200/#/backtest/2ca17713-06a5-42ea-8956-6de60653e2a5).

Leí registros ORCHESTRATION_RESEARCH_LEDGER, BTC_NEW_ANGLES_RESULTS, PHASE2_PORTFOLIO_DIAGNOSIS, PORTFOLIO_ROLES_STAGE_PROTOCOL y PORTFOLIO_ROLES_RESULTS de18octubre. No los trato como evidencia fuera de muestra. Consulté código baseline, MultiAssetSleeves4h y OrchManageFastMrBtc4h. La documentación DOCS tiene decisiones antiguas2%/BTCsolo que están superadas por autorización explícita3%/8% ycartera.

Snapshot independiente a762f055a07f4df1b78dd6a88236a92c succeeded verifica estructura. Análisis independiente5e4cf8e7d9fe49309d42c75246de9b9a succeeded, artefacto portfolio_efficiency.json, calculado conTODOS trades de ambas sesiones. Se normaliza neto por suma de nocional inicial y por suma de nocional inicial×horas reales. No es retorno de cartera, rentabilidad anualizada ni counterfactual de eliminar trades. Los tamaños endógenos de cuenta compartida afectan cocientes. No se calculó PnL por mes de cierre.

## Hallazgos nuevos

|Componente|N referencia/11|Neto bps sobre suma nocional entrada referencia/11|Neto USD por millón nocional-hora referencia/11|
|---|---:|---:|---:|
|BTC long|31/31|296.583/325.764|174.757/192.751|
|BTC short|123/125|31.791/29.409|171.139/159.078|
|SPY long|31/123|24.324/5.552|11.833/3.122|
|PAXG long|35/73|31.705/9.088|19.097/15.793|

Comisiones observadas~9bps por roundtrip sobre nocional inicial. Margen neto5.552bpsSPY/9.088bpsPAXG es el coste extra agregado sobre mismos fills que agotaría el beneficio realizado de esa pata; no es stress test ejecutado. Impacto, funding, spread y cambio de decisiones pueden empeorar/diferir del cálculo. No aplico un precio de funding supuesto.

SPY11 ocupa23768.78horas versus6971.42de referencia y815.68Mnocional-horas versus309.33M. Su neto cae3660.42→2546.79USD; no hay evidencia de que mayor participación sea el ingrediente faltante. PAXG11 también reduce neto4632.27→2546.98USD. BTC conserva comportamiento por trade prácticamente, pero su tamaño cambia.

MTMya reconciliado en722aa973845c4c89b6acfe9eff63ce0e fue consultado directamente: correlaciones mensuales poractivo casi0en referencia no garantizan cola complementaria.11PAXG-SPY−.217 tampoco evitaDD−26.93%. Los porcentajesmensuales/trimestrales no permiten promover11. BTCrunner sigue siendo aportador principal; exigirle salida rápida no es remedio natural.

Juicio: la arquitectura combina mayormente fuentes de payoff asimétrico y con poca frecuencia; sustituirlas por actividad sin edge convierte capital-tiempo en turnover. Falta demostrar una expectativa corta, neta y estable, no simplemente añadir exposición ni optimizar correlaciones históricas. La especialización debe ser económica y temporal, no un nombre diferente sobre la misma señal.

## Propuesta antes de código: SPY recuperación diaria de pullback

Hipótesis, sin evidencia afirmada: una caída breve de renta variable dentro de tendencia alcista seguida de recuperación puede expresar reversión por provisión de liquidez; su horizonte corto podría complementar los runnersBTC. Sólo cambiarSPY; BTC/PAXGreferencia, cuenta compartida. No hay garantía de mejora, ni se seleccionan meses negativos.

IMPORTANTE duplicación: MultiAssetSleeves4hYAcontieneSPYMR conRSI3<=20,macroEMA120, targetEMA20y5d; además cambióotrosactivos/asignación. La propuesta diaria pertenece a la misma familiaeconómica y cuenta como nueva variante adaptativa, no descubrimiento independiente. OrchManageFastMrBtc4h esMRBTC4h ya fallida. Necesario revisar resultados exactos de sleeves antes de gastar un full.

Recipeprovisional para revisión root, no congelado ni autorizado para run: observaciones hábiles16UTC con quoteM1estrictamenteasof,serie diaria de16UTCsin imputar holidays ni velas faltantes. Precio sobremedia200observaciones,descenso acumulado3observaciones yprimer cierre que recupera el previo, estando bajo media10. EntrarMARKETsólo con cotización fresca;targetmedia10dinámica mediante salidaMARKETen observacionesválidas;stop2ATRdiario inicialdesde fill;máximo5observacionesválidas,con deuda de salida hastaquotepropiafresca. Stops siempreactivos. Riesgo3%trade/8%agregado,5xaislado/gross4.4,fee.00045porladoTODASórdenes;compartirledger original y respetarshareATRpara no convertir asignación en segunda hipótesis. Sin piramidado, trailing ni retocarumbrales trasresultado. Debe especificarse qué constituye sesiónválida y verificarhistory200antes de congelar;startupcashincluido y warmup no inventado.

Revisar si3sesionesyrecuperación juntos duplican demasiados filtros: son diseño propuesto, no selección por resultados. Debe existircontrol de quote/paridad y revisión técnica antes de1full económico. No usarM1para fabricar footprint ni volumenSPY.

Aceptación:65–70%mesesactivospositivos,80%quarters,DD<=25%y rentabilidad útil resistenteacostes. Reportartodos/calendariocompleto,conteos,exposición,distribuciónpayoff,costeextraagotador,concentración y mesesdeterioradosademásderescatados. Si falla, no barrerSMA/ATR/días; conservar fallo. MCsólo después sihaypromesa, conservando dependencias conjuntas ylimitaciones deejecución.

No scripts, datasets nuevos, instalaciones, cambiosframework, reinicios, fondos, live/paper ni2026. Diseño enviado aroot antes de cualquierbacktest.

## Control adicional de duplicación: evidencia anterior revisada independientemente

[MultiAssetSleeves4h motor corregido](http://localhost:9200/#/backtest/262fb59f-2b20-4247-aa9a-e7823cc3c930) terminado. Su SPYMR produjo86trades,neto−5148.175368USD,fees2834.828737USD yantesdefees−2313.346631USDsobre esosfills.35ganadores,1919.9horas,Neto−16.3384bpssobre sumanocionalentrada. Validación independiente por snapshot en398f14c4d76e422b953bb9fd63591020 succeeded/exit0,artefactospy_prior_mr.json. La variante diaria propuesta tiene sólo justificación de horizonteejecución diferente; no evidencia positiva deMR. Recomendación porahora: no gastarfullautomáticamente. Primerocongelar mecanismo/contraste que justifique revisarMRy revisar disponibilidad diariaasof; si no hay razón adicional, retirar la propuesta antesderun,registrando el descarte deidea. No bajarRSI/stops/díaspararescatarla.
