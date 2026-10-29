# X03 R2 — validación condicional de referencias X03

El incremento neto frente a controles permanece positivo bajo costes estáticos, pero la regularidad objetivo ya falla a +5bps RT. El remuestreo no demuestra ausencia de sobreajuste: X03 fue seleccionado tras búsquedas previas sobre los mismos datos, B/C comparten mecanismo y muestra, y 2026 sigue cerrado.

Job exitoso11b3b51b8d2e4f8395c622b1ac986b0c. Cuatro referencias y cuatro anchors; métodos de fills y MTM de BTC_R1_COST_CALENDAR_SOURCE_20261019.md. Código reproducible en X03_R2_VALIDATION_ANALYSIS_SOURCE_20261019.md; datos íntegros en X03_R2_BASELINE_BOOTSTRAP_DATA_20261019.md. Primer intento b8b02f7f4e924618bf28ec30ed2f4f1f falló en fake sin symbol; corregido sólo el harness. Sin cambio de fuentes trading por ese fallo.

## Bootstrap pareado

10.000 réplicas de bloques circulares de3meses, seed20261019. Índices comunes para carteras y costes; no agrupar B/C. Sensibilidad bloque6 guardada íntegra. Unidad: incremento mensual MTM en USDT de X03 menos control, preservando capital/sizing observados; no retorno compuesto de estrategia nueva. Todas las bandas son condicionales a la muestra empírica reutilizada.

| Cartera | Bins | Extra bps RT | Media observada USDT/mes | Percentiles2.5/50/97.5 de media |
|---|---|---:|---:|---|
| B | full61 | 0 | 48.92 | 9.27 / 49.45 / 90.73 |
| B | full61 | 5 | 44.38 | 4.87 / 44.86 / 86.01 |
| B | full61 | 10 | 39.84 | 0.55 / 40.39 / 81.25 |
| C | full61 | 0 | 49.22 | 9.77 / 49.69 / 90.56 |
| C | full61 | 5 | 44.66 | 5.55 / 45.20 / 85.67 |
| C | full61 | 10 | 40.11 | 1.18 / 40.58 / 80.90 |
| B | partial63 | 0 | 43.33 | 3.84 / 43.33 / 84.82 |
| B | partial63 | 5 | 38.79 | -0.60 / 38.74 / 79.92 |
| B | partial63 | 10 | 34.24 | -4.81 / 34.26 / 75.33 |
| C | partial63 | 0 | 43.30 | 4.13 / 43.35 / 84.34 |
| C | partial63 | 5 | 38.71 | -0.38 / 38.73 / 79.73 |
| C | partial63 | 10 | 34.12 | -4.86 / 34.12 / 74.97 |

Con61meses completos los límites inferiores permanecen positivos, también con bloques6. Incluyendo63bins y fronteras, las bandas de+5y+10 cruzan0. La dependencia de fronteras debe mostrarse, sin declarar significativo el caso más favorable ni elegir longitud de bloque por resultado. La fracción positiva de réplicas guardada es una frecuencia empírica condicionada, no probabilidad de no sobreajuste.

## Dependencia temporal

La mejora MTM nominal por año es positiva en2021/2022/2023/2025, negativa en2024 y parcial2020. Aproximadamente77% del incremento de cartera proviene de2022+2025, diferente del~80% del neto de suplementos cerrados. La contribución de otras patas y los desplazamientos son endógenos.

| Año | ΔMTM B nominal | ΔMTM C nominal | ΔMTM B +10 | ΔMTM C +10 |
|---|---:|---:|---:|---:|
| 2020 parcial | -69.18 | -69.18 | -70.52 | -70.52 |
| 2021 | 463.20 | 453.98 | 443.24 | 434.86 |
| 2022 | 839.26 | 827.32 | 758.05 | 747.32 |
| 2023 | 389.17 | 428.61 | 211.47 | 251.97 |
| 2024 | -163.77 | -169.92 | -255.69 | -264.45 |
| 2025 | 1271.36 | 1257.24 | 1070.63 | 1050.31 |

Eliminar aritméticamente cualquier año deja suma incremental positiva; el caso mínimo elimina2025: a+10bps quedan1086.54USDT B y1099.18USDT C. Esto no es backtest reejecutado sin ese año ni validación temporal independiente: conserva trayectorias endógenas de capital observadas y utiliza meses ya conocidos.

Los siete vecinos son pruebas de sensibilidad excluidas de selección. La matriz completa, los costes y las pérdidas deben reportarse sin elegir parámetros ganadores. QA156checks verificó invariantes de código y causalidad controlada; no valida capacidad predictiva, paridad de proxies o liquidez. No se ejecutó MCmultiasset porque documentación no garantiza correlaciones ni semillas compartidas; no se constató fallo de runner y no se atribuye ninguno.
