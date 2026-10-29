# V3 CHANNEL OI: replay continuo y robustez

El replay nominal [2024-01-01,2026-01-01) conserva capital entre los cuatro semestres congelados y conserva cada frontera por separado. No supera el gate histórico: 84 operaciones frente a 100 requeridas y CAGR 10.840253% frente a 15%. Los cuatro semestres fueron positivos según conciliación central. Este resultado no habilita promoción.

| Sesión | Trades | Neto % | CAGR motor % | PF derivado | DD motor % |
|---|---:|---:|---:|---:|---:|
| [NOMINAL](http://localhost:9200/#/backtest/48ee9577-29cb-4860-8dff-be0d82caf796) | 84 | 22.890263 | 10.840253 | 1.259787 | -17.168436 |
| [S1](http://localhost:9200/#/backtest/ed30f8b8-cef6-4412-b8a8-fab373e83686) | 84 | 16.333016 | 7.846624 | 1.187037 | -18.100742 |
| [S2](http://localhost:9200/#/backtest/fc83768f-8b75-49c9-ab16-dac612680700) | 85 | 13.176649 | 6.375508 | 1.143316 | -18.650307 |
| [S3](http://localhost:9200/#/backtest/522314c0-d4b6-48a1-b229-b9fbe8ca3305) | 86 | -2.307014 | -1.158660 | 0.975584 | -23.813695 |
| [N09](http://localhost:9200/#/backtest/b4f28840-ab21-42a0-93ae-31f331f33e1c) | 90 | 7.478741 | 3.666840 | 1.074383 | -20.549458 |
| [N11](http://localhost:9200/#/backtest/ff6758bb-97f8-474f-b704-91f826563e7f) | 82 | 20.231874 | 9.636478 | 1.246815 | -15.853786 |
| [LAG1](http://localhost:9200/#/backtest/5fe5146d-cf80-4cc1-aed1-b2300b1eb888) | 73 | 30.613050 | 14.265191 | 1.475020 | -13.796998 |

S1 duplica fee a 0.0009, S2 usa slippage5bps con fee nominal, S3 combina fee0.0009/slippage10bps. N09 cambia sólo STOP/TRAIL a1.8/2.7, N11 a2.2/3.3. LAG1 cambia sólo OI_LAG_BARS a1. Cada sesión reinicia capital10000; calendario, límites, reglas y datos permanecen congelados. Las siete sesiones terminaron sin error y se iniciaron una sola vez. No se ejecutaron análisis propios, live ni datos2026.

El beneficio se deteriora con fricción: S3 termina negativo y PF<1. El vecino inferior N09 produce un avance considerablemente menor. N11 permanece positivo, pero también por debajo del nominal. El lag mejora esta muestra, con sólo73 operaciones: sirve para describir sensibilidad, sin reseleccionar ni reemplazar la especificación nominal.

Cada auditoría propia verifica4386 decisiones,24 meses, particiones direccionales materializadas, allowed=entradas y contabilidad entradas/cierres, provenance y calendario exactos. Las entradas/cierres fueron84/84,84/84,85/85,86/86,90/90,82/82,73/73 respectivamente. No hubo cierre forzado posterior al bloque final de auditoría. Cuatro decisiones boundary_or_inactive por sesión conservan las fronteras. Los buckets direccionales sin observaciones no se fabrican. La conciliación financiera y de ejecución completa corresponde a root; la conciliación central nominal ya pasó con error máximo2.01e-11USDT.

Artefactos propios: V3_OI_REPLAY_PROGRESS.json (configuraciones, fuentes, SHA de descriptores, IDs/URLs, timestamps, respuestas completas y resúmenes); AUDIT_<estrategia>_<escenario>.json (siete auditorías). Fuentes estáticas fueron congeladas centralmente en job93fc699d8de0433594ab56ce072c22d7. No se modificaron parámetros tras observar resultados.

OI utiliza archivo retrospectivo, no certificado point-in-time. Las cifras de CAGR/PF/DD mostradas provienen del summary de motor (PF=gross_profit/abs(gross_loss)); root conserva la auditoría terminal y de funding. Los resultados describen un avance parcial frágil a costos, sin evidencia suficiente para candidato histórico.
