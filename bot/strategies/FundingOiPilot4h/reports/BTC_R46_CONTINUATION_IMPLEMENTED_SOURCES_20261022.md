# R46 — implementación de continuación incremental, sin ejecución

Fecha: 2026-10-22. Protocolo BTC_R46_CONTINUATION_VALUE_PROTOCOL_20261022.md leído completo antes de fuentes y releído completo con addendum de side antes del cierre. Recurso jesse://funding leído completo, con API pública de historial causal y orden fills/funding/decisiones. R10 leído para reutilizar closed_window y atr14, sin modificarlo.

## Estado, hashes y alcance

Sólo dos fuentes nuevas por MCP; primer intento y readbacks completos exactos. Cero jobs, análisis, drafts, backtests u órdenes ejecutados por esta subtarea. Ningún dataset/candle preinspeccionado, filesystem del bot, storage/backend/DB, research_scripts, dependencia nueva o cambio de framework/configuración. El observador no calcula sizing económico ni impone un consejo al camino de las sombras.

BtcResearchR46ContinuationMath: SHA256 d99555ef0ae33616e5e2a2f5d08ba590163be0fdd2c49d435f1cea9d13da10e4; 8456 caracteres; readback exacto.
BtcResearchR46ContinuationObserver1m: SHA256 2db2a55099f4cf32aa173fca7475ea8ee9708411e7980965c6d134fc3b282858; 19864 caracteres; readback exacto.
Protocolo final leído: SHA256 35e4332fa036cb318e1549cb3799c8e043dae5303d14cd085bb1fa6423250b35.
R10 leído: SHA256 2279d3b9706163620405d73ca6d5588745924a19b4014f713e493affb2698ba9.

No existió una fuente creada sin side: root fortaleció el benchmark antes de la creación y preservó el protocolo v1 por separado. Ambas regresiones incluyen intercept/age2..11/side/progress; contexto añade únicamente recent/giveback (13/15 columnas).

## Interfaces y datos

Math, clase importable sin órdenes:
- stop_event(side,stop,m1): None o exit_time/exit_price/reason STOP; toque inclusivo y fill adverso al open.
- review_features(side,entry,D,previous_mark,bestR,mark,age): side/age/progress/recent/giveback/bestR desde cierres4h ya vistos. Age1 recent=progress.
- merge_registry(registry,incoming,now,exchange,symbol): registro normalizado y filas nuevas; pura, sin acceso externo.
- label_value(side,mark,exit_price,D,fee,events,node_time,exit_time,exit_kind,finish): price_component/fee_component/funding/delta y effective IDs usados.
- design_vector(row,context): 13/15 columnas fijas.
- weighted_ridge(rows,context): columnas/means/scales/constant/beta, N/days/weights_sum/day_counts.
- fit_window(bank,fit_time): (pairfit,reason) o abstención común explícita; pairfit tiene control/context/day_ids/age_counts/origin_episodes.
- predict(model,row): Delta pronosticada finita, sin clipping ni escalado del target.

Bank[origin]={origin,valid,reason,released,release_at,nodes,closed_sides}. Nodos conservan origen/lado/edad/features, mark/entry/D/stop, previous_mark/bestR_before, fitid/predicciones, relojes, salida congelada y madurez/delta. Cada día inválido queda como placeholder de ambos lados; no se busca un día válido más antiguo.

## Flujo temporal y conservación

before valida M1 completo START+1m→FINISH con OHLC/quote/paridad; gap o duplicado es fallo técnico explícito. Procesa stops del minuto cerrado antes de cualquier otra acción. En lectura START+1m y cada4h+1m: ingiere historial público, madura labels y libera banco. En fronteras4h antes de FINISH: intento mensual, resuelve horizontes/deadlines, crea origen diario y revisiones. Resolver un horizonte fija precio/clock de salida pero espera ready=T+4h+1m para financiación/delta.

Origen diario estrictamente después de START: 1.903 slots esperados; una pair válida crea sombras +1/−1. Reutiliza closed_window/atr14 de15 barras4h. D=2ATR y ambos stops positivos; el fallo de cualquiera invalida el pair, sin selección de lado. ORIGIN exporta header y quince barrasOHLC en tres partes de cinco para replay de ATR.

Activos exógenos en r46_active; una sombra viva mantiene un nodo activo por intervalo. El stop cierra primero y fija la salida del nodo pendiente, cuyo label mantiene su deadline de madurez original. En frontera4h se resuelve el nodo previo y se crea la siguiente revisión sólo si aún vive; no revisión12. bestR usa cierres4h, sin extrema M1 o futuros. Cada sombra sigue aunque predDelta<=0.

Bank sólo libera a origin+48h+1m, incluso stop temprano o cero nodos. Requiere ambas sombras cerradas y todos sus nodos maduros. Se conserva ventana móvil exacta180 días de origen liberados más episodios recientes pendientes; pruna sólo registros antiguos ya liberados. Refit mensual usa los últimos180 días completamente maduros al fit_time,360 sombras previstas; no anticipa la liberación que ocurre un minuto después de un corte00UTC. Seed/invalid-day/support<360nodos o<20 por edad abstiene ambos todo el mes; no recupera ajuste anterior.

FINISH permite únicamente procesar el stop observable del último minuto2025. No resuelve MARKETdeadline, crea origen/revisión, ingiere rate2026 ni madura un label con fecha posterior. Finalización cuenta y registra pendientes/sombras vivas/orígenes aún no liberados como censura, sin fabricar rentabilidad. Asserts de conservación nodes=labels+censored y shadows=stops+deadlines+censored, además de origen/coverage M1 y wallet10000/qty0/noentryorders. No son assertions de potencia ni resultados económicos.

## Registro funding y etiqueta

Sólo strategy.get_funding_history(count=16). Schema público confirmado por root: exchange,symbol,settled_at,rate_decimal,mark_price,mark_price_source,available_at; NO effective_at. Se deriva effective=settled−settled%60000, conserva jitter y exige available=effective+1m<=now, orden estricto y valores finitos/markpositivo. Después de la primera ventana exige overlap con la última fila previa y rechaza conflictos/regresión. Iniciales preSTART se aceptan/logean como seed; core>=START se cuenta por separado. No se usa longitud16 como certificado de cobertura.

La madurez exige lectura de esa frontera ready completada y al menos un evento efectivo<=node_time en registry. Con overlap y cobertura nativa del dataset esto acredita completitud relativa al contrato de replay, no al proveedor. Efectivos posteriores a revisión se filtran por salida: STOP excluye igualdad con exit_time; MARKET horizon/deadline la incluye; FINISH siempre exclusivo. Label sólo usa cash futuro por unidad, sin leverage adicional.

Delta=(side*(exit−mark)+fee*(mark−exit)+funding_future)/D. Entryfee y financiación hasta revisión son hundidos, no se cobran otra vez. Los eventos futuros sólo entran al madurar labels y luego, una vez liberados, al entrenamiento; ninguna tasa entra como feature.

SHADOW_CLOSE STOP exporta minuto open/end y OHLC para verificar gapfill. NODE exporta previous_mark/bestR_before para reconstruir features causalmente. Esas observaciones no son un feed M1 independiente completo y no acreditan por sí solas ausencia de un stop anterior.

## Ridge, evaluación y telemetría

Cada día con nodos aporta masa1, distribuida entre todos sus nodos de ambos lados; días sin nodos permanecen en cobertura pero no regresión. Pesos reescalados a media1. Medias/std ponderadas sólo train. np.ptp==0 fuerza mean=valor constante,sd1,columna transformada0 exacta. Intercept sin penalizar, lambda1 en otras columnas, solve determinista; no target scaling, retry o selección. Números no finitos/fallo solve son errores técnicos explícitos.

Predicciones y labels quedan congelados por identidad. Scores nodoigual y díaigual usan TODOS los nodos comunes maduros, no sólo HOLD; v=delta si pred>0, si no0. Días finales parcialmente censurados conservan sus nodos maduros y se cuentan como parciales. Cohortes por año UTC de origen, no cierre. Root aplica gates desde evidencia; el observador no convierte resultados en filtros.

Logs JSON estrictos<1800 por línea, sin exportar cada M1:
- R46_ORIGIN header/atr_inputs; R46_SHADOW_CLOSE; R46_NODE; R46_LABEL.
- R46_FUND_EVENT cada evento nuevo una vez con seed/core y provenance.
- R46_BANK documenta cada liberación diaria, incluidos inválidos/cero nodos.
- R46_FIT status, train_days chunks40 con counts por día, scalers/constant/columns, beta, N/weights_sum. Permite replay de población/pesos/coeficientes desde NODE/LABEL.
- R46_CENSORED por nodo/sombra/origen; R46_SUMMARY financiero0/conservación y scores todo/años; R46_DAY_SCORE permite agrupación/concentración diaria independiente.

La escritura valida sintaxis y guarda fuentes, pero no acredita harness, reloj efectivo nativo, cobertura real, funding relativo, scores o rentabilidad. Los checks supplied-source, observador único y auditoría posterior quedan bajo coordinación de root. Los objetivos r9 y cierres anteriores permanecen intactos.

## Fuentes nuevas completas

### BtcResearchR46ContinuationMath

```python
import math
from collections import Counter
import numpy as np
from jesse.strategies import Strategy

MINUTE = 60000
BAR = 14400000
DAY = 86400000
BASE_COLUMNS = ["intercept"] + ["age"+str(age) for age in range(2, 12)] + ["side", "progress"]


def stop_event(side, stop, m1):
    """Independent unit shadow: last closed M1 touch, adverse open gap, no TP."""
    assert side in (-1, 1)
    touched = float(m1[4]) <= stop if side == 1 else float(m1[3]) >= stop
    if not touched:
        return None
    price = min(float(m1[1]), stop) if side == 1 else max(float(m1[1]), stop)
    return dict(exit_time=int(m1[0])+MINUTE, exit_price=price, reason="STOP")


def review_features(side, entry, D, previous_mark, bestR, mark, age):
    """Only already observed 4h closing marks update bestR; no high/low extrema."""
    assert side in (-1, 1) and 1 <= age <= 11 and D > 0
    progress = side*(mark-entry)/D
    best = max(0., bestR, progress)
    result = dict(side=int(side), age=int(age), progress=float(progress),
                  recent=float(side*(mark-previous_mark)/D),
                  giveback=float(best-progress), bestR=float(best))
    assert all(math.isfinite(float(value)) for value in result.values())
    return result


def merge_registry(registry, incoming, now, exchange, symbol):
    """Pure public-history ingestion; registry is insertion-ordered effective->row.

    Incoming rows expose settled_at, not effective_at; boundary jitter is retained.
    Every later causal window must overlap the previous most recent event.
    """
    assert isinstance(incoming, list) and 0 < len(incoming) <= 16, "R46_FUND_WINDOW_EMPTY"
    normalized = []
    previous = None
    for source in incoming:
        assert source["exchange"] == exchange and source["symbol"] == symbol
        settled = int(source["settled_at"])
        effective = settled-settled % MINUTE
        available = int(source["available_at"])
        assert 0 <= settled-effective <= 1000
        assert available == effective+MINUTE and available <= now
        assert previous is None or effective > previous, "R46_FUND_WINDOW_ORDER"
        previous = effective
        rate, mark = float(source["rate_decimal"]), float(source["mark_price"])
        assert math.isfinite(rate) and math.isfinite(mark) and mark > 0
        normalized.append(dict(exchange=exchange, symbol=symbol, settled_at=settled,
            effective_at=effective, available_at=available, rate_decimal=rate,
            mark_price=mark, mark_price_source=source["mark_price_source"]))
    if registry:
        last = next(reversed(registry))
        assert any(row["effective_at"] == last for row in normalized), "R46_FUND_OVERLAP_LOST"
    updated, fresh = dict(registry), []
    for row in normalized:
        key = row["effective_at"]
        if key in updated:
            assert updated[key] == row, "R46_FUND_CONFLICT"
        else:
            assert not updated or key > next(reversed(updated)), "R46_FUND_REGRESSION"
            updated[key] = row
            fresh.append(row)
    return updated, fresh


def label_value(side, mark, exit_price, D, fee, events,
                node_time, exit_time, exit_kind, finish):
    """Incremental cashflow per D: entry fees and funding through node_time are sunk.

    events may be a causal registry slice; the caller separately proves its
    relative completeness via overlap and the target+1m ingestion.
    """
    assert side in (-1, 1) and D > 0 and exit_time > node_time
    assert exit_kind in ("STOP", "horizon", "deadline")
    included = [row for row in events
        if node_time < row["effective_at"] < finish
        and (row["effective_at"] < exit_time if exit_kind == "STOP"
             else row["effective_at"] <= exit_time)]
    funding = -side*sum(row["mark_price"]*row["rate_decimal"] for row in included)
    price_component = side*(exit_price-mark)
    fee_component = fee*(mark-exit_price)
    delta = (price_component+fee_component+funding)/D
    assert all(math.isfinite(x) for x in (funding, price_component, fee_component, delta))
    return dict(price_component=float(price_component), fee_component=float(fee_component),
                funding=float(funding), delta=float(delta),
                funding_effectives=[row["effective_at"] for row in included])


def design_vector(row, context=False):
    """13-column shared control; context appends only recent and giveback."""
    age = int(row["age"])
    assert 1 <= age <= 11 and row["side"] in (-1, 1)
    values = [1.] + [float(age == value) for value in range(2, 12)]
    values += [float(row["side"]), float(row["progress"])]
    if context:
        values += [float(row["recent"]), float(row["giveback"])]
    return np.asarray(values, dtype=float)


def weighted_ridge(rows, context=False):
    """Origin-day mass1, weights rescaled to mean1; lambda1, no target scaling."""
    N = len(rows)
    assert N > 0
    day_counts = Counter(int(row["origin"]) for row in rows)
    days = len(day_counts)
    weights = np.array([N/(days*day_counts[int(row["origin"])]) for row in rows])
    X = np.array([design_vector(row, context) for row in rows])
    y = np.array([float(row["delta"]) for row in rows])
    assert np.all(np.isfinite(X)) and np.all(np.isfinite(y))
    means, scales = np.zeros(X.shape[1]), np.ones(X.shape[1])
    constant = np.zeros(X.shape[1], dtype=bool)
    transformed = X.copy()
    for j in range(1, X.shape[1]):
        if np.ptp(X[:, j]) == 0:
            means[j], scales[j], constant[j] = X[0, j], 1., True
            transformed[:, j] = 0.
        else:
            means[j] = np.sum(weights*X[:, j])/np.sum(weights)
            scales[j] = math.sqrt(float(np.sum(weights*(X[:, j]-means[j])**2)/np.sum(weights)))
            assert math.isfinite(scales[j]) and scales[j] > 0
            transformed[:, j] = (X[:, j]-means[j])/scales[j]
    penalty = np.eye(X.shape[1])
    penalty[0, 0] = 0.
    beta = np.linalg.solve(transformed.T@(weights[:, None]*transformed)+penalty,
                           transformed.T@(weights*y))
    assert np.all(np.isfinite(beta)) and np.all(np.isfinite(means)) and np.all(np.isfinite(scales))
    return dict(context=bool(context), columns=BASE_COLUMNS+(["recent", "giveback"] if context else []),
                means=means, scales=scales, constant=constant, beta=beta, N=N,
                days=days, weights_sum=float(weights.sum()),
                day_counts=sorted(day_counts.items()))


def fit_window(bank, fit_time):
    """Last180 origin DAYS mature at48h+1m, no filling older valid observations.

    bank[origin]={origin,valid,released,release_at,nodes}; each node is a mature
    row with origin/side/age/progress/recent/giveback/delta/ready.
    """
    latest = ((fit_time-2*DAY-MINUTE)//DAY)*DAY
    wanted = [latest-i*DAY for i in range(179, -1, -1)]
    episodes = [bank.get(day) for day in wanted]
    if any(episode is None for episode in episodes):
        return None, "missing_180_origin_days"
    if any(not e["released"] or e["release_at"] > fit_time for e in episodes):
        return None, "origin_days_not_mature"
    if any(not e["valid"] for e in episodes):
        return None, "invalid_origin_day_in_window"
    rows = [node for episode in episodes for node in episode["nodes"]]
    assert all(node["mature"] and node["ready"] <= fit_time for node in rows)
    if len(rows) < 360:
        return None, "fewer_than_360_nodes"
    counts = Counter(int(node["age"]) for node in rows)
    if any(counts[age] < 20 for age in range(1, 12)):
        return None, "age_support_below_20"
    return dict(control=weighted_ridge(rows, False), context=weighted_ridge(rows, True),
                day_ids=wanted, age_counts={age:counts[age] for age in range(1, 12)},
                origin_episodes=360), None


def predict(model, row):
    vector = design_vector(row, model["context"])
    transformed = (vector-model["means"])/model["scales"]
    transformed[0] = 1.
    transformed[model["constant"]] = 0.
    value = float(transformed@model["beta"])
    assert math.isfinite(value)
    return value


class BtcResearchR46ContinuationMath(Strategy):
    """Importable pure helper container, never an economic strategy."""
    def should_long(self):
        return False

    def should_short(self):
        return False

    def go_long(self):
        raise AssertionError("R46 math has no orders")

    def go_short(self):
        raise AssertionError("R46 math has no orders")
```

### BtcResearchR46ContinuationObserver1m

```python
import bisect
import json
import math
from datetime import datetime, timezone
import numpy as np
from jesse.strategies import Strategy
from strategies.BtcResearchR10Base4h import closed_window, atr14
from strategies.BtcResearchR46ContinuationMath import (
    MINUTE, BAR, DAY, stop_event, review_features, merge_registry,
    label_value, fit_window, predict,
)


class BtcResearchR46ContinuationObserver1m(Strategy):
    """Exogenous unit shadows and incremental labels, never orders or capital sizing."""
    START = 1602720000000
    FINISH = 1767225600000

    def should_long(self):
        return False

    def should_short(self):
        return False

    def go_long(self):
        raise AssertionError("R46 observer has no orders")

    def go_short(self):
        raise AssertionError("R46 observer has no orders")

    def _log(self, label, value):
        encoded = label+" "+json.dumps(value, separators=(",", ":"), allow_nan=False)
        assert len(encoded) < 1800, "R46_LOG_TOO_LARGE"
        self.log(encoded)

    def _counts(self):
        return self.vars.setdefault("r46_counts", dict(
            minutes=0, origins=0, valid_origins=0, invalid_origins=0,
            shadows=0, shadow_stops=0, shadow_deadlines=0, censored_shadows=0,
            zero_review_shadows=0, nodes=0, predicted_nodes=0, unpredicted_nodes=0,
            labels=0, mature_predicted_nodes=0, censored_nodes=0,
            released_days=0, released_valid_days=0, released_nodes=0,
            zero_node_origin_days=0, censored_origin_days=0,
            fit_attempts=0, fit_valid=0, fit_invalid=0,
            funding_reads=0, funding_new=0, funding_seed=0, funding_core=0))

    def _ingest_funding(self, now):
        registry, fresh = merge_registry(self.vars.get("r46_funding", {}),
            self.get_funding_history(count=16), now, self.exchange, self.symbol)
        self.vars["r46_funding"] = registry
        times = self.vars.setdefault("r46_funding_times", [])
        counts = self._counts()
        counts["funding_reads"] += 1
        for event in fresh:
            assert event["effective_at"] < self.FINISH
            times.append(event["effective_at"])
            counts["funding_new"] += 1
            seed = event["effective_at"] < self.START
            counts["funding_seed" if seed else "funding_core"] += 1
            self._log("R46_FUND_EVENT", dict(observed_at=now, seed_pre_start=seed, **event))
        self.vars["r46_funding_read_at"] = now
        assert times and times == list(registry), "R46_REGISTRY_INDEX"

    def _resolve_node(self, node, exit_time, exit_price, reason):
        assert node["exit_time"] is None
        assert node["time"] < exit_time <= node["target"]
        node["exit_time"], node["exit_price"], node["exit_kind"] = exit_time, exit_price, reason

    def _close_shadow(self, shadow, exit_time, exit_price, reason, m1=None):
        bank = self.vars["r46_bank"][shadow["origin"]]
        assert shadow["side"] not in bank["closed_sides"]
        bank["closed_sides"].add(shadow["side"])
        counts = self._counts()
        counts["shadow_stops" if reason == "STOP" else "shadow_deadlines"] += 1
        if shadow["reviews"] == 0:
            counts["zero_review_shadows"] += 1
        payload = dict(shadow_id=shadow["id"], origin=shadow["origin"],
            side=shadow["side"], entry=shadow["entry"], D=shadow["D"], stop=shadow["stop"],
            deadline=shadow["deadline"], exit_time=exit_time, exit_price=exit_price,
            reason=reason, reviews=shadow["reviews"])
        if m1 is not None:
            payload.update(minute_open=int(m1[0]), minute_end=int(m1[0])+MINUTE,
                           m1_ohlc=[float(v) for v in m1[:5]])
        self._log("R46_SHADOW_CLOSE", payload)
        del self.vars["r46_active"][shadow["id"]]

    def _stops(self, m1):
        for shadow in list(self.vars.setdefault("r46_active", {}).values()):
            exit_event = stop_event(shadow["side"], shadow["stop"], m1)
            if exit_event is None:
                continue
            node_id = shadow["active_node"]
            if node_id is not None:
                self._resolve_node(self.vars["r46_pending"][node_id],
                    exit_event["exit_time"], exit_event["exit_price"], "STOP")
            self._close_shadow(shadow, exit_event["exit_time"],
                               exit_event["exit_price"], "STOP", m1)

    def _score(self, node):
        if node["pred_control"] is None:
            return
        scores = self.vars.setdefault("r46_score_days", {})
        bucket = scores.setdefault(node["origin"], dict(n=0,
            mse_control_sum=0., mse_context_sum=0.,
            value_control_sum=0., value_context_sum=0.))
        bucket["n"] += 1
        bucket["mse_control_sum"] += (node["pred_control"]-node["delta"])**2
        bucket["mse_context_sum"] += (node["pred_context"]-node["delta"])**2
        bucket["value_control_sum"] += node["delta"]*int(node["pred_control"] > 0)
        bucket["value_context_sum"] += node["delta"]*int(node["pred_context"] > 0)
        self._counts()["mature_predicted_nodes"] += 1

    def _mature(self, now):
        pending = self.vars.setdefault("r46_pending", {})
        times = self.vars["r46_funding_times"]
        registry = self.vars["r46_funding"]
        for node_id, node in list(pending.items()):
            if node["ready"] > now:
                continue
            assert node["ready"] == now and node["exit_time"] is not None
            assert self.vars["r46_funding_read_at"] == now, "R46_LABEL_NO_BOUNDARY_READ"
            assert bisect.bisect_right(times, node["time"]) > 0, "R46_NO_PRIOR_FUND_EVENT"
            left = bisect.bisect_right(times, node["time"])
            right = bisect.bisect_right(times, node["exit_time"])
            events = [registry[key] for key in times[left:right]]
            value = label_value(node["side"], node["mark"], node["exit_price"],
                node["D"], float(self.fee_rate), events, node["time"],
                node["exit_time"], node["exit_kind"], self.FINISH)
            node.update(value)
            node["mature"] = True
            self._counts()["labels"] += 1
            self._score(node)
            self._log("R46_LABEL", dict(node_id=node_id, origin=node["origin"],
                side=node["side"], age=node["age"], node_time=node["time"],
                target=node["target"], ready=node["ready"], observed_at=now,
                exit_time=node["exit_time"], exit_price=node["exit_price"],
                exit_kind=node["exit_kind"], mark=node["mark"], D=node["D"], **value))
            del pending[node_id]

    def _release_bank(self, now):
        bank = self.vars.setdefault("r46_bank", {})
        for origin, episode in list(bank.items()):
            if episode["released"] or episode["release_at"] > now:
                continue
            assert episode["release_at"] == now
            if episode["valid"]:
                assert episode["closed_sides"] == {-1, 1}
                assert all(node["mature"] and node["ready"] <= now for node in episode["nodes"])
                self._counts()["released_valid_days"] += 1
                self._counts()["released_nodes"] += len(episode["nodes"])
                if not episode["nodes"]:
                    self._counts()["zero_node_origin_days"] += 1
            episode["released"] = True
            self._counts()["released_days"] += 1
            self._log("R46_BANK", dict(origin=origin, release_at=now,
                valid=episode["valid"], reason=episode["reason"],
                shadow_count=2 if episode["valid"] else 0, nodes=len(episode["nodes"])))
        latest = ((now-2*DAY-MINUTE)//DAY)*DAY
        earliest = latest-179*DAY
        for origin in list(bank):
            if origin < earliest and bank[origin]["released"]:
                del bank[origin]

    def _fit(self, now):
        month = datetime.fromtimestamp(now/1000, timezone.utc).strftime("%Y-%m")
        if month == self.vars.get("r46_fit_month"):
            return
        self.vars["r46_fit_month"] = month
        fit_id = month+"_"+str(now)
        self.vars["r46_fit_id"] = fit_id
        self.vars["r46_fit"] = None
        self._counts()["fit_attempts"] += 1
        fitted, reason = fit_window(self.vars.setdefault("r46_bank", {}), now)
        if fitted is None:
            self._counts()["fit_invalid"] += 1
            self._log("R46_FIT", dict(kind="status", time=now, fit_id=fit_id,
                valid=False, reason=reason))
            return
        self.vars["r46_fit"] = fitted
        self._counts()["fit_valid"] += 1
        self._log("R46_FIT", dict(kind="status", time=now, fit_id=fit_id,
            valid=True, first_origin=fitted["day_ids"][0], last_origin=fitted["day_ids"][-1],
            origin_days=180, origin_episodes=360, N=fitted["control"]["N"],
            age_counts=fitted["age_counts"], lambda_nonintercept=1))
        for offset in range(0, 180, 40):
            days = fitted["day_ids"][offset:offset+40]
            counts_by_day = dict(fitted["control"]["day_counts"])
            self._log("R46_FIT", dict(kind="train_days", fit_id=fit_id,
                offset=offset, N=180, days=days,
                node_counts=[counts_by_day.get(day, 0) for day in days]))
        for name in ("control", "context"):
            model = fitted[name]
            self._log("R46_FIT", dict(kind="scaler", fit_id=fit_id, model=name,
                columns=model["columns"], means=model["means"].tolist(),
                scales=model["scales"].tolist(), constant=model["constant"].tolist(),
                N=model["N"], weighted_days=model["days"], weights_sum=model["weights_sum"]))
            self._log("R46_FIT", dict(kind="beta", fit_id=fit_id, model=name,
                columns=model["columns"], beta=model["beta"].tolist()))

    def _horizon_and_deadline(self, now, price):
        for shadow in list(self.vars.setdefault("r46_active", {}).values()):
            node_id = shadow["active_node"]
            if node_id is not None:
                node = self.vars["r46_pending"][node_id]
                if node["target"] == now:
                    reason = "deadline" if now == shadow["deadline"] else "horizon"
                    self._resolve_node(node, now, price, reason)
                    shadow["active_node"] = None
            if now >= shadow["deadline"]:
                assert now == shadow["deadline"]
                self._close_shadow(shadow, now, price, "deadline")

    def _origin(self, now, price):
        assert now % DAY == 0 and self.START < now < self.FINISH
        bank = self.vars.setdefault("r46_bank", {})
        assert now not in bank
        self._counts()["origins"] += 1
        rows = closed_window(self.get_candles(self.exchange, self.symbol, "4h"), now, 15)
        reason, D, atr = None, None, None
        if rows is None:
            reason = "origin_4h_window_invalid"
        elif not math.isclose(float(rows[-1, 2]), price, rel_tol=1e-10, abs_tol=1e-8):
            reason = "origin_4h_price_asof"
        else:
            atr = atr14(rows)
            if atr is None:
                reason = "origin_atr_invalid"
            else:
                D = 2*atr
                if not all(math.isfinite(v) and v > 0 for v in (D, price-D, price+D)):
                    reason = "origin_pair_stop_geometry"
                    D = D if math.isfinite(D) else None
        valid = reason is None
        bank[now] = dict(origin=now, valid=valid, reason=reason, released=False,
                         release_at=now+2*DAY+MINUTE, nodes=[], closed_sides=set())
        self._counts()["valid_origins" if valid else "invalid_origins"] += 1
        self._log("R46_ORIGIN", dict(kind="header", origin=now, valid=valid,
            reason=reason, entry=price, atr=atr, D=D, release_at=now+2*DAY+MINUTE,
            deadline=now+2*DAY, long_stop=price-D if valid else None,
            short_stop=price+D if valid else None))
        if rows is not None:
            for offset in range(0, 15, 5):
                self._log("R46_ORIGIN", dict(kind="atr_inputs", origin=now,
                    offset=offset, N=15, bars=rows[offset:offset+5, :5].astype(float).tolist()))
        if not valid:
            return
        for side in (1, -1):
            shadow_id = str(now)+":"+str(side)
            self.vars.setdefault("r46_active", {})[shadow_id] = dict(id=shadow_id,
                origin=now, side=side, entry=price, D=D, stop=price-side*D,
                deadline=now+2*DAY, previous_mark=price, bestR=0.,
                reviews=0, active_node=None)
            self._counts()["shadows"] += 1

    def _reviews(self, now, price):
        for shadow in self.vars.setdefault("r46_active", {}).values():
            elapsed = now-shadow["origin"]
            if elapsed <= 0:
                continue
            assert elapsed % BAR == 0
            age = elapsed//BAR
            assert 1 <= age <= 11 and shadow["active_node"] is None
            previous_mark, previous_best = shadow["previous_mark"], shadow["bestR"]
            features = review_features(shadow["side"], shadow["entry"], shadow["D"],
                previous_mark, previous_best, price, int(age))
            shadow["previous_mark"], shadow["bestR"] = price, features["bestR"]
            shadow["reviews"] += 1
            node_id = shadow["id"]+":"+str(age)
            fitted = self.vars.get("r46_fit")
            pred_control = predict(fitted["control"], features) if fitted is not None else None
            pred_context = predict(fitted["context"], features) if fitted is not None else None
            node = dict(node_id=node_id, origin=shadow["origin"], time=now,
                target=now+BAR, ready=now+BAR+MINUTE, entry=shadow["entry"],
                D=shadow["D"], stop=shadow["stop"], mark=price,
                previous_mark=previous_mark, bestR_before=previous_best,
                fit_id=self.vars.get("r46_fit_id"), pred_control=pred_control,
                pred_context=pred_context, exit_time=None, exit_price=None,
                exit_kind=None, mature=False, delta=None, **features)
            self.vars.setdefault("r46_pending", {})[node_id] = node
            self.vars["r46_bank"][shadow["origin"]]["nodes"].append(node)
            shadow["active_node"] = node_id
            counts = self._counts()
            counts["nodes"] += 1
            counts["predicted_nodes" if fitted is not None else "unpredicted_nodes"] += 1
            payload = dict(node)
            payload.pop("delta")
            self._log("R46_NODE", payload)

    def before(self):
        now = int(self.time)
        assert self.START < now <= self.FINISH, "R46_M1_OUTSIDE_WINDOW"
        if not self.vars.get("r46_checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "1m"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["r46_checked"] = True
        previous = self.vars.get("r46_last_minute", self.START)
        assert now == previous+MINUTE, "R46_M1_GAP_OR_DUPLICATE"
        m1 = np.asarray(self.current_candle)
        assert m1.ndim == 1 and len(m1) >= 5
        assert all(math.isfinite(float(v)) for v in m1[:5])
        assert float(m1[0]) == now-MINUTE and now % MINUTE == 0
        assert int(self.closed_candle_open_time) == now-MINUTE
        opening, price, high, low = map(float, m1[1:5])
        assert min(opening, price, high, low) > 0
        assert high >= max(opening, price) and low <= min(opening, price)
        assert math.isclose(price, float(self.price), rel_tol=1e-10, abs_tol=1e-8)
        self.vars["r46_last_minute"] = now
        self._counts()["minutes"] += 1
        # Last-minute STOP is observable at FINISH; no later decision is permitted.
        self._stops(m1)
        if now == self.FINISH:
            return
        if now == self.START+MINUTE or now % BAR == MINUTE:
            self._ingest_funding(now)
            self._mature(now)
            self._release_bank(now)
        if now % BAR:
            return
        self._fit(now)
        # Funding at this boundary belongs to later labels, published at now+1m.
        self._horizon_and_deadline(now, price)
        if now % DAY == 0:
            self._origin(now, price)
        self._reviews(now, price)

    def _finalize(self):
        if self.vars.get("r46_finalized"):
            return
        assert self.vars.get("r46_last_minute") == self.FINISH, "R46_INCOMPLETE_M1"
        self.vars["r46_finalized"] = True
        counts = self._counts()
        partial = set()
        for node in self.vars.get("r46_pending", {}).values():
            counts["censored_nodes"] += 1
            partial.add(node["origin"])
            self._log("R46_CENSORED", dict(kind="node", node_id=node["node_id"],
                origin=node["origin"], time=node["time"], target=node["target"],
                ready=node["ready"], exit_time=node["exit_time"],
                exit_price=node["exit_price"], reason="finish_before_label_ready"))
        for shadow in self.vars.get("r46_active", {}).values():
            counts["censored_shadows"] += 1
            partial.add(shadow["origin"])
            self._log("R46_CENSORED", dict(kind="shadow", shadow_id=shadow["id"],
                origin=shadow["origin"], side=shadow["side"], deadline=shadow["deadline"],
                reason="alive_at_finish"))
        for origin, episode in self.vars.get("r46_bank", {}).items():
            if not episode["released"]:
                partial.add(origin)
                counts["censored_origin_days"] += 1
                self._log("R46_CENSORED", dict(kind="origin", origin=origin,
                    valid=episode["valid"], release_at=episode["release_at"],
                    reason="finish_before_origin_release"))
        wallet, qty = float(self.balance), float(self.position.qty)
        assert math.isclose(wallet, 10000., rel_tol=0., abs_tol=1e-6)
        assert qty == 0. and len(self.entry_orders) == 0
        assert counts["origins"] == (self.FINISH-self.START)//DAY-1
        assert counts["nodes"] == counts["labels"]+counts["censored_nodes"]
        assert counts["shadows"] == counts["shadow_stops"]+counts["shadow_deadlines"]+counts["censored_shadows"]
        self._log("R46_SUMMARY", dict(kind="counts", wallet=wallet,
            position_qty=qty, entry_orders=len(self.entry_orders), **counts))
        score_days = self.vars.get("r46_score_days", {})
        for cohort in ("all", "2021", "2022", "2023", "2024", "2025"):
            selected = [(origin, row) for origin, row in score_days.items()
                if cohort == "all" or datetime.fromtimestamp(origin/1000, timezone.utc).strftime("%Y") == cohort]
            N, days = sum(row["n"] for _, row in selected), len(selected)
            payload = dict(kind="scores", cohort=cohort, node_N=N, origin_days=days,
                partial_origin_days=sum(origin in partial for origin, _ in selected))
            for metric in ("mse_control", "mse_context", "value_control", "value_context"):
                payload["node_"+metric] = sum(row[metric+"_sum"] for _, row in selected)/N if N else None
                payload["day_"+metric] = sum(row[metric+"_sum"]/row["n"] for _, row in selected)/days if days else None
            payload["node_advantage"] = (payload["node_value_context"]-payload["node_value_control"]) if N else None
            payload["day_advantage"] = (payload["day_value_context"]-payload["day_value_control"]) if days else None
            self._log("R46_SUMMARY", payload)
        for origin, row in sorted(score_days.items()):
            self._log("R46_DAY_SCORE", dict(origin=origin, partial=origin in partial, **row))

    def before_terminate(self):
        self._finalize()
```
