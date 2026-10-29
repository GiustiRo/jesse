# r56-B F6–F7: puente de mercado, datos nuevos y estabilizadores (2026-10-26)

**N_régimen: 22 → 28** (techo 40, aprobado por el usuario). La N de estrategias sigue en 140. El protocolo de la extensión y la selección de N2 se commitearon en `4284cb5d`, antes de cualquier corrida y de la descarga. F7 se registró en `0829a54b`.

## F6: infraestructura (no suma N_régimen)
- **Factor de mercado** (`r56_noise.py`): cada etiqueta se midió por segunda vez con los mismos datos.

| f_mkt | vol | tendencia | rango |
|---|---|---|---|
| 20 días | **1,048** | 0,987 → 1,0 | 1,000 |
| 40 días | **1,058** | 1,000 | 1,001 |

  El ruido de medición agrega como mucho ~5% de cambios. **El puente enmendado exige cambios del estado operable ≤ f_mkt × los cambios de la etiqueta del mismo eje.**
- **Etiquetas a 40 días** (regla de F0): e = 0,25 y k = 4,0 ATR.
  - Cambios por año de la etiqueta: vol 9,0, tendencia 29,4 y rango 28,3.
  - A 40 días, la persistencia vuelve a quedar por debajo del azar en tendencia y rango.
- **N2:** 20 perpetuos nuevos (CHZ, COTI, RSR, VET, CELO, KAVA, RUNE, DUSK, OGN, ONE, DYDX, RVN, PEOPLE, JASMY, MANA, GRT, TRB, ENS, THETA e IOTX). Se descargaron hasta 2024-12 y no se miran hasta F10.
- **Reproducción:** T1 y V1 reproducen sus predicciones de F3/F4 (diferencia máxima de 3·10⁻⁸) y sus BSS (+0,1355 y +0,1142).
- **Prueba sintética de los estabilizadores:** pasa. Con un estado persistente y probabilidades ruidosas, los tres bajan los cambios sin perder exactitud.

## F7: estabilizadores del estado operable (Y_vol, 20 días)
Las probabilidades no se tocan, así que el BSS es el del modelo base. El parámetro se elige por trimestre con los 4 trimestres previos, sin mirar el futuro.

| Config. | Exactitud balanceada (des. / 2024) | Cambios/año (des. / 2024) | ÷ cambios de la etiqueta | Anticipación modelo vs. persistencia (des. / 2024) |
|---|---|---|---|---|
| T1 sin estabilizar | 0,417 / 0,547 | 23,0 / 41,2 | 1,30 / 1,92 | −6,5 vs. −14 / +10 vs. +7 |
| **Z1T** confirmación | 0,401 / 0,539 | 12,5 / 19,0 | **0,70 / 0,88** | −15 vs. −14 / +8 vs. +7 |
| Z2T histéresis | 0,404 / 0,548 | 9,0 / 21,8 | 0,51 / 1,02 | −15 vs. −14 / +9 vs. +7 |
| Z3T penalización | 0,406 / 0,548 | 9,8 / 24,2 | 0,55 / 1,13 | −16 vs. −14 / +8 vs. +7 |
| V1 sin estabilizar | 0,445 / 0,510 | 43,0 / 54,3 | 2,4 / 2,5 | +14 vs. −14 / +18 vs. +7 |
| **Z1V** confirmación | 0,434 / 0,493 | 15,3 / 17,5 | **0,86 / 0,81** | **+10,5 vs. −14 / +15 vs. +7** |
| **Z2V** histéresis | 0,439 / 0,485 | 15,2 / 16,1 | **0,86 / 0,75** | **+12,5 vs. −14 / +15 vs. +7** |
| **Z3V** penalización | 0,435 / 0,487 | 12,7 / 15,5 | **0,72 / 0,72** | **+10 vs. −14 / +12 vs. +7** |

Cambios de la etiqueta en esas filas: 17,7 por año en desarrollo y 21,4 en 2024.

## Lectura
1. **Estabilizar resuelve el criterio de cambios.** Los seis llevan el estado operable a la frecuencia de la etiqueta o por debajo, con una pérdida de exactitud balanceada de 1–2 puntos. La confirmación (St1) es la más robusta en los dos períodos.
2. **HAR estabilizado (Z1V–Z3V) cumple también la anticipación:** en la mediana de las transiciones anticipa a la persistencia por +24 días en desarrollo y por +5–8 en 2024. Junto con su BSS (+0,114 / +0,210), es **el primer candidato que cumple en desarrollo y 2024 todos los criterios de uso del puente, salvo la calibración**, que se juzga en N2. La pendiente de la clase alta de V1 en desarrollo es baja (0,36).
3. **Con T1 estabilizado, la anticipación se pierde.** El estado de Chronos llega a las transiciones casi al mismo tiempo que la persistencia (−15 contra −14; +8 contra +7). Su ventaja está en las probabilidades (BSS), no en anticipar el cambio de estado.

## Siguiente
- **F8:** HExp, HExpGl, la combinación con Chronos, el modelo ordinal y Chronos-2 con covariables, cada uno con el mejor estabilizador.
- **F9:** horizonte de 40 días.
