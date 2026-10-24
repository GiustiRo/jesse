# SPY LAST RESET — cierre de seis controles

La selección de rupturas posteriores de BR02 conserva eficiencia parecida al cambiar el reset, pero la muestra sigue siendo pequeña y muy compartida. Ninguna variante supera el neto del centro BR02. No se elige un nuevo ganador ni se amplía la investigación después de esta última ronda.

Se completaron exactamente seis fulls RESET, manteniendo canal de entrada26, ordinal>=2, gestión, riesgo, costes y calendario. Cq y BR02 se reutilizaron como referencias existentes, sin rerun.

## Resultados de todas las variantes

| Control | Reset | N | Neto | PF | Sharpe motor | DD diario UTC % | Tiempo abierto % |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) | Sin selección por episodio | 31 | 751.35 | 1.49 | 0.458 | −5.218 | 15.26 |
| [BR02](http://localhost:9200/#/backtest/f89d7afb-9876-4e7e-9ddf-78ff85137810) | Midpoint26, centro fijo | 16 | 874.80 | 2.32 | 0.718 | −3.805 | 8.79 |
| [RESET01](http://localhost:9200/#/backtest/046e8f71-8b39-40ed-843f-146e43a45a37) | Canal20 | 16 | 864.02 | 2.30 | 0.717 | -3.378 | 8.58 |
| [RESET02](http://localhost:9200/#/backtest/12c939ee-a51b-4ae6-a323-dabd8fb7ab8e) | Canal32 | 17 | 781.90 | 2.04 | 0.642 | -4.203 | 8.84 |
| [RESET03](http://localhost:9200/#/backtest/d66af143-2178-4453-ab95-e9f992d6a0c4) | Fracción0.4 | 17 | 781.90 | 2.04 | 0.642 | -4.203 | 8.84 |
| [RESET04](http://localhost:9200/#/backtest/98565a46-f7a1-45b1-9e92-54473b959d62) | Fracción0.6 | 16 | 864.02 | 2.30 | 0.717 | -3.378 | 8.58 |
| [RESET05](http://localhost:9200/#/backtest/492fb702-3333-4696-ae4b-9f36d52d5a96) | Dos cierres bajo midpoint26 | 16 | 874.80 | 2.32 | 0.718 | -3.805 | 8.79 |
| [RESET06](http://localhost:9200/#/backtest/3f71c37c-5dca-4047-8bee-8dda7478d9ea) | EMA20 | 15 | 657.85 | 2.00 | 0.585 | -4.995 | 8.01 |


Capital inicial10 000USDT. N son trades cerrados, no observaciones independientes. Neto y tipos de orden concilian con qty/fees/PnL/wallet; DD diario procede de la auditoría MTM independiente de root, no del muestreo Portfolio del motor. Sharpe pertenece al motor. CAGR/DDmotor y todos los valores completos están en SPY_LAST_RESET_EXACT_RESULTS_20261019.md.

Cinco de seis variantes superan el neto de Cq, pero ese recuento incluye duplicados exactos y una réplica de BR02. EMA20 gana657.85, menos que751.35 de Cq, aunque con menor tiempo expuesto y DD observado. Todos los controles usan sólo15–17 operaciones frente31 de Cq; no se interpreta esa reducción como prueba estadística de ventaja.

## Equivalencias verificadas

- RESET01 (canal20) y RESET04 (fracción0.6) tienen todos los campos económicos de trades y curva numérica exactamente iguales.
- RESET02 (canal32) y RESET03 (fracción0.4) también son idénticas.
- RESET05, dos cierres consecutivos bajo midpoint26, coincide exactamente con el BR02 central.
- RESET06, EMA20, es una trayectoria distinta.

Por tanto, seis variantes más BR02 representan cuatro trayectorias ejecutadas distintas; sólo tres son nuevas respecto al centro. No son seis confirmaciones independientes. Root confirmó las identidades con hashes MTM, además del comparador de snapshots de esta auditoría.

La igualdad de fills/curva no demuestra que nunca difirieran señales o armings sin fill. Los snapshots no exportan todas las vars, contadores y órdenes canceladas. Los periodos se aplicaron realmente: root revisó fuentes y constantes y verificó que sólo cambia el reset; entrada y demás métodos siguen intactos.

## Qué aprendimos sobre estabilidad

Cambiar20/26/32 o las fracciones0.4/0.5/0.6 no destruye el beneficio observado ni obliga a una nueva salida. Los vecinos resultantes ganan781.90–864.02, frente874.80 del centro, con participación8.58–8.84% del tiempo. Es estabilidad local de una política de selección de episodio, sobre la misma historia y en buena parte los mismos trades.

Exigir dos cierres consecutivos no cambia la trayectoria económica del centro. EMA20 reduce el beneficio y empeora DD frente a BR02. No se cambia a otra definición de reset por escoger una cifra atractiva de la tabla.

En todos los vecinos el bruto de precio es MENOR que en Cq; la reducción de turnover/comisiones sigue siendo esencial. El centro tiene bruto1025.39 y fees150.59 frente1037.82/286.48 de Cq: mejora neta123.45, formada por bruto−12.43 y ahorro de fees135.88. Es una identidad contable entre políticas distintas, no causalidad aislada sobre el mismo conjunto de entradas.

La exposición temporal de los vecinos es8.01–8.84%, frente15.26% de Cq; su notional×tiempo a precio de entrada es .07190–.08165x, frente .14149x de Cq. Esta medida no usa marks contemporáneos, por lo que no es exposición MTM ni beta constante. Mayor neto por unidad rotada no prueba alpha si cambian momentos de mercado, ocupación y disponibilidad posterior.

## Costes, concentración y calendario

| Control | Bruto de precio | Fees | Neto +10 bps RT | Sin mejor trade | Sin tres mejores |
| --- | ---: | ---: | ---: | ---: | ---: |
| Cq | 1037.82 | 286.48 | 433.04 | 349.58 | -298.22 |
| BR02 | 1025.39 | 150.59 | 707.47 | 455.51 | -86.36 |
| RESET01 | 1015.17 | 151.15 | 696.07 | 445.14 | -86.43 |
| RESET02 | 945.40 | 163.50 | 600.23 | 366.18 | -175.69 |
| RESET03 | 945.40 | 163.50 | 600.23 | 366.18 | -175.69 |
| RESET04 | 1015.17 | 151.15 | 696.07 | 445.14 | -86.43 |
| RESET05 | 1025.39 | 150.59 | 707.47 | 455.51 | -86.36 |
| RESET06 | 796.82 | 138.97 | 503.44 | 246.93 | -254.63 |


Todos los vecinos permanecen positivos con10bps adicionales por roundtrip y al retirar sólo su mejor trade. Todos quedan negativos al retirar los tres mejores. Los recargos son estáticos sobre mismos fills/sizes, no un simulador de spread/impacto/colas. Eliminar runners es diagnóstico de concentración, no descarte automático; aquí limita la fuerza de la evidencia con15–17 trades.

Las cohortes por año de cierre2022 y2023 son negativas en TODAS las variantes;2024 y2025 son positivas. No se recortan años para elegir la mejor. Las cohortes de cierres no son retornos MTM anuales. La similitud temporal entre vecinos muestra que comparten episodios y debilidades, no que se haya multiplicado la muestra.

RootMTM39c5fd2539894967886c6ac977cbfb00 succeeded y todas las cuentas concilian. RESET01..05 tienen12/61 meses completos y9/19 trimestres completos positivos; RESET06 tiene11/61 y8/19. BR02 central tiene12/61 y9/19; Cq15/61 y9/19. No hay mejora en recuento de trimestres positivos. La regularidad de cartera no se fuerza como obligación de cada señal aislada, y reducir participación no equivale a producir más meses.

## Contrato y calidad de la implementación

Únicamente cambió el bloque de reset del before de SpyStructR1BR02. Normalizar clase y ese bloque devuelve la base completa byte-a-byte en los seis casos. Se preservaron las12 fuentesR1 y ambas referencias. Snapshot completo de base, protocolo y seis diffs fueron guardados antes de resultados; readbacks6/6 y revisión root antes de ejecutar.

RESET05 usa dos observaciones retenidas consecutivas, cada cierre contra su propio midpoint26 de velas PREVIAS. Offsession no cuenta ni rompe racha; no se imputan ausencias. Sólo se actualiza con timestamp de la candle filtrada igual al closed_candle_open_time; reset no se condiciona a ventanaentry, quote-fresh ni ocupación. RESET06 usa la misma EMA20 causal del régimen. Ningún reset añade un gate al origen Cq.

Origen calificante antes de capital/posición; ordinal>=2 y censura hasta primer reset observado. Gestión idéntica: stop2ATR desde fill, BE2.25R, trail4.2 con tightening. SPY4h+M1, warm240, fast/debugfalse, historiaUTC Mon-Fri00–20 y baropen00–16entry.10k/1%riesgo presupuestado/.00045porlado/isolated5x/cap4.4/reserva.001 sólo sizing. El presupuesto no es garantía de pérdida máxima ante gaps.

Desarrollo2020-10-15→2025-12-31 exclusivo,2026 cerrado. Proxy de precio aceptado, funding fuera. La selección histórica acumulada no se reinicia y esta ventana no es OOS limpio. Sin instalaciones, datasets, scripts, framework/configglobal, reinicios, BTC/PAXG, live/paper/Pi o nuevos fulls de referencias.

Root ejecutó QA sintética de métodos reales por AST:113assertions sobre12fuentes, jobe97c0f4493b449abba005c64ac9f4d48, informe SPY_LAST_STATE_QA_20261019.md. Esa prueba lógica es distinta de evidencia económica y no cuenta oportunidades reales.

## Evidencia preservada y estado final

Auditoría8snapshots c44367f60a1f4299ba8ad8af3987ce17 succeeded. ResumenJSON32291bytes<50KB íntegro en SPY_LAST_RESET_AUDIT_20261019.md; seis filas exactas y dos referencias separadas en SPY_LAST_RESET_EXACT_RESULTS_20261019.md. Pares completos del centro/vecinos y de identidades en SPY_LAST_RESET_pairs_*.md.

Protocolo SPY_LAST_RESET_PROTOCOL_20261019.md, snapshotbase SPY_LAST_RESET_BASE_SNAPSHOT_20261019.md, diffs/readbacks SPY_LAST_RESET_IMPLEMENTATION_REVIEW_20261019.md, fuente de auditoría SPY_LAST_RESET_ANALYSIS_SOURCE_20261019.md. Registro terminal SPY_LAST_RESET_SESSION_REGISTRY_20261019.md. Las fuentes completas están en notes de cada sesión desde antes de su ejecución.

RESET01 — SpyLastReset01

Dashboard: http://localhost:9200/#/backtest/046e8f71-8b39-40ed-843f-146e43a45a37

RESET02 — SpyLastReset02

Dashboard: http://localhost:9200/#/backtest/12c939ee-a51b-4ae6-a323-dabd8fb7ab8e

RESET03 — SpyLastReset03

Dashboard: http://localhost:9200/#/backtest/d66af143-2178-4453-ab95-e9f992d6a0c4

RESET04 — SpyLastReset04

Dashboard: http://localhost:9200/#/backtest/98565a46-f7a1-45b1-9e92-54473b959d62

RESET05 — SpyLastReset05

Dashboard: http://localhost:9200/#/backtest/492fb702-3333-4696-ae4b-9f36d52d5a96

RESET06 — SpyLastReset06

Dashboard: http://localhost:9200/#/backtest/3f71c37c-5dca-4047-8bee-8dda7478d9ea


Última ronda cerrada, seis de seis terminadas, sin trabajos propios pendientes ni nuevas pruebas. BR02 central se conserva como candidata de eficiencia de investigación; los vecinos aportan estabilidad local limitada y no justifican sustituirlo por otro máximo. No se promueve una configuración para operar ni se abre una ronda adicional.
