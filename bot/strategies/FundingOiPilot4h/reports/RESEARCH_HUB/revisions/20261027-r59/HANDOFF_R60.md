# Handoff a r60 (desde r59, 2026-10-27)

## Estado
- **Candidata sin cambios:** P-r55 (`../20261026-r55/P55_FREEZE.md`).
- **Contadores:** N = 145; N_régimen = 38; N_temática = 19.
- **Datos reservados:** 2025 sellado y 2026 reservado.
- **Holdout H = N2 ∪ N3:** solo se lee con `research_scripts/r59_oracle.py`. Lleva 1 de 5 consultas usadas (q0 = r58 F2), así que **quedan 4**. Log en `../../holdout/ORACLE_LOG.jsonl`.

## Hallazgos vigentes
1. **La ventaja que sobrevive a la selección es R1,** la tendencia diaria con objetivo de vol (F1, SPA contra cash p 0,002–0,015).
   - Lo que suman C6 y las variantes posteriores sobre R1 sola **no** supera la selección (p 0,23 / 0,29).
   - Lo esperable fuera de muestra es el Sharpe de R1 (1,2 a 1,5 según la ventana), no el 1,72 de P-r55.
2. **Las variantes de cartera de r50–r58 son intercambiables:** correlación de 0,91 a 0,95 y PBO de 0,58 a 0,63. Optimizar más P-r55 tiene retorno esperado ~0.
3. **Funding no saturado | compresión** pasa el prefiltro en U50 (p1 +0,31; p2 p 0,0135).
   - Está **sin consultar en H**, porque el poder contra la mitad del efecto da 0,36.
   - La clase saturada no aparece en 2022, así que la variable se mezcla en parte con el régimen.

## Lo que no hay que repetir
- **Más variantes de P-r55** que retoquen la construcción o sumen activos: el PBO muestra que se elige entre ruido.
- **Mirar H fuera del oráculo**, o sumarle consultas sin commitear antes el criterio.
- Todo lo listado en `../20261027-r58/HANDOFF_R59.md`.

## Ideas para r60, en orden (a criticar)
1. **Decisión del usuario sobre 2025.** Hacer la mirada preregistrada a P-r55 completa y a R1 sola, lado a lado. F1 sugiere que lo que hay que medir es si C6 suma sobre R1 fuera de muestra.
2. **Simplificación:** R1 sola contra P-r55, como pregunta de diseño (menos piezas, mismo Sharpe esperado tras la selección). La decide el usuario; no hace falta otra ronda de búsqueda.
3. **Si se quiere usar q1 igual:** antes, proteger `data/r58/f0_days.npz` y separar sus columnas de U50. Después, commitear el criterio y aceptar un poder de ~0,36 contra la mitad del efecto. Como el efecto es casi un régimen, conviene más ponerlo a prueba en 2025, si se abre.

## Reutilizable
- **`research_scripts/r59.py`:**
  - `cv` (grupo × año), `rotation`/`rotation_p` (con estratos) y `f2_prefilter`;
  - `save_series`/`load_series` y `spa_pvalue`/`pbo`;
  - `f1_build`/`f1_audit`, que corren de nuevo sobre el almacén.
- **`research_scripts/r59_capture.py`:** reconstruye las curvas de cualquier script congelado, en un contenedor de solo lectura.
- **`data/r59/series/`:** 149 series de r50–r58 más las varas `BENCH_P55_*` y `BENCH_R1_*`. **Desde r59, toda variante nueva guarda su serie al correr.**
