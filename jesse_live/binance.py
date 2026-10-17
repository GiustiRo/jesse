"""Thin Binance USD-M futures client with optional SOCKS5 egress."""

from __future__ import annotations

import hashlib
import hmac
import os
import time
from urllib.parse import urlencode

import httpx

CONDITIONAL_ORDER_TYPES = {
    "STOP",
    "STOP_MARKET",
    "TAKE_PROFIT",
    "TAKE_PROFIT_MARKET",
    "TRAILING_STOP_MARKET",
}
ALGO_FILLED_STATUSES = {"FILLED", "FINISHED", "EXECUTED"}


def algo_order_payload(params: dict) -> dict:
    payload = dict(params)
    payload["algoType"] = payload.get("algoType") or "CONDITIONAL"
    payload["type"] = str(payload.get("type") or "").upper()
    if payload.get("triggerPrice") is None and payload.get("stopPrice") is not None:
        payload["triggerPrice"] = payload.pop("stopPrice")
    else:
        payload.pop("stopPrice", None)
    return payload


class BinanceFuturesClient:
    def __init__(
        self,
        *,
        api_key: str = "",
        api_secret: str = "",
        rest_base_url: str | None = None,
        socks5_proxy_url: str | None = None,
        proxy_required: bool | None = None,
        recv_window_ms: int = 20000,
    ):
        self.api_key = api_key or os.getenv("BINANCE_API_KEY", "")
        secret = api_secret or os.getenv("BINANCE_API_SECRET", "")
        self.api_secret = secret.encode("utf-8") if secret else b""
        self.rest_base_url = (rest_base_url or os.getenv("BINANCE_REST_BASE_URL") or "https://fapi.binance.com").rstrip("/")
        proxy = socks5_proxy_url if socks5_proxy_url is not None else os.getenv("BINANCE_SOCKS5_PROXY_URL", "")
        self.proxy = proxy.strip() or None
        required = os.getenv("BINANCE_PROXY_REQUIRED", "false").lower() in {"1", "true", "yes"}
        if proxy_required is not None:
            required = proxy_required
        if required and not self.proxy:
            raise RuntimeError("BINANCE_PROXY_REQUIRED is set but BINANCE_SOCKS5_PROXY_URL is empty.")
        self.recv_window_ms = recv_window_ms
        self._time_offset_ms = 0
        headers = {}
        if self.api_key:
            headers["X-MBX-APIKEY"] = self.api_key
        self._client = httpx.Client(timeout=20.0, proxy=self.proxy, headers=headers)

    def close(self) -> None:
        self._client.close()

    @staticmethod
    def to_binance_symbol(jesse_symbol: str) -> str:
        return jesse_symbol.replace("-", "").replace("/", "").upper()

    def server_time(self) -> int:
        return int(self._public("/fapi/v1/time")["serverTime"])

    def ticker_price(self, symbol: str) -> float:
        data = self._public("/fapi/v2/ticker/price", {"symbol": self.to_binance_symbol(symbol)})
        if isinstance(data, list):
            data = data[0] if data else {}
        return float(data["price"])

    def account_balance_usdt(self) -> float | None:
        if not self.api_key or not self.api_secret:
            return None
        payload = self._signed("GET", "/fapi/v3/balance")
        if isinstance(payload, dict):
            payload = payload.get("balances") or []
        for row in payload:
            if row.get("asset") == "USDT":
                return float(row.get("balance") or row.get("walletBalance") or 0)
        return None

    def ping(self) -> None:
        self._public("/fapi/v1/ping")
        try:
            self.sync_time()
        except Exception:
            pass

    def sync_time(self) -> None:
        server = self.server_time()
        self._time_offset_ms = server - int(time.time() * 1000)

    def _now_ms(self) -> int:
        return int(time.time() * 1000) + self._time_offset_ms

    def klines(self, symbol: str, interval: str, limit: int = 500) -> list[list]:
        return self._public(
            "/fapi/v1/klines",
            {"symbol": self.to_binance_symbol(symbol), "interval": interval, "limit": limit},
        )

    def exchange_info(self, symbol: str) -> dict:
        return self._public("/fapi/v1/exchangeInfo", {"symbol": self.to_binance_symbol(symbol)})

    def place_order(self, params: dict) -> dict:
        order_type = str(params.get("type") or "").upper()
        if order_type in CONDITIONAL_ORDER_TYPES:
            return self._normalize_order(self._signed("POST", "/fapi/v1/algoOrder", algo_order_payload(params)))
        return self._normalize_order(self._signed("POST", "/fapi/v1/order", params))

    def cancel_order(self, symbol: str, order_id: str) -> dict:
        symbol_b = self.to_binance_symbol(symbol)
        try:
            return self._signed("DELETE", "/fapi/v1/order", {"symbol": symbol_b, "orderId": order_id})
        except Exception:
            return self._signed("DELETE", "/fapi/v1/algoOrder", {"symbol": symbol_b, "algoId": order_id})

    def cancel_all_orders(self, symbol: str) -> dict:
        symbol_b = self.to_binance_symbol(symbol)
        last_error: Exception | None = None
        result = None
        for path in ("/fapi/v1/allOpenOrders", "/fapi/v1/algoOpenOrders"):
            try:
                result = self._signed("DELETE", path, {"symbol": symbol_b})
            except Exception as exc:
                last_error = exc
        if result is None and last_error is not None:
            raise last_error
        return result or {}

    def get_order(self, symbol: str, order_id: str) -> dict:
        symbol_b = self.to_binance_symbol(symbol)
        try:
            return self._normalize_order(
                self._signed("GET", "/fapi/v1/order", {"symbol": symbol_b, "orderId": order_id})
            )
        except Exception:
            return self._normalize_order(
                self._signed("GET", "/fapi/v1/algoOrder", {"symbol": symbol_b, "algoId": order_id})
            )

    @staticmethod
    def _normalize_order(remote: dict | list) -> dict:
        if isinstance(remote, list):
            remote = remote[0] if remote else {}
        if not isinstance(remote, dict):
            return {}
        out = dict(remote)
        if out.get("orderId") is None and out.get("algoId") is not None:
            out["orderId"] = out["algoId"]
        status = str(out.get("status") or out.get("algoStatus") or "").upper()
        if status in ALGO_FILLED_STATUSES:
            status = "FILLED"
        out["status"] = status
        return out

    def _public(self, path: str, params: dict | None = None) -> dict | list:
        return self._request("GET", path, params or {}, signed=False)

    def _signed(self, method: str, path: str, params: dict | None = None) -> dict | list:
        return self._request(method, path, params or {}, signed=True)

    def _request(self, method: str, path: str, params: dict, signed: bool) -> dict | list:
        last_error: Exception | None = None
        attempts = 2 if method == "GET" else 1
        for attempt in range(attempts):
            query = dict(params)
            if signed:
                query["timestamp"] = self._now_ms()
                query["recvWindow"] = self.recv_window_ms
                encoded = urlencode(query, doseq=True)
                query["signature"] = hmac.new(self.api_secret, encoded.encode("utf-8"), hashlib.sha256).hexdigest()
            try:
                response = self._client.request(method, self.rest_base_url + path, params=query)
            except httpx.HTTPError as exc:
                last_error = exc
                if attempt + 1 < attempts:
                    time.sleep(1)
                    continue
                raise
            if response.status_code < 400:
                return response.json()
            body = response.text
            last_error = RuntimeError(f"Binance HTTP {response.status_code} {path}: {body}")
            if attempt + 1 < attempts and response.status_code in {400, 408, 429, 500, 502, 503, 504}:
                if "-1021" in body:
                    try:
                        self.sync_time()
                    except Exception:
                        pass
                time.sleep(1)
                continue
            raise last_error
        raise last_error
