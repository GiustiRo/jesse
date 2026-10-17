"""Live dashboard chart helpers. View-only timeframes never become strategy routes."""

from __future__ import annotations

CHART_STRATEGY = "__chart__"
CHART_TIMEFRAMES = ("1m", "5m", "15m", "1h", "4h", "1D")
TF_MS = {
    "1m": 60_000,
    "3m": 3 * 60_000,
    "5m": 5 * 60_000,
    "15m": 15 * 60_000,
    "30m": 30 * 60_000,
    "45m": 45 * 60_000,
    "1h": 60 * 60_000,
    "2h": 2 * 60 * 60_000,
    "3h": 3 * 60 * 60_000,
    "4h": 4 * 60 * 60_000,
    "6h": 6 * 60 * 60_000,
    "8h": 8 * 60 * 60_000,
    "12h": 12 * 60 * 60_000,
    "1D": 24 * 60 * 60_000,
    "3D": 3 * 24 * 60 * 60_000,
}


def is_chart_route(route) -> bool:
    return isinstance(route, dict) and route.get("strategy") == CHART_STRATEGY


def trading_routes(routes: list | None) -> list:
    return [route for route in list(routes or []) if not is_chart_route(route)]


def chart_routes(strategy_routes: list | None) -> list:
    routes = [dict(route) for route in list(strategy_routes or []) if isinstance(route, dict)]
    if not routes:
        return routes
    first = routes[0]
    seen = {(row.get("symbol"), row.get("timeframe")) for row in routes}
    for timeframe in CHART_TIMEFRAMES:
        key = (first.get("symbol"), timeframe)
        if key in seen:
            continue
        seen.add(key)
        routes.append({
            "exchange": first.get("exchange"),
            "symbol": first.get("symbol"),
            "timeframe": timeframe,
            "strategy": CHART_STRATEGY,
        })
    return routes


def update_forming(forming: dict, timeframe: str, price: float, now_ms: int) -> dict:
    tf_ms = TF_MS.get(timeframe, 60_000)
    bucket = (int(now_ms) // tf_ms) * tf_ms
    previous = forming.get(timeframe)
    if previous is None or int(previous["time"]) * 1000 != bucket:
        open_price = float(previous["close"]) if previous is not None else float(price)
        forming[timeframe] = {
            "time": bucket // 1000,
            "open": open_price,
            "high": max(open_price, float(price)),
            "low": min(open_price, float(price)),
            "close": float(price),
            "volume": 0.0,
        }
    else:
        previous["close"] = float(price)
        previous["high"] = max(previous["high"], float(price))
        previous["low"] = min(previous["low"], float(price))
    return forming[timeframe]


def current_candles_map(exchange: str, symbol: str, forming: dict, timeframes: list[str]) -> dict:
    payload = {}
    for timeframe in timeframes:
        candle = forming.get(timeframe)
        if candle is None:
            continue
        payload[f"{exchange}-{symbol}-{timeframe}"] = candle
    return payload
