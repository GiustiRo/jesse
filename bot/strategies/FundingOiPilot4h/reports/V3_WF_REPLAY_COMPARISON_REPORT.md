# V3 — comparación independiente WF/replay nominal

Job final **8aec2dc27d76401a80f0b0068001f2de**, succeeded con diez snapshots completos. Código/manifest/raws/resultados completos y métricas conservados en V3_WF_REPLAY_COMPARISON_SOURCE.json, _JOB.json, _RESULTS.json y _METRICS.json. Job inicial4ed19d5771334b2e9c63ce5515996e8d también succeeded; se repitió sólo para exportar chunks40k porque el transporte truncaba chunks90k a65512caracteres. Raw preservado en _JOB_INITIAL.json. Ningún motor nuevo.

| Nominal | Trades | Saldo replay | WF sintético reescalado | Diferencia USDT | CAGR replay731d | PF replay | DD motor |
|---|---:|---:|---:|---:|---:|---:|---:|
| [P](http://localhost:9200/#/backtest/16da36e2-2807-4a9b-85e3-51cf8fa67c75) | 95 | 13822.585629 | 13822.585688 | -0.000058979 | 17.543463% | 1.348511 | -18.413964% |
| [OI](http://localhost:9200/#/backtest/48ee9577-29cb-4860-8dff-be0d82caf796) | 84 | 12289.026304 | 12289.026191 | 0.000113112 | 10.840253% | 1.259787 | -17.168436% |

El selector global permanece **OI en C1–C4**. El rebase WF es producto hipotético de ratios de equity de sesiones independientes; no una cuenta ejecutada. Los retornos replay provienen de equity de la misma cuenta continua, no de sumar PNL de cierres semestrales. PF se reconstruye sólo por trades únicos de cada sesión real, nunca se suma o promedia entre folds.

| Variante/fold | Retorno WF | Retorno replay por equity | Equity inicial replay | Equity final replay | Entradas coincidentes |
|---|---:|---:|---:|---:|---:|
| P/C1 | 16.31462581% | 16.31462581% | 10000.000000 | 11631.462581 | 25/25 |
| P/C2 | 18.94485407% | 18.94485480% | 11631.462581 | 13835.026279 | 21/21 |
| P/C3 | 1.87025886% | 1.87025807% | 13835.026279 | 14093.776974 | 25/25 |
| P/C4 | -1.92419184% | -1.92419211% | 14093.776974 | 13822.585629 | 24/24 |
| OI/C1 | 11.99157983% | 11.99157983% | 10000.000000 | 11199.157983 | 22/22 |
| OI/C2 | 0.81318478% | 0.81318534% | 11199.157983 | 11290.227894 | 22/22 |
| OI/C3 | 2.98072824% | 2.98072803% | 11290.227894 | 11626.758882 | 22/22 |
| OI/C4 | 5.69606163% | 5.69606224% | 11626.758882 | 12289.026304 | 18/18 |

Coinciden las95entradas P y84OI por opened_at y dirección, sin entradas exclusivas en ningún fold. Los tiempos de salida coinciden en todas las parejas. Precios de entrada difieren a precisión flotante: P 14 parejas, máximo 1.455e-11 USDT; OI 15 parejas, máximo 2.910e-11 USDT. No se afirma igualdad literal de precios. Las cantidades se escalan según el capital transportado, con diferencias pequeñas de redondeo; desde C2 la equity inicial replay ya no es10000. Diferencias de saldo final menores a0,00012USDT son compatibles con precisión de cantidades/capital en las parejas; no se atribuyen a un mecanismo económico no observado.

En todos los límites de ambos replays, snapshots completos muestran cero posiciones candidatas antes del límite y cero funding efectivo exacto. No hubo cierres exactos allí. Esto coincide con cero calendar_liquidations informado por dueño P; **no implica reinicio de capital**, como demuestran equity y cantidades. El potencial efecto de funding previo a decisiónT no se manifestó en estos bordes concretos; el JSON conserva eventos/órdenes vecinos y reloj effective_at.

No se observa diferencia de entradas en las primeras28h de ningún semestre. Inicialización OI mantiene **evidencia insuficiente para atribución causal directa**: el contrato snapshot omite logs V3_AUDIT/V3_ENTRY. La explicación esperada de seis decisiones por sesión WF frente a historia continua replay no se fuerza como diferencia empírica. Sin nuevos gates, selección retrospectiva o cambios a calendarios.

Curvas terminales coinciden con balance final real (delta0 en ambos replays); se usa convención mensual−61s y override terminal final exclusivamente. Este diagnóstico no sustituye la auditoría central de contabilidad/gates. P puede rendir más que OI sin alterar el selector train ya congelado.
