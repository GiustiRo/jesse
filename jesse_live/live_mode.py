from __future__ import annotations

import os
import time
import traceback

from jesse.config import config, set_config
from jesse.enums import live_session_statuses
from jesse.repositories import live_session_repository
from jesse.routes import router
from jesse.services import logger
from jesse.services.db import database
from jesse.services.failure import register_custom_exception_handler
from jesse.services.notifier import notify, start_notifier_loop
from jesse.services.redis import is_process_active
from jesse.store import store

from jesse_live.binance import BinanceFuturesClient
from jesse_live.discord import DiscordNotifier
from jesse_live.settings import allow_trading, discord_enabled, discord_webhook_url
from jesse_live.strategy_loader import load_strategy_class, strategy_wants_entry


def run(
    client_id,
    debug_mode,
    exchange,
    exchange_api_key_id,
    notification_api_key_id,
    conf,
    routes,
    data_routes,
    trading_mode,
):
    if database.is_closed():
        database.open_connection()

    config["app"]["debug_mode"] = bool(debug_mode)
    config["app"]["trading_mode"] = trading_mode

    live_conf = {
        "warm_up_candles": 240,
        "logging": config["env"]["logging"],
        "exchanges": {},
        "notifications": {"enabled": True, "events": {"errors": True, "opened_position": True, "updated_position": True}},
        "persistency": False,
        "generate_candles_from_1m": False,
    }
    if isinstance(conf, dict):
        live_conf.update(conf)
        live_conf.setdefault("exchanges", {})
        live_conf.setdefault("logging", config["env"]["logging"])
        live_conf.setdefault("notifications", {"enabled": True, "events": {}})
        live_conf.setdefault("warm_up_candles", 240)
        live_conf.setdefault("persistency", False)
        live_conf.setdefault("generate_candles_from_1m", False)
    set_config(live_conf)

    store.reset()
    store.app.set_session_id(str(client_id))
    if exchange_api_key_id:
        store.app.set_exchange_api_key(str(exchange_api_key_id))
    if notification_api_key_id:
        store.app.set_notifications_api_key(str(notification_api_key_id))

    router.initiate(routes or [], data_routes or [])
    register_custom_exception_handler()
    start_notifier_loop()

    live_session_repository.update_live_session_status(str(client_id), live_session_statuses.RUNNING)

    strategy_names = [route.strategy_name for route in router.routes if route.strategy_name]
    symbol = router.routes[0].symbol if router.routes else os.getenv("BINANCE_SYMBOL", "BTC-USDT")
    timeframe = router.routes[0].timeframe if router.routes else "4h"
    trading_enabled = allow_trading() and trading_mode == "livetrade"

    logger.info(
        f"OSS live adapter started exchange={exchange} symbol={symbol} "
        f"timeframe={timeframe} strategies={strategy_names or ['Idle']} "
        f"allow_trading={trading_enabled} paper={trading_mode != 'livetrade'}",
        send_notification=True,
    )
    notify(
        "Jesse live session started\n"
        f"exchange={exchange}\n"
        f"symbol={symbol}\n"
        f"strategies={', '.join(strategy_names) or 'Idle'}\n"
        f"allow_trading={trading_enabled}"
    )

    fallback_discord = DiscordNotifier(
        discord_webhook_url(),
        enabled=discord_enabled() and not store.app.notifications_api_key,
    )
    try:
        fallback_discord.send_message(
            "Jesse live session started",
            [f"exchange={exchange}", f"symbol={symbol}", f"allow_trading={trading_enabled}"],
        )
    except Exception as exc:
        logger.error(f"Discord fallback failed: {exc}", send_notification=False)

    client = _build_binance_client()
    strategy_classes = []
    for name in strategy_names:
        try:
            strategy_classes.append((name, load_strategy_class(name)))
        except Exception as exc:
            logger.error(f"Could not load strategy {name}: {exc}")

    try:
        client.ping()
        price = client.ticker_price(symbol)
        balance = client.account_balance_usdt()
        logger.info(f"Binance connected price={price} usdt_balance={balance}", send_notification=True)

        while is_process_active(str(client_id)):
            price = client.ticker_price(symbol)
            wanted = False
            side = "flat"
            for name, strategy_cls in strategy_classes:
                wanted, side = strategy_wants_entry(strategy_cls)
                if wanted:
                    logger.info(f"Strategy {name} signal={side} ignored_by_idle_or_gate={not trading_enabled}")
                    if trading_enabled:
                        logger.error(
                            f"ALLOW_TRADING is true but order routing is not implemented yet. Signal={side}"
                        )
                    break
            logger.info(f"heartbeat symbol={symbol} price={price} signal={side} trading={trading_enabled}")
            time.sleep(30)
    except Exception:
        logger.error(traceback.format_exc())
        live_session_repository.store_live_session_exception(
            str(client_id),
            "live adapter crashed",
            traceback.format_exc(),
        )
        live_session_repository.update_live_session_status(str(client_id), live_session_statuses.STOPPED)
        raise
    finally:
        fallback_discord.close()
        client.close()
        live_session_repository.update_live_session_status(str(client_id), live_session_statuses.STOPPED)
        live_session_repository.update_live_session_finished(str(client_id))
        logger.info("OSS live adapter stopped", send_notification=True)
        if database.is_open():
            database.close_connection()


def _build_binance_client() -> BinanceFuturesClient:
    api_key = ""
    api_secret = ""
    if store.app.exchange_api_key is not None:
        api_key = store.app.exchange_api_key.api_key
        api_secret = store.app.exchange_api_key.api_secret
    api_key = api_key or os.getenv("BINANCE_API_KEY", "")
    api_secret = api_secret or os.getenv("BINANCE_API_SECRET", "")
    return BinanceFuturesClient(api_key=api_key, api_secret=api_secret)
