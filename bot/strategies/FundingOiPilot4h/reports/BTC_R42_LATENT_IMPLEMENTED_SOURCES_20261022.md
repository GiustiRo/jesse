# R42 — implementación del observador latente, sin ejecución

Fecha: 2026-10-22. Protocolo BTC_R42_LATENT_PERSISTENCE_PROTOCOL_20261022.md leído completo; también recurso jesse://strategy (reloj de velas cerradas/asof). Sólo dos fuentes nuevas creadas por MCP, ambas con readback exacto completo. No se modificaron padres, framework, configuración o dependencias. Cero jobs, análisis, drafts o motores de esta subtarea. No se observaron precios reales ni se consultó cobertura.

## Diseño e interfaces

BtcResearchR42LatentMath contiene las funciones puras y una clase Strategy sin órdenes para poder crearse/importarse mediante el catálogo. BtcResearchR42LatentObserver4h hereda Strategy directamente y devuelve False en ambas admisiones; go_long/go_short fallan explícitamente si se llaman por error. No ejecuta broker, gestión o contabilidad virtuales.

Funciones públicas:
- closed_bars(candles,now,count): slice cerrado4h validado o None; supone timestamps ordenados del motor, valida sólo la porción usada.
- fit_emissions(returns): exactamente360 retornos -> (model,reason); 30 EM, cuantiles25/75, varianza mínima1e-6 en z, ocupaciones finales recalculadas>=10, retorno a unidades originales y orden mu/var.
- transition_matrix(w,rho): convención de posterior fila q@P. Distribución estacionaria w compartida.
- emission_logpdf(values,model): matriz N×2 en unidades originales.
- forward_filter(loge,w,rho): (secuencia posterior filtrada,loglik), inicio w.
- transition_counts(loge,w,rho): (C2×2,loglik), 359 transiciones para360 retornos; backward sólo sobre entrenamiento pasado.
- rho_m_step(C,w): endpoints o40 bisecciones, rango[0,1−1e-6].
- fit_persistence(returns,model): (fit,reason), 20 EM desde.5 y nuevo filtrado final del prefijo para q.
- assimilate(q,value,model,rho): una sola nueva observación cerrada.
- forecast_paths(q,model,rho,horizon=6): mean,p_positive,path_count64, peso inicial qP y cinco transiciones. No aproxima la mezcla por una normal.
- density_log(value,weights,model): logdensidad exacta de mezcla de un paso.

Errores numéricos capturados explícitamente: FloatingPointError/OverflowError. Los fallos de programación/contrato no se silencian con except general. No clipping de señal/rho posterior, reinicios de ajuste ni reajustes dentro del mes. La cota de rho y el piso de varianza son exactamente los registrados.

## Reloj y conservación

Primer callback observado de cada mes intenta ajuste una sola vez; una ventana362 inválida o un fallo numérico deja el modelo indisponible hasta el próximo mes. Los360 retornos entrenan hasta T−BAR; el retorno actual T se asimila después del ajuste. Parámetros/model_id y posterior tienen timestamps separados.

Al entrar un nuevo mes, sólo cambia el modelo para futuras predicciones. Pending6 y pending1 conservan sus números y emisiones originales; el paso de madurez ocurre antes del nuevo ajuste. Fallo de modelo conserva pendientes. Sólo invalidez OHLC/asof o salto del camino censura pendientes con razón explícita. Callbacks repetidos/anteriores son no-op.

El horizonte6 usa precio de origen y target exacto; igualdad y=0 es no positivo. Cohortes año se asignan por año UTC del origen, no de su madurez. pending1 conserva pesos exactos y referencia a emisiones que nunca se mutan; ningún score vuelve a estimar el forecast.

FINISH sólo admite madurar con un cierre válido expuesto por el motor, nunca crear un origen ni ajustar enero2026. before_terminate llama before con su latch para admitir ese cierre si es fresco; si no hay callback/cierre observable, los remanentes quedan censurados con terminal_unobserved_target. No se fabrica un precio final. Censura y resumen son idempotentes. Root deberá verificar el reloj nativo efectivo en su check/auditoría.

## Logs acotados y auditoría

El escritor usa JSON estricto y assert de longitud total<1800 caracteres; nunca trunca evidencia:
- R42_TRAIN: cada ventana mensual válida se exporta antes del ajuste,360 retornos en nueve chunks de40, con offset/N, model_id y extremos de entrenamiento.
- R42_FIT: parámetros comunes w/mu/var/ocupaciones/escala, rho, q_train/q_iid_train, likelihoods y clocks; o razón de invalidez.
- R42_PRED: precio/previous_price/return_current, q/q_iid/q_at, rho/model_id/parameter_at/train clocks, medias y p_positivo de ambos, pesos1 exactos y targets1/6.
- R42_SCORE: origin/target/model_id, precios, y, signo y scores/diferencias congelados, cohorte00UTC/año.
- R42_DENSITY: label de un paso y logdensidades de ambos, o invalidez numérica explícita.
- R42_CENSORED/R42_INVALID: horizonte/reloj/razón y alcance camino/modelo.
- R42_SUMMARY: contadores, wallet/position_qty/entry_orders (con asserts de invariantes de observador), sumas/counts por all4h,utc00,2021..2025, y densidad por separado. Root aplica el gate numérico registrado; fuente no selecciona por resultados.

No se afirma que los límites de longitud, fórmulas o ausencia de órdenes hayan pasado un harness: la subtarea sólo escribe/readback; los checks pertenecen a root. Tampoco se acredita convergencia global, identificabilidad económica de regímenes, potencia, OOS o rentabilidad.

## Hashes y fuentes completas

Protocolo leído en este momento SHA256: 9f44e921772f06e1ab95b95b13b1e10fe0d071d66e1cd3cb99b45bcf12f12363.
BtcResearchR42LatentMath: 1e601b4831115923bbfc9f05870b3afd312cf347c08a9ee335acaded3473f142; 9934 caracteres; readback exacto.
BtcResearchR42LatentObserver4h: c9ba8a41111ade0348e3a4e829cf4a7afe5a08a61fa12fdcd3480720ebdc88e1; 14423 caracteres; readback exacto.

Ambas fuentes fueron creadas en un intento, sin errores de herramientas. Antes de checks, root pidió añadir a SUMMARY wallet, position_qty y entry_orders, con asserts de wallet10.000/posición0/sin entradas; se realizó sólo ese cambio de código en Observer. La primera fuente Observer está preservada íntegra en BTC_R42_LATENT_OBSERVER_INITIAL_SUPERSEDED_20261022.md. Math permanece idéntica. La validación sintáctica de create_strategy no sustituye la revisión ni el check suministrado.

### BtcResearchR42LatentMath

```python
import itertools
import math
import numpy as np
from jesse.strategies import Strategy

BAR = 14400000
RHO_MAX = 1.0 - 1e-6


def closed_bars(candles, now, count):
    """Validate only the requested closed 4h slice; never repair a gap."""
    rows = np.asarray(candles)
    if rows.ndim != 2 or rows.shape[1] < 5 or len(rows) < count:
        return None
    end = int(np.searchsorted(rows[:, 0], now - BAR, side="right"))
    tail = rows[max(0, end-count):end]
    if len(tail) != count or tail[-1, 0] != now-BAR:
        return None
    if not np.all(np.isfinite(tail[:, :5])) or np.any(tail[:, 1:5] <= 0):
        return None
    if not np.all(np.diff(tail[:, 0]) == BAR):
        return None
    if np.any(tail[:, 3] < np.maximum(tail[:, 1], tail[:, 2])):
        return None
    if np.any(tail[:, 4] > np.minimum(tail[:, 1], tail[:, 2])):
        return None
    return tail


def _finite(values):
    if not np.all(np.isfinite(values)):
        raise FloatingPointError("nonfinite numerical result")


def _logsumexp(values, axis=None):
    maximum = np.max(values, axis=axis, keepdims=True)
    _finite(maximum)
    result = maximum + np.log(np.sum(np.exp(values-maximum), axis=axis, keepdims=True))
    return np.squeeze(result, axis=axis)


def _gaussian_logpdf(values, mu, var):
    return -.5 * (math.log(2*math.pi) + np.log(var)
                  + (np.asarray(values, dtype=float)[:, None]-mu)**2 / var)


def fit_emissions(returns):
    """Exactly 360 returns, 30 EM updates; returns (frozen model, reason).

    model arrays w/mu/var are in original return units, sorted by mu then var.
    The 1e-6 z-variance floor is numerical regularization fixed by protocol.
    Occupancy is recomputed using the final parameters, not the last old E-step.
    """
    x = np.asarray(returns, dtype=float)
    if x.shape != (360,) or not np.all(np.isfinite(x)):
        return None, "training_shape_or_nonfinite"
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
            center, scale = float(np.mean(x)), float(np.std(x, ddof=0))
            if not math.isfinite(scale) or scale <= 0:
                return None, "training_std_degenerate"
            z = (x-center)/scale
            mu = np.asarray(np.quantile(z, [.25, .75]), dtype=float)
            if mu[0] == mu[1]:
                return None, "equal_initial_quantiles"
            var, w = np.ones(2), np.full(2, .5)
            for _ in range(30):
                logs = _gaussian_logpdf(z, mu, var) + np.log(w)
                normalizer = _logsumexp(logs, axis=1)
                gamma = np.exp(logs-normalizer[:, None])
                mass = np.sum(gamma, axis=0)
                if np.any(mass <= 0):
                    return None, "empty_em_component"
                w = mass/len(z)
                mu = np.sum(gamma*z[:, None], axis=0)/mass
                var = np.maximum(np.sum(gamma*(z[:, None]-mu)**2, axis=0)/mass, 1e-6)
                _finite(np.concatenate((w, mu, var)))
            logs = _gaussian_logpdf(z, mu, var) + np.log(w)
            normalizer = _logsumexp(logs, axis=1)
            occupancy = np.sum(np.exp(logs-normalizer[:, None]), axis=0)
            if np.any(occupancy < 10):
                return None, "final_occupancy_below_10"
            original_mu = center + scale*mu
            original_var = scale**2*var
            _finite(np.concatenate((original_mu, original_var, w, occupancy)))
            if np.any(original_var <= 0):
                return None, "original_variance_degenerate"
            order = np.lexsort((original_var, original_mu))
            model = dict(w=w[order].copy(), mu=original_mu[order].copy(),
                         var=original_var[order].copy(), occupancy=occupancy[order].copy(),
                         center=center, scale=scale, em_iterations=30,
                         iid_train_loglik=float(np.sum(normalizer)-len(z)*math.log(scale)))
            _finite(model["iid_train_loglik"])
            return model, None
    except (FloatingPointError, OverflowError):
        return None, "em_numerical_failure"


def transition_matrix(w, rho):
    """Row-vector convention: q_next_prior=q@P; w@P=w for every allowed rho."""
    weights = np.asarray(w, dtype=float)
    assert weights.shape == (2,) and np.all(weights > 0)
    assert math.isclose(float(weights.sum()), 1., rel_tol=1e-10, abs_tol=1e-12)
    assert math.isfinite(rho) and 0 <= rho <= RHO_MAX
    return rho*np.eye(2)+(1-rho)*np.tile(weights, (2, 1))


def emission_logpdf(values, model):
    """N observations x two states, using frozen original-unit Gaussian emissions."""
    result = _gaussian_logpdf(np.asarray(values, dtype=float), model["mu"], model["var"])
    _finite(result)
    return result


def _forward_scaled(loge, w, rho):
    P = transition_matrix(w, rho)
    loge = np.asarray(loge, dtype=float)
    assert loge.ndim == 2 and loge.shape[1] == 2 and len(loge) > 0
    _finite(loge)
    offset = np.max(loge, axis=1)
    relative = np.exp(loge-offset[:, None])
    alpha = np.empty_like(loge)
    scales = np.empty(len(loge))
    for t in range(len(loge)):
        prior = np.asarray(w, dtype=float) if t == 0 else alpha[t-1]@P
        raw = prior*relative[t]
        scales[t] = float(np.sum(raw))
        if not math.isfinite(scales[t]) or scales[t] <= 0:
            raise FloatingPointError("forward scale invalid")
        alpha[t] = raw/scales[t]
    loglik = float(np.sum(np.log(scales)+offset))
    _finite(alpha)
    _finite(loglik)
    return alpha, relative, scales, loglik


def forward_filter(loge, w, rho):
    """Training only: initial state w, no smoothed state exposed for old forecasts."""
    alpha, _, _, loglik = _forward_scaled(loge, w, rho)
    return alpha, loglik


def transition_counts(loge, w, rho):
    """Forward/backward on a past prefix; 360 returns give 359 xi transitions."""
    alpha, relative, scales, loglik = _forward_scaled(loge, w, rho)
    P = transition_matrix(w, rho)
    beta = np.ones_like(alpha)
    for t in range(len(alpha)-2, -1, -1):
        beta[t] = P@(relative[t+1]*beta[t+1])/scales[t+1]
    C = np.zeros((2, 2))
    for t in range(len(alpha)-1):
        xi = (alpha[t, :, None]*P
              *(relative[t+1]*beta[t+1])[None, :]/scales[t+1])
        C += xi
    _finite(C)
    return C, loglik


def rho_m_step(C, w):
    """Concave transition objective: endpoints or exactly 40 bisection steps."""
    C, w = np.asarray(C, dtype=float), np.asarray(w, dtype=float)
    direction = np.eye(2)-np.tile(w, (2, 1))

    def derivative(rho):
        return float(np.sum(C*direction/transition_matrix(w, rho)))

    if derivative(0.) <= 0:
        return 0.
    if derivative(RHO_MAX) >= 0:
        return RHO_MAX
    low, high = 0., RHO_MAX
    for _ in range(40):
        middle = .5*(low+high)
        if derivative(middle) > 0:
            low = middle
        else:
            high = middle
    return .5*(low+high)


def fit_persistence(returns, model):
    """Fixed emissions, rho=.5 then exactly20 EM updates; final q refiltered."""
    x = np.asarray(returns, dtype=float)
    if x.shape != (360,) or not np.all(np.isfinite(x)):
        return None, "training_shape_or_nonfinite"
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
            loge = emission_logpdf(x, model)
            rho = .5
            for _ in range(20):
                C, _ = transition_counts(loge, model["w"], rho)
                rho = rho_m_step(C, model["w"])
            posterior, loglik = forward_filter(loge, model["w"], rho)
            return dict(rho=float(rho), q=posterior[-1].copy(),
                        loglik=loglik, em_iterations=20), None
    except (FloatingPointError, OverflowError):
        return None, "persistence_numerical_failure"


def assimilate(q, value, model, rho):
    """Single newly closed return; the caller supplies posterior known before it."""
    prior = np.asarray(q, dtype=float)@transition_matrix(model["w"], rho)
    logs = np.log(prior)+emission_logpdf([value], model)[0]
    posterior = np.exp(logs-_logsumexp(logs))
    _finite(posterior)
    return posterior


def forecast_paths(q, model, rho, horizon=6):
    """Exactly64 paths: qP for first future state, then five transitions.

    Gaussian emissions are conditionally independent along a state path.
    This is model marginalization, not a market-independence claim.
    """
    assert horizon == 6
    P = transition_matrix(model["w"], rho)
    first = np.asarray(q, dtype=float)@P
    mean, positive, mass = 0., 0., 0.
    for states in itertools.product((0, 1), repeat=horizon):
        weight = float(first[states[0]])
        for t in range(1, horizon):
            weight *= float(P[states[t-1], states[t]])
        location = sum(float(model["mu"][state]) for state in states)
        variance = sum(float(model["var"][state]) for state in states)
        probability = .5*(1+math.erf(location/math.sqrt(2*variance)))
        mean += weight*location
        positive += weight*probability
        mass += weight
    _finite((mean, positive, mass))
    assert math.isclose(mass, 1., rel_tol=1e-10, abs_tol=1e-12)
    return dict(mean=float(mean), p_positive=float(positive), path_count=64)


def density_log(value, weights, model):
    """Exact frozen two-Gaussian one-step log density, not a Gaussian shortcut."""
    answer = float(_logsumexp(np.log(np.asarray(weights, dtype=float))
                             +emission_logpdf([value], model)[0]))
    _finite(answer)
    return answer


class BtcResearchR42LatentMath(Strategy):
    """Importable helper container; never an economic strategy."""
    def should_long(self):
        return False

    def should_short(self):
        return False

    def go_long(self):
        raise AssertionError("R42 math has no orders")

    def go_short(self):
        raise AssertionError("R42 math has no orders")
```

### BtcResearchR42LatentObserver4h

```python
import json
import math
from datetime import datetime, timezone

import numpy as np
from jesse.strategies import Strategy
from strategies.BtcResearchR42LatentMath import (
    BAR, closed_bars, fit_emissions, fit_persistence, emission_logpdf,
    forward_filter, assimilate, forecast_paths, transition_matrix, density_log,
)

DAY = 86400000


class BtcResearchR42LatentObserver4h(Strategy):
    """Prequential model observer only: no trading, smoothed historical signals or PnL."""
    START = 1602720000000
    FINISH = 1767225600000

    def should_long(self):
        return False

    def should_short(self):
        return False

    def go_long(self):
        raise AssertionError("R42 observer has no orders")

    def go_short(self):
        raise AssertionError("R42 observer has no orders")

    def _log(self, label, payload):
        encoded = label + " " + json.dumps(payload, separators=(",", ":"), allow_nan=False)
        # Audit records are deliberately split instead of truncating their evidence.
        assert len(encoded) < 1800
        self.log(encoded)

    def _counts(self):
        return self.vars.setdefault("r42_counts", dict(
            callbacks=0, fit_attempts=0, fit_valid=0, fit_invalid=0,
            forecasts=0, unavailable_origins=0, scores=0, density_scores=0,
            censored_six=0, censored_one=0, invalid_paths=0, invalid_models=0,
            invalid_density=0))

    def _groups(self):
        return self.vars.setdefault("r42_groups", {
            key: dict(n=0, mse_p_sum=0., mse_i_sum=0., brier_p_sum=0., brier_i_sum=0.)
            for key in ("all4h", "utc00", "2021", "2022", "2023", "2024", "2025")})

    def _censor(self, reason):
        counts = self._counts()
        for horizon, key, counter in ((6, "r42_pending6", "censored_six"),
                                      (1, "r42_pending1", "censored_one")):
            for record in self.vars.get(key, []):
                counts[counter] += 1
                self._log("R42_CENSORED", dict(origin=record["origin"],
                    target=record["target"], model_id=record["model_id"],
                    horizon=horizon, reason=reason, observed_at=int(self.time)))
            self.vars[key] = []

    def _model_failure(self, reason):
        self.vars["r42_model"] = None
        self._counts()["invalid_models"] += 1
        self._log("R42_INVALID", dict(time=int(self.time), scope="model", reason=reason))
        # Valid old forecasts survive monthly/model failures unchanged.

    def _path_failure(self, reason):
        self.vars["r42_model"] = None
        self._counts()["invalid_paths"] += 1
        self._log("R42_INVALID", dict(time=int(self.time), scope="path", reason=reason))
        self._censor(reason)

    def _fit_failure(self, model_id, reason):
        self.vars["r42_model"] = None
        self._counts()["fit_invalid"] += 1
        self._log("R42_FIT", dict(time=int(self.time), model_id=model_id,
            status="invalid", reason=reason))

    def _fit(self, now, model_id):
        rows = closed_bars(self.candles, now, 362)
        if rows is None:
            self._fit_failure(model_id, "training_362_closed_bars_invalid")
            return
        values = np.diff(np.log(rows[:, 2]))
        train = values[:-1]
        train_start, train_finish = int(rows[0, 0])+BAR, int(rows[-2, 0])+BAR
        # These are consumed in the native observer, never an external input peek.
        for offset in range(0, 360, 40):
            self._log("R42_TRAIN", dict(model_id=model_id, time=now,
                offset=offset, N=360, train_start=train_start,
                train_finish=train_finish, returns=train[offset:offset+40].tolist()))
        model, reason = fit_emissions(train)
        if model is None:
            self._fit_failure(model_id, reason)
            return
        persistent, reason = fit_persistence(train, model)
        if persistent is None:
            self._fit_failure(model_id, reason)
            return
        try:
            with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
                iid_sequence, iid_loglik = forward_filter(
                    emission_logpdf(train, model), model["w"], 0.)
        except (FloatingPointError, OverflowError):
            self._fit_failure(model_id, "iid_filter_numerical_failure")
            return
        self.vars["r42_model"] = dict(emissions=model, rho=persistent["rho"],
            q=persistent["q"], q_iid=iid_sequence[-1].copy(), q_at=now-BAR,
            model_id=model_id, parameter_at=now,
            train_start=train_start, train_finish=train_finish)
        self._counts()["fit_valid"] += 1
        self._log("R42_FIT", dict(time=now, model_id=model_id, status="valid",
            train_start=train_start, train_finish=train_finish, train_N=360,
            q_train_at=now-BAR, w=model["w"].tolist(), mu=model["mu"].tolist(),
            var=model["var"].tolist(), occupancy=model["occupancy"].tolist(),
            center=model["center"], scale=model["scale"], mixture_iterations=30,
            persistence_iterations=20, rho=persistent["rho"],
            q_train=persistent["q"].tolist(), q_iid_train=iid_sequence[-1].tolist(),
            persistent_train_loglik=persistent["loglik"], iid_train_loglik=iid_loglik))

    def _mature(self, now, price):
        waiting = []
        for record in self.vars.get("r42_pending6", []):
            if record["target"] > now:
                waiting.append(record)
                continue
            assert record["target"] == now
            y = math.log(price)-math.log(record["price"])
            positive = int(y > 0)
            squared_p = (record["mean_p"]-y)**2
            squared_i = (record["mean_i"]-y)**2
            brier_p = (record["p_p"]-positive)**2
            brier_i = (record["p_i"]-positive)**2
            stamp = datetime.fromtimestamp(record["origin"]/1000, timezone.utc)
            cohorts = ["all4h"]
            if record["origin"] % DAY == 0:
                cohorts.append("utc00")
            if str(stamp.year) in self._groups():
                cohorts.append(str(stamp.year))
            for key in cohorts:
                group = self._groups()[key]
                group["n"] += 1
                group["mse_p_sum"] += squared_p
                group["mse_i_sum"] += squared_i
                group["brier_p_sum"] += brier_p
                group["brier_i_sum"] += brier_i
            self._counts()["scores"] += 1
            self._log("R42_SCORE", dict(origin=record["origin"], target=record["target"],
                time=now, model_id=record["model_id"], origin_price=record["price"],
                target_price=price, y=y, positive=positive,
                mse_p=squared_p, mse_i=squared_i, mse_delta=squared_p-squared_i,
                brier_p=brier_p, brier_i=brier_i, brier_delta=brier_p-brier_i,
                utc00=record["origin"] % DAY == 0, origin_year=stamp.year))
        self.vars["r42_pending6"] = waiting
        waiting = []
        for record in self.vars.get("r42_pending1", []):
            if record["target"] > now:
                waiting.append(record)
                continue
            assert record["target"] == now
            y = math.log(price)-math.log(record["price"])
            try:
                with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
                    log_p = density_log(y, record["weights_p"], record["emissions"])
                    log_i = density_log(y, record["weights_i"], record["emissions"])
            except (FloatingPointError, OverflowError):
                self._counts()["invalid_density"] += 1
                self._log("R42_DENSITY", dict(origin=record["origin"], target=now,
                    model_id=record["model_id"], y=y, status="numerical_invalid"))
                continue
            counts = self._counts()
            counts["density_scores"] += 1
            density = self.vars.setdefault("r42_density",
                                          dict(n=0, log_p_sum=0., log_i_sum=0.))
            density["n"] += 1
            density["log_p_sum"] += log_p
            density["log_i_sum"] += log_i
            self._log("R42_DENSITY", dict(origin=record["origin"], target=now,
                model_id=record["model_id"], y=y, status="valid",
                log_p=log_p, log_i=log_i, log_delta=log_p-log_i))
        self.vars["r42_pending1"] = waiting

    def _predict(self, now, price, previous_price):
        fit = self.vars.get("r42_model")
        if fit is None:
            self._counts()["unavailable_origins"] += 1
            return
        assert fit["q_at"] == now-BAR
        current = math.log(price)-math.log(previous_price)
        emissions = fit["emissions"]
        try:
            with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
                q = assimilate(fit["q"], current, emissions, fit["rho"])
                q_iid = assimilate(fit["q_iid"], current, emissions, 0.)
                prediction_p = forecast_paths(q, emissions, fit["rho"])
                prediction_i = forecast_paths(q_iid, emissions, 0.)
                weights_p = q@transition_matrix(emissions["w"], fit["rho"])
                weights_i = q_iid@transition_matrix(emissions["w"], 0.)
        except (FloatingPointError, OverflowError):
            self._model_failure("filter_or_forecast_numerical_failure")
            self._counts()["unavailable_origins"] += 1
            return
        fit["q"], fit["q_iid"], fit["q_at"] = q, q_iid, now
        six = dict(origin=now, target=now+6*BAR, price=price, model_id=fit["model_id"],
                   mean_p=prediction_p["mean"], mean_i=prediction_i["mean"],
                   p_p=prediction_p["p_positive"], p_i=prediction_i["p_positive"])
        one = dict(origin=now, target=now+BAR, price=price, model_id=fit["model_id"],
                   weights_p=weights_p.copy(), weights_i=weights_i.copy(),
                   emissions=emissions)
        self.vars.setdefault("r42_pending6", []).append(six)
        self.vars.setdefault("r42_pending1", []).append(one)
        self._counts()["forecasts"] += 1
        self._log("R42_PRED", dict(origin=now, target=now+6*BAR, density_target=now+BAR,
            model_id=fit["model_id"], parameter_at=fit["parameter_at"],
            train_start=fit["train_start"], train_finish=fit["train_finish"],
            q_at=now, price=price, previous_price=previous_price, return_current=current,
            q=q.tolist(), q_iid=q_iid.tolist(), rho=fit["rho"],
            mean_p=six["mean_p"], mean_i=six["mean_i"],
            p_p=six["p_p"], p_i=six["p_i"],
            weights1_p=weights_p.tolist(), weights1_i=weights_i.tolist(), paths=64))

    def before(self):
        now = int(self.time)
        if not self.START <= now <= self.FINISH:
            return
        previous_time = self.vars.get("r42_last_time")
        if previous_time is not None and now <= previous_time:
            return
        if not self.vars.get("r42_checked"):
            assert self.symbol == "BTC-USDT" and self.timeframe == "4h"
            assert self.leverage == 3 and abs(self.fee_rate-.00045) < 1e-12
            assert abs(self.balance-10000) < 1e-6
            self.vars["r42_checked"] = True
        self.vars["r42_last_time"] = now
        self._counts()["callbacks"] += 1
        month = datetime.fromtimestamp(now/1000, timezone.utc).strftime("%Y-%m")
        new_month = now < self.FINISH and month != self.vars.get("r42_month")
        model_id = month + "_" + str(now)
        if new_month:
            self.vars["r42_month"] = month
            self.vars["r42_model"] = None
            self._counts()["fit_attempts"] += 1
        rows = closed_bars(self.candles, now, 2)
        reason = None
        if now % BAR:
            reason = "callback_not_4h_boundary"
        elif rows is None:
            reason = "closed_ohlc_invalid"
        elif not math.isclose(float(rows[-1, 2]), float(self.price),
                              rel_tol=1e-10, abs_tol=1e-8):
            reason = "current_price_asof_mismatch"
        elif previous_time is not None and now != previous_time+BAR:
            reason = "callback_gap"
        if reason is not None:
            self._path_failure(reason)
            if new_month:
                self._fit_failure(model_id, reason)
            return
        price, previous_price = float(rows[-1, 2]), float(rows[-2, 2])
        # Old forecasts mature before a refit; no retrospective rewriting.
        self._mature(now, price)
        if now == self.FINISH:
            self._censor("target_after_finish")
            return
        if new_month:
            self._fit(now, model_id)
        self._predict(now, price, previous_price)

    def _summary(self):
        if self.vars.get("r42_summary_emitted"):
            return
        wallet = float(self.balance)
        position_qty = float(self.position.qty)
        entry_orders = len(self.entry_orders)
        assert math.isclose(wallet, 10000., rel_tol=0., abs_tol=1e-6)
        assert position_qty == 0. and entry_orders == 0
        self.vars["r42_summary_emitted"] = True
        self._log("R42_SUMMARY", dict(stage="FINAL", kind="counts",
            wallet=wallet, position_qty=position_qty, entry_orders=entry_orders,
            **self._counts()))
        for key, group in self._groups().items():
            n = group["n"]
            payload = dict(stage="FINAL", kind="scores", cohort=key, **group)
            for name in ("mse_p", "mse_i", "brier_p", "brier_i"):
                payload[name] = group[name+"_sum"]/n if n else None
            payload["mse_delta"] = payload["mse_p"]-payload["mse_i"] if n else None
            payload["brier_delta"] = payload["brier_p"]-payload["brier_i"] if n else None
            # Root applies the fixed strict-improvement numerical gate to these sums.
            self._log("R42_SUMMARY", payload)
        self._log("R42_SUMMARY", dict(stage="FINAL", kind="density",
            **self.vars.get("r42_density", dict(n=0, log_p_sum=0., log_i_sum=0.))))

    def before_terminate(self):
        # If the native engine exposes a fresh closed FINISH bar here, process it.
        # The time latch prevents duplicate assimilation/scoring of a prior callback.
        self.before()
        self._censor("terminal_unobserved_target")
        self._summary()
```
