import math
from jesse.strategies import Strategy
import jesse.indicators as ta

# Fixed research recipe, not hyperparameters selected from a search.
TRADE_RISK = 0.01
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4
SLIPPAGE_RESERVE = 0.001  # Sizing reserve only; not fill friction.
MAX_HOLD_MS = 48 * 60 * 60 * 1000


class OrchManageFastMrBtc4h(Strategy):
    """Bounded BTC-only fast mean reversion in a rising 4h regime.

    This revisits the same economic MR premise as earlier failed sleeves.
    MARKET execution and a dynamic five-bar mean exit, rather than a passive
    dip fill and frozen EMA20 target, are the material falsification.
    EMA200 on 4h is roughly 33 days, not a 200-day trend measure.
    """

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

    def _plan(self) -> bool:
        # Standalone diagnostic only. Combining sleeves needs a separate
        # coordinated-account design and a new preregistered comparison.
        if self.symbol != 'BTC-USDT' or len(self.routes) != 1:
            return False
        c = self.candles
        # Enough history for a 200-bar EMA and the six-bar slope comparison.
        if len(c) < 207:
            return False
        macro = ta.ema(c, period=200, sequential=True)
        mean = float(ta.sma(c, period=5))
        rsi = float(ta.rsi(c, period=2))
        atr = float(ta.atr(c))
        entry = float(self.price)
        if not all(math.isfinite(v) for v in (macro[-1], macro[-7], mean, rsi, atr, entry)):
            return False
        if not (atr > 0 and entry > macro[-1] > macro[-7]
                and rsi <= 10 and entry < mean):
            return False
        # Freeze the signal ATR distance; place the stop from actual fill.
        distance = 2.5 * atr
        if not 0 < distance < entry:
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK,
                     max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry - distance) + SLIPPAGE_RESERVE * entry
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        gross_room = max(0.0, capital * NOTIONAL_CAP - notional)
        if budget <= 0 or unit_risk <= 0 or margin_room <= 0 or gross_room <= 0:
            return False
        qty = min(budget / unit_risk, margin_room / entry, gross_room / entry)
        # Same BTC research precision as the frozen reference. No native
        # lot/min-notional parity is implied by this simulator precision.
        qty = math.floor(qty / 0.001) * 0.001
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry}
        return True

    def should_long(self) -> bool:
        return self._plan()

    def should_short(self) -> bool:
        return False

    def go_long(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        # Equal to the closed-bar decision price: Jesse selects MARKET.
        self.buy = plan['qty'], plan['entry']

    def go_short(self) -> None:
        pass

    def should_cancel_entry(self) -> bool:
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:
        assert self.is_long, 'FAST_MR_UNEXPECTED_SHORT'
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        assert 0 < distance < entry, 'FAST_MR_INVALID_FILL_STOP'
        self.vars['opened_time'] = int(self.time)
        self.vars['initial_distance'] = distance
        self.stop_loss = abs(self.position.qty), entry - distance
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:
        # The current candle is already closed. Exits remain active every day;
        # elapsed timestamps bound the hypothesis without month-end cosmetics.
        mean = float(ta.sma(self.candles, period=5))
        expired = self.time - self.vars['opened_time'] >= MAX_HOLD_MS
        if expired or (math.isfinite(mean) and self.price >= mean):
            self.liquidate()

    def on_close_position(self, order, closed_trade) -> None:
        self._ledger().pop(self._key(), None)
