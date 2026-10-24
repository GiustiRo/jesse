# Observador estructural: resultado negativo y archivo del recipe
Fecha 2026-10-18. Referencia inmutable: [sesión principal](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).
Conclusión: el observador causal 1D/4h probado NO añadió información predictiva útil con el estimador fijado. Empeoró Brier y logloss respecto de climatología; añadir pivots a tendencia diaria también empeoró ambos scores. Sucedió globalmente, en cada año y en la cohorte diaria sin horizontes solapados. Recomiendo archivar este recipe, sin estrategia de trading ni búsqueda posterior de ventana/shrink/pivots ganadores.

## Qué demuestra y qué no
Causal describe disponibilidad temporal de datos; no identifica causalidad económica. Este resultado rechaza la utilidad demostrada de esta representación+estimador+horizonte, no demuestra que toda estructura de precio carezca de información. La peor puntuación puede reflejar ruido/varianza adicional en estados poco frecuentes o falta de señal; no se puede distinguir sólo con estos promedios.

La referencia mantiene 28.83%CAGR,DD 14.89%,33/61 meses activos positivos54.10% y 15/21 trimestres 71.43%. Metas 65–70% / 80% intactas. No se ejecutó backtest/PnL, no se tocó baseline, riesgo 3% / 8%,gross 4.4 / 5x aislado ni fees 0.00045 por lado. First-touch±ATR / 24h no representa el payoff de retests multiday y no prueba mejora económica tras 9 bps RT/funding/gaps.

## Protocolo y datos realmente usados
Protocolo guardado antes de scores: INDEPENDENT_PREQUENTIAL_PROTOCOL_20261018.md en este mismo directorio de reportes.40 días de warmup sólo estructura/ATR; ningún label de warmup. BTC-USDT Binance Perpetual Futures vía API pública research.get_candles, consultas anuales acotadas. Semántica comprobada con 2020-10-15: tuple(None,candlesN × 6) cuando warmup=0, inicio incluido/fin excluido. __doc__ ausente; no se leyó source/SQL/env/red.

Inicio pronósticos 2020-10-15 00:00UTC. Fin exclusivo 2025-12-31 00:00UTC: el 31 de diciembre 2025 NO se consultó. Última M1 devuelta 2025-12-30 23:59; último origen 2025-12-30 20:00. No se pidió ni leyó 2026. Esta cota coincide con el formulario finish_date=2025-12-31 y la descripción exclusiva de la referencia, pero la métrica predictiva no es directamente comparable a su retorno. No es una evaluación completa del año civil 2025.

Hay 1903 días de origen y 6 slots por día=11418 forecasts. La cohorte00UTC contiene 1903 episodios válidos, incluido 2025-12-30 00UTC cuyo deadline coincide exactamente con el fin exclusivo. Los últimos 5 orígenes 4h posteriores a esa medianoche son right-censored. Eso explica que la cohorte diaria no pierda un día mientras el conjunto4h pierde 5 labels. No se añadió el 31 para rellenar ni se trató censura como none.

Modelos fijos: base Dirichlet 1 sobre ventana 180 días; trend signo de los dos últimos cierres 1D completos, shrink 20 contra base; pivot estados U/D/M por dos últimos highs/lows confirmados en 1D / 4h, shrink 20 contra base; combined cruza trend+pivot, shrink 20 contra trend. Pivots estrictos 2 izquierda / 2 derecha, sin empates ni dualoutside. Unknown debía devolver benchmark; cobertura terminó 100% conocida, por lo que esta rama no fue necesaria en datos reales. No se eliminó arranque: primera predicción evidence_n=0; máximo 1075 labels maduros dentro de ventana.

## Scores: menor es mejor
Brier multiclase=sum(p-y)^2; logloss=-log(p_label). Delta=modelo−benchmark: positivo es PEOR.

| Modelo | Brier global | Logloss global |
|---|---:|---:|
| base | 0.628630 | 1.034203 |
| trend | 0.630654 | 1.037788 |
| pivot | 0.631770 | 1.039421 |
| combined | 0.634620 | 1.044082 |

Pivot−base: ΔBrier+0.003139258, Δlogloss+0.005217032. Combined−trend: +0.003966410,+0.006294837. Trend tampoco supera base: +0.002023169,+0.003584009. Por tanto la conclusión no depende de haber escogido un benchmark de tendencia demasiado fuerte: fallan incluso contra la climatología.

| Año origen | Válidos | Ambiguos | Censurados | ΔBrier pivot−base | ΔLL pivot−base | ΔBrier combined−trend | ΔLL combined−trend |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2020 | 468 | 0 | 0 | 0.002092 | 0.009282 | 0.003722 | 0.011365 |
| 2021 | 2190 | 0 | 0 | 0.004539 | 0.005504 | 0.005705 | 0.007735 |
| 2022 | 2189 | 1 | 0 | 0.003491 | 0.005236 | 0.004186 | 0.006346 |
| 2023 | 2189 | 1 | 0 | 0.000547 | 0.001072 | 0.001354 | 0.001299 |
| 2024 | 2196 | 0 | 0 | 0.003844 | 0.006549 | 0.004716 | 0.007281 |
| 2025 | 2179 | 0 | 5 | 0.003497 | 0.006858 | 0.003920 | 0.007732 |

2020 sólo desde 15 octubre; 2025 hasta 30 diciembre. Las cuatro columnas principales son positivas en TODOS los años, sin seleccionar sólo años favorables.

| Estado | Emitidos | Peso | Válidos | ΔBrier pivot−base | ΔLL pivot−base | ΔBrier combined−trend | ΔLL combined−trend |
|---|---:|---:|---:|---:|---:|---:|---:|
| M | 9336 | 81.77% | 9330 | 0.001076 | 0.001542 | 0.001524 | 0.002238 |
| U | 1247 | 10.92% | 1246 | 0.010741 | 0.018045 | 0.013803 | 0.021480 |
| D | 835 | 7.31% | 835 | 0.014846 | 0.027134 | 0.016583 | 0.028964 |

M significa mezcla/rango con escalas disponibles, NO unknown. La persistencia y dominancia deM(~82%) reducen diversidad;U/D son menos frecuentes y muestran mayor deterioro. No borrar U/D o conservar sólo M después de ver esto. Existen algunas celdas año×estado favorables (p.ej.U 2023 en ambos scores), pero no rescatan resultado global/año y no autorizan un filtro retrospectivo. Todas las intersecciones están en summary.json.

Cohorte00 UTC, 1903 episodios sin solapamiento de sus propios horizontes 24h: pivot−base ΔBrier+0.001868103,ΔLL+0.005228328; combined−trend+0.002859519,+0.005786550. El pronosticador sigue entrenando con episodios 4h solapados y los estados persisten: esta cohorte es un control descriptivo, no 1903 ensayos IID ni OOS independiente.

## Cobertura, clases y ambigüedad
Emitidos 11418 de 11418 slots; estructura conocida 11418; ausencias ATR/4h = 0; missing_or_invalid = 0 en todos los años/estados. Válidos 11411(99.94%),ambiguos 2(0.0175%),censurados 5(0.0438%). Clases válidas up 4805, down 4673, none 1933. Ambiguos:1 en 2022 estado M y 1 en 2023 estado U; censura 5 en 2025 estado M. Los años 2020/21/24 no tienen exclusiones.

Cobertura íntegra exige 1440 min del horizonte incluso tras primer toque. Open fuera de barrera resuelve primero; open dentro con ambas mechas significa ambiguo; no se inventó orden intraminuto. Labels, incluso toques tempranos, sólo entran al deadline 24h. La API devolvió reloj completo; eso NO demuestra ausencia de relleno/sintetización anterior del proveedor ni valida procedencia de cada vela. Tampoco establece missing-at-random para otros datasets.

Bounds globales incluyendo ambos órdenes compatibles de ambiguos:
- Pivot−base: Brier[+0.003125107,+0.003149535],LL[+0.005197863,+0.005227504].
- Combined−trend: Brier[+0.003948379,+0.003978075],LL[+0.006269742,+0.006304516].
Incluso la asignación más favorable de los dos ambiguos no cambia signo. No son intervalos de confianza ni solucionan posibles datos no observados.

## Calibración
Se guardaron 60 celdas: 4 modelos × 3 clases × 5 bins fijos. No hay evidencia de probabilidades estructurales bien calibradas:
- pivot/up,bin[.2,.4):n2660,media0.37277 frente frecuencia0.43797;bin[.4,.6):n8600,media0.43994 frente0.41407.
- pivot/down,[.4,.6):n6850,media0.43129 frente0.40832.
- pivot/none,[.2,.4):n2115,media0.22271 frente0.18156.
- combined/none,[.2,.4):n2698,media0.22457 frente0.16716.
Base tampoco está perfectamente calibrado: base/up,[.4,.6),n9002,media0.43663 frente0.42213. Celdas pequeñas no permiten certezas; no se recalibró ni cambió bins tras resultados. Tabla íntegra en calibration.csv/summary.json.

## Controles y auditoría del resultado
Prototipo previo leído entero e inalterado.13 controles sintéticos originales PASS,11 adicionales PASS (paridad vectorizado/incremental de 5 labels/casos de apertura; missing; maduración; expiración;unknown;prefijo tendencia). Son controles de corrección, no evidencia de edge.

Fullrun único a3d3904dcb764db4b987fa0be7883d7d succeeded exit0,00:31:54–00:32:42UTC. No se repitió tras ver scores. Probe inicial23a773a45f3441c08b262e6dbb4c326b falló por asumir que warmup=0devuelve ndarray; se corrigió ese control de contrato, sin cambiar modelo/labels. Probe finalcb952386b5884263bb92caf9ddeada75 succeeded.

Auditoría de artefactos ec58a9386a9f4151b3c1ac8764d28548 succeeded:11.418 vectores reproducidos exactamente con sólo cola de etiquetas maduras, evidence_n idéntico, scores/calibración recalculados exactamente y todo pivot confirmado≤origen. Leyó sólo forecasts persistidos, ninguna nueva query de mercado. Reusa la misma implementación de estimador/scoring; no equivale a una segunda implementación estadística independiente.

Persistencia en host Jesse, no workspace de asistente:
- research_scripts/fresh_structure_probability/observer_evaluation_v1.py
- research_scripts/fresh_structure_probability/output_v1/forecasts.jsonl
- research_scripts/fresh_structure_probability/output_v1/summary.json
- research_scripts/fresh_structure_probability/output_v1/manifest.json
- research_scripts/fresh_structure_probability/output_v1/artifact_audit.json
- research_scripts/fresh_structure_probability/calibration.csv
- research_scripts/fresh_structure_probability/audit_api_controls.json
- research_scripts/fresh_structure_probability/adapter_controls.json

## Decisión
ARCHIVAR el recipe congelado 1D / 4h+pivots+first-touch±ATR 24h con conteos 180 días / shrink 20. No promover, no transformar argmax en órdenes, no variar parámetros para rescatarlo y no abrir 2026. Mantener baseline principal y sus metas.2020–25 ya se exploró extensamente: esto es desarrollo adaptativo, no OOS limpio. El hallazgo útil es eliminar una vía que añadió complejidad sin mejorar probabilidades, no declarar probado ningún sistema alternativo.
