import turingarena as ta 
import networkx as nx

DEBUG = False

# Goals:
# time limit = 0.2s
# - lineare     O(M + N)    N <= 2000, M <= 2000
# - quadratica  O(M * N)    N <= 200, M <= 200
# - cubica      O(M^2 * N)  N <= 20, M <= 20

def test_case(n, m):
    print(f"Evaluating test case: N = {n}, M = {m}...  \t", end="")

    G = nx.gnm_random_graph(n, m, directed=True)
    if DEBUG:
        for u, v in G.edges():
            print(f"{u} -> {v}")

    Ain = [[] for _ in range(n)]
    Aout = [[] for _ in range(n)]

    for u, v in G.edges():
        Aout[u].append(v)
        Ain[v].append(u)

    components = []
    with ta.run_algorithm(ta.submission.source, time_limit=0.2) as p:
        def start_component():
            p.check(len(components) <= n, "You found more components than nodes in the graph!")
            components.append([])

        def add_node(u):
            p.check(0 <= u < n, "Invalid node index!")
            p.check(len(components[-1]) < n, "Your components have more nodes than the graph!")
            components[-1].append(u)

        p.procedures.scc(n, [len(d) for d in Aout], Aout, [len(d) for d in Ain], Ain, callbacks=[start_component, add_node])

    
    result = frozenset(
        frozenset(c) for c in components
    )

    correct_result = frozenset(
        frozenset(c) for c in nx.strongly_connected_components(G)
    )

    if DEBUG:
        print(f"Your components = {result}")
        print(f"Correct components = {correct_result}") 

    res = result == correct_result
    if res:
        print("[CORRECT]")
    else:
        print("[WRONG]")

    return res


def main(): 
    for n in (10, 15, 20):
        for m in (10, 15, 20):
            if not test_case(n, m):
                ta.goals["cubica"] = False
    ta.goals.setdefault("cubica", True)

    for n in (100, 150, 200):
        for m in (100, 150, 200):
            if not test_case(n, m):
                ta.goals["quadratica"] = False
    ta.goals.setdefault("quadratica", True)

    for n in (1000, 1500, 2000):
        for m in (1000, 1500, 2000):
            if not test_case(n, m):
                ta.goals["lineare"] = False
    ta.goals.setdefault("lineare", True)

    print(ta.goals)

if __name__ == "__main__":
    main()
