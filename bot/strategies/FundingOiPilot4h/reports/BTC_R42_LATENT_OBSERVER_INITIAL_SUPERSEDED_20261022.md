# R42 observer — primera fuente supersedida antes de checks

SHA256 4619be17fbde234c2de2d425d99c8ad8ff49db03df53c1b0b628869c8af3b6af. Root solicitó añadir comprobación explícita de wallet/posición/entry_orders al resumen de un observador sin órdenes. Se preserva esta primera versión; no hubo jobs o motores con ella. Math permanece intacta.

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
        self.vars["r42_summary_emitted"] = True
        self._log("R42_SUMMARY", dict(stage="FINAL", kind="counts", **self._counts()))
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
