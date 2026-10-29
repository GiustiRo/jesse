# V6 Deleveraging — sector rechazado

Los dos screenings nominales terminaron con error nulo. Ninguno satisface neto positivo, PF≥1,2 ni DD absoluto≤25%. No se modifica el mecanismo, OI decreciente, horizonte o protección después de ver estos resultados.

| Variante | Operaciones | Neto del período | PF | Drawdown | Sharpe |
|---|---:|---:|---:|---:|---:|
| P | 236 | -17.430155% | 0.885348 | -35.991951% | -0.259499 |
| POI | 86 | -28.896805% | 0.545979 | -32.061813% | -1.102728 |

Dashboard P: http://localhost:9200/#/backtest/2baa85a1-e673-4c84-bce9-38640f7b4e44
Dashboard POI: http://localhost:9200/#/backtest/3421d437-5eb7-4c74-8c44-9942162b7892

## Configuración y ejecución

BTC-USDT Binance Perpetual Futures,4h, período continuo2020-09-01→2024-01-01. Capital10000,isolated3x,cap1x,riesgo2%stop+fees,fee.00045/slippage0,fundinghistóricoON,OIexactodatasetcongelado,240barraswarmup. Config/readback de ambos drafts exactos antes de arranque. Root inició una vez cada sesión; el owner no repitió solicitudes. El timeout HTTP de POI fue recuperado leyendo el mismo ID. Los raws de inicio están en los archivos V6_DELEVERAGING_P_SCREEN_START.json y V6_DELEVERAGING_POI_SCREEN_START.json.

Señal idéntica de precio en ambos: desplazamiento24h contra dirección de entrada de al menos2ATR14simpleactual y corrección estricta en la última barra4h. Stop2A,objetivo4A=2R yhold48h. POI añade explícitamente OIbase0/OIbase24≤.98; no incluye rising adicional. No gate funding predictivo.

## Auditoría de ejecución

Se recorrieron todos los logs: P20páginas/3857líneas yPOI12páginas/2287líneas. Cada nominal tiene40meses y7302decisiones, con particiones de primary y feature_reasons exactas. Máxima línea P1113/POI1112 caracteres, inferior a1900; JSONfinito.

P:236entradas y236cierres;89stops,27objetivos y120maximum_hold exactamente48h. POI:86entradas y86cierres;32stops,4objetivos y50maximum_hold48h. No cierres forzados finales ni posiciones abiertas residuales inferidas de metadatos. Las322entradas son conteos por configuración, no una cartera ni muestras independientes.

Todos los planes se verificaron: cantidadfloor8 derivada de capital/stop+ambosfees,cap1x,distancia2ATR congelada,stop yobjetivo desde fillreal,fuentes/hash/offset0/15OHLC,precioC0/C1/C6,desplazamiento/corrección,cuotaUTC y ausencia de reentrada en misma decisión que cierre. La financiación visible por entrada era asof.

Las86entradas POI tienen ratio≤.98, ambos extremos positivos/finitos/frescos,available=label+6min yreferencia exactaT−24h realmente observada.233oportunidades se rechazaron por oi_decline_below_threshold. P admitió159entradas cuyo contexto declining no pasaba, acreditando que su ablación no exige caídaOI. La ausencia de gate de calidadOI en P está fijada en fuente y pruebas comunes; esas159entradas no se presentan como159casos de datos inválidos. Las dos variantes tuvieron360setups de precio, con diferentes ocupaciones/censura: no son operaciones idénticas emparejadas ni efecto causal aislado del filtro.

| Causa primaria | P | POI |
|---|---:|---:|
| Desplazamiento insuficiente | 6008 | 6008 |
| Corrección rechazada | 933 | 933 |
| Permitida | 236 | 86 |
| Posición o pendiente | 120 | 40 |
| OI cae menos del umbral | 0 | 233 |
| Cuota diaria | 4 | 1 |
| Borde final | 1 | 1 |
| Total | 7302 | 7302 |

## Evidencia y límites

- AUDIT_ResearchV6DeleverageP4h_SCREEN.json yAUDIT_ResearchV6DeleverageOi4h_SCREEN.json contienen todos los buckets, cierres, sumarios y procedencia.
- V6_DELEVERAGING_P_ENTRYPLAN_AUDIT.json yV6_DELEVERAGING_POI_ENTRYPLAN_AUDIT.json contienen los322planes verificados.
-32páginas rawlogs completas guardadas comoV6_DELEVERAGING_P_SCREEN_LOGS_XX.json yPOI equivalentes.
- V6_DELEVERAGING_PROGRESS.json preserva propuestas, fuentes, prerun, raws, auditorías y estado.
- Contabilidad monetaria completa, equity mensual/anual,ledger/costes y decisión global pertenecen al análisis central de root sobre snapshots completos.

Los hashes de ventanas identifican construcción y fuente; no se afirma recálculo independiente de cada OHLC mediante estos logs resumidos. El gate OI no identifica liquidaciones forzadas ni su lado. Archivo retrospectivo noPIT yfunding con marcas proxy mantienen límites. No hubo fills de calendario en estos nominales; cobertura determinista está en V6_STATIC_VERIFICATION.json.

No se abren nuevas pruebas, vecinos o confirmaciones por decisión de este sector. Gates faltantes no rescatan los fallos ya observados. Sólo root determina la shortlist global con el protocolo inmutable; estos dos nominales quedan rechazados.2026 cerrado, sin ML/live/paper/órdenes reales/Pi/cuentas ni cambios de fuente.
