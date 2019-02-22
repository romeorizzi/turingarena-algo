def lsp(n):
    return n & (-n)

def is_power_of_2(n):
    return n == lsp(n)

def num_mosse_for_powers_of_two(n):
    assert is_power_of_2(n)
    return 2*n-1

def num_of_ones_in_binary_rep(n):
    if n == 0:
        return 0
    return 1 + num_of_ones_in_binary_rep(n - lsp(n))

def num_mosse(n):
    risp = 0
    while n!=0:
        risp += 1
        if num_of_ones_in_binary_rep(n) % 2 == 1:
            #since the correct first move is move 1 (flip the rightmost bit), then:
            if n%2 == 1:
                n = n-1
            else:
                n = n+1
        else:	
            if lsp(n-lsp(n)) == 2*lsp(n):
                n = n - 2*lsp(n)
            else:
                n = n + 2*lsp(n)
    return risp


def mossa(n):
    assert n > 0
    if num_of_ones_in_binary_rep(n) % 2 == 1:
        return 1
    else:
        return 2

#    n | num_mosse
#    1 |  1
#   10 |  3 = 1 + 1 + 1
#  100 |  7 = 3 + 1 + 3
# 1000 | 15 = 7 + 1 + 7 
