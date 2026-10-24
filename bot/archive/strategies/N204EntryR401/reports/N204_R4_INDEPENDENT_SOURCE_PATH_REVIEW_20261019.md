# Revisión independiente de fuentes y diagnóstico de trayectorias — R4

Revisión de lectura, sin jobs, backtests, datos nuevos ni cambios de estrategia. Leí las 13 fuentes completas actuales: cuatro Entry, cuatro Exit, cuatro Experimental y PathDiagnosticR400, además del protocolo y N204. La referencia N204 sigue byte-idéntica a su congelación. Las cuatro Entry conservan sus fuentes aprobadas por QA.

No encontré errores materiales. Veinte métodos protegidos por fuente coinciden exactamente con la base tras quitar espacios exteriores: 260 comparaciones de HP, horarios, ledger, capital, reservas, cuotas de volatilidad, planes originales, señales, órdenes, sizing y validación de ventanas. Los cambios restantes corresponden a los hooks y fórmulas autorizados.

Los cuatro gates Entry, las cuatro fórmulas Experimental y sus índices coinciden con el protocolo. T401 requiere tres barras completas posteriores al fill; T402 revisa exactamente la sexta barra contigua; T403 reinicia su latch al abrir y exige recuperación en una barra estrictamente posterior; T404 mantiene stop y plazo, divide el TP con el redondeo acordado y reajusta la cantidad protegida tras una reducción. El deadline conserva prioridad. La conciliación de fills parciales reales de T404 corresponde al auditor root cuando termine su corrida.

## Diagnóstico y contraste con fills

[Retry B](http://localhost:9200/#/backtest/c26a2bbc-d960-4a13-873b-07e52f57b05b) y [retry C](http://localhost:9200/#/backtest/cacecd6c-6f04-46d4-b456-5b667010bee8): leí summary primero y después las 273/280 operaciones completas, cuatro páginas por sesión. Leí ambos journals compactos completos de 79 filas. Cada fila coincide con un BTC short MARKET real en timestamps de apertura/cierre, precios y cantidad.

Las 79 filas tienen cv=true, n=ne y err vacío; el manifiesto registra 79 partes, 79 filas y ninguna observación abierta. Los conteos esperados coinciden con la fórmula de minutos estrictamente anteriores al fill de salida. Esto verifica registros, joins y lógica de captura; no constituye otra descarga ni reproducción independiente de los OHLC M1 subyacentes.

La fuente excluye barras anteriores al fill y minutos que terminan al mismo tiempo o después de la salida. Por eso MFE/MAE son cotas inferiores observadas: no prueban que los minutos excluidos no tocaran 1R, ni identifican orden intraminuto. La reparación de _path_report emite una fila compacta por línea y no interviene en órdenes o riesgo.

B/C tienen los mismos 79 eventos: coinciden clocks, precios, D, MFE, MAE, horizontes y cobertura. Sus cantidades y PNL monetarios pueden cambiar. No son 158 observaciones independientes. Los 96 eventos de before de N204 tampoco son 96 fills: el estado avanza ocupado/pending y los planes originales tienen prioridad. events_occupied describe estado, no una partición completa de rechazos.

Los journals y fills concuerdan con el informe central:
- 19 TP a 2R, 21 stops a −1R y 39 timeouts de 48 horas.
- 42 operaciones netas positivas y 37 no positivas.
- 32 MFE observadas ≥1R, todas en el grupo ganador.
- Medianas MFE 0,7771206248491174R y MAE 0,5833473202796631R.
- A 6/12/24 horas: 74/66/51 observaciones y 5/13/28 cierres anteriores o simultáneos; cero missing.

Los horizontes exigen horizonte < salida, excluyendo correctamente cierres simultáneos. Sus medianas están condicionadas a seguir abierto; no son expectativas incondicionales ni recorridos contrafactuales. Agrupar por PNL final es retrospectivo. El texto central ya contiene estas cautelas y no propone ajustar T después del diagnóstico.

La paridad completa de 273/280 trades y máximo ΔPNL=0 procede del job root 25e703b4972645fe932465cacf5895fb. Esta revisión verificó directamente los 79 joins sobre todas las operaciones retry; no ejecutó otro job de paridad global. La ausencia de gaps registrados no demuestra exactitud externa ni liquidez real. 2026 permanece cerrado y todo corresponde a desarrollo reutilizado.

Corrección editorial de mi informe Entry: una frase inicial decía E404=57 suplementos; el registro real, tabla y contadores muestran 56. Corregí esa frase a 56 antes del handoff, sin cambiar fuentes ni resultados.

```json
{
  "journal_fill_checks": {
    "B": {
      "net": 2856.514710837504,
      "counts": {
        "target2R": 19,
        "stop1R": 21,
        "timeout48h": 39
      },
      "horizons": {
        "6": {
          "observed": 74,
          "closed": 5,
          "missing": 0
        },
        "12": {
          "observed": 66,
          "closed": 13,
          "missing": 0
        },
        "24": {
          "observed": 51,
          "closed": 28,
          "missing": 0
        }
      },
      "positive": 42,
      "nonpositive": 37,
      "observed_MFE_ge1": 32,
      "nonpositive_observed_MFE_ge1": 0
    },
    "C": {
      "net": 2836.6311553139217,
      "counts": {
        "target2R": 19,
        "stop1R": 21,
        "timeout48h": 39
      },
      "horizons": {
        "6": {
          "observed": 74,
          "closed": 5,
          "missing": 0
        },
        "12": {
          "observed": 66,
          "closed": 13,
          "missing": 0
        },
        "24": {
          "observed": 51,
          "closed": 28,
          "missing": 0
        }
      },
      "positive": 42,
      "nonpositive": 37,
      "observed_MFE_ge1": 32,
      "nonpositive_observed_MFE_ge1": 0
    }
  },
  "sources_read": 13,
  "protected_methods_per_source": 20,
  "identical_79_BC": true
}
```
