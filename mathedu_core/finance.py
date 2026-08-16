"""Simple and compound interest formulas."""


def simple_interest(principal, rate, time):
    """SI = (P * R * T) / 100, rounded to 2 decimal places."""
    return round((principal * rate * time) / 100, 2)


def compound_interest(principal, rate, time):
    """Return (compound interest, amount) rounded to 2 decimal places."""
    amount = principal * (1 + rate / 100) ** time
    return round(amount - principal, 2), round(amount, 2)