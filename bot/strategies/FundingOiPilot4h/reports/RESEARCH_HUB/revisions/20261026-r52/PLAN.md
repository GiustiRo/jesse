# r52: ampliar el universo, apostar a diferencias entre monedas y a la estructura del flujo

## Contexto
- r50 y r51 agotaron la familia de tendencia sobre 7 activos:
  - P1 sigue siendo la candidata: 2018-09+ con CAGR 36,9% y Sharpe 1,60; 2021–25 con 24,3% y 1,42.
  - No hay cortos rentables por sí solos ni ventaja en bonos.
  - N = 108.
- El usuario pidió ideas nuevas con fundamento y tecnología, en 4h/1h, que no sean «más tendencia».
- La investigación (`reports/Nuevas fuentes de ventaja r52.md`) concluye que la ventaja no va a salir de un modelo más sofisticado sobre los mismos 7 activos, sino de **cambiar la dimensión de la apuesta**:
  - diferencias *entre* monedas, en un universo amplio y neutral al mercado;
  - estructura de quién opera y cuándo (el reloj del flujo de órdenes).
- Las dos líneas necesitan una pieza de infraestructura que hoy no existe: **un universo de 50 perpetuos cripto de Binance activos, con historia 2020–2025**.
- Sin deslistados, por decisión del usuario. Se opera solo con perpetuos.
- Esto deja un sesgo de supervivencia declarado: las 50 monedas que siguen activas hoy son las «ganadoras» del período.
  - Para que no infle el ranking, cada semana una moneda entra solo con su volumen de ese momento y con ≥ 90 días listada.
  - Se reporta aparte el resultado de las 20 monedas más antiguas.
- Decisiones del usuario: los desbloqueos de tokens quedan **descartados**. Siguen afuera LLM/noticias, modelos fundacionales, CNN sobre gráficos, liquidaciones, paper y live.

## Las tres líneas de r52
1. **Ranking transversal semanal, neutral al mercado, sobre 50 perpetuos** (estilo CTREND, JFQA 2025).
   - Combina con ML (elastic net o gradient boosting) indicadores técnicos de precio y volumen de muchos horizontes para ordenar las monedas de mejor a peor.
   - Va largo las mejores y corto las peores, o largo las mejores cubierto con BTC/ETH.
   - Gana por diferencias entre monedas, suba o baje el mercado. Ataca la causa de 6 de los 8 trimestres negativos de P1 y trae el lado corto como cobertura.
   - Evidencia: Sharpe 1,94 bruto y neto significativo en el top-100 (spot 2015–22).
   - Contraevidencia: en 10 perpetuos a 8 horas no hay ventaja.
   - Por eso se va a universo amplio y horizonte semanal.
2. **Reloj del flujo de órdenes («cuarto de hora»)**, arXiv 2607.09426.
   - El desbalance comprador/vendedor agresor en los primeros minutos de :00/:15/:30/:45 predice el retorno de las 4–12 horas siguientes en perpetuos de Binance. Viene de algoritmos periódicos, no de la tendencia.
   - Se construye gratis con el volumen agresor de las velas de 1m.
   - Es un solo preprint, así que se trata como hipótesis con presupuesto chico.
3. **Permiso de régimen con *jump model* sobre BTC** para las mangas largas cripto de P1 (Shu, Yu y Mulvey 2024).
   - Recorta el sangrado de R1/C6 en cripto lateral o bajista.
   - La penalización de salto se fija de la literatura, sin optimizarla.

## Fases

**F0. Infraestructura del universo (no suma a N)**
- **Inventario:** los 50 perpetuos USDT-M cripto activos hoy con más volumen y listados antes de 2023, según `exchangeInfo`.
  - Se excluyen stablecoins, índices y TradFi.
- **Descargas** de `data.binance.vision`, en ZIP mensual con checksum, hasta el 2025-12-31:
  - velas 1h (con volumen agresor) y funding de todos;
  - velas 1m solo para BTC, ETH y la canasta de alts de la línea 2.
  - Se guardan comprimidas en `bot/research_scripts/data/r52/`, fuera de git y fuera de la base de Jesse, por volumen. Estimo ~2–3 GB; hay 224 GB libres.
- **Elegibilidad semanal dentro de las 50:**
  - listado hace ≥ 90 días;
  - volumen mínimo en dólares (mediana de 30 días) de ese momento.
- **Simulador transversal** `r52_xs.py`:
  - rebalanceo semanal, fee taker 0,045% más 2 bp, funding por símbolo, neteo por símbolo;
  - reutiliza métricas y DSR de `r50_harness.py`, `r50_f1b.dsr` y `r50_f2.r9`.
- **Cortes de tiempo**, fijados antes de cualquier resultado:
  - desarrollo 2020-07 → 2023-12, para entrenar y elegir;
  - validación 2024, una sola mirada;
  - **2025 sellado**, una mirada final;
  - 2026 sigue reservado.
- **Herramientas:** scikit-learn 1.8 (elastic net, HistGradientBoosting), ya instalado en el contenedor. **No se instala nada.**
- **Protocolo `PROTOCOL_R52.md`**: features, modelos, compuertas y presupuesto, commiteado antes de cualquier resultado. Hub y `DOCS.md` actualizados.

**F1. Ranking transversal (4 ensayos)**
- **X0, referencia:** ranking por momentum de varios horizontes (1, 4 y 12 semanas). La ML tiene que superarlo.
- **X1, CTREND:** elastic net transversal sobre los indicadores del paper (medias de precio y de volumen de varios horizontes, momentum, volatilidad, volumen agresor).
  - Entrenamiento expansivo walk-forward con purga y embargo de 1 semana.
  - Largo el quintil superior y corto el inferior, por igual riesgo.
- **X2:** lo mismo que X1, con gradient boosting regularizado (HistGradientBoosting).
- **X3:** el mejor de X1/X2 en versión largo el quintil superior, cubierto con BTC/ETH por beta. La pata corta de momentum en cripto rinde ~0.
- **Compuertas**, en desarrollo salvo donde se indica:
  - Sharpe neto ≥ 0,5;
  - supera a X0 por ≥ 0,2 de Sharpe neto;
  - con costos ×2, Sharpe > 0;
  - ρ con P1 ≤ 0,3;
  - validación 2024: Sharpe > 0.

**F2. Reloj del flujo (3 ensayos)**
- **Q1:** réplica estadística en BTC/ETH del poder predictivo a 4–12h, con IC y regresión walk-forward.
- **Q2:** regla operable en 4h, largo/corto en BTC y ETH, neta de costos y funding.
- **Q3:** Q2 congelada sobre una canasta de 20 alts nunca usadas.
- **Compuertas:**
  - Q1 con t ≥ 2 fuera de muestra;
  - Q2 con Sharpe neto ≥ 0,5 y ρ con P1 ≤ 0,3;
  - Q3 con la mayoría de las alts > 0 y la canasta con t ≥ 1,28.

**F3. Permiso de régimen (1 ensayo)**
- **J1:** *jump model* de 2 estados sobre rasgos diarios de BTC (retorno, volatilidad, desvío negativo), con penalización fija tomada del paper y un día de demora.
- En el estado de riesgo, R1/BTC, R1/ETH y C6 van a la mitad de tamaño.
- Compuerta: la regla de inclusión de r51 (ΔSharpe en 2018-09+ ≥ +0,05, o +1 trimestre positivo sin bajar el Sharpe, y 2021–25 sin bajar más de 0,05).

**F4. Cartera y mirada sellada (≤ 1 ensayo de cartera)**
- Construcción de F2 de r50 con P1 más las mangas que pasen, con la regla de inclusión de r51.
- Una sola mirada a 2025 de lo que haya entrado. Puertas: Sharpe > 0 y ningún derrumbe (Sharpe < −0,5 o DD < −30%).
- Si falla, la manga se retira, sin ajustes.
- Cierre con informe, congelamiento y propuesta para r53: meta-labeling con >1.000 eventos, la mirada a 2026 y SOL/XRP/BNB.

## Presupuesto y proceso
- **N:** **sin techo**, por decisión del usuario, para explorar libremente.
  - Igual se registra cada ensayo, para que el DSR sea honesto: parte de 108.
  - Las variantes nuevas que surjan en el camino se agregan al protocolo con fecha antes de correrlas.
- **Ejecución autónoma:** el usuario deja a cargo la investigación completa.
  - Subagentes en paralelo para descargas, construcción y ensayos independientes.
  - Reintentos ante interrupciones.
  - No se frena hasta cerrar F4.
  - Si el trabajo crece, se abren rondas siguientes (r53, r54…) en sesiones nuevas, con un handoff escrito en el Hub y en las notas compartidas, para no saturar el contexto.
  - Candidatas ya identificadas para esas rondas: meta-labeling sobre el universo de 50, variantes que surjan de F1–F3, la mirada a 2026 y SOL/XRP/BNB.
- No se usan corridas Jesse en r52: las mangas transversales no se pueden confirmar en Jesse con una sesión por manga. Queda declarado.
- Un informe corto por fase con `save_strategy_report`, `TRIAL_REGISTRY.json` al día, y commit y push a `origin exploration/gpt-6.1-sol` al cerrar cada fase.
- **Autorizaciones que pide este plan:**
  - descargas desde `data.binance.vision` (~2–3 GB);
  - scripts `r52_*.py`;
  - push.
- Sin instalaciones, sin cambios en la configuración de Jesse y sin reinicios.

## Verificación
- **F0, datos:**
  - checksums de cada ZIP;
  - conteo de huecos por símbolo;
  - las velas 1h de BTC/ETH desde vision tienen que coincidir con las de la base de Jesse (diferencia < 1e-6);
  - el funding de BTC/ETH desde vision tiene que coincidir con los datasets `0ab14bc2…` y `22bd891c…`.
- **F0, simulador:** test sintético en el que un ranking perfecto da el retorno esperado y uno aleatorio da ~0 menos costos.
- **F1–F3:** tablas por ensayo con Sharpe neto en desarrollo, validación y costos ×2, ρ con P1, rotación y pesos por moneda (para detectar concentración).
- **F4:** tablero de cartera contra P1 en 2018-09+ y 2021–25, DSR con el N final y la mirada sellada a 2025.
