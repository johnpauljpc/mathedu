import math

def newton_raphson_method(f, initial_guess, tolerance=1e-6, max_iterations=100, h=1e-6):
    def numerical_derivative(x):
        print("................")
        return (f(x + h) - f(x - h)) / (2 * h)

    x = initial_guess
    last_initial = 1
    iteration = 0
    other_results = []
    x_i = []
    x_i.append(x)
    e = []
   
    fx = [] #for the function of the equation
    fx1 = [] #for the first derivative of fx
    while abs(f(x)) > tolerance and iteration < max_iterations:
        fx.append(f(x))
        initials = x
        fx1.append(numerical_derivative(x))
        x = x - f(x) / numerical_derivative(x)
        other_results.append(x)
        x_i.append(x) #results for Xi
        iteration += 1
        e_tol = ((x - initials)/x)
        if e_tol < 0:
            e_tol = (e_tol)*-1
        e.append(format(e_tol))

        
        

    if abs(f(x)) <= tolerance:
        print("last initial ", initials, x)
        e_tol = (x- initials)/x
        if e_tol < 0:
            e_tol = e_tol * (-1)
            print("--------> ", e_tol)

        result = x
        other_results.append(result)

        fx.append(f(x))
        fx1.append(numerical_derivative(x))
        # e_tol = ((result - initials)/result)
        e.append((e_tol))
        print("result")
        print(other_results)
        print("fx")
        print(fx)
        print("fx1")
        print(fx1)
        print("Xi")
        print(x_i)
        print("tolerance")
        print(e)

        
        return {"result":format(result, ".4f"), "other_results":other_results, "e":e, "x_i":x_i, "fx":fx, "fx1":fx1 }
    else:
        return {"result":"Newton-Raphson method did not converge within the specified number of iterations.", "other_results":None }
        # raise ValueError("Newton-Raphson method did not converge within the specified number of iterations.")


# # Example usage with a different equation
# def equation1(x):
#     return math.cos(x) - 3*x + 5

# # Example usage
# initial_guess = 2.0  # You can change the initial guess
# solution = newton_raphson_method(equation1, initial_guess)

# print("Approximate solution:", solution)
