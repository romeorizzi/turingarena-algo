// evaluation_assert data["goals"]["correct"]
// evaluation_assert not data["goals"]["efficient"]

YES = 1
NO = 0

def set_a_and_b(a_, b_):
    assert a_ > 0 and b_ > 0
    global a, b
    a = a_
    b = b_

def do_the_hard_computations():
    assert a > 0 and b > 0
    global gcd, x, y
    gcd = 1
    for i in range(2,a+b):
        if a%i == 0 and b%i == 0:
            gcd = i
    if gcd > 1:
        a_and_b_coprime = NO
    else:
        a_and_b_coprime = YES
        for y in range(a):
            if (a*b+gcd - y*b) % a == 0:
                x = (gcd - y*b) / a
                break
    # gcd = xa + yb con |x|<b e |y|<a con xy <= 0
    # -> ab + gcd = xa +yb con x,y >= 0, x<b e y<a

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


