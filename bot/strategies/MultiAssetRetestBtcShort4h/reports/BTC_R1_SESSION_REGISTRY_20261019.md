# BTC R1 — registro final de sesiones — 2026-10-19

Las 18 sesiones autorizadas finalizaron sin errores. Tres agentes nuevos evaluaron nueve hipótesis distintas, cada una por separado en B y C. Cada ticket permitió un par B/C simultáneo; máximo global de cuatro backtests y dos análisis. No quedan pruebas económicas pendientes.

Los cuatro originales PortCompare permanecen idénticos a sus versiones iniciales. Las copias Entry recibieron después de sus corridas una corrección de un comentario sobre persistencia de logs; no cambió código ejecutable. Root verificó que revertir ese único comentario recupera exactamente los bytes congelados en las tres clases. Los snapshots de tres fuentes por sesión conservan la procedencia económica.

Controles reutilizados, sin nuevas corridas: [B](http://localhost:9200/#/backtest/29387384-c48c-4ac9-94bd-632a2ec3bb7f) y [C](http://localhost:9200/#/backtest/30ab3788-51bb-4435-8c21-9b12c45f8835). Riesgo de 1% por trade y 8% agregado; la cartera histórica de 3% no es comparable.

## Sesiones

| Nombre | Estado | Dashboard |
|---|---|---|
| E01B | finished | [E01B](http://localhost:9200/#/backtest/9de1ae4d-ef15-4d8f-9022-20ee1a830ec6) |
| E01C | finished | [E01C](http://localhost:9200/#/backtest/1a62497a-7609-4bfd-9153-15c8640cf67a) |
| P01B | finished | [P01B](http://localhost:9200/#/backtest/17867dbb-3676-46e9-a427-d60694384528) |
| P01C | finished | [P01C](http://localhost:9200/#/backtest/dc50d6e4-8799-437a-8d1e-8b81e22cf8ee) |
| X01B | finished | [X01B](http://localhost:9200/#/backtest/77a80211-701a-4af4-9fb6-b77130b7b4c8) |
| X01C | finished | [X01C](http://localhost:9200/#/backtest/9b5cbe51-91ee-4361-b080-c28c0cd38fdb) |
| E02B | finished | [E02B](http://localhost:9200/#/backtest/97d654d0-5917-4a26-b151-11ef396591e6) |
| E02C | finished | [E02C](http://localhost:9200/#/backtest/a9b5fe7e-9fb3-47bc-9c1c-25155d7929c3) |
| P02B | finished | [P02B](http://localhost:9200/#/backtest/85a2fe07-0f26-4271-88d0-4ebdcd8814f1) |
| P02C | finished | [P02C](http://localhost:9200/#/backtest/b91112c0-e3f3-4c31-8dea-abf184cf2d40) |
| X02B | finished | [X02B](http://localhost:9200/#/backtest/56c48468-10dd-489e-b921-fa948dbd34ae) |
| X02C | finished | [X02C](http://localhost:9200/#/backtest/dd5b6e8d-6207-4e01-9bce-8a18c5d416e4) |
| E03B | finished | [E03B](http://localhost:9200/#/backtest/20ca6dae-a6c9-44ed-8349-5877e2d3827c) |
| E03C | finished | [E03C](http://localhost:9200/#/backtest/f551da25-c6c9-4a31-8ad9-7fc4f71ad823) |
| P03B | finished | [P03B](http://localhost:9200/#/backtest/6eea0aa5-84fa-45b1-9e44-86d1e2c29a18) |
| P03C | finished | [P03C](http://localhost:9200/#/backtest/5652bfcb-64b2-4131-a757-3c5fcde4f886) |
| X03B | finished | [X03B](http://localhost:9200/#/backtest/53937852-34a3-48c7-ab35-fac586341127) |
| X03C | finished | [X03C](http://localhost:9200/#/backtest/3935efb3-2b27-4ada-86ce-94123d7a6e2c) |

## Comprobaciones de root

Los 18 formularios y 54 snapshots de fuentes pasaron verificación independiente: ventana 2020-10-15→2025-12-31 exclusiva; rutas BTC/PAXG/SPY ordenadas en 4h y tres datos M1; cuenta de 10000 USDT; comisión .00045 por lado; isolated 5x; warmup 240; debug=true, fast=false y export_chart=true. Las fuentes preservan 1%/8%/4.4 y el ledger común.

Los 18 resultados pasaron conciliación de fills, cantidades, fees, PNL, wallet, cierre terminal y MTM diario. No se consultó 2026 ni se cambió producción, live, paper o configuración global.

```json
[
  {
    "name": "X03B",
    "id": "53937852-34a3-48c7-ab35-fac586341127",
    "url": "http://localhost:9200/#/backtest/53937852-34a3-48c7-ab35-fac586341127",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "X03C",
    "id": "3935efb3-2b27-4ada-86ce-94123d7a6e2c",
    "url": "http://localhost:9200/#/backtest/3935efb3-2b27-4ada-86ce-94123d7a6e2c",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "P03B",
    "id": "6eea0aa5-84fa-45b1-9e44-86d1e2c29a18",
    "url": "http://localhost:9200/#/backtest/6eea0aa5-84fa-45b1-9e44-86d1e2c29a18",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "P03C",
    "id": "5652bfcb-64b2-4131-a757-3c5fcde4f886",
    "url": "http://localhost:9200/#/backtest/5652bfcb-64b2-4131-a757-3c5fcde4f886",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "E03C",
    "id": "f551da25-c6c9-4a31-8ad9-7fc4f71ad823",
    "url": "http://localhost:9200/#/backtest/f551da25-c6c9-4a31-8ad9-7fc4f71ad823",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "E03B",
    "id": "20ca6dae-a6c9-44ed-8349-5877e2d3827c",
    "url": "http://localhost:9200/#/backtest/20ca6dae-a6c9-44ed-8349-5877e2d3827c",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "X02C",
    "id": "dd5b6e8d-6207-4e01-9bce-8a18c5d416e4",
    "url": "http://localhost:9200/#/backtest/dd5b6e8d-6207-4e01-9bce-8a18c5d416e4",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "X02B",
    "id": "56c48468-10dd-489e-b921-fa948dbd34ae",
    "url": "http://localhost:9200/#/backtest/56c48468-10dd-489e-b921-fa948dbd34ae",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "P02C",
    "id": "b91112c0-e3f3-4c31-8dea-abf184cf2d40",
    "url": "http://localhost:9200/#/backtest/b91112c0-e3f3-4c31-8dea-abf184cf2d40",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "P02B",
    "id": "85a2fe07-0f26-4271-88d0-4ebdcd8814f1",
    "url": "http://localhost:9200/#/backtest/85a2fe07-0f26-4271-88d0-4ebdcd8814f1",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "E02C",
    "id": "a9b5fe7e-9fb3-47bc-9c1c-25155d7929c3",
    "url": "http://localhost:9200/#/backtest/a9b5fe7e-9fb3-47bc-9c1c-25155d7929c3",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "E02B",
    "id": "97d654d0-5917-4a26-b151-11ef396591e6",
    "url": "http://localhost:9200/#/backtest/97d654d0-5917-4a26-b151-11ef396591e6",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "X01B",
    "id": "77a80211-701a-4af4-9fb6-b77130b7b4c8",
    "url": "http://localhost:9200/#/backtest/77a80211-701a-4af4-9fb6-b77130b7b4c8",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "X01C",
    "id": "9b5cbe51-91ee-4361-b080-c28c0cd38fdb",
    "url": "http://localhost:9200/#/backtest/9b5cbe51-91ee-4361-b080-c28c0cd38fdb",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "P01C",
    "id": "dc50d6e4-8799-437a-8d1e-8b81e22cf8ee",
    "url": "http://localhost:9200/#/backtest/dc50d6e4-8799-437a-8d1e-8b81e22cf8ee",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "P01B",
    "id": "17867dbb-3676-46e9-a427-d60694384528",
    "url": "http://localhost:9200/#/backtest/17867dbb-3676-46e9-a427-d60694384528",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "E01C",
    "id": "1a62497a-7609-4bfd-9153-15c8640cf67a",
    "url": "http://localhost:9200/#/backtest/1a62497a-7609-4bfd-9153-15c8640cf67a",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  },
  {
    "name": "E01B",
    "id": "9de1ae4d-ef15-4d8f-9022-20ee1a830ec6",
    "url": "http://localhost:9200/#/backtest/9de1ae4d-ef15-4d8f-9022-20ee1a830ec6",
    "status": "finished",
    "dates": true,
    "routes": true,
    "data": true,
    "exchange": true,
    "warmup": true,
    "options": true,
    "BTC": true,
    "PAXG": true,
    "SPY": true
  }
]
```

## Tickets

```json
[
  {
    "id": "E01",
    "agent": "btc_entry_fresh",
    "status": "finished"
  },
  {
    "id": "P01",
    "agent": "btc_payoff_fresh",
    "status": "finished"
  },
  {
    "id": "X01",
    "agent": "btc_explore_fresh",
    "status": "finished"
  },
  {
    "id": "E02",
    "agent": "btc_entry_fresh",
    "status": "finished"
  },
  {
    "id": "P02",
    "agent": "btc_payoff_fresh",
    "status": "finished"
  },
  {
    "id": "X02",
    "agent": "btc_explore_fresh",
    "status": "finished"
  },
  {
    "id": "E03",
    "agent": "btc_entry_fresh",
    "status": "finished"
  },
  {
    "id": "P03",
    "agent": "btc_payoff_fresh",
    "status": "finished"
  },
  {
    "id": "X03",
    "agent": "btc_explore_fresh",
    "status": "finished"
  }
]
```

Decisión y límites: BTC_R1_RESULTS_20261019.md. Todo está guardado dentro del proyecto Jesse.
