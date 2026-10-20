import math
import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta

# One preregistered recipe, not an optimization grid.
TRADE_RISK = 0.01
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4
ASSET_NOTIONAL_CAP = 2.2  # Equal ex-ante gross ceilings for two configured assets.
SLIPPAGE_RESERVE = 0.001  # Risk sizing only, not simulated spread/slippage.


class OrchManageTurtleDaily(Strategy):
    """Simplified daily trend control on BTC and Spot-price proxy PAXG.

    Prior 55-day closing breakout, fixed initial 2*ATR20 stop and ratcheting
    ten-day channel exits. This revisits the trend family; it is not a newly
    independent edge. No EMA/ADX/RSI, profit target, breakeven or pyramiding.
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

    def _plan(self, side: int) -> bool:
        if self.symbol not in ('BTC-USDT', 'PAXG-USDT'):
            return False
        c = self.candles
        # Warmup40 is ingestion history, not an artificial cap. Wait for enough
        # accumulated data; do not invent unavailable PAXG2019 candles.
        if len(c) < 56:
            return False
        previous = c[-56:-1]
        upper = float(np.max(previous[:, 3]))
        lower = float(np.min(previous[:, 4]))
        atr = float(ta.atr(c, period=20))
        entry = float(self.price)
        if not all(math.isfinite(v) for v in (upper, lower, atr, entry)):
            return False
        if not (atr > 0 and ((side == 1 and entry > upper)
                             or (side == -1 and entry < lower))):
            return False
        distance = 2.0 * atr
        if not 0 < distance < entry:
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK,
                     max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry - side * distance) + SLIPPAGE_RESERVE * entry
        room = min(max(0.0, capital * NOTIONAL_CAP - notional),
                   capital * ASSET_NOTIONAL_CAP)
        margin_room = max(0.0, float(self.leveraged_available_margin) * 0.90)
        if budget <= 0 or room <= 0 or margin_room <= 0 or unit_risk <= 0:
            return False
        qty = min(budget / unit_risk, room / entry, margin_room / entry)
        step = 0.001 if self.symbol == 'BTC-USDT' else 0.0001
        qty = math.floor(qty / step) * step
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'side': side, 'risk': qty * unit_risk,
                             'notional': qty * entry}
        return True

    def _signal(self) -> int:
        # Freeze one plan per closed candle; probing shorts after a long
        # submission must never overwrite its pending risk reservation.
        if self.vars.get('signal_index') != self.index:
            self.vars['signal_index'] = self.index
            self.vars['signal_value'] = 1 if self._plan(1) else (-1 if self._plan(-1) else 0)
        return self.vars['signal_value']

    def should_long(self) -> bool:
        return self._signal() == 1

    def should_short(self) -> bool:
        return self._signal() == -1

    def go_long(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        # MARKET after the daily close confirms the prior channel break.
        self.buy = plan['qty'], plan['entry']

    def go_short(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:
        entry = float(self.position.entry_price)
        distance = self.vars['plan']['distance']
        assert 0 < distance < entry, 'TURTLE_INVALID_FILL_STOP'
        self.vars['initial_distance'] = distance
        if self.is_long:
            self.stop_loss = abs(self.position.qty), entry - distance
        elif self.is_short:
            self.stop_loss = abs(self.position.qty), entry + distance
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:
        c = self.candles
        # This window includes the latest already closed day. The replacement
        # protects future quotes; it is never applied retroactively inside it.
        if len(c) < 10:
            return
        if self.is_long:
            stop = float(np.min(c[-10:, 4]))
            if math.isfinite(stop) and self.average_stop_loss < stop < self.price:
                self.stop_loss = abs(self.position.qty), stop
        elif self.is_short:
            stop = float(np.max(c[-10:, 3]))
            if math.isfinite(stop) and self.average_stop_loss > stop > self.price:
                self.stop_loss = abs(self.position.qty), stop

    def after(self) -> None:
        # By November the40-day warmup plus elapsed daily closes must exceed55.
        # Detect a retention/config mistake rather than accepting an empty test.
        if self.closed_candle_open_time >= 1604188800000:
            assert len(self.candles) >= 56, 'TURTLE_HISTORY_DID_NOT_GROW'

    def on_close_position(self, order, closed_trade) -> None:
        self._ledger().pop(self._key(), None)
