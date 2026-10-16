from __future__ import annotations

import importlib
from typing import Any


def load_strategy_class(strategy_name: str):
    module = importlib.import_module(f"strategies.{strategy_name}")
    strategy_cls = getattr(module, strategy_name, None)
    if strategy_cls is None:
        raise RuntimeError(f'Strategy class "{strategy_name}" was not found in strategies/{strategy_name}/__init__.py')
    return strategy_cls


def strategy_wants_entry(strategy_cls: type, instance: Any | None = None) -> tuple[bool, str]:
    strategy = instance or strategy_cls()
    want_long = bool(strategy.should_long())
    want_short = bool(strategy.should_short())
    if want_long:
        return True, "long"
    if want_short:
        return True, "short"
    return False, "flat"
