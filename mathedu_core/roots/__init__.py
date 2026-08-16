"""Numerical root-finding algorithms."""
from .bisection import bisection_method
from .newton_raphson import newton_raphson_method
from .sign_change import has_root_between
from .successive_approx import successive_approximation

__all__ = [
    "bisection_method",
    "newton_raphson_method",
    "has_root_between",
    "successive_approximation",
]