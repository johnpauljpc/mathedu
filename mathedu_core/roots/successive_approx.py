"""Successive approximation (bisection-style bracketing) method."""


def successive_approximation(f, a, b, tol, max_iter):
    """Find a root of ``f`` within ``[a, b]`` by repeated midpoint sampling.

    Returns ``{"result", "other_results"}``.
    """
    for _ in range(max_iter):
        x = (a + b) / 2.0
        if abs(f(x)) < tol:
            return {"result": format(x, ".4f"), "other_results": None}
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

    return {
        "result": f"Root not found within maximum iterations ({max_iter}).",
        "other_results": None,
    }