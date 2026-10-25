# r50 F1: screening de motores M1–M4 (2026-10-25)

**Veredicto: ninguna manga pasa F1.**
- **M1:** pasa la falsación de la ventana común solo por regularidad: 65% de trimestres positivos contra 60% del nulo, con Sharpe 0,48 contra 1,05. En la ventana larga lo veta la regla de DD: −10,1% contra −4,0%, más de 1,5x.
- **M2a:** cumple Sharpe (0,66) y descorrelación, pero falla la frecuencia: 31 trades/año contra ≥50. También lo veta la regla de DD.
- **M2b, M3 y M4:** Sharpe negativo en la ventana común.
- **N declarado: 63.**
- **Corridas Jesse:** 0 de 10.
- **Costes:**
  - fees y funding real en BTC y ETH;
  - slippage extra por lado: 15 bp en el bono y 5 bp en el gas;
  - 5 bp en los stops.

**Regla del usuario:** sin mangas que pasen no se rescatan variantes vecinas. Se reporta y se espera la decisión.

**Protocolo:** `RESEARCH_HUB/revisions/20261024-r50/PHASE1_PROTOCOL.md`, commiteado antes de los resultados (`c727df98`), más la enmienda 4b de costes, también previa. Ninguna regla se tocó después de ver resultados.

## Canastas (equiponderadas en riesgo; Sharpe de calendario √365)

**Ventana común: 2021-01-01 → 2025-12-31**

| Motor | Sharpe | CAGR | DD | Trim. + | Trades/año | ρ con M1 | ρ con M1 en sus trim. negativos (7) |
|---|---|---|---|---|---|---|---|
| Nulo r49 (6 activos) | **1,05** | 5,1% | −5,8% | 60% | — | 0,74 | 0,68 |
| M1 tendencia v2 | 0,48 | 1,7% | −4,0% | 65% | 92 | — | — |
| M2a RSI(2) | 0,66 | 1,6% | −2,3% | 60% | 31 | 0,08 | −0,00 |
| M2b IBS | −0,33 | −1,2% | −13,8% | 40% | 82 | 0,30 | 0,30 |
| M3 corto con régimen | −0,13 | −0,5% | −8,6% | 40% | 20 | 0,21 | 0,32 |
| M3-nr (sin régimen) | −0,57 | −2,7% | −17,5% | 25% | 37 | 0,12 | 0,18 |
| M4 ETH/BTC | −0,18 | −3,5% | −35,1% | 40% | 10 | −0,01 | 0,01 (ρ BTC −0,06) |

**Ventana larga (solo veta)**

| Motor | Desde | Sharpe | DD | Trim. + |
|---|---|---|---|---|
| Nulo r49 | 2010-12 | 0,88 | −12,6% | 57% |
| M1 | 2010-12 | 0,62 | −10,1% | 49% |
| M2a | 2010-12 | 0,43 | −9,2% | 67% |
| M2b | 2010-12 | −0,30 | −28,1% | 46% |
| M3 | 2010-12 | −0,12 | −14,0% | 33% |
| M4 (spot) | 2017-11 | 0,26 | −37,8% | 45% |

El bono no tiene lente larga (límite declarado), así que las canastas largas no lo incluyen.

Los CAGR son chicos porque cada canasta promedia mangas de vol objetivo 17% con exposición parcial. Sin apalancamiento de cartera, la comparación relevante es el Sharpe; el escalado a vol de cartera es tarea de F2.

## Puertas prerregistradas

| Motor | Puerta | Resultado |
|---|---|---|
| M1 | Falsado si no mejora al nulo ni en Sharpe ni en trimestres positivos (común) | **No falsado por poco:** Sharpe 0,48 < 1,05, pero trimestres positivos 65% > 60% (13 contra 12 de 20). |
| M1 por activo | ídem | Falla en BTC, oro, SPX, WTI y gas. «Mejora» en el bono, con Sharpe −0,63 contra −1,11 (los dos negativos). |
| M1 cortos (WTI, gas y bono, juzgados en ventanas con bajista) | Tramo corto > 0 | Pierden en los tres: −1.831, −1.568 y −792 USDT en la común. |
| M1 veto largo | Sharpe < 0 o DD > 1,5 × DD común | **Vetado:** DD −10,1% contra −4,0%. |
| M2a | Sharpe ≥ 0,5; ≥ 50 trades/año; ρ ≤ 0,2 en trimestres negativos de M1 | ✓ 0,66; **✗ 31/año**; ✓ −0,00. Además vetado en la larga por DD (−9,2% contra −2,3%). |
| M2b | ídem | ✗ Sharpe −0,33; ✓ 82/año; ✗ ρ 0,30. |
| M3 | Sharpe ≥ 0,5; quitar el régimen resta ≥ 0,4; < 50% del PnL en 3 trades | ✗ −0,13; ✓ el régimen suma 0,43; n/a (PnL < 0). |
| M4 | Sharpe ≥ 0,6; \|ρ con BTC\| ≤ 0,3 | ✗ −0,18; ✓ −0,06. |

## Por activo (ventana común; Sharpe)

| Activo | Nulo r49 | M1 | M2a | M2b | M3 | M3-nr |
|---|---|---|---|---|---|---|
| BTC (perp + funding) | 0,62 | 0,61 | — | — | 0,02 | −0,04 |
| ETH (perp + funding) | — | — | — | — | 0,47 | −0,63 |
| Oro | 1,31 | 0,92 | 0,24 | −0,21 | −0,33 | −0,81 |
| SPX | 0,80 | 0,43 | **0,88** | 0,34 | −0,30 | −0,59 |
| WTI | 0,06 | −0,37 | 0,55 | −0,00 | −0,58 | −0,42 |
| Gas | 0,33 | 0,14 | 0,23 | −0,13 | 0,16 | 0,46 |
| Bono (sin lente larga) | −1,11 | −0,63 | −0,97 | −1,58 | 0,13 | 0,06 |

En la ventana larga, M2a da Sharpe 0,34 en SPX y 0,47 en gas, y M3 da 0,57 en ETH spot. El detalle completo está en `research_scripts/data/r50/f1_screen.json`.

## Verificaciones técnicas (hechas antes de aceptar los resultados)
1. **Test sintético de signo** (`r50_engines.py selftest`):
   - en una serie que baja linealmente, el corto gana +5.292 contra +5.000 de precio, más +299 de funding cobrado;
   - el M1 L/S termina corto y con ganancia;
   - pasa.
2. **Precio del bono:**
   - Dukascopy USTBOND cae de 158,0 a 124,7 en 2022 (−21%), coherente con el futuro ZB. TLT (−35%) tiene más duración.
   - Máximo de 191,6 en mar-2020.
   - Sin saltos de roll: los mayores movimientos diarios son eventos reales (COVID, el dato de inflación de nov-2022, los aranceles de abr-2025).
3. **Bono M1 en 2022:**
   - exposición media de −0,6x y equity +5,5%;
   - los rebotes de marzo, julio–agosto y noviembre y los costes (15 bp) se comen la mitad de la caída;
   - comportamiento de tendencia normal, no un error.
4. **Gas y WTI:** niveles verificados (gas 10,0 en 2022; WTI 130,5 en 2022). El salto de WTI en 2020 es el hueco excluido abr–jul y queda antes de la medición.
5. **Comparación justa M1 contra nulo:** mismos 6 activos, misma ventana y misma construcción equiponderada.

No hubo correcciones técnicas: los resultados de este informe son los de la primera corrida.

## Lectura
1. **La reversión de corto plazo (M2a) es la única familia nueva con señal.**
   - Sharpe 0,66 en la común y 0,43 en la larga, con 60–67% de trimestres positivos y correlación nula con la tendencia cuando la tendencia pierde.
   - Su perfil es el esperado. Lo que falla es la frecuencia: 31 trades/año en 5 activos, contra la puerta de ≥50.
   - El veto de DD sale de comparar un DD muy chico en la común (−2,3%) con −9,2% en 15 años.
2. **La tendencia v2 continua no mejora al ensamble Donchian r49,** que sigue siendo el mejor motor de tendencia: Sharpe 1,05 en la común y 0,88 en la larga.
3. **Los cortos no funcionan como manga propia** en este universo: M3, los cortos de M1 y M4.
   - El filtro de régimen sí aporta (+0,43 de Sharpe frente a la ablación), pero no alcanza el positivo.
   - M3 en ETH (0,47 común, 0,57 larga) es la única celda corta decente; no se rescata por regla.
4. **El bono, operado con este coste, no aporta en 2021–25** con ningún motor. La operabilidad real (TMF/TBT, 3–6 k de profundidad) ya era dudosa.

## Decisión del usuario (no se avanza a F2)
F1 cierra **sin mangas que pasen**. Por regla no se prueban variantes vecinas. Opciones a decidir:
- **a)** Cerrar r50 con el diagnóstico: el ensamble r49 sigue siendo la referencia y la reversión de corto plazo es la única diversificadora con señal.
- **b)** Revisar puertas ya prerregistradas, lo que exige tu autorización. Las candidatas, de forma explícita:
  - la frecuencia de M2a (≥50 trades/año) contra el riesgo de sobreajustar la puerta al resultado;
  - el veto de DD relativo (1,5x), que penaliza a motores con DD común muy bajo.
  
  Cualquier cambio suma a N y se documenta como posterior a los resultados.
- **c)** Una F1b con hipótesis nuevas prerregistradas, por ejemplo M2 en un universo más amplio para ganar frecuencia. Sería una ronda nueva que suma a N.

Datos de validación (F3): EWJ y EWY listos; plata en descarga; Nasdaq y cobre en cola. No se usaron.
