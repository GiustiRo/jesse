from __future__ import annotations

import os


def env_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def allow_trading() -> bool:
    from jesse_live.switches import allow_trading as switches_allow_trading

    return switches_allow_trading()


def is_armed() -> bool:
    from jesse_live.switches import is_armed as switches_is_armed

    return switches_is_armed()


def allocation_pct() -> float:
    raw = os.getenv("BINANCE_ALLOCATION_PCT", "10")
    try:
        value = float(raw)
    except (TypeError, ValueError):
        return 10.0
    return min(100.0, max(1.0, value))


def discord_webhook_url() -> str:
    return os.getenv("DISCORD_WEBHOOK_URL", "").strip()


def discord_enabled() -> bool:
    return env_bool("DISCORD_ENABLED", bool(discord_webhook_url()))
