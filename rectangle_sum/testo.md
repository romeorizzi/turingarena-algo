First, you receive an $m\times n$ matrix of natural numbers $mat[i][j]$, $i=0,1, \ldots, m-1$, $j=0,1, \ldots, n-1$.
You can assume that $m\leq MAX_M := 5\,000$ and $n\leq MAX_N := 5\,000$.

Second and last, you receive a sequence of queries:
each query specifies an interval of row indexes $[r_1,r_2] \subseteq [0,m-1]$ with $r_1\leq r_2$
and an interval of column indexes $[c_1,c_2] \subseteq [0,n-1]$ with $c_1\leq c_2$
(actually, we also allow for $r_2=r_1-1$ and $r_2=r_1-1$, these cases represent a query on an empty submatrix).In as short time as possible,
you must answer such queries by returning the value $\sum_{i=r_1}^{r_2} \sum_{j=c_1}^{c_2} mat[i][j]$.

You should submit a file containing the implementations of two functions.

1. a first function to be called once, where you receive the matrix $mat$:
   ```   function get_matrix(int m, int n, int[][] mat);```
   within function get_matrix you are allowed to set up an $O(n)$ memory
   data structure to speed up the later queries;

2. the query function:
   ```   function rectangle_sum(int r1, int r2, int c1, int c2) -> int;
         // returns the sum of the elements whose row and column indexes fall within the [r1,r2] and the [c1,c2] intervals
         // special case: returns 0 if r2 == r1-1 or c2 == c1-1```

In a full solution, function rectangle_sum should cost $O(1)$ time.