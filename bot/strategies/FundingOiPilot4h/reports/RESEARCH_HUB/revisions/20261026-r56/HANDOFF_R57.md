# Handoff a r57 (desde r56, 2026-10-26)

## Estado
- **Candidata sin cambios:** P-r55 = P1 sin bono (`../20261026-r55/P55_FREEZE.md`).
- **Contadores:** N de estrategias = 140; N_régimen = 22 (techo de 30).
- **Datos reservados:** 2025 sellado para un candidato nuevo preregistrado, con autorización del usuario. 2026 reservado.
- **Puente r56 → r57: no lo pasa ningún detector** (`../../../R56_CLOSE_20261026.md`).
  - Según lo preregistrado, r57 **no** gasta N en estrategias que cambian de modo según el régimen.
- **T1 (Chronos-Bolt zero-shot sobre la vol) es el mejor detector:**
  - holdout de 16 alts con BSS +0,176, positivo los 4 años y en 16/16 monedas;
  - bien calibrado y con anticipación;
  - falla un solo criterio: ≤ 12 cambios por año (da 26).

## Pregunta abierta para el usuario (decide antes de preregistrar r57)
**¿Se habilitan usos continuos del pronóstico de vol?** Los dos usos posibles, que no dependen de cambiar de estado:
- **U1, dimensionamiento:** en cada manga de P-r55, reemplazar σ30 por la vol pronosticada (T1, con V1 como alternativa más simple) en la regla de vol objetivo 0,17/σ.
- **U2, freno de riesgo:** recortar R1 cripto (BTC/ETH) cuando la probabilidad de vol alta de T1 supera un umbral fijado de antemano.

Habilitarlos es una **enmienda del puente**:
- solo puede aprobarla el usuario;
- cada uso cuenta en la N de estrategias;
- necesita puertas económicas propias, preregistradas: inclusión r51 en las dos ventanas, puertas de régimen r55 y costos de r49.

Si el usuario no los habilita, r57 vuelve a la agenda del handoff de r56: ML3 y el intercambio de R1 cripto.

## Lo que deja r56, reutilizable tal cual
- **Panel diario de U50 con RV de 1h, etiquetas, varas y holdout:** `r56_panel.py`, `data/r56/`.
- **Motor de evaluación:** walk-forward, BSS, DM, SPA, anticipación y la prueba de no mirar el futuro (`r56_eval.py`).
- **Pronósticos Chronos de log-RV a 20 días** por moneda y día, hasta 2024-12-31: `data/r56/chronos_bolt.npy` y `chronos_chronos2.npy` (gitignore; se regeneran con `r56_chronos.py` en `/opt/chronos-venv`, ~15 min Bolt y ~1 h Chronos-2).
  - Para usarlos en 2025 hay que recalcularlos con datos de 2025, **solo** cuando el usuario abra ese año.
- **Implementaciones en numpy** de JM, CJM, sparse JM, BOCPD, signatures y WK-means, con pruebas sintéticas (`r56_models.py`, `r56_feats.py`).

## Lo que no hay que repetir
- Pronosticar la tendencia a 20 días con indicadores, estados o patrones: no se puede pronosticar con ninguna familia.
- Modelos globales con todas las variables (G1/G2): sobreajustan entre años.
- HMM, filtrado o con Viterbi, como detector operable.
- Dirección de salida de rangos con Wyckoff-lite o banderines (X1): inestable.
- Chronos-2 en lugar de Bolt: no mejora y es ~4 veces más lento.

## Advertencias
- **El contenedor de investigación** tiene `/opt/chronos-venv`. Si el contenedor se recrea, el venv se pierde y hay que reinstalarlo (torch CPU + chronos-forecasting ≥ 2.0).
- **Recursos de Docker:** el usuario quiere revisar la RAM y la CPU de Docker/WSL2 entre rondas.
  - Durante r56 el equipo estuvo al 91% de RAM.
  - El Administrador de tareas no muestra la CPU del contenedor; para eso hay que usar `docker stats`.
