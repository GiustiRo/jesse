# Atribución SPY — entrada, gestión y exposición direccional

La referencia se reproduce exactamente, y la descomposición muestra que mantener exposición durante largos períodos puede aumentar mucho el retorno bruto de esta ventana alcista. Eso no demuestra ventaja predictiva de la entrada. El break-even no cambia el resultado observado de la referencia; el trailing cambia fuertemente duración, ocupación y conjunto de operaciones. Sustituir retest por MARKET deteriora el resultado de la política en esta muestra. Los relojes dentro/fuera del régimen producen resultados dispersos y dependientes de unos pocos trades: no establecen una estrategia ganadora ni una prueba de significación.

Se completaron17 controles SPY, autorizados junto a17 PAXG por root. No son17 ideas nuevas. Ninguna semilla fue elegida por desempeño; no hubo cambios de fuente ni de parámetro después de resultados. Todos los backtests terminaron y los snapshots completos fueron auditados.

## Tabla de controles

| Control | Cambio | N | Neto | PF | DD motor % | CAGR motor % | Tiempo abierto % | Exposición P₀ |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [C0](http://localhost:9200/#/backtest/798e6f62-979d-46a2-bf6d-b5983bcb3269) | Referencia exacta | 31 | 751.35 | 1.49 | -5.21 | 1.40 | 15.26 | 0.141x |
| [Cq](http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639) | Fresh en entry | 31 | 751.35 | 1.49 | -5.21 | 1.40 | 15.26 | 0.141x |
| [E1](http://localhost:9200/#/backtest/a0e806e0-9c7e-49e2-a044-79a32763dce0) | Sin BE | 31 | 751.35 | 1.49 | -5.21 | 1.40 | 15.26 | 0.141x |
| [E2](http://localhost:9200/#/backtest/069cb46d-09a5-4c8e-b164-f9c2d1061691) | BE, sin trailing | 8 | 4889.75 | 11.78 | -20.72 | 7.93 | 85.95 | 0.591x |
| [E3](http://localhost:9200/#/backtest/1fdaa89f-1d25-4832-a446-3c8fc5764cd2) | Stop inicial | 1 | 3485.35 | — | -11.06 | 5.90 | 98.86 | 0.359x |
| [E4](http://localhost:9200/#/backtest/0c2efecc-aa4d-41c4-a9ac-832af72595a5) | Stop inicial +72h | 44 | -28.87 | 0.98 | -7.47 | -0.06 | 5.85 | 0.059x |
| [M](http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07) | MARKET mismo evento | 38 | 151.60 | 1.07 | -7.72 | 0.29 | 16.00 | 0.145x |
| [R01](http://localhost:9200/#/backtest/83cdff20-9d2e-4d36-8c6c-2ba74a0c0a41) | Régimen seed101 | 11 | -81.60 | 0.87 | -4.93 | -0.16 | 4.38 | 0.037x |
| [R02](http://localhost:9200/#/backtest/c41e39a4-88b2-4423-87c0-f7863ccbe6d0) | Régimen seed202 | 13 | 1054.72 | 3.00 | -3.25 | 1.94 | 6.11 | 0.063x |
| [R03](http://localhost:9200/#/backtest/205744ff-a7cd-46e8-893b-17e9ebf31fa9) | Régimen seed303 | 16 | 153.75 | 1.18 | -5.55 | 0.29 | 6.11 | 0.059x |
| [R04](http://localhost:9200/#/backtest/a657dc36-13bd-440f-a423-917ab3caeb8c) | Régimen seed404 | 16 | -348.55 | 0.63 | -6.37 | -0.68 | 5.00 | 0.049x |
| [R05](http://localhost:9200/#/backtest/ee7ee861-0137-4d13-a95d-837cb2a3e97e) | Régimen seed505 | 9 | 143.16 | 1.43 | -3.17 | 0.27 | 3.76 | 0.041x |
| [U01](http://localhost:9200/#/backtest/da59b8b5-9d77-47fc-ac97-8aa5e28091a8) | Sin régimen seed101 | 72 | 1874.98 | 1.41 | -11.63 | 3.35 | 30.97 | 0.263x |
| [U02](http://localhost:9200/#/backtest/998764bf-03f3-4643-b5cf-b569b6c6196b) | Sin régimen seed202 | 70 | 2572.14 | 1.64 | -5.49 | 4.49 | 31.99 | 0.261x |
| [U03](http://localhost:9200/#/backtest/63dd9d81-c7bf-417b-823f-728977051fd8) | Sin régimen seed303 | 74 | -440.28 | 0.90 | -14.79 | -0.86 | 26.74 | 0.228x |
| [U04](http://localhost:9200/#/backtest/4ac55781-679a-4d6d-a79a-320f162147b2) | Sin régimen seed404 | 79 | -1075.46 | 0.74 | -18.08 | -2.16 | 25.90 | 0.182x |
| [U05](http://localhost:9200/#/backtest/37c6ae11-78b0-49c6-9b58-4c9190542841) | Sin régimen seed505 | 70 | 75.74 | 1.02 | -16.98 | 0.14 | 26.61 | 0.210x |


Neto expresado en unidades de cuenta USDT, con capital inicial10 000. N son trades cerrados; fills de entrada/salida son otra métrica. PFnull enE3 indica ninguna pérdida observada en un solo trade, no fortaleza infinita. CAGR y DD de esta tabla son los del motor; no presentar su curva de muestreo como cierre diario UTC. Root completó auditoría MTM de las17 sesiones y reconciliación terminal independiente de estos PNG.

Tiempo abierto=sum(duración de trades)/ventana. ExposiciónP₀=sum(precioentrada×abs(qty)×duración)/(capital inicial×ventana); mide notional a precio de entrada, no notional marcado cada minuto. Una exposiciónP₀.141x no equivale a un buy-and-hold constante. Ambas métricas hacen visibles diferencias grandes de ocupación, pero no igualan beta, riesgo ni drawdown entre políticas.

## C0, Cq y BE

[C0](http://localhost:9200/#/backtest/798e6f62-979d-46a2-bf6d-b5983bcb3269) coincide exactamente con [referencia aislada previa](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2):31 operaciones, net751.3477149671152, fees286.47552620734854, balancefinal10751.34771496711. Paridad completa de timestamps, precios, cantidades, PnL, fees, duración, campos económicos de órdenes ejecutadas y curva completa, excluyendo UUID. Se verificó ANTES de liberar los otros16.

Cq añade sólo frescura de entry. C0 y Cq tienen mismas31 operaciones/fills/cierres y curva económica. Efecto económico observado nulo en esta ventana; no permite afirmar que el guard nunca rechazara algún arming sin fill, porque los snapshots no contienen toda señal ni orden cancelada.

E1 elimina únicamente el BE manteniendo trailing y tightening: mismas31 entradas, cantidades y resultados. El BE no aporta diferencia marginal observada cuando ese trailing permanece activo. No se concluye que el bloqueBE jamás se evaluara internamente; esos estados no están conservados.

## Horizonte y gestión de salida

E2 conserva BE pero elimina trailing/tightening. Produce+4889.75 con ocho trades y85.95% del tiempo abierto, frente15.26% enC0. El mejor trade suma5340.43 y se liquida al final del motor; sin él, el neto es−450.69. DDmotor−20.72%, muy superior al−5.21% deC0. Ocho de sus entradas son comunes exactas conC0, pero la duración bloquea23 entradas adicionales de la referencia. No comparar sus beneficios como efecto aislado del stop sobre31 trades fijos.

E3 elimina BE y trailing: una sola posición desde noviembre2020 hasta el fin,98.86% del tiempo abierto y exposiciónP₀.359x. Gana3485.35 con un único episodio terminal. Es evidencia de participación persistente en la trayectoria alcista con stop inicial, no de repetibilidad de la señal ni de un mecanismo de generación de alpha. La atribución anual por cierre colocaría todo en2025; sería incorrecto describirlo como retorno ganado sólo ese año.

E4 añade plazo72h al stop inicial. Pasa a44 trades,5.85% del tiempo y net−28.87. El precio aporta+377.56 antes de406.43 de comisión; con fricción adicional pierde más. Treinta entradas exactas son comunes conC0, pero hay14 sóloE4 y una sóloC0: la nueva salida modifica la disponibilidad para señales posteriores. El máximo hold observado fue117.98h porque72h es deadline contractual desde fill, revisado por ticks4h y deuda hasta quote fresh. No se retrofecha una salida a un precio ausente.

Estos resultados muestran un intercambio entre participación, protección y ocupación. No justifican escoger el retorno máximo deE2/E3 ni afirmar que todo trailing sea perjudicial. La serie tiene una trayectoria específica, un proxy, una ventana reutilizada y muy pocos episodios largos independientes.

## Entrada inmediata frente a política de retest

Cq yM mantienen el mismo evento Donchian, régimen y frescura. M entra al close MARKET y recalcula tamaño con ese precio y stop2ATR; conserva elegibilidad de distancia contra boundary original antes de repricing. Cq gana751.35; M151.60, PF1.074, DD−7.72%, y con+5bpsRT M ya pierde35.47. M sin su mejor trade pierde224.73.

Exposición temporal15.26%/16.00% y exposiciónP₀.141/.145x resultan similares en agregado; eso no iguala los momentos de mercado ni los fills. Cq tiene31 trades yM38. Sólo cinco pares comparten símbolo/lado/timestamp real de fill exacto (primario predefinido); el resto no se fuerza a coincidir por cercanía.

El diagnóstico SECUNDARIO por created_at de una única orden ejecutada de entrada, agregado tras revisión, encuentra25 decisiones comunes inequívocas,20 con filltimestamp distinto. Neto de ese subconjunto Cq285.82/M35.69; sumaPnL/entrynotional .023735/−.013271. Refuerza la utilidad descriptiva de distinguir la decisión y la ejecución, pero sigue condicionado a que ambas políticas obtengan fill y a su ocupación previa. No es la población completa de oportunidades ni un efecto causal puro de LIMIT contra MARKET. No se reemplaza el contraste primario por el más favorable.

La política de referencia intenta un retest pasivo, pero sus órdenes ejecutadas constan como24LIMIT+7MARKET. Las siete MARKET se crean y ejecutan en el mismo timestamp de apertura del trade. Root verificó que smart-order clasifica primero is_price_near:abs(1−requested/current)<=.00015 genera MARKET antes de la comparación STOP/LIMIT. Los snapshots no conservan boundary solicitado y quote de decisión por separado; no se reconstruyen sus distancias exactas. No hay evidencia aquí de fills ficticios; sí una semántica del motor que debe nombrarse correctamente. Fee.00045 por lado en todos los tipos.

## Qué dicen las cinco semillas

Los diez relojes R/U usan exactamente SHA256('ATTR1|symbol|seed|baropen'), primeros8bytes bigendian%48==0, seeds101/202/303/404/505. Es pseudoaleatorio determinista aproximado1/48 por barra elegible; no datos futuros, Pythonhash, cola ni replay. El reloj se actualiza aun con posición. R mantiene EMA/ADX/RSI/rango pero retira breakout y distancia al canal. U retira todo ese régimen, incluido rango, conservando mismo calendario/history100/ATR/sizing/fresh. Gestión original idéntica.

| Grupo | Neto mediano | Rango de neto | Neto positivo | Tiempo mediano | ExposiciónP₀ mediana | Neto bps entrada mediano |
| --- | ---: | --- | --- | ---: | ---: | ---: |
| R, con régimen | 143.16 | −348.55 a1054.72 | 3/5 | 5.00% | .049x | 9.52 |
| U, sin régimen | 75.74 | −1075.46 a2572.14 | 3/5 | 26.74% | .228x | 1.36 |

C0 supera en neto a cuatro de cincoR, pero tiene unas tres veces la exposición temporal mediana y31 trades frente9–16. No es una comparación a exposición constante. UnaR supera aC0; no se selecciona como candidata. En las cincoR, quitar los tres mejores trades deja neto negativo; la mediana+10bpsRT es−7.85.

U tiene mucho más tiempo y turnover, drawdowns de motor mayores en las cinco semillas queC0 y retornos muy dispersos. DosU superan netoC0 y dos pierden; la quinta apenas gana. La medianaU con+5bpsRT es−201.86. U02 sigue positiva al retirar los tres mejores, mientras las otras cuatroU no; ese hecho no autoriza elegirU02 después de observar resultados.

Con la misma semilla, R supera netoU en tres de cinco pares, pero U supera ampliamente aR en los otros dos. Entradas exactamente comunes por seed:6/6/14/11/7. La disponibilidad cambia por duración y régimen; el mismo hash no produce carteras ni exposición iguales. Medianas, medias, rangos y diferencias se conservan como descripciones de cinco escenarios dependientes, sin p-valuesIID, intervalos basados en cinco independientes ni selección de seed.

La lectura prudente es que el régimen reduce mucho participación y turnover y eleva la mediana neta por notional rotado, pero esta tanda no demuestra superioridad robusta de rentabilidad ajustada a exposición. Tampoco demuestra que el breakout/retest sea innecesario: no se igualó su cantidad/tiempo de operaciones. Los relojes cuestionan explicaciones demasiado fuertes de necesidad del régimen o de precisión de entrada, sin resolver por sí solos el origen del beneficio.

## Costes y concentración

| Control | Neto +5 bps RT | Neto +10 bps RT | Sin mejor trade | Sin tres mejores |
| --- | ---: | ---: | ---: | ---: |
| C0 | 592.19 | 433.04 | 349.58 | -298.22 |
| Cq | 592.19 | 433.04 | 349.58 | -298.22 |
| E1 | 592.19 | 433.04 | 349.58 | -298.22 |
| E2 | 4857.84 | 4825.94 | -450.69 | -453.73 |
| E3 | 3482.66 | 3479.97 | 0.00 | 0.00 |
| E4 | -254.66 | -480.45 | -215.95 | -483.52 |
| M | -35.47 | -222.54 | -224.73 | -864.91 |
| R01 | -143.46 | -205.32 | -293.73 | -582.46 |
| R02 | 980.51 | 906.30 | 517.16 | -167.30 |
| R03 | 72.95 | -7.85 | -276.51 | -647.78 |
| R04 | -425.51 | -502.46 | -595.08 | -879.04 |
| R05 | 92.01 | 40.86 | -156.40 | -310.34 |
| U01 | 1516.77 | 1158.56 | 1036.19 | -216.22 |
| U02 | 2252.39 | 1932.64 | 2005.53 | 959.59 |
| U03 | -762.93 | -1085.58 | -1050.49 | -2029.05 |
| U04 | -1374.83 | -1674.21 | -1413.33 | -1973.56 |
| U05 | -201.86 | -479.45 | -305.66 | -995.56 |


Stress usa tamaños y fills fijos y añade5/10bps por roundtrip proporcional al notional de ambas piernas. No rerutea ni simula impacto/cola/spread. Retirar los mejores trades es diagnóstico de concentración, no criterio automático para descartar estrategias runner. En E3 retirar su única operación deja muestra vacía, no una estrategia cero-riesgo.

## Metodología y límites

Ventana2020-10-15→2025-12-31 exclusiva,2026 cerrado; capital10 000, riesgo presupuestado1% por trade con reserva.001 sólo sizing, cartera8%, capgross4.4, isolated5x, fee.00045 por lado incluyendo LIMIT; warmup240, fastfalse, debugfalse. Un presupuesto de riesgo no garantiza pérdida realizada máxima ante gaps. Las clases son autocontenidas, sin herencia de archivos experimentales ni cambios de framework/configuración global/referencia/BTC. Sin live/paper, instalaciones ni scripts de investigación nuevos.

Se conserva EXACTO calendario de referencia: historia UTC Mon-Fri00:00–20:00, barras elegibles de entrada abiertas00:00–16:00 (decisiones4/8/12/16UTC). No se cambia a RTH. Filtrar por horario no certifica upstream, festivos, barras completas ni paridad Binance. C0/E no reciben un guard de entrada nuevo; Cq/M/R/U comprueban M1T−60s, finitud y paridad. Guard no filtra trailing; E4 mantiene deuda de salida hasta quote fresh. Stops permanecen activos fuera del calendario de entry.

ProxySPXCFDBID/10 aceptado para desarrollar precio; funding fuera. Este estudio no valida spreads, liquidación, lot sizes ni transporte operativo a perpetual24/7. Historial2020–2025 reutilizado: no OOS limpio. El conjunto de17 políticas se conserva en la cronología acumulada, no sólo las favorables. Las estrategias long-only tampoco separan retorno direccional general de alpha neutral.

Todos los snapshots completos reconciliaron sumaPnL, fees de ambas piernas y balance terminal. Las cohortes por año de cierre son diagnóstico de trades y NO retornosMTManuales. Root ya auditó las17 sesiones en MTMUTC con terminales conciliados. Esta tabla mantiene explícitamente DD/CAGRmotor para distinguir relojes de valoración.

Límite visual MCP: equity_engine.png del primer bloque fue inspeccionado y muestra superposición C0/Cq/E1. Los otros seis PNG devuelven artifact_changed incluso al segundo fetch; no se hicieron más reintentos ni fallbacks. Los siete jobs económicos succeeded y los JSON completos fueron recuperados; las cifras y auditoría MTM independiente no dependen de poder mostrar esos PNG. No se afirma inspección visual de las seis imágenes inaccesibles.

## Fuentes y resultados preservados

Propuesta ATTRIBUTION_SPY_PROTOCOL_PROPOSAL_20261018.md; adenda definitiva17fulls ATTRIBUTION_SPY_FREEZE_ADDENDUM_20261019.md; ajuste elegibilidadM ATTRIBUTION_SPY_MARKET_ELIGIBILITY_ADDENDUM_20261019.md; código común/diffs ATTRIBUTION_SPY_IMPLEMENTATION_REVIEW_20261019.md. Readback exacto17/17; fuentes completas en notes de dashboards antes del run y en strategies/AttrSpy*/__init__.py. El ajusteM fue previo a cualquier resultado suyo; no rescate.

Datos exactos17filas: ATTRIBUTION_SPY_EXACT_RESULTS_20261019.md. Registro: ATTRIBUTION_SPY_SESSION_REGISTRY_20261019.md. Auditorías1..7 en ATTRIBUTION_SPY_AUDIT*.md. Fuente numérica en ATTRIBUTION_SPY_ANALYSIS_SOURCE_20261019.md; resumen semillas en ATTRIBUTION_SPY_SEED_ANALYSIS_SOURCE_20261019.md. Diagnósticos separados en ATTRIBUTION_SPY_MARKET_ORDER_DIAGNOSTIC_20261019.md y ATTRIBUTION_SPY_CREATED_TIME_SECONDARY_20261019.md.

No se promueve ni integra ninguna variante por esta descomposición. El avance útil es distinguir observación reproducible, dependencia de exposición, valor marginal de gestión y selección de fills. Cualquier siguiente contraste deberá fijar su pregunta y exposición antes de resultados y conservar toda esta selección previa.
