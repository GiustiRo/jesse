# K1001 OOS 2026 — registro definitivo

Finalizaron cuatro corridas con datos corregidos. Resultado y decisión: K1001_OOS_2026_10K_RESULTS_20261019.md. Datos completos: K1001_OOS_2026_10K_DATA_20261019.md. Mantener separadas de las cuatro ejecuciones iniciales inválidas por PAXG truncado y del intento que reutilizó su caché. No hubo ajustes de reglas/parámetros.

```json
{
  "valid_runs": [
    {
      "label": "B_N",
      "id": "d6ed3b7d-19c5-4240-8ad9-9cb2f7706667",
      "status": "finished_verified",
      "invalid_previous": "7f4892ec-ffe5-46ce-9597-aea14676766c",
      "url": "http://localhost:9200/#/backtest/d6ed3b7d-19c5-4240-8ad9-9cb2f7706667"
    },
    {
      "label": "C_N",
      "id": "3c175497-66bf-4cf0-a9f8-c888834961da",
      "status": "finished_verified",
      "invalid_previous": "8229453f-5214-4c71-9696-9aadc514e4c3",
      "url": "http://localhost:9200/#/backtest/3c175497-66bf-4cf0-a9f8-c888834961da"
    },
    {
      "label": "B_F95",
      "id": "40239c00-168a-4ab4-b423-069c91e6e6b7",
      "status": "finished_verified",
      "invalid_previous": "62a5d042-6b65-4dcc-a89c-ea6bf593d99a",
      "url": "http://localhost:9200/#/backtest/40239c00-168a-4ab4-b423-069c91e6e6b7"
    },
    {
      "label": "C_F95",
      "id": "df30484a-1331-4faa-9097-6c2e7d7011bc",
      "status": "finished_verified",
      "invalid_previous": "b18d5096-32cd-42ae-a8d1-144ec0122fb5",
      "url": "http://localhost:9200/#/backtest/df30484a-1331-4faa-9097-6c2e7d7011bc"
    }
  ],
  "checks": [
    {
      "label": "B_N",
      "status": "finished",
      "form_identical": true,
      "source_identical": true
    },
    {
      "label": "C_N",
      "status": "finished",
      "form_identical": true,
      "source_identical": true
    },
    {
      "label": "B_F95",
      "status": "finished",
      "form_identical": true,
      "source_identical": true
    },
    {
      "label": "C_F95",
      "status": "finished",
      "form_identical": true,
      "source_identical": true
    }
  ],
  "invalid_original_runs": [
    {
      "label": "B_N",
      "id": "7f4892ec-ffe5-46ce-9597-aea14676766c",
      "status": "INVALID_missing_PAXG_tail",
      "url": "http://localhost:9200/#/backtest/7f4892ec-ffe5-46ce-9597-aea14676766c"
    },
    {
      "label": "C_N",
      "id": "8229453f-5214-4c71-9696-9aadc514e4c3",
      "status": "INVALID_missing_PAXG_tail",
      "url": "http://localhost:9200/#/backtest/8229453f-5214-4c71-9696-9aadc514e4c3"
    },
    {
      "label": "B_F95",
      "id": "62a5d042-6b65-4dcc-a89c-ea6bf593d99a",
      "status": "INVALID_missing_PAXG_tail",
      "url": "http://localhost:9200/#/backtest/62a5d042-6b65-4dcc-a89c-ea6bf593d99a"
    },
    {
      "label": "C_F95",
      "id": "b18d5096-32cd-42ae-a8d1-144ec0122fb5",
      "status": "INVALID_missing_PAXG_tail",
      "url": "http://localhost:9200/#/backtest/b18d5096-32cd-42ae-a8d1-144ec0122fb5"
    }
  ],
  "jobs": {
    "paxg_import": "540f0200-6eaf-4b73-b14e-780149efde8d",
    "paxg_append": "2886cd079897455db72ef6bad534732d",
    "spx_import": "81c596cc01e5435cb6cb4257ace3dcea",
    "tick_audit": "dcc16174b48a4c758f87b7397bf584f1",
    "final_analysis": "3543852d0eab43d9be15e066eb7017d4"
  },
  "candle_cache_cleared_after_paxg": true
}
```

El apéndice PAXG verificó419040minutos de reloj completo e igualdad OHLCV con fuenteSpot;78840filas solapadas idénticas,340200añadidas,2808716históricas conservadas. SPX270634minutos observados,6minutos julio reconstruidos desde ticks del mismo proveedor. Ver addendum de datos y sus manifests. Conteos y fuentes verificados; cuatro conciliaciones contables pasaron con brecha terminal0. No cambios globales ni live/paper.
