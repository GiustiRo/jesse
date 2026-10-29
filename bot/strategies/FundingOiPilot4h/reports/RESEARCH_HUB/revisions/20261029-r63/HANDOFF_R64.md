# Handoff a r64 (desde r63, 2026-10-29)

## Estado
- **Candidata:** P-r55, sin cambios (R1, ensamble Donchian diario multiactivo, + C6, rupturas cripto de 4 h). Sharpe 1,68 en 2018-09 → 2024.
- **Contadores:**
  - N = 156; N_régimen = 38; N_temática = 19.
  - N_fab = 1.614 (r63 no sumó: la fábrica no corrió sobre datos reales).
- **Datos reservados:** 2025 sellado y 2026 reservado.
- **Oráculo H:** 1 de 5 consultas usadas; quedan 4.
- **La búsqueda de un segundo motor está cerrada** (decisión del usuario para r63). Lo intentaron r59–r63, con métodos a mano, rankings, la fábrica y la fábrica con universo completo. Ninguno se distinguió del ruido después de cobrar la búsqueda.

## r64: robustez operativa de P-r55 (opción 1 de `HANDOFF_R63.md`)
Objetivo: dejar P-r55 lista para el momento en que el usuario decida abrir 2025. Sin buscar estrategias nuevas.
1. **Costos reales:**
   - fees por nivel de cuenta;
   - slippage medido sobre el libro de los símbolos que opera R1 (CFD/TradFi de Binance y cripto) y C6;
   - funding real;
   - sensibilidad del Sharpe a costos ×1,5 y ×2.
2. **Ejecución:**
   - horarios de las órdenes;
   - qué pasa con los huecos de fin de semana en los perpetuos TradFi;
   - tamaño mínimo y redondeo;
   - margen aislado;
   - qué pasa si una orden no se llena.
3. **Riesgo y monitoreo:**
   - drawdown esperado y su distribución (bootstrap);
   - reglas de pausa;
   - deriva de la volatilidad y la correlación entre mangas;
   - alertas.
4. **Deslistamientos:** C6 opera alts, y en r63 se vio que el archivo sigue publicando meses con volumen 0 después del deslistamiento. Hay que revisar cómo trata eso el motor de C6.
5. **Plan para abrir 2025:** un protocolo de una sola mirada, con criterios de continuidad fijados de antemano.

## Lo que no hay que repetir
- Otra fábrica sobre canastas de cripto 2020–2024: su poder no alcanza para ventajas de Sharpe < ~2 en desarrollo (F1 de r63).
- `voljump` largo: descartado en L63 (Sharpe −0,04).
- Leer un Sharpe de 1,5–2 de una búsqueda grande como evidencia (en r63 el ruido da hasta 2,2).

## Reutilizable
- **`r63_data.py`:** descarga de todo el universo USDT-M con deslistadas, limpieza (huecos, tramos, cola sin volumen) y elegibilidad causal por volumen. `data/r63/bars/` no está versionada; se regenera con `r63_data.py download`.
- **`r63_dsl.py` / `r63_eval.py`:** motor de r62 con elegibilidad, slippage por volumen y cierre por deslistamiento; canasta de activos activos.
- **`r63_run.py`:** fábrica en un solo proceso nativo con pool (~20 min por corrida de 1.620 programas con 16 procesos).
- **`r63_f3.py`:** N_eff por razón de participación, poder y prueba en holdout local.
- **L63** (98 alts) sigue fresco para cualquier hipótesis **nueva** (solo se usó con voljump).
