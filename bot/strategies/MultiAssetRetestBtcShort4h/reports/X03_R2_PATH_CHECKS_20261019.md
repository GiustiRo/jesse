# X03 R2 — recorrido de operaciones ejecutadas

Comparación con X03 original: clave única símbolo/lado/timestamp de entrada. Los recuentos son descriptivos; no atribuyen beneficio causal porque cantidades y capital compartido cambian.

En 20 de las 21 fuentes nominales, los 31 longs BTC originales retienen sus timestamps de entrada y salida. La excepción es V207 (retraso fuerte): sólo30/31 se retienen y aparecen dos longs nuevos,32 en total. El código de longs sigue idéntico; la ocupación de la ruta cambia el recorrido. La prueba de que la lógica original es inmutable no implica operaciones idénticas.

N201 y N202 producen exactamente el mismo recorrido ejecutado completo en B y C, con igualdad de todos los campos extraídos, incluidos cantidades, comisiones y PNL. Dos recetas no son dos evidencias independientes. No se añadieron variantes de rescate.

En CONF5 frente a N204 nominal, los223trades BTC y12/19SPY conservan todas las entradas y salidas. PAXG38→39 y36/38salidas coinciden; el fee entra en el BE y afecta gestión, además de cantidades y capital. La comparación principal contra X03 se mantiene abajo por consistencia; la comparación específica CONF5/N204 se añade aparte.

```json
{
  "versus_X03": {
    "FEE5B": {
      "counts": {
        "current": 274,
        "reference": 273,
        "retained": 273,
        "removed": 0,
        "added": 1
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 271,
      "identical_to_N201": null
    },
    "FEE5C": {
      "counts": {
        "current": 281,
        "reference": 280,
        "retained": 280,
        "removed": 0,
        "added": 1
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 278,
      "identical_to_N201": null
    },
    "N201B": {
      "counts": {
        "current": 236,
        "reference": 273,
        "retained": 212,
        "removed": 61,
        "added": 24
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 212,
      "identical_to_N201": null
    },
    "N201C": {
      "counts": {
        "current": 243,
        "reference": 280,
        "retained": 219,
        "removed": 61,
        "added": 24
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 219,
      "identical_to_N201": null
    },
    "V201B": {
      "counts": {
        "current": 294,
        "reference": 273,
        "retained": 214,
        "removed": 59,
        "added": 80
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 214,
      "identical_to_N201": null
    },
    "V201C": {
      "counts": {
        "current": 301,
        "reference": 280,
        "retained": 221,
        "removed": 59,
        "added": 80
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 221,
      "identical_to_N201": null
    },
    "K201B": {
      "counts": {
        "current": 271,
        "reference": 273,
        "retained": 271,
        "removed": 2,
        "added": 0
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 271,
      "identical_to_N201": null
    },
    "K201C": {
      "counts": {
        "current": 278,
        "reference": 280,
        "retained": 278,
        "removed": 2,
        "added": 0
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 278,
      "identical_to_N201": null
    },
    "N202B": {
      "counts": {
        "current": 236,
        "reference": 273,
        "retained": 212,
        "removed": 61,
        "added": 24
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 212,
      "identical_to_N201": true
    },
    "N202C": {
      "counts": {
        "current": 243,
        "reference": 280,
        "retained": 219,
        "removed": 61,
        "added": 24
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 219,
      "identical_to_N201": true
    },
    "N203B": {
      "counts": {
        "current": 267,
        "reference": 273,
        "retained": 240,
        "removed": 33,
        "added": 27
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 240,
      "identical_to_N201": null
    },
    "N203C": {
      "counts": {
        "current": 274,
        "reference": 280,
        "retained": 247,
        "removed": 33,
        "added": 27
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 247,
      "identical_to_N201": null
    },
    "NOX5B": {
      "counts": {
        "current": 207,
        "reference": 273,
        "retained": 193,
        "removed": 80,
        "added": 14
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 191,
      "identical_to_N201": null
    },
    "NOX5C": {
      "counts": {
        "current": 214,
        "reference": 280,
        "retained": 200,
        "removed": 80,
        "added": 14
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 198,
      "identical_to_N201": null
    },
    "V202B": {
      "counts": {
        "current": 252,
        "reference": 273,
        "retained": 218,
        "removed": 55,
        "added": 34
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 218
    },
    "V202C": {
      "counts": {
        "current": 259,
        "reference": 280,
        "retained": 225,
        "removed": 55,
        "added": 34
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 225
    },
    "N204B": {
      "counts": {
        "current": 273,
        "reference": 273,
        "retained": 256,
        "removed": 17,
        "added": 17
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 256
    },
    "N204C": {
      "counts": {
        "current": 280,
        "reference": 280,
        "retained": 263,
        "removed": 17,
        "added": 17
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 263
    },
    "K202B": {
      "counts": {
        "current": 236,
        "reference": 273,
        "retained": 194,
        "removed": 79,
        "added": 42
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 194
    },
    "K202C": {
      "counts": {
        "current": 243,
        "reference": 280,
        "retained": 201,
        "removed": 79,
        "added": 42
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 201
    },
    "N205B": {
      "counts": {
        "current": 265,
        "reference": 273,
        "retained": 263,
        "removed": 10,
        "added": 2
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 263
    },
    "N205C": {
      "counts": {
        "current": 272,
        "reference": 280,
        "retained": 270,
        "removed": 10,
        "added": 2
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 270
    },
    "V203B": {
      "counts": {
        "current": 276,
        "reference": 273,
        "retained": 272,
        "removed": 1,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 252
    },
    "V203C": {
      "counts": {
        "current": 283,
        "reference": 280,
        "retained": 279,
        "removed": 1,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 259
    },
    "N206B": {
      "counts": {
        "current": 210,
        "reference": 273,
        "retained": 199,
        "removed": 74,
        "added": 11
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 199
    },
    "N206C": {
      "counts": {
        "current": 217,
        "reference": 280,
        "retained": 206,
        "removed": 74,
        "added": 11
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 206
    },
    "K203B": {
      "counts": {
        "current": 248,
        "reference": 273,
        "retained": 193,
        "removed": 80,
        "added": 55
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 193
    },
    "K203C": {
      "counts": {
        "current": 255,
        "reference": 280,
        "retained": 200,
        "removed": 80,
        "added": 55
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 200
    },
    "N207B": {
      "counts": {
        "current": 257,
        "reference": 273,
        "retained": 255,
        "removed": 18,
        "added": 2
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 255
    },
    "N207C": {
      "counts": {
        "current": 264,
        "reference": 280,
        "retained": 262,
        "removed": 18,
        "added": 2
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 262
    },
    "V204B": {
      "counts": {
        "current": 272,
        "reference": 273,
        "retained": 272,
        "removed": 1,
        "added": 0
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 257
    },
    "V204C": {
      "counts": {
        "current": 279,
        "reference": 280,
        "retained": 279,
        "removed": 1,
        "added": 0
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 264
    },
    "N208B": {
      "counts": {
        "current": 278,
        "reference": 273,
        "retained": 273,
        "removed": 0,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 234
    },
    "N208C": {
      "counts": {
        "current": 285,
        "reference": 280,
        "retained": 280,
        "removed": 0,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 241
    },
    "K204B": {
      "counts": {
        "current": 272,
        "reference": 273,
        "retained": 272,
        "removed": 1,
        "added": 0
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 258
    },
    "K204C": {
      "counts": {
        "current": 279,
        "reference": 280,
        "retained": 279,
        "removed": 1,
        "added": 0
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 265
    },
    "N209B": {
      "counts": {
        "current": 277,
        "reference": 273,
        "retained": 273,
        "removed": 0,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 225
    },
    "N209C": {
      "counts": {
        "current": 284,
        "reference": 280,
        "retained": 280,
        "removed": 0,
        "added": 4
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 232
    },
    "V205B": {
      "counts": {
        "current": 278,
        "reference": 273,
        "retained": 273,
        "removed": 0,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 223
    },
    "V205C": {
      "counts": {
        "current": 285,
        "reference": 280,
        "retained": 280,
        "removed": 0,
        "added": 5
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 230
    },
    "N210B": {
      "counts": {
        "current": 273,
        "reference": 273,
        "retained": 273,
        "removed": 0,
        "added": 0
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 266
    },
    "N210C": {
      "counts": {
        "current": 280,
        "reference": 280,
        "retained": 280,
        "removed": 0,
        "added": 0
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 273
    },
    "V206B": {
      "counts": {
        "current": 267,
        "reference": 273,
        "retained": 267,
        "removed": 6,
        "added": 0
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 230
    },
    "V206C": {
      "counts": {
        "current": 274,
        "reference": 280,
        "retained": 274,
        "removed": 6,
        "added": 0
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 237
    },
    "CONF5B": {
      "counts": {
        "current": 274,
        "reference": 273,
        "retained": 256,
        "removed": 17,
        "added": 18
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 254
    },
    "CONF5C": {
      "counts": {
        "current": 281,
        "reference": 280,
        "retained": 263,
        "removed": 17,
        "added": 18
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 31,
        "same_exit": 31
      },
      "same_exit_retained": 261
    },
    "V207B": {
      "counts": {
        "current": 272,
        "reference": 273,
        "retained": 192,
        "removed": 81,
        "added": 80
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 30,
        "same_exit": 30
      },
      "same_exit_retained": 192
    },
    "V207C": {
      "counts": {
        "current": 279,
        "reference": 280,
        "retained": 199,
        "removed": 81,
        "added": 80
      },
      "btc_long": {
        "reference": 31,
        "retained_entry": 30,
        "same_exit": 30
      },
      "same_exit_retained": 199
    }
  },
  "CONF5_versus_N204_nominal": {
    "B": {
      "BTC-USDT": {
        "nominal": 223,
        "enginefee": 223,
        "same_entry": 223,
        "same_entry_and_exit": 223
      },
      "PAXG-USDT": {
        "nominal": 38,
        "enginefee": 39,
        "same_entry": 38,
        "same_entry_and_exit": 36
      },
      "SPY-USDT": {
        "nominal": 12,
        "enginefee": 12,
        "same_entry": 12,
        "same_entry_and_exit": 12
      }
    },
    "C": {
      "BTC-USDT": {
        "nominal": 223,
        "enginefee": 223,
        "same_entry": 223,
        "same_entry_and_exit": 223
      },
      "PAXG-USDT": {
        "nominal": 38,
        "enginefee": 39,
        "same_entry": 38,
        "same_entry_and_exit": 36
      },
      "SPY-USDT": {
        "nominal": 19,
        "enginefee": 19,
        "same_entry": 19,
        "same_entry_and_exit": 19
      }
    }
  }
}
```