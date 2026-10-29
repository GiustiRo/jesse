# R60: revisión raíz de fuentes antes de ejecutar

Root leyó las veinte fuentes completas por MCP y comparó sus métodos con las bases actuales. Las tres bases coinciden exactamente con las fuentes revisadas en atribución. Tras normalizar clase y únicamente el método cambiado, las veinte fuentes recuperan exactamente su base. No hay otros cambios de imports, constantes, atributos o métodos.

S01–S04 sólo cambian el predicado de distancia normalizada en _plan; S05–S10 sólo el default declarado en hyperparameters. En PAXG, las diez cambian sólo un default de hyperparameters y un comentario que identifica el contexto; las políticas Cq/M mantienen las diferencias originales de entrada. No se modifica gestión, sizing, ledger, cancelación, riesgo o calendario.

El protocolo global R60_SPY_PAXG_FROZEN_PROTOCOL_20261019.md se guardó antes de los resultados. Se autorizaron las colas después de revisar cada activo: dos runs por especialista y cuatro globales; un análisis por especialista y dos globales. Exactamente diez configuraciones nuevas por activo, sin otra ejecución de referencias. La verificación de snapshots y formularios se añadirá al completar.

```json
[
  {
    "name": "R60SpyGapMin10",
    "normalizedExact": true,
    "changed": [
      "_plan"
    ]
  },
  {
    "name": "R60SpyGapMin25",
    "normalizedExact": true,
    "changed": [
      "_plan"
    ]
  },
  {
    "name": "R60SpyGapMax50",
    "normalizedExact": true,
    "changed": [
      "_plan"
    ]
  },
  {
    "name": "R60SpyGapMax75",
    "normalizedExact": true,
    "changed": [
      "_plan"
    ]
  },
  {
    "name": "R60SpyN24",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60SpyN28",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60SpyAdx24",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60SpyAdx28",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60SpyFast16",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60SpyFast24",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60PaxgN24Retest4h",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60PaxgN24Market4h",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60PaxgN28Retest4h",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60PaxgN28Market4h",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60PaxgAdx24Retest4h",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60PaxgAdx24Market4h",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60PaxgAdx28Retest4h",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60PaxgAdx28Market4h",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60PaxgFast24Retest4h",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  },
  {
    "name": "R60PaxgFast24Market4h",
    "normalizedExact": true,
    "changed": [
      "hyperparameters"
    ]
  }
]
```

## Verificación final de ejecución

Las20 sesiones están finished. Root cotejó strategy_codes con las20 fuentes revisadas: igualdad exacta. Formularios: fechas/rutas/símbolo M1/4h/capital10k/fee.00045/isolated5x/warmup240/fastfalse/debugfalse correctos. También recuperó por MCP los8 hiperparámetros registrados de cada ejecución, incluyendo DNA vacío, y verificó sus valores efectivos contra la matriz. Así, la identidad de resultados de varios vecinos SPY no se atribuye a que no se haya aplicado el cambio. No hubo cambios de fuentes tras resultados.

Las20 sesiones están cubiertas por MTM independiente y todos los terminales concilian. Sin nuevas rutas BTC, histórico, funding, instalaciones, cambios de framework/configuración global o live/paper/Pi.

```json
{
  "snapshots": [
    {
      "session_id": "09fa1c9a-d363-47ee-bfb9-522a9e13ba14",
      "name": "R60PaxgFast24Market4h",
      "dashboard_url": "http://localhost:9200/#/backtest/09fa1c9a-d363-47ee-bfb9-522a9e13ba14",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "9a272836-5fd1-471f-b6d1-17a7d0d0b55e",
      "name": "R60PaxgFast24Retest4h",
      "dashboard_url": "http://localhost:9200/#/backtest/9a272836-5fd1-471f-b6d1-17a7d0d0b55e",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "2c562667-f6cc-498b-932b-2983bc41b7dd",
      "name": "R60PaxgAdx28Retest4h",
      "dashboard_url": "http://localhost:9200/#/backtest/2c562667-f6cc-498b-932b-2983bc41b7dd",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "ac0ed1df-254d-4d7d-9fc1-ce5656107504",
      "name": "R60PaxgAdx28Market4h",
      "dashboard_url": "http://localhost:9200/#/backtest/ac0ed1df-254d-4d7d-9fc1-ce5656107504",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "92ac3dc0-e141-4977-b31f-185499127c3c",
      "name": "R60PaxgAdx24Market4h",
      "dashboard_url": "http://localhost:9200/#/backtest/92ac3dc0-e141-4977-b31f-185499127c3c",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "b51a2052-0e26-47d4-bbe3-45013f196248",
      "name": "R60PaxgAdx24Retest4h",
      "dashboard_url": "http://localhost:9200/#/backtest/b51a2052-0e26-47d4-bbe3-45013f196248",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "84eb15ef-1a1d-4621-b21f-fcd09bb4989f",
      "name": "R60SpyFast16",
      "dashboard_url": "http://localhost:9200/#/backtest/84eb15ef-1a1d-4621-b21f-fcd09bb4989f",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "333221fd-d6ed-462d-87eb-2eb255bbc50a",
      "name": "R60SpyFast24",
      "dashboard_url": "http://localhost:9200/#/backtest/333221fd-d6ed-462d-87eb-2eb255bbc50a",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a",
      "name": "R60PaxgN28Market4h",
      "dashboard_url": "http://localhost:9200/#/backtest/98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "62b6dc3e-2dc7-4612-90ca-935242ed8936",
      "name": "R60PaxgN28Retest4h",
      "dashboard_url": "http://localhost:9200/#/backtest/62b6dc3e-2dc7-4612-90ca-935242ed8936",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "60d1237b-6b7a-435b-ae6d-fa1103205b60",
      "name": "R60SpyAdx24",
      "dashboard_url": "http://localhost:9200/#/backtest/60d1237b-6b7a-435b-ae6d-fa1103205b60",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "19be9941-b9e5-4709-8ff4-29f0c5bbdefb",
      "name": "R60SpyAdx28",
      "dashboard_url": "http://localhost:9200/#/backtest/19be9941-b9e5-4709-8ff4-29f0c5bbdefb",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "d2fcc787-b228-49d3-be41-0c3f657fd2bb",
      "name": "R60PaxgN24Market4h",
      "dashboard_url": "http://localhost:9200/#/backtest/d2fcc787-b228-49d3-be41-0c3f657fd2bb",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "39964cd7-d0e4-4684-9261-01ccad239e26",
      "name": "R60PaxgN24Retest4h",
      "dashboard_url": "http://localhost:9200/#/backtest/39964cd7-d0e4-4684-9261-01ccad239e26",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "8bae70a3-ab31-4fc5-9905-c65023b03134",
      "name": "R60SpyN24",
      "dashboard_url": "http://localhost:9200/#/backtest/8bae70a3-ab31-4fc5-9905-c65023b03134",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "2327e98c-4c6d-4a70-b54d-75646cdd82c2",
      "name": "R60SpyN28",
      "dashboard_url": "http://localhost:9200/#/backtest/2327e98c-4c6d-4a70-b54d-75646cdd82c2",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "89d81c40-6ccc-43c8-b3c4-3326a94a3b35",
      "name": "R60SpyGapMax75",
      "dashboard_url": "http://localhost:9200/#/backtest/89d81c40-6ccc-43c8-b3c4-3326a94a3b35",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e",
      "name": "R60SpyGapMax50",
      "dashboard_url": "http://localhost:9200/#/backtest/9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "d404c47e-025a-4789-b1a8-b054402f6c21",
      "name": "R60SpyGapMin10",
      "dashboard_url": "http://localhost:9200/#/backtest/d404c47e-025a-4789-b1a8-b054402f6c21",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    },
    {
      "session_id": "cd61d362-4b1c-4793-80b7-e85a9494edae",
      "name": "R60SpyGapMin25",
      "dashboard_url": "http://localhost:9200/#/backtest/cd61d362-4b1c-4793-80b7-e85a9494edae",
      "status": "finished",
      "sourceExact": true,
      "formExact": true
    }
  ],
  "recorded_hyperparameters": [
    {
      "name": "R60PaxgFast24Market4h",
      "session_id": "09fa1c9a-d363-47ee-bfb9-522a9e13ba14",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 24,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60PaxgFast24Retest4h",
      "session_id": "9a272836-5fd1-471f-b6d1-17a7d0d0b55e",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 24,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60PaxgAdx28Retest4h",
      "session_id": "2c562667-f6cc-498b-932b-2983bc41b7dd",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 28,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60PaxgAdx28Market4h",
      "session_id": "ac0ed1df-254d-4d7d-9fc1-ce5656107504",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 28,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60PaxgAdx24Market4h",
      "session_id": "92ac3dc0-e141-4977-b31f-185499127c3c",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 24,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60PaxgAdx24Retest4h",
      "session_id": "b51a2052-0e26-47d4-bbe3-45013f196248",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 24,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60SpyFast16",
      "session_id": "84eb15ef-1a1d-4621-b21f-fcd09bb4989f",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 16,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60SpyFast24",
      "session_id": "333221fd-d6ed-462d-87eb-2eb255bbc50a",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 24,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60PaxgN28Market4h",
      "session_id": "98f0d7d6-d7a3-4188-ba27-1f45e9f7a48a",
      "recorded": {
        "DNA": "",
        "donchian_len": 28,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60PaxgN28Retest4h",
      "session_id": "62b6dc3e-2dc7-4612-90ca-935242ed8936",
      "recorded": {
        "DNA": "",
        "donchian_len": 28,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60SpyAdx24",
      "session_id": "60d1237b-6b7a-435b-ae6d-fa1103205b60",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 24,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60SpyAdx28",
      "session_id": "19be9941-b9e5-4709-8ff4-29f0c5bbdefb",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 28,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60PaxgN24Market4h",
      "session_id": "d2fcc787-b228-49d3-be41-0c3f657fd2bb",
      "recorded": {
        "DNA": "",
        "donchian_len": 24,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60PaxgN24Retest4h",
      "session_id": "39964cd7-d0e4-4684-9261-01ccad239e26",
      "recorded": {
        "DNA": "",
        "donchian_len": 24,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60SpyN24",
      "session_id": "8bae70a3-ab31-4fc5-9905-c65023b03134",
      "recorded": {
        "DNA": "",
        "donchian_len": 24,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60SpyN28",
      "session_id": "2327e98c-4c6d-4a70-b54d-75646cdd82c2",
      "recorded": {
        "DNA": "",
        "donchian_len": 28,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60SpyGapMax75",
      "session_id": "89d81c40-6ccc-43c8-b3c4-3326a94a3b35",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60SpyGapMax50",
      "session_id": "9c9d037d-e9f9-42d9-af5c-7c0e3bb5a46e",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60SpyGapMin10",
      "session_id": "d404c47e-025a-4789-b1a8-b054402f6c21",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    },
    {
      "name": "R60SpyGapMin25",
      "session_id": "cd61d362-4b1c-4793-80b7-e85a9494edae",
      "recorded": {
        "DNA": "",
        "donchian_len": 26,
        "ema_fast": 20,
        "ema_slow": 80,
        "adx_min": 26,
        "stop_atr": 2,
        "trail_atr": 4.2,
        "be_r": 2.25
      },
      "pass": true
    }
  ]
}
```
