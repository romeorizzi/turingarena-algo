val = []

def get_sequence(n, s):
    global N
    N = n
    for i in range(N):
        val.append(s[i])

def interval_sum(a, b):
    assert a >= 0
    assert b >= a -1
    assert b < N
    risp = 0
    for i in range(a, b+1):
       risp += val[i]
    return risp
