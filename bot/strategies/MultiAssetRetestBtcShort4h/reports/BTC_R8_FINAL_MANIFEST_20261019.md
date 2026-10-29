# BTC R8 — manifiesto de cierre

26 backtests nominales terminados y auditados; ninguna receta elegible. Se aplica la regla congelada: cero backtests adicionales. 26 formularios / 78 snapshots coherentes, 37 fuentes exactas al readback final, 13 auditorías financieras de pares con cuatro anclas inmutables y reconciliación terminal. Identificación de suplementos creativos por logs paginados completos, separada de los cálculos financieros. Sin reinicios, purgas ni eliminación de historial. 2026 permanece cerrado.

QA registra comprobaciones de fixtures y fuentes, no pruebas de rentabilidad ni cobertura exhaustiva del motor. Análisis y figuras derivadas no cuentan como nuevas observaciones independientes. La muestra de desarrollo se reutilizó; no hay validación fuera de muestra en esta ronda.

```json
{
  "research": "R8",
  "closed_2026": true,
  "window": "2020-10-15 inclusive ->2025-12-31 exclusive",
  "nominal_fulls": 26,
  "extra_fulls": 0,
  "selected": null,
  "eligible": [],
  "registry": [
    {
      "name": "V801B",
      "id": "b0c5ce4f-ed64-4b07-bdca-f708aae2d445",
      "url": "http://localhost:9200/#/backtest/b0c5ce4f-ed64-4b07-bdca-f708aae2d445",
      "strategy": "BtcContextR801",
      "seed": "N204",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "V801C",
      "id": "5de86562-4ba7-4f2f-b9fb-f647ed2a8b70",
      "url": "http://localhost:9200/#/backtest/5de86562-4ba7-4f2f-b9fb-f647ed2a8b70",
      "strategy": "BtcContextR801",
      "seed": "N204",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "V802B",
      "id": "876feccb-b93c-4fb0-a6ea-3a4b58c642c7",
      "url": "http://localhost:9200/#/backtest/876feccb-b93c-4fb0-a6ea-3a4b58c642c7",
      "strategy": "BtcContextR802",
      "seed": "N204",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "V802C",
      "id": "8e889155-eabc-4187-acc5-748f98dc5378",
      "url": "http://localhost:9200/#/backtest/8e889155-eabc-4187-acc5-748f98dc5378",
      "strategy": "BtcContextR802",
      "seed": "N204",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "V803B",
      "id": "e7ef94a6-5249-44ea-b0bc-8c3cb7e3c531",
      "url": "http://localhost:9200/#/backtest/e7ef94a6-5249-44ea-b0bc-8c3cb7e3c531",
      "strategy": "BtcContextR803",
      "seed": "N204",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "V803C",
      "id": "1d818489-9707-43ab-8106-98cacdbf0a56",
      "url": "http://localhost:9200/#/backtest/1d818489-9707-43ab-8106-98cacdbf0a56",
      "strategy": "BtcContextR803",
      "seed": "N204",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "V804B",
      "id": "b481d1da-f0b2-4c9c-b663-b4a4a8c44896",
      "url": "http://localhost:9200/#/backtest/b481d1da-f0b2-4c9c-b663-b4a4a8c44896",
      "strategy": "BtcContextR804",
      "seed": "N204",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "V804C",
      "id": "b042558a-4ea4-41f1-a2de-7d51d8d53b56",
      "url": "http://localhost:9200/#/backtest/b042558a-4ea4-41f1-a2de-7d51d8d53b56",
      "strategy": "BtcContextR804",
      "seed": "N204",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "V805B",
      "id": "0af9be29-c28a-490b-a7d7-6a481660a950",
      "url": "http://localhost:9200/#/backtest/0af9be29-c28a-490b-a7d7-6a481660a950",
      "strategy": "BtcContextR805",
      "seed": "N204",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "V805C",
      "id": "ec8d524e-d8c0-4b55-8dbe-da6ae8051918",
      "url": "http://localhost:9200/#/backtest/ec8d524e-d8c0-4b55-8dbe-da6ae8051918",
      "strategy": "BtcContextR805",
      "seed": "N204",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "X801C",
      "id": "4e432aac-71c2-4023-a978-6d8a618aa660",
      "url": "http://localhost:9200/#/backtest/4e432aac-71c2-4023-a978-6d8a618aa660",
      "strategy": "BTCExploreR801",
      "seed": "N204",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "X801B",
      "id": "f660ef63-d7c6-4792-9f21-06c1d7ebd85f",
      "url": "http://localhost:9200/#/backtest/f660ef63-d7c6-4792-9f21-06c1d7ebd85f",
      "strategy": "BTCExploreR801",
      "seed": "N204",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "X802B",
      "id": "261696a9-33ee-4504-a310-b8a44c63dcd3",
      "url": "http://localhost:9200/#/backtest/261696a9-33ee-4504-a310-b8a44c63dcd3",
      "strategy": "BTCExploreR802",
      "seed": "N204",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "X802C",
      "id": "07a45656-81e2-4fd8-9851-3aa16a782c2e",
      "url": "http://localhost:9200/#/backtest/07a45656-81e2-4fd8-9851-3aa16a782c2e",
      "strategy": "BTCExploreR802",
      "seed": "N204",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "X803B",
      "id": "5208fe79-c420-4328-b5dd-1a67177f1ccf",
      "url": "http://localhost:9200/#/backtest/5208fe79-c420-4328-b5dd-1a67177f1ccf",
      "strategy": "BTCExploreR803",
      "seed": "N204",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "X803C",
      "id": "a86de192-2f0d-4b34-a4ae-ce4f686d4757",
      "url": "http://localhost:9200/#/backtest/a86de192-2f0d-4b34-a4ae-ce4f686d4757",
      "strategy": "BTCExploreR803",
      "seed": "N204",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "X804C",
      "id": "09421154-a313-480c-9ab0-6c28cdcf810d",
      "url": "http://localhost:9200/#/backtest/09421154-a313-480c-9ab0-6c28cdcf810d",
      "strategy": "BTCExploreR804",
      "seed": "N204",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "X804B",
      "id": "ed50a692-6ce7-4014-baea-eb7b6b5acad9",
      "url": "http://localhost:9200/#/backtest/ed50a692-6ce7-4014-baea-eb7b6b5acad9",
      "strategy": "BTCExploreR804",
      "seed": "N204",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "X805C",
      "id": "69c41479-2763-4150-ad60-68e1fd605b41",
      "url": "http://localhost:9200/#/backtest/69c41479-2763-4150-ad60-68e1fd605b41",
      "strategy": "BTCExploreR805",
      "seed": "N204",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "X805B",
      "id": "22b632fe-7fa2-450a-9f34-47c6e13efec8",
      "url": "http://localhost:9200/#/backtest/22b632fe-7fa2-450a-9f34-47c6e13efec8",
      "strategy": "BTCExploreR805",
      "seed": "N204",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "Y901B",
      "id": "ee4ecf79-a83d-4388-b4de-3f2e44d62fd2",
      "url": "http://localhost:9200/#/backtest/ee4ecf79-a83d-4388-b4de-3f2e44d62fd2",
      "strategy": "BTCNovelR901",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "Y901C",
      "id": "fc3f7e80-a6a0-4d61-8bc1-11ef693aac9c",
      "url": "http://localhost:9200/#/backtest/fc3f7e80-a6a0-4d61-8bc1-11ef693aac9c",
      "strategy": "BTCNovelR901",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "Y902C",
      "id": "b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff",
      "url": "http://localhost:9200/#/backtest/b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff",
      "strategy": "BTCNovelR902",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "Y902B",
      "id": "cb305a17-1312-463e-bbf1-c8173dfae22c",
      "url": "http://localhost:9200/#/backtest/cb305a17-1312-463e-bbf1-c8173dfae22c",
      "strategy": "BTCNovelR902",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "Y903B",
      "id": "99393647-2bca-405b-b3f3-6c2b1a0bed33",
      "url": "http://localhost:9200/#/backtest/99393647-2bca-405b-b3f3-6c2b1a0bed33",
      "strategy": "BTCNovelR903",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "Y903C",
      "id": "745952c3-9fef-4c4c-8450-9fe8b6d142ff",
      "url": "http://localhost:9200/#/backtest/745952c3-9fef-4c4c-8450-9fe8b6d142ff",
      "strategy": "BTCNovelR903",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    }
  ],
  "forms": {
    "b0c5ce4f-ed64-4b07-bdca-f708aae2d445": {
      "name": "V801B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "5de86562-4ba7-4f2f-b9fb-f647ed2a8b70": {
      "name": "V801C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "4e432aac-71c2-4023-a978-6d8a618aa660": {
      "name": "X801C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "f660ef63-d7c6-4792-9f21-06c1d7ebd85f": {
      "name": "X801B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "876feccb-b93c-4fb0-a6ea-3a4b58c642c7": {
      "name": "V802B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "8e889155-eabc-4187-acc5-748f98dc5378": {
      "name": "V802C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "261696a9-33ee-4504-a310-b8a44c63dcd3": {
      "name": "X802B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "07a45656-81e2-4fd8-9851-3aa16a782c2e": {
      "name": "X802C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "e7ef94a6-5249-44ea-b0bc-8c3cb7e3c531": {
      "name": "V803B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "1d818489-9707-43ab-8106-98cacdbf0a56": {
      "name": "V803C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "5208fe79-c420-4328-b5dd-1a67177f1ccf": {
      "name": "X803B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "a86de192-2f0d-4b34-a4ae-ce4f686d4757": {
      "name": "X803C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "b481d1da-f0b2-4c9c-b663-b4a4a8c44896": {
      "name": "V804B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "b042558a-4ea4-41f1-a2de-7d51d8d53b56": {
      "name": "V804C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "09421154-a313-480c-9ab0-6c28cdcf810d": {
      "name": "X804C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "ed50a692-6ce7-4014-baea-eb7b6b5acad9": {
      "name": "X804B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "69c41479-2763-4150-ad60-68e1fd605b41": {
      "name": "X805C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "22b632fe-7fa2-450a-9f34-47c6e13efec8": {
      "name": "X805B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "0af9be29-c28a-490b-a7d7-6a481660a950": {
      "name": "V805B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "ec8d524e-d8c0-4b55-8dbe-da6ae8051918": {
      "name": "V805C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "ee4ecf79-a83d-4388-b4de-3f2e44d62fd2": {
      "name": "Y901B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "fc3f7e80-a6a0-4d61-8bc1-11ef693aac9c": {
      "name": "Y901C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "b5a2a176-9a8d-4dc8-b51e-5d03dd2fcdff": {
      "name": "Y902C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "cb305a17-1312-463e-bbf1-c8173dfae22c": {
      "name": "Y902B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "99393647-2bca-405b-b3f3-6c2b1a0bed33": {
      "name": "Y903B",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    },
    "745952c3-9fef-4c4c-8450-9fe8b6d142ff": {
      "name": "Y903C",
      "status": "finished",
      "dates": true,
      "routes": true,
      "feeds": true,
      "settings": true,
      "sources": [
        true,
        true,
        true
      ]
    }
  },
  "source_checks": [
    {
      "name": "BtcExploreR103",
      "exact": true,
      "chars": 21361
    },
    {
      "name": "PortComparePaxgMarket4h",
      "exact": true,
      "chars": 16178
    },
    {
      "name": "PortCompareSpySecond4h",
      "exact": true,
      "chars": 19930
    },
    {
      "name": "PortCompareSpyMarket4h",
      "exact": true,
      "chars": 20101
    },
    {
      "name": "PortCompareBtc4h",
      "exact": true,
      "chars": 15447
    },
    {
      "name": "X03ExploreR204",
      "exact": true,
      "chars": 21582
    },
    {
      "name": "N204ExploreR503",
      "exact": true,
      "chars": 22182
    },
    {
      "name": "N503ExploreR601",
      "exact": true,
      "chars": 22492
    },
    {
      "name": "N503ExploreR602",
      "exact": true,
      "chars": 22644
    },
    {
      "name": "N503ExploreR603",
      "exact": true,
      "chars": 22469
    },
    {
      "name": "N503ExploreR604",
      "exact": true,
      "chars": 22679
    },
    {
      "name": "N503ExploreR605",
      "exact": true,
      "chars": 24147
    },
    {
      "name": "N503CapacityR601",
      "exact": true,
      "chars": 24511
    },
    {
      "name": "N503CapacityR602",
      "exact": true,
      "chars": 24717
    },
    {
      "name": "N503CapacityR603",
      "exact": true,
      "chars": 24908
    },
    {
      "name": "N503CapacityR604",
      "exact": true,
      "chars": 25412
    },
    {
      "name": "N503CapacityR605",
      "exact": true,
      "chars": 25230
    },
    {
      "name": "N503ManageR701",
      "exact": true,
      "chars": 26071
    },
    {
      "name": "N503ManageR702",
      "exact": true,
      "chars": 25731
    },
    {
      "name": "N503ManageR703",
      "exact": true,
      "chars": 25886
    },
    {
      "name": "N503ManageR704",
      "exact": true,
      "chars": 25748
    },
    {
      "name": "N204ManageR705",
      "exact": true,
      "chars": 25132
    },
    {
      "name": "N204ManageR706",
      "exact": true,
      "chars": 25287
    },
    {
      "name": "N503ObserveR700",
      "exact": true,
      "chars": 25970
    },
    {
      "name": "BtcContextR801",
      "exact": true,
      "chars": 22564
    },
    {
      "name": "BtcContextR802",
      "exact": true,
      "chars": 24810
    },
    {
      "name": "BtcContextR803",
      "exact": true,
      "chars": 24821
    },
    {
      "name": "BtcContextR804",
      "exact": true,
      "chars": 24820
    },
    {
      "name": "BtcContextR805",
      "exact": true,
      "chars": 24826
    },
    {
      "name": "BTCExploreR801",
      "exact": true,
      "chars": 21318
    },
    {
      "name": "BTCExploreR802",
      "exact": true,
      "chars": 21247
    },
    {
      "name": "BTCExploreR803",
      "exact": true,
      "chars": 21530
    },
    {
      "name": "BTCExploreR804",
      "exact": true,
      "chars": 21328
    },
    {
      "name": "BTCExploreR805",
      "exact": true,
      "chars": 23569
    },
    {
      "name": "BTCNovelR901",
      "exact": true,
      "chars": 23016
    },
    {
      "name": "BTCNovelR902",
      "exact": true,
      "chars": 23016
    },
    {
      "name": "BTCNovelR903",
      "exact": true,
      "chars": 24215
    }
  ],
  "qa_jobs": [
    {
      "family": "context",
      "job": "44c8766edb5e4eb7a39112996ea5280a",
      "checks": 102
    },
    {
      "family": "experimental",
      "job": "02f73c58f2c3422cbd48344fcc4cb74e",
      "checks": 184
    },
    {
      "family": "creative_initial",
      "job": "795e5b8a6a8d444eb4c1468716674788",
      "checks": 200
    },
    {
      "family": "creative_final_telemetry",
      "job": "745b2036ce3c456c933267f36026baaf",
      "checks": 201
    }
  ],
  "financial_jobs": [
    {
      "batch": "V801",
      "names": [
        "V801B",
        "V801C"
      ],
      "job": "2c5b266bf19a422180c1c14b8e3206a0",
      "status": "succeeded"
    },
    {
      "batch": "X801",
      "names": [
        "X801B",
        "X801C"
      ],
      "job": "90dc2c2281d34b2a858e62cdc57d4b09",
      "status": "succeeded"
    },
    {
      "batch": "V802",
      "names": [
        "V802B",
        "V802C"
      ],
      "job": "2db618493b2b4e299b6efe84c609cb7a",
      "status": "succeeded"
    },
    {
      "batch": "X802",
      "names": [
        "X802B",
        "X802C"
      ],
      "job": "3c415386ccd245029ae5d51228e0b1e2",
      "status": "succeeded"
    },
    {
      "batch": "V803",
      "names": [
        "V803B",
        "V803C"
      ],
      "job": "d98bf412474840ceaeefc087880b3856",
      "status": "succeeded"
    },
    {
      "batch": "X803",
      "names": [
        "X803B",
        "X803C"
      ],
      "job": "86bb83956bb942d584fa13b706cb371f",
      "status": "succeeded"
    },
    {
      "batch": "V804",
      "names": [
        "V804B",
        "V804C"
      ],
      "job": "7f586b3ec7f84bb9bc8fbdfe28f03aed",
      "status": "succeeded"
    },
    {
      "batch": "X804",
      "names": [
        "X804B",
        "X804C"
      ],
      "job": "22acea68e8574c2f8b1a10b1b0e32e69",
      "status": "succeeded"
    },
    {
      "batch": "V805",
      "names": [
        "V805B",
        "V805C"
      ],
      "job": "ea4903ff2ffb4921a49b050ec8aabe60",
      "status": "succeeded"
    },
    {
      "batch": "X805",
      "names": [
        "X805B",
        "X805C"
      ],
      "job": "dc76be2c57b2461a91b319f4decacc99",
      "status": "succeeded"
    },
    {
      "batch": "Y901",
      "names": [
        "Y901B",
        "Y901C"
      ],
      "job": "26a008d34c3f402c8dbf5429e40afb1b",
      "status": "succeeded"
    },
    {
      "batch": "Y902",
      "names": [
        "Y902B",
        "Y902C"
      ],
      "job": "b997bf717a4149b0b3c8a57ff0ba07ae",
      "status": "succeeded"
    },
    {
      "batch": "Y903",
      "names": [
        "Y903B",
        "Y903C"
      ],
      "job": "aae5cdc6f7a64478a1ec82b5371fdb29",
      "status": "succeeded"
    }
  ],
  "financial_audits": [
    {
      "name": "V801B",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "V801C",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "V802B",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "V802C",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "V803B",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "V803C",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "V804B",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "V804C",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "V805B",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "V805C",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "X801C",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "X801B",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "X802B",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "X802C",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "X803B",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "X803C",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "X804C",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "X804B",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "X805C",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "X805B",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "Y901B",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "Y901C",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "Y902C",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "Y902B",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "Y903B",
      "status": "passed",
      "terminal": true
    },
    {
      "name": "Y903C",
      "status": "passed",
      "terminal": true
    }
  ],
  "sleeve_metadata": {
    "N503B": {
      "ok": true,
      "log_fill_count": 67,
      "terminal_fills": 67,
      "matched": 67,
      "pages": 17,
      "lines_read": 8467,
      "boundary_counter_adjustment": 0,
      "types": {
        "MARKET": 67
      },
      "errors": []
    },
    "N503C": {
      "ok": true,
      "log_fill_count": 67,
      "terminal_fills": 67,
      "matched": 67,
      "pages": 18,
      "lines_read": 8671,
      "boundary_counter_adjustment": 0,
      "types": {
        "MARKET": 67
      },
      "errors": []
    },
    "Y901B": {
      "ok": true,
      "log_fill_count": 33,
      "terminal_fills": 33,
      "matched": 33,
      "pages": 17,
      "lines_read": 8087,
      "boundary_counter_adjustment": 0,
      "types": {
        "LIMIT": 33
      },
      "errors": []
    },
    "Y901C": {
      "ok": true,
      "log_fill_count": 33,
      "terminal_fills": 33,
      "matched": 33,
      "pages": 17,
      "lines_read": 8291,
      "boundary_counter_adjustment": 0,
      "types": {
        "LIMIT": 33
      },
      "errors": []
    },
    "Y902C": {
      "ok": true,
      "log_fill_count": 46,
      "terminal_fills": 46,
      "matched": 46,
      "pages": 17,
      "lines_read": 8385,
      "boundary_counter_adjustment": 0,
      "types": {
        "STOP": 45,
        "MARKET": 1
      },
      "errors": []
    },
    "Y902B": {
      "ok": true,
      "log_fill_count": 46,
      "terminal_fills": 46,
      "matched": 46,
      "pages": 17,
      "lines_read": 8181,
      "boundary_counter_adjustment": 0,
      "types": {
        "STOP": 45,
        "MARKET": 1
      },
      "errors": []
    },
    "Y903B": {
      "ok": true,
      "log_fill_count": 70,
      "terminal_fills": 70,
      "matched": 70,
      "pages": 18,
      "lines_read": 8591,
      "boundary_counter_adjustment": 0,
      "types": {
        "MARKET": 70
      },
      "errors": []
    },
    "Y903C": {
      "ok": true,
      "log_fill_count": 70,
      "terminal_fills": 70,
      "matched": 70,
      "pages": 18,
      "lines_read": 8795,
      "boundary_counter_adjustment": 0,
      "types": {
        "MARKET": 70
      },
      "errors": []
    }
  },
  "ranking": {
    "matrix": [
      {
        "id": "V801",
        "strategy": "BtcContextR801",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 13328.71171281593,
            "delta": 272.0967977382661,
            "delta_seed": 272.0967977382661,
            "plus10": 11220.146271081927,
            "delta10": 288.9365275360633,
            "dd": -8.78368484676294,
            "counts": {
              "Mfull": "41/61",
              "Mall": "41/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.0007936507936507908,
            "modified_exits": 0,
            "changed_supplement_entries": 14,
            "supplement_fills": 67,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": -72.90188103549553,
              "2022": 87.32831076860566,
              "2023": 405.01430376222197,
              "2024": 74.43740092361259,
              "2025": -221.78133668066585
            },
            "positive_years": 3,
            "best_incremental_month": 159.5820684544633,
            "delta_without_best_month": 112.51472928380281,
            "gates": {
              "nominal": true,
              "calendar": true,
              "plus10": true,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": true,
              "without_best_month": true
            },
            "eligible": true
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 13536.902513059405,
            "delta": 297.4601332126131,
            "delta_seed": 297.4601332126131,
            "plus10": 11314.250079982301,
            "delta10": 310.83461560191427,
            "dd": -9.054184091363382,
            "counts": {
              "Mfull": "40/61",
              "Mall": "40/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.015079365079365137,
            "modified_exits": 0,
            "changed_supplement_entries": 14,
            "supplement_fills": 67,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": -63.82971253784126,
              "2022": 83.56625363574494,
              "2023": 417.2901000535858,
              "2024": 73.62851916740692,
              "2025": -213.19502710630331
            },
            "positive_years": 3,
            "best_incremental_month": 155.548978857978,
            "delta_without_best_month": 141.91115435463507,
            "gates": {
              "nominal": true,
              "calendar": false,
              "plus10": true,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": true,
              "without_best_month": true
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.015079365079365137,
        "delta10": 288.9365275360633,
        "worstDD": -9.054184091363382
      },
      {
        "id": "V802",
        "strategy": "BtcContextR802",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 12838.90136850396,
            "delta": -217.71354657370284,
            "delta_seed": -217.71354657370284,
            "plus10": 10719.75434351168,
            "delta10": -211.45540003418319,
            "dd": -9.58638892964332,
            "counts": {
              "Mfull": "40/61",
              "Mall": "40/63",
              "Qfull": "16/19",
              "Qall": "17/21"
            },
            "margin": -0.015079365079365137,
            "modified_exits": 0,
            "changed_supplement_entries": 1,
            "supplement_fills": 78,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": 0,
              "2022": 0,
              "2023": 0,
              "2024": -182.3491912662139,
              "2025": -35.36435530746894
            },
            "positive_years": 0,
            "best_incremental_month": 7.276918231153104,
            "delta_without_best_month": -224.99046480485595,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": false,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 13013.553731190143,
            "delta": -225.88864865664982,
            "delta_seed": -225.88864865664982,
            "plus10": 10784.301180705828,
            "delta10": -219.11428367455846,
            "dd": -9.58992909843186,
            "counts": {
              "Mfull": "40/61",
              "Mall": "40/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.015079365079365137,
            "modified_exits": 0,
            "changed_supplement_entries": 1,
            "supplement_fills": 78,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": 0,
              "2022": 0,
              "2023": 0,
              "2024": -189.31673454334668,
              "2025": -36.571914113308594
            },
            "positive_years": 0,
            "best_incremental_month": 8.888303590447322,
            "delta_without_best_month": -234.77695224709714,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": false,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.015079365079365137,
        "delta10": -219.11428367455846,
        "worstDD": -9.58992909843186
      },
      {
        "id": "V803",
        "strategy": "BtcContextR803",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 13056.614915077664,
            "delta": 0,
            "delta_seed": 0,
            "plus10": 10931.209743545864,
            "delta10": 0,
            "dd": -8.77680090479469,
            "counts": {
              "Mfull": "41/61",
              "Mall": "41/63",
              "Qfull": "16/19",
              "Qall": "17/21"
            },
            "margin": 0.0007936507936507908,
            "modified_exits": 0,
            "changed_supplement_entries": 0,
            "supplement_fills": 79,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": 0,
              "2022": 0,
              "2023": 0,
              "2024": 0,
              "2025": 0
            },
            "positive_years": 0,
            "best_incremental_month": 1.0913936421275139e-11,
            "delta_without_best_month": -1.0913936421275139e-11,
            "gates": {
              "nominal": false,
              "calendar": true,
              "plus10": true,
              "dd": true,
              "modified_entries": false,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 13239.442379846792,
            "delta": 0,
            "delta_seed": 0,
            "plus10": 11003.415464380387,
            "delta10": 0,
            "dd": -9.057883731399553,
            "counts": {
              "Mfull": "41/61",
              "Mall": "41/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.0007936507936507908,
            "modified_exits": 0,
            "changed_supplement_entries": 0,
            "supplement_fills": 79,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": 0,
              "2022": 0,
              "2023": 0,
              "2024": 0,
              "2025": 0
            },
            "positive_years": 0,
            "best_incremental_month": 7.275957614183426e-12,
            "delta_without_best_month": -7.275957614183426e-12,
            "gates": {
              "nominal": false,
              "calendar": true,
              "plus10": true,
              "dd": true,
              "modified_entries": false,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": 0.0007936507936507908,
        "delta10": 0,
        "worstDD": -9.057883731399553
      },
      {
        "id": "V804",
        "strategy": "BtcContextR804",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 13123.604695779431,
            "delta": 66.98978070176781,
            "delta_seed": 66.98978070176781,
            "plus10": 11021.043414931815,
            "delta10": 89.83367138595167,
            "dd": -9.583827851927795,
            "counts": {
              "Mfull": "40/61",
              "Mall": "40/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.015079365079365137,
            "modified_exits": 0,
            "changed_supplement_entries": 15,
            "supplement_fills": 66,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": -72.90188103549553,
              "2022": 87.32831076860566,
              "2023": 405.01430376222197,
              "2024": -101.919315371626,
              "2025": -250.5316374219401
            },
            "positive_years": 2,
            "best_incremental_month": 159.5820684544633,
            "delta_without_best_month": -92.59228775269548,
            "gates": {
              "nominal": true,
              "calendar": false,
              "plus10": true,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 13307.8134999793,
            "delta": 68.37112013250771,
            "delta_seed": 68.37112013250771,
            "plus10": 11091.963637903975,
            "delta10": 88.54817352358805,
            "dd": -9.606876085197747,
            "counts": {
              "Mfull": "39/61",
              "Mall": "39/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.030952380952380953,
            "modified_exits": 0,
            "changed_supplement_entries": 15,
            "supplement_fills": 66,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": -63.82971253784126,
              "2022": 83.56625363574494,
              "2023": 417.2901000535858,
              "2024": -115.22743977399296,
              "2025": -253.42808124499425
            },
            "positive_years": 2,
            "best_incremental_month": 155.548978857978,
            "delta_without_best_month": -87.17785872547029,
            "gates": {
              "nominal": true,
              "calendar": false,
              "plus10": true,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.030952380952380953,
        "delta10": 88.54817352358805,
        "worstDD": -9.606876085197747
      },
      {
        "id": "V805",
        "strategy": "BtcContextR805",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 13056.614915077664,
            "delta": 0,
            "delta_seed": 0,
            "plus10": 10931.209743545864,
            "delta10": 0,
            "dd": -8.77680090479469,
            "counts": {
              "Mfull": "41/61",
              "Mall": "41/63",
              "Qfull": "16/19",
              "Qall": "17/21"
            },
            "margin": 0.0007936507936507908,
            "modified_exits": 0,
            "changed_supplement_entries": 0,
            "supplement_fills": 79,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": 0,
              "2022": 0,
              "2023": 0,
              "2024": 0,
              "2025": 0
            },
            "positive_years": 0,
            "best_incremental_month": 1.0913936421275139e-11,
            "delta_without_best_month": -1.0913936421275139e-11,
            "gates": {
              "nominal": false,
              "calendar": true,
              "plus10": true,
              "dd": true,
              "modified_entries": false,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 13239.442379846792,
            "delta": 0,
            "delta_seed": 0,
            "plus10": 11003.415464380387,
            "delta10": 0,
            "dd": -9.057883731399553,
            "counts": {
              "Mfull": "41/61",
              "Mall": "41/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.0007936507936507908,
            "modified_exits": 0,
            "changed_supplement_entries": 0,
            "supplement_fills": 79,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": 0,
              "2022": 0,
              "2023": 0,
              "2024": 0,
              "2025": 0
            },
            "positive_years": 0,
            "best_incremental_month": 7.275957614183426e-12,
            "delta_without_best_month": -7.275957614183426e-12,
            "gates": {
              "nominal": false,
              "calendar": true,
              "plus10": true,
              "dd": true,
              "modified_entries": false,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": 0.0007936507936507908,
        "delta10": 0,
        "worstDD": -9.057883731399553
      },
      {
        "id": "X801",
        "strategy": "BTCExploreR801",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 4947.1336769834115,
            "delta": -8109.481238094252,
            "delta_seed": -8109.481238094252,
            "plus10": 2629.9956233168796,
            "delta10": -8301.214120228984,
            "dd": -12.617243194253858,
            "counts": {
              "Mfull": "32/61",
              "Mall": "32/63",
              "Qfull": "10/19",
              "Qall": "11/21"
            },
            "margin": -0.2761904761904762,
            "modified_exits": 0,
            "changed_supplement_entries": 257,
            "supplement_fills": 210,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": 107.30453883225528,
              "2022": -2393.3940330703863,
              "2023": -1604.7041285971245,
              "2024": -1999.9376311885626,
              "2025": -2164.4321274097874
            },
            "positive_years": 1,
            "best_incremental_month": 599.9488565786796,
            "delta_without_best_month": -8709.43009467293,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 5129.7021715969595,
            "delta": -8109.740208249833,
            "delta_seed": -8109.740208249833,
            "plus10": 2720.1089131726026,
            "delta10": -8283.306551207785,
            "dd": -12.498769810868481,
            "counts": {
              "Mfull": "32/61",
              "Mall": "32/63",
              "Qfull": "10/19",
              "Qall": "11/21"
            },
            "margin": -0.2761904761904762,
            "modified_exits": 0,
            "changed_supplement_entries": 257,
            "supplement_fills": 210,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": 134.74044646788388,
              "2022": -2358.376061570374,
              "2023": -1705.9351253187742,
              "2024": -1997.290570683679,
              "2025": -2128.988542635996
            },
            "positive_years": 1,
            "best_incremental_month": 617.8373518071439,
            "delta_without_best_month": -8727.577560056976,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.2761904761904762,
        "delta10": -8301.214120228984,
        "worstDD": -12.617243194253858
      },
      {
        "id": "X802",
        "strategy": "BTCExploreR802",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 7971.101112515078,
            "delta": -5085.513802562586,
            "delta_seed": -5085.513802562586,
            "plus10": 5856.987373416839,
            "delta10": -5074.222370129025,
            "dd": -13.03677643602208,
            "counts": {
              "Mfull": "36/61",
              "Mall": "36/63",
              "Qfull": "12/19",
              "Qall": "13/21"
            },
            "margin": -0.18095238095238098,
            "modified_exits": 0,
            "changed_supplement_entries": 198,
            "supplement_fills": 127,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": -1124.9881788026487,
              "2022": 345.19527182099773,
              "2023": -1732.4050838168914,
              "2024": -1355.738477262972,
              "2025": -1236.9394250339792
            },
            "positive_years": 1,
            "best_incremental_month": 572.9192886340134,
            "delta_without_best_month": -5658.433091196599,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 8181.461352205392,
            "delta": -5057.9810276414,
            "delta_seed": -5057.9810276414,
            "plus10": 5969.540031398857,
            "delta10": -5033.87543298153,
            "dd": -13.780626346698666,
            "counts": {
              "Mfull": "37/61",
              "Mall": "37/63",
              "Qfull": "12/19",
              "Qall": "13/21"
            },
            "margin": -0.18095238095238098,
            "modified_exits": 0,
            "changed_supplement_entries": 198,
            "supplement_fills": 127,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": -1094.8988407647867,
              "2022": 341.05970120900383,
              "2023": -1766.9835390654061,
              "2024": -1357.0833082923891,
              "2025": -1198.8402487039348
            },
            "positive_years": 1,
            "best_incremental_month": 561.1023598713509,
            "delta_without_best_month": -5619.083387512751,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.18095238095238098,
        "delta10": -5074.222370129025,
        "worstDD": -13.780626346698666
      },
      {
        "id": "X803",
        "strategy": "BTCExploreR803",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 8013.226139398318,
            "delta": -5043.388775679346,
            "delta_seed": -5043.388775679346,
            "plus10": 5941.004124521748,
            "delta10": -4990.205619024116,
            "dd": -11.77260066965019,
            "counts": {
              "Mfull": "34/61",
              "Mall": "34/63",
              "Qfull": "15/19",
              "Qall": "17/21"
            },
            "margin": -0.11031746031746037,
            "modified_exits": 0,
            "changed_supplement_entries": 186,
            "supplement_fills": 133,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": -516.1256700094837,
              "2022": -1384.6879106631695,
              "2023": -1011.5975452828152,
              "2024": -465.31608262441296,
              "2025": -1632.7683900743905
            },
            "positive_years": 0,
            "best_incremental_month": 589.6638442508702,
            "delta_without_best_month": -5633.052619930216,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 8180.365367683822,
            "delta": -5059.07701216297,
            "delta_seed": -5059.07701216297,
            "plus10": 6014.519409760476,
            "delta10": -4988.8960546199105,
            "dd": -11.487975749130818,
            "counts": {
              "Mfull": "35/61",
              "Mall": "35/63",
              "Qfull": "13/19",
              "Qall": "15/21"
            },
            "margin": -0.11578947368421055,
            "modified_exits": 0,
            "changed_supplement_entries": 186,
            "supplement_fills": 133,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": -496.0110049846553,
              "2022": -1354.1562395706715,
              "2023": -1086.0741502203382,
              "2024": -476.19686230340994,
              "2025": -1613.745578058868
            },
            "positive_years": 0,
            "best_incremental_month": 600.6154241227123,
            "delta_without_best_month": -5659.692436285683,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.11578947368421055,
        "delta10": -4990.205619024116,
        "worstDD": -11.77260066965019
      },
      {
        "id": "X804",
        "strategy": "BTCExploreR804",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 5040.5029169225645,
            "delta": -8016.111998155099,
            "delta_seed": -8016.111998155099,
            "plus10": 2833.2784758542966,
            "delta10": -8097.931267691567,
            "dd": -14.829776373431812,
            "counts": {
              "Mfull": "30/60",
              "Mall": "30/62",
              "Qfull": "11/19",
              "Qall": "12/21"
            },
            "margin": -0.22857142857142865,
            "modified_exits": 0,
            "changed_supplement_entries": 237,
            "supplement_fills": 178,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": 380.71340600720396,
              "2022": -1706.2919071059205,
              "2023": -2325.1648687762026,
              "2024": -1952.5653444849086,
              "2025": -2264.613356215197
            },
            "positive_years": 1,
            "best_incremental_month": 590.4984883442103,
            "delta_without_best_month": -8606.61048649931,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 5213.663656207337,
            "delta": -8025.778723639455,
            "delta_seed": -8025.778723639455,
            "plus10": 2914.099872852777,
            "delta10": -8089.315591527609,
            "dd": -11.74677605147243,
            "counts": {
              "Mfull": "31/60",
              "Mall": "31/62",
              "Qfull": "11/19",
              "Qall": "12/21"
            },
            "margin": -0.22857142857142865,
            "modified_exits": 0,
            "changed_supplement_entries": 237,
            "supplement_fills": 178,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": 395.55594285075495,
              "2022": -1674.1022228477723,
              "2023": -2400.8853018844566,
              "2024": -1957.9208878560894,
              "2025": -2240.0066683458354
            },
            "positive_years": 1,
            "best_incremental_month": 606.4052137733797,
            "delta_without_best_month": -8632.183937412836,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.22857142857142865,
        "delta10": -8097.931267691567,
        "worstDD": -14.829776373431812
      },
      {
        "id": "X805",
        "strategy": "BTCExploreR805",
        "seed": "N204",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 3846.1896810928224,
            "delta": -9210.42523398484,
            "delta_seed": -9210.42523398484,
            "plus10": 406.1427389635348,
            "delta10": -10525.067004582328,
            "dd": -16.051434546194887,
            "counts": {
              "Mfull": "31/61",
              "Mall": "31/63",
              "Qfull": "11/19",
              "Qall": "11/21"
            },
            "margin": -0.2761904761904762,
            "modified_exits": 0,
            "changed_supplement_entries": 450,
            "supplement_fills": 421,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": 726.8018600233736,
              "2022": -2455.1252329904164,
              "2023": -1570.2153838561917,
              "2024": -2008.6440532800643,
              "2025": -3340.743342462638
            },
            "positive_years": 1,
            "best_incremental_month": 608.1083859640075,
            "delta_without_best_month": -9818.533619948848,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 3967.0240499071715,
            "delta": -9272.41832993962,
            "delta_seed": -9272.41832993962,
            "plus10": 443.5553492177095,
            "delta10": -10559.860115162677,
            "dd": -15.796504143155188,
            "counts": {
              "Mfull": "32/61",
              "Mall": "32/63",
              "Qfull": "11/19",
              "Qall": "11/21"
            },
            "margin": -0.2761904761904762,
            "modified_exits": 0,
            "changed_supplement_entries": 450,
            "supplement_fills": 421,
            "diversity_measure": "changed entries versus N204",
            "annual_delta_MTM": {
              "2021": 724.2065167329656,
              "2022": -2413.3547744076004,
              "2023": -1668.7553315327023,
              "2024": -2028.774973999818,
              "2025": -3324.248613194439
            },
            "positive_years": 1,
            "best_incremental_month": 639.1027728591725,
            "delta_without_best_month": -9911.521102798793,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.2761904761904762,
        "delta10": -10559.860115162677,
        "worstDD": -16.051434546194887
      },
      {
        "id": "Y901",
        "strategy": "BTCNovelR901",
        "seed": "N503",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 11046.643830038212,
            "delta": -2009.9710850394513,
            "delta_seed": -2282.0678827777174,
            "plus10": 9248.682149616321,
            "delta10": -1682.5275939295425,
            "dd": -9.149153111577924,
            "counts": {
              "Mfull": "40/61",
              "Mall": "40/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.015079365079365137,
            "modified_exits": 0,
            "changed_supplement_entries": 100,
            "supplement_fills": 33,
            "diversity_measure": "changed execution versus N503",
            "annual_delta_MTM": {
              "2021": -332.9773985318134,
              "2022": -553.8922982524564,
              "2023": 85.89468150264474,
              "2024": -454.7123376701311,
              "2025": -753.2604923359831
            },
            "positive_years": 1,
            "best_incremental_month": 261.17951549829377,
            "delta_without_best_month": -2271.150600537745,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 11228.810189574659,
            "delta": -2010.6321902721338,
            "delta_seed": -2308.092323484747,
            "plus10": 9324.252479559813,
            "delta10": -1679.162984820574,
            "dd": -9.148244087455126,
            "counts": {
              "Mfull": "39/61",
              "Mall": "39/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.030952380952380953,
            "modified_exits": 0,
            "changed_supplement_entries": 100,
            "supplement_fills": 33,
            "diversity_measure": "changed execution versus N503",
            "annual_delta_MTM": {
              "2021": -318.9255769498195,
              "2022": -548.2233816660209,
              "2023": 57.93297151276238,
              "2024": -452.14585848098795,
              "2025": -748.2471049363776
            },
            "positive_years": 1,
            "best_incremental_month": 260.49738445799085,
            "delta_without_best_month": -2271.1295747301247,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.030952380952380953,
        "delta10": -1682.5275939295425,
        "worstDD": -9.149153111577924
      },
      {
        "id": "Y902",
        "strategy": "BTCNovelR902",
        "seed": "N503",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 13446.234525575226,
            "delta": 389.61961049756246,
            "delta_seed": 117.52281275929636,
            "plus10": 11477.310426090633,
            "delta10": 546.1006825447694,
            "dd": -9.694111596125987,
            "counts": {
              "Mfull": "41/60",
              "Mall": "41/62",
              "Qfull": "16/19",
              "Qall": "17/21"
            },
            "margin": 0.00952380952380949,
            "modified_exits": 0,
            "changed_supplement_entries": 111,
            "supplement_fills": 46,
            "diversity_measure": "changed execution versus N503",
            "annual_delta_MTM": {
              "2021": 21.225657331864568,
              "2022": 154.22912855232062,
              "2023": 287.4741597636712,
              "2024": -73.08507298060431,
              "2025": 32.75556154476362
            },
            "positive_years": 4,
            "best_incremental_month": 409.3801886544152,
            "delta_without_best_month": -19.760578156852716,
            "gates": {
              "nominal": true,
              "calendar": true,
              "plus10": true,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": true,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 13680.349170886384,
            "delta": 440.90679103959155,
            "delta_seed": 143.44665782697848,
            "plus10": 11594.99862797829,
            "delta10": 591.583163597903,
            "dd": -9.630062412368668,
            "counts": {
              "Mfull": "42/60",
              "Mall": "42/62",
              "Qfull": "16/19",
              "Qall": "17/21"
            },
            "margin": 0.00952380952380949,
            "modified_exits": 0,
            "changed_supplement_entries": 111,
            "supplement_fills": 46,
            "diversity_measure": "changed execution versus N503",
            "annual_delta_MTM": {
              "2021": 25.937163572742065,
              "2022": 148.9034131719418,
              "2023": 315.30783956492087,
              "2024": -68.13295410644787,
              "2025": 51.871792893925885
            },
            "positive_years": 4,
            "best_incremental_month": 400.58164502733234,
            "delta_without_best_month": 40.32514601225921,
            "gates": {
              "nominal": true,
              "calendar": true,
              "plus10": true,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": true,
              "without_best_month": true
            },
            "eligible": true
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": 0.00952380952380949,
        "delta10": 546.1006825447694,
        "worstDD": -9.694111596125987
      },
      {
        "id": "Y903",
        "strategy": "BTCNovelR903",
        "seed": "N503",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 10679.17256382918,
            "delta": -2377.4423512484846,
            "delta_seed": -2649.5391489867507,
            "plus10": 8711.308825975375,
            "delta10": -2219.9009175704887,
            "dd": -8.185595399711133,
            "counts": {
              "Mfull": "38/61",
              "Mall": "38/63",
              "Qfull": "13/19",
              "Qall": "14/21"
            },
            "margin": -0.13333333333333341,
            "modified_exits": 29,
            "changed_supplement_entries": 3,
            "supplement_fills": 70,
            "diversity_measure": "modified exits versus N503",
            "annual_delta_MTM": {
              "2021": -204.12214282209789,
              "2022": -746.4514328989098,
              "2023": -843.061168347218,
              "2024": 74.83812428872261,
              "2025": -689.3253272405855
            },
            "positive_years": 1,
            "best_incremental_month": 262.9596728770812,
            "delta_without_best_month": -2640.4020241255657,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 10898.840239454648,
            "delta": -2340.602140392144,
            "delta_seed": -2638.062273604757,
            "plus10": 8823.544272012321,
            "delta10": -2179.8711923680657,
            "dd": -8.983352943299616,
            "counts": {
              "Mfull": "38/61",
              "Mall": "38/63",
              "Qfull": "15/19",
              "Qall": "16/21"
            },
            "margin": -0.04682539682539688,
            "modified_exits": 29,
            "changed_supplement_entries": 3,
            "supplement_fills": 70,
            "diversity_measure": "modified exits versus N503",
            "annual_delta_MTM": {
              "2021": -181.6269323501183,
              "2022": -733.3932224477485,
              "2023": -869.459195670217,
              "2024": 89.81914262310784,
              "2025": -676.621528318763
            },
            "positive_years": 1,
            "best_incremental_month": 267.2811530112813,
            "delta_without_best_month": -2607.8832934034253,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true,
              "modified_entries": true,
              "supplement_fills": true,
              "metadata_identified": true,
              "year_distribution": false,
              "without_best_month": false
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.13333333333333341,
        "delta10": -2219.9009175704887,
        "worstDD": -8.983352943299616
      }
    ],
    "eligible": [],
    "selected": null
  }
}
```
