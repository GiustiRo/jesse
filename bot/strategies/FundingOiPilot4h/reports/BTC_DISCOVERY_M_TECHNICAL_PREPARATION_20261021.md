# Tanda M: preparación técnica completada, economía no iniciada

Protocolo BTC_DISCOVERY_M_PROTOCOL_20261021.md guardado antes de economía. No se crearon borradores ni se ejecutaron backtests económicos o técnicos. No hay resultados financieros ni dashboard de sesión de esta tanda todavía.

## Fuentes nuevas y dependencias

- BtcResearchR13GeometryBase1m: fuente completa SHA256 3968e9a2733fbe9e4a22b32ba71d023defcefa79eae65e992833f1810fb82b97.
- BtcResearchR13GeometryConditional1m: wrapper MODE=COND, leído de vuelta exactamente.
- BtcResearchR13GeometryGlobal1m: wrapper MODE=GLOBAL, leído de vuelta exactamente.

Las tres fuentes nuevas se leyeron de vuelta por MCP y coinciden con lo enviado. Las dependencias existentes se volvieron a leer y siguen idénticas: BtcResearchR12ArBase1m 1b4d448f0d054e48cbb18a3f3ac4a2bd2d12df40469fa6ad2047968cf3110343, BtcResearchR11Base1m be1a1d6379b03d81eb6585a334dccae76c900c794193f55bd1922bbd5d3d6d87, BtcResearchR10Base4h 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9. Ninguna fue modificada. La base AR sólo aporta observador, sizing, stop sinTP y salida24h; su predictor no se llama.

## Check previo

Análisis 800fc7c5eeb54250b472a89e7f0ec017: succeeded, 125 aserciones. Un intento sintético, cero fallos y cero reintentos. Leyó sólo código suministrado en el propio análisis; no datos de mercado ni archivos de estrategia. El análisis ya terminó y liberó el límite propio de ejecución.

El oráculo independiente por bucle revisó los360 orígenes1..360 y targets7..366 conocidos enT. El origen actual366 no aporta etiqueta de entrenamiento. Se verificaron medias porbin y global, gate común de almenos30 orígenes del bin actual, exclusión de cambios/TRcero, igualdadE=0,5, respuestas follow/fade/cash y transformación de dirección. Se comprobó invariancia a historia anterior a la ventana, exclusión de futuras velas por closed_window y rechazo de huecos, sizing fee-aware2% heredado, ausencia deTP y hold24h heredados. Los fills follow/fade se cuentan después de on_open del padre, no como simples forecasts bloqueados.

El modelo se recalcula de forma stateless con367OHLC; no necesita reconstruir un estado de entrenamiento después de reiniciar. Las etiquetas que vencen enT ya observado son admisibles desdeT. GLOBAL conserva el mismo gate de validez del bin actual, así que el contraste no cambia su calendario sólo por mínimo de evidencia. Labels y ventanas se solapan: las125 aserciones no aportan evidencia de alpha ni independencia estadística.

## Antes de economía

Root debe revisar protocolo/fuente, crear formularios de las dos wrappers con ruta1m/data4h, warmup4004h,ventana[2020-10-15,2026-01-01),10k,3xaislado,fee.00045 y fundinghistóricoBTC snapshot fijo. Guardar manifiesto con esos formularios y readbacks antes de ejecutar. Presupuesto exactamente dos económicas y hasta dos reemplazos únicamente técnicos, sin vecinos posteriores. No se creó un manifiesto con sesiones o resultados pendientes inventados.

Se preservan gatesr9 y2%/6%/3x; slippage0 y fundingproxy declarados, sin estrés o2026nuevo. Preparar esto no demuestra rentabilidad, operabilidad ni autoriza live/paper/Pi. Fuente, check y código completo de análisis en BTC_DISCOVERY_M_TECHNICAL_CHECK_20261021.json.
