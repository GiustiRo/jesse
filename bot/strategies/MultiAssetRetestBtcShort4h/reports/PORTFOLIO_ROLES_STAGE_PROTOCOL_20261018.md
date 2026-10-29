# Cartera por funciones — protocolo de desarrollo previo a resultados

Fecha local: 18/10/2026 (America/Montevideo). El usuario AUTORIZA investigar BTC, PAXG y SPY como cartera. Posteriormente autoriza estudiar investigación open source/ML y reabrir evaluación de funding en paralelo. No se convierten esos estudios en integración automática ni en scripts/datasets nuevos.

## Objetivo y referencia

Referencia fuente y sesión inmutables: MultiAssetRetestBtcShort4h, [dashboard](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb). Se conservan 65–70% de meses activos positivos,80% de trimestres,DD no peor de−25%,rentabilidad útil resistente a costes. Reportar también todos los períodos y completos, actividad/exposición y pérdidas grandes. No usar2026.

## Diseño predeclarado

Ventana 2020-10-15 →2025-12-31 exclusiva, tres rutas4h BTC/PAXG/SPY, misma cuenta10.000USDT,fee.00045porladoTODASórdenes,5xaislado,risk3%/8%agregado/gross4.4 y shareATR original. Nuevas fuentes sólo velas existentes. Las tres configuraciones usan auxiliares M1 de los tres símbolos para validar cotizaciones conocidas, sin cambiar la ventana ni fabricar datos.

Configuraciones económicas fijas:
- 00: referencia existente.
- 10: sólo reemplazar política PAXG por divergencia contextual, BTC/SPY originales.
- 01: sólo reemplazar entrada SPY por participación sostenida con cooldown, BTC/PAXG originales.
- 11: ambos cambios juntos, BTC original. Es la comparación primaria de complementariedad.

Máximo tres full económicos nuevos, sin barrer horizontes, stops, riesgo, horarios o cooldown tras resultados.10/01 son atribución del diseño, no menú de meses o trades que combinar retrospectivamente. Se registra todo lo visto como desarrollo adaptativo. No promover una ablation por un único número ni abrir2026 al ver algo atractivo. Si sólo una pata aporta, formular explícitamente el siguiente protocolo antes de nuevas pruebas, conservando la selección acumulada.

## SPY: control económico de participación

PortfolioSpyPersistent4h: sustituye sólo elegibilidad/ejecución SPY por MARKET estando flat,en ventana original y quoteM1 exactaT−60s; espera168h desde closed_trade.closed_at real antes de reentrar. Inicio sin espera artificial. Mismos2ATR iniciales,trailing4.2ATR,BE heredado y sizing/riesgo/caps originales. Sin rebalanceo mensual ni stop porcentual nuevo. No es nueva alpha ni cobertura anticíclica: pregunta si el forecast de breakout justifica su baja participación. La exposición efectiva y turnover cambiarán y deben medirse.

## PAXG: divergencia contextual

AnglePortfolioPaxgDivergence4h: reemplaza breakout por long/cash si retorno7dBTC<0,SPY<0,PAXG>0 en timestamps idénticos. Decisión hábil16UTC sobre extremos12UTC y12UTC−7d. Antes se guardan quotesM1 frescas a12 en memoria8d, luego se valida paridad de cierres4h ya terminados. Requiere SPY/PAXG M1 frescos también a16. Startup cash incluido hasta disponer de7d; sin imputar holidays/gaps. Sólo transiciónfalse→true, consumida inclusoopen/pending/sinriesgo, sin cola. Falso válido produce deuda de salida con quotepropia; ausencia de datos no cambia estado. Stop2ATR fijo sinTP/trailing, mismos3%/8% y caps originales. Es una nueva política de entrada/salida, no prueba aislada de un filtro; comparte premisa conRiskOff previo y no demuestra flujosmacro ni hedge.

## Implementación y comparación

Fuentes específicas revisadas por root y otro agente, todos los cuerpos no modificados contrastados conbaseline. La fuente11 se compone por despachos de símbolo, sin reescribir ni ajustar la idea de cada celda. CapturasM1 y señales son causales; helpersde horasSPY y filtering conservados. Stops activos durante cierres del mercado; proxy CFD/BID y PAXGSpot no acreditan paridad de ejecución nativa24/7. No tocar framework/live/fondos/servidor.

AuditorV4: órdenes/fees/wallet/MTM UTC reconciliados, contribucionesporactivo/dirección, rescates/deterioros,y años/calendario completo. Compararholding/exposición/turnover y concentración, no sólo CAGR.11−10−01+00 es interacción descriptiva de trayectorias endógenas, no suma de cuentas ejecutables ni causalidadformal.

Primero10/01, después11 ya congelada. Si falla la implementación, corregir causa técnica y registrar; no tocar alpha para rescatar resultados. Una mejora prometedora necesita costes y perturbaciones antes de lockbox; el fee original participa en señales/BE, por lo que cualquier stress futuro debe separar decisiones fijas de coste efectivo y comprobar paridadbase.

## Línea explorativa independiente

Observador multiescala causalBTC, protocolo en strategies/OrchManageTurtleDaily/reports/ANGLE_CAUSAL_MULTISCALE_OBSERVER_PROTOCOL_20261018.md: estructura1D/4h con pivots2+2 confirmados,probabilidades de3resultados24h,learn sóloepisodiosmaduros,baselineincondicional,unknown/ambigüedad/cobertura ydependencia explícitos. Sin operaciones iniciales ni edge prometido. Se revisan bibliotecas y PineScriptML abiertos por calidad de etiquetas/asof/licencia,repainting y utilidad frentecontrolsimple. Funding queda en viabilidaddocumental multiplaça, no se descarga ni integra todavía.
