# BTC — protocolo congelado R7

## Hipótesis y presupuesto

Separar defensa de ganancias del suplemento MARKET y convivencia con el corto STOP original. Evidencia anterior: P604 cuatro salidas ganadoras ya en N503, dos mejoran/dos empeoran; neto marginal19.25/25.31USDT; dosSTOPnuevos pierden. N503 ventaja concentrada en2023 ycapitalcompartido.

14backtests nominales:2control de observación N503ObserveR700(B/C),6recetas×2B/C. Máximo2backtests simultáneos,2análisis simultáneos; sin agentes nuevos. No añadir recetas tras resultados. S701 es control de mecanismo esperadoidénticoP604, no indicador nuevo ni evidencia independiente. Dos transferencias a N204 controlan dependencia del filtroER.

### S701 — N503ManageR701

Semilla N503. P604 con salida sólo si E-C>fee*(E+C); mismo shadowR exacta siguientevela. Control económico esperado: las4salidas anteriores ya eran rentables, posible identidad P604, no nueva evidencia.

### S702 — N503ManageR702

Semilla N503. Defensa de beneficio por estructura: desde2velas4h completas postfill, C_actual>H_velaprevia completa Y E-C>fee*(E+C), cierreMARKET. SinR/G ni shadow.

### S703 — N503ManageR703

Semilla N503. Defensa de beneficio por devolución: mejorC=mincierres4hcompletospostfill, ganancia máximaE-mejorC>0, E-C>fee*(E+C), C-mejorC>=.5*(E-mejorC), cierreMARKET. Fracción1/2prefijada, no barrido.

### S704 — N503ManageR704

Semilla N503. Convivencia condicionada al beneficio: primera4hcompletapostfill R(current)True Y E-C>fee*(E+C), cierreMARKET. P603 con puerta de beneficio; sinshadow.

### S705 — N204ManageR705

Semilla N204. Transferencia exacta S702 a N204 sinER; sincombinarotrosfiltros.

### S706 — N204ManageR706

Semilla N204. Transferencia exacta S703 a N204 sinER; sincombinarotrosfiltros.

## Reglas técnicas comunes

Sólo cierres de velas4h enteras tras fillreal; excluirvela deentrada parcial; reloj contiguo/actual, idempotencia por decisión, reset porfill; deadline48hprioritario. Beneficio calculado a cierreobservado descontando feeentrada+salida, E-C>fee*(E+C),cantidadcancela; no es garantía del fillposterior ni beneficio con overlays. Sinparciales,nuevasentradasoriginalesforzadas ni shadowcontabilizado comofill. SL1R,TP2R,geometría yprioridad originalesintactas. Registro de todas las liberaciones con causa/reloj/profitunit/cantidad; control R700 registra contextosR yeventosN503incluidoocupado, sin tocarplan/ledger/órdenes ni varsdeoperativa. ContextoR conservahelperpuro R6:140velascontiguascerradas, EMA120sube[-1]>[-10],C>EMA120−ATR,RSI3<=20,e=minL/C−.25ATR,d=EMA20−e entre1..3ATR y>=6fee*e. Es preparación técnica, no ordenasequible.

R700 tieneque reproducirN503B/C en todoslosfills/precios/cantidades/fees/PNLtiempos y tipos, tolerancia1e-7. Si falla, corregirúnicamentelainstrumentación,documentarcuarentena y noanalizarlocomomejoracandidata. No ajustar reglas económicas paraarreglar resultados.

## Contrato

Misma muestra2020-10-15→2025-12-31exclusiva;2026CERRADO inclusoinspección. Muestra reusada, noOOSni pruebaantisobreajuste.10000USDTcompartidos;1%trade/8%agregado;isolated5x;cap4.4;reserva.001sizing;nopyramid;fee.00045porlado;warmup240;debugtrue;fastfalse;charttrue. RutasBTC/PAXG/SPY4h y3feeds1m;PAXGMarketBEdependientefeeoriginal;SPYBSecond/CMarket. Long yshortSTOPoriginales byteidénticos, tambiénledger,sizing,HP,entrada,latch (exceptoetiquetareceta). Fundingnoimplementado.

## Auditoría y selección antes de resultados

Fills/qty/fees/PNL/wallet/terminal,MTMUTC diario4anclas;cohortessuplMARKET/STOP/long/otrasrutas. Overlays5/10bpsRTadicionales conqty/precio/tiemposfijos,no feeengine. Mesesfull61/all63,Q19/21;activosycalendarioexpresos;positivos>0sinredondeo. ReferenciaultimateN204,semillaN503oN204paraatribución,P604comparaciónmecanismo. GatesheredadosambasB/C:ΔnetN204>1e-7,+5Mactivos>=65%yQ>=80%full/all,+10net>=N204−1e-7,DDmotor>=−25%.

Añadir controles de concentración predeclarados por el diagnóstico: mínimo10salidas emparejadas modificadas respecto a su semilla en CADAcartera (umbraloperativodiversidad,nopruebaestadística);ΔMTManualN204>1e-7 en almenos3de5añoscompletos2021..2025;ΔnetN204trasdescontar aritméticamentemejormesincremental>1e-7ambas. Se calculan sobre recorridos grabados; omitir no reejecutaoperativa. Estas puertas no cambian porresultados. S701 esperado4casosnoelegible; referencias anterioresnopromovidas. RankingR6:mayormínmargenM/Q,mayorminΔ+10,menorpeorDD,IDlex.

Una única receta elegiblealcompletar14 puede activar6fullsadicionales:feeengine.00070/ladoB/C vsN204feealtoB9a6c7c24-8847-42d1-aadb-206f21723c1f/C541d2bf4-ffca-4f2d-969b-c25165e7b960;Δnetpositivo,M65/Q80full/allambas,DD25;4sensibilidadesTP1.8R/2.2RcadaB/C,restofijo. Noelegirotrasi falla,ni vecino ganador. Si ninguna elegible,ceroextras;máximototal20.

## Mantenimiento

ConsultasMCPdetextoyfuentesrespondennormalmente;0backtestsactivosalinicio. Fallo previoPNGartifact_changednosostienehipótesisdesaturaciónporfuentes. No se justifica borrar estrategias para resolverlo. Conservar fuentes/reportes/sesiones;si aparece lentitudreal,reducirconcurrencia ydiagnosticarmismoMCP. Cualquier archivado debe conservarfuenteexacta,dependencias,hipótesis,resultados,URLs,motivo de descarte ymanifiestorecuperación antes de removerdelcatálogo. No tocarcandles,configglob,live/paper,credenciales ni Pi.

## Aclaración de calendario, sin cambiar regla ni ventana

El término «añoscompletos2021..2025» en la puerta de concentración es una errata descriptiva:2025 está recortado al2025-12-30porfinish_dateexclusiva. El algoritmo congelado compara exactamente los cinco bloques anuales2021..2025 y exige3de5positivos; se mantiene sin modificación. No se reclasifica2025comoaño completo ni seusa2026. Los4añoscalendariocompletos son2021..2024;2020y2025parciales se muestran explícitamente en el informe. Mesesfull61/19Qcorrectos permanecenintactos. Esta aclaraciónno cambia seleccióneconómica, ranking ni presupuesto.
