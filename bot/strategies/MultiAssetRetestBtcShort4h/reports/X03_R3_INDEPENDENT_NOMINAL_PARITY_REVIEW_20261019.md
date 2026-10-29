# X03 R3 — revisión independiente de paridad nominal

Se revisaron los ocho summaries por MCP, el código y reporte X03_R3_NOMINAL_PARITY_20261019.md, el fallo original y el estado/artefacto del job corregido. No se ejecutó ningún nuevo análisis o backtest desde este rol.

## Equivalencia de configuración

El job 75de1c39efa54164a2fe2b7840d130dd terminó failed por el assert de configuración X03C/FBN0C. La referencia X03 C guarda explícitamente simulation_model=perpetual_futures y annualization=365; el nuevo draft omite esos dos metadatos. No hubo evidencia de discrepancia económica en el fallo.

En lectura independiente de los summaries, los ocho tienen exchange.type=futures y annualization=365 en métricas. El fee nominal es .00045. Comparé los formularios completos tras normalizar únicamente los dos defaults conocidos y el nombre permitido de la fuente PAXG: coinciden en los cuatro pares. Esto incluye rutas, símbolo/timeframe PAXG, datos auxiliares, fechas, balances, fees, leverage, warmup, logging y opciones de exportación/ejecución.

La excepción de metadatos fue autorizada por root antes del retry y no cambia fuente, datos, tolerancia económica ni parámetros. No se debe generalizar para ignorar otros campos, valores explícitos diferentes o discrepancias de ejecución.

## Resultado económico de paridad

El job 6f2bfdbdc05c46d49c5c623793a8c444 está succeeded, exit_code 0. Su artefacto nominal_parity.json confirma los cuatro pares PASS:

| Referencia → clon | Trades | BTC / PAXG / SPY | Neto común USDT | Máximo ΔPNL trade |
|---|---:|---|---:|---:|
| X03 B → FBN0 B | 273 | 223 / 38 / 12 | 11964.238131473841 | 0 |
| X03 C → FBN0 C | 280 | 223 / 38 / 19 | 12135.876833976640 | 0 |
| N204 B → FBN1 B | 273 | 223 / 38 / 12 | 13056.614915077666 | 0 |
| N204 C → FBN1 C | 280 | 223 / 38 / 19 | 13239.442379846789 | 0 |

El harness rechaza claves duplicadas de trade, exige conjuntos idénticos de símbolo/dirección/open_ts, y compara closed_at, cantidad, precios de entrada/salida y fee exactamente. Compara órdenes ejecutadas por campos económicos, excluyendo IDs aleatorios y etiquetas; exige igualdad y valida PNL con tolerancia 1e-7 USDT. Todos los PNL difieren exactamente cero. También concilia starting/finishing balance, neto y fee agregado.

La revisión independiente no repite el cómputo de todos los trades: verificó el código completo del harness, los manifiestos de ocho inputs y su artefacto terminal; adicionalmente comprobó los formularios completos desde los summaries. Esta evidencia complementa la revisión textual de fuente y QA sintética previa.

## Dictamen

Paridad nominal satisfecha en los cuatro controles negativos. No hay objeción de equivalencia o implementación que impida el contraste de stress ya congelado, sujeto a ticket root. No se requiere rerun nominal ni cambio de hipótesis.

Paridad valida la equivalencia nominal del clon, no capacidad predictiva, robustez futura ni ausencia de sobreajuste. El futuro contraste al mismo fee alto seguirá siendo efecto total de la intervención en el simulador, con capital/ocupación como mediadores. Sin promoción ni apertura de 2026.
