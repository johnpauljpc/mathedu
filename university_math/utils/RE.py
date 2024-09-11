import re

def interpret_expression(expression):
    #change equations to expressions
    # Find the part before the equal sign (left-hand side of the equation)
    match = re.search(r'([^=]+)', expression)
    if match:
        expression = match.group(0).strip()
   

    # Replace 'Nx' with 'N*x' and 'Nxx' with 'N*x*x' for any numeric coefficient N.
    pattern = r'(\d*\.\d+|\d+)([a-zA-Z])'
    # pattern2 = r'(\b\w+)(\d+)' #for replacing x2, x3 etc with x**2, x**3 etc
    pattern2 = r'(\b\w+)(?<!\d)(\d+)' #for replacing x2, x3 etc with x**2, x**3 etc

    replacement = r'\1*\2'
    expression = re.sub(pattern, replacement, expression)
    
    # for replacing x2, x3 etc with x**2, x**3 etc
    expression = re.sub(pattern2, r'\1**\2', expression)

    

    
    try:
        result = expression
        return result
    except:
        print("Invalid expression....")
        return "Invalid expression"
