# R60 PAXG: fuentes y diferencias para revisión previa

Diez clases autocontenidas creadas; readback completo exacto10/10. Ningún R60 PAXG lanzado. Bases actuales coinciden con sus snapshots de atribución. Cambia sólo hyperparameters: un default por clase, nombre y comentario de trazabilidad. Restituir esos cambios devuelve cada base byte por byte. _plan, fresh guard searchsorted, gestión, sizing/ledger/hooks no cambian. Min/max no se usan en optimización.

Protocolo: strategies/AttrPaxgC0Retest4h/reports/R60_PAXG_PROTOCOL_20261019.md. Bases: AttrPaxgCqFreshRetest4h y AttrPaxgMMarketSignal4h, verificadas contra sesiones0fc6e1f7.../8b43d9d2... en MCP antes de generar.

## Prueba mecánica

```json
[
  {
    "id": "P1_Cq",
    "name": "R60PaxgN24Retest4h",
    "base": "AttrPaxgCqFreshRetest4h",
    "parameter": "donchian_len",
    "old": 26,
    "new": 24,
    "restorationExact": true,
    "readbackExact": true
  },
  {
    "id": "P1_M",
    "name": "R60PaxgN24Market4h",
    "base": "AttrPaxgMMarketSignal4h",
    "parameter": "donchian_len",
    "old": 26,
    "new": 24,
    "restorationExact": true,
    "readbackExact": true
  },
  {
    "id": "P2_Cq",
    "name": "R60PaxgN28Retest4h",
    "base": "AttrPaxgCqFreshRetest4h",
    "parameter": "donchian_len",
    "old": 26,
    "new": 28,
    "restorationExact": true,
    "readbackExact": true
  },
  {
    "id": "P2_M",
    "name": "R60PaxgN28Market4h",
    "base": "AttrPaxgMMarketSignal4h",
    "parameter": "donchian_len",
    "old": 26,
    "new": 28,
    "restorationExact": true,
    "readbackExact": true
  },
  {
    "id": "P3_Cq",
    "name": "R60PaxgAdx24Retest4h",
    "base": "AttrPaxgCqFreshRetest4h",
    "parameter": "adx_min",
    "old": 26,
    "new": 24,
    "restorationExact": true,
    "readbackExact": true
  },
  {
    "id": "P3_M",
    "name": "R60PaxgAdx24Market4h",
    "base": "AttrPaxgMMarketSignal4h",
    "parameter": "adx_min",
    "old": 26,
    "new": 24,
    "restorationExact": true,
    "readbackExact": true
  },
  {
    "id": "P4_Cq",
    "name": "R60PaxgAdx28Retest4h",
    "base": "AttrPaxgCqFreshRetest4h",
    "parameter": "adx_min",
    "old": 26,
    "new": 28,
    "restorationExact": true,
    "readbackExact": true
  },
  {
    "id": "P4_M",
    "name": "R60PaxgAdx28Market4h",
    "base": "AttrPaxgMMarketSignal4h",
    "parameter": "adx_min",
    "old": 26,
    "new": 28,
    "restorationExact": true,
    "readbackExact": true
  },
  {
    "id": "P5_Cq",
    "name": "R60PaxgFast24Retest4h",
    "base": "AttrPaxgCqFreshRetest4h",
    "parameter": "ema_fast",
    "old": 20,
    "new": 24,
    "restorationExact": true,
    "readbackExact": true
  },
  {
    "id": "P5_M",
    "name": "R60PaxgFast24Market4h",
    "base": "AttrPaxgMMarketSignal4h",
    "parameter": "ema_fast",
    "old": 20,
    "new": 24,
    "restorationExact": true,
    "readbackExact": true
  }
]
```

## Diffs completos de defaults

### R60PaxgN24Retest4h

Método único alterado: hyperparameters().

```diff
-            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},
+            # R60 P1: predeclared single-default sensitivity, not optimization.
+            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 24},
```

### R60PaxgN24Market4h

Método único alterado: hyperparameters().

```diff
-            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},
+            # R60 P1: predeclared single-default sensitivity, not optimization.
+            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 24},
```

### R60PaxgN28Retest4h

Método único alterado: hyperparameters().

```diff
-            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},
+            # R60 P2: predeclared single-default sensitivity, not optimization.
+            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 28},
```

### R60PaxgN28Market4h

Método único alterado: hyperparameters().

```diff
-            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},
+            # R60 P2: predeclared single-default sensitivity, not optimization.
+            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 28},
```

### R60PaxgAdx24Retest4h

Método único alterado: hyperparameters().

```diff
-            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},
+            # R60 P3: predeclared single-default sensitivity, not optimization.
+            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 24},
```

### R60PaxgAdx24Market4h

Método único alterado: hyperparameters().

```diff
-            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},
+            # R60 P3: predeclared single-default sensitivity, not optimization.
+            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 24},
```

### R60PaxgAdx28Retest4h

Método único alterado: hyperparameters().

```diff
-            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},
+            # R60 P4: predeclared single-default sensitivity, not optimization.
+            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 28},
```

### R60PaxgAdx28Market4h

Método único alterado: hyperparameters().

```diff
-            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},
+            # R60 P4: predeclared single-default sensitivity, not optimization.
+            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 28},
```

### R60PaxgFast24Retest4h

Método único alterado: hyperparameters().

```diff
-            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},
+            # R60 P5: predeclared single-default sensitivity, not optimization.
+            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 24},
```

### R60PaxgFast24Market4h

Método único alterado: hyperparameters().

```diff
-            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},
+            # R60 P5: predeclared single-default sensitivity, not optimization.
+            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 24},
```

Cada archivo completo reside en strategies/<nombre>/__init__.py y es autocontenido. No módulo común externo. Base Cq LIMIT a frontera; base M valida frontera antes de repricing al cierre. No otro cambio ni nuevos datos. Pendiente revisión/autorización root antes de los dos primeros runs.
