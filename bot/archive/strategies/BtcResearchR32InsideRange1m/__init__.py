from strategies.BtcResearchR32SpecialistBase1m import BtcResearchR32SpecialistBase1m


def containment_event(rows, now, require_inside):
    """Resolve one fixed B2 mother after B1; no stored or deferred episode."""
    mother, prior, current = rows[-3:]
    high, low = float(mother[3]), float(mother[4])
    inside = bool(float(prior[3]) < high and float(prior[4]) > low)
    close_inside = bool(low < float(prior[2]) < high)
    if not high > low or not close_inside or (require_inside and not inside):
        return None
    close = float(current[2])
    direction = 1 if close > high else -1 if close < low else 0
    if direction == 0:
        return None
    # The close resolves even a bar that traded beyond both mother boundaries.
    return dict(direction=direction, meta=dict(
        mother_at=int(mother[0]), prior_at=int(prior[0]), resolution_at=now,
        mother_high=high, mother_low=low, prior_close=float(prior[2]),
        prior_inside=inside, resolution_close=close))


class BtcResearchR32InsideRange1m(BtcResearchR32SpecialistBase1m):
    LABEL = "C_INSIDE"
    HOLD_HOURS = 24
    TP_R = None

    def _event(self, rows, now):
        return containment_event(rows, now, True)
