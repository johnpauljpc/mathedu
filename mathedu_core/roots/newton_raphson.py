"""Newton-Raphson method with a central-difference derivative."""


def newton_raphson_method(f, initial_guess, tolerance=1e-6, max_iterations=100, h=1e-6):
    """Find a root of ``f`` starting from ``initial_guess``.

    Returns a dict with the approximate root and the iteration table:
    ``{"result", "other_results", "e", "x_i", "fx", "fx1"}``.
    """
    def numerical_derivative(x):
        return (f(x + h) - f(x - h)) / (2 * h)

    x = initial_guess
    initials = initial_guess
    iteration = 0
    other_results = []
    x_i = [x]
    fx = []
    fx1 = []
    e = []

    while abs(f(x)) > tolerance and iteration < max_iterations:
        fx.append(f(x))
        initials = x
        fx1.append(numerical_derivative(x))
        x = x - f(x) / numerical_derivative(x)
        other_results.append(x)
        x_i.append(x)
        iteration += 1
        e.append(abs((x - initials) / x))

    if abs(f(x)) <= tolerance:
        other_results.append(x)
        fx.append(f(x))
        fx1.append(numerical_derivative(x))
        e.append(abs((x - initials) / x))
        return {
            "result": format(x, ".4f"),
            "other_results": other_results,
            "e": e,
            "x_i": x_i,
            "fx": fx,
            "fx1": fx1,
        }

    return {
        "result": "Newton-Raphson method did not converge within the specified number of iterations.",
        "other_results": None,
    }