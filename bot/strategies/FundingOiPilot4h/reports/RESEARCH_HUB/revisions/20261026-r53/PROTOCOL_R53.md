# r53: protocolo preregistrado (fijado antes de cualquier resultado)

Continúa r52 según [`HANDOFF_R53.md`](../20261026-r52/HANDOFF_R53.md), bajo el mandato del usuario: investigación autónoma, N sin techo y registro de cada ensayo.
- La app no permitió abrir r53 en una sesión nueva desde un evento automático, así que corre en la misma sesión que r52.
- Datos, costos, universo U50, elegibilidad y cortes son los de r52: desarrollo hasta 2023-12, validación 2024, 2025 sellado y 2026 reservado.
- N parte de 116.

## Problema que ataca
En r52, el ranking ML (X1, elastic net) tiene IC semanal por rangos de 0,106 (t 5,6), pero su spread medio entre quintiles es ~0. La causa son las subas explosivas de unas pocas monedas en la pata corta. r53 prueba formas de **cobrar ese IC sin quedar expuesto a la cola**.

## Ensayos F1: construcción de cartera sobre el mismo puntaje
Todos usan los puntajes walk-forward de X1 (r52, sin cambios) salvo que se indique otra cosa.

- **Y1, pesos por rango con filtro de cola.**
  - Peso de cada moneda ∝ (rango centrado), con bruto 1,0 repartido 0,5/0,5 entre largos y cortos.
  - Se excluyen de la formación las monedas cuyo |retorno de 1 semana| supere el percentil 90 transversal de esa semana.
  - Holding de 1 semana.
- **Y2, Y1 con holding de 4 semanas:** 4 sub-carteras escalonadas, cada una rebalanceada cada 4 semanas, con 1/4 del capital cada una.
- **Y3, objetivo ajustado por riesgo:** elastic net re-entrenado con objetivo = rango de (retorno de la semana siguiente / vol 30 d). Misma cartera que Y1.
- **Y4, solo largo cubierto:** pesos por rango del quintil superior (bruto 1,0), con el filtro de cola de Y1, cubierto 50/50 con BTC y ETH por beta de 60 días, como X3.
- **Y5, reversión semanal:**
  - puntaje = −rango(retorno de 1 semana), solo entre las 25 monedas elegibles de mayor volumen de esa semana;
  - pesos por rango largo/corto, bruto 1,0;
  - sin filtro de cola (es parte de la señal), holding de 1 semana.
- **Y6, QOI como variable:**
  - X1 re-entrenado con 2 variables más: QOI medio de 7 y de 30 días por moneda (desbalance agresor del primer minuto de cada cuarto de hora, como en r52 F2) en rango transversal;
  - misma cartera que Y1;
  - requiere el 1m de las 50 monedas.

**Compuertas** (las de r52 F1, en desarrollo salvo indicación):
- Sharpe neto ≥ 0,5;
- con costos ×2, Sharpe > 0;
- ρ con P1 ≤ 0,3;
- validación 2024: Sharpe neto > 0.
- Y1–Y4 y Y6 además tienen que superar a X1 por ≥ 0,2 de Sharpe neto en desarrollo.
- Se reportan también las 20 monedas antiguas y la rotación.

## Ensayo F2: QOI como filtro de C6
- **C6q:** C6 (R2 + R3 en BTC/ETH, código congelado de r50) solo abre si en la vela 4h de la señal z(QOI) > 0, con el mismo z que en r52 F2.
- Se evalúa reemplazando a C6 dentro de P1 con la regla de inclusión de r51, en las ventanas de P1 cortadas al 2024-12-31.
- Ventana de C6q: perpetuo 2020-10 → 2024. El QOI existe desde 2020, así que la lente 2018-09+ usa C6 sin filtro antes de 2020-10, y se declara.

## F3: cartera y mirada sellada
- Las mangas que pasen entran a P1 con la regla de inclusión de r51, con ventanas cortadas al 2024-12-31.
- Solo lo que entre se mira una vez en 2025. Puertas: Sharpe > 0 y ningún derrumbe (Sharpe < −0,5 o DD < −30%).
- Si nada entra, 2025 sigue sellado.
- Cierre de la ronda y handoff a r54.
