# Control técnico BTC 1m: equivalencia verificada
Fecha: 2026-10-18. Estado: PASS TÉCNICO; no es una hipótesis económica adicional.

[Dashboard del control](http://localhost:9200/#/backtest/9f2d190c-111d-4db4-af19-39ad2a7331d1).
[Referencia combinada](http://localhost:9200/#/backtest/2dbdb4dc-6b32-42d1-b637-15eefa6a4ecb).

Root ejecutó el control AngleCombinedBtcClockControl1m y la auditoría 3e58c073425c45a5ba8ef163147f54d7 terminó succeeded. Comunicó equivalencia estricta de 220 trades, 440 órdenes, 1.904 puntos de cartera y 45 métricas, con diferencia máxima de curva de 3,64e-12 y wallet 37.461,463374839186.

La política permanece LIMIT long/STOP short original, con decisiones y gestión 4h aunque BTC use trading route 1m y auxiliar 4h; PAXG/SPY mantienen 4h. Este resultado valida ese adaptador de reloj en este motor/configuración y ventana, no demuestra rentabilidad nueva ni equivalencia live.

La fuente del control fue releída intacta antes de clonar la futura variante reclaim. No se modifica para acomodar esa variante. El PASS permite plantear la atribución de la ejecución touch-and-reclaim, pero no certifica de antemano su implementación ni su resultado.

Protocolo previo: ANGLE_BTC_CLOCK_CONTROL_PROTOCOL_20261018.md. Ventana 2020-10-15→2025-12-31 exclusiva; 2026 reservado, sin cambios de framework ni scripts.
