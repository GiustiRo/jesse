# V5 Funding Trend — C1 evaluación2024H1

Selección previa SELECTION_V5_C1.json guardada2026-10-21 01:11:54UTC: ambas elegibles por trainSCREEN reutilizado y OI elegido por menorDD. Esta elección permanece OI pese al resultado observado; no reasignar retrospectivamente a FP.

| Sesión [2024-01-01,2024-07-01) | Trades | Neto% | PF | DD motor% |
|---|---:|---:|---:|---:|
| [OI seleccionado](http://localhost:9200/#/backtest/f9c5a6f5-e7f7-45f8-9cd4-c7f51bd977f0) | 14 | −2.756309 | 0.717979 | −6.822363 |
| [FP diagnóstico](http://localhost:9200/#/backtest/b3a5c7e3-99b2-4540-a928-6927af51a602) | 18 | −2.720469 | 0.760388 | −7.545336 |

Ambas finished/errornull. OI saldo9724.369133,fees50.477182,funding+42.419848; FP saldo9727.953097,fees65.902292,funding+54.444067.2024H1 ya fue observado por ciclos previos: confirmación interna reutilizada, no OOSvirgen. No inferir rechazo o promoción definitiva por un solo semestre; root continúa únicamente según protocolo y GO por etapa.

Auditorías propias PASS: logs completos3páginas cada una (910OI/960FP), máximos1022/1023caracteres. Cada sesión1092decisiones,6meses y546publicaciones canónicas únicas;546SHA por sesión recalculados de tokens JSON originales yrawaccessor/asof/gaps/signos válidos. Causas featureidénticas:240no_setup_price,351setup,460carry_sign_reject,41funding_mixed. OIprimary14allowed/277in_position/57oi_nonrising/1oi_initialization/2daily_limit; FP18allowed/331in_position/2daily_limit,además de causas no_setup/carry/mixed yfrontera final.

Todos32planes/entradas/cierres short verificados: SMA120/C30/trío,stop3ATRdesde fill,fee/riesgo2%/cap1x,cuotaUTC ydatosOI de14entradas. OIcierres6trend/4funding/3stop/1fold_end; FP11trend/4funding/2stop/1fold_end. Contadores precierre13/17exits más1fold_end cada uno concilian14/18trades. Metadataopen_trades1/open_pl es anterior a cierre final; V5_CLOSE final lo confirma. Sin longfill/maximumhold real enC1; no afirmar cobertura de esas ramas.

IncidenteFP: run_backtest respondió HTTPConnectionPool127.0.0.1:9000 Read timed out10s. Raw completo conservado; se consultó el mismoID yrecuperó running→finished, sin nuevo start ni duplicado. OIstart normal. Todos prerun/config/datasets/bounds exactos ytimestamps conservados enV5_C1_BRANCH_PROGRESS.json. Auditorías AUDIT_ResearchV5FT_OI_C1V.json yAUDIT_ResearchV5FT_FP_C1V.json contienen todos los planes/ventanas deentrada/buckets/cierres ymanifiesto dehashes. Root realiza conciliación financiera completa por snapshots. No jobs propios,nuevas fuentes,drafts niC2sinGO.
