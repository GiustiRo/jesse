# R6 — registro y manifiesto final

20 backtests nominales finalizados; 10 análisis financieros succeeded; 17 fuentes idénticas al contrato congelado; 20 formularios y 60 snapshots verificados. Los códigos E y P son las familias exploratoria y de convivencia; B y C son carteras con distinta ejecución de SPY. 2026 cerrado. Las dos verificaciones con mayor fee real y cuatro sensibilidades eran condicionales: cero ejecutadas por ausencia de elegible.

## URLs de los veinte backtests

- [P601C](http://localhost:9200/#/backtest/4c23dbbc-ea56-4709-9835-e2e2b332214f) — N503CapacityR601; finished
- [P601B](http://localhost:9200/#/backtest/7fc34b8d-bbc4-48c0-9dd9-ef1751ed3bf5) — N503CapacityR601; finished
- [E601B](http://localhost:9200/#/backtest/9a11306e-c60c-4453-800a-34cac602dbdc) — N503ExploreR601; finished
- [E601C](http://localhost:9200/#/backtest/b12c2e5d-2a3b-4036-be2a-3de93ee3b359) — N503ExploreR601; finished
- [E602B](http://localhost:9200/#/backtest/19a83d39-c77e-41a4-a0b7-0edabd14b136) — N503ExploreR602; finished
- [E602C](http://localhost:9200/#/backtest/4da71fcf-5806-4aaa-9f52-5c7a62761040) — N503ExploreR602; finished
- [P602C](http://localhost:9200/#/backtest/7df75aa0-a2c1-456e-b196-d96a9d00c3c7) — N503CapacityR602; finished
- [P602B](http://localhost:9200/#/backtest/35c8f77f-e7fa-4c12-b9cc-8a6141192096) — N503CapacityR602; finished
- [P603C](http://localhost:9200/#/backtest/60c0e24b-cd8e-42e0-be3c-b915104fab92) — N503CapacityR603; finished
- [P603B](http://localhost:9200/#/backtest/b667d009-bcec-425f-8120-ac7fd24ea523) — N503CapacityR603; finished
- [E603C](http://localhost:9200/#/backtest/aabc659d-e33f-472b-942a-e9b2adcc0abe) — N503ExploreR603; finished
- [E603B](http://localhost:9200/#/backtest/0fff0dca-c5c4-4745-a1f7-1926300d7867) — N503ExploreR603; finished
- [E604B](http://localhost:9200/#/backtest/3a0b72cf-183b-4920-a863-845b77a9443e) — N503ExploreR604; finished
- [E604C](http://localhost:9200/#/backtest/a20faa2e-315a-4319-8138-44a12b84d49b) — N503ExploreR604; finished
- [P604C](http://localhost:9200/#/backtest/e312a439-4afb-4be4-af3b-4d08325d47bb) — N503CapacityR604; finished
- [P604B](http://localhost:9200/#/backtest/bf8cf6df-8055-4e88-a52d-5cb3d12d8b52) — N503CapacityR604; finished
- [P605B](http://localhost:9200/#/backtest/49c13ad1-4802-4c9f-99f8-fffec43fdac9) — N503CapacityR605; finished
- [P605C](http://localhost:9200/#/backtest/12d3aae7-b298-4afc-aa6a-e46f6fc24a2f) — N503CapacityR605; finished
- [E605B](http://localhost:9200/#/backtest/fbae9638-daef-4a34-ba29-5fdfd1c796e6) — N503ExploreR605; finished
- [E605C](http://localhost:9200/#/backtest/adfde635-9272-4a1c-ad63-347d7a0cd826) — N503ExploreR605; finished

## Datos de cierre

```json
{
  "date": "2026-10-19",
  "scope": "R6 20 nominal fulls only; 2026 closed even to inspection",
  "references": [
    {
      "name": "N204B",
      "id": "bc5aaba6-2746-4e90-b0de-7b7955b66142",
      "url": "http://localhost:9200/#/backtest/bc5aaba6-2746-4e90-b0de-7b7955b66142",
      "strategy": "X03ExploreR204",
      "fee": 0.00045,
      "portfolio": "B"
    },
    {
      "name": "N204C",
      "id": "6dead093-4663-4da9-ac62-c2ad9f9bb794",
      "url": "http://localhost:9200/#/backtest/6dead093-4663-4da9-ac62-c2ad9f9bb794",
      "strategy": "X03ExploreR204",
      "fee": 0.00045,
      "portfolio": "C"
    },
    {
      "name": "N503B",
      "id": "a0db99e9-2638-4a58-a407-11fa8442f752",
      "url": "http://localhost:9200/#/backtest/a0db99e9-2638-4a58-a407-11fa8442f752",
      "strategy": "N204ExploreR503",
      "fee": 0.00045,
      "portfolio": "B"
    },
    {
      "name": "N503C",
      "id": "fd459b54-ea49-44ce-8dd1-290e2c2c4a65",
      "url": "http://localhost:9200/#/backtest/fd459b54-ea49-44ce-8dd1-290e2c2c4a65",
      "strategy": "N204ExploreR503",
      "fee": 0.00045,
      "portfolio": "C"
    }
  ],
  "registry": [
    {
      "name": "P601C",
      "id": "4c23dbbc-ea56-4709-9835-e2e2b332214f",
      "url": "http://localhost:9200/#/backtest/4c23dbbc-ea56-4709-9835-e2e2b332214f",
      "strategy": "N503CapacityR601",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "P601B",
      "id": "7fc34b8d-bbc4-48c0-9dd9-ef1751ed3bf5",
      "url": "http://localhost:9200/#/backtest/7fc34b8d-bbc4-48c0-9dd9-ef1751ed3bf5",
      "strategy": "N503CapacityR601",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "E601B",
      "id": "9a11306e-c60c-4453-800a-34cac602dbdc",
      "url": "http://localhost:9200/#/backtest/9a11306e-c60c-4453-800a-34cac602dbdc",
      "strategy": "N503ExploreR601",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "E601C",
      "id": "b12c2e5d-2a3b-4036-be2a-3de93ee3b359",
      "url": "http://localhost:9200/#/backtest/b12c2e5d-2a3b-4036-be2a-3de93ee3b359",
      "strategy": "N503ExploreR601",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "E602B",
      "id": "19a83d39-c77e-41a4-a0b7-0edabd14b136",
      "url": "http://localhost:9200/#/backtest/19a83d39-c77e-41a4-a0b7-0edabd14b136",
      "strategy": "N503ExploreR602",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "E602C",
      "id": "4da71fcf-5806-4aaa-9f52-5c7a62761040",
      "url": "http://localhost:9200/#/backtest/4da71fcf-5806-4aaa-9f52-5c7a62761040",
      "strategy": "N503ExploreR602",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "P602C",
      "id": "7df75aa0-a2c1-456e-b196-d96a9d00c3c7",
      "url": "http://localhost:9200/#/backtest/7df75aa0-a2c1-456e-b196-d96a9d00c3c7",
      "strategy": "N503CapacityR602",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "P602B",
      "id": "35c8f77f-e7fa-4c12-b9cc-8a6141192096",
      "url": "http://localhost:9200/#/backtest/35c8f77f-e7fa-4c12-b9cc-8a6141192096",
      "strategy": "N503CapacityR602",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "P603C",
      "id": "60c0e24b-cd8e-42e0-be3c-b915104fab92",
      "url": "http://localhost:9200/#/backtest/60c0e24b-cd8e-42e0-be3c-b915104fab92",
      "strategy": "N503CapacityR603",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "P603B",
      "id": "b667d009-bcec-425f-8120-ac7fd24ea523",
      "url": "http://localhost:9200/#/backtest/b667d009-bcec-425f-8120-ac7fd24ea523",
      "strategy": "N503CapacityR603",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "E603C",
      "id": "aabc659d-e33f-472b-942a-e9b2adcc0abe",
      "url": "http://localhost:9200/#/backtest/aabc659d-e33f-472b-942a-e9b2adcc0abe",
      "strategy": "N503ExploreR603",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "E603B",
      "id": "0fff0dca-c5c4-4745-a1f7-1926300d7867",
      "url": "http://localhost:9200/#/backtest/0fff0dca-c5c4-4745-a1f7-1926300d7867",
      "strategy": "N503ExploreR603",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "E604B",
      "id": "3a0b72cf-183b-4920-a863-845b77a9443e",
      "url": "http://localhost:9200/#/backtest/3a0b72cf-183b-4920-a863-845b77a9443e",
      "strategy": "N503ExploreR604",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "E604C",
      "id": "a20faa2e-315a-4319-8138-44a12b84d49b",
      "url": "http://localhost:9200/#/backtest/a20faa2e-315a-4319-8138-44a12b84d49b",
      "strategy": "N503ExploreR604",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "P604C",
      "id": "e312a439-4afb-4be4-af3b-4d08325d47bb",
      "url": "http://localhost:9200/#/backtest/e312a439-4afb-4be4-af3b-4d08325d47bb",
      "strategy": "N503CapacityR604",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "P604B",
      "id": "bf8cf6df-8055-4e88-a52d-5cb3d12d8b52",
      "url": "http://localhost:9200/#/backtest/bf8cf6df-8055-4e88-a52d-5cb3d12d8b52",
      "strategy": "N503CapacityR604",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "P605B",
      "id": "49c13ad1-4802-4c9f-99f8-fffec43fdac9",
      "url": "http://localhost:9200/#/backtest/49c13ad1-4802-4c9f-99f8-fffec43fdac9",
      "strategy": "N503CapacityR605",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "P605C",
      "id": "12d3aae7-b298-4afc-aa6a-e46f6fc24a2f",
      "url": "http://localhost:9200/#/backtest/12d3aae7-b298-4afc-aa6a-e46f6fc24a2f",
      "strategy": "N503CapacityR605",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "E605B",
      "id": "fbae9638-daef-4a34-ba29-5fdfd1c796e6",
      "url": "http://localhost:9200/#/backtest/fbae9638-daef-4a34-ba29-5fdfd1c796e6",
      "strategy": "N503ExploreR605",
      "seed": "N503",
      "portfolio": "B",
      "fee": 0.00045,
      "status": "finished"
    },
    {
      "name": "E605C",
      "id": "adfde635-9272-4a1c-ad63-347d7a0cd826",
      "url": "http://localhost:9200/#/backtest/adfde635-9272-4a1c-ad63-347d7a0cd826",
      "strategy": "N503ExploreR605",
      "seed": "N503",
      "portfolio": "C",
      "fee": 0.00045,
      "status": "finished"
    }
  ],
  "forms_and_three_source_snapshots": {
    "4c23dbbc-ea56-4709-9835-e2e2b332214f": {
      "name": "P601C",
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
    "7fc34b8d-bbc4-48c0-9dd9-ef1751ed3bf5": {
      "name": "P601B",
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
    "9a11306e-c60c-4453-800a-34cac602dbdc": {
      "name": "E601B",
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
    "b12c2e5d-2a3b-4036-be2a-3de93ee3b359": {
      "name": "E601C",
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
    "19a83d39-c77e-41a4-a0b7-0edabd14b136": {
      "name": "E602B",
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
    "4da71fcf-5806-4aaa-9f52-5c7a62761040": {
      "name": "E602C",
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
    "7df75aa0-a2c1-456e-b196-d96a9d00c3c7": {
      "name": "P602C",
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
    "35c8f77f-e7fa-4c12-b9cc-8a6141192096": {
      "name": "P602B",
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
    "60c0e24b-cd8e-42e0-be3c-b915104fab92": {
      "name": "P603C",
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
    "b667d009-bcec-425f-8120-ac7fd24ea523": {
      "name": "P603B",
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
    "aabc659d-e33f-472b-942a-e9b2adcc0abe": {
      "name": "E603C",
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
    "0fff0dca-c5c4-4745-a1f7-1926300d7867": {
      "name": "E603B",
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
    "3a0b72cf-183b-4920-a863-845b77a9443e": {
      "name": "E604B",
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
    "a20faa2e-315a-4319-8138-44a12b84d49b": {
      "name": "E604C",
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
    "e312a439-4afb-4be4-af3b-4d08325d47bb": {
      "name": "P604C",
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
    "bf8cf6df-8055-4e88-a52d-5cb3d12d8b52": {
      "name": "P604B",
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
    "49c13ad1-4802-4c9f-99f8-fffec43fdac9": {
      "name": "P605B",
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
    "12d3aae7-b298-4afc-aa6a-e46f6fc24a2f": {
      "name": "P605C",
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
    "fbae9638-daef-4a34-ba29-5fdfd1c796e6": {
      "name": "E605B",
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
    "adfde635-9272-4a1c-ad63-347d7a0cd826": {
      "name": "E605C",
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
  "source_exact_readbacks": [
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
    }
  ],
  "financial_jobs": [
    {
      "batch": "E601",
      "names": [
        "E601B",
        "E601C"
      ],
      "job": "043f1658998d45a3a55232020b305e19",
      "status": "succeeded"
    },
    {
      "batch": "P601",
      "names": [
        "P601B",
        "P601C"
      ],
      "job": "a3df792f3eb84d68ba643955c6e2df26",
      "status": "succeeded"
    },
    {
      "batch": "E602",
      "names": [
        "E602B",
        "E602C"
      ],
      "job": "ed8bdf67e98347f6b4f91bc7c4b34dc0",
      "status": "succeeded"
    },
    {
      "batch": "P602",
      "names": [
        "P602B",
        "P602C"
      ],
      "job": "3eccf568c84b4953a40f1397ad7c1b24",
      "status": "succeeded"
    },
    {
      "batch": "E603",
      "names": [
        "E603B",
        "E603C"
      ],
      "job": "19c898c9dacd45b591c6726bb0158c92",
      "status": "succeeded"
    },
    {
      "batch": "P603",
      "names": [
        "P603B",
        "P603C"
      ],
      "job": "e61f4c62412f48089d9c2cf6dc46d680",
      "status": "succeeded"
    },
    {
      "batch": "E604",
      "names": [
        "E604B",
        "E604C"
      ],
      "job": "92b710debf414ebba3068556a158ef8b",
      "status": "succeeded"
    },
    {
      "batch": "P604",
      "names": [
        "P604B",
        "P604C"
      ],
      "job": "86356e04cb8a4454b61f6f7b5ae06e2d",
      "status": "succeeded"
    },
    {
      "batch": "E605",
      "names": [
        "E605B",
        "E605C"
      ],
      "job": "5fa7716fc2a54f7c8094dd0dcfb0f997",
      "status": "succeeded"
    },
    {
      "batch": "P605",
      "names": [
        "P605B",
        "P605C"
      ],
      "job": "379e41e3c31b45c9827380707221953c",
      "status": "succeeded"
    }
  ],
  "source_QA_jobs": [
    {
      "family": "E_initial",
      "job": "5d43e8e4530140119ca8d5f7a975dcba",
      "checks": 194,
      "status": "succeeded"
    },
    {
      "family": "E_final",
      "job": "c93ea284cfff4f98883ebb99b7943f0f",
      "checks": 196,
      "status": "succeeded",
      "clarification": "E605missingfeedshape/emptyfalse,beforeE605full"
    },
    {
      "family": "P",
      "job": "b03123cc60cc412dac8a64815b322681",
      "checks": 311,
      "status": "succeeded"
    }
  ],
  "financial_reconciliation": [
    {
      "name": "P601C",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "P601B",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "E601B",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "E601C",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "E602B",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "E602C",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "P602C",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "P602B",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "P603C",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "P603B",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "E603C",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "E603B",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "E604B",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "E604C",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "P604C",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "P604B",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "P605B",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "P605C",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "E605B",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 0,
        "boundary_liquidations_reconciled": 0,
        "boundary_close_is_execution_liquidity_proof": false
      }
    },
    {
      "name": "E605C",
      "audit": "passed",
      "terminal_reconciles": true,
      "terminal_diagnostics": {
        "pretermination_open_counter": 1,
        "boundary_liquidations_reconciled": 1,
        "boundary_close_is_execution_liquidity_proof": false
      }
    }
  ],
  "trade_paths": {
    "E601B": {
      "counts": {
        "current": 250,
        "reference": 273,
        "retained": 243,
        "removed": 30,
        "added": 7
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 243,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 243,
        "max_abs_economic_field_delta": 38.92316754314106,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 247,
        "max_abs_economic_field_delta": 58.98666424466455,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "E601C": {
      "counts": {
        "current": 257,
        "reference": 280,
        "retained": 250,
        "removed": 30,
        "added": 7
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 250,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 250,
        "max_abs_economic_field_delta": 35.67957024787961,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 254,
        "max_abs_economic_field_delta": 58.98666424466455,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "P601B": {
      "counts": {
        "current": 264,
        "reference": 273,
        "retained": 259,
        "removed": 14,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 259,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 259,
        "max_abs_economic_field_delta": 25.837271944348686,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 263,
        "max_abs_economic_field_delta": 19.66222141488811,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "P601C": {
      "counts": {
        "current": 271,
        "reference": 280,
        "retained": 266,
        "removed": 14,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 266,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 266,
        "max_abs_economic_field_delta": 26.967331552252745,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 270,
        "max_abs_economic_field_delta": 19.66222141488811,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "E602B": {
      "counts": {
        "current": 226,
        "reference": 273,
        "retained": 216,
        "removed": 57,
        "added": 10
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 216,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 216,
        "max_abs_economic_field_delta": 90.82072426732952,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 219,
        "max_abs_economic_field_delta": 90.82072426732952,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "E602C": {
      "counts": {
        "current": 233,
        "reference": 280,
        "retained": 223,
        "removed": 57,
        "added": 10
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 223,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 223,
        "max_abs_economic_field_delta": 87.57712697206784,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 226,
        "max_abs_economic_field_delta": 90.82072426732975,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "P602B": {
      "counts": {
        "current": 264,
        "reference": 273,
        "retained": 260,
        "removed": 13,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 260,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 39.324442829776444,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": true,
        "matched": 264,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "P602C": {
      "counts": {
        "current": 271,
        "reference": 280,
        "retained": 267,
        "removed": 13,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 267,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 39.32444282977622,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": true,
        "matched": 271,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "E603B": {
      "counts": {
        "current": 258,
        "reference": 273,
        "retained": 254,
        "removed": 19,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 254,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 254,
        "max_abs_economic_field_delta": 103.79511344837647,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 257,
        "max_abs_economic_field_delta": 103.79511344837647,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "E603C": {
      "counts": {
        "current": 265,
        "reference": 280,
        "retained": 261,
        "removed": 19,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 261,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 261,
        "max_abs_economic_field_delta": 100.55151615311502,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 103.79511344837692,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "P603B": {
      "counts": {
        "current": 273,
        "reference": 273,
        "retained": 258,
        "removed": 15,
        "added": 15
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 245,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 258,
        "max_abs_economic_field_delta": 4576.865430518708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 262,
        "max_abs_economic_field_delta": 4576.865430518708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "P603C": {
      "counts": {
        "current": 280,
        "reference": 280,
        "retained": 265,
        "removed": 15,
        "added": 15
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 252,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 265,
        "max_abs_economic_field_delta": 4576.865430518708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 269,
        "max_abs_economic_field_delta": 4576.865430518708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "E604B": {
      "counts": {
        "current": 207,
        "reference": 273,
        "retained": 193,
        "removed": 80,
        "added": 14
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 193,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 193,
        "max_abs_economic_field_delta": 217.3210187825382,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 196,
        "max_abs_economic_field_delta": 217.3210187825382,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "E604C": {
      "counts": {
        "current": 214,
        "reference": 280,
        "retained": 200,
        "removed": 80,
        "added": 14
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 200,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 200,
        "max_abs_economic_field_delta": 210.83382419201484,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 203,
        "max_abs_economic_field_delta": 216.28443556376988,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "P604B": {
      "counts": {
        "current": 266,
        "reference": 273,
        "retained": 260,
        "removed": 13,
        "added": 6
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 256,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 264,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "P604C": {
      "counts": {
        "current": 273,
        "reference": 280,
        "retained": 267,
        "removed": 13,
        "added": 6
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 263,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 271,
        "max_abs_economic_field_delta": 948.75,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "E605B": {
      "counts": {
        "current": 229,
        "reference": 273,
        "retained": 223,
        "removed": 50,
        "added": 6
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 223,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 223,
        "max_abs_economic_field_delta": 129.7438918104708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 226,
        "max_abs_economic_field_delta": 129.7438918104708,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "E605C": {
      "counts": {
        "current": 236,
        "reference": 280,
        "retained": 230,
        "removed": 50,
        "added": 6
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 230,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 230,
        "max_abs_economic_field_delta": 120.01309992468555,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": false,
        "matched": 233,
        "max_abs_economic_field_delta": 123.25669721994745,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "P605B": {
      "counts": {
        "current": 264,
        "reference": 273,
        "retained": 260,
        "removed": 13,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 260,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 260,
        "max_abs_economic_field_delta": 39.324442829776444,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": true,
        "matched": 264,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    },
    "P605C": {
      "counts": {
        "current": 271,
        "reference": 280,
        "retained": 267,
        "removed": 13,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 267,
      "identity_vs_N204": {
        "economic_identity_within_1e_7": false,
        "matched": 267,
        "max_abs_economic_field_delta": 39.32444282977622,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      },
      "identity_vs_seed": {
        "economic_identity_within_1e_7": true,
        "matched": 271,
        "max_abs_economic_field_delta": 0,
        "note": "Exact entry/exit times and entry type; economic fields tolerance1e-7. Same paths are not new independent observations."
      }
    }
  },
  "selection": {
    "matrix": [
      {
        "id": "E601",
        "strategy": "N503ExploreR601",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 12139.275231409001,
            "delta": -917.3396836686625,
            "plus10": 10198.375214980148,
            "delta10": -732.834528565716,
            "dd": -8.773182737359509,
            "counts": {
              "Mfull": "39/60",
              "Mall": "39/62",
              "Qfull": "15/19",
              "Qall": "16/21"
            },
            "margin": -0.03809523809523818,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 12329.381307172616,
            "delta": -910.0610726741761,
            "plus10": 10276.913142711026,
            "delta10": -726.5023216693608,
            "dd": -9.054184091363382,
            "counts": {
              "Mfull": "39/60",
              "Mall": "39/62",
              "Qfull": "16/19",
              "Qall": "17/21"
            },
            "margin": -0.020967741935483897,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.03809523809523818,
        "delta10": -732.834528565716,
        "worstDD": -9.054184091363382
      },
      {
        "id": "E602",
        "strategy": "N503ExploreR602",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 12229.552825404462,
            "delta": -827.0620896732016,
            "plus10": 10443.208020034375,
            "delta10": -488.0017235114883,
            "dd": -7.4651132055334575,
            "counts": {
              "Mfull": "41/59",
              "Mall": "41/61",
              "Qfull": "15/19",
              "Qall": "16/21"
            },
            "margin": -0.03809523809523818,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 12426.752530477384,
            "delta": -812.689849369408,
            "plus10": 10530.080652587509,
            "delta10": -473.3348117928781,
            "dd": -8.168012803517167,
            "counts": {
              "Mfull": "42/59",
              "Mall": "42/61",
              "Qfull": "16/19",
              "Qall": "17/21"
            },
            "margin": 0.00952380952380949,
            "gates": {
              "nominal": false,
              "calendar": true,
              "plus10": false,
              "dd": true
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.03809523809523818,
        "delta10": -488.0017235114883,
        "worstDD": -8.168012803517167
      },
      {
        "id": "E603",
        "strategy": "N503ExploreR603",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 12378.550859335639,
            "delta": -678.0640557420247,
            "plus10": 10403.780450608509,
            "delta10": -527.4292929373551,
            "dd": -8.234413022132514,
            "counts": {
              "Mfull": "41/61",
              "Mall": "41/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.0007936507936507908,
            "gates": {
              "nominal": false,
              "calendar": true,
              "plus10": false,
              "dd": true
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 12551.137809329666,
            "delta": -688.3045705171262,
            "plus10": 10467.165628806304,
            "delta10": -536.2498355740827,
            "dd": -9.054184091363382,
            "counts": {
              "Mfull": "40/61",
              "Mall": "40/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.015079365079365137,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.015079365079365137,
        "delta10": -536.2498355740827,
        "worstDD": -9.054184091363382
      },
      {
        "id": "E604",
        "strategy": "N503ExploreR604",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 9055.465019728588,
            "delta": -4001.1498953490755,
            "plus10": 7541.712173002783,
            "delta10": -3389.4975705430807,
            "dd": -8.2687831198186,
            "counts": {
              "Mfull": "36/57",
              "Mall": "36/59",
              "Qfull": "13/19",
              "Qall": "14/21"
            },
            "margin": -0.13333333333333341,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 9206.394154149863,
            "delta": -4033.04822569693,
            "plus10": 7591.526557728236,
            "delta10": -3411.8889066521506,
            "dd": -8.280447342727648,
            "counts": {
              "Mfull": "38/57",
              "Mall": "38/59",
              "Qfull": "15/19",
              "Qall": "16/21"
            },
            "margin": -0.03809523809523818,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.13333333333333341,
        "delta10": -3411.8889066521506,
        "worstDD": -8.280447342727648
      },
      {
        "id": "E605",
        "strategy": "N503ExploreR605",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 11674.378423686756,
            "delta": -1382.2364913909078,
            "plus10": 9928.7249249676,
            "delta10": -1002.484818578263,
            "dd": -7.462807641796232,
            "counts": {
              "Mfull": "41/59",
              "Mall": "41/61",
              "Qfull": "16/19",
              "Qall": "17/21"
            },
            "margin": 0.00952380952380949,
            "gates": {
              "nominal": false,
              "calendar": true,
              "plus10": false,
              "dd": true
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 11883.704692525409,
            "delta": -1355.7376873213834,
            "plus10": 10026.747960476912,
            "delta10": -976.6675039034744,
            "dd": -8.168012803517177,
            "counts": {
              "Mfull": "42/59",
              "Mall": "42/61",
              "Qfull": "15/19",
              "Qall": "16/21"
            },
            "margin": -0.03809523809523818,
            "gates": {
              "nominal": false,
              "calendar": false,
              "plus10": false,
              "dd": true
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.03809523809523818,
        "delta10": -1002.484818578263,
        "worstDD": -8.168012803517177
      },
      {
        "id": "P601",
        "strategy": "N503CapacityR601",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 13123.604695779431,
            "delta": 66.98978070176781,
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
            "gates": {
              "nominal": true,
              "calendar": false,
              "plus10": true,
              "dd": true
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 13307.8134999793,
            "delta": 68.37112013250771,
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
            "gates": {
              "nominal": true,
              "calendar": false,
              "plus10": true,
              "dd": true
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
        "id": "P602",
        "strategy": "N503CapacityR602",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 13328.71171281593,
            "delta": 272.0967977382661,
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
            "gates": {
              "nominal": true,
              "calendar": true,
              "plus10": true,
              "dd": true
            },
            "eligible": true
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 13536.902513059405,
            "delta": 297.4601332126131,
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
            "gates": {
              "nominal": true,
              "calendar": false,
              "plus10": true,
              "dd": true
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
        "id": "P603",
        "strategy": "N503CapacityR603",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 12143.856484375285,
            "delta": -912.758430702379,
            "plus10": 10027.387379943882,
            "delta10": -903.8223636019811,
            "dd": -9.355006819199618,
            "counts": {
              "Mfull": "43/61",
              "Mall": "43/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.032539682539682535,
            "gates": {
              "nominal": false,
              "calendar": true,
              "plus10": false,
              "dd": true
            },
            "eligible": false
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 12310.794248954551,
            "delta": -928.6481308922412,
            "plus10": 10084.798143385558,
            "delta10": -918.6173209948283,
            "dd": -9.370866588714522,
            "counts": {
              "Mfull": "41/61",
              "Mall": "41/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.0007936507936507908,
            "gates": {
              "nominal": false,
              "calendar": true,
              "plus10": false,
              "dd": true
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": 0.0007936507936507908,
        "delta10": -918.6173209948283,
        "worstDD": -9.370866588714522
      },
      {
        "id": "P604",
        "strategy": "N503CapacityR604",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 13347.964134693444,
            "delta": 291.3492196157804,
            "plus10": 11232.89487257444,
            "delta10": 301.68512902857583,
            "dd": -8.781604713439917,
            "counts": {
              "Mfull": "41/61",
              "Mall": "41/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.0007936507936507908,
            "gates": {
              "nominal": true,
              "calendar": true,
              "plus10": true,
              "dd": true
            },
            "eligible": true
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 13562.215143060492,
            "delta": 322.77276321369936,
            "plus10": 11332.481937376444,
            "delta10": 329.0664729960572,
            "dd": -9.054184091363382,
            "counts": {
              "Mfull": "40/61",
              "Mall": "40/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": -0.015079365079365137,
            "gates": {
              "nominal": true,
              "calendar": false,
              "plus10": true,
              "dd": true
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.015079365079365137,
        "delta10": 301.68512902857583,
        "worstDD": -9.054184091363382
      },
      {
        "id": "P605",
        "strategy": "N503CapacityR605",
        "rows": [
          {
            "portfolio": "B",
            "pending": false,
            "net": 13328.71171281593,
            "delta": 272.0967977382661,
            "plus10": 11220.146271081927,
            "delta10": 288.9365275360633,
            "dd": -8.783684846762952,
            "counts": {
              "Mfull": "41/61",
              "Mall": "41/63",
              "Qfull": "17/19",
              "Qall": "18/21"
            },
            "margin": 0.0007936507936507908,
            "gates": {
              "nominal": true,
              "calendar": true,
              "plus10": true,
              "dd": true
            },
            "eligible": true
          },
          {
            "portfolio": "C",
            "pending": false,
            "net": 13536.902513059405,
            "delta": 297.4601332126131,
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
            "gates": {
              "nominal": true,
              "calendar": false,
              "plus10": true,
              "dd": true
            },
            "eligible": false
          }
        ],
        "pending": false,
        "eligible": false,
        "margin": -0.015079365079365137,
        "delta10": 288.9365275360633,
        "worstDD": -9.054184091363382
      }
    ],
    "eligible": [],
    "selected": null
  },
  "conditional_six_runs": {
    "executed": 0,
    "reason": "No eligible candidate; protocol does not activate fee engine/sensitivity runs."
  }
}
```
