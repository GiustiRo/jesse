# X03 R3 — fixedBE ejecución y divergencias observadas

Ocho backtests finished sinerrores. Cuatro nominales coinciden exactamente con referencias en273/280trades cadaBTC (PNLportrade0diferencia);QA59succeeded. Rootleyóclon antes tickets. Todosforms y24snapshots exactos pre-run,originalPAXG yclon releídosbyteexactos al cierre.2026cerrado. No se cambió ninguna señal ni se seleccionó pisoBE por PNL.

|Parfee.00070|Neto fixed|ΔvsBEreal|CAGR|DDmotor|
|---|---:|---:|---:|---:|
|[FBS0B](http://localhost:9200/#/backtest/9bebb1e9-d0a0-4d74-a530-76c852c18d3a)|10220.330399|876.182822|14.459258|-8.284311|
|[FBS0C](http://localhost:9200/#/backtest/b97e3a45-d5df-4bc5-97c1-cb9ab56fdd18)|10264.855982|843.988979|14.507557|-9.125162|
|[FBS1B](http://localhost:9200/#/backtest/931bc4d2-d12d-4e93-a2d0-7bc2f23daa44)|11175.994090|908.682711|15.477568|-9.027062|
|[FBS1C](http://localhost:9200/#/backtest/2fd1c355-c50b-4851-921b-3e6432925b31)|11327.398216|918.462942|15.635473|-9.073367|

N204−X03 a fee.00070 es+955.663691B/+1062.542234C bajo fixedBE, frente+923.163802/+988.068271 conBEreal; diferencia de diferencias+32.499889/+74.473963. Contraste de implementación condicionado al simulador/muestra, coninteracciones de capital; no efecto universal ni purocostedirecto. TratamientooficialsiguesiendoPAXGoriginal,contrafactualnoelegiblereemplazo. RootcentralizaMTM/MQ ycriterios.

La primera ejecución PAXG distinta observada en los cuatro pares corresponde a la entrada2020-12-27T12:00Z: STOPdinámico1929.0799925ejecuta2021-01-06T18:21Z; fijo1927.87642375ejecuta2021-01-08T08:01Z. Laqtyinicialesidéntica dentrocada par. El cierre nominalnetopequeñopositivo del dinámico se vuelve negativo en fijo:2.004508→−1.585028B,2.002359→−1.583329C. No se filtran efectosadversos.

Jan2025 es el granefectoeconómico, no el primer cambio: entrada3ene04Z sobre2661 sale antes conBEreal2665.65675;fixedla conserva hastatrailing2832.535238. Esa posiciónocupadadesplazauna reentrada22ene12Z ganadora189–201USDT delcontrol. PAXG39→38trades,38entradas retenidas,36 salidasretenidas,1entradaeliminada y0nuevas enloscuatropares. Losdetallesincluyen todosretainedchanged/removed/added, pérdidas,fees,órdenes yqtyposteriores por símbolo y año.

BTCconserva223/223 entry/exittimestamps;SPY12B/19Ctambién. CantidadescambianenBTC53/91/48/50tradesyenSPY11/18/11/18 paraFBS0B/C,FBS1B/C. No hay diferencia observada enprecio/timing defillsBTC/SPY; el campoexit_priceVWAP deltrade presenta a vecesdiferencias de redondeo al cambiarqty, por eso no se interpreta desigualdad exacta de esecampo como cambioeconómico defill. LasPAXGqtyretenidascambian37/38entradas.

|Par|ΔPAXG|ΔBTC|ΔSPY|
|---|---:|---:|---:|
|FBS0B|801.507759|50.379752|24.295312|
|FBS0C|807.974175|20.252231|15.762574|
|FBS1B|840.691466|42.828168|25.163077|
|FBS1C|851.893783|47.589049|18.980110|

No hay historialcompleto de instrucciones de modificaciónSTOP ni beforestate. Los snapshots retienen extremoscreated/executed/canceled ypreciofinal; created_at puedeconservarse cuando unSTOPsemodifica. Por eso primerainstruccióncambiada yprimeradivergencia delestadocompleto quedan explícitamente desconocidas. Se informan primeraejecución económica observada (incluyeqty) yprimeraejecución precio/timingobservada, más registrosSTOPendpoints separados. No inferimos señalesbloqueadas noobservadas.

Auditor8inputsfinale59c586237944330917483c5429cceddsucceeded. Original411aff846d8644a6ac5fdb613ebadc88succeeded, pero tooltruncósummaryalrededor65512chars; no se usaronarraysparciales. CorrectivoEXCLUSIVAMENTEoutput, resultadosDIDidénticos.83artefactos ymanifestrecuperadostruncated=false,max34066chars. Listasdynamicallypartitioned<=35000bytesconrows+SHA256porparte/concatenación,summary<=40000. Los83JSONpayloads se guardaron permanentemente comoMarkdownreportsporMCP; índiceX03_R3_FIXEDBE_DATA_MANIFEST_20261019.md. FuenteauditorX03_R3_FIXEDBE_DIVERGENCE_SOURCE_20261019.md. QAterminalX03_R3_FIXEDBE_TERMINAL_QA_20261019.md. NominalparityX03_R3_NOMINAL_PARITY_20261019.md. Sin jobsni nuevosruns propiospendientes.
