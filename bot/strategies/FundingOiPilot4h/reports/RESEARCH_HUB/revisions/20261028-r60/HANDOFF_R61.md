# Handoff a r61 (desde r60, 2026-10-28)

## Estado
- **Candidata sin cambios:** P-r55. **N = 148**; N_régimen = 38; N_temática = 19.
- **Datos reservados:** 2025 sellado y 2026 reservado.
- **Holdout H = N2 ∪ N3:** 1 de 5 consultas usadas, **quedan 4**. r60 no lo leyó.
- **Advertencia:** H ya se usó para rupturas de C6 en alts (q0, r58).

## Hallazgos de r60
1. **El ranking entre monedas no agrega nada sobre la construcción.** Con puntajes rotados, el libro K de X1 da 1,16 de media, contra 1,05 con los puntajes reales (p 0,59). Rotar destruye la información de timing del puntaje, y aun así el Sharpe se mantiene.
2. **La construcción K tiene Sharpe estructural en D:** ~1,1 de media con patas al azar, p5 0,50, positiva en el 100% de 100 rotaciones, con ρ ≈ 0 contra R1 y P-r55.
   - Sale de tres asimetrías: el stop de 2σ en los cortos (en efecto, largo en las rupturas intrasemana), la exclusión de cortos con funding 7 d < 0 (en efecto, largo en esas monedas) y la cobertura beta contra BTC.
   - Ninguna pieza sola alcanza: sin las tres da ~0.
3. **La cola del L/S de r52 son rupturas graduales:** el stop alcanza el 94% de las peores moneda-semanas cortas.
4. **SPA de la familia transversal:** L1 contra cash p 0,143; la combinación con R1 contra R1, p 0,61. El eje ya acumula 15 ensayos.
5. **Unlocks:** con datos gratis no alcanza (23/48 monedas, 4/10 coincidencias entre fuentes, calendarios reconstruidos). Línea cerrada.
6. **Capacidad:** ~2 M USDT con posiciones ≤ 1% del volumen diario.

## Propuesta para r61 (a criticar)
**Preregistrar el «libro de asimetría neutral» y confirmarlo en H:**
- Cada semana, sobre todas las alts elegibles:
  - largo en la alt desde el primer cierre 1h que supere +2σ_sem sobre el cierre del domingo, hasta el cierre del domingo siguiente;
  - largo toda la semana en las alts con funding 7 d < 0, si el usuario habilita el funding como señal de entrada;
  - cobertura beta 60 d con el perpetuo de BTC;
  - pesos inversos a la vol; costos, funding y stop como en K; ningún parámetro nuevo.
- Es el límite determinista de K con patas al azar. Hay que comprobarlo con una aserción: el promedio de K sobre muchas rotaciones tiene que aproximarse a este libro.
- **Antes de correr:**
  - **decisión del usuario** sobre la regla r49 (funding solo como freno). Sin la pata de funding, solo queda la continuación de rupturas;
  - verificar cuánto se parece a C6 en las alts (r54/r58) y decidir si es una variante de C6, que hereda su historial de selección, o una manga nueva;
  - criterio q3 commiteado, con poder ≥ 0,4 y la advertencia de q0.
- **Puertas:** las de r60 (g1–g8), reemplazando p2 por un placebo de timing: desfasar la hora de entrada al azar dentro de la semana manteniendo el número de entradas.

## Lo que no hay que repetir
- Más rankings L/S (X/Y/ML/L): son 15 ensayos y ninguno supera la selección.
- Variantes de K con otros k, ventanas o filtros sobre los mismos datos de D.

## Reutilizable
`research_scripts/r60.py`:
- `Panel`, `FastBook` (construcción K vectorizada, verificada contra `Book`);
- `coin_rows`/`rotate` (rotación transversal) y `predict_wf_split`;
- `q2_compute`/`q2_power`/`q2_selftest` (plantilla de consulta sobre un banco);
- `f3` (SPA/PBO de familia, con `pbo_cscv` sin base de datos).

En `r59_oracle.py`, el modo `schema`.
