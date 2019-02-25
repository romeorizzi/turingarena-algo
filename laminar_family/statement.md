# Recognize a laminar family of sets

Consider a family of $m$ sets on an universe of $n$ elements.
Two sets $S_1$ and $S_2$ of the family are called a bad pair of sets if none of the following sets is empty:

* $S_1\cap S_2$;
* $S_1\setminus S_2$;
* $S_2\setminus S_1$.

The family is called laminar if no bad pair of sets exists.

# The goals

Goal 1: Write a function which recognizes laminar families.
Goal 2: Certify your negative answers: in case the given set family is not laminar, return a bad pair of sets.
Goal 3: Certify your positive answers: in case the given set family is laminar, return a collection of rooted trees. Every set of the family is a node of one of these rooted trees, with the root nodes being the maximal sets, and where each non-maximal set has the set immidiately containing it as its father.
Each element of the ground set is a leaf and has the set immidiately containing it as its father.
Play a DFS visit of this tree to transmit it through the primitives:

    procedure open_root_node(s);
    procedure open_child_node(s);
    procedure give_leaf_node(elem);
    procedure close_node().

Goal 4: Certify your positive answers: without affecting its laminarity, add to the family all the singleton sets (number them from m to m+n-1) and the universe set (number it m+n). In case the given set family is laminar, then every set excepte the universe has a unique minimal including set.
Implement the primitive:

    procedure minimal_including set(s);

This primitive will allow for a simple test of laminarity.

Goal 5: Certify your positive answers: suppose you can lay down the elements in a row so that, for every set in the family, its elements are consecutive. Then we can conclude that the family is indeed laminar.
We ask you not only to specify the elements one by one, as they occur in the row, but also to tell when the interval of the elements of a set opens and closes.
Use the following primitives.

    procedure lay_down_element(elem);
    procedure open_set(s);
    procedure close_set(s).

These primitives will allow for a simple check of laminarity when such an ordering exists.
