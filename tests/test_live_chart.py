from jesse_live.chart import (
    CHART_STRATEGY,
    chart_routes,
    current_candles_map,
    trading_routes,
    update_forming,
)


def test_chart_routes_do_not_replace_strategy_timeframe():
    routes = chart_routes([
        {"exchange": "Binance Perpetual Futures", "symbol": "BTC-USDT", "timeframe": "1h", "strategy": "TemaTrendFollowing"},
    ])
    trading = trading_routes(routes)
    assert trading == [
        {"exchange": "Binance Perpetual Futures", "symbol": "BTC-USDT", "timeframe": "1h", "strategy": "TemaTrendFollowing"},
    ]
    extra = [route for route in routes if route["strategy"] == CHART_STRATEGY]
    assert {route["timeframe"] for route in extra} >= {"1m", "5m", "15m", "4h", "1D"}
    assert all(route["symbol"] == "BTC-USDT" for route in extra)


def test_trading_routes_strip_chart_only_rows():
    stripped = trading_routes([
        {"symbol": "BTC-USDT", "timeframe": "1h", "strategy": "TemaTrendFollowing"},
        {"symbol": "BTC-USDT", "timeframe": "5m", "strategy": CHART_STRATEGY},
    ])
    assert stripped == [{"symbol": "BTC-USDT", "timeframe": "1h", "strategy": "TemaTrendFollowing"}]


def test_forming_candle_updates_same_bucket_and_opens_next():
    forming = {}
    first = update_forming(forming, "1m", 100.0, 1_700_000_000_000)
    assert first["open"] == 100.0
    same = update_forming(forming, "1m", 101.5, 1_700_000_010_000)
    assert same["time"] == first["time"]
    assert same["high"] == 101.5
    assert same["close"] == 101.5
    nxt = update_forming(forming, "1m", 99.0, 1_700_000_060_000)
    assert nxt["time"] == first["time"] + 60
    assert nxt["open"] == 101.5
    payload = current_candles_map("Binance Perpetual Futures", "BTC-USDT", forming, ["1m", "1h"])
    assert "Binance Perpetual Futures-BTC-USDT-1m" in payload
    assert payload["Binance Perpetual Futures-BTC-USDT-1m"]["close"] == 99.0
