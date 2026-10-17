from jesse_live.binance import algo_order_payload, BinanceFuturesClient, CONDITIONAL_ORDER_TYPES


def test_stop_market_payload_renames_stop_price():
    payload = algo_order_payload({
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "STOP_MARKET",
        "stopPrice": 80000,
        "quantity": 0.01,
        "reduceOnly": "true",
    })
    assert payload["algoType"] == "CONDITIONAL"
    assert payload["type"] == "STOP_MARKET"
    assert payload["triggerPrice"] == 80000
    assert "stopPrice" not in payload


def test_conditional_types_cover_stops_and_take_profits():
    assert {"STOP_MARKET", "TAKE_PROFIT", "TAKE_PROFIT_MARKET", "STOP"} <= CONDITIONAL_ORDER_TYPES
    assert "LIMIT" not in CONDITIONAL_ORDER_TYPES
    assert "MARKET" not in CONDITIONAL_ORDER_TYPES


def test_normalize_algo_id_and_finished_status():
    out = BinanceFuturesClient._normalize_order({
        "algoId": 123,
        "algoStatus": "FINISHED",
        "executedQty": "0.01",
    })
    assert out["orderId"] == 123
    assert out["status"] == "FILLED"
