# AA — propuesta documental: volumen como modificador de persistencia direccional

Fecha: 2026-10-21. Estado: PROPUESTA PARA REVISIÓN ROOT; no es protocolo aprobado. Cero código, clases, jobs, drafts, economía o velas observadas. Se fijan esta pregunta y su formulación sin consultar resultados Y. Z sobre financiación acumulada quedó descartada en su propio archivo, sin experimento.

## Pregunta económica

¿El volumen relativo conocido al terminar un movimiento BTC4h cambia su pendiente predictiva de retorno posterior24h, más allá de los efectos principales de ese movimiento y del propio volumen?

La explicación a contrastar es compensación por absorber demanda de liquidez: una variación acompañada por actividad extraordinaria podría revertir más, o continuar menos, que otra de igual dirección/magnitud con actividad ordinaria. La alternativa es que el volumen sólo acompañe noticias, volatilidad o atención y no añada un pronóstico direccional. No se observan órdenes agresoras, agentes informados, inventarios o demanda exógena. El contraste mide utilidad predictiva de una interacción; no identifica el mecanismo causal.

La diferencia material propuesta es que volumen pueda modificar la respuesta al retorno con signo. No basta cambiar de estimador: el término nuevo r·v debe compararse con un modelo que ya contiene r y v por separado, manteniendo idénticos datos/target/admisión/gestión. No se impone reversión ni se seleccionará sólo una cola de volumen.

## Literatura primaria y alcance

Campbell, Grossman y Wang, Trading Volume and Serial Correlation in Stock Returns, Quarterly Journal of Economics108(4),1993,905–939. [Ficha del autor](https://campbell.scholars.harvard.edu/publications/trading-volume-and-serial-correlation-stock-returns), [PDF original alojado por el autor](https://web.mit.edu/wangj/www/pap/CampbellGrossmanWang93.pdf), DOI10.2307/2118454; antecedente working paper NBER4193(1992), DOI10.3386/w4193.

Se leyó el PDF primario: resumen, medición/detrending y regresiones, especialmente pp5–10 del PDF. Pasaje breve del resumen: “the first-order daily return autocorrelation tends to decline with volume”. El estudio vincula esa relación a provisión de liquidez; en su muestra diaria de acciones interactúa retorno con volumen, considera efectos de día semanal y discute sensibilidad al crash1987. Su volumen se expresa como turnover y se resta una media anual de volumen logarítmico calculada HACIA ATRÁS, sin datos posteriores a cada fecha. Evidencia de retardos posteriores es más débil. No se trasladan coeficientes o significancia.

AA sería una adaptación propia a BTC perpetuo24/7, volumen de un solo venue y target directo24h tras un retorno4h. No replica el estudio ni presume que su evidencia valide Binance, este horizonte, nuestros costes o riesgo. El PDF fue accesible; NBER devolvió403 y el redirectDOI no fue accesible. No se usaron esos errores como contenido; el PDF del autor y su ficha identifican la publicación.

## Receta sugerida única, ex ante

Usar sólo OHLCV BTC4h ya existente, obtenido causalmente en cada cierreT4h. Índices siguientes sobre exactamente408filas cerradas consecutivas; última fila407 con aperturaT−4h.

Para C_i cierre y V_i volumen:
- r_i=log(C_i)−log(C_(i−1)), retorno4h con signo.
- v_i=log(V_i)−mean(log(V_(i−42)),...,log(V_(i−1))).
- z_i=r_i·v_i.
- y_i=log(C_(i+6))−log(C_i), retorno bruto posterior24h.

42barras previas equivalen a una semana completa24/7. Se escoge esa referencia para contener todos los bloques horarios/semanales en el baseline de actividad y separar volumen actual de su nivel reciente; es una decisión de diseño informada por calendario, no una calibración ni demostración de estacionariedad. NO se copia la ventana25de Y: aquí hay42observaciones exclusivamente anteriores, sin normalización conjunta de dos lags o magnitudes. La actual V_i no entra a su propia media. Este baseline no elimina toda estacionalidad de v ni todos cambios del venue; esa confusión permanece declarada. No se probarán otros baselines si falla.

Cada origen histórico calcula su propio v_i con42volúmenes anteriores a ÉL. Prohibido usar una media calculada enT para reconstruir sorpresas antiguas. No log1p, epsilon, winsorizar, imputar o interpretar v como turnover real.

Entrenamiento: exactamente360orígenes i=42..401, sin buscar casos anteriores. Sus targets48..407 ya maduraron enT. Característica actual i=407; no participa como origen entrenado. Las seis barras de cada target están dentro de la ventana íntegra; no se exige independencia de labels solapados.

Dos ajustes OLS separados sobre los MISMOS360casos:
- INTERACTION: y=a+b·r+c·v+g·(r·v).
- MAIN_EFFECTS: y=a+b·r+c·v.

Ambas políticas hacen pronóstico directo de y24h; no seis recursiones de retorno4h. El control contiene el efecto principal de volumen para no atribuir a interacción una prima aditiva de actividad. Los coeficientes comunes se reestiman en cada modelo anidado; comparar libros no identifica aisladamente un efecto causal de g. No usar el AR ya negativo de G como si fuera control económico equivalente.

Escalado puramente numérico sugerido: columnas no constantes del diseño se centran/escalan con media/std poblacional de SUS360valores de entrenamiento conocidos enT; aplicar exactamente esos mismos centros/escalas al punto actual. Construir r,v,r·v antes de ese escalado. Esto es parametrización de OLS, no reconstrucción de v con centros futuros respecto a su origen. Sin normalizar labels, reescalar con toda la historia o usar el current para entrenar centros.

Admisibilidad común:408OHLCV íntegros, timestamps exactos/alineados/asof y OHLC positivos/coherentes; todos los volúmenes finitos estrictamente positivos. Toda aritmética,360labels, features y ambos pronósticos finitos. Desviaciones de columnas positivas y rango completo de ambos diseños (4 y3respectivamente); si cualquier condición falla, AMBAS cash. No eliminar filas y completar con más viejas, fallback a modelo menor, pseudo-inversa de rango insuficiente, clipping, ridge, shrinkage, SEgate, selección de variables o grilla. Si se usa lstsq, su rcond numérico y criterio de rango deberán quedar explícitos antes de implementar, sin umbral de condición optimizable. La implementación requerirá revisión técnica posterior; aquí no se calcula ningún rango observado.

Señal: forecast>.0019 LONG; forecast<−.0019 SHORT; banda/equivalencias cash. Se conserva la misma regla para ambas y no se fija g<0 como filtro. Una g positiva podría dar utilidad predictiva, pero refutaría la explicación anticipada de menor persistencia con actividad elevada; no cambiar la narrativa o invertir signo después. No aceptar sólo g negativa, un lado, un horario, un año o discrepancias entre modelos tras conocerPnL.

CadaT4h es oportunidad nueva; matemática aunque ocupado, evento consumido, sin cola/reentrada en mismo timestamp de salida. Warmup sugerido420barras4h por408exigidas, sin ampliar datos: cobertura real no acreditada, motor autoridad si alguna vez se aprueba. Historia insuficiente =>cash, no importar ni rellenar.

## Gestión, cuenta y falsación

R10 entry_plan literal, R11observadorM1 y R12ARgestión usual: entradaMARKET al precio actual, stop2ATR14simple actual conocido, sinTP,24hdesde fill a frontera4h elegible, proteccionesM1 yfees terminales. ATR inválida impide plan, no transforma forecast. Una posición BTC, sin pirámides. Padres intactos.

Contrato vigente: Binance Perpetual Futures BTC-USDT, ruta1m+BTC4hdata; UTC[2020-10-15,2026-01-01), capital10000USDT,2%/6%/3xaislado, fee.00045porlado, fundingBTC histórico ON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571 con marcasproxy declaradas, slippage modelado0. NoETH/SPY/PAXG/portfolio/OI, nuevaeconomía2026, imports, stress, riesgo o gestión alternativos.

Falsación económica prefijable si root aprueba protocolo: INTERACTION debe alcanzar todas las puertas vigentes por sí misma y mejorar el neto del libro MAIN_EFFECTS bajo contrato común para sostener aporte económico incremental. Mejorar un control malo no valida estrategia. No se decide mediante p-values posthoc ni por signo de g aislado. El control se juzga también bajo gatesabsolutos, sin que su fallo salve INTERACTION. La ganancia relativa no prueba causalidad, sinergia o significancia por360labels.

Gates conservados: CAGR30mínimo/aspiración40–50%+, PF1.2, DDtecho25%/objetivo20%, M65activos/aspiración70%, Q80completos, mediana mensual calendario positiva con inactivos, neto aritmético sin dos mejores meses positivo, N100operativo preliminar sin confianza por conteo. Desarrollo ampliamente seleccionado, noOOS.

Si root decide continuar: presupuesto sugerido sólo dos economías y hasta dos reemplazos técnicos documentados; no se autoriza ahora. Después de resultados no vecinos de interacción, ventana/baseline, target, grado, regularización, hurdle, lados, coste, riesgo o gestión; no convertir AA en búsqueda de tabla o polinomio que rescate G/Y/V4.

## Matriz de deduplicación

| Antecedente consultado | Regla exacta relevante | Diferencia / límite de AA |
|---|---|---|
| ResearchV4ShockPV1h y ResearchV4Base1h/shock_features.py completos; FINAL_DECISION_V4.md | Desplazamiento1h>=2ATRprev y volumen>=2media24previos; entrada contraria inmediata; stop1ATR/TP1R/6h. Negativa antes de costes. | AA no relaja umbrales de ese evento, no conserva ni invierte su trade; estudia pendiente continua a todos los niveles con control aditivo. No refuta ni rescata aquel shock. Si se exigieran shocks como admisión, retirar por vecino. |
| BTCExploreR804 completo; BTC_R8_FINAL_RESEARCH_RESULTS_20261019.md | Suma de12volúmenes×innovaciones monetarias, primera mitad positiva/segunda negativa, confirmación bajista y setup con latch; sustituye suplemento short dentro de libro heredado. | Mismo producto genérico volumen/retorno como ingrediente no equivale al estimando: AA pregunta interacción en pronóstico24h con respuesta aprendida y control anidado; no orden de12presiones, cambio de liderazgo o suplemento legacy. Debilidad real de proximidad reconocida; root decide materialidad. |
| N204ExploreR501 completo; protocolo/cierreR5 | Cohortes positivas/negativas de cierre en rango y VWAP HLC3; separación de precios como filtro del setupN204. | AA no estima coste de cohortes, VWAP, posición de cierre o resistencia; no elimina filtro para repetir libro. |
| BtcResearchR12ParticipationBase1m completo; BTC_DISCOVERY_I_PROTOCOL_20261021.md | Impulso>=ATR con volumen escaso por fase, reparación50–100% y retorno de participación; comparaciónPHASE/PRICE. | AA no usa una segunda barra reparadora ni estado secuencial; compara respuesta al retorno ACTUAL condicionado por magnitud relativa de volumen. No intenta rescatar soporte de I. |
| BtcResearchR12ArBase1m completo; protocolo/cierreG | OLS240pares r4h→siguiente r4h, forecast recursivo6; control deriva. Gnegativa, sin vecinos beta/ventana. | Añade una hipótesis económica sobre interacción participación×dirección, no nueva beta o regularización. Targetdirecto24h/controladitivo requieren ambos nuevos brazos si se autorizan; Gnoequivalente y no se reabre como optimización. |
| BtcResearchR25VolumeLagBase1m completo; protocoloY, sin resultados | Asociación entre abs(r) y logV en dos orientaciones de lag; estados s/q/d; control s/q. | AA no usa F/R/S/D, orden de asociación de magnitudes ni celdas; usa signo/magnitudr como regressor y modificadorv contemporáneo. No se cambia el estimador de Y para mejorar su curva. |
| RESEARCH_PROTOCOL_V1.md y cierresV1/V4/V5 | Funding/OI como filtros; OIcreciente24h común a lados, fundingextremo/carry/normalización. | AA no añade esos datos. Un filtro por volumen del setup precio antiguo sería insuficiente novedad; aquí control conserva principales y cambia sólo interacción. |

Fuentes documentales adicionales: Hubr23index/revision/HANDOFF/DISCOVERY_RESULTS; BTC_INDIVIDUAL_EVIDENCE_MATRIX_20261021.md; historialr4; cierresR4/R5/R6/R8 yR20/R40leídos. No se encontró una ejecución equivalente en fuentes consultadas, pero no se afirma búsqueda exhaustiva de todo el servidor ni novedad universal de usar volumen para condicionar reversión.

## Objeciones antes de aprobar

La evidencia primaria es de acciones/turnover diario, no volumenBTC4h. El baseline semanal no replica su tendencia anual; el horizonte24h puede diluir un efecto breve. Volumen puede estar confundido con volatilidad/noticias/horario; sin shock exógeno no hay identificación causal. La interacción añade un parámetro y puede aumentar ajuste sin aportar utilidad fuera del mismo desarrollo.360casos con labels solapados no aportan360muestras independientes. No se propone añadir más controles, filtros o horizontes después de fallar para sostener la narrativa.

AA aporta una pregunta de interacción económicamente motivada que root puede rechazar por proximidad a las líneas cerradas. Este documento no da por aprobada esa evaluación ni inicia protocolo, código o motores. Alternativa de disposición/coste de tenencia queda en documento AB_HOLD por datos no disponibles.

## Límite de adaptación a mercado24/7

La propuesta usa BTC nativo continuo, barras4h UTC y target24h: no porta horario bursátil, sesiones de acciones, coeficientes, datos o calendario del estudio. Su autocorrelación diaria de índice y el forecastBTC seisbarras no son el mismo estimando. Stop/riesgo se calculan sobre ATR14SIMPLE nativaBTC según contrato, sin filtro de sesiones. Antes de cualquier implementación autorizada se debe leer jesse://strategy, en particular Trading Hours y adaptation workflow, y registrar esa comprobación. Este requisito queda pendiente porque no se implementó ninguna clase en esta tarea.
