"""Bisection method for finding roots of continuous functions."""


def bisection_method(func, a, b, tolerance):
    """Find a root of ``func`` within ``[a, b]``.

    Returns a dict with the approximate root and the full iteration table:
    ``{"result", "other_results", "a", "b", "b_c", "func"}``.
    """
    a_list, b_list, b_c_list, func_list, other_results = [], [], [], [], []

    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        a_list.append(a)
        b_list.append(b)
        b_c_list.append(b - c)
        func_list.append(func(c))
        other_results.append(format(c, ".4f"))

        if func(c) == 0:
            a = b = c
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    result = (a + b) / 2
    a_list.append(a)
    b_list.append(b)
    b_c_list.append(b - result)
    func_list.append(func(result))
    other_results.append(format(result, ".4f"))

    return {
        "result": format(result, ".4f"),
        "other_results": other_results,
        "a": a_list,
        "b": b_list,
        "b_c": b_c_list,
        "func": func_list,
    }