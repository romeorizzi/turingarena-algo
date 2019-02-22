import turingarena as ta
import networkx as nx


def test_case(n,m):
    print(f"testcase (n={n},m={m})")
    g = nx.gnm_random_graph(n,m)
    #print(g.edges())

    added_nodes = set()
    components = []
    bridges = []

    with ta.run_algorithm(ta.submission.source) as p:
        with p.section(time_limit=0.1):
            def start_component():
                p.check(len(components) < g.order(), f"too many components")
                components.append([])

            def add_node(u):
                p.check(u not in added_nodes, f"node {u} already added")
                added_nodes.add(u)
                components[-1].append(u)

            def add_bridge(u, v):
                p.check(len(bridges) < g.size(), f"too many bridges")
                bridges.append((u, v))

            p.procedures.build(
                g.order(),
                [g.degree(u) for u in g.nodes],
                [g.neighbors(u) for u in g.nodes],
                callbacks=[
                    add_bridge,
                    start_component,
                    add_node,
                ],
            )
        
    expected_ccs = set(frozenset(c) for c in nx.k_edge_components(g, k=2))
    expected_bridges = set(frozenset(e) for e in nx.bridges(g))

    actual_ccs = set(frozenset(c) for c in components)
    actual_bridges = set(frozenset(e) for e in bridges)

    if expected_bridges != actual_bridges:
        if n <= 20:
            for u,v in g.edges():
                print(u,v)
        print("The true bridges:")
        print(expected_bridges)
        print("The computed bridges:")
        print(actual_bridges)
    if expected_ccs != actual_ccs:
        if n <= 20:
            for u,v in g.edges():
                print(u,v)
        print("The true connected components:")
        print(expected_ccs)
        print("The computed connected components:")
        print(actual_ccs)

    return (expected_bridges == actual_bridges, expected_ccs == actual_ccs)

def main():
    for n in [10, 20, 50]:
        for m in [3*n//2, 2*n, 5*n//2, 5*n]:
            correct_bridges, correct_componets = test_case(n,m)
            if correct_bridges == False:
                ta.goals["bridges_linear"] = False
                ta.goals["bridges_mn"] = False
                ta.goals["bridges_m2"] = False
            if correct_componets == False:
                ta.goals["components_linear"] = False
                ta.goals["components_mn"] = False
                ta.goals["components_m2"] = False
    ta.goals.setdefault("bridges_m2", True)            
    ta.goals.setdefault("components_m2", True)            
    for n in [100, 200]:
        for m in [3*n//2, 2*n, 5*n//2]:
            correct_bridges, correct_componets = test_case(n,m)
            if correct_bridges == False:
                ta.goals["bridges_linear"] = False
                ta.goals["bridges_mn"] = False
            if correct_componets == False:
                ta.goals["components_linear"] = False
                ta.goals["components_mn"] = False

    ta.goals.setdefault("bridges_mn", True)            
    ta.goals.setdefault("components_mn", True)            
    for n in [1000]:
        for m in [3*n//2, 2*n]:
            correct_bridges, correct_componets = test_case(n,m)
            if correct_bridges == False:
                ta.goals["bridges_linear"] = False
            if correct_componets == False:
                ta.goals["components_linear"] = False

    ta.goals.setdefault("bridges_linear", True)            
    ta.goals.setdefault("components_linear", True)            

    print(dict(ta.goals))


if __name__ == "__main__":
    main()
