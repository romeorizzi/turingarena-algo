import turingarena as ta
#import matplotlib.pyplot as plt
import networkx as nx


def test_case_random(n,m):
    print(f"testcase (n={n},m={m})")
    g = nx.gnm_random_graph(n,m)
    return test_case(g)
    
def test_case(g):
    print(g.edges())
    #nx.draw(g)
    #plt.show()
    
    cutnodes = set()
    added_nodes = set()
    components = []

    with ta.run_algorithm(ta.submission.source) as p:
        with p.section(time_limit=0.1):
            def add_cutnode(v):
                p.check(v not in cutnodes, f"node {v} already added as a cutnode")
                cutnodes.add(v)

            def start_component():
                nonlocal added_nodes
                p.check(len(components) < g.order(), f"too many components")
                added_nodes = set()
                components.append([])

            def add_node(u):
                p.check(u not in added_nodes, f"node {u} already added")
                added_nodes.add(u)
                components[-1].append(u)

            p.procedures.build(
                g.order(),
                [g.degree(u) for u in g.nodes],
                [g.neighbors(u) for u in g.nodes],
                callbacks=[
                    add_cutnode,
                    start_component,
                    add_node,
                ],
            )
        
    expected_ccs = set(frozenset(c) for c in nx.biconnected_components(g))
    expected_cutnodes = set(v for v in nx.articulation_points(g))
    actual_ccs = set(frozenset(c) for c in components)
    actual_cutnodes = cutnodes

    if expected_cutnodes != actual_cutnodes:
        if n <= 20:
            for u,v in g.edges():
                print(u,v)
        print("The true cutnodes:")
        print(expected_cutnodes)
        print("The computed cutnodes:")
        print(actual_cutnodes)
    if expected_ccs != actual_ccs:
        if n <= 20:
            for u,v in g.edges():
                print(u,v)
        print("The true connected components:")
        print(expected_ccs)
        print("The computed connected components:")
        print(actual_ccs)

    return (expected_cutnodes == actual_cutnodes, expected_ccs == actual_ccs)

def main():
    handmade_graphs = []
    g = nx.Graph()
    g.add_edge(0,1)
    g.add_edge(2,3)
    g.add_nodes_from([4,5,6])
    assert g.order() == 7
    handmade_graphs.append(g)
    for g in handmade_graphs:
        correct_cutnodes, correct_componets = test_case(g)
        if correct_cutnodes == False:
            ta.goals["cutnodes_linear"] = False
            ta.goals["cutnodes_mn"] = False
            ta.goals["cutnodes_m2"] = False
        if correct_componets == False:
            ta.goals["components_linear"] = False
            ta.goals["components_mn"] = False
            ta.goals["components_m2"] = False
    for n in [10, 20, 50]:
        for m in [3*n//2, 2*n, 5*n//2, 5*n]:
            correct_cutnodes, correct_componets = test_case_random(n,m)
            if correct_cutnodes == False:
                ta.goals["cutnodes_linear"] = False
                ta.goals["cutnodes_mn"] = False
                ta.goals["cutnodes_m2"] = False
            if correct_componets == False:
                ta.goals["components_linear"] = False
                ta.goals["components_mn"] = False
                ta.goals["components_m2"] = False

    ta.goals.setdefault("components_m2", True)            
    ta.goals.setdefault("cutnodes_m2", True)            
    for n in [100, 200]:
        for m in [3*n//2, 2*n, 5*n//2]:
            correct_cutnodes, correct_componets = test_case_random(n,m)
            if correct_cutnodes == False:
                ta.goals["cutnodes_linear"] = False
                ta.goals["cutnodes_mn"] = False
            if correct_componets == False:
                ta.goals["components_linear"] = False
                ta.goals["components_mn"] = False

    ta.goals.setdefault("components_mn", True)            
    ta.goals.setdefault("cutnodes_mn", True)            
    for n in [1000]:
        for m in [3*n//2, 2*n]:
            correct_cutnodes, correct_componets = test_case_random(n,m)
            if correct_cutnodes == False:
                ta.goals["cutnodes_linear"] = False
            if correct_componets == False:
                ta.goals["components_linear"] = False

    ta.goals.setdefault("components_linear", True)            
    ta.goals.setdefault("cutnodes_linear", True)            

    print(dict(ta.goals))


if __name__ == "__main__":
    main()
