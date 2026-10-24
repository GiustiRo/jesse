# V5 — cierre del screening VWAP

Las dos variantes nominales quedan RECHAZADAS por neto negativo, PF<1.2 y drawdown>25%. Cumplen N>=30, pero ningún criterio se relaja. No se cambia señal, bandas, volumen, salida, stop o holding para rescatar resultados. No se promueve una variante porque pierda menos.

| Variante | Trades | Neto período | PF neto de trades | DD absoluto motor | Saldo final |
| --- | ---: | ---: | ---: | ---: | ---: |
| [VWAP_PV](http://localhost:9200/#/backtest/46f494e4-aca0-455e-979e-f279d3d87106) | 546 | -33.869417% | 0.883113 | 40.951584% | 6613.058282 |
| [VWAP_PVOI](http://localhost:9200/#/backtest/6b21c3d2-69f7-4d70-8f8d-56d69974c270) | 350 | -33.138824% | 0.845920 | 38.282996% | 6686.117650 |

Ventana continua [2020-09-01,2024-01-01), 1h; 10000 inicial por sesión, aislado3x con cap1x, riesgo previsto2% de stop+fees, fee.00045 por lado, slip0, funding histórico ON, warmup240. Las fuentes y configuración permanecieron congeladas. PV fees3258.876678/funding+236.732606; PVOI fees2249.920054/funding+176.842343 USDT. CAGR descriptivo −11.664461%/−11.372894%, sin añadir gate CAGR en SCREEN.

Root creó ambos drafts; este sector inició únicamente esos IDs, con respuestas started sin timeout. PV fue consultado running/errornull antes de solicitar PVOI. Dos motores simultáneos dentro de la autorización global de dos; ambos terminaron y se liberaron antes de auditar. No nuevos drafts, motores o jobs de análisis.

## Auditoría completa

Ambas sesiones: 40 meses, 29208 decisiones, 690 features de reingreso idénticas, particiones de primary/features/dirección correctas. Entradas=trades=cierres:546 y350; cero cierres finales forzados. Una entrada por día UTC y ninguna entrada en la misma decisión que un cierre.

Se recorrieron todos los logs:15 páginas PV y11 PVOI, sin has_more pendiente. Se leyeron todos los trades y órdenes almacenadas:7 páginas PV y4 PVOI. Se verificaron todos los planes/fills/cierres; sizing exacto por distancia+fees, floor8, cap1x, stop2ATR desde fill y targetNone. ATRoffset0 y ventanas15, señal25 con ventanas actuales/previas propias y reglas de reingreso/centro/corrección concuerdan con los contextos.

PV:314 normalizaciones VWAP,223 stops,9 maximum_hold. PVOI:190 normalizaciones,155 stops,5 maximum_hold. Las504 salidas VWAP cumplen estado del lado correcto del centro móvil, T>opened_at, ventana24h terminada en T; no TP LIMIT ni fill retroactivo. Las14 salidas hold cumplen edad>=24h. Calendario/fold_end no se ejercieron en estos screenings.

Todos los reingresos verificados usan K2 y escala=max(σ ponderada,ATR14), con C0 todavía antes del centro. Los contextos de entrada no mostraron cero volumen. La calidad de OHLCV y el cálculo de pesos/media/varianza se respaldan por validación del helper, hashes y checks estáticos; esta auditoría no reconstruye todas las velas originales desde logs ni certifica VWAP exacto de ticks. Ventanas con volumen inválido se rechazan por código; no se atribuye cobertura de ceros/gaps reales si no aparecen en estos contextos.

PV registró99 daily_limit y45 in_position_or_pending. PVOI registró62/28, además247 OI no creciente,1 inicialización,1 stale y1 cero. Todos los fills PVOI tienen qualityvalid/passed y referencia exactamente24h; PV permitió falta/calidad desfavorable de OI conforme a su definición. As-of funding/OI y límites de líneas JSON<=1900 pasan.

## Riesgo observado y límites

Hubo26 cierres PV y21 PVOI con pérdida mayor que presupuesto2%, máximos excesos7.117025 y8.114521 USDT. Los componentes de pérdida de precio más fees, excluido funding, permanecen dentro del presupuesto en todos esos casos. Funding adverso adicional explica el exceso; no es stop aflojado ni error que habilite retocar la estrategia. Se conserva cada evento y su trade en las auditorías.

El auditor inicialmente exigía igualdad binaria entre el promedio de entrada almacenado y el fill registrado, y exigía timestamp OI válido incluso para registros absent/stale en PV. Se corrigió sólo el control: diferencia de precio<=1e−8 para representación del promedio y aceptación explícita de null provenance cuando OI no está disponible; PVOI conserva calidad obligatoria estricta. No se introdujo tolerancia en desigualdades de señal ni fuentes productivas y no se repitió ningún backtest. Evidencia en V5_VWAP_AUDIT_HARNESS_NOTE.json.

La conciliación financiera de snapshots completos corresponde a root. Los checks de este sector acreditan reglas y contadores, no aprobación económica. OI retrospectivo y marcas proxy de funding mantienen sus límites. Datos 2020–2023 ya observados no constituyen OOS virgen. No se consultó economía VWAP V5 de2024+ ni2026.

## Evidencia guardada

V5_VWAP_PROGRESS.json conserva prerun/config y respuestas crudas de los dos inicios, summaries y checks finales. AUDIT_ResearchV5VwapPV1h_SCREEN.json y AUDIT_ResearchV5VwapPVOi1h_SCREEN.json guardan buckets, provenance, causas, riesgos y verificaciones.

Los archivos V5_VWAP_PV_SCREEN_LOGS_XX.json / V5_VWAP_PVOI_SCREEN_LOGS_XX.json conservan todos los logs; los correspondientes TRADES_XX.json conservan trades/órdenes; PLANS_XX.json conserva todas las entradas/features en bloques de150; EXIT_CONTEXTS.json conserva todos los contextos de salida y cierres. No se seleccionaron sólo ejemplos favorables.

Sector cerrado RECHAZADO; sin cambios a V1–V5, nuevas variantes o sesiones. Root conserva coordinación de V6 y de cualquier otra fase autorizada.
