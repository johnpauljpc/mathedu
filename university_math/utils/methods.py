import math


def bisection_method(func, a, b, tolerance):
    other_results = []
    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        other_results.append(c)

        if func(c) == 0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    result = (a + b) / 2
    return {"result":result, "other_results":other_results }


# Raphson method
import sympy as sp

def newton_raphson_method(func, func_derivative, initial_guess, tolerance, max_iterations=100):
    results = []

    x = initial_guess

    for _ in range(max_iterations):
        if abs(func(x)) < tolerance:
            return {"result": x, "other_results": results}

        results.append(x)

        x = x - func(x) / func_derivative(x)

    return {"result": x, "other_results": results}

# Example usage:
x = sp.symbols('x')

# Define the function and its derivative symbolically
equation = x**3 - 4*x - 8.95
equation_derivative = sp.diff(equation, x)

# Convert the symbolic functions to Python functions
func = sp.lambdify(x, equation)
func_derivative = sp.lambdify(x, equation_derivative)

initial_guess = 3.0  # Initial guess
tolerance = 0.0333  # Tolerance

result = newton_raphson_method(func, func_derivative, initial_guess, tolerance)
print(f"Root found: {result['result']}")
print(f"Other results: {result['other_results']}")



# Successive method
# def successive_approximation_method(func, initial_guess, tolerance, max_iterations=100):
#     results = []

#     x = initial_guess

#     for _ in range(max_iterations):
#         if abs(func(x) - x) < tolerance:
#             return {"result": x, "other_results": results}

#         results.append(x)

#         x = func(x)

#     return {"result": x, "other_results": results}

# # Example usage:
# def equation(x):
#     return x**2 - 4

# initial_guess = 2.0  # Initial guess
# tolerance = 1e-6  # Tolerance

# result = successive_approximation_method(equation, initial_guess, tolerance)
# print(f"Root found: {result['result']}")
# print(f"Other results: {result['other_results']}")


