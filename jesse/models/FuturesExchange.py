import numpy as np
import math
import jesse_rust as jr

import jesse.helpers as jh
import jesse.services.logger as logger
from jesse.enums import sides
from jesse.exceptions import InsufficientMargin
from jesse.models.Order import Order
from jesse.models.Exchange import Exchange
from jesse.store import store


class FuturesExchange(Exchange):
    def __init__(
            self,
            name: str,
            starting_balance: float,
            fee_rate: float,
            futures_leverage_mode: str,
            futures_leverage: int
    ):
        super().__init__(name, starting_balance, fee_rate, 'futures')

        # # # # live-trading only # # # #
        # in futures trading, margin is only with one asset, so:
        self._available_margin = 0
        # in futures trading, wallet is only with one asset, so:
        self._wallet_balance = 0
        # so is started_balance
        self._started_balance = 0
        # # # # # # # # # # # # # # # # #

        self.futures_leverage_mode = futures_leverage_mode
        self.futures_leverage = futures_leverage

    @property
    def started_balance(self) -> float:
        if jh.is_livetrading():
            return self._started_balance

        return self.starting_assets[jh.app_currency()]

    @property
    def wallet_balance(self) -> float:
        if jh.is_livetrading():
            return self._wallet_balance

        return self.assets[self.settlement_currency]

    @property
    def available_margin(self) -> float:
        if jh.is_livetrading():
            return self._available_margin

        return self._free_margin(include_pnl=True)

    def _free_margin(self, include_pnl: bool) -> float:
        # In both live trading and backtesting/paper trading, we start with the balance
        margin = self.wallet_balance

        # Calculate the total spent amount considering leverage
        # Here we need to calculate the total cost of all open positions and orders, considering leverage
        total_spent = 0
        for asset in self.assets:
            if asset == self.settlement_currency:
                continue

            position = store.positions.get_position(self.name, f"{asset}-{self.settlement_currency}")
            if position and position.is_open:
                # Adding the cost of open positions. Funding already debited
                # from the wallet out of isolated collateral is no longer
                # reserved by the position, so it is not subtracted twice.
                total_spent += position.total_cost - position.funding_margin_drawn
                # add unrealized PNL
                if include_pnl:
                    total_spent -= position.pnl

            # Summing up the cost of open orders (buy and sell), considering leverage
            sum_buy_orders = (self.buy_orders[asset][:][:, 0] * self.buy_orders[asset][:][:, 1]).sum()
            sum_sell_orders = (self.sell_orders[asset][:][:, 0] * self.sell_orders[asset][:][:, 1]).sum()

            total_spent += max(
                abs(sum_buy_orders) / self.futures_leverage, abs(sum_sell_orders) / self.futures_leverage
            )

        # Subtracting the total spent from the margin
        margin -= total_spent

        return margin

    def charge_fee(self, amount: float) -> None:
        if jh.is_livetrading():
            return

        fee_amount = abs(amount) * self.fee_rate
        new_balance = self.assets[self.settlement_currency] - fee_amount
        if fee_amount != 0:
            logger.info(
                f'Charged {round(fee_amount, 2)} as fee. Balance for {self.settlement_currency} on {self.name} changed from {round(self.assets[self.settlement_currency], 2)} to {round(new_balance, 2)}'
            )
        self.assets[self.settlement_currency] = new_balance

    def add_realized_pnl(self, realized_pnl: float) -> None:
        if jh.is_livetrading():
            return

        new_balance = self.assets[self.settlement_currency] + realized_pnl
        logger.info(
            f'Added realized PNL of {round(realized_pnl, 2)}. Balance for {self.settlement_currency} on {self.name} changed from {round(self.assets[self.settlement_currency], 2)} to {round(new_balance, 2)}')
        self.assets[self.settlement_currency] = new_balance

    def apply_funding(self, cashflow: float, position=None) -> None:
        """Backtest financing changes the wallet once, independently of fees.

        Live wallet balances already contain the venue's financing; applying
        simulated funding there would debit the same payment twice.
        """
        if jh.is_live():
            raise ValueError('Simulated funding accounting is only supported in backtests')
        if not math.isfinite(cashflow):
            raise ValueError('Funding cashflow must be finite')
        if not math.isfinite(self.wallet_balance + cashflow):
            raise ValueError('Funding would produce a nonfinite wallet balance')
        if (cashflow < 0 and position is not None and position.is_open
                and self.futures_leverage_mode == 'isolated'):
            self._debit_isolated_funding(-cashflow, position)
        elif cashflow < 0 and self.available_margin + cashflow < 0:
            # Cross liquidation is not simulated at all, so a debit beyond the
            # free margin cannot be absorbed by any modeled collateral.
            raise InsufficientMargin('Funding exhausts available margin; venue collateral liquidation is not modeled')
        self.assets[self.settlement_currency] += cashflow

    def _debit_isolated_funding(self, debit: float, position) -> None:
        """Binance USD-M: funding is paid from the available balance first, and
        any remainder from the position margin, moving its liquidation price.

        Isolated unrealized PnL is not part of that available balance. The
        wallet is still debited in full by apply_funding; this only records
        which part came out of the isolated collateral.
        """
        free = max(self._free_margin(include_pnl=False), 0)
        drawn = debit - free
        if drawn <= 0:
            return
        # The liquidation price moves by the drawn collateral per unit of size.
        shift = drawn / abs(position.qty)
        if position.is_long:
            liquidated = position.current_price <= position.liquidation_price + shift
        else:
            liquidated = position.current_price >= position.liquidation_price - shift
        if liquidated:
            # Binance would liquidate the position at this settlement; closing
            # it from inside settlement is not simulated, so stop rather than
            # report a run the venue would not have allowed.
            raise InsufficientMargin('Funding exhausts isolated margin and would liquidate the position; '
                                     'liquidation at a funding settlement is not modeled')
        position.funding_margin_drawn += drawn
        logger.info(
            f'Funding of {round(debit, 2)} exceeded the available balance; {round(drawn, 2)} was taken from the '
            f'{position.symbol} isolated margin (liquidation price now {round(position.liquidation_price, 2)})'
        )

    def on_order_submission(self, order: Order) -> None:
        if jh.is_livetrading():
            return

        base_asset = jh.base_asset(order.symbol)

        # make sure we don't spend more than we're allowed considering current allowed leverage
        if not order.reduce_only:
            # Calculate the effective order size considering leverage
            effective_order_size = abs(order.qty * order.price) / self.futures_leverage

            if effective_order_size > self.available_margin:
                raise InsufficientMargin(
                    f'Cannot submit an order with a value of ${round(order.qty * order.price)} when your available margin is ${round(self.available_margin)}. Consider increasing leverage number from the settings or reducing the order size.'
                )

        self.available_assets[base_asset] += order.qty

        if not order.reduce_only:
            if order.side == sides.BUY:
                self.buy_orders[base_asset].append(np.array([order.qty, order.price]))
            else:
                self.sell_orders[base_asset].append(np.array([order.qty, order.price]))

    def on_order_execution(self, order: Order) -> None:
        if jh.is_livetrading():
            return

        base_asset = jh.base_asset(order.symbol)

        if not order.reduce_only:
            # Gap fills replace order.price for real fill/fee accounting. The
            # pending margin was reserved at submission, so release that row.
            submitted_price = (order.vars or {}).get('submitted_price', order.price)
            order_array = np.array([order.qty, submitted_price])
            if order.side == sides.BUY:
                item_index = np.where(np.all(self.buy_orders[base_asset].array == order_array, axis=1))[0]
                if len(item_index) > 0:
                    index = item_index[0]
                    self.buy_orders[base_asset].delete(index, axis=0)
            else:
                item_index = np.where(np.all(self.sell_orders[base_asset].array == order_array, axis=1))[0]
                if len(item_index) > 0:
                    index = item_index[0]
                    self.sell_orders[base_asset].delete(index, axis=0)

    def on_order_cancellation(self, order: Order) -> None:
        if jh.is_livetrading():
            return

        base_asset = jh.base_asset(order.symbol)

        self.available_assets[base_asset] -= order.qty
        if not order.reduce_only:
            order_array = np.array([order.qty, order.price])
            if order.side == sides.BUY:
                index = find_order_index(self.buy_orders[base_asset].array, order_array)
                if index != -1:
                    self.buy_orders[base_asset].delete(index, axis=0)
            else:
                index = find_order_index(self.sell_orders[base_asset].array, order_array)
                if index != -1:
                    self.sell_orders[base_asset].delete(index, axis=0)

    def update_from_stream(self, data: dict) -> None:
        """
        Used for updating the exchange from the WS stream (only for live trading)
        """
        if not jh.is_livetrading():
            raise Exception('This method is only for live trading')
        self._available_margin = data['available_margin']
        self._wallet_balance = data['wallet_balance']
        if self._started_balance == 0:
            self._started_balance = self._wallet_balance


def find_order_index(orders, order_array):
    return jr.find_order_index(
        np.ascontiguousarray(orders, dtype=np.float64),
        np.ascontiguousarray(order_array, dtype=np.float64),
    )
