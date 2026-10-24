# R8 — dictamen independiente final de selección

Se leyeron íntegramente la matriz final13recetas/26filas y la trazabilidadY903. 310 comprobaciones PASS:248recomputaciones de puertas/conjunciones/selección y62sobre58pares de salida identificados, cardinalidad y unicidad. Sin nuevos análisis ni backtests. No es una segunda reconstrucción financieraMTM: se contrastan números y pruebas de identidad publicados por el auditor central.

## Selección

Ninguna receta es elegible simultáneamente en B/C. Selecciónvacía correcta; no activar las seis verificaciones condicionales. N204 permanece referencia. Las cinco X fallan nominal, regularidad, Δ+10 y distribución; V801replicaN503yfallaregularidadC; V803/V805replicanN204, noavance; V804netpositivo sinregularidad/distribución; Y901/Y903pierden nominal/costes.

Y902 sí es una candidata de investigación positiva: +389.61961049756246/+440.90679103959155USDT frenteN204 y+117.52281275929636/+143.44665782697848frenteN503. Δ+10 estático +546.1006825447694/+591.583163597903. Pasa calendario activo, DD, diversidad, metadata y4de5bloques anuales en ambas. C pasa todas las puertas. B falla únicamente la ventaja tras descontar aritméticamente su mejor mes incremental:389.61961049756246−409.3801886544152=−19.760578156852716. C:440.90679103959155−400.58164502733234=40.32514601225921.

Esa cifra−19.76 no es la pérdida del año2022, ni el rendimiento de una cartera ejecutada sinenero2022, ni una pruebaOOS. Es el diferencial acumulado contraN204 menos el componente del mejor mes incremental. No corresponde relajar la puerta porque esté cerca de cero. RetenerY902 para estudiar concentración y ejecución es coherente; promocionarla o correr verificacionescondicionales contradice el protocolo.

## Diversidad Y903

Se verificaron29salidas modificadas porcartera usando sólo pares etiquetados como suplementoBTCshortMARKET, entradas al mismo tiempo/tipo yprecio dentro1e-7, salida con tiempooprecio diferente.58parescumplen,29únicos porcartera;metadata70actuales/67N503. Coinciden con29del diagnóstico de toda la cartera, pero el contador usado ahora procede del filtroexplícito. La aclaración conservadora previa aY903resultados evita contaminar diversidad con otrasrutas o cortosoriginales; umbral10 no cambió. Gate Y903sobre29>=10 correcto, no sobre las3entradasmodificadas. Las etiquetasSTOP/LIMIT deY901/902 no identifican el corto original: el suplemento tambiénpuede usarlas y exige logsreconciliados.

Prueba: strategies/MultiAssetRetestBtcShort4h/reports/BTC_R8_Y903_SUPPLEMENT_EXIT_TRACE_20261019.md.

## Método y límites

Se recalcularon tasas positivas estrictas usando denominadores activos publicados: Y90241/62y42/62incluidos,41/60y42/60full; el calendario incluido total sigue63meses y debe mostrarse separado, no mezclar activo/calendario. Q16/19y17/21ambas. Los bloques2021..2025incluyen2025parcial. Omisiones mensuales/anuales son aritméticas sin replay de capital, no contrafactualejecutable. Overlays5/10bpsRTsobre fillsfijos no sustituyen mayoresfeesengine ni alteran capital/capacidad.

B/Ccompartenmuestra, 2026cerrado, búsqueda acumulada sin garantía contra sobreajuste. Código/prioridades originales preservados no implican mismas ejecuciones: X805desplazaunade31entradaslargasBTCporocupación. Paridades repetidasN204/N503 no aportan nuevasobservacionesindependientes. Ninguna recomendación de live ni afirmación de mercado actual.

## Enlaces de las26sesiones

- V801B: http://localhost:9200/#/backtest/b0c5ce4f-ed64-4b07-bdca-f708aae2d445
- V801C: http://localhost:9200/#/backtest/5de86562-4ba7-4f2f-b9fb-f647ed2a8b70
- V802B: http://localhost:9200/#/backtest/876feccb-b93c-4fb0-a6ea-3a4b58c642c7
- V802C: http://localhost:9200/#/backtest/8e889155-eabc-4187-acc5-748f98dc5378
- V803B: http://localhost:9200/#/backtest/e7ef94a6-5249-44ea-b0bc-8c3cb7e3c531
- V803C: http://localhost:9200/#/backtest/1d818489-9707-43ab-8106-98cacdbf0a56
- V804B: http://localhost:9200/#/backtest/b481d1da-f0b2-4c9c-b663-b4a4a8c44896
- V804C: http://localhost:9200/#/backtest/b042558a-4ea4-41f1-a2de-7d51d8d53b56
- V805B: http://localhost:9200/#/backtest/0af9be29-c28a-490b-a7d7-6a481660a950
- V805C: http://localhost:9200/#/backtest/ec8d524e-d8c0-4b55-8dbe-da6ae8051918
- X801B: http://localhost:9200/#/backtest/f660ef63-d7c6-4792-9f21-06c1d7ebd85f
- X801C: http://localhost:9200/#/backtest/4e432aac-71c2-4023-a978-6d8a618aa660
- X802B: http://localhost:9200/#/backtest/261696a9-33ee-4504-a310-b8a44c63dcd3
- X802C: http://localhost:9200/#/backtest/07a45656-81e2-4fd8-9851-3aa16a782c2e
- X803B: http://localhost:9200/#/backtest/5208fe79-c420-4328-b5dd-1a67177f1ccf
- X803C: http://localhost:9200/#/backtest/a86de192-2f0d-4b34-a4ae-ce4f686d4757
- X804B: http://localhost:9200/#/backtest/ed50a692-6ce7-4014-baea-eb7b6b5acad9
- X804C: http://localhost:9200/#/backtest/09421154-a313-480c-9ab0-6c28cdcf810d
- X805B: http://localhost:9200/#/backtest/22b632fe-7fa2-450a-9f34-47c6e13efec8
- X805C: http://localhost:9200/#/backtest/69c41479-2763-4150-ad60-68e1fd605b41
- Y901B: http://localhost:9200/#/backtest/ee4ecf79-a83d-4388-b4de-3f2e44d62fd2
- Y901C: http://localhost:9200/#/backtest/fc3f7e80-a6a0-4d61-8bc1-11ef693aac9c
- Y902B: http://localhost:9200/#/backtest/cb305a17-1312-463e-bbf1-c8173dfae22c
- Y902C: http://localhost:9200/#/backtest/b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff
- Y903B: http://localhost:9200/#/backtest/99393647-2bca-405b-b3f3-6c2b1a0bed33
- Y903C: http://localhost:9200/#/backtest/745952c3-9fef-4c4c-8450-9fe8b6d142ff

## Comprobaciones

```json
{
  "gates": [
    {
      "name": "V801B:nominal",
      "pass": true
    },
    {
      "name": "V801B:calendar",
      "pass": true
    },
    {
      "name": "V801B:plus10",
      "pass": true
    },
    {
      "name": "V801B:dd",
      "pass": true
    },
    {
      "name": "V801B:modified_entries",
      "pass": true
    },
    {
      "name": "V801B:supplement_fills",
      "pass": true
    },
    {
      "name": "V801B:year_distribution",
      "pass": true
    },
    {
      "name": "V801B:without_best_month",
      "pass": true
    },
    {
      "name": "V801B:eligibility",
      "pass": true
    },
    {
      "name": "V801C:nominal",
      "pass": true
    },
    {
      "name": "V801C:calendar",
      "pass": true
    },
    {
      "name": "V801C:plus10",
      "pass": true
    },
    {
      "name": "V801C:dd",
      "pass": true
    },
    {
      "name": "V801C:modified_entries",
      "pass": true
    },
    {
      "name": "V801C:supplement_fills",
      "pass": true
    },
    {
      "name": "V801C:year_distribution",
      "pass": true
    },
    {
      "name": "V801C:without_best_month",
      "pass": true
    },
    {
      "name": "V801C:eligibility",
      "pass": true
    },
    {
      "name": "V801:bothportfolios",
      "pass": true
    },
    {
      "name": "V802B:nominal",
      "pass": true
    },
    {
      "name": "V802B:calendar",
      "pass": true
    },
    {
      "name": "V802B:plus10",
      "pass": true
    },
    {
      "name": "V802B:dd",
      "pass": true
    },
    {
      "name": "V802B:modified_entries",
      "pass": true
    },
    {
      "name": "V802B:supplement_fills",
      "pass": true
    },
    {
      "name": "V802B:year_distribution",
      "pass": true
    },
    {
      "name": "V802B:without_best_month",
      "pass": true
    },
    {
      "name": "V802B:eligibility",
      "pass": true
    },
    {
      "name": "V802C:nominal",
      "pass": true
    },
    {
      "name": "V802C:calendar",
      "pass": true
    },
    {
      "name": "V802C:plus10",
      "pass": true
    },
    {
      "name": "V802C:dd",
      "pass": true
    },
    {
      "name": "V802C:modified_entries",
      "pass": true
    },
    {
      "name": "V802C:supplement_fills",
      "pass": true
    },
    {
      "name": "V802C:year_distribution",
      "pass": true
    },
    {
      "name": "V802C:without_best_month",
      "pass": true
    },
    {
      "name": "V802C:eligibility",
      "pass": true
    },
    {
      "name": "V802:bothportfolios",
      "pass": true
    },
    {
      "name": "V803B:nominal",
      "pass": true
    },
    {
      "name": "V803B:calendar",
      "pass": true
    },
    {
      "name": "V803B:plus10",
      "pass": true
    },
    {
      "name": "V803B:dd",
      "pass": true
    },
    {
      "name": "V803B:modified_entries",
      "pass": true
    },
    {
      "name": "V803B:supplement_fills",
      "pass": true
    },
    {
      "name": "V803B:year_distribution",
      "pass": true
    },
    {
      "name": "V803B:without_best_month",
      "pass": true
    },
    {
      "name": "V803B:eligibility",
      "pass": true
    },
    {
      "name": "V803C:nominal",
      "pass": true
    },
    {
      "name": "V803C:calendar",
      "pass": true
    },
    {
      "name": "V803C:plus10",
      "pass": true
    },
    {
      "name": "V803C:dd",
      "pass": true
    },
    {
      "name": "V803C:modified_entries",
      "pass": true
    },
    {
      "name": "V803C:supplement_fills",
      "pass": true
    },
    {
      "name": "V803C:year_distribution",
      "pass": true
    },
    {
      "name": "V803C:without_best_month",
      "pass": true
    },
    {
      "name": "V803C:eligibility",
      "pass": true
    },
    {
      "name": "V803:bothportfolios",
      "pass": true
    },
    {
      "name": "V804B:nominal",
      "pass": true
    },
    {
      "name": "V804B:calendar",
      "pass": true
    },
    {
      "name": "V804B:plus10",
      "pass": true
    },
    {
      "name": "V804B:dd",
      "pass": true
    },
    {
      "name": "V804B:modified_entries",
      "pass": true
    },
    {
      "name": "V804B:supplement_fills",
      "pass": true
    },
    {
      "name": "V804B:year_distribution",
      "pass": true
    },
    {
      "name": "V804B:without_best_month",
      "pass": true
    },
    {
      "name": "V804B:eligibility",
      "pass": true
    },
    {
      "name": "V804C:nominal",
      "pass": true
    },
    {
      "name": "V804C:calendar",
      "pass": true
    },
    {
      "name": "V804C:plus10",
      "pass": true
    },
    {
      "name": "V804C:dd",
      "pass": true
    },
    {
      "name": "V804C:modified_entries",
      "pass": true
    },
    {
      "name": "V804C:supplement_fills",
      "pass": true
    },
    {
      "name": "V804C:year_distribution",
      "pass": true
    },
    {
      "name": "V804C:without_best_month",
      "pass": true
    },
    {
      "name": "V804C:eligibility",
      "pass": true
    },
    {
      "name": "V804:bothportfolios",
      "pass": true
    },
    {
      "name": "V805B:nominal",
      "pass": true
    },
    {
      "name": "V805B:calendar",
      "pass": true
    },
    {
      "name": "V805B:plus10",
      "pass": true
    },
    {
      "name": "V805B:dd",
      "pass": true
    },
    {
      "name": "V805B:modified_entries",
      "pass": true
    },
    {
      "name": "V805B:supplement_fills",
      "pass": true
    },
    {
      "name": "V805B:year_distribution",
      "pass": true
    },
    {
      "name": "V805B:without_best_month",
      "pass": true
    },
    {
      "name": "V805B:eligibility",
      "pass": true
    },
    {
      "name": "V805C:nominal",
      "pass": true
    },
    {
      "name": "V805C:calendar",
      "pass": true
    },
    {
      "name": "V805C:plus10",
      "pass": true
    },
    {
      "name": "V805C:dd",
      "pass": true
    },
    {
      "name": "V805C:modified_entries",
      "pass": true
    },
    {
      "name": "V805C:supplement_fills",
      "pass": true
    },
    {
      "name": "V805C:year_distribution",
      "pass": true
    },
    {
      "name": "V805C:without_best_month",
      "pass": true
    },
    {
      "name": "V805C:eligibility",
      "pass": true
    },
    {
      "name": "V805:bothportfolios",
      "pass": true
    },
    {
      "name": "X801B:nominal",
      "pass": true
    },
    {
      "name": "X801B:calendar",
      "pass": true
    },
    {
      "name": "X801B:plus10",
      "pass": true
    },
    {
      "name": "X801B:dd",
      "pass": true
    },
    {
      "name": "X801B:modified_entries",
      "pass": true
    },
    {
      "name": "X801B:supplement_fills",
      "pass": true
    },
    {
      "name": "X801B:year_distribution",
      "pass": true
    },
    {
      "name": "X801B:without_best_month",
      "pass": true
    },
    {
      "name": "X801B:eligibility",
      "pass": true
    },
    {
      "name": "X801C:nominal",
      "pass": true
    },
    {
      "name": "X801C:calendar",
      "pass": true
    },
    {
      "name": "X801C:plus10",
      "pass": true
    },
    {
      "name": "X801C:dd",
      "pass": true
    },
    {
      "name": "X801C:modified_entries",
      "pass": true
    },
    {
      "name": "X801C:supplement_fills",
      "pass": true
    },
    {
      "name": "X801C:year_distribution",
      "pass": true
    },
    {
      "name": "X801C:without_best_month",
      "pass": true
    },
    {
      "name": "X801C:eligibility",
      "pass": true
    },
    {
      "name": "X801:bothportfolios",
      "pass": true
    },
    {
      "name": "X802B:nominal",
      "pass": true
    },
    {
      "name": "X802B:calendar",
      "pass": true
    },
    {
      "name": "X802B:plus10",
      "pass": true
    },
    {
      "name": "X802B:dd",
      "pass": true
    },
    {
      "name": "X802B:modified_entries",
      "pass": true
    },
    {
      "name": "X802B:supplement_fills",
      "pass": true
    },
    {
      "name": "X802B:year_distribution",
      "pass": true
    },
    {
      "name": "X802B:without_best_month",
      "pass": true
    },
    {
      "name": "X802B:eligibility",
      "pass": true
    },
    {
      "name": "X802C:nominal",
      "pass": true
    },
    {
      "name": "X802C:calendar",
      "pass": true
    },
    {
      "name": "X802C:plus10",
      "pass": true
    },
    {
      "name": "X802C:dd",
      "pass": true
    },
    {
      "name": "X802C:modified_entries",
      "pass": true
    },
    {
      "name": "X802C:supplement_fills",
      "pass": true
    },
    {
      "name": "X802C:year_distribution",
      "pass": true
    },
    {
      "name": "X802C:without_best_month",
      "pass": true
    },
    {
      "name": "X802C:eligibility",
      "pass": true
    },
    {
      "name": "X802:bothportfolios",
      "pass": true
    },
    {
      "name": "X803B:nominal",
      "pass": true
    },
    {
      "name": "X803B:calendar",
      "pass": true
    },
    {
      "name": "X803B:plus10",
      "pass": true
    },
    {
      "name": "X803B:dd",
      "pass": true
    },
    {
      "name": "X803B:modified_entries",
      "pass": true
    },
    {
      "name": "X803B:supplement_fills",
      "pass": true
    },
    {
      "name": "X803B:year_distribution",
      "pass": true
    },
    {
      "name": "X803B:without_best_month",
      "pass": true
    },
    {
      "name": "X803B:eligibility",
      "pass": true
    },
    {
      "name": "X803C:nominal",
      "pass": true
    },
    {
      "name": "X803C:calendar",
      "pass": true
    },
    {
      "name": "X803C:plus10",
      "pass": true
    },
    {
      "name": "X803C:dd",
      "pass": true
    },
    {
      "name": "X803C:modified_entries",
      "pass": true
    },
    {
      "name": "X803C:supplement_fills",
      "pass": true
    },
    {
      "name": "X803C:year_distribution",
      "pass": true
    },
    {
      "name": "X803C:without_best_month",
      "pass": true
    },
    {
      "name": "X803C:eligibility",
      "pass": true
    },
    {
      "name": "X803:bothportfolios",
      "pass": true
    },
    {
      "name": "X804B:nominal",
      "pass": true
    },
    {
      "name": "X804B:calendar",
      "pass": true
    },
    {
      "name": "X804B:plus10",
      "pass": true
    },
    {
      "name": "X804B:dd",
      "pass": true
    },
    {
      "name": "X804B:modified_entries",
      "pass": true
    },
    {
      "name": "X804B:supplement_fills",
      "pass": true
    },
    {
      "name": "X804B:year_distribution",
      "pass": true
    },
    {
      "name": "X804B:without_best_month",
      "pass": true
    },
    {
      "name": "X804B:eligibility",
      "pass": true
    },
    {
      "name": "X804C:nominal",
      "pass": true
    },
    {
      "name": "X804C:calendar",
      "pass": true
    },
    {
      "name": "X804C:plus10",
      "pass": true
    },
    {
      "name": "X804C:dd",
      "pass": true
    },
    {
      "name": "X804C:modified_entries",
      "pass": true
    },
    {
      "name": "X804C:supplement_fills",
      "pass": true
    },
    {
      "name": "X804C:year_distribution",
      "pass": true
    },
    {
      "name": "X804C:without_best_month",
      "pass": true
    },
    {
      "name": "X804C:eligibility",
      "pass": true
    },
    {
      "name": "X804:bothportfolios",
      "pass": true
    },
    {
      "name": "X805B:nominal",
      "pass": true
    },
    {
      "name": "X805B:calendar",
      "pass": true
    },
    {
      "name": "X805B:plus10",
      "pass": true
    },
    {
      "name": "X805B:dd",
      "pass": true
    },
    {
      "name": "X805B:modified_entries",
      "pass": true
    },
    {
      "name": "X805B:supplement_fills",
      "pass": true
    },
    {
      "name": "X805B:year_distribution",
      "pass": true
    },
    {
      "name": "X805B:without_best_month",
      "pass": true
    },
    {
      "name": "X805B:eligibility",
      "pass": true
    },
    {
      "name": "X805C:nominal",
      "pass": true
    },
    {
      "name": "X805C:calendar",
      "pass": true
    },
    {
      "name": "X805C:plus10",
      "pass": true
    },
    {
      "name": "X805C:dd",
      "pass": true
    },
    {
      "name": "X805C:modified_entries",
      "pass": true
    },
    {
      "name": "X805C:supplement_fills",
      "pass": true
    },
    {
      "name": "X805C:year_distribution",
      "pass": true
    },
    {
      "name": "X805C:without_best_month",
      "pass": true
    },
    {
      "name": "X805C:eligibility",
      "pass": true
    },
    {
      "name": "X805:bothportfolios",
      "pass": true
    },
    {
      "name": "Y901B:nominal",
      "pass": true
    },
    {
      "name": "Y901B:calendar",
      "pass": true
    },
    {
      "name": "Y901B:plus10",
      "pass": true
    },
    {
      "name": "Y901B:dd",
      "pass": true
    },
    {
      "name": "Y901B:modified_entries",
      "pass": true
    },
    {
      "name": "Y901B:supplement_fills",
      "pass": true
    },
    {
      "name": "Y901B:year_distribution",
      "pass": true
    },
    {
      "name": "Y901B:without_best_month",
      "pass": true
    },
    {
      "name": "Y901B:eligibility",
      "pass": true
    },
    {
      "name": "Y901C:nominal",
      "pass": true
    },
    {
      "name": "Y901C:calendar",
      "pass": true
    },
    {
      "name": "Y901C:plus10",
      "pass": true
    },
    {
      "name": "Y901C:dd",
      "pass": true
    },
    {
      "name": "Y901C:modified_entries",
      "pass": true
    },
    {
      "name": "Y901C:supplement_fills",
      "pass": true
    },
    {
      "name": "Y901C:year_distribution",
      "pass": true
    },
    {
      "name": "Y901C:without_best_month",
      "pass": true
    },
    {
      "name": "Y901C:eligibility",
      "pass": true
    },
    {
      "name": "Y901:bothportfolios",
      "pass": true
    },
    {
      "name": "Y902B:nominal",
      "pass": true
    },
    {
      "name": "Y902B:calendar",
      "pass": true
    },
    {
      "name": "Y902B:plus10",
      "pass": true
    },
    {
      "name": "Y902B:dd",
      "pass": true
    },
    {
      "name": "Y902B:modified_entries",
      "pass": true
    },
    {
      "name": "Y902B:supplement_fills",
      "pass": true
    },
    {
      "name": "Y902B:year_distribution",
      "pass": true
    },
    {
      "name": "Y902B:without_best_month",
      "pass": true
    },
    {
      "name": "Y902B:eligibility",
      "pass": true
    },
    {
      "name": "Y902C:nominal",
      "pass": true
    },
    {
      "name": "Y902C:calendar",
      "pass": true
    },
    {
      "name": "Y902C:plus10",
      "pass": true
    },
    {
      "name": "Y902C:dd",
      "pass": true
    },
    {
      "name": "Y902C:modified_entries",
      "pass": true
    },
    {
      "name": "Y902C:supplement_fills",
      "pass": true
    },
    {
      "name": "Y902C:year_distribution",
      "pass": true
    },
    {
      "name": "Y902C:without_best_month",
      "pass": true
    },
    {
      "name": "Y902C:eligibility",
      "pass": true
    },
    {
      "name": "Y902:bothportfolios",
      "pass": true
    },
    {
      "name": "Y903B:nominal",
      "pass": true
    },
    {
      "name": "Y903B:calendar",
      "pass": true
    },
    {
      "name": "Y903B:plus10",
      "pass": true
    },
    {
      "name": "Y903B:dd",
      "pass": true
    },
    {
      "name": "Y903B:modified_entries",
      "pass": true
    },
    {
      "name": "Y903B:supplement_fills",
      "pass": true
    },
    {
      "name": "Y903B:year_distribution",
      "pass": true
    },
    {
      "name": "Y903B:without_best_month",
      "pass": true
    },
    {
      "name": "Y903B:eligibility",
      "pass": true
    },
    {
      "name": "Y903C:nominal",
      "pass": true
    },
    {
      "name": "Y903C:calendar",
      "pass": true
    },
    {
      "name": "Y903C:plus10",
      "pass": true
    },
    {
      "name": "Y903C:dd",
      "pass": true
    },
    {
      "name": "Y903C:modified_entries",
      "pass": true
    },
    {
      "name": "Y903C:supplement_fills",
      "pass": true
    },
    {
      "name": "Y903C:year_distribution",
      "pass": true
    },
    {
      "name": "Y903C:without_best_month",
      "pass": true
    },
    {
      "name": "Y903C:eligibility",
      "pass": true
    },
    {
      "name": "Y903:bothportfolios",
      "pass": true
    },
    {
      "name": "selectionempty",
      "pass": true
    }
  ],
  "trace": [
    {
      "name": "Y903B:supplementPair0",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair1",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair2",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair3",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair4",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair5",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair6",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair7",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair8",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair9",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair10",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair11",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair12",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair13",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair14",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair15",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair16",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair17",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair18",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair19",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair20",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair21",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair22",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair23",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair24",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair25",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair26",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair27",
      "pass": true
    },
    {
      "name": "Y903B:supplementPair28",
      "pass": true
    },
    {
      "name": "Y903B:count",
      "pass": true
    },
    {
      "name": "Y903B:unique",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair0",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair1",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair2",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair3",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair4",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair5",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair6",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair7",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair8",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair9",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair10",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair11",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair12",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair13",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair14",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair15",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair16",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair17",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair18",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair19",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair20",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair21",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair22",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair23",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair24",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair25",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair26",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair27",
      "pass": true
    },
    {
      "name": "Y903C:supplementPair28",
      "pass": true
    },
    {
      "name": "Y903C:count",
      "pass": true
    },
    {
      "name": "Y903C:unique",
      "pass": true
    }
  ]
}
```
