# BTC — resultados de la iteración R7

## Decisión

Se completaron14backtests nominales: dos controles observacionales y seis variantes en B/C. Ninguna supera todas las puertas prefijadas. Ninguna habría pasado tampoco el conjunto de criterios heredados de R6: el resultado no depende de añadir las puertas de concentración. Se conserva N204 como referencia, N503 y P604 como candidatas de investigación sin promoción. Cero verificaciones condicionales adicionales. Las dos variantes de salida con beneficio reproducen mecanismos anteriores; no son evidencia nueva independiente.

## Resultados

|Receta|Mecanismo|Semilla|Neto B / C, USDT|Δ N204 B / C|Salidas modificadas B / C|Resultado|
|---|---|---|---:|---:|---|---|
|S701|P604 con beneficio neto obligatorio|N503|[13347.96](http://localhost:9200/#/backtest/a05b76ab-842f-428e-ba54-4099070ecea5) / [13562.22](http://localhost:9200/#/backtest/ca2c6fea-b723-4308-ba85-199535fde594)|291.35 / 322.77|4 / 4|Falla calendar, modified_exits|
|S702|Reversión por cierre sobre máximo previo|N503|[12458.52](http://localhost:9200/#/backtest/3b464cbf-426f-4197-9646-834a8117c943) / [12667.17](http://localhost:9200/#/backtest/9ff8c173-f3fa-459d-b467-092ec3c4924e)|-598.10 / -572.27|21 / 21|Falla nominal, calendar, plus10, without_best_month|
|S703|Devolución del 50% de la ganancia al cierre|N503|[11840.24](http://localhost:9200/#/backtest/576a3b11-dc73-46ea-938b-02088406ad52) / [12033.14](http://localhost:9200/#/backtest/04acc6c2-7fb2-4e55-b4d6-7aab52722b74)|-1216.38 / -1206.31|24 / 24|Falla nominal, calendar, plus10, year_distribution, without_best_month|
|S704|Preparación técnica original y beneficio neto|N503|[12143.86](http://localhost:9200/#/backtest/f005ba80-5b39-42f8-9ab5-97fb5568f07c) / [12310.79](http://localhost:9200/#/backtest/2d941297-ac9f-4196-ac3b-3066298d6a5d)|-912.76 / -928.65|13 / 13|Falla nominal, plus10, year_distribution, without_best_month|
|S705|Reversión estructural transferida a N204|N204|[11831.98](http://localhost:9200/#/backtest/789d5a10-e2cc-468c-8f76-f20fba9277aa) / [12026.17](http://localhost:9200/#/backtest/aedc08d8-2ad7-4c62-8186-a777fe32ae25)|-1224.63 / -1213.28|25 / 25|Falla nominal, calendar, plus10, year_distribution, without_best_month|
|S706|Devolución del 50% transferida a N204|N204|[11521.16](http://localhost:9200/#/backtest/de7e68d4-3adb-4afe-9c62-ecb7496877a1) / [11716.48](http://localhost:9200/#/backtest/f407f8a8-15b4-41cb-b756-46ced2f041b4)|-1535.46 / -1522.96|28 / 28|Falla nominal, calendar, plus10, year_distribution, without_best_month|

Los enlaces son backtests completos sobre la cartera compartida; no resultados aislados BTC. B=SPY segunda oportunidad exacta/precio estructural; C=SPY desde segunda/precio mercado; BTC y PAXG iguales. Cada cifra de neto incluye comisiones nominales. Matriz detallada: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R7_RESULTS_MATRIX_20261019.md.

## Aprendizaje

O700 registró sin modificar:264/271operaciones idénticas a N503, diferencia máxima0en tiempos/tipos/precios/qty/fees/PNL.375contextos técnicosR,11418decisiones,82eventosN503 y11ocupados,67fills/closesporcartera. R no implica una orden asequible ni ejecutada. Los registros completos quedan en las sesiones. La observación puede reutilizarse sin rehacer la hipótesis económica.

S701 reproduceexactamenteP604ambascarteras,con4salidasmodificadasrespectoN503. Exigirbeneficionetonoañade selección en estosdatos. S704 reproduceexactamenteP603ambascarteras,con13salidasmodificadas. Enambosmecanismoslas salidas anteriores ya satisfacían la condición de beneficio observado; el problema no se resuelve añadiendo simplemente «cerrar sólo en ganancia».

S702 yS703 prueban defensas de ganancias más generales, con21/24liberaciones respectivamente en N503. La cartera y el suplemento pierden rentabilidad frente a sus referencias: actuar más veces no demuestra mejor gestión. S705/S706 comprueban los mismos mecanismos sobre N204 para aislar dependencia del filtro ER; sus resultados y puertas constan en la tabla, sin escoger combinaciones nuevas tras observarlos.

No se concluye que toda salida anticipada sea mala. Se descartan estas reglas concretas bajo este contrato y muestra. La mejora de P604 continúa concentrada en4casos; las corridas idénticas no aumentan su muestra ni su confianza. El diagnóstico previo está finalmente guardado en strategies/MultiAssetRetestBtcShort4h/reports/BTC_CANDIDATE_DIAGNOSTIC_RESULTS_20261019.md.

## Verificación y límites

Fills/cantidades/fees/PNL/wallet/terminal/MTMUTC de las14sesiones conciliados. QA61casos de sintaxis/helpers; no se presenta como test de ciclo del motor. ControlrealO700 sí verifica paridad de ejecución. Autorrevisión determinista de86comprobaciones aprobada, contrastando reconciliación,paridades ypuertas; no revisión externa independiente ni segunda reconstrucciónMTM. Veinticuatrofuentesexactasleídas,14formulariosy42snapshots; originales ydependenciaspreservados. Todaslas31entradaslargasBTCysusmomentosdesalida permanecen iguales; cantidades pueden cambiar por capitalcompartido.

10000USDT,1%trade/8%total,isolated5x,cap4.4,reserva.001sizing,nopyramid;fee.00045porlado. SL1R/TP2R/48hdel suplemento; originales intactos. PAXG mantiene BE dependiente del fee. Costes+5/+10bpsRTson recargos sobre fills/cantidades/precios/tiemposfijos; no son mayorfeeengine ni replay de capital. No se activaron las2corridasfee.00070ni4vecinosTP1.8R/2.2R por ausencia de candidata elegible.

Puertas heredadas:ΔnetN204>1e-7;+5Mactivos>=65%yQ>=80%full/included;+10net>=N204−1e-7;DDmotor>=−25%,ambasB/C. Puertas nuevas deconcentración, fijadasantesresultados:>=10salidasmodificadasrespectosemilla,ventajaMTM en>=3delos5bloques2021..2025,ventajatrasdescontar mejormesincremental. Son filtros operativos, no pruebasestadísticas niOOS. La errata descriptiva«añoscompletos» se corrigió sin variar elalgoritmo:2025esparcialporfinish_dateexclusiva,completos2021..2024. Mesesfull61/Q19;incluidos63/21. Omisionesanuales/mensuales sonaritméticas,no curvasejecutablescontrafactuales.

Misma muestra2020-10-15→2025-12-31exclusiva,últimoprecio2025-12-30.2026cerradoinclusoinspección. Desarrollo reusado yselección acumulada; no prueba de ausencia de sobreajuste.

## Mantenimiento y continuidad

Jesse respondió con normalidad durante esta iteración: no fallos de las14corridas, duracionesmotor yURLs en manifiesto. No hay evidencia de que el número de carpetas de estrategias provoque el error previoartifact_changedalrecuperarPNG; no se intentó resolverlo borrando fuentes. No se borraron ni movieron estrategias, sesiones, informes, velas ni configuración. El registro de hipótesis fallidas, matrices, códigos y motivos permanece en los reportes, las fuentes y los snapshots de sesiones. Antes de cualquier archivado futuro se preservará fuenteexacta/dependencias/hipótesis/URLs/resultados/motivo/manifiestorecuperación; la búsqueda de salud no autoriza purgar datos históricos.

Continuaría por selección de entradas y contexto de convivencia a partir del registro, con pocas hipótesis económicas, conservando los stops/targets originales como control. Antes de otra búsqueda masiva, estudiar por qué los casos que N503 excluye cambian la disponibilidad del STOP y qué condiciones observables acompañan esos cambios; contrastar la distribución temporal, no diseñar reglas para2023o unmesparticular. No seguir afinando estas defensas de salida para recuperar las cuatro operaciones de P604.

## Trazabilidad

Protocolo: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R7_FROZEN_PROTOCOL_20261019.md.

QAfuentes: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R7_SOURCE_QA_20261019.md.

Auditor/ranking: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R7_AUDITOR_AND_RANKING_SOURCE_20261019.md.

Paridadobservador: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R7_OBSERVER_PARITY_20261019.md.

Manifiestocompleto: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R7_FINAL_MANIFEST_20261019.md.

## Cohortes y atribución observada

```json
[
  {
    "id": "S701",
    "seed": "N503",
    "rows": [
      {
        "portfolio": "B",
        "supplement": {
          "n": 67,
          "net": 2661.450239918451,
          "fees": 406.1174398291136,
          "gross": 3067.567679747566,
          "plus10": 2210.2086401083257,
          "exbest": 2252.6241013787057,
          "ex3": 1552.2557690318504,
          "ex3_plus10": 1138.0420389449064,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 390.29967243252156,
            "2022": 944.212118973172,
            "2023": 739.5644460215218,
            "2024": 92.74381803853478,
            "2025": 559.7292388047014
          }
        },
        "STOP": {
          "n": 118,
          "net": 1863.0734345754781,
          "fees": 691.8087802823007,
          "gross": 2554.882214857778,
          "plus10": 1094.3970120395888,
          "exbest": 1630.9535602475862,
          "ex3": 1206.4094033834724,
          "ex3_plus10": 485.83059929461285,
          "year_net": {
            "2020": -147.9985775394502,
            "2021": -330.9622615538136,
            "2022": 925.8436398402449,
            "2023": 539.8605199332997,
            "2024": 279.08512269596645,
            "2025": 597.2449911992312
          }
        },
        "delta_supp": 62.04499288801071,
        "delta_STOP": -23.554729546364342
      },
      {
        "portfolio": "C",
        "supplement": {
          "n": 67,
          "net": 2633.157500581747,
          "fees": 405.6239381315789,
          "gross": 3038.781438713326,
          "plus10": 2182.464235991104,
          "exbest": 2219.2210353102464,
          "ex3": 1508.1179475215713,
          "ex3_plus10": 1095.0000305479737,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 384.9090575833119,
            "2022": 929.1516261988636,
            "2023": 724.1595178893153,
            "2024": 90.03573477016795,
            "2025": 570.0006184920883
          }
        },
        "STOP": {
          "n": 118,
          "net": 1872.0041017322803,
          "fees": 692.4874284222622,
          "gross": 2564.491530154542,
          "plus10": 1102.5736257075446,
          "exbest": 1636.0580756297516,
          "ex3": 1205.51292130387,
          "ex3_plus10": 484.9099608330084,
          "year_net": {
            "2020": -147.9985775394502,
            "2021": -319.09521780608986,
            "2022": 910.7815385845606,
            "2023": 528.484622701125,
            "2024": 287.0446231599508,
            "2025": 612.7871126321841
          }
        },
        "delta_supp": 55.364264490541245,
        "delta_STOP": -6.2912777583201205
      }
    ]
  },
  {
    "id": "S702",
    "seed": "N503",
    "rows": [
      {
        "portfolio": "B",
        "supplement": {
          "n": 67,
          "net": 1967.8804654709518,
          "fees": 399.75368250241195,
          "gross": 2367.6341479733624,
          "plus10": 1523.7097071349378,
          "exbest": 1617.7675964235784,
          "ex3": 930.6319772580209,
          "ex3_plus10": 521.9755723188728,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 471.4619440399017,
            "2022": 629.4133479297362,
            "2023": 699.7542648320439,
            "2024": 203.91357953612192,
            "2025": 28.436383485146962
          }
        },
        "STOP": {
          "n": 117,
          "net": 1734.2637445267917,
          "fees": 677.3945141287433,
          "gross": 2411.658258655535,
          "plus10": 981.603173272633,
          "exbest": 1509.7961737481685,
          "ex3": 1090.2838184949999,
          "ex3_plus10": 384.704954565294,
          "year_net": {
            "2020": -147.9985775394502,
            "2021": -330.37026893685413,
            "2022": 913.5396782317148,
            "2023": 531.2749172950927,
            "2024": 176.48213485004658,
            "2025": 591.335860626242
          }
        },
        "delta_supp": -631.5247815594887,
        "delta_STOP": -152.36441959505078
      },
      {
        "portfolio": "C",
        "supplement": {
          "n": 67,
          "net": 1943.3438900479168,
          "fees": 399.3886168438988,
          "gross": 2342.7325068918153,
          "plus10": 1499.5787602213627,
          "exbest": 1588.229408585584,
          "ex3": 887.8610762387282,
          "ex3_plus10": 480.25247686656417,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 466.6137650085447,
            "2022": 620.3153005571373,
            "2023": 684.8666702748787,
            "2024": 205.81638386791272,
            "2025": 30.83082469144307
          }
        },
        "STOP": {
          "n": 117,
          "net": 1724.0942659882467,
          "fees": 678.3584962775477,
          "gross": 2402.4527622657943,
          "plus10": 970.3626034576381,
          "exbest": 1495.8005434349873,
          "ex3": 1070.2871907200554,
          "ex3_plus10": 364.3671326207435,
          "year_net": {
            "2020": -147.9985775394502,
            "2021": -325.29950427825446,
            "2022": 900.2529295491044,
            "2023": 518.9445488361971,
            "2024": 177.1733045317226,
            "2025": 601.0215648889275
          }
        },
        "delta_supp": -634.4493460432891,
        "delta_STOP": -154.2011135023538
      }
    ]
  },
  {
    "id": "S703",
    "seed": "N503",
    "rows": [
      {
        "portfolio": "B",
        "supplement": {
          "n": 67,
          "net": 1603.725490702961,
          "fees": 391.8078157201098,
          "gross": 1995.5333064230713,
          "plus10": 1168.3834732361734,
          "exbest": 1263.6158464855175,
          "ex3": 593.5388338098351,
          "ex3_plus10": 192.79501152676724,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 146.16051075140112,
            "2022": 618.8707980218867,
            "2023": 764.8722896447923,
            "2024": 116.78925212658874,
            "2025": 22.131694510293016
          }
        },
        "STOP": {
          "n": 117,
          "net": 1642.1305052669932,
          "fees": 668.1390475390355,
          "gross": 2310.2695528060285,
          "plus10": 899.7537857791762,
          "exbest": 1424.0398541127608,
          "ex3": 1016.5294937831312,
          "ex3_plus10": 319.88940649052904,
          "year_net": {
            "2020": -147.9985775394502,
            "2021": -210.56375429602377,
            "2022": 898.4480537317286,
            "2023": 523.1511772032871,
            "2024": 3.4711834046741217,
            "2025": 575.622422762778
          }
        },
        "delta_supp": -995.6797563274795,
        "delta_STOP": -244.4976588548493
      },
      {
        "portfolio": "C",
        "supplement": {
          "n": 67,
          "net": 1581.5798779267964,
          "fees": 391.371585982241,
          "gross": 1972.9514639090373,
          "plus10": 1146.722560168752,
          "exbest": 1236.4686212943889,
          "ex3": 555.6568531768877,
          "ex3_plus10": 155.94581088250675,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 145.93599628204512,
            "2022": 608.9501292666606,
            "2023": 750.8994522172297,
            "2024": 115.81728152917515,
            "2025": 25.076072983686004
          }
        },
        "STOP": {
          "n": 117,
          "net": 1621.6655275325477,
          "fees": 669.2961850539567,
          "gross": 2290.9617125865047,
          "plus10": 878.0030996948185,
          "exbest": 1399.7487246036824,
          "ex3": 986.2373668122798,
          "ex3_plus10": 289.04146827661134,
          "year_net": {
            "2020": -147.9985775394502,
            "2021": -207.21158790695887,
            "2022": 883.4430599273942,
            "2023": 512.377171606119,
            "2024": 1.757612621355321,
            "2025": 579.2978488240888
          }
        },
        "delta_supp": -996.2133581644096,
        "delta_STOP": -256.62985195805277
      }
    ]
  },
  {
    "id": "S704",
    "seed": "N503",
    "rows": [
      {
        "portfolio": "B",
        "supplement": {
          "n": 67,
          "net": 2093.7156312413294,
          "fees": 394.8227229356204,
          "gross": 2488.53835417695,
          "plus10": 1655.0237168684184,
          "exbest": 1705.330799628567,
          "ex3": 1079.6774740493775,
          "ex3_plus10": 676.4643971210218,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 363.22884256902177,
            "2022": 817.5015999439354,
            "2023": 790.7163217070372,
            "2024": -310.35490821780337,
            "2025": 497.7228295911395
          }
        },
        "STOP": {
          "n": 125,
          "net": 1425.871320955959,
          "fees": 729.0351248190261,
          "gross": 2154.906445774985,
          "plus10": 615.8322933792637,
          "exbest": 1203.954518027093,
          "ex3": 794.5057659958164,
          "ex3_plus10": 30.663814342917505,
          "year_net": {
            "2020": -147.9985775394502,
            "2021": -428.43970875758384,
            "2022": 812.9679247779045,
            "2023": 528.895538419448,
            "2024": 291.9498969239445,
            "2025": 368.49624713169555
          }
        },
        "delta_supp": -505.68961578911103,
        "delta_STOP": -460.75684316588354
      },
      {
        "portfolio": "C",
        "supplement": {
          "n": 67,
          "net": 2052.7004100660856,
          "fees": 393.67501398717604,
          "gross": 2446.3754240532608,
          "plus10": 1615.2837278581117,
          "exbest": 1659.2052517215777,
          "ex3": 1025.2596788834362,
          "ex3_plus10": 623.7836711063771,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 355.8980212591688,
            "2022": 802.2060854157095,
            "2023": 774.1477214422218,
            "2024": -316.7181472175145,
            "2025": 502.2657835184995
          }
        },
        "STOP": {
          "n": 125,
          "net": 1407.6975228127126,
          "fees": 729.3499608810789,
          "gross": 2137.0474836937924,
          "plus10": 597.3086773892918,
          "exbest": 1181.9545681092106,
          "ex3": 766.5048186161669,
          "ex3_plus10": 3.0429462233897766,
          "year_net": {
            "2020": -147.9985775394502,
            "2021": -425.8892798555444,
            "2022": 800.2351165366393,
            "2023": 513.0323055407839,
            "2024": 298.71494030122625,
            "2025": 369.6030178290579
          }
        },
        "delta_supp": -525.0928260251203,
        "delta_STOP": -470.5978566778879
      }
    ]
  },
  {
    "id": "S705",
    "seed": "N204",
    "rows": [
      {
        "portfolio": "B",
        "supplement": {
          "n": 80,
          "net": 2044.1817212947858,
          "fees": 456.76206137579834,
          "gross": 2500.943782670585,
          "plus10": 1536.6683197661218,
          "exbest": 1709.0736894923018,
          "ex3": 1047.8184856041505,
          "ex3_plus10": 574.4411045484296,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 623.8354136218252,
            "2022": 624.0472702063045,
            "2023": 359.5119828817998,
            "2024": 193.43622465382697,
            "2025": 308.44988428303
          }
        },
        "STOP": {
          "n": 114,
          "net": 1271.1433260738725,
          "fees": 643.0579150995939,
          "gross": 1914.2012411734656,
          "plus10": 556.6345315187679,
          "exbest": 1053.0526749196438,
          "ex3": 649.9966070971259,
          "ex3_plus10": -19.055640045939043,
          "year_net": {
            "2020": -147.9985775394502,
            "2021": -579.0261228526164,
            "2022": 740.9515592318655,
            "2023": 515.8441957558073,
            "2024": 168.55109461297866,
            "2025": 572.8211768652873
          }
        },
        "delta_supp": -812.3329895427182,
        "delta_STOP": -181.68951204450445
      },
      {
        "portfolio": "C",
        "supplement": {
          "n": 80,
          "net": 2022.3645256484074,
          "fees": 454.7427581322987,
          "gross": 2477.1072837807064,
          "plus10": 1517.0947943902972,
          "exbest": 1682.2548814309616,
          "ex3": 1010.2649221009902,
          "ex3_plus10": 539.6792915957694,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 612.0838333026156,
            "2022": 612.7811656340893,
            "2023": 352.48586315998773,
            "2024": 196.21850937357345,
            "2025": 313.8942085301416
          }
        },
        "STOP": {
          "n": 114,
          "net": 1279.8953147571326,
          "fees": 643.6331019766677,
          "gross": 1923.528416733801,
          "plus10": 564.7474236719465,
          "exbest": 1057.978511828268,
          "ex3": 648.9214465439834,
          "ex3_plus10": -20.040000022318424,
          "year_net": {
            "2020": -147.9985775394502,
            "2021": -564.2298875106868,
            "2022": 729.9147434600826,
            "2023": 504.7206267184895,
            "2024": 173.17266119997757,
            "2025": 584.3157484287207
          }
        },
        "delta_supp": -814.2666296655143,
        "delta_STOP": -167.04893407827808
      }
    ]
  },
  {
    "id": "S706",
    "seed": "N204",
    "rows": [
      {
        "portfolio": "B",
        "supplement": {
          "n": 80,
          "net": 1863.8048835476015,
          "fees": 452.62019043270885,
          "gross": 2316.425073980309,
          "plus10": 1360.8935608445913,
          "exbest": 1533.6984641600804,
          "ex3": 883.1780157137523,
          "ex3_plus10": 413.8546332037377,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 287.76694472132397,
            "2022": 795.4852896821905,
            "2023": 434.81864652035983,
            "2024": 111.66072465056865,
            "2025": 299.17233232515844
          }
        },
        "STOP": {
          "n": 114,
          "net": 1212.728076920742,
          "fees": 640.9634079635143,
          "gross": 1853.6914848842564,
          "plus10": 500.5465125168372,
          "exbest": 997.1881936162679,
          "ex3": 600.1331232555166,
          "ex3_plus10": -67.20707175874128,
          "year_net": {
            "2020": -147.9985775394502,
            "2021": -453.3490339177573,
            "2022": 730.7643947674845,
            "2023": 515.379690153804,
            "2024": 1.5476456690230975,
            "2025": 566.3839577876381
          }
        },
        "delta_supp": -992.7098272899025,
        "delta_STOP": -240.10476119763484
      },
      {
        "portfolio": "C",
        "supplement": {
          "n": 80,
          "net": 1842.2158954569009,
          "fees": 450.7511884362482,
          "gross": 2292.9670838931484,
          "plus10": 1341.3812416388464,
          "exbest": 1507.1078636544128,
          "ex3": 845.8526597662668,
          "ex3_plus10": 379.1540264211556,
          "year_net": {
            "2020": -65.09905435199995,
            "2021": 281.920120347116,
            "2022": 781.1137891179737,
            "2023": 427.74974356546426,
            "2024": 113.69393699531713,
            "2025": 302.8373597830292
          }
        },
        "STOP": {
          "n": 114,
          "net": 1201.803367052136,
          "fees": 642.1650242507504,
          "gross": 1843.9683913028862,
          "plus10": 488.2866734401913,
          "exbest": 983.7127158979048,
          "ex3": 580.6566480753847,
          "ex3_plus10": -87.40349812451515,
          "year_net": {
            "2020": -147.9985775394502,
            "2021": -444.9140358105193,
            "2022": 720.083149838826,
            "2023": 503.0910358454837,
            "2024": -2.3571927581153886,
            "2025": 573.8989874759111
          }
        },
        "delta_supp": -994.4152598570208,
        "delta_STOP": -245.1408817832746
      }
    ]
  }
]
```
