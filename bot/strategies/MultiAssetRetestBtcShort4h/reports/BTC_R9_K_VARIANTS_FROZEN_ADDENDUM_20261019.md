# BTC R9 — cinco variantes Y902 congeladas antes de fuentes y backtests

Autorizadas por root antes de creación. Presupuesto fijo: cinco recetas × B/C = diez backtests nominales, cero extras y sin tuning posterior. 2026 cerrado incluso a inspección; ventana 2020-10-15 inclusiva a 2025-12-31 exclusiva. Misma muestra de desarrollo reutilizada, sin prueba OOS.

Base BTCNovelR902 (Y902). Cambia un mecanismo por receta, sin combinar variantes:
- K1001 / BtcY902ExploreR1001: precio solicitado SELL STOP = min(L_s,L_t), mínimo conjunto de las dos velas de señal. Distancia original d y TP2d permanecen congelados desde C_t. Cancelación original una barra, sin reintento.
- K1002 / BtcY902ExploreR1002: precio solicitado = L_t − (O_t−C_t)/2. Exige continuidad adicional de medio cuerpo rojo: mitad es una proporción geométrica previa, no parámetro buscado. Misma d, cancelación y guardas.
- K1003 / BtcY902ExploreR1003: únicamente primera decisión 4h con barra completa posterior al fill (open >= filltime): liquidar MARKET si C >= entry real. Se consume la oportunidad incluso si no liquida; no repite la prueba. No altera SL1R/TP2R/48h.
- K1004 / BtcY902ExploreR1004: interacción de Y902 con invalidación ya explorada en Y903 MARKET, no hipótesis nueva independiente: en cada barra completa postfill, liquidar MARKET si C > A congelado de señal y q_t > 0 y C > entry real. q=V*(2C−H−L)/(H−L), q=0 si rango cero. No altera protecciones.
- K1005 / BtcY902ExploreR1005: activar trailing persistente cuando una barra completa cierra C <= entry−d. Desde esa decisión y en cada barra completa posterior proponer stop=min(SLactual,H_anterior); actualizar sólo si price < nuevoSL < SLactual. H_anterior es barra cerrada conocida. Activación sigue activa aunque luego C > entry−d. TP2R y 48h conservados.

Gestión K1003/4/5: deadline primero, reloj idempotente por open de la barra cerrada, validar continuidad exacta 4h y fin <= self.time, exigir open >= opened_time real, reset en cada nuevo fill. No reutilizar extremos anteriores al fill como progreso del trade. K1005 H_anterior sólo se usa cuando ambas barras ya están cerradas: referencia estructural conocida, no supuesto fill intrabar. Stop válido estrictamente entre precio y stop actual.

Invariantes: evento y latch N503 antes de geometry, d original desde señal, SL1R y TP2R desde fill real; fórmula sizing/ledger/prioridad long y STOP original intactas. Guardas Y902 de precio finito, positivo, entry>2d y entry<price para smart order. No forzar tipo: clasificar suplemento por logs completos BTC_EXPLORE_FILL recipe y match tiempo/entry/qty, nunca por tipo STOP. Mantener requested_entry, signal_anchor, distance y target_distance en log original.

Contrato: capital compartido10000USDT, riesgo1%/8%, aislado5x, nocional4.4, reserva.001 sólo sizing, fee.00045 por lado; BTC/PAXG/SPY4h y tresfeeds1m; PAXG PortComparePaxgMarket4h, SPY B PortCompareSpySecond4h/C PortCompareSpyMarket4h; warm240/debugtrue/fastfalse/charttrue. Sin funding ni modificaciones ajenas.

Comparar cartera completa frente Y902 y referencias bajo nominal y +10bps overlay estático; DD >=−25%,>=30 suplementos,>=10 cambios de mecanismo identificados. Root audita finanzas MTM y metadata, regularidad y concentración heredadas se reportan. Ninguna promoción automática. Root protocolo BTC_R9_FROZEN_PROTOCOL_20261019.md tiene decisión conjunta. Dos backtests propios máximo, cuatro globales y cada par sólo con ticket root.
