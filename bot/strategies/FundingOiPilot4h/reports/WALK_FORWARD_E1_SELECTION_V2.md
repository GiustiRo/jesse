# Selección E1 V2 — SIN_CANDIDATA
Decisión UTC: 2026-10-20T22:33:49.399Z. Sólo entrenamiento [2020-09-01,2022-01-01).

| Configuración | Trades | Neto % | PF | DD % | Elegible |
|---|---:|---:|---:|---:|---|
| [H1_FIXED_P](http://localhost:9200/#/backtest/16f2c940-30b1-4bb2-95cb-f25614e88770) | 284 | -28.63 | 0.907 | -42.72 | No |
| [H1_FIXED_POI](http://localhost:9200/#/backtest/032ec154-d3a3-4aea-b2a0-e4334b705644) | 212 | -6.83 | 0.973 | -33.94 | No |
| [H1_ATR_P](http://localhost:9200/#/backtest/5d77182b-2071-4056-a11f-4f7c5d5ef12f) | 263 | -12.69 | 0.928 | -31.19 | No |
| [H1_ATR_POI](http://localhost:9200/#/backtest/8e030d85-6762-42d7-91ef-546ca2a6b340) | 198 | -0.20 | 0.999 | -29.08 | No |

Las cuatro superan 30 trades, pero las cuatro fallan neto>0, PF>=1,2 y absDD<=25%. No se relajan gates porque ATR+OI se acerque a equilibrio.

El selector E1 permanecerá plano en [2022-01-01,2022-07-01), retorno convencional0 y PF indefinido por ausencia de trades seleccionados. Las evaluaciones ATR previstas siguen siendo diagnósticas, no operaciones elegidas por el selector.

Esta selección se guarda antes de iniciar o consultar las dos evaluaciones nuevas ATR E1V; ambas siguen especificadas sin sesión. Los controles fijos y sus evaluaciones ya se observaron en V1; no se afirma independencia nueva. La ausencia de candidata en E1 no cierra todo V2: faltan sus evaluaciones y E2–E4 según protocolo.

Job MCP de comparación y conciliación: 167602b5b53c43079d0778bd52dfe83c. Fuente congelada y datasets en REGISTRY_V2.json y RESEARCH_PROTOCOL_V2_20261020.md. Sin consultas2026.
