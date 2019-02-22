# Finding topologial orders

A topological order of G is a total order < on its nodes such that:
   for every arc (u,v) of G, it holds that u < v

Can you decide whether a generic input graph G admits a topological order?
And can you produce a topological order of G whenever it exists?

can you find out whether G contains a directed cycle?
And can you produce such a directed cycle (a walk that starts from a node and, after traversing a few arcs of G, finally returns where it started from) whenever it exists?

# Finding directed cycles

Given a directed graph G, can you find out whether G contains a directed cycle?
And can you produce such a directed cycle (a walk that starts from a node and, after traversing a few arcs of G, finally returns where it started from) whenever it exists?

# The task

Implement the following functions:

function is_dag(N, Din[], Ain[][], Dout[], Aout[][]);
receives the directed graph G (the number of nodes, the in-degrees of the nodes, the out-degrees of the nodes, the predecessors of the nodes, the successor of the nodes)
returns 1 if G is a Directed Acyclic Graph, and 0 otherwise.

function get_cycle_length();
in case you have found a cycle, return here its length.

function get_cycle_node(i);
this is for returning the nodes of the cycle one by one.

function get_order_node(i);
this is for returning the node occuring in the i-th position within the topological order that you might have possibly produced.

# The goals

(1) correctly decide whether a graph contains a cycle or is acyclic (a DAG)
(1+) do it in linear time
(2,2+) return a cycle if you can find it
(3,3+) return a topological order if you can find it

