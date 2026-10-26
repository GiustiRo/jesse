# Handoff a r56 (desde r55, 2026-10-26)

## Estado
- **Candidata:** P-r55 = P1 sin R1/bono ([`P55_FREEZE.md`](P55_FREEZE.md)).
  - R1 en BTC, ETH, oro, SPX, WTI y gas, más C6 en BTC/ETH; construcción de r50 F2.
  - 2018-09→2024: Sharpe 1,677. 2021–24: Sharpe 1,723.
  - Todas sus mangas están confirmadas en Jesse (r51 F1).
- **N = 140.**
- **2025 sellado:** se abre una sola vez, para un candidato **nuevo** preregistrado y con autorización explícita del usuario.
  - Para P-r55 no es informativo: su 2025 ya se conoce desde r50/r51.
- **2026 reservado.** Es el único fuera de muestra limpio de P-r55.

## Reglas vigentes
- Solo perpetuos USDT-M de Binance; sin live, paper ni Pi.
- Preregistro antes de mirar. Cada ensayo se registra en `TRIAL_REGISTRY.json` antes de leer su resultado.
- Reportar al usuario al cierre de cada fase.
- Los scripts corren en el contenedor de investigación: `docker exec -w /src/bot jesse-research-jesse-1 python research_scripts/<script> run`.

## Lo que deja r55
1. **Regímenes de BTC** (`r55_regimes.py`, k = 0,5).
   - Etiqueta trimestral ex post para juzgar y estado causal T90 para operar.
   - Reutilizables tal cual. Cambiarlos sería una variante nueva.
2. **Diagnóstico de P1 por régimen:**
   - la debilidad está en los laterales de 2021–24 (−2,3%) y en la mediana de los bajistas;
   - R1 cripto resta y C6 suma en todas las clases;
   - el estado causal llega tarde a los bajistas (36%).
3. **El intercambio de R1 cripto:**
   - captura los alcistas (2019–2020);
   - pierde en los bajistas y en los laterales.
   - Ni recortarlo por régimen (E2) ni quitarlo (E1) mejoran la cartera completa.
4. **ML3**, el resultado más prometedor:
   - C6 congelado en las 48 alts de U50, que solo abre si la moneda está en el top-10 del puntaje X1 de esa semana;
   - reemplaza la mitad del riesgo de C6 en P1;
   - cumple la inclusión (+0,06 / +0,17) y su canasta da 1,31 contra 0,85 de V1;
   - **falla la puerta bajista** (suma 10,1% contra 13,2%), su mejora viene casi toda de 2024 y la manga va escalada ~10 veces sobre 429 trades.
5. **Lo que no hay que repetir:**
   - libros largos top-k cubiertos con BTC o BTC/ETH (ML1, ML2, Y4);
   - ranking como tamaño en C6 (ML4);
   - seguro corto en BTC por régimen (E3);
   - el veto AR(1) de A3;
   - plata, cobre, EWY y EWJ en R1.

## Agenda propuesta para r56 (la decide el usuario; preregistrar antes de correr)
1. **Validación única de ML3 en 2025.**
   - ML3 congelado sin cambios (`r55_ml.py`: `make_mult('ML3')` y `c6_prime`), dentro de P-r55 en lugar de P1.
   - Puertas fijadas antes de mirar: Sharpe de la manga > 0, ningún derrumbe, y la cartera con ML3 no peor que P-r55 en 2025.
   - Consume la mirada sellada de 2025, así que requiere autorización.
   - Antes conviene una sensibilidad sin costo de N: ML3 con escala limitada (por ejemplo, un techo de 5×), solo como diagnóstico declarado, para saber cuánto depende del apalancamiento.
2. **Alternativa a ML3 sin consumir 2025:** validarlo en monedas fuera de U50 (perpetuos activos con menos volumen) con el mismo puntaje re-entrenado. Exige ampliar los datos de `r52_download.py`.
3. **El intercambio de R1 cripto** sigue abierto. Toda idea nueva tiene que capturar alcistas sin depender de una señal de régimen lenta: por ejemplo, salidas más rápidas propias de R1 en cripto, preregistradas como variante de R1 (cuentan en N).
4. **A3:** solo con una idea de quiebre que no sea una prueba estadística lenta. Si no la hay, queda archivado.

## Archivos clave
- Protocolo y enmiendas: [`PROTOCOL_R55.md`](PROTOCOL_R55.md).
- Informes: `strategies/FundingOiPilot4h/reports/R55_PHASE0…4_RESULTS_20261026.md` y `R55_CLOSE_20261026.md`.
- Scripts: `research_scripts/r55_regimes.py`, `r55_engine.py`, `r55_ml.py`, `r55_a3.py` y `r55_portfolio.py`.
- Datos: `research_scripts/data/r55/` (los `*.npy` están en gitignore y se regeneran).
