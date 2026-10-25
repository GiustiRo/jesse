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
| **[r50 `PLAN.md`](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r50/PLAN.md)** | **Plan vigente: varios motores, universo de 10 activos, dos lentes y fases F0–F5.** Ejecución según [`HANDOFF.md`](bot/strategies/FundingOiPilot4h/reports/RESEARCH_HUB/revisions/20261024-r50/HANDOFF.md). |
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

## Decisiones vigentes (r50, 2026-10-24)

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
  - validación: plata, Nasdaq 100, cobre, EWJ, EWY y platino, que solo se usan con motores congelados en la F3. EWJ, EWY y platino se sumaron el 2026-10-25; EWJ y EWY van con datos diarios de los ETF.
- **Dos lentes:**
  - la ventana común decide: 2020-10 → 2025, o 2018 → 2025 en los motores cripto con spot;
  - la ventana larga por activo solo veta: oro, SPX, WTI y gas desde 2012; BTC/ETH spot desde 2017-08, en símbolos aparte, sin funding ni empalme.
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
- **Operativa en Binance:** perpetuos USDT-M, una sesión por cuenta (one-way netea el símbolo).
- **Seguridad:** no commitear `.env`, `bot/docs/raspberry-pi.md` ni claves, y no imprimirlas.
- **Frontend:** el que se sirve vive en `jesse/static/`. Sus módulos Nuxt distribuidos están en `_nuxt/`; las extensiones editables quedan fuera de esos bundles.

## Histórico

Los acuerdos r5–r11 y r9 (BTC individual, 2%/6%/3x, puertas por pieza), el handoff de Fase 2 ([`bot/docs/multi-asset-pivot-handoff.md`](bot/docs/multi-asset-pivot-handoff.md)) y los protocolos OOS de K1001 quedan como evidencia histórica, superada por r49. Sus veredictos no cambian. Ver `HISTORY_SUMMARY.md` y `RESEARCH_HUB/revisions/`.
