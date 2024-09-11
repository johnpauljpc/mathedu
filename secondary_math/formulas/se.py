from sympy import symbols, Eq, solve

def solve_simultaneous_equations(equation1, equation2):
    # Define symbols
    x, y = symbols('x y')

    # Parse equations
    eq1 = Eq(eval(equation1.replace('=', '-(') + ')'))
    eq2 = Eq(eval(equation2.replace('=', '-(') + ')'))

    # Solve equations
    solution = solve((eq1, eq2), (x, y))
    
    return solution

# Sample input equations
equation1 = "2*x + 3*y = 8"
equation2 = "4*x - 2*y = 6"

# Solve equations
solution = solve_simultaneous_equations(equation1, equation2)
print("Solution:", solution)
