# Investigación BTC: cierre de tandas C y D

Cuatro backtests económicos nuevos completados; ninguna candidata. Tres hipótesis y un control, con reglas registradas antes de ejecutar cada tanda. No son cuatro muestras independientes ni validación fuera de muestra.

## Resultados

| Prueba | CAGR neto base | DD M1 + ejecuciones | PF | Meses activos positivos | Trimestres positivos | Operaciones |
|---|---:|---:|---:|---:|---:|---:|
| [Detección acumulativa CUSUM](http://localhost:9200/#/backtest/2664ba2b-b192-47ae-95aa-18fd2e6a4d9e) | 8.98% | 19.27% | 1.153 | 33/62 | 12/20 | 310 |
| [Absorción y escape](http://localhost:9200/#/backtest/e8af10d8-200f-4d21-b5dd-b59daa7b116b) | -1.12% | 13.53% | 0.838 | 13/29 | 4/20 | 40 |
| [Reloj de volumen](http://localhost:9200/#/backtest/72326aa5-947f-410b-b7d7-f2ccadaf3c57) | 4.49% | 22.33% | 1.057 | 32/62 | 11/20 | 424 |
| [Control calendario](http://localhost:9200/#/backtest/696277c8-e897-4528-8327-dc1b5b621a2e) | -4.96% | 38.96% | 0.921 | 24/62 | 6/20 | 386 |

Ventana común: 2020-10-15 inclusivo a 2026-01-01 exclusivo. Capital virtual 10.000 USDT; riesgo objetivo 2% por trade, límite agregado 6%, 3x aislado. Neto de fee 0,00045 por lado y funding histórico aplicado/verificado; slippage modelado cero. El dataset de funding incluye marcas proxy declaradas. No se hicieron pruebas económicas nuevas de 2026 ni estrés de costos o variantes de riesgo.

## Qué preguntamos y qué aprendimos

C probó una transferencia CUSUM desde el antecedente PAXG y una idea creativa de absorción: volumen alto sin desplazamiento, seguido por escape del rango. El control de antecedentes distinguió esta última de shock contrarian, NR7, filtros de volumen y presión ya explorados. CUSUM obtuvo retorno positivo pero insuficiente y poca regularidad; absorción perdió y sólo produjo 40 operaciones. No convertir la atribución long/short observada en una selección retrospectiva de dirección.

D preguntó si medir el tiempo por volumen acumulado mejora una misma señal de ruptura de tres bloques previos. Se comparó con bloques calendario de seis velas 4h. El objetivo de volumen se fija al iniciar cada bloque con información previa; el exceso se consume sin repartir ni arrastrar. Ambas políticas mantienen protección y riesgo iguales. El reloj de volumen mejoró al calendario en este histórico, pero su CAGR 4,49%, PF 1,057 y regularidad no cumplen los objetivos. Al retirar sus dos mejores meses el resultado aritmético es negativo: −1.679,58 USDT. Superar el control no basta para promover.

Las cuatro incumplen CAGR mínimo 30%, PF mínimo 1,2, 65% de meses activos positivos y 80% de trimestres completos positivos. El control calendario además supera el DD máximo 25%. El reloj de volumen queda dentro del techo de 25% pero excede el objetivo de 20%. Medianas mensuales calendario: CUSUM +0,1714%, absorción 0%, volumen +0,0886%, calendario −0,7363%; incluyen meses inactivos. Diagnóstico sin los dos mejores meses: CUSUM +2.179,50 USDT; absorción −1.465,11; volumen −1.679,58; calendario −4.364,11. El mínimo operativo preliminar N=100 no constituye potencia estadística ni confianza por sí mismo.

## Medición y auditoría

Cada corrida registró 2.741.760 marcas M1 más ejecuciones, 63 intervalos mensuales contiguos (62 completos) y 20 trimestres completos; cero ventanas de señal inválidas. Equity se calcula como wallet + PnL abierto, sin multiplicarlo otra vez por apalancamiento. No se cambió el framework. DD representa muestras M1 y eventos, no todos los extremos intraminuto.

Las fronteras mensuales son a 00:00 UTC después del funding efectivo y antes de decisiones nuevas; el funding de esa frontera pertenece al intervalo que termina según esta convención. No equivale a agrupar cada evento en meses estrictamente [inicio,fin). Actividad se determina por exposición y ejecución, no por PnL distinto de cero. Los cuatro acabaron sin posiciones abiertas.

La auditoría completa de 310/40/424/386 operaciones reconcilió PnL bruto − comisiones + funding con PnL de trades y equity final; error máximo inferior a 1e−6 USDT. También se verificó que la suma de contribuciones mensuales coincide con el resultado final. Job de auditoría: 2eac4d059f45473f98ed4d832f068309. Esto acredita contabilidad, no rentabilidad futura.

## Decisión y continuidad

Cerrar los presupuestos C/D sin candidata y sin búsqueda de parámetros vecinos, filtros retrospectivos o eliminación de shorts para rescatar curvas. Desde r9 se completaron siete corridas económicas nuevas: A/B tres y C/D cuatro. El bloque histórico V1–V6 conserva sus 209 económicas; no es un censo global del proyecto ni se suma como muestras independientes.

La autorización autónoma sigue vigente. La siguiente tanda requiere otra pregunta material, contraste con antecedentes y protocolo con presupuesto previo. El contraste D aporta una diferencia histórica que puede orientar preguntas, pero no demuestra ventaja económica suficiente ni autoriza repetir sus vecinos. Mantener BTC individual y costos/riesgo acordados; estrés queda para candidatas y acuerdo conjunto. PAXG/SPY/cartera son fases eventuales.

## Evidencia

Protocolos y manifiestos: BTC_DISCOVERY_C_PROTOCOL_20261021.md, BTC_DISCOVERY_C_ACTIVITY_ADDENDUM_20261021.md, BTC_DISCOVERY_C_MANIFEST_20261021.json, BTC_DISCOVERY_D_PROTOCOL_20261021.md y BTC_DISCOVERY_D_MANIFEST_20261021.json. Fuentes y hashes en manifiestos; telemetría completa y recibos en los cuatro archivos TELEMETRY. Contabilidad completa: BTC_DISCOVERY_CD_ACCOUNTING_20261021.json. Contrato de medición: BTC_RESEARCH_M1_MEASUREMENT_20261021.md. Resultados estructurados de este cierre: BTC_DISCOVERY_CD_RESULTS_20261021.json.
