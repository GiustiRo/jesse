# V3 — tres mecanismos nuevos, cribado y confirmación cronológica
Fecha: 2026-10-20. Estado: reglas económicas congeladas antes de implementación y resultados V3.
El usuario autorizó continuar de forma autónoma, iterar, analizar y definir líneas con subagentes dedicados. V1 y V2 siguen cerradas SIN_CANDIDATA; sus criterios no se modifican y sus slots no se reutilizan como búsqueda libre.

## Objetivo y alcance
Buscar una candidata histórica BTC-USDT que supere PF1,2, DD25% y resultados positivos con fricción; meta orientativa20–30% anual. Se considerará acercamiento cuantitativo un replay de confirmación con CAGR>=15%, PF>=1,2, DD<=25%, >=100 trades y resultados positivos bajo fricción, siempre presentado como evidencia histórica limitada. Un retorno por encima30% no se penaliza por ese techo orientativo. Sin promesas de rentabilidad.
BTC-USDT Binance Perpetual Futures,4h señales/1m replay completo,10000plano inicial,isolated3x,capnotionalC,riesgo2%stop+fees,fee0,00045/slippage0 nominal,fundingcontableON en todas las variantes. No gate económico funding; no ML, RST, otras monedas, live/paper, Pi, cuentas, instalaciones, reinicio, commit/push ni2026.
Datasets inmutables del freeze previo; no sustituirlos automáticamente.
ID funding exacto: 9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571.
ID OI exacto: 6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf.
Conservar límites previos: funding decimal, publicación+1m,marksproxy; OI label+6m asumido,maxage10m desde disponibilidad,ceros inválidos,nointerpolación,PITno certificado. Ventanas previas de V1/V2 ya observadas; no presentarlas como holdout nuevo.

## Seis configuraciones nominales, sin grillas
Tres líneas, cada una con P y POI24h. POI exige valor disponible actual>valor observado en T−24h, ambos>0, con primera24h de inicialización dentro de cada sesión. No se infiere dirección desde OI. Apagado no requiere calidad OI.
Cada línea tiene subagente exclusivo y propuesta exacta guardada: V3_TREND_CHANNEL_PROPOSAL.md, V3_TREND_PULLBACK_PROPOSAL.md y V3_RANGE_REVERSION_PROPOSAL.md.
Root es único escritor del registry global y selecciona finalistas; máximo dos motores globales inicialmente, uno por sector activo. Cada agente puede gestionar hasta dos según autorización, pero no superar el límite global. El tercer sector se turna al liberar un slot. Máximo dos jobs run_analysis globales, coordinados por root.
Propuestas son diseño; este protocolo decide discrepancias. Cualquier ambigüedad material se resuelve y registra antes de resultados, no a partir de rentabilidad.

## Convenciones causales comunes
En T sólo barras con open_time+4h<=T; última terminada exactamenteT y barras consecutivas requeridas. SMA_n(k) es media aritmética de n cierres terminando k barras antes de la última cerrada. Sin EMA ni semillas. ATR=A es media aritmética de14TR sobre15OHLC cerradas; mismo cálculo exacto causal de V2.
Warmup240barras4h sin operar. Nada de backfill OI desde warmup; medias/ATR sí usan velas pasadas. OHLC finito,positivo,coherente; si falta dato no habilitar entradas dependientes; mantener gestión de protección/holding.
Una entrada ejecutada por día UTC,plano/sin pendiente,sin piramidar. start<T<finish. Precio de decisión p; dirección s=+1/−1; distancia d=2A. stop_pre=p−s*d,positivo. qty=floor8(min(C/p,0,02*C/[d+fee*(p+stop_pre)])),C=available_margin antes de entrar. Fee estresada también afecta sizing. Sin leverage multiplicador.
Stop desde fill e−s*d con A congelada en decisión. Funding/slippage/gaps adicionales fuera de presupuesto2%; medir exceso, no garantizar pérdida máxima2%. Target favorable desde fill; si un target congelado queda atravesado por fill adverso, cerrarMARKET inmediato con motivo explícito, sin inventar otra orden.
Salida a primer cierre4h que cumpla holding; cierre forzado al borde con fees/slippage. No usar nuevo stop intrabar retroactivamente; gestionarlo sólo después de esa barra cerrada. Guardar motivos, distancias/riesgo, features/timestamps y procedencia acotada (<1900caracteres/línea) y contadores mensuales.

## L1 — CHANNEL, ruptura y tendencia
Entrada por estado: long C0>máximo high de20barras anteriores (excluye B0), C0>SMA120(0) y SMA120(0)>SMA120(6); short espejo respecto mínimo low/SMA/pendiente. Exigir126barras cerradas consecutivas.
Stop inicial2A. Sin TP ni salida SMA/canal adicional. Holding máximo42barras4h=7d.
HWM/LWM anclado al fill y actualizado sólo con extremos de barras cerradas de open_time>=opened_at. En cada cierre, candidato long=HWM−3*A_actual, short=LWM+3*A_actual; sólo ratchet favorable, nunca aflojar. Si nuevo stop ya quedó atravesado al precio de decisión, cerrarMARKET ahora, no rellenar al nuevo stop retrospectivo. Si ATR actual inválido, mantener stop anterior y límite de holding.
Las reglas antiguas protectoras se ejecutan intrabar antes de cualquier ratchet nuevo.

## L2 — PULLBACK, reanudación tras retroceso
Long: C0>SMA120(0)>SMA120(6); C−2>SMA20(2); rango low/high deB−1 contiene SMA20(1); C0>H−1 y C0>SMA20(0). Short espejo: C0<SMA120(0)<SMA120(6); C−2<SMA20(2); toque rango deB−1; C0<L−1 y C0<SMA20(0).
Sin filtro adicional de color, volumen o SMA20vsSMA120. Requiere126barras cerradas consecutivas.
Stop2A y objetivo3R=6A desde fill, ambos fijos; no trailing ni salida por media. Holding18barras4h=72h.

## L3 — RANGE, retorno a media bajo poca deriva
Bandas SMA20(k)±2*std20(k,ddof0); z(k)=(C−k−SMA20(k))/std20(k),ventana incluye su propia barra cerrada. Varianza positiva finita.
Régimen: abs(SMA120(0)−SMA120(24))/A<=0,5;24barras=96h, distinto de OI24h. Requiere144barras cerradas consecutivas.
Long cruce fresco z(1)>=−2 y z(0)<−2; short z(1)<=2 y z(0)>2. Sin filtro de R mínimo adicional.
Stop2A desdefill; objetivo SMA20(0) de decisión congelada (no recalcular en posición). Debe estar al lado favorable de precio de decisión y del fill; de otro modo rechazar antes o liquidar inmediatamente trasfill.
Holding12barras4h=48h. Sin trailing. No es una repetición de RangeFade5m: cambia horizonte y régimen; esa estrategia sigue descartada.

## Fase A — cribado de mecanismos, seis sesiones continuas
Desarrollo [2020-09-01,2024-01-01), seis sesiones nuevas, una por especificación. Las reglas no se optimizan en esa ventana; screening no es validación independiente. Capital se transporta dentro de cada sesión.
Gates: >=30trades,neto>0,PF>=1,2,absDDmotor<=25%. Además al menos dos de los tres años completos2021/2022/2023 deben ser positivos por equity anual;2020parcial se reporta sin tratarlo como año completo. No gate de CAGR de desarrollo; reportarlo con su duración real.
Máximo dos finalistas entre elegibles, orden menorabsDD,mayorPF,menorturnover,menosfeaturesOI,ID lexicográfico. Guardar shortlist y fuentes completas/hashes antes de consultar resultados2024–2025.
Si ninguna pasa, cerrar V3 SIN_CANDIDATA y la siguiente iteración necesita hipótesis nueva y protocolo nuevo; no barrer períodos/multiplicadores para rescatar una línea. Usuario autorizó iterar, pero cada nuevo ciclo conserva historial de intentos/datos vistos.
Este cribado sustituye conscientemente las48sesiones de exploraciónWF de seisconfiguraciones por una etapa inicial de falsación más económica. No se afirma selecciónprevia a2022/2023 a partir de ver todo2020–2023.

## Fase B — confirmación walk-forward2024–2025
Sólo finalistas congeladas. Cuatro folds C1–C4 de medio año:2024H1,2024H2,2025H1,2025H2. Train expansivo desde2020-09-01 hasta inicioeval, fin exclusivo. Los trains C1 equivalen a screening si fuentes/config/ventana exactas, reutilizar.
Antes de cada eval, evaluar gate train (>=30,neto>0,PF>=1,2,DD<=25) para cada finalista; guardar decisión entre ellas con mismo ranking o SIN_CANDIDATA. No usar su eval para elegir. Todas las finalistas se pueden evaluar para diagnóstico, pero sólo elegida contribuye al selector.
No consultar métricas2024–2025 antes de shortlist;2026cerrado. Reserva interna no virgen por investigaciones antiguas.
Hasta dos finalistas×cuatrofolds×train/eval=16slots nominales, de los cuales hasta dos trainsC1 reutilizan screening. Cuando pasadoevaluado entra train siguiente, reglas no cambian.
Para cada finalista, calendario de ventanas en las que individualmente pasa train se conserva como política fija de exposición para su replay posterior; se informa separado del selector que elige una entre dos. Ese calendario no depende de evaluaciones ni cambia por estrés.

## Fase C — replay continuo de capital y robustez
Hasta dos replays nominales [2024-01-01,2026-01-01), uno por finalista,10000 iniciales con capital transportado. Entradas habilitadas sólo en sus semestres elegibles por train; cierre de posiciones en cada borde semestral, sin reiniciar capital. OI mantiene historial causal a lo largo del replay, a diferencia de sesiones semestrales reiniciadas; cuantificar diferencias, no exigir igualdad ficticia.
Reporte adicional del selectorWF reescalado y su supuesto de reinversión, sin confundirlo con replay real.
Gates para considerar una finalista candidata histórica: replay neto>0,PF>=1,2,DDmotor<=25%,>=100trades,almenos3de4semestres positivos por equity delreplay y CAGR nominal>=15% como acercamiento a20–30. CAGR=(saldo_final/10000)^(365/días_exactos)−1; no anualizar sólo mejor semestre. Si<CAGR15 pero pasaotrosgates, registrar progreso parcial sin marcar objetivoalcanzado.
Fricción por replay: S1fee0,0009/slip0;S2fee0,00045/slip5bps;S3fee0,0009/slip10bps. Mantener calendario de exposición nominal, sin nueva selección en estrés. Deben quedar netosS1 yS3>0 yDD<=25 para promoción, reportar PF/trades/CAGR también.
Vecindad por replay dos variantes sin elegir ganadora: escala0,9 y1,1 de distancias protectoras; stop1,8A/2,2A. CHANNEL trailing2,7A/3,3A; PULLBACK target5,4A/6,6A; RANGE mantiene media congelada, sólo cambia stop/sizing. Ambas deben quedar neto>0,DD<=25; si no,FRÁGIL.
Retraso OI adicional1barra4h por replay si usaOI, frescura en reloj original, referencia igualmente retrasada y siete decisiones inicialización. Debe seguir neto>0,DD<=25;si no,FRÁGIL.
Sensibilidad marksproxy por run_analysis de cashflows×0,5/1,5 con cantidadesfijas (no replay). Informar cambio de signo; no costes exactos certificados.
No MonteCarlo/RST/bootstrap automático ni ajuste de stops por resultados. Probar futura independencia requiere2026autorizaciónespecífica o datosprospectivos; no se abre por alcanzar gates históricos.

## Presupuesto y verificaciones
Máximo36slots económicos nominales V3:6screening+16confirmación+2replays+6fricción+4vecinos+2lagOI. Reutilizaciones cuentan como slots pero no runs nuevos. Si no usaOI, lag se reutiliza y no crea otro parámetro libre. Hasta tres smokes técnicos adicionales de7d [2020-09-01,2020-09-08), uno por línea, sin usar su rentabilidad para elegir parámetros.
Antes de economía: tests deterministas de señaleslong/short, medias sinsemilla,cruces/toque/bandas, prefijos ymutaciónfutura, entradas inválidas, protecciones/ratchet yvela postfill; fuentes completas de base/helpers/subclases,hashes,config,datasets yregistro de fuente/ejecución. No modificar V1/V2.
Todos los resultados viaMCP; análisis run_analysis sólo inputs/→output/, sinresearch_scripts/CLI/DB/credenciales. Backend/motor existentes; no instalar ni reiniciar. Ante timeout consultar mismajob/sesión; guardarrawcompleto, no duplicar; siMCPunavailable parar dependientes hasta respuestaexitosa, sinworkaround.
Root audita contabilidad y selección, sectores guardan fuentes/progresos/auditorías exclusivos. Errores máximo1e-6USDT numéricos. Registrar meses/años/longshort/gross/fees/funding/turnover/exposición y motivos de rechazo/salida. Cada sesión citada incluye dashboard_url real.
Estados: SIN_CANDIDATA,RECHAZADA,FRÁGIL,INCONCLUSA oCANDIDATA_HISTÓRICA. Nada autoriza live/paper. Siguiente ciclo si hacefalta declarará todo lo observado y se prerregistrará de nuevo; no se promete hallar rentabilidad por insistir.
