import turingarena as ta

def lsp(n):
    return n & (-n)

def bin_enc(n):
    bits = []
    while n != 0:
        if n%2 == 1:
            bits.append(1)
        else:
            bits.append(0)
        n //= 2
    bits.reverse()
    return bits

def display_sol(n):
    bits = bin_enc(n)
    if n > 0:
        with ta.run_algorithm("solutions/solution.py") as p:
            num_moves = p.functions.num_mosse(n)
            right_move = p.functions.mossa(n)
        print(f"n = {n} : bin_enc(n) = {bits} : richiede {num_mosse} mosse")
        print(f"opera la mossa {right_move}, ed ottieni:")
        if right_move == 1:
            if n%2 == 1:
                display_sol(n-1)
            else:
                display_sol(n+1)
        else:
            if lsp(n-lsp(n)) == 2*lsp(n):
                display_sol(n-2*lsp(n))
            else:
                display_sol(n+lsp(n))

def test_case(n):
    while n > 0:
        print(f"case n={n}")

        with ta.run_algorithm("solutions/solution.py") as p:
            expected_res1 = p.functions.num_mosse(n)
        with ta.run_algorithm("solutions/solution.py") as p:
            expected_res2 = p.functions.mossa(n)

        try:    
            with ta.run_algorithm(ta.submission.source) as p:
                with p.section(time_limit=0.002):
                    res1 = p.functions.num_mosse(n)
        except ta.AlgorithmError as e:
            print("During the execution of your code we got the following exception:")
            print(e)
            ta.goals["num_mosse_big"] =  False
            if n <= 2**10:
                ta.goals["num_mosse_small"] =  False
        else:
            print(f"expected {expected_res1}, got {res1}")
            if res1 != expected_res1:
                if res1 < expected_res1:
                    print(f"According to your num_mosse function, you can solve {n} within {res1} moves. We disbelieve this." )
                else:    
                    print(f"According to your num_mosse function, to solve {n} you need {res1} moves.")
                    if n <= 25:
                        print(f"Here follows a shorter solution:" )
                        display_sol(n)
                ta.goals["num_mosse_big"] =  False
                if n <= 2**10:
                    ta.goals["num_mosse_small"] =  False
            
        try:    
            with ta.run_algorithm(ta.submission.source) as p:
                with p.section(time_limit=0.002):
                    res2 = p.functions.mossa(n)
        except ta.AlgorithmError as e:
            print("During the execution of your code we got the following exception:")
            print(e)
            ta.goals["mossa_big"] =  False
        else:
            if n <= 2**8:
                if res2 != 1 and res2 != 2:
                    ta.goals["mossa_small"] =  False
                    print(f"Your mossa = {res2} is not valid. You only have two possible moves: either move 1 or move 2" )
                else:
                    if res2 != expected_res2:
                        ta.goals["mossa_small"] =  False
                        print(f"Your mossa = {res2} for n = {n} does not allow for a smallest possible number of moves." )
                if res2 == 1:
                    if n%2 == 1:
                        n -= 1
                    else:
                        n += 1
                if res2 == 2:
                    if lsp(n-lsp(n)) == 2*lsp(n):
                        n -= 2*lsp(n)
                    else:
                        n += 2*lsp(n)
            else:
                n = 0
        

def run_all_test_cases():
    for n in [7,8,2**4, 20, 2**10]:
        test_case(n)
    ta.goals.setdefault("mossa_small", True)                    
    ta.goals.setdefault("num_mosse_small", True)                    
    for n in [2**13, 2**13 + 117, 1000000]:
        test_case(n)
    ta.goals.setdefault("mossa_big", True)                    
    ta.goals.setdefault("num_mosse_big", True)                    
        
run_all_test_cases()
print(dict(ta.goals))

