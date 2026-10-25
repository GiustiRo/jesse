# r50 F1g: operativas descorrelacionadas fuera de cripto (2026-10-25)

**Veredicto: ninguna de las tres pasa.**
- Las tres son **efectivamente descorrelacionadas**: su correlación diaria con P1 va de 0,04 a 0,18, también en los trimestres negativos de P1.
- Pero ninguna tiene ventaja sostenida: Sharpe largo (2001–25) entre 0,11 y 0,19.
- P5 queda igual a P1 (R1 + C6).

**N declarado: 98. Corridas Jesse:** 0 de 10.

**Protocolo:** `RESEARCH_HUB/revisions/20261024-r50/PHASE1G_PROTOCOL.md`, commiteado antes del código (`33e038be`).

## Canastas (clase acciones; perpetuos de Binance con proxy)

| Manga | Activos | Común: Sharpe | Larga 2001+: Sharpe | Mitades (≤2017 / ≥2018) | DD largo | Trades/año | ρ con P1 (trim. negativos) | Compuertas |
|---|---|---|---|---|---|---|---|---|
| G1 cambio de mes | 8 | −0,14 | 0,11 | 0,19 / −0,04 | −29,1% | 84 | 0,10 (0,04) | ✗ Sharpe, ✗ mitades |
| G2 reversión EE.UU. | 4 | 0,55 | 0,19 | 0,42 / −0,13 | −22,3% | 20 | 0,12 (0,16) | ✗ Sharpe largo, ✗ mitades |
| G3 pánico de volatilidad | 8 | 0,38 | 0,16 | 0,20 / 0,13 | −14,3% | 4,5 | 0,04 (0,09) | ✗ Sharpe |

**Por activo (Sharpe común / larga):**

| Activo | G1 | G2 | G3 |
|---|---|---|---|
| SPX | −0,08 / −0,23 | 0,88 / 0,34 | 0,12 / 0,18 |
| NDX | −0,09 / −0,09 | 0,42 / 0,25 | 0,22 / 0,42 |
| IWM | −0,30 / −0,23 | −0,32 / −0,12 | 0,02 / −0,07 |
| SMH | 0,15 / 0,10 | 0,40 / 0,21 | 0,16 / 0,13 |
| EWJ | −0,34 / −0,33 | — | 0,40 / 0,12 |
| EWY | 0,12 / 0,35 | — | 0,00 / −0,08 |
| EWZ | −0,47 / 0,38 | — | 0,42 / 0,08 |
| EWT | 0,16 / 0,47 | — | 0,87 / 0,32 |

## Lectura
1. **El efecto cambio de mes desapareció.** Es positivo hasta 2017 (0,19) y negativo después, y negativo en SPX desde 2001. Es el patrón de decaimiento después de la publicación que documentan McLean y Pontiff: el efecto se conoce desde 1988.
2. **La reversión en índices de EE.UU. dejó de funcionar después de 2017** (mitad 2018–25: −0,13). Su Sharpe de 0,55 en la común lo sostiene casi solo SPX en 2021–25. Confirma lo visto en F3.
3. **La compra en pánico tiene la mejor estabilidad,** con las dos mitades positivas, pero muy poca frecuencia (4,5 trades al año) y un Sharpe chico.
4. **Diversificar no es solo encontrar algo descorrelacionado: tiene que tener ventaja.** Las tres cumplen la descorrelación, ninguna la ventaja.

## Balance de r50 en futuros (F1 → F1g, 98 pruebas)

| Familia | ¿Generaliza? | ¿Con ventaja? | Dónde |
|---|---|---|---|
| Tendencia (ensamble Donchian R1) | ✓ | ✓, moderada | oro, SPX, Nasdaq, SMH; BTC y ETH |
| Rupturas cripto (R2/R3 → C6) | ✓ | ✓, fuerte | BTC, ETH |
| Tendencia en más mercados (F1f) | ✓ | diluye | Sharpe ~0,5 en 21 mercados |
| Reversión de corto plazo | ✗ | se derrumba fuera de muestra | — |
| Rotación, momentum 12-1, value | parcial | no suma | — |
| Calendario y pánico (F1g) | descorrelacionado | ✗ | — |
| Carry de funding | — | ✓ | fuera de alcance (spot) |

**La diversificación que sí funciona está dentro de R1:**
- R1 corre 7 mangas en metales, acciones, energía, bonos y cripto;
- en F2 las mangas de R1 tenían correlaciones diarias ≤ 0,16 entre sí;
- C6 agrega una ventaja cripto de otra temporalidad (4h, rupturas).

**La mejor cartera operable en futuros es P1 = R1 + C6:**
- 2018-09 → 2025: CAGR 36,9%, DD −14,3%, Sharpe 1,60, DSR 0,99;
- 2021–25: CAGR 24,6%, Sharpe 1,44, DSR 0,76.

## Opciones
- **a) Confirmar P1:** confirmación única en activos nuevos y 2026, y después F4 en Jesse. Es la operativa diversificada con evidencia real.
- **b) Seguir explorando otras familias.** Se gasta presupuesto de pruebas con una tasa de acierto que en r50 fue baja: de 98 pruebas, pasaron tres bloques.
- **c) Cerrar r50.**
