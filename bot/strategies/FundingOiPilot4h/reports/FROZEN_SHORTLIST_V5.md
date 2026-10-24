# V5 — shortlist congelada antes de confirmación

Fijada 2026-10-21 01:10:16 UTC. Seis screenings completos y conciliados. Cuatro elegibles; dos finalistas por ranking prerregistrado: menor DD absoluto, mayor PF, menor turnover, menos features OI, ID. No se cambian criterios por retorno observado.

| Orden | Variante | Elegible | Trades | Neto período | CAGR desarrollo | PF | DD |
|---|---|---|---:|---:|---:|---:|---:|
| 3 | [ResearchV5CrossP4h](http://localhost:9200/#/backtest/50827027-6d6f-4c5d-8c23-5f2f91d7d971) | sí | 77 | 90.5292% | 21.3292% | 1.7118 | -17.6955% |
| 4 | [ResearchV5CrossOi4h](http://localhost:9200/#/backtest/642c5e9e-8705-4a9f-860d-d7ec071ef510) | sí | 57 | 60.0709% | 15.1534% | 1.6187 | -22.6662% |
| 2 | [ResearchV5FundingFP4h](http://localhost:9200/#/backtest/2c40635d-6a44-4bea-9a49-6b1ce1b8742d) | sí | 171 | 30.6788% | 8.3558% | 1.3627 | -15.7236% |
| 1 | [ResearchV5FundingFPOi4h](http://localhost:9200/#/backtest/e5bd6218-1066-4181-9ee6-7d5de2fae0c4) | sí | 132 | 34.0369% | 9.1835% | 1.5058 | -13.0230% |
| — | [ResearchV5VwapPV1h](http://localhost:9200/#/backtest/46f494e4-aca0-455e-979e-f279d3d87106) | no | 546 | -33.8694% | -11.6645% | 0.8831 | -40.9516% |
| — | [ResearchV5VwapPVOi1h](http://localhost:9200/#/backtest/6b21c3d2-69f7-4d70-8f8d-56d69974c270) | no | 350 | -33.1388% | -11.3729% | 0.8459 | -38.2830% |

Finalistas en orden:

1. FUNDING_FPOI: ResearchV5FundingFPOi4h, sesión SCREEN e5bd6218-1066-4181-9ee6-7d5de2fae0c4.
2. FUNDING_FP: ResearchV5FundingFP4h, sesión SCREEN 2c40635d-6a44-4bea-9a49-6b1ce1b8742d.

CROSS P/OI aprueban screening y quedan fuera por límite de dos finalistas y ranking de DD. Su CAGR de desarrollo superior no cambia la selección ya fijada. No se atribuye confirmación futura a esas dos variantes.

No se consultó todavía economía V5 de 2024–2025. Las dos finalistas se evalúan por separado y el selector global se decide con train antes de cada semestre. C1train reutiliza SCREEN exacto. Fuente/config/datasets/vecinos congelados en RESEARCH_PROTOCOL_V5_20261020.md, REGISTRY_V5.json y V5_IMPLEMENTATION_SOURCE_20261020.md.2020–2025 ya observado en otros ciclos: confirmación interna reutilizada.2026 cerrado.
