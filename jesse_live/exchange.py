"""Binance USD-M driver registered on Jesse's live_drivers hook."""

from __future__ import annotations

from decimal import Decimal, ROUND_DOWN

from jesse.enums import exchanges, order_types
from jesse.exchanges.exchange import Exchange
from jesse.models.Order import Order
from jesse.services import logger, order_service
import jesse.helpers as jh

from jesse_live.binance import BinanceFuturesClient
from jesse_live.settings import allow_trading


def _decimals(step: str) -> int:
    text = str(step)
    if "." not in text:
        return 0
    return len(text.rstrip("0").split(".")[1])


def _round_down(value: float, decimals: int) -> float:
    quant = Decimal("1").scaleb(-decimals)
    return float(Decimal(str(value)).quantize(quant, rounding=ROUND_DOWN))


class BinancePerpetualFuturesDriver(Exchange):
    name = exchanges.BINANCE_PERPETUAL_FUTURES

    def __init__(self) -> None:
        super().__init__()
        self.client = BinanceFuturesClient()
        self.vars = {"precisions": {}}
        self._load_precisions()

    def _load_precisions(self) -> None:
        from jesse.routes import router

        for route in router.routes:
            info = self.client.exchange_info(route.symbol)
            symbols = info.get("symbols") or []
            if not symbols:
                continue
            filters = {item["filterType"]: item for item in symbols[0].get("filters", [])}
            tick = filters.get("PRICE_FILTER", {}).get("tickSize", "0.1")
            step = filters.get("LOT_SIZE", {}).get("stepSize", "0.001")
            self.vars["precisions"][route.symbol] = {
                "price_precision": _decimals(tick),
                "qty_precision": _decimals(step),
            }

    def _prec(self, symbol: str) -> dict:
        return self.vars["precisions"].get(symbol, {"price_precision": 1, "qty_precision": 3})

    def _maybe_place(self, payload: dict) -> str | None:
        if not allow_trading():
            logger.info(f"DRY-RUN Binance order skipped (allow_trading switch off): {payload}")
            return None
        result = self.client.place_order(payload)
        return str(result.get("orderId") or "")

    def market_order(self, symbol: str, qty: float, current_price: float, side: str, reduce_only: bool) -> Order:
        qty = _round_down(abs(qty), self._prec(symbol)["qty_precision"])
        payload = {
            "symbol": self.client.to_binance_symbol(symbol),
            "side": side.upper(),
            "type": "MARKET",
            "quantity": qty,
            "reduceOnly": "true" if reduce_only else "false",
        }
        exchange_id = self._maybe_place(payload)
        return order_service.create_order({
            "id": jh.generate_unique_id(),
            "exchange_id": exchange_id,
            "symbol": symbol,
            "exchange": self.name,
            "side": side,
            "type": order_types.MARKET,
            "reduce_only": reduce_only,
            "qty": jh.prepare_qty(qty, side),
            "price": current_price,
        })

    def limit_order(self, symbol: str, qty: float, price: float, side: str, reduce_only: bool) -> Order:
        qty = _round_down(abs(qty), self._prec(symbol)["qty_precision"])
        price = _round_down(price, self._prec(symbol)["price_precision"])
        payload = {
            "symbol": self.client.to_binance_symbol(symbol),
            "side": side.upper(),
            "type": "LIMIT",
            "timeInForce": "GTC",
            "quantity": qty,
            "price": price,
            "reduceOnly": "true" if reduce_only else "false",
        }
        exchange_id = self._maybe_place(payload)
        return order_service.create_order({
            "id": jh.generate_unique_id(),
            "exchange_id": exchange_id,
            "symbol": symbol,
            "exchange": self.name,
            "side": side,
            "type": order_types.LIMIT,
            "reduce_only": reduce_only,
            "qty": jh.prepare_qty(qty, side),
            "price": price,
        })

    def stop_order(self, symbol: str, qty: float, price: float, side: str, reduce_only: bool) -> Order:
        qty = _round_down(abs(qty), self._prec(symbol)["qty_precision"])
        price = _round_down(price, self._prec(symbol)["price_precision"])
        payload = {
            "symbol": self.client.to_binance_symbol(symbol),
            "side": side.upper(),
            "type": "STOP_MARKET",
            "stopPrice": price,
            "quantity": qty,
            "reduceOnly": "true" if reduce_only else "false",
        }
        exchange_id = self._maybe_place(payload)
        return order_service.create_order({
            "id": jh.generate_unique_id(),
            "exchange_id": exchange_id,
            "symbol": symbol,
            "exchange": self.name,
            "side": side,
            "type": order_types.STOP,
            "reduce_only": reduce_only,
            "qty": jh.prepare_qty(qty, side),
            "price": price,
        })

    def cancel_all_orders(self, symbol: str) -> None:
        if allow_trading():
            self.client.cancel_all_orders(symbol)
        from jesse.store import store
        for order in store.orders.get_active_orders(self.name, symbol):
            order_service.cancel_order(order)

    def cancel_order(self, symbol: str, order_id: str) -> None:
        from jesse.store import store
        order = store.orders.get_order_by_id(self.name, symbol, order_id)
        if allow_trading() and order and order.exchange_id:
            self.client.cancel_order(symbol, order.exchange_id)
        if order:
            order_service.cancel_order(order)

    def _fetch_precisions(self) -> None:
        self._load_precisions()
