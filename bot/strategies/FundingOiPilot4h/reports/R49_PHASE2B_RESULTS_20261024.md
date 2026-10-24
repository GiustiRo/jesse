# r49 Fase 2b: diagnóstico, lados largo/corto, ETH corto y petróleo (2026-10-24)

**Veredicto: no pasa r9.** La cartera fijada de antemano (protocolo B, commit `dbf538b1`) queda así:
- CAGR **29,98%** (falla por 0,02 pp), DD −18,4% ✓, Sharpe 1,41.
- Meses positivos ~62%: falla por ~3 pp.
- Trimestres positivos 75% (15 de 20): falla por 5 pp, es decir, un trimestre.
- DSR con N=55: 0,79 (falla por 0,16).

**Lado corto:**
- El corto **pierde en los tres activos** y la regla B4 deja los tres en solo-largo.
- ETH solo-corto pierde (Sharpe −0,26) y no entra.
- La manga de petróleo quedó fuera: HistData no publica WTIUSD M1 después del 2023-12-01.

## A. Diagnóstico 2021–22 (resumen)
El detalle está en `RESEARCH_HUB/revisions/20261024-r49/PHASE2B_PROTOCOL.md`.
- 5 de los 6 trimestres negativos de la cartera de Fase 2 caen en 2021–22.
- **Causas:**
  - (a) Solo-largo en mercado bajista: 3 trimestres, −5,4 pp.
  - (b) Warmup de PAXG: 1 trimestre, −3,2 pp.
  - (c) Freno −12%/−6%: cambió el signo de 1 trimestre y costó −37,8 pp en 2023.
  - (d) Fees y whipsaw: menos de 0,1% anual; despreciable.
- No hubo walk-forward ni re-estimación. Lo único estimado fue la volatilidad, de forma causal.

## C1. Motor L/S simétrico (atribución por trade, exacta)

| Activo | Sesión L/S | Sharpe L/S | Sharpe solo-largo | PnL largo | PnL corto (trades) | Decisión B4 |
|---|---|---|---|---|---|---|
| BTC | http://localhost:9200/#/backtest/50dbfcfe-7f4c-48ca-958a-aee2560957c0 | 0,73 | 1,04 | +7.386 | **−1.381** (17) | solo-largo |
| PAXG | http://localhost:9200/#/backtest/b633eb35-5ee1-42b6-8504-e61a5c11f35d | 1,01 | 1,26 | +10.335 | **−1.229** (10) | solo-largo |
| SPY | http://localhost:9200/#/backtest/ac68589e-459f-4e15-bf8e-e6d28e5e3b11 | 0,63 | 0,98 | +4.715 | **−1.008** (11) | solo-largo |

- **BTC L/S:** CAGR 9,4%, DD −23,0%. Funding −1.989 USDT, aplicado: los cortos cobran, pero el tramo largo paga más.
- **PAXG L/S:** CAGR 13,2%, DD −18,3%, sin funding.
- **SPY L/S:** CAGR 6,2%, DD −19,9%, sin funding.
- Separación de tramos: cada trade de Jesse tiene un único lado, y su PNL incluye fees y funding.
- **Lectura:** con estos lookbacks, el canal corto entra tarde en las caídas y devuelve en los rebotes.
  - En 2022 BTC (−65%) el corto no alcanzó a compensar.
  - La cartera solo-L/S da CAGR 14,8%, DD −24,7%, Sharpe 0,93, peor que la solo-larga.

## C2. ETH solo-corto
Sesión: http://localhost:9200/#/backtest/b6b72481-43ef-45df-accd-cedf32b94dca
- 22 trades, PnL −1.045, CAGR −2,1%, DD −24,1%, Sharpe −0,26, ρ con la manga BTC −0,15.
- No entra: exige Sharpe ≥0,5.
- **Funding:** `import_funding` solo soporta BTC-USDT, así que ETH corrió sin funding y el cobro de los cortos con funding positivo no está modelado.
  - Con funding medio del 10% APR y exposición media baja, el aporte sería del orden de +1–2% anual. No cambiaría el signo del Sharpe.
- La idea «cripto short-first» con este motor no tiene respaldo en 2020–25.

## C3. Petróleo WTI: no ejecutado
- Con la autorización de descarga del usuario se bajaron los ZIP de HistData WTIUSD M1 2020–2023.
- **Cobertura:** el de 2023 termina el 2023-12-01, y 2023-12, 2024 y 2025 no tienen archivo. El formulario público devuelve un token vacío; 2022, como control, sí lo devuelve.
- Siguiendo la instrucción, se paró el punto: no se importaron datos parciales ni se sustituyó la fuente.
- Scripts: `research_scripts/histdata_wti_download.py` y `histdata_wti_probe.py`.
- **Alternativa a acordar:** Dukascopy (hay scripts `dukascopy_download*.py` en el repo) o una fuente de futuros CL.

## C4. Cartera fijada (B1+B2) con las decisiones de B4/B5
- **Mangas:** BTC, PAXG y SPY, las tres solo-largo (sesiones `b4792187…`, `02a484b6…`, `21063c59…`).
- **Construcción:** vol expansiva, cada manga entra con ≥120 días de exposición, rebalanceo mensual, vol objetivo 17%, techo 2,5, freno catastrófico −20% (activo 0 días).
- **Medición:** desde 2021-03-01.

| Puerta r9 | Resultado | ¿Pasa? |
|---|---|---|
| CAGR ≥30% | 29,98% | ✗ (−0,02 pp) |
| DD ≤20% | −18,4% | ✓ |
| PF ≥1,2 (trades) | 9,8 | ✓ |
| Meses + ≥65% | 61,7% de 60 (≈62,7% sin el stub de 2026-01) | ✗ (~−2,5 pp) |
| Trimestres + ≥80% | 15/20 = 75% (2021Q1–2025Q4) | ✗ (−5 pp = 1 trimestre) |
| Mediana mensual >0 | +1,43% | ✓ |
| Positiva sin los 2 mejores meses | +147% | ✓ |
| DSR ≥0,95 | 0,79 (N=55); 0,49 (N=650) | ✗ |

- **Por año:** 2021 −5,4%, 2022 −7,5%, 2023 +42,5%, 2024 +84,4%, 2025 +55,6%. Vol realizada 20,0%.
- **Trimestres negativos:** 2021Q2 (−6,0%), 2021Q3 (−3,2%), 2022Q2 (−7,5%), 2022Q3 (−2,3%) y 2023Q3 (−6,9%).

Correlación de las mangas en esos trimestres:
- **Agregada:** BTC–PAXG 0,01, BTC–SPY 0,19, PAXG–SPY 0,07, contra 0,01, 0,16 y 0,09 en todo el período. La descorrelación se mantiene.
- **Por trimestre:** BTC–SPY sube a 0,70 en 2022Q2 y a 0,31 en 2023Q3, y en 2023Q3 PAXG–SPY también llega a 0,31.
- **Lectura:** los trimestres negativos no vienen de un contagio de correlación. Las tres mangas pierden poco a la vez en mercados sin tendencia, y la vol objetivo amplifica esa suma.

## N y presupuesto
- **N:** 55 declarado en el protocolo (decisiones de lado en 3 activos, ETH y construcción). CL no se decidió, así que no suma.
- **Corridas:** 4 económicas nuevas (BTC, PAXG y SPY L/S, ETH corto). Quedan 5 de 15. Ninguna corrida técnica fallida.

## Conclusión y siguiente paso
- La cartera solo-larga de tres mangas está **a un trimestre y a ~3 pp de meses** de las puertas de regularidad. El CAGR queda en el umbral y el DD dentro.
- El lado corto, tal como lo define el motor simétrico, resta en todos los activos y **no** es la palanca de regularidad.
- Para cerrar el hueco hay tres caminos, ninguno elegido aquí:
  1. una 4.ª manga descorrelacionada con datos completos: CL vía Dukascopy u otra fuente, a acordar;
  2. el piloto de 5–10 perps cripto previsto en la Fase 3;
  3. revisar con el usuario si Q80 sobre 20 trimestres es la vara correcta para una cartera de tendencia.
- Cualquier opción suma a N.

Análisis: jobs `dcde8606cc594e4895b5ae1fd948cedf` (A y B) y `c172a7184cb2446fa604d0de27589359` (C4).

Dashboard (sesiones nuevas):
- http://localhost:9200/#/backtest/50dbfcfe-7f4c-48ca-958a-aee2560957c0
- http://localhost:9200/#/backtest/b633eb35-5ee1-42b6-8504-e61a5c11f35d
- http://localhost:9200/#/backtest/ac68589e-459f-4e15-bf8e-e6d28e5e3b11
- http://localhost:9200/#/backtest/b6b72481-43ef-45df-accd-cedf32b94dca
