import math
import numpy as np
from jesse.strategies import Strategy
import jesse.indicators as ta

TRADE_RISK = 0.01  # Exploratory sleeve; no search over risk.
PORTFOLIO_RISK = 0.08
NOTIONAL_CAP = 4.4  # Admission buffer inside isolated 5x.
SLIPPAGE_RESERVE = 0.001  # Sizing only, not applied fill friction.
QUIET_RATIO = 0.75  # Fixed broad contraction criterion, not fitted percentile.


class OrchShortQuietChannel1h(Strategy):
    """Simplified compression-to-trend hypothesis, not an independent proven edge.

    Preceding 72/720 log-return volatility excludes the latest closed signal bar.
    Future STOP uses 72 completed hourly lows including that latest bar.
    Warmup 800 is required; buffer insufficiency fails visibly, never as zero trades.
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


    def before(self) -> None:
        # 721 previous closes create 720 returns, plus the excluded signal bar.
        # Verify retained history each callback instead of silently warming up
        # through an undocumented buffer limit and misreading no trades as no edge.
        if len(self.candles) < 722:
            raise ValueError('QuietChannel needs >=722 retained 1h candles; set warm_up_candles=800')

    def should_long(self) -> bool:
        return False

    def go_long(self) -> None:
        return

    def should_short(self) -> bool:
        if self.symbol != 'BTC-USDT':
            return False
        c = self.candles
        prior = c[:-1]
        closes = prior[-721:, 2]
        if len(closes) != 721 or np.any(closes <= 0) or not np.all(np.isfinite(closes)):
            return False
        changes = np.diff(np.log(closes))
        short_vol = float(np.std(changes[-72:], ddof=0))
        long_vol = float(np.std(changes, ddof=0))
        if not (math.isfinite(short_vol) and math.isfinite(long_vol)
                and long_vol > 0 and short_vol <= QUIET_RATIO * long_vol):
            return False
        atr = float(ta.atr(c))
        entry = float(np.min(c[-72:, 4]))
        # This is a future confirmation order, never a retrospective fill at a
        # low already traded by the completed signal candle.
        if not (math.isfinite(atr) and atr > 0
                and 0 < self.price - entry <= atr):
            return False
        distance = 2 * atr
        if distance >= entry:
            return False
        capital = self._capital()
        risk, notional = self._committed()
        budget = min(capital * TRADE_RISK,
                     max(0.0, capital * PORTFOLIO_RISK - risk))
        unit_risk = distance + self.fee_rate * (2 * entry + distance) + SLIPPAGE_RESERVE * entry
        room = max(0.0, capital * NOTIONAL_CAP - notional)
        qty = min(budget / unit_risk, room / entry,
                  max(0.0, float(self.leveraged_available_margin) * 0.90) / entry)
        # Research precision only; native lot and minimum notional need validation.
        qty = math.floor(qty / 0.001) * 0.001
        if qty <= 0:
            return False
        self.vars['plan'] = {'qty': qty, 'entry': entry, 'distance': distance,
                             'risk': qty * unit_risk, 'notional': qty * entry}
        return True

    def go_short(self) -> None:
        plan = self.vars['plan']
        self._ledger()[self._key()] = dict(plan)
        self.sell = plan['qty'], plan['entry']

    def should_cancel_entry(self) -> bool:
        # One future hourly bar lifetime; subsequent plans recompute from closes.
        self._ledger().pop(self._key(), None)
        return True

    def on_open_position(self, order) -> None:
        if self.is_short:
            # Preserve the planned ATR distance around the actual gap fill.
            self.stop_loss = abs(self.position.qty), (
                float(self.position.entry_price) + self.vars['plan']['distance'])
        self._ledger().pop(self._key(), None)

    def update_position(self) -> None:
        if not self.is_short:
            return
        # Faster 24h channel invalidates a failed 72h breakout. Only tighten;
        # never place a stop below the current observed quote or backdate a fill.
        stop = float(np.max(self.candles[-24:, 3]))
        if math.isfinite(stop) and self.price < stop < self.average_stop_loss:
            self.stop_loss = abs(self.position.qty), stop

    def on_close_position(self, order, closed_trade) -> None:
        self._ledger().pop(self._key(), None)
