# V5 CROSS — propuesta de cruce finito SMA20/SMA80, 4h

Autor: /root/audit, sector CROSS. Fecha: 2026-10-21 UTC (20 de octubre local).
Estado: sólo diseño previo a implementación y resultados V5. No se crearon fuentes ejecutables, drafts, jobs o backtests. La autorización nueva del usuario para V5 y V6 no abre aquí el diseño de V6.

## Evidencia previa y parentesco

Se leyeron completos por Jesse MCP los cierres FINAL_DECISION_V1.md a FINAL_DECISION_V4.md y RESEARCH_CONSOLIDATED_DECISION_20261020.md. También se contrastaron los protocolos V1/V2, las propuestas CHANNEL/PULLBACK y los protocolos V3/V4.

V1/V2 terminaron sin entrenamientos elegibles. V3 dejó CHANNEL_P como avance parcial, con 95 operaciones frente al mínimo fijo de 100 y retorno concentrado en 2024; la variante OI fue frágil. Los seis screenings V4 fueron negativos. En particular, la ventaja bruta de OSCILLATOR_P no cubrió sus costes. Ningún criterio anterior se modifica.

El cierre consolidado registra 151 sesiones económicas nuevas y 170 slots nominales hasta V4. No son muestras independientes. Los años 2020–2025, incluida la confirmación V3 de 2024–2025, ya están observados. Un prerregistro nuevo reduce discreción posterior; no restaura una reserva virgen. 2026 sigue cerrado y la excepción anterior K1001 no se extiende a esta línea. Fecha máxima: 2026-01-01 exclusiva.

DOCS vigente, según la lectura documental comunicada por root, permite explorar/definir timeframes y prioriza rentabilidad sobre frecuencia. El retorno a 4h consume configuraciones nuevas; no altera V4. Sólo MCP, sin CLI/DB/env/research_scripts, ML, instalaciones, reinicios, cuentas, Pi, live/paper, commits o push.

Hipótesis: una transición de signo entre una media rápida de varios días y otra lenta de casi dos semanas puede señalar persistencia de tendencia. Salir por transición opuesta, con protección inicial amplia y duración máxima de 30 días, permite investigar trayectorias que las salidas anteriores de horas o pocos días truncaban. No se presume que menor turnover compense retraso, financiación y whipsaws.

No es duplicado exacto:

- V1 H1/V2 entraban por ruptura del día UTC anterior, con TP y holding de 24h.
- V3 CHANNEL usaba ruptura de canal, régimen SMA120, trailing y máximo de siete días.
- V3 PULLBACK exigía toque SMA20/reanudación, TP y máximo de 72h.
- V3 RANGE y V4 RSI/shock/reset buscaban reversión o normalización de eventos.

CROSS usa un cruce fresco entre dos medias como entrada y el cruce contrario como salida. No exige ruptura de extremos, toque, oscilador, volumen o funding como señal. Comparte la familia amplia de tendencia con CHANNEL y los mismos datos: no se afirmará independencia estadística ni efecto aislado de cambiar sólo un componente.

## Elección del régimen

**Sin filtro SMA200 adicional.** El signo SMA20−SMA80 ya define orientación entre dos escalas. Añadir un tercer nivel o pendiente incorporaría selección adicional sin una necesidad mecánica suficiente. No habrá una alternativa con SMA200 si falla la nominal. Esta omisión queda fijada antes de resultados V5.

## Reloj, medias y datos válidos

BTC-USDT, Binance Perpetual Futures, una ruta 4h UTC y ejecución completa 1m. Mercado continuo 24/7, long/short simétricos, una posición neta por sesión, sin parciales ni pirámides.

BAR = 14.400.000 ms. En decisión T, B0 es la vela abierta en T−BAR que acaba de terminar. C_k denota el cierre de B−k. Sólo filas con apertura+BAR<=T; última apertura exactamente T−BAR, alineadas y consecutivas cada BAR.

SMA_n(k) = suma(C_j, j=k…k+n−1)/n, media aritmética finita inclusiva de su propia barra cerrada. No EMA, semilla ni estado recursivo.

- F0=SMA20(0), F1=SMA20(1).
- S0=SMA80(0), S1=SMA80(1).

Se necesitan exactamente 81 OHLC cerradas: la media lenta previa usa C1…C80. La media actual incluye C0; no excluir la barra de señal como en el canal V3.

OHLC finito, positivo y coherente: H>=max(O,C), L<=min(O,C), H>=L. Verificar finitud también después de calcular medias y diferencias. Sin epsilon, redondeo de comparación, relleno o interpolación. Warmup de 240 velas 4h sin operar; cubre nominal y vecinos. OI no se obtiene del warmup.

## Entradas y salidas por cruce

Entrada long: F1<=S1 y F0>S0.
Entrada short: F1>=S1 y F0<S0.

La igualdad previa permite el cruce; igualdad actual no genera señal. No basta el estado F0>S0 o F0<S0. Sin banda mínima, pendiente, ADX, volumen, color o precio frente a SMA200.

Además: plano, sin pendiente, capital disponible positivo y finito, cuota UTC libre, start<T<finish y a<T<b en el intervalo activo. Una señal bloqueada se descarta: no se guarda para entrar después sin cruce nuevo.

Salida long: solicitar MARKET al cruce short definido arriba.
Salida short: solicitar MARKET al cruce long.

Sólo en cierre T>opened_at. La salida requiere las 81 barras válidas, pero no OI, ATR actual o un filtro de régimen adicional. Si falta historia, mantener stop y holding. Un cruce omitido por dato inválido no se reconstruye después mediante condición de estado.

**No es stop-and-reverse.** Se conserva la convención V4 de no abrir otra posición en la misma decisión que cierra una posición. El cruce opuesto usado para salir no abre la contraria ni se difiere a T+1. La siguiente entrada exige otro cruce fresco estando plano y con cupo. Esto puede omitir el siguiente tramo y producir desequilibrio entre direcciones según trayectoria; no se compensará con cuotas por lado o latch.

Si root decidiera otra política de reversión, deberá registrarse como aclaración económica y actualizar esta propuesta antes de cualquier resultado, nunca interpretarse silenciosamente al implementar.

## ATR, stop, tamaño y duración

A es la media aritmética de 14 true ranges sobre las últimas 15 OHLC cerradas, offset cero:

TR_j=max(H_j−L_j, |H_j−C_(j+1)|, |L_j−C_(j+1)|), j=0…13.

No ATR Wilder. A debe ser finito y positivo. Distancia nominal d=3A, congelada en la decisión de entrada.

Con precio p, dirección s=+1 long/−1 short, capital C=available_margin antes de entrar y fee f del escenario:

stop_pre=p−s*d
q=floor8(min(C/p, 0,02*C/[d+f*(p+stop_pre)]))

Exigir precio, capital, distancia y stop_pre finitos/positivos; fee finita>=0 y q>0. Floor8 redondea hacia abajo a ocho decimales. Sin multiplicar tamaño por leverage. Isolated3x conserva la configuración de investigación; C/p impone cap nocional 1x al precio del plan. La fee estresada participa en sizing.

Con fill real e: stop=e−s*d, sin recalcular A. Si la protección queda inválida tras el fill, liquidar MARKET de seguridad con costes, conservar el trade y consumir cuota. Sin TP, trailing, breakeven, ratchet o actualización del stop por medias/ATR posterior.

3ATR deja más espacio inicial a una transición lenta a cambio de menor cantidad y posible retroceso mayor. No es una escala estimada como óptima con resultados anteriores. Funding, gaps y slippage pueden superar el presupuesto previsto del 2% stop+fees y el cap prefill; medirlo sin redimensionamiento retrospectivo.

Holding máximo: 180 barras×4h=720h=30 días desde opened_at. Cerrar MARKET en el primer cierre que cumpla la edad, aunque falten indicadores.

Prioridades: protección intrabar del motor; en decisión, calendario, holding absoluto y finalmente cruce opuesto válido. Cerrar al borde de cada fold con costes. Tras stop o holding no se reentra por estado de medias: hace falta cruce nuevo. El holding no crea reentradas periódicas.

Una entrada ejecutada por día UTC compartida entre long y short; también una entrada de seguridad consume cuota. No reiniciar capital, historia o cuota para aumentar muestra.

## Dos variantes nominales y OI24h

CROSS_P: precio/cruce/ATR/riesgo anteriores; la calidad OI no condiciona entrada.

CROSS_POI: reglas idénticas más OI actual válido y positivo mayor que el observado exactamente en la decisión T−24h, también válido/positivo. OI confirma participación y no asigna dirección. Ninguna usa un gate económico de funding.

Dataset OI:
6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf

Disponibilidad asumida label+6min, frescura de diez minutos desde disponibilidad. Guardar slot en cada decisión, incluso ausente/cero/stale. No backfill, interpolación o ampliación de freshness. Archivo retrospectivo, sin certificación PIT.

En 4h, 24h son seis barras. Primeras seis decisiones inicializan; primera referencia posible en la séptima. Si la primera decisión es Tstart+4h, la séptima ocurre Tstart+28h y referencia Tstart+4h. Buffer nominal de ocho registros incluye holgura.

El retraso robusto sigue siendo **cuatro horas de reloj**: aquí una barra 4h, no las cuatro barras 1h de V4. En T entregar current observado T−4h y referencia T−28h, con calidad en sus relojes originales. Primeras siete decisiones inicializan; referencia posible en la octava. Buffer de nueve con holgura. El replay mantiene historia durante semestres inactivos; WF reinicia explícitamente.

## Financiación y fricción

Nominal: balance10000, fee0.00045 por lado, slippage0, funding histórico ON también en P, isolated3x/cap prefill1x. Configuración por sesión; sin cambios globales.

Dataset funding:
9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571

Cashflow=−signed_qty*mark*rate_decimal, sin multiplicar leverage otra vez. Precio bruto−fees+funding=PNL y saldo terminal conciliados con tolerancia1e−6 USDT. Clasificar marcas exactas/proxy y fuentes desconocidas.

Fills[T−1min,T)→funding efectivo T→decisiones MARKET T. Una entrada T no paga ese evento; una salida MARKET T puede pagarlo. Usar effective_at y conservar settled_at raw. No funding>=finish ni velas con apertura en 2026; el cierre Tfinish apoyado en la última vela histórica no es una consulta de datos 2026.

Treinta días pueden acumular aproximadamente 90 eventos de ocho horas. El carry es material, no un haircut posterior. Cruces tardíos, lateralidad y devolver ganancias sin trailing pueden dominar una menor cantidad de comisiones.

Mantener escenarios V4: S1 fee0.0009/slip0; S2 fee0.00045/slip5bps; S3 fee0.0009/slip10bps, mediante motor y calendario fijo. S1/S3 net>0 y DD<=25 para promoción; S2 se informa sin gate nuevo. Sensibilidades proxy/global funding×0.5/1.5 con cantidades y fills fijos son descriptivas, no replays ni alternativas elegibles.

## Cuatro vecinos fijados antes de resultados

Todos conservan holding180, ATR14, salida por cruce opuesto, OI24h y configuración nominal de costes:

| Vecino | Cambio | Lo que permanece |
|---|---|---|
| R09 | Stop2.7A | Medias20/80; sizing usa su distancia |
| R11 | Stop3.3A | Medias20/80; sizing usa su distancia |
| A09 | Medias18/72 | Stop3A; cambia cruce de entrada Y salida |
| A11 | Medias22/88 | Stop3A; cambia cruce de entrada Y salida |

Los lookbacks de señal vecinos son 73 y 89 cierres respectivamente. Escalas exactas enteras, sin redondeo ambiguo. Si se llega a robustez, cada vecino debe conservar net>0/DD<=25, además de informar N/PF/CAGR/semestres. Nunca escoger el vecino ganador ni combinar cambios para salvar el nominal.

Sin variantes SMA200, holding27/33d, ATR12/16, sólo long/short o stop-and-reverse. V6 de asimetría direccional queda fuera; no usar desgloses V5 para desactivar un lado dentro de este ciclo.

## Selección y gates intactos

Root fijará presupuesto y protocolo V5 con los otros sectores antes de economía. Este sector aporta dos configuraciones nuevas; no reutiliza sesiones V3 por parentesco. No implementar hasta GO.

Screening propuesto común [2020-09-01,2024-01-01), continuo desde10000:

- N>=30, net>0, PF>=1.2, |DD motor|<=25.
- Al menos dos de los tres años completos 2021–2023 positivos por equity; 2020 parcial separado.
- Ranking: menor |DD|, mayor PF, menor turnover, menos features OI, ID estable.

Si hay elegibles, congelar shortlist/fuentes antes de su economía 2024–2025. Cuatro trains expansivos C1–C4 y selección previa a cada evaluación, separados del calendario de elegibilidad individual. C1train puede reutilizar SCREEN sólo con igualdad exacta de fuentes/config/datos/ventana.

Replay [2024-01-01,2026-01-01), 731 días,10000 iniciales y capital continuo; cuatro intervalos semestrales separados, cierres en sus bordes, sin reset de capital/OI. El selector global y las variantes individuales son objetos distintos. WF reescalado es comparador sintético, no cuenta ejecutada.

Promoción: N>=100 trades únicos, net>0, PF>=1.2, DD motor<=25, al menos3/4 semestres positivos por equity y CAGR>=15%, más fricción/vecinos/lag aplicables. CAGR=(saldo_final/10000)^(365/731)−1, sin anualizar sólo tiempo expuesto o promediar PF.

Cruces frescos y holding largo pueden dejar muestra pequeña: si falla N100 se conserva el fallo. No acortar períodos/holding, añadir reentradas o sumar trades de otros ciclos para aprobar. Meta orientativa20–30% anual no es promesa.

## Pruebas previstas y trazabilidad

No ejecutadas en esta propuesta:

- Medias con sumas manuales, constantes e igualdad; actuales inclusivas de B0 y previas independientes. Exactos81/73/89 cierres, sin dependencia de prefijos anteriores. Finitud después de aritmética y JSON seguro con None al invalidar.
- Cruces long/short, igualdad previa/actual y ausencia de reentradas por estado. Reflexión OHLC positiva invierte señales; bloquear una señal no la difiere.
- Cruce opuesto cierra sólo lado activo después del fill; no abre contraria en T o T+1 sin nuevo cruce. Faltantes no inventan cruce ni desactivan protección/holding.
- Prefijos/mutación futura, alineación4h y ventanas causales; OI24h=6 barras, lag4h=1, slots ausentes y referencia exacta sin warmup OI. Auditar todos los componentes acoplados a BAR para evitar reloj1h heredado.
- ATR14 simple sobre15 OHLC, offset0, stop3A congelado/fill, floor8/cap1x/fees y cierre de seguridad. Protección intrabar anterior a gestión; calendario prioritario,180 barras exactas y cuota UTC/deduplicación.
- Registrar F0/F1/S0/S1, períodos, timestamps/hash de ventanas, ATR, margen/qty/precio/fill/stop/riesgo, OI y funding asof. Motivos opposite_cross/maximum_hold/calendar/fold_end/invalid_after_fill y orden protectora realmente ejecutada. Líneas JSON<=1900 caracteres.
- Contadores mensuales all/long/short/none con partición exclusiva y flags, entradas/cierres, cuota y datos. Separar resumen precierre forzado de trades/ledger/saldo final.
- PF/contabilidad y equity mensual/anual/semestral desde snapshots completos; long/short, gross/fees/funding, turnover, exposición, duración, concentración y signo al retirar mejor semestre. No sumar train en evaluación ni PNL de cierres como retorno semestral.

Riesgos finales: retraso y whipsaws, ganancias devueltas sin trailing, gap/funding de30d, escasez de cruces y correlación con CHANNEL. La autorización V5/V6 no convierte la reserva muy reutilizada en evidencia independiente. Un beneficio aislado o un vecino mejor no promueven esta especificación.
