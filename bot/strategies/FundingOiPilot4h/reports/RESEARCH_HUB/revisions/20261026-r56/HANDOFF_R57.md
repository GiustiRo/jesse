# Handoff a r57 (desde r56 y su extensión r56-B, 2026-10-26)

## Estado
- **Candidata sin cambios:** P-r55 = P1 sin bono (`../20261026-r55/P55_FREEZE.md`).
- **Contadores:** N de estrategias = 140; N_régimen = 38 (techo de 40).
- **Datos reservados:** 2025 sellado para un candidato nuevo preregistrado, con autorización del usuario. 2026 reservado.
- **Puente r56 → r57 (enmendado en r56-B, con tope de cambios relativo al mercado): no lo pasa ninguna configuración en N2**, las 20 monedas nuevas (`../../../R56_PHASE10_CLOSE_B_20261026.md`).
  - Según lo preregistrado, r57 **no** gasta N en estrategias que cambian de modo según el régimen.
- **T3 (Chronos-2 zero-shot con covariables BTC y vol global, estabilizado con histéresis) es el mejor pronóstico de vol:**
  - en N2: BSS +0,195, 20/20 monedas, calibración 0,98–1,10, cambia 16,4 veces por año contra 18,9 de la etiqueta;
  - falla solo la anticipación (4b): 5 días contra 9 de la persistencia;
  - en el holdout pasa todos los criterios, pero esa segunda mirada estaba declarada y no decide.
- **P5 (rango a 40 días, indicadores clásicos A3):**
  - en N2: BSS +0,14, 19/20 monedas, 4 de 4 años;
  - falla solo 4b, que en los ejes de rango no se puede cumplir por construcción.

## Pregunta abierta para el usuario (decide antes de preregistrar r57)
**¿Se habilitan usos continuos de los pronósticos?** Ninguno depende de cambiar de estado:
- **U1, dimensionamiento:** en cada manga de P-r55, reemplazar σ30 por la vol pronosticada en la regla de vol objetivo 0,17/σ. Se usa T3, o Chronos-Bolt (T1) como alternativa más barata.
- **U2, freno de riesgo:** recortar R1 cripto (BTC/ETH) cuando la probabilidad de vol alta supera un umbral fijado de antemano.
- **U3, filtro de rango:** usar p(sale del rango a 40 días) de P5 para filtrar estrategias de rango o de ruptura.

Habilitarlos es una **enmienda del puente**:
- solo puede aprobarla el usuario;
- cada uso cuenta en la N de estrategias;
- necesita puertas económicas propias, preregistradas: inclusión r51 en las dos ventanas, puertas de régimen r55 y costos de r49.

Si el usuario no los habilita, r57 vuelve a la agenda del handoff de r56: ML3 y el intercambio de R1 cripto.

**Próximo paso natural si se habilitan: recalibrar hacia adelante** (isotónica o por temperatura). En desarrollo, la calibración de las clases media y alta sigue siendo el punto débil.

## Lo que deja r56, reutilizable tal cual
- **Panel diario de U50 con RV de 1h, etiquetas, varas y holdout:** `r56_panel.py`, `data/r56/`.
- **Etiquetas a 20 y a 40 días.**
- **Panel de 70 monedas (U50 + N2):** `panel70.npz` y `labels70.npz`. La lista de N2 está en `data/r56/n2/universe_n2.json`.
- **Motor de evaluación** (`r56_eval.py`): walk-forward, BSS, DM, SPA, anticipación, prueba de no mirar el futuro, estabilizadores (`stabilise`, `stab_states`) y el factor de mercado (`f6_noise.json`, `r56_noise.py`).
- **Pronósticos Chronos de log-RV** por moneda y día hasta 2024-12-31, en `data/r56/` (gitignore; se regeneran con `r56_chronos.py`):
  - `chronos_bolt.npy`, `chronos_bolt40.npy`, `chronos_chronos2.npy`, `chronos_chronos2cov.npy`;
  - las versiones `_panel70` de los mismos.
  - Para usarlos en 2025 hay que recalcularlos con datos de 2025, **solo** cuando el usuario abra ese año.
- **Implementaciones en numpy** de JM, CJM, sparse JM, BOCPD, signatures y WK-means, con pruebas sintéticas (`r56_models.py`, `r56_feats.py`).

## Lo que no hay que repetir
- Pronosticar la tendencia, a 20 o a 40 días, con indicadores, estados o patrones. Ninguna familia señala tramos de tendencia; solo ajustan la probabilidad base.
- Modelos globales con todas las variables (G1/G2): sobreajustan entre años.
- HMM, filtrado o con Viterbi, como detector operable.
- Dirección de salida de rangos con Wyckoff-lite o banderines (X1): inestable.
- Combinar Chronos con HExp/HAR (K1) o pasar al logit ordinal (O1): no suman.
- Fijar topes absolutos de cambios por año. El tope tiene que salir del mercado (f_mkt × los cambios de la etiqueta).

## Advertencias
- **Cálculos pesados fuera de Docker** (decisión del usuario, 2026-10-26).
  - El Python de Windows (`C:\Python312`) ya tiene torch 2.11 con soporte XPU y detecta la Intel Arc.
  - Velocidades medidas:
    | Modelo | Docker (CPU) | PC (CPU) | Intel Arc |
    |---|---|---|---|
    | Chronos-Bolt | 83 por segundo | 147 por segundo | ~710 por segundo |
    | Chronos-2 con covariables | 6,1 por segundo | 9 por segundo | ~30 por segundo |
  - Los resultados son iguales a menos de 10⁻⁶.
  - Para el próximo cálculo pesado: crear un venv fijo (`--system-site-packages`, chronos-forecasting 2.3.2) y agregar a `r56_chronos.py` una opción de dispositivo.
- **El contenedor de investigación** tiene `/opt/chronos-venv`. Si el contenedor se recrea, el venv se pierde.
- **Recursos de Docker:** el usuario quiere revisar la RAM y la CPU de Docker/WSL2 entre rondas.
  - Durante r56 el equipo estuvo al 91% de RAM.
  - El Administrador de tareas no muestra la CPU del contenedor; para eso hay que usar `docker stats`.
