# Revisión raíz de implementación de atribución

Fecha: 19 de octubre de 2026.

Root revisó los informes completos y los métodos modificados antes de liberar las colas. También leyó las 34 fuentes actuales por `read_strategy` y comparó los cuerpos de métodos contra los snapshots aislados originales. Las dos C0 fueron contrastadas directamente antes de su ejecución: igualdad exacta tras renombrar únicamente la clase. Los readbacks completos de las variantes confirmaron los cambios esperados:

| Control | Métodos afectados |
|---|---|
| Cq | _plan; agrega _fresh_quote |
| E1, E2, E3 | update_position |
| E4 | on_open_position, update_position; agrega _fresh_quote |
| M | _plan; agrega _fresh_quote |
| R y U | _plan; agrega _fresh_quote y before |

Se conservaron riesgo 1%, capital 10.000 USDT, comisión 0,00045 por lado, reserva de sizing 0,001, cap de nocional 4,4, margen isolated 5x y ledger/cancelación originales. Fuentes autocontenidas, sin imports entre estrategias. No se cambió framework, datos, funding ni calendario.

Se realizaron dos correcciones antes de ejecutar las configuraciones afectadas: M de SPY valida 0 < 2 ATR < frontera Donchian original antes de sustituir el precio por el cierre, como PAXG; el guard de PAXG busca la M1 exacta T−60s mediante searchsorted en vez de asumir que es la última fila. C0 permanece intacta. La paridad económica completa de C0 pasó antes de liberar las otras 16 de cada activo. Los informes separados incluyen comparadores, un fallo técnico por metadata de color de curva en PAXG y su reparación sin repetir el backtest.

R y U usan ASCII ATTR1|symbol|seed|closed_candle_open_time, SHA256, primeros 8 bytes big-endian, módulo 48 igual a cero. Seeds 101, 202, 303, 404, 505. before actualiza incluso ocupado y nunca encola. R conserva EMA, ADX, RSI y rango; U los elimina y conserva soporte de 100 velas, ATR y reglas de riesgo. SPY conserva su calendario UTC original: lunes a viernes 00–20 para features y barras abiertas 00–16 para entradas; PAXG no tiene ventana. El protocolo global quedó fijado antes de los resultados en ATTRIBUTION_STAGE_PROTOCOL_20261019.md.

## Semántica heredada de órdenes

Lectura del framework local: jesse/strategies/Strategy.py, _submit_buy_orders, líneas 674–683, comprueba primero is_price_near y llama buy_at_market; después distingue STOP por precio superior y LIMIT por inferior. jesse/helpers.py, is_price_near, líneas 1253–1260, aplica abs(1−order_price/price) <= 0.00015: 1,5 bps. El comentario histórico habla de redondeo, pero la implementación no lo realiza.

C0 y Cq son políticas de retest a frontera con esa conversión automática cercana. En SPY, las entradas ejecutadas son 24 LIMIT y 7 MARKET. No describirlas como 31 LIMIT puras. M cambia el precio planificado al cierre y dispara MARKET; la comparación incluye selección de fills, sizing, ocupación posterior y ejecución. Los pares primarios por fill real y el diagnóstico secundario por created_at exacto son intersecciones seleccionadas. No prueban causalidad pura ni cubren oportunidades que no llenaron. El snapshot no conserva frontera y cotización de decisión por separado para reconstruir las distancias exactas de esas siete conversiones.

## Límites de inferencia

Los 34 fulls son controles de atribución, no 34 ideas de alpha independientes. Las cinco seeds se presentan juntas; no se elige la ganadora. Comparten la misma historia y no son observaciones IID ni un p-valor.

Cambiar salidas altera las oportunidades disponibles. Igual número de operaciones no demuestra igualdad de entradas. La exposición entry-notional × tiempo / (capital inicial × ventana) es una aproximación a precio de entrada, no nocional MTM real. Los costes adicionales de 5 y 10 bps round trip sobre fills congelados son diagnósticos estáticos, sin repetir ejecución ni modelar fricción dinámica.

La auditoría MTM a cierre diario UTC usa precios reescalados contra fills ejecutados y concilia el cierre terminal. La curva Portfolio muestreada a las 00:01 no se interpreta como cierre diario UTC. No se abrió 2026.

## Verificación final de snapshots ejecutados

Root recuperó las 34 sesiones terminales y contrastó strategy_codes con las 34 fuentes revisadas: igualdad exacta en todas. También verificó en cada formulario fechas, una sola ruta de 4h, una data route M1, capital 10.000, comisión 0,00045, isolated 5x, warmup 240, fast_mode y debug_mode desactivados. No hay excepciones. Las 34 sesiones están cubiertas por el auditor MTM y todos los terminales concilian.

```json
[
  {
    "id": "37c6ae11-78b0-49c6-9b58-4c9190542841",
    "name": "AttrSpyU05",
    "url": "http://localhost:9200/#/backtest/37c6ae11-78b0-49c6-9b58-4c9190542841",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "4ac55781-679a-4d6d-a79a-320f162147b2",
    "name": "AttrSpyU04",
    "url": "http://localhost:9200/#/backtest/4ac55781-679a-4d6d-a79a-320f162147b2",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "998764bf-03f3-4643-b5cf-b569b6c6196b",
    "name": "AttrSpyU02",
    "url": "http://localhost:9200/#/backtest/998764bf-03f3-4643-b5cf-b569b6c6196b",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "63dd9d81-c7bf-417b-823f-728977051fd8",
    "name": "AttrSpyU03",
    "url": "http://localhost:9200/#/backtest/63dd9d81-c7bf-417b-823f-728977051fd8",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "da59b8b5-9d77-47fc-ac97-8aa5e28091a8",
    "name": "AttrSpyU01",
    "url": "http://localhost:9200/#/backtest/da59b8b5-9d77-47fc-ac97-8aa5e28091a8",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "ee7ee861-0137-4d13-a95d-837cb2a3e97e",
    "name": "AttrSpyR05",
    "url": "http://localhost:9200/#/backtest/ee7ee861-0137-4d13-a95d-837cb2a3e97e",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "a657dc36-13bd-440f-a423-917ab3caeb8c",
    "name": "AttrSpyR04",
    "url": "http://localhost:9200/#/backtest/a657dc36-13bd-440f-a423-917ab3caeb8c",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "205744ff-a7cd-46e8-893b-17e9ebf31fa9",
    "name": "AttrSpyR03",
    "url": "http://localhost:9200/#/backtest/205744ff-a7cd-46e8-893b-17e9ebf31fa9",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "83cdff20-9d2e-4d36-8c6c-2ba74a0c0a41",
    "name": "AttrSpyR01",
    "url": "http://localhost:9200/#/backtest/83cdff20-9d2e-4d36-8c6c-2ba74a0c0a41",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "c41e39a4-88b2-4423-87c0-f7863ccbe6d0",
    "name": "AttrSpyR02",
    "url": "http://localhost:9200/#/backtest/c41e39a4-88b2-4423-87c0-f7863ccbe6d0",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "64ff8816-6e45-46f1-ae81-35aecf65ab07",
    "name": "AttrSpyMarket",
    "url": "http://localhost:9200/#/backtest/64ff8816-6e45-46f1-ae81-35aecf65ab07",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "0c2efecc-aa4d-41c4-a9ac-832af72595a5",
    "name": "AttrSpyE4Stop72h",
    "url": "http://localhost:9200/#/backtest/0c2efecc-aa4d-41c4-a9ac-832af72595a5",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "069cb46d-09a5-4c8e-b164-f9c2d1061691",
    "name": "AttrSpyE2NoTrail",
    "url": "http://localhost:9200/#/backtest/069cb46d-09a5-4c8e-b164-f9c2d1061691",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "1fdaa89f-1d25-4832-a446-3c8fc5764cd2",
    "name": "AttrSpyE3InitialStop",
    "url": "http://localhost:9200/#/backtest/1fdaa89f-1d25-4832-a446-3c8fc5764cd2",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "58877a96-b0da-4bc4-956b-f3b4d2055639",
    "name": "AttrSpyCqFreshLimit",
    "url": "http://localhost:9200/#/backtest/58877a96-b0da-4bc4-956b-f3b4d2055639",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "a0e806e0-9c7e-49e2-a044-79a32763dce0",
    "name": "AttrSpyE1NoBE",
    "url": "http://localhost:9200/#/backtest/a0e806e0-9c7e-49e2-a044-79a32763dce0",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "798e6f62-979d-46a2-bf6d-b5983bcb3269",
    "name": "AttrSpyC0",
    "url": "http://localhost:9200/#/backtest/798e6f62-979d-46a2-bf6d-b5983bcb3269",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "f9af824c-8ac8-4fd5-9b2f-52adaebb112a",
    "name": "AttrPaxgUnconditionalSeed4044h",
    "url": "http://localhost:9200/#/backtest/f9af824c-8ac8-4fd5-9b2f-52adaebb112a",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "54613844-7e5d-4911-9342-071f65e0922b",
    "name": "AttrPaxgUnconditionalSeed5054h",
    "url": "http://localhost:9200/#/backtest/54613844-7e5d-4911-9342-071f65e0922b",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "e572d0cc-9a77-4998-b2ae-ec335daadf7d",
    "name": "AttrPaxgUnconditionalSeed3034h",
    "url": "http://localhost:9200/#/backtest/e572d0cc-9a77-4998-b2ae-ec335daadf7d",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "4d938a9b-653e-4226-9a1c-899b689e6b62",
    "name": "AttrPaxgUnconditionalSeed2024h",
    "url": "http://localhost:9200/#/backtest/4d938a9b-653e-4226-9a1c-899b689e6b62",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "6cc08024-0aa2-4cdf-a666-25f4351681bd",
    "name": "AttrPaxgUnconditionalSeed1014h",
    "url": "http://localhost:9200/#/backtest/6cc08024-0aa2-4cdf-a666-25f4351681bd",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "cfff7109-04c5-4420-8a90-fc19ceec6ef8",
    "name": "AttrPaxgRegimeSeed5054h",
    "url": "http://localhost:9200/#/backtest/cfff7109-04c5-4420-8a90-fc19ceec6ef8",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "0e7552b8-3491-4925-b230-f31c89b92796",
    "name": "AttrPaxgRegimeSeed3034h",
    "url": "http://localhost:9200/#/backtest/0e7552b8-3491-4925-b230-f31c89b92796",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "0edfce4f-695a-4213-8426-304b9af6d5a4",
    "name": "AttrPaxgRegimeSeed4044h",
    "url": "http://localhost:9200/#/backtest/0edfce4f-695a-4213-8426-304b9af6d5a4",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "fa518c27-144f-4af4-837c-b00c837110b1",
    "name": "AttrPaxgRegimeSeed1014h",
    "url": "http://localhost:9200/#/backtest/fa518c27-144f-4af4-837c-b00c837110b1",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "a8e6461e-2b14-4130-b9f6-0989a4483c8c",
    "name": "AttrPaxgRegimeSeed2024h",
    "url": "http://localhost:9200/#/backtest/a8e6461e-2b14-4130-b9f6-0989a4483c8c",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "8b43d9d2-0b64-4566-a97d-fe91a200f7ae",
    "name": "AttrPaxgMMarketSignal4h",
    "url": "http://localhost:9200/#/backtest/8b43d9d2-0b64-4566-a97d-fe91a200f7ae",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "573cca4f-01b7-4be4-9af3-e64d9a50c837",
    "name": "AttrPaxgE4InitialStop72h4h",
    "url": "http://localhost:9200/#/backtest/573cca4f-01b7-4be4-9af3-e64d9a50c837",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "4175efce-ac59-4c16-b23a-278fb6c9b8bc",
    "name": "AttrPaxgE2NoTrail4h",
    "url": "http://localhost:9200/#/backtest/4175efce-ac59-4c16-b23a-278fb6c9b8bc",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "831637c7-ade9-4be6-a15b-d568cd5d9242",
    "name": "AttrPaxgE3InitialStop4h",
    "url": "http://localhost:9200/#/backtest/831637c7-ade9-4be6-a15b-d568cd5d9242",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "4cc65389-4537-4e5a-a4f2-1b008214bb1b",
    "name": "AttrPaxgE1NoBe4h",
    "url": "http://localhost:9200/#/backtest/4cc65389-4537-4e5a-a4f2-1b008214bb1b",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "0fc6e1f7-66ea-4587-884a-ef616ecbfbc1",
    "name": "AttrPaxgCqFreshRetest4h",
    "url": "http://localhost:9200/#/backtest/0fc6e1f7-66ea-4587-884a-ef616ecbfbc1",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  },
  {
    "id": "69c90bb0-e2b4-4c6a-a562-edd95399e673",
    "name": "AttrPaxgC0Retest4h",
    "url": "http://localhost:9200/#/backtest/69c90bb0-e2b4-4c6a-a562-edd95399e673",
    "status": "finished",
    "sourceExact": true,
    "invariant": true
  }
]
```
