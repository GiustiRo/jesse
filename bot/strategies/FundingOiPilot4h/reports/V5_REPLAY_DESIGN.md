# V5 — diseño de replay y escenarios FUNDING_TREND

Autor: /root/audit. Fecha: 2026-10-21 UTC.
Estado: sólo diseño y plantillas. No hay clases nuevas, drafts, motores ni jobs; no se modificaron fuentes congeladas o REGISTRY_V5. Antes de crear clases con calendario se requiere GO de root tras las cuatro decisiones train.

## Lecturas y soporte existente

Leídos completos por MCP: protocolo V5, ResearchV5Base4h, padres Funding FP/FPOI, funding_features.py y selecciones C1/C2. También manifiesto/verificación de los14wrappers WF y, como referencia, ResearchV3Base4h, dos replays CHANNEL V3, sus fuentes y verificación AST/hash.

Los14wrappers WF V5 fueron verificados y sólo modifican START/FINISH. El replay será otra envoltura de sus padres nominales, sin editar esos wrappers.

El core V5 permite la arquitectura sin cambios:

- _entry_window exige START<T<FINISH y cualquier intervalo a<T<b.
- ACTIVE_WINDOWS=None permite todo el intervalo global: no sirve como marcador pendiente. Una tupla vacía deshabilita entradas.
- FORCE_BOUNDARIES solicita calendar_boundary si T−BAR<boundary<=T, antes de holding e indicador.
- La salida indicadora sólo corre con T>opened_at; holding desde opened_at.
- OI se guarda antes del gate de calendario, incluso en períodos inactivos; buffer6+2+lag en4h.
- Balance, historia OI y cuotas no se reinician en semestres; no reentrada si v5_last_exit_at==T.
- before_terminate registra fold_end; el cierre final puede seguir al AUDIT. Metadata open precierre no demuestra posición residual activa.

V3 sirve como referencia para calendario separado y AST/hash, pero no se copiarán TRAIL_MULTIPLIER, stop2ATR, holding42 ni lógica CHANNEL. FundingV5 conserva stop3ATR fijo, holding180 y ausencia de TP/trailing.

## Calendario conocido y pendiente

| Fold | Período exclusivo al final | FP pasa train | FPOI pasa train |
|---|---|---|---|
| C1 | 2024-01-01→2024-07-01 | sí | sí |
| C2 | 2024-07-01→2025-01-01 | sí | sí |
| C3 | 2025-01-01→2025-07-01 | pendiente | pendiente |
| C4 | 2025-07-01→2026-01-01 | pendiente | pendiente |

C1/C2 se comprobaron en sus selecciones. El selector eligió OI en ambas, pero elegibilidad individual y elección global son objetos distintos: FP conserva sus propios semestres elegibles aunque no gane el ranking.

Pendiente no significa True, False o repetir la decisión anterior. Tampoco se creará una clase final con sólo C1/C2, porque fijaría implícitamente inactividad futura. Las fechas C3/C4 son calendario conocido; no exposición inferida ni datos futuros consultados.

Después de las cuatro selecciones, root guardará un calendario con: referencias/timestamps train; eligible individual por fold; windows de cada variante; cuatro finales forzados; selector por separado; fuentes/hashes y configuración.

Conservar semestres adyacentes separados. Si se estuviera plano en el límite T, una unión de intervalos permitiría una entrada exactamente enT que a<T<b bloquea. FORCE_BOUNDARIES liquida exposición existente, pero por sí solo no impide esa nueva entrada estando plano.

Finales fijos:

- 1719792000000:2024-07-01 UTC.
- 1735689600000:2025-01-01 UTC.
- 1751328000000:2025-07-01 UTC.
- 1767225600000:2026-01-01 UTC, final exclusivo global.

Mantener los cuatro incluso con semestres inactivos. El último puede ser redundante con terminación; registrar una sola liquidación real por calendar_boundary o fold_end según secuencia observada.

## Plantillas nominales exactas, aún no ejecutables

Los marcadores ⟪ ⟫ son deliberadamente no ejecutables. Se reemplazarán por tuplas literales del calendario final después de GO. Estos textos NO son archivos de estrategia creados.

~~~python
from strategies.ResearchV5FundingFP4h import ResearchV5FundingFP4h


class ResearchV5FundingFPReplay4h(ResearchV5FundingFP4h):
    START = 1704067200000
    FINISH = 1767225600000
    USE_OI = False
    OI_LAG_BARS = 0
    PRICE_SMA_PERIOD = 120
    RETURN_LAG = 30
    FUNDING_COUNT = 3
    STOP_MULTIPLIER = 3.
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 180
    TARGET_MODE = "none"
    ACTIVE_WINDOWS = ⟪TUPLA_WINDOWS_FP_CONGELADA_CON_CUATRO_TRAINS⟫
    FORCE_BOUNDARIES = (
        1719792000000,
        1735689600000,
        1751328000000,
        1767225600000,
    )
~~~

~~~python
from strategies.ResearchV5FundingFPOi4h import ResearchV5FundingFPOi4h


class ResearchV5FundingFPOiReplay4h(ResearchV5FundingFPOi4h):
    START = 1704067200000
    FINISH = 1767225600000
    USE_OI = True
    OI_LAG_BARS = 0
    PRICE_SMA_PERIOD = 120
    RETURN_LAG = 30
    FUNDING_COUNT = 3
    STOP_MULTIPLIER = 3.
    ATR_OFFSET_BARS = 0
    MAX_HOLD_BARS = 180
    TARGET_MODE = "none"
    ACTIVE_WINDOWS = ⟪TUPLA_WINDOWS_FPOI_CONGELADA_CON_CUATRO_TRAINS⟫
    FORCE_BOUNDARIES = (
        1719792000000,
        1735689600000,
        1751328000000,
        1767225600000,
    )
~~~

Atributos redundantes explícitos facilitan auditoría. Ningún wrapper define hooks o reimplementa señales, ejecución, tamaño, OI o contabilidad. Padres/helpers/core se mantienen congelados.

## Escenarios por herencia mínima

Cada vecino hereda su replay nominal, con idénticos límites/calendario/configuración nominal. El futuro archivo importa exclusivamente su padre y define estas asignaciones:

| Clase propuesta | Padre | Únicos atributos nuevos |
|---|---|---|
| ResearchV5FundingFPReplayR09_4h | ResearchV5FundingFPReplay4h | STOP_MULTIPLIER=2.7 |
| ResearchV5FundingFPReplayR11_4h | ResearchV5FundingFPReplay4h | STOP_MULTIPLIER=3.3 |
| ResearchV5FundingFPReplayA09_4h | ResearchV5FundingFPReplay4h | PRICE_SMA_PERIOD=108; RETURN_LAG=27 |
| ResearchV5FundingFPReplayA11_4h | ResearchV5FundingFPReplay4h | PRICE_SMA_PERIOD=132; RETURN_LAG=33 |
| ResearchV5FundingFPOiReplayR09_4h | ResearchV5FundingFPOiReplay4h | STOP_MULTIPLIER=2.7 |
| ResearchV5FundingFPOiReplayR11_4h | ResearchV5FundingFPOiReplay4h | STOP_MULTIPLIER=3.3 |
| ResearchV5FundingFPOiReplayA09_4h | ResearchV5FundingFPOiReplay4h | PRICE_SMA_PERIOD=108; RETURN_LAG=27 |
| ResearchV5FundingFPOiReplayA11_4h | ResearchV5FundingFPOiReplay4h | PRICE_SMA_PERIOD=132; RETURN_LAG=33 |
| ResearchV5FundingFPOiReplayLag4h | ResearchV5FundingFPOiReplay4h | OI_LAG_BARS=1 |

Ejemplo de patrón, no archivo creado:

~~~python
from strategies.ResearchV5FundingFPReplay4h import ResearchV5FundingFPReplay4h


class ResearchV5FundingFPReplayA09_4h(ResearchV5FundingFPReplay4h):
    PRICE_SMA_PERIOD = 108
    RETURN_LAG = 27
~~~

108/27 y132/33 son SMA y retorno de PRECIO, no lag de publicación. Mantienen tres pagos, ATR14/offset0, stop3ATR, holding180, sin TP/trailing. La media vecina también afecta salida adversa por precio; funding adverso conserva prioridad e independencia. No cambiar FUNDING_COUNT para rescatar un vecino.

R09/R11 sólo cambian protección y sizing asociado. A09/A11 sólo ventanas de precio. No combinar riesgo+señal ni elegir vecino ganador o calendario nuevo bajo escenarios.

Lag4h es UNA barra4h: current observadoT−4h/refT−28h, con calidad original. Precio/funding siguen enT; buffer9, primeras siete decisiones inicialización, referencia posible octava. No confundir con cuatro barras4h o RETURN_LAG. FP sinOI reutiliza nominal para ese slot, previa igualdad exacta.

## Costes por configuración de sesión

S1/S2/S3 reutilizan la clase replay nominal respectiva. Copiar profundamente la configuración nominal de REGISTRY_V5 y cambiar sólo form.config.exchange:

| Escenario | fee | slippage_bps |
|---|---:|---:|
| NOMINAL |0.00045|0|
| S1 |0.0009|0|
| S2 |0.00045|5|
| S3 |0.0009|10|

Todo lo demás permanece: BTC-USDT/Binance Perpetual Futures/4h, balance10000, isolated3x, warmup240, cap prefill1x, datasets versionados, missingOI permitido y max_age600000, logging nominal, debug/fast solicitados true, exports/benchmark false y fast efectivo false.

Fee estresada entra en sizing antes de qty; slippage MARKET/STOP según contrato del motor, nunca haircut. Distintas cantidades, trayectorias y oportunidades son esperables; no exigir mismos trades.

FaseC completa, sólo si root autoriza:2nominales+6costes+8vecinos+1lagOI=17runs nuevos; slot lag sinOI reutiliza nominal,18slots. No aumenta límite40 ni autoriza ejecuciones. Once clases bastan:2nominales+8vecinos+1lagOI; costes no requieren subclases.

## Capital y fronteras

Replay [2024-01-01,2026-01-01),731días,10000 una sola vez. Capital/OI/cuota continúan entre semestres incluso inactivos. No convertirlos en sesiones independientes; CAGR incluye todo el intervalo.

Con posición en borde internoT: fills del minuto anterior→funding efectivoT→decisión de cierre MARKET. Puede pagar fundingT que una sesión WF finish-exclusive no procese. EntryMARKETT no paga ese evento previo y, en límites de calendario, además está bloqueada por ventanas estrictas. Una protección anterior a funding debe auditarse por órdenes/fases, no sólo opened_at<=T<=closed_at.

Effective_at gobierna intervalos; settled_at raw conserva jitter documentado. No funding>=1767225600000 ni velas con apertura2026. Un cierreTfinish basado en última vela2025 no es consulta2026.

Que V3 no tuviera posiciones en sus bordes no prueba lo mismo para V5. FundingV5 puede mantener30d y llegar a un borde; si la rama no aparece en motor, declararla sólo como check determinista.

## Verificación futura antes de economía

Primero: completar cuatro trains, guardar calendario individual/selector y consultar root antes de crear clases. Después, root ejecutará sus validaciones; esta tarea no inició jobs.

1. Capturar core4h/helper/padres/dependencia V2 y comparar fuentes congeladas.
2. Generar once fuentes literales. Compile+AST sin importar proyecto: un ImportFrom, una ClassDef, padre exacto, únicamente Assign con literal_eval; sin métodos, llamadas o decoradores.
3. Nominales: START/FINISH exactos, constantes nominales, ACTIVE_WINDOWS idéntico al calendario individual y cuatro FORCE_BOUNDARIES. Rechazar marcador pendiente/None.
4. FechasUTC4h ordenadas, sin solapes; cada ventana coincide con semestre train elegible y no se fusionan adyacentes.
5. Vecinos: padre/atributos exactamente tabla. Lag sólo OI_LAG_BARS1 enFPOI. Prohibir TRAIL_MULTIPLIER y lógica CHANNEL.
6. HashSHA256 de fuentes/config/calendario y readbackMCP idéntico antes de drafts; prerun configuración exacta.
7. Fixtures puros a−BAR/a/a+BAR/b−BAR/b/b+BAR, plano y con posición; en semestres adyacentes el borde común sigue bloqueado.
8. Calendar close antes de holding y salidas INDICADORAS por funding adverso/precio; el cashflow de funding del MOTOR ocurre ANTES de la decisión calendar en un borde interno. Una solicitud, sin reversión enT ni resetcapital/OI. Fin global como máximo un cierre, admitiendo fold_end posterior alAUDIT.
9. OI nominal/lag/faltantes/ceros/stale e inactividad, buffers8/9 y primeras referencias séptima/octava, sin backfill.
10. Medias108/132 y referencias27/33 finitas exactas; tres tasas publicadas conservadas; stop2.7/3.3 desde fill y sizing con fee.
11. Logs JSON<=1900, contabilidad tolerancia1e−6 y planes/callback/ledger completos. Mocks prueban control, no fills del broker.

No repetir arbitrariamente smokes: cualquier técnico adicional necesita presupuesto y GO específico, sin usar su rentabilidad para elegir parámetros.

## Auditoría posterior

Root usará snapshots completos para bruto−fees+funding=PNL/saldo, ledgerqty/mark/rate/clock, fees/fills/slippage y continuidad. Calendario nominal train idéntico en costes/vecinos/lag.

Retornos mensuales/anuales/semestrales desde equity de la misma cuenta, nunca PNL de cierres. Convención−61s para sellos diarios00:01/terminal00:00 salvo baseline; saldo real sólo sustituye el punto terminal final. Registrar muestreo/resolución y timestamps, sin inventar equity intraminuto de borde ni rellenar evidencia faltante.

PF por trades únicos de cada replay; DDmotor gobierna gate y DDmuestreado es complementario. Gates nominales intactos:net>0/PF>=1.2/DD<=25/N>=100/3de4semestres positivos/CAGR>=15%. S1/S3, cada vecino ylag aplicable net>0/DD<=25; S2 informativo. No promover por escenario más favorable.

Reportar ambas sensibilidades fijas proxy-only/globalfunding×.5/1.5 con qty/fills originales, separando fuentes desconocidas. Son análisis, no replays. WF reescalado es comparador hipotético, separado de calendarios individuales/selector. No forzar igualdad de operaciones ni causalidadOI sin evidencia.

Los snapshots backtest omiten logs. Éstos se auditan aparte porMCP, sin pegar arrays como sustituto de inputs completos.

## Nota de réplica arquitectónica V6

Según actualización de root, V6 tiene shortlist única EFFICIENCY_P y siete wrappers WF con AST aprobado. Esta nota NO consultó economía C1V6 ni modifica su protocolo.

Puede reutilizarse la arquitectura de calendario train individual, capital continuo, cuatro bordes, AST/hash/config y contabilidad, no indicadores/padres V5. Conservar únicamente overlays V6 validados por su dueño: riesgo2.25/2.75ATR y umbral h0.315/0.385; nombres de atributos e intervención exacta según freeze propio de Efficiency. SinOI, el slot lag reutiliza nominal, no crea otra ejecución. No copiar FUNDING_COUNT, SMA120/C30 o señales de funding aV6.

## Próximo paso

Queda disponible sólo este diseño. Esperar C3/C4 y GO de root para las clases finales; luego fuente/calendario/config se verifican antes de cualquier arranque. No hubo calendario futuro inferido, nuevas fuentes productivas, sesiones o jobs.
