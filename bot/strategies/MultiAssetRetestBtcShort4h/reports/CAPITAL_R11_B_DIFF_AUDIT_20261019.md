# R11 B — auditoría de cambios

Se invirtieron mecánicamente únicamente las transformaciones permitidas (nombre/comentario, constantes R5A15 o inserciones de cap/helper M5A15). Las diez fuentes reconstruidas coinciden byte por byte con sus fuentes originales. La sintaxis fue aceptada por create_strategy y las diez fuentes guardadas coinciden exactamente tras read_strategy.

```json
[
  {
    "name": "CapitalR11K1001R5A15",
    "only_intended_changes": true
  },
  {
    "name": "CapitalR11N204R5A15",
    "only_intended_changes": true
  },
  {
    "name": "CapitalR11PaxgR5A15",
    "only_intended_changes": true
  },
  {
    "name": "CapitalR11SpyBR5A15",
    "only_intended_changes": true
  },
  {
    "name": "CapitalR11SpyCR5A15",
    "only_intended_changes": true
  },
  {
    "name": "CapitalR11K1001M5A15",
    "only_intended_changes": true
  },
  {
    "name": "CapitalR11N204M5A15",
    "only_intended_changes": true
  },
  {
    "name": "CapitalR11PaxgM5A15",
    "only_intended_changes": true
  },
  {
    "name": "CapitalR11SpyBM5A15",
    "only_intended_changes": true
  },
  {
    "name": "CapitalR11SpyCM5A15",
    "only_intended_changes": true
  }
]
```

No sustituye ejecución del motor ni prueba de equivalencia live. No se ejecutaron herramientas locales ni se instalaron dependencias.