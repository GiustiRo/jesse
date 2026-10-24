# R6 — revisión independiente de matriz, puertas y selección

Revisor: btc_capacity_r6. Leídos por MCP el protocolo congelado y la matriz completa strategies/MultiAssetRetestBtcShort4h/reports/N503_R6_RESULTS_MATRIX_20261019.md, incluyendo1153líneas mediante páginas contiguas. Se analizaron las10recetas/20filas del JSON íntegro, y se consultaron directamente los20resúmenes del motor por URL. No se ejecutaron nuevos backtests ni analysis jobs para esta revisión.

**PASS351comprobaciones. Selección vacía y decisión de no ejecutar verificaciones adicionales correctas.** Los351checks aritméticos/de consistencia no son nuevas observaciones de mercado.

Recalculados sin redondear: neto nominal frente a N204>1e−7; +5Mactivos>=65% yQ>=80%, ambos full/all; +10noinferiorN204 con tolerancia1e−7;DDmotor>=−25%. Contrastados exactamente los cuatrobooleanos de cada fila, el mínimo margenM/Q, elegibilidad de cada fila y de ambascarteras, mínimoΔ+10 ypeorDD. Los20netos/DD/conteos coinciden con resúmenes finished/errornull (tolerancia1e−7). Verificadas identidades de conteos retenidos+retirados=referencia y retenidos+añadidos=actual. P602yP605 muestran paridadseedtrue,deltaeconómico0 y264/271matched conforme pathChecks root. Esta revisión valida aritmética y evidencia publicada; NO es una segunda reconstrucción independiente de fills/MTM ni refuerza por repetición las identidades.

Las cincoE yP603fallan neto nominal y+10. P601mejoraN204 pero fallaMambas. P602/P605sonidentidadesdeN503 y fallanM enC40/63. P604tiene el mayor neto nominal observado pero C40/63=63.49206349%falla65%; no puede seleccionarse por ser la mejor nominal. B41/63=65.07936508% pasa por poco. P603pasa regularidad ambas, pero su neto inferior aN204 impide selección. DDpasa20/20; ese resultado no compensa otras puertas.

El ranking predefinido sólo ordena elegibles: margenM/Q, mínimoΔ+10, peorDD, ID. Con cero elegibles, el orden de recetas no elegibles es irrelevante y no se habilita una segunda elección. Corresponde detener tras20fulls nominales: cero feeengine.00070 y cero vecinos1.8R/2.2R. N204permanece congelada yN503/P604son investigación sin promoción. 2026cerrado incluso a inspección; muestra2020–2025reutilizada,noOOS ni prueba contra sobreajuste. No se relajaron denominadores/fechas/umbrales ni se combinaron recetas.

```json
{
  "checks": 351,
  "recomputed": [
    {
      "id": "E601",
      "eligible": false,
      "gateRows": [
        {
          "portfolio": "B",
          "gates": {
            "nominal": false,
            "calendar": false,
            "plus10": false,
            "dd": true
          },
          "eligible": false,
          "margin": -0.03809523809523818
        },
        {
          "portfolio": "C",
          "gates": {
            "nominal": false,
            "calendar": false,
            "plus10": false,
            "dd": true
          },
          "eligible": false,
          "margin": -0.020967741935483897
        }
      ]
    },
    {
      "id": "E602",
      "eligible": false,
      "gateRows": [
        {
          "portfolio": "B",
          "gates": {
            "nominal": false,
            "calendar": false,
            "plus10": false,
            "dd": true
          },
          "eligible": false,
          "margin": -0.03809523809523818
        },
        {
          "portfolio": "C",
          "gates": {
            "nominal": false,
            "calendar": true,
            "plus10": false,
            "dd": true
          },
          "eligible": false,
          "margin": 0.00952380952380949
        }
      ]
    },
    {
      "id": "E603",
      "eligible": false,
      "gateRows": [
        {
          "portfolio": "B",
          "gates": {
            "nominal": false,
            "calendar": true,
            "plus10": false,
            "dd": true
          },
          "eligible": false,
          "margin": 0.0007936507936507908
        },
        {
          "portfolio": "C",
          "gates": {
            "nominal": false,
            "calendar": false,
            "plus10": false,
            "dd": true
          },
          "eligible": false,
          "margin": -0.015079365079365137
        }
      ]
    },
    {
      "id": "E604",
      "eligible": false,
      "gateRows": [
        {
          "portfolio": "B",
          "gates": {
            "nominal": false,
            "calendar": false,
            "plus10": false,
            "dd": true
          },
          "eligible": false,
          "margin": -0.13333333333333341
        },
        {
          "portfolio": "C",
          "gates": {
            "nominal": false,
            "calendar": false,
            "plus10": false,
            "dd": true
          },
          "eligible": false,
          "margin": -0.03809523809523818
        }
      ]
    },
    {
      "id": "E605",
      "eligible": false,
      "gateRows": [
        {
          "portfolio": "B",
          "gates": {
            "nominal": false,
            "calendar": true,
            "plus10": false,
            "dd": true
          },
          "eligible": false,
          "margin": 0.00952380952380949
        },
        {
          "portfolio": "C",
          "gates": {
            "nominal": false,
            "calendar": false,
            "plus10": false,
            "dd": true
          },
          "eligible": false,
          "margin": -0.03809523809523818
        }
      ]
    },
    {
      "id": "P601",
      "eligible": false,
      "gateRows": [
        {
          "portfolio": "B",
          "gates": {
            "nominal": true,
            "calendar": false,
            "plus10": true,
            "dd": true
          },
          "eligible": false,
          "margin": -0.015079365079365137
        },
        {
          "portfolio": "C",
          "gates": {
            "nominal": true,
            "calendar": false,
            "plus10": true,
            "dd": true
          },
          "eligible": false,
          "margin": -0.030952380952380953
        }
      ]
    },
    {
      "id": "P602",
      "eligible": false,
      "gateRows": [
        {
          "portfolio": "B",
          "gates": {
            "nominal": true,
            "calendar": true,
            "plus10": true,
            "dd": true
          },
          "eligible": true,
          "margin": 0.0007936507936507908
        },
        {
          "portfolio": "C",
          "gates": {
            "nominal": true,
            "calendar": false,
            "plus10": true,
            "dd": true
          },
          "eligible": false,
          "margin": -0.015079365079365137
        }
      ]
    },
    {
      "id": "P603",
      "eligible": false,
      "gateRows": [
        {
          "portfolio": "B",
          "gates": {
            "nominal": false,
            "calendar": true,
            "plus10": false,
            "dd": true
          },
          "eligible": false,
          "margin": 0.032539682539682535
        },
        {
          "portfolio": "C",
          "gates": {
            "nominal": false,
            "calendar": true,
            "plus10": false,
            "dd": true
          },
          "eligible": false,
          "margin": 0.0007936507936507908
        }
      ]
    },
    {
      "id": "P604",
      "eligible": false,
      "gateRows": [
        {
          "portfolio": "B",
          "gates": {
            "nominal": true,
            "calendar": true,
            "plus10": true,
            "dd": true
          },
          "eligible": true,
          "margin": 0.0007936507936507908
        },
        {
          "portfolio": "C",
          "gates": {
            "nominal": true,
            "calendar": false,
            "plus10": true,
            "dd": true
          },
          "eligible": false,
          "margin": -0.015079365079365137
        }
      ]
    },
    {
      "id": "P605",
      "eligible": false,
      "gateRows": [
        {
          "portfolio": "B",
          "gates": {
            "nominal": true,
            "calendar": true,
            "plus10": true,
            "dd": true
          },
          "eligible": true,
          "margin": 0.0007936507936507908
        },
        {
          "portfolio": "C",
          "gates": {
            "nominal": true,
            "calendar": false,
            "plus10": true,
            "dd": true
          },
          "eligible": false,
          "margin": -0.015079365079365137
        }
      ]
    }
  ],
  "eligible": [],
  "selected": null,
  "summaryReads": 20,
  "limits": "Gate arithmetic, published path count identities and 20 engine summaries verified; no independent fill/MTM reconstruction."
}
```
