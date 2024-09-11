import math

def SI(P,R,T):
    I = (P*R*T)/100
    I = round(I, 2)
    return I


# Compound interest
def CompoundInterest(P, R, T):
    amount = P * (math.pow((1 + (R / 100)), T))
    CI = amount - P
    CI = round(CI, 2)
    amount = round(amount, 2)
    
    return CI, amount
