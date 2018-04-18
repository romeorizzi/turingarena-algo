from skeleton import n, vect

def min_val():
    assert n >= 0
    cost = [None]*(n+1)
    cost_alone = [None]*(n+1)
    cost_coupled = [None]*(n+1)
    cost[n] = 0
    cost[n-1] = abs( vect[n-1] )
    for i in reversed( range(n-1) ):
        cost_alone[i] = abs(vect[i]) + cost[i+1]
        cost_coupled[i] = abs( vect[i] - vect[i+1] ) + cost[i+2]
        cost[i] = min( cost_alone[i], cost_coupled[i] )
    return cost[0]    
