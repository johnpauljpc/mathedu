import math



def successive_approximation(f, a, b, tol, max_iter):
    res = []
    ff = []
    for i in range(max_iter):
        # Calculate the midpoint
        x = (((a + b) / 2.0))
        res.append(x)
        
        
        # Check if the current approximation is accurate enough
        if abs(f(x)) < tol:
            print("res   > ", res)
            print("\n fx: ", ff)
            return {"result":format(x, ".4f"), "other_results":None }
            break  # Converged
        
        # Update the bounds based on the function's sign
        if f(a) * f(x) < 0:
            b = x
            ff.append(f(b))
        else:
            a = x
            ff.append(f(a))
    else:
        err = f"Root not found within maximum iterations ({max_iter})."
        return {"result":err, "other_results":None}
