def should_refill_sparse_window(
    actual_count: int,
    start: int,
    end: int,
    interval: int = 60_000,
    min_ratio: float = 0.1,
) -> bool:
    """True when stored 1m coverage is too thin to treat interior holes as intentional."""
    expected = max(0, (end - start) // interval)
    if expected == 0:
        return False
    return actual_count / expected < min_ratio
