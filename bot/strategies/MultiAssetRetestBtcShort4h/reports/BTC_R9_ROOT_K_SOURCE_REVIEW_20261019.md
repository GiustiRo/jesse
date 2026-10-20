# R9 — revisión root de variantes K

Revisión previa a backtests. Las cinco fuentes económicas corresponden al addendum congelado. Se corrigió sólo el nombre de clase antes de crearla, tras detectar sustitución global de Y902 dentro de classname. QA del agente230PASS (fixtures, AST, guards, relojes). Root confirma métodos protegidos, fórmula de entrada K1001/2 y on_open sin modificaciones fuera del suplemento en K1003/4/5; update_position usa deadline primero, fullbar y reloj idempotente. K1004 es transporte de un mecanismo previamente desfavorable en entrada MARKET para probar interacción con entrada STOP. No es una señal independiente nueva. K1005 trailing estructural persistente tras cierre1R, usando máximo de vela anterior conocido y stopválido precio<SLnuevo<SLactual.

```json
{
  "BtcY902ExploreR1001": {
    "changed": [
      "before"
    ],
    "methods": 26
  },
  "BtcY902ExploreR1002": {
    "changed": [
      "before"
    ],
    "methods": 26
  },
  "BtcY902ExploreR1003": {
    "changed": [
      "on_open_position",
      "update_position"
    ],
    "methods": 27
  },
  "BtcY902ExploreR1004": {
    "changed": [
      "on_open_position",
      "update_position"
    ],
    "methods": 27
  },
  "BtcY902ExploreR1005": {
    "changed": [
      "on_open_position",
      "update_position"
    ],
    "methods": 27
  }
}
```
