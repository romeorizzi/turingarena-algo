// evaluation_assert data["goals"]["correct"]
// evaluation_assert not data["goals"]["efficient"]

YES = 1
NO = 0

def set_a_and_b(a_, b_):
    assert a_ > 0 and b_ > 0
    global a, b
    a = a_
    b = b_

def recEuclide(a,b):
"""returns the triple [d,x,y] where:
       d is the greatest divisor of a and b;
       x and y are integers such that  xa + yb = d.
"""    
    assert a >= 0 and b >= 0 and a + b > 0
    if b > a:
        answ =  recEuclide(b,a)
        return [ answ[0], answ[2], answ[1] ]
    assert a >= b >= 0 and a > 0    
    if b == 0 or a == b:
        return [a, 1, 0]
    A = a
    q = A // b
    a = A % b
    answ =  recEuclide(a,b)
#        A = bq + a
#        xa + yb = 1
#        xA +(y-xq)b= xbq + xa +yb -xqb
    return [ answ[0], answ[1], answ[2]-answ[1]*q ]


def do_the_hard_computations():
    assert a > 0 and b > 0
    answ = recEuclide(a,b)
    global gcd, x, y
    gcd, x, y = answ
    global a_and_b_coprime
    if gcd == 1:  
        a_and_b_coprime = YES
    else:
        a_and_b_coprime = NO

def gimme_a():
    return a

def gimme_b():
    return b

def are_a_and_b_coprime():
    return a_and_b_coprime

def gimme_nontrivial_divisor():
    assert gcd > 1
    return gcd

def gimme_a_multiplier():
    return x

def gimme_b_multiplier():
    return y

