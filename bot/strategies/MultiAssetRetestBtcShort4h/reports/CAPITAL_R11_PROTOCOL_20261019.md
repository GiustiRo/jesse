# Gestión de capital R11 — protocolo previo a resultados
Fecha: 2026-10-19. Pedido: comparar K1001, ganadora provisional, con N204, referencia congelada, bajo distinto apalancamiento y presupuesto de capital.

## Hipótesis
Una menor utilización de margen puede conservar una parte importante del retorno con mejor drawdown o duración de recuperación; incrementar el presupuesto de riesgo puede dejar de aportar tamaño por los límites de exposición y margen. Se buscan compromisos estables, no el mayor beneficio aislado.

## Etapa A autorizada y definida
16 corridas: K1001/N204 × carteras B/C originales × apalancamiento isolated 1/2/3/4x. Comparadores 5x existentes exactos: K1001B 10be7d01-51f7-480c-9b6c-8b653da82c5a; K1001C 08d01428-7abe-410a-bf7d-f8c8d46aa35c; N204B bc5aaba6-2746-4e90-b0de-7b7955b66142; N204C 6dead093-4663-4da9-ac62-c2ad9f9bb794.
Fuentes actuales comprobadas iguales byte por byte a los snapshots de las cuatro anclas, las tres rutas por cartera.
Sólo cambia form.config.exchange.futures_leverage por sesión. No editar configuración global ni fuentes. Riesgo objetivo 1% por operación/8% agregado, cap nominal 4.4, pesos inversos ATR, buffer margin 0.90, reservas pendientes y SLIPPAGE_RESERVE .001 exactos. El cap 4.4 se conserva deliberadamente para aislar el efecto del margen del motor; no se lo presenta como 4.4x alcanzable a 1x. El margen disponible y los pesos pueden alterar las cantidades de forma no proporcional.
Misma cuenta compartida 10000 USDT, Binance Perpetual Futures, BTC/PAXG/SPY 4h con feeds 1m, warmup240, fee .00045 por lado, fast_mode false, debug true, benchmark false. B usa SPY Second; C SPY Market. Orden de rutas BTC/PAXG/SPY igual. SPY conserva proxy SPX CFD y calendario previo; no certifica equivalencia operativa con un futuro nativo.
Ventana 2020-10-15 inclusiva a 2025-12-31 exclusiva. Histórico de desarrollo reutilizado; 2026 cerrado incluso inspección. Máximo dos backtests simultáneos y un análisis. Sin live/paper, instalaciones, reinicios ni purgas.

## Etapa B — semántica pendiente
Se preguntó al usuario si 5%/15% significa riesgo al stop o margen. No se ejecuta esta etapa hasta resolverlo. No asumir que 1% actual es margen. No escribir research_scripts.
Si riesgo: propuesta acotada 0.5/1/2/3/5% por trade, con caps agregados explícitos; incluir 5%/15% como escenario experimental solicitado, sin recomendación live. Si margen: límites por trade y agregado sobre nominal/leverage, contabilizando posiciones y pendientes; conservar protección técnica y documentar si el riesgo original sigue limitando. Congelar matriz exacta antes de resultados. No cruzar automáticamente todos los parámetros ni escoger el leverage vencedor de A para esconder selección.

## Evaluación y entregables
Tabla por estrategia, B/C y leverage: neto, retorno, CAGR motor, drawdown, Calmar, Sharpe, PF, trades, fees y underwater. Curvas de equity y drawdown, retornos calendario mensuales y anuales a partir de equity almacenada, incluyendo períodos sin operaciones y marcando períodos extremos parciales. Informar resolución de la curva, reconciliación terminal y límites de estas métricas. Auditoría financiera de trades y diferencias de señales/fills respecto al ancla para distinguir tamaños de cambios de operativa. Exposición sólo con definición y denominador claros; no llamar riesgo al stop a una mera exposición nominal.
Primero frontera retorno/DD: dominancia descriptiva si retorno >= y magnitud DD <= con al menos una desigualdad estricta. Desempate interpretativo por Calmar, recuperación y estabilidad temporal. DD -25% es umbral de investigación existente, no garantía. Comparar resultados entre B/C sin contarlas como muestras independientes. No promover por un ranking IS.
La reserva de slippage modifica sizing, no fills; funding ausente. Más adelante, una política elegida y congelada requerirá costes/fills estresados y validación nueva; no consumir 2026 para optimizar capital.

## Estado
Protocolo guardado antes de iniciar A. B pendiente de aclaración. No hay resultados nuevos en este documento.
