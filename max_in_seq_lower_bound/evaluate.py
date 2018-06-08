from turingarena import *

import random

algorithm = submitted_algorithm()

goals = {
    "correct_when_cycles": True,
    "correct_when_no_cycle": True,
    "correct_always": True,
}

def eval(N, a, b):
    cyc = []
    top_sort_1 = []
    top_sort_2 = []
    cycle_delivered = False
    def cycle(v):
        cyc.add(v)
        if cyc[0] == cyc[-1]:
            cyc = reversed(cyc)
            cyc_good = True
            for comparison in zip(cyc, cyc[1:]):
                if comparison not in zip(a,b):
                    cyc_good = False
                    print(f"WRONG reported cycle: {cyc}")
                    goals["correct_always"] = False 
            if cyc_good:
                print(f"Found cycle: {cyc} CORRECT")
                cycle_delivered = True

    def inv(perm):
        inverse = [0] * len(perm)
        for i, p in enumerate(perm):
            inverse[p] = i
        return inverse
            
    def is_perm(perm):
        count = [0] * len(perm)
        for ele in perm:
            count[ele] += 1
        return count == [1] * len(perm)
            
    def first_topological_sort(v):
        top_sort_1.add(v)
        if len(top_sort_1) == N:
            pos_of = inv(top_sort_1)
            top_sort_good = True
                         
            for [u,v] in zip(a,b):
                if pos_of[u] > pos_of[v]:
                    top_sort_good = False
                    print(f"WRONG reported first topological sort: {top_sort_1}")
                    goals["correct_always"] = False 
            if top_sort_good:
                print(f"Found first topological sort: {top_sort_1} CORRECT")
            
    def second_topological_sort(v):
        top_sort_2.add(v)
        if len(top_sort_2) == N:
            pos_of = inv(top_sort_2)
            top_sort_good = True
                         
            for [u,v] in comparisons:
                if pos_of[u] > pos_of[v]:
                    top_sort_good = False
                    print(f"WRONG reported second topological sort: {top_sort_2}")
                    goals["correct_always"] = False 
            if top_sort_good:
                print(f"Found second topological sort: {top_sort_2} CORRECT")
            
    with algorithm.run() as process:
        # first, the minimum number of moves to move an N disks tower:
        process.call.process_comparisons(N, a, b, cycle=cycle, first_topological_sort=first_topological_sort, second_topological_sort=second_topological_sort)
    if cycle_delivered:
        return
    if len(top_sort_1) * len(top_sort_2) == 0:
        goals["correct_always"] = False
        if len(cyc) == 0:
            print("You delivered neither a cycle nor two topological sorts. WRONG")                     
        else:
            print("You did not deliver two topological sorts and your cycle was never completed. (Remember that the first and last node should be the same!). WRONG")                     
    elif len(top_sort_1) != N or len(top_sort_2) != N:
        print("When you return topological sorts, both of them must list precisely n elements.")         
        goals["correct_always"] = False 
    elif not is_perm(top_sort_1) or not is_perm(top_sort_2):
        print("When you return topological sorts, they must be orderings of the labels in 1...N.")         
        goals["correct_always"] = False 
    elif top_sort_1[N] == top_sort_2[N]:
        print("The two topological sorts you deliver must differ on the last element.")         
        goals["correct_always"] = False 

for N in [4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100]:
    a = [random.randint(1,N+1)] *(N-2)
    b = [random.randint(1,N+1)] *(N-2)
    eval(N, a, b)

for N in [5, 6, 10, 15, 20, 30, 40, 50, 100]:
    node_in_pos = [[i+1] for i in range(N)]
    random.shuffle(node_in_pos)
    a = [random.randint(1,N)] *(N-2)
    b = [[random.randint(a[i],N+1)] for i in range(N)]                 
    eval(N, a, b)
                     
                         

evaluation_result(goals=goals)
