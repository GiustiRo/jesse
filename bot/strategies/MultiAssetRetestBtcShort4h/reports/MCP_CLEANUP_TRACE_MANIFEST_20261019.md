# Limpieza MCP — manifiesto final

13workspaces temporales R8 terminados y eliminados únicamente después de13archivos permanentes guardados con éxito. Inventario de inputs+artefactos temporales:65.51MiB; archivos permanentes nuevos:6.02MiB. La diferencia aproximada59.50MiB es un saldo del inventario conocido, no una medición de disco libre. Cada archivo preserva auditoría, MTM mensual, paths de trades, metadatos y código/inputs de reproducción. CSV diarios/figuras temporales pueden regenerarse desde sesiones completas preservadas. No se borraron backtests, estrategias, velas ni informes. No se presupone causa del fallo MCP. Se reduce carga de futuras corridas y tamaño de consultas.

```json
{
  "archives": [
    {
      "batch": "V801",
      "job": "2c5b266bf19a422180c1c14b8e3206a0",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_V801_20261019.md",
      "size_bytes": 438661,
      "known_temporary_bytes": 5043929
    },
    {
      "batch": "X801",
      "job": "90dc2c2281d34b2a858e62cdc57d4b09",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_X801_20261019.md",
      "size_bytes": 523269,
      "known_temporary_bytes": 5641321
    },
    {
      "batch": "V802",
      "job": "2db618493b2b4e299b6efe84c609cb7a",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_V802_20261019.md",
      "size_bytes": 446059,
      "known_temporary_bytes": 5091804
    },
    {
      "batch": "X802",
      "job": "3c415386ccd245029ae5d51228e0b1e2",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_X802_20261019.md",
      "size_bytes": 478429,
      "known_temporary_bytes": 5329449
    },
    {
      "batch": "V803",
      "job": "d98bf412474840ceaeefc087880b3856",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_V803_20261019.md",
      "size_bytes": 443963,
      "known_temporary_bytes": 5086485
    },
    {
      "batch": "X803",
      "job": "86bb83956bb942d584fa13b706cb371f",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_X803_20261019.md",
      "size_bytes": 481644,
      "known_temporary_bytes": 5328411
    },
    {
      "batch": "V804",
      "job": "7f586b3ec7f84bb9bc8fbdfe28f03aed",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_V804_20261019.md",
      "size_bytes": 440702,
      "known_temporary_bytes": 5046979
    },
    {
      "batch": "X804",
      "job": "22acea68e8574c2f8b1a10b1b0e32e69",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_X804_20261019.md",
      "size_bytes": 510661,
      "known_temporary_bytes": 5537490
    },
    {
      "batch": "V805",
      "job": "ea4903ff2ffb4921a49b050ec8aabe60",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_V805_20261019.md",
      "size_bytes": 443965,
      "known_temporary_bytes": 5086359
    },
    {
      "batch": "X805",
      "job": "dc76be2c57b2461a91b319f4decacc99",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_X805_20261019.md",
      "size_bytes": 667037,
      "known_temporary_bytes": 6550255
    },
    {
      "batch": "Y901",
      "job": "26a008d34c3f402c8dbf5429e40afb1b",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_Y901_20261019.md",
      "size_bytes": 459909,
      "known_temporary_bytes": 4930352
    },
    {
      "batch": "Y902",
      "job": "b997bf717a4149b0b3c8a57ff0ba07ae",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_Y902_20261019.md",
      "size_bytes": 470092,
      "known_temporary_bytes": 4948204
    },
    {
      "batch": "Y903",
      "job": "aae5cdc6f7a64478a1ec82b5371fdb29",
      "path": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_Y903_20261019.md",
      "size_bytes": 503631,
      "known_temporary_bytes": 5074136
    }
  ],
  "deletions": [
    {
      "job": "2c5b266bf19a422180c1c14b8e3206a0",
      "batch": "V801",
      "deleted": true,
      "archive": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_V801_20261019.md"
    },
    {
      "job": "90dc2c2281d34b2a858e62cdc57d4b09",
      "batch": "X801",
      "deleted": true,
      "archive": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_X801_20261019.md"
    },
    {
      "job": "2db618493b2b4e299b6efe84c609cb7a",
      "batch": "V802",
      "deleted": true,
      "archive": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_V802_20261019.md"
    },
    {
      "job": "3c415386ccd245029ae5d51228e0b1e2",
      "batch": "X802",
      "deleted": true,
      "archive": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_X802_20261019.md"
    },
    {
      "job": "d98bf412474840ceaeefc087880b3856",
      "batch": "V803",
      "deleted": true,
      "archive": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_V803_20261019.md"
    },
    {
      "job": "86bb83956bb942d584fa13b706cb371f",
      "batch": "X803",
      "deleted": true,
      "archive": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_X803_20261019.md"
    },
    {
      "job": "7f586b3ec7f84bb9bc8fbdfe28f03aed",
      "batch": "V804",
      "deleted": true,
      "archive": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_V804_20261019.md"
    },
    {
      "job": "22acea68e8574c2f8b1a10b1b0e32e69",
      "batch": "X804",
      "deleted": true,
      "archive": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_X804_20261019.md"
    },
    {
      "job": "ea4903ff2ffb4921a49b050ec8aabe60",
      "batch": "V805",
      "deleted": true,
      "archive": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_V805_20261019.md"
    },
    {
      "job": "dc76be2c57b2461a91b319f4decacc99",
      "batch": "X805",
      "deleted": true,
      "archive": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_X805_20261019.md"
    },
    {
      "job": "26a008d34c3f402c8dbf5429e40afb1b",
      "batch": "Y901",
      "deleted": true,
      "archive": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_Y901_20261019.md"
    },
    {
      "job": "b997bf717a4149b0b3c8a57ff0ba07ae",
      "batch": "Y902",
      "deleted": true,
      "archive": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_Y902_20261019.md"
    },
    {
      "job": "aae5cdc6f7a64478a1ec82b5371fdb29",
      "batch": "Y903",
      "deleted": true,
      "archive": "strategies/MultiAssetRetestBtcShort4h/reports/ARCHIVE_R8_Y903_20261019.md"
    }
  ],
  "known_temporary_bytes": 68695174,
  "permanent_archive_bytes": 6308022,
  "preserved": [
    "all backtest sessions/trades/orders/strategy snapshots",
    "all strategy sources including failed research",
    "all candles",
    "all previous reports",
    "all R9 workspaces used for pending audits"
  ],
  "causality": "The transient workspace count/size is not proven to cause MCP nonJSON errors.",
  "operating_change": "Maximum2concurrentbacktests globally; maximum1analysis; small session-list pages, summaryfirst, no whole sessions unless required."
}
```
