from functools import lru_cache

import turingarena as ta 

from solutions.solution import num_modi

@lru_cache(None)
def test_case(n, elenca=True):
    try:
        with ta.run_algorithm(ta.submission.source) as p:
            print(f"Testing case n={n}...")
            actual_res = p.functions.num_modi(n)
            correct_res = num_modi(n)

            if actual_res != correct_res:
                print(f"Hai detto che esistono {actual_res} modi, ma secondo noi ne esistono {correct_res}!")
                return False, False 
            
            print(f"Ok num modi")
            if not elenca:
                return True, None

            modi = set()
            L = []

            def pescato_intera():
                L.append("I")
            
            def pescato_mezza():
                L.append("M")

            def done():
                nonlocal L
                m = L.count("M")
                l = L.count("I")
                s = "".join(L)
                if m != n or l != n:
                    print(f"Il modo scelto {s} non è un modo valido!")
                    p.stop()
                if s in modi:
                    print(f"Il modo scelto {s} è già stato fornito!")
                    p.stop()
                modi.add(s)
                L = []
                
            p.procedures.elenca_modi(n, callbacks=[pescato_intera, pescato_mezza, done])
    except ta.AlgorithmRuntimeError as e:
        if "timeout expired" in str(e):
            print("Timelimit expired")
            return False, False

    if len(modi) != actual_res:
        print(f"Hai detto che esistevano {actual_res} modi diversi, ma ne hai forniti soltanto {len(modi)}!")
        return True, False
    
    print("Ok elenca modi")
    return True, True


ta.goals.check("correct_num_modi", lambda: test_case(1)[0])
ta.goals.check("correct_num_modi", lambda: test_case(2)[0])
ta.goals.check("correct_num_modi", lambda: test_case(3)[0])
ta.goals.check("correct_num_modi", lambda: test_case(4)[0])
ta.goals.check("correct_num_modi", lambda: test_case(5)[0])
ta.goals.check("correct_num_modi", lambda: test_case(8)[0])
ta.goals.check("correct_num_modi", lambda: test_case(10, elenca=False)[0])
ta.goals.setdefault("correct_num_modi", True)
ta.goals.check("correct_elenca_modi", lambda: test_case(1)[1])
ta.goals.check("correct_elenca_modi", lambda: test_case(2)[1])
ta.goals.check("correct_elenca_modi", lambda: test_case(3)[1])
ta.goals.check("correct_elenca_modi", lambda: test_case(4)[1])
ta.goals.check("correct_elenca_modi", lambda: test_case(5)[1])
ta.goals.check("correct_elenca_modi", lambda: test_case(8)[1])
ta.goals.setdefault("correct_elenca_modi", True)
ta.goals.check("correct_num_modi_big", lambda: test_case(15, elenca=False)[0])
ta.goals.check("correct_num_modi_big", lambda: test_case(20, elenca=False)[0])
ta.goals.check("correct_num_modi_big", lambda: test_case(25, elenca=False)[0])
ta.goals.check("correct_num_modi_big", lambda: test_case(30, elenca=False)[0])
ta.goals.setdefault("correct_num_modi_big", True)
print(ta.goals)