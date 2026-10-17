"""Decide which live sessions should come back after a dashboard restart."""

from __future__ import annotations

WANTED_ALIVE_KEY = "wanted_alive"
INTERRUPTED_STATUSES = {"running", "starting"}


def wanted_alive(state: dict | None) -> bool | None:
    if not isinstance(state, dict) or WANTED_ALIVE_KEY not in state:
        return None
    return bool(state[WANTED_ALIVE_KEY])


def should_resume(status: str | None, state: dict | None) -> bool:
    """Resume unless the session was a draft or stopped from the Live tab."""
    if status == "draft":
        return False
    flag = wanted_alive(state)
    if flag is False:
        return False
    if flag is True:
        return True
    return status in INTERRUPTED_STATUSES


def merge_wanted_alive(new_state: dict | None, previous_state: dict | None) -> dict:
    state = dict(new_state or {})
    if WANTED_ALIVE_KEY not in state and isinstance(previous_state, dict) and WANTED_ALIVE_KEY in previous_state:
        state[WANTED_ALIVE_KEY] = previous_state[WANTED_ALIVE_KEY]
    return state


def start_args_from_state(session_id: str, session_mode: str | None, exchange: str | None, state: dict | None) -> dict | None:
    form = (state or {}).get("form") if isinstance(state, dict) else None
    if not isinstance(form, dict):
        return None
    routes = form.get("routes") or []
    resolved_exchange = form.get("exchange") or exchange
    if not routes or not resolved_exchange:
        return None
    paper_mode = bool(form.get("paper_mode", session_mode == "papertrade"))
    return {
        "id": str(session_id),
        "config": form.get("config") or {},
        "exchange": resolved_exchange,
        "exchange_api_key_id": form.get("exchange_api_key_id") or "",
        "notification_api_key_id": form.get("notification_api_key_id") or "",
        "routes": routes,
        "data_routes": form.get("data_routes") or [],
        "debug_mode": bool(form.get("debug_mode", False)),
        "paper_mode": paper_mode,
    }
