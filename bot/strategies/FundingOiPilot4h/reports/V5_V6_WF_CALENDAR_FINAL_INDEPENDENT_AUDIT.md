# V5/V6 — auditoría independiente de WF, calendarios y fuentes

Fecha 2026-10-21T01:49:36.319Z. Estado: **PASS en el alcance WF/calendario/fuentes**. Fase C de replay y robustez sigue en curso; este informe no cierra los ciclos económicos ni promueve candidatas. No se iniciaron motores, jobs o drafts y no se modificaron fuentes productivas, registros ni reportes de otros dueños.

## Selección anterior a ejecución

Leídos completos los dos protocolos, shortlists, ocho SELECTION, START records y progresos. Se recalcularon gates TRAIN N>=30/net>0/PF>=1.2/absDD<=25 y ranking menorDD,mayorPF,menorturnover,menosOI,ID. Las ocho decisiones coinciden. No se aplicó gate anual/CAGR de SCREEN al train posterior ni se utilizó PNL de evaluación para elegir.

Consultados directamente 24 summaries de slots WF:12train (incluye3SCREEN reutilizados C1) y12evaluaciones, todos finished/errornull, con config nominal y fechas exactas. Las12sesiones de train terminaron antes de sus decisiones; las12evaluaciones individuales comenzaron después de la selección correspondiente. Son21sesionesWF nuevas y3reutilizaciones, no24experimentos independientes.

| Decisión | Selección | Evaluaciones individuales | Margen mínimo selección→START | Auditoría |
| --- | --- | ---: | ---: | --- |
| V5 C1 | ResearchV5FundingFPOi4h | 2 | 48.515 s | PASS |
| V5 C2 | ResearchV5FundingFPOi4h | 2 | 107.620 s | PASS |
| V5 C3 | ResearchV5FundingFPOi4h | 2 | 1.850 s | PASS |
| V5 C4 | ResearchV5FundingFPOi4h | 2 | 14.058 s | PASS |
| V6 C1 | ResearchV6EfficiencyP4h | 1 | 11.000 s | PASS |
| V6 C2 | ResearchV6EfficiencyP4h | 1 | 24.000 s | PASS |
| V6 C3 | SIN_CANDIDATA | 1 | 1.000 s | PASS |
| V6 C4 | SIN_CANDIDATA | 1 | 20.000 s | PASS |

V5 usa timestamps START de milisegundos de los progresos; V6 START records de segundos. El margen mínimo V6C3 es1segundo y el deV5C3 es1.850segundos. Se conserva esa resolución, sin inventar precisión. EnV5C1 creación de un draft comparte segundo con selección: no prueba orden estricto de creación, pero los inicios de ejecución fueron48.515/68.344segundos posteriores, cumpliendo el gate requerido. Fuentes/shortlist ya estaban congeladas.

## Elegibilidad y calendario sin PNL futuro

V5: ambas Funding elegibles individualmente enC1–C4. Global seleccionó FundingFPOI en los cuatro por menorDD histórico. Sus calendarios individuales tienen cuatro tuplas semestrales separadas, sin fusionar períodos vecinos.

V6: EfficiencyP elegible C1/C2. C3fallóPF1.180278<1.2; C4fallóPF1.064928 yDD31.494458>25. Se conservan C3/C4OFF aunque C4diagnóstico ganó+7.732447%. No se incorpora ese trade set al selector o replay activo.

Los tres replaynominales tienen START1704067200000 yFINISH1767225600000: [2024-01-01,2026-01-01). Cuatro FORCE_BOUNDARIES:1719792000000,1735689600000,1751328000000,1767225600000. También permanecen todos los bordes enV6 aunque esté inactivo2025. Capital inicial10000 y luego disponible continuo, sin reinicio semestral. El core acumula historiaOI en before antes de bloquear entradas inactivas; wrappers no añaden hooks que reseteen cuenta/historia.

FINISH es exclusivo: ninguna vela abierta en2026 ni fundingefectivo>=finish debe procesarse. El cierreTfinish puede usar la última vela2025. Summaries verifican fechas máximas ypolítica funding finish_exclusive. Esto revisa el contrato y la evidencia de fechas; no vuelve a reconstruir velas/ledgers de escenarios todavía pendientes.

## Fuentes, escenarios y protección

**67/67readbacksMCP actuales exactos** frente a fuentes congeladas:
-30nominal/helper/core (16V5+14V6).
-21wrappersWF (14V5+7V6), todos cambian únicamente START/FINISH ysin métodos.
-16wrappersreplay (11V5+5V6):3nominales,12vecinos(8Funding+4Efficiency) y1lagFPOI.

La dependencia V2 se revisó por separado: readback byteigual al literal original de V5_REPLAY_TEST_CODE.json, SHA existente577b84ebd15f27f5f598af5a4d1a3d3ed98313797656206c7691d29ad877564b. No hubo job de hash nuevo. El bloque Markdown de dependencia omite sólo newline terminal; para comparación byteexacta se usó JSONcapturado que lo conserva, no se normalizó fuente productiva.

Se revisaron las verificaciones existentes: V5PASS1002assertions/11clases yV6PASS606/5; no se repitieron tests. Se resolvió herencia de los16wrappers: calendario/bordes iguales alnominal en riesgo/señal/lag. Los costes usan la misma clase nominal, con cambios de config S1fee.0009/slip0,S2.00045/5bps,S3.0009/10bps, no exposición elegida de nuevo. La tabla de17escenariosV5 concuerda; los futuros escenariosV6 se deben auditar al ejecutar, sin afirmar aquí su finalización.

Funding nominal: SMA120/retorno30/3pagos,stop3ATR,hold180barras4h,sinTP/trailing. Riesgo2.7/3.3; señalSMA108/C27 y132/C33, conserva tres pagos; lagFPOIuna barra4h con calidad en reloj original. Efficiency nominalh.35,24deltas,stop2.5ATR,hold60barras; riesgo2.25/2.75; señalh.315/.385. Ningún wrapper introduce trailingV3 o métodos económicos. SinOI, el slotlag reutiliza nominal.

Tamaño con2%stop+ambosfees ycap1x, floor8 ycapital disponible; isolated3x no multiplica cantidad. Protección desde fill con distancia congelada. Core ordena calendario antes dehold y después salida indicadora sóloT>fill. Funding/gaps/slippage pueden exceder riesgo previsto; no se garantiza pérdida máxima2%.

## Matiz de CROSS y límites de inferencia

CROSS_P yCROSS_POI **aprobaronSCREEN V5**, pero quedaron fuera por cap2 y rankingDD: Funding13.023/15.724 frente aCROSS17.696/22.666. No son rechazadas por economía futura que nunca se ejecutó. CROSS_P desarrolloCAGR21.329%/net90.529% es resultado de desarrollo observado, noOOS ni aprobación histórica. No se sobreconcluye que los seis mecanismos/sectores carezcan de utilidad.

Los statics capturados acreditan lógica/atributos, no fills del broker, secuencia de cashflows en bordes, liquidación final real ni robustez financiera de todos los escenarios. Los snapshots de análisis no contienen logs; validaciones de logs de ejecución requieren páginasMCP y auditorías de sus dueños. Este alcance usa sus progresos/verificaciones y no sustituye sus auditorías de faseC.

2020–2025 ya está observado; WF/replays son confirmación interna reutilizada, noOOSvirgen. Las pruebas usan mismo activo/datos yno son muestras independientes. No se agregan PNLde train ni se venden sumas de cuentas reseteadas como replay continuo.

Sin divergencias materiales detectadas; incertidumbres operativas de faseC quedan abiertas hasta auditorías financieras yde ejecución finales. Evidenciacompacta y12cronologías en V5_V6_WF_CALENDAR_FINAL_INDEPENDENT_AUDIT.json. No cerrarV5/V6 con este informe.
