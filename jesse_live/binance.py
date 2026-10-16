"""Thin Binance USD-M futures client with optional SOCKS5 egress."""

from __future__ import annotations

import hashlib
import hmac
import os
import time
from urllib.parse import urlencode

import httpx


class BinanceFuturesClient:
    def __init__(
        self,
        *,
        api_key: str = "",
        api_secret: str = "",
        rest_base_url: str | None = None,
        socks5_proxy_url: str | None = None,
        proxy_required: bool | None = None,
        recv_window_ms: int = 5000,
    ):
        self.api_key = api_key
        self.api_secret = api_secret.encode("utf-8") if api_secret else b""
        self.rest_base_url = (rest_base_url or os.getenv("BINANCE_REST_BASE_URL") or "https://fapi.binance.com").rstrip("/")
        proxy = socks5_proxy_url if socks5_proxy_url is not None else os.getenv("BINANCE_SOCKS5_PROXY_URL", "")
        self.proxy = proxy.strip() or None
        required = os.getenv("BINANCE_PROXY_REQUIRED", "false").lower() in {"1", "true", "yes"}
        if proxy_required is not None:
            required = proxy_required
        if required and not self.proxy:
            raise RuntimeError("BINANCE_PROXY_REQUIRED is set but BINANCE_SOCKS5_PROXY_URL is empty.")
        self.recv_window_ms = recv_window_ms
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
        data = self._public("/fapi/v1/ticker/price", {"symbol": self.to_binance_symbol(symbol)})
        return float(data["price"])

    def account_balance_usdt(self) -> float | None:
        if not self.api_key or not self.api_secret:
            return None
        payload = self._signed("GET", "/fapi/v2/balance")
        for row in payload:
            if row.get("asset") == "USDT":
                return float(row.get("balance") or 0)
        return None

    def ping(self) -> None:
        self._public("/fapi/v1/ping")

    def _public(self, path: str, params: dict | None = None) -> dict | list:
        response = self._client.get(self.rest_base_url + path, params=params or {})
        response.raise_for_status()
        return response.json()

    def _signed(self, method: str, path: str, params: dict | None = None) -> dict | list:
        query = dict(params or {})
        query["timestamp"] = int(time.time() * 1000)
        query["recvWindow"] = self.recv_window_ms
        encoded = urlencode(query, doseq=True)
        query["signature"] = hmac.new(self.api_secret, encoded.encode("utf-8"), hashlib.sha256).hexdigest()
        response = self._client.request(method, self.rest_base_url + path, params=query)
        response.raise_for_status()
        return response.json()
