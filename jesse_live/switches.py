"""Live arming switches persisted on disk so they survive without a container restart.

The live worker is a separate process from the dashboard, so env vars cannot be
the source of truth. Both processes read this JSON file.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

DEFAULTS = {"armed": True, "allow_trading": True}


def _storage_dir() -> Path:
    env_file = os.getenv("JESSE_ENV_FILE")
    if env_file:
        return Path(env_file).resolve().parent / "storage"
    return Path.cwd() / "storage"


def switches_path() -> Path:
    return _storage_dir() / "trading_switches.json"


def load_switches() -> dict:
    path = switches_path()
    if not path.exists():
        return dict(DEFAULTS)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return dict(DEFAULTS)
    if not isinstance(data, dict):
        return dict(DEFAULTS)
    return {
        "armed": bool(data.get("armed", DEFAULTS["armed"])),
        "allow_trading": bool(data.get("allow_trading", DEFAULTS["allow_trading"])),
    }


def save_switches(armed: bool | None = None, allow_trading: bool | None = None) -> dict:
    current = load_switches()
    if armed is not None:
        current["armed"] = bool(armed)
    if allow_trading is not None:
        current["allow_trading"] = bool(allow_trading)
    path = switches_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(current, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)
    return current


def is_armed() -> bool:
    return load_switches()["armed"]


def allow_trading() -> bool:
    return load_switches()["allow_trading"]
