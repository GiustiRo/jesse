from __future__ import annotations

import hmac

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from jesse.services.auth import require_auth
from jesse.services.env import ENV_VALUES
from jesse.services.web import LoginRequestJson
from jesse_live.switches import load_switches, save_switches

router = APIRouter(prefix="/arm", tags=["Arm"])


class SwitchesPatch(BaseModel):
    armed: bool | None = None
    allow_trading: bool | None = None


def _payload(switches: dict) -> dict:
    return {
        "armed": switches["armed"],
        "allow_trading": switches["allow_trading"],
    }


@router.get("/switches", dependencies=[Depends(require_auth)])
def get_switches():
    return JSONResponse(_payload(load_switches()))


@router.post("/unlock", dependencies=[Depends(require_auth)])
def unlock(json_request: LoginRequestJson):
    expected = ENV_VALUES.get("PASSWORD") or ""
    if not hmac.compare_digest(json_request.password, expected):
        return JSONResponse({"message": "Invalid password"}, status_code=401)
    return JSONResponse({"ok": True, **_payload(load_switches())})


@router.post("/switches", dependencies=[Depends(require_auth)])
def patch_switches(body: SwitchesPatch):
    if body.armed is None and body.allow_trading is None:
        return JSONResponse({"message": "No switches provided"}, status_code=400)
    return JSONResponse(_payload(save_switches(body.armed, body.allow_trading)))
