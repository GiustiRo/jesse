# V5 Funding Trend — replay continuo y robustez

Estado: **SIN_CANDIDATA**. Completado 2026-10-21T02:04:38.264Z. Las 17 nuevas corridas prerregistradas terminaron, con 18 slots incluyendo reutilización de FP nominal como lag FP. No se retocaron fuentes, calendarios, reglas ni criterios según resultados.

## Nominales

- [OI nominal](http://localhost:9200/#/backtest/46f4c14a-1ac2-4cc0-b347-5d6bff007051): N=84; net -6.866518%; PF 0.853912; DD 17.669256%; CAGR -3.489614%; semestres positivos 1/4. Falla: net_positive, pf_ge_1_2, trades_ge_100, positive_semesters_ge_3, cagr_ge_15.
- [FP nominal](http://localhost:9200/#/backtest/ff2f12bf-1faf-4bec-808f-800a778421a4): N=107; net -2.079607%; PF 0.960575; DD 14.311619%; CAGR -1.043844%; semestres positivos 2/4. Falla: net_positive, pf_ge_1_2, positive_semesters_ge_3, cagr_ge_15.

OI falla cinco de seis criterios nominales; FP cuatro de seis. Ninguna puede promoverse. El funding cobrado fue positivo (+141.154922 USDT OI y +167.581792 USDT FP), insuficiente para compensar el resultado de precio y costos.

## Pruebas congeladas

| Escenario | Variante | N | Neto % | PF | DD absoluto % | Gate |
|---|---|---:|---:|---:|---:|---|
| NOMINAL | [OI](http://localhost:9200/#/backtest/46f4c14a-1ac2-4cc0-b347-5d6bff007051) | 84 | -6.866518 | 0.853912 | 17.669256 | RECHAZADO |
| NOMINAL | [FP](http://localhost:9200/#/backtest/ff2f12bf-1faf-4bec-808f-800a778421a4) | 107 | -2.079607 | 0.960575 | 14.311619 | RECHAZADO |
| S1 | [OI](http://localhost:9200/#/backtest/61c51f03-91d9-4142-8ad5-3f52f19cf4cb) | 84 | -10.143576 | 0.787782 | 19.639122 | FAIL net>0 |
| S1 | [FP](http://localhost:9200/#/backtest/12b33663-1fd7-4883-bb74-519549664e21) | 107 | -6.643530 | 0.876646 | 17.025102 | FAIL net>0 |
| S2 | [OI](http://localhost:9200/#/backtest/e7846d15-86e3-4c78-a5c4-c34122b0d8f5) | 84 | -10.418381 | 0.786189 | 20.030092 | Informativo, negativo |
| S2 | [FP](http://localhost:9200/#/backtest/ef49d5d4-f4b7-4754-a91d-ec13cc6b51c4) | 107 | -7.032193 | 0.872033 | 17.483515 | Informativo, negativo |
| S3 | [OI](http://localhost:9200/#/backtest/3733bd0f-ab2d-4ef8-b520-8455c1ecb44f) | 84 | -16.720499 | 0.672628 | 24.081217 | FAIL net>0 |
| S3 | [FP](http://localhost:9200/#/backtest/0d37d117-ee67-4dcb-a3bf-44e16ccd32ad) | 107 | -15.661284 | 0.729832 | 22.969672 | FAIL net>0 |
| R09 | [OI](http://localhost:9200/#/backtest/8d8a26f8-89dc-4afb-818e-1a9b02093d04) | 84 | -6.034780 | 0.880690 | 18.517683 | FAIL net>0 |
| R09 | [FP](http://localhost:9200/#/backtest/f7c84508-165c-4788-83fc-52a9bd048e19) | 107 | -0.408729 | 0.992765 | 14.405857 | FAIL net>0 |
| R11 | [OI](http://localhost:9200/#/backtest/65d8ecaa-5769-45cd-a0d1-8ce5eac88c50) | 84 | -6.601088 | 0.846575 | 16.215933 | FAIL net>0 |
| R11 | [FP](http://localhost:9200/#/backtest/bd499d4f-5b7f-4ae1-882b-fac50e6becf3) | 107 | -1.389741 | 0.970934 | 12.520911 | FAIL net>0 |
| A09 | [OI](http://localhost:9200/#/backtest/37f3b888-9751-4521-96a1-1711768f37f6) | 91 | -8.773788 | 0.824356 | 19.541916 | FAIL net>0 |
| A09 | [FP](http://localhost:9200/#/backtest/ec1db1af-39f4-4ad3-83b7-f481566578a6) | 112 | -1.506224 | 0.973012 | 12.167023 | FAIL net>0 |
| A11 | [OI](http://localhost:9200/#/backtest/26d1d710-e190-40c2-ab35-c49622e8bca7) | 82 | -9.938799 | 0.783284 | 18.666421 | FAIL net>0 |
| A11 | [FP](http://localhost:9200/#/backtest/f81ccfbc-4887-419a-9a5b-2d341b75c93e) | 103 | -5.766922 | 0.885754 | 16.529101 | FAIL net>0 |
| LAG4H | [OI](http://localhost:9200/#/backtest/08c43974-9ebf-4015-a3bf-f31481bcadfa) | 87 | -10.942969 | 0.777568 | 20.608490 | FAIL net>0 |

S1 fee0.0009/slip0; S2 fee0.00045/slip5bps; S3 fee0.0009/slip10bps. R09/R11 stop2.7/3.3 ATR; A09 SMA108/return27; A11 SMA132/return33; lag OI retrasa la señal OI una barra4h manteniendo su reloj original de disponibilidad/frescura. Cada corrida empezó con10000 y cuatro ventanas separadas dentro de2024–2025, con capital continuo y cierre obligatorio en cada frontera. Todos los nuevos escenarios requeridos (13/13) fallan net>0; los8 vecinos son negativos y FP lag reutiliza nominal negativo. S2 es informativo. Ningún vecino mejor sustituye el nominal ni modifica selección.

## Auditoría y evidencia

17 auditorías completas de logs aprobadas:74562 decisiones,1621 entradas/planes,1621 cierres y37281 ventanas publicadas de tres pagos con SHA verificado. Se verificaron68 controles de frontera (4 por sesión), ausencia de entradas en los bordes y ausencia de exposición que los atraviese. Las liquidaciones efectivas por calendario dependen de estar abierto; no se afirma que hubo un fill en cada borde. No hubo cierres forzados finales posteriores a la auditoría.

9 snapshots financieros completos aprobados con código exacto capturado en V5_V6_ACCOUNTING_CODE.json y expected config/strategy/dates/timeframe. Máximo error 3.637978807091713e-11 USDT. Incluyen trades/órdenes/ledger, fees de fills, slippage de MARKET/STOP, funding y relojes raw/effective, equity diario y terminal, semestres, CAGR/DD, datasets y configuración. DD con equity terminal coincide con DD del motor a precisión numérica; no se cambió el gate.

Las ventanas SHA se comprobaron todas contra los logs originales. Se duplicaron como evidencia las ventanas asociadas a todas las entradas y muestras inicial/media/final; las demás publicaciones permanecen en los logs de sesión. Precios/ATR se comprobaron desde contexto, con construcción de ventanas causal respaldada por fuente congelada y checks. No se descargaron candles nuevos ni se ejecutaron research scripts. Fuentes y condiciones retrospectivas de disponibilidad OI siguen siendo limitaciones: archive label+6min no certifica publicación histórica original.

Cada detalle conserva form completo, prerun, timestamps, raw start, terminal summary y hash de fuente; cada AUDIT conserva buckets completos, counters, causas y referencias a shards de hasta40 entradas. Índice ligero: V5_REPLAY_STRESS_BRANCH_PROGRESS.json. Filas completas: V5_REPLAY_<SCENARIO>_ACCOUNTING.json. Resumen legible por máquina: V5_REPLAY_STRESS_BRANCH_SUMMARY.json.

Tres arranques devolvieron timeout10s: FP_S3,OI_R09,FP_R09. Cada raw íntegro se guardó y se recuperó el MISMO ID mediante lectura exitosa; ningún start se repitió. La concurrencia comenzó en un motor V5, aumentó a dos sólo tras GO explícito de root al concluir motores V6; se mantuvo un analysis job propio.

## Replay frente a walk forward

Comparación directa de trades capturados, sin motores ni jobs adicionales: OI replay84 frente a suma WF83. Las83 entradas WF coinciden por opened_at+direction; ninguna falta en replay. Hay exactamente una entrada adicional: **short2025-01-01T04:00:00Z**, cierre stop2025-01-03T18:45:00Z, PNL−195.502023 USDT. Las83 entradas comunes tienen precios y tiempos de cierre iguales dentro de1e−6, aunque cantidades, fees y PNL varían por capital continuo.

La evidencia concreta del trade adicional muestra OI actual91170.567 contra referencia90681.416 registrada2024-12-31T04:00Z; ambas filas eran válidas/asof. El replay continuo conserva esa referencia de24h. C3V independiente empieza2025-01-01 y su buffer de decisiones carece del registroT−24h; la fuente congelada exige coincidencia exacta y prohíbe backfill. C3V registra5 oportunidades de inicialización y no tiene esa entrada. El trío funding coincide por SHA y el precio satisface setup short. Esto explica la diferencia de una entrada, sin atribuir todos los deltas de PNL exclusivamente a ella.

OI2025H1 replay−2.934626742% frente a C3V−0.983972059%; replay total−6.866518447% frente a índice WF−4.9980397%. El índice rebasa semestres independientes; no representa equity continuo. FP mantiene107 entradas y pequeños deltas por capital/fees/fronteras. Comparación completa y evidencia: V5_REPLAY_VS_WF_ENTRY_COMPARISON.json. No se forzó igualdad entre diseños.

## Sensibilidad funding

Sensibilidades nominales sobre cantidades fijas (no nuevos replays): funding×0.5/1.5 deja OI net−7.572293%/−6.160744% y FP−2.917515%/−1.241698%. Ninguno cambia de signo. Sensibilidad proxy-only no altera estos nominales porque el funding aplicado capturado en esos trades utiliza marks exactos; las limitaciones del dataset completo siguen declaradas. Valores por escenario/fuente en filas completas de accounting.

Conclusión operativa: terminar la rama V5 rechazada, sin rescatar parámetros, nuevos motores ni promoción. Tokens de motor y analysis liberados. Fuentes2026 continúan cerradas; finish2026-01-01 es exclusivo y sólo consume datos hasta2025.
