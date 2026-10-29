"""Independent audit of previously reviewed observer; no market data queries."""
import importlib
import inspect
import json
import runpy
from pathlib import Path
import jesse.helpers as jh

def main():
    core = runpy.run_path("research_scripts/portfolio_roles/causal_multiscale_observer.py", run_name="audit_core")
    result = {"controls": core["self_test"]()}
    research = importlib.import_module("jesse.research")
    result["public_api"] = {
        "signature": str(inspect.signature(research.get_candles)),
        "doc": inspect.getdoc(research.get_candles),
        "query_performed": False
    }
    target = Path("research_scripts/fresh_structure_probability")
    target.mkdir(exist_ok=True)
    (target / "audit_api_controls.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    jh.debug(json.dumps(result))

if __name__ == "__main__":
    main()
