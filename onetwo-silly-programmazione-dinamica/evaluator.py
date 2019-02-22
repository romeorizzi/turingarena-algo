import random

def min_val(n, vect):
    assert n >= 0
    cost = [None]*3
    cost_alone = [None]*3
    cost_coupled = [None]*3
    cost[n%3] = 0
    cost[(n-1)%3] = abs( vect[n-1] )
    for i in reversed( range(n-1) ):
        cost_alone[i%3] = abs(vect[i]) + cost[(i+1)%3]
        cost_coupled[i%3] = abs( vect[i] - vect[i+1] ) + cost[(i+2)%3]
        cost[i%3] = min( cost_alone[i%3], cost_coupled[i%3] )
    return cost[0]    
        

def evaluate(algo):
    n = 1000
    vect = [ random.randint(-100,100) for _ in range(n) ]
    print(n, vect)
    risp_ref = min_val(n, vect)
    print( risp_ref )
    
    with algo.run(global_variables=dict(n = n, vect = vect) ) as process:
        risp_p = process.call.min_val()
        print(risp_p)
        if risp_ref == risp_p:
            print ("CORRECT")
        else:
            print ("WRONG")
        

    
