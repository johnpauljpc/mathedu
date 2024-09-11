# Test if the intervals are possible roots for bisection and successive methods
def test_root(a, b, expr):
    x = float(a)
    root1 = eval(expr)
    x = float(b)
    root2 = eval(expr)
    
    test = root1 * root2
    if test < 0:
        return True
    return False
