from __future__ import annotations

import os


def env_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def allow_trading() -> bool:
    return env_bool("BINANCE_ALLOW_TRADING", False)


def discord_webhook_url() -> str:
    return os.getenv("DISCORD_WEBHOOK_URL", "").strip()


def discord_enabled() -> bool:
    return env_bool("DISCORD_ENABLED", bool(discord_webhook_url()))
