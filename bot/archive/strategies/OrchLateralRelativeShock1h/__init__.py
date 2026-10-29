import math
import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta

HOUR = 60 * 60 * 1000
SYMBOLS = ('BTC-USDT', 'ETH-USDT')
BASE_FEE = 0.00045
SLIPPAGE_RESERVE = 0.001  # Sizing buffer, never a claimed fill-cost model.
BASKET_RISK = 0.01
LEG_RISK = 0.005
GROSS_CAP = 4.4


class OrchLateralRelativeShock1h(Strategy):
    """Two sequential MARKET legs fading a confirmed relative-return shock.

    Shared state is a coordination protocol, not atomic exchange execution.
    Emergency stops can leave one leg until its next strategy execution.
    This is an isolated research basket, not an integration with the reference.
    """

    def _book(self):
        return self.shared_vars.setdefault('orch_relative_shock', {
            'phase': 'flat', 'plan': None, 'last_exit': -1,
            'baskets': 0, 'aborts': 0, 'orphan_hours': 0})

    def _strategies(self):
        selected = {r.symbol: r.strategy for r in self.routes
                    if r.exchange == self.exchange}
        # A new deployment with additional routes needs its own coordinated
        # allocator; silently mixing this prototype into a portfolio is forbidden.
        assert set(selected) == set(SYMBOLS), 'PAIR_REQUIRES_EXACTLY_BTC_ETH'
        assert all(s.timeframe == '1h' for s in selected.values())
        return selected

    def _histories(self):
        result = {}
        for symbol in SYMBOLS:
            c = self.get_candles(self.exchange, symbol, '1h')
            if len(c) < 100:
                return None
            # Skip rather than invent synchronized history or use a stale quote.
            c = c[-100:]
            if int(c[-1, 0]) != int(self.closed_candle_open_time):
                return None
            assert np.all(c[:, 0] <= self.closed_candle_open_time), 'PAIR_FUTURE_BAR'
            if not np.all(np.diff(c[:, 0]) == HOUR):
                return None
            result[symbol] = c
        assert np.array_equal(result[SYMBOLS[0]][:, 0], result[SYMBOLS[1]][:, 0])
        return result

    def _new_plan(self, history):
        b, e = (history[s] for s in SYMBOLS)
        rb, re = np.diff(np.log(b[:, 2])), np.diff(np.log(e[:, 2]))
        # Fit uses 96 hourly returns strictly before the two shock hours plus
        # the latest confirmation hour. No signal bar enters its own baseline.
        x, y = re[:-3], rb[:-3]
        assert len(x) == 96 and len(y) == 96
        variance = float(np.mean((x - x.mean()) ** 2))
        if not math.isfinite(variance) or variance <= 0:
            return None
        beta = float(np.mean((x - x.mean()) * (y - y.mean())) / variance)
        alpha = float(y.mean() - beta * x.mean())
        sigma = float(np.std(y - alpha - beta * x, ddof=1))
        # Reject unstable/sign-inverted hedge estimates instead of clipping them.
        if not (0.25 <= beta <= 4 and math.isfinite(sigma) and sigma > 1e-8):
            return None
        residual = rb[-3:] - alpha - beta * re[-3:]
        shock, confirmation = float(residual[:2].sum()), float(residual[-1])
        remaining = shock + confirmation
        shock_scale = sigma * math.sqrt(2)
        if not (abs(shock) >= 2 * shock_scale
                and shock * confirmation < 0 and shock * remaining > 0):
            return None
        sign = 1 if shock > 0 else -1
        sides = {SYMBOLS[0]: -sign, SYMBOLS[1]: sign}
        prices = {s: float(history[s][-1, 2]) for s in SYMBOLS}
        # Emergency stops use ATR known before any of the three signal hours.
        distances = {s: 3 * float(ta.atr(history[s][:-3])) for s in SYMBOLS}
        if not all(math.isfinite(distances[s]) and 0 < distances[s] < prices[s]
                   for s in SYMBOLS):
            return None
        capital = max(0.0, min(float(self.balance), float(self.portfolio_value)))
        if capital <= 0:
            return None
        # Expected log-spread recovery is only an eligibility approximation.
        # Demand two complete two-leg round trips at BASE fees, kept fixed in
        # cost stress. Realized cash PnL can differ from this approximation.
        if abs(remaining) < 4 * BASE_FEE * (1 + beta):
            return None
        risk_fraction = {
            s: distances[s] / prices[s]
            + self.fee_rate * (2 + distances[s] / prices[s])
            + SLIPPAGE_RESERVE for s in SYMBOLS}
        rb_frac, re_frac = (risk_fraction[s] for s in SYMBOLS)
        free_margin = max(0.0, float(self.available_margin))
        # Compute both legs before arming either: beta links their notionals,
        # while per-leg and basket risk caps independently constrain scale.
        btc_notional = min(
            capital * LEG_RISK / rb_frac,
            capital * LEG_RISK / (beta * re_frac),
            capital * BASKET_RISK / (rb_frac + beta * re_frac),
            capital * GROSS_CAP / (1 + beta),
            free_margin * 0.90 / ((1 + beta) * (1 / self.leverage + self.fee_rate)))
        notionals = {SYMBOLS[0]: btc_notional, SYMBOLS[1]: beta * btc_notional}
        # Historical research precision; native venue minimums are unverified.
        qty = {s: math.floor(notionals[s] / prices[s] / 0.001) * 0.001 for s in SYMBOLS}
        if min(qty.values()) <= 0:
            return None
        notionals = {s: qty[s] * prices[s] for s in SYMBOLS}
        risks = {s: notionals[s] * risk_fraction[s] for s in SYMBOLS}
        gross = sum(notionals.values())
        margin = gross * (1 / self.leverage + self.fee_rate)
        assert max(risks.values()) <= capital * LEG_RISK + 1e-8
        assert sum(risks.values()) <= capital * BASKET_RISK + 1e-8
        assert sum(risks.values()) <= capital * 0.08 + 1e-8
        assert gross <= capital * GROSS_CAP + 1e-8
        assert margin <= free_margin * 0.90 + 1e-8
        # Rounding only reduces each leg. Bound deviation by their maximum lot
        # losses, not an arbitrary percentage that fails with small quantities.
        hedge_error = abs(notionals[SYMBOLS[1]] - beta * notionals[SYMBOLS[0]])
        assert hedge_error <= 0.001 * (prices[SYMBOLS[1]] + beta * prices[SYMBOLS[0]]) + 1e-8
        return dict(time=int(self.time), prices=prices, qty=qty, distances=distances,
                    sides=sides, risks=risks, margin=margin, gross=gross,
                    beta=beta, alpha=alpha, sigma=sigma, shock_scale=shock_scale,
                    sign=sign, remaining=remaining,
                    refs={s: float(history[s][-4, 2]) for s in SYMBOLS},
                    ref_time=int(b[-4, 0]) + HOUR,
                    queued=set(), filled={}, closed=set(), exit_reason=None)

    def _request_exit(self, reason):
        book = self._book()
        plan = book['plan']
        if plan is not None and plan['exit_reason'] is None:
            if reason in ('missing_or_closed_leg', 'leader_not_queued',
                          'entry_clock_or_price_mismatch', 'fill_mismatch',
                          'unexpected_pending_market_order'):
                book['aborts'] += 1
            plan['exit_reason'] = reason
            book['phase'] = 'exiting'
            self.log('ORCH_PAIR_EXIT reason=' + reason + ' basket=' + str(plan['time']))

    def before(self):
        assert self.is_futures_trading and self.leverage == 5
        strategies = self._strategies()
        book = self._book()
        plan = book['plan']
        if plan is not None and book['phase'] != 'flat':
            if self.time > plan['time']:
                opened = {s for s in SYMBOLS if strategies[s].is_open}
                if len(plan['filled']) != 2 or len(opened) != 2:
                    if opened:
                        if self.symbol == SYMBOLS[0]:
                            book['orphan_hours'] += 1
                        self._request_exit('missing_or_closed_leg')
                    else:
                        book['phase'] = 'flat'
                        book['last_exit'] = int(self.time)
                        book['plan'] = None
            return
        # BTC is the lead route under Jesse's symbol ordering. If synchronized
        # histories are not available at this callback, skip the opportunity.
        if self.symbol != SYMBOLS[0] or self.time <= book['last_exit']:
            return
        if any(s.is_open or s.entry_orders for s in strategies.values()):
            return
        history = self._histories()
        if history is None:
            return
        plan = self._new_plan(history)
        if plan is not None:
            book['plan'] = plan
            book['phase'] = 'armed'
            self.log('ORCH_PAIR_ARM basket=' + str(plan['time'])
                     + ' beta=' + str(plan['beta']) + ' risks=' + str(plan['risks']))

    def _side(self):
        book = self._book()
        plan = book['plan']
        if plan is None or book['phase'] not in ('armed', 'entering'):
            return 0
        if plan['time'] != int(self.time) or plan['exit_reason'] is not None:
            return 0
        if self.symbol in plan['queued']:
            return 0
        # Both callbacks enqueue before simulated MARKET orders execute.
        # Never require BTC.is_open here: doing so would block the ETH leg.
        if self.symbol == SYMBOLS[1] and SYMBOLS[0] not in plan['queued']:
            self._request_exit('leader_not_queued')
            return 0
        if not math.isclose(float(self.price), plan['prices'][self.symbol],
                            rel_tol=1e-10, abs_tol=1e-8):
            self._request_exit('entry_clock_or_price_mismatch')
            return 0
        return plan['sides'][self.symbol]

    def should_long(self):
        return self._side() == 1

    def should_short(self):
        return self._side() == -1

    def _enqueue(self):
        book = self._book()
        plan = book['plan']
        assert self.symbol not in plan['queued']
        plan['queued'].add(self.symbol)
        book['phase'] = 'entering'
        return plan['qty'][self.symbol]

    def go_long(self):
        self.buy = self._enqueue(), self.price

    def go_short(self):
        self.sell = self._enqueue(), self.price

    def should_cancel_entry(self):
        self._request_exit('unexpected_pending_market_order')
        return True

    def on_open_position(self, order):
        book = self._book()
        plan = book['plan']
        assert plan is not None and self.symbol in plan['queued']
        assert self.symbol not in plan['filled'], 'PAIR_DUPLICATE_ENTRY'
        actual = float(self.position.entry_price)
        qty = abs(float(self.position.qty))
        distance = plan['distances'][self.symbol]
        # A protective order is attached to each fill even if its counterpart
        # fails. No assumption of atomic entry or stop execution is made.
        stop = actual - distance if self.is_long else actual + distance
        self.stop_loss = qty, stop
        plan['filled'][self.symbol] = dict(price=actual, qty=qty, time=int(self.time))
        if not (math.isclose(actual, plan['prices'][self.symbol], rel_tol=1e-10, abs_tol=1e-8)
                and math.isclose(qty, plan['qty'][self.symbol], rel_tol=1e-10, abs_tol=1e-8)):
            self._request_exit('fill_mismatch')
        if len(plan['filled']) == 2 and plan['exit_reason'] is None:
            assert plan['queued'] == set(SYMBOLS)
            assert len({v['time'] for v in plan['filled'].values()}) == 1
            book['phase'] = 'active'
            book['baskets'] += 1

    def update_position(self):
        book = self._book()
        plan = book['plan']
        assert plan is not None
        if plan['exit_reason'] is None and book['phase'] == 'active':
            history = self._histories()
            if history is not None:
                hours = (self.time - plan['ref_time']) / HOUR
                residual = (math.log(float(history[SYMBOLS[0]][-1, 2]) / plan['refs'][SYMBOLS[0]])
                            - plan['beta'] * math.log(float(history[SYMBOLS[1]][-1, 2])
                                                      / plan['refs'][SYMBOLS[1]])
                            - plan['alpha'] * hours)
                if plan['sign'] * residual <= 0:
                    self._request_exit('relative_recovery')
                elif plan['sign'] * (residual - plan['remaining']) >= plan['shock_scale']:
                    self._request_exit('relative_adverse_stop')
            if self.time - plan['time'] >= 12 * HOUR:
                self._request_exit('twelve_hour_expiry')
        if plan['exit_reason'] is not None:
            self.liquidate()

    def on_close_position(self, order, closed_trade):
        book = self._book()
        plan = book['plan']
        assert plan is not None
        assert self.symbol not in plan['closed'], 'PAIR_DUPLICATE_CLOSE'
        plan['closed'].add(self.symbol)
        if plan['exit_reason'] is None:
            self._request_exit('individual_emergency_or_terminal')
        if plan['closed'] == set(SYMBOLS):
            book['phase'] = 'flat'
            book['last_exit'] = int(self.time)
            book['plan'] = None

    def on_increased_position(self, order):
        raise AssertionError('PAIR_PYRAMIDING_UNSUPPORTED')

    def on_reduced_position(self, order):
        raise AssertionError('PAIR_PARTIAL_EXIT_UNSUPPORTED')
