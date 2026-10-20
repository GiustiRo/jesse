# R14 — BTC sin funding: resultados y cierre
2026-10-20. Doce backtests nuevos terminados y cuatro anclas reutilizadas. Ninguna variante cumple las puertas congeladas. Se conserva K1001 como referencia de investigación, sin promoción. C sigue principal; B control. PAXG/SPY originales y framework intactos. Funding queda planificado para otro bloque.

## Conclusiones
R1401 quitar suplemento: C nominal25952.80USDT vs37184.83; estrés16947.61vs24652.00. Retiene69.79%/68.75%del neto. EnC DDnominal13.82135%vs13.81806%(casiigual,ligeramentepeor), estrés14.50389%vs14.54413%(ligeramentemejor). La mejoraDDmásclara esB. La pérdida del suplemento en2026 no justifica eliminarlo retrospectivamente: elhistoricomuestraotroaporte yocupación.
R1402 longER12>1/3: C nominal30090.29, estrés19715.64, retención80.92%/79.98%; DD16.90098%/17.61649% empeora.31longsbaseline→28; PFpropio3.128→3.951, pero netolong11824.94→10014.36 y netocarteramenor. Se excluye long6/2/2021 05:14UTC +1519.78 y apareceotroelmismodía17:17UTC -210.65; tambiénotrasentradasyshortscambian. El deltacartera no es suma simple detradesevitados: compounding/ocupación ycantidadesdiferentes.
R1403 alinear longEMA120conpendiente10: C nominal38116.47(+931.64; +2.505%relativoalneto), estrés25328.00(+675.99; +2.742%). CAGR34.659→35.165%nominal y26.917→27.389%estrés. MejoraCalmarCestrés sólo1.845%, inferioral5%previsto. Únicadiferenciadeentradas: excluye long8/7/2022 05:52UTC, pérdida334.06enCnominal. El resto del incremento refleja capitalposterior. No son10casos ni robustezmultirregimen. BDDnominal empeora0.00766puntos, diferenciaeconómicamentepequeña; falta deamplitud yCalmarsonmotivosmásrelevantes.
La regla macro se conserva como hipótesis exploratoria, no nueva ganadora. Uncasofavorable no justifica retocar horizonte/lag.
No se ejecutaron vecinos,ventanascondicionales ni nuevaspruebas2026 porque ninguna pasó la primera fase. Desenlace previsto enprotocolo; no retocarcriteriosparaabrirbúsqueda.

## Contrato
Protocolo BTC_R14_SIN_FUNDING_PROTOCOL_20261020.md guardadoantesdecrearvariantes. Desarrollo2020-10-15→2025-12-31exclusiva,capitalcompartido10000,2%/6%,isolated3x,fee.00045/.00095porlado,4h+M1,warmup240,cap4.4,reserva.001sólosizing,fastfalse/debugtrue.
R1401ablatefallbacksuplementario;R1402eficiencia12cambios>1/3;R1403precio>EMA120actual>EMA120[-10]. Sincombinacionesnioptimización. Inspecciónprevia evitórepetirprogreso24h/1R yreclaimM1ya descartados.
Configuraciónglobal5x;12sesionesfijadas3xsinmutarconfigglobal. Fuentesanclaigualesoriginalesactuales; velas sincambios.
Hipótesisinformadaspor2026.2020–2025reutilizado. No validaciónciega ni reinicio del historial de intentos.

## Matriz completa
NetoUSDT; CAGR/DDen%; DDnegativo. Mesespositivos61calendariocompletos2020-11..2025-11, incluyeinactivos.
| Sesión | Neto | CAGR | DD | PF | Calmar | Trades | Meses + |
|---|---:|---:|---:|---:|---:|---:|---:|
| [BASE_B_N](http://localhost:9200/#/backtest/b9f0cccc-8de0-4076-a7fa-eb9ae8e1be38) | 35727.07 | 33.85 | -13.34 | 2.058 | 2.537 | 242 | 46/61 |
| [BASE_C_N](http://localhost:9200/#/backtest/3ec33cac-3ea6-43c7-9cfe-4d315930fee2) | 37184.83 | 34.66 | -13.82 | 2.056 | 2.508 | 249 | 44/61 |
| [BASE_B_F](http://localhost:9200/#/backtest/bb6e80f2-36f1-4c8f-8c8c-cac840794b8c) | 24064.34 | 26.50 | -14.59 | 1.786 | 1.817 | 242 | 38/61 |
| [BASE_C_F](http://localhost:9200/#/backtest/ac57b4d3-cfeb-4add-88cb-19358d701db1) | 24652.00 | 26.92 | -14.54 | 1.775 | 1.851 | 249 | 40/61 |
| [R1401_B_N](http://localhost:9200/#/backtest/5fc55e71-f600-4b63-945a-4659e0f2216c) | 24817.74 | 27.03 | -12.19 | 1.953 | 2.218 | 206 | 41/61 |
| [R1401_C_N](http://localhost:9200/#/backtest/5423c8a5-f001-40f2-b75f-22361191218e) | 25952.80 | 27.82 | -13.82 | 1.956 | 2.013 | 213 | 41/61 |
| [R1401_B_F](http://localhost:9200/#/backtest/cc3df18a-21af-4e8b-9a83-679be45c1e20) | 16500.54 | 20.55 | -12.57 | 1.686 | 1.635 | 206 | 37/61 |
| [R1401_C_F](http://localhost:9200/#/backtest/80bc73db-5984-4461-b91b-12a8b36d0be4) | 16947.61 | 20.94 | -14.50 | 1.678 | 1.444 | 213 | 38/61 |
| [R1402_B_N](http://localhost:9200/#/backtest/971627a1-6814-478a-ad52-b3cf74e55c2c) | 29374.84 | 30.07 | -13.74 | 2.040 | 2.188 | 239 | 45/61 |
| [R1402_C_N](http://localhost:9200/#/backtest/6db7602b-e352-4b9d-bc2c-f0e79aabc73d) | 30090.29 | 30.52 | -16.90 | 2.031 | 1.806 | 246 | 43/61 |
| [R1402_B_F](http://localhost:9200/#/backtest/14eaf384-d4b4-4c29-aacb-03158e0e1e5f) | 19619.27 | 23.15 | -14.58 | 1.763 | 1.588 | 239 | 38/61 |
| [R1402_C_F](http://localhost:9200/#/backtest/46dd71fe-c252-477d-88e1-3724ab45558a) | 19715.64 | 23.23 | -17.62 | 1.745 | 1.319 | 246 | 40/61 |
| [R1403_B_N](http://localhost:9200/#/backtest/705f49cf-9ca0-4aa7-abc4-f0d305da0774) | 36609.29 | 34.34 | -13.35 | 2.077 | 2.572 | 241 | 47/61 |
| [R1403_C_N](http://localhost:9200/#/backtest/24bd82e9-06f5-4f6b-81cc-75adf9b245cc) | 38116.47 | 35.17 | -13.82 | 2.075 | 2.545 | 248 | 45/61 |
| [R1403_B_F](http://localhost:9200/#/backtest/da5c2292-c9ac-408d-8a4b-bbf07217567f) | 24737.82 | 26.98 | -14.58 | 1.803 | 1.850 | 241 | 39/61 |
| [R1403_C_F](http://localhost:9200/#/backtest/260dfa6c-cb96-45dd-8eb5-a345821c1780) | 25328.00 | 27.39 | -14.53 | 1.792 | 1.885 | 248 | 41/61 |

## Comparación contra ancla correspondiente
ΔDDpositivo=menorcaída; entradas distintas=diferencia simétrica(symbol,side,opened_at), no qty.
| Caso | Δneto USDT | Δneto relativo | ΔDD puntos | ΔCalmar relativo | Entradas distintas | Δmeses positivos |
|---|---:|---:|---:|---:|---:|---:|
| R1401_B_F | -7563.80 | -31.43% | 2.0158 | -10.01% | 56 | -1 |
| R1401_B_N | -10909.33 | -30.54% | 1.1563 | -12.56% | 56 | -5 |
| R1401_C_F | -7704.40 | -31.25% | 0.0402 | -21.99% | 56 | -2 |
| R1401_C_N | -11232.03 | -30.21% | -0.0033 | -19.76% | 56 | -3 |
| R1402_B_F | -4445.07 | -18.47% | 0.0055 | -12.60% | 11 | 0 |
| R1402_B_N | -6352.24 | -17.78% | -0.3988 | -13.76% | 11 | -1 |
| R1402_C_F | -4936.37 | -20.02% | -3.0724 | -28.75% | 11 | 0 |
| R1402_C_N | -7094.54 | -19.08% | -3.0829 | -28.01% | 11 | -1 |
| R1403_B_F | 673.48 | 2.80% | 0.0052 | 1.83% | 1 | 1 |
| R1403_B_N | 882.22 | 2.47% | -0.0077 | 1.39% | 1 | 1 |
| R1403_C_F | 675.99 | 2.74% | 0.0135 | 1.85% | 1 | 1 |
| R1403_C_N | 931.64 | 2.51% | 0.0000 | 1.46% | 1 | 1 |

## Retornos anuales C según snapshots diarios
2020desde15/10,2025hasta30/12,parciales. Incluye liquidaciónterminal delmotoralfinishexclusivo, sobreúltimoprecioprevio yatribuidaalperíodoanterior. No retorno porcohortesdecierre.
| Caso | 2020* | 2021 | 2022 | 2023 | 2024 | 2025* |
|---|---:|---:|---:|---:|---:|---:|
| BASE_C_N | 7.14% | 45.54% | 18.10% | 42.07% | 32.47% | 36.13% |
| R1401_C_N | 9.25% | 34.57% | 5.40% | 35.53% | 32.58% | 29.12% |
| R1402_C_N | 7.14% | 20.11% | 17.69% | 42.07% | 34.58% | 38.45% |
| R1403_C_N | 7.14% | 45.54% | 20.45% | 42.08% | 32.45% | 36.12% |
| BASE_C_F | 6.19% | 39.63% | 15.38% | 37.33% | 26.26% | 16.81% |
| R1401_C_F | 8.25% | 29.37% | 3.64% | 31.54% | 26.69% | 11.40% |
| R1402_C_F | 6.19% | 15.64% | 14.96% | 37.31% | 28.38% | 19.41% |
| R1403_C_F | 6.19% | 39.63% | 17.67% | 37.34% | 26.22% | 16.81% |

## Puertas
~~~json
{
  "R1401": {
    "pass": false,
    "criteria": {
      "retention90_all": false,
      "dd_no_worse_all": false,
      "calmar_C_stress_5pct": false,
      "changed_btc_entries_10": true,
      "year_breadth_C_nominal": false,
      "year_breadth_C_stress": false,
      "calendar_C_nominal": false,
      "calendar_C_stress": false
    },
    "failed": [
      "retention90_all",
      "dd_no_worse_all",
      "calmar_C_stress_5pct",
      "year_breadth_C_nominal",
      "year_breadth_C_stress",
      "calendar_C_nominal",
      "calendar_C_stress"
    ]
  },
  "R1402": {
    "pass": false,
    "criteria": {
      "retention90_all": false,
      "dd_no_worse_all": false,
      "calmar_C_stress_5pct": false,
      "changed_btc_entries_10": true,
      "year_breadth_C_nominal": false,
      "year_breadth_C_stress": false,
      "calendar_C_nominal": true,
      "calendar_C_stress": true
    },
    "failed": [
      "retention90_all",
      "dd_no_worse_all",
      "calmar_C_stress_5pct",
      "year_breadth_C_nominal",
      "year_breadth_C_stress"
    ]
  },
  "R1403": {
    "pass": false,
    "criteria": {
      "retention90_all": true,
      "dd_no_worse_all": false,
      "calmar_C_stress_5pct": false,
      "changed_btc_entries_10": false,
      "year_breadth_C_nominal": true,
      "year_breadth_C_stress": true,
      "calendar_C_nominal": true,
      "calendar_C_stress": true
    },
    "failed": [
      "dd_no_worse_all",
      "calmar_C_stress_5pct",
      "changed_btc_entries_10"
    ]
  }
}
~~~
Retener>=90%neto yDDnopeorB/Cambosfees;CalmarCestrés>=+5%;>=10entradasBTCdistintas;incrementoanualno negativoen>=3/5bloquesCnomyestrés; noperder>1mespositivoCnomyestrés. Criteriosoperativos,nosignificancia.

## Auditoría
12formulariosy36snapshotsdefuenteexactos;7fuentesreleídasexactasalfinal. AST:sólo_signal+terminateenR1401,_plan+terminateenR1402/R1403;24métodosintactosporvariante. Sintaxiscompila; QAfunciónERascenso/descenso/plano/zigzag, no testexhaustivodelmotor.
ContadoresR1401:70candidatosfallback,0fillssuplementarios. R1402long51candidatos/42admitidos/9rechazados. R1403long45/44/1. Plan no equivaleafill;rechazarlongpuedeliberarotraentrada.
PNLtrades=netomotor,precioPNL-fees=neto,equityterminal=balancefinal en12sesionesy4anclas. Métricasopen_pl/open_tradesCpuedenserpreviasaliquidaciónforzada: tradeSPYfinal ycashconcilian; no posicionesvivas.
DatosBTC_R14_DATA_R1401_20261020.md,R1402,R1403. RegistroBTC_R14_REGISTRY_20261020.md;fuentesBTC_R14_SOURCES_20261020.md;BTC_R14_QA_20261020.md;codigoBTC_R14_ANALYSIS_SOURCE_20261020.md.
Jobsfinales38b9cc624439426eb48667460edfdd20/0542aaf5c9754d239e72a6b10296335a/bc724158c7ea49f0abf4421d7f7bf7fc,succeeded. Errores previosdetransportecampoURL yexclusiónpuntoterminal fueroncorregidosen análisis, sinrepetirbacktests; detalleQA.
Datoscompletosincluyenatribuciónporlado, sensibilidadaritméticasin3mejores,añosymeses. Excluirganadoresobservadosnoesreplaycausal.

## Límites y continuidad
PAXG proxyBinanceSpot ySPY HistDataSPXCFDBID/10. No funding,slippageefectivo,liquidez/spread/gapsdevenue/impacto. Feeestresadoreejecutasizing,no recargofijosobrefills.
Cierre de tanda sinreglanuevaconvincentementemejor; no pruebaimposibilidadde mejorarBTC. Eliminarunramofallidoen2026destruyeaportehistórico;filtraravancesexcluyetendenciasrentables;contextolentomejorasólouncaso.
SiguienteplanenFUNDING_BTC_NEXT_BLOCK_PLAN_20261020.md: auditoríacapacidades/unidades/calendario,ledgercontableBTCconparidadMCP/backtest/runtime,yensayopredictivosimplecon/sinfunding. Sinimplementar ese bloque ni tocarlive.
