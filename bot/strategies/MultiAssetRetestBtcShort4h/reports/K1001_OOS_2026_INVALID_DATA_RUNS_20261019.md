# INVALIDADAS — primeras cuatro corridas por PAXG truncado

La auditoría posterior a las corridas detectó PAXG-USDT únicamente hasta2026-02-24T17:59Z:78840minutos2026 y ningún registro posterior. El motor terminó la ventana2026-01-01→2026-10-19 sin rechazar esa cola ausente en la cartera de fuentes mixtas. Una posiciónPAXG abierta en febrero se mantuvo a precio antiguo hasta el cierre de frontera; junioMTM fue plano pese a esa posición. Es un defecto de cobertura de esta ejecución, NO evidencia económica OOS utilizable.

**No usar +1.54%/+14.87% nominal ni -1.62%/+9.89%estresado como resultados OOS válidos.** La conciliación contable pasó, pero no valida integridad de la serie. Las cuatro corridas se conservan, sin ocultarlas, y se repetirán tras completar la MISMA fuente PAXG Binance Spot y verificar paridad de todo solape. No se modifica ninguna regla/parámetro ni selección B/C después de los números provisionales.

## Evidencia
Auditor read-only research_scripts/k1001_oos_route_coverage.py, jobdb286e1e9a954e5c926e18a9d44848f6 succeeded. Reporte research_scripts/data/histdata/K1001_2026_all_route_coverage.json. BTC2026 completo419040minutos hasta18oct23:59, cero huecos. SPX270634minutos observados hasta16oct21:13, huecos del mercado conservados. PAXG truncado24feb17:59.

## Sesiones inválidas conservadas
```json
[
  {
    "label": "B_N",
    "id": "7f4892ec-ffe5-46ce-9597-aea14676766c",
    "status": "finished_but_invalid_missing_PAXG_tail",
    "url": "http://localhost:9200/#/backtest/7f4892ec-ffe5-46ce-9597-aea14676766c"
  },
  {
    "label": "C_N",
    "id": "8229453f-5214-4c71-9696-9aadc514e4c3",
    "status": "finished_but_invalid_missing_PAXG_tail",
    "url": "http://localhost:9200/#/backtest/8229453f-5214-4c71-9696-9aadc514e4c3"
  },
  {
    "label": "B_F95",
    "id": "62a5d042-6b65-4dcc-a89c-ea6bf593d99a",
    "status": "finished_but_invalid_missing_PAXG_tail",
    "url": "http://localhost:9200/#/backtest/62a5d042-6b65-4dcc-a89c-ea6bf593d99a"
  },
  {
    "label": "C_F95",
    "id": "b18d5096-32cd-42ae-a8d1-144ec0122fb5",
    "status": "finished_but_invalid_missing_PAXG_tail",
    "url": "http://localhost:9200/#/backtest/b18d5096-32cd-42ae-a8d1-144ec0122fb5"
  }
]
```

Análisis contable provisional1cf22b6ffea84324a0a177e6a8dc063b succeeded, pero sus números quedan invalidados por calidad de datos. Primer job111e2a885c784b289467ab600313cd7e falló sólo al importar logger, corregido sin cambiar cálculos. No es evaluación válida de estrategia. Imagen no recuperable por herramienta artifact_changed; no se usa fallback.

Corrección autorizada dentro de la ejecución: importación Binance Spot PAXG desde2025-11-01 iniciada; apéndice2026 al proxy Binance Perpetual Futures verificará solape, unicidad y conservará histórico. Crear cuatro nuevas sesiones iguales y guardar resultados corregidos; no reoptimizar2026.
