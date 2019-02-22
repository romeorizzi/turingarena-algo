import sys
sys.setrecursionlimit(1000000)


def scc(N, Dout, Aout, Din, Ain, start_component, add_node):
    
    visited = [False] * N
    S = []

    def dfs_in(u):
        if not visited[u]:
            visited[u] = True
            for v in Ain[u]:
                dfs_in(v)
            S.append(u)

    def dfs_out(u):
        if not visited[u]:
            visited[u] = True
            add_node(u)
            for v in Aout[u]:
                dfs_out(v) 

    for u in range(N):
        dfs_in(u)

    visited = [False] * N
    for u in S[::-1]:
        if not visited[u]:
            start_component()
            dfs_out(u)
    