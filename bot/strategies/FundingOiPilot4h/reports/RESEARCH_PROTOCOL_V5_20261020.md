# V5 — prerregistro de cruces, VWAP móvil y carry persistente

Emitido 2026-10-21 00:47:53 UTC, antes de implementación y economía V5. El usuario pidió continuar explícitamente con V5 y V6 después del cierre V4. Esta autorización extiende el alcance anterior; no modifica V1–V4 ni abre 2026.

## Antecedentes y alcance

Hasta V4 se completaron 151 backtests económicos nuevos, 170 slots nominales con 19 reutilizaciones y 17 intentos técnicos. Ninguna candidata aprobó. CHANNEL_P de V3 dejó CAGR17,54%, PF1,35, DD18,41% y95 operaciones; no se baja el mínimo100 ni se reemplaza retrospectivamente el selector que eligió OI.

Todo2020–2025 está observado en investigaciones previas.2024–25 sólo será confirmación interna reutilizada, nunca OOS independiente.2026 permanece cerrado; la excepción K1001 no aplica. Sólo BTC-USDT Binance Perpetual Futures. Sin ML, RST no solicitado, live/paper, órdenes reales, Pi, cuentas, instalaciones, reinicios, CLI de investigación, cambios de configuración global, commits o push. Toda investigación, fuentes, sesiones y reportes por Jesse MCP local.

Tres sectores y dueños: CROSS /root/audit, VWAP /root/atr_oi, FUNDING_TREND /root/atr_p. Root mantiene núcleos, registro, auditoría financiera y selección. Máximo dos motores globales, dos por agente y dos jobs analíticos. No se inicia economía hasta compilación/checks y smoke de las tres líneas.

## Fuentes normativas y reglas únicas

V5_CROSS_PROPOSAL.md, V5_VWAP_PROPOSAL.md y V5_FUNDING_TREND_PROPOSAL.md se incorporan íntegros. Este documento ratifica las decisiones siguientes. No hay grilla ni alternativas ocultas.

CROSS: 4h. F0/F1=SMA20 actual/previa; S0/S1=SMA80 actual/previa. Long F1<=S1 yF0>S0; short F1>=S1 yF0<S0. Exactos81 cierres. Sin SMA200. Salida por cruce opuesto después del fill. No reversión ni latch: el cruce que cierra no se usa para entrar contrario en esa decisión o una posterior sin cruce nuevo. Stop fijo3ATR14 simple, sinTP/trailing, hold180barras4h=30d. Vecinos señal18/72 y22/88 cambian tanto entrada como salida; riesgo2.7/3.3ATR.

VWAP: 1h. Proxy HLC3 ponderado por volumen base en ventanas móviles24h actuales/previas propias. No es VWAP de ticks ni indicador anchoredD de Jesse. Pesos normalizados por máximo volumen, luego suma; dos pasadas media/varianza poblacional, sin epsilon/clamp. Ceros individuales permitidos, ventana toda cero inválida. S=max(desvío ponderado,ATR14simple), banda M±2S. Long C1<M1−2S1, M0−2S0<=C0<M0 yC0>C1; short espejo. Exactos25 cierres para entrada. Salida estado C0>=M0long/<=M0short, sóloT>fill, con24cierres válidos ysin exigirATR. Stop2ATRactual fijo, sinTP/trailing, hold24h. Vecinos señalK1.8/2.2; riesgo1.8/2.2ATR.

FUNDING_TREND: 4h. Estado de tendencia C0>SMA120 yC0>C30long, espejo short. Últimos tres pagos publicados estrictamente negativos long o positivos short. Tres pagos abarcan16h entre extremos; no baseline/zscore/reset. Ventana120cierres. Cada timestamp raw y tasa coinciden con accesores, separados8h±1000ms, available<=T y>settled_at; último0<edad<=8h+1000ms. Entrada por estado repetible; mismo trío puede habilitar otra decisión si plano/cupo libre. Deduplicar eventos sólo en evidencia, no consumir señal. Cero no abre ni obliga a cerrar. Salida por última tasa válida/fresca adversa (long>0,short<0), o precio<=SMA120long/>=SMA120short. Funding tiene prioridad sobre salida por precio; si funding inválido sigue activa salida de precio/stop/hold. Sólo después del fill. Stop3ATRfijo, sinTP/trailing, hold180barras30d. Vecinos señalSMA108/C27 ySMA132/C33, manteniendo tres pagos; riesgo2.7/3.3ATR.

Seis nombres/IDs/atributos nominales exactos en REGISTRY_V5.json. P es precio; PV incluye volumen; FP incluye funding. Cada pareja añade exclusivamente filtro OI creciente24h. No confundir FP/PV con controles de precio puro.

## Núcleos, datos, reloj y ejecución

Nuevos ResearchV5Base1h yResearchV5Base4h se derivan de la fuente congelada V4 para mantener no reentrada en misma decisión, prioridad calendario/hold/indicador, JSON acotado y auditoría de causas. Sólo se heredan hooks neutrales al reloj de ResearchV2Core4h, que permanece congelado. V1–V4 no se editan.

BAR1h=3600000 yBAR4h=14400000, DAY=86400000. Cada helper verifica velas cerradas, alineadas y consecutivas, última aperturaT−BAR; OHLC finitos positivos/coherentes. Aritmética finita tras medias/productos. Prefijos viejos y futuras filas no influyen. ATR se mantiene como media14TR sobre15OHLC, offset0. VWAP también calcula ATRprevio con ventana propia excluyendo última barra. Warmup240 velas de cada ruta (10d1h/40d4h), sin operar; suficiente para todas las ventanas y vecinos. No preinspeccionar velas: motor primero, importación MCP sólo ante error de datos.

Dataset funding 9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571; OI 6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf. Funding históricoON en todas las variantes, también sin filtro. Tasas finales publicadas asof, nunca tasa siguiente. Marcas exactas/proxy separadas.

OI por cada decisión incluyendo slots ausentes/cero/stale, sin warmup artificial. Referencia EXACTA T−24h:24 barras1h o6barras4h. Primeras24/6decisiones inicializan, primera referencia posible25ª/7ª; buffers26/8. Valores positivos, disponibilidad asumida etiqueta+6min y freshness10min desde disponibilidad; archivo retrospectivo noPIT. Precio sinOI no exige calidadOI. Retardo robusto adicional4h de reloj:4barras1h/1barra4h; currentT−4h/refT−28h con calidad de relojes originales ybuffers30/9.

Plan MARKET actual con capitalC=available_margin, preciop, distanciad ydireccións:
q=floor8(min(C/p,.02*C/[d+fee*(p+stop_pre)])), stop_pre=p−s*d>0.
Capital inicial10000 por sesión, isolated3x, capnocional1x; sin multiplicar q por leverage. Instalar stop desde fill real con d congelada. Riesgo previsto2%stop+ambosfees; funding/gaps/slippage pueden excederlo. Entrada de seguridad se conserva con costes yconsume cuota. Sin piramidar/parciales.

Una entrada ejecutada por díaUTC compartida longshort; no reentrada cuando v5_last_exit_at==T. start<T<finish yventanas activas a<T<b estrictas. Señal bloqueada no se difiere. Salidas intrabar protectoras según motor; decisión calendario, luego hold absoluto desde opened_at, luego indicador únicamenteT>opened_at. Final/folds cierran con costes. Fundingefectivo>=finish yvelas con apertura>=finish excluidos; cierreTfinish basado enúltima vela2025 no abre datos2026.

Fee nominal.00045, slippage0; debug/fast solicitadostrue yfast efectivo false por funding; exports/benchmarkfalse. Config completa congelada por sesión.

## A — screening

Seis sesiones continuas [2020-09-01,2024-01-01),cada una con10000. Gates sin cambios: N>=30,neto>0,PF dePNLneto>=1.2,DD absoluto del motor<=25%,almenos2/3años completos2021–23 positivos por equity.2020parcial se informa. CAGR de desarrollo descriptivo, sin gate nuevo.

Hasta dos finalistas por ranking menorDD absoluto,mayorPF,menorturnover,menosfeaturesOI,IDlex. Guardar shortlist/fuentes/config/hashes antes de economía2024–25V5. Sin elegibles se omiten fases futurasV5 yse conserva cierre negativo. El usuario autorizó V6 de forma separada: se completa según su prerregistro, sin reasignar slots V5 a nuevas variantes.

## B — walk-forward

Cuatro semestres2024H1/H2,2025H1/H2; trains expansivos desde2020Sep hasta comienzoeval. C1train reutilizaSCREEN si exacto. Para cada fold guardar gatestrain N30/net/PF/DD yselección global por ranking ANTESdeeval. Evaluar finalistas individuales permitido para diagnóstico; selección global no cambia por retorno futuro.

Hasta16slots (2finalistas×4×train/eval),incluye hasta2reutilizaciones. Wrapper sóloSTART/FINISH. Calendarios individuales de replay contienen semestres elegibles en train, distintos del selector global; sin seleccionar retrospectivamente según PNL de evaluación.

## C — replay y robustez

Hasta dos replays [2024-01-01,2026-01-01),731días,capital10000 continuo. Cuatro intervalos semestrales separados ycierres en todos bordes. OI/capital siguen continuos durante inactividad. Nominal candidato histórico requiere net>0,PF>=1.2,DD<=25,N>=100,>=3/4semestres positivos por equity yCAGR>=15% (convención365días). Meta orientativa20–30%anual, no garantía.

S1fee.0009/slip0;S2fee.00045/slip5;S3fee.0009/slip10bps. Motor completo con calendario nominal fijo, fee entra en sizing. S1/S3 net>0/DD<=25 obligatorios;S2 informativo. Cuatro vecinos por finalista, definidos arriba, todos net>0/DD<=25 requeridos. Señal y riesgo separados, sin elegir vecino ganador. RetardoOI4h también net>0/DD<=25;sinOI reutiliza nominal para ese slot. No modificar calendarios por costes o vecinos.

Sensibilidades proxy-only/globalfunding×.5/1.5 con cantidades fijas son descriptivas,no replays; fuentes desconocidas separadas. WF reescalado y replay comparados por operaciones/capital, sin vender sumas de sesiones reseteadas como cuenta continua.

## Presupuesto y auditoría

Máximo40slots económicos =6SCREEN+16WF+2REPLAY+6COST+8VECINOS+2LAG. Reutilizaciones cuentan slots, no motores nuevos. Hasta6técnicos: smoke7d2020Sep1→Sep8 por sector ycomo máximo un reemplazo por sector sólo por fallo técnico documentado. No usar PNL del smoke para cambiar reglas. Si no hay trade, no afirmar cobertura real de fills.

Antes de economía: compilar/AST/hashes, checks causales de cada señal/entrada/salida/overflow,bar1h/4h,OI24h/lag4h/slots,cuotaUTC/no reentrada,protecciónfill/riesgo+fees/cap,prioridadhold/calendario yJSON<=1900chars. Smoke engine con asserts en hooks según skill local. Fuentes/helpers nuevos porMCP; reportes.md save_strategy_report; JSON write_project_file.

Snapshotrun_analysis completo summary/metrics/trades/equity, sóloinputs/ youtput/. Nada de lectura proyecto/DB/env desde análisis, ni scripts persistentes. Validación estática con fuentes literales capturadas yAST, no importación de proyecto. Contabilidad tolerancia1e−6USDT, bruto−fees+funding=PNL/saldo, ledgerqty/mark/rate/effectiveclock yfeesfills/slippage. Reloj raw conserva jitter<=1000ms.

Logs completos, contadores por mes/dirección/features/causas, planes/cierres yprovenance. Equity diaria completa, años/semestres por calendario, PF sin duplicar trades, DDmotor ymuestreado terminal separados, Sharpe si disponible, gross/fees/funding,turnover/exposición/longshort/concentración. Zero-trades puede carecer de métricas/curvas: etiquetar ausencia, no fabricar meses/retornos.

Timeout de start: guardarraw, consultar mismoID tras recuperar lectura, jamás duplicar. Si MCPunavailable, suspender dependientes hasta lectura exitosa, sin workaround. No resets/restarts.

Estados SIN_CANDIDATA/RECHAZADA/FRÁGIL/INCONCLUSA/CANDIDATA_HISTÓRICA; criterios no se redondean ni se reducen para aprobar. Fuentes deV5secongelan después de checks yantes de economía. V6seprerregistra aparte antes de sus datos; se definirán sus mecanismos antes de los resultadosV5 para reducir selección adaptativa. El nuevo permiso amplía investigación, no convierte las reservas reutilizadas en evidencia independiente.
