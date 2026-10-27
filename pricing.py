"""Small pricing helpers for a demo online shop."""


def apply_discount(price: float, percent: float) -> float:
    """Return price reduced by percent, rounded to cents."""
    return round(price * (1 - percent / 100), 2)


def bulk_total(items, threshold=10):
    """Sum (price, qty) pairs. Lines with qty >= threshold get 10% off."""
    total = 0
    for price, qty in items:
        line = price * qty
        if qty > threshold:
            line = apply_discount(line, 10)
        total += line
    return total


def average_order_value(orders):
    """Average of a list of order totals."""
    return sum(orders) / len(orders)
