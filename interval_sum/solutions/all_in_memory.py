val = []
memo_risp = []

def get_sequence(n, s):
    global N
    N = n
    for i in range(N):
        val.append(s[i])
        memo_risp.append([s[i]])
        for j in range(i+1,N):
            memo_risp[-1].append(memo_risp[-1][-1]+s[j])

def interval_sum(a, b):
    assert a >= 0
    assert b >= a -1
    assert b < N
    if b < a:
        return 0
    return memo_risp[a][b-a]
