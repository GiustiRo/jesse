# PAXG: resultado del control de ejecución

El [backtest de salida MARKET al cierre horario](http://localhost:9200/#/backtest/cb5bdb97-ba8a-4997-a009-673d76b4a156) terminó correctamente. Se conservaron las entradas y el stop de la primaria de 1 ATR, eliminando el target LIMIT y cerrando al callback horario posterior al toque del objetivo.

| Métrica | Primaria | Control de ejecución |
|---|---:|---:|
| Trades | 37 | 37 |
| Neto USDT | 400,22 | 321,19 |
| Fees USDT | 259,13 | 257,96 |
| PF neto | 1,507 | 1,409 |
| DD del motor | −2,062% | −2,332% |
| DD de cierres diarios UTC | −2,102% | −2,371% |
| Neto con otros 5 bps RT sobre mismos fills | 256,10 | 177,72 |
| Neto con otros 10 bps RT sobre mismos fills | 111,97 | 34,24 |
| Neto de trades cerrados en 2023–2025 | −34,82 | −73,91 |
| Neto excluyendo los tres mayores ganadores | 102,92 | 24,26 |

La ganancia agregada sobrevive a esta política alternativa de ejecución, pero se reduce. No es un modelo garantizado de slippage adverso: el cierre horario puede ser mejor o peor que el precio del target. La fragilidad temporal continúa; no se acepta la receta ni se integra por este resultado.

## Auditoría independiente

Job final bfffb8fd76674597927438f48bad3b3c: succeeded / exit 0. Conciliaron cantidades, fees, PnL, wallet y MTM. Los 37 timestamps y direcciones de entrada coinciden exactamente. La diferencia máxima de precios medios de entrada es 4,55e-13, atribuible al cálculo con floats; satisface la tolerancia M1 de la propia estrategia. El intento anterior e719b8a43d4f418f8085de1b69a1fe97 falló por exigir igualdad exacta de floats después de conciliar MTM; se corrigió el comparador, sin cambiar ni repetir los backtests.

MTM: primaria 18/30 meses activos positivos y 18/63 calendario, 12/21 trimestres; control 18/30 activos y 18/63 calendario, 11/21 trimestres. En períodos completos, el control tiene 18/30 meses activos positivos, 18/61 calendario y 10/19 trimestres. La regularidad es un objetivo de cartera, no un gate para cada señal.

Fuente reproducible completa e inputs: ROOT_ROBUSTNESS_ANALYSIS_SOURCE_20261018.md en esta misma carpeta. Sin nuevas fuentes, funding, framework, live/paper, BTC o evaluación de 2026. Ventana de desarrollo y riesgo nominal 1% iguales al protocolo.