"""Small pricing helpers for a demo online shop."""


def apply_discount(price: float, percent: float) -> float:
    """Return price reduced by percent, rounded to cents."""
    return round(price * (1 - percent / 100), 2)
