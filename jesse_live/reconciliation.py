"""Reconcile only fills belonging to this session; never adopt an account position.

The REST adapter has no user-data stream. Batch validation against positionRisk
prevents its local position from staying flat after a fill, or from silently
claiming a manual/other-bot trade. In-flight fills can race reads; mismatches block
new exposure and are retried on the next loop instead of fabricating a position.
"""

import math
from decimal import Decimal
from itertools import groupby

import jesse.helpers as jh
from jesse.enums import order_types
from jesse.services import order_service, position_service
from jesse.store import store


TERMINAL_CANCEL = {'CANCELED', 'CANCELLED', 'EXPIRED', 'EXPIRED_IN_MATCH', 'REJECTED'}


def venue_position(client, symbol: str) -> dict:
    rows = client.position_information(symbol)
    if not isinstance(rows, list):
        raise ValueError('Invalid Binance position-risk response')
    expected_symbol = client.to_binance_symbol(symbol)
    if any(row.get('symbol') != expected_symbol for row in rows):
        raise ValueError('Unexpected position-risk instrument')
    if len(rows) > 1 or any(row.get('positionSide') != 'BOTH' for row in rows):
        raise ValueError('Funding live reconciliation requires one-way position mode')
    if not rows:
        return {'qty': 0.0, 'entry_price': 0.0, 'liquidation_price': 0.0, 'mark_price': None}
    row = rows[0]
    result = {'qty': float(row['positionAmt']), 'entry_price': float(row['entryPrice']),
              'liquidation_price': float(row['liquidationPrice']), 'mark_price': float(row['markPrice'])}
    if (not all(math.isfinite(value) for value in result.values())
            or result['mark_price'] <= 0 or result['entry_price'] < 0
            or (result['qty'] != 0 and result['entry_price'] <= 0)):
        raise ValueError('Invalid Binance position-risk quantities or prices')
    return result


def require_flat_start(client, symbol: str) -> None:
    # Automatic adoption/restoration needs persisted ownership of orders/trades.
    # This adapter deliberately refuses it instead of sharing another position.
    mode = client.position_mode()
    if not isinstance(mode, dict) or mode.get('dualSidePosition') is not False:
        raise ValueError('Funding/OI live startup requires confirmed one-way position mode')
    if venue_position(client, symbol)['qty'] != 0:
        raise ValueError('Funding/OI live startup requires a flat BTC position; existing positions need explicit recovery')
    if client.open_orders(symbol):
        raise ValueError('Funding/OI live startup requires no pre-existing BTC orders; refusing to claim or cancel them')


def _add_qty(quantity: float, delta: float) -> float:
    # Binance quantities are decimal lot sizes. Float subtraction such as
    # .3-.1-.2 must not invent a tiny short or prevent a native close hook.
    return float(Decimal(str(quantity)) + Decimal(str(delta)))


def _entry_after(old_qty: float, old_entry: float, delta: float, price: float) -> float:
    new_qty = _add_qty(old_qty, delta)
    if new_qty == 0:
        return 0.0
    if old_qty == 0 or old_qty * new_qty < 0:
        return price
    if old_qty * delta > 0:
        return (abs(old_qty) * old_entry + abs(delta) * price) / abs(new_qty)
    return old_entry


def _ordered_updates(updates: list, starting_qty: float) -> list:
    """A UUID is not a venue clock: prove tied fills from position constraints.

    An entry followed by its reduce-only exit is uniquely ordered when starting
    flat. If several orders are feasible at the same millisecond, a REST order
    snapshot cannot prove their lifecycle order; reject before invoking hooks.
    """
    result = []
    quantity = starting_qty
    updates = sorted(updates, key=lambda update: update[0])
    for _, group in groupby(updates, key=lambda update: update[0]):
        pending = list(group)
        while pending:
            eligible = [update for update in pending if (
                not update[1].reduce_only
                or (quantity * update[4] < 0 and abs(update[4]) <= abs(quantity) + 1e-9)
            )]
            if not eligible:
                raise ValueError('Venue fill order violates reduce-only position constraints')
            if len(eligible) > 1:
                raise ValueError('Ambiguous same-millisecond venue fills; lifecycle ordering requires trade history')
            update = eligible[0]
            result.append(update)
            quantity = _add_qty(quantity, update[4])
            pending.remove(update)
    return result


def synchronize_fills(client, exchange: str, symbol: str) -> dict:
    position = store.positions.get_position(exchange, symbol)
    if position is None:
        raise ValueError('Missing initialized live position')
    updates = []
    cancellations = []
    for order in list(store.orders.get_active_orders(exchange, symbol)):
        if not order.is_cancellable or not order.exchange_id:
            continue
        options = {'is_algo': True} if order.type == order_types.STOP else {}
        remote = client.get_order(symbol, str(order.exchange_id), **options)
        status = str(remote.get('status') or '').upper()
        cumulative = abs(float(remote.get('executedQty') or 0))
        previous = getattr(order, '_live_applied_qty', abs(order.filled_qty or 0))
        if not math.isfinite(cumulative) or cumulative < previous or cumulative > abs(order.qty) + 1e-9:
            raise ValueError('Invalid or decreasing cumulative venue fill')
        if cumulative > previous:
            average = float(remote.get('avgPrice') or remote.get('price') or order.price)
            if not math.isfinite(average) or average <= 0:
                raise ValueError('Invalid venue execution price')
            prior_notional = getattr(order, '_live_cumulative_notional', previous * order.price)
            notional = cumulative * average
            incremental_price = (notional - prior_notional) / (cumulative - previous)
            if not math.isfinite(incremental_price) or incremental_price <= 0:
                raise ValueError('Invalid incremental venue execution price')
            incremental_qty = float(Decimal(str(cumulative)) - Decimal(str(previous)))
            delta = jh.prepare_qty(incremental_qty, order.side)
            updates.append((int(remote.get('updateTime') or 0), order, status, cumulative,
                            delta, incremental_price, average, notional))
        if status in TERMINAL_CANCEL:
            cancellations.append(order)
    updates = _ordered_updates(updates, position.qty)
    actual = venue_position(client, symbol)
    expected_qty = position.qty
    expected_entry = float(position.entry_price or 0)
    for _, _, _, _, delta, price, _, _ in updates:
        expected_entry = _entry_after(expected_qty, expected_entry, delta, price)
        expected_qty = _add_qty(expected_qty, delta)
    # Quantities/weighted prices are serialized decimal strings at the venue.
    # These tolerances cover float conversion, not a second trader's exposure.
    if not math.isclose(expected_qty, actual['qty'], rel_tol=1e-9, abs_tol=1e-9):
        raise ValueError('Unexplained venue position change; refusing to adopt external exposure')
    if (actual['qty'] != 0 and not math.isclose(expected_entry, actual['entry_price'],
                                             rel_tol=1e-8, abs_tol=1e-8)):
        raise ValueError('Venue entry price does not match this session fills')
    for _, order, status, cumulative, delta, price, average, notional in updates:
        new_entry = _entry_after(position.qty, float(position.entry_price or 0), delta, price)
        position_service.update_from_stream(position, {
            'qty': _add_qty(position.qty, delta), 'entry_price': new_entry,
            'liquidation_price': actual['liquidation_price'],
        }, is_initial=False)
        if actual['mark_price'] is not None:
            position._mark_price = actual['mark_price']
        order.filled_qty = jh.prepare_qty(cumulative, order.side)
        order.price = price
        if status == 'FILLED':
            order_service.execute_order(order)
        else:
            order_service.execute_order_partially(order)
        # A partial event records its incremental VWAP; the visible order retains
        # the venue's cumulative VWAP for subsequent polls and persistence.
        order.price = average
        order._live_applied_qty = cumulative
        order._live_cumulative_notional = notional
    for order in cancellations:
        order_service.cancel_order(order)
    return {'status': 'ready', 'fills_applied': len(updates), 'position_qty': actual['qty'],
            'observed_at': jh.now_to_timestamp(), 'error': None}


def cancel_pending_entries(client, exchange: str, symbol: str) -> dict:
    """Individually cancel entries; confirm outcomes, leave protective exits alone.

    A cancellation can race a full/partial fill. No local fill/cancel is inferred
    from a failed DELETE: synchronize_fills subsequently verifies the venue state.
    """
    result = {'pending_count': 0, 'canceled_count': 0, 'race_fill_count': 0, 'errors': []}
    for order in list(store.orders.get_active_orders(exchange, symbol)):
        if order.reduce_only or not order.is_cancellable:
            continue
        if getattr(order, '_input_cancel_confirmed', False):
            continue
        if not order.exchange_id:
            order_service.cancel_order(order)
            result['canceled_count'] += 1
            continue
        try:
            try:
                options = {'is_algo': True} if order.type == order_types.STOP else {}
                client.cancel_order(symbol, str(order.exchange_id), **options)
            except Exception:
                # Already filled/canceled is common; a signed read establishes
                # the outcome without retrying or canceling unrelated orders.
                pass
            options = {'is_algo': True} if order.type == order_types.STOP else {}
            remote = client.get_order(symbol, str(order.exchange_id), **options)
            status = str(remote.get('status') or '').upper()
            filled = abs(float(remote.get('executedQty') or 0))
            if status in TERMINAL_CANCEL:
                order._input_cancel_confirmed = True
                result['canceled_count'] += 1
                if filled:
                    result['race_fill_count'] += 1
            elif status == 'FILLED':
                order._input_cancel_confirmed = True
                result['race_fill_count'] += 1
            else:
                result['pending_count'] += 1
        except Exception as exc:
            result['pending_count'] += 1
            result['errors'].append({'order_id': str(order.id), 'category': type(exc).__name__})
    return result
