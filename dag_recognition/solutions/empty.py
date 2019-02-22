
class Wrapper:
    pass


g = Wrapper()

g.top_sort = []
g.stack = []
g.cycle = None


def DFS(u):
    if g.visited[u]:
        if not g.closed[u]:
            g.cycle = g.stack[g.stack.index(u):]
    else:
        g.visited[u] = True
        g.stack.append(u)
        for v in g.Aout[u]:
            DFS(v)
        g.closed[u] = True
        g.stack.pop()
        g.top_sort.append(u)


def is_dag(N, Din, Ain, Dout, Aout):
    g.N, g.Din, g.Ain, g.Dout, g.Aout = N, Din, Ain, Dout, Aout
    g.visited = [False for _ in range(N)]
    g.closed = [False for _ in range(N)]
    for u in range(N):
        DFS(u)
    return g.cycle is None


def get_cycle_length():
    return len(g.cycle)


def get_cycle_node(i):
    return g.cycle[i]


def get_order_node(i):
    return g.top_sort[i]


def build_order():
    g.top_sort.reverse()
