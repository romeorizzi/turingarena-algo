import sys
import os

import turingarena as ta
import networkx as nx

#
DEBUG = True


def D(*s):
    if DEBUG:
        print(*s, file=sys.stderr)


def gnm_random_dag(n, m):
    g = nx.gnm_random_graph(n, m, directed=True)
    dag = nx.DiGraph()
    dag.add_nodes_from(g.nodes())
    dag.add_edges_from([(u, v) for (u, v) in g.edges() if u < v])
    return dag


def valid_cycle(g, cycle):
    for u, v in zip(cycle, cycle[1:] + cycle[:1]):
        if (u, v) not in g.edges():
            print(f"You said {cycle} is a cycle, but ({u}, {v}) is not an edge of G")
            return False
    return True


def valid_order(g, order):
    for u, v in g.edges():
        if order.index(u) >= order.index(v):
            print(f"You said {order} is a topological order, but is violated by the edge ({u}, {v})")
            return False
    return True

input_ii = 0
def test_graph(g):
    global input_ii
    expected_is_dag = nx.is_directed_acyclic_graph(g)
    actual_is_dag = not expected_is_dag
    input_txt = os.path.join(ta.get_temp_dir(), "input.txt")
    output_txt = os.path.join(ta.get_temp_dir(), "output.txt")
    try:
        with ta.run_algorithm(
            ta.submission.source, downward_tee=input_txt, upward_tee=output_txt) as p:
            actual_is_dag = bool(p.functions.is_dag(
                g.order(),
                [g.in_degree(u) for u in g.nodes()],
                [g.predecessors(u) for u in g.nodes()],
                [g.out_degree(u) for u in g.nodes()],
                [g.successors(u) for u in g.nodes()],
            ))

            #D("Expected is dag", expected_is_dag)
            #D("Actual is dag", actual_is_dag)

            if expected_is_dag and not actual_is_dag:
                print("The graph is a DAG, look topological order:",
                    list(nx.topological_sort(g)))
            if not expected_is_dag and actual_is_dag:
                print("The graph is cyclic, look:", list(nx.find_cycle(g)))

            if expected_is_dag != actual_is_dag:
                ta.goals["ok_detection"] = False

            ok = False
            if expected_is_dag and actual_is_dag:
                p.procedures.build_order()
                top_sort = [p.functions.get_order_node(
                    i) for i in range(len(g.nodes()))]
                ok = valid_order(g, top_sort)
                if not ok:
                    ta.goals["ok_top_order"] = False
            if not expected_is_dag and not actual_is_dag:
                l = p.functions.get_cycle_length()
                cycle = [p.functions.get_cycle_node(i) for i in range(l)]
                ok = valid_cycle(g, cycle)
                if not ok:
                    ta.goals["ok_cycle_find"] = False
    except ta.AlgorithmError as e:
        print(e)
        ta.goals["ok_detection"] = False
        ta.goals["ok_top_order"] = False
        ta.goals["ok_cycle_find"] = False
        ok = False
    if not ok:
        ta.evallib.evaluation.send_file_as_path(input_txt, filename=f"input_{input_ii}.txt")
        ta.evallib.evaluation.send_file_as_path(output_txt, filename=f"output_{input_ii}.txt")
        input_ii += 1

    return expected_is_dag == actual_is_dag, ok


def test_case(n, m, dag):
    print(f"Testing N={n}, M={m}, DAG={dag} ...\t", end="")
    if dag:
        g = gnm_random_dag(n, m)
    else:
        g = nx.gnm_random_graph(n, m, directed=True)
    res1, res2 = test_graph(g)
    if res1 and res2:
        print("[CORRECT]")
    elif res1 and not res2:
        print("[PARTIAL]")
    else:
        print("[WRONG]")
    return res1, res2

goals = [
    "ok_top_order",
    "ok_cycle_find",
    "ok_detection",
]

def main():
    for n in (10, 100, 1000):
        for m in (n, n * 2, 5 * n):
            test_case(n, m, True)
            test_case(n, m, False)

    for goal in goals:
        ta.goals.setdefault(goal, True)
    
    print(ta.goals)

if __name__ == "__main__":
    main()
