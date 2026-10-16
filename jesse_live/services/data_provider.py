from __future__ import annotations


def get_logs(session_id: str, log_type: str, start_time: int):
    from jesse.models.Log import Log
    from jesse.services.db import database

    if database.is_closed():
        database.open_connection()

    type_code = 2 if log_type == "error" else 1
    rows = (
        Log.select()
        .where(
            (Log.session_id == session_id)
            & (Log.type == type_code)
            & (Log.timestamp >= int(start_time or 0))
        )
        .order_by(Log.timestamp.asc())
    )
    return [
        {
            "id": str(row.id),
            "session_id": str(row.session_id),
            "timestamp": row.timestamp,
            "message": row.message,
        }
        for row in rows
    ]


def get_orders(session_id: str):
    from jesse.models.Order import Order
    from jesse.services.db import database
    from jesse.services.transformers import get_order_details

    if database.is_closed():
        database.open_connection()

    rows = Order.select().where(Order.session_id == session_id).order_by(Order.created_at.desc())
    return [get_order_details(row) for row in rows]
