"""Quadratic equation solver."""
import math


def solve_quadratic(a, b, c):
    """Return ``(root1, root2, message)`` for ``a*x**2 + b*x + c = 0``.

    ``message`` is ``None`` for two distinct roots, a description for equal
    roots, and ``ValueError`` is raised when both roots are imaginary.
    """
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = round((-b + math.sqrt(discriminant)) / (2 * a), 4)
        root2 = round((-b - math.sqrt(discriminant)) / (2 * a), 4)
        return root1, root2, None

    if discriminant == 0:
        root = -b / (2 * a)
        if root == -0:
            root = 0
        return root, root, "Two real and equal roots"

    raise ValueError("Roots are imaginary")