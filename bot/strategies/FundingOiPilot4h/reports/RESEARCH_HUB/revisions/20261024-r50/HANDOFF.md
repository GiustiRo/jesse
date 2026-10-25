# r50: handoff para la sesión que ejecuta

Ejecutá la investigación **r50** según el plan aprobado por el usuario, [`PLAN.md`](PLAN.md), en esta misma carpeta. Ese archivo es la especificación.

## Antes de empezar
- Leer:
  - `DOCS.md`, `AGENTS.md` y `bot/AGENTS.md`;
  - `RESEARCH_HUB/revisions/20261024-r49/` (PLAN, HISTORY_SUMMARY, PHASE2B_PROTOCOL);
  - `R49_PHASE0/2/2B/2C_RESULTS_*.md` y `R49_CLOSE_20261024.md` en `bot/strategies/FundingOiPilot4h/reports/`.
- Verificar que estén las herramientas del MCP `jesse-local`. Si faltan, parar y avisar.

## Orden de trabajo

**F0**
1. **Descargas en background**, en este orden:
   1. BTC/ETH spot de Binance desde 2017-08, con la importación nativa de Jesse (`Binance Spot`), en símbolos separados de los perpetuos. Sin empalmar series.
   2. Gas natural.
   3. Bono largo de EE.UU.
   4. Plata, Nasdaq y cobre. Usar Dukascopy con `dukascopy_download_v3.py --base-url http://...`, igual que en r49.
   - Usar un mecanismo que despierte la sesión al terminar cada descarga: `run_in_background` o un monitor con condición de salida.
   - Si un proxy no existe en Dukascopy, reportarlo y proponer una alternativa antes de sustituirlo.
2. **Arnés vectorizado diario** en `bot/research_scripts/`, en paralelo con las descargas.
   - Tiene que reproducir las sesiones Jesse de r49 con un error de equity menor a 0,5%:
     - BTC `b4792187-8847-450d-9f52-320edb4a61dd`
     - PAXG `02a484b6-a237-4ffb-a283-7db32354a61e`
     - SPY `21063c59-f0f5-4a07-a66a-040f75e3f475`
   - Entregar la tabla de reproducción.
3. Publicar r50 en el Hub (`revision.json` en esta carpeta, después el índice) y actualizar `DOCS.md`.

**F1**
- Antes de mirar cualquier resultado: escribir y commitear el protocolo de screening de M1–M4, con hipótesis, valores por defecto y puertas de falsación según el plan.
- Recién después, correr el screening.

**F2–F5**
- Según el plan.
- Reportar al usuario al cerrar cada fase. No avanzar a la F2 sin reportar la F1.

## Reglas
- **2026 queda reservado por definición:** ningún dato posterior al 2025-12-31 se mira ni se usa hasta que el usuario lo apruebe.
- **Activos de validación:** plata, Nasdaq y cobre no se usan para diseñar ni calibrar. Solo entran en la F3, con los motores ya congelados.
- **Jesse:** ≤10 corridas en la F4, máximo 2 simultáneas.
- **Registro:** cada variante va a `TRIAL_REGISTRY.json`, con N actualizado (parte de 57).
- **Informes:** uno corto por fase, con `save_strategy_report` y URLs de dashboard.
- **Git:** commit y push a `origin exploration/gpt-6.1-sol` al cerrar cada fase.
- **Autorizado por el usuario para r50:**
  - scripts en `research_scripts`;
  - descargas de los 10 activos del plan;
  - importación de BTC/ETH spot;
  - push de la rama.
- **Prohibido sin autorización específica:**
  - live/paper y la Pi;
  - configuración global;
  - reinicios del servidor;
  - instalación de paquetes.
