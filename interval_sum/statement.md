# Structuring data to prepare for queries
## Interval Sums

First, you receive a sequence of $n$ natural numbers $s[0], s[1], \ldots, s[n-1]$.
Second and last, you receive a sequence of queries:
each query specifies an interval $[a,b] \subseteq [0,n-1]$ with $a\leq b$
(actually, we also allow for $b=a-1$, which represents an empty query interval).
In as short time as possible,
you must answer such queries by returning the value $\sum_{i=a}^b s[i]$.

You should submit a file containing the implementations of two functions.

1. a first function to be called once, where you receive the sequence $s$:
      ```function get_sequence(int n, int[] s);```
   within function get_sequence you are allowed to set up an $O(n)$ memory
   data structure to speed up the later queries;

2. the query function:
```   function interval_sum(int a, int b) -> int;
      // interval_sum returns the sum of the elements within the [a,b] interval of s,
      //   that is, the value s[a] + s[a+1] + ...  + s[b]
      // special case: returns 0 if b == a-1
```      

In a full solution, function interval_sum should cost $O(1)$ time.
