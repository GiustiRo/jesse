# Handoff a r63 (desde r62, 2026-10-29)

## Estado
- **Candidata:** P-r55, sin cambios.
- **Contadores:**
  - **N = 155**; N_régimen = 38; N_temática = 19; familia C6 en alts = 11.
  - **N_fab = 1.614**, con techo de 3.000 por ronda de fábrica y N_eff de 65. Está en `TRIAL_REGISTRY.json` → `factory_trials`.
- **Datos reservados:** 2025 sellado y 2026 reservado.
- **Holdout H:** 1 de 5 consultas usadas, **quedan 4**.
  - El criterio q4 quedó registrado en `r59_criteria.py`, sin consultar; `data/r62/q4_program.json` todavía no se escribió.
  - No reutilizar q4 con otro programa sin un protocolo nuevo.

## Hallazgos de r62
1. **La fábrica cobra bien la búsqueda.** Su calibración (F1) es reutilizable: con ~1.600 programas, el ruido da Sharpe 1,4–1,6 en desarrollo y el SPA lo descarta (p 0,16–0,27).
2. **En datos reales no apareció nada fuera del rango del ruido:** SPA p 0,30 contra cash y 0,63 marginal.
3. **Pista más concreta:** `voljump` en cripto 1 h, con rotación p 0,005 y ρ baja con R1. El mejor t individual es 3,25, contra un umbral de 4,0. Ya está vista en D: si se quiere probar, tiene que ser en datos nuevos.
4. **La potencia es limitada para ventajas moderadas y concentradas** (P1 de F1 no apareció).
5. **Datos gratis de cascadas:** las liquidaciones USDT-M están borradas. Lo que queda es el OI de metrics (BTC desde 2020-09, ETH desde 2021-12) y las liquidaciones COIN-M 2023-06→2024-10.

## Propuestas para r63 (a criticar)
**Opción 1, recomendada: aceptar P-r55 como cartera y pasar a robustez operativa.**
- Después de r59–r62, la búsqueda de una segunda fuente en D devolvió tres negativos con métodos distintos: a mano, rankings y fábrica.
- El próximo paso con más valor esperado no es buscar más, sino preparar P-r55 para el momento en que el usuario decida abrir 2025:
  - costos reales;
  - ejecución;
  - un plan de monitoreo.

**Opción 2: `voljump` cripto 1 h, juzgado solo en H.**
- Usar el finalista congelado de `runs/real_f2/final.json` (celda `rho1|hold1|long` u otra `voljump`), sin tocar parámetros.
- Gasta 1 consulta con q4 en las 50 alts H a 1 h, con su poder calculado antes de consultar.
- **Crítica:** en la fábrica no se distinguió del ruido. Gastar el oráculo en lo mejor de una búsqueda que no pasó el SPA es una apuesta de baja probabilidad, y H también tiene supervivencia.

**Opción 3: otra fábrica sobre un DSL distinto.** Por ejemplo, basis/carry, o datos que hoy no tenemos.
- Cada ronda suma N_fab y vuelve a mirar los mismos años.
- Requiere datos nuevos para valer la pena.

## Lo que no hay que repetir
- Otra búsqueda grande sobre el mismo DSL y los mismos datos de 2018–2024.
- Leer un Sharpe ~1,5 de una búsqueda grande como evidencia.
- Libros de alts juzgados en D (r60/r61).

## Reutilizable (`bot/research_scripts/`)
- `r62_dsl.py`:
  - DSL;
  - simulador maker/taker con barras de 1 h;
  - fees y slippage por activo.
- `r62_eval.py`:
  - `Panel` y `Evaluator` (pliegues grupo × año, e1/e2/e3, casilleros);
  - `spa_fast`, equivalente a `r59.spa_pvalue` y vectorizado.
- `r62_factory.py`, `r62_run.py` y `r62_step.sh`:
  - MAP-Elites;
  - búsqueda genética;
  - paquetes anonimizados con `leak_check`;
  - corrida paso a paso con un subagente entre pasos.
  - **Nota operativa:** correr el paso de cómputo (~30 s) en primer plano. No confiar en que el aviso de cierre del subagente llegue solo.
- `r62_synth.py`: historias de ruido, plantado y regímenes con el mismo formato que el panel real.
- `r62_liq.py`: OI de Binance metrics y su z horaria.
- `r62_data.py`: barras de 1 h y diarias de Dukascopy y perpetuos, con sha.
- **Series:** `r59/series/r62.npz` (round `r62`, 1.614 series en float32, con sha en el manifiesto).
