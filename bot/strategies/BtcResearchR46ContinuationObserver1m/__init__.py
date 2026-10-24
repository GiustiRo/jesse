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
