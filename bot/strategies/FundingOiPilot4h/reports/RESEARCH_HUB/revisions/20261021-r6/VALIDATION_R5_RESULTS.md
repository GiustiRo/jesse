# Resultado de la validación intermedia r5

Fecha UTC: 2026-10-21T14:45:00Z. Publicación documental: 20261021-r6. Se revisaron resultados existentes; no se ejecutaron pruebas económicas nuevas.

## Definiciones que quedan cerradas
- Perfil fijo de investigación: **2% por operación, 6% agregado y 3x aislado**. No se reabre su exploración.
- Conservar **K1001 B/C como referencias congeladas de investigación** y **N204 B/C como controles comparables**. No hay ganadora aprobada para operar.
- Conservar las piezas PAXG MARKET, SPY Second y SPY Market por su función ya investigada. La revisión no retira longs, elimina el suplemento ni cambia señales.
- La revisión de evidencia solicitada está completada. El siguiente punto es revisar estas definiciones con el usuario; no se inicia automáticamente otra fase.

## La comparación compatible ya existe
Hay resultados de K1001 y N204 con 10.000 USDT compartidos, perfil 2%/6%/3x, mismas rutas 4h+M1 y ventana 2020-10-15 inclusiva →2025-12-31 exclusiva. No es necesario reconstruirlos. Nominal:fee 0,00045 por lado; estrés:fee 0,00095.

| Referencia | CAGR nominal | CAGR con fee estresado | DD nominal / estrés |
|---|---:|---:|---:|
| K1001 B | 33,85% | 26,50% | −13,34% / −14,59% |
| K1001 C | 34,66% | 26,92% | −13,82% / −14,54% |
| N204 B | 32,66% | 25,02% | −13,38% / −14,03% |
| N204 C | 33,46% | 25,36% | −15,00% / −15,66% |

K1001 tiene mayor retorno en las cuatro parejas equivalentes revisadas. Eso no significa superioridad universal: N204 B con estrés tiene menor drawdown y42 meses positivos de 61, frente a38 deK1001 B. B/C son carteras relacionadas, no dos muestras independientes. Conservar ambas evita seleccionar retrospectivamente sólo la favorable.

Estos son CAGR de desarrollo reutilizado y de la **cartera compartida**, no de BTC aislado. No acreditan 20–30%para cada pieza ni cada año. En2022K1001 C ganó 18,10%nominal y15,38%con estrés, pese a un CAGR global mayor. Los extremos 2020/2025 son parciales. Superar 30%de CAGR no se rechaza por exceder una meta orientativa; tampoco garantiza persistencia futura.

R13 con 50k conserva el mismo perfil de riesgo, pero es otra base de capital. Se mantiene como sensibilidad histórica separada; no se mezcla ni se reescala para fabricar comparabilidad.

Fuentes: CAPITAL_R12_RESULTS_20261019.md y sus cuatro anexos K1001/N204 B/C; CAPITAL_R12_SOURCE_QA_20261019.md; BTC_R14_SIN_FUNDING_RESULTS_20261020.md; CAPITAL_R13_50K_RESULTS_20261019.md. En esta revisión se contrastaron además los doce summaries guardados listados en SESSION_RECEIPTS.json.

## La evidencia posterior conserva sus fallos
La evaluación ya realizada de 2026-01-01 →2026-10-19 exclusivo, también 10k/2%/6%/3x, dice:

| Caso ya evaluado | Retorno del período | PF | DD reportado | Trades |
|---|---:|---:|---:|---:|
| [K1001 B nominal](http://localhost:9200/#/backtest/d6ed3b7d-19c5-4240-8ad9-9cb2f7706667) | −1,27% | 0,971 | −25,88% | 46 |
| [K1001 C nominal](http://localhost:9200/#/backtest/3c175497-66bf-4cf0-a9f8-c888834961da) | +10,35% | 1,224 | −19,26% | 47 |
| [K1001 B estrés](http://localhost:9200/#/backtest/40239c00-168a-4ab4-b423-069c91e6e6b7) | −5,28% | 0,881 | −27,82% | 46 |
| [K1001 C estrés](http://localhost:9200/#/backtest/df30484a-1331-4faa-9097-6c2e7d7011bc) | +4,96% | 1,105 | −21,07% | 47 |

Son retornos del período, no rentas anuales proyectadas. C cumple los mínimos originales; B falla y el protocolo conjunto no se supera. Una operación SPY aporta 1.298,98USDT frente a1.035,12 de neto totalC. PAXG aporta 1.616,64 con 8 trades y BTC−1.880,50 con 38. Restar una contribución no simula retirar ese activo bajo capital compartido.

La ampliación posterior a N204/N503/P604/C504/K1005 tampoco encontró una candidata que pasara sus puertas. Fue exploratoria después de observarK1001; Y902 fue excluida expresamente, no falló esa prueba. Se usan las ejecuciones corregidas: las preliminares con PAXG truncado siguen invalidadas. Esta revisión no consultó velas nuevas ni volvió a ejecutar 2026.

## Qué aprendimos de BTC
La ventaja incremental K1001 frente a Y902 tiene sólo **tres situaciones únicas de señal discordante**: dos fills retrasados y una ausencia de fill. Las cinco diferencias de registros eran tres retirados y dos nuevos; no cinco casos independientes. B/C repiten las mismas situaciones. Una pérdida evitada enjulio 2024 explica casi toda esa mejora; los intervalos primarios incluían cero. Los vecinos de fees/TP no generan nuevos episodios de mercado.

Esto procede del contrato históricoR10 de 1%/8%/5x: sirve para juzgar la amplitud de su evidencia, no para mezclarlo con la tabla 2%/6%/3x.

En el perfil fijo, R14 ya investigó quitar suplemento, filtrar eficiencia de longs y EMA120 conpendiente. Ninguna variante cumplió sus criterios. La mejora de EMA dependió de una sola entrada; no se rescata después del fallo. El diagnóstico 2026 tuvo ocho longs BTC perdedores, pero el corto original y el suplemento se comportaron de forma distinta. No prueba una causa de régimen ni autoriza apagar longs o todo el short.

## Qué aprendimos de PAXG, SPY y diversificación
PAXG MARKET y el calendario de fin de semana 0,75 son líneas diferentes. La comparación de cuenta compartida del calendario fue descartada como reemplazo por regularidad; no invalida automáticamente PAXG MARKET. Este último conserva evidencia local en atribución/R60/cartera, con mayor exposición y dependencia temporal.

SPY Second/MECH01 sirve como referencia selectiva; SPY Market/MECH05 como alternativa de mayor neto histórico. Sus muestras aisladas son pequeñas. MECH01 conservó 105,62USDT sin 3 mejores ycon 10 bps RT extra; el diagnóstico era posthoc/estático. MECH05/06 fallaron ese castigo conjunto. Ninguno de esos análisis se convierte en prueba independiente por repetirlo.

**Las correlaciones y co-pérdidas sí fueron medidas antes.** PORT_CANDIDATES_RESULTS y EXACT_AUDIT documentan 61 meses de contribuciones mensuales MTM, bajo 1%/8%/5x:
- B: correlaciones BTC/PAXG−0,093; BTC/SPY−0,065; PAXG/SPY−0,047.
- C: −0,093; −0,111; −0,014.
- BTC/SPY:0 meses con ambas pérdidas sobre 14 con ambas patas no nulas enB;2/21 enC.
- PAXG/SPY:0/7 enB;2/11 enC.

Incluyen ceros y meses sin exposición. No son correlaciones de precios, ni los ceros de co-pérdida garantizan cobertura. Enabril 2021Cperdió en las cuatro patas. La contribución contable de una pieza y el efecto de incluirla en la cuenta no son intercambiables.

En los anexosR12 revisados no se acreditó una matriz mensual equivalente de las versiones 2%/6%/3x. Ese es el hueco acotado: no corresponde afirmar que jamás se midió diversificación. Se declara la limitación sin crear otra corrida.

## Límites que impiden una aprobación económica
1. Tres situaciones discordantes no acreditan una ventaja incremental generalizable; la incertidumbre y la selección histórica persisten.
2. El CAGR de cartera no acredita el objetivo individual de BTC/PAXG/SPY en el perfil fijo.
3. La evidencia de correlación histórica no se transfiere a otra versión, riesgo o frecuencia sin respaldo compatible.
4. PAXG spot y SPXCFDBID/10 son proxies: no certifican ejecución o precio del perpetual nativo. Funding, slippage efectivo, colas, liquidez e impacto no están modelados enK1001. La reserva 0,001 sólo interviene en sizing; feeestresado no cubre todo.
5.2026 ya fue observado; no vuelve a ser una muestra ciega para reglas informadas por esos resultados.

Son incertidumbres y límites, no órdenes de repetir pruebas.

## Alcance de la verificación r5
Tres revisores realizaron lecturas documentales por separado. Eso ayuda a contrastar interpretación, pero no constituye tres muestras de mercado ni una réplica estadística.

Root verificó doce summaries existentes: ochoK1001(desarrollo y2026) ycuatroN204 desarrollo. Todos finished/errornull,capital 10k,3x aislado,fee/ventana/rutascorrectos. Las fuentes congeladasR12 acreditan 2%/6%; el formulario acredita 3x. La identidadsaldo final−inicial−neto tuvo error máximo 5,10×10⁻¹¹USDT, inferior a la tolerancia contable heredada 1e−6.

Se leyeron únicamente los dos últimos trades almacenados deK1001Cdesarrollo para corroborar el cierre terminal documentado. No se calcularon totales a partir de esas páginas parciales. No se repitió la auditoría completa de todos losfills o de losdatos. Un contador rawopen 1 preterminal no se convirtió en posición viva: las salidas MARKET reduce-onlyconstan EXECUTED alfinish.

## Decisión final y punto de salida
**La revisión intermedia r5 queda completada; ninguna candidata se promueve.** Se conservan referencias, datos y reglas. No se cambia el riesgo ni se elige otra variante porque un período haya sido favorable.

Queda revisar con el usuario estas definiciones y decidir qué incertidumbre condiciona una eventual continuación. No se inicia automáticamente validación prospectiva, nuevos backtests, análisis jobs, exploraciones, cambios de estrategia o live/paper.
