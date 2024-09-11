import re

def replace_math_functions(expression):
    # Replace '^' with '**'
    modified_expression = re.sub(r'\^', '**', expression)
    modified_expression = modified_expression.replace("y", "x")
    modified_expression = modified_expression.replace("z", "x")
    modified_expression = modified_expression.replace("a", "x")
    # modified_expression = modified_expression.replace("b", "x")
    # c skipped because of cos
    modified_expression = modified_expression.replace("d", "x")
    # e skipped for the sake of expenentials
    modified_expression = modified_expression.replace("f", "x")
    # g skipped because of log
    modified_expression = modified_expression.replace("h", "x")
    # i skipped because of sine
    modified_expression = modified_expression.replace("j", "x")
    modified_expression = modified_expression.replace("k", "x")
    # l skipped because of log
    modified_expression = modified_expression.replace("m", "x")
    # n skipped for the sake of sin
    # o skipped because of log and cos
    modified_expression = modified_expression.replace("p", "x")
    modified_expression = modified_expression.replace("q", "x")
    # modified_expression = modified_expression.replace("r", "x")
    # s skipped because of sine
    # t skipped because of tan
    modified_expression = modified_expression.replace("u", "x")
    modified_expression = modified_expression.replace("v", "x")
    modified_expression = modified_expression.replace("w", "x")

     




    # Replace sin, cos, tan, and e
    modified_expression = modified_expression.replace('sinx', 'sin(x)')
    modified_expression = modified_expression.replace('cosx', 'cos(x)')
    modified_expression = modified_expression.replace('tanx', 'tan(x)')
    modified_expression = modified_expression.replace('logx', 'log(x)')
    modified_expression = modified_expression.replace('log10x', 'log(x)')

    modified_expression = re.sub(r'\blog\b', 'math.log', modified_expression)

    modified_expression = re.sub(r'\bsin\b', 'math.sin', modified_expression)
    modified_expression = re.sub(r'\blog10\b', 'math.log', modified_expression)
    modified_expression = re.sub(r'\bcos\b', 'math.cos', modified_expression)
    modified_expression = re.sub(r'\btan\b', 'math.tan', modified_expression)
    modified_expression = re.sub(r'\bcbrt\b', 'math.cbrt', modified_expression)

    # math.cos(math.radians(x))
    modified_expression = modified_expression.replace("cos(x)", "cos(math.radians(x))")
    modified_expression = modified_expression.replace("sin(x)", "sin(math.radians(x))")
    modified_expression = modified_expression.replace("tan(x)", "tan(math.radians(x))")

    modified_expression = modified_expression.replace('ex', 'e(x)')
    modified_expression = modified_expression.replace('e^x', 'e(x)')
    modified_expression = modified_expression.replace('e**x', 'e(x)')
    # modified_expression = modified_expression.replace('log10(x)', 'log(x)')
    # modified_expression = modified_expression.replace('log10x', 'log(x)')
    modified_expression = re.sub(r'\be\b', 'math.exp', modified_expression)

    
    



    print("....modified...Expr...>>>>  ", modified_expression)
    return modified_expression

