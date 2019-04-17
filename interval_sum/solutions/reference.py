_prefix_sum = [0]

def get_sequence(n, s):
    global N
    N = n
    for i in range(N):
        _prefix_sum.append(_prefix_sum[-1] + s[i])

def interval_sum(a, b):
    assert a >= 0
    assert b >= a -1
    assert b < N
    prefix_sum = _prefix_sum[1:]
    return prefix_sum[b] - prefix_sum[a-1]



