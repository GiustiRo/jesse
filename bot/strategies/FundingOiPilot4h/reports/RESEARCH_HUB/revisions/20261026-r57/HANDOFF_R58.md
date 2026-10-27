# Handoff a r58 (desde r57, 2026-10-26)

## Estado
- **Candidata sin cambios:** P-r55 (`../20261026-r55/P55_FREEZE.md`).
- **Contadores:** N = 143; N_régimen = 38.
- **Datos reservados:** 2025 sellado y 2026 reservado.
- **Usos continuos de r56 probados y descartados:**
  - U1 (vol pronosticada en el tamaño de R1 cripto);
  - Q2 (M2a en alts con p(rango) alto).
  - F3 (C6 con selección por T3) no corrió, porque el diagnóstico no lo respaldó. Ver `../../../R57_CLOSE_20261026.md`.

## Agenda propuesta para r58, en orden (cada variante suma N)
1. **C6 en alts filtrado por la compresión de la vol pasada.**
   - Hipótesis post-hoc de F1: la persistencia en compresión da +0,61 R, contra −0,08 en el resto.
   - **Cómo probarla:** preregistrarla y confirmarla una sola vez en las 20 monedas de N2, donde C6 nunca corrió. Recién si pasa N2, construcción ML3 dentro de P-r55 con las puertas r55.
   - **Advertencia:** es pariente de ML3, que falló la puerta bajista.
2. **C6 sin entradas cuando p(rango a 40 días) es alto.**
   - Hipótesis post-hoc de F1: −0,19 R contra +0,41.
   - Misma prueba en N2. Puede combinarse con 1 en una sola variante, si se declara antes.
3. **DVOL como insumo,** ya bajado en `data/r58/dvol_{BTC,ETH}_1d.csv` (gitignore; se regenera con `r57_dvol_probe.py`).
   - **Primero, sin N:** ¿la prima DVOL − RV pronosticada (T3) anticipa las rupturas de C6 en BTC/ETH, o la vol realizada a 20 días mejor que T3? Si es pronóstico, cuenta en N_régimen.
   - **Advertencia:** solo hay dos monedas y empieza en 2021-03. Tiene poco poder.
4. **Lo que no hay que repetir:**
   - usar el pronóstico de vol para **reducir** el tamaño de una manga de ruptura (U1);
   - reemplazar riesgo de C6 por reversión diaria (Q1/Q2).

## Reutilizable
- `research_scripts/r57.py`:
  - `states` (particiones T3, persistencia, P5 y cociente con sesgo, también para N2);
  - `diag` (bootstrap por semana);
  - `u1` (subclase de `DonchianEnsR49` con multiplicador);
  - `rev` (M2a con compuerta, barras diarias desde 1h, U50 y N2).
- C6 todavía no corrió en N2. El loop de `r55_ml.c6_alts` sirve si se cambia `r54_v1.DATA` a `data/r56/n2` (así lo hace `r57.rev_book`).
