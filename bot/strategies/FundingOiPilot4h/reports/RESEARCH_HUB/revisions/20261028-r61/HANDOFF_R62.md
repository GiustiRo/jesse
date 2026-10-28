# Handoff a r62 (desde r61, 2026-10-28)

## Estado
- **Candidata sin cambios:** P-r55. **N = 150**; N_régimen = 38; N_temática = 19; familia C6 en alts = 11.
- **Datos reservados:** 2025 sellado y 2026 reservado.
- **Holdout H = N2 ∪ N3:** 1 de 5 consultas usadas, **quedan 4**. r61 no lo leyó. El criterio q3 sigue registrado en `r59_criteria.py`, sin consultar; no reutilizarlo con otra variante sin un protocolo nuevo.
- **Advertencia:** q0 (r58) ya usó H para rupturas de C6 en alts.

## Hallazgos de r61
1. **En D, estar largo en cualquier alt de U50 con cobertura beta contra BTC da ~1,6 de Sharpe.** Es el sesgo de supervivencia. La ruptura de +2σ no agrega timing (placebo p 0,69). Ningún libro de alts juzgado solo en D sirve como evidencia.
2. **K de r60 contiene un L/S de funding neutral en dólares** (enmienda E1): largo en las alts con funding 7 d < 0 y corto en las no hacinadas, por la renormalización de la pata corta. Su forma límite da 2,6 en D (sin costos ni varianza de patas). Es post hoc, y en D está contaminado por haberlo visto.
3. **El funding negativo como entrada aporta frente al azar** (p 0,008), pero como largo puro es una cola: 80% del PnL en 5 semanas y DD −48%.
4. **Libros A/B:** ρ ≈ 0 con R1 y P-r55, ρ 0,18–0,29 con C6alts. Suman +0,4 sobre R1 + C6alts en D, pero fallan las puertas de concentración (g5) y el DSR de la familia (B).

## Propuesta para r62 (a criticar)
**Opción 1, recomendada: el L/S de funding neutral en dólares, juzgado solo en H.**
- Cada semana, largo en las alts con funding 7 d < 0 y corto en las demás alts elegibles, con pesos inversos a la vol, cada pata con 0,5 de bruto, beta neutral, el stop 2σ de los cortos y ningún parámetro nuevo. Es la forma operable de la pieza E1.
- **En D solo se corre como diagnóstico, sin puertas.** D ya está vista y tiene sesgo de supervivencia, que en un L/S perjudica a los cortos.
- **La única prueba es q3' en H:** criterio y poder commiteados antes, ρ con R1 y con B de r61 como márgenes, y la advertencia de q0.
- **Crítica:** H también tiene sesgo de supervivencia (son monedas que hoy cotizan). La pieza salió de mirar D, y un funding negativo generalizado (como en 2022) concentra el libro en pocas semanas.

**Opción 2: cerrar la línea de alts.** Llevar la búsqueda de la segunda fuente a otro eje: carry/basis de BTC y ETH, o activos fuera de cripto ya cargados (r50/r51). Es la opción conservadora si el usuario no quiere gastar otra consulta en la familia.

## Lo que no hay que repetir
- Libros de alts largos (o sesgados al largo) juzgados en D: el sesgo de supervivencia da ~1,6 a cualquier entrada al azar.
- Más disparos de ruptura sobre los mismos datos.
- Rankings L/S (15 ensayos en r52–r60).

## Reutilizable
`research_scripts/r61.py`:
- `AsymBook`, con el motor exacto y el simplificado vectorizado sobre sorteos;
- `expected_weights` (pesos esperados exactos de K);
- `c6_basket(syms, src_of)`: C6 congelado sobre cualquier banco;
- `q3_compute`/`q3_selftest` (plantilla de consulta con C6alts del banco).

Para lo que importa `r50_harness`, el contenedor descartable se une a `jesse-research_default` con `JESSE_ENV_FILE=/src/bot/.env.research`.
