from jesse_live.autostart import merge_wanted_alive, should_resume, start_args_from_state, wanted_alive


def test_manual_stop_does_not_resume():
    assert should_resume("stopped", {"wanted_alive": False, "form": {}}) is False
    assert wanted_alive({"wanted_alive": False}) is False


def test_wanted_alive_survives_status_stopped_after_crash():
    assert should_resume("stopped", {"wanted_alive": True}) is True


def test_running_without_flag_is_treated_as_power_cut():
    assert should_resume("running", {"form": {}}) is True
    assert should_resume("starting", None) is True


def test_old_stopped_session_without_flag_stays_stopped():
    assert should_resume("stopped", {"form": {}}) is False
    assert should_resume("draft", {"wanted_alive": True}) is False


def test_dashboard_save_keeps_wanted_alive():
    merged = merge_wanted_alive({"form": {"exchange": "Binance Perpetual Futures"}}, {"wanted_alive": True})
    assert merged["wanted_alive"] is True
    overwritten = merge_wanted_alive({"wanted_alive": False, "form": {}}, {"wanted_alive": True})
    assert overwritten["wanted_alive"] is False


def test_start_args_require_routes_and_exchange():
    assert start_args_from_state("abc", "livetrade", "Binance Perpetual Futures", {"form": {}}) is None
    args = start_args_from_state(
        "abc",
        "livetrade",
        "",
        {
            "form": {
                "exchange": "Binance Perpetual Futures",
                "exchange_api_key_id": "key-1",
                "routes": [{"symbol": "BTC-USDT", "timeframe": "1h", "strategy": "TemaTrendFollowing"}],
                "data_routes": [{"symbol": "BTC-USDT", "timeframe": "4h"}],
                "debug_mode": True,
                "paper_mode": False,
                "config": {"warm_up_candles": 240},
            }
        },
    )
    assert args["id"] == "abc"
    assert args["exchange"] == "Binance Perpetual Futures"
    assert args["paper_mode"] is False
    assert args["debug_mode"] is True
    assert args["routes"][0]["timeframe"] == "1h"
    assert args["data_routes"][0]["timeframe"] == "4h"
