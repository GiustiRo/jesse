# r52 F1: ranking transversal semanal sobre 50 perpetuos (2026-10-26)

**Resultado:** ninguno de los 4 ensayos pasa. N pasa de 109 a 113.

**Hallazgo central:** el ML sí ordena las monedas mejor que el azar.
- X1 tiene un IC semanal por rangos de 0,106 (t = 5,6).
- La mediana del spread entre quintiles es +0,73% semanal.
- Pero las subas explosivas de unas pocas monedas en la pata corta se comen la ganancia: el spread *medio* es de apenas +0,07% semanal. Es el riesgo de salto de la pata corta que anticipaba la literatura.

Protocolo: `PROTOCOL_R52.md` F1 (`840747c3`). Código: `r52_xs.py` (`d2719e1b`).
- Corrección hecha antes de cualquier resultado de F1 (`7707c399`): la vol faltante de monedas con huecos de datos se completa con la mediana de la semana.
- F0 verificado (`verify.json`):
  - las velas 1h de vision coinciden con Jesse en 43.799 de 43.800 horas;
  - el funding es idéntico a los datasets de r50;
  - rankings aleatorios con 8 semillas dan Sharpe medio de 0,12 (rango −0,3 a 0,76).

## Resultados (desarrollo 2021-05 → 2023-12; validación 2024; 2025 sellado)
| Ensayo | Sharpe neto (desarrollo) | CAGR | DD | Costos ×2 | 2024 | ρ con P1 | IC semanal (t) | Monedas antiguas (20) | Pasa |
|---|---|---|---|---|---|---|---|---|---|
| X0 momentum 1/4/12 semanas | −0,37 | −10,5% | −41% | −0,54 | −0,43 | 0,03 | −0,051 (−2,9) | 0,09 | no |
| X1 elastic net | −0,02 | −2,6% | −28% | −0,17 | −0,30 | −0,21 | 0,106 (5,6) | −0,34 | no |
| X2 gradient boosting | 0,17 | 1,4% | −21% | −0,05 | 0,24 | −0,21 | 0,083 (5,1) | −0,47 | no |
| X3 = X2 solo largo, cubierto con BTC/ETH | 0,15 | −0,3% | −46% | 0,02 | −0,04 | −0,02 | — | — | no |

**Diagnóstico de X1** (equal weight, 137 semanas):
- quintil superior +0,49% semanal contra quintil inferior +0,42%;
- mediana del spread +0,73%, con 52,5% de semanas positivas;
- Sharpe anual del spread medio: 0,08.

## Lectura
1. **Hay información, pero falta la forma de cobrarla.** En 50 monedas líquidas, las colas de los retornos semanales anulan la media del spread.
2. **El momentum semanal se revierte en este universo:** X0 tiene IC negativo (t −2,9).
3. **El ML supera claramente al momentum simple:** entre 0,35 y 0,54 más de Sharpe. X2 es positivo en 2024.
4. **El sesgo de supervivencia no explica el resultado:** las 20 monedas más antiguas tampoco ganan.

## Archivos
- `research_scripts/r52_xs.py`
- `research_scripts/data/r52/xs.json`
- `research_scripts/data/r52/verify.json`
- `research_scripts/data/r52/manifest.json`

Guardado el 2026-10-26, después de la caída de red de Docker Desktop. El texto se fijó cuando terminó la fase.
