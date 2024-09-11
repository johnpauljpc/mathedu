import cmath, math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = (b ** 2) - (4 * a * c)

    # Check if the discriminant is positive, negative, or zero
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        msg = None
        root1 = round(root1, 4)
        root2 = round(root2, 4)
        return root1, root2, msg
    elif discriminant == 0:
        # Two real and equal roots
        root = -b / (2 * a)
        if root == -0:
            root = 0
        msg = "Two real and equal roots"
        return root, root, msg
    else:
        # Two complex roots
        # real_part = -b / (2 * a)
        # imaginary_part = cmath.sqrt(abs(discriminant)) / (2 * a)
        # root1 = complex(real_part, imaginary_part)
        # root2 = complex(real_part, -imaginary_part)
        # return False#root1, root2
        raise ValueError("Roots are imaginary")

# try:
#     root1, root2 = solve_quadratic(a=11, b=2, c=1)
#     print('r1', root1)
#     print('r2', root2)
# except Exception as err:
#     print(err)

