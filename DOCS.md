# Índice para agentes

Leer este archivo antes de trabajar en el repo. Aquí están solo el mapa y las decisiones vigentes; el detalle vive en los documentos enlazados.

## Documentos

| Documento | Para qué |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Convenciones del framework Jesse: tests, API, typing y publicación. |
| [`bot/AGENTS.md`](bot/AGENTS.md) | Reglas generadas por Jesse para trabajar estrategias vía MCP. |
| [`LIVE_ADAPTER.md`](LIVE_ADAPTER.md) | Adapter live open source; no instalar el plugin comercial. |
| [`bot/README.md`](bot/README.md) | Proyecto ejecutable, estrategias y tab ARMAS. |
| [`bot/docs/local-research.md`](bot/docs/local-research.md) | Réplica Docker local para backtests y Monte Carlo. |
| [`bot/docs/raspberry-pi.md`](bot/docs/raspberry-pi.md) | SSH, rutas y operación de la Pi. Local y gitignored; no copiar secretos al chat ni a git. |
| [`bot/docs/socks-proxy.md`](bot/docs/socks-proxy.md) | Salida SOCKS hacia Binance. |
| [`jesse/mcp/resources/funding.md`](jesse/mcp/resources/funding.md) | Funding/OI: fuentes, MCP/UI, contabilidad y límites de live. |
| [`.claude/skills/jesse-strategy-tests/SKILL.md`](.claude/skills/jesse-strategy-tests/SKILL.md) | Cómo escribir tests de estrategias y del motor. |
| **[r56 `PROTOCOL_R56.md`](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261026-r56/PROTOCOL_R56.md)** | **Ronda en curso: detección de régimen cripto como pronóstico de estados (vol, tendencia, rango), sin PnL, con contador N_régimen aparte (techo 30) y puente fijo a r57.** |
| [r55 `PROTOCOL_R55.md`](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261026-r55/PROTOCOL_R55.md) | Ronda cerrada: regímenes de BTC, motor cripto, ranking ML, Brent–WTI e integración. Candidata P-r55; agenda en el [handoff a r56](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261026-r55/HANDOFF_R56.md). |
| [r51 `PLAN.md`](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261025-r51/PLAN.md) | Cortos, bono y WTI con reglas propias y pronósticos continuos sobre P1. Reglas y puertas en [`PROTOCOL_R51.md`](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261025-r51/PROTOCOL_R51.md). |
| [r50 `PLAN.md`](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r50/PLAN.md) | Varios motores, universo de 10 activos, dos lentes; cerrada con P1 ([cierre](bot/strategies/FundingOiPilot4h/reports/R50_CLOSE_20261025.md)). |
| [r49 `PLAN.md`](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r49/PLAN.md) | Puertas, riesgo y costes heredados por r50; r49 cerrada sin candidata ([cierre](bot/strategies/FundingOiPilot4h/reports/R49_CLOSE_20261024.md)). |
| [`r50_harness.py`](bot/research_scripts/r50_harness.py) | Arnés de investigación r50 (barras, cuenta, métricas); `repro` lo valida contra las sesiones Jesse de r49. |
| [r49 `HISTORY_SUMMARY.md`](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r49/HISTORY_SUMMARY.md) | Todo lo ejecutado hasta r48 en una página. Leerlo antes de proponer un experimento. |
| [`TRIAL_REGISTRY.json`](bot/strategies/FundingOiPilot4h/reports/TRIAL_REGISTRY.json) | Registro global de ensayos (N para el Deflated Sharpe). Toda corrida económica nueva se agrega aquí. |
| [Hub `index.json`](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/index.json) | Revisiones del Hub; vista en <http://localhost:9200/#/research>. |

## Dónde trabajar

- Investigación, backtests y Monte Carlo: PC local, <http://localhost:9200>, MCP `jesse-local`.
- Live y administración de la Pi: <http://192.168.1.10:9100>, MCP `jesse-pi`, solo si la tarea lo pide. Hoy en la Pi solo corre una POC (`TemaTrendFollowing`), no una operativa.
- No copiar `.env`, volúmenes ni la base completa entre ambas. La réplica local no tiene claves y no opera.

## Organización del espacio de investigación

- `bot/strategies/` contiene solo estrategias vigentes: referencias, bases de medición y sus dependencias.
- `bot/archive/strategies/` guarda las 661 carpetas de rondas cerradas, con su código y reportes. Para re-ejecutar una, primero hay que devolverla a `bot/strategies/`.
- El tag git `research-archive-r48` guarda el estado completo previo a la limpieza, incluidos los volcados crudos `*_PART_NN_*.json`. Esos volcados ya no se versionan: se regeneran desde la base de Jesse.

## Decisiones vigentes (r56, 2026-10-26)

- **r56 en curso** ([protocolo](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261026-r56/PROTOCOL_R56.md)), con el plan aprobado por el usuario:
  - **Objetivo:** pronosticar el régimen de cada moneda de U50 a 20 días en tres ejes (vol por nivel, tendencia y rango), sin PnL. Las estrategias por régimen quedan para r57, solo si se cumple el puente del protocolo (§6).
  - **N_régimen** es un contador aparte, con techo de 30, en `TRIAL_REGISTRY.json → regime_trials`. **La N de estrategias sigue en 140.**
  - **Exclusión levantada solo en r56 y en formato agrupado:** HMM (filtrado, como vara) y GBM vía sklearn.
  - **Autorizado** instalar `torch` + `chronos-forecasting` en el contenedor de investigación para la familia T.
  - **Holdout:** 16 alts intocables hasta F5. 2025 sellado y 2026 reservado.
  - **F0 cerrada:**
    - etiquetas fijadas, con la enmienda F0-1: la vol pasa de cociente a nivel;
    - la persistencia solo tiene contenido en la vol;
    - tendencia y rango cambian ~40 veces por año, así que su vara es la climatología.

## Decisiones r55 (2026-10-26)

- **r55 cerrada (2026-10-26)** ([cierre](bot/strategies/FundingOiPilot4h/reports/R55_CLOSE_20261026.md), [handoff a r56](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261026-r55/HANDOFF_R56.md)).
  - Candidata: **P-r55 = P1 sin bono**.
  - 2025 sigue sellado por decisión del usuario: queda reservado para un candidato nuevo preregistrado (ML3 es el propuesto). N = 140.
- r55 preregistrada (2026-10-26) ([protocolo](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261026-r55/PROTOCOL_R55.md)), con el plan aprobado por el usuario.
  - **Regímenes de BTC**, fijados antes de sumar N, con un solo parámetro k = 0,5:
    - etiqueta trimestral ex post (±k·σ anual previa·√0,25) para juzgar;
    - estado diario causal T90 (±0,5) para operar.
  - **Presupuesto:** N parte de 125; techo de 143. El tuning anidado de GBM queda fuera por decisión del usuario.
  - **Advertencias declaradas:**
    - 2024 ya no es limpio para el ranking;
    - U50 tiene sesgo de supervivencia, que favorece a los libros largos;
    - A3 y los activos de validación ya tienen 2025 visto, así que A3 v2 solo puede entrar como provisional.
  - 2025 se abre una sola vez, sobre la cartera congelada y con autorización del usuario. 2026 sigue reservado.
  - **Estado tras F4:** F1 (E1–E3), F2 (ML1–ML4) y F3 (A3 v2) no pasan.
    - ML3 (C6 solo en las alts del top-10 de X1) cumple la inclusión, pero falla la puerta bajista.
    - En F4 no entra ningún activo marginal y sí «R1 sin bono».
  - **P-r55 = P1 sin bono**, congelada en [`P55_FREEZE.md`](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261026-r55/P55_FREEZE.md): 2018-09→2024 Sharpe 1,677; 2021–24 1,723. N = 140.

## Decisiones r54 (2026-10-26)

- **r54 cerrada (2026-10-26)** ([protocolo](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261026-r54/PROTOCOL_R54.md)): primera validación independiente de C6.
  - C6 congelado generaliza en 48 alts: 32 positivas, canasta con Sharpe 1,03 y t 2,05 en 2021–24. SOL, XRP y BNB positivas.
  - Sumarlo a P1 no diversifica (W1 rechazado) y el meta-labeling no aporta (AUC 0,43).
  - P1 sin cambios; 2025 sellado. N = 125.
- Los informes R52–R54 se guardaron por MCP el 2026-10-26, tras reiniciar Docker Desktop (la red de Docker se había caído).

## Decisiones r53 (2026-10-26)

- **r53 cerrada (2026-10-26)** ([protocolo](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261026-r53/PROTOCOL_R53.md)): seis carteras alternativas del ranking y C6 filtrado por QOI.
  - Ninguna pasa; P1 sin cambios; 2025 sigue sellado. N = 123.
  - Y4 (largo en las mejores por rango, filtro de cola, cubierto con BTC/ETH) queda al borde: Sharpe 0,49 contra 0,5, 2024 +0,27, ρ −0,02.

## Decisiones r52 (2026-10-26)

- **r52 cerrada (2026-10-26)** ([protocolo](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261026-r52/PROTOCOL_R52.md), [handoff a r53](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261026-r52/HANDOFF_R53.md)): universo de 50 perpetuos cripto activos (sin deslistados, decisión del usuario).
  - Ninguna manga nueva pasa; P1 sigue sin cambios; 2025 sellado sin abrir. N = 116, sin techo por decisión del usuario.
  - El ranking ML tiene IC semanal 0,106 (t 5,6), pero las colas de la pata corta anulan el spread medio.
  - El reloj del flujo (QOI) replica (t 2,9), pero no paga costos solo. El jump model no mejora a P1.
  - Datos: `research_scripts/r52_download.py` (host; el DNS del contenedor cayó).
- Mandato del usuario: investigación autónoma, rondas siguientes en sesiones nuevas.

## Decisiones r51 (2026-10-25)

- **r51 cerrada (2026-10-25)** ([cierre](bot/strategies/FundingOiPilot4h/reports/R51_CLOSE_20261025.md)): P1 sigue sin cambios, ahora confirmada en Jesse (10/10 corridas). En 2021–25 la curva R1/bono se toma de Jesse. Ninguna de las 10 mangas nuevas pasa (cortos, bono/WTI propios, pronósticos Carver). A3 (spread Brent–WTI, Sharpe 1,21) quedó vetado por el DD de 2013 y es la hipótesis a preregistrar en r52. N = 108.
- r51 (2026-10-25), plan aprobado por el usuario:
  - Cortos como prioridad central y reglas propias para bono, WTI y gas.
  - Pronósticos continuos estilo Carver como enfoque transversal; ML diferido.
  - SOL/XRP/BNB diferidos a r52; paper fuera de alcance; 2026 sigue reservado.
  - TLT diario 2002–2025 como lente larga del bono que solo veta.
  - Primero se confirma P1 en Jesse (≤10 corridas). N parte de 98, techo 115.

## Decisiones r50 (2026-10-24)

- **r50 cerrada (2026-10-25)** ([cierre](bot/strategies/FundingOiPilot4h/reports/R50_CLOSE_20261025.md)): candidata P1 = R1 (ensamble Donchian en los 7 activos del núcleo) + C6 (rupturas cripto R2+R3 en BTC/ETH), 100% futuros USDT-M, congelada en `5caf4a53`. Cumple 6/8 metas r9 en 2018–25 y 3/8 en 2021–25; nunca alcanza M65/Q80. Pendientes para r51: F4 en Jesse, validación independiente con activos operables nuevos (SOL, XRP, BNB, DOGE) y 2026, y la decisión sobre bono y WTI. La reversión de corto plazo no generaliza; el carry de funding queda fuera (usa spot).

- **r49 cerrada** sin candidata: la tendencia sobre 3–4 activos no sostiene Q80 en historia larga.
- **Objetivo r50:** varios motores con perfiles distintos, sin dar ninguno por sentado:
  - M1 tendencia v2;
  - M2 reversión de corto plazo;
  - M3 corto con régimen;
  - M4 valor relativo ETH/BTC;
  - el funding (M5) solo como freno o filtro.
  
  Se mantiene la ambición r9 de cartera (abajo).
- **Universo (10 activos operables en Binance USDT-M):**
  - núcleo de diseño: BTC, ETH, oro, SPX, WTI, gas natural y bono largo de EE.UU.;
  - validación: plata, Nasdaq 100, cobre, EWJ y EWY, que solo se usan con motores congelados en la F3. EWJ y EWY se sumaron el 2026-10-25 y van con datos diarios de los ETF (Yahoo). El platino se pidió pero quedó excluido por datos.
- **Dos lentes:**
  - la ventana común decide: 2020-10 → 2025, o 2018 → 2025 en los motores cripto con spot;
  - la ventana larga por activo solo veta: oro, SPX, WTI y gas desde 2012; BTC/ETH spot desde 2017-08, en símbolos aparte, sin funding ni empalme. El bono no tiene lente larga (Dukascopy desde 2018-03, decisión del usuario).
- **2026 reservado por definición:** ningún dato posterior al 2025-12-31 se mira ni se usa hasta que el usuario lo apruebe.
- **Iteración:** con `bot/research_scripts/r50_harness.py`, validado contra Jesse. Jesse se usa para confirmar en la F4, con ≤10 corridas.
- **Scripts:** el usuario autorizó scripts en `research_scripts/`, las descargas de los 10 activos y el push de la rama para r50.

Lo que sigue viene de r49 y continúa vigente salvo lo dicho arriba:

- **Objetivo (r49):** cartera BTC–PAXG–SPY con descorrelación real, evaluada como cartera.
  - Puertas de cartera: CAGR neto ≥30% (aspiración 40–50%), DD ≤20% (techo 25%), PF ≥1,2, ≥65% de meses activos positivos, ≥80% de trimestres positivos, mediana mensual >0 y resultado positivo sin los 2 mejores meses.
  - Puertas de cada manga: Deflated Sharpe ≥0,95 con N declarado, Sharpe neto ≥0,8, ≥100 trades (≥30 si es diaria), los 5 mejores trades <60% del PnL y superar a los benchmarks nulos.
- **Riesgo (perfil intermedio):**
  - volatilidad objetivo de cartera 16–18%;
  - techos: 3% por trade, 8% agregado, 5x aislado;
  - freno de DD: en −12% el riesgo baja a la mitad hasta volver a −6%;
  - cota ¼–½ Kelly.
  
  Reemplaza el perfil fijo 2%/6%/3x.
- **Costes base:** fee 0,00045 por lado (taker con BNB) y funding aplicado y verificado. Exits maker cuando aplique. Las candidatas se estresan con slippage de stop de 3–5 bps y fee 0,0009.
- **Datos:** desarrollo con 2020–2025. 2026 ya fue observado (K1001 y candidatas archivadas): es in-sample para cualquier regla diseñada después del 2026-10-19. Excepción: la OOS de `BtcMomentumCore4h`, congelada antes de esa fecha.
- **Fuera de alcance:**
  - señales de menos de 1h sin ejecución maker modelada;
  - HMM/LightGBM sobre un solo activo;
  - funding/OI como señal de entrada (solo sirven como freno de riesgo);
  - rescatar vecinos de rondas cerradas.
- **Proceso:**
  - hipótesis contrastada con `HISTORY_SUMMARY.md`;
  - presupuesto fijado antes de ejecutar;
  - cada corrida económica se agrega a `TRIAL_REGISTRY.json`;
  - un informe corto por tanda;
  - auditoría contable completa solo para candidatas;
  - máximo 2 backtests simultáneos.
- **Live:** paper, live, cambios en la Pi o en la configuración global requieren autorización explícita. No ejecutar `jesse install-live` ni definir `LICENSE_API_TOKEN`: es un repo open source 100% customizable.
- **Operativa en Binance:** perpetuos USDT-M, una sesión por cuenta (one-way netea el símbolo). Toda estrategia candidata debe operarse solo con futuros USDT-M; spot (por ejemplo BTC/ETH desde 2017) se usa únicamente como proxy de datos históricos, nunca como pata operada.
- **Seguridad:** no commitear `.env`, `bot/docs/raspberry-pi.md` ni claves, y no imprimirlas.
- **Frontend:** el que se sirve vive en `jesse/static/`. Sus módulos Nuxt distribuidos están en `_nuxt/`; las extensiones editables quedan fuera de esos bundles.

## Histórico

Los acuerdos r5–r11 y r9 (BTC individual, 2%/6%/3x, puertas por pieza), el handoff de Fase 2 ([`bot/docs/multi-asset-pivot-handoff.md`](bot/docs/multi-asset-pivot-handoff.md)) y los protocolos OOS de K1001 quedan como evidencia histórica, superada por r49. Sus veredictos no cambian. Ver `HISTORY_SUMMARY.md` y `RESEARCH_HUB/revisions/`.
