import math 

def newton_raphson(f, initial_guess, tolerance=1e-6, max_iterations=100, delta=1e-8):
    x = initial_guess
    iteration = 0

    def numerical_derivative(x):
        return (f(x + delta) - f(x)) / delta

    while abs(f(x)) > tolerance and iteration < max_iterations:
        x = x - f(x) / numerical_derivative(x)
        iteration += 1

    if abs(f(x)) <= tolerance:
        return x
    else:
        raise ValueError("Newton-Raphson method did not converge within the specified number of iterations.")

# Example usage with a different equation
def equation1(x):
    print(type(math.cos(x) - 3*x + 5))
    return math.cos(x) - 3*x + 5

# Example usage
initial_guess = 2.0  # You can change the initial guess
solution = newton_raphson(equation1, initial_guess)

print("Approximate solution:", solution)
