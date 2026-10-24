# Fase C V3 — propuesta de fuentes CHANNEL_P
Fecha: 2026-10-20.
Estado: PROPUESTA PREVIA AL CALENDARIO. No se crearon clases, fuentes ejecutables ni sesiones de replay. No se consultaron resultados económicos nuevos.
Leído por MCP: V3_REPLAY_AUDIT_PLAN.md y padre nominal ResearchV3ChannelP4h.
Root congela E(P,C1..C4) después de C4 train; la ejecución esperará además el cierre de la confirmación nominal y GO explícito de fase C.

## Política temporal exacta
Replay individual P: [2024-01-01,2026-01-01), capital10000 inicial transportado durante731días UTC. Se filtran los siguientes cuatro intervalos, conservándolos separados y ordenados:
| Fold | Inicio inclusivo de datos | Fin exclusivo | Intervalo para entradas a<T<b |
|---|---|---|---|
| C1 | 2024-01-01 | 2024-07-01 | (1704067200000,1719792000000) |
| C2 | 2024-07-01 | 2025-01-01 | (1719792000000,1735689600000) |
| C3 | 2025-01-01 | 2025-07-01 | (1735689600000,1751328000000) |
| C4 | 2025-07-01 | 2026-01-01 | (1751328000000,1767225600000) |

ACTIVE_WINDOWS contendrá únicamente las tuplas de Cj donde esta finalistaP pasó su gate train nominal, E(P,j), tomadas del registro previo a cada evaluación. No se usa el calendario del selector globalG ni el deCHANNEL_POI ni las rentabilidades de evaluación.
No fusionar intervalos adyacentes: incluso entre dos semestres activos está prohibida la nueva entrada exactamente en el borde y se cierra la posición que llega a ese borde.
FORCE_BOUNDARIES propuesto en todos los cierres semestrales:1719792000000,1735689600000,1751328000000,1767225600000.
Los tres primeros son cortes internos imprescindibles. El último declara también el cierre final solicitado; la terminación normal del motor sigue siendo el respaldo al fin exclusivo y no requiere vela ni funding efectivo de2026. Si el motor no invoca update_position en el instante final, before_terminate/fold_end cierra lo restante. Nunca solicitar una barra de2026 para materializarlo.
Una lista activa vacía significa política plana; no convertirla en None, que quitaría el filtro de exposición. En esta propuesta sólo se usa () como guardia de plantilla; no representa un calendario ya resuelto.

## Plantilla nominal para renderizar después de congelar calendario
NO crear esta clase con el placeholder ni usar su hash como fuente final. Sustituir sólo ACTIVE_WINDOWS por las tuplas literales E(P,j) aprobadas por root; después guardar fuente íntegra/hash y verificar contra formulario.
```python
from strategies.ResearchV3ChannelP4h import ResearchV3ChannelP4h


class ResearchV3ChannelPReplay4h(ResearchV3ChannelP4h):
    START = 1704067200000
    FINISH = 1767225600000
    USE_OI = False
    OI_LAG_BARS = 0
    STOP_MULTIPLIER = 2.
    TRAIL_MULTIPLIER = 3.
    MAX_HOLD_BARS = 42
    TARGET_MODE = "none"
    # Placeholder fail-closed: replace with the frozen E(P,j) literal tuple before creation.
    ACTIVE_WINDOWS = ()
    FORCE_BOUNDARIES = (
        1719792000000,
        1735689600000,
        1751328000000,
        1767225600000,
    )
```

No sobreescribir callbacks, posición, gestión, features, regla de rango/medias ni cuota diaria. El padre conserva trailing causal desde fill, stop inicial2A, sinTP y máximo7d. STOP2/TRAIL3/HOLD42/MODE none se explicitan para evitar una deriva de atributos al revisar fuentes; no cambian su valor nominal.
El START/FINISH explícito impide heredar por error FINISH=2024-01-01 del screening, que bloquearía todo el período de confirmación/replay aunque se cambiara el formulario.

## Dos vecinos exactos, sin búsqueda adicional
Cada clase hereda de la clase replay congelada y por tanto comparte calendario, límites, datos, señales, holding y ausencia deOI. Cambia sólo estos dos atributos:
```python
from strategies.ResearchV3ChannelPReplay4h import ResearchV3ChannelPReplay4h


class ResearchV3ChannelPReplayN09_4h(ResearchV3ChannelPReplay4h):
    STOP_MULTIPLIER = 1.8
    TRAIL_MULTIPLIER = 2.7
```
```python
from strategies.ResearchV3ChannelPReplay4h import ResearchV3ChannelPReplay4h


class ResearchV3ChannelPReplayN11_4h(ResearchV3ChannelPReplay4h):
    STOP_MULTIPLIER = 2.2
    TRAIL_MULTIPLIER = 3.3
```
No reestimarATR, cambiar SMA/canal/holding o elegir el mejor vecino para sustituir el nominal. El sizing usa la distancia vecina desde el comienzo de su replay.

## Fricción reutiliza exactamente la clase nominal
Las cuatro sesiones usan la misma ruta ResearchV3ChannelPReplay4h y el mismo calendario. Sólo cambian los campos indicados de form.config.exchange:
| Caso | fee | slippage_bps | Clase |
|---|---:|---:|---|
| nominal | 0.00045 | 0 | ResearchV3ChannelPReplay4h |
| S1 | 0.0009 | 0 | ResearchV3ChannelPReplay4h |
| S2 | 0.00045 | 5 | ResearchV3ChannelPReplay4h |
| S3 | 0.0009 | 10 | ResearchV3ChannelPReplay4h |

Fee estresada participa en sizing real de cada sesión. El motor ajusta MARKET/STOP adversamente; no sumar un haircut al final. No copiar/resetear trades nominales para crear los escenarios.
Los dos vecinos usan fee0,00045/slip0 nominales. SinOI, el escenario de retraso adicional es equivalente económicamente y se registra como reutilización del nominal; no crear clase/ motor extra ni reasignar ese slot a otro parámetro.
Total previsto de esta rama faseC: seis motores nuevos (nominal+S1+S2+S3+N09+N11), una reutilización lagP, dentro del presupuesto global. Root mantiene slots y registry; esta propuesta no arranca ninguno.

## Configuración que debe quedar idéntica salvo fricción indicada
Una ruta Binance Perpetual Futures/BTC-USDT/4h,10000USDT iniciales,isolated3x,capnotionalC,riesgo2%stop+fees,warmup240,debugtrue,benchmarkfalse,exportsfalse. Funding yOI configurados historical con datasets inmutables:
- funding9c5618c2393e7281467184f804c58032b1219a6057ce6a009324ec4cc089f571;
- OI6694352b75cba232bf1ffa6aa1d62e54e0cf751582ef0a9c4b49972ebc7e1abf,max_age_ms600000,allow_missing_observationsTrue.
P mantieneUSE_OI=False aunque la base siga observando OI de forma causal para procedencia. Sin gateeconómico funding.
No reiniciar balance/margen/historialOI/cuota diaria entre semestres. La gestión de protecciones continúa aunque el calendario bloquee entradas; FORCE_BOUNDARIES exige los cierres de borde.
Las clases P/OI de faseC tendrán calendarios individuales distintos si difieren sus gates. No copiar el calendario de la otra rama por conveniencia.

## Registro y preflight previstos, sin ejecutarlos ahora
1. Root entrega cuatro valores E(P,j), decisiones train y timestamps previos a cada eval; filtrar tuplas sin consultar retornos para decidir exposición.
2. Renderizar fuente nominal y dos vecinos; guardar por MCP más snapshots íntegros de cadena replay→CHANNEL_P→V3Base→V2Core y channel_features, hashes y config.
3. Verificar START/FINISH clase==formulario; calendarios literales e intervalos separados; todos los cierres; atributos iguales salvo los dos multiplicadores vecinos. Clase de lagP se reutiliza, no motor.
4. Crear drafts y guardar ID/dashboard_url/config antes de run. Cada timeout requiere lectura del mismo ID; preservar raw y no duplicar.
5. Sólo ejecutar cuando root dé GO, máximo un motor P simultáneo bajo el límite global de dos con la ramaPOI. No editar el registry global desde esta rama.
6. Capturar auditorías mensuales completas:24meses y4386decisiones4h, hasta96buckets materializados. No exigir buckets cero que no se crean: conservar cada all mensual y sus particiones reales. Conciliar exits al snapshot final, incluido fold_end posterior al resumen.
7. Root realiza snapshots completos/run_analysis y tablas de bordes según V3_REPLAY_AUDIT_PLAN.md, sin sumar saldos de dos finalistas.
8. Revisar ledger de cada borde: funding efectivo puede cobrarse antes de un cierre MARKET del mismo instante. Eso difiere de una sesión semestral finish-exclusive y no se corrige omitiendo cargos.
9. CAGR usa731días y todos los meses planos; retorno semestral proviene de equity de este replay, no suma de trades cerrados en un intervalo.

## Límites
La auditoría estática V3_CALENDAR_STATIC_AUDIT.md aprobó58checks de superficie; no sustituye este replay, sus fills, broker, ledger o transporte de capital. La continuidad OI se demuestra bajo misma instancia; debe conservarse en el motor real.
Slippage no garantiza liquidez/latencia/aceptación en venue; marcasproxy y archivoOIretrospectivo siguen limitando interpretación. No se cambia protocolo/gates tras observar escenarios.
Se aguarda calendario yGO; cero clases/drafts/backtests nuevos, cero consultas económicas nuevas y ninguna vela/evento2026 en esta entrega.
