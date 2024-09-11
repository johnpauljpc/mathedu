import math

def bisection_method(func, a, b, tolerance):
    other_results = []
    a_ = []
    b_ = []
    b_c = []
    func_ = []
    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        c_ = format(c, ".4f")

        a_.append(a)
        b_.append(b)
        bc = b - c
        b_c.append(bc)
        func_.append(func(c))
        other_results.append(c_)

        if func(c) == 0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c


    # Additional fields data and rows
    # print("a, b, b -c, func ",a_, b_, b_c, func_)
    
    result = format(((a + b) / 2), ".4f")
    a_.append(a)
    b_.append(b)
    bc = b - float(result)
    b_c.append(bc)
    func_.append(func(float(result)))
    other_results.append(result)
    print(other_results)
    return {"result":result, "other_results":other_results, "a":a_, "b":b_, "b_c":b_c, "func":func_ }