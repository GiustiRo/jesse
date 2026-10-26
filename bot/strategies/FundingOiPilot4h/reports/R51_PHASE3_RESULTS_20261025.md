# r51 F3: bloque A, bono, WTI y gas con reglas propias (2026-10-25)

**Resultado:** ninguno de los 5 ensayos pasa todas las compuertas. N pasa de 103 a 108.

**A3, el spread Brent–WTI, es el mejor hallazgo de r51**, pero queda vetado por la lente larga:
- Sharpe 1,21 en la decisión y 1,18 en 2021–25;
- ρ −0,05 con P1;
- 72% de trades ganadores;
- el veto viene de su DD de 2013, el quiebre estructural del spread que el protocolo había anticipado.

**No se rescata.**

**Protocolo y código**
- Protocolo: `PROTOCOL_R51.md` F3 y compuertas F6 (`8ac56348`). Código: `83f9e6ab`, con la enmienda de huecos `73a1c6da`.
- Datos nuevos: Brent CFD de Dukascopy (desde 2010-12), EURUSD de Dukascopy y TLT diario desde 2002.
- A5 usa EURUSD en lugar del índice dólar: Dukascopy tiene el índice recién desde ~2019, y el protocolo preveía ese sustituto.

## Resultados
| Ensayo | Decisión: Sharpe | CAGR | DD | Trim. + | 2021–25: Sharpe | Larga: Sharpe / DD | PnL en bajistas | ρ con P1 | Trades | Falla |
|---|---|---|---|---|---|---|---|---|---|---|
| A1 tendencia L/S lenta (WTI, gas, bono) | −0,31 | −3,3% | −37% | 40% | −0,52 | −0,48 / −74% | +2,9% | 0,10 | 238 | G1, G3 |
| A2 bono con compuerta de correlación | −0,30 | −4,8% | −40% | 28% | −0,33 | −0,36 / −70% | +26% | −0,03 | 55 | G1, G3 |
| **A3 spread Brent–WTI** | **1,21** | **8,4%** | **−5,0%** | **73%** | **1,18** | 0,80 / −12,7% | +9,1% | −0,05 | 43 | **G3 (DD largo > 1,5×)** |
| A4 fin de mes en el bono | −0,21 | −1,5% | −17% | 44% | −0,29 | −0,35 / −36% | −8,9% | 0,01 | 75 | G1, G2, G3, G5 |
| A5 WTI con filtro dólar | 0,11 | 0,6% | −26% | 47% | −0,19 | 0,36 / −26% | +11% | −0,03 | 71 | G1 |

**A1 por activo (decisión / larga):**
- WTI: −0,21 / +0,07.
- Gas: +0,06 / −0,04.
- Bono: −0,54 / −0,51, con TLT desde 2003 y DD de −83%.

## A3 en detalle
Retorno por año:

| Año | Retorno |
|---|---|
| 2012 | −0,1% |
| 2013 | **−4,6%** |
| 2014 | +10,3% |
| 2015 | +3,9% |
| 2016 | +13,5% |
| 2017 | +0,6% |
| 2018 | −0,5% |
| 2019 | +9,2% |
| 2020 | +11,2% |
| 2021 | +7,3% |
| 2022 | +16,7% |
| 2023 | −0,8% |
| 2024 | +5,0% |
| 2025 | +9,6% |

- **Positivo en 11 de 14 años.**
- DD máximo de la lente larga: −12,7%, desde el pico del 2013-01 al piso del 2013-11, cuando se normalizó el spread después del cuello de botella de Cushing.
- La regla de veto (DD largo peor que 1,5 veces el de la decisión, −7,5%) lo descarta.

**Lo que no está modelado:**
- solo hay barras diarias de CFD;
- los perpetuos BZUSDT y CLUSDT existen recién desde 2026-04, así que no hay historia operable;
- no se modela el funding de los perpetuos TradFi.

## Lectura
1. **Bono:** con ninguna de las reglas probadas en r50 y r51 (tendencia L/S, compuerta de correlación, fin de mes) hay ventaja.
   - TLT, con 23 años de historia, confirma la falta de ventaja: Sharpe −0,5 en A1.
   - Ganar el corto de 2022 no compensa los rebotes de 2023–25.
   - Con evidencia ya de dos rondas, el bono no tiene una regla direccional que funcione con estos datos.
2. **WTI direccional:** ni la tendencia ni el filtro del dólar le dan ventaja en la ventana de decisión.
3. **WTI como pata de valor relativo (A3) sí funciona.** Es la primera regla con ventaja en energía, descorrelacionada de P1 y regular, con 73% de trimestres positivos.
   - El riesgo es de régimen: el quiebre de 2013.
   - Para usarla hace falta un preregistro nuevo, en r52 y con decisión del usuario. Por ejemplo, un veto que distinga quiebres estructurales, o validación en otro par de la misma familia (gasolina–crudo o diésel–crudo si fueran operables).

## Archivos
- `research_scripts/data/r51/explore_A.json`.
