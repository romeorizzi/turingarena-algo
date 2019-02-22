Find all cutnodes (articulation points) and all biconnected components of a given undirected graph.

Consider an undirected graph G. The graph is simple (parallel edges and loops would have no role on the problem and notions here proposed).
A node of G is called a cutnode (or articulation point) if its removal augments the number of conneced components. (Notice: the graph with two nodes and one edge between them has no cutnode, and is considered biconnected).

Biconnected components are maximal subgraphs such that the removal of a node (and all edges incident on that node) will not disconnect the subgraph. Note that nodes may be part of more than one biconnected component. Those nodes are cutnodes.

Consider the following relation, which we define in two equivalent ways:
ways:
u -:- v if u and v remain in the same connected component whatever node z, other than u and v, gets removed;
u -:- v if there exists two internally node-disjoint paths between u and v.

The maximal subsets of nodes S such that the induced subgraph G[S] is biconnected are the biconnected components of G.
Equivalently, these are the maximal subsets of nodes S such that u -:- v for any two nodes u and v in S.

Notice: the relation -:- is reflexive and symmetric, but is NOT an equivalence relation since it is not transitive:
consider the path graph (V,E) = {(a,b,c), (ab,bc)}.
As such, we have two biconnected components ({a,b} and {b,c}) sharing a common node b. Such shared nodes are the cutnodes. A cutnode can belong to more components but two components can share at most one cutnode. In fact, something stronger is true: if we consider the bipartite graph having the cutnodes and the biconnected components as its color classes, and an edge between cutnode v and component C iff v in C, then this bicolored graph is acyclic (a forest). This bipartite graph is a tree (called the tree of the biconnected components) when G is connected. To know more, search "the tree of the biconnected components", you can find nice drawings also on Wikipedia.