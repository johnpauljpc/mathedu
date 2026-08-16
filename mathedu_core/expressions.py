"""Safe parsing and evaluation of user-supplied math expressions.

The old implementation used ``eval()`` on raw user input, which is a remote
code-execution vulnerability. This module instead parses input with sympy's
parser using a restricted namespace (no Python builtins), then compiles it to
a numeric callable with ``lambdify``.
"""
import math
import re

import sympy as sp
from sympy.parsing.sympy_parser import (
    convert_xor,
    parse_expr,
    standard_transformations,
)

X = sp.Symbol("x")

# Build a sympy namespace WITHOUT Python builtins so strings like
# ``__import__('os')`` cannot execute anything. Only sympy symbols/functions
# survive, and user variables are bound through ``local_dict``.
_SAFE_GLOBALS = {}
exec("from sympy import *", _SAFE_GLOBALS)  # noqa: S102 - restricted below
_SAFE_GLOBALS["__builtins__"] = {}

_TRANSFORMATIONS = standard_transformations + (convert_xor,)

# Math functions the parser is allowed to produce. Any other function name in
# the input (e.g. ``eval``, ``os``) is rejected, not executed.
_ALLOWED_FUNCTIONS = {
    "sin", "cos", "tan",
    "asin", "acos", "atan",
    "sinh", "cosh", "tanh",
    "log", "log10", "exp", "sqrt", "cbrt", "Abs",
}

# Namespace used when compiling the parsed expression to a numeric callable.
# Trig functions are evaluated in degrees to match the existing UX.
_LAMBDIFY_NAMESPACE = {
    "sin": lambda v: math.sin(math.radians(v)),
    "cos": lambda v: math.cos(math.radians(v)),
    "tan": lambda v: math.tan(math.radians(v)),
    "log": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "sqrt": math.sqrt,
    "cbrt": math.cbrt if hasattr(math, "cbrt") else (lambda v: v ** (1 / 3)),
    "abs": abs,
    "pi": math.pi,
    "E": math.e,
}


class ExpressionError(ValueError):
    """Raised when a user string cannot be turned into a valid function."""


def normalize_expression(expression):
    """Convert loose user input into a parseable string.

    - ``^`` becomes ``**``
    - compact function spellings (``sinx``, ``log10x``, ``e**x``) expand
    - any other standalone single letter is treated as the variable ``x``
    """
    expr = re.sub(r"\^", "**", expression)

    expr = re.sub(r"\bsinx\b", "sin(x)", expr)
    expr = re.sub(r"\bcosx\b", "cos(x)", expr)
    expr = re.sub(r"\btanx\b", "tan(x)", expr)
    expr = re.sub(r"\blog10x\b", "log(x, 10)", expr)
    expr = re.sub(r"\blogx\b", "log(x)", expr)
    expr = re.sub(r"\be\*\*x\b", "exp(x)", expr)

    # Remaining standalone single letters (y, z, a, ...) mean "x".
    expr = re.sub(r"\b[a-z]\b", "x", expr)

    return expr


def interpret_expression(expression):
    """Add implicit multiplication and exponents (``4x`` -> ``4*x``, ``x2`` -> ``x**2``)."""
    # Keep only the left-hand side of any "=" equation.
    match = re.search(r"([^=]+)", expression)
    if match:
        expression = match.group(0).strip()

    # 4x -> 4*x, 2.5x -> 2.5*x
    expression = re.sub(r"(\d*\.\d+|\d+)([a-zA-Z])", r"\1*\2", expression)
    # x2 -> x**2 (single letter followed by digits is an exponent)
    expression = re.sub(r"(\b[a-zA-Z])(\d+)", r"\1**\2", expression)

    return expression


def build_equation(expression):
    """Return a callable ``f(x)`` for a user string, or raise ExpressionError."""
    try:
        normalized = normalize_expression(expression.lower())
        interpreted = interpret_expression(normalized)
        parsed = parse_expr(
            interpreted,
            local_dict={"x": X},
            transformations=_TRANSFORMATIONS,
            global_dict=_SAFE_GLOBALS,
        )
    except Exception as err:  # noqa: BLE001 - any parse failure becomes a user-facing error
        raise ExpressionError(f"'{expression}' is not a valid equation") from err

    # Reject anything that is not a plain expression (e.g. an empty tuple).
    if not isinstance(parsed, sp.Basic):
        raise ExpressionError(f"'{expression}' is not a valid equation")

    unknown = parsed.free_symbols - {X}
    if unknown:
        raise ExpressionError(
            f"'{expression}' uses unknown variable(s): {sorted(s.name for s in unknown)}"
        )

    # Reject any function name outside the math whitelist.
    unknown_funcs = {a.func.__name__ for a in parsed.atoms(sp.Function)} - _ALLOWED_FUNCTIONS
    if unknown_funcs:
        raise ExpressionError(f"'{expression}' is not a valid equation")

    return sp.lambdify(X, parsed, modules=[_LAMBDIFY_NAMESPACE])