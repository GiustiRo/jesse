# BTC R9 — manifiesto final

20 nuevas corridas terminadas y auditadas,60snapshots,10jobs financieros (el primero incluye2referencias reutilizadas adicionales),44fuentes exactas finales de bases/rondas preservadas yR9. Fuentes originales sin cambios; 2026cerrado. QA es verificación sintética y de fuente, no prueba estadística. Los resultados de incertidumbre se guardan en BTC_R9_UNCERTAINTY_RESULTS_20261019.md con sus propios3jobs descriptivos.

```json
{
  "round": "R9",
  "development_only": true,
  "closed_2026": true,
  "nominal_reference_fee": 0.00045,
  "total_new_fulls": 20,
  "root_validation": 10,
  "exploration": 10,
  "forms": 20,
  "snapshots": 60,
  "registry": [
    {
      "name": "F70B",
      "id": "c20f22a8-38bf-4ad3-99d0-2d583d91d81c",
      "url": "http://localhost:9200/#/backtest/c20f22a8-38bf-4ad3-99d0-2d583d91d81c",
      "strategy": "BTCNovelR902",
      "seed": "Y902",
      "portfolio": "B",
      "fee": 0.0007,
      "recipe": "Y902",
      "role": "validation",
      "tp": 2,
      "status": "finished",
      "source_chars": 23016
    },
    {
      "name": "F70C",
      "id": "2297b82f-5db7-457a-8d46-9b53465dde7d",
      "url": "http://localhost:9200/#/backtest/2297b82f-5db7-457a-8d46-9b53465dde7d",
      "strategy": "BTCNovelR902",
      "seed": "Y902",
      "portfolio": "C",
      "fee": 0.0007,
      "recipe": "Y902",
      "role": "validation",
      "tp": 2,
      "status": "finished",
      "source_chars": 23016
    },
    {
      "name": "F95B",
      "id": "2b1ef237-1c48-40a9-84b3-d939ab99a3ba",
      "url": "http://localhost:9200/#/backtest/2b1ef237-1c48-40a9-84b3-d939ab99a3ba",
      "strategy": "BTCNovelR902",
      "seed": "Y902",
      "portfolio": "B",
      "fee": 0.00095,
      "recipe": "Y902",
      "role": "validation",
      "tp": 2,
      "status": "finished",
      "source_chars": 23016
    },
    {
      "name": "F95C",
      "id": "26f5560f-8db8-45f4-8203-1d0612658136",
      "url": "http://localhost:9200/#/backtest/26f5560f-8db8-45f4-8203-1d0612658136",
      "strategy": "BTCNovelR902",
      "seed": "Y902",
      "portfolio": "C",
      "fee": 0.00095,
      "recipe": "Y902",
      "role": "validation",
      "tp": 2,
      "status": "finished",
      "source_chars": 23016
    },
    {
      "name": "N95B",
      "id": "9b7b99b1-a5a1-440d-98f5-aa1c45a1108c",
      "url": "http://localhost:9200/#/backtest/9b7b99b1-a5a1-440d-98f5-aa1c45a1108c",
      "strategy": "X03ExploreR204",
      "seed": "Y902",
      "portfolio": "B",
      "fee": 0.00095,
      "recipe": "N204",
      "role": "validation",
      "tp": 2,
      "status": "finished",
      "source_chars": 21582
    },
    {
      "name": "N95C",
      "id": "b1399fa4-5495-43c1-bc45-3bc6d1b3da7b",
      "url": "http://localhost:9200/#/backtest/b1399fa4-5495-43c1-bc45-3bc6d1b3da7b",
      "strategy": "X03ExploreR204",
      "seed": "Y902",
      "portfolio": "C",
      "fee": 0.00095,
      "recipe": "N204",
      "role": "validation",
      "tp": 2,
      "status": "finished",
      "source_chars": 21582
    },
    {
      "name": "T18B",
      "id": "3723e918-e830-4697-abb4-7f9e2d0f172a",
      "url": "http://localhost:9200/#/backtest/3723e918-e830-4697-abb4-7f9e2d0f172a",
      "strategy": "BtcY902RobustT18",
      "seed": "Y902",
      "portfolio": "B",
      "fee": 0.00045,
      "recipe": "T18",
      "role": "validation",
      "tp": 1.8,
      "status": "finished",
      "source_chars": 23354
    },
    {
      "name": "T18C",
      "id": "07e4ce1e-e76b-410c-903e-156864907ea5",
      "url": "http://localhost:9200/#/backtest/07e4ce1e-e76b-410c-903e-156864907ea5",
      "strategy": "BtcY902RobustT18",
      "seed": "Y902",
      "portfolio": "C",
      "fee": 0.00045,
      "recipe": "T18",
      "role": "validation",
      "tp": 1.8,
      "status": "finished",
      "source_chars": 23354
    },
    {
      "name": "T22B",
      "id": "826b451d-5836-4385-b421-ad63b64f1a76",
      "url": "http://localhost:9200/#/backtest/826b451d-5836-4385-b421-ad63b64f1a76",
      "strategy": "BtcY902RobustT22",
      "seed": "Y902",
      "portfolio": "B",
      "fee": 0.00045,
      "recipe": "T22",
      "role": "validation",
      "tp": 2.2,
      "status": "finished",
      "source_chars": 23354
    },
    {
      "name": "T22C",
      "id": "dc26f343-496f-4fea-9394-0ef595e8e65a",
      "url": "http://localhost:9200/#/backtest/dc26f343-496f-4fea-9394-0ef595e8e65a",
      "strategy": "BtcY902RobustT22",
      "seed": "Y902",
      "portfolio": "C",
      "fee": 0.00045,
      "recipe": "T22",
      "role": "validation",
      "tp": 2.2,
      "status": "finished",
      "source_chars": 23354
    },
    {
      "name": "K1001C",
      "id": "08d01428-7abe-410a-bf7d-f8c8d46aa35c",
      "url": "http://localhost:9200/#/backtest/08d01428-7abe-410a-bf7d-f8c8d46aa35c",
      "strategy": "BtcY902ExploreR1001",
      "seed": "Y902",
      "portfolio": "C",
      "fee": 0.00045,
      "recipe": "K1001",
      "tp": 2,
      "role": "exploration",
      "status": "finished",
      "source_chars": 23118
    },
    {
      "name": "K1001B",
      "id": "10be7d01-51f7-480c-9b6c-8b653da82c5a",
      "url": "http://localhost:9200/#/backtest/10be7d01-51f7-480c-9b6c-8b653da82c5a",
      "strategy": "BtcY902ExploreR1001",
      "seed": "Y902",
      "portfolio": "B",
      "fee": 0.00045,
      "recipe": "K1001",
      "tp": 2,
      "role": "exploration",
      "status": "finished",
      "source_chars": 23118
    },
    {
      "name": "K1002C",
      "id": "36c79fa4-2e96-482d-80d3-7692b85a261d",
      "url": "http://localhost:9200/#/backtest/36c79fa4-2e96-482d-80d3-7692b85a261d",
      "strategy": "BtcY902ExploreR1002",
      "seed": "Y902",
      "portfolio": "C",
      "fee": 0.00045,
      "recipe": "K1002",
      "tp": 2,
      "role": "exploration",
      "status": "finished",
      "source_chars": 23151
    },
    {
      "name": "K1002B",
      "id": "728f638d-0f10-4b6c-9b6f-4f5533c89df9",
      "url": "http://localhost:9200/#/backtest/728f638d-0f10-4b6c-9b6f-4f5533c89df9",
      "strategy": "BtcY902ExploreR1002",
      "seed": "Y902",
      "portfolio": "B",
      "fee": 0.00045,
      "recipe": "K1002",
      "tp": 2,
      "role": "exploration",
      "status": "finished",
      "source_chars": 23151
    },
    {
      "name": "K1003B",
      "recipe": "K1003",
      "portfolio": "B",
      "strategy": "BtcY902ExploreR1003",
      "id": "82105bee-e22b-4ae2-a311-b369453b03e9",
      "url": "http://localhost:9200/#/backtest/82105bee-e22b-4ae2-a311-b369453b03e9",
      "seed": "Y902",
      "fee": 0.00045,
      "role": "exploration",
      "tp": 2,
      "status": "finished",
      "source_chars": 24387
    },
    {
      "name": "K1003C",
      "recipe": "K1003",
      "portfolio": "C",
      "strategy": "BtcY902ExploreR1003",
      "id": "00c0f043-ea8a-4d28-88be-7553442909e1",
      "url": "http://localhost:9200/#/backtest/00c0f043-ea8a-4d28-88be-7553442909e1",
      "seed": "Y902",
      "fee": 0.00045,
      "role": "exploration",
      "tp": 2,
      "status": "finished",
      "source_chars": 24387
    },
    {
      "name": "K1004B",
      "recipe": "K1004",
      "portfolio": "B",
      "strategy": "BtcY902ExploreR1004",
      "id": "a523b5c5-8a91-4dd0-b596-550405b10fe5",
      "url": "http://localhost:9200/#/backtest/a523b5c5-8a91-4dd0-b596-550405b10fe5",
      "seed": "Y902",
      "fee": 0.00045,
      "role": "exploration",
      "tp": 2,
      "status": "finished",
      "source_chars": 24405
    },
    {
      "name": "K1004C",
      "recipe": "K1004",
      "portfolio": "C",
      "strategy": "BtcY902ExploreR1004",
      "id": "e32e4b65-850b-475f-9179-be61b25131d6",
      "url": "http://localhost:9200/#/backtest/e32e4b65-850b-475f-9179-be61b25131d6",
      "seed": "Y902",
      "fee": 0.00045,
      "role": "exploration",
      "tp": 2,
      "status": "finished",
      "source_chars": 24405
    },
    {
      "name": "K1005B",
      "recipe": "K1005",
      "portfolio": "B",
      "strategy": "BtcY902ExploreR1005",
      "id": "3f979db7-44e2-44c6-9b82-7c3362084f62",
      "url": "http://localhost:9200/#/backtest/3f979db7-44e2-44c6-9b82-7c3362084f62",
      "seed": "Y902",
      "fee": 0.00045,
      "role": "exploration",
      "tp": 2,
      "status": "finished",
      "source_chars": 24606
    },
    {
      "name": "K1005C",
      "recipe": "K1005",
      "portfolio": "C",
      "strategy": "BtcY902ExploreR1005",
      "id": "8d198fc1-eae8-4a67-8258-e6fabe58756a",
      "url": "http://localhost:9200/#/backtest/8d198fc1-eae8-4a67-8258-e6fabe58756a",
      "seed": "Y902",
      "fee": 0.00045,
      "role": "exploration",
      "tp": 2,
      "status": "finished",
      "source_chars": 24606
    }
  ],
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
    },
    {
      "name": "BtcY902RobustT18",
      "exact": true,
      "chars": 23354
    },
    {
      "name": "BtcY902RobustT22",
      "exact": true,
      "chars": 23354
    },
    {
      "name": "BtcY902ExploreR1001",
      "exact": true,
      "chars": 23118
    },
    {
      "name": "BtcY902ExploreR1002",
      "exact": true,
      "chars": 23151
    },
    {
      "name": "BtcY902ExploreR1003",
      "exact": true,
      "chars": 24387
    },
    {
      "name": "BtcY902ExploreR1004",
      "exact": true,
      "chars": 24405
    },
    {
      "name": "BtcY902ExploreR1005",
      "exact": true,
      "chars": 24606
    }
  ],
  "form_checks": {
    "c20f22a8-38bf-4ad3-99d0-2d583d91d81c": {
      "name": "F70B",
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
    "2297b82f-5db7-457a-8d46-9b53465dde7d": {
      "name": "F70C",
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
    "2b1ef237-1c48-40a9-84b3-d939ab99a3ba": {
      "name": "F95B",
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
    "26f5560f-8db8-45f4-8203-1d0612658136": {
      "name": "F95C",
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
    "9b7b99b1-a5a1-440d-98f5-aa1c45a1108c": {
      "name": "N95B",
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
    "b1399fa4-5495-43c1-bc45-3bc6d1b3da7b": {
      "name": "N95C",
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
    "3723e918-e830-4697-abb4-7f9e2d0f172a": {
      "name": "T18B",
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
    "07e4ce1e-e76b-410c-903e-156864907ea5": {
      "name": "T18C",
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
    "826b451d-5836-4385-b421-ad63b64f1a76": {
      "name": "T22B",
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
    "dc26f343-496f-4fea-9394-0ef595e8e65a": {
      "name": "T22C",
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
    "08d01428-7abe-410a-bf7d-f8c8d46aa35c": {
      "name": "K1001C",
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
    "10be7d01-51f7-480c-9b6c-8b653da82c5a": {
      "name": "K1001B",
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
    "36c79fa4-2e96-482d-80d3-7692b85a261d": {
      "name": "K1002C",
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
    "728f638d-0f10-4b6c-9b6f-4f5533c89df9": {
      "name": "K1002B",
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
    "82105bee-e22b-4ae2-a311-b369453b03e9": {
      "name": "K1003B",
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
    "00c0f043-ea8a-4d28-88be-7553442909e1": {
      "name": "K1003C",
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
    "a523b5c5-8a91-4dd0-b596-550405b10fe5": {
      "name": "K1004B",
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
    "e32e4b65-850b-475f-9179-be61b25131d6": {
      "name": "K1004C",
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
    "3f979db7-44e2-44c6-9b82-7c3362084f62": {
      "name": "K1005B",
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
    "8d198fc1-eae8-4a67-8258-e6fabe58756a": {
      "name": "K1005C",
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
  "financial_jobs": [
    {
      "batch": "F70",
      "names": [
        "F70B",
        "F70C",
        "N70B",
        "N70C"
      ],
      "job": "2d6f506cc70945479f12cce11e16a2a0",
      "status": "succeeded"
    },
    {
      "batch": "F95",
      "names": [
        "F95B",
        "F95C"
      ],
      "job": "bc707f055b59457598705f9f40d6a6a1",
      "status": "succeeded"
    },
    {
      "batch": "K1001",
      "names": [
        "K1001B",
        "K1001C"
      ],
      "job": "5b3590fd123c4eefbb495815b5d02115",
      "status": "succeeded"
    },
    {
      "batch": "N95",
      "names": [
        "N95B",
        "N95C"
      ],
      "job": "2d7c762c832b4cbc82d4da27f37bda75",
      "status": "succeeded"
    },
    {
      "batch": "K1002",
      "names": [
        "K1002B",
        "K1002C"
      ],
      "job": "066902519f304a5fad842cbc6d97f5e3",
      "status": "succeeded"
    },
    {
      "batch": "T18",
      "names": [
        "T18B",
        "T18C"
      ],
      "job": "5f1aaf8d9faa4cc08fc459430b173a2c",
      "status": "succeeded"
    },
    {
      "batch": "K1003",
      "names": [
        "K1003B",
        "K1003C",
        "N204B",
        "N204C"
      ],
      "job": "2677216f1fce42eda424f223a901a206",
      "status": "succeeded"
    },
    {
      "batch": "T22",
      "names": [
        "T22B",
        "T22C"
      ],
      "job": "370b56f89378453ca44c9c70cebd605f",
      "status": "succeeded"
    },
    {
      "batch": "K1004",
      "names": [
        "K1004B",
        "K1004C",
        "N204B",
        "N204C"
      ],
      "job": "e779160ebcde4a6986014a11fb6c09e1",
      "status": "succeeded"
    },
    {
      "batch": "K1005",
      "names": [
        "K1005B",
        "K1005C",
        "N204B",
        "N204C"
      ],
      "job": "6666db461dc14880b8d0f4e788eb7423",
      "status": "succeeded"
    }
  ],
  "financial_checks": [
    {
      "name": "F70B",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "F70C",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "F95B",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "F95C",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "N95B",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "N95C",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "T18B",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "T18C",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "T22B",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "T22C",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "K1001C",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "K1001B",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "K1002C",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "K1002B",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "K1003B",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "K1003C",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "K1004B",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "K1004C",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "K1005B",
      "audit": "passed",
      "terminal": true
    },
    {
      "name": "K1005C",
      "audit": "passed",
      "terminal": true
    }
  ],
  "sleeve_metadata": {
    "F70B": {
      "ok": true,
      "pages": 17,
      "lines_read": 8140,
      "log_fills": 46,
      "matched": 46,
      "types": {
        "STOP": 45,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "F70C": {
      "ok": true,
      "pages": 17,
      "lines_read": 8342,
      "log_fills": 46,
      "matched": 46,
      "types": {
        "STOP": 45,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "F95B": {
      "ok": true,
      "pages": 17,
      "lines_read": 8125,
      "log_fills": 46,
      "matched": 46,
      "types": {
        "STOP": 45,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "F95C": {
      "ok": true,
      "pages": 17,
      "lines_read": 8325,
      "log_fills": 46,
      "matched": 46,
      "types": {
        "STOP": 45,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "T18B": {
      "ok": true,
      "pages": 17,
      "lines_read": 8194,
      "log_fills": 46,
      "matched": 46,
      "types": {
        "STOP": 45,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "T18C": {
      "ok": true,
      "pages": 17,
      "lines_read": 8398,
      "log_fills": 46,
      "matched": 46,
      "types": {
        "STOP": 45,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "T22B": {
      "ok": true,
      "pages": 17,
      "lines_read": 8178,
      "log_fills": 46,
      "matched": 46,
      "types": {
        "STOP": 45,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "T22C": {
      "ok": true,
      "pages": 17,
      "lines_read": 8382,
      "log_fills": 46,
      "matched": 46,
      "types": {
        "STOP": 45,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "K1001C": {
      "ok": true,
      "pages": 17,
      "lines_read": 8372,
      "log_fills": 45,
      "matched": 45,
      "types": {
        "STOP": 44,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "K1001B": {
      "ok": true,
      "pages": 17,
      "lines_read": 8168,
      "log_fills": 45,
      "matched": 45,
      "types": {
        "STOP": 44,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "K1002C": {
      "ok": true,
      "pages": 17,
      "lines_read": 8099,
      "log_fills": 20,
      "matched": 20,
      "types": {
        "STOP": 20
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "K1002B": {
      "ok": true,
      "pages": 16,
      "lines_read": 7895,
      "log_fills": 20,
      "matched": 20,
      "types": {
        "STOP": 20
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "K1003B": {
      "ok": true,
      "pages": 17,
      "lines_read": 8303,
      "log_fills": 47,
      "matched": 47,
      "types": {
        "STOP": 46,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "K1003C": {
      "ok": true,
      "pages": 18,
      "lines_read": 8507,
      "log_fills": 47,
      "matched": 47,
      "types": {
        "STOP": 46,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "K1004B": {
      "ok": true,
      "pages": 17,
      "lines_read": 8222,
      "log_fills": 47,
      "matched": 47,
      "types": {
        "STOP": 46,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "K1004C": {
      "ok": true,
      "pages": 17,
      "lines_read": 8426,
      "log_fills": 47,
      "matched": 47,
      "types": {
        "STOP": 46,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "K1005B": {
      "ok": true,
      "pages": 17,
      "lines_read": 8222,
      "log_fills": 46,
      "matched": 46,
      "types": {
        "STOP": 45,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    },
    "K1005C": {
      "ok": true,
      "pages": 17,
      "lines_read": 8426,
      "log_fills": 46,
      "matched": 46,
      "types": {
        "STOP": 45,
        "MARKET": 1
      },
      "boundary_adjustment": 0,
      "errors": []
    }
  },
  "qa": {
    "tp_final": {
      "checks": 63,
      "job": "76daf922500d4f28aea6d0ff25289687"
    },
    "exploratory": {
      "checks": 230,
      "job": "c568aedf303a420a90d74a2d0f2a391d"
    }
  },
  "data_handling": {
    "snapshot_key_formats": [
      "exchange-symbol",
      "class"
    ],
    "root_report_page_join_correction": [
      {
        "name": "BtcY902ExploreR1005",
        "readback_exact_after_removing_artificial_page_join_newline": true,
        "offset": 2063
      }
    ],
    "sources_not_changed_by_correction": true
  },
  "selection": "Diagnostics and candidates only; no live promotion, no TP-neighbour selection; no additional backtests."
}
```
