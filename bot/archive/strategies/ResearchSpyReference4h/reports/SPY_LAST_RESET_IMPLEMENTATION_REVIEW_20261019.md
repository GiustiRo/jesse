# SPY LAST RESET — seis fuentes y diffs para revisión root

Protocolo SPY_LAST_RESET_PROTOCOL_20261019.md guardado antes de código/resultados; snapshot completo de base en SPY_LAST_RESET_BASE_SNAPSHOT_20261019.md. Seis fuentes autocontenidas creadas por MCP y readback exacto6/6. Normalizar sólo nombredeclase y bloqueRESET devuelve byte-a-byte la base completa en las seis. BaseBR02 actual permanece intacta; no se editó ninguna fuenteR1.

## Bloque original sustituido

```python
            # Left-censored epoch remains ineligible until a reset is observed.
            n = int(self.hp['donchian_len'])
            if len(c) >= n + 1:
                upper = float(np.max(c[-n-1:-1, 3]))
                lower = float(np.min(c[-n-1:-1, 4]))
                if math.isfinite(upper) and math.isfinite(lower) and self.price <= (upper + lower) / 2:
                    self.vars.update(epoch_seen=True, epoch_count=0)

```

## SpyLastReset01

```python
            # Left-censored epoch remains ineligible until a reset is observed.
            n = 20  # Reset horizon only; entry Donchian remains26.
            if len(c) >= n + 1:
                upper = float(np.max(c[-n-1:-1, 3]))
                lower = float(np.min(c[-n-1:-1, 4]))
                if math.isfinite(upper) and math.isfinite(lower) and self.price <= (upper + lower) / 2:
                    self.vars.update(epoch_seen=True, epoch_count=0)

```

## SpyLastReset02

```python
            # Left-censored epoch remains ineligible until a reset is observed.
            n = 32  # Reset horizon only; entry Donchian remains26.
            if len(c) >= n + 1:
                upper = float(np.max(c[-n-1:-1, 3]))
                lower = float(np.min(c[-n-1:-1, 4]))
                if math.isfinite(upper) and math.isfinite(lower) and self.price <= (upper + lower) / 2:
                    self.vars.update(epoch_seen=True, epoch_count=0)

```

## SpyLastReset03

```python
            # Left-censored epoch remains ineligible until a reset is observed.
            n = int(self.hp['donchian_len'])
            if len(c) >= n + 1:
                upper = float(np.max(c[-n-1:-1, 3]))
                lower = float(np.min(c[-n-1:-1, 4]))
                if math.isfinite(upper) and math.isfinite(lower) and self.price <= lower + 0.4 * (upper - lower):
                    self.vars.update(epoch_seen=True, epoch_count=0)

```

## SpyLastReset04

```python
            # Left-censored epoch remains ineligible until a reset is observed.
            n = int(self.hp['donchian_len'])
            if len(c) >= n + 1:
                upper = float(np.max(c[-n-1:-1, 3]))
                lower = float(np.min(c[-n-1:-1, 4]))
                if math.isfinite(upper) and math.isfinite(lower) and self.price <= lower + 0.6 * (upper - lower):
                    self.vars.update(epoch_seen=True, epoch_count=0)

```

## SpyLastReset05

```python
            # Two consecutive OBSERVED filtered closes, each using its own prior channel.
            n = int(self.hp['donchian_len'])
            if len(c) >= n + 1:
                upper = float(np.max(c[-n-1:-1, 3]))
                lower = float(np.min(c[-n-1:-1, 4]))
                below = (math.isfinite(upper) and math.isfinite(lower)
                         and self.price <= (upper + lower) / 2)
                streak = self.vars.get('reset_streak', 0) + 1 if below else 0
                self.vars['reset_streak'] = streak
                if streak >= 2:
                    self.vars.update(epoch_seen=True, epoch_count=0)

```

## SpyLastReset06

```python
            # Same causal EMA20 as the regime; reset does not require entry eligibility.
            n = int(self.hp['donchian_len'])
            if len(c) >= n + 1:
                fast_reset = float(ta.ema(c, period=int(self.hp['ema_fast'])))
                if math.isfinite(fast_reset) and self.price <= fast_reset:
                    self.vars.update(epoch_seen=True, epoch_count=0)

```

## Readbacks y prueba de delta exhaustivo

```json
[
  {
    "name": "SpyLastReset01",
    "readback_exact": true,
    "only_class_and_reset_delta": true,
    "entry_hp_donchian26": true,
    "BR_MODE2": true,
    "chars": 17372
  },
  {
    "name": "SpyLastReset02",
    "readback_exact": true,
    "only_class_and_reset_delta": true,
    "entry_hp_donchian26": true,
    "BR_MODE2": true,
    "chars": 17372
  },
  {
    "name": "SpyLastReset03",
    "readback_exact": true,
    "only_class_and_reset_delta": true,
    "entry_hp_donchian26": true,
    "BR_MODE2": true,
    "chars": 17359
  },
  {
    "name": "SpyLastReset04",
    "readback_exact": true,
    "only_class_and_reset_delta": true,
    "entry_hp_donchian26": true,
    "BR_MODE2": true,
    "chars": 17359
  },
  {
    "name": "SpyLastReset05",
    "readback_exact": true,
    "only_class_and_reset_delta": true,
    "entry_hp_donchian26": true,
    "BR_MODE2": true,
    "chars": 17551
  },
  {
    "name": "SpyLastReset06",
    "readback_exact": true,
    "only_class_and_reset_delta": true,
    "entry_hp_donchian26": true,
    "BR_MODE2": true,
    "chars": 17302
  }
]
```

Todos los demás métodos/constantes/HP/estado ordinal/origen/sizing/gestión/fresh y calendario están idénticos por normalizaciónexhaustiva. RESET01/02 cambian sólo nLOCAL delreset; _context yHPentry siguen26. RESET05 actualiza racha en cada barrafiltradaactual; entrywindow/fresh/posición no condicionanreset. Offsession no entra enbefore yno toca racha; última candle filtrada stale tampoco. RESET06taEMA20decontexto causal se recalcula conmisma llamada para no modificar _context ni añadir gates de origen; guardlen>=27original permanece.

Seisestrategias guardadas en strategies/SpyLastReset01..06/__init__.py. No drafts/runs todavía. Revisiónrootantesdeejecución, sin R3 ni pruebas extra.