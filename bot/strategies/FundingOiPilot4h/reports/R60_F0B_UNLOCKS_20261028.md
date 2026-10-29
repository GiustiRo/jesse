# r60 F0b: sondeo de datos de unlocks (2026-10-28)

**Protocolo:** `PROTOCOL_R60.md` §2. **N + 0.** No se cargó ningún precio, retorno ni volumen: el script (`research_scripts/r60_unlocks.py`) borra los campos de mercado (`price`, `mcap`, `volume`, `fdv`) antes de escribir a disco.

Dashboard: no aplica.

**Datos** (`research_scripts/data/r60/unlocks/`):
- `coverage.csv` (48 monedas);
- `events.csv` (694 eventos 2021–2024);
- `crosscheck.csv` (10 eventos);
- `raw/` (48 MB, gitignored, datos de terceros no confiables).

## Veredicto
**Con datos gratis no alcanza para un estudio de unlocks sobre las 48 alts.** Como mucho permitiría un estudio de eventos acotado y descriptivo en 9 monedas. Además, los calendarios son reconstruidos después de los hechos, así que hay riesgo de look-ahead. **No recomiendo abrir una línea de investigación con esto.**

## Fuentes
| Fuente | Estado |
|---|---|
| DefiLlama, bucket público `defillama-datasets.llama.fi/emissions/<slug>` | Funciona sin clave y cubre 23 de 48. La API equivalente (`api.llama.fi/emissions`) ya es paga (402), así que el acceso gratis podría cerrarse. |
| CryptoRank, página pública de vesting | Sin cuenta muestra solo una asignación por moneda. Tiene vesting parcial en 16. Sus términos probablemente restringen el scraping. |
| Tokenomist / Token Unlocks | 403 por protección anti-bot. No se esquivó. |
| GitHub (adapters de DefiLlama) | 404. |

## Cobertura en D (2021-05-24 → 2024-12-31)
- **23 monedas con calendario usable** (todas de DefiLlama). **9 tienen cliffs ≥ 1% de la oferta desbloqueada:**

  | Moneda | Días con cliff |
  |---|---|
  | APE | 33 |
  | APT | 26 |
  | OP | 23 |
  | INJ | 14 |
  | AVAX | 13 |
  | LINK | 10 |
  | HBAR | 9 |
  | BNB | 1 |
  | ICP | 1 |

  - En total son 130 días-moneda: 101 contando solo los destinados a insiders o inversores, y 26 con cliffs ≥ 5%.
  - **APE, APT y OP juntan el 63%.**
- **4 parciales** (solo CryptoRank): SAND, GALA, GTC y ATOM.
- **15 sin unlocks por diseño** (PoW o 100% circulantes).
- **9 sin calendario gratis:** XRP, ADA, DOT, XLM, IOST, ZIL, ALGO, EGLD y AR.

## Calidad
- **Cruce entre fuentes (10 eventos):** coinciden en fecha (±3 días) y tamaño (±20%) solo 4 de 10. Otros 2 coinciden solo en el monto entre lotes.
  - Los 4 desacuerdos: NEAR y UNI (lineal contra escalones), CRV (tasa 0,71×) y OP (asignación de 859 M contra 59 M).
  - Las dos fuentes probablemente salen de la misma documentación, así que tampoco son del todo independientes.
- **Reconstrucciones a posteriori**, no fotos de cómo se veía cada calendario en su fecha. Tienen supuestos explícitos, como fechas redondeadas o «desbloqueado en génesis».
- **El % circulante es un proxy** (la oferta desbloqueada según la propia fuente) y da absurdos en los TGE (SOL 1.321%).
- 125 de los 570 cliffs van a wallets no circulantes.
- Los datos de LINK son transferencias observadas on-chain, no un calendario.

## Efecto en el plan
- Sin N. La línea de unlocks queda **cerrada por datos** salvo que el usuario consiga una fuente paga (Tokenomist o CryptoRank Pro) con calendarios fechados tal como se veían en cada momento.
- Aun así, 9 monedas y ~100 eventos de insiders, con 3 monedas que juntan dos tercios, darían poco poder.
