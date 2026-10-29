# r52 F2: reloj del flujo de órdenes («cuarto de hora») (2026-10-26)

**Resultado:** el efecto estadístico **se replica** (Q1 pasa), pero la regla operable pierde después de costos (Q2 y Q3 no pasan). N pasa de 113 a 116.

Protocolo: `PROTOCOL_R52.md` F2 (`840747c3`). Datos: velas 1m de `data.binance.vision` reducidas a cuartos de hora, con checksums verificados.

## Resultados (desarrollo 2021 → 2023; validación 2024)
| Ensayo | Resultado | Compuerta |
|---|---|---|
| Q1: IC del QOI contra el retorno de 8 h | BTC 0,033 (t 2,67), ETH 0,031 (t 2,57), canasta 0,037 (t 2,94) | pasa |
| Q2: regla 4h en BTC/ETH (z > 1 largo, z < −1 corto, 8 h) | Sharpe −0,47 en desarrollo y −1,67 en 2024; unos 3.000 trades por moneda; ρ con P1 −0,09 | no |
| Q3: Q2 congelada en 20 alts | Sharpe −1,72; 2 de 20 alts positivas | no |

## Lectura
1. **El reloj del flujo es real.** El desbalance agresor del primer minuto de cada cuarto de hora predice el retorno de las 8 h siguientes en BTC y ETH, con t ≈ 2,9.
2. **Es demasiado chico para operarlo solo.** Un IC de 0,035 no paga una ida y vuelta de 0,13% en unas 3.000 operaciones.
3. **Su uso natural es como variable o filtro.** r53 lo probó en ese rol (Y6 y C6q) y tampoco aportó.

## Archivos
- `research_scripts/r52_q.py`
- `research_scripts/data/r52/q.json`
