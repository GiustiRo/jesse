# r49: acuerdos vigentes y plan de investigación

Aprobado por el usuario el 2026-10-24. Reemplaza los acuerdos r9 en la *ubicación* de las puertas y en el riesgo; los objetivos numéricos de cartera se mantienen. Antecedentes en [`HISTORY_SUMMARY.md`](HISTORY_SUMMARY.md).

## Por qué cambia la dirección

- **Las puertas de r9 son inalcanzables para un activo solo.** Pedir ≥65% de meses y ≥80% de trimestres positivos con CAGR 30% y DD 20% sobre un único activo implica un Sharpe neto ≈2. Lo documentado para BTC direccional es 0,5–1,0, y para tendencia diversificada 1,0–1,5. En una simulación de 5 años, una manga con Sharpe 1,0 pasa todas las puertas con probabilidad ≈0; con Sharpe 1,5, ≈0,29.
- **Las puertas de regularidad castigan la ventaja más documentada en cripto.** La tendencia tiene sesgo positivo: pocos meses grandes y un hit-rate mensual del 40–55%.
- **Con cientos de ensayos sobre 5 años, el ruido solo ya produce Sharpe ≈1,4.** El mejor resultado esperado sin ventaja alguna es ese. Cualquier promoción necesita un Deflated Sharpe con N declarado.
- **La regularidad sale de combinar activos.** Tres mangas descorrelacionadas con Sharpe 1,0 dan un Sharpe de cartera ≈1,7.

## Puertas

**Manga individual** (no dependen del apalancamiento):
- Deflated Sharpe ≥0,95 con N efectivo declarado.
- Sharpe neto ≥0,8.
- ≥100 trades, o ≥30 si la manga es diaria con tesis documentada.
- Los 5 mejores trades suman <60% del PnL.
- Ningún año con DD mayor que 2× la mediana anual.
- Superar a los benchmarks nulos del mismo activo: buy & hold, B&H escalado a la misma exposición y ensamble Donchian sin optimizar.

**Cartera combinada** (los números r9 se mantienen):
- CAGR neto ≥30% (aspiración 40–50%).
- DD ≤20% (techo 25%).
- PF ≥1,2.
- ≥65% de meses activos positivos y ≥80% de trimestres positivos.
- Mediana mensual calendario >0.
- Positiva sin los 2 mejores meses.
- Medición mensual MTM sobre equity, como en r11.

## Riesgo (perfil intermedio, elegido en r49)

- Volatilidad objetivo de cartera 16–18% anual, repartida entre mangas por volatility parity.
- Techos duros:
  - riesgo por trade ≤3%;
  - riesgo abierto agregado ≤8%;
  - aislado ≤5x, solo como respaldo: con stops ATR de 4h el apalancamiento casi nunca es la restricción que limita.
- Freno de DD: con −12% desde el máximo, el riesgo se reduce a la mitad; se restaura al volver a −6%. Se fija antes de la Fase 3 y no se ajusta mirando resultados.
- Cota de seguridad ¼–½ Kelly. Si el Sharpe estimado baja, baja la volatilidad objetivo. El valor final se calibra una vez en la Fase 3 y se congela.

## Costes

- Fee base 0,00045 por lado (taker con BNB) y funding histórico aplicado y verificado.
- Exits por trailing o TP como LIMIT maker (0,00018) cuando la mecánica lo permita.
- El estrés para candidatas incluye slippage de stop de 3–5 bps y fee 0,0009.

## Fases

0. **Línea base, reutilizando evidencia:**
   - OOS 2026 de `BtcMomentumCore4h` congelada, a riesgo 5% y a 2%/6%/3x, con funding ON.
   - Benchmarks nulos 2020-10→2025.
   - Deflated Sharpe de las referencias: BtcMomentumCore4h, K1001/N204 BTC-only, CHANNEL_P, N-state.
1. **Publicar r49 en el Hub y el registro de ensayos.**
2. **Familia de tendencia:** un motor, tres activos (BTC, PAXG, SPY).
   - Ensamble Donchian/TSMOM de lookbacks fijos, sin optimizarlos, vol-targeted, salida BE 2,25R / trail 3R.
   - Funding y OI solo como freno de riesgo.
   - Cuenta como una familia de ensayos.
3. **Cartera:**
   - Risk parity, freno de DD y puertas de cartera.
   - Walk-forward sin re-optimización.
   - Si la cartera queda corta, proponer una manga de tendencia en 5–10 perps cripto líquidos, con su correlación medida (requiere acuerdo).
4. **Incubación forward** en paper o testnet con regla de corte secuencial. Requiere autorización explícita aparte.

## Proceso

- **Registro de ensayos:** `bot/strategies/FundingOiPilot4h/reports/TRIAL_REGISTRY.json`, con id, familia, hipótesis, sesión y curva mensual. Cada cierre informa N efectivo y DSR.
- **Embudo de evaluación:**
  1. Screening vectorizado por IC en `research_scripts/`. El usuario dio su opt-in al aprobar r49.
  2. Un backtest Jesse de la receta congelada.
  3. Auditoría contable completa solo para candidatas.
- **Un informe corto por tanda.** No se publican revisiones documentales sin resultados nuevos.
- **Señales:** nada por debajo de 1h salvo ejecución maker modelada.
- **Presupuesto r49:** ≤15 corridas económicas entre las Fases 0 y 3, con un máximo de 2 simultáneas.

## Descartado y por qué

- **Más micro-patrones 1m/4h sobre BTC:** los fees se comen el bruto.
- **HMM:** retraso estructural, y su acuerdo con etiquetas manuales fue 56,7%. Un filtro de tendencia por precio da la misma información.
- **LightGBM / triple barrier sobre un activo:** las etiquetas solapadas dejan pocas observaciones independientes. El lockbox con Sharpe ~4 contra un mes demo con PF 1,10 es la firma del sobreajuste. Vuelve solo como meta-labeling.
- **Funding u OI como entrada:** V1–V6 y la literatura no muestran ventaja neta. Lo único robusto es que el funding alto precede caídas, y por eso queda como freno de riesgo.
- **Carry delta-neutral como núcleo:** en 2025–26 rinde ~2–5% neto. Queda solo como overlay si el funding supera ~15% APR.
