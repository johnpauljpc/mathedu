import sympy as sp
import math

# Define the symbol and the equation
def calculate_derivative(equation):
    x = sp.symbols('x')
    derivative = sp.diff(equation, x)
    return derivative
 

# Calculate the derivative


# Print the derivative
# print("The derivative of the equation {} is: {}".format(equation, derivative))
