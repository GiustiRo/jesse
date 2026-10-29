# Propuesta creativa — explotar el alivio de estrés de volatilidad
Fecha: 22 de octubre de 2026. Sólo propuesta documental; sin código nuevo, precios, cobertura, imports, jobs, drafts o motores. Hub r33 leído: R32 está cerrada sin candidata.

## Una pregunta
¿Esperar la disipación observable de un episodio de volatilidad permite explotar mejor el movimiento posterior que esperar simplemente un día desde el mismo episodio?

Hipótesis: el shock puede contener reajuste desordenado y costos de atravesarlo; después de caer la amplitud realizada, una dirección de precio ya observada podría persistir durante dos días. Rival: la volatilidad informa sobre dispersión, pero no sobre retorno; esperar puede llegar tarde o eliminar oportunidades sin mejorar ventaja. No se observan liquidaciones, agentes ni liquidez. No se promete que calma implique continuación o rentabilidad.

## Antecedente y diferencia
El antecedente exacto es R20SpyPostShockReentry, leído completo: vol10>2·vol60, descenso de vol5 a menos de mitad de su pico y recuperación de cinco sesiones; long con horizonte240h. Su cierre R20 sólo tuvo dos operaciones positivas, insuficientes: no motiva la propuesta por rendimiento ni transfiere evidencia a BTC.

La adaptación usa BTC continuo4h, sin sesiones SPY/NYSE, calendario o proxy externo; ambos sentidos según precio observado. Se leyó jesse://strategy, incluida adaptación de mercados tradicionales. Se propone una comparación de relojes posterior al mismo estrés y horizonte48h común; no copiar240h del antecedente como si tuviera fundamento para BTC.

Otros antecedentes leídos: V4_VOLUME_SHOCK_1H_PROPOSAL (shock de precio y volumen, contrarian inmediato1h/6h); protocolos C y cierre CD (CUSUM de sorpresas direccionales y absorción/escape); protocolo y cierre F (concentración RV/BV24h, follow/fade48h); V2 (ATR modifica protección/sizing, no momento de disipación); fuentes MultiAssetVolBudget4h y ResearchPaxgShockContinue/Reverse4h; Y (asociación rezagada volumen/amplitud aprendida); BtcResearchR12ReversionBase1m (excursión de precio madura y recuperación de media profundidad).
La diferencia material es esperar un estado de amplitud posterior al estrés frente a un reloj fijo. No es un gate añadido a R32, no recupera K ni afirma novedad universal. El parentesco con momentum y recuperación sigue explícito.

## Dos políticas, reglas propuestas
Decisiones UTC4h con64OHLC cerradas, consecutivas y válidas por infraestructura R32; señal calcula sobre últimos61cierres y60 retornos simples r=C_actual/C_previo−1. Volatilidades poblacionales ddof0: v60 de los60, v10 de los últimos10, v5 de los últimos5. Series exactamente constantes tienen volatilidad0; toda aritmética debe ser finita, sin epsilon ni imputación.

Estrés S=(v60>0 y v10>2·v60), estricto. Los60 incluyen los10: es contraste relativo contemporáneo, no baseline preevento independiente. Nuevo episodio sólo en transición false→true sin episodio vigente. Primera observación válida inicializa S sin abrir episodio. Se congela origen T0 y se inicia pico=max observado de v5 desde T0.

Episodio común dura hasta20barras4h inclusive después de T0. Mientras exista, actualizar pico con cada v5; ignorar nuevos shocks para armar otro. Persiste hasta su caducidad aunque una oportunidad ya se haya consumido. Así ambas políticas mantienen idéntico universo y reloj de episodios, independiente de cuenta/ocupación.

- NORMALIZACIÓN: primer cierre con edad entre1 y20barras y v5<0,5·pico actualizado, estricto. Consume su única oportunidad en ese instante.
- DÍA_FIJO: única oportunidad exactamente a edad6barras=24h desde T0, sin exigir normalización.

En el instante propio de cada oportunidad, dirección=sign(C_actual−C_cinco_barras_atrás): long si positiva, short si negativa; cero consume sin entrada. Ese retorno abarca20h y es conocido. No elegir dirección con recuperación futura ni con PnL. Los dos brazos usan idéntica fórmula direccional, pero pueden tener distinto signo por entrar en tiempos distintos: comparación de políticas completas, no efecto puro del reloj sobre fills emparejados.

Consumir oportunidad antes de comprobar posición, pendientes, guardas de cuenta, ATR o START/FINISH; si bloqueada se pierde. Sin cola, reintento, pirámides, reversión o entrada en mismo timestamp de salida. Datos inválidos o salto de reloj censuran episodio y reinicializan S sin inventar transición; _event procesa T monotónico una vez. A edad20 se permite normalización; después se cierra episodio. No ampliar plazo si no normaliza.

MARKET actual, stop2ATR14 simple actual congelado, sin TP/BE/trailing, salida a48h desde fill real en primera frontera4h elegible o terminal. Se reutiliza R11 y baseR32 mediante hojas con HOLD_HOURS48/TP_RNone, sin mutar padres. No normalizar usando el mínimo futuro de volatilidad ni salir cuando el pasado parezca más favorable.

## Contrato, decisión y presupuesto
Máximo dos motores nuevos, uno por política, sólo después de revisión, protocolo/fuentes/checks/manifiesto. Sin vecinos posteriores, búsqueda de otros ratios/ventanas, inversión de signos o selección de lado. Si falta frecuencia no se relajan reglas para fabricar N.

Cuenta alternativa de10.000USDT, cuota1% sobre capital BTC total; legacy_plan(.5wallet,.5margin), reserva.001 sólo sizing, lote.001, sin redistribuir cuota ociosa. BTC total eventual2%, global6%,3x aislado. Fee taker.00045 por lado, funding histórico ON dataset9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571; slippage modelado0. UTC[2020-10-15,2026-01-01), R11M1+fills y cortes por fase. Desarrollo reutilizado, no OOS ni cuenta conjunta.

Puertas r9 intactas: CAGR30/PF1,2/DD25 con objetivo20/M65/Q80/mediana calendario positiva/neto sin dos mejores meses positivo/N100 preliminar. La normalización sólo tiene preferencia relativa predeclarada si mejora neto y DD frente al día fijo sin reducir meses calendario positivos; además debe superar todas las puertas absolutas para ser candidata. Si no, cerrar esta comparación sin rescatarla por alguna celda/año. Ninguna salida se considera óptima por declararla antes.

Registrar episodios comunes, caducados, momentos de ambos disparadores, signos y bloqueos, además de contabilidad y regularidad. Esto permite distinguir actividad/costos de una supuesta mejora predictiva sin confundir oportunidades con trades contrafactuales.
No estrés de costos, riskgrid, nuevos datos,2026 nuevo,USDC,cartera,live/paper,Pi,install o configuración global. Este entregable no habilita ejecución por sí solo.
