"""Bracketing helper: does the function change sign across an interval?"""


def has_root_between(f, a, b):
    """Return True if ``f(a) * f(b) < 0`` (a root is bracketed)."""
    fa = f(float(a))
    fb = f(float(b))
    return fa * fb < 0