# N204 / T403 R5 — registro final de veinte backtests

Dos agentes nuevos, diez hipótesis independientes(cinco por semilla),B/Cporcadauna=20runsnominales. Todosfinished/errornull en resúmenes previos al auditor. No reruns económicos, no nuevas variantes después de resultados. Ninguna elegible; cero de las seis verificaciones condicionales. Dos fallos/correccionespreviasdeQA:fixtureN503malcalculado(nocambiofuente/umbral), yguardadjacencyC501antesdeprimerfull(no nuevaidea). Sin2026, sininspecciónnueva de datos.

ReferenciasreutilizadasyresumidasantesR5:[N204B](http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142), [N204C](http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794), [T403B](http://localhost:9200/#/backtest/9014f7d9-fa7e-4af7-94b7-dc98940f21b8), [T403C](http://localhost:9200/#/backtest/bd5f78dd-b730-48ad-ab01-e4c3f4726d29).

|Sesión|Semilla|ClaseBTC|Cartera|Fee/lado|Estado|
|---|---|---|---|---:|---|
|[N501B](http://localhost:9200/#/backtest/16ce69b3-da09-4bc4-9eb4-be31b7e5d39d)|N204|N204ExploreR501|B|0.00045|finished|
|[N501C](http://localhost:9200/#/backtest/febab2e7-f15f-4260-b9c0-8d92c669ac10)|N204|N204ExploreR501|C|0.00045|finished|
|[C501B](http://localhost:9200/#/backtest/e798f4aa-2793-4900-95b7-94b0b44d3fb0)|T403|T403ExploreR501|B|0.00045|finished|
|[C501C](http://localhost:9200/#/backtest/b8b318ea-c2ca-4269-b602-e1e3f97ab06c)|T403|T403ExploreR501|C|0.00045|finished|
|[N502B](http://localhost:9200/#/backtest/8e4fd64f-49c6-4049-b6da-abafede9cb8e)|N204|N204ExploreR502|B|0.00045|finished|
|[N502C](http://localhost:9200/#/backtest/d492f34b-8a1e-4099-8ec3-eae1b3b5d284)|N204|N204ExploreR502|C|0.00045|finished|
|[C502B](http://localhost:9200/#/backtest/4ac5e198-139d-4f17-8c8f-de1c8aa6a67f)|T403|T403ExploreR502|B|0.00045|finished|
|[C502C](http://localhost:9200/#/backtest/7e4411c6-6d8c-4bb8-9092-343f8089cc3d)|T403|T403ExploreR502|C|0.00045|finished|
|[C503C](http://localhost:9200/#/backtest/cf4808de-d32d-46ec-98cf-2e453b486b85)|T403|T403ExploreR503|C|0.00045|finished|
|[C503B](http://localhost:9200/#/backtest/57634d6a-96a9-480f-b4f4-2e5546c8693e)|T403|T403ExploreR503|B|0.00045|finished|
|[N503C](http://localhost:9200/#/backtest/fd459b54-ea49-44ce-8dd1-290e2c2c4a65)|N204|N204ExploreR503|C|0.00045|finished|
|[N503B](http://localhost:9200/#/backtest/a0db99e9-2638-4a58-a407-11fa8442f752)|N204|N204ExploreR503|B|0.00045|finished|
|[N504B](http://localhost:9200/#/backtest/e3201a9a-3ac0-47f5-94f5-6f16feeee8ab)|N204|N204ExploreR504|B|0.00045|finished|
|[N504C](http://localhost:9200/#/backtest/72d9e745-e4e1-4e09-99eb-e550f2560206)|N204|N204ExploreR504|C|0.00045|finished|
|[C504C](http://localhost:9200/#/backtest/6c7b3c72-9096-4004-bac4-ef61c251c082)|T403|T403ExploreR504|C|0.00045|finished|
|[C504B](http://localhost:9200/#/backtest/2ce5ecba-4ae6-4fd1-9917-4bf8117b09c8)|T403|T403ExploreR504|B|0.00045|finished|
|[N505B](http://localhost:9200/#/backtest/6a2cc667-11cf-4467-b1a4-0c8e84f2b792)|N204|N204ExploreR505|B|0.00045|finished|
|[C505B](http://localhost:9200/#/backtest/8b0b2376-126b-4918-806e-d63aa0fec3f1)|T403|T403ExploreR505|B|0.00045|finished|
|[N505C](http://localhost:9200/#/backtest/8e693681-095b-4db9-affb-053f19085948)|N204|N204ExploreR505|C|0.00045|finished|
|[C505C](http://localhost:9200/#/backtest/ddac5c97-6655-417d-855a-fac467e06c6d)|T403|T403ExploreR505|C|0.00045|finished|

Contrato:10000USDTshared,1%trade/8%agregado,isolated5x,cap4.4,reserva.001sizing,nopyramid;2020-10-15→2025-12-31exclusiva,fee.00045;3rutasBTC/PAXG/SPY4h+3feeds1m,warmup240debugtruefastfalsecharttrue. PAXGoriginalfeeBE,SPYSecondB/MarketC. Las20formas y60sourcesnapshots fueroncomparadosliteralmente.

## Formas/snapshots
```json
{
  "16ce69b3-da09-4bc4-9eb4-be31b7e5d39d": {
    "name": "N501B",
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
  "febab2e7-f15f-4260-b9c0-8d92c669ac10": {
    "name": "N501C",
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
  "e798f4aa-2793-4900-95b7-94b0b44d3fb0": {
    "name": "C501B",
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
  "b8b318ea-c2ca-4269-b602-e1e3f97ab06c": {
    "name": "C501C",
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
  "8e4fd64f-49c6-4049-b6da-abafede9cb8e": {
    "name": "N502B",
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
  "d492f34b-8a1e-4099-8ec3-eae1b3b5d284": {
    "name": "N502C",
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
  "4ac5e198-139d-4f17-8c8f-de1c8aa6a67f": {
    "name": "C502B",
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
  "7e4411c6-6d8c-4bb8-9092-343f8089cc3d": {
    "name": "C502C",
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
  "cf4808de-d32d-46ec-98cf-2e453b486b85": {
    "name": "C503C",
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
  "57634d6a-96a9-480f-b4f4-2e5546c8693e": {
    "name": "C503B",
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
  "fd459b54-ea49-44ce-8dd1-290e2c2c4a65": {
    "name": "N503C",
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
  "a0db99e9-2638-4a58-a407-11fa8442f752": {
    "name": "N503B",
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
  "e3201a9a-3ac0-47f5-94f5-6f16feeee8ab": {
    "name": "N504B",
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
  "72d9e745-e4e1-4e09-99eb-e550f2560206": {
    "name": "N504C",
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
  "6c7b3c72-9096-4004-bac4-ef61c251c082": {
    "name": "C504C",
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
  "2ce5ecba-4ae6-4fd1-9917-4bf8117b09c8": {
    "name": "C504B",
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
  "6a2cc667-11cf-4467-b1a4-0c8e84f2b792": {
    "name": "N505B",
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
  "8b0b2376-126b-4918-806e-d63aa0fec3f1": {
    "name": "C505B",
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
  "8e693681-095b-4db9-affb-053f19085948": {
    "name": "N505C",
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
  "ddac5c97-6655-417d-855a-fac467e06c6d": {
    "name": "C505C",
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
}
```

## Fuentes finales
```json
{
  "BtcExploreR103": true,
  "PortComparePaxgMarket4h": true,
  "PortCompareSpySecond4h": true,
  "PortCompareSpyMarket4h": true,
  "PortCompareBtc4h": true,
  "X03ExploreR204": true,
  "N204ExitR403": true,
  "N204ExploreR501": true,
  "N204ExploreR502": true,
  "N204ExploreR503": true,
  "N204ExploreR504": true,
  "N204ExploreR505": true,
  "T403ExploreR501": true,
  "T403ExploreR502": true,
  "T403ExploreR503": true,
  "T403ExploreR504": true,
  "T403ExploreR505": true
}
```

## Jobs de auditoría
```json
[
  {
    "batch": "N501",
    "names": [
      "N501B",
      "N501C"
    ],
    "job": "6552d72e0ce54d128ffdffbd83524f8c",
    "status": "succeeded"
  },
  {
    "batch": "C501",
    "names": [
      "C501B",
      "C501C"
    ],
    "job": "2399b0c0377b4533b0ad19c2438f4bd4",
    "status": "succeeded"
  },
  {
    "batch": "N502",
    "names": [
      "N502B",
      "N502C"
    ],
    "job": "c25237cc23bc49c497699fa303f8d395",
    "status": "succeeded"
  },
  {
    "batch": "C502",
    "names": [
      "C502B",
      "C502C"
    ],
    "job": "2a302b4560074d28b9ab2e0daa858be8",
    "status": "succeeded"
  },
  {
    "batch": "N503",
    "names": [
      "N503B",
      "N503C"
    ],
    "job": "ec1e92de790a4676a5b83f497a001617",
    "status": "succeeded"
  },
  {
    "batch": "C503",
    "names": [
      "C503B",
      "C503C"
    ],
    "job": "78dbc1fd87b343608a63110ace97ea73",
    "status": "succeeded"
  },
  {
    "batch": "N504",
    "names": [
      "N504B",
      "N504C"
    ],
    "job": "ce94b6e82d6247879dea404ee3b31f3d",
    "status": "succeeded"
  },
  {
    "batch": "C504",
    "names": [
      "C504B",
      "C504C"
    ],
    "job": "24d3cfe4b0044cd79317c7088820de2f",
    "status": "succeeded"
  },
  {
    "batch": "N505",
    "names": [
      "N505B",
      "N505C"
    ],
    "job": "f993d0c1fd3348198070abd95950945a",
    "status": "succeeded"
  },
  {
    "batch": "C505",
    "names": [
      "C505B",
      "C505C"
    ],
    "job": "696dc5f70813437c95523f17c4e0e8cd",
    "status": "succeeded"
  }
]
```

## QA de implementación
```json
[
  {
    "family": "N204",
    "job": "ef8d61b738d94a649d2153894df719dd",
    "checks": 250,
    "status": "succeeded",
    "earlier_fixture_failure": "c967c73184a741748e3eb0ce5af50200"
  },
  {
    "family": "T403_initial",
    "job": "03b64f9b832a4519ab5025c9019ce7ef",
    "checks": 298,
    "status": "succeeded",
    "clarification_C501_consecutive_callback_pending": false,
    "supersededBy": "00393cba330f4237b9549a5c9d1c5543"
  },
  {
    "family": "T403_final",
    "job": "00393cba330f4237b9549a5c9d1c5543",
    "checks": 304,
    "status": "succeeded",
    "clarification": "C501 resets recovery count if adjacent processed4hclock missing; preserves frozen consecutive rule."
  }
]
```
