# BTC R9 — cierre del agente explorador de Y902

Diez backtests nominales terminados y auditados por root, cinco recetas previamente congeladas, cero corridas adicionales. 2026 cerrado incluso a inspección. Muestra reutilizada 2020-10-15 inclusiva→2025-12-31 exclusiva: no OOS ni prueba de ausencia de sobreajuste. Las pruebas de fee y TP de Y902 pertenecen al bloque root; no validan automáticamente K1001 ni K1005.

## Resultados de cartera compartida

|Receta|Neto B/C USDT|Δ Y902 B/C|DD B/C %|Suplementos|
|---|---:|---:|---:|---:|
|K1001|[13619.21](http://localhost:9200/#/backtest/10be7d01-51f7-480c-9b6c-8b653da82c5a) / [13854.33](http://localhost:9200/#/backtest/08d01428-7abe-410a-bf7d-f8c8d46aa35c)|172.98 / 173.98|-8.8231 / -8.7768|45 / 45|
|K1002|[10640.89](http://localhost:9200/#/backtest/728f638d-0f10-4b6c-9b6f-4f5533c89df9) / [10831.16](http://localhost:9200/#/backtest/36c79fa4-2e96-482d-80d3-7692b85a261d)|-2805.35 / -2849.19|-9.1501 / -9.1250|20 / 20|
|K1003|[10934.01](http://localhost:9200/#/backtest/82105bee-e22b-4ae2-a311-b369453b03e9) / [11124.49](http://localhost:9200/#/backtest/00c0f043-ea8a-4d28-88be-7553442909e1)|-2512.23 / -2555.86|-9.0837 / -9.1062|47 / 47|
|K1004|[12407.21](http://localhost:9200/#/backtest/a523b5c5-8a91-4dd0-b596-550405b10fe5) / [12654.85](http://localhost:9200/#/backtest/e32e4b65-850b-475f-9179-be61b25131d6)|-1039.02 / -1025.50|-8.8275 / -8.8031|47 / 47|
|K1005|[13844.91](http://localhost:9200/#/backtest/3f979db7-44e2-44c6-9b82-7c3362084f62) / [14103.94](http://localhost:9200/#/backtest/8d198fc1-eae8-4a67-8258-e6fabe58756a)|398.67 / 423.59|-9.7072 / -9.6427|46 / 46|

Fuente monetaria: BTC_R9_RESULTS_MATRIX_20261019.md, auditorías financieras root. Fee.00045 por lado, capital10000USDT compartido y riesgo1%/8%, aislado5x. Reserva.001es sizing, no fillfriction. Misma PAXG y SPYB/C. B y C son configuraciones relacionadas, no muestras independientes.

## Qué aporta cada mecanismo

K1001 sustituye mínimo de t por min(L_s,L_t). Mejora neto +172.98/+173.98USDT frente Y902 y DD de−9.6941/−9.6301Y902 a−8.8231/−8.7768. Sube a43/63 y44/63 meses nominales positivos,42/63 y43/63 bajo overlay+5bpsRT. Bajo+10 estático superaY902 +177.54/+177.96. Root identifica únicamente cinco cambios de entrada frenteY902 y45suplementos44STOP+1MARKET. La ganancia es prometedora, pero pocos cambios no sostienen una afirmación fuerte de generalización. FrenteN204, omitir mejor mes incremental de63meses deja+155.35/+216.43USDT; limitando a61mesescompletos deja−41.76/+21.57. Hay sensibilidad al universo calendario incluido; no ocultarla.

K1002 pide continuidad extra de medio cuerpo rojo bajoL_t. Sólo20suplementos frente46Y902, por debajo del mínimo30; pierde aproximadamente2805/2849USDT frenteY902. Un umbral más distante puede suprimir oportunidades valiosas. No se ajusta el coeficiente tras observarlo.

K1003 cierra si primera barra completa postfill termina C>=entry.47suplementos,42primeras comprobaciones y23salidas de gestión;200comprobaciones completas. Neto cae aproximadamente2512/2556USDT. Una reacción inicialmente adversa no demuestra invalidación suficiente para este corte temprano.

K1004 transporta invalidaciónY903 a ejecuciónY902: C>A_frozen,q>0,C>entry.47suplementos,11salidas de gestión y302comprobaciones completas. Neto cae aproximadamente1039/1026USDT. Es una interacción con el cambio de entrada, no una hipótesis independiente recién descubierta; tampoco mejoró neto aquí.

K1005 activa trailing persistente tras cierre favorable1R y usa máximo de barra previa conocida para estrechar SL cuando queda válidamente sobreprecio y bajoSLactual. Conserva46suplementos45STOP+1MARKET,337comprobaciones completas y24actualizaciones de stop. Root identifica sólo cinco salidas emparejadas modificadas;24actualizaciones NO son24trades distintos. Mejora neto +398.67/+423.59 frenteY902 y +788.29/+864.50 frenteN204. Bajo overlay+10 conserva +374.02/+394.90 frenteY902. DD−9.7072/−9.6427 es ligeramente peor queY902: no mejora todas las dimensiones. Meses positivos nominales42/63,43/63; con+5estático41/63,42/63. Trimestres17/21ambas.

K1005 reduce concentración frenteN204: al omitir mejor mes incremental de63meses queda +376.79/+461.79USDT, y sobre61mesescompletos +184.35/+273.70. Cuatro de cinco bloques2021–25mejoran, pero2025parcial y sobre61mesescompletos son3/5. Son omisiones aritméticas sobre recorridos fijos, no replaydelcapital ni validación temporal independiente.

## Decisión de investigación

Retener Y902, K1001 y K1005 como candidatas diferenciadas: K1001 aporta mejor regularidad/DD;K1005 aporta mayor neto y menor concentración monetaria. Ninguna K alcanza la puerta de diez cambios de mecanismo identificados: K1001tiene cincoentradas yK1005cincosalidas. No promover automáticamente ni afirmar que el sobreajuste quedó descartado. K1005 requiere validación propia confeeendógeno y sensibilidad antes de atribuirle la robustez ya estudiada deY902. K1002/3/4no justifican sustitución aquí; conservar registro.

## Verificación final y recuperación

Cinco fuentes releídas exactas; diez formularios completos y treinta snapshots exactos tras recuperación, usando listadoslimit2porreceta. Jesse transforma las claves de snapshots después de correr: de nombreclase a exchange-symbol. El mismatchinicial deK1001era acceso a clave incorrecta, no diferencia de contenido. Normalizando ambas representaciones se verificó identidad literal de los trescódigos porformulario. Se preservaron sources/sesiones/velas.

Hubo respuestaMCPnoJSON y se suspendieron herramientas. K1005siguió enhost y terminó; después de autorización y recuperación se verificaron sesionesexistentes sin duplicarbacktests. QA230PASS previo a fulls, fixes deharness ynombreclase anteriores a creación, sin retuning económico. Root archivó artefactos R8 antes de limpiar13workspaces antiguos; jobsR9intactos. Este cierre no inició análisis ni backtests nuevos.

## Fuentes exactas

```json
[
  {
    "name": "BtcY902ExploreR1001",
    "exact": true
  },
  {
    "name": "BtcY902ExploreR1002",
    "exact": true
  },
  {
    "name": "BtcY902ExploreR1003",
    "exact": true
  },
  {
    "name": "BtcY902ExploreR1004",
    "exact": true
  },
  {
    "name": "BtcY902ExploreR1005",
    "exact": true
  }
]
```

## Formularios y snapshots finales

```json
[
  {
    "name": "K1001C",
    "status": "finished",
    "url": "http://localhost:9200/#/backtest/08d01428-7abe-410a-bf7d-f8c8d46aa35c",
    "form_exact": true,
    "snapshots_exact": 3,
    "snapshot_key_format": "exchange-symbol"
  },
  {
    "name": "K1001B",
    "status": "finished",
    "url": "http://localhost:9200/#/backtest/10be7d01-51f7-480c-9b6c-8b653da82c5a",
    "form_exact": true,
    "snapshots_exact": 3,
    "snapshot_key_format": "exchange-symbol"
  },
  {
    "name": "K1002C",
    "status": "finished",
    "url": "http://localhost:9200/#/backtest/36c79fa4-2e96-482d-80d3-7692b85a261d",
    "form_exact": true,
    "snapshots_exact": 3,
    "snapshot_key_format": "exchange-symbol"
  },
  {
    "name": "K1002B",
    "status": "finished",
    "url": "http://localhost:9200/#/backtest/728f638d-0f10-4b6c-9b6f-4f5533c89df9",
    "form_exact": true,
    "snapshots_exact": 3,
    "snapshot_key_format": "exchange-symbol"
  },
  {
    "name": "K1003C",
    "status": "finished",
    "url": "http://localhost:9200/#/backtest/00c0f043-ea8a-4d28-88be-7553442909e1",
    "form_exact": true,
    "snapshots_exact": 3,
    "snapshot_key_format": "exchange-symbol"
  },
  {
    "name": "K1003B",
    "status": "finished",
    "url": "http://localhost:9200/#/backtest/82105bee-e22b-4ae2-a311-b369453b03e9",
    "form_exact": true,
    "snapshots_exact": 3,
    "snapshot_key_format": "exchange-symbol"
  },
  {
    "name": "K1004B",
    "status": "finished",
    "url": "http://localhost:9200/#/backtest/a523b5c5-8a91-4dd0-b596-550405b10fe5",
    "form_exact": true,
    "snapshots_exact": 3,
    "snapshot_key_format": "exchange-symbol"
  },
  {
    "name": "K1004C",
    "status": "finished",
    "url": "http://localhost:9200/#/backtest/e32e4b65-850b-475f-9179-be61b25131d6",
    "form_exact": true,
    "snapshots_exact": 3,
    "snapshot_key_format": "exchange-symbol"
  },
  {
    "name": "K1005C",
    "status": "finished",
    "url": "http://localhost:9200/#/backtest/8d198fc1-eae8-4a67-8258-e6fabe58756a",
    "form_exact": true,
    "snapshots_exact": 3,
    "snapshot_key_format": "exchange-symbol"
  },
  {
    "name": "K1005B",
    "status": "finished",
    "url": "http://localhost:9200/#/backtest/3f979db7-44e2-44c6-9b82-7c3362084f62",
    "form_exact": true,
    "snapshots_exact": 3,
    "snapshot_key_format": "exchange-symbol"
  }
]
```

## Trazabilidad

BTC_R9_K_VARIANTS_FROZEN_ADDENDUM_20261019.md;BTC_R9_K_FROZEN_SOURCES_20261019.md;BTC_R9_K_SOURCE_QA_20261019.md(jobc568aedf303a420a90d74a2d0f2a391d);BTC_R9_K_DRAFT_REGISTRY_20261019.md;BTC_R9_K_TERMINAL_JOURNAL_20261019.md;BTC_R9_RESULTS_MATRIX_20261019.md y auditorías/metadata root.
