Find all bridges and all 2-edge-connected components of a given undirected graph.

Consider an undirected graph G (parallel edges are allowed but loops make no sense).
An edge of G is called a bridge if its removal augments the number of conneced components. Equivalently, an edge e=uv is a bridge if e is the only path between u and v in G.
Consider the following relation, defined in two equivalent ways:
u -:- v if u and v remain in the same connected component whatever bridge gets removed;
u -:- v if there exists two edge-disjoint paths between u and v.

Notice that the above is an equivalence relation (check that it is reflexive, symmetric, and transitive). 

Being an equivalence relation, the node set V of G is partitioned into its equivalence classes. These are called the 2-edge-connected components of G. 
