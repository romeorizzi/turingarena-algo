import sys

def build(n, d, a, add_cutnode, start_component, add_node):
    already_recognized_cutnode = [False]*n
    open = [None]*n
    t = 0
    back = [None]*n
    stack = []

    def dfs(v,dad):
        nonlocal t
        back[v] = open[v] = t = t+1
        stack.append(v)
        #print(f"nodo {v} aperto at time back[{v}] = open[{v}] = {open[v]}. Suo padre è {dad}",file=sys.stderr)
        for z in a[v]:
            if z != dad:
                if open[z] is not None:
                    if open[z] < back[v]:
                       back[v] = open[z]
                       #print(f"back[{v}] updated to {open[z]} = open[{z}] per back-edge da {v} as antenato {z}",file=sys.stderr)
                else:
                    res = dfs(z,v)
                    if res < back[v]:
                       back[v] = res
                       #print(f"back[{v}] updated to {res} = res = dfs(node,dad) = dfs({z},{v})",file=sys.stderr)
                    if back[z] >= open[v]:
                        if dad == v and not already_recognized_cutnode[v]:
                            for root_child in a[v]:
                                if not open[root_child]:
                                    add_cutnode(v)
                            already_recognized_cutnode[v] = True
                        if dad != v or already_recognized_cutnode[v]:
                            #print(f"back[{z}] = {back[z]} >= open[{v}] ossia back[figlio] >= open[padre] a figlio {z} ormai chiuso",file=sys.stderr)
                            if not already_recognized_cutnode[v]:
                                add_cutnode(v)
                                already_recognized_cutnode[v] = True
                            #print(f"cutnode = {v}, component with child {z}, stack = {stack}",file=sys.stderr)
                            start_component()
                            z_not_gone = True
                            while z_not_gone:
                                if stack[-1] == z:
                                    z_not_gone = False
                                add_node(stack.pop())
                            add_node(v)
                            #print(f"residual stack = {stack}",file=sys.stderr)
        #print(f"Chiudo il nodo {v}",file=sys.stderr)                
        return back[v]


    for v in range(n):
        if open[v] == None:
            #print(f"lounch dfs({v})",file=sys.stderr)
            dfs(v,v)
    return 0
