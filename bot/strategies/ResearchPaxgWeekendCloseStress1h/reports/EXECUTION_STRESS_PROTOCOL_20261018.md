# Control de ejecución de la hipótesis PAXG de fin de semana

Protocolo fijado antes de ejecutar la sesión cb5bdb97-ba8a-4997-a009-673d76b4a156. La receta primaria ya observada tiene 37 trades y +400,22 USDT netos; su concentración temporal sigue siendo una limitación. Este control no selecciona una nueva entrada ni sustituye la primaria.

Se copia la señal, el anclaje, el stop y el sizing de ResearchPaxgWeekendReturn1h. Se elimina únicamente el target LIMIT. Si la vela horaria cerrada después de la entrada tocó el objetivo original, se solicita liquidación MARKET en ese callback, al precio de cierre disponible. Si falta una cotización M1 fresca y consistente, la deuda de salida persiste. Se conserva la salida máxima de 24 horas y el stop de protección continuo.

El cambio tensiona la dependencia de un fill pasivo al precio del ancla. Puede salir a un precio mejor o peor: no es un modelo de slippage real ni una nueva fuente de alpha. Los resultados se compararán con la primaria sin elegir la política ganadora retrospectivamente. Verificar mismas fechas/direcciones de entrada, fills, fees, wallet, concentración y costes adicionales sobre los mismos fills.

Ventana 2020-10-15 a 2025-12-31 exclusiva; capital 10.000 USDT; riesgo 1%; fee 0.00045 por lado; 5x aislado; nocional máximo 4.4x; sin funding. Root ocupa un slot de backtest y el agente PAXG hasta dos, dentro del límite global de cuatro. Referencia, BTC y 2026 intactos.

El protocolo de robustez común fue guardado por el agente PAXG con el nombre PAXG_WEEKEND_ROBUSTNESS_PROTOCOL_20261018.md antes de estas pruebas. Root no lo sobrescribe: este archivo documenta su control específico, también antes del run.