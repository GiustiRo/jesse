# Auditoría independiente V5 C2 y V6 C1

Autor: /root/audit. Resultado: **PASS documental**, con las limitaciones indicadas abajo. Lectura por MCP y escritura exclusiva de estos documentos; sin motores, jobs nuevos ni modificaciones de fuentes productivas o registros.

## Selecciones

V5 C2: ambas Funding pasan N≥30, neto>0, PF≥1,2 y |DD|≤25%. Los cinco campos N/neto/PF/DD/turnover coinciden exactamente con V5_C2_TRAIN_ACCOUNTING.json. Funding OI fue seleccionada por el primer criterio, |DD| 13,022950% frente a 15,723609% de FP. No hizo falta desempatar mediante PF, turnover u OI. No se utilizaron resultados de C2V.

V6: se reproducen los gates de las seis filas de V6_SCREENING_FINAL.json. Única elegible: Efficiency P (N148; PF1,247768; DD21,869573%; 2/3 años completos positivos). Efficiency OI falla PF/DD/años. Deleverage P falla neto/PF/DD y OI además años. NR7 P y OI fallan PF/DD: el mayor neto de NR7 P no permite promoverla. El año parcial 2020 no cuenta. Shortlist y C1 conservan únicamente Efficiency P.

C1 train V6 reutiliza exactamente el SCREEN nominal 2020-09-01→2024-01-01: mismo identificador, configuración, ventana y métricas de selección. [SCREEN Efficiency P](http://localhost:9200/#/backtest/8c8a2a0b-f3f9-4494-a557-7fbd2c5e0dd1).

## Cronología UTC

| Decisión / evidencia previa | Arranque asociado | Margen |
|---|---|---:|
| V5 selección C2 01:21:57 | [OI C2V](http://localhost:9200/#/backtest/6b6726e1-aea7-4b64-824d-a1cd2234fab9), start_requested_at 01:23:44.620 | 107,620 s |
| V5 selección C2 01:21:57 | [FP C2V](http://localhost:9200/#/backtest/b9581488-fa1a-4fb0-ad8a-925aaa434c80), start_requested_at 01:24:01.524 | 124,524 s |
| V6 shortlist guardada 01:25:19; selección C1 01:26:14 | [Efficiency C1V](http://localhost:9200/#/backtest/33180680-9dd0-44f1-a7a5-6fcf4ba0c363), recorded_at de start 01:26:25 | 66 / 11 s |

Todos los horarios corresponden al 2026-10-21. Las formas de evaluación preservan las ventanas previstas, configuración nominal, 4h, debug/fast y exports/benchmark false. Los duplicados V5 C2 de los dos progresos concuerdan. No se depende de la creación del draft ni de un orden dentro del mismo segundo.

El archivo contable V5 C2 se guardó a 01:21:58, un segundo después de seleccionar. El job existente 3ba4eb6de583476cb01e06f5af34cbe3 ya había terminado correctamente a 01:21:34, 23 s antes; las métricas de selección son idénticas a sus filas.

[V6 C2 TRAIN](http://localhost:9200/#/backtest/f3fb5ce3-f506-43d1-905d-4fde351caa1a) tiene recorded_at 01:27:56 y ventana train 2020-09-01→2024-07-01. Es entrenamiento: no debe confundirse con una evaluación C2 ni exigir una selección C2 previa a entrenar.

## Inmutabilidad

Readback por MCP de las 16 fuentes V5 y 14 V6: texto actual idéntico al snapshot congelado; los SHA guardados coinciden con los registros. Los 14 wrappers WF V5 y 7 V6 coinciden exactamente con sus manifests y conservan sólo herencia y fechas; los atributos coinciden con las verificaciones AST guardadas. No se repitieron compilación, hashes ni pruebas estáticas.

Fuentes: protocolos V5/V6, implementaciones congeladas, STATIC_VERIFICATION, REGISTRY_V5/V6, manifests CONFIRMATION_WRAPPERS y VERIFIED, screening final, selecciones y progresos/records de arranque. El JSON acompañante conserva pruebas por archivo y wrapper.

## Límites

El record V6 contiene recorded_at asociado al start y boolean start_requested; no ofrece timestamp independiente fraccional del inicio efectivo del motor. Los 11 s son margen documental. No se consultaron métricas de C1V V6 para esta auditoría ni se usaron retornos de evaluación para seleccionar.

Los snapshots contables y sus filas no sustituyen las auditorías sectoriales de logs/contadores. El código contable capturado usa trades y equity, sin acreditar logs incluidos. Tampoco se rehasheó independientemente la dependencia externa V2 fuera de los manifests V5/V6.

C3/C4 siguen fuera de esta auditoría; no se infiere elegibilidad futura ni calendario replay. V5_REPLAY_DESIGN.md quedó aclarado: el cashflow de funding del motor ocurre antes de la decisión calendar; la prioridad calendar sobre funding se refiere únicamente a la salida por indicador de funding adverso.
