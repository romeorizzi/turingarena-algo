import sys

def build(n, d, a, add_bridge, start_component, add_node):
    open = [None]*n
    t = 0
    back = [None]*n
    stack = []

    def dfs(v,dad):
        nonlocal t
        if open[v] is not None:
            return open[v]
        else:
            back[v] = open[v] = t = t+1
            stack.append(v)
            #print(f"back[{v}] updated to {res} = res = dfs(node,dad) = dfs({z},{v})",file=sys.stderr)
            for z in a[v]:
                if z != dad:
                    res = dfs(z,v)
                    if res < back[v]:
                       back[v] = res
                       #print(f"back[{v}] updated to response res = dfs(z,v) = dfs({z},{v}) = {res}",file=sys.stderr)
                    if back[z] > open[v]:
                        add_bridge(v,z)
                        start_component()
                        z_not_gone = True
                        while z_not_gone:
                            if stack[-1] == z:
                                z_not_gone = False
                            add_node(stack.pop())
            return back[v]

        
    for v in range(n):
        if open[v] == None:
            #print(f"lounch dfs({v})",file=sys.stderr)
            dfs(v,v)
            start_component()
            while len(stack) != 0:
                #print(stack[-1],file=sys.stderr)
                add_node(stack.pop())
    return 0
