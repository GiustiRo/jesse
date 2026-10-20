# SPY y PAXG: resultados consolidados de investigación
Fecha local: 18 de octubre de 2026, America/Montevideo.

## Resultado de la etapa
Se completaron **17 backtests nuevos**: cinco de SPY y doce de la línea PAXG, incluidos controles aislados, sensibilidad, controles de ejecución y dos carteras compartidas. Participaron dos agentes, uno por activo, con coordinación y revisión de root. Se verificó que el servicio aceptó cuatro backtests simultáneos.

Apareció una pauta de reversión de fin de semana en PAXG que merece conservarse como candidata de investigación. En cartera mejora moderadamente CAGR y drawdown respecto de su control de riesgo comparable, pero **no mejora el conteo de meses o trimestres positivos frente a ese control**. Ninguna nueva estrategia se acepta como reemplazo de la referencia. El objetivo de regularidad sigue sin alcanzarse.

SPY no produjo una mejora defendible en las dos familias exploradas. No se volvió a investigar señales de BTC: sus reglas se conservaron como contexto de cartera.

## Datos, riesgo y selección
El usuario aceptó desarrollar señales de precio con los proxies existentes: SPX CFD BID dividido por diez para SPY y spot PAXG para el destino Binance perpetual. No se impusieron nuevas fuentes ni funding, que permanece fuera de esta etapa.

Ventana de desarrollo: 2020-10-15 a 2025-12-31 exclusiva. No incluye el 31 de diciembre de 2025. **2026 permanece sin evaluar**. El historial 2020–2025 ya fue ampliamente seleccionado; ni las nuevas comparaciones ni la predeclaración de sus controles lo convierten en OOS limpio.

Comparaciones aisladas: 10.000 USDT, riesgo planificado del 1%, fee 0,00045 por lado para todas las órdenes, 5x aislado y techo nocional 4,4x. La reserva de 10 bps sólo afecta sizing. Las carteras finales conservan BTC/SPY al 3% y PAXG al 1%, con máximo agregado planificado del 8%, ledger y reservas originales. No se aumentó exposición para rescatar señales.

## SPY: dos familias, cinco corridas
| Prueba | Trades | Neto USDT | CAGR | DD del motor |
|---|---:|---:|---:|---:|
| [Retest aislado de control](http://localhost:9200/#/backtest/23c4974f-7503-4afe-8ffa-f69eb78c5ef2) | 31 | 751,35 | 1,40% | −5,21% |
| [Ruptura del rango de apertura de 60 minutos](http://localhost:9200/#/backtest/a68dbfa8-3efe-410a-9c8b-861bf3609f38) | 890 | −6.273,02 | −17,25% | −63,75% |
| [Impulso inicial como control](http://localhost:9200/#/backtest/98918ea4-78a2-4548-8f23-8c7459d07a30) | 1.162 | −8.700,06 | −32,38% | −87,22% |
| [Exposición lenta con filtro](http://localhost:9200/#/backtest/12c25b07-a649-450a-979a-2bbd21c4ae5d) | 7 | 284,88 | 0,54% | −3,39% |
| [Exposición lenta sin filtro](http://localhost:9200/#/backtest/531fdbfd-a092-44cc-b879-228a51c45e14) | 7 | 385,77 | 0,73% | −3,30% |

La apertura tiene beneficio por precio demasiado pequeño frente a las comisiones: aproximadamente 1,53 y 0,82 bps por giro de nocional, antes de unos 9 bps de fees. Ambos sentidos pierden neto. Se archivan las recetas sin seleccionar direcciones u horarios después de ver resultados.

El filtro lento no supera al control de exposición: menor retorno y DD ligeramente peor. El stop del 10% con riesgo del 1% despliega alrededor de 0,098x de nocional; no corresponde extrapolar sus resultados a una exposición 1x. Siete trades son insuficientes para validar una regla general. Esto no rechaza toda estrategia de tendencia ni toda operativa de SPY.

Informe específico: strategies/ResearchSpyReference4h/reports/SPY_INDEPENDENT_RESEARCH_FINAL_20261018.md. La auditoría root posterior completó su apartado MTM: defensa 27/47 meses activos positivos, 27/63 calendario y 11/21 trimestres; control sin filtro 32/54, 32/63 y 12/21. Ambos cierres de frontera y wallets conciliaron. El apartado de ese informe que indicaba MTM pendiente queda resuelto por este consolidado y el job c761869862e74de89d19eca1c4114aee.

## PAXG: de los descartes a una pista contrastable
Los dos modelos de shock de 4h se descartaron: continuación −2.140,19 USDT y reversión −2.398,95 USDT, ambos negativos también antes de fees. Su control de retest aislado ganó 546,11 USDT en 35 trades.

La nueva familia observa el precio propio del viernes a las 16:00 de Nueva York y su desviación el domingo a las 16:00. Opera en sentido contrario, con target en el ancla, stop de dos ATR fijados al ancla y máximo 24 horas. No observa valor justo del oro ni demuestra actividad de arbitraje. El control hábil usa lunes/miércoles con el mismo reloj y horizonte. Los protocolos explican calendario, DST, cotizaciones M1 frescas y ATR de 4h ya completas.

| Prueba | Trades | Neto USDT | PF | DD del motor |
|---|---:|---:|---:|---:|
| [Fin de semana: primaria 1 ATR](http://localhost:9200/#/backtest/2da06c02-d246-43a0-b265-8837aa9c4be5) | 37 | 400,22 | 1,507 | −2,06% |
| [Control hábil: 1 ATR](http://localhost:9200/#/backtest/3855e023-3d66-4aff-8a13-fbb3110a3255) | 162 | −1.245,28 | 0,714 | −13,04% |
| [Vecino de 0,75 ATR](http://localhost:9200/#/backtest/ff199ebe-dab0-4c09-9078-fff98188e97c) | 60 | 764,04 | 1,732 | −2,99% |
| [Vecino de 1,25 ATR](http://localhost:9200/#/backtest/dd08508d-0124-44a7-99e8-4d2806e18790) | 24 | 80,21 | 1,125 | −1,93% |
| [Primaria con salida al cierre horario](http://localhost:9200/#/backtest/cb5bdb97-ba8a-4997-a009-673d76b4a156) | 37 | 321,19 | 1,409 | −2,33% |
| [Control hábil igualado a 0,75 ATR](http://localhost:9200/#/backtest/62e11d8f-f098-44df-8b6f-2861a0503811) | 188 | −1.171,40 | 0,757 | −12,71% |
| [0,75 ATR con salida al cierre horario](http://localhost:9200/#/backtest/d75e1a23-0429-4b61-800e-a1cb24835459) | 60 | 768,17 | 1,736 | −2,99% |

La primaria de 1 ATR concentra el 84,3% de su neto en trades cerrados en 2022 y pierde 34,82 USDT en las cohortes 2023–2025. El vecino de 1,25 ATR no sostiene otros 5 bps RT. No existe una meseta económica uniforme.

La versión de 0,75 ATR sí aporta evidencia exploratoria adicional: cohortes de cierre anuales positivas, +310,76 USDT en 2023–2025, +303,17 USDT después de otros 10 bps RT estáticos y +461,72 USDT excluyendo sus tres mayores ganadores. Su control hábil parejo pierde y el control de salida sin target LIMIT conserva la ganancia. Este último, sin embargo, pierde 2,89 USDT en la cohorte 2025. No se eliminan longs ni se ocultan períodos débiles.

**0,75 ATR fue identificado después de observar sensibilidad.** Sus controles posteriores se registraron antes de ejecutarse, pero son continuación adaptativa del descubrimiento, no validación independiente ni sustitución retrospectiva de la primaria.

MTM de 0,75 ATR aislado: 28/40 meses activos positivos (70%), 28/63 calendario (44,44%) y 16/21 trimestres (76,19%). En períodos completos: 27/39 activos (69,23%), 27/61 calendario (44,26%) y 14/19 trimestres (73,68%). Su control de ejecución conserva 28/40 meses activos positivos, pero baja a 15/21 trimestres, 13/19 completos. No confundir esta señal poco frecuente con una cartera que cumple las metas.

Informe específico: strategies/ResearchPaxgWeekendReturn1h/reports/PAXG_RESEARCH_FINAL_20261018.md, más su extensión de falsación y reportes de auditoría. El control de root está bajo strategies/ResearchPaxgWeekendCloseStress1h/reports/.

## Cuenta compartida: resultado decisivo de la etapa
Se predeclararon dos configuraciones nuevas y se revisaron sus fuentes antes de lanzar. En ambas el share de exposición usa exclusivamente 4h completas de los tres activos, para evitar que el reloj PAXG de 1h cambie la asignación por medir otra volatilidad. Se conservan los límites y reservas compartidas. C no es una réplica exacta de la referencia: reduce PAXG al 1% y fija ese reloj común.

| Cartera | CAGR | DD motor | Meses positivos / activos | Positivos / calendario | Trimestres positivos |
|---|---:|---:|---:|---:|---:|
| [Referencia conservada](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb) | 28,83% | −14,89% | 33/61 (54,10%) | 33/63 | 15/21 (71,43%) |
| [C: retest PAXG al 1%](http://localhost:9200/#/backtest/148f089d-2a06-48e0-b3eb-cd45a9f69eb2) | 27,03% | −13,52% | 35/61 (57,38%) | 35/63 | 14/21 (66,67%) |
| [T: fin de semana PAXG al 1%](http://localhost:9200/#/backtest/08975619-224b-415a-9c40-bde9ded32d69) | 27,55% | −12,36% | 35/61 (57,38%) | 35/63 | 14/21 (66,67%) |

En períodos completos, C tiene 35/59 meses activos positivos y T 35/60; ambos 35/61 calendario y 13/19 trimestres. DD de cierres diarios: referencia −14,878%, C −13,510%, T −12,359%; no sustituir DD motor por el más favorable.

T frente a C añade 756,71 USDT y reduce DD aproximadamente 1,16 puntos porcentuales. Esa mejora neta permanece en +500,59/+244,48 USDT con otros 5/10 bps RT estáticos sobre todos los fills. Estos recargos conservan tamaños y decisiones: no son simulaciones dinámicas.

La atribución importa: PAXG aporta **menos** neto realizado en T (1.553,07 frente a 1.683,61 USDT). BTC long añade 433,44, BTC short 366,01 y SPY 87,80 USDT por tamaños y trayectoria de capital endógenos. Los eventos de entrada BTC/SPY coinciden entre C y T. No atribuir todo el incremento al alpha aislado de PAXG. T ejecuta los 60 eventos aislados de PAXG; eso no prueba cobertura de todas las oportunidades posibles del proveedor.

La regularidad no mejora frente a C: T rescata tres meses negativos y deteriora cuatro positivos, con cambios en meses antes planos que dejan igual el total de positivos. Frente a la referencia añade dos meses positivos, pero pierde un trimestre positivo y tiene menor CAGR. No cumple 65% de meses activos y 80% de trimestres. La referencia no se reemplaza.

## Auditoría, persistencia y estado final
Se revisaron fuentes, reloj causal, DST, ATR previo, stops, fees por fill, posiciones, wallets y cierres de frontera. El auditor V4 reconstruye MTM al cierre diario UTC usando fills y precios observados anclados; no asigna PnL al mes de cierre ni usa las muestras 00:01 del motor como cierre de día.

Jobs root completos: a19d7e0afb404303aa33ca7cc1c19c53 (primera ronda), c761869862e74de89d19eca1c4114aee (segunda), bfffb8fd76674597927438f48bad3b3c (sensibilidad y ejecución), 1f79d5830ded4f7b9ba0c8049638308e (controles parejos de 0,75) y 63531bd31d1a47d28c3f3702a8d8b6a9 (cartera final). Todos succeeded / exit 0.

Se conservaron también fallos técnicos de análisis: anclas insuficientes en un primer intento, una aserción que detectó cruces de medianoche y comparación exacta de floats. Se repararon los análisis, sin volver a correr estrategias para modificar sus resultados. La fuente completa reproducible de la auditoría final está en strategies/ResearchPortfolioPaxgWeekend075/reports/ROOT_SHARED_ACCOUNT_ANALYSIS_SOURCE_20261018.md. Los artefactos temporales pueden caducar; los informes y fuentes persistidos fijan los resultados principales.

La figura segunda_ronda.png fue generada, pero su herramienta de lectura devolvió artifact_changed. No se utilizó un acceso alternativo ni se afirma haber mostrado la figura; las conclusiones dependen de auditorías numéricas completas.

Esta tanda termina sin tareas económicas pendientes y sin despliegue. Se conservan como comparaciones de investigación la pauta PAXG y las carteras C/T; no se declara cumplido el objetivo global. La siguiente investigación debería partir de estos contrastes y buscar una contribución temporal distinta, evitando barrer umbrales, retirar longs retrospectivamente o volver a optimizar las aperturas SPY rechazadas. Abrir 2026 requerirá antes congelar una selección final y su protocolo de evaluación; esta etapa no lo abrió.
