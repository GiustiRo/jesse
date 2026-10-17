from __future__ import annotations

import os
import time
import traceback

import jesse.helpers as jh
from jesse.config import config, set_config
from jesse.enums import exchanges, live_session_statuses
from jesse.modes.backtest_mode import _prepare_routes
from jesse.repositories import live_session_repository
from jesse.routes import router
from jesse.services import candle_service, exchange_service, logger, order_service, position_service
from jesse.services.db import database
from jesse.services.failure import register_custom_exception_handler
from jesse.services.notifier import notify, start_notifier_loop
from jesse.services.redis import is_process_active, sync_publish
from jesse.store import store

from jesse_live.binance import BinanceFuturesClient
from jesse_live.candles import closed_klines, inject_native_candles, last_timestamp
from jesse_live.chart import CHART_TIMEFRAMES, chart_routes, current_candles_map, trading_routes, update_forming
from jesse_live.discord import DiscordNotifier
from jesse_live.exchange import BinancePerpetualFuturesDriver
from jesse_live.settings import allocation_pct, allow_trading, discord_enabled, discord_webhook_url, is_armed


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
    config["app"]["live_drivers"][exchanges.BINANCE_PERPETUAL_FUTURES] = BinancePerpetualFuturesDriver
    jh.clear_config_caches()

    live_conf = {
        "warm_up_candles": 240,
        "logging": config["env"]["logging"],
        "exchanges": {},
        "notifications": {"enabled": True, "events": {"errors": True, "opened_position": True, "updated_position": True, "executed_orders": True}},
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
    jh.clear_config_caches()

    routes = trading_routes(_with_exchange(exchange, list(routes or [])))
    data_routes = _with_exchange(exchange, list(data_routes or []))
    data_routes = _ensure_4h_data_route(exchange, routes, data_routes)

    store.reset()
    store.app.set_session_id(str(client_id))
    if exchange_api_key_id:
        store.app.set_exchange_api_key(str(exchange_api_key_id))
    if notification_api_key_id:
        store.app.set_notifications_api_key(str(notification_api_key_id))

    router.initiate(routes, data_routes)
    jh.clear_config_caches()
    register_custom_exception_handler()
    start_notifier_loop()

    store.candles.init_storage(5000)
    exchange_service.initialize_exchanges_state()
    order_service.initialize_orders_state()
    position_service.initialize_positions_state()

    live_session_repository.update_live_session_status(str(client_id), live_session_statuses.RUNNING)

    symbol = router.routes[0].symbol if router.routes else os.getenv("BINANCE_SYMBOL", "BTC-USDT")
    timeframe = router.routes[0].timeframe if router.routes else "15m"
    strategy_names = [route.strategy_name for route in router.routes if route.strategy_name]
    logger.info(
        f"OSS live adapter started exchange={exchange} symbol={symbol} "
        f"timeframe={timeframe} strategies={strategy_names or ['Idle']} "
        f"armed={is_armed()} allow_trading={allow_trading()} "
        f"paper={trading_mode != 'livetrade'} allocation_pct={allocation_pct()}",
        send_notification=True,
    )
    notify(
        "Jesse live session started\n"
        f"exchange={exchange}\n"
        f"symbol={symbol}\n"
        f"timeframe={timeframe}\n"
        f"strategies={', '.join(strategy_names) or 'Idle'}\n"
        f"armed={is_armed()}\n"
        f"allow_trading={allow_trading()}\n"
        f"allocation_pct={allocation_pct()}"
    )

    fallback_discord = DiscordNotifier(
        discord_webhook_url(),
        enabled=discord_enabled() and not store.app.notifications_api_key,
    )
    try:
        fallback_discord.send_message(
            "Jesse live session started",
            [
                f"exchange={exchange}",
                f"symbol={symbol}",
                f"timeframe={timeframe}",
                f"armed={is_armed()}",
                f"allow_trading={allow_trading()}",
                f"allocation_pct={allocation_pct()}",
            ],
        )
    except Exception as exc:
        logger.error(f"Discord fallback failed: {exc}", send_notification=False)

    client = _build_binance_client()
    try:
        _start_live_driver(exchange, client)
        _copy_precisions(exchange)
        client.ping()
        price = client.ticker_price(symbol)
        wallet = client.account_balance_usdt()
        allocated = _apply_wallet_allocation(exchange, wallet)
        logger.info(
            f"Binance connected price={price} usdt_wallet={wallet} allocated={allocated}",
            send_notification=True,
        )

        started_at = jh.now_to_timestamp()
        forming: dict = {}
        _warmup_candles(client, exchange, symbol)
        _publish_dashboard(exchange, symbol, allocated, started_at, price, forming)
        logger.info("Initializing strategy")
        _prepare_routes(with_candles_pipeline=False)
        logger.info("Live session ready")
        _publish_dashboard(exchange, symbol, allocated, started_at, price, forming)

        last_armed = is_armed()
        last_allow = allow_trading()
        consecutive_errors = 0
        last_minute = None
        last_price = price
        while is_process_active(str(client_id)):
            loop_started = time.monotonic()
            armed = is_armed()
            trading = allow_trading()
            if armed != last_armed or trading != last_allow:
                logger.info(
                    f"Arm switches changed armed={armed} allow_trading={trading}",
                    send_notification=True,
                )
                last_armed, last_allow = armed, trading
            try:
                last_price = client.ticker_price(symbol)
                allocated = _apply_wallet_allocation(exchange, client.account_balance_usdt())
                now_ms = jh.now_to_timestamp()
                minute = now_ms // 60_000
                if minute != last_minute:
                    new_trading_candle = _refresh_candles(client, exchange, symbol, timeframe)
                    last_minute = minute
                    if new_trading_candle and armed:
                        for route in router.routes:
                            if route.strategy is not None:
                                route.strategy._execute()
                _sync_fills(client, exchange, symbol)
                consecutive_errors = 0
            except Exception:
                consecutive_errors += 1
                logger.error(
                    f"Live loop error ({consecutive_errors}): {traceback.format_exc()}",
                    send_notification=consecutive_errors == 1,
                )
            _publish_dashboard(exchange, symbol, allocated, started_at, last_price, forming)
            time.sleep(max(0.0, 1.0 - (time.monotonic() - loop_started)))
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


def _dashboard_routes() -> list:
    routes = [
        {
            "exchange": route.exchange,
            "symbol": route.symbol,
            "timeframe": route.timeframe,
            "strategy": route.strategy_name,
        }
        for route in router.routes
    ]
    return chart_routes(routes)


def _publish_dashboard(
    exchange: str,
    symbol: str,
    allocated: float,
    started_at: int,
    price: float | None = None,
    forming: dict | None = None,
) -> None:
    """The Live tab stays on 'Starting trading session…' until general_info arrives."""
    try:
        now_ms = jh.now_to_timestamp()
        px = float(price or 0)
        if forming is not None and px > 0:
            timeframes = list(dict.fromkeys([
                *CHART_TIMEFRAMES,
                *list(config["app"].get("considering_timeframes") or []),
            ]))
            for timeframe in timeframes:
                update_forming(forming, timeframe, px, now_ms)
            sync_publish("current_candles", current_candles_map(exchange, symbol, forming, timeframes))

        positions = _position_payloads(exchange, symbol, px)
        orders = _order_payloads(exchange, symbol)
        open_positions = sum(1 for row in positions if row.get("type") != "close")
        pnl = sum(float(row.get("pnl") or 0) for row in positions)
        pnl_perc = sum(float(row.get("pnl_perc") or 0) for row in positions)
        info_logs = getattr(store.logs, "info", [])
        error_logs = getattr(store.logs, "errors", [])
        started_balance = float(allocated or 0)
        accounting = store.exchanges.get_exchange(exchange)
        if accounting is not None and getattr(accounting, "_started_balance", None):
            started_balance = float(accounting._started_balance)
        current_balance = started_balance + pnl

        sync_publish("progressbar", {
            "message": "Live session running",
            "current": 1,
            "total": 1,
            "indeterminate": False,
            "estimated_remaining_seconds": 0,
        })
        sync_publish("positions", positions)
        sync_publish("orders", orders)
        sync_publish("equity_snapshot", {
            "timestamp": now_ms,
            "equity": current_balance,
            "currency": jh.quote_asset(symbol) if symbol else "USDT",
        })
        sync_publish("general_info", {
            "started_at": int(started_at or 0),
            "current_time": now_ms,
            "started_balance": started_balance,
            "current_balance": current_balance,
            "available_margin": allocated,
            "count_error_logs": len(error_logs),
            "count_info_logs": len(info_logs),
            "count_active_orders": len([
                order for order in orders if order.get("status") in {"ACTIVE", "QUEUED"}
            ]),
            "open_positions": open_positions,
            "pnl": pnl,
            "pnl_perc": pnl_perc,
            "count_trades": int(getattr(store.closed_trades, "count", 0) or 0),
            "count_winning_trades": 0,
            "count_losing_trades": 0,
            "leverage": 1,
            "exchange": exchange,
            "routes": _dashboard_routes(),
        })
    except Exception as exc:
        logger.error(f"dashboard publish failed: {exc}", send_notification=False)


def _position_payloads(exchange: str, symbol: str, price: float) -> list[dict]:
    position = store.positions.get_position(exchange, symbol)
    if position is None or not position.is_open:
        return []
    if price:
        position.current_price = price
    qty = abs(float(position.qty or 0))
    try:
        pnl = float(position.pnl or 0)
    except Exception:
        pnl = 0.0
    try:
        pnl_perc = float(position.pnl_percentage or 0)
        if pnl_perc != pnl_perc:
            pnl_perc = 0.0
    except Exception:
        pnl_perc = 0.0
    return [{
        "symbol": position.symbol,
        "type": position.type,
        "qty": qty,
        "value": float(position.value or 0),
        "currency": jh.quote_asset(symbol),
        "entry": float(position.entry_price or 0),
        "current_price": float(position.current_price or price or 0),
        "liquidation_price": position._liquidation_price,
        "pnl": pnl,
        "pnl_perc": pnl_perc,
    }]


def _order_payloads(exchange: str, symbol: str) -> list[dict]:
    from jesse.services import transformers

    return [
        transformers.get_order_details(order)
        for order in store.orders.get_orders(exchange, symbol)
    ]


def _with_exchange(exchange: str, items: list) -> list:
    """Dashboard live routes omit exchange; Jesse's router requires it on every row."""
    filled = []
    for item in items:
        if not isinstance(item, dict):
            filled.append(item)
            continue
        row = dict(item)
        row.setdefault("exchange", exchange)
        filled.append(row)
    return filled


def _ensure_4h_data_route(exchange: str, routes: list, data_routes: list) -> list:
    existing = []
    for item in list(routes) + list(data_routes):
        if isinstance(item, dict):
            existing.append((item.get("exchange") or exchange, item.get("symbol"), item.get("timeframe")))
    if any(timeframe == "4h" for _ex, _sym, timeframe in existing):
        return data_routes
    if not routes:
        return data_routes
    first = routes[0]
    data_routes.append({
        "exchange": first.get("exchange") or exchange,
        "symbol": first.get("symbol") or os.getenv("BINANCE_SYMBOL", "BTC-USDT"),
        "timeframe": "4h",
    })
    return data_routes


def _build_binance_client() -> BinanceFuturesClient:
    api_key = ""
    api_secret = ""
    if store.app.exchange_api_key is not None:
        api_key = store.app.exchange_api_key.api_key
        api_secret = store.app.exchange_api_key.api_secret
    api_key = api_key or os.getenv("BINANCE_API_KEY", "")
    api_secret = api_secret or os.getenv("BINANCE_API_SECRET", "")
    return BinanceFuturesClient(api_key=api_key, api_secret=api_secret)


def _start_live_driver(exchange: str, signed_client: BinanceFuturesClient) -> None:
    # Import after trading_mode/live_drivers are set. jesse.services.api instantiates
    # API() at import time and would crash the dashboard POST /live otherwise.
    from jesse.services.api import api

    api.initiate_driver(exchange)
    for _ in range(50):
        if exchange in api.drivers:
            driver = api.drivers[exchange]
            old = getattr(driver, "client", None)
            driver.client = signed_client
            if old is not None and old is not signed_client:
                old.close()
            return
        time.sleep(0.1)
    raise RuntimeError(f"Live driver for {exchange} did not start")


def _copy_precisions(exchange: str) -> None:
    from jesse.services.api import api

    driver = api.drivers.get(exchange)
    accounting = store.exchanges.get_exchange(exchange)
    if driver is None or accounting is None:
        return
    accounting.vars["precisions"] = driver.vars.get("precisions", {})


def _apply_wallet_allocation(exchange: str, wallet: float | None) -> float:
    accounting = store.exchanges.get_exchange(exchange)
    total = float(wallet or 0)
    allocated = total * (allocation_pct() / 100.0)
    if allocated <= 0:
        allocated = 1000.0
    accounting._wallet_balance = allocated
    accounting._available_margin = allocated
    accounting._started_balance = allocated
    accounting.assets[accounting.settlement_currency] = allocated
    return allocated


def _warmup_candles(client: BinanceFuturesClient, exchange: str, symbol: str) -> None:
    timeframes = list(config["app"]["considering_timeframes"])
    for timeframe in timeframes:
        candles = closed_klines(client, symbol, timeframe, limit=500)
        inject_native_candles(exchange, symbol, timeframe, candles)
        logger.info(f"Loaded {len(candles)} {timeframe} candles for {symbol}")
    store.candles.initiated_pairs[f"{exchange}-{symbol}"] = True
    store.candles.are_all_initiated = True
    store.app.time = jh.now()


def _refresh_candles(client: BinanceFuturesClient, exchange: str, symbol: str, trading_timeframe: str) -> bool:
    new_trading = False
    for timeframe in config["app"]["considering_timeframes"]:
        candles = closed_klines(client, symbol, timeframe, limit=5)
        if len(candles) == 0:
            continue
        previous = last_timestamp(exchange, symbol, timeframe)
        candle_service.add_candle(
            candles[-1],
            exchange,
            symbol,
            timeframe,
            with_execution=False,
            with_generation=False,
            with_skip=False,
        )
        current = last_timestamp(exchange, symbol, timeframe)
        if timeframe == trading_timeframe and previous is not None and current is not None and current > previous:
            new_trading = True
            logger.info(f"New {timeframe} candle {symbol} close={candles[-1][2]}")
    store.app.time = jh.now()
    return new_trading


def _sync_fills(client: BinanceFuturesClient, exchange: str, symbol: str) -> None:
    if not allow_trading():
        return
    for order in store.orders.get_active_orders(exchange, symbol):
        if not order.exchange_id:
            continue
        try:
            remote = client.get_order(symbol, str(order.exchange_id))
        except Exception as exc:
            logger.error(f"Order poll failed id={order.exchange_id}: {exc}", send_notification=False)
            continue
        status = str(remote.get("status") or "")
        if status != "FILLED":
            continue
        order.filled_qty = float(remote.get("executedQty") or order.qty)
        avg = remote.get("avgPrice") or remote.get("price") or order.price
        order.price = float(avg)
        order_service.execute_order(order)
