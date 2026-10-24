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
