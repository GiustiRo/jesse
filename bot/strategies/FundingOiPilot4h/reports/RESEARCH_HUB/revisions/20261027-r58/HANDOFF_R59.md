# Handoff a r59 (desde r58, 2026-10-27)

## Estado
- **Candidata sin cambios:** P-r55 (`../20261026-r55/P55_FREEZE.md`).
- **Contadores:** N = 145 (techo r58 146); N_régimen = 38; N_temática = 19.
- **Datos reservados:** 2025 sellado y 2026 reservado.
- **Bancos gastados para C6:** U50 alts (desarrollo), N2 y N3 (confirmación r58). De las 32 candidatas de la regla N3 quedan solo 2 sin usar.

## Hallazgo vigente
- **C6 filtrado por compresión ∧ p(rango) bajo confirma en monedas nuevas** (D +0,60 R; canasta 0,455 contra 0,132).
- **Dentro de P-r55 no sirve:** −0,04 de Sharpe, y peor en trimestres bajistas y laterales (F3).
- **Sobre BTC/ETH, el filtro resta** (descriptivo).

## Lo que no hay que repetir
- Sumar alts de C6 a P-r55 en cualquier forma (R54_W1, ML3, ML4, I1).
- El desbalance taker y el número redondo como filtros de C6.
- El OI histórico de Binance antes de 2021-12: no existe para alts.

## Ideas para r59, en orden (a criticar)
1. **Cambiar la pregunta de cartera, no la de señal.** El filtro sirve donde C6 sin filtro es débil. Una cartera nueva de alts filtradas, aparte de P-r55, con su propio objetivo de riesgo, solo tiene sentido si el usuario quiere una segunda línea. Hoy da Sharpe ~0,45–1,0: poco.
2. **Funding no saturado condicionado a la compresión** (+0,79 R en U50, no elegible por la regla marginal).
   - **Necesita un banco nuevo:** N2 y N3 están gastados para C6.
   - La única fuente limpia es **2025**, y abrirlo es decisión del usuario.
3. **Si el usuario abre 2025:** primero la mirada preregistrada a P-r55 completa. Después, como secundario, la regla de r58 sobre las alts de 2025 (544 trades ya calculados en `v1_events.json`, sin mirar).

## Reutilizable
- **`research_scripts/r58.py`:**
  - `bar_features` (volumen relativo, taker, σ30, ATR, número redondo y funding saturado por vela 4h);
  - `trade_table` (une trades con la vela de señal y el día anterior);
  - `sweep` (D, D condicional, bootstrap semanal y reglas de elegibilidad);
  - `c6_bank` (C6 congelado en cualquier banco, con compuerta y costos ×k);
  - `integrate` (ML3 dentro de P-r55).
- **`data/r58/n3`:** 30 monedas en 1h + funding, hasta 2024 (gitignore; se regenera con `r58.py n3_download`).
- **`data/r56/panel_n3.npz` / `labels_n3.npz`:** se regeneran con `r58.py n3_panel`.
