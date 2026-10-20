import math
import numpy as np
from jesse.strategies import Strategy, cached
from jesse import utils
import jesse.indicators as ta

# User-approved research limits; risk is not an optimization parameter.
TRADE_RISK = 0.03
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4  # Leaves a margin buffer within the configured isolated 5x leverage.
SLIPPAGE_RESERVE = 0.001  # 10 bps round trip for sizing only, not simulated fill friction.


class MultiAssetSleeves4h(Strategy):
    """Pre-positioned Donchian STOP entries with shared risk and margin reservations.

    Research prototype for BTC/PAXG and a session-filtered SPX CFD proxy.
    Weekday calendar only; holidays and venue-native parity remain unverified. No live session is authorized by this code.
    """

    def hyperparameters(self) -> list:
        return [
            {'name': 'donchian_len', 'type': int, 'min': 20, 'max': 40, 'default': 26},
            {'name': 'ema_fast', 'type': int, 'min': 16, 'max': 32, 'default': 20},
            {'name': 'ema_slow', 'type': int, 'min': 80, 'max': 140, 'default': 80},
            {'name': 'adx_min', 'type': int, 'min': 16, 'max': 30, 'default': 26},
            {'name': 'stop_atr', 'type': float, 'min': 1.6, 'max': 3.0, 'default': 2.0},
            {'name': 'trail_atr', 'type': float, 'min': 3.0, 'max': 5.0, 'default': 4.2},
            {'name': 'be_r', 'type': float, 'min': 1.75, 'max': 3.0, 'default': 2.25},
        ]

    def trading_hours(self):
        if self.symbol == 'SPY-USDT':
            # The fixed UTC whole-bar intersection excludes the US index daily
            # break in both DST regimes. This is an intentional common window,
            # not an assertion that the source's full session ends at 20:00 UTC.
            return {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-20:00'}}
        return None

    @property
    @cached
    def signal_candles(self):
        return utils.filter_candles_by_hours(self.candles, self.trading_hours())

    def _entry_window(self) -> bool:
        if self.symbol != 'SPY-USDT':
            return True
        # A closed bar opening at 12:00 triggers at 16:00. Its order expires
        # at 20:00, before the excluded 20:00-24:00 bucket. A 16:00-open bar
        # must not arm a new order at 20:00. Pending orders still cancel then.
        window = {'timezone': 'UTC', 'hours': {'Mon-Fri': '00:00-16:00'}}
        return self.is_trading_hours and utils.is_in_trading_hours(
            self.closed_candle_open_time, window)

    def _ledger(self) -> dict:
        return self.shared_vars.setdefault('phase2_reservations', {})

    def _key(self) -> str:
        return self.exchange + ':' + self.symbol

    def _capital(self) -> float:
        # Floating gains do not enlarge the risk budget; floating losses reduce it.
        return max(0.0, min(float(self.balance), float(self.portfolio_value)))

    def _committed(self) -> tuple:
        risk, notional = 0.0, 0.0
        ledger = self._ledger()
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            strategy = route.strategy
            if strategy.is_open:
                qty = abs(float(strategy.position.qty))
                entry = float(strategy.position.entry_price)
                # Risk is measured from the current mark, so protected floating PnL
                # is not silently treated as free capacity for another trade.
                value = abs(float(strategy.position.value))
                mark = value / qty if qty else entry
                stop = float(strategy.average_stop_loss)
                distance = max(0.0, mark - stop) if strategy.is_long else max(0.0, stop - mark)
                risk += qty * (distance + mark * (self.fee_rate + SLIPPAGE_RESERVE))
                notional += value
            else:
                reservation = ledger.get(route.exchange + ':' + route.symbol)
                if reservation:
                    # Includes not-yet-filled STOP/LIMIT entries, not only open positions.
                    risk += reservation['risk']
                    notional += reservation['notional']
        return risk, notional

    def _volatility_share(self) -> float:
        """Reserve a common gross-exposure budget using inverse ATR fractions.

        All configured assets receive an ex-ante share, even while their signal
        is idle. This prevents the first route from consuming all shared margin.
        It is a capital-efficiency tradeoff to test, not an optimal allocation.
        """
        weights = {}
        for route in self.routes:
            if route.exchange != self.exchange:
                continue
            c = utils.filter_candles_by_hours(route.strategy.candles, route.strategy.trading_hours())
            if len(c) < int(self.hp['ema_slow']) + 20:
                return 0.0
            atr = float(ta.atr(c))
            price = float(c[-1, 2])
            if not math.isfinite(atr) or atr <= 0 or price <= 0:
                return 0.0
            # Stops use a common ATR multiple. Equal risk therefore needs
            # notional proportional to price/ATR before gross-leverage scaling.
            weights[route.symbol] = price / atr
        if not weights:
            return 0.0
        # Predeclared 50/50 blend keeps inverse-volatility scaling while reserving
        # an equal-capital sleeve. This tests idle low-volatility budget crowding.
        return 0.5 / len(weights) + 0.5 * weights.get(self.symbol, 0.0) / sum(weights.values())

    def _plan(self) -> bool:
        """Asset-specific long hypotheses, declared before this variant's run.

        BTC retains closing confirmation; gold tests a slower 55-bar STOP.
        SPY tests oversold LIMIT mean reversion in a rising regime, with its
        entire position exited at the pre-entry EMA20 target, never partials.
        """
        if not self._entry_window():
            return False
        c = self.signal_candles
        if len(c) < 140:
            return False
        atr = float(ta.atr(c))
        fast = float(ta.ema(c, period=20))
        slow = ta.ema(c, period=80, sequential=True)
        rsi = float(ta.rsi(c))
        adx = float(ta.adx(c))
        if not all(math.isfinite(v) for v in (atr, fast, slow[-1], slow[-5], rsi, adx)) or atr <= 0:
            return False
        target = None
        if self.symbol == 'SPY-USDT':
            macro = ta.ema(c, period=120, sequential=True)
            quick_rsi = float(ta.rsi(c, period=3))
            if not (math.isfinite(quick_rsi) and macro[-1] > macro[-10]
                    and self.price > macro[-1] - atr and quick_rsi <= 20):
                return False
            entry = min(float(c[-1, 4]), self.price - 0.25 * atr)
            distance = 1.5 * atr
            target = fast
            # Reject trades whose full EMA target cannot cover one ATR and at
            # least three modeled round-trip commissions before execution costs.
            if target - entry < max(atr, 6 * self.fee_rate * entry):
                return False
        else:
            n = 26 if self.symbol == 'BTC-USDT' else 55
            boundary = float(np.max(c[-n-1:-1, 3]))
            if not (self.price > slow[-1] and fast > slow[-1] > slow[-5]
                    and adx >= 26 and 52 <= rsi <= 76
                    and self.high - self.low <= 3 * atr):
                return False
            if self.symbol == 'BTC-USDT':
                if self.price <= boundary:
                    return False
                entry = self.price
                # Preserve the original BTC floor against unnaturally tight risk.
                distance = max(2 * atr, 0.008 * entry)
                if distance > 0.055 * entry:
                    return False
            elif self.symbol == 'PAXG-USDT':
                entry = float(np.max(c[-55:, 3]))
                if not 0 < entry - self.price <= 2 * atr:
                    return False
                distance = 2.5 * atr
            else:
                return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK, max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry - distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * NOTIONAL_CAP * self._volatility_share())
        qty = min(budget / unit_risk, room / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        step = 0.001 if self.symbol in ('BTC-USDT', 'SPY-USDT') else 0.0001
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry,
                             'target': target}
        return True

    def should_long(self) -> bool:
        return self._plan()

    def should_short(self) -> bool:
        # Preserve Phase 1 direction for the first entry-mechanics ablation.
        return False

    def go_long(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.buy = plan['qty'], plan['entry']

    def go_short(self) -> None:
        pass

    def should_cancel_entry(self) -> bool:
        # One closed 4h bar lifetime: stale channels cannot remain active indefinitely.
        # Jesse processes cancellation before evaluating the next route.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        self.vars['initial_distance'] = distance
        # An intrabar fill must not inherit highs/closes from before its entry.
        self.vars['best_close'] = entry
        self.stop_loss = abs(self.position.qty), entry - distance
        self.vars['opened_time'] = int(self.time)
        if self.symbol == 'SPY-USDT':
            self.take_profit = abs(self.position.qty), self.vars['plan']['target']
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:
        if self.symbol == 'SPY-USDT':
            # A mean-reversion premise expires after five calendar days.
            if self.time - self.vars['opened_time'] >= 5 * 24 * 60 * 60 * 1000:
                self.liquidate()
            return
        history = self.signal_candles
        atr = float(ta.atr(history))
        if not math.isfinite(atr) or atr <= 0:
            return
        entry = float(self.position.entry_price)
        distance = self.vars['initial_distance']
        self.vars['best_close'] = max(self.vars['best_close'], float(history[-1, 2]))
        best_r = (self.vars['best_close'] - entry) / distance
        mult = float(self.hp['trail_atr'])
        # Inherited late-trend tightening; retained as a controlled baseline choice.
        if best_r >= 8:
            mult *= 0.62
        elif best_r >= 5:
            mult *= 0.78
        stop = self.vars['best_close'] - mult * atr
        if best_r >= float(self.hp['be_r']):
            stop = max(stop, entry * (1 + 2.5 * self.fee_rate))
        if self.average_stop_loss < stop < self.price:
            self.stop_loss = abs(self.position.qty), stop

    def on_close_position(self, order, closed_trade) -> None:
        self._ledger().pop(self._key(), None)
